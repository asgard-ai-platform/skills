---
name: "algo-rec-mf"
description: "Implement matrix factorization to decompose user-item interaction matrices into latent factor representations. Use this skill when the user needs scalable collaborative filtering, latent feature discovery, or dimensionality reduction for recommendation — even if they say 'SVD recommendations', 'latent factors', or 'factorize the rating matrix'."
metadata:
  category: "WP-36 推薦系統"
  tags: ["recommendation", "matrix-factorization", "svd", "latent-factors"]
---

# Matrix Factorization

## Overview

Matrix factorization decomposes the user-item interaction matrix R (m×n) into two low-rank matrices: U (m×k) and V (n×k), where k << min(m,n). Predicted rating: r̂ᵢⱼ = uᵢ · vⱼ. Trains in O(k × nnz × iterations) where nnz = non-zero entries.

## When to Use

**Trigger conditions:**
- Scaling CF beyond pairwise similarity (millions of users/items)
- Discovering latent factors that explain user-item interactions
- Predicting ratings for unobserved user-item pairs

**When NOT to use:**
- When interaction data is extremely sparse (< 0.1% fill) — insufficient for learning
- When you need real-time updates (retraining is expensive)

## Algorithm

```
IRON LAW: Rank k Controls Bias-Variance Trade-Off
- Too LOW k: underfits, misses nuanced preferences (high bias)
- Too HIGH k: overfits to noise, poor generalization (high variance)
- Typical k: 20-200. Select via cross-validation on held-out ratings.
- Always add regularization (λ) to prevent overfitting.
```

### Phase 1: Input Validation
Load sparse interaction matrix. Split into train/validation/test. Check minimum density.
**Gate:** Train matrix has sufficient entries per user and item.

### Phase 2: Core Algorithm
**ALS (Alternating Least Squares):**
1. Initialize U, V randomly (or with SVD warm-start)
2. Fix V, solve for U: minimize ||R - UV^T||² + λ(||U||² + ||V||²)
3. Fix U, solve for V using same objective
4. Alternate until convergence (RMSE change < ε)

**SGD alternative:** Update u_i, v_j incrementally for each observed rating using gradient descent.

### Phase 3: Verification
Compute RMSE on held-out validation set. Compare against baseline (global mean, user mean).
**Gate:** Validation RMSE significantly below baseline.

### Phase 4: Output
Return top-N predictions per user with predicted scores.

## Output Format

```json
{
  "recommendations": [{"user_id": "u1", "items": [{"item_id": "i5", "predicted_rating": 4.3}]}],
  "metadata": {"rank_k": 50, "regularization": 0.01, "iterations": 20, "train_rmse": 0.82, "val_rmse": 0.91}
}
```

## Examples

### Sample I/O
**Input:** 3×3 rating matrix R (0 = unobserved), k=1
```
R = [[5, 3, 0],
     [4, 0, 2],
     [0, 1, 1]]
```
**Expected:** After ALS with k=1 (one latent factor, λ=0.01, 50 iterations), approximate factorization:
```
U ≈ [[2.24], [1.84], [0.53]]
V ≈ [[2.23], [1.06], [0.98]]
R_hat ≈ [[4.99, 2.37, 2.20],
         [4.10, 1.95, 1.80],
         [1.18, 0.56, 0.52]]
```
Verify: R_hat ≈ R on observed entries (within 0.2 RMSE). U[0] >> U[2] correctly captures user 0's higher ratings.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| User with 1 rating | Poor predictions for that user | Insufficient data to learn user factors |
| Highly popular item | Predicted near average | Dominant first latent factor captures popularity |
| All ratings = 5 | Trivial factorization | No variance to learn from |

## Gotchas

- **Implicit data needs different loss**: For clicks/views (no explicit ratings), use weighted matrix factorization (Hu et al. 2008) with confidence weighting, not RMSE.
- **Cold start remains**: New users/items have no entries in R. MF can't factorize what doesn't exist. Use side features or hybrid approaches.
- **Negative sampling**: For implicit feedback, you must sample negative examples (unobserved ≠ disliked). Random negative sampling works but biased sampling is better.
- **Initialization matters**: Random initialization can converge to poor local optima. SVD-based warm-start often helps.
- **Bias terms**: Add user bias bᵢ and item bias bⱼ: r̂ᵢⱼ = μ + bᵢ + bⱼ + uᵢ·vⱼ. This captures systematic rating tendencies.

## References

- For ALS vs SGD comparison, see `references/optimization-comparison.md`
- For implicit feedback matrix factorization, see `references/implicit-mf.md`
