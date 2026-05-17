---
name: burn-rate-runway-planner
description: "Models cash burn, runway, and scenario-based cash flow with explicit triggers, default-alive vs. default-dead diagnosis, and a 13-week rolling forecast. Use when planning a fundraise, deciding on layoffs, evaluating hiring plans, modeling a downturn, presenting cash position to the board, or pressure-testing a CFO operating plan."
---

# Burn Rate & Runway Planner

> Turns the operating plan into an honest cash narrative — with decision triggers, not just a runway number.

## What this skill is

A startup-CFO instrument that decomposes burn, builds three operating scenarios (base, conservative, stretch), and lays out an explicit lever stack ranked by return per unit of strategic damage. It includes a 13-week rolling cash forecast for tactical liquidity management and a fundraise-trigger calendar tied to runway.

## What it solves

- Reporting runway as a single number with no scenario range
- Treating investor commitments as cash before they're wired
- Recommending layoffs as the first lever (instead of last)
- Hiding lumpy disbursements (payroll, tax, insurance) inside an average burn
- No explicit triggers for when fundraising or cost-cutting starts

## When to invoke

- Quarterly board prep for any pre-profitability company
- Pre-fundraise modeling (Series A through pre-IPO)
- Recession or downside scenario planning
- Layoff vs. hiring-freeze vs. spend-cut deliberation
- 13-week tactical cash management when liquidity is tight

## Phase 1: Baseline cash position

- Cash + equivalents as of date
- Available debt capacity (undrawn lines, available SAFEs / converts)
- Restricted cash — exclude from runway math
- Net AR + AP position (working capital)

Define:
- **Gross burn** = total monthly cash out
- **Net burn** = cash out − cash in (revenue + expansion)
- **Cash-zero date** at current net burn

## Phase 2: Burn decomposition

Break monthly cash out by category as **% of total** so the conversation moves to mix, not absolute dollars:

| Category | Monthly $ | % of total | Trend (last 3 mo) |
|----------|----------:|-----------:|-------------------|
| Payroll + benefits | $X | x% | ↑↓→ |
| Contractors | $X | x% | ↑↓→ |
| Cloud / infra | $X | x% | ↑↓→ |
| SaaS subscriptions | $X | x% | ↑↓→ |
| Marketing / paid acquisition | $X | x% | ↑↓→ |
| Office / facilities | $X | x% | ↑↓→ |
| Professional services | $X | x% | ↑↓→ |
| Other | $X | x% | ↑↓→ |
| **Total gross burn** | **$Y** | **100%** | |

Flag any line growing >10% MoM and the top 3 categories.

## Phase 3: Default-alive vs. default-dead

Apply Paul Graham's framing:
- **Default alive**: at current growth, will revenue exceed expenses before cash runs out?
- **Default dead**: it won't — fundraise or cost cuts required

Compute:
- Revenue MoM growth (trailing 6 months, trimmed mean)
- Months until revenue ≥ gross burn at current growth
- Cumulative cash needed to reach break-even

Present the default-alive curve: cash balance over time at current growth.

## Phase 4: Scenario planning

Always build three scenarios:

**Base** — current plan, current sales productivity, current churn
**Conservative** — hiring frozen, sales productivity −20%, churn +25%, no new round
**Stretch** — hiring +30%, sales productivity +15%, new round closes in 4 months

Build the levers table:

| Lever | Cash impact / month | Runway extension | Strategic cost |
|-------|-------------------:|-----------------:|----------------|
| Freeze hiring | +$X | +Y months | Slows roadmap |
| Reduce paid marketing 50% | +$X | +Y months | New ARR −20% |
| 10% RIF | +$X | +Y months | Morale, severance |
| Defer planned hires 1Q | +$X | +Y months | Mild roadmap slip |
| Negotiate vendor deferral | +$X | +Y months | One-time |
| Draw on credit line | +$X | +Y months | Adds interest |

Stack levers by **return per unit of strategic damage** — layoffs are rarely the first move if other levers exist.

## Phase 5: 13-week rolling forecast

| Week | Beg cash | Collections | Disbursements | Net | End cash |
|------|---------:|------------:|--------------:|----:|---------:|
| W1   | $X | $X | $X | $X | $X |
| ...  | | | | | |
| W13  | $X | $X | $X | $X | $X |

Inputs: AR aging, AP aging, payroll calendar, tax estimates, insurance, lease.
Flag any week where end cash < 30 days of operating expense.

## Phase 6: Fundraise trigger calendar

| Runway remaining | Action |
|------------------|--------|
| 18+ months | No pressure; focus on growth metrics |
| 12–18 months | Prepare data room; soft talks with existing investors |
| 9–12 months | Active fundraise process |
| 6–9 months | Bridge / extension; activate cost cuts |
| <6 months | Survival mode; aggressive cuts; strategic alternatives |

Tie each trigger to a calendar date based on current burn.

## Output

- Cash position memo: balance, gross burn, net burn, runway
- Default-alive verdict with reasoning
- Three scenarios with quantified runway under each
- Recommended levers in priority order with $ and strategic-cost impact
- Fundraise calendar with trigger dates
- 13-week tactical forecast with liquidity warnings flagged
- 3–5 leading indicators that would shift the plan

## Operating rules

**Always**
- Separate gross burn from net burn
- Use trimmed-mean growth, not last-month
- Build all three scenarios
- Quantify each lever in dollars and strategic cost
- Set fundraise triggers as calendar dates
- Stress-test with lumpy payroll, tax, and insurance disbursements

**Never**
- Report runway as one number
- Assume revenue grows linearly from one good month
- Treat investor commitments as cash until wired
- Recommend layoffs before exhausting cheaper levers
- Mix restricted cash into runway
