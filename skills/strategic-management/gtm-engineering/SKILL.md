---
name: gtm-engineering
description: 'Designs the technical infrastructure that powers go-to-market — lead scoring models, CRM enrichment pipelines, lifecycle automation, attribution, and reverse ETL. Use when: gtm engineering, revops engineering, lead scoring, lead routing, CRM data pipeline, marketing automation architecture, attribution model, reverse ETL, customer data platform, growth engineering.'
---

# GTM Engineering

Designs the technical and data infrastructure that powers a modern go-to-market motion — the systems behind lead scoring, routing, enrichment, lifecycle automation, attribution, and the data flows between product, CRM, marketing automation, and the warehouse.

This is **not** GTM strategy (positioning, channels, messaging). This is the plumbing that makes GTM strategy actually executable at scale.

## When to Use This Skill
- Designing a lead scoring or PQL/MQL model
- Architecting CRM ↔ warehouse ↔ MAP data flows
- Building lifecycle automation (onboarding, expansion, churn-risk)
- Setting up multi-touch attribution
- Planning reverse ETL from warehouse to Salesforce/HubSpot/Marketo
- Auditing a broken or fragmented RevOps stack
- Standing up the GTM data layer for a new company or motion

## The Problem

Most GTM stacks are an accidental archaeology of point tools wired together with Zapier and hope. Lead scores don't reflect actual conversion data, attribution models contradict each other, sales reps work the wrong leads, and nobody can answer "what does a good lead actually look like?" The strategy doesn't fail — the execution layer does.

GTM Engineering is the discipline of treating the revenue stack like a product: with schemas, contracts, observability, and tested logic.

## What You'll Need

**Critical inputs (ask if not provided):**
- Sales motion (PLG, sales-led, hybrid, channel)
- Current stack (CRM, MAP, CDP, warehouse, product analytics)
- Definition of a "qualified" lead/account in this business
- Where data currently lives and where it's broken

**Nice-to-have inputs:**
- Conversion data by source/segment (last 4 quarters)
- Existing scoring rules
- SLA targets (lead routing time, enrichment latency)
- Data team capacity / tooling budget

## Process

### Step 1: Map the Current Data Topology
Inventory every system that produces or consumes GTM data. Identify the source of truth for accounts, contacts, opportunities, product usage, and intent signals. Flag duplicates, conflicts, and orphaned fields.

### Step 2: Define the Canonical Schema
Specify the unified account/contact/event model that downstream systems will conform to. Decide what lives in the warehouse vs. CRM vs. MAP and why.

### Step 3: Build the Lead/Account Scoring Model
Choose the model type appropriate to data volume:
- **Rules-based** — small data, high explainability
- **Logistic regression / gradient boosting** — sufficient labeled history
- **Two-model (fit × intent)** — separate ICP fit from buying intent

Validate against historical conversion data, not gut feel.

### Step 4: Design Routing & SLA Logic
Specify routing rules (round-robin, territory, account ownership, capacity-aware) and the SLA clock for each lead type. Define escalation paths when SLAs breach.

### Step 5: Architect Lifecycle Automation
Map the journeys (onboarding, activation, expansion, churn-risk, win-back). For each, specify trigger event, audience query, channel, exit criteria, and the metric it moves.

### Step 6: Specify the Attribution Model
Pick the model honestly: first-touch, last-touch, linear, time-decay, U-shaped, W-shaped, or data-driven (Markov / Shapley). Document its known biases. Plan for at least two parallel models so debate is data-grounded.

### Step 7: Define Reverse ETL & Sync Contracts
For every field synced from warehouse → operational tool, specify: source query, refresh cadence, conflict resolution, downstream consumer, and a backfill strategy.

### Step 8: Add Observability & Tests
Lead score drift, routing latency, enrichment hit rate, sync failures, dedupe collisions — all need monitoring. Treat the GTM stack like production infrastructure.

## What You'll Get

- Current-state data topology diagram
- Canonical account/contact/event schema
- Lead/account scoring model spec (with validation plan)
- Routing rules + SLA matrix
- Lifecycle journey specs (trigger → audience → channel → exit)
- Attribution model selection memo
- Reverse ETL sync contracts
- Observability checklist (metrics, alerts, owners)
- Phased rollout plan (what ships in 30 / 60 / 90 days)

## Framework Reference

**The GTM Data Stack — typical layers:**
- **Sources** — Product events, CRM, MAP, ads, billing, support, intent providers
- **Warehouse** — Snowflake / BigQuery / Databricks (the source of truth)
- **Modeling layer** — dbt / SQLMesh (canonical entities and metrics)
- **Activation** — Reverse ETL (Hightouch / Census) → CRM, MAP, ads, Slack
- **Operational tools** — Salesforce / HubSpot, Marketo / Customer.io, Outreach
- **Observability** — Monte Carlo / Sifflet / custom dbt tests

**Scoring model anti-patterns:**
- Scoring on activity (opens/clicks) instead of fit + intent
- One score that conflates fit and intent (ship two)
- Never re-validating against actual closed-won data
- Manual rule sprawl with no kill-switch for stale rules

**Attribution honesty checklist:**
- Does the model match the actual sales motion length?
- Are dark social / direct / brand-search captured anywhere?
- Are offline touches (events, AE outreach) ingested?
- Do marketing and sales agree on the model — or just tolerate it?

**Routing SLA defaults (starting point, tune to motion):**
- Inbound demo request: < 5 minutes to first touch
- High-fit PQL: < 1 hour
- MQL: < 24 hours
- Re-engagement: nurture, no SLA
