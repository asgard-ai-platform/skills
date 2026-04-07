---
name: "algo-social-engagement"
description: "Calculate and benchmark social media engagement rates across platforms and variants. Use this skill when the user needs to compute engagement metrics, compare performance across accounts or posts, or set engagement benchmarks — even if they say 'what is my engagement rate', 'benchmark engagement', or 'social media KPIs'."
metadata:
  category: "WP-38 社群演算法"
  tags: ["social-media", "engagement-rate", "analytics", "benchmarking"]
---

# Engagement Rate Calculation

## Overview

Engagement rate measures audience interaction relative to reach or audience size. Formula: (reactions + comments + shares) / denominator × 100%. The denominator choice (reach, impressions, followers) significantly affects the result. Computes in O(n) per post set.

## When to Use

**Trigger conditions:**
- Computing engagement metrics for social media reporting
- Benchmarking account or post performance against industry averages
- Comparing content performance across posts or accounts

**When NOT to use:**
- When evaluating influence holistically (use influence measurement)
- When modeling content spread dynamics (use virality models)

## Algorithm

```
IRON LAW: Engagement Rate Denominator MATTERS
By reach, by impressions, and by followers produce DIFFERENT numbers:
- ER by Reach = engagements / reach × 100% (most accurate, requires analytics access)
- ER by Impressions = engagements / impressions × 100% (always lower than by reach)
- ER by Followers = engagements / followers × 100% (public data, but inflated by non-reaching followers)
ALWAYS specify which variant when reporting or comparing.
```

### Phase 1: Input Validation
Collect per post: likes, comments, shares/retweets, saves (platform-specific), reach or impressions or follower count.
**Gate:** Consistent denominator across all posts being compared.

### Phase 2: Core Algorithm
1. Sum engagements per post: likes + comments + shares (+ saves, clicks if available)
2. Weight engagements if desired: share=3×, comment=2×, like=1× (shares indicate higher commitment)
3. Divide by chosen denominator (reach preferred, followers as fallback)
4. Compute: per-post ER, average ER across posts, median ER, ER trend over time

### Phase 3: Verification
Compare against platform benchmarks. Flag anomalies (ER > 20% likely data error or viral outlier).
**Gate:** Results within plausible range for platform.

### Phase 4: Output
Return engagement metrics with benchmarking context.

## Output Format

```json
{
  "metrics": {"avg_er_by_reach": 3.2, "avg_er_by_followers": 1.8, "median_er": 2.9, "top_post_er": 8.5},
  "benchmark": {"platform": "instagram", "industry": "fashion", "benchmark_er": 2.5, "percentile": 72},
  "metadata": {"posts_analyzed": 30, "period": "2025-Q1", "denominator": "reach"}
}
```

## Examples

### Sample I/O
**Input:** Post: 150 likes, 20 comments, 5 shares, reach=5000
**Expected:** ER by reach = (150+20+5)/5000 × 100% = 3.5%

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Reach = 0 | Undefined, skip post | Can't divide by zero |
| Boosted/paid post | Separate from organic | Paid reach inflates denominator, deflates ER |
| Viral outlier (10x avg) | Flag, analyze separately | Skews averages |

## Gotchas

- **Platform algorithm changes**: Instagram's algorithm shifts regularly. Historical ER benchmarks become outdated. Use rolling 90-day benchmarks.
- **Vanity metric trap**: High ER doesn't mean business impact. 1000 likes on a meme ≠ 10 link clicks on a product post. Track meaningful engagements.
- **Story/Reel metrics differ**: Story engagement (taps, replies) and Reel engagement (plays, shares) need different formulas than feed posts. Don't mix.
- **Follower-based ER is noisy**: Not all followers see each post (reach < followers). ER by followers underestimates true engagement among those who saw the post.
- **Comparing across account sizes**: Smaller accounts naturally have higher ER by followers. Normalize or segment by account size for fair comparison.

## References

- For platform-specific benchmark data, see `references/platform-benchmarks.md`
- For weighted engagement scoring models, see `references/weighted-engagement.md`
