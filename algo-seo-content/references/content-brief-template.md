# Content Brief Template

A content brief is the single source of truth for a piece of content. It translates SERP research into concrete writing instructions. A brief that is too vague produces generic content; a brief that is over-specified kills the writer's ability to make judgment calls. The template below is calibrated for that balance.

---

## Canonical Fields

Every brief must include these fields — no exceptions.

| Field | Type | Notes |
|-------|------|-------|
| `primary_keyword` | string | The exact keyword phrase the page targets |
| `intent` | enum | informational / navigational / commercial / transactional |
| `format` | enum | See format decision table below |
| `target_word_count` | integer | Derived from median SERP word count, ±20% |
| `subtopics` | list | Required H2/H3 sections, ordered by SERP importance |
| `title_tag` | string | ≤ 60 chars, primary keyword front-loaded |
| `meta_description` | string | ≤ 155 chars, includes primary keyword, has CTA |
| `internal_links_min` | integer | Minimum number of internal links to include |
| `kd` | integer | Keyword difficulty score (0–100) |
| `search_volume` | integer | Monthly search volume |

Optional fields that matter for some content types:

| Field | When to include |
|-------|-----------------|
| `secondary_keywords` | When 3+ semantically related keywords cluster together |
| `competing_urls` | When defending against a specific competitor URL |
| `freshness_required` | When SERP shows dates in titles (news, annual rankings) |
| `eeat_signals` | When topic is health, finance, legal, or safety |
| `schema_type` | When SERP shows rich results (FAQ, HowTo, Article) |

---

## Format Decision Table

Check the dominant SERP format before choosing. Do not guess.

| SERP Signal | Choose Format |
|-------------|---------------|
| "How to", numbered steps in snippets | `how-to guide` |
| "Best X", "Top 10 X" in titles | `listicle` |
| "X vs Y", comparison tables | `comparison` |
| Definition in featured snippet | `explainer` |
| Mixed — no dominant format | `hub article` |
| Product page, "Buy X" intents | `product page` (out of scope for this skill) |

**Hub article** is a fallback, not a default. Use it only when the query genuinely covers multiple subtopics at overview depth (e.g., "content marketing strategy").

---

## Word Count Derivation

Do not guess word count. Derive it from the SERP.

```
median_word_count = median(word_counts of top 5 ranking URLs)
target_word_count = round(median_word_count / 100) * 100  # round to nearest 100
```

**Worked example:**

Top 5 results for "email行銷自動化":
- Result 1: 3,100 words
- Result 2: 2,600 words
- Result 3: 2,200 words
- Result 4: 4,100 words
- Result 5: 2,400 words

Sorted: 2,200 / 2,400 / **2,600** / 3,100 / 4,100 → median = 2,600

`target_word_count = 2600` (already a round number)

**Do not** add 20% "to be safe." Longer is not better. If your content is 4,000 words targeting a 2,600-word SERP, you will either pad or confuse the reader.

---

## Subtopic Extraction Procedure

1. Open the top 5 ranking URLs for the primary keyword.
2. List every H2 heading from each URL.
3. Mark which headings appear in 3 or more of the 5 results — these are **required subtopics**.
4. Mark headings appearing in 2 results as **recommended subtopics**.
5. Headings unique to one URL are optional signals only.
6. Order required subtopics by their median position across the SERPs (first occurring → first in brief).

**Example output for "email行銷自動化":**

| Subtopic | Frequency (of 5) | Classification |
|----------|-----------------|----------------|
| 什麼是 email 行銷自動化 | 5/5 | Required |
| 常見的自動化工具比較 | 4/5 | Required |
| 如何設定觸發條件 | 4/5 | Required |
| 自動化流程範例 | 3/5 | Required |
| A/B 測試整合 | 2/5 | Recommended |
| 價格與方案說明 | 1/5 | Optional |

---

## Worked Brief: Full Example

**Scenario:** New SaaS blog targeting Taiwan SMBs, targeting "email行銷自動化"

```json
{
  "primary_keyword": "email行銷自動化",
  "secondary_keywords": ["email automation", "行銷自動化工具", "電子報自動化"],
  "intent": "commercial",
  "format": "comparison guide",
  "target_word_count": 2600,
  "subtopics": [
    "什麼是 email 行銷自動化（定義 + 運作原理）",
    "常見工具比較：Mailchimp vs ActiveCampaign vs 本土工具",
    "如何設定自動化觸發條件（歡迎信、棄購追蹤、生日優惠）",
    "自動化流程範例（附流程圖）",
    "A/B 測試整合建議"
  ],
  "title_tag": "email行銷自動化完整指南：2025年工具比較與設定教學",
  "meta_description": "想用 email 行銷自動化提升轉換率？比較 Mailchimp、ActiveCampaign 等主流工具，附觸發條件設定步驟與實際流程範例。",
  "internal_links_min": 4,
  "kd": 38,
  "search_volume": 1900,
  "freshness_required": true,
  "eeat_signals": false,
  "schema_type": "Article",
  "competing_urls": [
    "https://example-competitor.com/email-marketing-automation"
  ],
  "notes": "SERP 前 5 名中有 3 篇包含工具比較表格，必須包含。KD 38 對新站而言可行，但需要至少 3 個外部反向連結才有機會進入前 5。"
}
```

---

## Title Tag Rules

The title tag is the most important on-page signal after the body content.

**Formula:**

```
{Primary Keyword} + {Year or qualifier} + {Hook or benefit}
```

**Enforcement rules:**
- Primary keyword must appear in the first 30 characters
- Total length: 50–60 characters (longer gets truncated in SERP)
- Do not repeat the primary keyword more than once
- Avoid clickbait modifiers that mismatch content (e.g., "ULTIMATE" for a 1,500-word overview)

**Title character count check (Python one-liner):**
```python
assert 50 <= len(title) <= 60, f"Title is {len(title)} chars — adjust"
```

**Bad titles:**
- "2025年最完整的Email行銷自動化工具比較指南教學大全" — 36 Chinese chars, likely truncated
- "讓你的業績翻倍！email 行銷自動化秘訣" — keyword not front-loaded, clickbait

**Good title:**
- "email行銷自動化完整指南：2025年工具比較與設定" — keyword first, year freshness signal, 30 chars

---

## Meta Description Rules

Meta descriptions do not directly affect ranking. They affect click-through rate.

**Formula:**
```
{Pain point or question} + {What the page gives} + {CTA or differentiator}
```

**Constraint:** 145–155 characters. Under 130 looks sparse. Over 155 gets cut mid-sentence.

**Bad:**
- "本文介紹了 email 行銷自動化的各種工具和設定方法，歡迎閱讀。" — no CTA, no differentiation

**Good:**
- "想用 email 行銷自動化提升轉換率？比較 5 款主流工具，附觸發條件設定步驟與範例流程圖。" — specific benefit, has deliverables

---

## H2 Structure Rules

H2s are the skeleton. They must:
1. Contain or paraphrase the subtopic keyword (but do not keyword-stuff)
2. Be written as the reader would phrase their question
3. Be ordered from broad → specific, or problem → solution

**Do not** write H2s in abstract noun form:
- Bad: `## 自動化的效益` (abstract)
- Good: `## email 行銷自動化能帶來哪些效益？` (question form matches user query style)

**H3 nesting rule:** Only nest H3 under an H2 when there are 2+ sub-items. A single H3 under an H2 is a structural mistake — promote it or merge it.

---

## Internal Links Minimum

The `internal_links_min` field sets a floor, not a target.

**Derivation heuristic:**
```
internal_links_min = max(3, floor(target_word_count / 600))
```

For 2,600 words: `max(3, floor(2600 / 600)) = max(3, 4) = 4`

Each internal link must go to a semantically related page — not the homepage, not a category archive. If you cannot identify 4 relevant internal link targets, the site's content library is too thin to support this page's ranking (a signal to build prerequisite content first).

---

## E-E-A-T Signals Field

Only populate this field for YMYL topics (health, finance, legal, safety). When present, the brief must specify:

```json
"eeat_signals": {
  "author_bio": "must include credentials (e.g., certified financial planner)",
  "citations": "minimum 3 cited external sources (.gov, peer-reviewed, or industry authority)",
  "last_updated": "must show publish + last updated date",
  "review_required": true
}
```

For non-YMYL topics, set `"eeat_signals": false` to explicitly acknowledge the check was done.

---

## Freshness Flag

Set `"freshness_required": true` when any of the following are true:
- Query contains a year ("best laptop 2025")
- Top 5 SERP results show publication dates within 12 months
- Topic is tied to changing data (pricing, rankings, regulations)

When `freshness_required` is true, the brief must include:
- A year in the title tag
- A "last updated" timestamp in the page template
- A calendar reminder to review the content in 10–12 months

---

## Schema Type Selection

| Content Format | Schema Type |
|----------------|-------------|
| how-to guide | `HowTo` |
| listicle | `ItemList` |
| comparison guide | `Article` |
| FAQ page | `FAQPage` |
| explainer | `Article` |
| hub article | `Article` |

Use `HowTo` schema only if the content has discrete, numbered steps with a clear end result. Do not use `HowTo` for general guides that happen to have a numbered outline.

---

## Brief Quality Checklist

Before handing a brief to a writer (or using it as an agent prompt), verify:

- [ ] Primary keyword confirmed from SERP volume data (not guessed)
- [ ] Intent field matches dominant SERP result type
- [ ] Word count derived from SERP median, not assumed
- [ ] All "Required" subtopics (3+ SERP frequency) are present
- [ ] Title tag is 50–60 characters and keyword-front-loaded
- [ ] Meta description is 145–155 characters
- [ ] `internal_links_min` is ≥ 3 and reachable from existing content
- [ ] `freshness_required` is explicitly set (true or false)
- [ ] `eeat_signals` is explicitly set (object or false)
- [ ] `schema_type` is specified

A brief that passes all 10 checks is ready to execute. A brief missing any check has at least one decision deferred to the writer — which introduces inconsistency.
