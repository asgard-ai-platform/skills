---
name: "algo-sc-eoq"
description: "Calculate Economic Order Quantity to minimize total inventory cost (ordering + holding). Use this skill when the user needs to determine optimal order size, balance ordering frequency against storage costs, or set reorder points — even if they say 'how much to order', 'optimal batch size', or 'inventory cost minimization'."
metadata:
  category: "WP-41 供應鏈演算法"
  tags: ["supply-chain", "eoq", "inventory", "ordering"]
---

# Economic Order Quantity (EOQ)

## Overview

EOQ determines the order quantity that minimizes total inventory cost = ordering cost + holding cost. Formula: EOQ = √(2DS/H) where D=annual demand, S=ordering cost per order, H=holding cost per unit per year. Assumes constant demand and instantaneous replenishment.

## When to Use

**Trigger conditions:**
- Setting standard order quantities for inventory replenishment
- Balancing ordering frequency against warehousing costs
- Baseline calculation before applying safety stock adjustments

**When NOT to use:**
- When demand is highly uncertain (use newsvendor model)
- When products are perishable with short shelf life
- When quantity discounts change the cost structure significantly

## Algorithm

```
IRON LAW: EOQ Assumes CONSTANT, KNOWN Demand
If demand is variable or uncertain, EOQ gives the wrong answer.
Real-world application: use EOQ as a starting point, then add
safety stock for demand variability and lead time uncertainty.
Total cost curve is flat near EOQ — ±20% from optimal Q changes
total cost by only ~2%.
```

### Phase 1: Input Validation
Determine: D (annual demand in units), S (fixed cost per order), H (holding cost per unit per year = unit cost × holding rate, typically 20-30% of unit value).
**Gate:** All costs positive, demand estimate reasonable.

### Phase 2: Core Algorithm
1. EOQ = √(2 × D × S / H)
2. Number of orders per year = D / EOQ
3. Reorder point = d × L (daily demand × lead time in days)
4. Total annual cost = (D/Q × S) + (Q/2 × H) at Q = EOQ

### Phase 3: Verification
Check: ordering cost component ≈ holding cost component (they're equal at EOQ). Total cost is at minimum.
**Gate:** Ordering cost ≈ holding cost (±5%).

### Phase 4: Output
Return EOQ with cost breakdown and reorder point.

## Output Format

```json
{
  "eoq": 500,
  "orders_per_year": 20,
  "reorder_point": 150,
  "annual_cost": {"ordering": 2000, "holding": 2000, "total": 4000},
  "metadata": {"demand": 10000, "order_cost": 100, "holding_cost": 4.0}
}
```

## Examples

### Sample I/O
**Input:** D=10,000 units/year, S=$100/order, H=$4/unit/year
**Expected:** EOQ = √(2×10000×100/4) = √500000 = 707 units

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Very high S, low H | Large EOQ, few orders | Minimize expensive ordering |
| Very low S, high H | Small EOQ, frequent orders | Minimize expensive holding |
| D = 0 | EOQ = 0, no ordering | No demand, no orders needed |

## Gotchas

- **Holding cost underestimation**: H should include: capital cost, storage, insurance, obsolescence, handling. Companies often only count warehouse rent, understating true H.
- **Flat cost curve**: Total cost is insensitive near EOQ. Rounding EOQ to a convenient number (full pallet, container) costs very little.
- **Quantity discounts**: Price breaks at certain quantities may make it cheaper to order MORE than EOQ. Compare total cost at EOQ vs discount breakpoints.
- **Lead time variability**: EOQ doesn't address when to order, only how much. Add safety stock: SS = z × σ_demand × √(lead time).
- **Multi-item coordination**: When multiple items share ordering costs (same supplier), use joint replenishment models, not individual EOQs.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/eoq.py` | Compute Economic Order Quantity and cost breakdown | `python scripts/eoq.py --help` |

Run `python scripts/eoq.py --verify` to execute built-in sanity tests.

## References

- For EOQ with quantity discounts, see `references/eoq-discounts.md`
- For safety stock calculation, see algo-sc-safety-stock
