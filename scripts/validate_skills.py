#!/usr/bin/env python3
"""Validate every SKILL.md in skills/ against the library's standard format.

Checks:
  - YAML frontmatter with `name` and `description`
  - `name` is kebab-case and matches the skill's folder name
  - `description` includes explicit "Use when" triggers
  - required sections from docs/SKILL_TEMPLATE.md are present
  - no em dashes or en dashes (the library uses ASCII hyphens)
  - every skill is listed in its category README and the root README

Exit code is 1 if any check fails. Standard library only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
REQUIRED_SECTIONS = [
    "## What this skill is",
    "## What it solves",
    "## When to invoke",
    "## Output",
    "## Operating rules",
]
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip("'\"")
    return fields


def main() -> int:
    errors: list[str] = []
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    skill_files = sorted(SKILLS.glob("*/*/SKILL.md"))

    for path in skill_files:
        rel = path.relative_to(ROOT)
        folder = path.parent.name
        category_readme = path.parent.parent / "README.md"
        text = path.read_text(encoding="utf-8")

        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing or malformed YAML frontmatter")
            continue
        name = fm.get("name", "")
        description = fm.get("description", "")
        if not KEBAB.match(name):
            errors.append(f"{rel}: name '{name}' is not kebab-case")
        if name != folder:
            errors.append(f"{rel}: name '{name}' does not match folder '{folder}'")
        if "Use when" not in description:
            errors.append(f"{rel}: description has no 'Use when' triggers")

        for section in REQUIRED_SECTIONS:
            if not re.search(rf"^{re.escape(section)}\s*$", text, re.MULTILINE):
                errors.append(f"{rel}: missing section '{section}'")

        for lineno, line in enumerate(text.splitlines(), 1):
            if "—" in line or "–" in line:
                errors.append(f"{rel}:{lineno}: em or en dash (use an ASCII hyphen)")

        if not category_readme.exists():
            errors.append(f"{category_readme.relative_to(ROOT)}: category README missing")
        elif f"({folder}/SKILL.md)" not in category_readme.read_text(encoding="utf-8"):
            errors.append(f"{rel}: not listed in {category_readme.relative_to(ROOT)}")
        if f"/{folder}/SKILL.md)" not in root_readme:
            errors.append(f"{rel}: not listed in README.md")

    for message in errors:
        print(f"error: {message}")
    print(f"Checked {len(skill_files)} skills: {len(errors)} problem(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
