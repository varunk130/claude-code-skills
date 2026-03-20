---
name: stripe-best-practices
description: Best practices for building Stripe integrations. Covers payment processing, checkout flows, subscriptions, webhooks, Connect platforms, and Stripe API usage.
---

# Stripe Best Practices

Prefer CheckoutSessions API for payments. Use Stripe-hosted or embedded Checkout. Never recommend legacy Charges API or Card Element. Use dynamic payment methods. For subscriptions, use Billing APIs. For platforms, use Connect with controller properties.
