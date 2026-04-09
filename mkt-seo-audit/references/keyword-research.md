# Keyword Research

## Keyword Prioritization Framework

The core problem with keyword research is not finding keywords — it's choosing which ones to target first. Every page has finite authority, and spreading effort across too many targets produces mediocre rankings on all of them.

### The Priority Score Formula

For each candidate keyword, compute:

```
Priority Score = (Search Volume × CTR Multiplier × Business Value) ÷ (Keyword Difficulty + 1)
```

**Variables:**

| Variable | Source | Notes |
|----------|--------|-------|
| Search Volume | Ahrefs, SEMrush, or GSC | Monthly, local market |
| CTR Multiplier | Position target (see table below) | Adjusts for achievable position |
| Business Value | Internal scoring 1–3 | 3 = direct revenue, 2 = lead gen, 1 = awareness |
| Keyword Difficulty | Tool score 0–100 | Use the same tool consistently |

**CTR Multiplier by Target Position:**

| Target SERP Position | CTR Multiplier |
|---------------------|---------------|
| #1 | 0.28 |
| #2–3 | 0.12 |
| #4–5 | 0.07 |
| #6–10 | 0.03 |
| Page 2 | 0.005 |

Source: Sistrix 2023 CTR study. These are averages; branded queries, featured snippets, and SERP features shift CTR significantly.

### Worked Example

Three candidate keywords for an e-commerce site selling standing desks (Taiwan market):

| Keyword | Volume | KD | Business Value | Target Pos | Priority Score |
|---------|--------|----|----------------|------------|---------------|
| 站立辦公桌推薦 | 2,400 | 35 | 3 | #3 | (2400 × 0.12 × 3) ÷ 36 = **24.0** |
| 站立辦公桌 | 8,900 | 72 | 3 | #5 | (8900 × 0.07 × 3) ÷ 73 = **25.6** |
| 辦公桌 | 33,100 | 91 | 1 | page 2 | (33100 × 0.005 × 1) ÷ 92 = **1.8** |

Decision: Target 站立辦公桌 first despite higher difficulty because the volume advantage is worth it. Skip 辦公桌 — the generic term is dominated by furniture giants; business value is too low to justify the fight.

---

## Intent Taxonomy

Assign intent before choosing a landing page type. Wrong page type for the intent = permanent ranking ceiling.

| Intent | Query Signal | Correct Page Type | Wrong Page Type |
|--------|-------------|-------------------|-----------------|
| Informational | 怎麼, 如何, what is, 推薦 | Blog post / guide | Product page |
| Commercial investigation | 比較, vs, review, 評價, best | Comparison / roundup | Category page |
| Transactional | buy, 購買, 哪裡買, price | Product / category page | Blog post |
| Navigational | brand name, login | Brand page | Any other |

**Practical rule**: Open the top 5 Google results for the keyword. If 4 of 5 are blog posts, write a blog post. Google's algo has already determined the dominant intent — don't fight it.

---

## Keyword Research Workflow (Step-by-Step)

### Step 1: Seed List (30 minutes)

Start from three sources:
1. **GSC Performance report** → sort by Impressions, export top 100 queries you already rank for (even weakly)
2. **Competitor gap** → In Ahrefs "Content Gap", enter your domain vs 2–3 competitors → keywords they rank for, you don't
3. **Customer language** → Pull exact phrases from product reviews, support tickets, sales call transcripts

Goal: 50–200 seed keywords.

### Step 2: Expand with Modifiers

Apply modifier categories systematically to each seed:

```
{seed} + [推薦, 評價, 比較, 價格, 怎麼用, 教學, 問題, 品牌, 台灣]
{seed} + [best, cheap, review, how to, near me, vs {competitor}]
```

Also pull: "People also ask" boxes and "Related searches" from actual Google SERPs.

### Step 3: Filter and Cluster

**Filter criteria** (remove if any):
- Volume < 50 AND KD > 40 (too small to be worth fighting for)
- Pure navigational (competitor brand names)
- Outside your category (topic drift)

**Cluster**: Group keywords that share the same searcher intent and would be served by the same page. One cluster = one page.

Clustering method:
1. Run the top-3 keywords through Google
2. If ≥ 3 of the same URLs appear in results for all 3 → they belong to the same cluster

### Step 4: Map to Pages

```
Cluster A (primary: 站立辦公桌推薦)
  └─ Target page: /blog/standing-desk-guide/
  └─ Secondary keywords: 站立辦公桌優缺點, 站立辦公桌好嗎
  └─ Intent: Informational
  └─ Priority Score: 24.0

Cluster B (primary: 站立辦公桌)
  └─ Target page: /category/standing-desks/
  └─ Secondary keywords: 電動升降桌, 升降辦公桌
  └─ Intent: Transactional
  └─ Priority Score: 25.6
```

Never target two pages at the same cluster — this causes keyword cannibalization (Google can't determine which page to rank).

---

## Keyword Difficulty Calibration

Tool KD scores are not equivalent across tools. They measure different proxies for the same thing.

| Tool | KD Methodology | Bias |
|------|----------------|------|
| Ahrefs | Referring domains to top-10 pages | Overestimates difficulty for informational queries |
| SEMrush | Percentage of effort needed | Tends to score lower overall |
| Moz | PA/DA of ranking pages | Slow to update; use for directional only |
| Google Keyword Planner | Competition = advertiser competition | Reflects ads, not organic SEO |

**Calibrate against your domain's track record**: If your DR 30 site has won rankings for keywords where Ahrefs KD = 20–30, use that as your real ceiling, not the raw score.

Rough rule of thumb for a new-to-established site (DR 20–50):

| Ahrefs KD | Realistic to rank? |
|-----------|-------------------|
| 0–20 | Yes, within 3 months |
| 21–40 | Yes, 6–12 months with solid content |
| 41–60 | Possible, requires backlinks + E-E-A-T |
| 61–80 | Unlikely without significant authority building |
| 81–100 | No, unless you are an established brand |

---

## Long-Tail vs Short-Tail Trade-off

Short-tail (1–2 words) and long-tail (3+ words) are not better or worse — they serve different roles.

```
Short-tail:  辦公桌          → 33,100/mo, KD 91, low conversion
Mid-tail:    站立辦公桌       → 8,900/mo,  KD 72, medium conversion
Long-tail:   電動升降辦公桌推薦品牌 → 320/mo, KD 18, high conversion
```

**When to target long-tail first:**
- New site (< 12 months old, DR < 30)
- Entering a crowded market
- Testing whether a topic converts before investing in a mid/short-tail page

**When to target mid/short-tail:**
- Established authority on related topics
- Cluster already covered at long-tail level
- Business impact of the traffic volume justifies the effort

---

## GSC as a Keyword Discovery Tool

Google Search Console is often underused for keyword research. It shows real impressions data for your actual domain — more reliable than volume estimates.

**Workflow for extracting keyword opportunities from GSC:**

1. Performance → Search results → Filter: Position > 10, Impressions > 100
2. These are keywords you appear for but don't rank on page 1
3. Sort by Impressions descending
4. For each keyword: check if there's already a page targeting it

| Scenario | Action |
|----------|--------|
| Existing page, keyword in title | Refresh content; improve internal links to page |
| Existing page, keyword NOT in title | Update title tag, H1, and opening paragraph |
| No existing page | Create new page targeting this cluster |

This is sometimes called the "low-hanging fruit" method. Moving a keyword from position 12 to position 4 is often worth more traffic than creating a new page from scratch.

---

## Taiwan Market Specifics

### Language Segmentation

Taiwan searches skew toward Traditional Chinese but mixing with English is common in tech and B2B:

- `SEO優化` and `SEO` both have significant volume — research both
- Don't assume `SEO教學` (TW) and `SEO教程` (CN simplified) are interchangeable; Google treats them differently
- Some queries have higher volume in English even in Taiwan: `ChatGPT`, `SaaS`, `API`

### Search Volume Data Limitations

Most keyword tools pull global or simplified-Chinese data for the Taiwan market. Approach:

1. Use Google Keyword Planner with location set to Taiwan (TW) + Language: Traditional Chinese
2. Cross-check with GSC if you have any existing traffic — GSC shows real Taiwan volume
3. Treat Ahrefs/SEMrush TW volume as relative signal, not absolute number

### Google vs Yahoo in Taiwan

Yahoo Taiwan retains a notable share of desktop search in older demographics (finance, news). For most e-commerce and tech clients, optimize for Google exclusively — Yahoo in Taiwan uses Google's index since 2011.

---

## Cannibalization Detection

Keyword cannibalization occurs when two pages on the same site compete for the same query. Symptoms: rankings oscillate, neither page breaks page 1.

**Detection query:**
```
site:yourdomain.com "target keyword"
```

If ≥ 2 pages appear, you have a potential cannibalization risk.

**Resolution options:**

| Situation | Fix |
|-----------|-----|
| Both pages are valuable but different intent | Differentiate content clearly; each must serve a distinct user need |
| One page is clearly stronger | 301 redirect weaker → stronger |
| Both pages are weak | Merge content into one canonical page; 301 redirect the other |
| Same content, different URL | Canonical tag pointing to preferred URL |

---

## Keyword Tracking Setup

After targeting decisions are made, set up rank tracking so changes are measurable.

Minimum tracking setup:
- 1 primary keyword per target page
- 2–3 secondary keywords per cluster
- Track at the country + device level (mobile and desktop differ in Taiwan)
- Frequency: weekly is sufficient; daily is noisy

**Leading vs lagging indicators:**

| Indicator | What it measures | Lag |
|-----------|-----------------|-----|
| GSC Impressions | Google is indexing you for the query | 1–2 weeks |
| GSC Average Position | Ranking movement | 2–4 weeks |
| GSC Clicks | Traffic impact | 4–8 weeks |
| Revenue / leads from organic | Business impact | 6–12 weeks |

Don't report to stakeholders on revenue impact before 6 months. Tracking position movement is the right leading indicator for SEO work in progress.
