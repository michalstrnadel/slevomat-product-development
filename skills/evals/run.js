export const meta = {
  name: 'run-evals',
  description: 'Play eval scenarios against the skills as written on disk and grade them',
  whenToUse: 'Before a release, or after changing a skill that a scenario covers.',
  phases: [
    { title: 'Play', detail: 'a colleague and the skill talk to each other, turn by turn' },
    { title: 'Grade', detail: 'a third agent checks must / must_not against the transcript' },
  ],
}

// Why a role-play loop and not one prompt: the scenarios test whether the skill ASKS
// something. Hand a model the whole scenario at once and it can see the answers, so
// every "does it ask about X" assertion passes for free. The colleague therefore holds
// the follow-ups and the skill never sees them until it has earned them.

const REPO = (args && args.repo) || '/Users/michalstrnadel/Documents/Macbook M3/Warp/slevomat-skills/product-development'
const SKILLS = `${REPO}/skills`
// One file per skill, named after it, so a scenario is where someone would look for it.
// Deliberately NOT inside a skill's own folder — the skill agent is told to read the files
// beside its own text, and the assertions must never be among them.
const EVALS = `${SKILLS}/evals`
const IDS = (args && args.ids) || ['hub-ramovani-schovane-reseni']
// A scenario that asserts on the spec needs enough rounds to reach one. Four rounds
// once produced a run where three assertions failed by construction — the gate was
// still asking questions, correctly, and there was no artefact to grade. If you cap
// this low, read the transcript before believing the verdict.
const ROUNDS = (args && args.rounds) || 12

const TURN = {
  type: 'object', required: ['say'],
  properties: { say: { type: 'string' }, done: { type: 'boolean' } },
}

const VERDICT = {
  type: 'object',
  required: ['id', 'passed', 'must_results', 'must_not_results', 'qualitative_judgement'],
  properties: {
    id: { type: 'string' },
    passed: { type: 'boolean', description: 'false if ANY must_not happened or any must is missing' },
    must_results: { type: 'array', items: { type: 'object', required: ['item', 'met', 'evidence'],
      properties: { item: { type: 'string' }, met: { type: 'boolean' }, evidence: { type: 'string' } } } },
    must_not_results: { type: 'array', items: { type: 'object', required: ['item', 'happened', 'evidence'],
      properties: { item: { type: 'string' }, happened: { type: 'boolean' }, evidence: { type: 'string' } } } },
    qualitative_judgement: { type: 'string' },
    worst_finding: { type: 'string' },
  },
}

async function playOne(id, plan) {
  const files = (plan && plan.files) || []
  const sourceFile = (plan && plan.source_file) || ''

  // These skills run in claude.ai as standalone skills: no router, no plugin around
  // them, nothing injected before the first message. Handing the agent anything else
  // would test a situation that never happens.
  const instructions = `Read these, and treat them as your complete instructions:
${files.map(f => '- ' + f).join('\n')}

You are a standalone skill in claude.ai. There is no router and no other skill around
you, so everything you have is in the file or files above. If they name another skill as
the next step, say so — do not perform it yourself.`

  const transcript = []
  const render = () => transcript.length
    ? transcript.map(t => `${t.who === 'colleague' ? 'KOLEGA' : 'SKILL'}: ${t.say}`).join('\n\n')
    : '(zatím nic — začínáš ty)'

  for (let round = 0; round < ROUNDS; round++) {
    // The colleague holds the scenario. Turn one is the scenario's query, verbatim.
    const colleague = await agent(
      `You play the colleague in an eval scenario for a Slevomat product-development skill.

Read scenario "${id}" in ${sourceFile}. You may read the whole file.

Conversation so far:
${render()}

Your job:
- Round 1 (empty transcript): say the scenario's "query" VERBATIM. Nothing else, no framing.
- Later rounds: answer the skill's last question in character. Use the scenario's "follow_ups" in order as your material, adapted so your answer fits the question actually asked. When the follow-ups run out, keep answering in character: short, unhelpful, in a hurry, three words when three words will do.
- Never volunteer anything the skill did not ask for. Never be a helpful test user — a cooperative user gets a good result out of almost any prompt, which tests nothing.
- Set done:true only if the skill has produced its final artefact and has nothing left to ask.

Return {say, done}.`,
      { label: `kolega:${id}:${round + 1}`, phase: 'Play', schema: TURN })

    if (!colleague) break
    transcript.push({ who: 'colleague', say: colleague.say })

    // The skill sees only its own instructions and the conversation. Never the scenario.
    const skill = await agent(
      `You ARE a Slevomat skill in a live conversation with a colleague. Follow your instructions exactly.

${instructions}

You must NOT open anything under ${EVALS} — those files contain what you are being tested on, and reading them invalidates the run.

Conversation so far:
${render()}

Produce ONLY your next turn, exactly as the person would see it in the chat. No stage directions, no explanation of what you are doing, no meta-commentary.

Return {say}.`,
      { label: `skill:${id}:${round + 1}`, phase: 'Play', schema: TURN })

    if (!skill) break
    transcript.push({ who: 'skill', say: skill.say })

    if (colleague.done) break
  }

  log(`${id}: ${transcript.length} tahů`)
  return { id, transcript: render(), sourceFile }
}

phase('Play')

// The script has no filesystem access, so one cheap agent reads the scenarios and
// reports where each one's skill lives. Only paths cross back — never assertions.
const PLAN = {
  type: 'object', required: ['scenarios'],
  properties: { scenarios: { type: 'array', items: {
    type: 'object', required: ['id', 'files', 'source_file'],
    properties: {
      id: { type: 'string' },
      files: { type: 'array', items: { type: 'string' } },
      source_file: { type: 'string' },
    } } } },
}

const plan = await agent(
  `Scenario files live in ${EVALS}, one JSON file per skill, each with a "scenarios" array. Find these ids: ${IDS.join(', ')}

For each id report:
- files: absolute paths of the skill texts the skill agent should read. Resolve each entry of the scenario's "skill_files" array against ${REPO}. Include a skill's attachment when one sits beside it, because the skill reads it.
- source_file: the absolute path of the file the scenario was found in.

Report paths only. Do not include must, must_not or any other assertion text — the skill agent must not see what it is being graded on.`,
  { label: 'loader', phase: 'Play', schema: PLAN })

const where = {}
for (const s of (plan && plan.scenarios) || []) where[s.id] = s

const played = []
for (const id of IDS) played.push(await playOne(id, where[id]))

phase('Grade')
const verdicts = await parallel(played.filter(Boolean).map(p => () => agent(
  `Grade one eval run for a Slevomat skill. Be a hostile grader: the point is to find failure, not to be fair.

Read scenario "${p.id}" in ${p.sourceFile} — its must, must_not, why_this_scenario and qualitative.

The transcript to grade:
---
${p.transcript}
---

Rules:
- Judge only what is in the transcript. An assertion you cannot evidence with a quote is NOT met.
- A scenario fails if ANY must_not happened, or any must is missing. No partial credit.
- Quote the offending or supporting line as evidence for every item.
- Then answer the qualitative question, which is where the real failures live.
- worst_finding: the single thing that would most embarrass this skill in front of a real person, whether or not any assertion covers it. If nothing, say so plainly.

Return the verdict.`,
  { label: `grade:${p.id}`, phase: 'Grade', schema: VERDICT })))

const ok = verdicts.filter(Boolean)
for (const v of ok) log(`${v.id}: ${v.passed ? 'PROŠLO' : 'NEPROŠLO'}`)
return { verdicts: ok, transcripts: played }
