# Content SEO Reference

## Core Principle

Content SEO answers one question: **does this page deserve to rank for this query?**

Google's ranking systems model the intent behind a query, find pages that satisfy it better than alternatives, and reward pages that demonstrate Experience, Expertise, Authoritativeness, and Trustworthiness (E-E-A-T). Optimization means making the page's actual quality legible to the ranking system — not gaming signals.

---

## Step 1: Map Page → Intent → Primary Keyword

Every optimized page has exactly one primary keyword and one dominant search intent. More than one primary keyword creates competing signals.

### Intent Classification

| Intent Type | Query Signal | Content Type That Wins |
|-------------|-------------|----------------------|
| Informational | "how to", "what is", "why does" | Guides, tutorials, definitions |
| Commercial investigation | "best X", "X vs Y", "X review" | Comparison tables, pros/cons, rankings |
| Transactional | "buy X", "X price", "X coupon" | Product pages, landing pages |
| Navigational | brand name, site name | Homepage, brand page |

**Worked example:**

Query: `best project management software for small teams`
- Intent: Commercial investigation
- ✅ Correct content: Comparison article with table, pros/cons per tool, recommendation
- ❌ Wrong content: A product page for one specific tool
- ❌ Wrong content: A how-to guide on project management

If your page type doesn't match the dominant intent in the SERP, no amount of on-page optimization will overcome the mismatch.

### How to Verify Intent Match

1. Search the target keyword in Google (private browsing, correct region)
2. Note the content type of the top 5 organic results
3. Note the format (listicle, long-form guide, short answer, video)
4. Your page should match the dominant pattern, not fight it

---

## Step 2: Measure and Target Content Depth

Thin content is a ranking weakness. "Thin" doesn't mean short — it means the page fails to satisfy the query relative to competing pages.

### Depth Proxy: Topic Coverage Score

Score your page against a reference set of top-ranking competitors:

```
For each subtopic covered by ≥ 3 of the top 5 competitors:
  +1 if your page also covers it
  0 if your page omits it

Coverage Score = (your covered subtopics) / (total required subtopics)
```

**Target**: Coverage Score ≥ 0.85 before focusing on prose quality.

### How to Build the Subtopic List

1. Open the top 5 ranking pages for the target keyword
2. Extract all H2 and H3 headings
3. Cluster semantically similar headings
4. Any cluster appearing in ≥ 3 pages is a required subtopic
5. Subtopics appearing in only 1-2 pages are optional differentiators

**Worked example** — keyword: `how to write a meta description`

| Subtopic | Competitor coverage | Include? |
|----------|-------------------|----------|
| What is a meta description | 5/5 | Required |
| Character limit / length | 5/5 | Required |
| Include target keyword | 4/5 | Required |
| Call to action tips | 4/5 | Required |
| How Google rewrites meta descriptions | 3/5 | Required |
| Meta description for ecommerce | 2/5 | Optional |
| Schema markup vs meta description | 1/5 | Optional |

A page covering only the first two topics would score 2/5 = 0.40. Required threshold is 5/5 = 1.0.

---

## Step 3: Keyword Integration (Without Stuffing)

### Placement Priority

1. **Title tag** — primary keyword, ideally near the start
2. **H1** — primary keyword (can reword title naturally)
3. **First 100 words of body** — state the topic explicitly
4. **At least one H2** — contains primary keyword or close variant
5. **Image alt text** — one image should have descriptive alt with keyword
6. **Meta description** — include keyword (improves SERP click-through, not ranking directly)

### Keyword Density: What Not to Do

Keyword density targets (e.g., "2-3%") are a legacy metric with no documented Google support. Optimize for:

- **Natural language variation**: Use synonyms and related phrases. A page about "project management" should also naturally contain "task tracking", "team workflow", "deadlines" — not repeat "project management" in every paragraph.
- **Semantic completeness**: Cover concepts related to the topic. If Google's NLP model associates certain terms with your topic, their presence signals topical relevance.

### LSI vs. Semantic Terms: The Distinction

"LSI keywords" is a misused term — Latent Semantic Indexing is not how Google works. What matters: **terms that are conceptually part of the topic**.

To find them: look at the "People also ask" section, the "Related searches" section at the bottom of the SERP, and the language used in the top-ranking pages' body copy.

---

## Step 4: E-E-A-T Signals

E-E-A-T is not a direct ranking factor but it shapes how Google's quality raters evaluate pages, which informs algorithm updates. It matters most for YMYL (Your Money or Your Life) topics: health, finance, legal, safety.

### Experience (the first E, added 2022)

**What it means**: the author has first-hand experience with the topic.

**How to signal it**:
- Author bio mentions relevant professional background or lived experience
- Content includes specific, real-world details that only hands-on experience provides (exact numbers, specific tools used, personal outcomes)
- Case studies or before/after examples with real data
- Photos, screenshots, or original research

**Anti-pattern**: generic how-to content that could have been written by someone who has never done the thing.

### Expertise

**What it means**: the content demonstrates domain knowledge.

**How to signal it**:
- Author credentials visible on the page (degree, certification, job title)
- Citations to primary sources (studies, official documentation, recognized authorities)
- Correct technical terminology used precisely
- Nuanced positions (acknowledging tradeoffs, not oversimplifying)

### Authoritativeness

**What it means**: the site or author is recognized as a source on this topic.

**How to signal it**:
- Backlinks from relevant, authoritative domains in the same industry
- Coverage/mentions in industry publications
- Author has published elsewhere on this topic
- About page that clearly establishes the site's focus and credentials

### Trustworthiness

**What it means**: the page and site are accurate, transparent, and safe.

**How to signal it**:
- Clear authorship (named author, not "Staff" or anonymous)
- Dates displayed and content updated
- Sources linked inline, not just listed at the bottom
- No deceptive design patterns (fake urgency, hidden prices, misleading headlines)
- HTTPS, privacy policy, contact information present

---

## Step 5: Content Freshness

### When Freshness Matters

Google's Query Deserves Freshness (QDF) algorithm boosts recently updated content for:
- News and events
- Regularly changing data (prices, statistics, rankings)
- Recurring topics ("best X in 2025")
- Evergreen topics where the landscape changes (e.g., software tools)

### When Freshness Is Less Critical

- Historical topics ("history of X")
- Definitional content ("what is X")
- Stable technical documentation

### Freshness Optimization

For pages that should rank on freshness-sensitive queries:

1. **Update the publish/modified date** — but only if the content actually changed meaningfully. Changing a word and republishing to fake freshness is a known bad practice.
2. **Add a "Last updated" date** visibly near the top
3. **Audit annually**: pages targeting years ("best tools 2024") need full review and date refresh before the year rolls over
4. **Replace outdated data**: a statistic from 2019 cited on a page today undermines credibility

---

## Step 6: Title Tag Construction

The title tag is the highest-impact on-page element. It determines SERP click-through rate (CTR) and signals relevance.

### Formula

```
[Primary Keyword] — [Secondary differentiator] | [Brand]
```

or

```
[Primary Keyword]: [Benefit or qualifier] — [Brand]
```

### Constraints

- **< 60 characters** (Google truncates at ~580px; 60 chars is a safe proxy)
- Primary keyword as close to the start as natural language allows
- Brand at the end unless it is the primary keyword (navigational queries)

### Worked Examples

| Query | Bad Title | Good Title |
|-------|-----------|------------|
| `project management software` | `Our Product - Manage Your Work Better Today!` | `Project Management Software for Small Teams — Basecamp` |
| `how to write a meta description` | `Meta Descriptions: Everything You Need To Know About Writing Them Well` | `How to Write a Meta Description (With Examples)` |
| `content seo checklist` | `Content SEO - A Complete Guide to Optimizing Your Content for Search` | `Content SEO Checklist: 12 Steps Before You Publish` |

### When Google Rewrites Your Title

Google rewrites titles it considers misleading, keyword-stuffed, or mismatched to the page content. If your title is being rewritten (visible in GSC via the reported title vs. your tag), diagnose:

1. Is the title tag content significantly different from H1?
2. Does the title match the page's actual content?
3. Is there keyword stuffing (repeating the keyword)?

Fix the underlying mismatch, not the symptom.

---

## Step 7: Meta Description

Meta descriptions are not a ranking factor. They affect CTR, which affects traffic volume (but CTR impact on rankings is contested and likely indirect at best).

### Formula

```
[Hook that matches search intent] + [specific benefit/detail] + [implicit or explicit CTA]
```

### Constraints

- **< 155 characters** (Google truncates beyond ~920px, ~155 chars)
- Include primary keyword (Google bolds query-matching terms in the snippet)
- Match the page's actual content — misleading descriptions increase bounce rate

### Worked Examples

**Query**: `how to audit website seo`

❌ Bad:
> We offer comprehensive SEO audit services for your website. Contact us today to learn more about how we can help improve your rankings.

✅ Good:
> A step-by-step SEO audit covering crawlability, Core Web Vitals, on-page factors, and backlinks. Includes a free checklist you can use right now.

---

## Step 8: Internal Linking for Content Pages

Internal links distribute PageRank through the site and help Google understand topical relationships.

### Rules

1. **Anchor text should be descriptive**: link text "SEO audit checklist" > "click here" > "this article"
2. **Link to relevant pages**, not just popular ones
3. **Pillar-cluster model**: hub pages (broad topic) link to cluster pages (specific subtopic) and vice versa
4. **Max 100 internal links per page** is a soft Googlebot limit; for content pages, 5-20 contextual links is typical
5. **Don't orphan new pages**: every new page should receive at least one internal link from an existing page before or at publish

### Pillar-Cluster Example for an SEO Site

```
Pillar: /seo-guide  (broad: "what is SEO")
  └── Cluster: /technical-seo-checklist
  └── Cluster: /keyword-research-guide
  └── Cluster: /on-page-seo-factors
  └── Cluster: /link-building-strategies
  └── Cluster: /seo-audit  ← this skill's home page
```

Each cluster page links back to the pillar and cross-links to adjacent clusters where contextually relevant.

---

## Content Quality Anti-Patterns

| Anti-Pattern | Description | Fix |
|-------------|-------------|-----|
| **Keyword cannibalization** | Two pages on the same site targeting the same keyword compete against each other | Merge into one page, or differentiate intent clearly |
| **Pogo-sticking bait** | Title/meta promise something the page doesn't deliver; users return to SERP immediately | Match title promise to page content |
| **Wall of text** | Dense paragraphs with no subheadings, bullets, or visual breaks | Break into ≤ 3-sentence paragraphs; use H2/H3 every 200-300 words |
| **FAQ padding** | Generic Q&A appended to inflate word count | Only include FAQ items with real search volume or common user questions |
| **Freshness theater** | Changing the publish date without updating content | Only re-date after substantive content review |
| **AI slop** | AI-generated filler that restates the obvious without adding experience or data | Every paragraph should add information the user couldn't find in 30 seconds via Google |

---

## Quick Pre-Publish Checklist

```
□ Intent match: content type matches dominant SERP pattern
□ Coverage: ≥ 85% of required subtopics covered
□ Title: < 60 chars, primary keyword present
□ Meta: < 155 chars, includes keyword, matches content
□ H1: present, unique, includes primary keyword
□ First 100 words: states the topic explicitly
□ At least one H2 includes primary keyword or synonym
□ Images: all have descriptive alt text
□ Internal links: page links to ≥ 2 related pages with descriptive anchors
□ Internal links: at least one existing page links to this new page
□ Author: named, with credentials visible for YMYL content
□ Date: publish date visible; set reminder to review in 12 months
□ Sources: any statistics or claims link to primary sources
```
