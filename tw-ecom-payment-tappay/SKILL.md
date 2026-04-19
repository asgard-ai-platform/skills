---
name: "tw-ecom-payment-tappay"
description: "Integrate TapPay for Taiwan e-commerce — TapPay Web/iOS/Android SDK, 3DS 2.0 flow, Apple Pay / Google Pay / LINE Pay integration via TapPay, TCS (TapPay Card Service) for tokenized recurring payments. Use when TapPay is chosen as PSP, comparing TapPay vs NewebPay, or debugging 3DS flows. Do NOT use for other gateways. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: []
  related_skills: ["tw-payment-integration", "tw-ecom-payment-newebpay", "tw-ecom-payment-dispute"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "payment", "tappay", "fintech"]
---

# TapPay Integration for Taiwan E-Commerce

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Integrating TapPay Web/iOS/Android SDK
- Adding Apple Pay / Google Pay / LINE Pay via TapPay
- Implementing TCS (tokenized recurring payments)
- Debugging 3DS 2.0 flow issues on TapPay
- Comparing TapPay vs NewebPay / ECPay for a specific use case

## Do NOT use when

- Generic TW payment gateway selection → `tw-payment-integration`
- Non-TapPay provider → their specific skill

## Core concepts

TODO: TapPay positioning (mobile-first), TapPay Direct vs TapPay Pay by Prime, TCS flow.

## Decision tree

TODO: when TapPay outperforms NewebPay/ECPay.

## Implementation guidance

TODO: Prime token acquisition, 3DS handling, TCS card binding + charge.

## Gotchas

TODO: 5-6 pitfalls (Prime token TTL, 3DS interstitial UX, TCS unbind on card expiry, Apple Pay domain verification, sandbox-to-prod merchant switch).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-payment-integration` for gateway comparison
- `tw-ecom-payment-dispute` for refund / chargeback handling

_Last verified: 2026-04_
