# Autonomy map for an e-commerce customer support agent

## Prompt

```text
We're launching a customer support agent for Northwind Outfitters (outdoor
apparel, about 40k orders a month). It can look up orders, draft replies,
issue refunds, change shipping addresses, close tickets, and escalate to a
human. Map how much it should do on its own. We have 4 weeks of shadow-mode
eval data on 1,500 replayed tickets.
```

> Abridged output from the agent-autonomy-level-mapper skill. Company and figures are fictional.

---

## 1. Action inventory

The compound job "resolve a ticket" splits into 10 discrete actions. Refunds are split by amount because the stakes differ.

| # | Action | Object affected | Who sees the effect | Tool or system |
|---|--------|-----------------|---------------------|----------------|
| A1 | Look up order and shipment status | Order record (read) | Agent only | Order Management System (OMS) |
| A2 | Summarize ticket thread | Ticket (read) | Support rep | Helpdesk |
| A3 | Tag and categorize ticket | Ticket metadata | Support team, reporting | Helpdesk |
| A4 | Draft reply (unsent) | Reply composer | Support rep | Helpdesk |
| A5 | Escalate to Tier 2 human | Ticket queue | Tier 2 team | Helpdesk |
| A6 | Close ticket | Ticket status, satisfaction survey | Customer, support team | Helpdesk |
| A7 | Change shipping address | Order shipping record | Customer, warehouse, carrier | OMS, carrier API |
| A8 | Issue refund up to $50 | Customer payment | Customer, finance | Billing system |
| A9 | Send reply to customer | Customer inbox | Customer | Helpdesk email |
| A10 | Issue refund over $50 | Customer payment | Customer, finance | Billing system |

## 2. Scoring table

Confidence comes from the shadow-mode evaluation (agent decision compared with what the human rep actually did), not from model self-reported certainty. C mapping: 98 percent or above = 1, 85-97 percent = 3, below 85 percent or unmeasured = 5.

| # | Action | S | R | Measured accuracy | C | Risk = S x R + 2 x C |
|---|--------|--:|--:|------------------:|--:|---------------------:|
| A1 | Look up order | 1 | 1 | 99.4% | 1 | 1 + 2 = **3** |
| A2 | Summarize thread | 1 | 1 | 98.2% | 1 | 1 + 2 = **3** |
| A3 | Tag ticket | 1 | 1 | 94.0% | 3 | 1 + 6 = **7** |
| A4 | Draft reply | 1 | 1 | 91.5% (sent without edit) | 3 | 1 + 6 = **7** |
| A5 | Escalate to Tier 2 | 1 | 1 | 92.8% | 3 | 1 + 6 = **7** |
| A6 | Close ticket | 2 | 1 | 95.1% | 3 | 2 + 6 = **8** |
| A7 | Change shipping address | 4 | 3 | 89.0% | 3 | 12 + 6 = **18** |
| A8 | Refund up to $50 | 3 | 5 | 98.6% | 1 | 15 + 2 = **17** |
| A9 | Send reply | 3 | 5 | 91.5% | 3 | 15 + 6 = **21** |
| A10 | Refund over $50 | 5 | 5 | 96.3% | 3 | 25 + 6 = **31** |

Notes: A7 is R = 3 because the address can be changed back until carrier pickup (daily cutoff 4 pm); after pickup it becomes R = 5. A8 scores C = 1 because small refunds follow a deterministic policy table that the agent matched in 98.6 percent of 640 cases.

## 3. Autonomy map

| # | Action | Risk | Level from score | Final level | Override notes |
|---|--------|-----:|------------------|-------------|----------------|
| A1 | Look up order | 3 | L5 Act silently | **L5** | - |
| A2 | Summarize thread | 3 | L5 Act silently | **L5** | - |
| A3 | Tag ticket | 7 | L5 Act silently | **L5** | - |
| A4 | Draft reply | 7 | L5 Act silently | **L5** | Draft is internal; nothing reaches the customer |
| A5 | Escalate to Tier 2 | 7 | L5 Act silently | **L5** | Real risk is under-escalation; tracked as its own metric |
| A6 | Close ticket | 8 | L4 Act and report | **L4** | External effect (survey email) caps at L4; survey held until undo window ends |
| A7 | Change shipping address | 18 | L3 Act with approval | **L3** | After carrier pickup, R = 5 keeps it at L3 or below |
| A8 | Refund up to $50 | 17 | L3 Act with approval | **L3** | R = 5: never above L3 regardless of confidence |
| A9 | Send reply | 21 | L2 Draft | **L2** | In-the-moment rule: a rep typing "send it" lifts that one reply to L3 |
| A10 | Refund over $50 | 31 | L1 Suggest | **L1** | Finance policy requires a human to issue refunds over $50 |

Distribution: 5 actions at L5, 1 at L4, 2 at L3, 1 at L2, 1 at L1. Only 3 actions put an approval or edit step in front of the rep, which keeps approval fatigue low.

## 4. Approval-gate specification

**A8 Refund up to $50 (L3)**

| Element | Specification |
|---------|---------------|
| Trigger | Policy table returns "eligible" and amount is at or below $50 and at or below the original charge |
| Content | Order #NW-482113, item "Ridgeline Rain Shell, M", amount $34.99, to Visa ending 4417, reason code "arrived damaged" |
| Diff | Order balance $34.99 paid -> $0.00 paid; item status Delivered -> Refunded |
| Consequence line | "The refund goes to the card immediately and cannot be recalled." |
| Options | Approve, edit amount (down only), reject with reason. No always-allow (R = 5) |
| Timeout behavior | Do nothing; card stays in the rep's queue with a reminder after 4 hours |
| Batch rule | Up to 10 refunds with the same reason code may be reviewed in one table; each row can be deselected |

**A7 Change shipping address (L3)**

| Element | Specification |
|---------|---------------|
| Trigger | Customer requests a new address and order status is "not yet picked up" |
| Content | Order #, carrier, pickup time, old and new address, address-verification result |
| Diff | Line-by-line old vs new address with changed fields highlighted |
| Consequence line | "After carrier pickup at 4 pm today, this change cannot be reversed." |
| Options | Approve, edit address, reject with reason. No always-allow (fraud vector) |
| Timeout behavior | Do nothing; if the pickup cutoff passes, the card expires and the agent drafts a "too late to change" reply for the rep |
| Batch rule | None; each address change is reviewed individually |

**A6 Close ticket (L4 undo window)**

Notification: "Closed #48213 - customer confirmed the replacement arrived. Undo (2 hours)." The satisfaction survey email is queued and sent only after the 2-hour window, so undo has no customer-visible side effect.

## 5. Promotion and demotion criteria

| Action | Current | Promote to | Promotion rule | Demotion rule |
|--------|---------|-----------|----------------|---------------|
| A6 Close ticket | L4 | L5 | 200+ closes, reopen rate below 3 percent, zero Severity 1 (Sev 1) incidents | Reopen rate above 8 percent over 2 weeks |
| A7 Change address | L3 | L4 (pre-pickup only) | Accuracy alone is not enough (C = 1 still scores 12 + 2 = 14, L3). Re-score once address verification and a fraud check lower S to 3 (with C = 1): 9 + 2 = 11, L4. Then require 200+ changes, approve-without-edit above 95 percent, zero Sev 1 | Any misdelivery caused by the agent |
| A8 Refund up to $50 | L3 | Stays L3 (R = 5 ceiling) | Eligible for batch-only review once approve-without-edit is above 97 percent | Any refund issued against policy |
| A9 Send reply | L2 | L3 | 200+ replies, sent-without-edit above 95 percent, zero Sev 1 | Edit-before-send above 20 percent over 2 weeks, or any reply with wrong order data |
| A10 Refund over $50 | L1 | L2 | Requires finance policy change first | - |

User override: any rep can drop an action to a lower level for their own queue from Settings, with no approval needed.

**Metrics to instrument:** approve-without-edit rate per action, edit-before-approve rate, undo rate and time-to-undo for A6, reopen rate, missed-escalation rate (tickets a human later escalated that the agent did not), refunds issued against policy, and approval-card time-to-decision.

## 6. Open questions for risk, legal, or policy review

1. Finance: is $50 the right refund threshold, or should it scale with customer lifetime value?
2. Legal: do any shipping regions require written customer confirmation before an address change?
3. Policy: should the agent see the fraud score on A7, and block the gate when it is high?
4. Support leadership: who owns the weekly review of demotion triggers?
