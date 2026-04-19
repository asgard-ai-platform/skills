---
name: "tw-ecom-logistics-cross-border"
description: "Handle cross-border shipping FROM or TO Taiwan — customs (報關 / 海關), HS codes, de minimis thresholds, carrier choices (DHL / FedEx / UPS / 郵局 國際), and returns friction. Use when a TW business ships internationally or sells cross-border to TW. Do NOT use for domestic TW shipping. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "logistics"
  related_mcps: []
  related_skills: ["tw-ecom-compliance-cross-border", "xborder-logistics", "xborder-sea-entry"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "logistics", "cross-border"]
---

# Cross-Border Logistics

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Shipping from TW to overseas customers
- Importing to TW for cross-border e-commerce
- Handling 報關 / de minimis / HS codes
- Choosing among DHL / FedEx / UPS / 郵局 國際
- Managing returns from overseas

## Do NOT use when

- Domestic TW → `tw-ecom-logistics-home` / `-cvs`
- Pure tax / compliance → `tw-ecom-compliance-cross-border`

## Core concepts

TODO: de minimis threshold, HS code basics, duty vs VAT, DDP vs DDU.

## Decision tree

TODO: carrier by destination / weight / speed / DDP preference.

## Implementation guidance

TODO: customs doc prep, label generation, tracking reconciliation.

## Gotchas

TODO: 5-6 pitfalls (HS misclassification, DDP total cost shock, returns black hole, restricted-items list, FTZ vs general customs).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-compliance-cross-border`
- `xborder-logistics`, `xborder-sea-entry`

_Last verified: 2026-04_
