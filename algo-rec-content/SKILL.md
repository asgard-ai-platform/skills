---
name: "algo-rec-content"
description: "Implement content-based recommendation by matching item features to user preference profiles. Use this skill when the user needs to recommend items based on attributes, solve the cold start problem for new items, or build recommendations without collaborative data — even if they say 'recommend similar products', 'items like this', or 'feature-based matching'."
metadata:
  category: "WP-36 推薦系統"
  tags: ["recommendation", "content-based", "feature-matching"]
---

# Content-Based Recommendation

## Overview

Content-based filtering recommends items whose features match the user's preference profile, built from their interaction history. Computes in O(I × F) per user where I=items, F=features. Solves new-item cold start since items only need features, not interaction history.

## When to Use

**Trigger conditions:**
- Recommending based on item attributes (genre, category, keywords, price range)
- New item cold start: items have features but no interaction data yet
- When user privacy requires no cross-user data sharing

**When NOT to use:**
- When serendipity matters (content-based creates filter bubbles)
- When item features are unavailable or uninformative (use CF instead)

## Algorithm

```
IRON LAW: Content-Based Can Only Recommend SIMILAR Items
It cannot discover unexpected interests (filter bubble problem).
Users who only interact with action movies will only get action
movie recommendations — even if they'd love a documentary.
```

### Phase 1: Input Validation
Extract item feature vectors (TF-IDF for text, one-hot for categories, numerical for attributes). Build user profile from weighted item features of interacted items.
**Gate:** Item features extracted, user profile vector built.

### Phase 2: Core Algorithm
1. Represent each item as a feature vector
2. Build user profile: weighted centroid of interacted item vectors (weight by recency, rating, or engagement)
3. Compute similarity between user profile and all candidate items (cosine similarity)
4. Rank by similarity score, exclude already-interacted items

### Phase 3: Verification
Evaluate: does the recommendation list reflect the user's demonstrated preferences? Check diversity metrics.
**Gate:** Recommendations are topically aligned with user history.

### Phase 4: Output
Return ranked recommendations with feature-level explanations.

## Output Format

```json
{
  "recommendations": [{"item_id": "456", "score": 0.87, "matching_features": ["genre:thriller", "director:Nolan"]}],
  "metadata": {"method": "content-based", "features_used": 15, "profile_items": 30}
}
```

## Examples

### Sample I/O
**Input:** User watched 5 sci-fi movies, 2 documentaries. Candidate: new sci-fi movie.
**Expected:** High score (~0.8+) due to genre match with dominant preference.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| New user, no history | Cannot build profile | New-user cold start — use popularity |
| All items same features | Equal scores | No differentiation possible |
| User with diverse history | Moderate scores for all | Profile averages dilute signal |

## Gotchas

- **Feature quality is everything**: Garbage features → garbage recommendations. Invest in feature engineering.
- **Filter bubble**: Users get increasingly narrow recommendations. Inject diversity by mixing in exploration items.
- **Profile drift**: User preferences change over time. Apply temporal decay to older interactions.
- **Feature sparsity**: Items with few features produce unreliable similarity. Set a minimum feature count threshold.
- **Over-specialization**: A user who rated one jazz album highly shouldn't get ALL jazz. Weight by interaction count, not just rating.

## References

- For hybrid approaches combining content and CF, see `references/hybrid-strategies.md`
- For text-based feature extraction techniques, see `references/feature-extraction.md`
