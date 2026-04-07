---
name: "algo-price-dynamic"
description: "Implement dynamic pricing strategies that adjust prices in real-time based on demand, time, and competition. Use this skill when the user needs to build a dynamic pricing system, implement surge pricing, or optimize prices for perishable inventory — even if they say 'real-time pricing', 'surge pricing', or 'demand-based price adjustment'."
metadata:
  category: "WP-39 定價演算法"
  tags: ["pricing", "dynamic-pricing", "revenue-management", "real-time"]
---

# Dynamic Pricing

## Overview

Dynamic pricing adjusts prices in real-time based on demand signals, time, inventory, and competitive conditions. Common in airlines, hotels, ride-sharing, and e-commerce. Objective: maximize revenue (or profit) subject to capacity/inventory constraints.

## When to Use

**Trigger conditions:**
- Pricing perishable inventory (hotel rooms, airline seats, event tickets)
- Implementing demand-responsive pricing for e-commerce
- Building surge pricing or time-based pricing systems

**When NOT to use:**
- For one-time pricing decisions (use Van Westendorp or conjoint)
- When price changes are impractical (regulated markets, long-term contracts)

## Algorithm

```
IRON LAW: Dynamic Pricing Requires REAL-TIME Data
Stale data produces prices optimal for PAST conditions, not current ones.
Three data streams must be current:
1. Demand signal (bookings, searches, cart additions)
2. Inventory/capacity status
3. Competitive prices (where applicable)
Update frequency: minutes for ride-sharing, hours for hotels, daily for retail.
```

### Phase 1: Input Validation
Collect: current demand indicators, remaining inventory/capacity, time until expiration/event, competitor prices, price floor/ceiling constraints.
**Gate:** Real-time data feeds connected, business rules defined.

### Phase 2: Core Algorithm
**Rule-based:** If demand > threshold, increase price by X%. Tiered rules by inventory level.

**Demand-curve based:** 1. Estimate demand curve at current conditions. 2. Find price that maximizes revenue = P × Q(P). 3. Apply inventory constraint: if capacity is scarce, price up; if excess, price down.

**ML-based:** Train model to predict demand at each price point given context features. Optimize over predicted demand curve.

### Phase 3: Verification
Monitor: revenue per unit, booking pace, customer complaints, competitive position. A/B test new pricing rules.
**Gate:** Revenue improved without significant volume loss or customer backlash.

### Phase 4: Output
Return recommended price with reasoning and expected impact.

## Output Format

```json
{
  "recommended_price": 1200,
  "current_price": 999,
  "reasoning": {"demand_signal": "high", "inventory_remaining_pct": 15, "competitor_avg": 1100},
  "expected_impact": {"revenue_change_pct": 18, "volume_change_pct": -5},
  "metadata": {"strategy": "demand-curve", "update_frequency": "hourly"}
}
```

## Examples

### Sample I/O
**Input:** Hotel room, 3 days until date, 85% occupancy, average competitor price $150
**Expected:** Price above competitor ($160-170) due to high occupancy, short time horizon.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Zero demand | Drop to floor price | Stimulate demand, recover some revenue |
| Last unit available | Price near ceiling | Scarcity maximizes willingness to pay |
| Competitor flash sale | Don't auto-match if unnecessary | Avoid price war; assess if your product differentiates |

## Gotchas

- **Customer fairness perception**: Visible price discrimination (same product, different prices for different users) generates backlash. Segment by time, channel, or bundle — not by individual.
- **Price war spiraling**: Automated competitive pricing can create a race to the bottom. Set absolute floors and rate-of-change limits.
- **Demand cannibalization**: If customers learn prices drop later, they wait. This is the "strategic customer" problem — don't train customers to delay.
- **Regulatory risk**: Dynamic pricing may violate anti-gouging laws during emergencies. Build in legal constraint rules.
- **A/B testing bias**: Testing different prices creates revenue measurement challenges. The control group at the "wrong" price loses money by design.

## References

- For revenue management models (airline/hotel), see `references/revenue-management.md`
- For fairness constraints in dynamic pricing, see `references/fairness-constraints.md`
