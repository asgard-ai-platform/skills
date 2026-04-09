# CLV Prediction: Extending RFM into Forward-Looking Value

RFM tells you what a customer did. CLV (Customer Lifetime Value) tells you what a customer is *worth going forward*. This document covers the two most practical CLV approaches for e-commerce teams: the **BG/NBD probabilistic model** and the **RFM-weighted heuristic**. Most teams should start with the heuristic; graduate to BG/NBD when they need per-customer probabilities.

---

## Why RFM Alone Is Insufficient for Budget Decisions

RFM segments are snapshots. A "Champions" customer who bought 30 days ago looks identical to one who bought yesterday. Neither tells you:

- **Probability** that a customer is still alive (hasn't churned silently)
- **Expected purchases** in the next 90 / 180 / 365 days
- **NPV** of that customer given a discount rate and margin

These are the numbers marketing needs to justify acquisition costs, retention spend caps, and win-back offer thresholds.

---

## Model 1: RFM-Weighted Heuristic CLV (Quick Start)

Use this when you have 6–18 months of data and need actionable numbers within a day.

### Formula

```
Historical CLV  = (Avg Order Value) × (Purchase Frequency per year) × (Customer Lifespan in years)
Forward CLV     = Historical CLV × Retention Probability × (1 / (1 + Discount Rate))
```

### Step-by-Step

**Step 1 — Compute per-customer trailing metrics** (same window as your RFM analysis, e.g., 12 months):

| Metric | Formula |
|--------|---------|
| AOV | Total Spend ÷ Order Count |
| Freq/year | Order Count ÷ Window Length in Years |
| Recency | Days since last order |

**Step 2 — Estimate retention probability by RFM segment**

Use this lookup table as a starting point; calibrate with your own cohort data when available:

| RFM Segment | Retention P (12-month) |
|-------------|----------------------|
| Champions (R5 F5 M5) | 0.85 |
| Loyal (R4-5 F4-5) | 0.75 |
| Potential Loyalists (R4-5 F2-3) | 0.55 |
| At Risk (R2-3 F3-5) | 0.30 |
| New Customers (R5 F1) | 0.40 |
| Hibernating (R1-2 F1-2) | 0.10 |

**Step 3 — Apply discount rate**

Typical e-commerce discount rates: 10–20% annually (use cost of capital or a business-specified hurdle rate).

```
Forward CLV (1-year) = AOV × Freq × Retention P × Margin %
```

Include margin % to get *profit* CLV rather than revenue CLV. Marketing budgets should be capped against profit CLV, not revenue CLV.

### Worked Example

Customer A:
- Total spend (12 months): $480
- Orders: 6
- Last purchase: 15 days ago → R=5
- AOV = $80, Freq = 6/year
- Segment: Loyal → Retention P = 0.75
- Margin: 35%
- Discount rate: 15%

```
Gross CLV    = $80 × 6 = $480/year
Margin CLV   = $480 × 0.35 = $168/year
Forward CLV  = $168 × 0.75 / 1.15 ≈ $109.6
```

**Maximum acquisition/retention spend per customer A ≈ $109.** A win-back campaign offering a $15 coupon is clearly worthwhile; a $120 gift basket is not.

---

## Model 2: BG/NBD Probabilistic Model

BG/NBD (Beta-Geometric / Negative Binomial Distribution) is the standard academic model for non-contractual CLV. It handles the core difficulty of non-subscription e-commerce: you don't know if a customer has churned or is just between purchases.

### What It Models

- **NBD part**: Number of transactions while alive follows a Poisson process with rate λ; λ varies across customers (Gamma-distributed)
- **BG part**: After each transaction, a customer has probability p of "dying" (churning); p varies across customers (Beta-distributed)

The model outputs, per customer:
1. `P(alive)` — probability the customer has not churned
2. `E[X | t]` — expected number of purchases in next *t* days

### Required Inputs (per customer, as of analysis date)

| Variable | Description |
|----------|-------------|
| `x` | Number of repeat transactions in observation window |
| `t_x` | Time from first purchase to last purchase (in days or weeks) |
| `T` | Time from first purchase to analysis date |

Note: First purchase is not counted in `x`. A customer with 3 orders has `x=2`.

### Python Implementation (using `lifetimes` library)

```python
from lifetimes import BetaGeoFitter, GammaGammaFitter
from lifetimes.utils import summary_data_from_transaction_data
import pandas as pd

# --- Prepare data ---
# df: columns [customer_id, order_date, order_value]
df['order_date'] = pd.to_datetime(df['order_date'])

rfm_table = summary_data_from_transaction_data(
    df,
    customer_id_col='customer_id',
    datetime_col='order_date',
    monetary_value_col='order_value',
    observation_period_end='2025-12-31'
)
# rfm_table columns: frequency, recency, T, monetary_value

# --- Fit BG/NBD ---
bgf = BetaGeoFitter(penalizer_coef=0.01)
bgf.fit(
    rfm_table['frequency'],
    rfm_table['recency'],
    rfm_table['T']
)

# --- Predict future purchases ---
t = 90  # days
rfm_table['predicted_purchases_90d'] = bgf.conditional_expected_number_of_purchases_up_to_time(
    t,
    rfm_table['frequency'],
    rfm_table['recency'],
    rfm_table['T']
)

rfm_table['p_alive'] = bgf.conditional_probability_alive(
    rfm_table['frequency'],
    rfm_table['recency'],
    rfm_table['T']
)

# --- Fit Gamma-Gamma for monetary value ---
# Filter: only customers with >0 repeat purchases for GG model
returning = rfm_table[rfm_table['frequency'] > 0]
ggf = GammaGammaFitter(penalizer_coef=0.01)
ggf.fit(returning['frequency'], returning['monetary_value'])

# --- CLV (12 months, monthly discount rate 1%) ---
clv = ggf.customer_lifetime_value(
    bgf,
    rfm_table['frequency'],
    rfm_table['recency'],
    rfm_table['T'],
    rfm_table['monetary_value'],
    time=12,         # months
    discount_rate=0.01,
    freq='D'
)
rfm_table['clv_12m'] = clv
```

### Interpreting BG/NBD Output

| `p_alive` | Interpretation |
|-----------|---------------|
| > 0.80 | Almost certainly still active |
| 0.40–0.80 | Uncertain; high-recency signals matter |
| < 0.40 | Likely churned; win-back cost must be low |

**Do not treat `p_alive < 0.5` as "definitely churned."** The model is probabilistic; use it to *rank* customers for intervention, not to hard-exclude them.

### Calibration / Holdout Validation

Always validate on a holdout period before using in production:

```python
from lifetimes.utils import calibration_and_holdout_data

summary_cal_holdout = calibration_and_holdout_data(
    df,
    customer_id_col='customer_id',
    datetime_col='order_date',
    calibration_period_end='2025-06-30',   # fit on first half
    observation_period_end='2025-12-31'    # evaluate on second half
)

bgf.fit(
    summary_cal_holdout['frequency_cal'],
    summary_cal_holdout['recency_cal'],
    summary_cal_holdout['T_cal']
)

from lifetimes.plotting import plot_calibration_purchases_vs_holdout_purchases
plot_calibration_purchases_vs_holdout_purchases(bgf, summary_cal_holdout)
```

A well-fit model should have predicted vs. actual within ±10% across frequency buckets.

---

## Combining RFM Segments with CLV Scores

CLV is a continuous score; RFM is categorical. They complement each other:

| RFM Segment | CLV Percentile | Interpretation | Action |
|-------------|---------------|----------------|--------|
| Champions | Top 20% | Confirmed high-value, active | Loyalty tier; protect |
| Champions | Bottom 20% | High historical value, model says cooling | Proactive outreach |
| At Risk | Top 30% CLV | High-value at risk — model says p_alive dropping | Highest-priority win-back |
| At Risk | Bottom 50% CLV | Low-value dormant | Low-cost email only |
| New Customers | Top 40% CLV | Early signals of high future value | Accelerate onboarding |

**The key insight**: At Risk customers in the top CLV quartile deserve more budget than Champions in the bottom quartile. RFM alone would invert this priority.

---

## Spend Cap by CLV Tier

Use CLV to set hard caps on per-customer marketing spend:

```
Max Intervention Spend = Forward CLV × (1 - Margin Floor)
```

Example thresholds (adjust to your margin structure):

| CLV 12-month | Win-back budget cap | Retention budget cap |
|-------------|--------------------|--------------------|
| > $500 | $75 | $40 |
| $200–$500 | $30 | $15 |
| $50–$200 | $10 | $5 |
| < $50 | $0 (no paid action) | $0 |

---

## Gotchas Specific to CLV Prediction

**BG/NBD assumes a stationary purchase process.** If your business is seasonal (e.g., holiday spike), the model will underfit customers acquired in November. Fit separate models per acquisition cohort or use a longer window (24+ months) to average out seasonality.

**Gamma-Gamma assumes spend is independent of purchase frequency.** This fails for volume-discount businesses. If your top customers get lower AOV because they buy in bulk at discount, GG will over-estimate their CLV. Check the correlation between `frequency` and `monetary_value`; if Pearson r > 0.3, GG is suspect.

**One-time buyers dominate and degrade the model.** If >60% of customers have `frequency=0`, BG/NBD parameters become unstable. Cap the penalizer at 0.1 or filter to customers with ≥2 purchases before fitting, then predict one-timers separately via a simpler rule.

**CLV from the heuristic model double-counts with CAC decisions.** If you use CLV to justify acquisition cost (CAC < CLV / 3), do not also use it to justify retention spend on the same customer. Pick one use case per planning cycle.

**Inflation and pricing changes invalidate historical monetary.** If you raised prices 20% mid-window, monetary values are not comparable. Normalize to a base period before fitting GG.

---

## Minimum Data Requirements

| Model | Min customers | Min window | Min repeat-buyer % |
|-------|--------------|-----------|-------------------|
| Heuristic | 100 | 6 months | N/A |
| BG/NBD | 500 | 12 months | 25% |
| BG/NBD + GG (full CLV) | 1,000 | 18 months | 30% |

Below these thresholds, use the heuristic with segment-level retention probabilities calibrated from cohort survival curves.
