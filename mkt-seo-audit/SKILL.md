---
name: "mkt-seo-audit"
description: "Conduct technical and on-page SEO audits covering crawlability, site speed, mobile-friendliness, and content optimization. Use this skill when the user needs to improve search rankings, diagnose traffic drops, audit a website for SEO issues, or plan an SEO strategy — even if they say 'why is our traffic dropping', 'audit our SEO', 'how do we rank higher on Google', or 'our site is slow'."
metadata:
  category: "WP-09 數位行銷"
  tags: ["digital-marketing", "seo", "technical-seo", "audit"]
---

# SEO Audit

## Framework

```
IRON LAW: Technical Foundation Before Content Optimization

A site with brilliant content but broken crawlability, slow speed, or
no mobile support will not rank. Fix technical issues FIRST, then optimize
content. A technically sound site with mediocre content outranks a
technically broken site with great content.

Priority: Crawlability → Speed → Mobile → On-Page → Content → Links
```

### Audit Checklist

**1. Crawlability & Indexing**
| Check | Tool | Red Flag |
|-------|------|----------|
| robots.txt blocking important pages | robots.txt tester | Disallow on key pages |
| Sitemap.xml exists and is valid | XML sitemap validator | Missing or has errors |
| Index coverage | Google Search Console | Excluded pages growing |
| Canonical tags correct | Manual check | Missing or pointing to wrong URL |
| 404 errors | Screaming Frog / GSC | > 5% of URLs return 404 |
| Redirect chains | Screaming Frog | Chain > 2 hops |

**2. Site Speed (Core Web Vitals)**
| Metric | Target | Tool |
|--------|--------|------|
| LCP (Largest Contentful Paint) | < 2.5s | PageSpeed Insights |
| INP (Interaction to Next Paint) | < 200ms | PageSpeed Insights |
| CLS (Cumulative Layout Shift) | < 0.1 | PageSpeed Insights |

**3. Mobile-Friendliness**
- Responsive design (passes Google mobile-friendly test)
- Touch targets > 48px
- No horizontal scrolling
- Text readable without zooming

**4. On-Page SEO (per page)**
| Element | Best Practice |
|---------|-------------|
| Title tag | Primary keyword + brand, < 60 chars |
| Meta description | Compelling, includes keyword, < 155 chars |
| H1 | One per page, includes primary keyword |
| URL structure | Short, descriptive, includes keyword |
| Image alt text | Descriptive, includes keyword naturally |
| Internal linking | Link to related pages with descriptive anchor text |

**5. Content Quality**
- Keyword targeting: each important page targets a primary keyword
- Content depth: covers the topic comprehensively (not thin content)
- E-E-A-T signals: Experience, Expertise, Authoritativeness, Trustworthiness
- Freshness: key content updated within last 12 months

**6. Backlink Profile**
- Total referring domains (Ahrefs, Moz)
- Domain authority / domain rating
- Toxic links (spammy, irrelevant)
- Anchor text distribution (natural vs over-optimized)

## Output Format

```markdown
# SEO Audit: {Website}

## Summary
| Category | Score | Priority Issues |
|----------|-------|----------------|
| Crawlability | 🟢/🟡/🔴 | {top issue} |
| Speed | 🟢/🟡/🔴 | {top issue} |
| Mobile | 🟢/🟡/🔴 | {top issue} |
| On-Page | 🟢/🟡/🔴 | {top issue} |
| Content | 🟢/🟡/🔴 | {top issue} |
| Backlinks | 🟢/🟡/🔴 | {top issue} |

## Critical Issues (fix immediately)
1. {issue + impact + fix}

## High Priority (fix within 30 days)
1. {issue + fix}

## Opportunities
1. {keyword/content opportunity}

## Action Plan
| Priority | Action | Impact | Effort | Timeline |
|----------|--------|--------|--------|----------|
| 1 | {action} | H/M/L | H/M/L | {weeks} |
```

## Gotchas

- **SEO results take 3-6 months**: Don't expect ranking changes within weeks. Measure over quarters, not days.
- **Google Search Console is the source of truth**: Third-party tools estimate. GSC shows actual Google data (clicks, impressions, index status).
- **Core Web Vitals are ranking factors**: Since 2021, Google uses page experience (speed, interactivity, visual stability) as ranking signals. Not optional.
- **AI-generated content**: Google doesn't penalize AI content per se, but penalizes low-quality, unhelpful content regardless of how it was produced. E-E-A-T matters.
- **Local SEO for Taiwan**: For local businesses, Google 我的商家 (Google Business Profile) is critical. Optimize GBP before worrying about organic rankings.

## References

- For keyword research methodology, see `references/keyword-research.md`
- For content optimization guidelines, see `references/content-seo.md`
