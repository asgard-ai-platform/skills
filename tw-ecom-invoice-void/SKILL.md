---
name: "tw-ecom-invoice-void"
description: "Void Taiwan e-invoices within the same bimonthly window, or issue allowances (折讓) for cross-period corrections. Use when handling returns / refunds that affect invoice state. Do NOT use for initial issuance — see the 加值中心-specific skills. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "invoice"
  related_mcps: []
  related_skills: ["tw-einvoice-guide", "tw-ecom-invoice-ezpay", "tw-ecom-payment-dispute"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-invoice", "void", "allowance"]
---

# Invoice Void & Allowance (作廢 / 折讓)

> **STATUS: SKELETON** — body pending.

## When to use this skill

- A return / refund occurs within same bimonthly → void
- A return / refund crosses bimonthly boundary → 折讓
- Debugging invoice state inconsistency post-refund
- Building void / allowance SOP

## Do NOT use when

- Initial issuance → issuance-layer skill
- Tax filing impact → `tw-tax-basics`

## Core concepts

TODO: void vs 折讓, bimonthly boundary, accounting implications.

## Decision tree

TODO: given refund date vs issuance date → void or 折讓.

## Implementation guidance

TODO: API calls, accounting entries, customer notification.

## Gotchas

TODO: 5-6 pitfalls (boundary off-by-one, 字軌 reservation, lottery invalidation, allowance numbering).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-invoice-ezpay`
- `tw-ecom-payment-dispute`

_Last verified: 2026-04_
