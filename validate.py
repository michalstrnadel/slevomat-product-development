#!/usr/bin/env python3
"""Validator for the Slevomat product-development skills.

These skills go into the Skill Hub, where the constraints differ from a Claude Code
plugin: text files only, a flat skill list in which the name is the only clue about
where a skill belongs, and a description that is everything Claude knows before it
opens the skill. Each check below is something that has actually broken.

  1. frontmatter  name and description present, and the name matches the file
  2. naming       kebab-case without diacritics, prefixed by its lane
  3. description  says when NOT to use the skill, and stays inside the length limit
  4. references   every skill a body names resolves to one that exists
  5. hub limits   text formats only, no more than three path levels
  6. vocabulary   no word the company does not say, and no emoji
  7. ladder       the canonical evidence ladder is identical wherever it appears
  8. evals        scenarios parse, ids are unique, and they point at real files

Run:  python3 validate.py
Exit code 0 means clean, 1 means at least one error.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SKILLS = ROOT / "skills"
EVALS = SKILLS / "evals"

MAX_DESCRIPTION_CHARS = 1024

# Skills that live elsewhere in the Hub. Naming one is fine, we just cannot resolve it.
EXTERNAL = {"slevomat-code", "slevomat-documentation", "slevomat-docs", "slevomat-ai-hub",
            # NEROZHODNUTO 19. 8.: krok 4 posílá na design-check, což je nejspíš nové jméno
            # skillu slevomat-design-principles. Dokud se to nerozhodne, je to tady, aby
            # CI běželo — ale je to dluh, ne cizí skill.
            "design-check"}

# A description that never says when to stay away collides with its neighbours, and in
# a flat list a trigger collision is the second most common way a skill fails.
BOUNDARY_MARKERS = ("NEPOUŽÍVEJ", "Nepoužívej", "NEPOUZIVEJ", "Do NOT use", "do NOT use")

# Words the company does not use about itself. The value is what to say instead.
BANNED_WORDS = {
    "spike": "jednorazovka",
    "account manaz": "obchodnik",
    "clovek z pece": "zakaznicka pece",
}

# One vocabulary across the whole process, or claims stop being comparable between steps.
LADDER = ("behaviorální data / tickety zákaznické péče a partnerské podpory / "
          "rozhovory / desk research / domněnka")

# The Hub takes text only. Anything else has to be rewritten so the skill works without it.
ALLOWED_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".csv", ".js"}

FOLD = str.maketrans("áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ", "acdeeinorstuuyzACDEEINORSTUUYZ")

EMOJI = re.compile(
    "["
    "\U0001f300-\U0001faff"
    "\U00002600-\U000027bf"
    "\U0000fe0f"
    "\U00002b00-\U00002bff"
    "]"
)

errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    fields: dict[str, str] = {}
    key = None
    for line in match.group(1).split("\n"):
        if m := re.match(r"([a-z_]+):\s*(.*)", line):
            key, value = m.group(1), m.group(2)
            fields[key] = unquote(value)
        elif key and line.startswith((" ", "\t")):
            fields[key] += " " + line.strip()
    return fields


def unquote(value: str) -> str:
    """Drop the YAML quotes around a value so the checks see the text itself."""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def unquoted_colon(text: str) -> str | None:
    """The frontmatter key whose value is unquoted and holds a colon followed by a space.

    YAML reads that as a nested mapping and refuses the whole block, which is how GitHub
    stops rendering the file and how any strict reader stops seeing the description.
    """
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    for line in match.group(1).split("\n"):
        if m := re.match(r"([a-z_]+):\s*(.*)", line):
            value = m.group(2)
            if value[:1] not in ("\"", "'", "") and ": " in value:
                return m.group(1)
    return None


def skill_files() -> list[tuple[Path, str]]:
    """(path, lane) for every skill text, where lane is product or design."""
    found = []
    for lane in ("product", "design"):
        directory = SKILLS / lane
        if not directory.is_dir():
            fail(f"skills/{lane}/ is missing")
            continue
        for path in sorted(directory.rglob("*.md")):
            if path.name == "README.md":
                continue
            # an attachment sits next to its skill and carries no frontmatter of its own
            if path.parent != directory and path.name != "SKILL.md":
                continue
            found.append((path, lane))
    return found


def check_skill(path: Path, lane: str) -> str | None:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")

    fields = frontmatter(text)
    if not fields:
        fail(f"{rel}: no frontmatter — the Hub reads name and description from it")
        return None

    if key := unquoted_colon(text):
        fail(f"{rel}: {key} holds a colon followed by a space and is not quoted, so the "
             f"frontmatter is not valid YAML. Wrap the value in double quotes.")

    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()

    if not name:
        fail(f"{rel}: frontmatter has no name")
        return None
    if not description:
        fail(f"{rel}: frontmatter has no description — it is the only thing Claude knows "
             f"before opening the skill")

    if name != name.translate(FOLD):
        fail(f"{rel}: name {name!r} contains diacritics")
    if not re.fullmatch(r"[a-z0-9-]+", name):
        fail(f"{rel}: name {name!r} is not kebab-case")

    # the file has to be findable from the name, and the other way round
    stem = path.parent.name if path.name == "SKILL.md" else re.sub(r"^\d+-", "", path.stem)
    if stem != name:
        fail(f"{rel}: name {name!r} does not match the file ({stem!r}) — renaming one and "
             f"not the other silently orphans every reference")

    # in a flat list the prefix is the only clue about where a skill belongs
    if not name.startswith(f"{lane}-"):
        if name.startswith("slevomat-"):
            warn(f"{rel}: name {name!r} carries the slevomat- prefix the Hub rules exclude. "
                 f"It is the already-published name, and the Hub has no delete tool, so "
                 f"renaming it orphans a draft only an admin can remove.")
        else:
            fail(f"{rel}: name {name!r} does not start with its lane ({lane}-)")

    if len(description) > MAX_DESCRIPTION_CHARS:
        fail(f"{rel}: description is {len(description)} chars, limit {MAX_DESCRIPTION_CHARS}")
    if not any(marker in description for marker in BOUNDARY_MARKERS):
        warn(f"{rel}: description never says when NOT to use the skill. In a flat list that "
             f"is how two skills end up triggering on the same phrase.")

    body = text[text.index("---", 3) + 3:]
    folded = body.translate(FOLD).lower()
    for banned, instead in BANNED_WORDS.items():
        if banned in folded:
            fail(f"{rel}: says {banned!r} — the company says {instead!r}")

    if found := EMOJI.findall(text):
        fail(f"{rel}: contains emoji ({''.join(sorted(set(found)))}) — it is an output rule, "
             f"and it applies to what we write too")

    return name


def check_references(paths: list[tuple[Path, str]], known: set[str]) -> None:
    """A skill naming a skill that does not exist sends the reader nowhere.

    Only names shaped like this family are checked, and EXTERNAL lists the ones owned
    elsewhere in the Hub. Everything else has to resolve here, description included: the
    plugin's slevomat-product-development was named in two descriptions for a day after it
    was archived, and nothing complained because only bodies were read.
    """
    # The lookarounds matter: without them the file path docs/.../product-variants.md
    # yields a phantom skill, and slevomat-code yields a phantom 'code'.
    pattern = re.compile(
        r"(?<![\w/-])((?:slevomat|product|design)-[a-z0-9-]+)(?![\w/-]|\.md)")
    for path, _ in paths:
        rel = path.relative_to(ROOT)
        # an HTML comment is bookkeeping — a "renamed from" note records a name that is
        # gone on purpose, which is the opposite of a dangling reference
        text = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)
        for match in sorted(set(pattern.findall(text))):
            if match not in known and match not in EXTERNAL:
                fail(f"{rel}: names {match!r}, which does not exist. Skills owned "
                     f"elsewhere in the Hub belong in EXTERNAL.")


def check_hub_limits() -> None:
    for path in sorted(SKILLS.rglob("*")):
        if path.is_dir() or path.name == ".DS_Store":
            continue
        rel = path.relative_to(ROOT)
        if path.suffix not in ALLOWED_SUFFIXES:
            fail(f"{rel}: the Hub takes text only ({', '.join(sorted(ALLOWED_SUFFIXES))}) — "
                 f"rewrite the skill so it does not need this file")
        if len(path.relative_to(SKILLS).parts) > 3:
            fail(f"{rel}: more than three path levels, which the Hub cannot hold")


def check_ladder(paths: list[tuple[Path, str]]) -> None:
    """The rungs land in a brief verbatim, so a paraphrase makes claims incomparable."""
    for path, _ in paths:
        text = path.read_text(encoding="utf-8")
        if "Příčky důkazů" in text and LADDER not in text:
            fail(f"{path.relative_to(ROOT)}: has an evidence ladder that is not the "
                 f"canonical wording. It has to read exactly:\n           {LADDER}")


def check_evals(known: set[str]) -> None:
    files = sorted(EVALS.glob("*.json"))
    if not files:
        fail("skills/evals/ has no scenarios — then nothing checks what the skills do, "
             "only that the files are well formed")
        return

    seen: dict[str, str] = {}
    covered: set[str] = set()

    for path in files:
        rel = path.relative_to(ROOT)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{rel} does not parse: {exc}")
            continue

        scenarios = data.get("scenarios", [])
        if not scenarios:
            fail(f"{rel} has no scenarios")

        for scenario in scenarios:
            sid = scenario.get("id", "?")
            if sid in seen:
                fail(f"{rel}: scenario id {sid!r} is already used in {seen[sid]}")
            seen[sid] = str(rel)
            covered.update(scenario.get("skills", []))

            if not scenario.get("query"):
                fail(f"{rel}: scenario {sid} has no query")
            if not scenario.get("must") or not scenario.get("must_not"):
                fail(f"{rel}: scenario {sid} needs both must and must_not")

            # the file is named after the skill it grades, so a rename cannot orphan it
            if path.stem not in scenario.get("skills", []):
                fail(f"{rel}: scenario {sid!r} does not name {path.stem!r}, the skill this "
                     f"file is for")

            for skill in scenario.get("skills", []):
                if skill not in known:
                    fail(f"{rel}: scenario {sid} names skill {skill!r}, which does not exist")

            for target in scenario.get("skill_files", []):
                if not (ROOT / target).exists():
                    fail(f"{rel}: scenario {sid} points at {target}, which does not exist")

    for name in sorted(known - covered):
        warn(f"{name} has no eval scenario — nothing checks whether it behaves")


def print_report(count: int = 0) -> None:
    for msg in errors:
        print(f"ERROR    {msg}")
    for msg in warnings:
        print(f"WARN     {msg}")
    if errors:
        print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    else:
        print(f"clean - {count} skill(s), {len(warnings)} warnings")


def main() -> int:
    paths = skill_files()
    if not paths:
        fail("no skills found under skills/")
        print_report()
        return 1

    known = set()
    for path, lane in paths:
        if name := check_skill(path, lane):
            known.add(name)

    check_references(paths, known)
    check_hub_limits()
    check_ladder(paths)
    check_evals(known)

    print_report(len(paths))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
