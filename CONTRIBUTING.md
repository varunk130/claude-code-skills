# Contributing

Thanks for considering a contribution to this skills library!

## Adding a new skill

1. **Open an issue** describing the gap and the proposed skill name (kebab-case)
2. **Wait for a thumbs-up** from a maintainer before opening a PR — this avoids duplicate work and disagreement-after-the-fact
3. **Create `skills/<skill-name>/SKILL.md`** using the template at [`docs/SKILL_TEMPLATE.md`](docs/SKILL_TEMPLATE.md)
4. **Update the catalog** table in the root README
5. **Open a PR** titled `feat(skills): add <skill-name> skill`

## SKILL.md frontmatter

Every SKILL.md begins with YAML frontmatter:

```yaml
---
name: <skill-name>
description: 'One-paragraph behavioral description ending with: Use when: <trigger phrases>.'
---
```

The `description` is what AI agents match against when deciding to invoke the skill — make the trigger phrases specific. See [the template](docs/SKILL_TEMPLATE.md) for full guidance.

## Style

- One H1 per file (the skill name)
- Lead with a `Core Principle` section
- Tables over long prose where structure exists
- No external API calls or network dependencies in the skill itself (or, if scaffolded for future wiring, an explicit "not wired" notice)
- No real customer / company names — use anonymized stand-ins
- No secrets or PII anywhere

## Quality bar

Before opening a PR, verify against the [quality bar checklist](docs/SKILL_TEMPLATE.md#quality-bar-checklist).

## Compatibility

Skills in this library are intended to work across Claude Code, GitHub Copilot, Cursor, and Codex. The [cross-agent test harness design](docs/CROSS_AGENT_TEST_HARNESS.md) describes how compatibility will be verified once the harness is wired.

## Code of Conduct

We follow the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Be kind.

## Reporting Issues

For bugs in existing skills: use the bug report template.
For new skill proposals: use the new skill proposal template.
For documentation: open an issue with the `docs` label.
