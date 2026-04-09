# WOE Binning

Weight of Evidence (WOE) binning transforms continuous or categorical features into a monotonic numeric representation that directly encodes the log-odds relationship with the binary outcome (default=1). It is the standard preprocessing step for logistic regression scorecards because it linearises the relationship between the feature and log-odds, handles missing values as a separate bin, and produces IV (Information Value) as a feature selection metric.

---

## Formulas

For a feature split into *k* bins:

```
WOE_i = ln( %Non-Events_i / %Events_i )
      = ln( (n_good_i / N_good) / (n_bad_i / N_bad) )
```

Where:
- **Event / Bad** = default (outcome = 1)
- **Non-Event / Good** = non-default (outcome = 0)
- `n_bad_i` = count of bads in bin *i*; `N_bad` = total bads across all bins
- `n_good_i` = count of goods in bin *i*; `N_good` = total goods across all bins

```
IV_i  = (  %Non-Events_i  -  %Events_i  ) × WOE_i
IV    = Σ IV_i   (sum over all bins)
```

**Sign convention**: A bin where bads are over-represented relative to the overall bad rate has negative WOE (riskier). A bin where goods dominate has positive WOE (safer). This sign is correct for a logistic regression where higher WOE = lower default probability.

---

## Step-by-Step Procedure

### Step 1 — Initial Binning

Split the feature into candidate bins before computing WOE:

| Feature type | Starting method |
|---|---|
| Continuous (income, utilization) | Equal-frequency quantiles, typically 10-20 bins |
| Ordinal (credit grade A/B/C) | One bin per category initially |
| Binary (has_mortgage) | Two bins |
| Missing values | Always a separate bin; never impute before WOE |

For continuous features, equal-frequency bins ensure each bin has enough observations to estimate stable bad rates. Do **not** use equal-width bins; they concentrate observations in dense regions and leave sparse bins with unstable WOE estimates.

### Step 2 — Check Bin Quality

Each bin must satisfy:
- **Minimum 5% of population** (or at least 100 observations if dataset is small)
- **At least 1 bad and 1 good** — a pure bin (all good or all bad) makes WOE undefined (ln(0) or ln(∞))

Bins that fail either criterion must be merged with an adjacent bin before computing WOE.

### Step 3 — Merge for Monotonicity

For continuous features, WOE must be **monotonically increasing or decreasing** as the feature value increases. Non-monotonic bins indicate noise or a true non-linear relationship.

Merge adjacent bins that break monotonicity using the following rule:
1. Scan bins in order; find the first adjacent pair where WOE direction reverses
2. Merge the smaller of the two bins into the larger neighbour
3. Recompute WOE for the merged bin
4. Repeat until monotonicity holds across all bins

If monotonicity cannot be achieved without reducing to 3 or fewer bins, the feature may have a true non-linear relationship. Consider creating a flag variable (e.g., `utilization > 80%`) instead of a continuous WOE transformation.

### Step 4 — Compute Final WOE and IV

After bins are stable and monotonic, compute WOE and IV for each bin.

### Step 5 — Replace Feature Values

Substitute each raw observation's feature value with the WOE of the bin it falls into. The transformed feature is now ready as direct input to logistic regression.

---

## Worked Example: Credit Utilization

Dataset: 10,000 borrowers, 350 bads (3.5% bad rate), 9,650 goods.

**Initial 10 equal-frequency bins (1,000 obs each):**

| Bin | Util Range | n | n_bad | n_good | %Bad | %Good | WOE | IV_i |
|-----|-----------|---|-------|--------|------|-------|-----|------|
| 1 | 0–10% | 1000 | 10 | 990 | 2.86% | 10.26% | ln(10.26/2.86) = **1.277** | 0.095 |
| 2 | 10–20% | 1000 | 20 | 980 | 5.71% | 10.16% | ln(10.16/5.71) = **0.576** | 0.026 |
| 3 | 20–30% | 1000 | 25 | 975 | 7.14% | 10.10% | ln(10.10/7.14) = **0.347** | 0.010 |
| 4 | 30–40% | 1000 | 28 | 972 | 8.00% | 10.07% | ln(10.07/8.00) = **0.230** | 0.005 |
| 5 | 40–50% | 1000 | 32 | 968 | 9.14% | 10.03% | ln(10.03/9.14) = **0.093** | 0.001 |
| 6 | 50–60% | 1000 | 38 | 962 | 10.86% | 9.97% | ln(9.97/10.86) = **−0.085** | 0.001 |
| 7 | 60–70% | 1000 | 45 | 955 | 12.86% | 9.90% | ln(9.90/12.86) = **−0.261** | 0.008 |
| 8 | 70–80% | 1000 | 55 | 945 | 15.71% | 9.79% | ln(9.79/15.71) = **−0.473** | 0.028 |
| 9 | 80–90% | 1000 | 62 | 938 | 17.71% | 9.72% | ln(9.72/17.71) = **−0.601** | 0.048 |
| 10 | 90–100% | 1000 | 35 | 965 | 10.00% | 10.00% | ln(10.00/10.00) = **0.000** | 0.000 |

**%Bad** = `n_bad_i / N_bad × 100` = `n_bad_i / 350 × 100`  
**%Good** = `n_good_i / N_good × 100` = `n_good_i / 9650 × 100`

**Monotonicity check**: Bins 1–9 show decreasing WOE (good, borrowers with higher utilization are riskier). Bin 10 breaks monotonicity — WOE jumps from −0.601 back to 0.000. This is suspicious; very high utilization borrowers appearing less risky than 80-90% is likely noise or a distinct subpopulation (e.g., convenience users who pay in full).

**After merging bin 9 and 10:**

| Bin | Util Range | n | n_bad | n_good | WOE | IV_i |
|-----|-----------|---|-------|--------|-----|------|
| 9+10 | 80–100% | 2000 | 97 | 1903 | ln((1903/9650) / (97/350)) = ln(0.1972/0.2771) = **−0.340** | 0.027 |

Now WOE is monotonically decreasing from bin 1 to bin 9+10. Total IV = Σ IV_i ≈ **0.221** (strong predictor).

---

## IV Interpretation Table

| IV | Predictive Power |
|----|-----------------|
| < 0.02 | Useless — drop the feature |
| 0.02 – 0.10 | Weak predictor |
| 0.10 – 0.30 | Medium predictor — include |
| 0.30 – 0.50 | Strong predictor |
| > 0.50 | Suspiciously strong — check for data leakage |

IV > 0.50 almost always indicates target leakage: the feature is derived from or correlated with the outcome label after the observation period. A common example is "total payments made" which reflects whether the borrower subsequently defaulted.

---

## Missing Value Bin

Missing values must be treated as a separate bin, not imputed:

```python
# Correct: missing becomes its own bin
df['util_woe'] = df['utilization'].map(bin_to_woe).fillna(woe_missing_bin)

# Wrong: imputing before binning hides information
df['utilization'] = df['utilization'].fillna(df['utilization'].median())
```

Compute the WOE of the missing bin the same way: count bads and goods among borrowers with missing values and apply the formula. If missing values are rare (<1% of population), you may merge the missing bin with the bin whose WOE is closest in value. If missing values are frequent (>5%), the missing pattern itself is informative — keep it as a separate bin and check if missingness correlates with default.

---

## Handling Categorical Features

For nominal categoricals (e.g., employment type: employed / self-employed / unemployed / student):

1. Compute raw bad rate for each category
2. Sort categories by bad rate ascending
3. Apply the same monotonic merging logic as for continuous features
4. Categories with identical or near-identical bad rates can be merged

If a category has fewer than 50 observations or zero bads/goods, merge it with the most similar category before computing WOE.

For high-cardinality categoricals (e.g., zip code with 1,000+ values): group into meaningful macro-categories first (e.g., region), then apply WOE. Directly WOE-encoding thousands of sparse categories will overfit.

---

## Python Implementation (stdlib + pandas)

```python
import numpy as np
import pandas as pd

def compute_woe_iv(df: pd.DataFrame, feature: str, target: str, bins: int = 10) -> pd.DataFrame:
    """
    Returns a DataFrame with bin boundaries, WOE, IV per bin.
    target: 1 = bad (default), 0 = good
    """
    total_bad = df[target].sum()
    total_good = (df[target] == 0).sum()

    # Equal-frequency binning; missing values become their own bin
    df = df[[feature, target]].copy()
    df['bin'] = pd.qcut(df[feature], q=bins, duplicates='drop')

    # Add missing bin
    missing_mask = df[feature].isna()
    if missing_mask.any():
        df.loc[missing_mask, 'bin'] = 'Missing'

    grouped = df.groupby('bin', observed=False)[target].agg(
        n_bad='sum',
        n=('count')
    )
    grouped['n_good'] = grouped['n'] - grouped['n_bad']
    grouped['pct_bad']  = grouped['n_bad']  / total_bad
    grouped['pct_good'] = grouped['n_good'] / total_good

    # Avoid log(0)
    grouped['pct_bad']  = grouped['pct_bad'].clip(lower=1e-9)
    grouped['pct_good'] = grouped['pct_good'].clip(lower=1e-9)

    grouped['woe'] = np.log(grouped['pct_good'] / grouped['pct_bad'])
    grouped['iv']  = (grouped['pct_good'] - grouped['pct_bad']) * grouped['woe']

    return grouped.reset_index()


def apply_woe_transform(df: pd.DataFrame, feature: str, woe_table: pd.DataFrame) -> pd.Series:
    """Map raw feature values to WOE scores using the fitted woe_table."""
    bin_col = pd.cut(df[feature], bins=woe_table['bin'].cat.categories)
    return bin_col.map(woe_table.set_index('bin')['woe'])
```

This implementation is illustrative. Production implementations typically use [`scorecardpy`](https://github.com/ShichenXie/scorecardpy) or [`optbinning`](https://github.com/guillermo-navas-palencia/optbinning) which handle monotonicity enforcement, statistical tests for bin boundaries, and edge cases more robustly.

---

## Interaction with the Scorecard Scaling Step

After WOE transformation and logistic regression fitting, the model output is:

```
log-odds = β₀ + β₁·WOE(feature_1) + β₂·WOE(feature_2) + ...
```

The credit score is then:

```
Score = Offset + Factor × log-odds
      = Offset + Factor × (β₀ + Σ βᵢ · WOEᵢ)
```

Typical scaling: **Score = 600 − 20 × log-odds** (doubles-odds point = 20 points, base score = 600 at even odds). This scales so that every 20-point increase in score corresponds to halving the odds of default.

Each feature's score contribution is:

```
Points_i = Factor × βᵢ × WOE_i
```

This additive decomposition — one contribution per WOE bin — is what makes logistic regression + WOE the dominant approach in regulated lending: the model is fully explainable as a points table.

---

## Common Mistakes

**Over-binning**: Starting with 50 fine-grained bins then merging creates overfitted WOE estimates. A bad rate of 0/50 in one bin makes WOE undefined. Start with 10-20 bins.

**Fitting WOE on the full dataset**: WOE must be computed on the training fold only and then applied (without refitting) to validation and test folds. Computing WOE on the full dataset and then splitting leaks label information into the validation set, inflating AUC by 2-5 points.

**Forcing monotonicity on truly non-monotonic features**: Some features (e.g., age) have U-shaped risk profiles — young and very old borrowers are both higher risk. Forcing monotonicity destroys this signal. Use segmented models or polynomial terms instead.

**Ignoring PSI for bin boundaries over time**: WOE bins fitted on 2022 data may not align with the 2024 population. If PSI > 0.25 for a feature, the bin boundaries should be re-examined — the WOE values may have shifted direction.

**Treating WOE as monotonic for categorical features**: The monotonicity requirement applies to ordered continuous features. For nominals, WOE is just a numeric encoding of the bad rate ratio; there is no monotonicity constraint.
