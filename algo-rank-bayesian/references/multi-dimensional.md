# Multi-Dimensional Bayesian Rating

Extends the single-score Bayesian average to items rated on multiple criteria simultaneously. Instead of one `BR` per item, each item receives a `BR_d` per dimension `d`, then an aggregation step produces a final rank score.

---

## When Single-Dimension BR Falls Short

A restaurant rated on "overall experience" collapses real signal. Reviewers weight food, service, and ambiance differently; the aggregate hides dimensional strength. Multi-dimensional BR solves this when:

- Items are rated on k ≥ 2 named criteria (food/service/price, plot/acting/visuals, ease/value/support)
- Stakeholders want to filter or re-weight by dimension ("show me high-value, low-service places I can tolerate")
- Dimensional review counts differ (users often skip optional sub-ratings)

**Do not use** if all dimensions always have the same reviewer filling all fields — you gain nothing over a weighted single score computed by the user before submission.

---

## Notation

| Symbol | Meaning |
|--------|---------|
| `d` | Dimension index, `d ∈ {1 … k}` |
| `n_i` | Total review count for item `i` |
| `n_id` | Reviews that include a rating for dimension `d` on item `i` |
| `avg_id` | Raw average rating for item `i`, dimension `d` |
| `m_d` | Global mean for dimension `d` across all items |
| `C_d` | Confidence (phantom vote) parameter for dimension `d` |
| `BR_id` | Bayesian average for item `i`, dimension `d` |
| `w_d` | Weight assigned to dimension `d` in final aggregation |
| `Score_i` | Final aggregated rank score for item `i` |

---

## Formula

### Step 1: Per-dimension Bayesian average

For each item `i` and dimension `d`:

```
BR_id = (C_d × m_d + n_id × avg_id) / (C_d + n_id)
```

This is the same formula as the parent skill, applied independently per dimension using dimension-specific globals `m_d` and `C_d`.

### Step 2: Aggregation

```
Score_i = Σ_d (w_d × BR_id)   where Σ_d w_d = 1
```

Rank items by `Score_i` descending.

---

## Choosing C_d Per Dimension

Each dimension may have different participation rates. If "ambiance" is an optional field, far fewer reviewers fill it in — you need a higher `C_d` to penalize that sparsity.

**Rule of thumb:** set `C_d` = median of `{n_id : item i has at least 1 rating on dimension d}`.

If dimension `d` has very low participation (< 20% of reviewers fill it), consider treating it as optional and excluding it from `Score_i` for items where `n_id = 0`, substituting `m_d` as the fallback:

```
BR_id = m_d        if n_id = 0
BR_id = (C_d × m_d + n_id × avg_id) / (C_d + n_id)   otherwise
```

This is equivalent to the standard formula at `n_id = 0` — it's just explicit about the fallback behavior.

---

## Worked Example: Restaurant Ranking

**Setup:**
- 3 dimensions: Food (d=1), Service (d=2), Value (d=3)
- Rating scale: 1–10
- Weights: Food 50%, Service 30%, Value 20%
- Global means: m_1=7.2, m_2=6.8, m_3=6.5
- Confidence parameters: C_1=80, C_2=60, C_3=50

**Two restaurants:**

| | Restaurant A | Restaurant B |
|--|--|--|
| Reviews (n) | 12 | 350 |
| Food avg | 9.4, n_1=12 | 7.6, n_1=350 |
| Service avg | 9.0, n_2=10 | 6.9, n_2=300 |
| Value avg | 8.5, n_3=8 | 6.4, n_3=280 |

**Step 1: BR_id for Restaurant A**

```
BR_A1 = (80×7.2 + 12×9.4) / (80+12) = (576 + 112.8) / 92 = 688.8 / 92 = 7.49
BR_A2 = (60×6.8 + 10×9.0) / (60+10) = (408 + 90) / 70   = 498 / 70   = 7.11
BR_A3 = (50×6.5 + 8×8.5)  / (50+8)  = (325 + 68) / 58   = 393 / 58   = 6.78
```

**Step 1: BR_id for Restaurant B**

```
BR_B1 = (80×7.2 + 350×7.6) / (80+350) = (576 + 2660) / 430 = 3236 / 430 = 7.53
BR_B2 = (60×6.8 + 300×6.9) / (60+300) = (408 + 2070) / 360 = 2478 / 360 = 6.88
BR_B3 = (50×6.5 + 280×6.4) / (50+280) = (325 + 1792) / 330 = 2117 / 330 = 6.42
```

**Step 2: Weighted aggregation**

```
Score_A = 0.5×7.49 + 0.3×7.11 + 0.2×6.78
        = 3.745 + 2.133 + 1.356 = 7.23

Score_B = 0.5×7.53 + 0.3×6.88 + 0.2×6.42
        = 3.765 + 2.064 + 1.284 = 7.11
```

Restaurant A ranks higher despite 12 reviews vs 350. The prior dampened A's raw 9.4 → 7.49, but B's established 7.6 also shrinks less dramatically. With these weights, A's stronger dimensional profile wins — but if you raised C_1 to 200, A's food score would collapse to ~7.47 and B would overtake it.

**Key takeaway:** The crossover point (where more reviews trump higher raw scores) is controlled by C_d. This is a deliberate product choice, not a math artifact.

---

## Weight Selection Strategies

### Strategy 1: Uniform weights
`w_d = 1/k` for all d. Default when you have no domain signal.

### Strategy 2: Stated preference
Survey users: "Which matters most?" Map percentage responses directly to weights. Rebalance quarterly.

### Strategy 3: Engagement-based
Use click-through or conversion data. If users who sort by "Value" convert 2× more, upweight Value. Requires A/B infrastructure.

### Strategy 4: Dimension correlation adjustment
If two dimensions are highly correlated (food quality and presentation, r > 0.85), one is redundant. Down-weight the correlated pair to avoid double-counting:

```
w_adjusted_d = w_d / (1 + Σ_{d'≠d} ρ_{dd'} × w_d')
```

Re-normalize so weights sum to 1. This is optional; only matters when k ≥ 4 with known correlations.

---

## Handling Missing Dimensions

Not all reviewers rate all dimensions. Three approaches:

| Approach | When to use | Risk |
|----------|------------|------|
| Substitute `m_d` (prior only) | Dimension is optional, low participation | Flattens scores for items with sparse optional ratings |
| Exclude from aggregation, renormalize weights | Dimension is rarely filled for an entire item category | Weight totals differ across items, harder to compare |
| Require minimum `n_id` threshold before including dimension | Enough reviewers that absence is a signal | Items below threshold look artificially average |

**Recommendation:** Substitute `m_d` for `n_id = 0`. It's equivalent to the standard formula and keeps all items on the same weight scale.

---

## Category-Level Priors

The parent skill notes that "4.0 in horror might be exceptional, while 4.0 in Studio Ghibli might be below average." This effect is stronger in multi-dimensional settings because dimensions interact with category.

**Category-specific global mean:**

```
m_d^(cat) = Σ_{i ∈ cat} (n_id × avg_id) / Σ_{i ∈ cat} n_id
```

Use `m_d^(cat)` instead of `m_d` when:
- Items fall into distinct categories with known rating-culture differences
- You want rankings to be relative within category, not absolute across all items

Using category priors makes cross-category comparison invalid — a restaurant's Score_i in "ramen" is no longer comparable to its Score_i in "fine dining."

---

## Iron Law Reinforcement

The parent skill's Iron Law holds per dimension: **without a prior, a single 5-star review on any dimension makes that item "best" on that dimension.**

Multi-dimensional BR amplifies this risk because an item can game a single optional dimension with one review. A spammy item that gets one 10/10 "value" review (n_3=1) gets:

```
BR_i3 = (50×6.5 + 1×10) / (50+1) = (325+10)/51 = 6.57
```

Only 0.07 above the global mean — the prior absorbs the manipulation. At C_3=50, you need roughly 50 reviews to move the needle significantly. This is the mechanism that makes Bayesian averaging manipulation-resistant at small n.

---

## Output Format Extension

Extend the parent skill's output format to include per-dimension breakdown:

```json
{
  "rankings": [
    {
      "item": "Restaurant_A",
      "score": 7.23,
      "dimensions": {
        "food":    {"bayesian_avg": 7.49, "raw_avg": 9.4, "reviews": 12, "weight": 0.5},
        "service": {"bayesian_avg": 7.11, "raw_avg": 9.0, "reviews": 10, "weight": 0.3},
        "value":   {"bayesian_avg": 6.78, "raw_avg": 8.5, "reviews": 8,  "weight": 0.2}
      }
    }
  ],
  "metadata": {
    "globals": {
      "food":    {"mean": 7.2, "C": 80},
      "service": {"mean": 6.8, "C": 60},
      "value":   {"mean": 6.5, "C": 50}
    },
    "weights": {"food": 0.5, "service": 0.3, "value": 0.2},
    "items_ranked": 1200
  }
}
```

Include `raw_avg` alongside `bayesian_avg` per dimension so downstream consumers can show users how much shrinkage occurred.

---

## Gotchas Specific to Multi-Dimensional Setting

**Dimension proliferation**: Adding more dimensions doesn't add more signal if reviewers don't fill them. Past k=5 dimensions, participation per dimension typically drops sharply. Audit fill rates before adding a dimension.

**Weight instability across user segments**: A single global weight vector may not represent any user. Consider letting users set weights interactively and storing `BR_id` values as the canonical data, computing `Score_i` at query time.

**Dimensional mean drift**: If you update `m_d` periodically (e.g., monthly), stored `BR_id` values become stale. Either recompute on the fly or store raw `(n_id, sum_id)` tuples and compute `BR_id` = `(C_d × m_d + sum_id) / (C_d + n_id)` at ranking time with the current `m_d`.

**Scale inconsistency across dimensions**: If Food is 1–10 and Service is 1–5, do not use a single `C` for both. The variance per dimension differs, so `C_d` should be calibrated per dimension independently.
