---
name: "ecom-inventory-health"
description: "Analyze inventory health using turnover ratios, ABC classification, safety stock calculations, and stockout vs overstock diagnostics. Use this skill when the user needs to optimize inventory levels, reduce carrying costs, prevent stockouts, or classify products by inventory priority — even if they say 'we have too much stock', 'we keep running out of bestsellers', 'how much safety stock do we need', or 'which products should we focus on'."
metadata:
  category: "WP-01 電商"
  tags: ["e-commerce", "inventory", "supply-chain", "abc-analysis"]
---

# Inventory Health Analysis

## Overview

Inventory health balances two risks: stockouts (lost sales, unhappy customers) and overstock (carrying costs, obsolescence). This skill provides tools to measure, classify, and optimize inventory levels.

## Framework

```
IRON LAW: Not All SKUs Deserve Equal Attention

ABC classification shows that ~20% of SKUs drive ~80% of revenue.
Treat A-items (top 20% revenue) with tight control and frequent review.
C-items (bottom 50% revenue) get simple rules and less attention.
Equal treatment of all SKUs wastes resources on low-impact items.
```

### Key Metrics

| Metric | Formula | Healthy Range |
|--------|---------|--------------|
| **Inventory Turnover** | COGS / Avg Inventory | 4-12x/year (industry-dependent) |
| **Days of Inventory (DOI)** | 365 / Inventory Turnover | 30-90 days |
| **Stockout Rate** | Stockout incidents / Total demand occasions | < 2-5% |
| **Fill Rate** | Orders filled completely / Total orders | > 95% |
| **Carrying Cost** | Avg Inventory × Carrying Cost % (typically 20-30%/year) | Minimize |
| **Dead Stock %** | Items with zero sales in 6+ months / Total SKUs | < 10% |

### ABC Classification

| Class | Revenue % | SKU % | Strategy |
|-------|----------|-------|----------|
| **A** | ~80% | ~20% | Tight control, frequent review, safety stock optimized |
| **B** | ~15% | ~30% | Moderate control, periodic review |
| **C** | ~5% | ~50% | Simple rules, min/max levels, consider dropping |

### Safety Stock Calculation

```
Safety Stock = Z × σ_d × √(Lead Time)

Where:
- Z = service level factor (1.65 for 95%, 2.33 for 99%)
- σ_d = standard deviation of daily demand
- Lead Time = supplier lead time in days
```

### Reorder Point

```
Reorder Point = (Average Daily Demand × Lead Time) + Safety Stock
```

### Diagnosis Steps

**Phase 1: Overall Health Check**
- Calculate turnover and DOI for total inventory
- Compare to industry benchmarks
- Identify trend: improving or deteriorating?

**Phase 2: ABC Classification**
- Rank all SKUs by revenue contribution
- Classify into A/B/C
- Check: are A-items well-stocked? Are C-items over-stocked?

**Phase 3: Problem Identification**
- **Overstock**: DOI > 90 days, dead stock > 10%, carrying costs rising
- **Stockout**: Fill rate < 95%, lost sales reports, customer complaints
- **Imbalance**: A-items understocked while C-items overstocked

**Phase 4: Optimization**
- Set safety stock by ABC class
- Implement reorder points for A-items
- Liquidate dead stock (discount, bundle, donate)
- Reduce lead times through supplier negotiation

## Output Format

```markdown
# Inventory Health Report: {Business}

## Summary
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Turnover | {X}x | {X}x | 🟢/🟡/🔴 |
| DOI | {X} days | {X} days | 🟢/🟡/🔴 |
| Fill Rate | {X%} | >95% | 🟢/🟡/🔴 |
| Dead Stock | {X%} | <10% | 🟢/🟡/🔴 |

## ABC Distribution
| Class | SKUs | Revenue % | Avg DOI | Issue |
|-------|------|----------|---------|-------|
| A | {N} | {%} | {days} | {stockout risk?} |
| B | {N} | {%} | {days} | ... |
| C | {N} | {%} | {days} | {overstock?} |

## Top Issues
1. {issue with specific SKUs and data}

## Recommendations
1. {action with expected impact}
```

## Gotchas

- **Seasonal products need separate treatment**: Swimsuits in January will show as "dead stock" but shouldn't be liquidated. Use seasonal adjustment or analyze by season.
- **Inventory turnover varies hugely by industry**: Grocery: 20-50x/year. Fashion: 4-6x. Electronics: 6-12x. Always benchmark within industry.
- **Low turnover ≠ bad if intentional**: Strategic inventory (buying ahead of price increases, securing supply) may justify lower turnover.
- **ABC classifications shift**: A product that was A-class last year may be C-class this year. Reclassify quarterly.
- **Carrying cost is often underestimated**: Include: warehouse rent, insurance, obsolescence, capital cost (opportunity cost of money tied up), handling labor. Total is typically 20-30% of inventory value per year.

## References

- For EOQ (Economic Order Quantity) model, see `references/eoq-model.md`
- For seasonal demand forecasting, see `references/seasonal-forecasting.md`
