# Contributing

Thanks for considering a contribution to this skills library.

## Adding a new skill

1. **Open an issue** describing the gap and the proposed skill name (kebab-case).
2. **Wait for a thumbs-up** from a maintainer — this avoids duplicate work.
3. **Create the file** at `skills/<category>/<skill-name>/SKILL.md` using [`docs/SKILL_TEMPLATE.md`](docs/SKILL_TEMPLATE.md). Categories live under `skills/`: `financial-analysis`, `product-management`, `strategic-management`, `game-theory`, `document-processing`.
4. **Update the catalog**:
   - Add a row to the corresponding table in the root [README.md](README.md).
   - Add a row to the category README at `skills/<category>/README.md`.
5. **Open a PR** titled `feat(<category>): add <skill-name> skill`.

## SKILL.md format

Every skill follows the same structure:

```
What this skill is → What it solves → When to invoke → Phase N → Output → Operating rules
```

See [`docs/SKILL_TEMPLATE.md`](docs/SKILL_TEMPLATE.md) for the full template, field-by-field guidance, length targets, and the quality checklist you should run through before opening a PR.

## Frontmatter

Every SKILL.md begins with YAML frontmatter:

```yaml
---
name: <skill-name>
description: "<What the skill produces.> Use when <trigger 1>; <trigger 2>; <trigger 3>."
---
```

The `description` is what AI agents match against when deciding to invoke the skill — make the trigger phrases specific.

## Style

- One H1 per file (the skill title)
- Tables over long prose where structure exists
- Formulas in code fences
- No external API calls or network dependencies in the skill itself
- No real customer / company names — use anonymized stand-ins
- No secrets or PII anywhere

## Reporting issues

- **Bugs** in existing skills: use the bug report template
- **New skill proposals**: use the new-skill proposal template
- **Documentation**: open an issue with the `docs` label

## Code of Conduct

We follow the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
