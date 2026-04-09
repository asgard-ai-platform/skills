# Difference-in-Differences (DID) Implementation

## The Estimator

The canonical 2×2 DID compares the change in outcomes for a treated group before and after treatment to the change for a control group over the same period.

```
DID = (Ȳ_treated,post − Ȳ_treated,pre) − (Ȳ_control,post − Ȳ_control,pre)
```

This removes:
- Time-invariant group differences (e.g., treated units were always higher)
- Common time trends (e.g., both groups improved due to the economy)

What remains is attributable to the treatment — **if** the parallel trends assumption holds.

### Regression Formulation

```
Y_it = β₀ + β₁·Treated_i + β₂·Post_t + β₃·(Treated_i × Post_t) + ε_it
```

| Term | Meaning |
|------|---------|
| `β₁` | Baseline difference between treated and control |
| `β₂` | Common time trend (pre→post, for control group) |
| `β₃` | **The DID estimate** — the causal effect of treatment |

The coefficient `β₃` on the interaction term is your estimate. Everything else is absorbed by the fixed effects.

## Worked Numerical Example

Scenario: A city introduces a minimum wage increase in Q3 2023. We want to know the effect on restaurant employment.

| Group | Pre (Q2 2023) | Post (Q4 2023) | Change |
|-------|--------------|----------------|--------|
| Treated city | 1,200 workers | 1,150 workers | −50 |
| Control city | 980 workers | 960 workers | −20 |

```
DID = (1,150 − 1,200) − (960 − 980)
    = (−50) − (−20)
    = −30
```

Interpretation: The minimum wage increase caused a **30-worker reduction** in restaurant employment, beyond the −20 that would have happened anyway (the common trend).

Without the control group, you'd falsely attribute all −50 to the policy.

## Python Implementation

### Basic 2×2 DID with OLS

```python
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# Simulate data
np.random.seed(42)
n = 500

df = pd.DataFrame({
    'unit_id': np.repeat(np.arange(n), 2),
    'treated': np.repeat(np.random.binomial(1, 0.5, n), 2),
    'post': np.tile([0, 1], n),
})

# True effect: -30 for treated units in post period
true_effect = -30
df['y'] = (
    1000                                         # baseline
    + 200 * df['treated']                        # treated units are higher
    - 20 * df['post']                            # common time trend
    + true_effect * df['treated'] * df['post']   # treatment effect
    + np.random.normal(0, 50, len(df))           # noise
)

df['treated_post'] = df['treated'] * df['post']

# OLS regression
model = smf.ols('y ~ treated + post + treated_post', data=df).fit()
print(model.summary())

# Extract the DID coefficient
did_estimate = model.params['treated_post']
ci_low, ci_high = model.conf_int().loc['treated_post']
print(f"\nDID Estimate: {did_estimate:.2f}")
print(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}]")
```

### With Unit and Time Fixed Effects (Panel Data)

When you have multiple units and multiple time periods, include unit and time fixed effects. This is the standard approach for panel data — it controls for all time-invariant unit characteristics and all unit-invariant time shocks.

```python
import linearmodels as lm  # pip install linearmodels

# Set panel index
panel = df.set_index(['unit_id', 'post'])

# Two-way fixed effects (TWFE)
# Equivalent: Y ~ treated_post + EntityEffects + TimeEffects
mod = lm.PanelOLS.from_formula(
    'y ~ treated_post + EntityEffects + TimeEffects',
    data=panel
)
res = mod.fit(cov_type='clustered', cluster_entity=True)
print(res.summary)
```

**Always cluster standard errors at the unit level** when using panel data. Observations from the same unit are correlated; ignoring this understates standard errors.

### Parallel Trends Test (Event Study)

Before the treatment period, treated and control groups should trend together. Plot and test this formally using leads and lags.

```python
# Create relative time variable (periods relative to treatment)
# Assume treatment occurs at period 0
df['rel_time'] = df['post'] - 0   # adjust for your actual treatment timing

# For event study: create dummies for each period except the omitted base (t=-1)
# rel_time ∈ {-3, -2, -1(omitted), 0, 1, 2, ...}

event_study_formula = (
    'y ~ '
    + ' + '.join([f'C(rel_time)[{t}]:treated' for t in [-3, -2, 0, 1, 2]])
    + ' + C(unit_id) + C(post)'
)
es_model = smf.ols(event_study_formula, data=df).fit(
    cov_type='cluster', cov_kwds={'groups': df['unit_id']}
)

# Plot coefficients
import matplotlib.pyplot as plt

coefs = {t: es_model.params.get(f'C(rel_time)[{t}]:treated', np.nan)
         for t in [-3, -2, 0, 1, 2]}
cis   = {t: es_model.conf_int().loc[f'C(rel_time)[{t}]:treated']
         for t in coefs if not np.isnan(coefs[t])}

times = sorted(coefs.keys())
estimates = [coefs[t] for t in times]

plt.figure(figsize=(8, 4))
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(-0.5, color='red', linestyle=':', label='Treatment')
plt.plot(times, estimates, 'o-', color='steelblue')
plt.xlabel('Period relative to treatment')
plt.ylabel('Estimated effect')
plt.title('Event Study: Parallel Trends Check')
plt.legend()
plt.show()
```

**Interpretation**: Pre-treatment coefficients (relative time < 0) should be statistically indistinguishable from zero and visually flat. Post-treatment coefficients show the dynamic treatment effect over time.

## R Implementation

```r
library(tidyverse)
library(fixest)   # fast fixed effects; preferred over lm() for panels

# Basic 2x2 DID
model_basic <- lm(y ~ treated * post, data = df)
summary(model_basic)

# Two-way fixed effects with clustering
model_twfe <- feols(
  y ~ treated_post | unit_id + period,
  data = df,
  cluster = ~unit_id
)
etable(model_twfe)

# Event study with fixest
model_es <- feols(
  y ~ i(rel_time, treated, ref = -1) | unit_id + period,
  data = df,
  cluster = ~unit_id
)
iplot(model_es, main = "Event Study")
```

`fixest::feols` is faster than `lm()` or `plm()` for large panels and handles clustering correctly.

## Assumption Checks

### 1. Parallel Trends (Testable Pre-Treatment)

Run the event study above. Formally test that pre-treatment coefficients are jointly zero:

```python
from scipy import stats

# Collect pre-treatment coefficient estimates and their SEs
pre_coefs = [es_model.params[f'C(rel_time)[{t}]:treated'] for t in [-3, -2]]
pre_ses   = [es_model.bse[f'C(rel_time)[{t}]:treated']   for t in [-3, -2]]

# Joint F-test (informal: just check if all pre-period CIs include 0)
# Formal: use model.f_test() for joint hypothesis
hypotheses = 'C(rel_time)[-3]:treated = 0, C(rel_time)[-2]:treated = 0'
f_test = es_model.f_test(hypotheses)
print(f"Pre-trend F-test p-value: {f_test.pvalue:.3f}")
# Desired: p > 0.05 (fail to reject — consistent with parallel trends)
```

**Warning**: Failing to reject is not the same as confirming parallel trends. The test has limited power, especially with short pre-periods.

### 2. No Spillovers (SUTVA)

Treatment of one unit should not affect control units. If treated and control units compete (e.g., cities competing for workers), control units are contaminated. Solutions:
- Use geographically distant controls
- Exclude "border" units from control group
- Document why spillovers are implausible

### 3. No Anticipation

Units should not change behavior *before* the treatment is implemented. Signs of anticipation: the event study shows large movements at t = −1 rather than t = 0. Fix: shift the treatment date or exclude the anticipation window.

## Staggered Adoption (Modern DID)

When different units receive treatment at different times, the classic TWFE estimator can give **wrong answers** — including the wrong sign. This is the Callaway-Sant'Anna / Sun-Abraham problem.

### Why TWFE Fails with Staggered Treatment

TWFE implicitly uses already-treated units as controls for later-treated units. If treatment effects are heterogeneous, this "forbidden comparison" contaminates the estimate.

```python
# Diagnosing the problem: Bacon decomposition
# pip install bacondecomp
from bacondecomp import bacon

# df must have: unit, time, outcome, treatment_indicator
bacon_out = bacon(
    formula='y ~ treated',
    data=df,
    id_var='unit_id',
    time_var='period',
)
print(bacon_out)
# Shows how much of the TWFE estimate comes from each pair of timing groups
# and whether "forbidden" 2x2s are driving the result
```

### Callaway-Sant'Anna Estimator (Python)

```python
# pip install csdid
from csdid.att_gt import ATTgt

cs = ATTgt(
    yname='y',
    tname='period',
    idname='unit_id',
    gname='treatment_cohort',   # period when unit first treated (0 = never)
    data=df,
    control_group='notyettreated',  # use not-yet-treated as controls (preferred)
)
cs.fit()
cs.aggregate('simple')  # overall ATT
cs.aggregate('dynamic') # event-study style
```

In R:

```r
library(did)

cs_result <- att_gt(
  yname = "y",
  tname = "period",
  idname = "unit_id",
  gname = "treatment_cohort",
  data = df,
  control_group = "notyettreated"
)

aggte(cs_result, type = "simple")   # overall ATT
aggte(cs_result, type = "dynamic")  # event study
ggdid(cs_result)                    # plot
```

### When to Use Which Estimator

| Setting | Recommended Estimator |
|---------|----------------------|
| 2×2 (one treated group, one period) | Classic OLS with interaction |
| Multiple periods, single treatment timing | TWFE with event study |
| Staggered adoption, homogeneous effects | TWFE (still consistent) |
| Staggered adoption, heterogeneous effects | Callaway-Sant'Anna or Sun-Abraham |
| Staggered adoption, unsure | Run Bacon decomposition first |

## Inference and Standard Errors

| Data Structure | SE Approach |
|---------------|-------------|
| Cross-section (one pre, one post per unit) | Heteroskedasticity-robust (HC3) |
| Short panel, few clusters (< 30) | Wild cluster bootstrap |
| Panel, many clusters (≥ 30) | Cluster-robust at unit level |
| Aggregate data (state-level policy) | Cluster at state level; consider Conley spatial SEs |

**Never use default OLS standard errors with panel data.** Residuals within a unit across time are correlated; ignoring this causes standard errors to be too small, inflating t-statistics.

Wild cluster bootstrap in R:

```r
library(fwildclusterboot)

boot_res <- boottest(
  model_twfe,
  clustid = "unit_id",
  param = "treated_post",
  B = 9999
)
summary(boot_res)
```

## Robustness Checks Checklist

Run all of these before reporting results:

- [ ] **Placebo outcome**: Run DID on an outcome that should NOT be affected by the treatment. A significant effect signals a violation (common shock or data error).
- [ ] **Placebo treatment timing**: Pretend the treatment happened 2 periods earlier. Pre-trend estimates should be near zero.
- [ ] **Alternative control group**: Repeat with a different set of control units. Results should be directionally consistent.
- [ ] **Varying bandwidth**: For short panels, drop observations far from the treatment date and re-estimate.
- [ ] **Dropping treated units one at a time**: Check that results aren't driven by a single influential treated unit.
- [ ] **Different clustering levels**: Compare unit-level vs. group-level clustered SEs to check sensitivity.

## Common Misuses

**Misuse 1 — Running DID on aggregate means without regression**

The table arithmetic (Ȳ differences) is correct for point estimates but gives no standard error or inference. Always use the regression form.

**Misuse 2 — Using post-treatment periods as pre-treatment controls**

If the treatment has dynamic effects that persist, the post-treatment period for an earlier cohort is contaminated when used as "pre" for a later cohort. Callaway-Sant'Anna handles this by excluding already-treated units from the control group.

**Misuse 3 — Interpreting TWFE coefficients as ATT under heterogeneity**

Under staggered adoption with heterogeneous effects, `β₃` from TWFE is a weighted average where *negative* weights are possible. The estimate can have the opposite sign from the true average treatment effect.

**Misuse 4 — Parallel trends test as proof**

A flat pre-trend plot says "we have no evidence against parallel trends." It does not say "parallel trends holds." Unmeasured shocks could have hit the treated group exactly at treatment. Acknowledge this as a limitation.
