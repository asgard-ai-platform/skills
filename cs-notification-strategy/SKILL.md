---
name: "cs-notification-strategy"
description: "Design push notification and messaging strategies including channel selection, timing optimization, personalization, and fatigue management. Use this skill when the user needs to improve notification engagement, reduce opt-out rates, plan multi-channel messaging, or A/B test notification content — even if they say 'our push open rates are low', 'users are unsubscribing', 'when should we send notifications', or 'which channel to use for alerts'."
metadata:
  category: "WP-06 Agent通訊+客服"
  tags: ["notification", "push", "engagement", "retention"]
---

# Notification Strategy

## Framework

```
IRON LAW: Every Notification Must Earn Its Send

Each notification interrupts the user. If it doesn't deliver clear value
to the RECIPIENT (not to your business), it erodes trust and drives
opt-outs. Before sending: "Would the user thank me for this notification?"
If no → don't send.
```

### Channel Comparison

| Channel | Open Rate | Speed | Cost | Best For | Limitations |
|---------|----------|-------|------|----------|-------------|
| **Push notification** | 5-15% | Instant | Free | Time-sensitive, action-needed | Easy to opt out, limited text |
| **Email** | 15-25% | Minutes | Low | Detailed content, receipts, newsletters | Spam filters, slow |
| **SMS** | 90%+ open | Instant | $$$ | Critical alerts, OTP, urgent | Expensive, intrusive, regulatory |
| **In-app** | 25-40% | Next session | Free | Feature announcements, tips | Only reaches active users |
| **LINE/Messenger** | 40-60% | Instant | Free-$ | Conversational, Taiwan/Asia | Platform dependency |

### Timing Optimization

| Audience | Best Time | Worst Time |
|----------|----------|-----------|
| B2C general | 10-12 AM, 7-9 PM | 12-6 AM, during commute |
| B2B | Tue-Thu 9-11 AM | Weekends, Friday PM |
| E-commerce | Thu-Sat (pre-weekend shopping) | Monday AM |
| Breaking/urgent | Immediately | N/A |

**Timezone rule**: Send in the RECIPIENT's timezone, not yours.

### Personalization Tiers

| Tier | What | Example | Lift vs Generic |
|------|------|---------|----------------|
| **None** | Same message to all | "Check out our sale!" | Baseline |
| **Segment** | By user group | "As a premium member, you get early access" | +20-30% |
| **Behavioral** | Based on past actions | "The item in your cart is almost sold out" | +40-60% |
| **Individual** | 1:1 personalized | "Hi [Name], your favorite [Product] is back in stock" | +60-80% |

### Fatigue Management

| Signal | What It Means | Action |
|--------|-------------|--------|
| Open rate declining | Content losing relevance | Improve targeting/content |
| Opt-out rate > 0.5%/send | Sending too much or wrong content | Reduce frequency, segment better |
| Uninstall spike after push | Notifications are driving users away | Immediately reduce volume |
| Click rate declining but open rate stable | Subject lines good, content disappointing | Improve content/offer quality |

**Frequency caps**: Set maximum notifications per user per time period:
- Push: max 3-5/week
- Email: max 2-3/week (marketing), unlimited for transactional
- SMS: max 2-4/month

### A/B Testing for Notifications

| Element | What to Test | Example |
|---------|-------------|---------|
| **Subject/title** | Length, tone, emoji, personalization | "Your order shipped 📦" vs "Order #1234 is on its way" |
| **Timing** | Hour of day, day of week | 10 AM vs 7 PM |
| **Content** | Short vs detailed, image vs text-only | 20 words vs 50 words |
| **CTA** | Button text, action type | "View" vs "Track Now" |
| **Channel** | Push vs email vs in-app for same message | Same content, different channel |

## Output Format

```markdown
# Notification Strategy: {Product/Campaign}

## Channel Mix
| Message Type | Primary Channel | Fallback | Frequency |
|-------------|----------------|----------|-----------|
| {type} | {channel} | {backup} | {max/period} |

## Segmentation
| Segment | Notification | Personalization Tier |
|---------|-------------|---------------------|
| {segment} | {content} | None/Segment/Behavioral/Individual |

## Timing
| Segment | Send Time | Day | Timezone |
|---------|----------|-----|---------|
| {segment} | {HH:MM} | {day(s)} | {user's TZ} |

## Fatigue Rules
- Max push: {N}/week
- Max email: {N}/week
- Opt-out threshold: {%} → action: {reduce/pause}

## A/B Test Plan
| Test | Variant A | Variant B | Metric | Sample |
|------|----------|----------|--------|--------|
| {test} | {A} | {B} | {open rate / CTR} | {N users} |
```

## Gotchas

- **Permission is a privilege**: iOS requires explicit opt-in for push. Ask at the RIGHT moment (after the user sees value), not at first launch. First-launch permission requests get 40-60% opt-in; contextual requests get 70-80%.
- **Transactional vs marketing**: Order confirmations, shipping updates, and security alerts are transactional (expected, high open rate). Marketing promotions are interruptive (optional, lower open rate). Never mix them in user perception.
- **LINE in Taiwan is unique**: LINE has 95% penetration in Taiwan. LINE Official Account messages have 60%+ open rates — significantly higher than email or push. Prioritize LINE for Taiwan audiences.
- **Rich push is underused**: Push notifications can include images, action buttons, and deep links. A rich push with "View Order" button converts 3-5x better than a text-only push.

## References

- For LINE notification setup, see `references/line-notification.md`
- For email deliverability optimization, see `references/email-deliverability.md`
