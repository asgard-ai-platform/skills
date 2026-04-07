---
name: "algo-seo-schema"
description: "Implement Schema.org structured data markup in JSON-LD format for enhanced search results. Use this skill when the user needs to add rich snippets to web pages, implement FAQ/Product/Article schema, or validate structured data — even if they say 'rich snippets', 'structured data', or 'Google rich results'."
metadata:
  category: "WP-35 SEO 演算法"
  tags: ["seo", "schema-org", "json-ld", "structured-data"]
---

# Schema.org Structured Data

## Overview

Schema.org structured data provides machine-readable page context to search engines via JSON-LD. Enables rich results (stars, FAQs, breadcrumbs, product cards) in SERPs. Implementation is O(1) per page — it's a markup task, not computational.

## When to Use

**Trigger conditions:**
- Adding rich snippet eligibility to web pages
- Implementing product, article, FAQ, HowTo, or event markup
- Debugging Google Search Console structured data errors

**When NOT to use:**
- When optimizing page content or keywords (use content SEO)
- When improving page speed (use Core Web Vitals optimization)

## Algorithm

```
IRON LAW: Schema Markup Must MATCH Visible Content
Marking up content that users can't see violates Google guidelines
and risks manual penalties. Every structured data field must
correspond to content visible on the page.
```

### Phase 1: Input Validation
Identify page type (Article, Product, FAQ, HowTo, Event, etc.). Map visible content to required and recommended schema properties.
**Gate:** Page type identified, all required properties have visible content.

### Phase 2: Core Algorithm
1. Select the correct Schema.org type from the vocabulary
2. Map page content to schema properties (name, description, image, etc.)
3. Build JSON-LD object with @context and @type
4. Handle nested types (e.g., Product contains Offer contains Price)
5. Place JSON-LD in `<script type="application/ld+json">` in `<head>`

### Phase 3: Verification
Validate with Google Rich Results Test. Check: no errors, all required fields present, no mismatch with visible content.
**Gate:** Passes Google Rich Results Test with zero errors.

### Phase 4: Output
Return complete JSON-LD markup ready for insertion.

## Output Format

```json
{
  "schema": {"@context": "https://schema.org", "@type": "Product", "name": "...", "offers": {"@type": "Offer", "price": "29.99", "priceCurrency": "TWD"}},
  "validation": {"errors": 0, "warnings": 1, "eligible_rich_results": ["Product snippet"]}
}
```

## Examples

### Sample I/O
**Input:** FAQ page with 3 questions and answers
**Expected:** FAQPage schema with 3 Question/Answer pairs in JSON-LD

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Page with no clear type | Use WebPage as fallback | Most generic valid type |
| Multiple schemas needed | Array of JSON-LD objects | One page can have multiple types |
| Missing required field | Error, do not generate | Incomplete schema hurts more than none |

## Gotchas

- **Required vs recommended**: Google requires certain fields per type. Missing required fields = schema ignored entirely. Check documentation per type.
- **Nesting depth**: Deeply nested schemas (Product > Offer > Seller > Address) are error-prone. Validate each nesting level.
- **Schema spam**: Adding schema for content not on the page (fake reviews, unavailable prices) triggers manual actions.
- **Type specificity**: Use the most specific type available. "Article" is better than "WebPage"; "NewsArticle" is better than "Article" for news content.
- **Testing gap**: Google Rich Results Test shows what Google sees, but not all valid schema triggers rich results. Eligibility ≠ guarantee of display.

## References

- For complete property reference by type, see `references/type-properties.md`
- For common validation errors and fixes, see `references/validation-errors.md`
