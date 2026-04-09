# Bayesian Average

Wilson Score works for binary outcomes (positive/negative). When ratings are **continuous** (1–5 stars, 1–10 score), the correct correction for sample size is **Bayesian Average** — a prior-smoothed mean that pulls sparse items toward a global baseline.

---

## The Problem Wilson Score Cannot Solve

Wilson Score requires a proportion: positive count / total count. A 4.2-star rating with 3 reviews has no natural "positive" count. You could binarize (4+ = positive), but you lose resolution — a 4.1-star item and a 4.9-star item become identical.

Bayesian Average keeps the full continuous scale and instead handles the cold-start problem via a **prior**: assume every item starts with *m* phantom reviews at the global average *C*.

---

## Formula

```
bayesian_avg = (C × m + Σ_ratings) / (m + n)
```

| Symbol | Meaning |
|--------|---------|
| `C`    | Global average rating across all items |
| `m`    | Prior weight (number of phantom reviews) |
| `n`    | Actual review count for this item |
| `Σ_ratings` | Sum of actual ratings for this item |

Equivalently:

```
bayesian_avg = (m / (m + n)) × C + (n / (m + n)) × item_avg
```

This is a **weighted blend**: when `n` is small, the result is pulled toward `C`; when `n` is large, it converges to the item's true average.

---

## Worked Example

**Scenario**: An e-commerce site with 3 products.

| Product | Ratings | Sum | Raw Avg |
|---------|---------|-----|---------|
| Alpha   | 2       | 9.0 (4.5 + 4.5) | 4.50 |
| Beta    | 80      | 340.0 | 4.25 |
| Gamma   | 5       | 17.5 | 3.50 |

**Step 1 — Global average C**

Total ratings: 2 + 80 + 5 = 87  
Total sum: 9.0 + 340.0 + 17.5 = 366.5  
`C = 366.5 / 87 ≈ 4.213`

**Step 2 — Choose prior weight m**

A common rule of thumb: `m = average review count per item` = 87 / 3 = 29.  
(See [Choosing m](#choosing-m) below.)

**Step 3 — Compute Bayesian averages**

```
Alpha:  (4.213 × 29 + 9.0)  / (29 + 2)  = (122.18 + 9.0)  / 31  ≈ 4.232
Beta:   (4.213 × 29 + 340.0) / (29 + 80) = (122.18 + 340.0) / 109 ≈ 4.241
Gamma:  (4.213 × 29 + 17.5) / (29 + 5)  = (122.18 + 17.5)  / 34  ≈ 4.109
```

**Final ranking**: Beta (4.241) > Alpha (4.232) > Gamma (4.109)

Compare to raw average ranking: Alpha (4.50) > Beta (4.25) > Gamma (3.50).  
Alpha dropped from 1st to 2nd because its 4.5 average rests on only 2 reviews.

---

## Choosing m

`m` is the single most consequential parameter. It controls how aggressively sparse items are penalized.

### Rule of thumb: set m = average review count

```python
m = total_reviews / item_count
```

This is the IMDB formula. It means an item needs roughly `m` reviews before its score is taken at "face value" (50% weight on its own average vs. the prior).

### Effect of different m values on Alpha (2 reviews, avg 4.50)

| m  | Bayesian Avg | Interpretation |
|----|-------------|----------------|
| 5  | 4.394       | Mild penalty, still near raw avg |
| 29 | 4.232       | Moderate penalty (recommended) |
| 100| 4.224       | Heavy penalty, collapses toward C |
| 500| 4.219       | Near-total collapse to global avg |

**Insight**: once `m >> n`, the Bayesian average saturates — increasing m beyond ~10× the typical review count adds no meaningful differentiation. Choose m in the range of your median-to-mean review count.

### When to use a larger m

- High-stakes ranking (e.g., medical device ratings) → larger m, more skepticism
- Discovery surface (e.g., "new arrivals" list) → smaller m, more trust in sparse signal
- User-generated content with spam risk → larger m acts as a noise filter

---

## Python Implementation

```python
def bayesian_average(ratings_sum: float, n: int, C: float, m: float) -> float:
    """
    Compute Bayesian average for a single item.

    Args:
        ratings_sum: Sum of all ratings for the item
        n: Number of ratings for the item
        C: Global average (prior mean)
        m: Prior weight (phantom review count)

    Returns:
        Bayesian average score
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return (C * m + ratings_sum) / (m + n)


def rank_items(items: list[dict], m: float | None = None) -> list[dict]:
    """
    Rank items by Bayesian average.

    Args:
        items: list of {"id": str, "sum": float, "n": int}
        m: prior weight; if None, uses mean review count

    Returns:
        Sorted list with "bayesian_avg" added, descending
    """
    total_n = sum(item["n"] for item in items)
    total_sum = sum(item["sum"] for item in items)
    item_count = len(items)

    if item_count == 0:
        return []

    C = total_sum / total_n if total_n > 0 else 0.0
    if m is None:
        m = total_n / item_count

    result = []
    for item in items:
        score = bayesian_average(item["sum"], item["n"], C, m)
        result.append({**item, "bayesian_avg": round(score, 6), "C": C, "m": m})

    return sorted(result, key=lambda x: x["bayesian_avg"], reverse=True)
```

**Usage:**

```python
items = [
    {"id": "Alpha", "sum": 9.0,   "n": 2},
    {"id": "Beta",  "sum": 340.0, "n": 80},
    {"id": "Gamma", "sum": 17.5,  "n": 5},
]
ranked = rank_items(items)
# [Beta: 4.241, Alpha: 4.232, Gamma: 4.109]
```

---

## Wilson Score vs. Bayesian Average: Decision Table

| Condition | Use Wilson Score | Use Bayesian Average |
|-----------|-----------------|---------------------|
| Rating type | Binary (upvote/downvote, like/dislike) | Continuous (stars, scores) |
| Output range | 0–1 probability | Same scale as input ratings |
| Binarization required? | Yes (for star ratings) | No |
| Cold-start handling | Confidence interval shrinks to near-zero | Pulled toward global mean |
| Interpretability | "Lower bound on true approval rate" | "Prior-smoothed expected rating" |
| Tuning parameters | Confidence level z (rarely changed) | Prior weight m (must tune) |
| Computational cost | O(1), no global state needed | O(1) per item, requires global C and m |

**Bottom line**: if your ratings are already binary, use Wilson Score (no parameter to tune, statistically principled). If your ratings are continuous and you need a "best rated" list, Bayesian Average is the standard approach.

---

## Gotchas

**Global C depends on current item set.** Adding or removing items changes C, which changes every score. For stable rankings in production, freeze C periodically (e.g., daily recalculation) rather than recomputing per request.

**Items with 0 reviews.** When `n = 0`, Bayesian average = C exactly. These items are rankable but cluster at the global mean — they are indistinguishable from each other. Apply a separate "not yet reviewed" tier or sort them below items with at least 1 review.

**m computed from a skewed distribution.** If a few items have 10,000 reviews and most have 10, the mean is dominated by the outliers, making m too large and crushing the sparse items unfairly. In that case, use `median` review count for m instead.

**Rating inflation over time.** If early reviews skew negative (tough early adopters) and later reviews skew positive, the global mean C drifts upward. Older items may appear penalized compared to newer ones. Time-decay weighting is a separate concern; Bayesian Average alone does not handle it.

**Not a confidence interval.** Bayesian Average gives a point estimate (the posterior mean), not a range. It does not tell you how uncertain the estimate is. For uncertainty quantification, you need a full Bayesian model with a Beta-Binomial (for binary) or Normal-Normal (for continuous) conjugate prior.

---

## IMDB Formula Equivalence

IMDB's published formula for their Top 250:

```
weighted_rating = (v / (v + m)) × R + (m / (v + m)) × C
```

where `v` = vote count, `R` = item average, `m` = minimum votes threshold, `C` = mean across all items.

This is algebraically identical to the Bayesian Average formula above:

```
(C × m + R × v) / (m + v)  ≡  (v / (v+m)) × R + (m / (v+m)) × C
```

The IMDB formula sets `m` to the minimum vote threshold required to appear on the list (~25,000 for Top 250), not the mean. This is a policy choice, not a statistical one — it pre-filters low-count items before Bayesian smoothing.
