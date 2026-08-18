# Changelog

`CHANGELOG.md` je zdroj pravdy pro verzování — tag a GitHub Release z něj vznikají automaticky, když v pushi do `main` přibude nový nadpis `## vX.Y.Z`.

Záznamy do v0.24.0 popisují Claude Code plugin, který v tomhle repu žil do 17. 8. 2026 a je v tagu `plugin-archive-v0.24.0`. Zůstávají tady, protože ledger, který se přepisuje, aby vypadal konzistentně, je horší než ledger s historií.

## v1.1.0 — 2026-08-18

**Krok 4 se nově ptá, kolik směrů chceš.** Claude Design sám od sebe nakreslí první řešení, které mu přijde dobré, a od druhé zprávy dál už jen vylepšuje jeho — debata se posune z „je tohle správný směr?" na „co s ním ještě uděláme", aniž to někdo rozhodl. `design-prototypovani` má proto čtvrtou vstupní otázku vedle rozsahu, věrnosti a zařízení, a s doporučením místo prázdného dotazu: víc směrů v hrubé věrnosti, když má HMW otázka víc rozumných odpovědí a žádná z kroků 1 až 3 nevyšla jako vítěz; jeden a dotažený, když je koncept rozhodnutý a jde o provedení. Odpověď jde do briefu číslem a s tím, v čem se mají směry lišit — když tam ta věta není, počet si vybere designér. Eval na krok 4 to hlídá z obou stran: musí se zeptat, a nesmí odevzdat brief, který počet nechá nevyřčený.

**A odkazy na archivovaný `slevomat-product-development` jsou pryč.** Ten skill odešel s pluginem 17. 8. a jeho jméno den poté pořád stálo ve dvou descriptions a v jedné hranici v textu — kdo tam došel, poslali jsme ho na skill, který neexistuje. Krok 4 teď posílá na krok 1, krok 1 na `psani-zadani` u hotových zadání. Kontrola odkazů ve validátoru četla jenom `product-` a `design-` jména, a jenom v tělech skillů; teď čte i `slevomat-` jména a celý soubor včetně frontmatteru, se seznamem `EXTERNAL` pro skilly, které patří jinam do Hubu.

**Frontmatter je konečně platný YAML.** `description` obsahuje dvojtečky s mezerou („na fráze: design check"), a nebyla v uvozovkách — YAML to čte jako začátek vnořené mapy a odmítne celý blok, takže GitHub přestal soubory renderovat a přísnější čtenář přišel o description úplně. Rozbité to bylo v pěti souborech ze šesti. Validátor to teď hlásí jako chybu, ne aby se na to zas přišlo přes renderer.

## v1.0.1 — 2026-08-17

**Poznámky pryč, protože obě lhaly.** `notes/2026-08-13-design-principles-kde-co-je.md` navigovala ke složce, která se přesunula, a jediný věcný údaj, který nesla — původ principů z interního workshopu 28. 4. — je stejně přímo v `design-principles.md` ve frontmatteru. `notes/2026-08-13-dve-drahy-review.md` bylo review, které rozhodlo, jak mají skilly vypadat, jenže po dnešku má šestnáct odkazů na plugin, který v tomhle repu není, a moje dřívější dávkové přejmenování mu rozbilo věty. Jeho obsah přežil na lepším místě: **u každého pravidla ve skillu stojí jeho důvod hned pod ním** — což je domácí pravidlo, ne náhrada — a shrnutí změn je v README u skillů. Obojí je v gitu i v tagu.

**A `skills/product/README.md` se přepsal celý, protože to je dokument, který Romča otevře první, a měl v sobě sedm nepravd:** odkazoval na smazanou složku `_superseded-osobni-verze/`, tvrdil „čtveřice", i když v `product/` jsou tři skilly, popisoval, co si na oplátku vzaly `discover`, `define` a `brief` z pluginu, který je pryč, a nesl větu zmrzačenou tím dávkovým přejmenováním („tam vede rozhovor slevomat-product-development"). Nová verze je psaná Romče, ne vývojáři: co se změnilo, **proč** se to změnilo, a čtyři kroky, jak to dostat ven — včetně toho, že u kroku 4 jsou dva bloky, které nepsala, a mají se projít pozorně.

## v1.0.0 — 2026-08-17

**Jen pět skillů, které jdou do Skill Hubu. Plugin je pryč.**

Verze 1.0.0, protože to není další krok na téže cestě — je to jiné repo. Do dneška tu vedle sebe žily dvě sady skillů a při každém předání se pletly. Vlastník to řekl přímo: plete se to na sdílení. Takže Claude Code plugin s třinácti skilly, dvaceti scénáři a vendorovanou dokumentací Mini*S odešel z pracovní kopie — **ne proto, že by byl špatný**, ale protože repozitář má být o jedné věci.

Je v tagu `plugin-archive-v0.24.0`, celý, včetně evalů a runneru. Vrátit ho jde jedním příkazem, který je v README i ve zprávě u tagu:

```
git checkout plugin-archive-v0.24.0 -- plugin .claude-plugin
```

**Co se muselo přepsat, protože se to opíralo o plugin.** Runner přežil, ale musel se zbavit pluginové dráhy — hubový skill běží v claude.ai samostatně, bez routeru a bez sousedů, a jiné podání by testovalo situaci, která nenastane. Eval na principy osiřel mazáním a je zpátky z tagu, teď navázaný na hubovou verzi jako zdroj pravdy. CI už nekontroluje hook, místo toho ověřuje, že runner parsuje. A `tag-on-merge` porovnával verzi v CHANGELOGu s manifestem, který zmizel: bez pluginu je changelog jediné místo, kde verze žije, takže se nemá proti čemu rozejít.

**Validátor je nový, ne osekaný.** Ten starý validoval marketplace a manifesty pluginu, což je polovina, která přestala existovat. Osm kontrol na tom, co u hubových skillů reálně praská: frontmatter, kebab-case bez diakritiky, jméno musí sedět na soubor, prefix dráhy, hranice „kdy NEpoužívat" v description, odkazy mezi skilly, meze Hubu (jen textové formáty, nejvýš tři úrovně cesty), firemní slovník a emoji, doslovná shoda příček důkazů, a struktura evalů včetně toho, že soubor scénáře jmenuje skill, pro který je. Regex na odkazy dostal lookarounds až po tom, co hlásil fantomy: `slevomat-design-principles` v něm vyráběl neexistující `design-principles` a cesta `docs/.../product-variants.md` vyráběla neexistující skill.

**Dvě hranice, které validátor vyžádal a měl pravdu.** Kroky 2 a 3 neměly v description ani slovo o tom, kdy je nepoužívat — v předchozím kole to bylo odepsané jako churn, protože pozornost byla na pluginu. Teď je hubová dráha to hlavní a v plochém seznamu claude.ai je kolize triggerů druhá nejčastější příčina, proč skill selže. Mapování tedy nepoužívat na hledání řešení, konkurenci na výběr řešení a bez mezer z mapování.

**Jedno varování zůstává schválně.** `slevomat-design-principles` nese prefix, který pravidla Hubu vylučují. Je to už publikované jméno, Hub neumí mazat, takže přejmenování po sobě nechá draft, který odklidí jen admin — validátor to hlásí s tímhle vysvětlením místo aby to tiše přešel.

README je napsané pro Romču, ne pro vývojáře: k čemu ten set je, pět skillů v tabulce, čtyři věci, na kterých to stojí, a čím se pozná, že to funguje — dvě zrámovaná témata od někoho jiného než od nás dvou do týdne po zveřejnění.

## v0.24.0 — 2026-08-17

**The plugin moves to `plugin/`, and the repository root becomes the Hub lane's.** The owner's call, and it follows a decision made just before it: the Hub lane is what gets pushed to people next, the plugin waits until it has been used on real work. So the layout now says which is which — `skills/` and `skills/evals/` are the four Hub texts and their scenarios, `plugin/` holds the Claude Code plugin with its own `evals/`, and `notes/` is shared history.

One file could not move: `.claude-plugin/marketplace.json` stays in the root, because that is the only place Claude Code looks when adding a marketplace. Its `source` now points at `./plugin/slevomat-product-development`, and the CI hook check, the validator's two eval homes and the runner's paths moved with it.

## v0.23.0 — 2026-08-17

**One eval file per skill, laid out like the skills.** `evals/evals.json` was a single file of twenty-four scenarios, which meant the eval for a skill was nowhere near the skill. Now it is `evals/plugin/<skill>.json` and `evals/hub/<skill>.json`, so a scenario gets edited in the same commit as the skill it grades, and the validator enforces the pairing — a file under `plugin/` may only hold scenarios that name the skill it is named after, so renaming a skill without moving its eval fails the build. Verified by breaking it on purpose before trusting it.

**They are next to the skills, not inside them, and that is the whole design.** The owner's instinct was to put them in the skill folders. The reason not to is that the skill agent is instructed to read the companion files beside its `SKILL.md` — `CONTEXT.md`, `CONTENT.md`, `reference/` — so assertions living there would be the answer key, sitting open. The runner already forbids opening anything under `evals/`; co-locating would have quietly undone that.

## v0.22.0 — 2026-08-17

**The Hub lane had no evals at all.** Twenty scenarios covered the thirteen plugin skills and not one covered the five that live in the Skill Hub — Romana's three framing steps, `design-prototypovani`, and the principles review. The owner asked twice before I checked properly, which is its own lesson.

Four new scenarios, group `hub`: framing handed a solution and a missing number („chybí nám filtr", „číslo nemám, ale obchod to říká"), mapping asked outright for a proposal with no code and no admin access, a competitor analysis with no rubric, no browser and an invitation to guess from memory, and a brief that prescribes a modal with three tiles while planning no validation beyond a product meeting. Twenty-four scenarios, and every skill in both lanes now has one.

**Which needed the harness to understand lanes.** A Hub skill runs standalone in claude.ai — no router injected, no companion skills — so binding the router to it would test a situation that never happens. Scenarios can now declare `lane: hub` and their own `skill_files`, and a loader agent reads that once and reports only paths; no assertion text ever reaches the skill agent.

**And a correction to `cce2414`.** That commit says it refreshed the design system, and it did — but it also silently carried a folder rename the owner had made in Finder, `hub/` to `skills/`, because I staged with `git add -A` and did not read what I was committing. The rename is right and it stays: a folder of skills called `skills` needs no explaining. The paths in the README and in the `principles` skill's provenance note now point at it.

## v0.21.0 — 2026-08-17

**The first real eval run failed the gate, and the findings are this release.** `evals/run.js` played the OG-image scenario against `brief` as written on disk. Two things it did right: the trigger was caught („Tohle jsou dvě různé věci — jednorázová dávka teď a nástroj na potom"), and the tykání and one-concrete-instance discipline held throughout. Then it threw the insight away and spent the rest of the conversation asking the person to count things. Five questions, one observation returned, no spec. The grader's words: *„an intake form with a good ear — the person walks away having been interviewed rather than helped."*

Four fixes, each traceable to a line in that transcript:

**The skill now knows what it is for.** Two sentences at the top, because a skill with no stated purpose optimises for the thing it can measure, which is asking questions. The person should leave knowing something about their own problem they did not know, and what gets built should be worth building — sometimes that means nothing gets built. From which follows the rule the run needed: **every turn owes them something back** — a reading, a consequence, a number turned into an implication, a pattern named — and a turn containing only a question is a turn that took without giving. At most one of those in a row.

**The signpost was a tic, not honesty.** Four of five turns opened with what the skill did not know: *„Ještě nevím… / Zatím nevím… / pořád nevím…"*. The rule said three moments per conversation; it needed a hard edge, so now it also says never twice in a row, and names the better opening — what you now **do** know. *„Takže pět obrázků ručně, každý zvlášť — to je odpoledne, ne nástroj."*

**Naming a pattern is half a move.** The split between the batch and the tool was named correctly and then abandoned: *„zatím nevím, která z nich bolí"*, followed by two questions about volume, and nobody ever asked which one the build serves. The move now has to finish in the same turn — say what follows, and make the next question the one it forces.

**Say what the number means.** The colleague answered „asi pět, možná šest" and the gate asked for another number. Five images by hand is an afternoon of somebody's time, not a product; three hundred is a build. Do the arithmetic out loud, and bound your own question instead of sending them off to count: *„Jestli je to víc než pár desítek, ruční klikání padá samo. Jsme nad, nebo pod?"* Two new example exchanges carry it, both from this run.

**And the trigger question gets asked even when the urgency arrives unprompted.** Volunteered urgency hands over the trigger but not what changed behind it, and it is the one of the four questions that gets skipped most, because the conversation feels like it already has its answer.

**Every skill in the plugin now has an eval.** Five new scenarios: `ideate-uz-mam-reseni` (asked to rank, twice), `variants-tri-odstiny` (three positions of one chart sold as three variants), `plan-postav-to-hned` („je to jednoduché"), `gaps-chybi-mi-modal` (a component promoted into the design system as a side effect), `validate-ukazu-to-kolegum` (a product meeting mistaken for validation). Twenty scenarios; the claim that the build skills did not need coverage is retired, because what is worth testing in them was never visual.

Two fixes to the harness itself, both learned the hard way. The default round count is twelve, not four: the first run was capped so low that three assertions failed by construction — the gate was still asking questions, correctly, and there was no spec to grade. And the skill agent now reads the router first and **routes itself** from there, instead of being handed `brief`; a scenario about a missing component or a finished prototype does not start at the gate, and choosing correctly is part of what is being tested.

## v0.20.0 — 2026-08-17

**The vendored design system was three days and seven commits stale, which is the most expensive kind of stale in here** — `minis` builds every prototype from it. Refreshed to `f11bc50` (2026-08-14) from `4786c65`: thirteen files changed and one new component appeared, `menu`, a labelled dropdown built for navigation overflow. A skill that does not know a component exists sends someone off to build it from scratch, which is the exact failure `gaps` is supposed to prevent.

One upstream rule was new and belongs in the digest, because it fails silently and the digest exists for precisely that: **a Slevomat web page opens with the topbar and then `<minis-navigation variant="main-nav">`, exactly once, at the very top, and no web page ships without it.** Inside a page — tabs, filters — the variant is `tabs`, which may repeat and never sits at the top. A `vibe-apps` prototype needs no main nav at all, which is most of what this plugin builds.

Verified rather than assumed while refreshing: the topbar still has no mobile variant, so that line in „Verify, don't assume" stands, and the list of components the system still lacks — `input`, `modal`, `table`, `avatar`, `Separator` — is unchanged.

## v0.19.0 — 2026-08-17

**Everything is Slevomat product development, including the plugin.** The owner's name, and the right altitude: this folder holds both lanes, so „design skills" mislabelled half of it — the framing texts in `hub/product/` are not design skills. Marketplace, folder and plugin are all `product-development` now (plugin `slevomat-product-development`, router `using-product-development`, commands `/slevomat-product-development:`). Second breaking rename in one day, deliberately: both were pending, and paying the reinstall twice would have been worse than getting the name right once.

One thing did not move: **the repository is still `slevomat/design-skills`.** Renaming it needs org admin, which the owner's token does not have (`admin: false`), so every install command and homepage URL still points there — a rename in those files would have pointed the marketplace at a repository that does not exist. It is the one loose end of this rename, and it needs an admin.

**Prototyping moved to the design lane.** `product-prototypovani` became `design-prototypovani` and sits in `hub/design/` next to the principles. Prototyping is design work, the owner had already taken it over from Romana, and the split now says something true: **product frames the problem, design prototypes it and judges the result.** Its description calls itself the handover point rather than „the fourth step", because that is what it is.

**The seven principles are a skill in the plugin.** `skills/principles/` carries them verbatim from the Hub, with provenance stated and the Hub named as the source of truth, exactly as `skills/minis/reference/` carries the design system. This closes the hole v0.17.0 left open: the design check was a step in `review-package` that could not run in Claude Code, because the only copy was in the Hub. Now it runs where the prototype is, and `review-package` and `minis` point at it. Thirteen skills.

**And the evals can finally be run.** They were twelve scenarios of prose in a JSON file that nothing executed — the owner's word for it was „divný", which was fair. `evals/run.js` is now a role-play harness: a colleague agent holds the scenario and answers in character, the skill agent reads only its own instructions on disk and is forbidden from opening `evals.json`, and a hostile grader must quote a line as evidence for every assertion it marks met. The separation is the whole design — hand one model the scenario and the conversation together and it sees the answers before it asks, so every „does it ask about X" assertion passes for free. It also tests the skills as written on disk rather than whatever stale version is installed in the session.

Three scenarios cover what today added and nothing tested: `principles-countdown-banner` for the new skill, on the concept that passes every mechanical check while being a dark pattern; `discover-existuje-ale-nepouziva-se` for the two patterns adopted from Romana; `define-hmw-bez-prikladu` for the mandatory example in parentheses. Fifteen scenarios.

**`CONTRIBUTING.md` is gone, its load-bearing half folded into the README.** For a private repository with one owner a contribution guide is ceremony — but the release process and the writing register were not, so they live in `## Development`: how a `## vX.Y.Z` heading becomes a tag, and the rule that matters most, that Mini*S documentation is vendored verbatim and never paraphrased.

**`hub/product/_superseded-osobni-verze/` is gone.** It held a variant with the old `slevomat-*` names for Romana's personal copies, which the transition rule made redundant: paste the canonical text, swap the prefix mechanically. Diffed before deleting — the difference was only what we changed on purpose (names, the owner and version comments, „produkťák" to „pisatel", the evidence-ladder paragraph). `git show 75a13ba` has it if that turns out to be wrong.

## v0.18.0 — 2026-08-17

**Breaking: the plugin is `slevomat-design`.** The identities went too, so the old name is now gone from paths and commands as well as prose: the plugin directory, `plugin.json` name, the marketplace source, the router skill (`using-design`), and the command prefix, which is now `/slevomat-design:brief`. Anyone who had it installed re-adds it — that cost is exactly why v0.16.1 left the identities alone, and it is paid once here rather than twice later.

**And the work lives in one place.** Everything that was scattered across the parent directory moved into this repository, which is the single folder the owner asked for:

- `hub/product/` — the four canonical texts of the product-process lane (`product-definice-problemu-a-hmw`, `product-mapovani-stavu`, `product-konkurence-inspirace`, `product-prototypovani`), staged here before they go to the Skill Hub, with their own README and the superseded personal versions in `_superseded-osobni-verze/`
- `hub/design/slevomat-design-principles/` — the review skill and its seven principles, mirroring what is in the Hub
- `notes/` — the review that argued the two lanes into one family

Romana's boundary sentences pointed at a skill name that no longer exists, so they now name the lane rather than the product: *„rozhovor o problému tam vede expresní dráha designu"*.

Two kinds of mention survive on purpose. `CHANGELOG.md` keeps the history, because a ledger that edits itself to pretend the name never existed is worse than the name. And the citations of [obra/superpowers](https://github.com/obra/superpowers) stay everywhere they appear: issue 444 is why the hook runs `async: false`, 571 is why it uses `printf` over a heredoc, and `plan` is adapted from that project's brainstorming skill. Removing an attribution to make a rename look complete would be a lie about where the work came from.

## v0.17.0 — 2026-08-17

The design team's own lane finally runs the design team's own principles. The owner spotted the asymmetry while reading the setup: all four of Romana's product-process skills name the principles check in „Co následuje", and not one of the twelve skills here did. It existed only as a hand-over row in the router's neighbours table — a table nothing consults at the moment a prototype is finished.

**`review-package` gets it as a step, before the handover.** The six checks it already ran are mechanical — placeholder text, Czech UI, price format, hardcoded values, `disabled`, dark mode — and a prototype can pass all six and still be a dark pattern; the countdown banner in the principles skill's own example passes every one of them. So `design/slevomat-design-principles` now runs as Step 4 and its verdict goes into `REVIEW.md` in its own words: Pusť dál, Doostři, Vrať, Chybí vstup. A `Vrať` found before the handover costs the author an hour; the same `Vrať` found through a reviewer costs two people a week.

**Which required guarding the rule it looks like it breaks.** This skill's HARD RULES say it does not judge the design, and a new step that produces a verdict is exactly the shape of the contradiction this plugin has shipped before. So the rule now says it outright: running the principles skill and passing its verdict on unchanged is the opposite of forming your own. An unrunnable check is written down as not run, with the reason — a blank row reads as passed.

**`minis` offers it once** at the end of „Verify, don't assume", because an internal tool that never goes to review is precisely the thing nobody ever checks.

Twelfth eval scenario, `review-without-the-design-check`, covers it. The principles check had zero eval coverage until now.

## v0.16.1 — 2026-08-17

The name „Superpower" is retired. The owner's verdict was blunt — the word earns nothing and it stays nowhere — so it is gone from every place a person or a model reads it: the router's title and description, the hook's comments, and the context tag injected into every session, which is now `<SLEVOMAT_DESIGN_PROCESS>` and opens with „This session runs the Slevomat design process." The one surviving mention is a citation of `obra/superpowers#444` in the README, which is why the hook runs `async: false` and cannot be paraphrased away.

Identities — the plugin name, the marketplace entry, the skill directories, the `/slevomat-design-superpower:` command prefix — are deliberately untouched for now. Renaming those forces everyone to reinstall, and the Skill Hub has no delete tool, so a rename there orphans drafts that only an admin can remove. The name gets decided once, after the process has been tested, not twice.

## v0.16.0 — 2026-08-14

The express lane joins the product family. Romana's four product-process skills move to the Skill Hub as plugin `product` (product-definice-problemu-a-hmw, product-mapovani-stavu, product-konkurence-inspirace, product-zadani-pro-design — pure prefix swaps), and this plugin becomes the express lane and the build of the same family: one vocabulary, reciprocal boundaries, one destination in Claude Design. Built by a 14-agent workflow — two architects, a judge, seven authors, four adversarial verifiers.

**The gate adopts three of her patterns.** `discover` writes findings as three one-line fields with a mandatory third — `Nález / Kde to vidím / Co nevíme` — because the gap admitted at write-time is the next question; and it collects live-but-unused mechanisms into an „existuje, ale nepoužívá se" list in `00-zadani.md` under `Odkud to víme`, where `brief`'s cheapest-non-build move now starts looking. `define` requires a concrete example in parentheses inside every challenge — *(například k náhrdelníku i náhrdelník s náušnicemi)* — attached wherever the ambiguity lives, because without it everyone at the meeting imagines something different.

**One evidence ladder across both lanes.** The canonical rungs — behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka — now appear verbatim in `brief`'s challenge move and spec template and in `discover`'s table, and the same line sits in all four product skills, so claims are comparable across lanes.

**The boundary stays in one place.** `brief`'s description now hands platform product topics to `product-zadani-pro-design` in the Hub. The verifiers killed a drafted second copy of the boundary in the router — this plugin has shipped a drifting-duplicate bug before, and the blueprint's own rule („druhá kopie hranice je druhá věc, která driftuje") held. The router ships unchanged.

Known debt, flagged not fixed: `ux-recon` and `ux-research` in the router's neighbours table point at Hub skills that do not exist yet.

## v0.15.1 — 2026-08-14

One change: a trigger boundary in `brief`'s description. Romana's product-process skills (rámování → mapování stavu → konkurence → zadání pro design, personal skills in claude.ai) trigger on the same phrases — „chci prototyp", „jdeme prototypovat" — and where both live, routing was a coin flip. The gate now says: a platform product topic that runs through the product process gets its brief from `slevomat-zadani-pro-design`; this gate is for building from scratch, and would make the person answer questions their process already answered. The reciprocal boundary for her step 4 is drafted in the review doc (`skill-reviews/2026-08-13-produktovy-proces-x-design-superpower.md`).

## v0.15.0 — 2026-08-13

Built from the third field test — the OG image generator. The conversation was finally a designer's, and the spec still failed the person in three ways the owner spotted and one he did not.

**The spec excluded the thing that triggered the request.** The person said *„teď budeme generovat všechny nové OG image kvůli nové kreativě"* — a one-off batch — and the spec put batch generation under `Co v tom NEBUDE`. Nobody noticed, including the designer. New challenge move: **ask what made it urgent now** (*„Co se stalo, že to řešíš zrovna teď?"*). The trigger and the recurring need are often two different things; when they differ, both go into the spec and the person decides which the build serves.

**„Nic se nezvažovalo" without the question is a hole, not a finding.** The conversation never asked about other paths and then wrote `Zavrhnuté cesty: nic se nezvažovalo`. All four discovery questions get asked now, and before that field gets written the designer asks for **the cheapest non-build** — a Figma template with swappable text, a script the developer already runs. Slevomat's own McKinsey incubation material asks for the manual version first and treats internal alternatives as competitors (Asset concept assessment).

**The spec now carries the build shape.** The person takes the spec to Claude Design and the technology decision happens there whether anyone made it or not. Three quick questions once `Co stavíme` holds — stores anything between uses? who opens it and from where? anything outside the browser? — and the designer **derives the shape and lets them correct it**, never asks a colleague to pick a technology. New `## Technologie` spec section: static FE / FE+backend+DB (vibe-kit-backend) / goes out = review mandatory; deployment named as vibe-kit (Google Cloud). From the Tech Advisor guide: don't say no because it is hard — surface the implications.

**Problem-solving teaching, not just interviewing teaching.** New move: **name the pattern when you see it**, one plain sentence — *„tohle jsou dvě různé věci: jednorázová dávka teď a nástroj na potom"*. And the closing grew a third line: the shakiest assumption in the spec, the last thing the designer teaches. The owner asked for a summary at the end; a designer's read of the spec is one, a recap is not.

## v0.14.0 — 2026-08-12

The designer tyká, guides, and teaches. Built from the owner's second field test — which, it turned out, ran a v0.8.0-era snapshot in the Claude app, so half the complaints were already fixed on GitHub and never reached the surface being tested. The other half were real and are this release.

**Tykání.** The designer is a colleague at the same table, not a service desk — *„kdy jsi to naposledy potřeboval"*, never *„kdy jste to potřeboval"*. Converted across all twelve skills by a three-agent sweep with two protected islands where vykání is correct because a customer reads or hears it: the session-script template and leading-questions table in `validate`, and every UI-copy rule in `minis` (Mini*S addresses customers with vy).

**Guiding without narrating.** The owner's complaint — *„neprovází tím procesem"* — collided with the standing ban on process narration, and the resolution is the signpost: a gap plus a stake, one clause, attached to a question. *„Ještě mi chybí, kdo s tím dneska bojuje — pak vymyslíme, co stavět."* Three per conversation (first question, subject change, the offer of the spec), never a phase name, never a counter, never a turn without a question. The router now names the echo and the signpost as the two things its banned-filler list does not cover.

**Teaching in flight.** *„Neučí mě to."* Every challenge move is craft the person can steal, but only if the reason lands in the same breath as the question: *„Ptám se na jeden konkrétní den, ne jak to chodí obecně, protože obecně si to každý zpětně vyhladí."* One reason per turn, always about the designer's own move, never twice, no method names — the second time a reason shows up it is a lecture. And the person does the thinking: their alternatives first, then which one they would kill.

**How it sounds.** Three example exchanges sit in the skill now, per the skill-authoring guidance that examples carry style better than adjectives. Voice drafted by two agents from different angles — The Mom Test interviewer and the design-lead-as-mentor — and merged by a judge.

## v0.13.0 — 2026-08-12

The evals were tested against the wrong work, and the gate assumed a blank slate.

**The scenarios are the company's actual work now.** v0.12.0 shipped seven scenarios with a quiz app for an offsite as the lead one. That request is real — it is where the first failed run came from — but it is a throwaway, and building the eval suite around it meant calibrating the gate on its least representative case. Five product scenarios replace it at the front, each naming the knowledge-base document its numbers come from so they can be checked: klouzavka bulk extension (hundreds of deals flagged KRITICKE every week), gamification of loyalty (850k users a year, episodic, the middle segment is the target), the referral PRD with its five open questions, goods shipping costs (997 respondents, 38 %), and repeating the travel credit campaign (62 000 claimed, 59 bought). The offsite quiz stays as a regression case, labelled as what it is.

**The gate now reads what already exists before asking.** Nothing in it said to. Someone arriving with a PRD, a survey or a weekly analysis got the full discovery conversation anyway, including *odkud to víme* about a claim their own document sources. Asking a person to re-explain what they already wrote down produces a worse answer than the document and reads as an interrogation. This was found by reading the skill, not by observing a run.

## v0.12.0 — 2026-08-12

Tested properly for the first time, and it turned out v0.11.0 had rewritten the gate and left the other eleven skills pointing at a file nobody writes.

**The twelve skills read the same file again.** `brief` started writing `00-zadani.md` in v0.11.0; `discover`, `define`, `sizing`, `ideate`, `variants`, `validate`, `plan`, `minis` and `review-package` all still read `00-brief.md` and wrote sections that the new spec does not contain. Anyone who ran the gate and then a phase reached for a file that was never created. The spec is now one file, every phase adds its own section to it, and `validate.py` fails the build if a retired artefact name reappears — this is the class of bug that no amount of re-reading catches, and it had shipped.

**The router told the model to announce itself.** `using-design-superpower` said *say which skill you are using and why*; `brief` said *do not announce*. The router is injected into every session by the SessionStart hook, so the router won — which is why the first real conversation opened with „Beru to přes brief" even after that was supposedly fixed. Two files disagreed for three versions. The rule now lives in one place and says the first thing the person sees is a question.

**A jednorázovka had no question left.** Removing the question budget in v0.10.0 also removed the only substantive thing the gate asked about a throwaway. It now asks exactly one — *co se z toho chceš dozvědět*, or *co se má stát, aby to fungovalo* for something that happens in a room — and goes. How hard it pushes scales with what it costs to be wrong, never with a counter.

**When there is no „dneska", it looks for the nearest real past.** A quiz for an offsite that has not happened has no current behaviour to ask about, and „co se děje dneska" pointed at it reads as bureaucracy. The move is to ask about the closest thing that did happen — the last offsite, the last launch, the last attempt in a spreadsheet. In testing that is where the actual problem surfaced: *„posledně byl pub quiz v týmech a lidi zůstali sedět s tím svým."*

**Not everything worth building fixes a pain.** For a party game or a one-off experiment the question is not *co bolí* but *co se má v tom sále stát*, and the success criterion is something you could watch happen instead of a metric. Forcing pain-framing onto an occasion is the single fastest way to make this feel like process for its own sake.

**When asking stops paying, it says the wrong version out loud.** Three-word answers in a row mean questions have stopped working. Offering a reading you are not sure about — *„takže to, co tě štve, je že se ti to sype až u schvalování — nebo mám blbě?"* — gets corrected faster and more precisely than any further question gets answered.

**Two-option questions are banned at the asking end.** Refusing to accept „ano přesně" was only half the fix; the other half is not to ask a question that invites it.

**It shows it was listening without saying „Rozumím".** Use the person's own noun in the next question. A slightly wrong echo gets corrected, and the correction is the useful part — which is the opposite of what an affirmation does.

**Added `evals/`.** Seven scenarios, each from a run that failed, with assertions that are checkable by reading a transcript plus one qualitative note where judgement is the only honest measure. Anthropic's own guidance is to build evaluations before documentation; this plugin had none for four months of versions, which is why every fix so far came from a complaint instead of a test. The validator now fails if a scenario names a skill that no longer exists.

**Rules carry their reasons.** Per `anthropics/skills`, rigid structures and shouted absolutes are a yellow flag: *"if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important."* The vendored copy of Anthropic's best practices inside obra/superpowers says the opposite — use capitals for rigid requirements — and is a stale snapshot. The live guidance wins; the `<HARD RULES>` blocks stay where the failure is real and repeated, but each line now says what goes wrong without it.

**Vocabulary.** `discover` still said „Account manažeři" in an example five versions after that word was rejected. The validator now fails on it, on „spike" and on „člověk z péče", with the glossary in `CONTEXT.md` exempt because listing an alias is its job.

## v0.11.0 — 2026-08-12

The gate is a designer now, not a rulebook, and it ends with one document.

**One spec instead of two artefacts.** `00-brief.md` and `01-plan.md` are replaced on the common path by `00-zadani.md` — a single block that is copyable in one go, because the person is pasting it into Claude Design where there is no repo and no second file. It carries the problem, who has it, where we know it from, what we are building, **what is faked**, what is explicitly out of scope, how we will know it worked, who will see it, and the paths that were rejected. Two documents were the plugin's convenience, not the user's.

**The conversation ends by offering the document, not by producing it.** *Myslim, ze to mam. Napisu z toho zadani — projdi ho a rekni, co doplnit nebo zmenit.* Then it waits. The person confirms or adds, and only then does it write. This is the `brainstorming` flow from obra/superpowers, which had been implemented in `plan` and was missing from the gate, the place it actually matters.

**Challenging is the job, not a courtesy.** "Push back once, then record" produced a stenographer: it recorded a shrug and called it a problem statement. It now keeps challenging while the answers do not hold. The stop condition is understanding, not a count.

**The skill reads like a designer instead of a defect log.** The ten-row "Never" table quoting the plugin's own past failures was defensive engineering documentation. The prohibitions survive as two paragraphs; the space went to the eight challenge moves, each sourced — pull answers back to the real world (Jamie Mill), find what the solution hangs on (Torres), ask why until you reach a cause, take the workaround seriously, be willing to challenge the framing, never reveal the hypothesis, quote them rather than interpret, keep contradictions.

**The four questions are the frame.** Jaky problem to resi, kdo ho ma, zvazil jine cesty, co se zmeni kdyz to vyjde — from the ASWA deck. The six-field problem statement is now the shape of an answer rather than the shape of the interview.

## v0.10.0 — 2026-08-12

The designer's reasoning, and the question limit removed.

**Added: the reflexes behind the questions.** Refusing a bad answer is not designing. Until now the gate knew what to collect and what not to accept, but nothing told it what to ask next. Eight moves now do, each with its source named so they read as craft rather than house opinion:

- **Pull every answer back to the real world** the moment it drifts into features, screens or technology. *"Stay in the real world. Push back whenever answers drift toward product or interface decisions"* — Jamie Mill, `layers-domain`. This is exactly what failed in the first transcript: "QR kód a odměna" was treated as an answer instead of a mechanism.
- **A request is a solution; find what it is attached to.** Solutions are never judged on their own, only against the opportunity they serve — Teresa Torres, opportunity solution tree.
- **Ask why until you reach a cause, not a mechanism.** "Zasekne se u nahrávání fotek" is where it happens, not why.
- **Find the workaround and take it seriously.** *"If your users' alternative solution is good enough, it might be time to revisit your goals"* — Problem Definition playbook, Synthesis.
- **Be willing to change the problem, not just the solution.** *"It's OK if your research is pointing you toward findings that don't seem to fit your original problem statement"* — same playbook.
- **Never give away your hypothesis** — playbook, interviewing.
- **Write what they said, not your interpretation** — playbook, note-taking. Quote them in the brief.
- **Record contradictions, do not smooth them** — Jamie Mill.

Most of this was sitting unused in sources the plugin already cited. The playbook had been mined for six fields out of five modules; Jamie Mill's rule had been taken by half.

**Removed: the question budget.** "jednorázovka 2, interní 5, ven 8" was a misreading of the owner's instruction — the ask was for short *output*, and a cap on *questions* is a different thing that actively caused the failure it was meant to prevent: the gate rushed to produce a brief instead of understanding anything.

The limit is now on the plugin's own words and never on how many questions it asks. It stops when the brief is true — when it can say, in the person's own words, who has the problem, what they do today and why it is hard, and when the next question would not change anything anyone does. Every question must be able to change what gets written down; one that cannot is the one that makes people switch this off.

## v0.9.0 — 2026-08-12

First real conversation, and it failed in six specific ways. Every change below comes from that transcript.

**The type question is no longer the first question.** Asked first it is an exit handed over before anything else was asked, and it got taken: "no spíš to zahodíme no" closed the whole conversation. Step 1 is now one question about the person who has the problem and what they do today, and **everyone answers it, including a jednorázovka.** The type comes second and only decides how much more to ask.

**A hedged answer is not a type.** „Spíš", „asi", „no…" means push back once and let them decide.

**Non-answers are now named and refused.** „Ano", „přesně", „asi jo", or agreement with a question that offered two options — none of them answer anything, and one of them ("ano přesně") became a written brief. „To nevím" and „je to zatím domněnka" stay valid answers; „asi jo" does not.

**Push back once, then record.** The old instruction to record and move on produced a stenographer: it wrote down a shrug and called it a problem statement. Now every weak answer gets one line naming what is missing plus one sharper question, then it gets recorded. Once, not twice — zero times is stenography, twice is an interrogation and people switch it off.

**Six things are now explicitly banned**, each because it happened: announcing which skill is being used, guessing the answer before asking ("nejspíš jednorázovka, ale rozhodne typ"), asking two things in one turn, offering a menu of next steps, defending the process by citing what the person said earlier, and recording without pushing back.

The worst line in the transcript was the skill defending itself — *„Ptal jsem se na začátku, řekl jste, že jde o zábavu"*. The rule now: if they say you never asked, you never asked. Do not cite the transcript back at them. Ask now.

**`plan` stops planning throwaways.** For a jednorázovka the plan is optional, and if asked for it is the screen list plus what is out of scope. No ledger, no estimate, no open questions. `Odpovídá na: uvidíme, jak to vypadá` is banned — if that is the honest answer, the plan has nothing to say.

**Internal jargon out of the artefacts.** `Rozsah: flow s fejkem` was the plugin's own taxonomy printed at a person who then had to ask what it meant. Now `jedna obrazovka, vymyšlená data` / `celý průchod, vymyšlená data` / `celý průchod, reálná data`, and the ledger column is `Vymyšlené` / `Nikam nevede`.

## v0.8.0 — 2026-08-12

Slevomat vocabulary for the prototype types, and every skill stops introducing itself.

**Changed**

- `spike` is gone. The word comes from engineering and nobody at Slevomat uses it; the type is now **jednorázovka**, which follows the pattern the internal glossary already establishes (klouzavka, dárkovka, DMka, VOPky). The three types are `jednorázovka | interní | ven` in every skill, in the brief template and in the question budget.
- Every skill lost its rhetorical opening. "Building is no longer the problem", "One concept is not a choice, it is a decision wearing a proposal's clothes", "Cheap bad ideas have to die before expensive ones do" — a model does not act on any of it, and a skill whose own rule is "no waffle" opening with three paragraphs about itself was indefensible.
- In their place, one factual line per skill saying what it produces, with numbers where there are numbers: what it owns, how many steps, how many questions. A reader decides in two seconds whether to run it, and the model gets nothing it cannot act on.

Rationale kept only where a rule gets argued away without it — "domněnka is a valid answer, because whoever is not offered it invents data instead" stays; "a two-hour argument here saves weeks of rework" does not.

## v0.7.1 — 2026-08-12

**Fixed**

- Removed `hooks` from `plugin.json`. Claude Code loads `hooks/hooks.json` automatically by convention, so declaring it in the manifest registered it twice and the whole hook failed to load with `Duplicate hooks file detected`. The manifest field is only for *additional* hook files. Found by installing the plugin, which is the only way this class of bug shows up.
- The validator now fails when `plugin.json` declares the conventional `hooks/hooks.json` path, so this cannot come back.

## v0.7.0 — 2026-08-12

Monorepo layout, and one name instead of four.

**Changed**

- The repository is now a **marketplace monorepo**, the way `phuryn/pm-skills` is laid out. `.claude-plugin/marketplace.json`, the README, the changelog, the validator and CI live at the root; each plugin gets its own directory with its own `.claude-plugin/plugin.json`. Adding a second plugin later means adding a directory and one marketplace entry, not restructuring.
- The plugin is `slevomat-design-superpower`, in a directory of the same name. Skills are referenced as `slevomat-design-superpower:brief`, `slevomat-design-superpower:minis`.
- The routing skill is `using-design-superpower` (was `using-discovery-kit`), keeping the `using-<plugin>` convention from obra/superpowers without repeating the `slevomat` prefix.
- The marketplace is `slevomat-design-skills`, matching the repository at `slevomat/design-skills`.

**Why the rename back**

v0.3.0 renamed this to `discovery-kit`. That left four different names for one thing — repo `design-skills`, directory `slevomat-design-superpower`, marketplace `slevomat-discovery-kit`, plugin `discovery-kit` — and every skill reference used the one that matched nothing anyone would see. Owner's decision: one name, `slevomat-design-superpower`, and the repository stays the marketplace.

**Fixed**

- `homepage` and `repository` in both manifests pointed at a repository that does not exist (`slevomat/slevomat-design-superpower`). They now point at `slevomat/design-skills`.
- `validate.py` walks plugin directories instead of assuming a single plugin at the root, and checks that every `plugin.json` version matches the marketplace.

## v0.6.0 — 2026-08-12

Real Slevomat vocabulary, and hard limits on how much gets written.

**Fixed**

- Invented terminology replaced throughout. "Člověk z péče" was mine, not the company's. The authority is `slevomat-ai-hub/docs/03-team-and-processes/Slovníček pojmů pro AI.md`, and the real words are: **CS** for the customer line, **PP** (partnerská péče, partner operations) for the partner line, **obchodník** for the person who wins and looks after B2B partners, **DM** for the deals manažer who owns a deal's content, **Inside sales** for the office-based half, **Admin** and **Padmin** for the internal and partner-facing systems, **Termino** for our reservation system.
- `brief/CONTEXT.md` rewritten from that glossary: names (Slevomat Group / Slevomat / Zľavomat / Sleváč), B2C and B2B, the three verticals with their spoken forms (cesto, travel domestik, lokál, zboží), who does what, the internal systems, and the commercial vocabulary a brief actually runs into — voucher, No show, dynamika, Slevomat ads, All stars, Dárkovka, Check list, VOP, OTA, PMS, AHR, CK Zanzo.
- Axis positions and examples in `ideate`, `variants`, `define`, `validate` and `sizing` now use those words: *zákazník sám / partner sám v Padminu / obchodník nebo DM ručně*, not invented job titles.

**Changed**

- **Output discipline is now a hard limit, not a preference.** One question per turn. Three lines of your own text per turn. One line per artefact field. A shared question budget for the whole path — jednorázovka 2, interní 5, ven 8 — across all phases together, not per phase.
- When the budget runs out, the missing sections get written down and the work hands over. A brief with three honest gaps beats an interrogation nobody finishes, and it is the same information either way.
- Canonical version of the rule lives in `using-design-superpower`; every skill carries a one-line reminder so it still holds when a skill loads on its own.
- Explicitly banned in every skill: repeating back what the person just said, summaries of the obvious, „Skvělé", „Rozumím", emoji, narrating which step you are on, offering to expand anything, and a menu of what you could do next.

## v0.5.0 — 2026-08-12

Choosing by looking, and one naming convention for companion files.

**Added**

- `variants` — builds two or three concepts as working, clickable versions behind a floating picker, judged full-size in real context, one promoted. This closed a real hole: `ideate` produced concepts as text and `plan` built one of them, so nobody ever actually **saw** three. For a company whose own deck says "120+ konceptů, filtr na 3" and "klikatelné prototypy hotové dřív, než skončí porada", that was the gap. Harness pattern adapted from the `prototype` skill in [emilkowalski/skills](https://github.com/emilkowalski/skills) (MIT).
- `variants/PICKER.md` — the picker's markup, styles and wiring, to be used as written. Deliberately not theme-aware and never restyled with Mini*S tokens: it is chrome, not a contestant. Number keys to flip, a hash so a variant can be sent in a message, and a print rule so it disappears from screenshots.

**Changed**

- `ideate` now demands a **named axis** per concept, with a table of the axes that are real in this context (who does the work, when in the journey, how much is decided for them, how much is visible, what we are betting on, what it costs). Two concepts on the same position on every axis are one concept. Names are Czech directions — *Tichá*, *Průvodce*, *Ruční* — never `Varianta A/B/C`, because a name that cannot be said out loud in a meeting will not survive the meeting.
- `ideate` also widens through the **trio's three seats** — product, design, engineering. That is the company's core working unit, and the engineering seat's *tohle za den, tohle za měsíc, tohle nikdy* removes more bad options in one sentence than a scoring matrix does in an hour.
- Companion files are now role-named siblings instead of a `references/` directory: `brief/CONTEXT.md`, `sizing/NUMBERS.md`, `minis/CONTENT.md`, `variants/PICKER.md`. Convention taken from emilkowalski/skills, and it removes the `references/` vs `reference/` near-collision. `minis/reference/` keeps its directory because it is a whole vendored tree, not a single file.

**Rejected, on purpose**

- TAM/SAM/SOM from `pm-market-research/market-sizing`. It is investor-pitch framing; for an internal marketplace feature it is exactly the academic detour this plugin is supposed to avoid. `sizing` keeps base x share x share plus a reality check from the company's own campaign.
- Per-skill `$ARGUMENTS` invocation and "Further Reading" link lists from pm-skills. The flow here is conversational, and link lists bloat a file that has a 500-line cap.

## v0.4.0 — 2026-08-12

Routing as a skill, and the missing step between "why" and "build".

**Added**

- `using-design-superpower` — how the eleven skills fit together, which one to reach for, and a **red flags** table of the thoughts that mean the model is rationalising its way into a build ("je to jednoduchý, hned to postavím", "brief si dopíšu sám"). Adapted from `using-superpowers`. Also states precedence: user instructions beat skills beat default behaviour.
- `plan` — what will actually exist in the prototype. Owns `01-plan.md`: screens, the real/faked/dead-end ledger, and an explicit list of what is **not** being built. Adapted from the `brainstorming` skill in obra/superpowers, retargeted from shipping code to prototypes.

**Changed**

- The hook no longer carries its own copy of the routing rules. It reads `skills/using-design-superpower/SKILL.md` and injects it, the way superpowers injects `using-superpowers` — one source of truth, and the routing still exists as a skill where no hook can run (Claude Desktop, Cowork, Cursor).
- `brief` hands off to `plan`, not straight to `minis`. What the prototype contains was previously nobody's decision, which meant it was the first screen's.
- All documentation is English now. Czech stays where the plugin produces something a human reads: questions, artefact templates, session scripts, example dialogues, and the trigger phrases inside every `description`.

**The fake/real ledger** is the part of `plan` with no equivalent in software plans, and it earns its place three times: the person running a session knows in advance where it hits a wall, the reviewer stops filing dead ends as bugs, and a jednorázovka stays visibly a jednorázovka — an exploratory and a candidate prototype look identical from the outside.

## v0.3.0 — 2026-08-12

Split into design-process phases. The plugin was called `discovery-kit` at this point; v0.7.0 renamed it.

**Changed**

- Renamed from `design-superpower` to `discovery-kit`, on the reasoning that `superpower` is obra/superpowers' brand and that `discovery-kit` reads as a pair with Andre's `vibe-kit` in the Hub. Reversed in v0.7.0 — see there.
- `discovery` split into a gate (`brief`) and four phases. The gate establishes the type, sets the **minimum path**, and owns `00-brief.md`; the phases write their own sections into it. No phase has its own document.
- `00-brief.md` grew from six sections to nine: added `Koho to trápí a kolik jich je`, `Dopad na cíl`, `Jak to ověříme`.
- `concept-test` became `validate` and gained the full validation ladder and the kill condition.

**Added**

- `discover` — who has the problem, what they do today, which rung of evidence the claim stands on. Questions about behaviour and the past, never about opinions and the future. Contradictions get recorded, not smoothed.
- `define` — one design challenge, and above all its **altitude**: the three-solutions test and the rejection test.
- `sizing` — how many people have it and which metric moves, computed from Slevomat's real numbers. The reality check is the company's own March 2026 campaign: 62 000 people claimed the credit, 59 bought.
- `sizing/references/cisla.md` — denominators, frequency segments, verticals, money, reality checks, team size for internal tools.
- `ideate` — their ideas first, then widening one constraint at a time, because a model converges. The test that matters is "how do they differ": two concepts differing only in layout are one concept.
- `gaps` — `gaps.md` as a lookup, not a log. Read **before** building a component Mini*S does not have, so five prototypes do not each invent their own modal.
- `review-package` — brief, `gaps.md`, mechanical showability checks, and who has seen it. Target: review in ten minutes instead of an hour.

**Decisions worth recording**

- Phases have exit criteria and one artefact each. That is what separates them from a catalog of methods, which waits for an invocation a vibecoder never makes.
- The gate does not run phases the type does not need. A jednorázovka is two questions, an internal tool two phases, anything going out all four. A process that always runs in full is a tax.
- The most important move in the plugin: **a request almost always names a solution, not a problem.** The gate reframes it once, in the person's own words, and asks what happens today.
- `ideate` may generate concepts but never ranks or recommends. The brief forbade generation outright, while the ASWA deck really did generate 120+ concepts with AI. The line is between volume (material) and the filter (human).
- The kill condition is written down **before** the test. A test without one cannot fail, so it manufactures a mandate instead of an answer.

## v0.2.0 — 2026-08-12

Not released separately; absorbed into 0.3.0. Kept for the order of decisions.

- First versions of `gaps`, `review-package` and `concept-test`.
- Vendored Mini*S documentation replaced the author's paraphrases. The original Czech retellings (`tokeny.md`, `komponenty.md`) were deleted: they blended the source's rules with the author's assumptions — specifically a claim about English UI in prototypes that appears in no source. A copy can be diffed against upstream; a paraphrase cannot.

## v0.1.0 — 2026-08-12

First version. Scope deliberately small: one interview, one file.

- `discovery` — a socratic interview writing `00-brief.md`.
- `discovery/references/slevomat.md` — company context, vocabulary, the four grounding sources, the rule about company data.
- `minis` — design-system rules carried inside the plugin.
- Optional `SessionStart` hook, `validate.py`, CI, and release-from-changelog.

**Decisions from the first version that still hold**

- No hard gate. `allowed-tools` is not enforced in Claude Code ([claude-code#37683](https://github.com/anthropics/claude-code/issues/37683)) and a gate that can be argued with gets argued with, so nothing depends on blocking.
- State lives on disk, not in context. It survives compaction, restarts, and moving between tools.
- The sixth problem-statement field (`Takže zatím…`) is not from the internal Problem Definition playbook, which has five. It is an addition, because it is the only one that cannot be filled from memory.
- A synthetic persona may pre-filter a concept, never serve as evidence for go/kill.

**Still not built**

- Integration into `slevomat/minis-design-system` — one row in the Non-negotiables table of `minis-app`, and a pointer in the `_CLAUDE.md` template.
- Proof that the gate does not put people off. **Kill criterion:** after a week there must be at least two filled-in briefs the owner did not write.
