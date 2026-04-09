# Attribution Models for CAC Calculation

Attribution determines which marketing channel "gets credit" for a customer acquisition — and therefore which channel's CAC you're calculating. Wrong attribution = wrong CAC = wrong budget decisions.

## The Core Problem

A typical B2C customer journey before converting:

```
Day 1:  Sees Instagram ad → no click
Day 3:  Clicks Facebook retargeting ad → bounces
Day 7:  Googles brand name → clicks organic result → reads blog
Day 9:  Clicks Google Search ad → starts free trial
Day 12: Receives email nurture → converts to paid
```

Five touchpoints. One customer. Each model assigns credit differently.

---

## The Five Standard Models

### 1. Last-Touch Attribution

100% of credit goes to the last touchpoint before conversion.

```
Touchpoint    Credit
Instagram     0%
Facebook      0%
Organic       0%
Google Ad     0%
Email         100%  ← last touch
```

**CAC implication:** Email CAC looks very low. Google Ads and paid social look expensive.

**Use when:** You have a very short sales cycle (< 1 day) with minimal multi-touch journeys.

**Systematic bias:** Overvalues bottom-funnel channels (email, retargeting, brand search). Undervalues awareness channels. Will cause you to cut top-of-funnel spend and wonder why pipeline dries up 60 days later.

---

### 2. First-Touch Attribution

100% of credit goes to the first touchpoint.

```
Touchpoint    Credit
Instagram     100%  ← first touch
Facebook      0%
Organic       0%
Google Ad     0%
Email         0%
```

**Use when:** You care about which channel *introduced* you to customers. Useful for brand awareness measurement.

**Systematic bias:** Overvalues awareness channels. Makes email and retargeting look useless (they get no credit even when they close deals).

---

### 3. Linear Attribution

Credit split equally across all touchpoints.

```
Touchpoint    Credit
Instagram     20%
Facebook      20%
Organic       20%
Google Ad     20%
Email         20%
```

**Formula:**
```
Credit per touchpoint = 1 / Total touchpoints in journey
```

**CAC implication:** If you spent NT$10,000 on Google Ads and NT$10,000 on email in a month, and the average journey has 5 touches:
- Each channel gets 20% of acquisition credit
- CAC per channel = Channel Spend / (Customers × 0.20)

**Use when:** You genuinely don't know which touchpoints matter more. It's unbiased, but also uninformative.

**Systematic bias:** Treats a fleeting ad impression the same as a 20-minute product demo. Equal weight ≠ equal influence.

---

### 4. Time-Decay Attribution

Recent touchpoints get more credit. Credit decays exponentially backward in time.

**Standard half-life: 7 days.** A touchpoint 7 days before conversion gets half the credit of one the day before conversion.

```
Decay formula:
Weight(t) = 2^(−d/half_life)

Where d = days before conversion
```

**Worked example** (7-day half-life):

| Touchpoint | Days Before Conversion | Raw Weight | Normalized Credit |
|-----------|----------------------|------------|-------------------|
| Instagram | 11 | 2^(−11/7) = 0.336 | 11.8% |
| Facebook | 9 | 2^(−9/7) = 0.406 | 14.3% |
| Organic | 5 | 2^(−5/7) = 0.609 | 21.4% |
| Google Ad | 3 | 2^(−3/7) = 0.743 | 26.1% |
| Email | 0 | 2^(0/7) = 1.000 | 35.2% |
| **Total** | | **3.094** | **108.8%** → normalize |

Normalization: divide each by sum (3.094):
```
Instagram: 0.336/3.094 = 10.9%
Facebook:  0.406/3.094 = 13.1%
Organic:   0.609/3.094 = 19.7%
Google Ad: 0.743/3.094 = 24.0%
Email:     1.000/3.094 = 32.3%
```

**Use when:** Your sales cycle is moderate (1-4 weeks) and closing activities genuinely matter more. Standard for B2C e-commerce.

---

### 5. Position-Based (U-Shaped) Attribution

First and last touchpoints each get 40%. Middle touchpoints split the remaining 20%.

```
Touchpoint    Credit
Instagram     40%   ← first
Facebook      6.7%  ← middle (20% / 3)
Organic       6.7%  ← middle
Google Ad     6.7%  ← middle
Email         40%   ← last
```

**Use when:** You believe both discovery and closing are high-value moments, but middle assists are less decisive. Common in B2B SaaS where the first demo and the final proposal meeting are the key events.

---

## Model Comparison: Same Data, Different CAC

**Setup:** A company acquires 100 customers in a month with the journey above (all five touchpoints, one customer type).

Monthly spend:
- Instagram: NT$50,000
- Facebook: NT$80,000
- Google Ads: NT$120,000
- Email tools + labor: NT$30,000
- Total: NT$280,000
- Blended CAC: NT$2,800

**CAC by channel under each model** (NT$):

| Channel | Spend | Last-Touch | First-Touch | Linear | Time-Decay | U-Shaped |
|---------|-------|-----------|-------------|--------|-----------|---------|
| Instagram | 50K | ∞* | 1,250 | 5,600 | 5,138 | 3,182 |
| Facebook | 80K | ∞* | ∞* | 11,200 | 8,122 | — |
| Google Ads | 120K | ∞* | ∞* | 16,800 | 6,667 | — |
| Email | 30K | 750 | ∞* | 4,200 | 2,480 | 1,818 |

*∞ = channel gets 0 conversions attributed, so CAC is undefined

**Key observation:** Under last-touch, Email CAC appears to be NT$750 — a "great" channel. Under time-decay, it's NT$2,480. The underlying economics haven't changed; your measurement model has.

---

## Decision Framework: Which Model to Use

```
Q1: Is your typical customer journey < 2 touchpoints or < 24 hours?
    YES → Last-touch is fine. Multi-touch models add noise, not signal.
    NO  → Go to Q2.

Q2: Do you have reliable data on all touchpoints across channels?
    NO  → Use linear. Admitting ignorance beats false precision.
    YES → Go to Q3.

Q3: Does your sales cycle exceed 2 weeks?
    YES → Time-decay (B2C) or U-shaped (B2B)
    NO  → Go to Q4.

Q4: Are you primarily trying to measure brand awareness ROI?
    YES → First-touch (plus last-touch as a secondary view)
    NO  → Time-decay
```

**Default recommendation for most Taiwanese e-commerce and SaaS companies:** Time-decay with 7-day half-life. It's defensible, accounts for recency without completely ignoring assists, and most analytics platforms implement it natively.

---

## Data Requirements by Model

| Model | Minimum Data Needed | What Breaks It |
|-------|--------------------|-----------------|
| Last-touch | Final conversion event + source tag | UTM stripping, Safari ITP |
| First-touch | First session source | Direct traffic that should be attributed elsewhere |
| Linear | Full session history with sources | Sessions with `(direct)/(none)` source |
| Time-decay | Full session history + timestamps | Clock skew between events |
| U-shaped | Full session history + touchpoint order | Journeys with only 1-2 touches |

**The data gap problem:** Cross-device journeys (mobile → desktop → tablet) break all session-based models. Logged-in users with a persistent ID are partially solvable; anonymous users are not. If > 30% of your traffic is cross-device anonymous, your attribution numbers have a structural error floor regardless of which model you pick.

---

## Implementing in Practice

### Using GA4 (Google Analytics 4)

GA4 offers: Last click, First click, Linear, Time decay, Position-based, and Data-driven (ML-based).

Navigation: **Admin → Attribution settings → Reporting attribution model**

⚠ GA4 only attributes to Google-trackable touchpoints. Offline events, dark social (WhatsApp shares, email forwards), and app-to-web journeys require manual stitching.

### Using a Spreadsheet (Manual Multi-Touch)

When you can export session-level data with UTM parameters:

```python
# Pseudocode for time-decay attribution
HALF_LIFE_DAYS = 7

for each conversion_event:
    sessions = get_sessions_before_conversion(user_id, lookback_days=30)
    
    weights = []
    for session in sessions:
        d = (conversion_date - session.date).days
        w = 2 ** (-d / HALF_LIFE_DAYS)
        weights.append((session.channel, w))
    
    total_weight = sum(w for _, w in weights)
    
    for channel, w in weights:
        channel_credits[channel] += w / total_weight
```

### CAC Calculation with Fractional Attribution

Once you have fractional credits per channel:

```
CAC (channel X) = Spend on channel X
                  ──────────────────────────────────────────
                  Σ attribution_credit(channel X, customer i)
                   for all customers i acquired in period
```

**Blended CAC check:** Sum of all channel-attributed credits should equal total customers acquired. If not, you have an attribution gap (usually untracked direct traffic).

---

## Common Mistakes

**1. Comparing CAC across models without disclosing the model**

"Our Facebook CAC improved from NT$800 to NT$600" — meaningless unless the attribution model is the same in both periods. Platform migrations (UA → GA4) often change the default model and create phantom improvements.

**2. Using channel-level CAC for budget decisions without checking blended CAC**

Individual channel CAC can look great even when blended CAC is terrible. Always anchor to blended CAC first:

```
If Σ(channel CAC × channel share) ≠ Blended CAC:
    → You have an attribution gap; do not trust channel-level numbers for budget decisions
```

**3. Letting the platform choose the model for you**

Meta Ads Manager defaults to last-click, 7-day click + 1-day view. Google Ads defaults to data-driven (when available) or last-click. These are different models. Comparing them directly inflates total attributed customers beyond actual acquisitions (double-counting assists).

**4. Treating UTM-based attribution as ground truth**

UTMs only survive if:
- The user clicks a link (impressions untracked)
- The browser preserves the parameter (Safari strips some cross-site params)
- The landing page passes the UTM through (redirects can strip them)

Use UTM-based numbers as directional, not absolute.

**5. Ignoring view-through attribution entirely**

A customer who saw your YouTube ad three times and then converted via "direct" was influenced by YouTube — but zero-touch last-click misses this entirely. View-through attribution (typically 1-day window for display, 7-day for video) is imprecise but not zero.

---

## The Incrementality Alternative

Attribution models answer "which channel got credit?" Incrementality answers "what would have happened without this channel?"

**Holdout test design:**
1. Randomly split customers into treatment (see ads) and holdout (ads suppressed)
2. Measure conversion rate difference
3. Incremental CAC = Spend / (Treatment conversions − Holdout conversions)

This is the only attribution method that is causally defensible. It requires:
- Minimum ~500 users per cell for statistical power
- A platform that supports holdouts (Meta, Google both do)
- 2-4 week test window

**When blended LTV:CAC is close to the 3:1 threshold**, incrementality testing is worth the setup cost. If your attributed ratio is 3.2:1 but actual incrementality shows 40% of conversions would have happened anyway, your true ratio is closer to 1.9:1 — a fundamentally different business situation.
