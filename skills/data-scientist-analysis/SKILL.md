---
name: data-scientist-analysis
description: Data analysis patterns, SQL best practices, and SaaS metrics conventions for product analytics
---

When performing data analysis:

## SQL Best Practices
- Use CTEs for readability over nested subqueries
- Apply proper filters early to reduce scan cost
- Use window functions for running totals, rankings, and comparisons
- Include indexing hints where applicable
- Comment complex logic and business assumptions

## SaaS Metrics Definitions
- **MRR/ARR**: Monthly/Annual recurring revenue, track expansion and contraction separately
- **NRR**: Net revenue retention = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR
- **GRR**: Gross revenue retention = (Starting MRR - Contraction - Churn) / Starting MRR
- **LTV**: Customer lifetime value = ARPU / Churn Rate
- **CAC**: Customer acquisition cost = Total Sales & Marketing Spend / New Customers
- **DAU/MAU ratio**: Daily active / Monthly active users as engagement proxy

## Analysis Standards
- Always state assumptions explicitly before presenting results
- Flag data quality issues proactively (nulls, outliers, gaps, duplicates)
- Provide confidence levels for recommendations
- Segment by cohort, plan type, and geography where relevant
- Calculate statistical significance for any A/B test interpretation (p-values, confidence intervals)
- Flag Simpson's paradox and selection bias risks

## Output Format
Every analysis must include:
1. **Question restated** — what we're actually answering
2. **Approach** — methodology and assumptions
3. **Key findings** — 3-5 bullets, most important first
4. **So what?** — what this means for product decisions
5. **Next steps** — what additional data would strengthen the conclusion

## Funnel & Cohort Conventions
- Report conversion rates between each stage, not just end-to-end
- Use weekly or monthly cohorts depending on volume
- Track retention at day 1, 7, 14, 30, 60, 90
- Separate new user funnels from returning user funnels
