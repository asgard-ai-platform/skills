# Expected Shortfall (CVaR)

Expected Shortfall (ES), also called Conditional Value at Risk (CVaR) or Expected Tail Loss (ETL), answers the question VaR deliberately ignores: **given that losses exceed the VaR threshold, how large are those losses on average?**

This directly addresses the parent skill's IRON LAW: VaR at 95% says nothing about the worst 5% of outcomes. ES is the mean of exactly that 5%.

---

## Definition

At confidence level α and horizon T:

```
ES_α = -E[R | R < -VaR_α]
```

- `R` = portfolio return (or P&L)
- `VaR_α` = the α-confidence VaR threshold (a positive number, representing a loss magnitude)
- The expectation is taken only over the tail — the worst (1-α) fraction of outcomes

For a continuous loss distribution F:

```
ES_α = (1 / (1-α)) × ∫_{-∞}^{-VaR_α} |r| · f(r) dr
```

Equivalently:

```
ES_α = (1 / (1-α)) × ∫_α^1 VaR_u du
```

This second form is useful: ES is the average of all VaRs from confidence level α up to 1.0. It makes clear that ES is always ≥ VaR at the same confidence level.

---

## Discrete Calculation (Historical Simulation)

Given N historical returns sorted ascending (worst to best), at confidence level α:

1. Identify the tail cutoff index: `k = floor(N × (1-α))`
2. The tail consists of the worst `k` observations: `r[0], r[1], ..., r[k-1]`
3. ES = `-(1/k) × Σ r[i]` for i = 0 to k-1

**If k = 0** (too few observations for the chosen α), ES is undefined. Minimum sample for 99% confidence: N ≥ 100; for 99.9%: N ≥ 1000.

### Interpolation at the boundary

When `N × (1-α)` is not an integer, include a fractional weight on observation `r[k]`:

```
fractional_weight = (N × (1-α)) - floor(N × (1-α))
ES = -(1 / (N×(1-α))) × [Σ_{i=0}^{k-1} r[i] + fractional_weight × r[k]]
```

This ensures ES is a consistent estimator regardless of sample size.

---

## Worked Example

Continuing from the parent SKILL.md example:

**Portfolio value:** $1,000,000  
**N = 20 returns, sorted ascending (worst first):**

| Index | Return | P&L ($) |
|-------|--------|---------|
| 0 | −0.050 | −50,000 |
| 1 | −0.040 | −40,000 |
| 2 | −0.035 | −35,000 |
| 3 | −0.030 | −30,000 |
| 4 | −0.025 | −25,000 |
| … | … | … |

**Confidence level α = 95%**

**Step 1: Tail cutoff**
```
k = floor(20 × (1 - 0.95)) = floor(20 × 0.05) = floor(1.0) = 1
```

**Step 2: VaR**
- VaR = -r[1] × $1M = 0.040 × $1M = **$40,000**
- (The VaR observation itself is r[1] = −0.040, i.e., the 2nd worst)

**Step 3: ES — the tail is only index 0 through k-1 = 0**
```
ES = -(1/1) × r[0] × $1M
ES = -(-0.050) × $1M = $50,000
```

**Result:** 95% 1-day ES = **$50,000**

This means: on the worst 5% of days (i.e., the 1 day in 20 where losses exceed VaR), the expected loss is $50,000 — which is $10,000 worse than VaR suggests.

**Sanity check:** ES ($50,000) ≥ VaR ($40,000). ✓

### With interpolation

If α = 97.5% instead:
```
tail_size = 20 × 0.025 = 0.5
k = floor(0.5) = 0
fractional_weight = 0.5
```

ES = -(1/0.5) × [0.5 × r[0]] × $1M = -2 × 0.5 × (−0.050) × $1M = **$50,000**

At 97.5% with this dataset, ES equals r[0] since only one observation anchors the tail.

---

## Parametric ES (Normal Distribution)

When returns are assumed normally distributed with mean μ and standard deviation σ:

```
ES_α = -μ + σ × φ(z_α) / (1-α)
```

Where:
- `z_α` = the standard normal quantile at α (e.g., 1.645 for 95%, 2.326 for 99%)
- `φ(z_α)` = standard normal PDF evaluated at `z_α`

**Common values:**

| α | z_α | φ(z_α) | φ(z_α)/(1-α) | ES multiplier vs σ |
|---|-----|--------|--------------|-------------------|
| 90% | 1.282 | 0.1755 | 1.755 | 1.755σ |
| 95% | 1.645 | 0.1031 | 2.063 | 2.063σ |
| 99% | 2.326 | 0.0267 | 2.665 | 2.665σ |

**Example:** Portfolio σ = $20,000/day, μ ≈ 0:
- 95% VaR = 1.645 × $20,000 = $32,900
- 95% ES = 2.063 × $20,000 = **$41,260**

Parametric ES is ~25% larger than parametric VaR at 95% confidence under normality.

**Warning:** Real return distributions have fatter tails than normal. Parametric ES will still underestimate true tail losses. Historical simulation ES is preferred when sufficient data exists.

---

## ES vs VaR: When Each Matters

| Criterion | VaR | ES |
|-----------|-----|----|
| Regulatory (Basel III market risk) | Required | Also required (since FRTB/Basel III.1) |
| Captures tail severity | No | Yes |
| Coherent risk measure* | No | Yes |
| Backtestable directly | Yes (count exceedances) | Harder (see backtesting section) |
| Stable with small samples | More stable | Needs larger N |
| Intuitive to non-quants | "Max loss at X% confidence" | Harder to explain |

*A coherent risk measure satisfies sub-additivity: ES(A+B) ≤ ES(A) + ES(B). VaR can violate this — two portfolios merged can have higher VaR than the sum of parts, incentivizing dangerous risk concentration.

---

## Python Implementation

```python
import numpy as np

def historical_es(returns: np.ndarray, confidence: float = 0.95) -> dict:
    """
    Compute VaR and ES via historical simulation.
    
    Args:
        returns: array of portfolio returns (as fractions, e.g., -0.05 for -5%)
        confidence: confidence level, e.g., 0.95 for 95%
    
    Returns:
        dict with 'var' and 'es' as positive loss amounts (fraction of portfolio)
    """
    sorted_returns = np.sort(returns)  # ascending, worst first
    n = len(sorted_returns)
    tail_size = n * (1 - confidence)
    k = int(np.floor(tail_size))
    
    if k == 0:
        raise ValueError(
            f"Insufficient data: {n} observations for {confidence:.0%} confidence. "
            f"Need at least {int(np.ceil(1/(1-confidence)))} observations."
        )
    
    # VaR: the k-th worst return (boundary of the tail)
    var = -sorted_returns[k]  # positive number
    
    # ES: mean of the worst k returns, with fractional boundary weight
    fractional = tail_size - k
    tail_sum = sorted_returns[:k].sum() + fractional * sorted_returns[k]
    es = -tail_sum / tail_size  # positive number
    
    return {"var": var, "es": es, "tail_observations": k, "tail_size": tail_size}


def parametric_es(mu: float, sigma: float, confidence: float = 0.95) -> dict:
    """
    Compute VaR and ES assuming normally distributed returns.
    """
    from scipy import stats
    z = stats.norm.ppf(confidence)
    phi_z = stats.norm.pdf(z)
    
    var = -mu + z * sigma
    es = -mu + phi_z / (1 - confidence) * sigma
    
    return {"var": var, "es": es, "method": "parametric_normal"}


# Verify with parent SKILL.md example
if __name__ == "__main__":
    returns = np.array([
        -0.050, -0.040, -0.035, -0.030, -0.025,
        -0.020, -0.015, -0.010, -0.005,  0.000,
         0.005,  0.010,  0.015,  0.020,  0.025,
         0.030,  0.035,  0.040,  0.045,  0.050
    ])
    portfolio_value = 1_000_000
    result = historical_es(returns, confidence=0.95)
    print(f"VaR:  ${result['var'] * portfolio_value:,.0f}")  # $40,000
    print(f"ES:   ${result['es'] * portfolio_value:,.0f}")   # $50,000
    assert result["var"] <= result["es"], "ES must be >= VaR"
```

---

## ES Backtesting

ES is harder to backtest than VaR because it is an average of unobservable tail expectations, not a single quantile.

### Exceedance Magnitude Test (Acerbi-Szekely, 2014)

Define the test statistic:

```
Z = (1 / (T × (1-α) × ES_t)) × Σ_{t: L_t > VaR_t} L_t  −  1
```

Where `L_t` is the actual loss on day t, and the sum runs only over days when losses exceeded VaR. Under a correct model, Z → 0. Negative Z means ES was overestimated (conservative); positive Z means underestimated (dangerous).

**Practical threshold:** |Z| > 0.2 for N=250 observations warrants investigation.

### Simple Exceedance Check (approximate)

Even without a formal ES backtest, verify:
1. VaR exceedance count is in bounds (Kupiec test, inherited from parent skill)
2. On days that exceeded VaR, compute the average actual loss
3. Compare to ES estimate — if average tail loss consistently exceeds ES, the model understates risk

---

## Common Mistakes

**Mistake 1: Using ES as a direct substitute for stress testing**  
ES is a statistical average of historical tail losses. It will not capture a scenario that hasn't happened in your data window. A 2008-style crisis, if outside your 250-day window, contributes nothing to ES. Supplement with scenario analysis.

**Mistake 2: Confusing ES confidence levels**  
95% ES and 99% VaR are sometimes used interchangeably in practice ("they give similar numbers"). They are not the same measure. 97.5% ES is the Basel FRTB standard — do not substitute 99% VaR without explicit regulatory approval.

**Mistake 3: Too few tail observations**  
At 99% confidence with 250 days of history, only ~2-3 observations enter the ES calculation. This produces a highly unstable estimate. The standard fix is to use 95% ES (12-13 observations) for internal risk management, reserving 99% ES for regulatory reporting where longer histories are mandated.

**Mistake 4: Treating ES as portfolio-additive without checking sub-portfolios**  
ES is sub-additive in theory, but in practice, the ES of a combined portfolio is not simply the sum of sub-portfolio ES values when computed from historical simulation — the joint tail behavior depends on which days each sub-portfolio suffered its worst losses simultaneously.
