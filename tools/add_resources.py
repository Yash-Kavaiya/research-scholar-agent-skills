#!/usr/bin/env python3
"""Install bundled resource files into skills from a batch file, and link them from SKILL.md.

A batch file holds several resources, each introduced by a header line:

    @@@ <skill-name> | <relative/path.md> | <when the agent should open this file>

followed by the file's content up to the next header. Resources go under references/
(guidance to read) or assets/ (templates to copy and fill). Each skill's SKILL.md gets a
"## Reference files" section listing its resources, placed before "## Examples".

    python tools/add_resources.py batch.txt [more.txt ...]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER = re.compile(r"^@@@ ([a-z0-9-]+) \| ((?:references|assets)/[A-Za-z0-9_.-]+) \| (.+)$")
SECTION = "## Reference files"


def parse(text: str) -> list[tuple[str, str, str, str]]:
    items, current, body = [], None, []
    for line in text.splitlines():
        match = HEADER.match(line)
        if match:
            if current:
                items.append((*current, "\n".join(body).strip() + "\n"))
            current, body = match.groups(), []
        elif current is not None:
            body.append(line)
        elif line.strip():
            raise ValueError(f"content before the first header: {line[:60]!r}")
    if current:
        items.append((*current, "\n".join(body).strip() + "\n"))
    return items


def link(skill_dir: Path, entries: dict[str, str]) -> None:
    """Write or refresh the Reference files section from every resource the skill has."""
    path = skill_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    existing = {}
    match = re.search(rf"\n{SECTION}\n\n(.*?)\n(?=\n## )", text, re.S)
    if match:
        for line in match.group(1).splitlines():
            row = re.match(r"- `([^`]+)`: (.+)$", line)
            if row:
                existing[row.group(1)] = row.group(2)
        text = text.replace(match.group(0), "", 1)
    existing.update(entries)
    order = sorted(existing, key=lambda p: (not p.startswith("references/"), p))
    block = (f"{SECTION}\n\nOpen these only when the step calls for them; they are not needed for every request.\n\n"
             + "\n".join(f"- `{p}`: {existing[p]}" for p in order) + "\n")
    marker = "\n## Examples\n"
    if marker not in text:
        raise ValueError(f"{skill_dir.name}: SKILL.md has no Examples section")
    path.write_text(text.replace(marker, "\n" + block + marker, 1), encoding="utf-8", newline="\n")


def main() -> int:
    by_skill: dict[str, dict[str, str]] = {}
    for name in sys.argv[1:]:
        for skill, rel, when, content in parse(Path(name).read_text(encoding="utf-8")):
            skill_dir = ROOT / "skills" / skill
            if not (skill_dir / "SKILL.md").is_file():
                print(f"error: unknown skill {skill}", file=sys.stderr)
                return 1
            target = skill_dir / rel
            target.parent.mkdir(exist_ok=True)
            target.write_text(content, encoding="utf-8", newline="\n")
            by_skill.setdefault(skill, {})[rel] = when.strip()
    for skill, entries in by_skill.items():
        link(ROOT / "skills" / skill, entries)
        print(f"{skill}: {', '.join(entries)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
