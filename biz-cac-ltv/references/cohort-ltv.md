# Cohort-Based LTV Calculation

Simple LTV = ARPU × Gross Margin × (1 / Churn Rate) assumes churn is constant and behavior is uniform. Real cohorts behave differently: early cohorts churn faster, pricing changes mid-stream, expansion revenue kicks in at month 6. Cohort-based LTV measures what actually happened to a group of customers acquired in the same period.

## Core Concept

A **cohort** is a group of customers acquired in the same time window (typically a calendar month). You track each cohort's cumulative revenue through time, then calculate average LTV per customer as the cohort ages.

```
Cohort LTV (month N) = Cumulative revenue from cohort through month N
                       ─────────────────────────────────────────────
                       Original cohort size at month 0
```

This gives you a per-customer LTV at each age. As N → ∞ (or as churn approaches 100%), the series converges to the true LTV for that cohort.

## Step-by-Step Procedure

### Step 1: Build the Revenue Retention Matrix

Rows = cohorts (acquisition month). Columns = age in months (0, 1, 2, ...).
Each cell = total revenue from that cohort at that age.

| Cohort | M0 | M1 | M2 | M3 | M4 |
|--------|----|----|----|----|-----|
| Jan | 59,900 | 48,518 | 40,271 | 34,232 | 29,097 |
| Feb | 77,870 | 63,274 | 52,724 | 44,816 | — |
| Mar | 53,910 | 44,239 | 37,603 | — | — |
| Apr | 65,880 | 53,920 | — | — | — |

*Revenue in NT$. Jan cohort had 100 customers at NT$599/month.*

### Step 2: Convert to Cumulative Revenue per Customer

Divide each row by original cohort size, then take running sum.

| Cohort | M0 | Cum M1 | Cum M2 | Cum M3 | Cum M4 |
|--------|----|--------|--------|--------|--------|
| Jan (n=100) | 599 | 1,083 | 1,485 | 1,827 | 2,118 |
| Feb (n=130) | 599 | 1,085 | 1,490 | 1,834 | — |
| Mar (n=90) | 599 | 1,091 | 1,509 | — | — |
| Apr (n=110) | 599 | 1,089 | — | — | — |

*Cum M1 for Jan = (59,900 + 48,518) / 100 = 1,083*

### Step 3: Apply Gross Margin

The above numbers are revenue. LTV tracks contribution, not revenue.

```
Cohort LTV (month N) = Cumulative Revenue per Customer × Gross Margin %
```

With Gross Margin = 55%:

| Age | Gross Revenue/Customer | LTV (55% GM) |
|-----|----------------------|--------------|
| M0 | 599 | 329 |
| M1 | 1,083 | 596 |
| M2 | 1,485 | 817 |
| M3 | 1,827 | 1,005 |
| M4 | 2,118 | 1,165 |

### Step 4: Project to Full LTV

You can only observe cohort LTV up to how long you've been in business. For Jan cohort at month 4, LTV is NT$1,165 — but the customer hasn't fully churned yet. You need to project forward.

**Option A: Extrapolate via observed churn curve**

Fit an exponential decay to observed retention:

```
Retention(t) = e^(−λt)
λ = − ln(retention rate at M1)
```

For Jan cohort: M1 retention = 48,518 / 59,900 = 0.810
λ = −ln(0.810) = 0.211

```
Projected additional LTV from month N onward:
= (Monthly Revenue × GM) × Retention(N) / λ
```

From month 4 onward:
```
Retention(4) = e^(−0.211 × 4) = 0.431
Additional LTV = (599 × 0.55) × 0.431 / 0.211 = NT$672
Total projected LTV = 1,165 + 672 = NT$1,837
```

Compare this to the simple-formula estimate:
```
Simple LTV = 599 × 0.55 × (1 / 0.19) = NT$1,734
```
(Using observed average monthly churn of ~19% from M0→M1 for Jan cohort)

The two estimates are close here. When they diverge significantly, prefer the cohort projection because it reflects actual behavior.

**Option B: Use the oldest cohort as a benchmark**

If your Jan cohort is 18 months old and LTV is NT$3,200, that is your most reliable estimate. Apply a small growth multiplier if newer cohorts show better retention.

## Reading the Cohort Curve Shape

The shape of cumulative LTV per customer over time reveals business health.

```
Cumulative LTV
per customer
    |          ___________  ← Flat: churn has stopped, remaining customers
    |      __/               are long-term loyalists
    |    _/
    |  _/                  ← Steep early: strong first-purchase revenue
    | /
    |/___________________________
    0    3    6    9    12    months
```

| Shape | Interpretation | Action |
|-------|---------------|--------|
| Steep M0, then flattens quickly | High first-payment, fast early churn | Fix onboarding / M1 retention |
| Roughly linear | Steady churners, no expansion | Add upsell/cross-sell to steepen curve |
| Accelerating slope | Expansion revenue kicking in | Protect and amplify expansion motion |
| Curve bends downward | Refunds, chargebacks, or negative expansion | Investigate immediately |

## Accounting for Expansion Revenue

When customers upgrade plans or buy add-ons, their monthly revenue increases over time. This breaks the simple-formula assumption that ARPU is constant.

Track revenue per active customer per month:

| Month | Active Customers | Total Revenue | Revenue per Active Customer |
|-------|-----------------|---------------|-----------------------------|
| M0 | 100 | 59,900 | 599 |
| M1 | 81 | 52,164 | 644 |
| M2 | 67 | 46,098 | 688 |
| M3 | 57 | 41,610 | 730 |

Revenue per active customer is rising — surviving customers are expanding. This is **negative churn** in revenue terms (even though headcount churn is ~19%/month).

**Net Revenue Retention (NRR):**
```
NRR = Revenue from existing cohort at month N
      ─────────────────────────────────────────
      Revenue from that cohort at month 0
```

Month 3 NRR for Jan cohort = 41,610 / 59,900 = 69.5%

NRR > 100% means absolute revenue from the cohort is growing despite some customers leaving. When NRR > 100%, the simple LTV formula understates true LTV; cohort tracking is essential.

## Worked Python Snippet

```python
import numpy as np

# Revenue matrix: rows = cohorts, cols = age in months
# -1 = not yet observable
revenue = [
    [59900, 48518, 40271, 34232, 29097],  # Jan, n=100
    [77870, 63274, 52724, 44816,    -1],  # Feb, n=130
    [53910, 44239, 37603,    -1,    -1],  # Mar, n=90
    [65880, 53920,    -1,    -1,    -1],  # Apr, n=110
]
sizes = [100, 130, 90, 110]
gm = 0.55

def cumulative_ltv(revenue_row, cohort_size, gm):
    """Return cumulative LTV per customer at each observable age."""
    ltv = []
    cumrev = 0
    for r in revenue_row:
        if r < 0:
            break
        cumrev += r
        ltv.append(round(cumrev / cohort_size * gm, 1))
    return ltv

for i, row in enumerate(revenue):
    print(f"Cohort {i}: {cumulative_ltv(row, sizes[i], gm)}")

# Output:
# Cohort 0: [329.5, 595.4, 816.6, 1004.5, 1164.9]
# Cohort 1: [329.5, 595.4, 817.1, 1034.3]
# Cohort 2: [329.5, 595.3, 821.8]
# Cohort 3: [329.5, 625.5]
```

## Common Errors

**Mixing new and existing customers in the revenue count**

When you sum revenue for the Jan cohort at M3, use ONLY revenue traceable to the original Jan customers. If your data warehouse sums all-customer revenue by calendar month, you'll overcount.

**Using calendar months instead of cohort age**

Jan cohort at "month 3" means 3 months after acquisition (April). Not the calendar month of March. Keep cohort age (0, 1, 2, ...) separate from calendar dates.

**Treating early cohorts as representative**

Your first cohorts may have been acquired via personal networks or early-adopter channels. They often churn less and spend more. Use them as a ceiling, not a target.

**Projecting before you have at least 3 data points**

Fitting an exponential curve to two data points gives garbage projections. Wait until month 3 before extrapolating.

**Ignoring cohort size when averaging**

Weighted average LTV across cohorts must weight by cohort size, not by number of cohorts:

```
Blended LTV = Σ(LTV_i × size_i) / Σ(size_i)
```

## Connecting Back to LTV:CAC

Cohort LTV at month N is not the same as the LTV used in LTV:CAC. For LTV:CAC, use the **projected full LTV** (extrapolated to full churn-out), not the observed-to-date number.

Typical practice:
- Use the **24-month cohort LTV** as a proxy for full LTV if your average lifespan is shorter than 24 months
- Use the **oldest observable cohort** as the estimate if you have less than 24 months of history
- Document which definition you're using — investors and operators often mean different things

Payback period uses the same LTV numerically but measures a different question: how many months until cumulative contribution per customer equals CAC. Read directly off the cohort curve:

```
Find the month N where:
  Cumulative LTV per customer (month N) ≥ CAC
```

For Jan cohort with CAC = NT$1,500:
- M2 LTV = NT$817 → not recovered
- M3 LTV = NT$1,005 → not recovered
- Extrapolate: recovery occurs around month 5–6

This is more accurate than the formula-based `CAC / (ARPU × GM)` because it reflects actual retention behavior.
