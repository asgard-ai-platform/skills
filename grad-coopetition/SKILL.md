---
name: "grad-coopetition"
description: "Apply the Co-opetition Value Net framework (Brandenburger and Nalebuff, 1996) to map cooperative and competitive dynamics in business relationships. Use this skill when the user needs to identify complementors, analyze the PARTS framework, or design strategies that simultaneously cooperate and compete with the same players."
metadata:
  category: "WP-24 創新與國際化"
  tags: ["coopetition", "value-net", "brandenburger-nalebuff", "PARTS-framework", "complementors", "game-theory-strategy"]
---

# Co-opetition: The Value Net (Brandenburger & Nalebuff, 1996)

## Overview

Co-opetition recognizes that business relationships are never purely competitive or purely cooperative. The Value Net model extends Porter's focus on rivalry by adding complementors — players whose products increase the value of yours. The PARTS framework (Players, Added value, Rules, Tactics, Scope) provides a structured approach to changing the game rather than just playing it.

## When to Use

**Trigger conditions:**
- User is analyzing a relationship that is simultaneously cooperative and competitive
- User asks about strategic alliances with competitors
- User needs to identify complementors or map all players in a value network
- User mentions "frenemy", "coopetition", "complementors", or "value net"

**When NOT to use:**
- For pure competitive analysis -> use Porter's Five Forces
- For internal organizational balance -> use grad-ambidexterity
- For international market entry mode -> use grad-oli

## Assumptions

```
IRON LAW: Every Business Relationship Contains BOTH Cooperative
          and Competitive Elements

There is NO purely competitive or purely cooperative relationship.
A supplier cooperates (provides inputs) AND competes (captures margin).
A competitor competes (takes share) AND cooperates (grows the category).

Any analysis that labels a player as ONLY competitor or ONLY partner
is incomplete. Always map BOTH dimensions.
```

- Business is a game — but players can change the game, not just play it
- Value creation is cooperative; value capture is competitive
- The same player can be a competitor AND a complementor simultaneously

## Methodology

### Step 1: Map the Value Net

Place the focal firm at the center and map four player types: Customers, Suppliers, Competitors (whose products DECREASE your value), and Complementors (whose products INCREASE your value). Key insight: a player can occupy multiple roles (Samsung supplies displays to Apple AND sells competing phones).

### Step 2: Assess Added Value

For each player, calculate added value:
- **Added value** = Total value of the game WITH the player MINUS total value WITHOUT the player
- A player can never capture more than their added value
- Strategies should aim to increase YOUR added value and manage others'

### Step 3: Apply PARTS Framework

Systematically evaluate five levers to change the game:

| Lever | Question | Action |
|-------|----------|--------|
| **Players** | Who is in the game? Should we add/remove players? | Bring in new complementors, attract new competitors to reduce supplier power |
| **Added value** | How can we increase our added value? | Differentiate, build switching costs, create loyal customers |
| **Rules** | What rules govern the game? Can we change them? | Contracts, regulations, industry standards, MFN clauses |
| **Tactics** | How do perceptions shape the game? | Signaling, commitments, transparency vs fog |
| **Scope** | What is the boundary of the game? | Link or de-link games, expand or narrow scope |

### Step 4: Design Co-opetition Strategy

For each key relationship, specify:
- Where to cooperate (value creation): joint R&D, standard setting, market expansion
- Where to compete (value capture): pricing, customer acquisition, differentiation
- Boundary rules: what information to share, what to protect

## Output Format

```markdown
# Co-opetition Analysis: {Focal Firm}

## Value Net Map
- Customers / Suppliers / Competitors / Complementors: {list each, note dual roles}

## Added Value Assessment
| Player | Added Value | Leverage |
|--------|-------------|----------|
| {Focal firm} | {assessment} | {high/medium/low} |

## PARTS Analysis
| Lever | Current State | Recommended Change |
|-------|---------------|-------------------|
| Players / Added value / Rules / Tactics / Scope | {current} | {action} |

## Co-opetition Strategy
- Cooperate on: {activities} | Compete on: {activities} | Boundary rules: {policy}
```

## Gotchas

- **Complementor identification is the hardest part**: Force yourself to ask: "Whose product makes mine more valuable?" The biggest insights hide here.
- **Dual roles create tension**: When a partner is also a competitor, define explicit information boundaries.
- **Added value is dynamic**: Every major move changes everyone's added value. Reassess after launches or market entries.
- **Cooperation without boundaries leads to knowledge leakage**: Alliances need explicit IP firewalls.
- **PARTS is about changing the game**: If your analysis only describes the current game, you missed the point.

## References

- For game theory foundations of co-opetition, see `references/coopetition-game-theory.md`
- For PARTS framework detailed application guide, see `references/parts-framework-guide.md`
