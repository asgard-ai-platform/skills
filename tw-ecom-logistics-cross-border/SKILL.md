---
name: "tw-ecom-logistics-cross-border"
description: "Select carriers and manage cross-border shipping operations for Taiwan — carrier choices (DHL / FedEx / UPS / 郵局 國際), customs clearance operations (報關), DDP vs DDU trade-offs, label generation, and returns handling. Use when choosing a carrier, estimating shipping cost or transit time, or managing the physical movement of cross-border goods. Do NOT use for duty/tax calculation, HS-code classification, or 境外電商 tax registration (see tw-ecom-compliance-cross-border). Do NOT use for domestic TW shipping. STATUS: SKELETON — body pending."
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

- Choosing a carrier for TW → overseas or overseas → TW shipments
- Estimating shipping cost, transit time, or DDP total landed cost
- Managing customs clearance operations (報關) and document prep
- Handling returns from overseas buyers
- Comparing DHL / FedEx / UPS / 郵局 國際 for a given route

## Do NOT use when

- Duty/tax calculation, HS-code classification, or 報單 filing → `tw-ecom-compliance-cross-border`
- 境外電商 sales-tax registration → `tw-ecom-compliance-cross-border`
- Domestic TW logistics → `tw-ecom-logistics-home` / `tw-ecom-logistics-cvs`

## Core concepts

TODO: DDP vs DDU trade-offs (landed cost transparency, liability shift), carrier-choice framework (weight / speed / destination / DDP capability), customs document prep (商業發票、包裝明細、原產地證明), label standards per carrier, returns friction and cost structure. NOTE: HS-code classification, de minimis thresholds, and duty/VAT rates belong in `tw-ecom-compliance-cross-border` — do not duplicate here.

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
