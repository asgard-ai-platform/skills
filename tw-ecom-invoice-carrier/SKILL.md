---
name: "tw-ecom-invoice-carrier"
description: "Handle Taiwan e-invoice carriers (載具) — 手機條碼, 自然人憑證, 會員載具, plus 捐贈碼 donation flow. Covers carrier validation, scan-to-store UX, member-carrier consolidation, and prize-draw winner notification. Use when designing carrier scanning UX, debugging invalid-carrier rejections, or implementing donation-code flow. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "invoice"
  related_mcps: []
  related_skills: ["tw-einvoice-guide", "tw-ecom-invoice-ezpay"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-invoice", "carrier"]
---

# E-Invoice Carriers (載具)

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Designing carrier-scan UX at checkout
- Implementing member-carrier consolidation
- Adding 捐贈碼 donation flow
- Handling prize-draw (中獎) winner notification
- Debugging carrier-format rejections

## Do NOT use when

- Landscape overview → `tw-einvoice-guide`
- Specific 加值中心 API → `tw-ecom-invoice-ezpay` / `-universalec`

## Core concepts

TODO: carrier types, format specs, validation rules.

## Decision tree

TODO: which carrier to default to given context.

## Implementation guidance

TODO: scan widget, validation, member-carrier linking.

## Gotchas

TODO: 5-6 pitfalls.

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-einvoice-guide`

_Last verified: 2026-04_
