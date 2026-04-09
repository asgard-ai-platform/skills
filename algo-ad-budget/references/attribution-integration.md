# Attribution Integration for Budget Allocation

## Why Attribution Choice Changes Allocation Output

Budget allocation depends on per-campaign CPA or ROAS estimates. Those estimates come directly from your attribution model. The same campaign with the same actual performance can report:

- Last-click CPA: $80
- First-click CPA: $220
- Linear (equal credit) CPA: $140
- Data-driven CPA: $115

If you run the marginal returns optimizer on last-click numbers, you systematically over-allocate to bottom-funnel campaigns (branded search, retargeting) and under-allocate to upper-funnel campaigns (prospecting display, YouTube). The Iron Law — equalize marginal returns — only holds if the returns you're equalizing reflect actual contribution.

---

## Attribution Models: What Each Measures

| Model | Credit rule | Typical bias | When to use for allocation |
|-------|-------------|--------------|---------------------------|
| Last-click | 100% to last touchpoint | Over-credits closers (branded search, retargeting) | Never for multi-channel allocation |
| First-click | 100% to first touchpoint | Over-credits discovery channels | Only if goal is pure acquisition reach |
| Linear | Equal split across all touches | Dilutes high-impact touches | Reasonable default when data-driven isn't available |
| Time-decay | More credit to recent touches | Over-credits bottom-funnel | Acceptable for short purchase cycles (< 3 days) |
| Position-based (40/20/40) | 40% first, 40% last, 20% middle | Less biased than last-click | Better than last-click for most e-commerce |
| Data-driven (DDA) | Regression/Shapley on path data | Reflects actual lift per channel | Preferred when ≥ 3,000 conversions/month per campaign |

---

## The Double-Counting Problem in Detail

When a user sees Display → Search → Retargeting before converting:

- Last-click gives 100 conversions to Retargeting, 0 to Display, 0 to Search
- The optimizer sees Retargeting as extremely efficient → raises Retargeting budget
- Retargeting audience = users who already showed intent (sourced from Display + Search)
- More Retargeting budget with less Display budget means the retargetable pool shrinks
- Retargeting CPA degrades; optimizer responds by cutting further → death spiral

This is attribution-induced over-concentration. The optimizer is locally correct given the inputs but globally wrong because the inputs are biased.

**Concrete check:** If your top-allocated campaign is Retargeting or Branded Search, and these campaigns show impression frequency > 4 for converters in the same window, you have a double-counting problem.

---

## Shapley Value Attribution: The Correct Framework

Shapley values from cooperative game theory distribute conversion credit by measuring each channel's marginal contribution across all possible coalition subsets.

### Formula

For channel $i$ in a set of $N$ channels:

$$\phi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(|N|-|S|-1)!}{|N|!} \left[ v(S \cup \{i\}) - v(S) \right]$$

Where:
- $S$ = subset of channels not including channel $i$
- $v(S)$ = conversion probability given exposure to channels in $S$
- $v(S \cup \{i\})$ = conversion probability when $i$ is added to $S$

### Worked Example (3 Channels)

Channels: Display (D), Search (S), Retargeting (R)

Observed path-level conversion rates:
| Path | Conv rate |
|------|-----------|
| D alone | 0.5% |
| S alone | 2.0% |
| R alone | 4.0% |
| D + S | 3.5% |
| D + R | 4.2% |
| S + R | 5.5% |
| D + S + R | 6.0% |
| none | 0.1% |

Baseline (no ads): 0.1%. Lift values (subtract baseline):

| Path | Lift |
|------|------|
| {D} | 0.4% |
| {S} | 1.9% |
| {R} | 3.9% |
| {D,S} | 3.4% |
| {D,R} | 4.1% |
| {S,R} | 5.4% |
| {D,S,R} | 5.9% |

**Shapley for Display (D):**

$$\phi_D = \frac{1}{6}\big[v(\{D\}) - v(\emptyset)\big] \cdot 2$$
$$+ \frac{1}{6}\big[v(\{D,S\}) - v(\{S\})\big] \cdot 1 + \frac{1}{6}\big[v(\{D,R\}) - v(\{R\})\big] \cdot 1$$
$$+ \frac{1}{6}\big[v(\{D,S,R\}) - v(\{S,R\})\big] \cdot 2$$

Plugging in:

$$\phi_D = \frac{2}{6}(0.4\%) + \frac{1}{6}(3.4\% - 1.9\%) + \frac{1}{6}(4.1\% - 3.9\%) + \frac{2}{6}(5.9\% - 5.4\%)$$
$$= \frac{2}{6}(0.4) + \frac{1}{6}(1.5) + \frac{1}{6}(0.2) + \frac{2}{6}(0.5) \quad [\text{all in \%}]$$
$$= 0.133 + 0.250 + 0.033 + 0.167 = 0.583\%$$

Repeat for S and R. The three values sum to the total lift of 5.9% (they must, by Shapley efficiency).

**Result:** Display gets ~10% of credit vs. 0% under last-click. This translates directly into lower attributed CPA for Display → more Display budget in the optimizer.

---

## Integrating Attributed Conversions into the Allocation Model

Replace raw reported conversions with Shapley-attributed conversions before fitting response curves.

### Step-by-Step Procedure

**Step 1: Collect path data**

For each conversion event, record the ordered sequence of campaign touchpoints within the lookback window (typically 30 days for considered purchase, 7 days for impulse).

```
conversion_id | path                              | revenue
C001          | [Display-Prospecting, Search-NB, Retargeting] | $150
C002          | [Search-Brand]                    | $90
C003          | [Display-Prospecting, Display-Prospecting, Search-NB] | $200
```

**Step 2: Compute Shapley credits**

For each conversion, distribute credit across the contributing campaigns:

```python
def shapley_credits(path: list[str], conversion_value: float) -> dict[str, float]:
    """
    Simplified Shapley via sampling for paths > 4 channels.
    For ≤ 4 channels, use exact enumeration.
    """
    from itertools import combinations
    
    campaigns = list(set(path))
    n = len(campaigns)
    credits = {c: 0.0 for c in campaigns}
    
    # v(S) = estimated conversion prob given subset S appeared in path
    # For simple implementation: use presence/absence logistic model
    # Here: proxy with path coverage ratio
    def v(subset):
        if not subset:
            return 0.0
        coverage = len(set(path) & set(subset)) / len(set(path))
        return coverage  # placeholder; replace with trained model
    
    for campaign in campaigns:
        others = [c for c in campaigns if c != campaign]
        for r in range(len(others) + 1):
            for subset in combinations(others, r):
                subset = list(subset)
                weight = (
                    len(subset) * factorial(len(subset)) 
                    * factorial(n - len(subset) - 1) 
                    / factorial(n)  # wait this is wrong
                )
                # correct weight:
                import math
                weight = math.factorial(len(subset)) * math.factorial(n - len(subset) - 1) / math.factorial(n)
                marginal = v(subset + [campaign]) - v(subset)
                credits[campaign] += weight * marginal
    
    # Scale to conversion value
    total_credit = sum(credits.values())
    if total_credit > 0:
        for c in credits:
            credits[c] = credits[c] / total_credit * conversion_value
    
    return credits
```

**Step 3: Aggregate by campaign and spend level**

For each campaign, sum attributed conversions and revenues across all paths where it appeared, bucketed by that campaign's actual spend level in that period.

```
Campaign: Display-Prospecting
Period: Week 1, Spend: $8,000
  Path C001 credit: 0.31 conversions × $150 = $46.50
  Path C003 credit: 0.55 conversions × $200 = $110.00
  Total attributed: 0.86 conversions, $156.50 revenue
  Attributed CPA: $9,302  ← use this for response curve, not $0 (last-click)
  Attributed ROAS: 0.020  ← vs 0.0 under last-click
```

**Step 4: Fit response curve on attributed data**

Use the attributed conversion values (not platform-reported) as your $y$ when fitting `conversions = f(spend)`.

**Step 5: Run optimizer**

The allocation optimizer in SKILL.md Phase 2-3 is unchanged — you're only changing the input data. The marginal returns it equalizes now reflect actual contribution.

---

## Practical Fallback: Fractional Attribution Without Path Data

If you don't have path-level data (common for smaller accounts or when using multiple ad platforms without a unified CDP), use position-based attribution adjusted for observed frequency.

### Adjusted Position-Based Model

Default 40/20/40 (first/middle/last) is a reasonable prior. Adjust based on purchase cycle:

| Purchase cycle | Recommended weights (first / middle / last) |
|----------------|---------------------------------------------|
| < 1 day (impulse) | 20 / 10 / 70 |
| 1–7 days | 30 / 20 / 50 |
| 7–30 days | 40 / 20 / 40 |
| > 30 days (considered) | 50 / 30 / 20 |

**Why:** Longer cycles mean discovery matters more relative to close.

To apply: when a campaign appears in position "first" on a path with 4 touches, assign it `first_weight / 1` of the conversion. For the two middle touches, each gets `middle_weight / 2`. Last touch gets `last_weight`.

---

## Cross-Platform Attribution Gap

Google Ads, Meta Ads, and TikTok each run their own attribution. If you pull CPA from each platform's native dashboard:

- Google counts a conversion if Search touched it within 30 days
- Meta counts a conversion if Meta touched it within 7-day click / 1-day view
- TikTok counts a conversion if TikTok touched it within 7-day click / 1-day view

One actual conversion becomes **3 reported conversions** — one in each platform. Total reported conversions ≫ actual conversions. This inflates all platforms' efficiency and makes the optimizer think total budget is insufficient.

### Detection

```
inflate_ratio = sum(platform_reported_conversions) / actual_conversions_from_crm
```

If `inflate_ratio > 1.3`, you have significant cross-platform double-counting. Values above 2.0 are common.

### Correction

**Method A (preferred):** Use a unified attribution tool (Northbeam, Triple Whale, Rockerbox, or custom CDP) that deduplicates on customer ID or hashed email. Pull conversions from there, not from ad platforms.

**Method B (approximation):** Scale down platform conversions proportionally.

```
correction_factor = actual_crm_conversions / sum(platform_reported_conversions)
adjusted_conversions_i = platform_reported_i × correction_factor
```

This is a blunt instrument — it applies the same correction to all platforms — but it removes the systematic inflation. Use only when you have no path data.

**Method C (heuristic floor):** Never let `sum(allocated_budget × ROAS_i) > 1.5 × actual_revenue`. If it does, flag that attribution inflation is distorting the optimizer.

---

## View-Through Attribution: When to Include

View-through conversions (user saw an ad, didn't click, later converted) are especially problematic for budget allocation:

- They're easy to fabricate: any user who converted and was in-market was probably served an impression
- Display and video campaigns claim most VTC, inflating their apparent efficiency
- Including 100% VTC credit double-counts with Search (user saw Display, then clicked Search)

**Recommendation for allocation models:**

| Scenario | VTC inclusion |
|----------|---------------|
| Incrementality test confirms VTC lift | Include at 50% credit (conservative) |
| No incrementality test | Exclude entirely |
| Awareness-only campaigns | Include at 20-30% as a proxy for reach value |

Default: **exclude view-through conversions** from the response curves used for allocation. Only add them back if you have hold-out test data showing they are incremental.

---

## Incrementality Testing as Ground Truth

Shapley and position-based models are still observational — they can't separate correlation from causation. If a user would have converted anyway (high intent), all campaigns in their path get credit for a conversion that wasn't caused by any of them.

The only way to measure true causal contribution is a holdout (incrementality) test:

1. Randomly withhold 10-15% of target audience from one campaign
2. Measure conversion rate difference: test (saw ad) vs. control (didn't)
3. True incremental conversions = (test conv rate − control conv rate) × test impressions
4. Use incremental conversions — not attributed conversions — as the $y$ in response curve fitting

**Practical constraint:** You need enough volume to detect a 10-20% lift with p < 0.05. Rule of thumb: ≥ 500 conversions in the control group per test period. Run incrementality tests sequentially per channel; don't run all channels simultaneously (confounds results).

When incrementality data is available for a campaign, replace its Shapley-attributed conversions with incrementally measured conversions in the optimizer input. Treat channels without incrementality tests as Shapley-attributed.

---

## Decision Table: Which Attribution Approach to Use

| Monthly conversions | Path data available? | Incrementality tests? | Use |
|--------------------|---------------------|----------------------|-----|
| < 500 | No | No | Position-based (40/20/40) with cross-platform dedup |
| 500–3,000 | Yes | No | Shapley on path data |
| 500–3,000 | No | No | Position-based + Method B correction |
| > 3,000 | Yes | No | Data-driven (DDA) or Shapley |
| > 3,000 | Yes | Yes (≥ 1 channel) | Incrementality for tested channels, Shapley for rest |
| > 3,000 | Yes | Yes (all channels) | Full incrementality as primary, Shapley as sanity check |

---

## What to Pass to the Budget Optimizer

The allocation algorithm in SKILL.md expects per-campaign spend-vs-conversions data points. After applying attribution:

```json
{
  "campaigns": [
    {
      "name": "Display-Prospecting",
      "attribution_model": "shapley",
      "response_data": [
        {"spend": 5000, "attributed_conversions": 18.4, "attributed_revenue": 2760},
        {"spend": 8000, "attributed_conversions": 26.1, "attributed_revenue": 3915},
        {"spend": 12000, "attributed_conversions": 33.5, "attributed_revenue": 5025}
      ]
    },
    {
      "name": "Search-NB",
      "attribution_model": "shapley",
      "response_data": [
        {"spend": 10000, "attributed_conversions": 95.2, "attributed_revenue": 14280},
        {"spend": 15000, "attributed_conversions": 127.6, "attributed_revenue": 19140},
        {"spend": 20000, "attributed_conversions": 152.0, "attributed_revenue": 22800}
      ]
    }
  ]
}
```

The key contract: `attributed_conversions` must be **deduplicated** across campaigns. The sum of attributed conversions across all campaigns for a given period must equal (or be scaled to equal) actual CRM conversions for that period. This is the invariant that makes the optimizer's output trustworthy.
