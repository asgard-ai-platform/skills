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
NOTE (填充時): 格式規格（手機條碼 `/` + 7 alphanumeric、自然人憑證 2 letters + 14 digits）
已在 `tw-ecom-invoice-ezpay` Gotchas 中詳細說明。此 skill 不重複格式規格；
改聚焦在 UX 層面：validation 在哪層做、錯誤訊息設計、掃碼元件選型。

## Decision tree

TODO: which carrier to default to given context (e.g., 有會員帳號 → 會員載具；無帳號 → 引導填手機條碼；B2B → 不需載具).

## Implementation guidance

TODO: scan widget 選型與整合、client-side validation 流程、member-carrier linking（會員帳號與手機條碼綁定）。
不重複 `issue_invoice` carrier_type / carrier_num 參數說明 — 那些在 ezpay/universalec skill。

## Gotchas

TODO: 5-6 pitfalls.

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-einvoice-guide`

_Last verified: 2026-04_
