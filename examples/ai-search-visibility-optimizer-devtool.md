# Artificial Intelligence (AI) search visibility audit for a developer observability tool

## Prompt

```text
Tracelight is our observability platform for developers (logs, metrics, and
traces, OpenTelemetry-native). Sales keeps hearing "the AI told me to look at
Kestrel APM." Audit how we show up in AI assistant answers versus Kestrel APM,
Driftwatch, and Signalyard, and give me a fix plan.
```

> Abridged output from the ai-search-visibility-optimizer skill. Company and figures are fictional.

All measurements below are **illustrative**: they show the shape of a real Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO) audit, not actual assistant behavior. Kestrel APM (Application Performance Monitoring), Driftwatch, and Signalyard are fictional competitors.

---

## 1. Query set (v1.0, frozen)

40 prompts across 5 intent tiers, 4 persona variants (platform engineer, Site Reliability Engineering (SRE) lead, startup Chief Technology Officer (CTO), engineering manager at a 200-person company).

| Intent tier | Example prompt | Prompts | Weight | Weighted total |
|-------------|----------------|--------:|-------:|---------------:|
| Category discovery | "Best observability tools for a 50-engineer startup on Kubernetes" | 12 | 3 | 36 |
| Comparison | "Tracelight vs Kestrel APM for OpenTelemetry traces" | 8 | 3 | 24 |
| Problem-led | "How do I cut log ingestion costs without losing trace context" | 10 | 2 | 20 |
| Alternatives | "Alternatives to Kestrel APM that are cheaper at scale" | 6 | 2 | 12 |
| Branded fact | "How does Tracelight price ingestion" | 4 | 1 | 4 |
| **Total** | | **40** | | **96** |

**Run conditions:** 13-17 October 2026, United States, English, logged-in where required. ChatGPT (default model, search on), Claude (web search on), Perplexity (default mode), Google AI Overviews (logged out). 3 runs per prompt per engine = 480 responses. AI Overviews did not trigger on 6 prompts; those runs are scored 0 and flagged.

**Control set:** 8 problem-led prompts about alerting and on-call that no fix below targets. They separate our impact from engine drift.

## 2. Share-of-answer scorecard

```
Share of answer (SoA) = sum(score x intent weight) / (3 x sum(intent weight)) across runs
Max per engine = 3 x 96 x 3 runs = 864 weighted points
```

| Engine | Category discovery (avg score) | Comparison | Problem-led | Alternatives | Branded fact | SoA | Mention rate |
|--------|-----:|-----:|-----:|-----:|-----:|----:|-------------:|
| ChatGPT | 0.5 | 1.6 | 0.9 | 0.4 | 2.5 | 31.0% | 62/120 (51.7%) |
| Claude | 0.7 | 1.8 | 1.2 | 0.6 | 2.6 | 38.2% | 72/120 (60.0%) |
| Perplexity | 1.1 | 2.0 | 1.4 | 0.9 | 2.8 | 47.8% | 84/120 (70.0%) |
| Google AI Overviews | 0.3 | 1.2 | 0.6 | 0.2 | 2.2 | 21.8% | 47/120 (39.2%) |
| **All engines** | 0.65 | 1.65 | 1.02 | 0.53 | 2.52 | **34.7%** | 265/480 (55.2%) |

Worked check (ChatGPT): (12 x 3 x 0.5 + 8 x 3 x 1.6 + 10 x 2 x 0.9 + 6 x 2 x 0.4 + 4 x 1 x 2.5) / (3 x 96) = (18 + 38.4 + 18 + 4.8 + 10) / 288 = 89.2 / 288 = 31.0%.

**SoA by intent tier versus competitors (all engines, same query set):**

| Brand | Category discovery | Comparison | Problem-led | Alternatives | Branded fact | Overall SoA |
|-------|-------------------:|-----------:|------------:|-------------:|-------------:|------------:|
| Kestrel APM | 80.0% | 76.7% | 66.7% | 60.0% | 90.0% | 74.3% |
| Driftwatch | 63.3% | 66.7% | 53.3% | 73.3% | 86.7% | 64.3% |
| Signalyard | 40.0% | 46.7% | 50.0% | 30.0% | 80.0% | 44.2% |
| **Tracelight** | **21.7%** | **55.0%** | **34.2%** | **17.5%** | **84.2%** | **34.7%** |

The gap is in category discovery and alternatives, where shortlists form. Branded-fact scores look healthy but carry the most accuracy problems.

## 3. Accuracy log

Of 265 mentions: 211 accurate, 31 outdated, 18 wrong, 5 negative.

| Statement in answers | Flag | Runs | Likely source | Correct fact |
|----------------------|------|-----:|---------------|--------------|
| "Tracelight is a log management tool" | Outdated | 24 | Directory profile, 2024 blog posts | Logs, metrics, and traces since v3 (March 2025) |
| "Priced at $15 per host per month" | Wrong | 11 | Cached third-party pricing roundup | $0.25 per GB ingested, 50 GB free per month |
| "No native OpenTelemetry support" | Wrong | 7 | Old forum thread | OpenTelemetry-native since v3 |
| "Self-hosted only" | Outdated | 7 | Old docs page still indexed | Cloud and self-hosted |
| "Hard to set up at scale" | Negative | 5 | One developer-forum thread | Partly valid; addressed in v3.4 Helm chart |

## 4. Citation-source map (top 10 cited domains)

1,140 citations logged from engines that show sources. Domains are placeholders.

| Rank | Domain | Source type | Citations | Tracelight presence | Competitor presence | Gap action |
|-----:|--------|-------------|----------:|---------------------|---------------------|------------|
| 1 | devops-weekly.example | Editorial | 118 | Absent from "best tools" listicle | Kestrel, Driftwatch | Outreach with cost benchmark data |
| 2 | stackreviews.example | Review | 104 | 14 reviews, 3.9 rating | Kestrel 410 reviews | Review drive with verified customers |
| 3 | devforum.example | Community | 96 | 3 threads | 40+ threads | Engineers answer real questions, disclosed |
| 4 | docs.tracelight.example | Owned | 71 | Present | - | Answer-first blocks, freshness dates |
| 5 | kestrelapm.example | Competitor owned | 66 | Framed as "logs-only" | - | Publish honest comparison page |
| 6 | opensource-wiki.example | Reference | 58 | No entry | Kestrel, Signalyard | Neutral factual entry if notability is met |
| 7 | tracelight.example/pricing | Owned | 41 | Present, price behind a script | - | Static pricing table |
| 8 | cloudnative-news.example | Editorial | 39 | 1 mention (2024) | Driftwatch | Pitch OpenTelemetry migration data |
| 9 | tooldirectory.example | Directory | 33 | Profile says "log management" | Complete profiles | Update category and pricing |
| 10 | repo-discussions.example | Community | 30 | Active | Active | Maintain |

## 5. Entity-consistency check

| Fact | Canonical value | Site | Docs | Review profiles | Social bios | Structured data |
|------|-----------------|------|------|-----------------|-------------|-----------------|
| Category label | Observability platform | OK | OK | **Conflict: "log management"** | **Conflict: "logging"** | **Missing** |
| One-line description | OpenTelemetry-native logs, metrics, traces | OK | OK | **Conflict: logs only** | OK | **Missing** |
| Pricing model and starting price | $0.25 per GB, 50 GB free | OK (script-rendered) | **Conflict: per host (old page)** | **Conflict: $15 per host** | n/a | **Missing** |
| Primary integrations | OpenTelemetry, Kubernetes, Prometheus | OK | OK | **Missing OpenTelemetry** | OK | **Missing** |
| Target segment | Platform teams, 50-500 engineers | OK | n/a | OK | **Conflict: "startups"** | **Missing** |

Add Organization, Product, and FAQ (frequently asked questions) schema.org markup to the home, pricing, and comparison pages.

## 6. Priority page scores (1-5)

| Page | Direct answer | Verifiable facts | Freshness date | Comparison coverage | Crawlability | Total /25 |
|------|-----:|-----:|-----:|-----:|-----:|-----:|
| Pricing | 2 | 4 | 1 | 1 | 1 | 9 |
| Home | 2 | 2 | 1 | 1 | 4 | 10 |
| Docs: OpenTelemetry setup | 4 | 5 | 3 | 1 | 5 | 18 |
| Blog: "Cutting log costs" | 3 | 3 | 2 | 2 | 5 | 15 |

## 7. Prioritized fix backlog

| Fix | Intent tier affected | Expected SoA lift (L/M/H) | Effort (L/M/H) | Owner | Re-test date |
|-----|----------------------|---------------------------|----------------|-------|--------------|
| Correct category and pricing on review and directory profiles; remove old per-host docs page | Branded fact, Category discovery | H | L | Product marketing | 8 Dec 2026 |
| Static pricing table with date stamp and FAQ markup | Branded fact | M | L | Web team | 8 Dec 2026 |
| Honest comparison pages vs Kestrel APM and Driftwatch, including where we do not fit | Comparison, Alternatives | H | M | Product marketing | 8 Dec 2026 |
| Publish an ingestion-cost benchmark others can cite; pitch to the top 2 editorial sources | Category discovery, Problem-led | H | H | Developer relations | 19 Jan 2027 |
| Verified-customer review drive (no incentives tied to rating) | Category discovery | M | M | Customer success | 19 Jan 2027 |
| Disclosed engineer answers on devforum.example | Problem-led | M | M | Developer relations | 19 Jan 2027 |

Re-run query set v1.0 and the control set every 6 weeks. If the control set moves as much as the targeted prompts, attribute the change to engine drift, not to these fixes. No fix here guarantees inclusion in any assistant's answers.
