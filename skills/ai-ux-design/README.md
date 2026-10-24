# AI UX & Design Skills

User experience design for Artificial Intelligence (AI) products and agents: autonomy, human oversight, failure handling, uncertainty, input design, and research methods built for non-deterministic systems.

| Skill | What it produces |
|-------|------------------|
| [agent-autonomy-level-mapper](agent-autonomy-level-mapper/SKILL.md) | Per-action autonomy map (suggest / draft / act-with-approval / act-and-report / act-silently) from a stakes x reversibility x confidence score, with approval-gate spec and promotion criteria |
| [ai-failure-state-designer](ai-failure-state-designer/SKILL.md) | Failure-mode inventory mapped to User Interface (UI) patterns, recovery actions, latency treatments, and microcopy library |
| [ai-usability-test-planner](ai-usability-test-planner/SKILL.md) | Usability study plan for non-deterministic features: Wizard-of-Oz and seeded-output tasks, variance-aware metrics, trust-calibration measures, offline evaluation pairing |
| [ai-ux-audit](ai-ux-audit/SKILL.md) | Stakes-weighted heuristic scorecard across six AI dimensions with stress-scenario evidence and severity-ranked fix list |
| [human-in-the-loop-designer](human-in-the-loop-designer/SKILL.md) | Human-in-the-loop (HITL) touchpoint design: checkpoints, approval gates, escalation triggers, handoff packages, interruption-cost scoring, and review-fatigue limits |
| [prompt-surface-designer](prompt-surface-designer/SKILL.md) | Chat and agent input experience: capability inventory, blank-box risk score, scored starter prompts, input affordances, follow-ups, and first-run onboarding |
| [uncertainty-and-explainability-patterns](uncertainty-and-explainability-patterns/SKILL.md) | Confidence, citation, and reasoning pattern spec matched to audience and risk, with calibration checks and anti-pattern review |

## Who these are for

Product designers, User Experience (UX) researchers, product managers, design leads, and engineers building copilots, assistants, and agents that act on behalf of users.

## Design principles

- **Calibrated trust over maximum trust** - help users rely on AI exactly as much as it deserves
- **Measure before you display** - confidence and autonomy rest on evaluation data, not demos
- **Design for failure first** - the failure path is a primary flow, not an edge case
- **Attention is a budget** - every approval and interruption must earn its cost
- **Separate interface from model** - diagnose whether a problem is design, behavior, or policy
