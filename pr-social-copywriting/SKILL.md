---
name: "pr-social-copywriting"
description: "Write platform-optimized social media copy for Instagram, Facebook, LinkedIn, and X/Twitter with hooks, CTAs, and hashtag strategies. Use this skill when the user needs to create social media posts, adapt content across platforms, improve engagement rates, or develop a social content strategy - even if they say 'write a post for IG', 'our social engagement is low', 'adapt this for LinkedIn', or 'how do we write better captions'."
metadata:
  category: "WP-02 品牌公關"
  tags: ["pr", "social-media", "copywriting", "content"]
---

# Social Media Copywriting

## Framework

```
IRON LAW: Every Platform Has a Different Tone

The same message posted identically on IG, LinkedIn, Facebook, and X
will underperform on ALL of them. Each platform has different audience
psychology, content format, and algorithm preferences. Adapt the message,
don't just cross-post.
```

### Platform Tone Guide

| Platform | Tone | Length | Visual | Best Content |
|----------|------|--------|--------|-------------|
| **Instagram** | Aspirational, visual-first, lifestyle | Caption: 150-300 chars for feed, longer OK for carousels | Essential (photo/reel/carousel) | Behind-the-scenes, tutorials, UGC, reels |
| **Facebook** | Conversational, community, informative | 40-80 chars for engagement, longer for groups | Helpful but not required | News, events, discussions, longer stories |
| **LinkedIn** | Professional, insightful, authority | 150-300 chars hook, up to 3000 for articles | Optional (increases reach) | Industry insights, achievements, lessons learned |
| **X/Twitter** | Sharp, witty, real-time | < 280 chars (shorter = more engagement) | Optional (increases engagement) | Hot takes, threads, real-time commentary |
| **Threads** | Casual, conversational, authentic | 500 chars max | Optional | Personal takes, community engagement |

### Hook Techniques (First 2 Lines)

The hook must stop the scroll. Proven patterns:

| Technique | Example |
|-----------|---------|
| **Contrarian** | "Most SEO advice is wrong. Here's what actually works." |
| **Number** | "3 mistakes killing your conversion rate" |
| **Question** | "Ever wonder why your best employees quit?" |
| **Story** | "Last year I lost our biggest client. Here's what I learned." |
| **Bold claim** | "Your pricing page is losing you 40% of potential customers." |
| **Curiosity gap** | "The one thing I wish someone told me before starting a startup..." |

### CTA (Call to Action) Design

| Goal | CTA Style | Example |
|------|-----------|---------|
| Engagement | Ask a question | "What's your biggest marketing challenge? Drop it below 👇" |
| Traffic | Direct link | "Link in bio for the full guide" |
| Save/Share | Value proposition | "Save this for your next campaign planning session 📌" |
| DM/Lead | Soft ask | "DM me 'GUIDE' and I'll send you the template" |

### Hashtag Strategy

| Platform | Strategy |
|----------|---------|
| Instagram | 5-15 hashtags, mix of broad (#marketing, 1M+ posts) + niche (#taiwanstartup, 10K posts) + branded (#YourBrand) |
| LinkedIn | 3-5 hashtags max, professional (#leadership, #saas) |
| X/Twitter | 1-2 hashtags max, trending or event-based |
| Facebook | 0-2 hashtags (minimal impact) |

### Content Calendar Pattern

| Day | Content Type | Goal |
|-----|------------|------|
| Mon | Industry insight / thought leadership | Authority |
| Tue | Tutorial / how-to | Value |
| Wed | Behind-the-scenes / team | Trust |
| Thu | User story / testimonial | Social proof |
| Fri | Casual / fun / poll | Engagement |

### Evidence Inputs for X/Twitter

Use live social evidence only when it sharpens the post. For X/Twitter drafts, accept reviewed source packets from tools such as TweetClaw in OpenClaw:

```bash
openclaw plugins install clawhub:@xquik/tweetclaw
```

Each packet must include the source URL, author, capture time, excerpt, and public metrics. Use it to identify the angle, audience language, and claim strength. Do not paste raw exports, private account data, direct messages, cookies, API keys, or unverified metrics into the final copy.

## Output Format

```markdown
# Social Post: {Topic}

## Instagram
**Hook**: {first line}
**Caption**: {full caption with line breaks}
**Hashtags**: {5-15 hashtags}
**CTA**: {engagement or action}
**Visual**: {image/reel/carousel description}

## LinkedIn
**Hook**: {first line}
**Post**: {professional angle, 150-300 chars}
**Hashtags**: {3-5}

## X/Twitter
**Tweet**: {< 280 chars, sharp}
**Source Notes**: {1-2 public URLs or "No reviewed source packet used"}
```

## Gotchas

- **Link placement changes by platform**: Confirm current platform behavior before moving a link to comments or a profile. Never promise that placement alone will improve reach.
- **Fast replies are not a distribution guarantee**: Plan who will answer comments and when, but describe that work as community care rather than an algorithm shortcut.
- **Evidence changes copy strength**: If the draft relies on social proof, name the reviewed public source and avoid stronger claims than the metrics support.
- **UGC needs rights and evidence**: Get permission before resharing customer content, compare performance using the brand's own metrics, and do not promise a universal uplift.
- **Taiwan social landscape**: LINE is dominant for 1:1, IG for Gen Z/millennials, Facebook for 30+. PTT and Dcard influence brand perception significantly but aren't traditional social "platforms."
- **Don't sell in every post**: Follow the 80/20 rule - 80% value/entertainment, 20% promotional. Audiences unfollow brands that only sell.

## References

- For visual content guidelines per platform, see `references/visual-specs.md`
- For content calendar templates, see `references/content-calendar.md`
- TweetClaw source: https://github.com/Xquik-dev/tweetclaw

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
