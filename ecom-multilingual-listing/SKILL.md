---
name: "ecom-multilingual-listing"
description: "Optimize multilingual product listings for international e-commerce including SEO localization, machine translation workflows, and cultural adaptation. Use this skill when the user needs to create product listings in multiple languages, optimize for local search, or adapt marketing content for different markets — even if they say 'translate our listings', 'optimize for local SEO', 'adapt for the Japanese market', or 'our translated listings don't convert'."
metadata:
  category: "WP-01 電商"
  tags: ["e-commerce", "localization", "seo", "multilingual"]
---

# Multilingual Listing Optimization

## Framework

```
IRON LAW: Localization ≠ Translation

Translating product listings word-for-word produces listings that are
grammatically correct but commercially ineffective. Localization adapts
the message for the TARGET MARKET's search behavior, cultural preferences,
and purchasing psychology.

"機能性飲料" doesn't translate to "functional beverage" for a US audience —
it translates to "energy drink" or "performance drink" because that's
what Americans search for.
```

### Localization Workflow

**Phase 1: Keyword Research (per market)**
- Research LOCAL search terms (not translations of your keywords)
- Tools: Google Keyword Planner (set to target country), Ahrefs, local marketplace search suggest
- Identify: high-volume + low-competition keywords in the target language

**Phase 2: Listing Structure**
| Element | Localization Requirement |
|---------|------------------------|
| **Title** | Include top local keywords, follow platform character limits, front-load important terms |
| **Bullet points** | Highlight benefits that matter to LOCAL consumers (may differ from home market) |
| **Description** | Natural language with local idioms, NOT translated corporate-speak |
| **Images** | Local models/settings, local measurements (cm vs inches), local lifestyle context |
| **Search terms** | Backend keywords in local language, including misspellings and synonyms |

**Phase 3: Cultural Adaptation**
- Color symbolism (red = luck in China, danger in West)
- Sizing (Asian vs Western sizing charts — always provide conversion)
- Trust signals (differs by market: reviews in US, certifications in Japan, influencer endorsements in SEA)
- Pricing display (tax-inclusive vs exclusive varies by market)

**Phase 4: Quality Assurance**
- Native speaker review (not just bilingual — native in TARGET market)
- A/B test title variants for CTR
- Monitor search ranking for target keywords
- Check competitor listings in the target market for conventions

### Translation Quality Tiers

| Tier | Method | Cost | Quality | Use Case |
|------|--------|------|---------|----------|
| Machine translation | AI (GPT, DeepL) | Lowest | Readable but often unnatural | Internal use, draft |
| Machine + human edit | AI draft → native editor | Medium | Good | B-items, high-volume SKUs |
| Professional localization | Human translator with market expertise | Highest | Best | A-items, brand-critical content |
| Transcreation | Creative rewriting for target culture | Premium | Exceptional | Taglines, brand stories, ads |

## Output Format

```markdown
# Listing Localization: {Product} → {Target Market}

## Keyword Research
| Local Keyword | Search Volume | Competition | Priority |
|-------------|-------------|------------|---------|
| {keyword} | {N/month} | H/M/L | 1/2/3 |

## Localized Listing
- **Title**: {optimized for local keywords}
- **Bullet Points**: {adapted for local benefits emphasis}
- **Description**: {localized, natural language}

## Cultural Adaptations
| Element | Home Market | Target Market | Change |
|---------|-----------|-------------|--------|
| {element} | {original} | {adapted} | {why} |

## QA Checklist
- [ ] Native speaker reviewed
- [ ] Keywords included in title/backend
- [ ] Sizing chart converted
- [ ] Images culturally appropriate
```

## Gotchas

- **Google Translate is NOT localization**: It produces grammatically correct but commercially dead listings. "高品質的真皮皮夾" → "High quality genuine leather wallet" is translation. "Premium leather bifold wallet for men — RFID blocking" is localization (targets actual US search terms).
- **Each marketplace has different SEO rules**: Amazon A9, Shopee's algorithm, Rakuten's ranking — keyword placement rules differ. Research platform-specific best practices.
- **Don't translate reviews**: Reviews should come from local customers. Translated reviews look fake and erode trust.
- **Backend keywords matter**: Most marketplaces have hidden keyword fields. Fill them with synonyms, misspellings, and alternate terms in the local language.
- **Japanese market demands perfection**: Japanese consumers expect flawless language, precise specifications, and detailed product descriptions. Machine translation is unacceptable for the Japanese market.

## References

- For platform-specific SEO guides, see `references/marketplace-seo.md`
