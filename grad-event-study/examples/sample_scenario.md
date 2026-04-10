# Example: FDA Approval Announcement — BioNovus Therapeutics

## Scenario

A buy-side analyst at a hedge fund is evaluating whether the FDA's surprise approval of BioNovus Therapeutics' (ticker: BNVS) lead oncology drug on 2024-03-15 (Friday, after market close) generated statistically significant abnormal returns. The fund holds a position and wants to understand: (1) how large the market reaction was, (2) whether it was statistically significant, and (3) whether larger biotech firms reacted differently than smaller ones.

The analyst has daily price data for BNVS and the NASDAQ Biotechnology Index (NBI) as the market proxy, covering 2023-01-03 through 2024-04-05.

---

## Analysis

### Step 1 — Define Event and Windows

**Event date (day 0):** 2024-03-18 (Monday — first trading day after the Friday after-hours announcement)

| Window | Period | Trading Days | Rationale |
|--------|--------|--------------|-----------|
| Estimation | [-252, -11] | ~242 days | One trading year pre-event; ends 10 days before to avoid event contamination |
| Event | [-2, +5] | 8 days | Pre-announcement leakage check (−2, −1) + approval day + post-approval drift |

**Confounding check:** No earnings release, no secondary offering, and no competing drug readouts within the event window. Proceed.

---

### Step 2 — Estimate Normal Returns (Market Model)

OLS regression of BNVS daily returns on NBI returns over the estimation window [-252, -11]:

```
R_BNVS,t = α + β × R_NBI,t + ε_t

Estimated parameters:
  α̂  =  0.0003  (daily intercept ≈ +0.03%)
  β̂  =  1.18    (higher systematic exposure than index)
  R²  =  0.41
  σ_ε =  0.0214  (daily residual std dev = 2.14%)
```

**Normal return for any day t in the event window:**

```
E[R_BNVS,t] = 0.0003 + 1.18 × R_NBI,t
AR_t = R_BNVS,t − E[R_BNVS,t]
```

---

### Step 3 — Compute Abnormal and Cumulative Abnormal Returns

NBI daily returns during the event window (observed):

| Day | Calendar Date | R_NBI (%) | E[R_BNVS] (%) | R_BNVS (%) | AR (%) |
|-----|---------------|-----------|----------------|------------|--------|
| −2 | 2024-03-14 | +0.31 | +0.40 | +0.55 | +0.15 |
| −1 | 2024-03-15 | +0.18 | +0.24 | +2.80 | +2.56 |
| 0 | 2024-03-18 | −0.22 | −0.23 | +18.40 | +18.63 |
| +1 | 2024-03-19 | +0.45 | +0.56 | +3.10 | +2.54 |
| +2 | 2024-03-20 | −0.10 | −0.09 | +0.60 | +0.69 |
| +3 | 2024-03-21 | +0.27 | +0.35 | −0.15 | −0.50 |
| +4 | 2024-03-22 | +0.15 | +0.21 | +0.40 | +0.19 |
| +5 | 2024-03-25 | −0.05 | −0.03 | +0.20 | +0.23 |

**Note on day −1:** AR of +2.56% on the day *before* the official announcement (the Friday itself, during regular hours) warrants investigation. The FDA approval came after-hours on Friday — some pre-announcement trading activity or information leakage is plausible but not conclusive.

**Cumulative Abnormal Returns:**

```
CAR[-1, 0]  = 2.56 + 18.63 = +21.19%
CAR[0, +1]  = 18.63 + 2.54 = +21.17%
CAR[-1, +5] = 2.56 + 18.63 + 2.54 + 0.69 − 0.50 + 0.19 + 0.23 = +24.34%
```

---

### Step 4 — Statistical Testing

Using the cross-sectional t-test (single firm), the test statistic for CAR[τ₁, τ₂] is:

```
t = CAR[τ₁, τ₂] / (σ_ε × √(τ₂ − τ₁ + 1))
```

| Window | CAR (%) | Std Error (%) | t-stat | p-value (two-tail) | Significant? |
|--------|---------|---------------|--------|--------------------|-------------|
| [−1, 0] | +21.19 | 3.03 | 6.99 | < 0.001 | **Yes** |
| [0, +1] | +21.17 | 3.03 | 6.99 | < 0.001 | **Yes** |
| [0, 0] | +18.63 | 2.14 | 8.71 | < 0.001 | **Yes** |
| [−1, +5] | +24.34 | 6.05 | 4.02 | < 0.001 | **Yes** |
| [−2, −1] | +2.71 | 3.03 | 0.89 | 0.37 | No |

**Sign test (non-parametric):** With only one firm this is trivial; meaningful when extended to an event portfolio. For robustness, the analyst flags that the Patell (1976) standardized residual test and Kolari-Pynnönen (2010) generalized rank test should be applied when the sample is expanded to a panel.

---

## Result

```markdown
## Event Study: FDA Approval — BioNovus Therapeutics (BNVS), 2024-03-18

### Window Design
| Window | Period | Rationale |
|--------|--------|-----------|
| Estimation | [−252, −11] | 242-day pre-event estimation; avoids leakage contamination |
| Event | [−2, +5] | Captures pre-announcement leakage check and post-approval drift |

### Abnormal Returns
| Day | AR (%) | t-stat |
|-----|--------|--------|
| −2 | +0.15 | 0.07 |
| −1 | +2.56 | 1.20 |
| 0 | +18.63 | 8.71 |
| +1 | +2.54 | 1.19 |
| +2 | +0.69 | 0.32 |
| +3 | −0.50 | −0.23 |
| +4 | +0.19 | 0.09 |
| +5 | +0.23 | 0.11 |

### Cumulative Abnormal Returns
| Window | CAR (%) | t-stat | p-value | Significant? |
|--------|---------|--------|---------|-------------|
| [−1, 0] | +21.19 | 6.99 | <0.001 | Yes |
| [0, +1] | +21.17 | 6.99 | <0.001 | Yes |
| [0, 0] | +18.63 | 8.71 | <0.001 | Yes |
| [−1, +5] | +24.34 | 4.02 | <0.001 | Yes |
| [−2, −1] | +2.71 | 0.89 | 0.37 | No |

### Cross-Sectional Analysis
- Single-firm study; cross-sectional regression of CAR on market cap, pipeline stage,
  and prior FDA interaction score recommended if study is expanded to a panel of
  biotech FDA approvals (2020–2024).
- Day −1 AR of +2.56% warrants SEC EDGAR review for unusual options activity
  (not statistically significant at 5%, but economically notable for a drug approval).

### Limitations
- Beta estimated from NBI proxy; biotech factor model (Fama-French + momentum) would
  reduce model misspecification risk given BNVS's small-cap profile.
- Single-event study: conclusions are descriptive, not generalizable.
- Post-approval drift in [+1, +5] is economically small (+3.34% CAR) and
  statistically insignificant — consistent with rapid price discovery.
```

**Bottom line for the analyst:** The FDA approval generated an economically large and highly significant +18.6% abnormal return on the event day. No statistically significant pre-announcement leakage is detected, though the +2.56% on day −1 (when the approval came after-hours) merits further investigation. Post-event drift is negligible, suggesting the market processed the information efficiently within two trading days.
