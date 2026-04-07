---
name: "algo-rec-session"
description: "Implement session-based recommendation from short-term user behavior sequences without long-term profiles. Use this skill when the user needs to recommend in anonymous sessions, predict next click from browsing sequence, or build recommendations for non-logged-in users — even if they say 'what should they click next', 'anonymous user recommendations', or 'browsing sequence prediction'."
metadata:
  category: "WP-36 推薦系統"
  tags: ["recommendation", "session-based", "sequential", "real-time"]
---

# Session-Based Recommendation

## Overview

Session-based recommendation predicts the next item a user will interact with based on their current session's click/view sequence, without relying on long-term user profiles. Uses Markov chains, association rules, or neural approaches (GRU4Rec). Operates in real-time with O(sequence_length) inference.

## When to Use

**Trigger conditions:**
- Anonymous users (no login, no long-term profile)
- Short browsing sessions where recency matters most
- Real-time "next item" prediction during active sessions

**When NOT to use:**
- When rich user history is available (use CF or content-based for better personalization)
- When sessions are extremely short (1-2 clicks) — insufficient signal

## Algorithm

```
IRON LAW: First Few Clicks Are Disproportionately Important
Session-based methods operate WITHOUT long-term profiles. Intent must
be inferred from SHORT sequences. The first 2-3 clicks establish the
session's intent — misreading early signals derails the entire session.
```

### Phase 1: Input Validation
Parse clickstream into sessions (by session ID or timeout-based splitting, typically 30min inactivity). Filter sessions below minimum length (3+ events).
**Gate:** Sessions parsed, minimum length threshold applied.

### Phase 2: Core Algorithm
**Markov Chain approach:**
1. Build transition matrix from item-to-item sequences across all sessions
2. For current session [A, B, C], predict next item from P(next | C) or higher-order P(next | B, C)

**Association Rules approach:**
1. Mine frequent item sequences (sequential pattern mining)
2. Match current session suffix against known patterns
3. Recommend items that frequently follow the matched pattern

### Phase 3: Verification
Evaluate with leave-one-out: hide last item in each session, predict, check hit rate and MRR (Mean Reciprocal Rank).
**Gate:** Hit@20 significantly above random baseline.

### Phase 4: Output
Return ranked next-item predictions with confidence scores.

## Output Format

```json
{
  "predictions": [{"item_id": "789", "score": 0.65, "based_on": "last_3_clicks"}],
  "session": {"length": 5, "items_viewed": ["a", "b", "c", "d", "e"]},
  "metadata": {"method": "markov_order2", "hit_rate_at_20": 0.35}
}
```

## Examples

### Sample I/O
**Input:** Session: [shoes_page, running_shoes, nike_air_max]
**Expected:** Recommend: nike_air_zoom (0.72), adidas_ultraboost (0.58), shoe_size_guide (0.41)

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Session length = 1 | Popularity fallback | Single click insufficient for sequence pattern |
| Repeated item views | Weight recency, not count | User may be comparing, not broadening |
| Session intent shift | Adapt to latest clicks | User changed their goal mid-session |

## Gotchas

- **Session definition matters**: 30-minute timeout is conventional but arbitrary. E-commerce may need shorter (15min); research browsing may need longer (60min).
- **Position bias**: Users click top results more. Session data reflects UI position, not just preference. Correct for position bias.
- **Repeat recommendations**: Users often revisit items. Distinguish "recommend something new" from "remind of previously viewed."
- **Cold start for new items**: Items with zero prior session appearances can't be predicted by transition matrices. Mix in feature-based candidates.
- **Computational efficiency**: For real-time inference, pre-compute transition probabilities. Recomputing per-request at scale is too slow.

## References

- For GRU4Rec neural session model, see `references/gru4rec.md`
- For session splitting heuristics, see `references/session-splitting.md`
