# Demand Fitting for Newsvendor Inputs

The newsvendor formula `Q* = F⁻¹(CR)` is only as good as the demand distribution `F`. This document covers how to estimate `μ`, `σ`, and which distribution to choose from historical sales data.

---

## Step 1 — Collect the Right Data

Use **sell-through data, not order data**. If you ordered 100 units and sold 100, you only know demand was ≥ 100. The true demand may have been 130 (stockout). This is **censored demand** and causes systematic underestimation of μ.

| Data source | Usable? | Caveat |
|---|---|---|
| Sales when never stocked out | Direct estimate of demand | Ideal |
| Sales with occasional stockouts | Censored — need correction | Common case |
| Only total sold, no per-period breakdown | Aggregated — disaggregate by period | Reduces sample size |
| Expert forecast only | No historical fit possible | See §6 |

**Minimum usable sample**: 20–30 observations per SKU for parametric fitting. Below 10, use a non-parametric approach or informative priors.

---

## Step 2 — Choose a Distribution

Use this decision table before estimating parameters:

| Condition | Recommended distribution | Reason |
|---|---|---|
| μ ≥ 30, CV < 0.5 | Normal(μ, σ) | CLT applies; negative values rare |
| μ ≥ 30, CV ≥ 0.5 | Lognormal(μ_ln, σ_ln) | Right-skewed; bounded at zero |
| μ < 20, discrete units | Poisson(λ) | Discrete; CV ≈ 1/√λ built in |
| μ < 20, variance > mean | Negative Binomial(r, p) | Overdispersed count data |
| μ ≥ 30, CV < 0.5, but negative demand impossible | Truncated Normal | When Normal's left tail is problematic |

**CV = σ / μ** (coefficient of variation). Compute this first — it is the single best guide to distribution choice.

---

## Step 3 — Estimate Parameters

### 3a. Normal Distribution

Sample estimators (MLE = method of moments here):

```
μ̂ = (1/n) Σ dᵢ
σ̂ = sqrt( (1/(n-1)) Σ (dᵢ - μ̂)² )
```

These are the sample mean and sample standard deviation. Use `n-1` (Bessel's correction) for small samples.

**Worked example** (fashion retailer, 25 weeks of a similar seasonal product):

```
Observations: [88, 112, 95, 104, 78, 130, 92, 101, 87, 115,
               99, 108, 83, 121, 97, 106, 94, 119, 85, 103,
               111, 90, 127, 96, 102]
n = 25
μ̂ = 100.8
σ̂ = 13.2
CV = 0.131  →  Normal is appropriate
```

For this product: `Q* = μ̂ + z(CR) × σ̂ = 100.8 + z(CR) × 13.2`

### 3b. Lognormal Distribution

If data is right-skewed (CV ≥ 0.5), fit in log-space:

```
yᵢ = ln(dᵢ)          # transform each observation
μ_ln = (1/n) Σ yᵢ
σ_ln = sqrt( (1/(n-1)) Σ (yᵢ - μ_ln)² )
```

Back-transform to get distribution moments:

```
E[D] = exp(μ_ln + σ_ln² / 2)
Var[D] = (exp(σ_ln²) - 1) × exp(2μ_ln + σ_ln²)
```

To get Q*: `Q* = exp( μ_ln + z(CR) × σ_ln )`  ← quantile in log-space, then exponentiate.

**Worked example** (online fashion, high-variance SKU):

```
Raw: [12, 45, 8, 310, 22, 88, 5, 190, 34, 67, 15, 420, 9, 55]
μ_raw = 91.4, σ_raw = 120.8, CV = 1.32  →  Lognormal

ln-transformed: [2.48, 3.81, 2.08, 5.74, 3.09, 4.48, 1.61, 5.25, 3.53, 4.20, 2.71, 6.04, 2.20, 4.01]
μ_ln = 3.66, σ_ln = 1.37

For CR = 0.67 (z = 0.44):
Q* = exp(3.66 + 0.44 × 1.37) = exp(4.26) ≈ 71 units
```

Note: the median (exp(μ_ln) = 38.9) and mean (91.4) differ substantially. Q* = 71 reflects neither.

### 3c. Poisson Distribution

For discrete, low-mean demand:

```
λ̂ = μ̂ = (1/n) Σ dᵢ     # MLE for Poisson
```

Poisson has one parameter: mean = variance = λ. If your sample variance >> λ̂, use Negative Binomial instead.

Q* for Poisson: smallest integer Q such that `CDF_Poisson(Q, λ̂) ≥ CR`.

**Worked example** (specialty bookstore, 18 months data):

```
Monthly sales: [2, 0, 3, 1, 4, 0, 2, 1, 3, 2, 1, 0, 4, 2, 1, 3, 0, 2]
λ̂ = 31/18 = 1.72
Sample variance = 1.39 ≈ λ̂  →  Poisson is appropriate

CR = 0.80 (high margin item)
Poisson CDF(Q=3, λ=1.72) = 0.916 ≥ 0.80  →  Q* = 3
```

---

## Step 4 — Goodness-of-Fit Check

Do not skip this. A misspecified distribution is worse than a rough estimate.

### Visual check (fast, sufficient for most decisions)

1. Plot a histogram of demand observations
2. Overlay the fitted PDF
3. Check for: skewness, heavy tails, bimodality, mass at zero

### Quantitative check (when precision matters)

Use the **Kolmogorov-Smirnov statistic** or **Anderson-Darling test** (AD is more sensitive to tails, which matter for newsvendor since CR often pushes Q* into the tail):

```python
from scipy import stats

data = [88, 112, 95, 104, 78, ...]  # your observations
mu_hat, sigma_hat = np.mean(data), np.std(data, ddof=1)

# KS test
stat, p_value = stats.kstest(data, 'norm', args=(mu_hat, sigma_hat))
# p_value < 0.05 means reject Normal at 5% significance

# Anderson-Darling test
result = stats.anderson(data, dist='norm')
# result.statistic vs. result.critical_values
```

**Practical threshold**: if n < 30, these tests have low power — use visual inspection plus domain knowledge. Only reject a distribution if the visual fit is obviously wrong or the test p-value is very small (< 0.01).

---

## Step 5 — Correcting for Censored Demand (Stockouts)

When you ran out of stock in some periods, your recorded sales understate true demand. Ignoring this biases μ̂ downward and causes systematic under-ordering.

### Simple correction: Kaplan-Meier for demand

For each period `t`, record:
- `sₜ` = units sold
- `cₜ` = 1 if stocked out (demand censored), 0 otherwise
- `Qₜ` = stock level at start of period

Use the **EM algorithm** (iterative):

```
E-step: For censored periods, estimate E[Dₜ | Dₜ ≥ Qₜ, μ, σ]
        = μ + σ × φ(z_t) / (1 - Φ(z_t))   where z_t = (Qₜ - μ) / σ
        (this is the mean of a truncated normal above Qₜ)

M-step: Update μ, σ using all periods, replacing censored dₜ with E[Dₜ]

Repeat until convergence (|Δμ| < 0.01)
```

**Rule of thumb**: if fewer than 20% of periods were stockouts, the bias in simple sample mean is small (< 5%). If > 30% of periods were stockouts, censoring correction is essential.

---

## Step 6 — Sparse Data: Bayesian Updating

When you have fewer than 10 historical observations (new product launch, infrequent item), use a **conjugate prior** approach.

### Normal model with known σ (simplest case)

Start with a prior belief `μ ~ Normal(μ₀, σ₀²)` based on:
- Analogous product historical data
- Buyer/merchandiser expert estimate

After observing `n` sales periods with sample mean `x̄`:

```
Posterior mean: μ_post = (σ²/n × μ₀ + σ₀² × x̄) / (σ²/n + σ₀²)
Posterior variance: σ_post² = 1 / (n/σ² + 1/σ₀²)
```

Use `μ_post` and `sqrt(σ_post² + σ²)` (predictive std) in the newsvendor formula.

**Worked example** (new product, μ₀ = 100 from analogous SKU, σ₀ = 20 representing prior uncertainty, σ = 15 assumed from category):

```
After 5 periods: x̄ = 80
μ_post = (225/5 × 100 + 400 × 80) / (225/5 + 400)
       = (4500 + 32000) / (45 + 400)
       = 36500 / 445 ≈ 82.0
σ_post = sqrt(1 / (5/225 + 1/400)) = sqrt(1 / (0.0222 + 0.0025)) ≈ 20.1
Predictive σ = sqrt(20.1² + 15²) ≈ 25.0

Q* = 82.0 + z(CR) × 25.0
```

The posterior is pulled toward x̄ = 80 but with more uncertainty than pure sample estimate. This conservatism is appropriate: with only 5 observations, you genuinely don't know if demand shifted or you got unlucky.

### Bayesian updating from early in-season signals

If early sales are observable before the full season (e.g., first 2 weeks of a 12-week season), update the prior mid-season:

```
Ratio signal: r = early_sales / expected_early_sales
Revised μ̂ = original_μ̂ × r  (simple multiplicative update)
```

Blend with original estimate using a credibility weight `Z = n_early / (n_early + k)` where k ≈ 20 is a smoothing constant:

```
μ_revised = Z × (μ̂ × r) + (1 - Z) × μ̂
```

---

## Common Mistakes

**Using order quantities as demand estimates.** Orders are constrained by what you decide to stock, not by what customers wanted. Always trace back to POS data or lost-sale estimates.

**Fitting to aggregate (weekly/monthly) when ordering at SKU level.** If your demand distribution is fitted to product-family totals, applying it to individual SKUs will understate variance by √n (diversification effect).

**Treating the fitted distribution as certain.** Parameter uncertainty adds to Q* uncertainty. When σ̂ is estimated from few observations, widen your predictive interval by adding `σ̂ × t(α/2, n-1) / √n` to cover estimation error.

**Ignoring seasonality.** If demand is seasonal, fitting a single Normal to all historical periods mixes different underlying distributions. Segment by season or apply a seasonal index before fitting.

**CV threshold is not universal.** The CV ≥ 0.5 → lognormal rule is a heuristic, not a law. Always check with a histogram. Some high-CV products have bimodal demand (hit/miss dynamics) that neither Normal nor lognormal captures — in those cases, consider a mixture model or use empirical quantiles directly.
