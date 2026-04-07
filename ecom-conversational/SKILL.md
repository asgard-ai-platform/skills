---
name: "ecom-conversational"
description: "Design conversational commerce experiences across messaging platforms including chatbot flows, product cards, and conversion strategies. Use this skill when the user needs to sell through LINE, WhatsApp, Instagram DM, or other messaging channels, design chatbot purchasing flows, or integrate messaging into their sales funnel — even if they say 'sell through LINE', 'build a shopping chatbot', 'customers ask to buy in our DMs', or 'conversational sales strategy'."
metadata:
  category: "WP-01 電商"
  tags: ["e-commerce", "conversational-commerce", "chatbot", "messaging"]
---

# Conversational Commerce

## Framework

```
IRON LAW: Conversation First, Commerce Second

Conversational commerce works because it meets customers WHERE THEY
ALREADY ARE (messaging apps). Forcing a sales pitch into a chat channel
kills trust. The conversation must provide genuine value (answering questions,
solving problems) BEFORE introducing products or purchases.

The sequence: Help → Trust → Recommend → Convert
```

### Platform Comparison (Asia-Pacific Focus)

| Platform | Users (Taiwan) | Commerce Features | Best For |
|----------|---------------|------------------|----------|
| **LINE** | 21M+ (95% penetration) | LINE Shopping, Rich Menu, LIFF, payment | Taiwan, Japan, Thailand primary channel |
| **Instagram DM** | ~10M | Shop tags, quick replies, product stickers | Visual products, younger demographic |
| **Facebook Messenger** | ~18M | Shops integration, automated responses | Broad reach, older demographic |
| **WhatsApp** | Limited in Taiwan | Catalog, cart, payment (select markets) | SEA, India, Brazil |
| **WeChat** | ~1M (Taiwan) | Mini Programs, WeChat Pay | China-connected businesses |

### Conversation Flow Design

**1. Entry Points** — How customers start the conversation
- QR code in store, ad click-to-message, website chat widget, social media link

**2. Welcome Flow** — First 3 messages
- Greet warmly, set expectations, offer navigation options
- Rich menu (LINE) or quick reply buttons — don't ask open-ended questions early

**3. Product Discovery** — Help them find what they need
- Guided questions: "What are you looking for?" → category → product
- Product cards with image, price, and "Buy" button
- AI-powered recommendations based on conversation context

**4. Purchase Flow** — Minimize friction
- In-chat checkout where possible (LINE Pay, in-app payment)
- If redirecting to website, deep-link to the specific product (not homepage)
- Order confirmation message with tracking

**5. Post-Purchase** — Retain and upsell
- Shipping updates via message
- Follow-up: "How's the product?" (7 days after delivery)
- Personalized recommendations based on purchase history

### Chatbot vs Human Handoff

| Scenario | Handle with Bot | Hand off to Human |
|----------|----------------|------------------|
| FAQ (hours, shipping, returns) | ✓ | — |
| Product recommendations (simple) | ✓ | — |
| Complex product questions | — | ✓ |
| Complaints / issues | — | ✓ (immediately) |
| High-value purchases | Bot assists → human closes | ✓ |

**Key metric**: Bot containment rate (% resolved without human) — target 60-70% for mature bots.

## Output Format

```markdown
# Conversational Commerce Plan: {Business}

## Channel Selection
- Primary: {platform} — rationale: {why}
- Entry points: {QR / ad / social / website}

## Conversation Flow
1. Welcome: {message template}
2. Discovery: {question flow}
3. Product Card: {template}
4. Checkout: {in-chat / redirect}
5. Post-purchase: {follow-up sequence}

## Bot vs Human Split
| Scenario | Handler | SLA |
|----------|---------|-----|
| {scenario} | Bot/Human | {response time} |

## KPIs
| Metric | Target |
|--------|--------|
| Response time | < {X} seconds (bot) / < {X} minutes (human) |
| Containment rate | > 60% |
| Conversation-to-purchase rate | > {X%} |
| Customer satisfaction (CSAT) | > 4.0/5 |
```

## Gotchas

- **LINE Official Account tiers matter**: Free tier limits monthly messages. If you exceed, messages are throttled. Budget for premium tier if customer base > 500.
- **Don't over-automate**: A bot that can't understand the question and loops "I didn't understand, please choose from the menu" destroys trust faster than no bot at all. Always offer a human escalation path.
- **Messaging is asynchronous**: Unlike phone calls, customers expect to message and come back later. Design flows that work with interruptions — save cart state, remember context.
- **Privacy in messaging**: Chat history is personal. Don't share conversations internally without consent, and be transparent about data usage.
- **Social commerce is exploding in SEA/Taiwan**: LINE Shopping, Instagram Shopping, TikTok Shop — these blur the line between social and commerce. Treat them as primary channels, not add-ons.

## References

- For LINE Official Account setup, see `references/line-oa-setup.md`
- For chatbot NLU design patterns, see `references/chatbot-design.md`
