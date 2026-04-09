# Intermittent Demand Methods for Safety Stock

Intermittent (or "lumpy") demand — characterised by many zero-demand periods interspersed with sporadic positive demands — breaks the normal distribution assumption underpinning the standard safety stock formula. Using z × σ_combined on such data produces either absurd over-stock (when σ is inflated by zeros) or severe under-stock (when periods are aggregated to hide the sparsity).

This file covers: how to detect intermittent demand, why normal-based SS fails, and three tractable alternatives — Poisson SS, the Croston / SBA forecast, and Negative Binomial SS.

---

## 1. Detecting Intermittent Demand

Two statistics classify demand patterns:

| Statistic | Definition | Threshold |
|-----------|-----------|-----------|
| **ADI** (Average Demand Interval) | average number of periods between non-zero demands | ADI ≥ 1.32 → intermittent |
| **CV²** (squared coefficient of variation of non-zero demand sizes) | (σ_nonzero / μ_nonzero)² | CV² ≥ 0.49 → "lumpy" |

Classification matrix (Syntetos–Boylan–Croston 2005):

```
              CV² < 0.49          CV² ≥ 0.49
ADI < 1.32    Smooth              Erratic
ADI ≥ 1.32    Intermittent        Lumpy
```

- **Smooth / Erratic**: use standard normal-based safety stock.
- **Intermittent**: use Croston or Poisson methods.
- **Lumpy**: use Negative Binomial or Croston/SBA with caution; empirical simulation often beats parametric methods here.

### Computing ADI and CV² in practice

```python
import statistics

def classify_demand(periods: list[float]) -> dict:
    """
    periods: list of demand values per period (may contain zeros)
    returns ADI, CV2, and classification
    """
    n = len(periods)
    nonzero = [x for x in periods if x > 0]
    zero_count = n - len(nonzero)

    if len(nonzero) < 2:
        return {"adi": float("inf"), "cv2": 0.0, "class": "lumpy"}

    # ADI: average interval between demands
    # Count gaps between demand occurrences
    indices = [i for i, x in enumerate(periods) if x > 0]
    gaps = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    adi = statistics.mean(gaps) if gaps else float("inf")

    # CV² of non-zero demand sizes
    mu = statistics.mean(nonzero)
    sigma = statistics.pstdev(nonzero)
    cv2 = (sigma / mu) ** 2 if mu > 0 else 0.0

    if adi < 1.32 and cv2 < 0.49:
        cls = "smooth"
    elif adi < 1.32:
        cls = "erratic"
    elif cv2 < 0.49:
        cls = "intermittent"
    else:
        cls = "lumpy"

    return {"adi": round(adi, 2), "cv2": round(cv2, 3), "class": cls}
```

---

## 2. Why Normal-Based Safety Stock Fails

**Example:** Weekly demand over 20 weeks:
```
0, 0, 0, 5, 0, 0, 12, 0, 0, 0, 3, 0, 0, 0, 8, 0, 0, 0, 0, 6
```

Normal-distribution approach:
- Mean d = 34/20 = 1.7 units/week
- σ = 3.4 (inflated by zeros)
- CV = 3.4/1.7 = 2.0 (CV² = 4.0 — clearly lumpy)
- SS at 95%: 1.65 × 3.4 = 5.6 units per week

The problem: demand is not 1.7 units every week — it arrives in bursts of 3–12 units every 4–5 weeks. The normal model treats every period as equally risky. It will either chronically over-stock (holding 5+ units in all the zero weeks) or under-stock in burst weeks.

**The actual risk** is: what is the probability that total demand over the lead time exceeds the stock on hand? For lumpy demand this must be modelled at the **lead-time aggregate level**, not period-by-period.

---

## 3. Method A: Poisson Safety Stock

Use when: ADI ≥ 1.32, CV² < 0.49 (intermittent, not lumpy — demand sizes are relatively consistent when they occur).

### Rationale

If demand events arrive independently and infrequently, the count of demand events over lead time follows a Poisson distribution. When demand sizes are roughly constant, total demand over LT is also approximately Poisson.

### Formula

Let:
- λ = expected total demand over lead time = d̄ × LT (in same time units)
- SS = F⁻¹_Poisson(SL, λ) − λ

where F⁻¹_Poisson(SL, λ) is the smallest integer k such that the Poisson CDF P(X ≤ k | λ) ≥ SL.

Reorder point = F⁻¹_Poisson(SL, λ) (the safety stock is implicitly embedded).

### Worked Example

**Input:**
- Weekly demand (non-zero weeks only): 4, 6, 5, 7, 4 units
- Demand occurs in roughly 1 out of 4 weeks → ADI ≈ 4.0
- CV² of non-zero sizes ≈ 0.17 → intermittent (not lumpy)
- d̄ = 5 units/occurrence × (1/4 occurrences/week) = 1.25 units/week
- Lead time = 3 weeks
- Target: 95% cycle service level

**Step 1:** λ = 1.25 × 3 = 3.75 units over lead time

**Step 2:** Find F⁻¹_Poisson(0.95, 3.75):

| k | P(X=k) | P(X≤k) |
|---|--------|--------|
| 0 | 0.0235 | 0.0235 |
| 1 | 0.0882 | 0.1107 |
| 2 | 0.1654 | 0.2761 |
| 3 | 0.2067 | 0.4828 |
| 4 | 0.1938 | 0.6766 |
| 5 | 0.1454 | 0.8220 |
| 6 | 0.0909 | 0.9129 |
| **7** | **0.0487** | **0.9616** |

F⁻¹(0.95, 3.75) = 7 (first k where CDF ≥ 0.95)

**Step 3:** Reorder point = 7 units. SS = 7 − 3.75 = 3.25 → round to **3 units**.

Compare to naive normal: SS = 1.65 × √3.75 ≈ 3.2 units. Happens to agree here because Poisson approximates normal at larger λ. At λ < 2 the difference becomes significant and Poisson is correct.

### Python snippet

```python
import math

def poisson_cdf(k: int, lam: float) -> float:
    """P(X <= k) for Poisson(lam)."""
    total = 0.0
    term = math.exp(-lam)
    for i in range(k + 1):
        total += term
        term *= lam / (i + 1)
    return total

def poisson_reorder_point(lam: float, service_level: float) -> int:
    """Smallest k such that P(X <= k) >= service_level."""
    k = 0
    while poisson_cdf(k, lam) < service_level:
        k += 1
    return k

def poisson_safety_stock(
    avg_demand_per_period: float,
    lead_time_periods: float,
    service_level: float,
) -> dict:
    lam = avg_demand_per_period * lead_time_periods
    rop = poisson_reorder_point(lam, service_level)
    ss = rop - lam
    return {
        "lambda": round(lam, 3),
        "reorder_point": rop,
        "safety_stock": math.ceil(ss),
        "actual_service_level": round(poisson_cdf(rop, lam), 4),
    }
```

---

## 4. Method B: Croston's Method and SBA for Demand Forecasting

Croston and SBA do not directly output a safety stock figure — they produce a **demand rate forecast** and an associated **variance**, which you then feed into either the Poisson model or the normal model.

Use when: you need a forward-looking demand rate (not just historical mean) for an intermittent SKU, before computing SS.

### Croston's Method

Croston (1972) separately smooths two series:
- **q̂** = smoothed non-zero demand size
- **p̂** = smoothed inter-demand interval

Demand rate forecast: ẑ = q̂ / p̂

**Algorithm:**

```
Initialise: q̂₁ = first non-zero demand, p̂₁ = 1
For each period t:
  if demand[t] > 0:
    q̂ₜ = α × demand[t] + (1−α) × q̂ₜ₋₁
    p̂ₜ = α × interval_since_last_demand + (1−α) × p̂ₜ₋₁
  else:
    q̂ₜ = q̂ₜ₋₁, p̂ₜ = p̂ₜ₋₁

Forecast: ẑₜ = q̂ₜ / p̂ₜ  (demand per period)
```

Typical α: 0.1 – 0.2 for slow-moving items.

### Syntetos–Boylan Approximation (SBA)

Croston's estimator is biased upward. SBA corrects it:

```
ẑ_SBA = (1 − α/2) × (q̂ / p̂)
```

SBA is recommended over Croston in virtually all empirical studies. Use Croston only as a baseline.

### Worked Example

Demand series (24 months):
```
0,0,3,0,0,0,5,0,0,4,0,0,0,0,6,0,0,3,0,0,0,7,0,0
```
α = 0.15

Trace through non-zero events (periods 3, 7, 10, 15, 18, 22):

| Event | Period | Demand | Interval | q̂     | p̂     | ẑ_SBA  |
|-------|--------|--------|----------|--------|--------|--------|
| 1     | 3      | 3      | —        | 3.000  | 1.000  | —      |
| 2     | 7      | 5      | 4        | 3.300  | 1.450  | 2.142  |
| 3     | 10     | 4      | 3        | 3.355  | 1.733  | 1.826  |
| 4     | 15     | 6      | 5        | 3.752  | 2.073  | 1.709  |
| 5     | 18     | 3      | 3        | 3.589  | 2.012  | 1.684  |
| 6     | 22     | 7      | 4        | 4.051  | 2.060  | 1.858  |

After period 22: q̂ = 4.05, p̂ = 2.06, ẑ_SBA = (1 − 0.075) × (4.05/2.06) = **1.82 units/month**.

Feed ẑ_SBA into the Poisson model as `avg_demand_per_period = 1.82`.

---

## 5. Method C: Negative Binomial Safety Stock

Use when: ADI ≥ 1.32 AND CV² ≥ 0.49 (lumpy — demand sizes vary widely).

### Why Negative Binomial

Negative Binomial (NB) is a compound distribution that models both:
- The randomness in whether demand occurs (Poisson-like)
- The randomness in how much demand occurs when it does (Gamma-like)

It has two parameters, r and p, which can match both the mean and variance of observed lead-time demand.

### Parameter Estimation

Given observed lead-time demand samples with mean μ and variance σ²:

- Condition: σ² > μ (over-dispersion — if σ² ≤ μ, use Poisson instead)
- r = μ² / (σ² − μ)
- p = μ / σ²

NB CDF gives P(X ≤ k), and the reorder point is the smallest k where P(X ≤ k) ≥ SL.

### Worked Example

**Lead-time demand observations** (over 30 replenishment cycles):

Observed values: mostly zeros plus occasional bursts of 10–40 units.
- μ = 8.0 units per lead time
- σ² = 64.0 (measured, not inferred — track lead-time totals directly)

Check: σ² = 64 > μ = 8 → use NB.

**Parameters:**
- r = 8² / (64 − 8) = 64 / 56 = **1.143**
- p = 8 / 64 = **0.125**

**NB CDF** (using scipy, or the recursive formula below):

| k  | P(X ≤ k) |
|----|---------|
| 0  | 0.127   |
| 5  | 0.422   |
| 10 | 0.637   |
| 15 | 0.790   |
| 20 | 0.882   |
| 25 | 0.934   |
| 30 | **0.962** |

At 95% SL: reorder point = **30 units**, SS = 30 − 8 = **22 units**.

Compare to normal-based: SS = 1.65 × √64 = 13.2 units — a 40% under-estimate.

### Python snippet (no scipy)

```python
import math

def nb_pmf(k: int, r: float, p: float) -> float:
    """P(X = k) for NB(r, p). Mean = r(1-p)/p."""
    # Using NB parameterisation: r = num successes, p = prob success
    # Mean = r(1-p)/p, Var = r(1-p)/p^2
    log_coeff = math.lgamma(k + r) - math.lgamma(r) - math.lgamma(k + 1)
    return math.exp(log_coeff) * (p ** r) * ((1 - p) ** k)

def nb_reorder_point(mu: float, var: float, service_level: float) -> dict:
    """
    mu, var: mean and variance of lead-time demand (observed).
    Returns reorder point and safety stock.
    """
    if var <= mu:
        raise ValueError("var <= mu: use Poisson, not NegBin")
    r = mu ** 2 / (var - mu)
    p = mu / var          # P(success) in NB parameterisation

    k = 0
    cdf = 0.0
    while cdf < service_level:
        cdf += nb_pmf(k, r, p)
        k += 1
    rop = k - 1
    return {
        "r": round(r, 4),
        "p": round(p, 4),
        "reorder_point": rop,
        "safety_stock": rop - round(mu),
        "actual_service_level": round(cdf, 4),
    }
```

---

## 6. Method Selection Decision Table

| Condition | Method |
|-----------|--------|
| ADI < 1.32, CV² < 0.49 | Standard normal SS (see SKILL.md) |
| ADI < 1.32, CV² ≥ 0.49 | Normal SS, but use robust σ estimate (trimmed mean) |
| ADI ≥ 1.32, CV² < 0.49 | **Poisson SS** |
| ADI ≥ 1.32, CV² ≥ 0.49 | **Negative Binomial SS** |
| < 10 non-zero observations | Empirical simulation or judgment; no parametric method is reliable |
| Demand is integer, discrete | Always prefer discrete distributions (Poisson, NB) over normal |

**Quick heuristic:** If more than 40% of periods are zero, do not use the standard normal safety stock formula under any circumstances.

---

## 7. Estimating σ² at Lead-Time Aggregate Level

All parametric methods need μ and σ² of **total demand over the lead time**, not per-period demand. Two approaches:

### Approach 1: Direct measurement (preferred)

For each historical replenishment cycle, record the total demand received while awaiting the order. Compute mean and variance directly from these totals.

This automatically incorporates both demand variability and lead time variability without needing to separate them — no compound formula required.

### Approach 2: Compound formula (when LT data is short)

If you only have per-period demand and an estimated LT distribution:

- E[D_LT] = d̄ × LT̄
- Var[D_LT] = LT̄ × σ²_d + d̄² × σ²_LT  ← this is the SKILL.md formula

For Poisson/NB, plug these computed μ and σ² into the distribution fitting step. The formula still holds; only the final distribution changes.

---

## 8. Gotchas Specific to Intermittent Demand

**Zeros are data, not missing values.** Do not drop zero-demand periods when computing statistics. The frequency of zeros is precisely what makes demand intermittent and must be represented in the model.

**Lead-time aggregation changes the distribution.** A Poisson per-period demand summed over 5 periods is still Poisson (additive property). A NB per-period demand summed over multiple periods is NOT simply NB — use compound formulas or direct measurement.

**Croston/SBA forecasts ≠ safety stock.** They give a demand rate estimate; you still need a distribution (Poisson or NB) and a service level to translate that into SS.

**Backorders in intermittent items are often very costly.** When mean demand is 1–2 units/month and lead time is 4 weeks, a single stockout can mean a 4-week backorder. The asymmetry between holding cost (low, because the item is cheap per period) and stockout cost (high, because customers wait weeks) often justifies a higher service level than ABC rank alone would suggest.

**Do not use fill rate (β) service level with Poisson model.** The Poisson model natively computes cycle service level (P(no stockout per cycle)). Converting to fill rate requires additional computation. Stick to cycle SL unless the business explicitly measures fill rate, then apply the Type II service level formula for discrete distributions.
