---
name: "econ-market-structure"
description: "Analyze market structures across perfect competition, monopolistic competition, oligopoly, and monopoly to predict firm behavior and market outcomes. Use this skill when the user needs to classify a market's competitive structure, predict pricing behavior, evaluate antitrust implications, or understand why an industry behaves the way it does — even if they say 'why can they charge so much', 'is this market competitive', or 'will prices come down'."
metadata:
  category: "WP-17 經濟學院"
  tags: ["economics", "market-structure", "industrial-organization"]
---

# Market Structure Analysis

## Overview

Market structure determines how firms compete, set prices, and earn profits. The four structures — perfect competition, monopolistic competition, oligopoly, monopoly — predict increasingly different behaviors as concentration rises and differentiation increases.

## Framework

```
IRON LAW: Structure Determines Behavior, Not Vice Versa

Classify the market structure FIRST based on structural characteristics
(number of firms, barriers, differentiation), THEN predict behavior.
"This company charges high prices" does not mean it's a monopoly —
high prices can occur in oligopolies and even monopolistic competition.
```

### The Four Structures

| Feature | Perfect Competition | Monopolistic Competition | Oligopoly | Monopoly |
|---------|-------------------|------------------------|-----------|----------|
| Firms | Very many | Many | Few | One |
| Product | Homogeneous | Differentiated | Homogeneous or differentiated | Unique, no close substitutes |
| Entry barriers | None | Low | High | Very high |
| Price power | None (price taker) | Some (limited by substitutes) | Significant (interdependent) | Full (price maker) |
| Long-run profit | Zero (economic) | Zero (economic) | Positive possible | Positive |
| Examples | Agricultural commodities, forex | Restaurants, clothing | Airlines, telecom, auto | Utilities, patents |

### Classification Steps

1. **Count sellers**: How many significant firms serve this market?
2. **Assess differentiation**: Are products identical or differentiated?
3. **Evaluate entry barriers**: Can new firms enter easily?
4. **Check interdependence**: Do firms react to each other's moves?

### Behavior Predictions by Structure

**Perfect Competition**: Price = marginal cost. Firms are price takers. No advertising needed. Long-run economic profit = 0.

**Monopolistic Competition**: Short-run profits possible through differentiation. Long-run: entry erodes profits to zero. Firms compete on brand, quality, location.

**Oligopoly**: Firms are interdependent — each watches rivals' moves. Game theory applies. May collude (tacitly or explicitly). Kinked demand curve or Cournot/Bertrand models.

**Monopoly**: Price > marginal cost. Deadweight loss exists. May be regulated (utilities) or temporary (patents). Natural monopolies occur when average costs decline with scale.

## Output Format

```markdown
# Market Structure Analysis: {Industry}

## Classification
- Structure: {type}
- Evidence:
  - Number of firms: ...
  - Product differentiation: ...
  - Entry barriers: ...
  - Interdependence: ...

## Predicted Behavior
- Pricing: {price-taking / markup / strategic}
- Long-run profit: {zero / positive}
- Competition type: {price / quality / advertising / innovation}

## Policy Implications
{Antitrust concerns, regulation needs, consumer impact}
```

## Examples

### Correct Application
**Scenario:** Taiwan's telecom market
- **Firms**: 3 major (中華電信, 台灣大, 遠傳) + 2 minor → **Few**
- **Differentiation**: Moderate (speed/coverage differences, but largely substitutable)
- **Entry barriers**: Very high (spectrum licenses, infrastructure costs ~NT$100B+)
- **Interdependence**: High (price changes by one trigger immediate responses)
- **Classification: Oligopoly** ✓
- **Predicted behavior**: Tacit price coordination, competition on bundling and service rather than price, stable high margins

### Incorrect Application
- "iPhone has no competitors so Apple is a monopoly" → Smartphones have many competitors (Samsung, Google, Xiaomi). Apple has market power through differentiation, but the smartphone market is **oligopoly**, not monopoly. Structure is about the market, not one firm's product uniqueness.

## Gotchas

- **Market definition changes the answer**: "Smartphones" is an oligopoly. "iOS devices" is a monopoly. The market boundary determines the structure classification.
- **Perfect competition is theoretical**: Almost no real market is perfectly competitive. Use it as a benchmark, not a classification for real industries.
- **Oligopoly is the most complex**: Game theory, collusion, and strategic behavior make oligopoly analysis harder than other structures. Be explicit about assumptions.
- **Contestable markets**: Even a monopoly may behave competitively if entry barriers are low (threat of entry disciplines pricing). Barriers matter as much as current firm count.
- **Dynamic markets**: Tech markets may look like monopolies today (Google Search) but face competitive pressure from disruption (AI chat). Consider trajectory, not just snapshot.

## References

- For oligopoly game theory models (Cournot, Bertrand, Stackelberg), see `references/oligopoly-models.md`
