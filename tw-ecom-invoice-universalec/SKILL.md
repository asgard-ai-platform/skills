---
name: "tw-ecom-invoice-universalec"
description: "Issue Taiwan e-invoices via UniversalEC (汎宇電商) using mcp-universalec-e-invoice (27 tools). Use when a merchant uses UniversalEC as their 加值服務中心 instead of ezPay, or when migrating between centers. Do NOT use for ezPay flows (`tw-ecom-invoice-ezpay`) or MOF direct integration (`tw-einvoice-guide`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "invoice"
  related_mcps: ["mcp-universalec-e-invoice"]
  related_skills: ["tw-einvoice-guide", "tw-ecom-invoice-ezpay", "tw-ecom-invoice-carrier", "tw-ecom-invoice-void"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-invoice", "universalec", "tax-compliance"]
---

# UniversalEC (汎宇電商) E-Invoice Integration

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Merchant uses UniversalEC as 加值服務中心
- Migrating between ezPay and UniversalEC
- Using UniversalEC-specific features (27 tools — richer than ezPay's 7)
- Reconciling UniversalEC ↔ MOF platform

## Do NOT use when

- Using ezPay → `tw-ecom-invoice-ezpay`
- Direct MOF → `tw-einvoice-guide`

## Core concepts

TODO: UniversalEC market position, tool-set breadth.

## Decision tree

TODO: UniversalEC vs ezPay trade-offs.

## Implementation guidance

TODO: the 27 tool categories, common flows.

## Gotchas

TODO.

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-invoice-ezpay` (parallel skill)
- `tw-einvoice-guide`

_Last verified: 2026-04_
