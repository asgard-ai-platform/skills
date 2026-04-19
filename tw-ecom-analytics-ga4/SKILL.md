---
name: "tw-ecom-analytics-ga4"
description: "Implement GA4 for Taiwan e-commerce — Enhanced Ecommerce events (view_item, add_to_cart, begin_checkout, purchase), TW-specific parameter conventions (含稅 revenue, NT$ currency, 統編 as user property), Looker Studio reporting, and Big Query export. Use when instrumenting a TW store with GA4 or auditing existing GA4 setup. Do NOT use for generic analytics (use `ecom-analytics`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "analytics"
  related_mcps: []
  related_skills: ["ecom-analytics", "data-cohort-analysis", "tw-ecom-analytics-benchmarks"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "ga4", "analytics"]
---

# GA4 for Taiwan E-Commerce

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Instrumenting a TW store with GA4 Enhanced Ecommerce
- Auditing an existing GA4 setup for TW conventions
- Designing Looker Studio reports for TW KPI
- Setting up BigQuery export
- Attributing across LINE OA / marketplace channels

## Do NOT use when

- Generic analytics → `ecom-analytics`
- Benchmarks only → `tw-ecom-analytics-benchmarks`

## Core concepts

TODO: GA4 event model, 含稅 revenue handling, currency = TWD, content_group usage for 檔期.

## Decision tree

TODO: event → parameter mapping for TW conventions.

## Implementation guidance

TODO: dataLayer template, tag setup, consent mode, BigQuery export.

## Gotchas

TODO: 5-6 pitfalls (含稅 double-count, cross-domain marketplace attribution, LINE IAB tracking block, consent-mode revenue undercount, parameter cardinality limits).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `ecom-analytics`
- `tw-ecom-analytics-benchmarks`

_Last verified: 2026-04_
