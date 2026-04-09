# Implicit Feedback in Collaborative Filtering

Explicit feedback (star ratings, thumbs up/down) directly signals preference. Implicit feedback — clicks, page views, purchases, play counts, dwell time — signals *interest* indirectly. The critical difference: **silence is ambiguous**. A user who hasn't watched a movie might hate it, not know it exists, or simply not have time. This ambiguity breaks standard CF.

---

## The Core Problem: Missing ≠ Disliked

In an explicit matrix, a missing rating means "unrated" and is excluded from similarity computation. In an implicit matrix, zeros dominate — a typical e-commerce matrix is 99.9% zero. Treating all zeros as "no interest" destroys signal; ignoring zeros makes optimization ill-defined.

The standard resolution: **convert implicit counts to binary preference + a confidence weight**.

---

## Hu-Koren-Volinsky Model (2008)

This is the foundational formulation. Define:

| Symbol | Meaning |
|--------|---------|
| `r_ui` | Raw implicit signal (click count, play count, etc.) for user `u`, item `i` |
| `p_ui` | Binary preference: 1 if `r_ui > 0`, else 0 |
| `c_ui` | Confidence in the preference signal |

**Preference:**
```
p_ui = 1  if r_ui > 0
p_ui = 0  if r_ui = 0
```

**Confidence (linear):**
```
c_ui = 1 + α × r_ui
```

The constant `1` means even zero-interaction pairs have minimum confidence `1` — they count, but weakly. Alpha `α` (typically 1–40) controls how fast confidence grows with interaction count.

**Confidence (log-scaled):**
```
c_ui = 1 + α × log(1 + r_ui / ε)
```

Use log-scaling when your raw counts span several orders of magnitude (e.g., play counts from 1 to 10,000). `ε` is typically 1.0.

---

## Worked Example: Music Play Counts

Suppose you have play counts for 3 users × 4 songs:

```
         Song A  Song B  Song C  Song D
User 1:    50       0       3       0
User 2:     0      12       0       7
User 3:     1       0       0      20
```

**Step 1: Compute preferences (p_ui)**
```
         Song A  Song B  Song C  Song D
User 1:    1       0       1       0
User 2:    0       1       0       1
User 3:    1       0       0       1
```

**Step 2: Compute confidence (c_ui) with α = 40, log-scaling, ε = 1**

Formula: `c_ui = 1 + 40 × log(1 + r_ui)`

```
         Song A   Song B   Song C   Song D
User 1:  158.7    1.0      6.5      1.0
User 2:    1.0   101.0     1.0     84.3
User 3:    1.7    1.0      1.0    136.7
```

User 1 played Song A 50 times → confidence 158.7 (strong signal).  
User 1 never played Song D → confidence 1.0 (weak signal, not zero).

**Step 3: What this means for the optimizer**

The model is trained to predict `p_ui`, weighted by `c_ui`. High-confidence zeros (items the user skipped many times despite exposure) can be added by explicitly marking them — see "Negative Sampling" below.

---

## Optimization: Weighted ALS for Implicit Feedback

Standard matrix factorization minimizes:
```
L = Σ_{observed} (r_ui - u · i)²  +  regularization
```

Implicit ALS minimizes over ALL pairs (observed and unobserved):
```
L = Σ_{u,i} c_ui × (p_ui - u_vec · i_vec)²  +  λ(||u_vec||² + ||i_vec||²)
```

**Why ALS works here:** The update equations have closed-form solutions when you alternate between fixing user vectors and item vectors.

**User vector update (item vectors fixed):**
```
u_vec_u = (I^T C^u I + λI)^{-1} I^T C^u p_u
```
Where:
- `I` = item factor matrix (items × factors)
- `C^u` = diagonal matrix of confidence weights for user `u`
- `p_u` = preference vector for user `u`

The trick: `I^T C^u I = I^T I + I^T (C^u - I) I`. The first term `I^T I` is constant across all users and computed once. Only the second term varies per user and is sparse (only non-zero entries in `C^u - I` matter).

**Time complexity per iteration:** O(k² × |non-zero| + k³ × U)  
where k = latent factors, U = users. This is tractable.

---

## Choosing α

Alpha controls the signal-to-noise ratio of your confidence weights.

| α too low | Confidence differences collapse — play-once ≈ play-100-times |
|-----------|--------------------------------------------------------------|
| α too high | A single interaction dominates; zeros have no effective weight |

**Tuning procedure:**
1. Hold out 20% of non-zero interactions (set them to zero in training)
2. Evaluate precision@K on held-out items: did they appear in top-K recommendations?
3. Grid search over α ∈ {1, 5, 10, 20, 40}; pick highest precision@K
4. Typical starting point: α = 40 for play counts, α = 1 for binary click data

For binary click data (clicked / not clicked), the raw count is already 0 or 1, so linear confidence degenerates to `c_ui ∈ {1, 1+α}`. Log-scaling adds nothing — use linear.

---

## Negative Sampling (Alternative to Full-Matrix Training)

Training on all U × I pairs is expensive when U and I are large. Negative sampling approximates the full-matrix loss by explicitly sampling zeros.

**Procedure:**
1. For each user `u`, collect their positive items (non-zero interactions)
2. Sample `k` negative items uniformly from uninteracted items (k = 3–10× positives)
3. Assign sampled negatives confidence `c_ui = 1`; positives get their computed confidence
4. Train only on positives + sampled negatives

**Caution:** Uniform negative sampling underweights popular items as negatives (they appear too rarely in samples despite being genuine "not interested" signals). **Popularity-biased negative sampling** corrects this:

```
P(sample item i as negative) ∝ frequency(i)^β,  β ∈ [0.5, 0.75]
```

This oversamples popular items as negatives, preventing the model from over-recommending them.

---

## Exposure-Corrected Confidence

Not all zeros are equal. A user who was shown an item (e.g., it appeared in search results) and didn't click it is stronger evidence of disinterest than a user who was never exposed. If you have exposure logs:

```
c_ui = 1                                if r_ui = 0, item never shown
c_ui = 1 + α_neg                        if r_ui = 0, item was shown (explicit skip)
c_ui = 1 + α × log(1 + r_ui / ε)       if r_ui > 0
```

where `α_neg > 1` (e.g., 5) makes explicit skips meaningfully negative. This requires an impression log — without it, fall back to uniform zero confidence.

---

## Similarity-Based CF with Implicit Feedback

If you're using neighborhood-based CF (not matrix factorization), implicit data requires adjusting the similarity metric.

**Problem:** Cosine similarity on raw counts is dominated by users with high activity. A user who clicked 500 items overwhelms a user who clicked 5, even if their preferences align.

**Fix 1: Binarize before similarity**
```
r_ui_binary = 1 if r_ui > 0 else 0
```
Then compute cosine similarity on binary vectors. Simple, effective for sparse data.

**Fix 2: TF-IDF weighting**
Downweight items that appear in many users' histories (high document frequency):
```
weight_ui = log(1 + r_ui) × log(U / df_i)
```
where `df_i` = number of users who interacted with item `i`. This suppresses popularity bias in similarity computation.

**Fix 3: BM25 weighting** (stronger than TF-IDF for implicit data)
```
weight_ui = r_ui × (k+1) / (r_ui + k × (1 - b + b × |H_u| / avg_H))
```
where `|H_u|` = total interactions of user `u`, `avg_H` = average across all users, `k ∈ [1.2, 2.0]`, `b ∈ [0.5, 0.8]`. BM25 normalizes for user activity level, preventing prolific users from dominating similarity.

---

## Decision Table: Which Approach to Use

| Condition | Approach |
|-----------|----------|
| Dataset < 1M interactions, need interpretability | Neighborhood CF + BM25 weighting |
| Dataset > 1M interactions, need accuracy | Implicit ALS (matrix factorization) |
| Binary signals only (clicked / not clicked) | ALS with linear confidence, α = 1–10 |
| Count signals (play counts, purchase quantity) | ALS with log confidence, α = 20–40 |
| Exposure logs available | Add explicit skip confidence (`α_neg`) |
| Exposure logs unavailable | Uniform zero confidence (c=1 for all zeros) |
| U × I too large to train full matrix | Popularity-biased negative sampling |

---

## What "Confidence = 1 for zeros" Actually Means

A common confusion: if zeros have `c_ui = 1`, doesn't that mean the model is equally confident the user dislikes all uninteracted items?

No. It means: **the model is equally (minimally) uncertain** about all uninteracted items. The loss function penalizes predicting a high score for an uninteracted item, but only weakly. High-confidence positive interactions dominate. In practice, the model learns to predict low scores for uninteracted items without being "sure" — which is exactly right.

If you set `c_ui = 0` for zeros (i.e., ignore them), the model has no incentive to rank interacted items above uninteracted ones. Recommendations degrade to noise.

---

## Gotchas Specific to Implicit Data

- **Don't treat play-count-1 as strong signal.** A single interaction may be accidental. Log-scaling helps; alternatively, set a minimum threshold (`r_ui ≥ 2` to count as positive).
- **Recency matters implicitly.** A play from 3 years ago is weaker signal than a play last week. Consider time-decay: `r_ui_effective = r_ui × exp(-λ × days_since)` before computing confidence.
- **Session boundary artifacts.** A user who replayed a song 10 times in one session might have left it on loop. Cap raw counts at session level before aggregating.
- **Purchase ≠ preference.** A gift purchase or accidental double-order pollutes implicit signal. If you have return data, subtract returned items from the interaction matrix.
- **The sparsity IRON LAW still applies.** With < 5 interactions per user, confidence weighting cannot rescue poor coverage. Implicit data is typically denser than explicit ratings (clicks are cheap) — but verify before assuming.
