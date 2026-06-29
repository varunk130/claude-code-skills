# Changelog

Notable changes to this project, newest first.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## 2026-06-29 - Documentation

### Changed
- Corrected the AI-Eval-Skills reference in Related Work to 7 skills (the upstream repo added the tool-use-eval skill).
- Added the three Next.js multi-agent demos (Compound, Beacon, Atlas) to the Related Work section.

## 2026-06-16 - Documentation

### Changed
- Updated the ai-customer-discovery-skills status in Related Work (5 of 12 skills shipped).

## 2026-05-17 - v2.1: Polish pass and category focus

### Polish
- Removed the `engineering/` and `data-analysis/` categories to focus the library on business decision-making (finance, product, strategy, game theory) and keep `document-processing/`
- Renamed the prior landscape-mapping skill to `strategic-landscape-mapper` and replaced branded terminology with neutral, professional vocabulary (operating principles, environmental forces, strategic plays, maturity axis)
- Spelled out every acronym on first use across all 20 newly-added skills with the abbreviation in parentheses (e.g., Discounted Cash Flow (DCF), Weighted Average Cost of Capital (WACC), Best Alternative to a Negotiated Agreement (BATNA)). Universal acronyms like ASCII are not expanded
- Updated the root README and category README to reflect the new structure and counts

## 2026-05-17 - v2.0: Categorized library and 20 new skills

### Restructure
- Reorganized the flat `skills/` directory into category subfolders for easier discovery and navigation
- Added a category README to each folder with skill index, target audience, and design principles
- Rewrote the top-level README with a complete category-by-category table of contents
- Standardized every custom skill on the same format: *What this skill is → What it solves → When to invoke → Phases → Output → Operating rules*
- Rewrote `docs/SKILL_TEMPLATE.md` to match the unified format and added a quality checklist
- Removed `docs/AUTHORING_QUICKSTART.md` (duplicated `SKILL_TEMPLATE.md` with a different format)
- Removed `docs/CROSS_AGENT_TEST_HARNESS.md` (unwired design document)
- Updated `CONTRIBUTING.md` to reflect the new category structure and unified format

### New skills - Financial Analysis (5)
- `dcf-valuation-builder` - defensible DCF with WACC build, terminal-value reconciliation, sensitivity, football field
- `saas-cohort-analyzer` - retention triangles, NRR / GRR, LTV, CAC payback, movement bridge
- `capital-allocation-framework` - NPV / IRR / PI / EAA plus strategic option value across a portfolio frontier
- `burn-rate-runway-planner` - burn decomposition, scenario plans, 13-week cash forecast, fundraise triggers
- `financial-statement-analyzer` - Form 10-K and Form 10-Q teardown with margin waterfall and accounting red-flag log

### New skills - Product Management (5)
- `jobs-to-be-done-extractor` - JTBD job statements, job map, outcome scoring, hire / fire analysis
- `opportunity-solution-tree` - Opportunity Solution Tree connecting outcomes to opportunities and assumption tests
- `product-roadmap-prioritizer` - RICE plus Kano plus MoSCoW plus Cost of Delay convergence analysis
- `customer-interview-synthesizer` - coded transcripts, themes, JTBD signals, opportunity hypotheses
- `product-discovery-coach` - continuous discovery practice with trio cadence and dual-track

### New skills - Strategic Management (5)
- `porters-five-forces-analyzer` - Five Forces scorecard with dominant force and strategic moves
- `blue-ocean-strategy-canvas` - ERRC grid, non-customer analysis, buyer utility map, sequence test
- `strategic-landscape-mapper` - value chain on a maturity axis with environmental forces, operating principles, and strategic plays
- `swot-tows-analyzer` - evidence-anchored SWOT plus TOWS producing prioritized options
- `okr-cascade-planner` - company → function → team OKR cascade with quarterly rituals

### New skills - Game Theory (5)
- `nash-equilibrium-solver` - pure and mixed equilibria, dominance, subgame perfection, selection
- `negotiation-strategist` - BATNA, ZOPA, multi-issue trades, anchoring, concession plan, tactics
- `competitive-response-modeler` - multi-round action-reaction tree with commitment and signaling
- `mechanism-design-planner` - auctions, matching, pricing with IC / IR / revenue equivalence
- `repeated-game-strategist` - discount factor analysis, tit-for-tat variants, reputation, retaliation
