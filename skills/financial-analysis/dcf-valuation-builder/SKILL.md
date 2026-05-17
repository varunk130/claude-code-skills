---
name: dcf-valuation-builder
description: "Builds a transparent discounted cash flow (DCF) valuation with 5–10 year forecast, terminal value, WACC derivation, sensitivity tables, and a football-field summary. Use when valuing a company, business unit, acquisition target, or capital project; pressure-testing an investment thesis; preparing a board valuation memo; or stress-testing assumptions against precedent transactions and trading comps."
---

# DCF Valuation Builder

> Defensible intrinsic-value modeling that holds up in an IC, audit committee, or M&A negotiation.

## What this skill is

A structured, auditable workflow that turns a set of financial assumptions into a discounted cash flow model with explicit reasoning at every step. It builds the revenue and operating model bottoms-up, derives WACC from first principles, reconciles two terminal-value methods, and triangulates the output against trading and transaction comps on a football field.

## What it solves

- Hand-waved valuations where the discount rate is hardcoded and the terminal value drives everything
- Single-point answers that hide enormous sensitivity to a few inputs
- Force-fitting a number to a target price with no traceability
- Forecasts disconnected from operating drivers (revenue, margin, capex, working capital)
- Inability to defend assumptions when an investment committee or board pushes back

## When to invoke

- Valuing a company, business unit, or M&A target for an internal memo
- Building a fairness opinion or board valuation pack
- Stress-testing a sell-side or banker model
- Comparing strategic investment options on an apples-to-apples NPV basis
- Re-underwriting an existing investment after material new information

## Phase 1: Scope & inputs

Before modeling, establish:
- Valuation date and fiscal-year convention
- Valuation purpose (M&A, fairness opinion, internal IRR hurdle, restructuring, tax)
- Currency and inflation assumptions
- Forecast horizon (5y default; 10y for long-cycle assets like infra, pharma, energy)
- Available data: 3–5y historicals, management forecast, comp set, recent transactions

Log every input source with file, date, and confidence (High / Med / Low).

## Phase 2: Revenue build (bottoms-up)

Pick the right driver tree:
- **SaaS / subscription**: net new ARR = (new logos × ACV) + (expansion − churn); revenue = beginning ARR + ½ × net new ARR
- **Transactional / marketplace**: GMV × take-rate
- **Volume × price**: units × ASP, broken by segment / geography
- **Consumption**: active users × ARPU × engagement

Always show three scenarios — Base, Bull (+1σ), Bear (−1σ) — with explicit CAGR for each.

## Phase 3: Operating model

Forecast each line as **% of revenue** with a credible glide path to terminal margins:

| Line item | Year 1 | Year 5 | Terminal | Convergence logic |
|-----------|--------|--------|----------|-------------------|
| Gross margin | X% | Y% | Z% | Mature peer benchmark |
| S&M | X% | Y% | Z% | LTV/CAC discipline |
| R&D | X% | Y% | Z% | Innovation intensity |
| G&A | X% | Y% | Z% | Operating leverage |
| EBIT margin | X% | Y% | Z% | Industry steady-state |

Build to unlevered free cash flow:

```
UFCF = EBIT × (1 − tax rate) + D&A − capex − Δ NWC
```

Validate that capex ≈ D&A at terminal year (steady-state requirement).

## Phase 4: WACC derivation

Show every input — never hardcode WACC.

| Component | Value | Source |
|-----------|-------|--------|
| Risk-free rate (10y) | x.xx% | Fed / Bloomberg |
| Equity risk premium | x.xx% | Damodaran / Duff & Phelps |
| Levered beta | x.xx | Comps, re-levered |
| Cost of equity (CAPM) | x.xx% | Rf + β × ERP |
| Pre-tax cost of debt | x.xx% | YTM or synthetic rating |
| After-tax cost of debt | x.xx% | × (1 − tax rate) |
| Target D/(D+E) | x.xx% | Industry-median |
| **WACC** | **x.xx%** | Weighted sum |

Add country risk premium and size premium where applicable.

## Phase 5: Terminal value

Use **both** methods and reconcile:

1. **Gordon growth**: TV = FCF(n+1) / (WACC − g) — with g ≤ long-run nominal GDP
2. **Exit multiple**: TV = terminal EBITDA × peer median EV/EBITDA

Show implied perpetuity growth from the exit multiple, and the implied exit multiple from the perpetuity. Flag unrealistic values (>5% g, >25× exit) and explain.

## Phase 6: Discount & bridge to equity

- Use mid-year convention unless cash flows are seasonal
- Discount each year's UFCF + TV to PV → **Enterprise Value**
- Bridge: Equity value = EV − debt − preferred − minority interest + cash + non-core
- Divide by diluted shares (treasury method) → implied share price

## Phase 7: Sensitivity & football field

Produce a 2-way sensitivity on the top drivers (typically WACC × g, or WACC × terminal margin):

|         | g = 1.5% | g = 2.0% | g = 2.5% | g = 3.0% |
|---------|---------:|---------:|---------:|---------:|
| WACC 8% | $xx | $xx | $xx | $xx |
| WACC 9% | $xx | $xx | $xx | $xx |
| WACC 10%| $xx | $xx | $xx | $xx |

Triangulate on a football field: trading comps, precedent transactions, 52-week range, LBO floor, sum-of-the-parts.

## Output

- One-page valuation memo with value range, midpoint, and recommended point estimate
- WACC build, terminal value reconciliation, and sensitivity table
- Football field with at least 3 cross-check methods
- Top 3 value drivers and top 3 risks (with downside cases quantified)
- Explicit list of "what would change the call"

## Operating rules

**Always**
- Show every formula; no black-box outputs
- Tie every assumption to a source or benchmark
- Reconcile both terminal value methods
- Stress-test with a downside case where IRR < WACC
- Present a range, never a single point

**Never**
- Force-fit a target valuation
- Use a discount rate without showing CAPM derivation
- Assume perpetuity growth above long-run GDP
- Skip the bridge from EV to equity value
- Confuse equity value with enterprise value
