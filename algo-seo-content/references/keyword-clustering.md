# Keyword Clustering

Keyword clustering groups semantically related keywords into topic clusters so each page targets one coherent intent rather than competing with itself. The output of clustering is the direct input to content briefs.

---

## Why Cluster Before Writing

A keyword list without clustering leads to two failure modes:

1. **Cannibalization** — creating three separate pages for "email行銷工具", "email行銷軟體", "email行銷平台", each too thin to rank
2. **Missed coverage** — writing one page for "email行銷" while ignoring 40 related long-tail queries that belong on the same page

Clustering resolves both: it tells you which keywords to merge onto one page and which belong on separate pages.

---

## Clustering Signal: SERP Overlap Method

The most reliable clustering signal is **shared ranking URLs**, not semantic similarity. Two keywords belong in the same cluster if Google returns overlapping results for them.

### Formula

```
Overlap(A, B) = |top10(A) ∩ top10(B)| / 10
```

| Overlap Score | Interpretation | Action |
|--------------|----------------|--------|
| ≥ 0.3 (3+ shared URLs) | Same cluster | Target on same page |
| 0.1–0.29 (1–2 shared URLs) | Related but separate | Consider separate pages with internal links |
| 0 | Different topics | Separate pages |

**Why 3?** Google uses the same pages to satisfy both queries → they share intent close enough to co-target.

### Worked Example

Seed keywords: `email行銷自動化`, `email自動化工具`, `自動化行銷軟體`, `email行銷策略`

Fetch top-10 results for each. Suppose:

| Pair | Shared URLs | Score | Decision |
|------|-------------|-------|----------|
| email行銷自動化 ↔ email自動化工具 | 4 | 0.40 | Same cluster ✓ |
| email行銷自動化 ↔ 自動化行銷軟體 | 3 | 0.30 | Same cluster ✓ |
| email行銷自動化 ↔ email行銷策略 | 1 | 0.10 | Separate pages |

Result: `{email行銷自動化, email自動化工具, 自動化行銷軟體}` → one cluster → one page.
`email行銷策略` → separate cluster → separate page.

---

## Manual Clustering (No Tools)

When SERP overlap data isn't available, use a two-pass manual method.

### Pass 1 — Intent Split

Sort all keywords into the four intent buckets first. Keywords from different intent buckets **never** go in the same cluster. This is non-negotiable per the IRON LAW.

```
Informational:   "email行銷是什麼", "如何做email行銷"
Commercial:      "最好的email行銷工具", "email行銷軟體比較"
Transactional:   "Mailchimp購買", "HubSpot免費試用"
Navigational:    "Mailchimp登入"
```

### Pass 2 — Topic Affinity Within Intent

Within each intent bucket, group by **root topic + modifier pattern**:

```
Root: email行銷自動化
  Modifiers (cluster together): 工具, 軟體, 平台, 系統
  → One cluster: "email行銷自動化工具" page

Root: email行銷策略
  Modifiers (cluster together): 技巧, 方法, 步驟
  → One cluster: "email行銷策略" page
```

Decision rule: if removing the modifier from two keywords leaves the same root concept, they likely cluster together.

---

## Pillar vs. Cluster Page Decision

After clustering, decide the page hierarchy:

```
Cluster size × average monthly search volume → Page type

High volume head term   + 3+ supporting long-tails  → Pillar page (2000–4000 words)
Medium volume           + 1–2 supporting long-tails → Cluster page (1000–2000 words)
Low volume long-tail    + 0 supporting terms        → Thin post or FAQ section
```

**Do not** make every cluster a pillar. Pillar pages require substantial depth. Forcing thin content into 3000 words introduces fluff.

---

## Cluster-to-Content-Brief Mapping

Each cluster produces exactly one content brief. The mapping:

```
Primary keyword   → highest search volume term in cluster
Secondary keywords → remaining cluster members (use naturally in body/subheadings)
Title tag         → primary keyword front-loaded
H2 structure      → driven by SERP subtopics, not by secondary keywords
```

Avoid stuffing secondary keywords into subheadings mechanically. Their presence in the cluster means they'll appear naturally if the content covers the topic properly.

---

## Cannibalization Detection

Run this check before publishing any new cluster page:

1. Google search: `site:yourdomain.com "primary keyword"`
2. Also check: `site:yourdomain.com "secondary keyword1"` for each secondary

If existing pages appear → you have a pre-existing cluster. Options:

| Existing page status | Action |
|---------------------|--------|
| Ranks in top 5 | Expand and update existing page; do NOT create new one |
| Ranks 6–20 | Consolidate new content into existing page; 301 if needed |
| Not ranking at all | Decide: rewrite existing page, or 301 it to the new one |
| Thin / outdated | Merge all content into one authoritative page |

Creating a second page when one already exists will split link equity and anchor signals between two competitors — both will rank lower than one strong page would.

---

## Tooling Options

| Method | Accuracy | Cost | When to use |
|--------|----------|------|-------------|
| SERP overlap (manual) | High | Free, slow | ≤ 50 keywords |
| Ahrefs / SEMrush cluster view | High | Paid | ≥ 50 keywords |
| Vector similarity (embeddings) | Medium | Low | When SERP data unavailable |
| Keyword modifier pattern (manual) | Low–Medium | Free | Quick first-pass triage |

Vector/embedding clustering (grouping by semantic distance) is a useful first pass but will merge keywords that Google treats as separate intents. Always validate embedding clusters with at least a spot-check SERP overlap check on borderline pairs.

---

## Common Mistakes

**Clustering by root word only** — "SEO工具" and "SEO是什麼" share the root "SEO" but have opposite intents. Intent split must come before topic affinity.

**Ignoring search volume during clustering** — clusters with total volume < 100/month usually don't justify a standalone page. Merge into a FAQ section of a related pillar instead.

**Over-clustering** — forcing 30 keywords onto one page to maximize coverage. If a page needs to cover 30 subtopics equally, it covers none of them well. Cap clusters at ~10 keywords for a single page.

**Under-clustering** — one keyword per page for a new site. New sites can't rank for anything with KD > 50. Cluster 3–5 long-tail variants together to build topical relevance before targeting head terms.

**Re-clustering too early** — don't re-run clustering after publishing until you have 3+ months of ranking data. Premature reshuffling wastes crawl budget and resets any authority the page has built.
