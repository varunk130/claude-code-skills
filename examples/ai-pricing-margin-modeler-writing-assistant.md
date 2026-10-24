# Pricing and margin model for a business-to-business (B2B) Artificial Intelligence (AI) writing assistant

## Prompt

```text
Quillmark is our B2B AI writing assistant for marketing teams. We charge
$30 per seat per month, unlimited. Margin looks fine on average but finance
is nervous about heavy users and the new campaign agent. Should we stay per
seat, or move to usage-based or credits? Beta logs for 2,400 seats attached.
```

> Abridged output from the ai-pricing-margin-modeler skill. Company and figures are fictional.

---

## 1. Cost per successful task

Assumed model prices: input $3.00, output $15.00, cached input $0.30 per million tokens. Retrieval call $0.002. Per-request safety filtering and logging $0.001. Token counts are p50 values from beta logs.

```
Cost per attempt = tokens x price + calls x $0.002 + $0.001
Cost per successful task = Cost per attempt x (1 + retry rate) / success rate
Loaded cost = Cost per successful task x 1.25 (25% contingency, under 3 months of data)
```

| Task type | Input tokens | Output tokens | Cached tokens | Tool or retrieval calls | Retry rate | Success rate | Cost per attempt | Cost per successful task | Loaded (+25%) |
|-----------|-------------:|--------------:|--------------:|------------------------:|-----------:|-------------:|-----------------:|-------------------------:|--------------:|
| Short rewrite | 1,500 | 300 | 4,000 | 0 | 5% | 90% | $0.0112 | $0.0131 | $0.0163 |
| Long-form draft | 6,000 | 2,500 | 4,000 | 3 | 10% | 75% | $0.0637 | $0.0934 | $0.1168 |
| Document summary | 15,000 | 800 | 4,000 | 0 | 5% | 92% | $0.0592 | $0.0676 | $0.0845 |
| Grounded answer | 8,000 | 600 | 4,000 | 2 | 8% | 85% | $0.0392 | $0.0498 | $0.0623 |
| Campaign agent run | 60,000 | 9,000 | 20,000 | 12 | 20% | 70% | $0.3460 | $0.5931 | $0.7414 |

Worked check (long-form draft): 6,000 x $3/M = $0.0180, 2,500 x $15/M = $0.0375, 4,000 x $0.30/M = $0.0012, 3 calls = $0.0060, plus $0.0010 = $0.0637. Then $0.0637 x 1.10 / 0.75 = $0.0934.

The campaign agent run costs 45x a short rewrite. Any packaging that treats all tasks the same can be arbitraged.

## 2. Usage distribution (per seat per month)

Credits are weighted by loaded cost so 1 credit is about $0.0165 for every task type: rewrite 1, answer 4, summary 5, draft 7, agent run 45.

| Percentile | Tasks per month | Task mix (rewrite / draft / summary / answer / agent) | Credits | Monthly inference cost |
|------------|----------------:|--------------------------------------------------------|--------:|-----------------------:|
| Median (p50) | 153 | 120 / 8 / 10 / 15 / 0 | 286 | $4.67 |
| p75 | 337 | 250 / 20 / 25 / 40 / 2 | 765 | $12.50 |
| p90 | 695 | 500 / 45 / 50 / 90 / 10 | 1,875 | $30.66 |
| p99 | 1,780 | 1,200 / 120 / 150 / 250 / 60 | 6,490 | $106.33 |
| Max | 4,550 | 3,000 / 300 / 400 / 600 / 250 | 20,750 | $340.53 |

```
Concentration = top 10% of seats' share of inference cost = 56%
Average inference cost per seat = $14.95
```

Concentration is above 50 percent, so packaging must include limits, tiers, or a usage component.

## 3. Gross-margin floor

Other per-seat costs: platform hosting $1.20, support allocation $1.50, payment and marketplace fees 3 percent of revenue.

```
Gross margin = (Revenue - inference - $1.20 - $1.50 - 3% x Revenue) / Revenue
```

Agreed with finance: Quillmark is an AI-native application, so the **floor is 50 percent at p50 and p90** with a 60-75 percent blended target. p99 seats may not fall below the floor on any plan we ship.

## 4. Packaging comparison

Same distribution under each option. Cells show gross margin (revenue per seat).

| Model | How it charges | Margin at p50 | Margin at p90 | Margin at p99 | Blended | Buyer predictability | Risk |
|-------|---------------|--------------:|--------------:|--------------:|--------:|----------------------|------|
| Per seat (unlimited) | $30 per seat | 72.4% ($30) | -14.2% ($30) | -266.4% ($30) | 38.2% | High | Top 10% of seats destroy margin |
| Per seat with fair-use cap | $30; above 1,500 credits, route to small model (25% of cost) | 72.4% ($30) | 1.1% ($30) | -62.1% ($30) | 53.0% | High | Quality drop for best customers; still below floor |
| Usage-based | $0.06 per credit, $10 minimum | 54.0% ($17.16) | 67.3% ($112.50) | 69.0% ($389.40) | 65.2% | Low | Bill shock, slower team rollout |
| Credits | Prepaid at $0.05 per credit | 45.4% ($14.30) | 61.4% ($93.75) | 63.4% ($324.50) | 58.4% | Medium | p50 below floor; breakage disputes |
| **Hybrid** | **$29 per seat incl. 500 credits, overage $0.05 per credit** | **71.6% ($29)** | **62.9% ($97.75)** | **63.8% ($328.50)** | **66.9%** | **Medium-high** | **Needs clear meters** |
| Outcome-based | $0.10 per accepted output, any type | 48.8% ($15.30) | 49.0% ($69.50) | 35.7% ($178.00) | 41.8% | Medium | Agent runs cost $0.74 but bill $0.10 |

Outcome pricing check for the campaign agent alone:

```
Cost per billed outcome = $0.519 per attempt (incl. retries and contingency) x 1.43 attempts = $0.7414
Price per outcome >= $0.7414 / (1 - 0.50) = $1.48
```

A flat $0.10 per output fails this test by 15x. Outcome pricing only works with per-type rates, which turns it back into credits.

Hybrid floor check: the worst case inside the bundle is a seat that uses exactly 500 credits ($8.25 of inference), which still earns 59.2 percent.

## 5. Sensitivity (recommended hybrid plan)

| Scenario | Change | Margin at p90 | Blended | Gross margin impact (blended, percentage points) |
|----------|--------|--------------:|--------:|--------------------:|
| Baseline | - | 62.9% | 66.9% | - |
| Model price drop | Token prices cut 50% | 77.2% | 78.6% | +11.7 |
| Model upgrade | Better model at 2.5x per token | 19.9% | 31.8% | -35.1 |
| Usage growth | All usage doubles (p50 margin falls to 60.1%) | 63.6% | 64.6% | -2.3 |
| Agent adoption | p90 agent runs rise from 10 to 40 per month | 63.4% | - | +0.5 at p90 (p90 seat modeled only) |
| Routing | 60% of tasks to a smaller model at 20% of token cost | 76.6% | 78.1% | +11.2 |

Agent adoption is margin-neutral because credit rates track cost. The real threat is a model upgrade: offer it only on a premium tier with re-weighted credit rates.

**Prioritized cost levers:** (1) route rewrites and grounded answers to a smaller model, (2) cache the 4,000-token brand-voice prompt on every call (already assumed), (3) cap agent-run context at 60,000 tokens, (4) cap long-form output at 2,500 tokens by default, (5) batch overnight summaries.

## 6. Recommendation and guardrails

**Move to Hybrid:** $29 per seat per month, 500 credits per seat pooled across the workspace, overage $0.05 per credit. The p50 seat pays $1 less than today; the top 10 percent pay for what they use.

- **Grandfathering:** existing annual contracts keep $30 unlimited until renewal, maximum 12 months
- **Notice:** 60 days before the change for monthly plans; at renewal for annual
- **Usage visibility:** in-product meter per seat and per workspace; alerts at 50, 80, and 100 percent of pooled credits before overage applies
- **Spend caps:** admins set a monthly overage cap; default $500 per workspace
- **Margin trigger:** re-price or re-package if blended margin is below 50 percent for 2 consecutive months
- **Pass-through:** model price cuts are split, half to customers via higher credit bundles, half retained; decided before launch
- **Re-run:** after any model, provider, or routing change
