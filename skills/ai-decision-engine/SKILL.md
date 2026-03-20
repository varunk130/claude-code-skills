---
name: ai-decision-engine
description: "Strategic product decision engine that reads ALL available project context (PRDs, research docs, metrics, competitive intel, roadmaps, CLAUDE.md) and provides holistic, multi-dimensional strategic recommendations. Use when making product prioritization decisions, quarterly planning, evaluating build/ship/kill tradeoffs, resolving conflicting stakeholder input, determining what to build next, or any strategic question requiring synthesis across multiple information sources."
---

# PM Decision Engine — Strategic Context Synthesizer

This skill is a strategic reasoning system. It reads ALL available project context, applies multiple frameworks simultaneously, looks for convergence, and produces a recommendation with explicit reasoning chains.

## PHASE 1: Context Assembly (Always Do This First)

Before answering ANY strategic question, scan the working directory for:
- CLAUDE.md or README.md → product context, team info, constraints
- docs/ or specs/ → existing PRDs, feature specs
- research/ → user research, interview notes, survey results
- data/ or metrics/ → analytics exports, dashboards
- competitive/ → competitor analysis, market research
- roadmap/ → planning artifacts

For each source found, log:
| Source | Key Signal | Recency | Confidence |
|--------|-----------|---------|------------|
| [filename] | [what it tells us] | [when updated] | [high/med/low] |

If critical context is missing, say so: "I don't have [X]. My recommendation will be stronger with it."

## PHASE 2: Situation Model

Write this out before reasoning:
- **Product stage:** Early / Growth / Mature / Turnaround
- **Primary constraint:** Engineering capacity / Market timing / Revenue pressure / Tech debt / Competitive threat
- **Active bets:** What we're currently building and why
- **Unresolved tensions:** Where evidence conflicts
- **Decision type:** One-way door (irreversible) vs. Two-way door (reversible)

## PHASE 3: Multi-Framework Analysis

Apply ALL FOUR frameworks. Never rely on just one.

### Framework 1: Impact x Confidence Matrix
| Option | Expected Impact | Confidence | Evidence Sources |
|--------|----------------|------------|------------------|
| [A] | [quantified if possible] | [High/Med/Low] | [which docs] |

### Framework 2: Strategic Alignment Scoring
Score each option 1-5:
| Dimension | Weight |
|-----------|--------|
| User pain severity | 25% |
| Business impact (revenue, retention, expansion) | 25% |
| Strategic fit (alignment with vision) | 20% |
| Timing sensitivity (competitive urgency) | 15% |
| Execution feasibility | 15% |

Calculate weighted scores. Show the math.

### Framework 3: Second-Order Effects
For top 2-3 options:
- Direct effect → Second-order effect → Third-order effect
- Opportunity cost (what gets delayed/killed)
- Team effect (morale, skills, hiring)
- Market signal (what this tells customers and competitors)

### Framework 4: Pre-Mortem
"It's 6 months from now and this FAILED. What happened?"
- Failure scenario 1: [specific] — Probability: [%] — Early warning: [signal]
- Failure scenario 2: [specific] — Probability: [%] — Early warning: [signal]
- Failure scenario 3: [specific] — Probability: [%] — Early warning: [signal]

## PHASE 4: Synthesis & Recommendation

**TL;DR:** One sentence — what to do and why

**Confidence level:** High / Medium / Low — because [reason]

**Framework convergence:**
- What each framework says
- Where they agree and disagree
- What the divergence tells us

**The recommendation:** 2-3 paragraphs with clear reasoning.

**What would change this recommendation:**
1. If we learned [X], we might instead do [Y]
2. If metric [Z] changes by more than [N%], reconsider
3. If competitor does [W], reassess

**Immediate next steps (this week):**
1. [Specific action]
2. [Specific action]
3. [Specific action]

## Reasoning Rules

**Always:**
- Show reasoning chains
- Quantify where possible
- Acknowledge uncertainty with confidence levels
- Include "do nothing" as an explicit option
- Separate observation from interpretation

**Never:**
- Apply a single framework alone
- Ignore contradictions between sources
- Recommend without stating trade-offs
- Be a yes-machine
- Forget opportunity cost
