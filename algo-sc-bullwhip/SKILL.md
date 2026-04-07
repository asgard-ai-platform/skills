---
name: "algo-sc-bullwhip"
description: "Analyze and mitigate the bullwhip effect where demand variability amplifies upstream in supply chains. Use this skill when the user needs to diagnose order variability amplification, quantify the bullwhip ratio, or implement dampening strategies — even if they say 'why are our orders so volatile', 'supply chain variability', or 'demand amplification problem'."
metadata:
  category: "WP-41 供應鏈演算法"
  tags: ["supply-chain", "bullwhip-effect", "demand-variability", "coordination"]
---

# Bullwhip Effect Analysis

## Overview

The bullwhip effect describes how small fluctuations in consumer demand amplify progressively at each upstream stage of the supply chain. A 5% retail demand increase can become a 40% order spike at the manufacturer. Caused by demand signal processing, order batching, price fluctuations, and rationing/shortage gaming.

## When to Use

**Trigger conditions:**
- Diagnosing why supplier orders are far more volatile than end-consumer demand
- Quantifying demand amplification across supply chain tiers
- Designing strategies to reduce order variability

**When NOT to use:**
- When demand is genuinely volatile (not amplified) — the issue is demand forecasting
- For single-echelon inventory optimization (use EOQ or safety stock)

## Algorithm

```
IRON LAW: Demand Variability Amplifies at EACH Upstream Stage
Bullwhip ratio = Var(orders) / Var(demand). A ratio > 1 at any stage
confirms the bullwhip effect. The four root causes (Lee et al., 1997):
1. Demand signal processing (forecasting with moving averages)
2. Order batching (periodic review, MOQs)
3. Price fluctuations (forward buying during promotions)
4. Rationing and shortage gaming (inflating orders during scarcity)
```

### Phase 1: Input Validation
Collect: end-consumer demand time series AND order time series at each supply chain stage (retailer → distributor → manufacturer → supplier).
**Gate:** At least 2 tiers of order data, minimum 26 periods.

### Phase 2: Core Algorithm
1. Compute variance of demand at each tier
2. Compute bullwhip ratio per tier: BWR_i = Var(orders_i) / Var(orders_{i-1})
3. Identify contribution of each cause: batch size analysis, promotion calendar overlap, forecast method evaluation
4. Quantify cost: excess inventory carrying cost, expediting cost, capacity misallocation

### Phase 3: Verification
Check: BWR > 1 at upstream stages (confirms bullwhip). Correlate order spikes with identifiable causes (promotions, forecast updates, batch cycles).
**Gate:** Bullwhip quantified and root causes identified.

### Phase 4: Output
Return bullwhip ratios with root cause attribution and mitigation recommendations.

## Output Format

```json
{
  "bullwhip_ratios": [{"tier": "retailer→distributor", "ratio": 1.8}, {"tier": "distributor→manufacturer", "ratio": 2.3}],
  "root_causes": [{"cause": "order_batching", "contribution_pct": 40}, {"cause": "demand_signal_processing", "contribution_pct": 35}],
  "metadata": {"periods": 52, "tiers_analyzed": 3}
}
```

## Examples

### Sample I/O
**Input:** Consumer demand CV=0.10, Retailer orders CV=0.18, Distributor orders CV=0.32
**Expected:** BWR retailer=3.24 (0.18²/0.10²), BWR distributor=3.16 (0.32²/0.18²). Strong bullwhip confirmed.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| BWR < 1 | Smoothing effect | Information sharing or VMI may dampen variability |
| Promotional periods | Spike in BWR | Forward buying amplifies orders |
| Single tier only | Cannot measure amplification | Need at least 2 tiers for comparison |

## Gotchas

- **Data granularity**: Weekly vs monthly data can show different bullwhip magnitudes. Use consistent time buckets across tiers.
- **VMI and CPFR**: Vendor-managed inventory and collaborative planning reduce bullwhip by sharing demand data. But they require trust and IT integration.
- **Information sharing ≠ bullwhip elimination**: Even with POS data sharing, lead times and batch constraints still cause some amplification.
- **Shortage gaming is hardest to fix**: During shortages, customers inflate orders. When supply recovers, cancellations flood in. Only committed-quantity allocations prevent this.
- **Measurement challenges**: True consumer demand is often unobserved (only POS data). Lost sales from stockouts are invisible, understating true demand variability.

## References

- For Lee-Padmanabhan-Whang formal model, see `references/bullwhip-model.md`
- For information sharing strategies, see `references/information-sharing.md`
