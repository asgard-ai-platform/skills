---
name: "tw-ecom-dtc-shopify-localization"
description: "Run Shopify stores for Taiwan market — localization (NT$ pricing, Traditional Chinese, TW address format), payment apps (ECPay / NewebPay / TapPay Shopify apps), shipping apps (CVS / 黑貓), and e-invoice integration. Use when setting up Shopify for TW, choosing TW payment/shipping apps, or adapting a global Shopify theme for TW. Do NOT use for general (non-TW) Shopify dev. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: []
  related_skills: ["tw-ecom-channel-strategy", "tw-ecom-payment-newebpay", "tw-ecom-logistics-cvs", "tw-ecom-invoice-ezpay"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "shopify", "localization"]
---

# Shopify for Taiwan

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Setting up a new Shopify store targeting Taiwan customers
- Adding TW-specific payment apps (ECPay, NewebPay, TapPay) to Shopify
- Adding TW-specific shipping apps (CVS 7-11/全家, 黑貓)
- Integrating e-invoice issuance with Shopify order events
- Adapting a global theme for Traditional Chinese + NT$ pricing

## Do NOT use when

- Non-Taiwan Shopify work → use generic Shopify docs
- Shopline/91APP platform work → use their specific skills

## Core concepts

TODO: Shopify market/region config, app-based extension model (TW via marketplace apps, not native), why no official mcp-shopify yet for TW context.

## Decision tree

TODO: when Shopify beats Shopline/91APP for TW (brand-led international expansion, heavy theme customization need).

## Implementation guidance

TODO: app selection, localization checklist, e-invoice hook.

## Gotchas

TODO: 5-6 pitfalls (theme i18n gaps, app double-charging, payment app settlement differences, CVS shipping quirks).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-channel-strategy`
- `tw-ecom-payment-newebpay`
- `tw-ecom-logistics-cvs`

_Last verified: 2026-04_
