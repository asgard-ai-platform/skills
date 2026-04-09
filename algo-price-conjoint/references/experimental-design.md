# Experimental Design for Conjoint Analysis

Experimental design determines which product profiles are shown to respondents. A poor design produces correlated attribute estimates (you can't tell if preference is driven by Brand or RAM) or wastes respondents' attention on redundant choice sets. This document covers design types, efficiency metrics, and a worked example using the Laptop scenario from the parent skill.

---

## 1. The Problem: Why You Can't Show Everything

For the Laptop example (Brand × RAM × Price = 3 × 3 × 3), the full factorial has 27 profiles. A CBC study with 3 profiles per choice set would need 9 choice sets just to show every profile once — before considering that each respondent needs 10-15 choice sets for stable estimates. In practice, attributes scale fast:

| Attributes | Levels Each | Full Factorial Profiles |
|-----------|-------------|------------------------|
| 3         | 3           | 27                     |
| 5         | 3           | 243                    |
| 6         | 3           | 729                    |
| 7         | 4           | 16,384                 |

Beyond ~32 profiles, full factorial is infeasible. You need a subset.

---

## 2. Design Types

### 2.1 Full Factorial

Show every combination of every attribute level. Feasible only when:
- Total profiles ≤ 16, **and**
- You want to estimate all interaction effects

For the 3×3×3 Laptop case: 27 profiles, organized into 9 choice sets of 3. Doable, but at the edge of practical.

### 2.2 Fractional Factorial (Orthogonal Arrays)

A pre-constructed subset of profiles where main effects are uncorrelated. Sizes are constrained to specific array dimensions.

**How to pick:** Find an orthogonal array L_n that supports your number of attributes and levels.

Common arrays for 3-level attributes:

| Array | Profiles | Max 3-level Attributes |
|-------|----------|------------------------|
| L9    | 9        | 4                      |
| L18   | 18       | 7 (plus one 2-level)   |
| L27   | 27       | 13                     |

**Worked example — Laptop 3×3×3 using L9:**

L9 orthogonal array (columns: Brand, RAM, Price):

| Profile | Brand | RAM   | Price |
|---------|-------|-------|-------|
| 1       | Apple | 8GB   | $800  |
| 2       | Apple | 16GB  | $1200 |
| 3       | Apple | 32GB  | $1600 |
| 4       | Dell  | 8GB   | $1200 |
| 5       | Dell  | 16GB  | $1600 |
| 6       | Dell  | 32GB  | $800  |
| 7       | Lenovo| 8GB   | $1600 |
| 8       | Lenovo| 16GB  | $800  |
| 9       | Lenovo| 32GB  | $1200 |

Each brand appears exactly 3 times. Each RAM level appears exactly 3 times. Each price appears exactly 3 times. Every Brand-RAM pair appears exactly once. This orthogonality means Brand and RAM estimates are uncorrelated.

**Limitation:** L9 assumes no interaction effects. If Apple laptops are less price-sensitive than Lenovo, this design cannot detect it.

### 2.3 D-Optimal Design

Instead of using a pre-built array, D-optimal generates a custom design that maximizes the determinant of the information matrix **X'X**, which minimizes the volume of the confidence ellipsoid around parameter estimates.

**When to use over orthogonal arrays:**
- Mixed levels (some attributes have 2 levels, others have 4)
- Constraints: certain combinations are impossible (e.g., Budget brand + $2000 price is unrealistic)
- You need a specific number of choice sets that doesn't match a standard array

**Objective function:**

Maximize:
$$D = \det(\mathbf{X}'\mathbf{X})^{1/p}$$

where **X** is the design matrix (coded attribute levels as indicator variables) and *p* is the number of parameters to estimate.

D-efficiency is reported as a percentage relative to a theoretical maximum:

$$D\text{-efficiency} = 100 \times \left(\frac{\det(\mathbf{X}'\mathbf{X})}{n^p}\right)^{1/p}$$

A D-efficiency ≥ 70% is generally acceptable. Below 50% means estimates will have large standard errors.

**How to generate (conceptual algorithm):**
1. Start with a random set of *n* choice sets
2. Iteratively swap profiles in/out to increase D
3. Stop when no swap improves D by more than a threshold (e.g., 0.001%)

Software: Sawtooth Software's CBC design module, R packages `AlgDesign` or `idefix`.

### 2.4 Balanced Overlap (Sawtooth Method)

Balanced overlap is a randomized design method that:
- Each attribute level appears approximately equally often across all respondents
- Within a choice set, the same level CAN appear more than once for a given attribute (overlap)

Overlap is intentional: showing "Apple $800 vs Dell $800" helps estimate brand utility independently of price.

**When to use:**
- Large-scale CBC studies with HB estimation
- You're using Sawtooth Software
- You have 300+ respondents (HB converges well with balanced overlap)

**When NOT to use:**
- Small samples (<100 respondents): overlap wastes choice set "power"
- You need exact orthogonality for MNL estimation

---

## 3. Design Type Decision Framework

```
Start
  │
  ▼
How many attributes × levels?
  │
  ├─ ≤4 attributes, all same level count, ≤2 interactions needed
  │    → Full Factorial (if ≤16 profiles) or L9/L18 Orthogonal Array
  │
  ├─ Mixed levels OR constraints (impossible combos)
  │    → D-Optimal
  │
  └─ 5+ attributes, 300+ respondents, using HB estimation
       → Balanced Overlap (Sawtooth default)
```

Rule of thumb for number of choice sets per respondent:

$$\text{Choice sets} = \max\!\left(10,\ \left\lceil\frac{3 \times p}{k-1}\right\rceil\right)$$

where *p* = number of parameters (attribute levels minus 1, summed across attributes), *k* = profiles per choice set (typically 3-4).

For the 3×3×3 Laptop: *p* = (3-1)+(3-1)+(3-1) = 6, *k* = 3.

$$\text{Choice sets} = \max\!\left(10,\ \left\lceil\frac{3 \times 6}{2}\right\rceil\right) = \max(10, 9) = 10$$

10 choice sets per respondent minimum.

---

## 4. Coding Attribute Levels

How you code levels affects the design matrix and what the intercept means.

### Effects Coding (Recommended for Conjoint)

For an attribute with *m* levels, use *m-1* dummy variables. The last level is the reference, coded as −1 for all dummies (not 0 as in treatment coding).

**Example — Brand (3 levels):**

| Level  | x_Apple | x_Dell |
|--------|---------|--------|
| Apple  | 1       | 0      |
| Dell   | 0       | 1      |
| Lenovo | −1      | −1     |

The part-worth for Lenovo = −(part-worth for Apple + part-worth for Dell).

This constraint forces part-worths to sum to zero within each attribute, which makes "importance" calculations consistent across attributes.

### Why NOT Treatment (0/1) Coding

Treatment coding absorbs brand effects into the intercept. The "Lenovo" level has no explicit coefficient — its utility is implicitly zero. This makes attribute importance calculations inconsistent: the range of Lenovo-related utility is invisible.

---

## 5. Evaluating Design Quality Before Fielding

Before launching, check these three properties:

### 5.1 Level Balance

Each level appears the same number of times across all choice sets × positions.

Check: for each attribute, count how many times each level appears. Ratio of max to min count should be < 1.5.

```python
# Quick balance check (pseudocode)
from collections import Counter

def check_balance(design, attribute_col):
    counts = Counter(design[attribute_col])
    levels = list(counts.values())
    ratio = max(levels) / min(levels)
    return ratio  # should be < 1.5

```

### 5.2 Orthogonality (for non-overlap designs)

Check pairwise correlations between all attribute columns in the design matrix. For a fully orthogonal design, all off-diagonal correlations = 0.

In practice, |r| < 0.3 between any pair of attributes is acceptable.

```python
import numpy as np

def check_orthogonality(X):
    """X: design matrix with effects coding, shape (n_profiles, n_params)"""
    corr = np.corrcoef(X.T)
    off_diag = corr[np.triu_indices_from(corr, k=1)]
    print(f"Max |r|: {np.abs(off_diag).max():.3f}")
    print(f"Mean |r|: {np.abs(off_diag).mean():.3f}")
```

### 5.3 Minimum Overlap (for CBC specifically)

In a choice set, the same level of an attribute appearing in all alternatives gives no information about that attribute. Count tasks where this happens:

$$\text{Overlap rate} = \frac{\text{tasks with all-same level for any attribute}}{\text{total tasks}}$$

For random designs: overlap rate > 30% signals a problem. Balanced overlap designs intentionally allow some overlap, but it should be controlled.

---

## 6. Holdout Choice Sets

Reserve 1-2 choice sets per respondent that are NOT used in model estimation. Use them to validate predictive accuracy.

**Construction rule:**
- Holdout sets must be constructed independently of the main design
- Use profiles that are representative of the full design space but not shown during estimation
- Never use the most extreme "dominant" profile (best on every attribute) — it will always be chosen and gives no validation information

**Holdout hit rate:**
$$\text{Hit rate} = \frac{\text{respondents who chose the predicted alternative}}{\text{total respondents}}$$

Benchmark: hit rate > 60% indicates the model has predictive validity. Chance level is 1/k (33% for 3-profile sets).

If hit rate < 60%, diagnose:
- Check if respondents understood the task (attention screeners)
- Check if model includes all important attributes
- Check if interaction effects are needed

---

## 7. Constraints: Handling Impossible Combinations

Some attribute level combinations are impossible or implausible:

- Budget brand + premium price: respondents know this is unrealistic; including it biases results
- High RAM + very low price: may signal a defect, not a value proposition

**Approach 1 — Hard exclusion:** Remove prohibited profiles from the candidate set before design generation. D-optimal works natively with this.

**Approach 2 — Prohibitions in Sawtooth:** Mark prohibited combinations; software avoids placing them in the same profile.

**Risk:** Over-constrained designs reduce D-efficiency because the feasible space shrinks. After applying constraints, recheck D-efficiency. If it drops below 70%, relax some constraints or accept wider confidence intervals.

**Warning from Iron Law:** Constraints implicitly restrict the range of tested levels. If you prohibit Apple+$1600 because "Apple is always premium," you cannot estimate Apple's price sensitivity at that price point. Your WTP estimate for the Apple brand will only be valid for the $800-$1200 range you actually tested.

---

## 8. Worked Design Generation (Python, No External Libraries)

This shows the L9 orthogonal array approach for 3 attributes × 3 levels each.

```python
"""
Generate L9 orthogonal array for 3x3x3 conjoint design.
Produces 9 profiles with orthogonal main effects.
"""

def generate_l9():
    """
    L9(3^4) orthogonal array — use first 3 columns for 3 attributes.
    Values are 0, 1, 2 representing the three levels of each attribute.
    """
    # Standard L9 array (Taguchi)
    l9 = [
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 2, 2, 2],
        [1, 0, 1, 2],
        [1, 1, 2, 0],
        [1, 2, 0, 1],
        [2, 0, 2, 1],
        [2, 1, 0, 2],
        [2, 2, 1, 0],
    ]
    return [row[:3] for row in l9]  # drop 4th column


def decode_profiles(design, attribute_levels):
    """
    attribute_levels: dict mapping attribute name to list of level labels
    e.g. {"Brand": ["Apple","Dell","Lenovo"], "RAM": ["8GB","16GB","32GB"], "Price": ["$800","$1200","$1600"]}
    """
    attrs = list(attribute_levels.keys())
    profiles = []
    for row in design:
        profile = {}
        for i, attr in enumerate(attrs):
            profile[attr] = attribute_levels[attr][row[i]]
        profiles.append(profile)
    return profiles


def check_orthogonality(design):
    """Check pairwise level co-occurrence for 3-column design."""
    n_attrs = len(design[0])
    for i in range(n_attrs):
        for j in range(i + 1, n_attrs):
            pairs = [(row[i], row[j]) for row in design]
            from collections import Counter
            counts = Counter(pairs)
            print(f"Attr {i} × Attr {j}: {dict(sorted(counts.items()))}")
            # For L9, each (level_i, level_j) pair appears exactly once


if __name__ == "__main__":
    attribute_levels = {
        "Brand": ["Apple", "Dell", "Lenovo"],
        "RAM":   ["8GB", "16GB", "32GB"],
        "Price": ["$800", "$1200", "$1600"],
    }

    design = generate_l9()
    profiles = decode_profiles(design, attribute_levels)

    print("=== 9 Profiles (L9 Design) ===")
    for i, p in enumerate(profiles, 1):
        print(f"Profile {i}: {p}")

    print("\n=== Orthogonality Check ===")
    check_orthogonality(design)
```

**Output:**
```
=== 9 Profiles (L9 Design) ===
Profile 1: {'Brand': 'Apple', 'RAM': '8GB', 'Price': '$800'}
Profile 2: {'Brand': 'Apple', 'RAM': '16GB', 'Price': '$1200'}
Profile 3: {'Brand': 'Apple', 'RAM': '32GB', 'Price': '$1600'}
Profile 4: {'Brand': 'Dell', 'RAM': '8GB', 'Price': '$1200'}
Profile 5: {'Brand': 'Dell', 'RAM': '16GB', 'Price': '$1600'}
Profile 6: {'Brand': 'Dell', 'RAM': '32GB', 'Price': '$800'}
Profile 7: {'Brand': 'Lenovo', 'RAM': '8GB', 'Price': '$1600'}
Profile 8: {'Brand': 'Lenovo', 'RAM': '16GB', 'Price': '$800'}
Profile 9: {'Brand': 'Lenovo', 'RAM': '32GB', 'Price': '$1200'}

=== Orthogonality Check ===
Attr 0 × Attr 1: {(0,0):1, (0,1):1, (0,2):1, (1,0):1, (1,1):1, (1,2):1, (2,0):1, (2,1):1, (2,2):1}
Attr 0 × Attr 2: {(0,0):1, (0,1):1, ...}
Attr 1 × Attr 2: {(0,0):1, ...}
```

Every pair of attribute levels co-occurs exactly once — perfect orthogonality.

---

## 9. Assembling Choice Sets from Profiles

After generating profiles, you need to group them into choice sets. For 9 profiles and 3 profiles per set, you get 3 choice sets. Each respondent sees all 3.

**Grouping options:**

1. **Sequential:** Profiles 1-3 → Set A, 4-6 → Set B, 7-9 → Set C. Simple, but within-set attribute correlation may be higher.

2. **Random assignment:** Shuffle profiles then assign to sets. Run `check_orthogonality` on the resulting within-set structure.

3. **For larger designs with 100+ profiles:** Use a blocked design — assign profiles to blocks ensuring balance across blocks. Each respondent receives one block.

**Rotation:** Randomize the order in which profiles appear within a choice set across respondents to eliminate position bias (respondents tend to choose the first option more often).

---

## 10. Common Design Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Using treatment coding instead of effects coding | Part-worth ranges are incomparable across attributes; importance scores wrong | Recode with −1 for reference level |
| Fewer than 10 choice sets with 5+ attributes | Insufficient data per respondent for stable HB draws | Increase to 12-15 sets or reduce attributes |
| Including a "none" option without modeling it | None-choosers' utilities are censored | Add explicit "none" utility term in MNL |
| Showing all-same-attribute choice set (e.g., all three profiles at $800) | That task provides zero price information | Check for constant columns within choice sets |
| Prohibiting too many combinations before D-optimal | Feasible space too small; D-efficiency collapses | Remove at most 10-15% of profiles as prohibited |
| Not randomizing choice set order across respondents | First-task anchoring biases estimates for all subsequent tasks | Randomize block order per respondent |
