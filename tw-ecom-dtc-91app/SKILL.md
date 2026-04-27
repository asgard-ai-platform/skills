---
name: "tw-ecom-dtc-91app"
description: "Integrate and operate 91APP in Taiwan e-commerce context via mcp-91app. Use when syncing orders/products/members on 91APP, running OMO (online-merge-offline) flows, integrating 91APP's app-first storefronts, or comparing 91APP vs Shopline/Shopify for mid-market DTC. Do NOT use for Shopline-specific integration (see tw-ecom-dtc-shopline). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: ["mcp-91app"]
  related_skills: ["tw-ecom-channel-strategy", "tw-ecom-dtc-shopline"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "91app", "platform", "integration"]
---

# 91APP Integration Methodology

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Integrating with 91APP via mcp-91app
- Running OMO (online-merge-offline) flows specific to 91APP
- Syncing member data between 91APP and CRM
- Debugging 91APP promotion / coupon flows
- Comparing 91APP vs Shopline for the mid-market DTC segment

## Do NOT use when

- You need generic platform selection guidance → use `tw-ecom-channel-strategy`
- You need 91APP API schema docs → consult mcp-91app README directly

## Core concepts

TODO: 91APP app-first positioning, OMO model, member-centric architecture.

## Decision tree

TODO: which mcp-91app tool for which task.

## Implementation guidance

TODO: order sync, member sync, promotion setup, inventory sync flows.

## Gotchas

TODO: 5-6 pitfalls (candidates: OMO state drift, promotion stacking rules, member merge across web/app, quota limits).

## IRON LAW

TODO: one non-obvious constraint.

## Output Format

TODO.

## Related

- `tw-ecom-channel-strategy`
- `tw-ecom-dtc-shopline` (methodology template)

_Last verified: 2026-04_
