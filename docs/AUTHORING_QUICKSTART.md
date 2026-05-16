# SKILL.md Authoring Quickstart

Copy the template below into `skills/<your-skill>/SKILL.md`, fill in the placeholders, and you have a working skill. Keep it under 200 lines; longer skills usually want to be split.

## Template

```markdown
---
name: <kebab-case-id>
description: <one-line action sentence — "Does X to produce Y for Z scenario.">
trigger: <when an agent should load this skill, in a sentence>
---

# <Human Name>

## When to use
- <bullet — concrete situation 1>
- <bullet — concrete situation 2>

## Inputs
- `<input-1>` — <shape + example>
- `<input-2>` — <shape + example, optional>

## Output
A deterministic shape, ideally fenced markdown or JSON:

\`\`\`markdown
## <Section>
- ...
\`\`\`

## Workflow
1. <Step that consumes the inputs>
2. <Step that produces the intermediate state>
3. <Step that emits the output>

## Anti-patterns (refuse to emit)
- <Smell 1 — describe and reject>
- <Smell 2>
```

## 6 questions to answer first

1. Who triggers this skill — a user, another skill, the orchestrator?
2. What's the exact input shape?
3. What's the deterministic output shape?
4. What's "success" — how do you know the skill worked?
5. What's the failure mode — what does the skill emit when it can't do its job?
6. What other skills would someone confuse this with — and how do you steer them right?

## Common anti-patterns

- **Open-ended scope.** "Helps with marketing" is not a skill; "Drafts a single LinkedIn ad variant for a stated ICP and CTA" is.
- **Hidden side effects.** A skill should not write files or call services unless the SKILL.md says so.
- **Output drift.** If the output shape is "freeform prose," consumers can't compose with it. Pin the shape.

## Test locally

```bash
# Drop the folder under your skills dir and invoke by name
cp -r skills/<your-skill> ~/.claude/skills/
# Then in Claude Code:  "Use the <your-skill> skill on <sample input>."
```
