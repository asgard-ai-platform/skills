---
name: "algo-social-influence"
description: "Measure social media influence using engagement-weighted metrics beyond follower count. Use this skill when the user needs to evaluate influencer effectiveness, compare influence across accounts, or build an influence scoring system — even if they say 'who is more influential', 'influencer ranking', or 'measure social impact'."
metadata:
  category: "WP-38 社群演算法"
  tags: ["social-media", "influence", "influencer-marketing", "metrics"]
---

# Social Influence Measurement

## Overview

Influence scoring evaluates an account's ability to drive actions (engagement, sharing, conversions) beyond mere reach. Combines reach, resonance (engagement depth), and relevance (topical authority). Computes as weighted composite score.

## When to Use

**Trigger conditions:**
- Evaluating and comparing influencers for marketing campaigns
- Building an influence scoring or ranking system
- Assessing brand ambassador effectiveness

**When NOT to use:**
- When measuring content virality dynamics (use viral spread models)
- When computing basic engagement rates (use engagement rate calculator)

## Algorithm

```
IRON LAW: Follower Count ≠ Influence
Influence requires ENGAGEMENT. An account with 1M followers and
0.01% engagement rate has less influence than one with 10K followers
and 5% engagement. Measure: reach × engagement rate × relevance.
```

### Phase 1: Input Validation
Collect per account: follower count, avg likes/comments/shares per post, posting frequency, audience demographics, topic categories.
**Gate:** Minimum 20 recent posts for stable metrics.

### Phase 2: Core Algorithm
1. **Reach score**: Normalize follower count to log scale (diminishing returns)
2. **Engagement score**: (avg engagements / followers) × 100, weighted by type (share > comment > like)
3. **Relevance score**: Topic overlap between influencer content and target campaign
4. **Composite**: Influence = w₁×Reach + w₂×Engagement + w₃×Relevance (weights tuned per campaign goal)
5. Adjust for: audience authenticity (bot follower %), post frequency consistency

### Phase 3: Verification
Spot-check: do high-scoring accounts actually drive actions? Cross-reference with historical campaign performance data if available.
**Gate:** Top-ranked accounts have demonstrable engagement history.

### Phase 4: Output
Return ranked influence scores with component breakdown.

## Output Format

```json
{
  "rankings": [{"account": "@handle", "influence_score": 82, "reach": 75, "engagement": 90, "relevance": 85}],
  "metadata": {"accounts_analyzed": 50, "weights": {"reach": 0.2, "engagement": 0.5, "relevance": 0.3}}
}
```

## Examples

### Sample I/O
**Input:** Account A: 500K followers, 0.5% engagement. Account B: 50K followers, 4.2% engagement. Same relevance.
**Expected:** B scores higher due to engagement dominance in weighting.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Viral one-hit account | High recent engagement, low stability | Need temporal consistency check |
| Celebrity with low engagement | High reach, low influence per dollar | Reach-only strategy, expensive |
| Micro-influencer niche | High relevance + engagement | Best ROI for targeted campaigns |

## Gotchas

- **Fake engagement**: Bot likes/comments inflate metrics. Use authenticity tools (HypeAuditor, etc.) to detect.
- **Platform differences**: 2% engagement on Instagram is average; 2% on Twitter/X is excellent. Normalize by platform benchmarks.
- **Engagement pods**: Groups of influencers artificially engaging with each other's content. Check if engagement comes from diverse sources.
- **Influence ≠ conversion**: High engagement doesn't guarantee purchase intent. Track downstream metrics (link clicks, promo code usage) for campaign ROI.
- **Temporal decay**: Influence changes. Quarterly reassessment is minimum; monthly is better for fast-moving categories.

## References

- For audience authenticity detection methods, see `references/authenticity-detection.md`
- For influencer ROI measurement framework, see `references/influencer-roi.md`
