---
name: "pr-media-monitoring"
description: "Set up and conduct media monitoring to track brand mentions, sentiment, and share of voice across news, social, and online channels. Use this skill when the user needs to track what's being said about their brand, monitor competitors' media presence, detect emerging PR issues early, or measure campaign reach — even if they say 'what are people saying about us', 'monitor our brand mentions', 'track competitor PR', or 'set up media alerts'."
metadata:
  category: "WP-02 品牌公關"
  tags: ["pr", "media-monitoring", "brand", "reputation"]
---

# Media Monitoring

## Framework

```
IRON LAW: Monitor for Action, Not Just Awareness

Media monitoring that produces weekly reports nobody reads is waste.
Every monitoring setup must have TRIGGER ACTIONS defined: if sentiment
drops below X, alert the PR team. If a competitor launches a campaign,
notify marketing within 24 hours. No triggers = no value.
```

### Monitoring Dimensions

| Dimension | What to Track | Tools |
|-----------|-------------|-------|
| **Volume** | Number of mentions over time | Google Alerts, Mention, Meltwater |
| **Sentiment** | Positive / Neutral / Negative ratio | Brandwatch, Talkwalker, manual coding |
| **Share of Voice** | Your mentions vs competitors' mentions | Industry reports, custom dashboards |
| **Source** | Where mentions appear (news, social, forums, blogs) | Platform analytics, social listening tools |
| **Influencer** | Who is talking (reach, authority) | BuzzSumo, social platform analytics |
| **Topics** | What themes/keywords are associated with your brand | Keyword clustering, topic modeling |

### Setup Steps

**Phase 1: Define Keywords**
- Brand name + common misspellings
- Product names, CEO name, key executives
- Competitor brand names
- Industry keywords (for context)
- Negative keywords to exclude irrelevant results

**Phase 2: Select Channels**
- News (traditional media, online news)
- Social media (Facebook, IG, X/Twitter, PTT, Dcard for Taiwan)
- Forums and review sites
- Video (YouTube, TikTok)
- Podcasts (emerging channel, harder to monitor)

**Phase 3: Set Triggers**
| Trigger | Threshold | Action |
|---------|-----------|--------|
| Negative sentiment spike | >20% increase in 24hrs | Alert PR manager immediately |
| Competitor product launch | Any mention | Notify marketing team |
| Influencer mention (>10K followers) | Any mention | Evaluate for engagement opportunity |
| Crisis keyword detected | "recall", "lawsuit", "scandal" + brand | Activate crisis protocol |

**Phase 4: Reporting Cadence**
- Real-time alerts for crisis triggers
- Daily digest for PR team
- Weekly summary for marketing leadership
- Monthly report for executive team (volume, sentiment, SOV trends)

## Output Format

```markdown
# Media Monitoring Report: {Brand} — {Period}

## Summary
| Metric | Current | Prior Period | Change |
|--------|---------|-------------|--------|
| Total Mentions | {N} | {N} | {%} |
| Sentiment (Pos/Neu/Neg) | {%}/{%}/{%} | ... | ... |
| Share of Voice | {%} | {%} | {±%} |

## Top Mentions
| Date | Source | Headline/Summary | Sentiment | Reach |
|------|--------|-----------------|-----------|-------|
| {date} | {outlet} | {summary} | +/0/- | {est. reach} |

## Alerts Triggered
| Date | Trigger | Action Taken |
|------|---------|-------------|
| {date} | {what happened} | {response} |

## Competitor Activity
| Competitor | Mentions | Key Activity |
|-----------|----------|-------------|
| {name} | {N} | {what they did} |

## Recommendations
1. {action based on findings}
```

## Gotchas

- **Sentiment analysis is imperfect**: Automated tools misclassify sarcasm, industry jargon, and context-dependent language. Manually review a sample weekly to calibrate.
- **PTT/Dcard matter in Taiwan**: For Taiwan brands, PTT and Dcard are critical channels that many international monitoring tools don't cover well. Consider local tools or manual monitoring.
- **Volume spikes ≠ crisis**: A viral meme mentioning your brand positively creates a volume spike. Don't panic — check sentiment before escalating.
- **Competitor monitoring is legal and ethical**: Tracking public mentions of competitors is standard practice. Accessing private data or impersonating competitors is not.

## References

- For crisis escalation protocol, see the pr-crisis-response skill
- For Taiwan-specific media landscape, see `references/taiwan-media.md`
