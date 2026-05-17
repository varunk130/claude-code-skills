---
name: ai-agent-financial-analyst
description: "SaaS financial modeling engine that generates unit economics models, feature ROI calculators, pricing scenario analyses, TAM/SAM/SOM sizing, build-vs-buy comparisons, and revenue projections from natural language inputs. Use when building business cases, calculating LTV/CAC/payback, modeling pricing changes, estimating feature revenue impact, running sensitivity analyses, or preparing financial justifications for product investments. Produces actual calculations with explicit assumptions and sensitivity ranges."
---

# SaaS Finance Lab — Financial Modeling for Product Managers

Turns natural language product questions into rigorous financial models with explicit assumptions, sensitivity analysis, and decision-ready output.

## STEP 1: Input Gathering

Before building any model, extract or request these inputs. Use SaaS defaults when PM doesn't have exact numbers.

**Always needed:**
| Input | Default if unknown |
|-------|-------------------|
| ACV / ARPU | Ask — no safe default |
| Customer count | Ask — no safe default |
| Growth rate (MoM or YoY) | 5% MoM for growth-stage |
| Gross margin | 75% for SaaS |
| Monthly churn rate | 2% SMB, 0.5% enterprise |

**Critical rule:** State EVERY assumption explicitly. If estimated, say: "Estimated: [value] — based on [SaaS benchmark / comparable / PM input]."

## STEP 2: Model Selection

| PM asks... | Build this model |
|------------|------------------|
| "What's the ROI of building X?" | Feature ROI Model |
| "What's our LTV? CAC?" | Unit Economics Dashboard |
| "How should we price this?" | Pricing Scenario Analysis |
| "How big is this market?" | TAM/SAM/SOM Calculator |
| "Should we build or buy?" | Build vs. Buy Comparison |
| "Forecast revenue" | Revenue Projection Model |

## STEP 3: Build the Model

---

### MODEL 1: Unit Economics Dashboard

**Revenue Metrics:** MRR, ARR, ARPU (monthly), ACV

**Customer Health:** GRR, NRR, logo churn (monthly), revenue churn (monthly)

**Unit Economics:**
- LTV = ARPU x Gross Margin % / Monthly Churn Rate
- CAC = Total Sales & Marketing Spend / New Customers
- LTV:CAC ratio — Target > 3:1
- CAC payback = CAC / (ARPU x Gross Margin %) — Target < 18 months
- NRR = (Beginning MRR + Expansion - Contraction - Churn) / Beginning MRR x 100

**Health Check with traffic lights:**
- LTV:CAC: > 3:1 (good) | 1.5-3:1 (warning) | < 1.5:1 (critical)
- Payback: < 12mo (good) | 12-18mo (warning) | > 18mo (critical)
- NRR: > 120% (excellent) | 100-120% (good) | 90-100% (warning) | < 90% (critical)

---

### MODEL 2: Feature ROI Calculator

**Investment table:**
| Cost Component | One-time | Monthly Ongoing | 12-month Total |
|---------------|----------|-----------------|----------------|
| Engineering (engineers x weeks x $/week) | $ | — | $ |
| Design | $ | — | $ |
| Infrastructure | $ | $/mo | $ |
| Maintenance (20% of build cost/year) | — | $/mo | $ |
| **Total** | **$** | **$** | **$** |

**Return table:**
| Revenue Driver | Assumption | Monthly Impact | 12-mo Impact |
|---------------|-----------|----------------|-------------|
| New customers (conversion increase) | X% | $ | $ |
| Expansion (upgrades) | X% of base | $ | $ |
| Churn reduction | X% reduction | $ | $ |

**ROI calculation:** 12-mo investment, 12-mo revenue impact, net return, ROI %, payback period (months), NPV (3-year, 10% discount)

**Sensitivity:** Bear (50% of base assumptions), Base, Bull (150%) — show ROI and payback for each

**Decision:** "Ship if you believe [conditions]" / "Kill if [conditions]" / "De-risk by [validation approach]"

---

### MODEL 3: Pricing Scenario Analysis

- Current state: price, customers, MRR, conversion rate, competitor range
- 3 scenarios compared: price point, est. conversion impact, churn impact, projected customers/MRR/ARR at 12mo, LTV change
- Revenue crossover analysis: at what point does higher-price x fewer-customers beat lower-price x more-customers?
- Price elasticity estimate and revenue-maximizing price
- Recommendation with key driving assumption

---

### MODEL 4: TAM/SAM/SOM Calculator

Three independent approaches for triangulation:
1. **Top-down:** Industry size x relevant segment % → TAM → SAM → SOM
2. **Bottom-up:** # potential customers x reachable % x conversion x ACV → SOM
3. **Value-theory:** Total cost of problem x willingness-to-pay % x potential customers → TAM

Triangulate all three. Note convergence or divergence. Provide Year 1-3 growth trajectory.

---

### MODEL 5: Build vs. Buy

- 5-year TCO comparison (year 0-4) with NPV at 10% discount
- Hidden costs: opportunity cost of eng time, integration complexity, vendor lock-in, customization flexibility, time to value, talent dependency
- Strategic assessment: core competency test, speed to market, long-term flexibility, total cost
- Recommendation with conditions that would flip the answer

---

## STEP 4: Sensitivity Analysis (Required for Every Model)

Identify top 3 variables by impact. Show:

| Var A / Var B | -20% | Base | +20% |
|---------------|------|------|------|
| -20% | $ | $ | $ |
| Base | $ | **$** | $ |
| +20% | $ | $ | $ |

**Breakeven conditions:** "Recommendation holds as long as [Variable A] stays above [X]"

## STEP 5: Generate Files (When Requested)

- **Markdown tables:** Output directly in conversation
- **CSV:** Generate via Python script
- **Excel:** Use openpyxl with sheets for assumptions (editable), calculations (with formulas), sensitivity, and summary dashboard

## Output Standards

Every model MUST include:
1. Assumptions table with source for each (PM input / SaaS benchmark / estimated)
2. The model with clear calculations
3. Sensitivity analysis (minimum: bear/base/bull)
4. Decision language: "Worth doing if..." / "Kill if..."
5. Model limitations: what it does NOT account for

**Precision:** Revenue <$1M round to thousands ($247K). Revenue >$1M round to hundred-thousands ($1.2M). Percentages: one decimal for rates (2.3%), whole numbers for changes (+15%). Never show false precision.

**Tone:** Direct. Conservative on revenue, aggressive on costs. If numbers don't support the investment, say so plainly.
