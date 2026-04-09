# Framework Comparison: Blue Ocean Strategy vs. Related Frameworks

This reference answers the single most common misuse question: **which framework do I reach for when?**

Blue Ocean Strategy is frequently confused with Porter's Differentiation strategy, Blue Ocean is frequently invoked when SWOT would suffice, and teams sometimes attempt to run Blue Ocean and Porter's Five Forces simultaneously in a way that contradicts each other's logic. This file gives you a decision table, a diagnostic, and worked examples to prevent those errors.

---

## Decision Table: Which Framework to Use

| Situation | Right Framework | Why NOT Blue Ocean |
|-----------|----------------|-------------------|
| "Should we enter this market?" | Porter's Five Forces | Five Forces assesses industry attractiveness; Blue Ocean assumes you're already committed to a space and asks how to redefine it |
| "Where do we stand vs. competitors?" | SWOT or Value Chain Analysis | These are internal/external audits; Blue Ocean is a design tool, not an audit tool |
| "What macro trends will affect us?" | PESTEL | Environmental scanning is a prerequisite to Blue Ocean, not a substitute |
| "We need to grow 10% — what to optimize?" | OKRs + Porter's Differentiation or Cost Leadership | Incremental improvement; Blue Ocean is for fundamental repositioning |
| "We're stuck in price war with 5 competitors" | **Blue Ocean Strategy** | Classic trigger: red ocean commoditization, need to reconstruct market boundaries |
| "We want to create demand that doesn't exist yet" | **Blue Ocean Strategy** | Non-customer analysis and value innovation are core Blue Ocean tools |
| "How do we beat Competitor X?" | Porter's Generic Strategies or Competitive Intelligence | Blue Ocean explicitly de-emphasizes beating competitors; wrong framing |
| "Which customer segment is most valuable?" | BCG Matrix or Segmentation/Targeting/Positioning (STP) | Blue Ocean challenges existing segmentation; STP works within it |
| "Should we diversify into a new business unit?" | BCG Matrix + Ansoff Matrix | Portfolio decisions, not value curve redesign |

---

## Conceptual Difference: Competition Logic

The deepest incompatibility between Blue Ocean and Porter-era frameworks is their **underlying competitive logic**.

### Porter's Five Forces Logic

```
Industry profitability = f(bargaining power of buyers, bargaining power of suppliers,
                            threat of new entrants, threat of substitutes,
                            competitive rivalry)
```

**Assumption**: industry structure is given. The strategist adapts to it.

**Output**: "this industry is attractive/unattractive; here's how to position within it."

### Blue Ocean Logic

```
Market boundaries = f(industry assumptions + competitor imitation)
∴ Market boundaries can be reconstructed by questioning those assumptions
```

**Assumption**: industry structure is malleable. The strategist can redefine it.

**Output**: "here's how to make the industry structure irrelevant to us."

### Why Running Both Simultaneously Is Usually Wrong

A common mistake: teams run Five Forces to assess an industry, conclude it's unattractive (high rivalry, low barriers), and then attempt Blue Ocean to "escape" the low scores.

The problem: Five Forces measures the existing competitive space. Blue Ocean creates a *new* space. The Five Forces score of the existing industry tells you nothing about the attractiveness of the blue ocean you're trying to create — because that ocean doesn't yet have the forces in it.

**Valid sequence:**
1. Five Forces → diagnose why current position is deteriorating
2. Blue Ocean → redesign the value curve to move away from that space
3. (Later) Five Forces applied to the *new* space → assess whether the blue ocean will stay blue

---

## Blue Ocean vs. Porter's Differentiation Strategy

This is the most frequent confusion. Both involve "doing something different." The difference is structural.

### Porter's Differentiation

- **Goal**: charge a price premium by offering unique value
- **Cost assumption**: differentiation typically costs more; accepted as tradeoff
- **Competitive reference**: still benchmarks against competitors (you're differentiating *from* them)
- **Test**: "Can we charge more because buyers prefer our product?"

### Blue Ocean Value Innovation

- **Goal**: simultaneously raise buyer value AND lower cost structure
- **Cost assumption**: eliminating and reducing factors that buyers don't value funds the raising and creating
- **Competitive reference**: competitors become irrelevant; you're creating demand from non-customers
- **Test**: "Does the new strategy attract buyers who previously rejected the category entirely?"

### Worked Diagnostic

A software company builds a $500/month project management tool with:
- Advanced AI-powered reporting (new, expensive to develop)
- 200+ integrations (industry standard, expensive to maintain)
- Premium 24/7 phone support (standard in enterprise tier)
- Clean, fast UI optimized for field workers (genuinely new)

**Is this Blue Ocean?**

Run the Four Actions test:
- What did they **Eliminate**? Nothing listed.
- What did they **Reduce**? Nothing listed.
- What did they **Raise**? AI reporting, UI quality.
- What did they **Create**? Field-worker optimization.

**Result**: This is Porter's Differentiation, not Blue Ocean. Cost structure went up (AI development, integrations maintenance). No cost savings fund the additions. To make it Blue Ocean, the team must identify which existing features field workers don't use and eliminate/reduce them to offset the new investment.

---

## Blue Ocean vs. Ansoff Matrix

Ansoff Matrix maps growth options on two axes: existing/new products × existing/new markets.

```
                    Existing Products    New Products
Existing Markets    Market Penetration   Product Development
New Markets         Market Development   Diversification
```

Blue Ocean most closely resembles **Market Development** (existing product, new market) or **Diversification** (new product, new market) — but differs in mechanism.

| Dimension | Ansoff New Market Entry | Blue Ocean |
|-----------|------------------------|-----------|
| Market definition | Pre-existing segment underserved | Market boundary reconstructed; segment may not exist yet |
| Customer source | Known non-buyers in adjacent segment | Non-customers who rejected the entire category |
| Product change | Usually minor adaptation | Value curve redesigned |
| Competition | Still present in new market | Aims to make competition irrelevant |

**When Ansoff suffices**: you know a geographic or demographic segment exists and is underserved. You adapt your existing product. No need to reconstruct the value curve.

**When Blue Ocean is needed**: buyers in a segment have consistently rejected the category for structural reasons (too expensive, too complex, wrong occasion). You need to rethink what value the category delivers.

---

## Blue Ocean vs. Jobs-to-Be-Done (JTBD)

JTBD (Christensen) and Blue Ocean overlap heavily on the customer insight side but differ in output.

| Dimension | Jobs-to-Be-Done | Blue Ocean |
|-----------|----------------|-----------|
| Core question | What job is the customer hiring this product to do? | Which competitive factors can we reconstruct to create new demand? |
| Unit of analysis | The customer's functional/social/emotional job | The industry's competitive factor set |
| Output | Product/service redesign brief | Strategy Canvas + Four Actions grid |
| Competition angle | Expand the competitive set (indirect substitutes as competitors) | Eliminate competition by creating uncontested space |
| Non-customer focus | Implicit (who isn't hiring current solutions?) | Explicit (Three Tiers of Non-Customers is a named tool) |

**How they complement each other**: JTBD is excellent as input to Blue Ocean's **Create** quadrant. When asking "what should we Create that the industry never offered?", JTBD interviews reveal unmet jobs that the entire industry ignores. The two frameworks run in sequence productively.

---

## Blue Ocean vs. BCG Matrix

BCG Matrix is a **portfolio management** tool for companies with multiple business units or product lines. It answers: where should capital flow?

Blue Ocean is a **competitive strategy design** tool. It answers: how should we redesign our value proposition?

They operate at different levels of analysis and almost never conflict, but teams sometimes confuse them when a "Cash Cow" product is in a declining red ocean and leadership asks whether to "Blue Ocean" it.

**The correct logic:**

```
BCG: "This product is a Cash Cow but market growth is declining."
     → BCG answer: harvest cash, don't invest heavily.
     
Blue Ocean question: "Can this product category be redefined?"
     → Separate question; BCG position tells you about current market
       dynamics, not about whether a new value curve is possible.
```

If the Cash Cow is declining because of commoditization (price war, feature convergence), Blue Ocean may be appropriate — but the decision to invest in that redesign requires a business case beyond BCG's output. BCG tells you the current state; Blue Ocean tells you what's possible.

---

## Framework Selection Flowchart

```
Start: What strategic question are you answering?
         │
         ├─► "Are we winning / where do we stand?"
         │       └─► SWOT, Value Chain, Competitive Intelligence
         │
         ├─► "Is this industry worth being in?"
         │       └─► Porter's Five Forces
         │
         ├─► "Where should we invest across our portfolio?"
         │       └─► BCG Matrix, Ansoff Matrix
         │
         ├─► "How do we grow within our current market?"
         │       └─► Porter's Generic Strategies (Cost Leadership, Differentiation, Focus)
         │           + OKRs for execution
         │
         ├─► "What trends will affect us?"
         │       └─► PESTEL
         │
         └─► "We're stuck in price competition / want to create new demand"
                 └─► Blue Ocean Strategy
                           │
                           └─► Use JTBD as input to the "Create" quadrant
                           └─► Run Five Forces on the proposed new space
                               AFTER the canvas is drawn (not before)
```

---

## Anti-Pattern: Using Blue Ocean as Rebranding for Differentiation

The most common failure mode in practice: a product team goes through the Four Actions exercise, produces a new value curve that looks like a parallel shift upward from competitors, and calls it Blue Ocean.

**How to detect this:**

1. Check if Eliminate and Reduce boxes are empty or filled with trivial items ("we'll stop offering our unpopular premium tier that 2% of customers use").
2. Check if the new value curve still converges with competitors on most factors and only diverges on 1-2 factors.
3. Check if the proposed customer base is a refined subset of current customers rather than current non-customers.

If any of these are true, the output is a differentiation play inside the existing red ocean — which may be the right answer, but should not be mislabeled.

**The correct label matters** because it changes the implementation mandate:
- True Blue Ocean → requires operational model redesign, not just product changes
- Porter Differentiation → can often be executed within the existing business model

---

## Summary Reference Card

| Framework | Primary Question | Key Output | When Blue Ocean Is Better |
|-----------|-----------------|-----------|--------------------------|
| Porter's Five Forces | Is this industry attractive? | Industry attractiveness score | When you want to reconstruct the industry, not just survive in it |
| Porter's Generic Strategies | How do we compete within the industry? | Position: cost, differentiation, or focus | When price war or feature war is the core problem |
| SWOT | Where do we stand? | Strengths/Weaknesses/Opportunities/Threats | When the problem is about strategic direction, not self-audit |
| BCG Matrix | How do we allocate capital? | Portfolio investment priorities | When the question is about a single product's value curve |
| Ansoff Matrix | How do we grow? | Growth vector (market/product × existing/new) | When new market means reconstructed demand, not just new segment |
| PESTEL | What external forces matter? | Macro trend scan | PESTEL is a *prerequisite* to Blue Ocean, not an alternative |
| Jobs-to-Be-Done | What is the customer actually hiring this for? | Job spec + design implications | JTBD feeds Blue Ocean's Create quadrant; they complement, not compete |
