---
name: "tw-ecom-logistics-cvs"
description: "Ship via Taiwan convenience store pickup (7-11 賣貨便 / 全家 / 萊爾富 / OK) — store selection API, shipping-label format, pickup SLA, COD reconciliation, return shipping. Use when setting up CVS 超取 on a TW store, choosing which chains to support, or debugging label printing. Do NOT use for home delivery or cross-border. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "logistics"
  related_mcps: ["mcp-ecpay-logistics"]
  related_skills: ["tw-ecom-logistics-home", "tw-ecom-payment-ecpay"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "logistics", "cvs", "super-pickup"]
---

# Convenience Store Pickup (超商取貨)

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Setting up CVS 超取 for a TW e-commerce store
- Choosing which chains to support (7-11 vs 全家 vs 萊爾富 vs OK)
- Integrating store-selection widget on checkout
- Handling COD (超取付款) reconciliation
- Managing CVS return flows

## Do NOT use when

- Home delivery (宅配) → `tw-ecom-logistics-home`
- Cross-border → `tw-ecom-logistics-cross-border`

## Core concepts

TODO: chain-specific quirks, 大宗 vs 一般 pickup, label formats, SLA.

## Decision tree

TODO: chain mix based on customer geo + avg order value.

## Implementation guidance

TODO: widget integration, label print, COD settlement, return flow.

## Gotchas

TODO: 5-6 pitfalls (label format divergence per chain, overweight rejection, address-to-store mismatch, COD settlement lag, store-closed edge case).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-payment-ecpay` (combined COD flow)

_Last verified: 2026-04_
