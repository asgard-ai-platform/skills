---
name: "tw-ecom-compliance-pdpa"
description: "E-commerce-specific PDPA (個資法) compliance — member consent at signup, cookie consent, order / payment data retention, DSAR (data subject access request) handling, and cross-border data transfer for TW merchants. Use when building a TW e-commerce signup / CRM flow, responding to member data requests, or auditing cookies. For generic PDPA / GDPR basics see `law-gdpr-pdpa`. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "compliance"
  related_mcps: []
  related_skills: ["law-gdpr-pdpa", "tw-ecom-compliance-consumer", "tw-ecom-operations-line-oa"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "compliance", "pdpa", "privacy"]
---

# E-Commerce PDPA Compliance

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Designing member signup consent for a TW store
- Building cookie-consent banner for TW traffic
- Responding to DSAR (resident data subject access request)
- Designing data-retention policy for order / payment data
- Cross-border transfer (TW → AWS US / GCP APAC)

## Do NOT use when

- Generic PDPA / GDPR concepts → `law-gdpr-pdpa`
- Marketing consent for LINE OA → `tw-ecom-operations-line-oa`

## Core concepts

TODO: 個資法 §5 specific-purpose principle, 第八條 告知義務, 蒐集 vs 處理 vs 利用 split.

## Decision tree

TODO: data flow → consent form design.

## Implementation guidance

TODO: consent form template, DSAR SOP, retention schedule, cross-border transfer assessment.

## Gotchas

TODO: 5-6 pitfalls (opt-in vs opt-out confusion, third-party embed leakage, employee access logging, data-breach 72hr notification).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `law-gdpr-pdpa`
- `tw-ecom-operations-line-oa`

_Last verified: 2026-04_
