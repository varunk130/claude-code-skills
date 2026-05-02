# SKILL.md Template

Copy this template when authoring a new skill. Replace placeholders in `<angle brackets>` and delete sections that don't apply, but preserve the section *order* — it's what readers (and AI agents matching descriptions) expect.

```markdown
---
name: <skill-name-in-kebab-case>
description: '<One paragraph describing what the skill does. End with: Use when: <trigger phrase 1>, <trigger phrase 2>, <trigger phrase 3>.>'
---

# <Skill Display Name>

<Two-sentence elevator pitch: what this skill does and why it exists. The reader should be able to decide in 10 seconds whether to invoke this skill or a different one.>

## Core Principle

**<The single key insight that the skill embodies, bolded.>** <One paragraph elaborating why this principle matters and what failures it prevents.>

## What You'll Get

| Artifact | Description |
|----------|-------------|
| **<Output 1>** | <One-sentence description> |
| **<Output 2>** | <One-sentence description> |
| **<Output 3>** | <One-sentence description> |

## Output

Save to `outputs/<topic>-[name]-[YYYY-MM-DD].md`

## Process

### Step 1: <Intake / Frame the Problem>
I'll ask:
> "<The 1–2 questions that frame the skill's input.>"

### Step 2: <Core Step>
<What the skill does mechanically. Be specific.>

### Step 3: <Synthesize / Output>
<How outputs are produced and structured.>

## Demo Scenario (optional)

**Input:**
> <A realistic prompt the skill could receive.>

**Sample Output (excerpt):**

| <Column 1> | <Column 2> | <Column 3> |
|------------|------------|------------|
| ... | ... | ... |

## Tips
1. **<Tip headline>.** <One-sentence elaboration.>
2. **<Tip headline>.** <One-sentence elaboration.>
3. **<Tip headline>.** <One-sentence elaboration.>

## Pairs With (optional)
- **<other-skill>** — <how they compose>
```

---

## Authoring Conventions

These are the rules that make a skill *good*, not just complete.

### Frontmatter

| Field | Required? | Notes |
|-------|-----------|-------|
| `name` | Yes | Must match the folder name (kebab-case) |
| `description` | Yes | Two parts: the *what* (one paragraph) + the *Use when* trigger list |
| Other fields | No | Don't add them — they confuse compatibility across agents |

The `Use when:` clause matters more than the description body. AI agents match user intent against trigger phrases; ambiguous triggers mean the skill never gets selected.

### Tone

- Direct and decision-oriented
- No hedging filler ("may potentially possibly")
- Tables over long prose where structure exists
- Quantitative where possible

### Section Order (don't reorder)

1. **Core Principle** — the insight
2. **What You'll Get / Output** — the deliverable
3. **Process** — how the skill operates
4. **Demo Scenario** (optional) — concrete example
5. **Tips** — operating wisdom
6. **Pairs With** (optional) — composition with other skills

### Length Guidelines

| Skill complexity | Target length |
|------------------|---------------|
| Simple (single output, single framework) | 1.5–3 KB |
| Standard (multi-step process, scoring rubric) | 3–6 KB |
| Complex (multiple sub-frameworks, demos) | 6–10 KB |
| Larger | Almost always means the skill should be split into 2 |

If you're over 10 KB, decompose: each major sub-framework becomes its own skill, with a "pairs with" link.

---

## Quality Bar Checklist

Before opening a PR for a new skill, verify:

- [ ] `name` matches folder name (kebab-case)
- [ ] `description` ends with a `Use when:` clause containing ≥ 3 trigger phrases
- [ ] Core Principle is a single bolded sentence followed by one paragraph
- [ ] Process has at least 3 numbered steps
- [ ] Output location is specified (`outputs/<topic>-...md`)
- [ ] At least 3 Tips, each with a bolded headline
- [ ] No external API dependencies (or, if scaffolded for future wiring, an explicit "not wired" notice)
- [ ] No real customer / company names in examples — use anonymized stand-ins
- [ ] No PII or secrets anywhere in the file
- [ ] Total length is appropriate (see Length Guidelines above)

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| `description` reads like a tagline ("the best X tool!") | Replace with a behavioral description: what the skill *does*, not what it *is* |
| `Use when:` triggers are vague ("when needed") | Concrete phrases the user might actually type |
| One H1 per file is violated | Exactly one H1 (the skill name); use H2 / H3 for everything else |
| Process steps lack a clear "I'll ask" intake | Skills without intake feel impersonal; explicit intake builds trust |
| Tips are generic platitudes | Tips should be the *operating wisdom* — what someone learns running this skill 50 times |
| Demo uses real customer names | Always anonymize ("[Customer X], 1,200 FTEs in your industry") |
| Skill claims to "integrate with X" without wiring | Either wire it, or explicitly mark as "scaffolded, not wired" with a path to live mode |

---

## Submitting a New Skill

1. Open an issue describing the gap and the proposed skill name (kebab-case)
2. Wait for thumbs-up from a maintainer
3. Create `skills/<skill-name>/SKILL.md` from the template above
4. Optionally add `examples/` and `tests.yaml`
5. Update the catalog table in the root README
6. Open a PR titled `feat(skills): add <skill-name> skill`
