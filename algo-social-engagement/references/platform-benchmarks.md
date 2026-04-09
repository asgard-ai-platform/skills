# Platform Engagement Rate Benchmarks

Benchmarks below are expressed as **ER by Followers** (public denominator) unless otherwise noted, because that's what most third-party studies can measure at scale. When you have analytics access, expect ER by Reach to run 1.5–3× higher.

---

## Instagram

### Feed Posts (Photo / Carousel / Single Image)

| Account Size (followers) | Median ER by Followers | Good (75th %ile) | Strong (90th %ile) |
|--------------------------|------------------------|------------------|--------------------|
| < 1K (nano)              | 5.0%                   | 8.0%             | 12%+               |
| 1K–10K (micro)           | 3.5%                   | 6.0%             | 9%+                |
| 10K–100K (mid-tier)      | 2.2%                   | 3.8%             | 6%+                |
| 100K–1M (macro)          | 1.5%                   | 2.5%             | 4%+                |
| 1M+ (mega)               | 0.8%                   | 1.5%             | 2.5%+              |

**Industry modifiers** (multiply median by factor):

| Industry          | Multiplier |
|-------------------|------------|
| Food & Beverage   | 1.2        |
| Fashion           | 1.0        |
| Beauty            | 1.1        |
| Fitness           | 1.3        |
| B2B / Tech        | 0.6        |
| Finance           | 0.5        |
| News / Media      | 0.7        |

**Example:** Mid-tier fashion account (50K followers) → median benchmark = 2.2% × 1.0 = **2.2%**. Same-size fitness account → 2.2% × 1.3 = **2.86%**.

### Reels

Reels benchmarks use a play-adjusted formula:

```
Reel ER = (likes + comments + shares + saves) / followers × 100%
```

Plays are NOT included in the numerator (they are the denominator analog for Reel-specific metrics). Separate Reel plays from engagement entirely.

| Account Size   | Median Reel ER | Good   |
|----------------|----------------|--------|
| < 10K          | 4.5%           | 8%+    |
| 10K–100K       | 3.0%           | 5%+    |
| 100K–1M        | 1.8%           | 3%+    |
| 1M+            | 1.0%           | 2%+    |

Reels consistently outperform feed posts by ~1.3–1.5× at the same account size. If your Reels ER equals your feed ER, Reels are underperforming.

### Stories

Stories use a separate metric: **Story Completion Rate** and **Interaction Rate**.

```
Story Interaction Rate = (replies + sticker taps + link taps) / story views × 100%
```

This is NOT comparable to feed ER. Benchmarks:

| Story Type          | Typical Interaction Rate |
|---------------------|--------------------------|
| Informational slide | 1–3%                     |
| Poll sticker        | 8–15%                    |
| Quiz sticker        | 10–20%                   |
| Link sticker        | 2–5%                     |

**Do not mix Story Interaction Rate with feed ER in any aggregate calculation.**

---

## TikTok

TikTok ER is by views (the platform's primary distribution unit), not followers:

```
TikTok ER by Views = (likes + comments + shares) / video_views × 100%
```

| Views Range        | Median ER by Views | Good   |
|--------------------|-------------------|--------|
| < 10K views        | 6.0%              | 10%+   |
| 10K–100K views     | 4.5%              | 7%+    |
| 100K–1M views      | 3.0%              | 5%+    |
| 1M+ views          | 1.8%              | 3%+    |

**Critical:** TikTok's denominator is fundamentally different from Instagram's. Never compare TikTok ER by Views directly with Instagram ER by Followers. The two numbers measure different things.

If forced to compare across platforms, convert to a common basis:

```
Comparable ER = engagements / estimated_reach × 100%
```

Use TikTok's "Profile Views" or follower count as a rough reach proxy for cross-platform comparison, but flag the approximation.

---

## Facebook

Facebook organic reach has declined sharply since 2018. Benchmarks reflect this.

| Content Type        | Median ER by Followers | Notes                        |
|---------------------|------------------------|------------------------------|
| Link post           | 0.07%                  | Penalized by algorithm       |
| Photo post          | 0.12%                  |                              |
| Video post          | 0.15%                  |                              |
| Reel (Facebook)     | 0.25%                  | Getting algorithmic boost    |
| Native video (3s+)  | 0.18%                  |                              |

Facebook ER by Followers below 0.05% signals organic reach collapse — paid amplification is likely needed.

**ER by Reach** on Facebook (when analytics available) typically runs 2–5% for photo posts, 3–7% for video. The gap between ER by Followers and ER by Reach is wider on Facebook than any other platform, precisely because organic reach is so constrained (~2–5% of followers see an average post).

---

## LinkedIn

LinkedIn ER formula uses impressions (what LinkedIn reports natively):

```
LinkedIn ER by Impressions = (likes + comments + reposts + clicks) / impressions × 100%
```

Note LinkedIn includes **clicks** as an engagement. This inflates ER compared to platforms where clicks aren't counted. When comparing with Instagram/TikTok, strip clicks:

```
LinkedIn ER (comparable) = (likes + comments + reposts) / impressions × 100%
```

| Content Type        | Median ER by Impressions (w/ clicks) | Without Clicks |
|---------------------|--------------------------------------|----------------|
| Text post           | 3.5%                                 | 1.2%           |
| Photo post          | 4.2%                                 | 1.5%           |
| Document/carousel   | 5.0%                                 | 2.0%           |
| Native video        | 4.8%                                 | 1.8%           |
| Poll                | 6.0%                                 | 3.5%           |

LinkedIn ER is not segmented by account size in the same way — it's segmented by content type and poster type (personal profile vs. company page). Personal profiles consistently outperform company pages by 2–3×.

---

## Twitter / X

Twitter ER uses impressions as the denominator (native to the platform):

```
Twitter ER = (likes + retweets + replies + link_clicks) / impressions × 100%
```

| Account Type        | Median ER by Impressions |
|---------------------|--------------------------|
| Personal / Creator  | 0.5–1.5%                 |
| Brand               | 0.3–0.8%                 |
| News / Media        | 0.2–0.5%                 |

Twitter benchmarks are volatile post-2022 due to algorithm changes and API restrictions affecting measurement. Use with caution; prefer 90-day rolling averages over historical baselines.

---

## Benchmark Staleness and Update Cadence

Platform algorithms change. Published benchmark studies lag reality by 6–18 months. Apply this decay model:

```
Adjusted Benchmark = Published Benchmark × Recency Factor
```

| Study Age  | Recency Factor |
|------------|----------------|
| < 6 months | 1.0            |
| 6–12 months| 0.9            |
| 1–2 years  | 0.75           |
| 2–3 years  | 0.6            |
| > 3 years  | Discard        |

**Preferred approach:** build internal benchmarks from your own 90-day rolling data as soon as you have 20+ posts per account. Own-account benchmarks beat industry averages for identifying genuine performance shifts.

---

## Percentile Calculation (Worked Example)

You have 30 Instagram feed posts from a fashion account with 45K followers. Average ER by followers = 2.8%.

**Step 1 — Identify the reference row:**
Account size 10K–100K, industry = fashion (multiplier 1.0).
Benchmark median = 2.2%, 75th %ile = 3.8%.

**Step 2 — Locate your number:**
2.8% sits between 2.2% (50th) and 3.8% (75th).

**Step 3 — Linear interpolation for percentile:**
```
percentile = 50 + (2.8 - 2.2) / (3.8 - 2.2) × (75 - 50)
           = 50 + 0.6 / 1.6 × 25
           = 50 + 9.4
           ≈ 59th percentile
```

**Step 4 — Report:**
```json
{
  "benchmark": {
    "platform": "instagram",
    "content_type": "feed",
    "industry": "fashion",
    "account_tier": "mid-tier",
    "benchmark_median_er": 2.2,
    "your_avg_er": 2.8,
    "percentile": 59
  }
}
```

---

## Cross-Platform Comparison Decision Table

When asked to compare ER across platforms, use this routing:

| Platforms Being Compared      | Valid Comparison? | Required Adjustment                              |
|-------------------------------|-------------------|--------------------------------------------------|
| Instagram feed vs. Instagram feed | Yes           | Ensure same denominator (reach or followers)     |
| Instagram feed vs. Reels      | Cautious          | Note format difference; Reels naturally higher   |
| Instagram vs. Facebook        | Cautious          | Normalize to ER by Reach if both available       |
| Instagram vs. TikTok          | Not direct        | TikTok uses views; requires proxy conversion     |
| Instagram vs. LinkedIn        | Not direct        | LinkedIn counts clicks; strip for comparison     |
| Any vs. Stories               | No                | Stories use a different metric entirely          |

When a direct comparison isn't valid, report each platform's percentile rank within its own benchmark distribution instead of comparing raw ER numbers.

---

## Quick Reference Card

| Platform   | Primary ER Denominator | Typical Good ER (mid-tier brand) | Comparable to Others? |
|------------|------------------------|----------------------------------|-----------------------|
| Instagram  | Followers or Reach     | 2–4% (followers)                 | Baseline              |
| TikTok     | Views                  | 3–5% (views)                     | Not directly          |
| Facebook   | Followers              | 0.1–0.3% (followers)             | Yes, but much lower   |
| LinkedIn   | Impressions            | 1–2% (excl. clicks)              | Yes, with adjustment  |
| Twitter/X  | Impressions            | 0.5–1.5%                         | Caution (volatile)    |
