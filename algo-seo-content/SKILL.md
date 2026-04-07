---
name: "algo-seo-content"
description: "Execute content SEO strategy from keyword research through content planning, writing, and on-page optimization. Use this skill when the user needs to create SEO-optimized content, perform keyword research, identify content gaps, or improve existing content rankings — even if they say 'content strategy', 'keyword research', or 'how to rank for this topic'."
metadata:
  category: "WP-35 SEO 演算法"
  tags: ["seo", "content-strategy", "keyword-research", "on-page-seo"]
---

# Content SEO Strategy

## Overview

Content SEO is the systematic process of creating and optimizing content to match search intent and rank organically. The pipeline: keyword research → intent mapping → content creation → on-page optimization → performance monitoring. Success depends on intent match, not keyword density.

## When to Use

**Trigger conditions:**
- Planning new content to capture organic search traffic
- Optimizing existing underperforming content
- Conducting keyword research and content gap analysis

**When NOT to use:**
- When the issue is technical (page speed, crawlability) — use technical SEO
- When the issue is off-page (backlinks, authority) — use backlink analysis

## Algorithm

```
IRON LAW: Content Must Match SEARCH INTENT
A perfectly optimized page targeting the wrong intent will NOT rank.
Four intent types:
1. Informational — wants to learn ("how to", "what is")
2. Navigational — wants a specific site ("github login")
3. Commercial — comparing options ("best CRM 2025")
4. Transactional — wants to buy/do ("buy iPhone 16 case")
Check SERP results to determine actual intent before writing.
```

### Phase 1: Input Validation
Define target topic/niche. Gather seed keywords from brainstorming, competitor analysis, and tools (Ahrefs, SEMrush, Google Keyword Planner).
**Gate:** Seed keyword list with search volume and difficulty estimates.

### Phase 2: Core Algorithm
1. **Keyword clustering**: Group related keywords by intent and topic
2. **SERP analysis**: Check top 10 results for each cluster — identify intent, content format, and depth
3. **Content gap analysis**: Find keywords competitors rank for that you don't
4. **Content brief**: Define: target keyword, intent, format (guide/list/comparison), word count benchmark, required subtopics from SERP analysis
5. **On-page optimization**: Title tag (keyword front-loaded), meta description, H1/H2 structure, internal links, image alt text

### Phase 3: Verification
Check: title contains primary keyword, intent matches SERP, all key subtopics covered, internal links to related content.
**Gate:** Content matches identified intent and covers SERP-derived subtopics.

### Phase 4: Output
Return content brief and optimization checklist.

## Output Format

```json
{
  "content_brief": {"primary_keyword": "...", "intent": "informational", "format": "how-to guide", "target_word_count": 2000, "subtopics": ["...", "..."]},
  "optimization": {"title": "...", "meta_description": "...", "h2_structure": ["...", "..."], "internal_links": 5},
  "metadata": {"search_volume": 2400, "keyword_difficulty": 35}
}
```

## Examples

### Sample I/O
**Input:** Topic "email marketing automation", target market: Taiwan SMBs
**Expected:** Primary KW: "email行銷自動化", intent: commercial investigation, format: comparison guide, 2500 words

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Zero search volume keyword | Consider if it's emerging or nonexistent | May be worth targeting if topically relevant |
| KD > 80 for new site | Target long-tail variants first | New sites can't compete on high-KD terms |
| Mixed intent SERP | Create content matching dominant intent | Don't try to serve all intents in one page |

## Gotchas

- **Keyword density is dead**: There's no optimal keyword density. Write naturally. Forced keyword insertion hurts readability and may trigger spam signals.
- **Search volume ≠ traffic**: A #1 ranking for a 10K volume keyword won't bring 10K visits. Click-through rates vary by SERP features (ads, featured snippets, PAA).
- **Content freshness**: Some queries demand fresh content (e.g., "best laptop 2025"). Outdated content drops rankings even if it once ranked #1.
- **Cannibalization**: Multiple pages targeting the same keyword compete with each other. One strong page outperforms three mediocre ones.
- **E-E-A-T**: For YMYL topics (health, finance), Google requires demonstrated Experience, Expertise, Authority, and Trust. Anonymous content won't rank.

## References

- For keyword clustering methodology, see `references/keyword-clustering.md`
- For content brief templates, see `references/content-brief-template.md`
