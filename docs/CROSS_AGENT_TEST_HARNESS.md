# Cross-Agent Test Harness — Design & Operating Notes

A scaffolding document describing how to verify that skills in this library behave consistently across multiple AI coding agents (Claude Code, GitHub Copilot, Cursor, Codex). Today the verification is manual; this document defines the structure for automating it.

> **No test harness is wired in this commit.** This is a design document, an output schema, and a documented seam. Anyone wiring the actual test runners has a single, well-defined interface to implement per agent.

---

## Why This Matters

Skills in this library claim to be "agent-compatible" — but compatibility is asserted, not tested. A skill that works in Claude Code may silently misbehave in another agent because of differences in:

- How `description` triggers are matched against user intent
- Token / context window budgets
- Markdown rendering (table support, frontmatter handling)
- Tool / file-access primitives the skill assumes are available
- Streaming vs batch invocation patterns

Without a test harness, regressions reach users before they reach maintainers.

---

## The Three Levels of Compatibility Testing

Different tests answer different questions. The harness supports three distinct levels:

| Level | Tests | Run Frequency | Cost |
|-------|-------|---------------|------|
| **L1 — Structural** | SKILL.md frontmatter validity, required sections present, internal links resolve, no banned content | Every PR | Free (no agent invocation) |
| **L2 — Trigger Match** | Does each agent recognize the skill from its `description` when given the canonical use phrases? | Nightly | Low (one short prompt per agent per skill) |
| **L3 — Behavioral** | Does the skill produce equivalent (not identical) outputs across agents on a fixed input? | Weekly | High (full skill invocation per agent) |

L1 is the cheapest and catches the most failures. L2 catches "the skill exists but the agent never picks it." L3 catches subtle behavioral drift.

---

## Per-Agent Adapter Interface

Each agent gets one adapter implementing this interface:

```
class AgentAdapter:
    name: str             # "claude-code" | "github-copilot" | "cursor" | "codex"
    available: bool       # whether the adapter has the credentials / runtime to execute

    def install_skills(self, skills_dir: Path) -> None:
        """Install / register the skills folder with this agent."""

    def trigger_match(self, skill_name: str, prompt: str) -> bool:
        """L2: given a prompt, did this agent select the named skill?"""

    def invoke(self, prompt: str, timeout_sec: int = 120) -> AgentResponse:
        """L3: run the agent against a prompt. Return the final response + tool/skill trace."""
```

If an adapter's `available` is False (missing credentials, runtime not installed), the harness skips that agent's tests with a clear "skipped: <reason>" annotation rather than failing.

---

## Test Definition Schema

Each skill ships an optional `tests.yaml` alongside its SKILL.md:

```yaml
skill: opportunity-triangulator
l2_triggers:
  - "size the opportunity for X"
  - "what's the TAM for X"
  - "validate this opportunity"
  - "is X worth building"
l3_behavioral:
  - id: basic-tam-question
    prompt: "Size the opportunity for an AI-native CRM for solo lawyers."
    expectations:
      - structure: "must contain 3 named sizing methods"
      - structure: "must contain a gap-analysis section"
      - quality: "TAM number must be present and within 1 order of magnitude across agents"
      - quality: "all three methods must produce numbers within 2x of each other"
```

`structure` expectations are evaluated with simple regex / section-presence checks. `quality` expectations are evaluated by a judge model against a rubric (see L3 Scoring below).

---

## L1 — Structural Validation

Runs on every PR. Pure static analysis, zero agent invocations:

| Check | Failure Action |
|-------|----------------|
| `name` field in frontmatter is present and matches folder name | Block PR |
| `description` field is present, non-empty, ≤ 500 chars | Block PR |
| `description` contains a `Use when:` clause with ≥ 3 trigger phrases | Warn |
| All internal markdown links resolve | Block PR |
| No external dependencies named without an explicit "no-wiring" notice | Warn |
| File size < 50 KB (large skills are usually under-decomposed) | Warn |

L1 is implemented in CI (GitHub Actions); no agent runtime needed.

---

## L2 — Trigger Match Testing

For each skill's `l2_triggers`, run each adapter:

1. Install the skill into the agent's skills directory
2. Issue the trigger prompt as a fresh conversation
3. Inspect: did the agent select the named skill?
4. Record pass/fail per (agent × trigger × skill)

Output: a per-skill trigger-match matrix that surfaces "this skill works in Claude Code but never gets picked by Cursor" patterns.

---

## L3 — Behavioral Equivalence Testing

The hardest level. Runs the full skill end-to-end on each agent and checks that outputs are *equivalent*, not *identical* (model differences make identical impossible).

### Equivalence Criteria

| Type | Definition |
|------|------------|
| **Structural** | Required sections present, output format matches, key fields populated |
| **Quantitative** | Numbers within tolerance (e.g., TAM estimates within 1 order of magnitude) |
| **Qualitative** | Judge-model rubric scores within 1 point on a 0–3 scale |

### L3 Scoring with a Judge Model

For qualitative checks, a judge model (separate from the agents under test) scores each agent's output against the skill's expected-behavior rubric. The judge model is *the same* across all agents to keep scoring fair.

**Important:** the judge model is not wired in this scaffolding. The seam exists; the implementation is deferred until the broader test harness is built.

---

## Output

The harness produces a **Compatibility Report** per release:

```
## ai-skills-library — Compatibility Report (release v1.4.0)

| Skill                       | L1 | L2 (CC) | L2 (GHC) | L2 (Cursor) | L3 (CC) | L3 (GHC) | L3 (Cursor) |
|-----------------------------|----|---------|----------|-------------|---------|----------|-------------|
| opportunity-triangulator    | ✅ | ✅ 4/4  | ✅ 4/4   | ⚠️ 3/4      | ✅      | ✅       | ⚠️          |
| jtbd-extractor              | ✅ | ✅ 5/5  | ✅ 5/5   | ✅ 5/5      | ✅      | ✅       | ✅          |
```

Skills with L2/L3 failures are flagged for skill-author attention before release. Skills that pass all levels can carry an `"Agent-Compatible: Verified"` badge.

---

## Cost Considerations

The harness is opt-in by level:

- **L1 only** (default in CI) — free, runs every PR
- **L1 + L2** — small cost per skill per agent per night
- **L1 + L2 + L3** — moderate cost; recommended weekly only

Expected per-run cost is bounded by:
- Number of skills × number of agents × number of test cases per skill
- Each test case is 1 prompt + 1 response (L2) or 1 full skill invocation (L3)

For a library of 12 skills × 4 agents × 5 cases per skill, L3 weekly = 240 invocations/week. The harness ships a `--max-cost-usd` flag that caps total spend per run.

---

## Out of Scope (for this scaffolding)

- Wiring any specific agent adapter
- Implementing the judge model
- CI integration (GitHub Actions workflow files)
- Cost reporting integration
- Compatibility badge automation

These are tracked as follow-on work; the design above is stable and the seams above are sufficient to start implementation.

---

## Why This Is Scaffolding, Not Implementation

Wiring real agents requires either bundling per-agent runtimes (Claude Code, Copilot CLI, Cursor extension APIs, etc.) or running them headlessly via specific subprocess / CLI integrations that vary substantially between agents. That work is meaningful but is a separate effort from defining *what* the harness should test and *how* its outputs should be structured.

This document captures the latter so the wiring work — when it happens — has clear targets.
