# Non-Normal Capability Analysis

Standard Cpk assumes the process output follows a normal distribution. When that assumption breaks down, Cpk both misestimates the true defect rate and gives misleading process comparisons. This reference covers how to detect non-normality, which remedy to apply, and how to compute capability correctly under each method.

---

## Why Non-Normality Breaks Cpk

Cpk converts σ into a defect-rate estimate via the normal-distribution tail. The lookup table below shows what standard Cpk implies vs. what actually happens when the distribution is right-skewed (shape typical of flatness, concentricity, contamination counts).

| Cpk (computed with normal formula) | Implied PPM (normal) | Actual PPM if skewness = 1.5 |
|-------------------------------------|----------------------|-------------------------------|
| 1.00 | 2,700 | ~8,000–15,000 |
| 1.33 | 63 | ~500–2,000 |
| 1.67 | 0.6 | ~20–200 |

The actual tail exposure on the right side (where most defects occur for right-skewed data) is far larger than normal-Cpk suggests. A process that looks capable at Cpk = 1.33 may be producing orders-of-magnitude more defects than the 63 PPM implied value.

---

## Step 1: Detect Non-Normality

Run both a statistical test and a visual check. Either failure is grounds to proceed with a non-normal method.

### Statistical Test: Shapiro-Wilk

Use Shapiro-Wilk for n < 2000; Anderson-Darling for larger samples.

```python
from scipy import stats
import numpy as np

data = np.array([...])  # your process measurements
stat, p = stats.shapiro(data)
print(f"W={stat:.4f}, p={p:.4f}")
# p < 0.05 → reject normality at 95% confidence
```

**Decision rule:** p < 0.05 triggers non-normal analysis. If 0.05 ≤ p < 0.10, also inspect the probability plot visually.

### Visual Check: Normal Probability Plot

Points following the diagonal line = normal. S-curve = kurtosis. Concave-up curve = right skew. Concave-down = left skew.

```python
import matplotlib.pyplot as plt
from scipy.stats import probplot

fig, ax = plt.subplots()
probplot(data, dist="norm", plot=ax)
ax.set_title("Normal Probability Plot")
plt.show()
```

### Quantify Skewness and Kurtosis

```python
skew = stats.skew(data)
kurt = stats.kurtosis(data)  # excess kurtosis; normal = 0
print(f"Skewness: {skew:.3f}, Excess Kurtosis: {kurt:.3f}")
```

| |Normal range | Action |
|---|---|---|
| \|skewness\| | < 0.5 | Proceed with standard Cpk |
| \|skewness\| | 0.5 – 1.5 | Mild: try Box-Cox first |
| \|skewness\| | > 1.5 | Severe: use percentile method or Johnson |
| \|kurtosis\| | > 3 | Heavy tails: use percentile method |

---

## Step 2: Choose a Method

Three methods cover the practical range of non-normal situations.

```
Decision table:

Bounded below zero (e.g. flatness, roughness)?
  → Yes: Box-Cox (log family) or percentile method
  → No, but still non-normal: Johnson transformation or percentile method

One-sided spec only?
  → Percentile method is simplest and most defensible

Customer requires a specific standard?
  → Check if they mandate ISO 22514-3 (percentile / quantile method)

Transformation produces normal p > 0.10?
  → Use transformed Cpk
  → Otherwise: fall back to percentile method
```

---

## Method A: Box-Cox Transformation

### Formula

For λ ≠ 0:
```
y = (x^λ − 1) / λ
```
For λ = 0:
```
y = ln(x)
```

The optimal λ is the value that maximizes the log-likelihood of normality on the transformed data. In practice, λ is constrained to interpretable values: {−2, −1, −0.5, 0, 0.5, 1, 2}.

### Procedure

**Step 1.** Fit λ using maximum likelihood:

```python
from scipy.stats import boxcox, shapiro

data_positive = data - data.min() + 0.001  # Box-Cox requires x > 0
transformed, lam = boxcox(data_positive)
stat, p = shapiro(transformed)
print(f"Optimal λ={lam:.3f}, Shapiro p={p:.4f}")
```

**Step 2.** Verify the transformed data passes normality (p ≥ 0.10 recommended, p ≥ 0.05 minimum).

**Step 3.** Transform the specification limits using the same λ:

```
USL_t = (USL^λ − 1) / λ
LSL_t = (LSL^λ − 1) / λ
```

⚠️ **Critical:** the transformation is nonlinear, so USL and LSL must be transformed before computing Cpk — do NOT transform specs linearly.

**Step 4.** Compute Cpk on the transformed space using the standard formula:

```
μ_t = mean(transformed data)
σ_t = within-subgroup σ on transformed data (R̄/d₂)
Cpk = min((USL_t − μ_t) / 3σ_t,  (μ_t − LSL_t) / 3σ_t)
```

### Worked Example

**Raw data:** flatness measurements (µm), n=150. Shapiro-Wilk p=0.003, skewness=1.8.  
**Specs:** LSL=0 (impossible by physics, use 0.001), USL=20 µm.  
**Measurements summary:** mean=8.4, σ_overall=4.2.

Naïve Cpk = min((20−8.4)/(3×4.2), (8.4−0.001)/(3×4.2)) = min(0.92, 0.67) = **0.67**.  
This uses overall σ and ignores skew — both wrong.

After Box-Cox (λ=0.18 ≈ near log), transformed data passes Shapiro p=0.14.

```
USL_t = (20^0.18 − 1) / 0.18 = (1.714 − 1) / 0.18 = 3.967
LSL_t = (0.001^0.18 − 1) / 0.18 ≈ (0.301 − 1) / 0.18 = −3.883
μ_t = 3.01 (from transformed sample)
σ_t = 0.52 (within-subgroup, R̄/d₂ on transformed data)
```

```
Cpk = min((3.967 − 3.01)/(3×0.52), (3.01 − (−3.883))/(3×0.52))
    = min(0.957/1.56, 6.893/1.56)
    = min(0.61, 4.42) = 0.61
```

The USL tail is limiting — same conclusion as naïve Cpk directionally, but the magnitude differs. Correct PPM from the transformed normal:

```python
from scipy.stats import norm
z_upper = (3.967 - 3.01) / 0.52  # = 1.84
ppm = norm.sf(z_upper) * 1e6  # = ~32,900 PPM
```

Naïve normal Cpk=0.67 implied ~50,000 PPM — different, but the order of magnitude is similar here. For more skewed distributions, the gap grows substantially.

### Box-Cox Limitations

- Requires all data > 0 (shift required for data including 0)
- λ estimated from data introduces uncertainty; report with confidence interval
- Not applicable when data has multimodality (bimodal → mixture model required)
- The transformed Cpk value cannot be directly compared to normal-data Cpk benchmarks (1.33, 1.67) without re-deriving PPM

---

## Method B: Percentile Method (ISO 22514-3 / Clements)

This method makes no distributional assumption. It reads capability directly from the empirical (or fitted) percentile positions.

### Formula

```
Cp_np  = (USL − LSL) / (X_99.865% − X_0.135%)
Cpk_np = min((USL − X_50%) / (X_99.865% − X_50%),
             (X_50% − LSL) / (X_50% − X_0.135%))
         × (1/3)    ← scaling factor so Cpk_np = 1.0 matches 3σ spread
```

Where X_p% is the p-th percentile of the process distribution. The 0.135% and 99.865% percentiles correspond to ±3σ quantiles of the standard normal — preserving the conventional Cpk scale.

**Simplified form** (how ISO 22514-3 writes it):

```
Let M = X_50%  (process median)
Let U = X_99.865%
Let L = X_0.135%

Cp_np  = (USL − LSL) / (U − L)
CPU_np = (USL − M) / (U − M)   × (1/3)... no
```

Actually the ISO 22514-3 formulation is:

```
CPU_np = (USL − M) / (U − M)
CPL_np = (M − LSL) / (M − L)
Cpk_np = min(CPU_np, CPL_np)
```

No ×(1/3) scaling — this directly gives a ratio of spec distance to tail distance. A value of 1.0 means the spec limit exactly coincides with the 0.135% or 99.865% tail.

### Computing Percentiles

**Option 1: Empirical (n ≥ 300)**

```python
import numpy as np
p_low  = np.percentile(data, 0.135)
p_med  = np.percentile(data, 50)
p_high = np.percentile(data, 99.865)
```

⚠️ With n < 300, the 0.135% and 99.865% percentiles are estimated from fewer than 1 data point on average. Unreliable — use a fitted distribution instead.

**Option 2: Fitted Distribution (n < 300)**

Fit a parametric non-normal distribution, then read off theoretical percentiles:

```python
from scipy import stats

# Try Weibull (common for flatness, fatigue life, surface finish)
params = stats.weibull_min.fit(data, floc=0)
p_low  = stats.weibull_min.ppf(0.00135, *params)
p_med  = stats.weibull_min.ppf(0.50,    *params)
p_high = stats.weibull_min.ppf(0.99865, *params)

# Validate fit
ks_stat, ks_p = stats.kstest(data, 'weibull_min', args=params)
print(f"KS test p={ks_p:.4f}")  # p > 0.05 = acceptable fit
```

Common distributions for manufacturing data:

| Process type | Typical distribution | Scipy name |
|---|---|---|
| Flatness, roundness | Weibull or lognormal | `weibull_min`, `lognorm` |
| Surface roughness Ra | Lognormal | `lognorm` |
| Particle counts | Gamma | `gamma` |
| Cycle times with outliers | Lognormal or gamma | `lognorm`, `gamma` |
| Concentricity (always ≥ 0) | Rayleigh or Weibull | `rayleigh`, `weibull_min` |
| Burr height | Extreme value (Gumbel) | `gumbel_r` |

### Worked Example

**Data:** surface roughness Ra, n=120. Shapiro p=0.001, skewness=2.1 (right-skewed, bounded at 0).  
**Specs:** USL=3.2 µm, LSL=0 (use 0 as lower bound — one-sided effectively).

Fit lognormal:

```python
params = stats.lognorm.fit(data, floc=0)  # (s, loc, scale)
# Suppose fit gives: s=0.45, loc=0, scale=1.21
p_low  = stats.lognorm.ppf(0.00135, *params)  # = 0.38
p_med  = stats.lognorm.ppf(0.50,    *params)  # = 1.21
p_high = stats.lognorm.ppf(0.99865, *params)  # = 3.94
```

```
CPU_np = (USL − M) / (U − M)
       = (3.2 − 1.21) / (3.94 − 1.21)
       = 1.99 / 2.73 = 0.73

CPL_np = (M − LSL) / (M − L)
       = (1.21 − 0) / (1.21 − 0.38)
       = 1.21 / 0.83 = 1.46

Cpk_np = min(0.73, 1.46) = 0.73
```

The upper tail is the problem — process is failing USL with significant frequency. Actual PPM:

```python
ppm_upper = stats.lognorm.sf(3.2, *params) * 1e6  # ~28,000 PPM
```

A naïve normal Cpk using the mean and overall σ of this data would have given a different (and wrong) answer.

### Percentile Method Strengths and Weaknesses

**Strengths:**
- Distribution-free for large n
- Directly interpretable: Cpk_np = 1.0 means 3.4 PPM on that side (same as normal Cpk = 1.0... roughly)
- Accepted by ISO 22514-3 and AIAG for non-normal data

**Weaknesses:**
- Requires large n for reliable extreme-percentile estimates
- Results vary with different percentile estimation algorithms (type 6 vs type 7 in numpy)
- For small n, depends heavily on the distributional assumption made during fitting

---

## Method C: Johnson Transformation System

The Johnson system fits one of three families (S_B, S_L, S_U) to match any combination of skewness and kurtosis. More flexible than Box-Cox but requires fitting 4 parameters.

Use Johnson when:
- Box-Cox fails to normalize the data (post-transform Shapiro still p < 0.05)
- The distribution has both skewness and excess kurtosis

```python
# Using scipy's johnsonsu / johnsonnb, or statsmodels
# (No built-in Johnson fitting in standard scipy — use pingouin or custom)

# Alternatively, use a pre-built implementation:
# pip install reliability  (for full Johnson fitting)
```

In practice, if Box-Cox fails and empirical percentiles are available (n ≥ 300), the percentile method is simpler and equally valid. Johnson is most useful for moderate n (50–300) where Box-Cox fails.

---

## Reporting Non-Normal Capability

Always document which method was used. A bare "Cpk = 0.73" is ambiguous.

### Required Report Fields

```json
{
  "capability": {
    "method": "percentile_lognormal",
    "cpk_np": 0.73,
    "cpu_np": 0.73,
    "cpl_np": 1.46,
    "ppm_defective_upper": 28000,
    "ppm_defective_lower": 12
  },
  "distribution_fit": {
    "family": "lognormal",
    "params": {"s": 0.45, "loc": 0, "scale": 1.21},
    "ks_test_p": 0.18
  },
  "normality": {
    "shapiro_p": 0.001,
    "skewness": 2.1,
    "excess_kurtosis": 5.3
  },
  "specs": {"usl": 3.2, "lsl": 0},
  "metadata": {"n": 120, "sigma_method": "lognormal_percentile"}
}
```

### Benchmark Targets for Non-Normal Cpk_np

The same thresholds apply when the percentile method preserves the scale (Cpk_np = 1.0 ≈ 2700 PPM):

| Cpk_np | Classification | Typical requirement |
|--------|----------------|---------------------|
| < 1.00 | Incapable | Process producing defects |
| 1.00 – 1.33 | Marginal | Under watch; improvement required |
| 1.33 – 1.67 | Capable | General manufacturing |
| ≥ 1.67 | Highly capable | Safety-critical, Tier 1 automotive |

⚠️ If using Box-Cox Cpk, re-derive the PPM from the transformed-space z-scores and report actual PPM alongside the index — the index alone is not comparable to normal-Cpk benchmarks.

---

## Quick Reference: Non-Normal Capability Workflow

```
1. Collect data (n ≥ 100 minimum; n ≥ 300 for percentile method)
2. Run Shapiro-Wilk + probability plot
   → p ≥ 0.05 AND no visual S-curve → use standard Cpk (SKILL.md Phase 2)
   → p < 0.05 OR visible departure → continue below

3. Compute skewness and kurtosis
   → |skewness| < 0.5, |kurtosis| < 3 → borderline; try both methods
   → |skewness| ≥ 0.5 or |kurtosis| ≥ 3 → non-normal method required

4. Select method:
   a. n ≥ 300 → percentile method (empirical, no distributional assumption)
   b. n = 100–299 → fit distribution (Weibull/lognormal), use fitted percentiles
   c. Transformation preferred by customer → Box-Cox (validate with Shapiro p ≥ 0.05)
   d. Box-Cox fails → Johnson or percentile method

5. Validate distribution fit (KS test p ≥ 0.05)

6. Compute Cpk_np or transformed Cpk

7. Report: method, distribution family, KS p-value, PPM estimate, and Cpk index
```
