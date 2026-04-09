# Issue Tree Templates by Problem Type

Issue trees decompose a problem into MECE sub-questions. This file contains ready-to-use templates for the most common business problem types, plus guidance on choosing the right decomposition logic.

---

## Decomposition Logic: The Three Approaches

Before picking a template, choose the decomposition logic:

| Logic | When to use | Example |
|-------|-------------|---------|
| **Component** | The problem has natural parts that add up to the whole | Revenue = Volume × Price |
| **Process / Causal** | You're tracing cause and effect through a sequence | Customer journey: Awareness → Consideration → Purchase → Retention |
| **Hypothesis** | You already have suspects; you're testing, not exploring | "Is it a pricing problem or a distribution problem?" |

Mix logic types across levels, but use only ONE logic per level. Never mix component and process decomposition at the same level — that's where MECE breaks down.

---

## Template 1: Profit Decline

**Trigger phrase**: "Profit is down", "margins are shrinking", "EBITDA fell"

**Decomposition logic**: Component (financial identity)

```
Profit declining
├── Revenue declining?                        [Component: Profit = Revenue − Cost]
│   ├── Volume declining?                     [Component: Revenue = Volume × Price]
│   │   ├── Existing customer purchases down?
│   │   │   ├── Purchase frequency down?
│   │   │   └── Basket size down?
│   │   └── New customer acquisition down?
│   │       ├── Top-of-funnel traffic down?
│   │       └── Conversion rate down?
│   └── Price declining?
│       ├── List price reduced?
│       ├── Discounting / promotion increased?
│       └── Product mix shifted toward lower-priced SKUs?
└── Costs increasing?                         [Component: Costs = COGS + OpEx]
    ├── COGS increasing?
    │   ├── Input costs up? (materials, labor, energy)
    │   └── Production efficiency down? (waste, yield)
    └── OpEx increasing?
        ├── Headcount / compensation up?
        ├── Marketing spend up?
        └── G&A up?
```

**MECE check**: Profit = Revenue − Cost is an accounting identity. Every dollar of profit change must flow through one of these two branches. No overlap, no gaps. ✓

**First branch to prioritize**: Compare revenue trend vs. cost trend before going deeper. If revenue is flat and cost spiked, skip the entire revenue subtree.

---

## Template 2: Market Share Loss

**Trigger phrase**: "We're losing share", "competitors are winning", "our growth is slower than the market"

**Decomposition logic**: Component (share = our growth vs. market growth)

```
Market share declining
├── Our volume growing slower than market?    [Root cause: relative growth]
│   ├── Our new customer acquisition lagging?
│   │   ├── Reach / awareness lower?
│   │   └── Win rate / conversion lower?
│   │       ├── Product perceived as inferior?
│   │       └── Price perceived as too high?
│   └── Our customer retention lower?
│       ├── Churn higher than competitors?
│       │   ├── Product satisfaction lower?
│       │   └── Competitor switching offers better?
│       └── Expansion revenue lower?
│           └── Upsell / cross-sell underperforming?
└── Market definition changed?               [Structural question — before diving into metrics]
    ├── New segment entered the market we don't serve?
    └── Existing competitor expanded into adjacent segment we own?
```

**Note on the second branch**: Always check structural market changes before assuming an operational failure. If a new competitor entered your segment, no amount of marketing spend will fix the "share loss" — the market itself changed.

---

## Template 3: Growth Strategy ("How do we grow?")

**Trigger phrase**: "We want to grow", "what are our growth options", "how do we hit our targets"

**Decomposition logic**: Ansoff Matrix (product × market)

```
Growth options
├── Existing products, existing markets        [Market Penetration]
│   ├── Increase purchase frequency?
│   ├── Increase basket size?
│   └── Reduce churn?
├── New products, existing markets             [Product Development]
│   ├── Adjacent product extensions?
│   └── New product lines for same customers?
├── Existing products, new markets             [Market Development]
│   ├── New geographies?
│   ├── New customer segments?
│   └── New channels?
└── New products, new markets                  [Diversification]
    ├── Related diversification (same capabilities)?
    └── Unrelated diversification?
```

**Usage rule**: The Ansoff decomposition is exhaustive by construction (2×2 matrix covers all combinations). Prioritize branches by feasibility and time-to-revenue, not by theoretical attractiveness. Market Penetration is almost always faster and cheaper than the other three.

**MECE note**: "New" vs. "existing" must be defined before you start. If your current product sells to SMBs, is "enterprise" a new market or an existing market? Lock the definition, then apply the tree.

---

## Template 4: Customer Churn

**Trigger phrase**: "Customers are leaving", "retention is down", "NPS is falling"

**Decomposition logic**: Process (customer journey — causal chain)

```
Churn increasing
├── Customers never became active?             [Onboarding failure]
│   ├── Did not complete setup?
│   └── Completed setup but never found value? (time-to-value too long)
├── Active customers losing engagement?        [Usage decline]
│   ├── Product no longer solves their problem?
│   │   ├── Customer's problem changed?
│   │   └── Product stopped keeping up?
│   └── Competitor solves it better?
│       ├── Feature gap?
│       └── Price gap?
└── Renewal decision failed?                   [Commercial failure]
    ├── Economic buyer changed and doesn't know the product?
    ├── Budget cut / company downturn?
    └── Contract terms unfavorable?
```

**Key diagnostic question before branching**: At what point in the lifecycle do customers churn? Pull churn data segmented by tenure (days since first purchase or activation). If most churn happens in month 1, the issue is in the onboarding branch. If churn spikes at renewal, the issue is in the commercial branch. This prevents wasting analysis on the wrong subtree.

---

## Template 5: Operational Failure ("Why is X broken?")

**Trigger phrase**: "This process is broken", "quality is falling", "SLA is being missed"

**Decomposition logic**: Fishbone / 6M (inputs to a process)

```
Process output failing
├── People?
│   ├── Skill gap — don't know how?
│   └── Will gap — know how but aren't doing it?
├── Process?
│   ├── Process is poorly designed?
│   └── Process exists but isn't followed?
├── Technology / Tools?
│   ├── Tool doesn't exist?
│   └── Tool exists but is unreliable or slow?
├── Materials / Inputs?
│   ├── Input quality degraded?
│   └── Input availability reduced?
├── Measurement?
│   ├── We're measuring the wrong thing?
│   └── Measurement lag hides the real problem?
└── Environment / External?
    ├── Regulatory change?
    └── Supplier / partner failure?
```

**MECE check**: The 6M categories (Man, Machine, Method, Material, Measurement, Mother Nature) are a standard exhaustive decomposition of process inputs. They are mutually exclusive by definition. ✓

**Prioritization heuristic**: People and Process failures are more common than Technology and Materials failures. Start there unless you have specific data pointing elsewhere.

---

## Template 6: Investment / Build-vs-Buy Decision

**Trigger phrase**: "Should we build or buy?", "is this worth investing in?", "make or outsource?"

**Decomposition logic**: Decision tree (binary choices)

```
Should we invest in X?
├── Is there a strategic need?                 [Gate 1 — exit if No]
│   ├── Does X solve a customer problem we've validated?
│   └── Does X fit our strategic priorities?
├── Can we do it ourselves?                    [Gate 2]
│   ├── Do we have the capabilities?
│   └── Do we have the capacity?
└── Should we do it ourselves?                 [Gate 3 — if Yes to Gate 2]
    ├── Build?
    │   ├── Cost to build < cost to buy over 3Y?
    │   └── Is differentiation high enough to justify?
    ├── Buy (acquire)?
    │   ├── Target exists at acceptable valuation?
    │   └── Integration cost manageable?
    └── Partner / license?
        ├── Partner available with acceptable terms?
        └── Dependency risk acceptable?
```

**MECE note**: This tree uses sequential gating, not full MECE decomposition. Gate 1 and 2 are filters — only proceed if the answer is Yes. The final level (Build / Buy / Partner) is MECE: these are the three ways to obtain a capability externally defined.

---

## Template 7: Pricing Problem

**Trigger phrase**: "Is our pricing right?", "are we leaving money on the table?", "pricing is hurting conversion"

**Decomposition logic**: Value-based pricing framework

```
Pricing suboptimal
├── Price too high? (losing volume)
│   ├── Absolute price above willingness-to-pay?
│   │   ├── WTP data: surveys, conjoint, or price tests?
│   │   └── Conversion funnel: at which step are users dropping?
│   └── Perceived value < price?
│       ├── Value proposition unclear?
│       └── Competitors perceived as better value at lower price?
└── Price too low? (leaving money on the table)
    ├── Customer willingness-to-pay higher than current price?
    │   ├── Price sensitivity tests show headroom?
    │   └── Customers report price is "surprisingly low"?
    └── Price signals low quality?
        ├── Category where price = quality signal?
        └── Conversion increases with price (Veblen effect)?
```

**Diagnostic before branching**: Run a simple price elasticity test. If demand is inelastic (price up 10% → volume down <10%), you're leaving money on the table. If demand is highly elastic, you may be priced too high. This single data point tells you which branch to investigate.

---

## How to Build a Custom Issue Tree

When none of the above templates fit, build from scratch using this procedure:

**Step 1: Write the problem as a question**
"Why is X happening?" or "How do we achieve Y?" — never a statement.

**Step 2: Pick your decomposition logic**
- If the problem has a mathematical identity (Profit = Revenue − Cost), use it. Identity-based trees are always MECE.
- If the problem is a process, decompose by stage (Awareness → Consideration → Purchase → Retention).
- If the problem is a decision, decompose by the alternatives.

**Step 3: Draft the first level (3-5 branches)**
Write them out. Then run the MECE test:

```
MECE Test Checklist:
□ Mutually Exclusive: Pick any two branches. Can one event fall into both? If yes → overlap → not MECE
□ Collectively Exhaustive: Is there any scenario that falls into NONE of the branches? If yes → gap → not MECE
```

**Step 4: Add qualifiers if categories blur**
Sometimes categories are near-MECE. Document the edge cases: "Churn is counted as month 1 if it occurs before first purchase; month 2+ if it occurs after." Defining the boundary is acceptable — pretending the boundary doesn't exist is not.

**Step 5: Go only 2-3 levels deep in the initial tree**
A 4-level tree at the start signals over-engineering. Build to the level where you can write a testable hypothesis. That's the right depth.

---

## Anti-Patterns in Issue Trees

**Overlap (non-ME)**

```
Revenue problem
├── Online sales down          ← "Online" can also be "Enterprise"
├── Enterprise sales down
└── Growth segment down        ← "Growth" is a strategy, not a channel
```
Fix: Pick one dimension. Channel OR segment OR product — not a mix.

**Gaps (non-CE)**

```
Why did customer churn?
├── Product dissatisfaction
└── Price sensitivity
```
Missing: Competitor switch, company bankruptcy, contact change. Not exhaustive.

**Action masquerading as diagnosis**

```
How do we grow?
├── Run more ads
├── Launch referral program
└── Expand to new market
```
These are solutions, not MECE decomposition of the problem space. An issue tree maps the problem, not the solution. Solutions come after the tree identifies which branch is the real issue.

**Recursive categories**

```
Why is engagement down?
├── Users are less engaged
└── Active users are churning
```
"Users are less engaged" is a restatement of the problem, not a decomposition of it.
