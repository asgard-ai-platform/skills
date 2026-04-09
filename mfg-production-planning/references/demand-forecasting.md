# Demand Forecasting for MPS Input

Demand forecasting feeds directly into Step 1 of the planning hierarchy: raw forecast → MPS → MRP. A bad forecast at this stage propagates errors through every downstream plan. This document covers method selection, key formulas with worked numbers, forecast accuracy measurement, and how to translate forecast error into safety stock.

---

## Method Selection

Pick the simplest method that fits your demand pattern. Complexity does not equal accuracy.

| Demand Pattern | Recommended Method | Avoid |
|---|---|---|
| Stable, no trend, no seasonality | Simple Moving Average or SES | Holt-Winters (overfits) |
| Trend, no seasonality | Holt's Double Exponential Smoothing | SMA (lags behind trend) |
| Trend + seasonality | Holt-Winters Triple Exponential Smoothing | SES (ignores both) |
| Lumpy / intermittent | Croston's Method | Any average-based method |
| New product (no history) | Analogy-based or collaborative (sales team) | Statistical (no data) |

**Diagnostic test**: plot 12–24 months of history. If you can see a clear upward/downward drift → trend present. If demand spikes at the same months each year → seasonality present. If demand is zero for many periods → intermittent.

---

## Method 1: Simple Moving Average (SMA)

**Use when**: stable demand, no trend, no seasonality.

**Formula**:

```
F(t+1) = [D(t) + D(t-1) + ... + D(t-n+1)] / n
```

Where:
- `F(t+1)` = forecast for next period
- `D(t)` = actual demand in period t
- `n` = number of periods in the average

**Window size rule of thumb**:
- Stable market: n = 6–12 months
- Volatile market: n = 3–4 months
- Longer n → smoother, slower to react; shorter n → noisier, faster to react

**Worked example** (n = 4):

| Month | Actual Demand | 4-Month SMA Forecast |
|-------|--------------|----------------------|
| Jan | 420 | — |
| Feb | 380 | — |
| Mar | 410 | — |
| Apr | 430 | — |
| May | ? | (420+380+410+430)/4 = **410** |
| Jun | ? | Use May actual once known |

---

## Method 2: Simple Exponential Smoothing (SES)

**Use when**: stable demand with no clear trend; you want recent data to have more weight than older data.

**Formula**:

```
F(t+1) = α × D(t) + (1 - α) × F(t)
```

Where:
- `α` (alpha) = smoothing constant, 0 < α < 1
- `D(t)` = actual demand in period t
- `F(t)` = forecast for period t (last period's forecast)

**Alpha selection**:
- α = 0.1–0.2 → slow adaptation, good for stable demand
- α = 0.3–0.5 → faster adaptation, good for moderate volatility
- Optimize α by minimizing Sum of Squared Errors (SSE) over historical data

**Initialization**: Set `F(1) = D(1)` (first actual demand), or use the average of the first 3–6 periods.

**Worked example** (α = 0.3):

| Period | Actual D(t) | Forecast F(t) | Error D(t)–F(t) |
|--------|------------|---------------|-----------------|
| 1 | 420 | 420 (init) | 0 |
| 2 | 380 | 420 | –40 |
| 3 | 410 | 0.3×380 + 0.7×420 = **408** | +2 |
| 4 | 430 | 0.3×410 + 0.7×408 = **408.6** | +21.4 |
| 5 | ? | 0.3×430 + 0.7×408.6 = ****415.0**** | — |

---

## Method 3: Holt's Double Exponential Smoothing (Trend)

**Use when**: demand has a consistent upward or downward trend, no seasonality.

**Three equations**:

```
Level:  L(t) = α × D(t) + (1 - α) × [L(t-1) + T(t-1)]
Trend:  T(t) = β × [L(t) - L(t-1)] + (1 - β) × T(t-1)
Forecast m periods ahead:  F(t+m) = L(t) + m × T(t)
```

Where:
- `α` = level smoothing constant (0 < α < 1)
- `β` = trend smoothing constant (0 < β < 1)
- `L(t)` = estimated level at period t
- `T(t)` = estimated trend at period t

**Initialization**:
- `L(1) = D(1)`
- `T(1) = D(2) - D(1)` (or average of first few period-to-period changes)

**Worked example** (α = 0.4, β = 0.3):

Monthly demand (upward trend): 200, 210, 225, 215, 240

| Period | D(t) | L(t) | T(t) | F(t+1) |
|--------|------|------|------|--------|
| 1 | 200 | 200 | 10 (init) | — |
| 2 | 210 | 0.4×210 + 0.6×(200+10) = **210** | 0.3×(210–200) + 0.7×10 = **10** | 220 |
| 3 | 225 | 0.4×225 + 0.6×(210+10) = **222** | 0.3×(222–210) + 0.7×10 = **10.6** | 232.6 |
| 4 | 215 | 0.4×215 + 0.6×(222+10.6) = **225.4** | 0.3×(225.4–222) + 0.7×10.6 = **8.4** | 233.8 |
| 5 | 240 | 0.4×240 + 0.6×(225.4+8.4) = **236.3** | 0.3×(236.3–225.4) + 0.7×8.4 = **9.2** | 245.5 |

Forecast for period 6 = L(5) + 1×T(5) = 236.3 + 9.2 = **245.5 units**

---

## Method 4: Holt-Winters (Trend + Seasonality)

**Use when**: demand has both trend and repeating seasonal pattern (e.g., peak every summer, dip every January).

**Additive model** (season adds/subtracts a fixed amount):

```
Level:    L(t) = α × [D(t) - S(t-m)] + (1 - α) × [L(t-1) + T(t-1)]
Trend:    T(t) = β × [L(t) - L(t-1)] + (1 - β) × T(t-1)
Seasonal: S(t) = γ × [D(t) - L(t)] + (1 - γ) × S(t-m)
Forecast: F(t+h) = L(t) + h × T(t) + S(t+h-m)
```

Where:
- `m` = season length (12 for monthly with annual seasonality)
- `γ` = seasonal smoothing constant (0 < γ < 1)

**Multiplicative model** (season scales by a percentage): use when seasonal swings grow proportionally with the level (common in growing businesses).

**Initialization** (additive, 2 full seasons of history required):
1. Compute per-period averages for each season's data
2. Fit a linear trend to the annual averages to get L(1) and T(1)
3. Initialize seasonal factors S(1)…S(m) = Period average – Year average

**Practical note**: Holt-Winters requires at least 2 full seasonal cycles (24 months for annual seasonality) of history. With less data, use collaborative forecasting or analogy.

---

## Croston's Method (Intermittent Demand)

Standard exponential smoothing breaks down for intermittent demand (many zero periods). Croston's method forecasts demand size and inter-demand interval separately.

**When to use**: if more than 30% of periods have zero demand.

**Algorithm**:

1. When `D(t) > 0` (non-zero period):
   - Update demand size: `Z(t) = α × D(t) + (1 - α) × Z(t-1)`
   - Update interval: `P(t) = α × q + (1 - α) × P(t-1)` where `q` = periods since last demand
2. When `D(t) = 0`: carry forward Z and P unchanged
3. Forecast per period: `F = Z / P`

**Worked example** (α = 0.4, demand occurs at periods 1, 3, 6):

| Period | D(t) | q | Z(t) | P(t) | F/period |
|--------|------|---|------|------|----------|
| 1 | 50 | 1 | 50 | 1 | 50/1=50 |
| 2 | 0 | — | 50 | 1 | 50 |
| 3 | 30 | 2 | 0.4×30+0.6×50=**38** | 0.4×2+0.6×1=**1.4** | 38/1.4=**27.1** |
| 4 | 0 | — | 38 | 1.4 | 27.1 |
| 5 | 0 | — | 38 | 1.4 | 27.1 |
| 6 | 60 | 3 | 0.4×60+0.6×38=**46.8** | 0.4×3+0.6×1.4=**2.04** | 46.8/2.04=**22.9** |

---

## Measuring Forecast Accuracy

### MAPE (Mean Absolute Percentage Error)

The primary accuracy metric referenced in SKILL.md.

```
MAPE = (1/n) × Σ |D(t) - F(t)| / D(t) × 100%
```

**Interpretation**:
- MAPE < 10% → excellent (high-volume, stable products)
- MAPE 10–20% → acceptable (most manufactured goods)
- MAPE 20–50% → poor; investigate causes before relying on MPS
- MAPE > 50% → forecasting is unreliable; use safety stock, not better models

**MAPE limitation**: undefined when D(t) = 0 (zero-demand periods). Use MAE or WMAPE for intermittent demand.

### MAE (Mean Absolute Error)

```
MAE = (1/n) × Σ |D(t) - F(t)|
```

Use MAE for safety stock sizing (it's in same units as demand).

### Bias (Mean Error)

```
Bias = (1/n) × Σ [F(t) - D(t)]
```

- Positive bias → consistently over-forecasting → excess inventory
- Negative bias → consistently under-forecasting → stockouts
- Target: near zero

**Critical**: low MAPE + high bias = model is wrong in a predictable direction. Fix the bias first.

### Tracking Signal

Detect when a model has drifted out of control:

```
Tracking Signal = Running Sum of Forecast Errors / MAE
```

Alert threshold: |Tracking Signal| > 4. When triggered, refit the model or investigate demand changes.

---

## Worked Accuracy Calculation

Seven months of actual vs. forecast:

| Month | Actual D(t) | Forecast F(t) | Error | |Error| | |Error|/D(t) |
|-------|------------|--------------|-------|---------|--------------|
| 1 | 420 | 410 | –10 | 10 | 2.4% |
| 2 | 380 | 415 | +35 | 35 | 9.2% |
| 3 | 410 | 395 | –15 | 15 | 3.7% |
| 4 | 430 | 405 | –25 | 25 | 5.8% |
| 5 | 400 | 425 | +25 | 25 | 6.3% |
| 6 | 450 | 410 | –40 | 40 | 8.9% |
| 7 | 390 | 430 | +40 | 40 | 10.3% |

- **MAPE** = (2.4+9.2+3.7+5.8+6.3+8.9+10.3)/7 = **6.7%** → acceptable
- **Bias** = (–10+35–15–25+25–40+40)/7 = **+1.4** → slightly over-forecasting; acceptable
- **MAE** = (10+35+15+25+25+40+40)/7 = **27.1 units/month**

---

## From Forecast Error to Safety Stock

SKILL.md states: "build safety stock proportional to forecast error." Here is the formula.

### Safety Stock Formula

```
SS = Z × σ_d × √LT
```

Where:
- `SS` = safety stock (units)
- `Z` = service level factor (see table below)
- `σ_d` = standard deviation of demand per period
- `LT` = lead time in periods (same unit as σ_d)

**Service level → Z factor**:

| Target Service Level | Z |
|---|---|
| 90% | 1.28 |
| 95% | 1.65 |
| 98% | 2.05 |
| 99% | 2.33 |

**When lead time also varies**, use:

```
SS = Z × √(LT × σ_d² + D̄² × σ_LT²)
```

Where:
- `D̄` = average demand per period
- `σ_LT` = standard deviation of lead time (in periods)

### Estimating σ_d from MAE

If you have MAE but not σ_d:

```
σ_d ≈ MAE × 1.25   (approximation for normally distributed errors)
```

### Worked Example

From the accuracy calculation above:
- MAE = 27.1 units/month
- `σ_d ≈ 27.1 × 1.25 = 33.9 units/month`
- Lead time = 2 months (supplier)
- Target service level = 95% → Z = 1.65

```
SS = 1.65 × 33.9 × √2 = 1.65 × 33.9 × 1.414 = 79 units
```

**Interpretation**: hold ~79 units of safety stock to cover 95% of demand variability during a 2-month lead time. If MAPE were 25% instead of 7%, σ_d would roughly triple, and safety stock would need to triple — this is why forecast accuracy directly drives inventory cost.

---

## Collaborative vs. Statistical Forecasting

Neither method alone is optimal. Use both and reconcile.

| | Statistical | Collaborative (Sales/Market) |
|---|---|---|
| **Strength** | Objective, consistent, handles large SKU counts | Captures upcoming promotions, new customers, market intelligence |
| **Weakness** | Backward-looking, blind to future events | Optimism bias, inconsistent across reps |
| **When to trust** | Stable, mature products with 12+ months history | New products, planned promotions, large new accounts |

**Reconciliation process (S&OP input)**:
1. Generate statistical baseline forecast
2. Sales team adjusts for known events (promotions, lost accounts, new wins)
3. Finance reviews for revenue consistency
4. Final forecast locked at S&OP meeting → feeds MPS

**Override discipline**: track every manual override. Calculate accuracy of statistical forecast vs. adjusted forecast separately. If adjustments hurt accuracy (common), constrain override authority.

---

## Forecast Horizons and Refresh Cadence

| Planning Level | Horizon | Granularity | Refresh |
|---|---|---|---|
| S&OP (feeds capacity decisions) | 12–18 months | Monthly, family-level | Monthly |
| MPS input | 3–6 months | Weekly, SKU-level | Weekly |
| MRP input | 4–12 weeks | Daily/weekly, component | Weekly |

**Rolling horizon**: always maintain a fixed-length forward window. At the start of each week, drop the oldest week and add a new week at the far end. Do not shrink the horizon as you approach the period.

**Frozen zone alignment**: the first 1–2 weeks of MPS are frozen (per SKILL.md). Forecast updates inside the frozen zone should not automatically trigger MPS changes — route them to exception review instead.

---

## Common Failure Modes

**Using MAPE to evaluate intermittent demand**: MAPE is undefined for zero-demand periods. Use MAE or fill rate instead.

**Optimizing α/β/γ on all history**: smoothing constants tuned on 5 years of data overfit to historical patterns. Tune on the most recent 12–18 months (or use rolling cross-validation).

**Treating the forecast as the plan**: the forecast is a probability distribution, not a point estimate. The MPS should incorporate safety stock for the uncertainty around the forecast, not assume the forecast is exact.

**Ignoring bias**: a model with 8% MAPE and +6% bias will consistently produce short materials. Fix bias before reducing MAPE.

**Single-number forecast for MPS**: provide the forecast plus a high/low range. The range width informs safety stock sizing. A point forecast alone discards information the planning team needs.

**Aggregation mismatch**: forecasting at the product-family level then disaggregating to SKU by a fixed ratio fails when the mix shifts. Forecast at the lowest MPS-relevant level whenever you have sufficient history.
