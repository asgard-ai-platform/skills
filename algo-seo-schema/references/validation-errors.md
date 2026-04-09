# Structured Data Validation Errors — Diagnosis & Fix

This document covers the validation errors that appear in Google Rich Results Test and Google Search Console's **Enhancements** reports. Each error is classified by severity, root cause, and fix procedure.

---

## Severity Classification

| Level | Label | Meaning | Impact |
|-------|-------|---------|--------|
| 🔴 | **Error** | Required field missing or malformed | Schema ignored entirely |
| 🟡 | **Warning** | Recommended field missing | Rich result eligible but degraded |
| ⚪ | **Info** | Best-practice suggestion | No eligibility impact |

Fix all Errors first. Warnings matter only after zero Errors.

---

## Error Catalogue

### E-01 — Missing required property

**Message:** `Missing field "X"`

**Trigger:** A field that Google marks as required for the given `@type` is absent.

**Example (broken):**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "USB-C Hub"
}
```

Google requires `offers` for Product rich results. The schema above is valid Schema.org but Google will not render a rich result.

**Fix:** Add the missing field with visible page content.
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "USB-C Hub",
  "offers": {
    "@type": "Offer",
    "price": "899",
    "priceCurrency": "TWD",
    "availability": "https://schema.org/InStock"
  }
}
```

**Per-type required fields quick reference:**

| @type | Required by Google (not just Schema.org) |
|-------|------------------------------------------|
| Product | `name`, `offers` (with `price` + `priceCurrency`) |
| FAQPage | `mainEntity` array, each item: `name`, `acceptedAnswer.text` |
| Article | `headline`, `author.name`, `datePublished` |
| NewsArticle | `headline`, `author.name`, `datePublished`, `image` |
| BreadcrumbList | Each `ListItem`: `item`, `name`, `position` |
| HowTo | `name`, `step` array, each step: `text` |
| Event | `name`, `startDate`, `location` |
| Recipe | `name`, `image`, `author`, `datePublished`, `description` |
| JobPosting | `title`, `description`, `datePosted`, `hiringOrganization`, `jobLocation` |

---

### E-02 — Invalid value type

**Message:** `Invalid value type for field "X"` or `Expected type URL, got Text`

**Trigger:** A property expects a specific value type (URL, Date, Number, Boolean) but receives a plain string or wrong format.

**Example (broken):**
```json
{
  "@type": "Event",
  "startDate": "下個週五",
  "endDate": "evening"
}
```

**Fix:** Use ISO 8601 for all date/time fields.
```json
{
  "@type": "Event",
  "startDate": "2026-04-17T19:00:00+08:00",
  "endDate": "2026-04-17T22:00:00+08:00"
}
```

**Common type mismatches:**

| Property | Wrong | Correct |
|----------|-------|---------|
| `price` | `"NT$899"` | `"899"` (numeric string, no currency symbol) |
| `priceCurrency` | `"NT$"` | `"TWD"` (ISO 4217 code) |
| `image` | `"product.jpg"` | `"https://example.com/product.jpg"` (absolute URL) |
| `datePublished` | `"April 2026"` | `"2026-04-09"` or `"2026-04-09T10:00:00+08:00"` |
| `author` | `"Chris Yuan"` | `{"@type": "Person", "name": "Chris Yuan"}` |
| `availability` | `"InStock"` | `"https://schema.org/InStock"` (full URL enum) |
| `ratingValue` | `"five stars"` | `"4.8"` |

---

### E-03 — Content mismatch (IRON LAW violation)

**Message:** `Structured data is not representative of the visible content`

**Trigger:** A property value does not match what is visible on the page. This is the most serious error — it can result in a manual action (penalty) rather than just a rich result being suppressed.

**Example (broken):**
```json
{
  "@type": "Product",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "1200"
  }
}
```
...but the page visibly shows "4.2 stars, 38 reviews".

**Fix:** The JSON-LD values must literally match what a user can read on the page. If the rating is dynamic (loaded via JavaScript), either:
1. Server-side render the rating into the JSON-LD, or
2. Inject the JSON-LD after the JS has resolved the rating.

There is no acceptable workaround that involves mismatched values.

---

### E-04 — Broken nesting

**Message:** `Either "offers", "review" or "aggregateRating" should be specified` (Product) or similar type-context errors

**Trigger:** A nested object is missing its `@type`, or is placed at the wrong level of nesting.

**Example (broken):**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "offers": {
    "price": "299",
    "priceCurrency": "TWD"
  }
}
```

`offers` is an object without `@type: "Offer"`. Google's parser may reject it.

**Fix:** Every nested entity needs its own `@type`.
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "offers": {
    "@type": "Offer",
    "price": "299",
    "priceCurrency": "TWD"
  }
}
```

**Common nesting patterns that must all include `@type`:**

```
Product
  └── offers → Offer
        └── seller → Organization
              └── address → PostalAddress
  └── aggregateRating → AggregateRating
  └── review[] → Review
        └── author → Person
        └── reviewRating → Rating
```

---

### E-05 — JSON syntax error

**Message:** `JSON parse error` or `Unparseable structured data`

**Trigger:** The JSON-LD block contains malformed JSON: trailing commas, unescaped characters, mismatched brackets.

**Diagnosis:** Paste the raw content of the `<script>` tag into [jsonlint.com](https://jsonlint.com) before running Google Rich Results Test. JSON errors prevent all other validation from running.

**Common sources:**

| Mistake | Example | Fix |
|---------|---------|-----|
| Trailing comma | `"name": "X",}` | Remove trailing comma |
| Unescaped quotes | `"description": "He said "hello""` | Escape: `\"hello\"` |
| HTML entities in JSON | `"price": "NT&amp;$899"` | Use plain text, not HTML-encoded values |
| Template variable not replaced | `"name": "{{product_name}}"` | Ensure template engine ran before serving |
| Multi-line string | `"description": "line1\nline2"` | Use `\n` escape, not actual newline |

---

### E-06 — Duplicate `@context`

**Message:** Usually silent failure, but schema may be partially ignored.

**Trigger:** Multiple JSON-LD blocks each declare `"@context": "https://schema.org"`, which is correct. The error occurs when schemas are **merged into one object** incorrectly:

```json
{
  "@context": "https://schema.org",
  "@context": "https://schema.org",
  "@type": "FAQPage"
}
```

This is invalid JSON (duplicate key). Some parsers take the last value; others reject it.

**Fix for multiple schemas on one page:** Use a JSON array or separate `<script>` blocks.

```html
<!-- Option 1: JSON array in one block -->
<script type="application/ld+json">
[
  {"@context": "https://schema.org", "@type": "BreadcrumbList", ...},
  {"@context": "https://schema.org", "@type": "FAQPage", ...}
]
</script>

<!-- Option 2: separate blocks -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "BreadcrumbList", ...}</script>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", ...}</script>
```

Both options are valid. Option 2 is easier to manage in CMS templates.

---

### E-07 — Image URL issues

**Message:** `The value provided for image must be a valid URL` or `Image not accessible`

**Trigger:** Image URLs are relative, use HTTP instead of HTTPS, or return a non-200 status code when Googlebot fetches them.

**Checklist:**
- [ ] URL is absolute (starts with `https://`)
- [ ] URL resolves publicly (not behind login, not 404)
- [ ] Image meets minimum size: **50×50px** minimum; **1200×630px** recommended for Article/NewsArticle
- [ ] File format is JPEG, PNG, GIF, BMP, SVG, or WebP
- [ ] `Content-Type` response header matches image type

**Fix pattern:**
```json
{
  "@type": "Article",
  "image": [
    "https://example.com/images/article-1200x630.jpg",
    "https://example.com/images/article-square.jpg"
  ]
}
```

Providing multiple image URLs (array) lets Google choose the best fit for the search result format.

---

### E-08 — FAQPage over-count or truncation

**Message:** No explicit error, but FAQ rich result shows fewer questions than markup.

**Trigger:** Google displays at most **2 FAQ entries** in desktop rich results. More entries are valid Schema.org but won't all be shown. This is not a validation error — it is a display limit.

**Separate issue:** If an FAQ answer contains HTML tags, they will be stripped in rich results. Write plain text in `acceptedAnswer.text`.

```json
{
  "@type": "Question",
  "name": "What is the return policy?",
  "acceptedAnswer": {
    "@type": "Answer",
    "text": "We accept returns within 30 days. Items must be unused and in original packaging."
  }
}
```

Do NOT write:
```json
"text": "<p>We accept returns within <strong>30 days</strong>.</p>"
```

Google will display the raw HTML tags as literal characters.

---

### E-09 — BreadcrumbList position gaps

**Message:** `Missing field "position"` or breadcrumb renders incorrectly

**Trigger:** `position` values are not sequential integers starting at 1, or there are gaps.

**Broken:**
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com"},
    {"@type": "ListItem", "position": 3, "name": "Products", "item": "https://example.com/products"},
    {"@type": "ListItem", "position": 5, "name": "USB-C Hub", "item": "https://example.com/products/usb-c-hub"}
  ]
}
```

**Fix:** Position must be `1, 2, 3, ...` with no gaps.

The last item in a breadcrumb does not need an `item` URL (it represents the current page), but including it is harmless.

---

### E-10 — priceValidUntil expired

**Message:** Warning: `The offer is expired` or product snippet shows strikethrough price.

**Trigger:** `priceValidUntil` date is in the past. Google may demote or suppress the Product rich result.

```json
{
  "@type": "Offer",
  "price": "299",
  "priceCurrency": "TWD",
  "priceValidUntil": "2025-12-31"
}
```

**Fix:** Either update the date or remove the field if there is no expiry. If price is always current (no sale end date), omit `priceValidUntil` entirely.

---

## Diagnostic Workflow

```
1. Paste page URL into Google Rich Results Test
   → If "JSON parse error": fix JSON syntax first (use jsonlint.com)
   → Otherwise: proceed

2. Collect all 🔴 Errors
   → Cross-reference error messages with E-01 through E-10 above
   → Fix in order: nesting (E-04) before required fields (E-01),
     because bad nesting can cause false "missing field" errors

3. Re-test after each fix group
   → Do not batch-fix all errors and test once;
     one fix may reveal a previously hidden error

4. When zero Errors: collect 🟡 Warnings
   → Prioritize warnings that correspond to visible content you can add
   → Ignore warnings for fields that genuinely don't apply (e.g., no review data)

5. Submit URL for indexing via Google Search Console
   → Rich result eligibility begins at next crawl, not at test-pass time
```

---

## Search Console vs Rich Results Test — Differences

| Dimension | Rich Results Test | Search Console Enhancements |
|-----------|------------------|----------------------------|
| Input | Single URL on demand | All indexed URLs, crawled over time |
| Timing | Instant | Days to weeks lag after deploy |
| Scope | Current live page | Google's last crawled version |
| Use for | Development iteration | Production monitoring |

If Rich Results Test shows zero errors but Search Console still shows errors: the indexed version of the page may be older than your deployed fix. Use "Request indexing" in Search Console to accelerate recrawl.

---

## Errors That Are NOT Validation Errors

These appear in Search Console but are not fixable via schema changes:

| Message | Actual Cause |
|---------|--------------|
| "Page is not eligible for rich results" | Schema is valid, but page-level quality signals are too low |
| "Rich result type not supported for this URL" | URL is blocked by robots.txt or noindex |
| "Property value exceeds character limit" | Description or text field over Google's display limit (not a spec limit) |
| "Unparseable structured data" after deploy | CDN cached old HTML; purge cache |
