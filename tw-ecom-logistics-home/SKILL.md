---
name: "tw-ecom-logistics-home"
description: "Ship via Taiwan home delivery carriers — 黑貓宅急便, 宅配通, 新竹物流, 郵局. Use when setting up home delivery, choosing carriers by region / parcel size, integrating label printing, or handling redelivery. Do NOT use for CVS pickup (`tw-ecom-logistics-cvs`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "logistics"
  related_mcps: []
  related_skills: ["tw-ecom-logistics-cvs", "tw-ecom-logistics-cold-chain"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "logistics", "home-delivery"]
---

# Home Delivery Logistics (宅配)

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Choosing among 黑貓 / 宅配通 / 新竹物流 / 郵局 for home delivery
- Integrating label API / batch printing
- Handling redelivery (二次配) scheduling
- Outer-island (離島) surcharge handling
- Time-slot delivery options

## Do NOT use when

- CVS pickup → `tw-ecom-logistics-cvs`
- Cold-chain / frozen → `tw-ecom-logistics-cold-chain`

## Core concepts

TODO: carrier pricing by 材積 vs weight, regional coverage differences, SLA promises.

## Decision tree

TODO: carrier pick by region / weight / 時效.

## Implementation guidance

TODO: label API, batch upload, tracking webhook.

## Gotchas

TODO: 5-6 pitfalls (材積-based upcharge, 離島 surcharge opacity, tracking update lag, failed delivery handling, fragile-item insurance).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-logistics-cvs`

_Last verified: 2026-04_
