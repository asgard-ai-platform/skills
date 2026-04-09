# VaR Backtesting

Backtesting checks whether a VaR model is calibrated correctly: at 95% confidence, realized losses should exceed VaR on roughly 5% of days. Two formal tests are standard — Kupiec (unconditional coverage) and Christoffersen (conditional coverage). Use both together; passing only Kupiec is not sufficient.

---

## Core Concept: Exceedance (Hit) Sequence

For each day `t` in the backtest window, define a hit indicator:

```
I_t = 1  if actual loss > VaR_t   (exceedance)
I_t = 0  otherwise
```

- **Unconditional coverage**: the fraction of hits should equal `1 - α` (e.g., 5% for 95% VaR)
- **Independence**: hits should be randomly scattered, not clustered

A model can pass unconditional coverage but fail independence (e.g., 5% hits but they all occur in two consecutive bad weeks). The Christoffersen test catches this.

---

## Kupiec POF Test (Proportion of Failures)

**What it tests:** Is the observed exceedance rate statistically consistent with the target rate?

### Notation

| Symbol | Meaning |
|--------|---------|
| `T` | Total days tested |
| `N` | Number of exceedances (hits) |
| `p` | Target exceedance rate = `1 - α` (e.g., 0.05 for 95% VaR) |
| `p̂` | Observed rate = `N / T` |

### Test Statistic

Under H₀ (model is correct), `N ~ Binomial(T, p)`. The likelihood ratio statistic is:

```
LR_uc = -2 × ln[ p^N × (1-p)^(T-N) / (p̂^N × (1-p̂)^(T-N)) ]
```

Which simplifies to:

```
LR_uc = -2 × [ N × ln(p/p̂) + (T-N) × ln((1-p)/(1-p̂)) ]
```

`LR_uc ~ χ²(1)` asymptotically under H₀.

**Reject the model** if `LR_uc > 3.841` (χ²(1) critical value at 5% significance).

### Worked Example

**Setup:** T = 250 days, α = 0.95 (p = 0.05), N = 20 observed exceedances.

```
p̂ = 20 / 250 = 0.080
LR_uc = -2 × [ 20 × ln(0.05/0.080) + 230 × ln(0.95/0.920) ]
      = -2 × [ 20 × (-0.4700) + 230 × (0.0328) ]
      = -2 × [ -9.400 + 7.544 ]
      = -2 × (-1.856)
      = 3.712
```

`3.712 < 3.841` → **fail to reject** at 5% significance. Model passes Kupiec.

**But note:** 20 exceedances vs. expected 12.5 — the model is borderline. At p = 0.01 significance (χ² critical = 6.635), it passes more comfortably. Always report both the statistic and the p-value.

### Python (stdlib only)

```python
import math

def kupiec_pof(T: int, N: int, p: float) -> dict:
    """
    Kupiec Proportion of Failures test.
    T: days tested, N: exceedances, p: target rate (1 - confidence)
    Returns: LR statistic, critical value (5%), pass/fail
    """
    p_hat = N / T
    if p_hat == 0 or p_hat == 1:
        return {"error": "p_hat is 0 or 1, cannot compute LR"}
    
    lr = -2 * (N * math.log(p / p_hat) + (T - N) * math.log((1 - p) / (1 - p_hat)))
    chi2_5pct = 3.841  # chi2(1) at 5% significance
    return {
        "T": T, "N": N, "p_target": p, "p_observed": round(p_hat, 4),
        "LR_uc": round(lr, 4),
        "critical_value_5pct": chi2_5pct,
        "pass": lr < chi2_5pct
    }
```

---

## Christoffersen Independence Test

**What it tests:** Are exceedances clustered? A correctly specified model should produce hits that are independently distributed over time.

### Transition Matrix

From the hit sequence `{I_1, I_2, ..., I_T}`, count transitions:

| | Next day: no hit (0) | Next day: hit (1) |
|---|---|---|
| **Today: no hit (0)** | n₀₀ | n₀₁ |
| **Today: hit (1)** | n₁₀ | n₁₁ |

Define:
```
π₀₁ = n₀₁ / (n₀₀ + n₀₁)    # P(hit | previous no-hit)
π₁₁ = n₁₁ / (n₁₀ + n₁₁)    # P(hit | previous hit)
π   = (n₀₁ + n₁₁) / T       # unconditional hit rate
```

### Test Statistic

```
LR_ind = -2 × ln[ π^(n₀₁+n₁₁) × (1-π)^(n₀₀+n₁₀) ]
            + 2 × ln[ π₀₁^n₀₁ × (1-π₀₁)^n₀₀ × π₁₁^n₁₁ × (1-π₁₁)^n₁₀ ]
```

`LR_ind ~ χ²(1)` under H₀ (independence).

**Reject independence** if `LR_ind > 3.841`.

### Combined (Christoffersen) Test

```
LR_cc = LR_uc + LR_ind  ~  χ²(2)
```

**Reject the model** if `LR_cc > 5.991` (χ²(2) critical value at 5%).

This is the preferred single test to use in practice — it catches both miscalibration and clustering simultaneously.

### Worked Example

**Setup:** 250 days, N = 13 hits (expected ~12.5 for 95% VaR).

Transition counts from the hit sequence:
```
n₀₀ = 214,  n₀₁ = 12
n₁₀ = 12,   n₁₁ = 1
```

Compute:
```
π₀₁ = 12 / (214 + 12) = 12/226 = 0.0531
π₁₁ = 1  / (12  + 1)  = 1/13   = 0.0769
π   = (12 + 1) / 250  = 13/250 = 0.0520

LR_ind = -2 × ln[ 0.052^13 × 0.948^237 ]
        + 2 × ln[ 0.0531^12 × 0.9469^214 × 0.0769^1 × 0.9231^12 ]
       ≈ 0.31  (small, as expected — hits are mostly independent here)
```

`LR_cc = LR_uc + LR_ind ≈ 0.15 + 0.31 = 0.46 < 5.991` → **model passes combined test**.

**Contrast — clustered case:** Suppose the same 13 hits all occurred in two consecutive weeks (10 + 3):
```
n₀₀ ≈ 230,  n₀₁ = 2
n₁₀ = 2,    n₁₁ = 11
π₁₁ = 11/13 = 0.846  ← far from π = 0.052
```

`LR_ind` would be large (>>10), model fails independence — a clear sign of risk clustering the VaR model isn't capturing.

---

## Decision Table

| LR_uc | LR_ind | Interpretation | Action |
|-------|--------|----------------|--------|
| Pass | Pass | Model well calibrated | Accept model, continue monitoring |
| Fail (too few hits) | — | Model too conservative | VaR overestimated; may free up capital |
| Fail (too many hits) | — | Model under-covers risk | Recalibrate — check window, distribution |
| Pass | Fail | Hits clustered | Volatility clustering not captured; add GARCH or switch to historical with stress window |
| Fail | Fail | Both problems | Full model rebuild needed |

---

## Minimum Sample Requirements

Backtesting with too few observations produces unreliable tests. Rules of thumb:

| Confidence Level | Minimum Days | Expected Exceedances |
|-----------------|-------------|----------------------|
| 95% | 250 (Basel minimum) | ~12.5 |
| 99% | 500 | ~5 |
| 99.9% | 2000+ | ~2 |

At 99% with only 250 days, you expect ~2.5 hits — far too few for the χ² approximation to hold. Basel III acknowledges this: for 99% VaR, it uses a zone-based (traffic light) approach rather than formal hypothesis testing.

### Basel Traffic Light Zones (99% VaR, 250 days)

| Exceedances | Zone | Regulatory Response |
|-------------|------|---------------------|
| 0–4 | Green | No action |
| 5–9 | Yellow | Supervisory review; capital multiplier may increase |
| 10+ | Red | Model presumed inadequate; immediate review required |

This binomial table is pre-computed assuming T = 250, p = 0.01. The green/yellow cutoff at 5 corresponds roughly to the 95th percentile of Binomial(250, 0.01).

---

## Implementation Checklist

```
□ Use out-of-sample data — never backtest on the same data used to fit the model
□ Recompute VaR daily using only information available at that time (no look-ahead)
□ Mark hit as 1 when loss strictly exceeds VaR (not ≥)
□ Use gross P&L (include fees, slippage) not theoretical returns
□ Run both Kupiec AND Christoffersen — passing one is not enough
□ Report raw counts (N, T) alongside test statistics in output
□ Re-run backtest after any model parameter change
```

---

## Connection to SKILL.md Output

The `backtest` block in the skill's JSON output maps directly to:

```json
"backtest": {
  "exceedances": 13,     ← N
  "expected": 12.5,      ← T × (1 - α)
  "days_tested": 250,    ← T
  "pass": true           ← LR_cc < χ²(2) critical at chosen significance
}
```

For full reporting, also include `LR_uc`, `LR_ind`, and `LR_cc` in an extended metadata block when the downstream consumer needs to audit the model.
