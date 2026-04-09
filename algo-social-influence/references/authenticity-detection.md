# Authenticity Detection for Influence Scoring

Fake engagement directly corrupts the composite influence score. A 10K-follower account with 8% engagement sounds excellent — until you discover 4,000 followers are bots and half the likes came from an engagement pod. This file covers how to detect and quantify inauthenticity so you can apply a correction factor before scoring.

---

## The Authenticity Adjustment Factor

The parent skill's composite formula is:

```
Influence = w₁×Reach + w₂×Engagement + w₃×Relevance
```

Before plugging in numbers, apply an authenticity correction to both Reach and Engagement:

```
Reach_adj       = followers × (1 - bot_follower_rate)
Engagement_adj  = raw_engagement_rate × (1 - pod_engagement_rate)
```

Then compute:

```
Influence = w₁×Reach_score(Reach_adj) + w₂×Engagement_score(Engagement_adj) + w₃×Relevance
```

A `bot_follower_rate` of 0.35 (35% fake followers) cuts an account with 500K followers down to 325K effective reach before log-normalization. The difference is often enough to flip rankings.

---

## Signal 1: Follower Quality Audit

### Follower-to-Engagement Ratio Anomaly

Authentic accounts exhibit platform-typical engagement rates. Use these benchmarks (2024–2025 data):

| Platform   | Typical ER range | Red-flag threshold |
|------------|------------------|--------------------|
| Instagram  | 1% – 5%          | < 0.3% or > 15%    |
| TikTok     | 5% – 12%         | < 1% or > 25%      |
| Twitter/X  | 0.5% – 2%        | < 0.05% or > 8%    |
| YouTube    | 1% – 4%          | < 0.2% or > 20%    |

> **Platform-normalization is mandatory.** A 2% ER on Instagram is average; the same 2% on Twitter/X is already above average. Scoring both identically misranks influencers.

An ER far below platform floor strongly suggests purchased followers. An ER far above ceiling suggests either extreme virality (verify via single viral post) or manufactured engagement.

### Ghost Follower Detection (Manual Sampling)

When you don't have access to a dedicated tool:

1. Sample 200 random followers from the account's follower list.
2. For each sampled account, check:
   - Profile photo exists (not default avatar)
   - Has posted in last 90 days
   - Following/follower ratio < 10 (not a follow-farm)
   - Bio is not empty
3. Count how many pass **all 4** checks. Call that `authentic_count`.
4. `bot_follower_rate_estimate = 1 - (authentic_count / 200)`

**Worked example:**

```
Sample size: 200 followers
- Profile photo: 160 have one
- Posted last 90 days: 140 qualify
- Follow ratio < 10: 150 qualify
- Non-empty bio: 155 qualify
- Pass ALL 4: 120 accounts

bot_follower_rate_estimate = 1 - (120/200) = 0.40 (40% suspicious)
```

A 40% rate is a hard disqualifier for campaigns requiring genuine reach.

---

## Signal 2: Engagement Quality Audit

### Comment Authenticity Scoring

Bot-driven or pod-driven comments have detectable patterns. Build a simple classifier:

| Comment type | Score |
|---|---|
| Specific reference to post content | +2 |
| Full sentence in post's primary language | +1 |
| Generic praise ("great post!", "love this!") | -1 |
| Single emoji only | -2 |
| Identical text appearing 2+ times | -3 |
| Posted within 0–5 minutes of publishing | -1 |

Sample 30 comments per post, score each, sum and normalize to 0–100:

```
comment_authenticity = max(0, min(100, (raw_sum / max_possible) × 100))
```

**Worked example:**

```
30 comments sampled:
- 8 content-specific (+2 each)     = +16
- 12 full-sentence (+1 each)       = +12
- 6 generic praise (-1 each)       = -6
- 4 emoji-only (-2 each)           = -8
- 0 duplicates                     = 0
- 5 posted within 5 min (-1 each)  = -5

raw_sum = +9
max_possible (all content-specific) = 30 × 2 = 60

comment_authenticity = max(0, min(100, (9/60) × 100)) = 15
```

A score of 15/100 is very low. This account's comment section shows strong inauthentic signals even though the engagement count looks fine.

### Like Velocity Analysis

Organic engagement follows a predictable time-decay curve: spike in the first 1–2 hours, tail off over 24–48 hours, then near-zero. Bot-purchased likes show different patterns:

```
Suspicious patterns:
- Flat drip rate (e.g., +50 likes every 30 minutes for 12 hours)
- Second spike 6–24 hours after posting with no story/repost trigger
- Like count jumps of >1000 within any 5-minute window outside first hour
```

You can approximate this by checking like counts at 1h, 6h, 24h, and 72h post-publish. Calculate the 6h→24h growth ratio and compare to the 1h→6h growth ratio:

```
velocity_ratio = (likes_at_24h - likes_at_6h) / (likes_at_6h - likes_at_1h)
```

Authentic accounts: `velocity_ratio` is typically 0.1 – 0.6 (engagement decays).  
Suspicious accounts: `velocity_ratio` > 1.0 (engagement accelerates after initial window, suggesting a second purchase batch).

---

## Signal 3: Engagement Pod Detection

Engagement pods are mutual-boosting groups (usually 10–50 accounts) that agree to like and comment on each other's content immediately after posting. The engagement is real behavior from real humans — but not organic audience behavior.

### Cross-Commenter Network Check

For 10 recent posts on a suspect account, collect the list of commenters per post. Then:

1. Build a commenter frequency table: how many posts did each commenter appear in?
2. Flag commenters appearing in ≥ 7 of 10 posts who do **not** appear to be close personal connections (check their own content for relationship signals).
3. Compute **pod_commenter_rate**: flagged recurring commenters ÷ total unique commenters.

```
pod_commenter_rate = flagged_recurring / total_unique_commenters
```

**Worked example:**

```
10 posts, 85 unique commenters total.
Commenters appearing in ≥ 7 posts:
  @user_A (8/10), @user_B (9/10), @user_C (7/10), @user_D (10/10)
After checking: @user_D is a verified sibling account (dismiss).
Flagged pod members: 3

pod_commenter_rate = 3 / 85 = 0.035 (3.5%)
```

A rate above 10% warrants investigation. Above 20% strongly suggests pod participation.

### Apply to Engagement Correction

```
pod_engagement_rate = pod_commenter_rate × (avg_comments / avg_total_engagements)
```

This scales by how much of total engagement is comments (pods mostly operate on comments, not likes).

---

## Combined Authenticity Score

Combine the three signals into a single authenticity multiplier:

```python
def authenticity_multiplier(
    bot_follower_rate: float,       # 0.0 – 1.0
    comment_authenticity: float,    # 0 – 100
    pod_engagement_rate: float,     # 0.0 – 1.0
    velocity_suspicious: bool,
) -> float:
    """
    Returns a multiplier between 0.0 and 1.0.
    Apply to both Reach_adj and Engagement_adj before scoring.
    """
    # Start with follower quality
    follower_quality = 1.0 - bot_follower_rate

    # Normalize comment authenticity to 0–1
    comment_quality = comment_authenticity / 100.0

    # Pod penalty reduces effective engagement
    engagement_quality = 1.0 - pod_engagement_rate

    # Velocity penalty: 15% reduction if suspicious
    velocity_penalty = 0.85 if velocity_suspicious else 1.0

    # Weighted harmonic mean (follower quality dominates)
    weights = [0.4, 0.3, 0.2, 0.1]
    values  = [follower_quality, comment_quality, engagement_quality, velocity_penalty]

    numerator   = sum(weights)
    denominator = sum(w / v for w, v in zip(weights, values) if v > 0)

    return numerator / denominator if denominator > 0 else 0.0
```

**Example call:**

```python
m = authenticity_multiplier(
    bot_follower_rate=0.40,
    comment_authenticity=15,
    pod_engagement_rate=0.035,
    velocity_suspicious=True,
)
# Returns approximately 0.46
# This account's effective scores are halved before composite scoring.
```

---

## Tooling Reference

When manual sampling is impractical at scale, these tools automate the audits above:

| Tool | What it measures | Output |
|---|---|---|
| HypeAuditor | Bot follower %, audience quality score | Score 0–100 |
| Modash | Fake follower %, engagement quality | Score + breakdown |
| Social Blade | Growth history anomalies (sudden follower spikes) | Charts |
| Sparktoro | Audience composition (real people vs. bots) | % breakdown |
| Phlanx | Engagement rate vs. platform average | ER score |

**Integration pattern:** Pull HypeAuditor's Audience Quality Score (AQS), normalize to 0–1, and use directly as `follower_quality` instead of computing it manually. Their AQS corresponds closely to `(1 - bot_follower_rate)` in the formula above.

---

## Decision Table: When to Disqualify vs. Adjust

| bot_follower_rate | comment_authenticity | Action |
|---|---|---|
| > 50% | any | Hard disqualify — do not score |
| 30–50% | < 30 | Hard disqualify |
| 30–50% | ≥ 30 | Apply multiplier, flag for manual review |
| 15–30% | < 40 | Apply multiplier, flag |
| 15–30% | ≥ 40 | Apply multiplier only |
| < 15% | any | Apply multiplier; no flag needed |

Disqualification means the account is excluded from the ranked output entirely. The final JSON output should include a `disqualified` array alongside `rankings`:

```json
{
  "rankings": [...],
  "disqualified": [
    {"account": "@handle", "reason": "bot_follower_rate=0.55", "raw_influence": 78}
  ]
}
```

---

## Gotchas Specific to Authenticity Detection

- **New accounts look clean**: An account that bought followers 6 months ago then stopped will pass velocity checks now. Always check 90-day follower growth history, not just current ratios.
- **Niche audiences fail generic benchmarks**: A B2B SaaS influencer with 5K followers and 0.8% ER may be fully authentic — their audience is professionals who don't engage publicly. Platform benchmarks assume consumer content.
- **High authenticity ≠ high influence**: Passing all authenticity checks means the engagement is real, not that it matters. A fully authentic micro-account can still have zero purchase-driving power. Authenticity is a floor check, not a ceiling.
- **Pod detection breaks for close communities**: Tight-knit communities (indie game devs, academic researchers) naturally cross-comment. Don't flag pod_commenter_rate > 10% for accounts in small professional niches without verifying the commenters are genuinely in the same field.
- **Purchased comments exist**: Some services sell comments that look qualitative. If comment_authenticity scores suspiciously high but follower quality is low, cross-check whether the same commenter accounts appear across multiple influencers in your sample.
