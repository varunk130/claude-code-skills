---
name: wardley-mapping
description: "Builds a Wardley Map: user-need value chain plotted against component evolution (genesis → custom-built → product → commodity), with climatic patterns, doctrine checks, and strategic plays identified. Use when designing platform strategy, deciding what to build / buy / outsource, anticipating commoditization waves, planning multi-year technology investment, or aligning a leadership team on landscape and direction."
---

# Wardley Mapping

> Strategic landscape mapping that shows where the terrain is moving, not just what it looks like today.

## What this skill is

A workflow that produces a Wardley Map: value chain from user need down to commodity components, plotted on the evolution axis (genesis → custom-built → product / rental → commodity / utility). It applies climatic patterns (everything evolves, no choice on direction), doctrine (universal best practices), and gameplay (deliberate strategic moves) to recommend where to invest, what to outsource, and what to anticipate next.

## What it solves

- "Strategy" decks that have no map — only frameworks
- Decisions to build in-house what is becoming commodity (or vice versa)
- Missing the predictable transition from custom-built to product to utility
- Confusing operational efficiency with strategic positioning
- Inability to communicate landscape to a leadership team in a single picture

## When to invoke

- Platform vs. product strategy decisions
- Build / buy / outsource trade-offs at scale
- Multi-year capex or tech investment planning
- Anticipating commoditization waves (and the firms it will hurt)
- Aligning a leadership team on the competitive landscape

## Phase 1: Anchor on the user and their need

Every map starts with the user (top of the map) and their **need** (one level below). Examples:
- Banking user → needs to send money
- Streaming viewer → needs to be entertained
- Developer → needs to ship code reliably

Without an anchored user need, the map is just a wishlist.

## Phase 2: Build the value chain

Below the user need, decompose the components required to satisfy it. Each component:
- Visible to user OR
- Required to deliver a higher component (inferred from technical architecture)

Layers typically follow:
- User need (e.g., send money)
- Capability (e.g., transfer service)
- Sub-capability (e.g., authentication, ledger, settlement, fraud detection)
- Practice (e.g., KYC processes)
- Data (e.g., transaction history)
- Infrastructure (e.g., compute, storage, network)

Connect each child to its parent with a dependency edge. The chain typically has 3–6 layers.

## Phase 3: Plot on the evolution axis

Place each component on the X-axis based on its evolution stage:

| Stage | Characteristics | Example (in 2025) |
|-------|-----------------|--------------------|
| **Genesis** | Novel, rare, uncertain, high variation | Quantum-resistant cryptography |
| **Custom-built** | Bespoke per organization, expensive | Custom LLM fine-tuning workflows |
| **Product / rental** | Multiple vendors, comparable offerings | Vector databases |
| **Commodity / utility** | Standardized, undifferentiated, metered | Compute, storage, bandwidth |

Plot each component as a node at the right horizontal position. Components shift right over time — never left.

## Phase 4: Apply climatic patterns

Climatic patterns are inevitable forces — like weather. You don't control them; you account for them.

Key patterns to check:
- **Everything evolves** — assume rightward drift; ask "what will commoditize in 3–5 years?"
- **Higher-order systems create new sources of worth** — commoditizing one component enables novel uses above it (e.g., cloud commoditization → SaaS explosion)
- **Past success breeds inertia** — incumbents resist commoditization of their core
- **Co-evolution of practice with activity** — DevOps emerged with cloud, not separately
- **Punctuated equilibrium** — long stability, then rapid transition; identify which components are near a tipping point

## Phase 5: Apply doctrine

Doctrine = universally good practices, independent of context:
- Focus on user needs
- Know your users
- Use a common language (the map itself)
- Be transparent
- Challenge assumptions
- Use appropriate methods at each evolution stage (genesis → experimental, commodity → industrial efficiency)
- Manage inertia (it's emotional and structural)
- Optimize flow, not silos
- Bias toward the new (or be eaten by it)

Score the organization on each. Doctrine gaps are easier to fix than strategy mistakes.

## Phase 6: Identify gameplay

Gameplay = deliberate strategic moves available on the map:
- **Accelerate evolution** — invest to push a component right (commoditize a competitor's differentiation)
- **Slow evolution** — patent, regulate, FUD (defensible only short-term)
- **Open source** — commoditize complements; classic IBM / Red Hat / Google move
- **Build a market** — create demand for a component (Stripe and "online payments")
- **Sensible** trade-off between methods at each stage:
  - Genesis → in-house lean / agile
  - Custom → in-house or contractor
  - Product → buy off-the-shelf
  - Commodity → use a utility provider
- **Pioneer / Settler / Town Planner** — explicit team structure matched to evolution stage

## Phase 7: Strategic recommendations

For each component on the map, recommend an action:

| Component | Current stage | 3y stage | Action | Rationale |
|-----------|--------------|---------|--------|-----------|
| [name] | Custom | Product | Stop building, buy | Pioneering effort no longer differentiates |
| [name] | Product | Commodity | Switch to utility, redeploy capex | Cost savings; redirect to genesis bets |
| [name] | Genesis | Custom | In-house team, accept high failure | Optionality; differentiation if it works |

Cross-check against:
- Competitor maps (where are they investing?)
- Substitute industries (where could lateral entrants come from?)
- Regulatory trajectory

## Output

- One-page Wardley Map with user need, value chain, and evolution plot
- Climatic patterns commentary
- Doctrine scorecard
- Gameplay recommendations per component
- 3-year forward-looking map showing predicted evolution
- Top 3 strategic plays with first 90-day moves
- Inertia map: which incumbents (internal or external) will resist

## Operating rules

**Always**
- Start with the user and their need
- Plot on evolution stage, not just dependency
- Apply climatic patterns first (the inevitable), then doctrine, then gameplay
- Re-map every 6–12 months
- Identify inertia explicitly

**Never**
- Build a map without an anchored user need
- Treat the map as a static deliverable
- Confuse the dependency axis with the evolution axis
- Skip the "what will be commodity in 3 years" question
- Use a single method (e.g., agile) across all evolution stages
