# Hybrid Recommendation Strategies

Hybrid systems combine content-based filtering (CB) with collaborative filtering (CF) to offset each method's blind spots. This reference covers the four architectures used in practice, with formulas, a decision table, and a worked numeric example.

---

## Why Hybrid

| Problem | CB alone | CF alone | Hybrid |
|---------|----------|----------|--------|
| New item cold start | Handles it | Fails | Handles it |
| New user cold start | Fails | Fails | Partially handles it |
| Filter bubble | Severe | Moderate | Mitigated |
| Popularity bias | None | Strong | Configurable |
| Feature-poor items | Fails | Handles it | Handles it |

CB is strong exactly where CF is weak (new items, privacy). CF is strong exactly where CB is weak (serendipity, complex taste). Hybrids exploit this complementarity.

---

## Architecture 1 — Weighted Score Fusion

**What it is:** Run CB and CF independently; blend their raw scores with a tunable weight α.

### Formula

```
hybrid_score(u, i) = α · score_cb(u, i) + (1 - α) · score_cf(u, i)
```

Where:
- `score_cb(u, i)` = cosine similarity between user profile vector and item feature vector (range 0–1)
- `score_cf(u, i)` = predicted rating or interaction probability from CF model (normalize to 0–1 before blending)
- `α ∈ [0, 1]` = blend weight (CB dominance as α → 1)

### Score Normalization (required before blending)

CF raw scores (e.g., matrix factorization dot products) are on an arbitrary scale. Normalize with min-max per recommendation batch:

```
score_cf_norm(u, i) = (raw_cf(u, i) - min_cf) / (max_cf - min_cf)
```

Do the same for CB if your cosine similarities are asymmetric due to non-unit vectors.

### Worked Example

User u has watched 8 sci-fi movies and 1 romance movie.

Candidate items:

| Item | score_cb | score_cf_norm | hybrid (α=0.6) |
|------|----------|---------------|----------------|
| Interstellar | 0.91 | 0.55 | 0.55 + 0.22 = **0.77** |
| The Notebook | 0.12 | 0.80 | 0.07 + 0.32 = **0.39** |
| Arrival | 0.85 | 0.72 | 0.51 + 0.29 = **0.80** |
| Dunkirk | 0.63 | 0.68 | 0.38 + 0.27 = **0.65** |

At α=0.6 the user's demonstrated sci-fi preference dominates, but CF still rescues "Arrival" (which CB also scores well independently).

### When to Tune α

- **New user** (< 5 interactions): CB is unreliable. Shift α toward 0.2 to rely on CF's popularity signal.
- **New item** (0 CF ratings): CF produces nothing. Force α = 1.0 (pure CB).
- **Established user, established item**: α = 0.5–0.7 is empirically safe.

Treat α as a hyperparameter tuned on offline holdout or A/B test, not a constant.

---

## Architecture 2 — Switching Hybrid

**What it is:** Route each (user, item) pair to CB or CF based on a condition. Simpler than blending; easier to reason about.

### Decision Tree

```
Is item new (< min_interactions threshold)?
  YES → Use CB score
  NO  → Is user new (< min_history threshold)?
          YES → Use CF popularity fallback
          NO  → Use CF score
```

Typical thresholds: `min_interactions = 10` ratings for an item, `min_history = 5` interactions for a user.

### Implementation Sketch

```python
MIN_ITEM_INTERACTIONS = 10
MIN_USER_HISTORY = 5

def score(user, item, cb_model, cf_model):
    if item.interaction_count < MIN_ITEM_INTERACTIONS:
        return cb_model.score(user, item)
    if user.history_count < MIN_USER_HISTORY:
        return cf_model.popularity_score(item)   # global popularity
    return cf_model.score(user, item)
```

### Trade-off vs Weighted Fusion

| | Weighted Fusion | Switching |
|--|----------------|-----------|
| Transparency | Low (scores blend) | High (one model wins) |
| Debugging | Harder | Easier |
| Edge handling | Implicit via α | Explicit branches |
| Performance | Requires both models | Runs only one model |
| Best for | Balanced catalogs | Catalogs with many new items |

---

## Architecture 3 — Feature Augmentation (CF-Enriched CB)

**What it is:** Use CF to generate pseudo-features for items, then feed them into the CB model. Single unified ranking model; no blending needed.

### Procedure

1. Train a matrix factorization CF model to get item latent vectors `q_i ∈ ℝ^k`.
2. Concatenate CF latent vector with CB feature vector:
   ```
   item_vec_hybrid(i) = [feature_cb(i) | q_i]
   ```
3. Build user profile from this augmented representation.
4. Score candidates with cosine similarity on the augmented vectors.

This lets the CB model inherit CF's collaborative signal (items that similar users co-engaged) without hard-coding a separate CF scoring path.

### Gotcha: Dimensionality Mismatch

CB feature vectors for text-heavy items can be high-dimensional (e.g., TF-IDF at d=5000). CF latent vectors are typically k=50–200. Concatenating directly makes CF signal tiny relative to CB signal. Fix:

```
item_vec_hybrid(i) = [β · normalize(feature_cb(i)) | (1-β) · normalize(q_i)]
```

Use β = 0.7 as a starting point; tune on validation set.

### When to Use Feature Augmentation

- You already have a production CB pipeline and want to inject CF signal incrementally.
- You need a single model for explainability (one similarity score, not two).
- You have good CF coverage (most items have latent vectors) — otherwise augmentation is sparse.

---

## Architecture 4 — Cascade Hybrid

**What it is:** Use CF as a rough ranker (fast, high-recall) then use CB as a re-ranker (slower, high-precision) on the shortlist.

```
Stage 1 (CF):   full catalog → top-K candidates  (K = 100–500)
Stage 2 (CB):   top-K candidates → top-N final   (N = 10–20)
```

### Why This Order

CF-based ANN retrieval (via FAISS, ScaNN, etc.) is O(log I) and scales to millions of items. CB cosine re-ranking over 500 candidates is O(500 × F), which is cheap. Reversing the order would require CB scoring over the full catalog — expensive for large F.

### Stage 2 Re-ranking Formula

At re-ranking, you can blend CB score with CF rank as a feature:

```
rerank_score(u, i) = score_cb(u, i) + λ · (1 / rank_cf(u, i))
```

The `1 / rank_cf` term rewards items CF placed near the top; λ controls how much you trust CF's coarse ordering. Start with λ = 0.1.

### Cascade vs Weighted Fusion

Use cascade when:
- Catalog size > 100k items (CB over full catalog is too slow)
- CB model is expensive (e.g., fine-tuned embeddings, not dot products)
- You want interpretable final scores (CB score is the primary signal)

---

## Choosing an Architecture

```
Start here:
│
├─ Do you need to score the full catalog in real time?
│    YES → Cascade (CF retrieval + CB re-rank)
│    NO  → continue
│
├─ Are > 30% of your catalog items new (< 10 interactions)?
│    YES → Switching hybrid (explicit cold-start routing)
│    NO  → continue
│
├─ Do you need a single interpretable score?
│    YES → Feature augmentation or weighted fusion
│    NO  → continue
│
└─ Default: Weighted fusion with α tuned on offline eval
```

---

## Cold Start Edge Cases in Hybrids

### New User + New Item (double cold start)

None of CB, CF, or simple hybrids solve this. Fallback sequence:

1. Use item metadata to find the most popular items in the same category.
2. Surface them with a diversity constraint (no more than 2 per subcategory).
3. Collect 3–5 explicit signals (e.g., onboarding preference survey) before attempting personalization.

### New User + Established Items (CF cold start only)

Switching: route to CB using default user profile (e.g., category-level priors from demographics or entry page).
Weighted fusion: set α high (0.8+) but build CB profile from browse history (clicks, time-on-page) not just ratings.

---

## Offline Evaluation

Hybrids must be evaluated on held-out interactions, not just individual model scores.

**Primary metric:** NDCG@10 (normalized discounted cumulative gain at cutoff 10)

```
NDCG@K = DCG@K / IDCG@K

DCG@K = Σ_{i=1}^{K} (2^rel_i - 1) / log2(i + 1)
```

Where `rel_i` is the relevance of the item at rank i (1 if interacted, 0 otherwise in binary feedback).

**Diversity metric:** Intra-List Diversity (ILD)

```
ILD = (2 / (N(N-1))) · Σ_{i≠j} (1 - sim(i, j))
```

Higher ILD = less filter bubble. Target ILD > 0.4 for content-heavy catalogs.

**Baseline to beat:** Always compare hybrid against CB-alone and CF-alone at the same K. A hybrid that doesn't beat both baselines in at least one metric is not worth the added complexity.

---

## Implementation Notes

- **Score normalization is mandatory** before any fusion. Un-normalized CF scores (e.g., raw dot products ranging −3 to +5) blended with CB cosine scores (0–1) will always be dominated by CF.
- **Don't retrain jointly**: CB and CF models are independently trained. Hybrid logic lives at inference, not training, for most architectures. Feature augmentation is the exception.
- **Monitor α over time**: User and catalog composition shift. Re-tune α quarterly or when catalog new-item ratio changes significantly.
- **Separate pipelines for serving**: CB and CF have different latency profiles. CF ANN retrieval is typically < 10ms; CB cosine over a large feature set can be 50–200ms. Design serving so they can scale independently.
