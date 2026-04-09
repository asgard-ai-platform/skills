# HR Feature Engineering for Turnover Prediction

Feature engineering is where most turnover models win or lose. This document covers the canonical feature set, how to compute each feature, known pitfalls per feature, and a worked example for a 500-employee dataset.

---

## Feature Taxonomy

| Category | Signal Type | Typical Predictive Power |
|----------|-------------|--------------------------|
| Compensation | Financial stress | High |
| Career velocity | Advancement frustration | High |
| Tenure & stability | Lifecycle position | Medium-High |
| Manager relationship | Environmental friction | Medium-High |
| Engagement | Self-reported intent | Medium (noisy) |
| Demographics | Indirect proxies | Low (use carefully) |

---

## 1. Compensation Features

### 1.1 Comp Ratio

The single most predictive compensation feature. Normalize raw salary against a market or internal benchmark.

```
comp_ratio = employee_salary / market_median_for_role_level_location
```

**Interpretation:**
- `comp_ratio < 0.90` → below-market, elevated risk
- `0.90–1.10` → market range
- `comp_ratio > 1.10` → above-market, lower financial pull to leave

**Worked example:**

| Employee | Salary | Market Median | Comp Ratio |
|----------|--------|---------------|------------|
| E001 | $72,000 | $85,000 | 0.847 ← high risk |
| E002 | $95,000 | $85,000 | 1.118 |
| E003 | $84,000 | $85,000 | 0.988 |

If market data is unavailable, use internal peer median (same role + level + location bucket).

### 1.2 Comp Ratio Trend

A declining comp ratio is more predictive than a low absolute value, because it signals the gap is widening.

```
comp_ratio_trend = comp_ratio_current - comp_ratio_12mo_ago
```

Employees who were once at-market but have fallen below are at higher risk than those who have always been below (the latter may have accepted the trade-off).

### 1.3 Last Salary Increase %

```
last_raise_pct = (salary_now - salary_at_last_review) / salary_at_last_review
```

Threshold to flag: `last_raise_pct < 0.03` (below CPI). Even employees at market may feel stagnation if their raise was below inflation.

### 1.4 Bonus-to-Target Ratio

For roles with variable compensation:

```
bonus_attainment = actual_bonus_paid / target_bonus
```

Two consecutive years with `bonus_attainment < 0.80` is a signal worth capturing as a separate binary feature.

---

## 2. Career Velocity Features

### 2.1 Months Since Last Promotion

```
months_since_promo = (snapshot_date - last_promotion_date).days / 30.44
```

**Risk thresholds by seniority level:**

| Level | Expected Promotion Cycle | Flag When |
|-------|--------------------------|-----------|
| IC1–IC2 (junior) | 12–18 months | > 24 months |
| IC3–IC4 (mid) | 18–30 months | > 36 months |
| IC5+ (senior) | 30–48 months | > 54 months |
| Manager | 24–36 months | > 48 months |

Do not apply a single threshold to all levels — junior employees churn on much shorter cycles.

### 2.2 Promotion Velocity

Captures career acceleration or stall relative to cohort peers (same hire year, same starting level).

```python
def promo_velocity(employee, cohort):
    employee_promos = len(employee.promotions)
    cohort_median_promos = cohort["num_promotions"].median()
    return employee_promos - cohort_median_promos
```

- Positive score → fast-tracker (lower turnover risk from stagnation, but may be poached)
- Score of -1 or lower → falling behind peers (elevated risk)

### 2.3 Role Stagnation Flag

Binary: has the employee been in the same role title for N+ months with no scope change?

```python
role_stagnation = int(months_in_current_role > role_stagnation_threshold[level])
```

Combine with `months_since_promo` — both firing together is a stronger signal than either alone.

---

## 3. Tenure Features

### 3.1 Raw Tenure (Months)

```
tenure_months = (snapshot_date - hire_date).days / 30.44
```

Non-linear relationship with turnover. Do **not** use as a linear feature — bucket it.

### 3.2 Tenure Buckets

| Bucket | Months | Turnover Pattern |
|--------|--------|-----------------|
| `new_hire` | 0–6 | High (onboarding failure) |
| `early_stage` | 7–18 | High (expectation mismatch) |
| `settled` | 19–36 | Decreasing |
| `established` | 37–60 | Low |
| `veteran` | 61–120 | Low-medium (may plateau) |
| `long_tenure` | 120+ | Low (golden handcuffs) |

In Python:
```python
import pandas as pd

bins = [0, 6, 18, 36, 60, 120, float("inf")]
labels = ["new_hire", "early_stage", "settled", "established", "veteran", "long_tenure"]
df["tenure_bucket"] = pd.cut(df["tenure_months"], bins=bins, labels=labels)
```

One-hot encode these buckets; do not treat them as ordinal integers.

### 3.3 Tenure at Company vs. Tenure in Role

Split tenure into two signals:

```
company_tenure_months = (snapshot_date - original_hire_date).days / 30.44
role_tenure_months = (snapshot_date - current_role_start_date).days / 30.44
```

An employee with high company tenure but low role tenure recently changed roles internally — usually a good sign. The reverse (low company tenure, high role tenure = hasn't moved) can indicate stagnation at a junior level.

---

## 4. Manager Relationship Features

### 4.1 Manager Tenure

Research consistently shows manager quality is among the top turnover drivers, yet HR data rarely captures it directly. A proxy: how long has the current manager been in their role?

```
manager_role_tenure_months = (snapshot_date - manager_role_start_date).days / 30.44
```

New managers (< 6 months) are associated with higher team turnover during transition periods.

### 4.2 Manager Change Count (Rolling 24 Months)

```
manager_changes_24mo = count of distinct managers in past 24 months
```

`manager_changes_24mo >= 3` is a high-risk flag. Frequent manager changes signal organizational instability and erode psychological safety.

### 4.3 Team Turnover Rate

The employee's immediate team's trailing 12-month voluntary turnover rate. Turnover is contagious — people in high-turnover teams leave at higher rates regardless of their own features.

```python
def team_turnover_rate(employee_id, team_roster, departures_12mo):
    team = team_roster[team_roster["manager_id"] == get_manager(employee_id)]
    avg_headcount = team["headcount"].mean()
    team_departures = departures_12mo[departures_12mo["team_id"] == team.id].count()
    return team_departures / avg_headcount
```

Cap at 1.0 to avoid distortion from very small teams.

---

## 5. Engagement Features

### 5.1 Engagement Score (Raw)

Most companies run annual or quarterly engagement surveys on a 1–5 or 0–100 scale. Use the most recent available score.

**Caveat:** Employees likely to leave often skip surveys (non-response bias), which means the signal is weaker than it appears. Model this as `(score, is_missing)` rather than imputing with a mean.

### 5.2 Engagement Trend (3-Period Slope)

A declining trajectory is more predictive than absolute level.

```python
import numpy as np

def engagement_trend(scores: list[float]) -> float:
    """
    Given a list of engagement scores (oldest first), return the
    OLS slope. Positive = improving, negative = declining.
    """
    if len(scores) < 2:
        return 0.0
    x = np.arange(len(scores))
    slope, _ = np.polyfit(x, scores, 1)
    return slope
```

An employee with scores `[4.2, 3.8, 3.1]` has a slope of approximately -0.55 — meaningful decline. One with scores `[3.0, 3.1, 3.0]` has a near-zero slope — stable (even if low).

### 5.3 eNPS (Employee Net Promoter Score) Component

If your engagement survey includes "Would you recommend this company as a place to work?", extract that single item as a separate feature. It has stronger predictive validity for intent-to-leave than composite engagement scores.

---

## 6. Absence and Behavioral Signals

### 6.1 Unplanned Absence Rate

```
unplanned_absence_rate = unplanned_days_absent_12mo / total_working_days_12mo
```

A sudden spike in unplanned absences (especially in the 3 months before departure) is predictive. However, lagged absence data introduces look-ahead bias if not handled carefully — ensure you're using absences logged **before** your snapshot date.

### 6.2 PTO Utilization Rate

```
pto_utilization = pto_days_taken_ytd / pto_days_accrued_ytd
```

Both extremes matter:
- `< 0.4` → possible burnout (employee afraid to take leave due to workload)
- `> 0.95` → possible job searching behavior (clearing out balance before leaving)

---

## 7. Feature Interaction Terms

Some feature pairs interact non-linely. Worth including explicitly for logistic regression (GBDT handles these automatically):

| Interaction | Construction | Why |
|-------------|--------------|-----|
| Low comp × no promotion | `comp_ratio < 0.9 AND months_since_promo > 30` | Double financial + career frustration |
| New manager × low engagement | `manager_changes_24mo >= 2 AND engagement_score < 3` | Manager instability hits motivated employees hardest |
| Veteran × zero promotion | `tenure_months > 60 AND months_since_promo > 54` | Plateau effect |

```python
df["double_frustration"] = (
    (df["comp_ratio"] < 0.90) & (df["months_since_promo"] > 30)
).astype(int)
```

---

## 8. Features to Exclude

These are either ethically/legally problematic or introduce leakage:

| Feature | Problem |
|---------|---------|
| Age / date of birth | Protected attribute; disparate impact risk |
| Gender | Protected attribute |
| Ethnicity / national origin | Protected attribute |
| Medical leave history | FMLA/ADA concerns (US); similar laws elsewhere |
| LinkedIn profile update | Surveillance of off-duty activity |
| Recruiter contact / job applications | Privacy; may be illegal to monitor |
| Performance rating (current cycle, unreleased) | Leakage if used before finalization |

**Proxy leakage**: some seemingly neutral features (zip code, graduation year, certain job titles) can serve as proxies for protected attributes. Run disparate impact analysis before finalizing feature set.

---

## 9. Worked Feature Table (5 Employees)

Snapshot date: 2025-01-01

| emp_id | tenure_mo | comp_ratio | months_since_promo | manager_changes_24mo | engagement_slope | team_turnover_rate | label |
|--------|-----------|------------|-------------------|----------------------|------------------|--------------------|-------|
| E001 | 38 | 0.84 | 34 | 1 | -0.6 | 0.22 | left |
| E002 | 14 | 1.05 | 12 | 0 | +0.2 | 0.08 | stayed |
| E003 | 72 | 0.91 | 52 | 3 | -0.3 | 0.31 | left |
| E004 | 8 | 0.98 | 8 | 0 | 0.0 | 0.10 | stayed |
| E005 | 45 | 1.12 | 28 | 2 | -0.1 | 0.15 | stayed |

E001 and E003 both left. Key differentiators vs. E005 (similar tenure, didn't leave): E001 had below-market comp AND career stagnation; E003 had 3 manager changes and high team turnover rate.

E005 shows why single features are insufficient: above-market comp compensated for the manager instability signal.

---

## 10. Feature Availability by HR Maturity

Not all companies have all data. Map your feature availability to model tier:

| Data Available | Recommended Model | Expected AUC |
|----------------|-------------------|--------------|
| Tenure + comp only | Logistic regression, 3 features | 0.60–0.65 |
| + promotions + manager history | Logistic regression or RF, 8–12 features | 0.68–0.73 |
| + engagement + absence | GBDT, full feature set | 0.73–0.82 |
| + engagement trend + team signals | GBDT + interaction terms | 0.78–0.85 |

Do not over-engineer for data you don't have. A well-tuned 5-feature logistic regression beats a 40-feature GBDT with 60% missing values.
