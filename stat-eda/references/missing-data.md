# Missing Data: Classification, Detection, and Handling

## The Three Mechanisms

Missing data is not random noise — it has a *cause*, and the cause determines which remedies are valid.

### MCAR — Missing Completely At Random

The probability of a value being missing is independent of **all** variables, observed or unobserved.

> Example: A lab technician accidentally drops one blood sample. The dropped sample has nothing to do with the patient's test result.

**Test**: Little's MCAR test (chi-square on the missing-data pattern). If MCAR holds, complete-case analysis (listwise deletion) gives unbiased estimates, just with reduced power.

**Consequence**: Any imputation method is valid. Listwise deletion is acceptable if missingness is low (< 5%).

---

### MAR — Missing At Random

The probability of being missing depends on **other observed variables** but NOT on the unobserved value itself.

> Example: Older survey respondents are less likely to answer income questions. Age is observed; the missing income value itself is not driving the missingness.

**Test**: Compare missingness indicator M against all other columns using logistic regression. If M is predictable from observed columns, suspect MAR.

**Consequence**: Multiple imputation and maximum-likelihood methods are valid under MAR. Listwise deletion is biased unless you also condition on the variables that drive missingness.

---

### MNAR — Missing Not At Random

The probability of being missing depends on the **unobserved value itself**.

> Example: People with very high income skip the income question *because* of their income.

**Test**: You cannot confirm MNAR from the data alone — it is a domain assumption. Check: "Would knowing the missing value change how likely it is to be missing?" If yes → MNAR.

**Consequence**: All standard imputation methods produce biased estimates. You need domain knowledge, sensitivity analysis, or a model of the missing-data mechanism. This is the hardest case.

---

## Quick Classification Checklist

```
1. Plot missingness rate by subgroup (age group, region, time period).
   └─ Is the rate uniform across groups?
      YES → MCAR candidate
      NO  → continue

2. Regress missingness indicator on all other observed columns.
   └─ Are any predictors significant (p < 0.05)?
      YES → MAR candidate
      NO  → revisit step 1

3. Domain knowledge: Does the missing value itself predict being missing?
   YES → MNAR — flag for domain expert review
   NO  → proceed with MAR-safe methods
```

---

## Detection: Code-Level

```python
import pandas as pd
import numpy as np

def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return per-column missing rate and MAR signal."""
    miss = df.isnull()
    total = len(df)
    summary = pd.DataFrame({
        "n_missing": miss.sum(),
        "pct_missing": miss.mean() * 100,
    })
    summary = summary[summary.n_missing > 0].sort_values("pct_missing", ascending=False)
    return summary

def mar_signals(df: pd.DataFrame, col: str) -> pd.Series:
    """
    For a column with missing values, check whether missingness correlates
    with other numeric columns. High absolute correlation → MAR signal.
    """
    indicator = df[col].isnull().astype(int)
    numeric_cols = df.select_dtypes(include="number").columns.drop(col, errors="ignore")
    correlations = df[numeric_cols].corrwith(indicator)
    return correlations.abs().sort_values(ascending=False)
```

**Pattern matrix** — shows which rows have simultaneous missingness:

```python
# Missingness co-occurrence (which columns are missing together)
miss_cols = df.columns[df.isnull().any()]
co_miss = df[miss_cols].isnull().astype(int).T.dot(df[miss_cols].isnull().astype(int))
# co_miss[i,j] = number of rows where both column i and j are missing
```

---

## Decision Framework

| Missingness % | Mechanism | Recommended Action |
|---------------|-----------|-------------------|
| < 5% | MCAR | Listwise deletion (or any imputation) |
| < 5% | MAR | Simple imputation (mean/median/mode) |
| < 5% | MNAR | Flag; domain-specific fix |
| 5–30% | MCAR | Simple imputation acceptable |
| 5–30% | MAR | Multiple imputation (MI) or model-based |
| 5–30% | MNAR | Sensitivity analysis required |
| > 30% | Any | Imputation results are fragile. Consider: (1) drop column, (2) add missingness indicator as new feature, (3) collect more data |

> **Iron Law reinforcement**: before imputing, check which rows are being dropped or filled. A column that is 40% missing is not a numeric variable — it is a different variable with sparse coverage.

---

## Imputation Methods

### 1. Mean / Median / Mode (Simple)

```python
from sklearn.impute import SimpleImputer

# Numeric → median (robust to outliers)
num_imputer = SimpleImputer(strategy="median")

# Categorical → most_frequent
cat_imputer = SimpleImputer(strategy="most_frequent")
```

**When valid**: MCAR or low-rate MAR.  
**Bias introduced**: attenuates variance and correlation with other variables. If the column appears in a regression, this underestimates the coefficient's standard error.

---

### 2. Multiple Imputation (MI)

MI creates **m copies** of the dataset, each with slightly different imputed values drawn from a model of the missing data. Results from analyses on each copy are combined using Rubin's rules.

**Rubin's combining rules** (for a scalar estimate Q̂ across m imputations):

```
Q̄  = (1/m) Σ Q̂ᵢ                    ← pooled estimate

W  = (1/m) Σ Var(Q̂ᵢ)                ← within-imputation variance

B  = [1/(m-1)] Σ (Q̂ᵢ - Q̄)²         ← between-imputation variance

T  = W + (1 + 1/m) × B              ← total variance

SE = √T
```

In Python:

```python
# Using sklearn IterativeImputer (MICE-style)
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge

m = 5  # number of imputations
imputed_datasets = []

for seed in range(m):
    imp = IterativeImputer(
        estimator=BayesianRidge(),
        max_iter=10,
        random_state=seed,
        sample_posterior=True  # draws from posterior → captures uncertainty
    )
    imputed_datasets.append(pd.DataFrame(imp.fit_transform(df), columns=df.columns))

# After running your analysis on each → pool with Rubin's rules
```

**When valid**: MAR assumption. The imputation model must include all variables that explain missingness.

**Minimum m**: 5 imputations suffice when missingness fraction γ ≤ 20%. Rule of thumb: m ≥ 100γ (e.g., 40% missingness → m ≥ 40).

---

### 3. K-Nearest Neighbors Imputation

For row i with missing value in column j: find k rows with no missing value in j, weighted by distance in other observed dimensions, and average their values.

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=5, weights="distance")
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
```

**When valid**: MCAR or MAR, when the feature space has meaningful distance (avoid mixing raw counts with proportions — normalize first).  
**Caution**: slow on large datasets; sensitive to scale.

---

### 4. Missingness Indicator (Add-Indicator Pattern)

Instead of (or in addition to) imputing, add a binary column `{col}_was_missing` before imputation.

```python
def add_missing_indicators(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    df = df.copy()
    for col in cols:
        df[f"{col}_was_missing"] = df[col].isnull().astype(int)
    return df
```

**When to use**:
- MNAR: the fact that income is missing *is itself* informative
- Any column with > 10% missingness fed into a downstream model
- Protects against the case where your imputed value is wrong but the model can learn "this row had missing X"

---

## Worked Example

**Dataset**: 1,000 e-commerce orders with columns `order_value`, `customer_age`, `region`, `return_flag`.  
`customer_age` has 120 missing values (12%).

**Step 1 — Rate and pattern**
```
n_missing: 120 (12%)
Missing by region: North=35%, South=5%, East=8%, West=7%
```
North has 4× higher missingness → not MCAR.

**Step 2 — MAR signal**
```python
mar_signals(df, "customer_age")
# region_encoded    0.41   ← strong signal
# order_value       0.09
# return_flag       0.03
```
`region` strongly predicts missingness. This looks like MAR.

**Step 3 — Imputation choice**

12% missing, MAR → use `IterativeImputer` (MICE) with `sample_posterior=True`, m=5 imputations. Include `region` as a predictor in the imputation model.

Also add `customer_age_was_missing` as a feature for downstream models.

**Step 4 — Sanity check after imputation**

```python
# Distribution should not shift dramatically
print(df["customer_age"].describe())
print(imputed_datasets[0]["customer_age"].describe())

# Mean before: 34.2  → mean after: 34.7 (plausible)
# Std  before: 11.4  → std  after: 11.1 (slight attenuation is normal)
```

If the imputed mean shifts by > 1 SD or the distribution becomes bimodal, the imputation model is mis-specified — recheck which predictors you included.

---

## What NOT to Do

| Mistake | Why it fails |
|---------|-------------|
| Drop all rows with any missing value | Listwise deletion biases results under MAR; destroys data under high missingness |
| Impute with global mean before train/test split | Leaks test-set information into imputation → inflated evaluation metrics |
| Impute MNAR data with MI and call it done | MI is only valid under MAR; MNAR bias remains |
| Impute then check distribution and declare success | Distribution match is necessary but not sufficient — correlations with other variables may still be distorted |
| Treat a 60%-missing column as a normal feature | At that point, presence/absence IS the variable; the numeric values add little signal |

---

## Imputation Before vs. After Train/Test Split

Always fit the imputer on **train data only**, then apply to test:

```python
from sklearn.pipeline import Pipeline
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer
from sklearn.ensemble import GradientBoostingClassifier

pipeline = Pipeline([
    ("imputer", IterativeImputer(random_state=0)),
    ("model", GradientBoostingClassifier()),
])

pipeline.fit(X_train, y_train)
pipeline.predict(X_test)  # imputer uses train-fit statistics on test data
```

Fitting the imputer inside a `Pipeline` enforces this automatically.
