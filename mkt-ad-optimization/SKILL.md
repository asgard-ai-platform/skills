---
name: "mkt-ad-optimization"
description: "Optimize digital advertising campaigns across Google Ads, Meta Ads, and LINE LAP including bidding strategies, audience targeting, creative testing, and ROAS optimization. Use this skill when the user needs to improve ad performance, reduce CPA, select bidding strategies, or allocate budget across platforms — even if they say 'our ads aren't working', 'reduce our cost per acquisition', 'Google vs Facebook ads', or 'improve our ROAS'."
metadata:
  category: "WP-09 數位行銷"
  tags: ["digital-marketing", "advertising", "google-ads", "meta-ads"]
---

# Digital Ad Optimization

## Framework

```
IRON LAW: Optimize for the Business Metric, Not the Ad Metric

High CTR with low conversion = wasted clicks (attracting curiosity, not buyers).
Low CPC with no sales = cheap traffic that doesn't convert.

The only metrics that matter: CPA (Cost Per Acquisition), ROAS (Return On Ad Spend),
and ultimately: profit per ad dollar. Optimize the funnel, not the ad.
```

### Platform Comparison

| Platform | Best For | Audience | Avg CPC (Taiwan) | Targeting Strength |
|----------|---------|---------|-----------------|-------------------|
| **Google Search** | High-intent queries, direct response | Active searchers | NT$5-30 | Keyword intent (strongest) |
| **Google Display** | Awareness, retargeting, broad reach | Passive browsing | NT$1-5 | Contextual, audience |
| **Meta (FB/IG)** | Social discovery, visual products, lookalike | Social users | NT$3-15 | Interest, behavior, lookalike |
| **LINE LAP** | Taiwan-specific, broad reach | LINE users (95% Taiwan) | NT$3-20 | Demographics, interests |
| **YouTube** | Video branding, consideration | Video viewers | NT$1-5 (CPV) | Intent, affinity, in-market |
| **TikTok** | Gen Z, viral products, short-form video | Young demographic | NT$2-10 | Interest, behavior |

### Bidding Strategies

| Strategy | How It Works | When to Use |
|----------|-------------|------------|
| **Manual CPC** | You set max CPC | Learning phase, small budgets, full control |
| **Target CPA** | Algorithm optimizes for target cost per acquisition | 30+ conversions/month, known CPA target |
| **Target ROAS** | Algorithm optimizes for target return on ad spend | E-commerce, known revenue per conversion |
| **Maximize Conversions** | Spend full budget to get max conversions | Growth phase, less concerned about CPA |
| **Maximize Clicks** | Most clicks for budget | Traffic campaigns, awareness |

### Optimization Workflow

**Phase 1: Audit Current Performance**
- CPA by campaign, ad group, keyword/audience
- Quality Score (Google) or Relevance Score (Meta)
- Conversion rate by landing page
- Wasted spend: search terms with clicks but no conversions

**Phase 2: Quick Wins (Week 1-2)**
- Add negative keywords (Google Search)
- Pause underperforming ad groups/audiences
- Reduce bids on high-CPA keywords
- Fix landing page mismatches (ad promise ≠ landing page content)

**Phase 3: Structural Improvements (Week 3-4)**
- Audience segmentation: separate cold, warm, hot audiences
- Creative refresh: new ad copy/images (fatigue sets in after 2-4 weeks)
- Landing page optimization: speed, mobile, clear CTA

**Phase 4: Scaling (Month 2+)**
- Increase budget on winning campaigns (incrementally, +20%/week)
- Expand to new audiences (lookalikes, new interests)
- Test new platforms
- Build retargeting funnel: awareness → consideration → conversion

### Creative Testing (A/B)

| Element | What to Test | Minimum Sample |
|---------|-------------|---------------|
| Headline | Benefit vs feature, question vs statement | 1,000 impressions each |
| Image/Video | Product shot vs lifestyle, static vs video | 1,000 impressions each |
| CTA | "Shop Now" vs "Learn More" vs "Get Offer" | 500 clicks each |
| Offer | Free shipping vs % discount vs gift | 100 conversions each |

## Output Format

```markdown
# Ad Optimization Report: {Campaign/Account}

## Performance Summary
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Spend | NT${X}/month | — | — |
| CPA | NT${X} | NT${X} | 🟢/🟡/🔴 |
| ROAS | {X}x | {X}x | 🟢/🟡/🔴 |
| CVR | {%} | {%} | 🟢/🟡/🔴 |

## Top Performing
| Campaign/Ad | CPA | ROAS | Action |
|------------|-----|------|--------|
| {name} | NT${X} | {X}x | Scale +20% |

## Underperforming
| Campaign/Ad | CPA | Issue | Action |
|------------|-----|-------|--------|
| {name} | NT${X} | {diagnosis} | Pause/Optimize/Restructure |

## Optimization Plan
| Priority | Action | Expected Impact | Timeline |
|----------|--------|----------------|----------|
| 1 | {action} | CPA -{X%} | {weeks} |
```

## Gotchas

- **Learning phase needs patience**: Google/Meta algorithms need 50+ conversions per week per ad group to optimize. Restructuring too frequently resets learning.
- **Attribution isn't perfect**: Google takes credit for Google, Meta takes credit for Meta. Use UTM parameters and a neutral analytics tool (GA4) for cross-platform attribution.
- **Creative fatigue is real**: Even winning ads degrade over 2-4 weeks as the same audience sees them repeatedly. Refresh creatives regularly.
- **Taiwan ad market specifics**: LINE LAP reaches demographics that Facebook is losing (older users). Google is dominant for search intent. Mix platforms based on your audience.
- **iOS privacy (ATT)**: Since iOS 14.5, Meta tracking is limited. Expect less accurate reporting for iOS users. Use conversion API and model-based attribution.

## References

- For Google Ads account structure best practices, see `references/google-ads-structure.md`
- For Meta Ads creative guidelines, see `references/meta-creative.md`
