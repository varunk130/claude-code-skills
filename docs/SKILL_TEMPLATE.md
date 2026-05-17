# SKILL.md Template

Every custom skill in this library follows the same structure so they are easy to learn, compose, and extend. Copy this template when authoring a new skill — replace placeholders in `<angle brackets>` and keep the section order.

---

## Template

```markdown
---
name: <skill-name-in-kebab-case>
description: "<One sentence on what the skill produces.> Use when <trigger 1>; <trigger 2>; <trigger 3>; <trigger 4>."
---

# <Skill Title>

> <One-line tagline / positioning statement.>

## What this skill is

<2–3 sentences. What is this skill? What approach does it take? Why does it exist?>

## What it solves

- <Pain 1 — concrete failure mode this skill prevents>
- <Pain 2>
- <Pain 3>
- <Pain 4>

## When to invoke

- <Trigger situation 1 — concrete, specific>
- <Trigger situation 2>
- <Trigger situation 3>
- <Trigger situation 4>

## Phase 1: <Name>

<What this phase produces, with any required tables, formulas, or rules.>

## Phase 2: <Name>

<...>

## Phase N: <Name>

<...>

## Output

- <Deliverable 1 produced by the skill>
- <Deliverable 2>
- <Deliverable 3>

## Operating rules

**Always**
- <Rule 1>
- <Rule 2>
- <Rule 3>

**Never**
- <Rule 1>
- <Rule 2>
- <Rule 3>
```

---

## Field-by-field guidance

### `name`

Kebab-case. Must match the folder name. Examples: `dcf-valuation-builder`, `opportunity-solution-tree`, `repeated-game-strategist`.

### `description`

Two parts in one sentence each:

1. **What the skill produces** — concrete output, not a tagline.
2. **Use when…** — at least 3 trigger phrases a user would actually type. AI agents match user intent against these triggers; vague triggers mean the skill never gets selected.

Bad: *"The best DCF tool. Use when you want to value something."*
Good: *"Builds a discounted cash flow valuation with WACC derivation, terminal value reconciliation, and football-field summary. Use when valuing a company, business unit, or acquisition target; preparing a board valuation memo; or stress-testing assumptions against precedent transactions."*

### Title and tagline

- One H1 only — the skill title in Title Case.
- A blockquote one-liner immediately after, capturing the positioning. Should fit on a single line.

### What this skill is

2–3 sentences. Answer: *what is this skill, what's its method, why does it exist?* This is the elevator pitch — a reader should know within 10 seconds whether to invoke this skill or a different one.

### What it solves

4–6 bullets, each a concrete failure mode the skill prevents. Not generic pains ("bad decisions") — specific symptoms a practitioner would recognize.

### When to invoke

4–6 bullets. Each one is a situation in which a user might invoke this skill. These overlap with the frontmatter `Use when` triggers but are more concrete and discoverable in the body.

### Phases

The structured workflow. Numbered phases, each with a clear purpose.

- Use tables for any structured data (scoring rubrics, frameworks, checklists).
- Use code fences for formulas.
- Keep prose tight — practitioners scan, they don't read.

Aim for 3–8 phases. Fewer than 3 → the skill might not need phases. More than 8 → the skill might need to split into two.

### Output

The concrete deliverables the skill produces. Bullet list. Each item is something a user could hand to a stakeholder.

### Operating rules

Two short subsections — **Always** and **Never** — each with 4–6 bullets. These are the guardrails that distinguish a good run of the skill from a bad one. Treat them as the operating wisdom of the skill.

---

## Length guidelines

| Skill complexity | Target size |
|------------------|-------------|
| Simple (single output, single framework) | 2–4 KB |
| Standard (multi-phase, scoring rubric) | 4–7 KB |
| Complex (multi-framework, sensitivity analysis) | 7–10 KB |
| Larger | Almost always means the skill should split into 2 |

If you're over 10 KB, decompose: each major sub-framework becomes its own skill.

---

## Quality checklist

Before opening a PR for a new skill:

- [ ] `name` matches folder name (kebab-case)
- [ ] `description` ends with a `Use when` clause containing ≥ 3 specific trigger phrases
- [ ] Skill lives in the correct category folder (`skills/<category>/<skill-name>/SKILL.md`)
- [ ] One H1 only (the skill title); H2 / H3 for everything else
- [ ] Tagline blockquote immediately under the H1
- [ ] All six core sections present: *What this skill is*, *What it solves*, *When to invoke*, *Phase N*, *Output*, *Operating rules*
- [ ] At least 3 phases
- [ ] Operating rules has both **Always** and **Never** sections
- [ ] No external API or network dependencies in the skill itself
- [ ] No real customer / company names — use anonymized stand-ins
- [ ] No PII or secrets anywhere in the file
- [ ] Total length within the guidelines above
- [ ] Main README updated with the new skill in its category table
- [ ] Category README updated with the new skill

---

## Common mistakes to avoid

| Mistake | Fix |
|---------|-----|
| `description` reads like a tagline | Replace with a behavioral description: what the skill *produces*, not what it *is* |
| `Use when` triggers are vague | Concrete phrases the user might actually type |
| Multiple H1s | Exactly one H1 (the skill title) |
| Phase descriptions are prose walls | Use tables, formulas in code fences, bullets |
| Operating rules are platitudes | They should be the wisdom from running this skill 50 times |
| Skill claims to integrate with X without wiring | Either wire it, or omit the claim |
| Examples use real company names | Use anonymized placeholders |
