---
name: "algo-sc-newsvendor"
description: "Solve the newsvendor problem for single-period ordering decisions under uncertain demand. Use this skill when the user needs to determine optimal order quantity for perishable goods, seasonal products, or one-time purchase decisions — even if they say 'how much to order for this season', 'perishable inventory', or 'single-period ordering'."
metadata:
  category: "WP-41 供應鏈演算法"
  tags: ["supply-chain", "newsvendor", "inventory", "demand-uncertainty"]
---

# Newsvendor Model

## Overview

The newsvendor model determines optimal order quantity for a single selling period with uncertain demand. Balances overage cost (Co = cost - salvage) against underage cost (Cu = price - cost). Optimal Q* satisfies: P(D ≤ Q*) = Cu / (Cu + Co). Known as the critical ratio solution.

## When to Use

**Trigger conditions:**
- One-time or seasonal purchasing decisions (fashion, holiday goods, event tickets)
- Perishable products with no restocking opportunity
- Setting initial stocking levels before demand is observed

**When NOT to use:**
- For continuous replenishment with stable demand (use EOQ)
- When backorders are acceptable and demand carries over (multi-period models)

## Algorithm

```
IRON LAW: The Critical Ratio Determines Optimal Service Level
Q* = F⁻¹(Cu / (Cu + Co)) where F⁻¹ is the inverse demand CDF.
If margin is high relative to cost (Cu >> Co), order MORE (high service level).
If margin is low relative to excess cost (Co >> Cu), order LESS (low service level).
The optimal solution almost NEVER equals expected demand.
```

### Phase 1: Input Validation
Define: unit cost (c), selling price (p), salvage value (v), demand distribution (mean μ, std σ). Compute: Cu = p - c, Co = c - v.
**Gate:** p > c > v (profitable with positive overage cost), demand distribution estimated.

### Phase 2: Core Algorithm
1. Critical ratio: CR = Cu / (Cu + Co) = (p - c) / (p - v)
2. If demand ~ Normal(μ, σ): Q* = μ + z(CR) × σ where z(CR) = inverse normal CDF at CR
3. Expected profit = Cu × E[min(Q,D)] - Co × E[max(Q-D, 0)]
4. Expected units sold = μ - σ × L(z) where L(z) is the standard loss function

### Phase 3: Verification
Check: Q* > 0, CR between 0 and 1, Q* is above or below μ depending on whether CR > or < 0.5.
**Gate:** Q* directionally correct relative to mean demand.

### Phase 4: Output
Return optimal order quantity with profit analysis.

## Output Format

```json
{
  "optimal_quantity": 130,
  "critical_ratio": 0.71,
  "expected_profit": 2800,
  "expected_leftover": 15,
  "expected_stockout_probability": 0.29,
  "metadata": {"price": 50, "cost": 20, "salvage": 5, "demand_mean": 100, "demand_std": 30}
}
```

## Examples

### Sample I/O
**Input:** p=$50, c=$20, v=$5, D~Normal(100, 30)
**Expected:** Cu=30, Co=15, CR=30/45=0.667, z=0.43, Q*=100+0.43×30=113 units.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| v = 0 (total loss) | Lower Q*, conservative | High overage cost pushes order down |
| p >> c (high margin) | Q* well above mean | Worth risking excess to avoid lost sales |
| σ = 0 (certain demand) | Q* = μ exactly | No uncertainty, order exactly demand |

## Gotchas

- **Distribution choice matters**: Normal allows negative demand. For low-mean items, use Poisson or truncated normal. For high CV, use lognormal.
- **Demand estimation**: The hardest part is estimating μ and σ. Use historical data, expert judgment, or Bayesian updating from early sales signals.
- **Risk aversion**: The newsvendor model is risk-neutral. Risk-averse decision makers systematically under-order relative to Q*. Adjust for behavioral bias.
- **Multi-product constraints**: With a shared budget constraint across products, solve the constrained newsvendor (Lagrangian relaxation).
- **Salvage value assumption**: Assumes all excess can be salvaged at v. If disposal has a cost (v < 0), the model still works but Q* drops further.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/newsvendor.py` | Compute newsvendor optimal quantity, expected profit, and fill rate | `python scripts/newsvendor.py --help` |

Run `python scripts/newsvendor.py --verify` to execute built-in sanity tests.

## References

- For multi-product constrained newsvendor, see `references/constrained-newsvendor.md`
- For demand distribution fitting, see `references/demand-fitting.md`
