# Strategy Framework Comparison: BCG Matrix vs Alternatives

This reference answers one question: **given a user's situation, should you use BCG Matrix or a different framework?** It covers the four most common alternatives with decision rules, not descriptions.

---

## Framework Selection Decision Tree

```
Is the user analyzing MULTIPLE products/BUs simultaneously?
├── No → BCG is wrong. Go to single-unit tools (SWOT, Blue Ocean, Porter's).
└── Yes ↓
    Does the user have (or can estimate) market share + market growth data?
    ├── No → Use GE-McKinsey (works with scored proxies, not hard ratios).
    └── Yes ↓
        Is the portfolio allocation decision primarily about cash flow?
        ├── Yes → BCG Matrix is the right tool.
        └── No (competitive strength, capabilities, fit matter equally)
            └── Use GE-McKinsey Matrix.
```

---

## Head-to-Head Comparison Table

| Dimension | BCG Matrix | GE-McKinsey | Ansoff Matrix | Porter's Five Forces |
|---|---|---|---|---|
| **Unit of analysis** | Multiple products/BUs | Multiple products/BUs | Single product + market combos | Single industry |
| **Primary output** | Cash allocation (invest / harvest / divest) | Investment priority (invest / hold / harvest) | Growth strategy (which market-product path) | Industry attractiveness score |
| **X-axis** | Relative market share | Business unit strength (composite) | Market: new vs existing | N/A |
| **Y-axis** | Market growth rate | Industry attractiveness (composite) | Product: new vs existing | N/A |
| **Data required** | Hard numbers: your share, leader's share, market growth % | Scored criteria: can use judgment | Qualitative: strategic intent | Qualitative: industry structure |
| **Time horizon** | Current snapshot → 3-year horizon | Current snapshot → 5-year horizon | Growth planning, 1-5 years | Structural, 5-10 years |
| **Handles synergies?** | No | Partial | No | No |
| **Complexity** | Low | High (requires weighting criteria) | Low | Medium |
| **Best used when** | Portfolio cash optimization, mature businesses with clear data | Large conglomerates, when market share data is unreliable | Deciding *how* to grow, not *what* to cut | Deciding whether to enter/exit an industry |

---

## BCG vs GE-McKinsey: When to Switch

GE-McKinsey is the most common BCG upgrade. Use this decision rule:

**Use BCG when:**
- You have reliable market share + growth data for each unit
- The primary question is "where does cash come from and where does it go?"
- Portfolio has 3-8 units (BCG gets cluttered beyond that)
- Speed matters: BCG can be sketched in a meeting

**Switch to GE-McKinsey when:**
- Market share data is unreliable or unavailable
- Some units operate in fundamentally different industries (hard to compare share figures)
- Competitive strength involves more than market share (e.g., brand, IP, distribution)
- The portfolio has >8 units (GE-McKinsey's composite scoring handles this better)
- Stakeholder needs a richer justification than a 2×2

### GE-McKinsey in Brief (for comparison only)

Two composite axes replace BCG's two hard metrics:

**Industry Attractiveness** (Y-axis) — weighted score of:
- Market size
- Market growth rate
- Profitability level
- Competitive intensity
- Cyclicality, regulation risk, etc.

**Business Unit Strength** (X-axis) — weighted score of:
- Relative market share ← same as BCG's X-axis, but one factor among many
- Profit margins vs competitors
- Brand strength
- Production capacity
- Technology advantage

Both axes scored 1-5 (or 1-10), then weighted. Each BU gets an (x, y) coordinate → placed in a 3×3 grid instead of 2×2.

**When BCG and GE-McKinsey give different answers:**

If BCG classifies a unit as a Dog (low share, low growth) but GE-McKinsey classifies it as Hold (high brand strength, moderate industry attractiveness), the discrepancy tells you something: BCG is measuring cash flow position; GE-McKinsey is measuring strategic value. Both can be correct simultaneously. Decide which lens matters more for the specific decision.

---

## BCG vs Ansoff: Complementary, Not Competing

These frameworks answer different questions. Do not substitute one for the other.

| Question | Right Framework |
|---|---|
| "Which products should we invest in?" | BCG |
| "How should we grow Product A?" | Ansoff |
| "Should we cut Product B?" | BCG |
| "Should Product A enter a new market?" | Ansoff |

**Ansoff Matrix:**

```
                  Existing Products    New Products
Existing Markets │ Market Penetration │ Product Development │
New Markets      │ Market Development │ Diversification     │
```

Risk increases as you move from top-left (lowest risk) to bottom-right (highest risk).

**Typical combined workflow:**

1. Run BCG first → identify Stars and Question Marks worth investing in
2. Run Ansoff on each selected unit → determine *how* to grow it

Example:
> BCG says Server Components is a Star. Ansoff says: should we grow by taking share in existing markets (Market Penetration) or by entering adjacent markets like cloud hardware (Market Development)? These are different strategies with different resource requirements.

BCG tells you the *size* and *direction* of the investment; Ansoff tells you the *type*.

---

## BCG vs Porter's Five Forces: Different Scope

Porter's Five Forces operates at the **industry level**, not the product/BU level.

- Porter answers: "Is this industry worth competing in?"
- BCG answers: "Given we're already competing, which bets should we make?"

**When Porter's precedes BCG:**

If a Question Mark is in a high-growth market but Porter's analysis reveals: (a) low barriers to entry, (b) commoditizing product, (c) buyer power is dominant → the "invest to capture share" BCG recommendation weakens significantly. The market is growing, but profitability may be structurally poor.

Rule: **Run Porter's on Question Mark markets before deciding to invest.** BCG's growth rate does not capture whether that growth creates profit.

---

## BCG vs SWOT: Not Comparable

SWOT is a single-unit diagnostic; BCG is a multi-unit allocation tool. The only relevant comparison:

**SWOT is the right choice (BCG is wrong) when:**
- User has one product or business unit
- User wants strengths/weaknesses/opportunities/threats inventory
- No resource allocation across units is required

If a user says "analyze my product strategy," clarify: do they have one product or many? One product → SWOT or similar. Multiple products → BCG.

**Combining them:** SWOT can be run on each BCG quadrant member to develop the specific action plan. BCG identifies *what to do*; SWOT on individual units helps figure out *how to do it*.

---

## Worked Example: Same Company, Two Frameworks

**Scenario:** Taiwanese B2B SaaS company, 5 products

| Product | Revenue (NT$M) | Market Growth | Your Share | Leader's Share | Rel. Share |
|---|---|---|---|---|---|
| ERP Core | 320 | 4% | 22% | 15% | **1.47x** |
| HR Module | 85 | 6% | 8% | 35% | **0.23x** |
| AI Analytics | 40 | 45% | 5% | 12% | **0.42x** |
| Legacy Billing | 110 | -3% | 18% | 25% | **0.72x** |
| Cloud Infra | 160 | 15% | 14% | 11% | **1.27x** |

**BCG output:**

```
                  High Share (>1.0x)    Low Share (<1.0x)
High Growth(>10%) ⭐ Cloud Infra        ❓ AI Analytics
Low Growth (<10%) 🐄 ERP Core           🐕 HR Module, Legacy Billing
```

**BCG recommendation:** Harvest ERP Core → fund Cloud Infra (Star) + selective invest in AI Analytics (Question Mark). Evaluate HR Module and Legacy Billing for divestiture.

**Now apply GE-McKinsey to AI Analytics before committing investment:**

AI Analytics is a Question Mark. Before investing, score its industry attractiveness:

| Factor | Weight | Score (1-5) | Weighted |
|---|---|---|---|
| Market growth (45%) | 30% | 5 | 1.50 |
| Market size | 20% | 3 | 0.60 |
| Competitive intensity (3 dominant players) | 25% | 2 | 0.50 |
| Profitability of market | 25% | 3 | 0.75 |
| **Industry Attractiveness** | | | **3.35 / 5** |

Score business unit strength:

| Factor | Weight | Score (1-5) | Weighted |
|---|---|---|---|
| Relative market share (0.42x) | 35% | 2 | 0.70 |
| Technology differentiation | 30% | 4 | 1.20 |
| Sales channel strength | 20% | 2 | 0.40 |
| Customer retention | 15% | 4 | 0.60 |
| **BU Strength** | | | **2.90 / 5** |

GE-McKinsey placement: Medium Industry Attractiveness, Medium-Low BU Strength → **Selective Investment / Hold**, not aggressive invest.

**Interpretation:** BCG says "possible Star candidate, invest." GE-McKinsey says "invest selectively, not aggressively." The discrepancy is caused by high competitive intensity that BCG's growth rate doesn't capture. Resolution: invest in AI Analytics at a lower resource level than Cloud Infra, with a clear 18-month milestone: if relative share hasn't improved from 0.42x to at least 0.6x, exit.

---

## Framework Selection Cheat Sheet

```
User has multiple products/BUs and needs allocation → BCG (first choice)
BCG data unavailable or unreliable → GE-McKinsey
BCG classification done, need growth direction for a unit → Ansoff
Question Mark in a high-growth market → run Porter's before investing
Single product analysis → SWOT (BCG is wrong tool)
Industry entry/exit decision → Porter's Five Forces
```
