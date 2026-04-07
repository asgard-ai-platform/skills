---
name: "algo-price-elasticity"
description: "Calculate price elasticity of demand to quantify how price changes affect sales volume. Use this skill when the user needs to estimate demand sensitivity, set optimal prices, or evaluate the revenue impact of price changes — even if they say 'how sensitive are customers to price', 'will a price increase hurt sales', or 'elasticity calculation'."
metadata:
  category: "WP-39 定價演算法"
  tags: ["pricing", "elasticity", "demand-analysis", "economics"]
---

# Price Elasticity of Demand

## Overview

Price elasticity measures the percentage change in quantity demanded for a 1% change in price. Ed = %ΔQ / %ΔP. |Ed| > 1 = elastic (price-sensitive), |Ed| < 1 = inelastic (price-insensitive). Critical for pricing decisions and revenue optimization.

## When to Use

**Trigger conditions:**
- Estimating how a price change will affect unit sales and revenue
- Determining if demand is elastic or inelastic for a product
- Optimizing price for maximum revenue or profit

**When NOT to use:**
- When you need consumer willingness-to-pay distribution (use Van Westendorp or conjoint)
- When pricing multiple products together (use bundle pricing)

## Algorithm

```
IRON LAW: Elasticity Is NOT Constant Along a Linear Demand Curve
It varies at every price point. At high prices, demand is elastic
(small price increase → big volume drop). At low prices, demand is
inelastic. Always calculate at the SPECIFIC price point of interest.
Revenue-maximizing price is where Ed = -1 (unit elastic).
```

### Phase 1: Input Validation
Collect: price-quantity pairs over time (or across markets). Control for: seasonality, promotions, competitor actions, other confounders.
**Gate:** Minimum 10 price-quantity observations, confounders identified.

### Phase 2: Core Algorithm
**Point elasticity:** Ed = (dQ/dP) × (P/Q) at a specific price point
**Arc elasticity:** Ed = ((Q₂-Q₁)/((Q₂+Q₁)/2)) / ((P₂-P₁)/((P₂+P₁)/2)) between two points
**Regression method:** log(Q) = α + β×log(P) + controls → β is the elasticity (constant elasticity model)

### Phase 3: Verification
Check: sign should be negative (price up → quantity down). Cross-validate with holdout periods.
**Gate:** Elasticity is negative, confidence interval is reasonable.

### Phase 4: Output
Return elasticity estimate with revenue impact projection.

## Output Format

```json
{
  "elasticity": -1.5,
  "interpretation": "elastic — 1% price increase → 1.5% quantity decrease",
  "revenue_impact": {"price_change_pct": 10, "quantity_change_pct": -15, "revenue_change_pct": -6.5},
  "metadata": {"method": "log-log regression", "r_squared": 0.82, "observations": 52}
}
```

## Examples

### Sample I/O
**Input:** Price increased 10% from $100 to $110, quantity dropped from 1000 to 850
**Expected:** Arc elasticity = ((-150/925) / (10/105)) = -1.70 (elastic)

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Luxury good | May be positive (Veblen) | Higher price → higher perceived value |
| Necessity (insulin) | Near zero | Demand barely responds to price |
| Perfect substitute available | Very elastic (< -3) | Customers switch immediately |

## Gotchas

- **Omitted variable bias**: Without controlling for advertising, seasonality, and competitor prices, elasticity estimates are biased.
- **Short-run vs long-run**: Short-run elasticity is typically lower (customers are locked in). Long-run gives them time to find substitutes.
- **Cross-price elasticity**: Demand for product A may depend on product B's price. Ignoring this in a portfolio context leads to suboptimal pricing.
- **Asymmetric elasticity**: Consumers may react differently to price increases vs decreases. Don't assume symmetry.
- **Small sample noise**: With few observations, elasticity estimates have wide confidence intervals. Report intervals, not just point estimates.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/arc_elasticity.py` | Compute arc elasticity and revenue impact | `python scripts/arc_elasticity.py --help` |

Run `python scripts/arc_elasticity.py --verify` to execute built-in sanity tests.

## References

- For regression-based elasticity estimation, see `references/regression-estimation.md`
- For cross-price elasticity analysis, see `references/cross-price.md`
