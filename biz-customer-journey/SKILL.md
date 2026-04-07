---
name: "biz-customer-journey"
description: "Map and analyze the customer journey across Awareness, Consideration, Decision, Usage, and Advocacy stages. Use this skill when the user needs to understand the customer experience end-to-end, identify drop-off points, optimize touchpoints, or improve conversion — even if they say 'where are we losing customers', 'what's our funnel look like', or 'map the user experience'."
metadata:
  category: "WP-14 商學院—行銷"
  tags: ["marketing", "customer-journey", "experience-design"]
---

# Customer Journey Mapping

## Overview

Customer Journey Mapping visualizes the entire experience a customer has with a brand — from first awareness through post-purchase advocacy. It identifies touchpoints, emotions, pain points, and opportunities at each stage. The goal is to find and fix where customers get stuck, frustrated, or leave.

## When to Use

**Trigger conditions:**
- User wants to improve conversion rates across the funnel
- User needs to understand where customers drop off
- User designing or redesigning a customer experience
- User asks "where are we losing customers?" or "what's the user experience like?"

**When NOT to use:**
- For market segmentation → use STP
- For product feature decisions → use Jobs to Be Done
- For one-time strategic analysis → use SWOT

## Framework

```
IRON LAW: Map the Customer's Reality, Not Your Ideal

The journey map must reflect what customers ACTUALLY experience, not what
you designed or intended. If customers Google your brand and find negative
reviews (reality), don't map "customer visits our website" (ideal).

Base the map on data: analytics, customer interviews, support tickets,
heatmaps — not internal assumptions.
```

```
IRON LAW: Every Touchpoint Needs an Emotion

A journey map without emotions is a process diagram. At every touchpoint,
note the customer's emotional state: confident, confused, frustrated,
delighted. Emotions predict behavior better than process steps.
```

### The Five Stages

**1. Awareness** — Customer realizes they have a need or discovers your brand
- Touchpoints: ads, social media, word-of-mouth, search results, content
- Key question: "How do they first encounter us?"

**2. Consideration** — Customer evaluates options and compares alternatives
- Touchpoints: website, reviews, comparisons, demos, sales conversations
- Key question: "What information do they seek and where?"

**3. Decision** — Customer chooses and purchases
- Touchpoints: checkout, pricing page, sales closing, contract signing
- Key question: "What friction exists at the purchase moment?"

**4. Usage** — Customer uses the product/service
- Touchpoints: onboarding, product interaction, support, documentation
- Key question: "Does the experience match the promise?"

**5. Advocacy** — Customer recommends (or warns against) the brand
- Touchpoints: reviews, referrals, social sharing, community
- Key question: "What triggers them to recommend us — or not?"

### Step 1: Define the Persona

Who is this journey for? Use the target segment from STP:
- Name, demographics, goals, pain points
- The more specific the persona, the more actionable the map

### Step 2: Map Touchpoints per Stage

For each stage, list:
- **Touchpoints**: Every interaction point (physical, digital, human)
- **Actions**: What the customer does
- **Emotions**: How the customer feels (😊 positive / 😐 neutral / 😤 negative)
- **Pain points**: What frustrates or blocks them
- **Opportunities**: How to improve the experience

### Step 3: Identify Moments of Truth

Find the 2-3 critical moments that disproportionately impact the overall experience:
- **First impression**: The first touchpoint sets expectations
- **Friction peak**: The highest-pain-point moment
- **Delight opportunity**: Where a small improvement creates outsized positive impact

### Step 4: Prioritize Improvements

Rank improvements by: Impact on customer satisfaction × Feasibility × Cost. Fix the highest-impact pain points first.

## Output Format

```markdown
# Customer Journey Map: {Product/Service}

## Persona
- Name: {persona name}
- Profile: {segment description}
- Goal: {what they're trying to achieve}

## Journey Map

| Stage | Touchpoints | Actions | Emotion | Pain Points | Opportunities |
|-------|------------|---------|---------|-------------|---------------|
| Awareness | {list} | {what they do} | 😊/😐/😤 | {friction} | {improvement} |
| Consideration | ... | ... | ... | ... | ... |
| Decision | ... | ... | ... | ... | ... |
| Usage | ... | ... | ... | ... | ... |
| Advocacy | ... | ... | ... | ... | ... |

## Moments of Truth
1. **{moment}** — {why this is critical}
2. **{moment}** — {why this is critical}

## Priority Improvements
1. {Stage} → {specific improvement} — Impact: High, Effort: Low
2. ...
```

## Examples

### Correct Application

**Scenario:** Journey for a Taiwanese food delivery app (persona: 30-year-old office worker ordering lunch)

| Stage | Touchpoints | Emotion | Pain Point |
|-------|------------|---------|------------|
| Awareness | Colleague mentions app during lunch discussion | 😊 Curious | None — organic discovery |
| Consideration | Downloads app, browses restaurants, reads reviews | 😐 → 😤 | Too many choices, no "nearby + fast" filter |
| Decision | Selects restaurant, adds items, sees delivery fee + minimum order | 😤 | Delivery fee NT$60 feels expensive for a NT$120 lunch; minimum order forces buying more than needed |
| Usage | Waits for delivery, receives food, eats | 😊 → 😐 | Food arrives in 35 min (app said 25), packaging leaked |
| Advocacy | Doesn't refer friends | 😐 | No referral incentive; experience was "okay, not great" |

**Moment of Truth**: Decision stage — the delivery fee shock causes 40% cart abandonment (data-backed ✓).

### Incorrect Application

**What went wrong:**
- Map shows "Customer visits website → Customer signs up → Customer makes purchase" → This is a **process flow**, not a journey map. No emotions, no pain points. Violates Iron Law: every touchpoint needs an emotion.
- Awareness stage shows "Customer sees our billboard campaign" when the company doesn't have billboards → Mapping the **ideal**, not reality. Violates Iron Law: map reality.

## Gotchas

- **Backstage vs frontstage**: Customers don't see your internal processes. Map what the customer experiences, not your operations. "Order routed to kitchen" is backstage; "Customer sees 'preparing your order' notification" is frontstage.
- **Multiple personas = multiple maps**: Different segments have different journeys. A B2B enterprise buyer's journey is completely different from a self-serve SMB user. Don't combine them.
- **Post-purchase is often ignored**: Most teams map Awareness → Decision thoroughly but skip Usage and Advocacy. Retention and referral happen post-purchase.
- **Data over intuition**: "We think customers feel frustrated at checkout" is a hypothesis. "Cart abandonment rate is 65% at the delivery fee screen" is evidence. Use data wherever possible.
- **Journey maps expire**: Customer behavior changes. A map from 2023 may be obsolete by 2025. Revisit quarterly for fast-moving products.

## References

- For service blueprint extension (adding backstage operations), see `references/service-blueprint.md`
