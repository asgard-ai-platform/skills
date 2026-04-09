# PARTS Framework: Detailed Application Guide

*Reference for `grad-coopetition` skill. Expands Step 3 of the methodology with move-by-move decision logic, worked examples, and common traps.*

---

## What PARTS Is (and Is Not)

PARTS is a **game-change checklist**, not a description framework. Its purpose is to surface the five levers that can alter the rules, players, or boundaries of a competitive game. If your PARTS analysis concludes "the game stays the same," you have not done PARTS — you have done a static competitive audit.

**Each lever answers one question:**

| Lever | The Question |
|-------|-------------|
| **P**layers | Who *should* be in this game? |
| **A**dded Value | How can I increase what disappears if I leave? |
| **R**ules | Which formal constraints can be rewritten? |
| **T**actics | How do I shape perceptions to move payoffs? |
| **S**cope | Should this be one game or many? |

---

## Lever 1 — Players

### Decision Logic

The key move is **adding or removing players** from each arm of the Value Net (Customers, Suppliers, Competitors, Complementors). The question is always *why* — what payoff changes when a new player enters or exits?

```
Add a competitor to reduce supplier power
Add a complementor to grow the pie
Add a customer to increase your added value
Remove a competitor (acquisition, exclusivity) to capture share
```

**When to add a competitor deliberately:**
- You are captive to a single supplier → introduce a second supplier to gain bargaining power
- Your market is perceived as a monopoly → attract entry to avoid regulatory risk
- A complementor's product needs a competing ecosystem to become legitimate (e.g., Blu-ray vs. HD-DVD needed studios on both sides)

**When to attract complementors:**
- Your product's standalone value is limited (platform economics)
- You can offer favorable terms early to lock in high-value complementors before competitors do

**Player Addition Decision Table:**

| Objective | Add Player Type | Mechanism |
|-----------|----------------|-----------|
| Reduce supplier margin capture | Competitor (second supplier) | Dual-source policy, open RFQ |
| Grow total market | Complementor | Co-marketing, API access, certification |
| Raise your added value signal | Customer (anchor/reference) | Design partnership, reference pricing |
| Weaken a rival's supply chain | Competitor into rival's supply base | Poach or fund a second supplier to rival |

### Worked Example: Intel and Microsoft

Intel added Microsoft as a complementor in the 1980s by ensuring Windows ran optimally on Intel chips. This grew the total PC market (cooperative dimension). Intel simultaneously used its chip roadmap to disadvantage clone chipmakers (competitive dimension). The player move was: *actively recruit the complementor before rivals could establish alternative pairings.*

---

## Lever 2 — Added Value

### The Formula

$$AV_i = V(\text{game with player } i) - V(\text{game without player } i)$$

Where $V$ is the total value created by all transactions in the game.

**Constraint (Iron Law of Added Value):**

> No player can capture more than their own added value. Strategies that try to do so will be blocked or unraveled.

This means: before negotiating for a large share, *increase your added value first*.

### Five Ways to Increase Your Added Value

| Method | Mechanism | Risk |
|--------|-----------|------|
| **Differentiation** | Make your product uniquely valuable to customers | Imitation |
| **Switching costs** | Raise the cost of replacing you | Customer resentment |
| **Scarcity / exclusivity** | Limit who can access what you offer | Regulatory scrutiny |
| **Loyalty** | Build relationships that persist past product-level evaluation | Requires time |
| **Complementor lock-in** | Be the only viable platform for the best complementors | Platform antitrust |

### Quantifying Added Value in Practice

When exact numbers are unavailable, use a **three-tier qualitative scale**:

```
HIGH   — the game cannot function without this player, or total value 
         drops by >30% in their absence
MEDIUM — the game continues but is materially worse; substitutes exist 
         but are costly
LOW    — easy to replace; contribution to total value is marginal
```

**Assessment template:**

```
Player: [Name]
What does this player contribute to total game value?
  [describe the value-creation mechanism]

What is the best available substitute?
  [describe substitute + its costs/gaps]

Added Value tier: HIGH / MEDIUM / LOW

Implication: [what share of the game can this player credibly claim?]
```

### Trap: Confusing Revenue Share with Added Value

A player who *captures* 40% of industry revenue does not necessarily *create* 40% of industry value. Distribution channels often capture high revenue share but have low added value (easily replaced by direct sales or alternative distributors). Map creation separately from capture.

---

## Lever 3 — Rules

### What Counts as a "Rule"

Rules are any formal or semi-formal constraints that govern how the game is played:

- **Contracts** (exclusivity clauses, MFN clauses, take-or-pay, non-compete)
- **Industry standards** (technical standards lock in platform advantages)
- **Regulations** (licensing requirements, data residency rules)
- **Norms** (informal but enforced by reputation — e.g., pricing transparency norms in an industry)

### Most-Favored-Nation (MFN) Clauses — A Key Rule Tactic

MFN clauses state: *"We will give you terms no worse than any other customer/supplier."*

**Offensive MFN (buyer uses it):** Forces supplier to extend best pricing to you. Effectively caps the supplier's ability to price-discriminate.

**Defensive MFN (seller uses it):** Commits seller not to undercut current buyer with a rival. This signals commitment but reduces flexibility.

```
MFN clause decision:
  If you are the weaker buyer → push for MFN to benefit from rivals' 
    negotiating power without doing the work
  If you are the market leader seller → avoid MFN clauses; they prevent 
    you from monetizing negotiating power with weaker buyers
  If you are a platform → offer MFN to anchor tenants; extract margin 
    from non-anchor tenants who lack leverage to resist
```

### Rule-Change Tactics by Relationship Arm

| Relationship | Rule to target | Change direction |
|-------------|----------------|-----------------|
| Supplier | Long-term supply contract | Lock in supply; reduce supplier's optionality |
| Supplier | Dual-source requirement | Prevent exclusivity; maintain competition |
| Customer | Subscription / annual commit | Raise switching cost; smooth revenue |
| Competitor | Industry standard body | Set standards around your architecture |
| Complementor | API terms of service | Control what complementors can build; retain platform rent |

### Standards as Rules

Setting a technical standard is the most durable rule change available. Once adopted:
1. Your architecture becomes the reference implementation
2. Competitors must be compatible with *your* choices
3. Complementors build to your interfaces

**Standard-setting strategy:**
- Propose open standards when you want to grow the ecosystem quickly (lower barrier for complementors)
- Propose proprietary standards when you want to capture ecosystem rent (Apple MFi program)
- Join standards bodies early to shape direction; join late only to block threats

---

## Lever 4 — Tactics

### The Fog vs. Clarity Tradeoff

Tactics work by shaping other players' **perceptions** of the game — specifically their beliefs about your intentions, capabilities, and payoffs. Two opposing strategies:

**Create Fog (increase uncertainty):**
- Obscure your cost structure to prevent suppliers from claiming all margin
- Mask your product roadmap to prevent complementors from timing entry
- Use multiple negotiating teams to make your true priorities unclear

**Create Clarity (reduce uncertainty):**
- Make credible commitments to signal you will not defect from cooperation
- Announce investments publicly to discourage entry (capacity preemption)
- Be transparent about shared interests to enable coordination

```
Fog is useful when: 
  - You are negotiating from weakness (hide the weakness)
  - You want optionality (announcing a direction closes doors)
  - Competitor is trying to coordinate against you

Clarity is useful when:
  - You are making a credible threat (threats only work if believed)
  - You are inviting a complementor to invest alongside you
  - You want to lock in a cooperative equilibrium before a rival can poach your partner
```

### Commitments and Credibility

A tactic only works if believed. A commitment is credible only if it is:

1. **Costly to reverse** — burning bridges, sunk investments, contracts with penalties
2. **Observable** — the other player must be able to see the commitment
3. **Understandable** — the other player must be able to interpret what you committed to

**Credibility test:**

```
Proposed commitment: [describe]
Is it costly to reverse? [yes/no + why]
Can the counterparty observe it? [yes/no + how]
Can they interpret it correctly? [yes/no + risk of misread]

If any answer is NO → the commitment will be discounted or ignored.
```

### Signaling in Practice

| Signal type | Mechanism | When to use |
|------------|-----------|-------------|
| Price signal | Set price above cost to signal quality/exclusivity | Premium positioning; avoid race to bottom |
| Capacity signal | Build excess capacity visibly | Deter entry; signal you will compete aggressively |
| Partnership announcement | Public joint venture or alliance | Signal to third parties that this space is occupied |
| Reference customer | Publish logos of anchor customers | Reduce uncertainty for next customer cohort |
| Patent filing | File broadly even on non-core IP | Signal litigation willingness; deter copycats |

---

## Lever 5 — Scope

### Link or De-link Games

Scope asks: are you treating this as one game or multiple? Linking games creates dependencies; de-linking preserves optionality.

**Link games when:**
- You want to transfer leverage from a game you dominate to one you don't
- Example: Microsoft used its Windows dominance (strong game) to push Internet Explorer (weak game). Bundling linked the games.
- Example: A retailer uses its store traffic (strong game) to extract slotting fees from suppliers (linked game)

**De-link games when:**
- A partner is extracting value from a linked game that you would prefer to compete in independently
- Example: A manufacturer selling direct-to-consumer should de-link its DTC channel from its wholesale channel to avoid price-coordination problems
- Example: A platform should de-link its marketplace business from its owned-brand business to avoid antitrust exposure

### Scope Expansion and Contraction

```
Expand scope → bring in adjacent games where your added value is high
  Risk: overextension, brand dilution, antitrust

Contract scope → exit games where your added value is low; 
  let others play there
  Risk: losing optionality, ceding territory to rivals who then 
        build added value through scale
```

### Scope Decision Matrix

| Your AV in adjacent game | Partner dependency | Recommended scope move |
|--------------------------|-------------------|----------------------|
| High | Low | Expand: enter unilaterally |
| High | High | Expand via the partnership; negotiate scope upfront |
| Low | Low | Contract: exit or ignore |
| Low | High | Caution: partner has leverage; only expand if strategic necessity forces it |

---

## Running PARTS as a Structured Session

### Sequence Matters

PARTS levers interact. Run them in this order to avoid circular analysis:

1. **Players first** — establish who is in the game before assessing their values
2. **Added Value second** — assess current leverage positions
3. **Rules third** — identify which constraints are fixed vs. changeable
4. **Tactics fourth** — given fixed rules, how can you shape beliefs?
5. **Scope last** — with everything mapped, decide where the game boundary should sit

### Session Template (one player type at a time)

```
PARTS Session for: [Focal Firm] × [Player: e.g., Key Supplier]

PLAYERS
  Current: [who is in this relationship?]
  Add candidates: [who could enter? what would change?]
  Remove candidates: [who could be exited? what would change?]

ADDED VALUE
  Their AV: HIGH / MEDIUM / LOW — [rationale]
  Our AV in their eyes: HIGH / MEDIUM / LOW — [rationale]
  AV-raising moves available to us: [list]

RULES
  Current rules governing this relationship: [list contracts, norms]
  Rules we could introduce: [list + mechanism]
  Rules they might introduce against us: [list + counter]

TACTICS
  What do they believe about our intentions? [current perception]
  Is this accurate? [yes/no]
  If not, what signal changes it? [action]
  Fog or clarity needed? [decision + rationale]

SCOPE
  Are adjacent games linked currently? [yes/no + description]
  Should they be? [decision + rationale]

SYNTHESIS
  Top 2-3 game-change moves: [prioritized list]
  Key risk of each move: [one-line per move]
```

---

## PARTS Anti-Patterns

**1. Describing instead of prescribing**
PARTS is a *change* framework. "Our customers are loyal and suppliers are fragmented" is a description. "We should introduce a second supplier to reduce our current supplier's AV from HIGH to MEDIUM" is a PARTS move.

**2. One lever in isolation**
Moves in one lever ripple into others. Adding a competitor (Players) changes AV calculations for all parties and may require new Rules (contracts) to manage the relationship. Always note the second-order effects.

**3. Ignoring the counterparty's PARTS moves**
Every player in the Value Net can run PARTS against you. For each move you consider, ask: "What is their available PARTS response?" A move with no viable counter-response is a strong move; a move that invites a devastating counter is a trap.

**4. Treating Rules as permanent**
Rules feel fixed because changing them requires effort. They are not permanent. Standard bodies, regulatory lobbying, contract renegotiation, and litigation are all mechanisms for rule change. The question is cost-benefit, not possibility.

**5. Confusing Tactics with Strategy**
Tactics are temporary perception management. They do not substitute for structural moves (Players, Rules, Scope). If your entire PARTS output is tactical, you are managing the current game, not changing it.

---

## Quick Reference Card

```
P — Who should be in the game?
    → Add: complementors to grow pie; competitors into supplier base
    → Remove: consolidate to increase AV

A — What disappears if I leave?
    → Formula: AV = V(with me) − V(without me)
    → Increase via: differentiation, switching costs, scarcity, loyalty

R — What rules can I rewrite?
    → Contracts, standards, regulations, norms
    → MFN clauses: offensive (buyer) vs. defensive (seller)
    → Standards: open to grow ecosystem; proprietary to capture rent

T — What do others believe, and should they?
    → Fog: hide weakness, preserve optionality
    → Clarity: make threats credible, invite complementor investment
    → Commitment credibility test: costly + observable + interpretable

S — One game or many?
    → Link: transfer leverage from strong game to weak game
    → De-link: exit games where AV is low; avoid antitrust exposure
```
