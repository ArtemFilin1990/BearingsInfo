#!/usr/bin/env python3
"""Validate Agent Skills package structure.

Checks:
- every skill directory has SKILL.md;
- SKILL.md contains YAML frontmatter;
- frontmatter contains name and description;
- name matches directory name where possible.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = "SKILL.md"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
FIELD_RE = re.compile(r"^(name|description):\s*(.+?)\s*$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.search(text)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for key, value in FIELD_RE.findall(match.group(1)):
        fields[key] = value.strip().strip('"').strip("'")
    return fields


def main() -> int:
    errors: list[str] = []
    skill_dirs = [p for p in ROOT.iterdir() if p.is_dir() and p.name != "scripts"]

    if not skill_dirs:
        errors.append("No skill directories found.")

    for skill_dir in sorted(skill_dirs):
        skill_file = skill_dir / SKILL_MD
        if not skill_file.exists():
            errors.append(f"{skill_dir.name}: missing {SKILL_MD}")
            continue

        text = skill_file.read_text(encoding="utf-8")
        fields = parse_frontmatter(text)

        if "name" not in fields:
            errors.append(f"{skill_dir.name}: missing frontmatter field 'name'")
        elif fields["name"] != skill_dir.name:
            errors.append(
                f"{skill_dir.name}: frontmatter name '{fields['name']}' does not match directory name"
            )

        if "description" not in fields:
            errors.append(f"{skill_dir.name}: missing frontmatter field 'description'")
        elif len(fields["description"]) < 30:
            errors.append(f"{skill_dir.name}: description is too short")

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed: {len(skill_dirs)} skills checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
