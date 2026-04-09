# Lee-Padmanabhan-Whang Bullwhip Model

Source: Lee, H.L., Padmanabhan, V., & Whang, S. (1997). "Information Distortion in a Supply Chain: The Bullwhip Effect." *Management Science*, 43(4), 546–558.

---

## Core Theorem

In a two-stage supply chain where the retailer uses an AR(1) demand process and a simple moving average forecast, the variance of retailer orders always exceeds the variance of consumer demand. The amplification factor is quantifiable and grows with lead time and forecast window size.

**Demand process (AR(1)):**

```
D_t = μ + ρ·D_{t-1} + ε_t
```

Where:
- `D_t` = consumer demand at period t
- `μ` = base demand
- `ρ` ∈ (–1, 1) = autocorrelation coefficient
- `ε_t` ~ i.i.d. N(0, σ²) = white noise

---

## Minimum Bullwhip Amplification Formula

For a retailer using **p-period moving average** to forecast and ordering to a **reorder point** with lead time **L**:

```
Var(q_t) / Var(D_t) ≥ 1 + (2L/p) + (2L²/p²)
```

Where:
- `q_t` = retailer's order quantity at period t
- `L` = replenishment lead time (periods)
- `p` = moving average window (periods)

This is the **lower bound** — the minimum possible bullwhip ratio given rational ordering behavior. Real ratios are typically higher due to batch constraints and promotions.

---

## Derivation (Condensed)

**Step 1: Forecast demand for lead time L**

The retailer needs to estimate total demand over the next L periods:

```
D̂_{t,L} = Σ_{i=1}^{L} E[D_{t+i} | I_t]
```

Using p-period moving average to estimate μ̂:

```
μ̂_t = (1/p) · Σ_{j=0}^{p-1} D_{t-j}
```

Lead-time demand forecast:

```
D̂_{t,L} = L · μ̂_t
```

**Step 2: Variance of forecast**

```
Var(D̂_{t,L}) = L² · Var(μ̂_t) = L² · (σ²/p) · [(1 + ρ)/(1 – ρ)] · [correction term]
```

For simplicity, in the i.i.d. case (ρ = 0):

```
Var(D̂_{t,L}) = L² · σ² / p
```

**Step 3: Safety stock adjustment**

Order-up-to level: `S_t = D̂_{t,L} + z · σ̂_L`

The retailer adjusts `S_t` each period. The change in S_t drives order variance:

```
q_t = D_{t-1} + (S_t – S_{t-1})
```

```
Var(q_t) = Var(D_t) + Var(S_t – S_{t-1})
```

Because `S_t` updates with each new demand observation:

```
Var(S_t – S_{t-1}) = Var(D̂_{t,L} – D̂_{t-1,L}) = (2L²/p) · σ²    [i.i.d. case]
```

Final result:

```
Var(q_t) / Var(D_t) = 1 + 2L/p + 2L²/p²
```

---

## Worked Numerical Example

**Setup:**
- Consumer demand: i.i.d., mean = 100, σ = 10, so Var(D) = 100
- Lead time: L = 3 weeks
- Moving average window: p = 4 weeks

**Step 1: Compute amplification ratio**

```
Ratio = 1 + (2·3/4) + (2·9/16)
      = 1 + 1.5 + 1.125
      = 3.625
```

**Step 2: Compute order variance**

```
Var(q) = 3.625 × 100 = 362.5
Std(q) = √362.5 ≈ 19.0
```

**Step 3: Interpretation**

| Metric | Consumer Demand | Retailer Orders |
|--------|----------------|-----------------|
| Mean | 100 | 100 |
| Std Dev | 10 | 19 |
| CV | 10% | 19% |
| Bullwhip Ratio | — | **3.625** |

A retail demand CV of 10% becomes a 19% order CV — without any external disturbance, purely from forecast mechanics.

---

## Sensitivity: How L and p Affect Amplification

```
Ratio(L, p) = 1 + 2L/p + 2L²/p²
```

| Lead Time L | Window p=2 | Window p=4 | Window p=8 | Window p=12 |
|-------------|-----------|-----------|-----------|------------|
| L = 1 | 3.00 | 1.63 | 1.28 | 1.18 |
| L = 2 | 7.00 | 3.50 | 2.13 | 1.72 |
| L = 3 | 13.00 | 6.13 | 3.28 | 2.50 |
| L = 4 | 21.00 | 9.50 | 5.00 | 3.56 |

**Key insight:** Long lead times are far more damaging than short forecast windows. Halving lead time from 4→2 at p=4 reduces ratio from 9.5 → 3.5 (–63%). Doubling the window from p=4→8 at L=4 reduces ratio from 9.5 → 5.0 (–47%). Lead time reduction is consistently more powerful.

---

## Autocorrelation Extension

When demand is autocorrelated (ρ ≠ 0), the formula becomes:

```
Var(q_t) / Var(D_t) = 1 + (2L/p) · [(1+ρ)/(1–ρ)] · [correction]
```

Full Lee et al. result for AR(1):

```
Var(q_t) / Var(D_t) ≥ 1 + (2ρ/p) · (1 – ρᵖ)/(1 – ρ)² · [lead time terms]
```

**Practical implications:**

| ρ value | Interpretation | Effect on Bullwhip |
|---------|---------------|-------------------|
| ρ > 0 (positive) | Trending demand | Amplification **increases** — forecast chases trend |
| ρ = 0 | i.i.d. demand | Base case formula applies |
| ρ < 0 (negative) | Mean-reverting | Amplification **decreases** — moving average is actually helpful |

For the typical retail setting (positively autocorrelated demand from seasonality and trends), bullwhip is worse than the i.i.d. formula predicts.

---

## Optimal Forecast Window

Given fixed lead time L, what window p minimizes bullwhip?

From the i.i.d. formula, larger p always reduces the ratio:

```
∂Ratio/∂p = –2L/p² – 4L²/p³ < 0
```

The ratio is monotonically decreasing in p — so the optimal strategy is **maximum available history**. However, in practice:

1. Old data may be less relevant for non-stationary demand
2. EWMA (exponential smoothing) is more common than simple MA and has different properties

**EWMA bullwhip ratio** (for smoothing parameter α):

```
Var(q_t) / Var(D_t) = 1 + (2Lα)/(2–α) + (2L²α²)/(2–α)²
```

Equivalent window: p_equiv = (2–α)/α. For α=0.2, p_equiv=9. For α=0.5, p_equiv=3.

High α (aggressive smoothing) = short effective window = more bullwhip.

---

## Multi-Echelon Extension

For a serial supply chain with N tiers, each stage i using lead time L_i and window p_i:

```
BWR_total = Π_{i=1}^{N} BWR_i
```

where each tier's BWR_i ≥ 1 + 2L_i/p_i + 2L_i²/p_i²

**Three-tier example:**

| Tier | Lead Time | Window | BWR_i |
|------|-----------|--------|-------|
| Retailer → Distributor | L=2 | p=4 | 3.50 |
| Distributor → Manufacturer | L=3 | p=4 | 6.13 |
| Manufacturer → Supplier | L=4 | p=4 | 9.50 |

```
BWR_total = 3.50 × 6.13 × 9.50 ≈ 204
```

A consumer demand CV of 5% reaches the supplier as:

```
CV_supplier = 5% × √204 ≈ 71%
```

This is why raw material suppliers see extreme volatility despite stable end demand.

---

## Model Limitations (Honest Assessment)

**What the model captures well:**
- Quantifies minimum amplification from forecast mechanics alone
- Shows why lead time reduction outperforms forecast improvement
- Explains why all stages amplify independently

**What the model does not capture:**
- **Order batching**: EOQ-driven periodic review adds discontinuous spikes not in the continuous model
- **Shortage gaming**: Demand inflation during scarcity requires a separate game-theoretic model (also in Lee et al. 1997, separate section)
- **Non-stationary demand**: Model assumes stable AR(1); structural breaks (new products, promotions) invalidate variance estimates
- **Correlated stages**: The multiplicative formula assumes each tier forecasts independently. If stages share POS data, amplification is lower

---

## Relationship to BWR Calculation in SKILL.md

The SKILL.md defines:

```
BWR_i = Var(orders_i) / Var(orders_{i-1})
```

This is the **empirical** measurement. The Lee-Padmanabhan-Whang formula provides the **theoretical minimum** for each stage. Comparing them diagnoses which causes dominate:

| Observed BWR vs. Theoretical Minimum | Diagnosis |
|--------------------------------------|-----------|
| Observed ≈ Theoretical | Bullwhip is primarily from forecast mechanics; fix: reduce L or increase p |
| Observed >> Theoretical | Additional causes: batch ordering, promotions, shortage gaming |
| Observed < 1 | Variance dampening: VMI, information sharing, or correlated cancellations |

**Diagnostic procedure:**
1. Compute theoretical minimum: `1 + 2L/p + 2L²/p²` using actual L and p values
2. Compute observed BWR from variance of actual order series
3. Residual = Observed – Theoretical minimum → attribute to batching/promotions/gaming
