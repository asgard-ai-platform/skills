---
name: "algo-seo-backlink"
description: "Evaluate backlink quality using Domain Authority, Domain Rating, and trust metrics. Use this skill when the user needs to assess link profile health, identify toxic backlinks, or plan link building strategy — even if they say 'check my backlinks', 'link building', or 'domain authority analysis'."
metadata:
  category: "WP-35 SEO 演算法"
  tags: ["seo", "backlinks", "domain-authority", "link-building"]
---

# Backlink Quality Assessment

## Overview

Backlink analysis evaluates incoming links by quality metrics (DA/DR, relevance, anchor text diversity, toxicity) to assess a site's off-page SEO strength. Quality assessment is heuristic-based using third-party metrics (Moz DA, Ahrefs DR) as PageRank proxies.

## When to Use

**Trigger conditions:**
- Auditing a site's backlink profile for SEO health
- Identifying and disavowing toxic or spammy links
- Planning link building strategy based on competitor analysis

**When NOT to use:**
- When optimizing on-page content (use content SEO)
- When computing actual PageRank from raw link graphs (use PageRank algorithm)

## Algorithm

```
IRON LAW: Backlink QUALITY Outweighs Quantity
One link from a high-authority, topically relevant domain is worth
more than hundreds from low-quality sites. Evaluate every link on:
1. Authority (DA/DR of linking domain)
2. Relevance (topical match between linking and target pages)
3. Placement (editorial in-content > footer/sidebar)
4. Anchor text (natural diversity > exact-match keyword stuffing)
```

### Phase 1: Input Validation
Export backlink data from Ahrefs, Moz, or Search Console. Required fields: referring domain, DA/DR, anchor text, link type (dofollow/nofollow), first seen date.
**Gate:** Complete backlink export with authority metrics.

### Phase 2: Core Algorithm
1. Deduplicate by referring domain (one link per domain for analysis)
2. Score each link: authority (0-100) × relevance (0-1) × placement weight
3. Flag toxic links: DA < 10, irrelevant foreign language, link farm patterns, PBN indicators
4. Compute profile metrics: total referring domains, DR distribution, anchor text diversity index

### Phase 3: Verification
Cross-reference flagged toxic links against known spam databases. Verify anchor text distribution follows natural pattern (branded > URL > keyword > misc).
**Gate:** Toxic links identified, anchor profile analyzed.

### Phase 4: Output
Return profile assessment with link quality distribution and action items.

## Output Format

```json
{
  "profile": {"referring_domains": 450, "avg_dr": 35, "toxic_count": 23, "anchor_diversity": 0.78},
  "actions": [{"type": "disavow", "domains": ["spam1.com"], "reason": "link farm pattern"}],
  "metadata": {"tool": "ahrefs", "export_date": "2025-01-15"}
}
```

## Examples

### Sample I/O
**Input:** 500 backlinks, 200 referring domains
**Expected:** Distribution: 15% DR 60+, 40% DR 20-59, 45% DR 0-19. Flag 23 toxic domains for disavow.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| All links from one domain | Low profile diversity | Single-source dependency is risky |
| 90% exact-match anchors | Anchor text penalty risk | Unnatural anchor pattern |
| Zero backlinks | Focus on content first | Can't optimize what doesn't exist |

## Gotchas

- **DA/DR are third-party estimates**: They approximate PageRank but are NOT Google metrics. Two tools often disagree on the same domain's authority.
- **Nofollow still matters**: Google treats nofollow as a "hint." A nofollow link from a DR 90 site still has SEO value, just less than dofollow.
- **Disavow carefully**: Google's disavow tool is a last resort. Disavowing legitimate links harms your own profile. Only disavow clearly toxic/spammy links.
- **Anchor text manipulation**: Exact-match anchor text used to be a ranking factor; now it's a spam signal. Natural profiles have mostly branded and URL anchors.
- **Temporal patterns**: Sudden spikes in backlinks (e.g., 100 links in one day) trigger spam filters. Natural link acquisition is gradual.

## References

- For link toxicity scoring methodology, see `references/toxicity-scoring.md`
- For competitor backlink gap analysis, see `references/competitor-gap.md`
