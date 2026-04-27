---
name: "tw-ecom-payment-ecpay"
description: "Integrate 綠界 (ECPay) for Taiwan e-commerce — credit card, ATM, CVS 代碼, 超商取貨付款, and CheckMacValue signature. Use when ECPay is the chosen PSP, setting up logistics-payment combined flows (超取+COD), computing or verifying CheckMacValue, or handling ECPay callbacks. Do NOT use for gateway selection or comparison (see tw-payment-integration). Do NOT use for non-ECPay providers. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: ["mcp-ecpay"]
  related_skills: ["tw-payment-integration", "tw-ecom-payment-newebpay", "tw-ecom-logistics-cvs"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "payment", "ecpay", "fintech"]
---

# ECPay (綠界) Integration

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Integrating ECPay for credit card / ATM / CVS 代碼 / 超商取貨付款
- Combining ECPay logistics + payment in one flow
- Computing / verifying CheckMacValue signatures
- Handling ECPay callback webhooks
- Reconciliation with ECPay merchant portal

## Do NOT use when

- Non-ECPay provider → specific skill for that provider
- Pure logistics (no payment) → `tw-ecom-logistics-cvs`

## Core concepts

TODO: ECPay positioning, CheckMacValue signature, the 超取+COD combined model.

## Decision tree

TODO: when ECPay's combined flow beats separating payment vs shipping.

## Implementation guidance

TODO: merchant setup, first txn, COD-at-pickup reconciliation.

## Gotchas

TODO: 5-6 pitfalls (CheckMacValue param ordering / URL encoding gotchas, COD settlement offset, 超取 failure refund flow, cross-sandbox credential leakage, 境外 card compatibility).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-payment-integration`
- `tw-ecom-logistics-cvs`

_Last verified: 2026-04_
