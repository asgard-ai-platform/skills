---
name: "skill-algo-risk-var"
description: "Calculate Value at Risk to estimate maximum portfolio loss at a given confidence level. Use this skill when the user needs to quantify downside risk, set risk limits, or report regulatory risk measures — even if they say 'worst case loss', 'portfolio risk', or 'how much could we lose'."
metadata:
  category: "WP-40 風險演算法"
  tags: ["risk", "value-at-risk", "portfolio", "risk-management"]
---

# Value at Risk (VaR)

## Overview

VaR estimates the maximum loss a portfolio can suffer over a given time horizon at a specified confidence level. Example: "95% 1-day VaR of $1M" means there's a 5% chance of losing more than $1M in one day. Three methods: parametric (normal), historical simulation, Monte Carlo.

## When to Use

**Trigger conditions:**
- Quantifying portfolio downside risk for risk management
- Setting trading limits and capital reserves
- Regulatory reporting (Basel III requires VaR-based capital)

**When NOT to use:**
- When you need to know how bad losses CAN get beyond VaR (use CVaR/Expected Shortfall)
- For illiquid assets with no price history (VaR needs return data)

## Algorithm

```
IRON LAW: VaR Does NOT Tell You How Bad It Gets BEYOND the Threshold
VaR says "95% of the time, losses won't exceed $X." It says NOTHING
about the 5% worst case. A portfolio can have low VaR but catastrophic
tail losses. Always supplement with Expected Shortfall (CVaR) which
measures the average loss in the tail.
```

### Phase 1: Input Validation
Collect: portfolio positions, historical returns (min 250 days for 1Y), confidence level (typically 95% or 99%), time horizon (1 day or 10 days).
**Gate:** Sufficient return history, positions valued at current market.

### Phase 2: Core Algorithm
**Parametric VaR:** VaR = -μ + zα × σ (assumes normal returns). For portfolio: use covariance matrix for portfolio σ.

**Historical Simulation:** 1. Compute daily P&L from historical returns. 2. Sort P&L ascending. 3. VaR = the (1-α) percentile loss.

**Monte Carlo:** 1. Fit return distribution (or use historical). 2. Simulate 10,000+ portfolio paths. 3. VaR = (1-α) percentile of simulated losses.

### Phase 3: Verification
Backtest: count how often actual losses exceed VaR over the past year. At 95% confidence, exceedances should be ~5%. Use Kupiec or Christoffersen test.
**Gate:** Backtest exceedance rate within acceptable bounds.

### Phase 4: Output
Return VaR estimate with backtest results.

## Output Format

```json
{
  "var": {"amount": 1250000, "confidence": 0.95, "horizon_days": 1, "currency": "TWD"},
  "cvar": {"amount": 1800000},
  "backtest": {"exceedances": 13, "expected": 12.5, "days_tested": 250, "pass": true},
  "metadata": {"method": "historical_simulation", "portfolio_value": 50000000}
}
```

## Examples

### Sample I/O
**Input:** Portfolio $50M, 250 days of daily returns, 95% confidence
**Expected:** Historical VaR ≈ 2-3% of portfolio = $1-1.5M

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Normal market conditions | VaR looks adequate | But misses tail events |
| 2008-like crisis in history | Higher VaR from historical method | Captures fat tails if crisis is in window |
| Very short history (30 days) | Unreliable VaR | Insufficient data for tail estimation |

## Gotchas

- **Normality assumption**: Parametric VaR assumes normal returns. Financial returns have fat tails — parametric VaR UNDERESTIMATES tail risk.
- **Historical window**: Historical simulation is only as good as the history. If the past 250 days were calm, VaR will be low even if a crisis is coming.
- **Time scaling**: VaR scales with √T only under independence and normality. For volatile or trending markets, this approximation is poor.
- **Diversification illusion**: VaR from correlated assets using normal-times correlations understates risk. Correlations spike during crises (correlation breakdown).
- **Gaming VaR**: Traders can structure positions that look safe under VaR but have catastrophic tail risk. This is why regulators also require stress testing.

## References

- For Expected Shortfall (CVaR) calculation, see `references/expected-shortfall.md`
- For VaR backtesting methods, see `references/backtesting.md`
