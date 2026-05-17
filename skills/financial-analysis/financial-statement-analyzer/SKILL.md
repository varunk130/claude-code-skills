---
name: financial-statement-analyzer
description: "Performs structured fundamental analysis of 10-K / 10-Q / annual reports: ratio analysis, quality of earnings, working-capital efficiency, segment decomposition, accounting red flags, and MD&A parsing. Use when underwriting an investment, evaluating a competitor, prepping for an earnings call, building peer comps, or screening for accounting risk."
---

# Financial Statement Analyzer

> A repeatable teardown of public-company financials that produces an institutional-quality analysis.

## What this skill is

A structured workflow that reads the full 10-K / 10-Q stack — income statement, balance sheet, cash flow, MD&A, footnotes, risk factors, and proxy — and produces a one-page summary with margin waterfalls, quality-of-earnings score, segment decomposition, and an accounting red-flag log. Designed to surface the data the headline numbers hide.

## What it solves

- Headline EBITDA reviews that ignore non-GAAP adjustments
- Margin analysis with no waterfall identifying which line item moved
- Missed red flags hiding in footnotes, risk factors, and CCC trends
- Segment data taken at face value (without checking corporate-overhead allocation)
- Skipping the year-over-year diff of risk factors — the single most under-read disclosure

## When to invoke

- Underwriting a long or short position in a public company
- Benchmarking a private company against the public peer set
- Pre-earnings prep for management Q&A
- Quarterly competitor financial review
- Diligence on a partnership, vendor, or acquisition target

## Phase 1: Source the filings

Confirm the latest:
- 10-K (or 20-F) — most recent fiscal year
- 10-Q — trailing 4 quarters
- 8-K — material events, guidance, restatements (last 12 months)
- DEF 14A proxy — exec comp, related-party, board composition
- Earnings release + supplemental (segment data often only here)
- Earnings call transcript — tone, Q&A pressure points

Log filing date and period for each. Note any restatements.

## Phase 2: Quality of revenue

- Revenue recognition policy (ASC 606 adherence)
- Performance obligation timing — ratable vs. point-in-time
- Deferred revenue trend (B/S liability) — should grow with bookings
- RPO / backlog — directional read on future revenue
- Customer concentration (top-10 % of revenue, footnotes)
- Geographic / segment mix — where is growth coming from?
- Channel inventory / sell-in vs. sell-through (CPG, hardware) — channel-stuffing risk
- Non-GAAP adjustments — list each and decide if defensible

Compute organic growth = reported growth − M&A − FX − accounting policy change.

## Phase 3: Profitability & margin architecture

Margin waterfall YoY:

| Line | Y-2 | Y-1 | Y | Δ bps | Driver |
|------|-----|-----|---|-------|--------|
| Revenue | $X | $X | $X | n/a | |
| Gross margin | xx% | xx% | xx% | ±bps | mix / pricing / cost |
| R&D % | xx% | xx% | xx% | ±bps | innovation intensity |
| S&M % | xx% | xx% | xx% | ±bps | growth investment |
| G&A % | xx% | xx% | xx% | ±bps | operating leverage |
| Operating margin | xx% | xx% | xx% | ±bps | |
| Tax rate | xx% | xx% | xx% | ±bps | mix / one-timers |
| Net margin | xx% | xx% | xx% | ±bps | |

DuPont decomposition: `ROE = Net margin × Asset turnover × Equity multiplier`. Identify which lever moved.

## Phase 4: Working capital & cash conversion

```
CCC = DSO + DIO − DPO
```

- DSO rising → collection problems, channel stuffing, or longer-term contracts
- DIO rising → demand softness, obsolescence
- DPO rising → vendor financing, possibly stress

Compare **CFO/Net income**:
- <1× across multiple periods → earnings-quality concern
- Identify the gap (working capital, SBC, deferred tax)

FCF / Adj. EBITDA conversion: SaaS 60–80% healthy; services 80%+.

## Phase 5: Balance sheet & capital structure

- Net debt / Adj. EBITDA → covenant headroom, refi risk
- Interest coverage = Adj. EBITDA / interest expense
- Maturity wall (footnotes) — concentration in next 18 months?
- Off-balance-sheet items (operating leases on B/S under ASC 842, purchase commitments, contingent consideration)
- Goodwill + intangibles as % of equity → impairment risk
- Pension / OPEB underfunded status
- Tangible book value vs. market cap → strategic floor

## Phase 6: Accounting red flags

| Red flag | Look for | Severity |
|----------|----------|----------|
| DSO jumping | up >20% YoY without business-model change | High |
| Cost reclass | COGS moved to opex | Medium |
| Asset quality decline | non-current up faster than revenue | Medium |
| Soft revenue | revenue growth >> cash collection growth | High |
| SG&A growing slower than revenue | possible cost capitalization | Medium |
| Depreciation rate dropping | useful-life extensions | Medium |
| Accruals / assets rising | earnings management | High |
| Recurring one-time charges | cookie-jar reserves | Medium |
| Goodwill up without impairment | rolling acquisitions, no test | Medium |
| Restatements last 3y | internal control weakness | High |

Cross-check the auditor's report: going concern, critical audit matters (CAMs), or auditor change.

## Phase 7: Segment decomposition

- Revenue + EBIT by segment with margins
- Inter-segment eliminations
- Allocation of corporate overhead — does management hide losses?
- Segment capex if disclosed
- Identify the value-driver and the value-destroyer segments
- Sum-of-the-parts cross-check on consolidated multiples

## Phase 8: MD&A & risk factors

- MD&A: specific vs. vague YoY explanations
- **Year-over-year diff of risk factors** — new risks added are the most revealing single signal in the filing
- Critical accounting estimates — where management has the most judgment
- Earnings call tone — hedging language, CFO guidance walk

## Output

- One-page executive summary: bull case, bear case, decisive data point
- Margin and CCC waterfalls with YoY drivers
- Quality-of-earnings score (1–10) with reasoning
- Red-flag log with severity and follow-up question
- Peer comp table: growth, GM, op margin, FCF margin, ROIC, leverage
- 3 questions to ask the CFO on the next earnings call

## Operating rules

**Always**
- Reconcile non-GAAP to GAAP and judge each adjustment
- Read footnotes — that's where the disclosures live
- Compare CFO to net income across multiple years
- Cross-check segment data against the press release supplemental
- Document data gaps explicitly

**Never**
- Trust headline EBITDA without the bridge
- Treat one quarter as a trend
- Skip the YoY risk factors diff
- Use peer multiples without normalizing for accounting policy
- Confuse organic growth with reported growth
