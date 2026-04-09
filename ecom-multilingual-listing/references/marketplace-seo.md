# Marketplace SEO: Platform-Specific Rules for Multilingual Listings

Each marketplace runs a distinct ranking algorithm. Keyword placement that boosts rankings on Amazon A9 may be irrelevant on Shopee or penalized on Rakuten. This document provides platform-specific rules for the five marketplaces most relevant to multilingual sellers: Amazon, Shopee, Lazada, Rakuten, and Yahoo! Shopping Japan.

---

## Amazon A9 / A10 (US, UK, DE, JP, etc.)

### How A9 Ranks Listings

A9 combines two signals:

1. **Relevance** — does the listing match the query?
2. **Performance** — does the listing convert when it matches?

Relevance is determined by keyword indexing. Performance is driven by CTR and conversion rate. A listing that ranks high but doesn't sell gets demoted.

### Keyword Indexing Rules

Amazon indexes keywords from these fields, in approximate priority order:

| Field | Max Length | Indexed? | Notes |
|-------|-----------|----------|-------|
| Title | 200 bytes (most categories) | Yes, high weight | Repeat once max |
| Bullet points (×5) | 500 chars each | Yes | Each bullet is indexed independently |
| Product description | 2,000 chars | Yes, lower weight | Ignored if A+ Content is present |
| Backend search terms | 250 bytes total | Yes, no weight decay | No commas; spaces as delimiters |
| Brand, manufacturer | — | Yes | Useful for brand name variants |

**Key rule**: Amazon deduplicates keywords across fields. A keyword in the title does NOT need to appear again in bullets or backend — it only needs to appear once total to be indexed.

### Title Formula (Amazon)

```
[Primary Keyword] + [Brand] + [Key Feature 1] + [Key Feature 2] + [Size/Variant] + [Use Case]
```

Example (US market, leather wallet):
```
Premium RFID Blocking Bifold Wallet for Men — Slim Genuine Leather, Minimalist Design, Gift Box Included
```

Character budget discipline:
- Desktop: first ~80 chars visible in search results
- Mobile: first ~55 chars visible
- Front-load the primary keyword and one differentiator within 55 chars

### Backend Search Terms (250-byte budget)

Rules that differ from common myths:
- **No commas** — space-separated only
- **No repeated keywords** — already indexed elsewhere, wastes budget
- **Include misspellings** — Amazon does NOT auto-correct in backend
- **Include synonyms and regional variants** — "trainers" for UK listings, "sneakers" for US
- **Do NOT include**: your brand name, competitor brand names, ASINs, profanity, temporary claims ("bestseller")

Example (250 bytes, men's wallet, US):
```
mens wallet slim card holder money clip travel wallet vegan leather wallet brown black bifold trifold card case gift for him husband dad boyfriend
```

Count: 145 chars — leaves room for category-specific synonyms.

### Localization Delta: Amazon JP vs Amazon US

Amazon Japan (amazon.co.jp) runs A9 but with different weighting:

| Element | Amazon US | Amazon JP |
|---------|-----------|-----------|
| Title length | Up to 200 bytes | Up to 100 bytes (stricter enforcement) |
| Bullet points | Benefit-focused | Spec-focused — dimensions, materials, certifications first |
| Backend keywords | English misspellings important | Katakana/Hiragana alternates critical (e.g., 財布 + さいふ + サイフ) |
| Search behavior | Natural language queries | Short noun queries dominate |
| Trust signals in title | Not necessary | JIS certification marks, PSE marks worth including |

**Japanese-specific indexing**: Amazon JP indexes kanji, hiragana, katakana, and romaji separately. A search for `財布` does not automatically match `さいふ` — you must include all script forms in either title, bullets, or backend.

---

## Shopee (SEA: SG, MY, TH, ID, PH, VN, TW)

### How Shopee's Algorithm Works

Shopee uses a **recency-weighted relevance** model. Fresh listings and recently active listings rank higher than stale ones, even if the stale listing has better sales history. This means listing optimization is not one-time.

Ranking factors (approximate importance):
1. Keyword match (title + description)
2. Listing freshness (last edited, last sold)
3. Shop rating and response rate
4. Sales velocity (last 30 days, not lifetime)
5. Paid boost (Shopee Ads — separate from organic)

### Title Rules

Shopee title limit: **120 characters**

Formula:
```
[Product Category Keyword] + [Brand/Model] + [Key Feature] + [Variant] + [Benefit]
```

Shopee-specific practices that differ from Amazon:
- **Keyword stuffing is common and accepted** — "Men Wallet Slim Leather Card Holder Bifold Money Clip" is a normal Shopee title
- Repeat the product category keyword in local language AND English where bilingual markets (SG, MY, PH) are common
- Capitalization of every major word is the marketplace convention — matching it increases perceived legitimacy

### Description: Shopee Indexes the Full Description

Unlike Amazon (where description weight is low), Shopee's search indexes the full description with meaningful weight. Minimum viable description for SEO:

1. First 200 chars: primary keyword + 2 secondary keywords, in natural language
2. Spec block: dimensions, materials, compatibility — in a scannable list
3. Keywords block at end: a comma-separated keyword list (common practice, not penalized)

Example structure (in Bahasa Malaysia for MY market):
```
Dompet lelaki kulit tulen slim kad holder RFID blocking. Sesuai untuk kegunaan harian...

Spesifikasi:
- Saiz: 11cm × 9cm
- Bahan: Kulit lembu tulen
- Warna: Hitam, Coklat
- Kapasiti: 8 kad + 2 slot wang

Kata kunci: dompet lelaki, dompet kulit, dompet slim, card holder, dompet RFID, hadiah untuk lelaki
```

### Market-Specific Title Variants

| Market | Title Pattern | Primary Language |
|--------|-------------|-----------------|
| Shopee SG | EN title, add key Mandarin term if relevant | English |
| Shopee MY | Mix EN + BM, BM category term + EN brand | Bahasa Malaysia |
| Shopee TH | Thai title mandatory; romaji/EN in parentheses acceptable | Thai |
| Shopee ID | Indonesian title; English brand names retained | Indonesian |
| Shopee TW | Traditional Chinese; Japanese brand names in katakana retained | Traditional Chinese |

---

## Lazada (SEA: SG, MY, TH, ID, PH, VN)

### Lazada vs Shopee SEO Differences

Lazada's algorithm is more similar to a traditional search engine — it weights **title keyword density** less and **listing completeness** more.

Key Lazada-specific factors:
- **Category attributes** — Lazada has mandatory and optional attribute fields per category. Filling all attributes (material, color, size, style) contributes to ranking. Amazon calls these "product facts"; Lazada calls them "attributes." Missing attributes = ranking penalty.
- **Image count** — minimum 3 images recommended; 8 images is Lazada's stated optimum
- **Seller metrics** — chat response rate < 12 hours has documented ranking impact (Lazada discloses this)

### Attribute Completion Checklist

Before publishing a Lazada listing, verify:
- [ ] All mandatory attributes filled (marked with * in Lazada Seller Center)
- [ ] Minimum 5 optional attributes filled
- [ ] Primary category correctly selected (recategorization after indexing delays ranking)
- [ ] At least 1 certification attribute if product category requires it (electronics, health products)

---

## Rakuten Ichiba (Japan)

### Fundamental Difference from Western Marketplaces

Rakuten is a **mall model**, not a pure marketplace. Shop design, HTML in descriptions, and brand presentation all affect ranking. It is closer to running a website within a marketplace than listing a product.

### Rakuten Search (Rakuten Market Search Engine)

Ranking factors unique to Rakuten:
1. **Shop rating** (overall satisfaction score) — highest weight of any marketplace
2. **Item catch copy** (キャッチコピー) — a secondary headline field; indexed and displayed
3. **Item name** (商品名) — the primary title; 256 characters
4. **Item explanation** (商品説明文) — full HTML allowed; fully indexed
5. **Search keywords** (検索キーワード) — comma-separated; 256 chars

### Title Structure (Rakuten)

Japanese e-commerce title conventions:

```
【商品カテゴリ】ブランド名 商品名 素材/仕様 サイズ カラー【特典あり】
```

Example:
```
【メンズ財布】PORTER ポーター 二つ折り財布 本革 スリム 薄型 カードケース ブラック【送料無料】
```

Brackets (`【】`) are a Rakuten title convention — they function as visual anchors and help CTR. Do not omit them because they look unusual; they are the market convention.

Character budget:
- Full title displayed: 63 characters in search results (count in full-width characters; each `【】` = 2 chars)
- Front-load category keyword + brand within first 30 chars

### Keyword Script Coverage (Critical for Japanese)

For any Japanese listing, provide keywords in ALL applicable forms:

| Script | Example | When required |
|--------|---------|--------------|
| Kanji | 財布 | Always |
| Hiragana | さいふ | Always |
| Katakana | サイフ | For foreign-origin words and brand names |
| Romaji | saifu | For younger demographic, trending items |
| English | wallet | For imported goods, premium positioning |

A 256-character keyword field for a wallet might look like:
```
財布,さいふ,サイフ,wallet,二つ折り,ふたつおり,折り財布,本革,ほんかわ,レザー,leather,メンズ,men,男性用,プレゼント,ギフト,gift,ポーター,PORTER
```

### Description HTML — Rakuten Specific

Rakuten allows and rewards rich HTML in descriptions. Minimum viable structure:

```html
<h2>商品説明</h2>
<p>本革を使用したスリム二つ折り財布です。...</p>

<h2>商品仕様</h2>
<table>
  <tr><th>素材</th><td>牛革（本革）</td></tr>
  <tr><th>サイズ</th><td>横11cm × 縦9cm × 厚さ1.5cm</td></tr>
  <tr><th>カラー</th><td>ブラック、ネイビー、ブラウン</td></tr>
  <tr><th>収納</th><td>カード8枚、お札、小銭</td></tr>
</table>

<h2>こんな方におすすめ</h2>
<ul>
  <li>薄型財布をお探しの方</li>
  <li>プレゼントをお探しの方</li>
</ul>
```

**Do not use inline styles that break Rakuten's mobile rendering.** Rakuten's mobile app strips some CSS. Use only structural HTML (`<h2>`, `<p>`, `<table>`, `<ul>`, `<strong>`).

---

## Yahoo! Shopping Japan (Yahoo!ショッピング)

Yahoo! Shopping Japan uses a different algorithm from Rakuten despite serving the same market.

Key differences from Rakuten:
- **PayPay integration** — listings with PayPay bonus point campaigns rank higher (platform incentive, not keyword SEO)
- **Review count** — weighted more heavily than Rakuten; a listing with 50 reviews outranks a better-optimized listing with 5
- **Title** — 75 characters; same bracket convention as Rakuten applies
- **Description** — plain text recommended; HTML is allowed but Yahoo's mobile rendering is inconsistent

For Japanese market: if you can only optimize for one platform, optimize for Rakuten first. The structural work (HTML description, keyword coverage across scripts) transfers to Yahoo with minor modifications.

---

## Cross-Platform Keyword Research Workflow

When entering a new language market, research keywords natively — do not translate your existing keywords.

### Step-by-Step: Finding Local Keywords from Scratch

**Step 1: Marketplace search suggest**

Type your product category in the target language in the marketplace search bar and capture autocomplete suggestions. These are real user queries ranked by volume.

For a wallet on Shopee TW:
- 皮夾 → 皮夾男、皮夾女、皮夾推薦、皮夾薄款
- 錢包 → 錢包男、錢包零錢、錢包牛皮
- Note: 皮夾 (Taiwan) ≠ 錢包 (China) — same product, different dominant term by market

**Step 2: Competitor title analysis**

Find the top 5 organic results for your product category. List every keyword they use in titles. Tally frequency.

```
Keyword tally (皮夾, Shopee TW top 10 listings):
皮夾        10/10
男用         8/10
真皮         7/10
薄型         6/10
卡片夾       5/10
RFID        4/10
牛皮         4/10
短夾         3/10
```

Terms appearing in 7+ of 10 top listings are table-stakes keywords — you must include them. Terms appearing in 4-6 are differentiators.

**Step 3: Google Keyword Planner (country-targeted)**

Set location to the target country, language to the target language. Search for the terms identified in Step 1. Extract:
- Monthly search volume
- Competition (Low/Medium/High)
- Related terms the marketplace suggest didn't surface

**Step 4: Prioritize by formula**

```
Keyword Priority Score = (Search Volume / 1000) × (1 / Competition multiplier)

Competition multiplier: Low = 1, Medium = 2, High = 4
```

Example:
| Keyword | Volume | Competition | Score |
|---------|--------|------------|-------|
| 皮夾男 | 8,000 | Medium | 4.0 |
| 真皮皮夾 | 3,500 | Low | 3.5 |
| 薄型皮夾推薦 | 1,200 | Low | 1.2 |
| 皮夾品牌 | 12,000 | High | 3.0 |

Build your title around keywords with scores ≥ 3.0.

---

## Platform Comparison: Quick Reference

| Factor | Amazon | Shopee | Lazada | Rakuten | Yahoo JP |
|--------|--------|--------|--------|---------|---------|
| Title weight | High | High | Medium | High | High |
| Description indexed | Low | High | Medium | High | Medium |
| Backend keyword field | 250 bytes | None | None | 256 chars | None |
| Attribute completion | Medium | Low | High | Low | Medium |
| Freshness/recency | Low | High | Medium | Low | Medium |
| Review weight | Medium | Medium | Medium | High | Very High |
| Listing HTML | No | No | No | Yes (rewarded) | Limited |
| Script variants (JP) | Required (JP) | N/A | N/A | Required | Required |

---

## Common Errors by Platform

**Amazon**: Backend keywords exceed 250 bytes → entire backend field may be ignored by indexer. Measure byte length, not character length (some Unicode chars = 2-3 bytes).

**Shopee**: Editing a listing resets its freshness timer — use this deliberately to re-boost stale listings. Editing simply to update a comma counts.

**Lazada**: Selecting the wrong subcategory causes wrong attribute fields to appear. If you publish before realizing the error, recategorization takes 48-72 hours to re-index.

**Rakuten**: Using `<div>` with class names from external CSS in descriptions — Rakuten strips external CSS; the layout breaks on mobile.

**Yahoo JP**: Assuming Rakuten keyword research transfers directly — Yahoo's search index weights differ. A keyword ranking #3 on Rakuten may rank #20 on Yahoo for the same listing.
