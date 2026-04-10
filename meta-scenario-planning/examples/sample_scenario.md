# Example: Formosa Data — AI-Native Pivot Decision

## Scenario

**Company**: Formosa Data Co., a Taipei-based B2B analytics SaaS with NT$180M ARR, 85 enterprise clients
(manufacturing, logistics, retail) mostly in Taiwan and Malaysia.

**Situation**: The founding team is debating whether to invest NT$60M over 18 months to rebuild the
product as AI-native (natural-language queries, agentic reporting, LLM-powered anomaly detection).
Their current BI product is stable but sales growth has stalled at 8% YoY. A mid-2027 board review
will evaluate the decision.

**Question from CEO**: "Should we commit to an AI-native rebuild? What futures are we betting on —
and what happens if we're wrong?"

---

## Analysis

### Step 1: Driving Forces

Brainstormed 12 forces; rated by Impact × Uncertainty:

| Force | Impact | Uncertainty | Notes |
|-------|--------|-------------|-------|
| Enterprise AI adoption pace | H | H | ✓ **axis candidate** |
| Hyperscaler bundling (MS Fabric, Google Looker AI) | H | H | ✓ **axis candidate** |
| LLM API cost trajectory | H | M | Costs falling but rate unclear |
| Taiwan enterprise IT budget cycles | M | M | Historically conservative |
| Regulatory AI disclosure requirements (EU AI Act spillover) | M | H | Could hit MNC clients |
| Talent availability (ML engineers in Taiwan) | M | H | Competitive, but not a pivot decider |
| Client data residency laws (Malaysia PDPA) | M | M | Manageable, not a pivot driver |
| Recession risk / budget freezes | H | M | Macro risk, secondary to core question |
| Open-source LLM quality (Llama, Qwen) | M | H | Could erode moat if self-hostable |
| Competitor pivot timing (regional BI players) | M | M | Followers, not leaders |
| PE/VC appetite for AI SaaS in SEA | L | H | Exit concern, not strategy driver |
| Founder execution bandwidth | M | L | Known constraint, not an axis |

**Selected axes**: Enterprise AI Adoption Pace × Hyperscaler Competitive Intensity
- Both are high-impact AND high-uncertainty
- They are reasonably independent: hyperscalers can be aggressive even if enterprises are slow

---

### Step 2: Two Axes

- **Axis 1 — Enterprise AI Adoption**: *Slow* (CIOs cautious, POCs stall, 2-3 year lag) vs. *Fast*
  (boardroom AI mandates, budgets unlocked, 12-18 month procurement cycles)
- **Axis 2 — Hyperscaler Competitive Intensity**: *Fragmented* (Microsoft/Google focus on Fortune 500,
  mid-market underserved) vs. *Bundled* (MS Fabric + Copilot sold at discount to SME/mid-market,
  price pressure on standalone BI)

---

### Step 3: Four Scenarios (2027–2029 horizon)

| | **Adoption: Slow** | **Adoption: Fast** |
|---|---|---|
| **Hyperscalers: Fragmented** | **"The Waiting Room"** | **"Gold Rush"** |
| **Hyperscalers: Bundled** | **"Slow Squeeze"** | **"Survival of the Differentiated"** |

**"The Waiting Room"** *(Slow adoption + Fragmented hyperscalers)*
Enterprises keep AI on the roadmap but don't buy. IT committees demand ROI proof. Hyperscalers focus
their AI push on U.S. enterprise; Taiwan/SEA mid-market sees minimal pricing pressure. Formosa Data's
current BI product still competes comfortably, but growth stays flat at 6–10% YoY. The window to
rebuild AI-native exists, but there's no urgency — and no AI revenue for 18 months post-rebuild.

**"Gold Rush"** *(Fast adoption + Fragmented hyperscalers)*
Enterprise AI budgets unlock. CIOs want AI-native analytics, and hyperscalers haven't flooded the
mid-market. Regional specialists who move first capture a land-grab opportunity. Formosa Data, if
AI-native by mid-2027, can close NT$30–50M in new logos in 12 months. This is the scenario the
board is most excited about. Risk: the rebuild has to actually ship.

**"Slow Squeeze"** *(Slow adoption + Bundled hyperscalers)*
The worst scenario. Enterprises aren't buying AI features, but Microsoft bundles Copilot + Fabric into
existing EA agreements at no incremental cost. Formosa Data's traditional BI faces pricing pressure
from "good enough" bundled tools. ARR erodes 10–15% annually. An AI rebuild doesn't help because
the demand isn't there to monetize it.

**"Survival of the Differentiated"** *(Fast adoption + Bundled hyperscalers)*
Enterprises want AI analytics, but hyperscalers capture the commodity layer. Surviving independents
win only on vertical depth: Formosa Data's manufacturing KPI library, Bahasa Malaysia support, and
OT/SCADA data connectors become genuine moats. A generic AI-native rebuild isn't enough — the
product must be **industry-specific** AI, not just AI. Mid-market clients who can't afford deep
customization from Microsoft turn to specialists.

---

### Step 4: Strategy Robustness Test

Three candidate strategies evaluated:

| Strategy | "Waiting Room" | "Gold Rush" | "Slow Squeeze" | "Survival of Diff." |
|----------|---------------|-------------|----------------|----------------------|
| **A. Full AI-native rebuild** (NT$60M, ship mid-2027) | △ Cost sunk, no near-term payoff | ✓ Perfect timing | ✗ Accelerates cash burn, no demand | △ Only works if rebuild is vertical-specific |
| **B. Stay traditional BI, bolt-on AI features** (NT$15M, additive) | ✓ Preserves cash, keeps clients | △ Late mover, loses new logos | ✓ Preserves margin during squeeze | ✗ Underdifferentiated when depth matters |
| **C. Vertical-AI rebuild — manufacturing + logistics depth** (NT$45M) | △ Conservative payoff | ✓ Wins industry-specific deals | △ Better than A, vertical clients sticky | ✓ Best fit: depth beats commodity AI |

**Legend**: ✓ Works well · △ Partial / mixed · ✗ Damages position

---

## Result

### Robust Strategy

**Strategy C — Vertical-AI rebuild (manufacturing + logistics)** is the most robust:
- Works well in the upside scenario (Gold Rush)
- Survives the differentiation war (Survival of the Differentiated)
- Avoids catastrophic downside in the Slow Squeeze (vertical clients churn less than horizontal ones)
- Only weak in The Waiting Room, but the cash spend is lower (NT$45M vs NT$60M), buying more runway

The generic AI-native rebuild (Strategy A) is fragile — it is a bet that only pays off in one scenario
and destroys value in the worst one.

### Contingency Triggers

| Early Signal | Indicates Scenario | Action |
|---|---|---|
| ≥3 existing clients request NL query features unprompted by Q3 2026 | Gold Rush or Survival | Accelerate rebuild timeline, hire 2 ML engineers immediately |
| Microsoft announces SEA mid-market EA bundle below NT$8K/seat | Slow Squeeze | Pause rebuild, shift to customer success and retention mode |
| Manufacturing client POC converts to paid within 6 months | Survival of the Differentiated | Double down on vertical depth; deprioritize horizontal features |
| CIO survey shows <20% have internal AI projects approved for 2027 | Waiting Room | Extend current product lifecycle; defer NT$45M rebuild by 12 months |

### Recommended Decision

Commit to **Strategy C** with a staged gate: invest NT$15M through Q3 2026 on vertical AI features
(manufacturing anomaly detection, logistics ETA prediction). Review in October 2026 against triggers
above before releasing the remaining NT$30M for the full rebuild. This converts a binary NT$60M bet
into a staged option that stays rational across all four scenarios.
