---
name: "tw-ecom-logistics-cold-chain"
description: "Ship refrigerated / frozen products in Taiwan — 宅配通 宅配通冷藏 / 黑貓宅急便 低溫, cold-chain CVS pickup limitations, packaging (保冷劑 / 乾冰), and shelf-life SLA. Use for 生鮮 / 冷凍 / 冰品 / 藥品 delivery. Do NOT use for ambient-temperature shipping. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "logistics"
  related_mcps: []
  related_skills: ["tw-ecom-logistics-home", "tw-ecom-compliance-product"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "logistics", "cold-chain"]
---

# Cold-Chain Logistics

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Shipping 生鮮 / 冷凍 / 冰品 / 藥品 / 保健品
- Choosing 冷藏 vs 冷凍 service level
- Packaging spec: 保冷劑 vs 乾冰, insulation grade
- Handling delivery-failure shelf-life loss
- Regional service coverage (離島, 偏遠地區)

## Do NOT use when

- Ambient-temp goods → `tw-ecom-logistics-home` or `-cvs`
- Regulatory aspects of 食品 / 藥品 → `tw-ecom-compliance-product`

## Core concepts

TODO: 冷藏 (0-7°C) vs 冷凍 (-18°C), packaging physics, cost structure.

## Decision tree

TODO: cold-chain required? carrier choice? package spec?

## Implementation guidance

TODO: vendor onboarding, test shipments, insurance, loss SOP.

## Gotchas

TODO: 5-6 pitfalls (Friday / weekend hold risk, 離島 no cold service, CVS cold-chain capacity, insurance claim friction, 乾冰 export restriction).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-logistics-home`
- `tw-ecom-compliance-product`

_Last verified: 2026-04_
