---
name: "ecom-promo-roi"
description: "Calculate and analyze promotional ROI including incremental sales lift, margin impact, and promo type comparison. Use this skill when the user needs to evaluate whether a promotion was profitable, compare promotion types, simulate promo scenarios, or optimize promotional spending — even if they say 'was this sale worth it', 'which promo type works best', 'are we giving away too many discounts', or 'plan our next promotion'."
metadata:
  category: "WP-01 電商"
  tags: ["e-commerce", "promotion", "roi", "marketing"]
---

# Promotion ROI Analysis

## Framework

```
IRON LAW: Measure INCREMENTAL Sales, Not Total Sales During Promo

A promotion that generates $100K in revenue during a sale week looks great —
until you realize $80K would have happened anyway (baseline). The incremental
lift is only $20K. If the discount cost $25K in margin, the promo LOST money.

Promo ROI = (Incremental Revenue × Margin - Promo Cost) / Promo Cost
```

### Key Metrics

| Metric | Formula |
|--------|---------|
| **Incremental Revenue** | Promo period revenue - Baseline revenue (what would have happened without promo) |
| **Promo Cost** | Discount amount + marketing spend + operational cost |
| **Promo ROI** | (Incremental Gross Profit - Promo Cost) / Promo Cost |
| **Cannibalization Rate** | % of promo sales that would have occurred at full price |
| **Pull-Forward Rate** | % of promo sales that are just earlier purchases (customers would have bought next week anyway) |

### Promo Type Comparison

| Type | Mechanism | Pros | Cons |
|------|-----------|------|------|
| % Discount | 20% off everything | Simple, high traffic | Erodes brand, trains discount-waiting |
| $ Off | NT$200 off orders >NT$1000 | Drives AOV up | Less exciting for low-AOV customers |
| BOGO | Buy one get one free | Moves inventory fast | 50% margin hit, attracts deal-seekers |
| Gift with purchase | Free item with min spend | Protects price perception | Cost of gift, may not drive incremental |
| Flash sale | Time-limited deep discount | Urgency, high engagement | Operational stress, cannibalization |
| Loyalty points | Earn/redeem points | Builds retention, deferred cost | Complex to manage, redemption liability |

### Analysis Steps

**Phase 1: Establish Baseline**
- What would revenue have been without the promo? (prior period, prior year same period, or control group)
- Account for seasonality, day-of-week effects, and trend

**Phase 2: Calculate Incremental Impact**
- Total promo revenue - baseline = incremental
- Subtract cannibalization and pull-forward estimates
- Calculate gross profit on incremental (not revenue)

**Phase 3: Calculate Full Cost**
- Discount dollars given up
- Marketing spend (ads, email, creative production)
- Operational cost (warehouse overtime, customer service spike)

**Phase 4: Compute ROI and Decide**
- ROI > 0: Promo was profitable
- ROI < 0 but strategic (new customer acquisition, inventory clearance): May still be justified
- ROI < 0 with no strategic rationale: Don't repeat

## Output Format

```markdown
# Promo ROI Report: {Promotion Name}

## Promo Summary
- Type: {discount type}
- Period: {dates}
- Offer: {details}

## Results
| Metric | Value |
|--------|-------|
| Total Revenue (promo period) | ${X} |
| Baseline Revenue (estimated) | ${X} |
| **Incremental Revenue** | **${X}** |
| Incremental Gross Profit | ${X} |
| Promo Cost (discount + marketing + ops) | ${X} |
| **Promo ROI** | **{X%}** |

## Profitability Assessment
{Profitable / Unprofitable — with context}

## Recommendation
{Repeat / Modify / Discontinue — with rationale}
```

## Gotchas

- **Baseline estimation is the hardest part**: The accuracy of your ROI depends on how well you estimate what would have happened without the promo. Use prior year same period as a starting point, adjust for trend.
- **Post-promo dip is real**: Sales often drop BELOW baseline after a promotion (customers pulled purchases forward). Include the dip period in your analysis.
- **Discounts are addictive**: Customers learn to wait for sales. Track the % of revenue sold at full price over time — if it's declining, you have a discount dependency problem.
- **New vs existing customer mix matters**: A promo that acquires 500 new customers at negative ROI may be worth it if their LTV justifies the acquisition cost. Track separately.

## References

- For A/B testing promotional offers, see `references/promo-testing.md`
