---
name: "grad-platform-economics"
description: "Apply platform economics to analyze network effects, solve chicken-and-egg problems, and design multi-sided platform pricing strategies. Use this skill when the user needs to evaluate a platform business model, diagnose why a platform is failing to scale, or choose a subsidy strategy for bootstrapping a two-sided market."
metadata:
  category: "WP-24 創新與國際化"
  tags: ["platform-economics", "network-effects", "two-sided-markets", "chicken-and-egg", "pricing-strategy", "multi-sided-platform"]
---

# Platform Economics: Network Effects and Multi-Sided Markets

## Overview

Platform economics studies businesses that create value by facilitating interactions between two or more distinct user groups. Unlike pipeline businesses that create value linearly, platforms exhibit network effects where each additional user increases value for others. The central challenge is the chicken-and-egg problem: neither side joins without the other.

## When to Use

**Trigger conditions:**
- User is designing or evaluating a multi-sided platform business model
- User asks how to bootstrap a marketplace with no users on either side
- User needs to decide pricing: who to subsidize, who to charge
- User mentions "network effects", "marketplace", "platform strategy", or "chicken-and-egg"

**When NOT to use:**
- For linear/pipeline business models -> use Porter's value chain
- For competitive dynamics between platforms -> use grad-coopetition
- For innovation strategy within platforms -> use grad-ambidexterity

## Assumptions

```
IRON LAW: Value Scales with Interactions, NOT Users

A platform with 1 million users but zero transactions has ZERO value.
The unit of platform value is the INTERACTION (transaction, match,
message), not the user count. Vanity metrics (registered users, downloads)
mask platform failure.

Always measure: interactions per user per time period.
```

- At least two distinct user groups exist with interdependent demand
- The platform does not own the means of production — it orchestrates
- Winner-take-all dynamics strengthen with network effect intensity

## Methodology

### Step 1: Identify Platform Type and Sides

Classify the platform and its sides:
- **Transaction platform**: Facilitates exchange (Uber, Airbnb, eBay)
- **Innovation platform**: Provides foundation for complements (iOS, AWS)
- **Hybrid**: Both transaction and innovation (Amazon, WeChat)

List each side and what value they seek from the platform.

### Step 2: Map Network Effects

For each pair of sides, identify:
- **Same-side (direct) effects**: More users on side A attract more users on side A? (Positive: social networks. Negative: seller competition on marketplaces.)
- **Cross-side (indirect) effects**: More users on side A attract more users on side B? (Riders attract drivers, and vice versa.)

### Step 3: Solve the Chicken-and-Egg Problem

Select a bootstrapping strategy:
| Strategy | Mechanism | Example |
|----------|-----------|---------|
| Subsidize one side | Make one side free/cheap to attract the other | Adobe PDF Reader free, Acrobat paid |
| Single-player mode | Provide standalone value before network kicks in | OpenTable reservation system for restaurants |
| Seeding | Create supply yourself initially | Reddit founders posted early content |
| Marquee users | Sign high-profile users to attract the mass | Gaming consoles sign exclusive titles |
| Piggybacking | Leverage existing network | PayPal on eBay |

### Step 4: Design Pricing Architecture

Determine the "money side" and "subsidy side":
- The side with **lower price elasticity** pays more
- The side that generates **stronger cross-side effects** gets subsidized
- Never charge both sides equally in early stages

## Output Format

```markdown
# Platform Analysis: {Platform Name}

## Platform Architecture
- Type: Transaction / Innovation / Hybrid
- Sides: {list each side and their value proposition}

## Network Effects Map
| Effect | Type | Direction | Strength |
|--------|------|-----------|----------|
| {Side A to Side A} | Same-side | Positive/Negative | High/Med/Low |
| {Side A to Side B} | Cross-side | Positive/Negative | High/Med/Low |

## Chicken-and-Egg Strategy
- Recommended approach: {strategy}
- Subsidy side: {which side and why}
- Money side: {which side and why}

## Key Metrics
- Core interaction: {what counts as a successful interaction}
- Interaction rate: {interactions per user per period}
- Liquidity threshold: {minimum activity for self-sustaining growth}
```

## Gotchas

- **Network effects are not viral effects**: Virality is about acquisition speed; network effects are about value increase. A product can be viral without network effects (Hotmail) or have network effects without virality (Bloomberg Terminal).
- **Negative same-side effects matter**: More sellers on a marketplace HURTS each seller. If negative same-side effects outpace cross-side benefits, the platform collapses.
- **Multi-homing kills lock-in**: If users easily use competing platforms simultaneously (drivers on Uber AND Lyft), network effects weaken. Assess multi-homing costs.
- **Winner-take-all is not guaranteed**: Markets with strong local effects, low multi-homing costs, or niche differentiation support multiple platforms.
- **Disintermediation risk**: Participants may bypass the platform once connected. Build ongoing value or enforce switching costs.

## References

- For network effects mathematical models (Metcalfe, Reed), see `references/network-effects-math.md`
- For platform pricing formalization (Rochet-Tirole), see `references/platform-pricing-models.md`
