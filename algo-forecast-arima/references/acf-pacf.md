# ACF / PACF Interpretation Guide for ARIMA Parameter Selection

This document covers how to read ACF and PACF plots to choose p (AR order) and q (MA order) for ARIMA(p,d,q). Apply **after** differencing the series d times so the input is stationary.

---

## Definitions

### Autocorrelation Function (ACF)

The ACF at lag k measures the correlation between the series and itself shifted k periods:

```
ρ(k) = Cov(Yₜ, Yₜ₋ₖ) / Var(Yₜ)
     = γ(k) / γ(0)
```

where γ(k) = E[(Yₜ − μ)(Yₜ₋ₖ − μ)].

**What it captures:** direct + indirect correlations. A strong lag-1 autocorrelation bleeds into lag-2, lag-3, etc., even if no direct relation exists at those lags.

Sample estimate (n observations):

```
r(k) = Σ(t=k+1 to n) (Yₜ − Ȳ)(Yₜ₋ₖ − Ȳ)
       ─────────────────────────────────────
       Σ(t=1 to n) (Yₜ − Ȳ)²
```

### Partial Autocorrelation Function (PACF)

The PACF at lag k measures the correlation between Yₜ and Yₜ₋ₖ **after removing** the linear effect of all intermediate lags 1, …, k−1:

```
φ(k,k) = Corr(Yₜ − Ŷₜ, Yₜ₋ₖ − Ŷₜ₋ₖ)
```

where Ŷₜ is the projection of Yₜ onto {Yₜ₋₁, …, Yₜ₋₍ₖ₋₁₎}.

**What it captures:** the unique contribution of lag k, with intermediate lags partialled out.

### 95% Confidence Bands

Under the null hypothesis of zero autocorrelation (white noise), the approximate 95% band is:

```
±1.96 / √n
```

Spikes outside this band are statistically significant at the 5% level. Do not treat every out-of-band spike as real; expect ~1 in 20 to be false positives by chance.

---

## The Canonical Decision Table

| Series type         | ACF pattern                        | PACF pattern                       | Model to fit  |
|---------------------|------------------------------------|------------------------------------|---------------|
| Pure AR(p)          | Decays slowly (tails off)          | Cuts off after lag p               | ARIMA(p,d,0)  |
| Pure MA(q)          | Cuts off after lag q               | Decays slowly (tails off)          | ARIMA(0,d,q)  |
| Mixed ARMA(p,q)     | Tails off                          | Tails off                          | ARIMA(p,d,q)  |
| White noise         | All within bands                   | All within bands                   | No model needed |
| Non-stationary      | Decays very slowly, stays positive | Large spike at lag 1, then drops   | Difference first (d+=1) |
| Over-differenced    | Negative spike at lag 1, recovers  | Cuts off at lag 1                  | Reduce d by 1 |

**Memory hook:**
- **AR → look at PACF** for cutoff (p = last significant PACF lag)
- **MA → look at ACF** for cutoff (q = last significant ACF lag)

---

## Interpreting "Tails Off" vs "Cuts Off"

**Cuts off at lag k** means: significant spike(s) at lags ≤ k, then all subsequent lags fall inside the confidence band. The transition is abrupt.

**Tails off** means: lags decay gradually (exponentially or in a damped sine wave pattern), never making a clean break. Individual lags may dip in and out of the band.

| Pattern                    | Looks like                                      |
|----------------------------|-------------------------------------------------|
| AR(1) decay in ACF         | Exponential decay: ρ(k) ≈ φ¹ᵏ                  |
| AR(2) decay in ACF         | Damped sine or exponential depending on φ₁,φ₂  |
| MA(1) cutoff in ACF        | One spike at lag 1, then zero                   |
| MA(2) cutoff in ACF        | Spikes at lags 1 and 2, then zero               |

---

## Worked Example: Monthly Retail Sales (n = 72)

### Raw data ACF (before differencing)

```
Lag:   1     2     3     4     5     6     7     8     9    10    11    12
ACF: 0.91  0.82  0.73  0.64  0.57  0.51  0.46  0.41  0.37  0.33  0.30  0.28
```

95% band: ±1.96/√72 ≈ ±0.23

**Observation:** ACF decays very slowly and stays positive well beyond the band. This is the classic non-stationary signature. → **Apply first difference (d=1).**

### After first difference: ACF and PACF

```
Lag:     1      2      3      4      5      6      7      8      9     10     11     12
ACF:  -0.32   0.08  -0.04   0.03  -0.02   0.01   0.03  -0.01   0.02  -0.03   0.04   0.61
PACF: -0.32  -0.06  -0.03   0.02  -0.01   0.01   0.04  -0.02   0.03  -0.04   0.05   0.58
```

95% band: ±0.23

**Reading the differenced ACF:**
- Lag 1: −0.32 — outside band (negative spike)
- Lags 2–11: inside band
- Lag 12: +0.61 — large spike → **seasonal MA term at s=12**

**Reading the differenced PACF:**
- Lag 1: −0.32 — outside band (negative spike)
- Lags 2–11: inside band
- Lag 12: +0.58 — large spike → **seasonal AR term at s=12**

**Step 1 — Non-seasonal terms:**
- ACF cuts off after lag 1 (one negative spike) → MA(1), q=1
- PACF cuts off after lag 1 (one negative spike, matching ACF) → consistent with MA(1)

**Step 2 — Seasonal terms (lag 12):**
- Both ACF and PACF show significant spikes at lag 12 only (lag 24 not visible with n=72) → start with SARIMA seasonal order (1,1,1,12) or (0,1,1,12)

**Initial candidate:** SARIMA(0,1,1)(1,1,1,12)

---

## Step-by-Step Reading Protocol

**Step 1: Check stationarity first.**
If ACF decays slowly (10+ lags above 0.2), the series is non-stationary. Difference and replot before attempting AR/MA identification. Reading ACF/PACF on non-stationary data gives misleading signals.

**Step 2: Check the lag-1 ACF of the differenced series.**
- Lag-1 ACF near −0.5 or below: possible over-differencing. Consider reducing d.
- Lag-1 ACF significantly positive: may need another difference (d+=1) or AR term.

**Step 3: Identify the dominant structure.**
Apply the canonical table above. If both ACF and PACF tail off, start with ARMA(1,1) and let AIC guide from there.

**Step 4: Identify seasonal structure.**
Look at lags s, 2s, 3s (where s = seasonal period). Same rules apply at seasonal lags:
- ACF cuts off at lag s → seasonal MA term (Q=1)
- PACF cuts off at lag s → seasonal AR term (P=1)
- Both tail off at seasonal lags → mixed seasonal ARMA

**Step 5: Propose 2–3 candidate models, fit all, compare AIC.**
Visual ACF/PACF identification is ambiguous in practice. Use the plots to narrow candidates, then let likelihood comparison decide.

---

## Common Patterns with Visual Descriptions

### AR(1), φ₁ > 0 (positive autoregression)

```
ACF:  ████ ███ ██ █ ·  ·  ·  ·    ← exponential decay, all positive
PACF: ████ ·  ·  · ·  ·  ·  ·    ← one spike at lag 1, then noise
```

p = 1, q = 0

### AR(1), φ₁ < 0 (negative autoregression)

```
ACF:  ████ ←neg ████ ←neg ···     ← alternating signs, decaying
PACF: ████ ·    ·    ·    ···     ← one spike at lag 1 (negative), then noise
```

p = 1, q = 0 (with negative φ₁)

### MA(1), θ₁ > 0

```
ACF:  ████ ·  ·  ·  ·  ·  ·  ·   ← one spike at lag 1, then clean cutoff
PACF: ████ ██ █  ·  ·  ·  ·  ·   ← exponential decay, alternating or monotone
```

p = 0, q = 1

### MA(2)

```
ACF:  ████ ███ ·  ·  ·  ·  ·  ·  ← two spikes, then cutoff
PACF: ████ ██  █  ·  ·  ·  ·  ·  ← tails off
```

p = 0, q = 2

### ARMA(1,1)

```
ACF:  ████ ███ ██  █  ·  ·  ·  ·  ← tails off after lag 1
PACF: ████ ███ ██  █  ·  ·  ·  ·  ← tails off after lag 1
```

Both tail off — the tailing starts from lag 1 for ACF, lag 1 for PACF. p = 1, q = 1.

---

## Numerical Example: Identifying p from PACF

Suppose you observe these PACF values for a stationary series (n=100, 95% band = ±0.196):

```
φ(1,1) =  0.72   ← significant
φ(2,2) =  0.41   ← significant
φ(3,3) =  0.08   ← inside band
φ(4,4) = -0.03   ← inside band
φ(5,5) =  0.11   ← inside band
```

**Reading:** PACF cuts off after lag 2. The ACF would show exponential decay (check to confirm AR pattern). → **AR(2): ARIMA(2,d,0).**

Theoretical ACF for AR(2) with φ₁ = 0.72, φ₂ = 0.41 satisfies the Yule-Walker equations:

```
ρ(1) = φ₁ / (1 − φ₂) = 0.72 / 0.59 ≈ 1.22  ← impossible if |φ₂| < 1 − φ₁
```

In practice you read the empirical PACF cutoff and verify the ACF decays — exact computation of theoretical ACF is not required to identify the order.

---

## Pitfalls in ACF/PACF Identification

### Pitfall 1: Treating borderline spikes as definitive

A spike at 0.20 when the band is ±0.23 is inside the band and should be ignored. Don't adjust model order for near-misses.

### Pitfall 2: Identifying order from non-stationary data

ACF/PACF on non-stationary series always shows slow decay regardless of the true AR/MA structure. Always ADF-test before reading the plots.

### Pitfall 3: Assuming MA(q) because "ACF cuts off"

An ACF that appears to cut off can also arise from a high-order AR with specific φ values. If AIC clearly favors AR over MA after fitting, defer to AIC.

### Pitfall 4: Ignoring seasonal lags

When working with weekly or monthly data, a strong spike at lag s that you misread as random can cause systematically biased forecasts. Always examine seasonal lags explicitly.

### Pitfall 5: Over-reading ARMA(1,1) ambiguity

When both ACF and PACF tail off, the starting point is ARMA(1,1). From there, compare AIC for (1,1), (2,1), (1,2), (2,2). Do not try to determine p and q independently — they interact.

---

## Python Code: Plot ACF and PACF

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller

def plot_acf_pacf(series: pd.Series, lags: int = 40, title: str = "") -> None:
    """
    Plot ACF and PACF side by side after ADF stationarity check.
    series: stationary (differenced) series
    lags: number of lags to display
    """
    adf_stat, adf_p, *_ = adfuller(series.dropna())
    stationary = "stationary" if adf_p < 0.05 else "NON-STATIONARY"

    fig, axes = plt.subplots(1, 2, figsize=(14, 4))
    fig.suptitle(f"{title} — ADF p={adf_p:.3f} ({stationary})")

    plot_acf(series.dropna(), lags=lags, ax=axes[0], zero=False)
    axes[0].set_title("ACF")

    plot_pacf(series.dropna(), lags=lags, ax=axes[1], zero=False, method="ywm")
    axes[1].set_title("PACF")

    plt.tight_layout()
    plt.show()


# Usage
# raw_series = pd.Series([...])
# plot_acf_pacf(raw_series, title="Raw")
# diff_series = raw_series.diff().dropna()
# plot_acf_pacf(diff_series, title="First difference")
```

**Note on `method="ywm"`:** statsmodels PACF offers several estimators. `"ywm"` (Yule-Walker with bias correction) is the standard for AR identification. `"ols"` is more robust for small samples but can give slightly different cutoff impressions. Either is acceptable; pick one and be consistent.

---

## Deciding Between ACF-Identified Order vs. auto_arima

| Situation | Prefer manual ACF/PACF | Prefer auto_arima |
|-----------|------------------------|-------------------|
| Series length < 100 | ✓ (auto search overfits small samples) | |
| Need interpretable rationale | ✓ | |
| Long series, seasonal | | ✓ (exhaustive AIC search is fast) |
| Batch forecasting many series | | ✓ |
| Unusual patterns (structural breaks) | ✓ (plots reveal anomalies) | |

The two approaches are complementary: use ACF/PACF to narrow the candidate space (e.g., "p ∈ {0,1}, q ∈ {0,1}"), then confirm with AIC comparison. Feeding unconstrained auto_arima with max_p=5, max_q=5 on short series is a common source of overfit.

---

## Quick Reference Card

```
After d differences, plot ACF and PACF. Read as follows:

          ACF tails off          ACF cuts off at q
PACF      ┌─────────────────┬──────────────────────┐
cuts off  │   AR(p)         │   ARMA(p,q)*          │
at p      │   → ARIMA(p,d,0)│   use AIC to resolve  │
          ├─────────────────┼──────────────────────┤
PACF      │   ARMA(p,q)*    │   MA(q)               │
tails off │   use AIC       │   → ARIMA(0,d,q)      │
          └─────────────────┴──────────────────────┘

* When both tail off, start with ARMA(1,1).

Seasonal lags (s, 2s, ...): apply same table at those lags
for P and Q in SARIMA(p,d,q)(P,D,Q,s).
```
