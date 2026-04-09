# Multi-Party Negotiation

Multi-party negotiation (3+ parties) is structurally different from bilateral negotiation. The core difference: **coalitions form**, and coalition membership determines outcomes more than any single party's BATNA. Everything in the parent SKILL.md still applies, but you need additional mechanics.

---

## The Coalition Problem

In a bilateral negotiation, ZOPA is a single range. In multi-party, ZOPA is multidimensional — an agreement must land inside *every* party's acceptable range simultaneously.

**Key insight**: Parties often find it rational to form a sub-coalition, agree among themselves, and present the rest with a fait accompli. Your job is to either:
- Be inside the winning coalition, or
- Make your exclusion costly enough that the coalition includes you anyway

### Coalition Vocabulary

| Term | Definition |
|------|-----------|
| **Minimum Winning Coalition (MWC)** | Smallest group that can pass a decision without outsiders |
| **Grand Coalition** | All parties agree — usually less stable (value is diluted too thin) |
| **Blocking Coalition** | A sub-group large enough to veto any agreement |
| **Core** | The set of agreements that no sub-coalition can profitably deviate from |

---

## BATNA in Multi-Party Contexts

Your BATNA is no longer just "walk away." It splits into three:

1. **Exit BATNA**: Your best outcome if you leave entirely (same as bilateral)
2. **Coalition BATNA**: Your best outcome if you form a sub-coalition with a *subset* of the parties and exclude the rest
3. **Veto BATNA**: If you can block any agreement from passing, your BATNA is the status quo — which may suit you fine

**Before entering a multi-party negotiation, map all three for yourself and estimate them for every other party.**

### BATNA Estimation Table (fill this out during prep)

| Party | Exit BATNA | Coalition BATNA (with whom?) | Can they veto? |
|-------|-----------|------------------------------|----------------|
| You | ? | ? | ? |
| Party B | ? | ? | ? |
| Party C | ? | ? | ? |

The party with the *worst* Exit BATNA and *weakest* Coalition BATNA is the most desperate — they will accept the worst deal. Do not let that be you.

---

## The Shapley Value: How to Measure Bargaining Power

In multi-party negotiations, the **Shapley value** gives each party a principled share of the total value created, based on their *marginal contribution* to every possible coalition.

### Formula

For party *i* in a set of parties *N*, with characteristic function *v(S)* giving the value coalition *S* can create:

```
φᵢ(v) = Σ [|S|!(|N|-|S|-1)! / |N|!] × [v(S ∪ {i}) - v(S)]
          S ⊆ N\{i}
```

In plain terms: average over all orderings of parties, what does party *i* contribute when they join?

### Worked Example

Three parties: **Buyer (B)**, **Supplier A (SA)**, **Supplier B (SB)**

Value each coalition can generate (estimated deal surplus, $K):
- v(∅) = 0
- v(B) = 0, v(SA) = 0, v(SB) = 0 (no single party can deal alone)
- v(B, SA) = 120
- v(B, SB) = 80
- v(SA, SB) = 0 (no value without the buyer)
- v(B, SA, SB) = 150 (grand coalition creates 150 but SA and SB compete)

Calculate Shapley value for **Buyer (B)**:

| Coalition S (not containing B) | v(S ∪ B) - v(S) | Weight [|S|!(2-|S|)!/3!] |
|-------------------------------|-----------------|--------------------------|
| {} | v({B}) - v({}) = 0 - 0 = 0 | (0!·2!/6) = 2/6 |
| {SA} | v({B,SA}) - v({SA}) = 120 - 0 = 120 | (1!·1!/6) = 1/6 |
| {SB} | v({B,SB}) - v({SB}) = 80 - 0 = 80 | (1!·1!/6) = 1/6 |
| {SA,SB} | v({B,SA,SB}) - v({SA,SB}) = 150 - 0 = 150 | (2!·0!/6) = 2/6 |

φ(B) = (2/6)×0 + (1/6)×120 + (1/6)×80 + (2/6)×150 = 0 + 20 + 13.3 + 50 = **83.3**

By similar calculation: φ(SA) ≈ 45, φ(SB) ≈ 21.7

**Interpretation**: The Shapley value tells the Buyer they "deserve" ~83K of the 150K total surplus. SA is worth ~45K; SB's presence is worth ~22K mostly as competitive threat.

**Practical use**: If the Buyer is being asked to accept a deal where they get only 60K, they have analytical grounds to push back — their marginal contribution justifies more. If SA is asking for 70K, you can show the math.

You don't need to present the Shapley value at the table. Use it privately to calibrate whether a proposed split is fair or exploitative.

---

## Coalition Strategy: When to Build vs. When to Block

### Decision Rule

```
Build a coalition when:
  Your coalition BATNA > Your share in the grand coalition

Block an agreement when:
  Status quo > Any reachable agreement (for you)
  AND you have enough votes/veto power to block
```

### Tactics for Each Position

**You need a coalition (weak position):**
1. Approach the party with the *second-worst* BATNA first — they're most motivated to ally
2. Lock in bilateral terms before the three-way table convenes
3. Frame the coalition as a "joint position," not an alliance — less threatening to outsiders
4. Give the coalition partner a slightly better deal than they'd get in the grand coalition; their incentive to stay is the surplus over their exit BATNA

**You're the target of a coalition (strong position):**
1. Identify the weakest link in the coalition and make them a separate side offer
2. Their coalition BATNA just got a better alternative — the coalition destabilizes
3. Alternatively, make the grand coalition more attractive than any sub-coalition by offering integrative gains only achievable with everyone present

**You can block but not win outright:**
1. Use your veto credibly — make it known early that no agreement passes without addressing your interests
2. Don't veto everything; selective use preserves credibility
3. Offer to drop the veto in exchange for specific concessions

---

## Managing the Multi-Party Table

### Sequencing: Who Do You Talk to First?

**Rule**: Talk to the party whose *alignment* most changes the situation.

Rank parties by:
1. Veto power (if they can block, you need them or need to neutralize them)
2. BATNA quality (weak BATNAs = easier to bring in, but they add less credibility)
3. Relationship to you (existing trust speeds up pre-agreement)

**Avoid** starting with the most powerful party — you'll reveal your position before building any coalition leverage.

### Agenda Control

Whoever sets the agenda in multi-party talks has disproportionate power. Before the first meeting:

- Push to set the agenda yourself, or at minimum negotiate it
- Put items where you have strength *first* — early agreements build momentum and create psychological commitment
- Keep your hardest item for when a partial agreement is already on the table (parties are reluctant to blow up deals already made)

### Single Negotiating Text (SNT)

Used in complex multi-party negotiations (Camp David was an example). Mechanics:

1. A neutral party (or the party with least to lose from a bad draft) produces a *single draft agreement*
2. Each party critiques the draft — they do not produce counter-proposals
3. The neutral revises and re-circulates
4. Repeat until no party can improve their position by rejecting

**Why it works**: Parties never have to formally "accept" anything until the final text. This avoids positional entrenchment. It also shifts the frame from "I'm giving something up" to "I'm improving a neutral draft."

**When to use it**: When there are 4+ parties and bilateral horse-trading has broken down. Offer to produce the first draft yourself — the drafter has enormous influence over what's "normal" in the text.

---

## Common Multi-Party Failure Modes

### 1. Grand Coalition Instability

The grand coalition (everyone agrees) is often *less* stable than a smaller coalition, because the value must be split so many ways that sub-coalitions can form and do better.

**Test**: After reaching a grand coalition agreement, check whether any sub-group of parties could defect and collectively do better. If yes, the agreement will likely unravel.

**Fix**: Build in side payments or joint-gains that are *only achievable* when all parties remain. Lock-in mechanisms (contracts, irreversible commitments) also stabilize grand coalitions.

### 2. Procedural Deadlock

With many parties, you can get majority agreement but no *unanimous* agreement — and the rules require unanimity.

**Fix options**:
- Change the decision rule (majority instead of unanimity) — requires all parties to agree to the rule change first, which is easier than the substantive agreement
- Create a smaller authorized working group empowered to negotiate on behalf of the full group
- Accept a partial agreement among willing parties, with a clear mechanism for others to join later

### 3. Reciprocity Breakdown

In bilateral negotiation, concessions are clearly bilateral. In multi-party, a concession to one party may not be reciprocated by the party who benefits most.

**Rule**: Make concessions party-specific and *conditional*. "I'll agree to X *if* Party B agrees to Y and Party C agrees to Z." Do not make unilateral concessions into the room hoping everyone adjusts favorably.

### 4. Side-Deal Contamination

Parties make bilateral side deals outside the main table that change the incentive structure at the main table — without disclosing this.

**Tactic if you suspect this**: Ask each party privately what their current *reservation price* is. Inconsistencies between their stated positions at the table and their apparent flexibility suggest a side deal exists. Probe with: "What would need to change for you to move on X?"

---

## Worked Scenario: Three-Way Licensing Negotiation

**Situation**: A tech startup (S) owns a patent. Two larger companies, Corp A and Corp B, both want a license. They could each license separately, or one could acquire an exclusive license blocking the other.

| Party | Exit BATNA | Key Interest |
|-------|-----------|--------------|
| Startup (S) | $200K (sell patent outright) | Max revenue, retain credibility |
| Corp A | $0 (can't build without license) | Exclusive use, block Corp B |
| Corp B | $0 (can't build without license) | Access to patent, not necessarily exclusive |

**ZOPA Analysis**:
- S's reservation price: anything > $200K
- A wants exclusive: will pay up to $500K (internal valuation)
- B wants non-exclusive: will pay up to $250K

**Coalition dynamics**:
- If A gets exclusive at $400K → S gets $400K; B is locked out
- If S licenses both non-exclusively → S gets $250K + $250K = $500K; A is unhappy (no exclusivity) but may still accept
- If B forms coalition with S to preempt A → non-exclusive deal at $250K, but S sacrifices $150K upside

**Optimal move for S**: Run a *sealed-bid auction* framed as "exclusive license auction." Set reserve at $400K. Tell both parties the reserve. This:
1. Creates competition between A and B
2. Forces A to reveal their true valuation
3. If A wins at $450K, S gets $250K more than exit BATNA
4. If neither bids above reserve, S falls back to bilateral negotiations with the knowledge of both parties' positions

**Key lesson**: S's best move was not to negotiate — it was to design a *mechanism* (the auction) that made competition explicit and extracted maximum value without positional bargaining.

---

## Quick Reference: Multi-Party Checklist

Before any multi-party negotiation:

- [ ] Map all parties, their Exit BATNAs, and estimated Coalition BATNAs
- [ ] Identify who has veto power and what they need to not veto
- [ ] Determine the decision rule (unanimity? majority? consensus?)
- [ ] Sequence your outreach: weakest BATNA parties first, build coalition before the main table
- [ ] Decide whether to push for a Single Negotiating Text if talks are complex
- [ ] Check grand coalition stability: can any sub-group defect and do better?
- [ ] Make all concessions conditional and party-specific, never unilateral
