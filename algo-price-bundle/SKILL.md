---
name: "algo-price-bundle"
description: "Design bundle pricing strategies using pure bundling, mixed bundling, and consumer surplus analysis. Use this skill when the user needs to set prices for product bundles, determine whether bundling increases profit, or analyze unbundling opportunities — even if they say 'should we bundle these products', 'bundle pricing', or 'package deal pricing'."
metadata:
  category: "WP-39 定價演算法"
  tags: ["pricing", "bundling", "consumer-surplus", "product-strategy"]
---

# Bundle Pricing Strategy

## Overview

Bundle pricing sells multiple products together at a combined price, extracting consumer surplus by averaging valuations across products. Works when customers have heterogeneous, negatively correlated valuations. Three types: pure bundling (bundle only), mixed bundling (bundle + individual), unbundling.

## When to Use

**Trigger conditions:**
- Deciding whether to bundle products/services together
- Setting bundle price relative to individual prices
- Analyzing whether a current bundle should be unbundled

**When NOT to use:**
- When products have independent demand with no valuation correlation (bundling adds no value)
- When regulations prohibit tying arrangements

## Algorithm

```
IRON LAW: Bundling Increases Profit ONLY With NEGATIVELY CORRELATED Valuations
If ALL customers value the same items highly, bundling adds no surplus.
Bundling works when: Customer A values Product 1 high + Product 2 low,
while Customer B values Product 1 low + Product 2 high. The bundle
price captures both at a middle price neither would pay for their
low-value item alone.
```

### Phase 1: Input Validation
Collect: individual product valuations (or willingness to pay) per customer segment. Compute correlation of valuations across products.
**Gate:** Valuation data available, correlation is negative or mixed.

### Phase 2: Core Algorithm
1. Compute optimal individual prices: maximize Σ(revenue per product)
2. Compute optimal bundle price: find price that maximizes bundle revenue given joint valuation distribution
3. Compare: pure bundling revenue, mixed bundling revenue, individual pricing revenue
4. Mixed bundling: set bundle price < sum of individual prices; discount = bundle incentive

### Phase 3: Verification
Check: mixed bundling should weakly dominate both pure bundling and individual pricing (Adams & Yellen, 1976). If not, review valuation assumptions.
**Gate:** Mixed bundling profit ≥ max(pure bundling, individual pricing).

### Phase 4: Output
Return optimal pricing strategy with profit projections.

## Output Format

```json
{
  "recommendation": "mixed_bundling",
  "prices": {"product_a": 299, "product_b": 199, "bundle_ab": 399},
  "profit_comparison": {"individual": 45000, "pure_bundle": 48000, "mixed_bundle": 52000},
  "metadata": {"segments": 3, "valuation_correlation": -0.35}
}
```

## Examples

### Sample I/O
**Input:** Product A (WTP: Seg1=$80, Seg2=$30), Product B (WTP: Seg1=$30, Seg2=$70). Each segment has 100 customers.
**Expected:** Individual optimal: A=$80, B=$70, revenue=$15K. Bundle at $100: both segments buy, revenue=$20K. Bundling wins.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Perfectly positive correlation | Individual pricing wins | All customers value both high or both low |
| One product is free good | Bundle = premium + free | Common in software (free trial + paid add-on) |
| 10+ products in bundle | Mixed bundling complex | Too many combinations — use tiered bundles |

## Gotchas

- **Cannibalization**: The bundle may cannibalize high-WTP customers who would have bought individually at higher total. Mixed bundling mitigates this.
- **Perceived value**: Bundle discount must be salient. A $499 bundle of $299+$299 products (16% off) is better perceived than $499 for two $260 products.
- **Marginal cost matters**: Zero marginal cost products (software, digital) benefit most from bundling. Physical goods with high COGS have tighter margins.
- **Complexity cost**: Too many bundle options create choice paralysis. Limit to 2-3 bundle tiers.
- **Regulatory tying**: In some markets, forcing purchase of one product to get another is illegal (antitrust). Ensure bundle is a discount, not a requirement.

## References

- For Adams-Yellen bundling theory, see `references/bundling-theory.md`
- For multi-product pricing optimization, see `references/multi-product-pricing.md`
