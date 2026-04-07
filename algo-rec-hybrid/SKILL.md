---
name: "algo-rec-hybrid"
description: "Design hybrid recommendation systems combining multiple strategies for improved accuracy. Use this skill when the user needs to overcome single-method limitations, combine collaborative and content-based filtering, or build a production recommendation pipeline — even if they say 'combine recommendation approaches', 'best recommendation architecture', or 'cold start plus personalization'."
metadata:
  category: "WP-36 推薦系統"
  tags: ["recommendation", "hybrid", "ensemble", "system-design"]
---

# Hybrid Recommendation System

## Overview

Hybrid recommendation combines multiple strategies (CF, content-based, knowledge-based) to overcome individual method limitations. Common architectures: weighted, switching, cascade, feature augmentation, and meta-level. Complexity varies by architecture.

## When to Use

**Trigger conditions:**
- Building a production recommendation system that must handle cold start AND personalization
- Single methods have known weaknesses for your use case
- Need to balance accuracy, diversity, and coverage

**When NOT to use:**
- When you have a single clean data source (start with the matching single method first)
- When system simplicity is more important than marginal accuracy gains

## Algorithm

```
IRON LAW: Hybrid Adds Value ONLY With Complementary Strengths
Combining two systems with the SAME weakness amplifies the weakness.
CF fails on cold start + content-based fails on cold start = hybrid
STILL fails on cold start. Choose components that cover each other's gaps.
```

### Phase 1: Input Validation
Identify available data: interaction history (for CF), item features (for content-based), contextual signals (time, device, location). Map data to method capabilities.
**Gate:** At least two complementary data sources available.

### Phase 2: Core Algorithm
**Weighted hybrid:** Score = α × CF_score + β × CB_score. Tune weights via cross-validation.

**Switching hybrid:** Use CF when sufficient data exists; switch to content-based for cold start items/users.

**Cascade hybrid:** First stage filters (e.g., content-based), second stage ranks (e.g., CF) within filtered set.

**Feature augmentation:** Use one method's output as input features for another (e.g., CF embeddings as content features).

### Phase 3: Verification
A/B test hybrid vs individual components. Measure: accuracy (NDCG, precision@K), coverage (% of catalog recommended), diversity (intra-list diversity).
**Gate:** Hybrid outperforms best individual component on primary metric.

### Phase 4: Output
Return recommendations with source attribution for explainability.

## Output Format

```json
{
  "recommendations": [{"item_id": "789", "score": 0.91, "sources": {"cf": 0.85, "content": 0.95}, "method": "weighted"}],
  "metadata": {"architecture": "weighted", "weights": {"cf": 0.6, "content": 0.4}, "coverage": 0.78}
}
```

## Examples

### Sample I/O
**Input:** New user with 2 interactions + rich item feature catalog
**Expected:** Switching hybrid: content-based recommendations (insufficient CF data), transitioning to CF as interactions accumulate

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Completely new user + new item | Fall back to popularity | No data for either method |
| Methods disagree strongly | Depends on architecture | Weighted averages; cascade defers to second stage |
| One component returns empty | Other component takes over | Graceful degradation |

## Gotchas

- **Complexity cost**: Each added component increases latency, maintenance, and debugging difficulty. Start simple, add complexity only when justified by metrics.
- **Weight tuning**: Static weights degrade over time. Retune periodically or use learned weights (e.g., a meta-model that predicts which component performs best per context).
- **Evaluation is harder**: You must evaluate the hybrid AND each component individually to understand contribution and detect regressions.
- **Feature leakage**: In feature augmentation, ensure the augmenting model's predictions don't leak test-set information during training.
- **Diminishing returns**: Going from one method to two gives the biggest lift. Adding a third rarely justifies the complexity.

## References

- For architecture selection decision guide, see `references/architecture-selection.md`
- For A/B testing recommendation systems, see `references/ab-testing-recs.md`
