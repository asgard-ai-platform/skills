---
name: "algo-rec-cf"
description: "Implement collaborative filtering for recommendations based on user behavior patterns. Use this skill when the user needs to build a recommendation engine from user-item interaction data, find similar users or items, or predict ratings — even if they say 'users who bought this also bought', 'similar users', or 'recommend based on behavior'."
metadata:
  category: "WP-36 推薦系統"
  tags: ["recommendation", "collaborative-filtering", "similarity"]
---

# Collaborative Filtering

## Overview

Collaborative filtering recommends items based on collective user behavior patterns. User-based CF finds similar users; item-based CF finds similar items. Computes in O(U² × I) for user-based or O(I² × U) for item-based where U=users, I=items.

## When to Use

**Trigger conditions:**
- Building recommendations from user-item interaction data (ratings, clicks, purchases)
- Finding "users like you also liked" or "frequently bought together" patterns

**When NOT to use:**
- When you have no interaction data (cold start — use content-based filtering)
- When item features matter more than behavior patterns (use content-based)

## Algorithm

```
IRON LAW: CF Requires SUFFICIENT Interaction Data
With sparse matrices (< 1% fill rate), similarity computation is
unreliable. Minimum viable: each user has rated 5+ items, each item
has 5+ ratings. Below this, fallback to content-based or popularity.
```

### Phase 1: Input Validation
Load user-item interaction matrix. Check sparsity level and filter users/items below minimum interaction threshold.
**Gate:** Matrix sparsity < 99%, minimum interaction thresholds met.

### Phase 2: Core Algorithm
**User-based CF:**
1. Compute pairwise user similarity (cosine or Pearson correlation)
2. For target user, find top-K most similar users
3. Predict rating: weighted average of similar users' ratings

**Item-based CF:**
1. Compute pairwise item similarity from co-rating patterns
2. For target item, find top-K most similar items
3. Predict: weighted average of user's ratings on similar items

### Phase 3: Verification
Hold out 20% of interactions for testing. Compute RMSE, MAE, or precision@K / recall@K.
**Gate:** RMSE below baseline (global mean predictor).

### Phase 4: Output
Return top-N recommendations with predicted scores.

## Output Format

```json
{
  "recommendations": [{"item_id": "123", "predicted_score": 4.2, "similar_items_used": 5}],
  "metadata": {"method": "item-based", "similarity": "cosine", "k_neighbors": 20, "sparsity": 0.97}
}
```

## Examples

### Sample I/O
**Input:** 5 users × 5 items rating matrix, target: user1, item5
**Expected:** Predicted rating based on weighted similarity of user1's rated items similar to item5

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| New user, no ratings | Cannot recommend | Cold start — fallback to popularity |
| Item rated by all users | Low differentiation | High popularity ≠ personalized match |
| Single shared item | Unreliable similarity | Need multiple co-ratings for stable similarity |

## Gotchas

- **Scalability**: User-based CF with millions of users is O(U²). Use approximate nearest neighbors (LSH) or switch to item-based CF (item catalog is usually smaller).
- **Popularity bias**: Popular items have more co-ratings, inflating their similarity scores. Normalize by inverse popularity.
- **Implicit vs explicit feedback**: Clicks/views (implicit) need different treatment than ratings (explicit). Use confidence weighting for implicit data.
- **Similarity metric matters**: Cosine similarity ignores rating scale differences; Pearson correlation accounts for user rating biases. Choose based on data characteristics.
- **Gray sheep**: Users with unusual taste patterns have no similar peers. CF fails for them — consider hybrid approaches.

## References

- For matrix factorization as a scalable alternative, see `references/matrix-factorization.md`
- For implicit feedback handling, see `references/implicit-feedback.md`
