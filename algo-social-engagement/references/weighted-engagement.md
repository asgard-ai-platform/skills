# Weighted Engagement Scoring Models

Weighted engagement treats different interaction types as non-equivalent.
A share costs the user more effort and signals stronger intent than a
like — weighting reflects that signal difference numerically.

---

## Core Formula

```
Weighted Engagements = (likes × w_like) + (comments × w_comment) + (shares × w_share) + (saves × w_save)

Weighted ER = Weighted Engagements / Denominator × 100%
```

The denominator follows the same IRON LAW as unweighted ER: reach,
impressions, or followers — pick one and hold it constant across all posts
being compared.

---

## Standard Weight Set (SKILL.md Default)

The parent SKILL.md specifies:

| Action | Weight | Rationale |
|--------|--------|-----------|
| Like / Reaction | 1× | Lowest friction, weakest signal |
| Comment | 2× | Requires thought and text input |
| Share / Retweet | 3× | Amplifies; user vouches for content |
| Save / Bookmark | — | Not in base formula; see below |

This is the **minimum viable weighted model** — use it when you have no
platform-specific calibration data.

---

## Extended Weight Set (with Saves and Clicks)

Saves indicate intent to return; clicks indicate intent to act. Both are
stronger purchase signals than likes.

| Action | Suggested Weight | Notes |
|--------|-----------------|-------|
| Like / Reaction | 1 | Baseline |
| Comment | 2 | |
| Share / Retweet | 3 | |
| Save / Bookmark | 3 | Same as share; indicates high-value content |
| Link Click | 4 | Exits platform; strongest intent signal |
| Video Play (≥50%) | 1 | Counts partial attention; cap at 1 |
| DM / Direct Reply | 5 | Highest-effort, private intent |

**Not every platform exposes all actions.** Use only what your analytics
API returns. Missing actions are treated as 0, not imputed.

---

## Worked Example

### Raw data (one Instagram feed post)

| Metric | Value |
|--------|-------|
| Likes | 420 |
| Comments | 38 |
| Shares (to Story) | 15 |
| Saves | 62 |
| Reach | 8 400 |

### Unweighted ER by reach

```
Engagements = 420 + 38 + 15 + 62 = 535
ER = 535 / 8 400 × 100% = 6.37%
```

### Weighted ER (extended set, with saves at 3×, no clicks available)

```
Weighted Engagements
  = (420 × 1) + (38 × 2) + (15 × 3) + (62 × 3)
  = 420 + 76 + 45 + 186
  = 727

Weighted ER = 727 / 8 400 × 100% = 8.65%
```

The gap between 6.37% and 8.65% exists because saves and shares are
disproportionately represented relative to their weight.

---

## When Weighted ER Diverges from Unweighted ER

| Pattern | Meaning |
|---------|---------|
| Weighted >> Unweighted | Post earned shares/saves; strong amplification/intent signal |
| Weighted ≈ Unweighted | Engagement is mostly likes; low-depth interaction |
| Weighted << Unweighted | Impossible with weights ≥ 1 unless you use fractional weights |

A post with 1 000 likes and 2 shares versus a post with 200 likes and 100
shares: unweighted ER favors the first; weighted ER likely favors the
second. Weighted ER is the better proxy for content that drives business
outcomes.

---

## Choosing Weights: Three Approaches

### Approach A — Heuristic (Default)

Use the SKILL.md defaults (1 / 2 / 3). Consistent, explainable, portable
across clients. Downside: not calibrated to actual business outcomes.

### Approach B — Conversion-Correlated

Regress post-level conversion rate against engagement action counts. Use
the regression coefficients (normalized to like = 1) as weights.

```
Require: N ≥ 60 posts with conversion data (UTM-tracked link clicks or purchases)

Model: conversions ~ β_like·likes + β_comment·comments + β_share·shares + ε

Normalize: w_like = 1, w_comment = β_comment / β_like, w_share = β_share / β_like
```

This approach is most accurate but requires conversion data tied to individual
posts — typically only available with UTM parameters and a full analytics
stack.

### Approach C — Platform-Native Relevance Score

Some platforms publish engagement-quality proxies (e.g., Facebook's
Relevance Score, TikTok's Completion Rate). Map these to weights:

```
Normalize platform score to 0–10 range.
Use as a multiplier on raw ER: Adjusted ER = Raw ER × (score / 5)
```

This is a fast approximation when cross-action weight calibration is
unavailable.

**Recommendation:** Use Approach A for reporting, Approach B for
optimization decisions if you have ≥ 60 posts with conversion data.

---

## Weighted ER Across a Post Set

When aggregating across N posts, use weighted average by reach (or chosen
denominator) — not simple mean of per-post weighted ER. Simple mean gives
equal weight to low-reach and high-reach posts.

```
Weighted Average ER = Σ(Weighted_Engagements_i) / Σ(Denominator_i) × 100%
```

### Example: three posts

| Post | W.Eng | Reach |
|------|-------|-------|
| A | 727 | 8 400 |
| B | 310 | 12 000 |
| C | 55 | 900 |

```
Correct:
  Σ W.Eng = 727 + 310 + 55 = 1 092
  Σ Reach = 8 400 + 12 000 + 900 = 21 300
  Avg Weighted ER = 1 092 / 21 300 × 100% = 5.13%

Wrong (simple mean):
  Per-post ER = 8.65%, 2.58%, 6.11%
  Mean = (8.65 + 2.58 + 6.11) / 3 = 5.78%  ← biased toward low-reach post C
```

---

## Fractional Weights for Passive Actions

Some analysts include passive signals (impressions, video views) at
fractional weights to capture content exposure quality.

| Action | Fractional Weight |
|--------|------------------|
| Impression (no action) | 0 |
| Video view < 3 s | 0.1 |
| Video view 3–30 s | 0.3 |
| Video view > 50% completion | 1.0 |
| Like | 1.0 |

Only use fractional weights if the platform provides view-duration
breakdowns. Without duration data, all video plays are ambiguous.

---

## Gotchas Specific to Weighting

**Weight inflation with viral outliers**: A post with 10 000 shares at
weight 3× creates weighted engagement = 30 000 from shares alone, which can
obscure the score's meaning for that post. Flag outliers before computing
averages.

**Comment spam caveat**: Comments include spam and low-effort emoji replies.
If comment quality is poor (common in giveaway campaigns), reduce w_comment
to 1.5 or strip spam comments before weighting.

**Cross-platform weight portability**: A LinkedIn share (professional
network, higher effort) signals more than a Twitter retweet (one click).
Weights calibrated for Instagram do not transfer to LinkedIn without
recalibration.

**Saves are often unavailable in export**: Instagram saves appear in the
native app but are frequently missing from third-party analytics exports
(Sprout, Hootsuite). Confirm data source before including saves in formula.
If saves are only partially available, drop them entirely rather than mixing
posts that include saves with posts that don't.

---

## Python Snippet (stdlib only)

```python
from dataclasses import dataclass, field
from typing import Optional

WEIGHTS_DEFAULT = {"likes": 1, "comments": 2, "shares": 3, "saves": 3, "clicks": 4}

@dataclass
class Post:
    reach: int
    likes: int = 0
    comments: int = 0
    shares: int = 0
    saves: int = 0
    clicks: int = 0

def weighted_er(post: Post, weights: dict = WEIGHTS_DEFAULT) -> Optional[float]:
    """Return weighted ER by reach. Returns None if reach == 0."""
    if post.reach == 0:
        return None
    w_eng = (
        post.likes    * weights.get("likes", 1) +
        post.comments * weights.get("comments", 2) +
        post.shares   * weights.get("shares", 3) +
        post.saves    * weights.get("saves", 3) +
        post.clicks   * weights.get("clicks", 4)
    )
    return w_eng / post.reach * 100

def portfolio_weighted_er(posts: list[Post], weights: dict = WEIGHTS_DEFAULT) -> Optional[float]:
    """Weighted average ER across post set (reach-weighted, not mean of means)."""
    total_w_eng = 0
    total_reach = 0
    for p in posts:
        if p.reach == 0:
            continue
        w_eng = (
            p.likes    * weights.get("likes", 1) +
            p.comments * weights.get("comments", 2) +
            p.shares   * weights.get("shares", 3) +
            p.saves    * weights.get("saves", 3) +
            p.clicks   * weights.get("clicks", 4)
        )
        total_w_eng += w_eng
        total_reach += p.reach
    if total_reach == 0:
        return None
    return total_w_eng / total_reach * 100


# --- verify ---
if __name__ == "__main__":
    p = Post(reach=8400, likes=420, comments=38, shares=15, saves=62)
    result = weighted_er(p)
    assert abs(result - 8.654761904761905) < 0.001, f"Expected ~8.65, got {result}"

    posts = [
        Post(reach=8400,  likes=420, comments=38, shares=15, saves=62),
        Post(reach=12000, likes=180, comments=22, shares=8,  saves=10),
        Post(reach=900,   likes=40,  comments=5,  shares=2,  saves=0),
    ]
    portfolio = portfolio_weighted_er(posts)
    assert portfolio is not None
    print(f"Single post weighted ER: {result:.2f}%")
    print(f"Portfolio weighted ER:   {portfolio:.2f}%")
```

---

## Decision Table: Which Weight Model to Use

| Situation | Use |
|-----------|-----|
| Client reporting, no conversion data | Approach A (1/2/3) |
| eCommerce brand with UTM-tracked posts, N ≥ 60 | Approach B (regression) |
| Platform provides relevance score | Approach C (platform-native) |
| Video-heavy content (Reels, TikTok) | Extended set with completion-rate weights |
| Giveaway campaign with comment spam | Reduce w_comment to 1 or exclude |
| Cross-platform comparison report | Approach A, same weights on all platforms; note non-portability in report |
