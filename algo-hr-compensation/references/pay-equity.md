# Pay Equity Regression Analysis

Pay equity analysis determines whether unexplained compensation gaps exist across demographic groups after controlling for **legitimate pay factors** (job level, experience, performance). The regression approach is the legal and statistical standard — raw mean comparisons without controls are misleading and legally insufficient.

---

## Core Concept: Explained vs. Unexplained Gaps

**Raw gap**: The average pay difference between Group A and Group B with no controls applied.

**Unexplained gap**: The residual pay difference after controlling for all legitimate, job-related factors. This is what courts and regulators scrutinize.

```
Unexplained Gap = Raw Gap − (Gap explained by level, tenure, performance, role, location...)
```

A company may have a 15% raw gender pay gap that shrinks to 2% after controlling for level — because men hold more senior positions. The 2% unexplained gap is the equity problem to address. The 13% explained gap may reflect a *representation* problem, but that is a separate analysis.

---

## Legitimate Pay Factors (Control Variables)

Include only factors that are:
- **Job-related** — directly tied to work requirements or performance
- **Documented** — captured in HR systems, not reconstructed retroactively
- **Applied consistently** — same criteria used across all employees

| Variable | Type | Notes |
|----------|------|-------|
| Job level / grade | Categorical | Most important control; prevents comparing IC5 vs IC2 |
| Job family / function | Categorical | Engineer vs. PM vs. Sales differ legitimately |
| Years of relevant experience | Continuous | Total or role-specific; cap at ~20 to avoid outlier distortion |
| Tenure at company | Continuous | Distinguish from total experience |
| Geographic location | Categorical | SF vs. Taipei vs. remote policy tier |
| Performance rating | Ordinal/Continuous | Only if ratings are applied consistently; if biased, omit |
| Educational credential | Categorical | Only when genuinely required for the role |
| Full-time vs. part-time | Binary | Adjust to FTE-equivalent base if needed |

**Do NOT include as controls:**
- Prior salary (perpetuates historical bias; illegal to use in many jurisdictions)
- Negotiation outcome (if negotiation itself shows demographic disparity)
- Time since last raise (if raise decisions themselves are inequitable)

---

## Regression Model

### Model Specification

Run OLS regression with log-transformed base salary as the dependent variable. Log transformation handles the right-skewed nature of salary distributions and makes coefficients interpretable as percentage differences.

```
ln(base_salary_i) = β₀ 
                  + β₁·level_i 
                  + β₂·job_family_i 
                  + β₃·experience_i 
                  + β₄·tenure_i 
                  + β₅·location_i 
                  + β₆·performance_i 
                  + γ·gender_i         ← group indicator
                  + ε_i
```

`γ` is the coefficient of interest. If the group indicator is binary (0/1), then `e^γ − 1` gives the unexplained pay gap as a percentage.

### Multiple Group Indicators

For more than two groups (e.g., race/ethnicity with 4+ categories), use dummy variables with one reference group:

```
+ γ₁·asian_i + γ₂·black_i + γ₃·hispanic_i   (reference: white)
```

Each γ is interpreted relative to the reference group after controls.

### Interaction Terms (Advanced)

If you suspect pay disparities concentrate at specific levels (e.g., gap only exists for senior roles), add an interaction:

```
+ δ·(gender_i × senior_level_i)
```

This is more complex to interpret and requires larger sample sizes. Use only when exploratory analysis suggests level-specific effects.

---

## Python Implementation

```python
import json
import math
import statistics
from typing import Any

def run_pay_equity_regression(employees: list[dict]) -> dict:
    """
    Minimal OLS pay equity regression using pure stdlib.
    
    Each employee record requires:
      base_salary, level (int 1-6), experience_years (float),
      tenure_years (float), is_female (0/1), performance (1-5 int)
    
    Returns coefficient for gender indicator with standard error and p-approx.
    For production, use statsmodels or R — this is for verification/learning only.
    """
    n = len(employees)
    if n < 30:
        return {"error": "Sample too small for reliable regression (need >= 30)"}

    # Build design matrix X and target y = ln(salary)
    # Variables: intercept, level, experience, tenure, is_female, performance
    def build_row(e):
        return [
            1.0,
            float(e["level"]),
            float(e["experience_years"]),
            float(e["tenure_years"]),
            float(e["is_female"]),
            float(e["performance"]),
        ]

    X = [build_row(e) for e in employees]
    y = [math.log(e["base_salary"]) for e in employees]
    
    # OLS: β = (X'X)^-1 X'y  — use scipy in production
    # This stub returns the structure; real computation needs matrix inversion
    return {
        "note": "Use statsmodels.OLS or R lm() for production",
        "n": n,
        "dependent_var": "ln(base_salary)",
        "controls": ["level", "experience_years", "tenure_years", "performance"],
        "group_indicator": "is_female",
    }
```

### Production Code (statsmodels)

```python
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np

def pay_equity_analysis(df: pd.DataFrame, group_col: str = "is_female") -> dict:
    """
    df columns required: base_salary, level, job_family, experience_years,
                         tenure_years, location, performance, {group_col}
    """
    df = df.copy()
    df["ln_salary"] = np.log(df["base_salary"])

    formula = (
        "ln_salary ~ C(level) + C(job_family) + experience_years "
        "+ tenure_years + C(location) + performance + " + group_col
    )

    model = smf.ols(formula=formula, data=df).fit()

    coef = model.params[group_col]
    pval = model.pvalues[group_col]
    ci_low, ci_high = model.conf_int().loc[group_col]

    gap_pct = (np.exp(coef) - 1) * 100

    return {
        "unexplained_gap_pct": round(gap_pct, 2),
        "coefficient": round(coef, 4),
        "p_value": round(pval, 4),
        "ci_95": [round(np.exp(ci_low) - 1, 4), round(np.exp(ci_high) - 1, 4)],
        "r_squared": round(model.rsquared, 3),
        "n": int(model.nobs),
        "statistically_significant": pval < 0.05,
    }
```

---

## Worked Example

### Dataset

500 employees, software company, Taiwan market. Analyzing gender pay equity.

| Metric | Value |
|--------|-------|
| Employees analyzed | 487 (13 excluded: missing data) |
| Female employees | 142 (29%) |
| Raw gender pay gap | −11.4% (women earn 11.4% less) |
| Control variables | level (L1-L6), job_family, experience, tenure, location, performance |

### Regression Output

```
Dependent variable: ln(base_salary)
N = 487, R² = 0.847

Coefficients:
  Intercept           12.847   p < 0.001
  C(level)[L2]         0.142   p < 0.001
  C(level)[L3]         0.289   p < 0.001
  C(level)[L4]         0.451   p < 0.001
  C(level)[L5]         0.621   p < 0.001
  C(level)[L6]         0.803   p < 0.001
  experience_years     0.018   p < 0.001
  tenure_years         0.012   p = 0.003
  performance          0.031   p < 0.001
  is_female           -0.032   p = 0.041   ← key result
```

### Interpreting the Result

```
gap_pct = (e^(-0.032) - 1) × 100 = -3.15%
```

After controlling for level, experience, tenure, performance, and location:
- Women earn **3.15% less** than men in equivalent roles
- p = 0.041 → statistically significant at α = 0.05
- 95% CI: [−6.1%, −0.2%] — does not include zero

**Interpretation**: The raw 11.4% gap is largely explained by level distribution (women are underrepresented at L5/L6). The remaining 3.15% unexplained gap is statistically significant and warrants action.

---

## Flagging Thresholds

There is no universal legal threshold. Use the following as operational guidelines:

| Unexplained Gap | Statistical Significance | Action |
|-----------------|--------------------------|--------|
| < 1% | Any | Monitor; no immediate action |
| 1–2% | p > 0.10 | Watch list; resurvey next cycle |
| 1–2% | p < 0.05 | Investigate individual cases |
| 2–5% | p < 0.05 | Remediation plan required |
| > 5% | p < 0.05 | Immediate remediation + legal review |
| Any | p < 0.01 + n > 100 | Escalate to legal counsel |

**Practical significance matters too.** A 1.5% gap in a company of 2,000 employees earning NT$2M average = NT$30,000/year per affected employee. Aggregate exposure is material even if the coefficient looks small.

---

## Segmented Analysis

Run the regression separately by:

- **Job family**: Engineering gap ≠ Sales gap; pooling hides differences
- **Level band**: Junior (L1-L3) vs. Senior (L4-L6) may show different patterns
- **Location**: Taipei vs. remote employees

For each segment, record:

```json
{
  "segment": "Engineering / Senior",
  "n": 94,
  "gap_pct": -2.8,
  "p_value": 0.031,
  "action_required": true
}
```

Be cautious with small segments: below n=30, regression is unreliable. Report confidence intervals wide when n is small; do not claim no gap simply because p > 0.05 with small samples (Type II error risk).

---

## Remediation Workflow

When a statistically significant unexplained gap is confirmed:

1. **Identify affected employees** — extract the subset where group membership predicts lower pay after controls
2. **Individual case review** — verify controls were correctly applied (was performance rating accurate? was level correct?)
3. **Calculate adjustment amounts** — for each flagged employee, compute the pay increment needed to bring them to parity, using the model's predicted salary as the target
4. **Prioritize by materiality** — sort by absolute dollar gap; remediate largest gaps first if budget is constrained
5. **Set remediation timeline** — immediate off-cycle adjustment vs. next merit cycle (immediate preferred for gaps > 3%)
6. **Re-run analysis post-adjustment** — confirm gap closes; document result

### Adjustment Calculation

```python
def compute_adjustment(actual_salary, predicted_salary_at_parity, buffer_pct=0.0):
    """
    predicted_salary_at_parity: model predicted salary assuming no group penalty
    buffer_pct: optional buffer (e.g., 0.02 = bring to 2% above parity)
    """
    target = predicted_salary_at_parity * (1 + buffer_pct)
    if actual_salary < target:
        return {
            "adjustment_needed": True,
            "current": actual_salary,
            "target": round(target),
            "increase": round(target - actual_salary),
            "increase_pct": round((target / actual_salary - 1) * 100, 1)
        }
    return {"adjustment_needed": False, "current": actual_salary}
```

---

## Common Errors

**Controlling for endogenous variables.** Do not control for variables that are themselves outcomes of pay discrimination. Example: if promotion rates are biased, controlling for level absorbs the discrimination and understates the gap. In such cases, report both the controlled and uncontrolled gap.

**Using raw performance scores without checking inter-rater reliability.** If managers rate women lower systematically, including performance as a control removes a biased variable as if it were legitimate. Validate performance ratings for demographic patterns before including them.

**Treating non-significance as proof of equity.** p > 0.05 with n=40 proves very little. Report the confidence interval and note that the test is underpowered. Do not write "no pay gap found" — write "gap could not be detected with current sample size."

**Running one pooled regression across the whole company.** A company-wide regression with many job families produces coefficients that reflect the average effect — hiding large gaps in specific functions. Always segment.

**Forgetting total compensation.** A base salary regression may show parity, but if bonus targets, equity grants, or commission structures differ by group, total comp equity remains a problem. Run separate regressions for each pay component if data allows.

---

## Legal Notes (Taiwan Context)

Under Taiwan's **Gender Equality in Employment Act (性別工作平等法)**, Article 10 prohibits discriminatory wage differences for equivalent work. "Equivalent work" is defined by job content, responsibilities, and working conditions — not job title. This aligns with the regression methodology: courts would look at whether pay differences can be explained by legitimate, job-related factors.

Key practical points:
- Maintain documentation of the legitimate pay factors used to set each employee's salary
- Remediation records (analysis, identified gaps, corrective actions, timeline) should be retained
- Legal counsel should review findings before any public disclosure or government inquiry response
- Analysis performed with outside legal counsel may qualify for attorney-client privilege

The analysis methodology here is not legal advice. Engage employment law counsel before acting on findings in a formal proceeding.
