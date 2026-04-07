---
name: "algo-sc-safety-stock"
description: "Calculate safety stock levels to buffer against demand and lead time uncertainty. Use this skill when the user needs to set inventory buffers, determine service level trade-offs, or optimize safety stock across SKUs — even if they say 'how much buffer inventory', 'stockout prevention', or 'service level calculation'."
metadata:
  category: "WP-41 供應鏈演算法"
  tags: ["supply-chain", "safety-stock", "inventory", "service-level"]
---

# Safety Stock Calculation

## Overview

Safety stock is buffer inventory held to protect against demand and lead time variability. Formula: SS = z × √(LT × σ²_d + d² × σ²_LT) where z=service factor, LT=lead time, σ_d=demand std dev, d=avg demand, σ_LT=lead time std dev. Directly trades inventory cost against stockout risk.

## When to Use

**Trigger conditions:**
- Setting inventory buffers for variable-demand items
- Choosing target service levels and computing required safety stock
- Optimizing safety stock across a portfolio of SKUs

**When NOT to use:**
- When demand is deterministic (use EOQ without safety stock)
- For one-time purchase decisions (use newsvendor model)

## Algorithm

```
IRON LAW: Safety Stock Is a TRADE-OFF, Not a Target
More safety stock = fewer stockouts but higher holding cost.
The relationship is non-linear: going from 95% to 99% service level
roughly DOUBLES safety stock. Going from 99% to 99.9% doubles it
again. Always quantify the cost of each service level increment.
z-values: 90%→1.28, 95%→1.65, 99%→2.33, 99.9%→3.09.
```

### Phase 1: Input Validation
Collect: historical demand data (weekly/monthly), lead time data (average and variability), target service level, unit cost and holding rate.
**Gate:** Minimum 12 periods of demand data, lead time estimates available.

### Phase 2: Core Algorithm
1. Compute demand statistics: average demand (d), demand standard deviation (σ_d)
2. Compute lead time statistics: average LT, LT standard deviation (σ_LT)
3. Compute combined variability: σ_combined = √(LT × σ²_d + d² × σ²_LT)
4. Look up z for target service level
5. Safety stock = z × σ_combined
6. Reorder point = d × LT + SS

### Phase 3: Verification
Simulate: using historical demand, would the computed SS have prevented stockouts at the target service level?
**Gate:** Simulated service level matches target (±2%).

### Phase 4: Output
Return safety stock with cost impact and service level analysis.

## Output Format

```json
{
  "safety_stock": 250,
  "reorder_point": 850,
  "service_level": 0.95,
  "annual_holding_cost": 5000,
  "metadata": {"avg_demand_weekly": 120, "demand_cv": 0.3, "avg_lead_time_weeks": 5}
}
```

## Examples

### Sample I/O
**Input:** Weekly demand: avg=100, σ=30. Lead time: avg=4 weeks, σ=1 week. Target: 95%.
**Expected:** σ_combined = √(4×900 + 10000×1) = √(3600+10000) = √13600 = 116.6. SS = 1.65 × 116.6 = 192 units.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Zero demand variability | SS from LT variability only | σ_d = 0, only lead time risk remains |
| Zero lead time variability | SS from demand variability only | σ_LT = 0, standard formula simplifies |
| Very long lead time | High SS | More uncertainty accumulates over longer periods |

## Gotchas

- **Normal distribution assumption**: Formula assumes normally distributed demand. Highly intermittent demand (many zeros) needs different approaches (Poisson, negative binomial).
- **Demand forecast error, not demand variability**: If you use a forecast, SS should buffer forecast ERROR (σ_error), not raw demand variability.
- **Service level definition**: Cycle service level (probability of no stockout per cycle) ≠ fill rate (fraction of demand met from stock). Companies often mean fill rate but calculate cycle SL.
- **Lead time data quality**: Lead time variability is often poorly tracked. Underestimating σ_LT leads to insufficient safety stock.
- **ABC segmentation**: Don't apply the same service level to all SKUs. A-items (high revenue) deserve 99%; C-items may be fine at 90%.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/safety_stock.py` | Compute safety stock and reorder point with combined demand/lead-time variability | `python scripts/safety_stock.py --help` |

Run `python scripts/safety_stock.py --verify` to execute built-in sanity tests.

## References

- For multi-echelon safety stock optimization, see `references/multi-echelon.md`
- For intermittent demand methods, see `references/intermittent-demand.md`
