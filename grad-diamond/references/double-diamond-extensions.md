# Double Diamond Extensions: Beyond Porter's Single-Country Model

## Why the Single Diamond Falls Short

Porter's Diamond (1990) was calibrated on ten large, relatively self-sufficient economies (the US, Germany, Japan, the UK, Switzerland, etc.). For these countries, domestic demand and domestic rivalry are the primary engines of international competitiveness. The model has a structural assumption baked in: the home base matters most, and the home base is a single country.

This assumption breaks down in three recurring situations:

| Situation | Why Single Diamond Misdiagnoses | Example |
|-----------|--------------------------------|---------|
| Small open economy | Domestic market too small to generate demanding customers at scale | Canada, Singapore, New Zealand |
| Deeply integrated economic bloc | "Domestic" and "foreign" rivalry are legally indistinguishable | Netherlands in EU manufacturing |
| MNC-anchored industry | Competitive advantage is assembled across borders by multinationals | Korean chaebols' global supply chains |

The extensions below address each situation.

---

## 1. Rugman's Double Diamond (1993)

### Core Argument

Alan Rugman and Joseph D'Cruz (*Journal of International Business Studies*, 1993) argued that for Canada, the relevant "home base" is not Canada alone — it is the Canada-US integrated market. A Canadian auto-parts manufacturer competes against American firms for American customers under the same trade rules. Forcing this into a single-country diamond produces a "weak diamond" verdict that is empirically wrong.

The Double Diamond adds an **international diamond** alongside the domestic one. Competitive advantage emerges from whichever diamond is stronger, or from the interaction between both.

### Structure

```
              INTERNATIONAL DIAMOND
         ┌────────────────────────────────┐
         │  Factor Conditions (global)    │
         │  Demand Conditions (export)    │
         │  Related Industries (MNC nets) │
         │  Rivalry (global competitors)  │
         └────────────────────────────────┘
                        │
               reinforcement /
               substitution
                        │
              DOMESTIC DIAMOND
         ┌────────────────────────────────┐
         │  Factor Conditions (domestic)  │
         │  Demand Conditions (home mkt)  │
         │  Related Industries (clusters) │
         │  Rivalry (local competitors)   │
         └────────────────────────────────┘
```

**Key operational rule**: If the international diamond is stronger for a given determinant, it *substitutes* for domestic weakness. If both are strong, they *compound* each other.

### Substitution vs. Compounding

| Determinant | Domestic | International | Verdict |
|-------------|----------|---------------|---------|
| Factor Conditions | Weak (small talent pool) | Strong (MNC R&D imports talent) | Substitution — acceptable |
| Demand Conditions | Weak (small home market) | Strong (access to demanding export markets) | Substitution — acceptable |
| Related Industries | Weak (no local cluster) | Strong (integrated into foreign cluster) | Substitution — acceptable |
| Rivalry | Weak (protected domestic oligopoly) | **Cannot be substituted** | Fatal weakness — see note |

**Note on rivalry**: Rugman and subsequent researchers agree that **domestic rivalry cannot be substituted by international rivalry**. Domestic firms that are protected at home do not develop the reflexes needed to compete globally, even if they face international competitors eventually. This is the one place where Porter's insight holds even in a double diamond.

---

## 2. Moon-Rugman-Verbeke Generalized Double Diamond (1995, 1998)

### The Generalization

Moon, Rugman, and Verbeke (*Journal of International Business Studies*, 1998) formalized the double diamond into a **Generalized Double Diamond (GDD)** that works for any country, not just Canada. The key innovation: each determinant is measured on two axes — domestic and international — and the effective strength is the *weighted combination*.

### GDD Determinant Formula

For each determinant *d*, effective strength:

```
E(d) = α · D(d) + (1 − α) · I(d)
```

Where:
- `D(d)` = domestic score for determinant *d* (0–10 scale)
- `I(d)` = international score for determinant *d* (0–10 scale)
- `α` = domestic weight (0 to 1), determined by **economic openness**

**Calibrating α:**

```
α = 1 − (Exports + Imports) / (2 × GDP)
```

For a closed economy (α → 1.0): reduces to Porter's single diamond.
For a small open economy (α → 0.3): international diamond dominates.

**Worked example — Singapore semiconductor industry (illustrative):**

Singapore trade openness ratio ≈ 170% of GDP → very high openness.

```
α = 1 − (170% / 2) = 1 − 0.85 = 0.15
```

So international determinants carry **85% weight** in Singapore's GDD. A domestic demand conditions score of 4/10 and an international score of 9/10:

```
E(demand) = 0.15 × 4 + 0.85 × 9 = 0.60 + 7.65 = 8.25 / 10
```

Single diamond would rate this 4/10 (weak). GDD rates it 8.25/10 (strong). The discrepancy explains why Singapore's semiconductor industry is more competitive than its domestic market size suggests.

---

## 3. The Nine-Factor Model (Moon et al., extended)

A further extension adds **human factors** and **physical factors** as explicit sub-dimensions, producing nine cells instead of four. This is more granular than the standard diamond and is used in comparative country studies.

```
Factor Conditions:
  ├── Physical endowment (land, climate, resources)
  └── Human endowment (skills, knowledge, entrepreneurship)

Demand Conditions:
  ├── Domestic demand (size, sophistication)
  └── International demand (export market quality)

Related & Supporting Industries:
  ├── Supplier industries (upstream)
  └── Related industries (horizontal spillovers)

Firm Strategy, Structure & Rivalry:
  ├── Business environment (culture, capital markets)
  └── Competitive rivalry (domestic intensity)

+ Government (policy coherence)
```

The nine-factor model is operationally heavier; use it when:
- You need to compare **multiple countries** for the same industry
- The client requires a scored output rather than qualitative assessment
- The standard four-determinant analysis produces ties or ambiguous ratings

---

## 4. Decision Framework: Which Model to Apply

```
Step 1: Is the country a large, self-sufficient economy?
        (US, Germany, Japan, China, UK, France)
        YES → Use Porter's Single Diamond. The home base dominates.
        NO  → Proceed to Step 2.

Step 2: Is the industry MNC-dominated?
        (Subsidiaries of foreign multinationals provide most of
         the employment, R&D, or exports in this industry)
        YES → Use Double Diamond; international determinants
               substitute for domestic weaknesses via MNC linkages.
        NO  → Proceed to Step 3.

Step 3: Trade openness ratio (Exports + Imports) / GDP:
        < 60%  → Use Single Diamond with caution
        60–120% → Use Double Diamond
        > 120% → Use GDD with α ≤ 0.4; international diamond dominates
```

---

## 5. Worked Example: Korea's Semiconductor Industry

This example shows how to move from single diamond to double diamond when the analysis produces a misleading result.

### Single Diamond Assessment (Porter)

| Determinant | Assessment | Rating |
|-------------|-----------|--------|
| Factor Conditions | Strong engineering talent; heavy STEM investment | Strong |
| Demand Conditions | Korean domestic electronics market is large but not globally sophisticated relative to US/Japan | Moderate |
| Related & Supporting Industries | Strong domestic chemical, equipment supply chains; Suwon cluster | Strong |
| Firm Strategy & Rivalry | Samsung-SK Hynix duopoly; intense rivalry but oligopolistic | Moderate |

**Single diamond verdict**: Moderate-Strong. But this undersells the industry's actual global dominance. Why?

### Where the Single Diamond Fails

Demand Conditions is rated Moderate because Korean domestic demand for memory chips is not especially sophisticated or anticipatory. Yet Samsung and SK Hynix shape global memory standards. The domestic demand signal is the wrong signal.

### Double Diamond Correction

**International diamond — Demand Conditions**:
- Samsung and SK Hynix supply Apple, Nvidia, AWS, and hyperscalers
- These customers are among the most demanding semiconductor buyers in the world
- They provide detailed specifications, co-development pressure, and volume scale

```
D(demand) = 5/10  (domestic: adequate but not anticipatory)
I(demand) = 10/10 (global hyperscaler customers)
α for Korea: trade openness ~80%, so α ≈ 1 − 0.40 = 0.60

E(demand) = 0.60 × 5 + 0.40 × 10 = 3.0 + 4.0 = 7.0 / 10
```

This raises the demand rating from Moderate to Strong, consistent with Korea's observable global competitiveness.

### Corrected Double Diamond Assessment

| Determinant | Domestic | International | α-Weighted | Rating |
|-------------|----------|---------------|-----------|--------|
| Factor Conditions | 8 | 7 (global talent attraction) | 7.6 | Strong |
| Demand Conditions | 5 | 10 (hyperscalers) | 7.0 | Strong |
| Related & Supporting | 8 | 6 (some import dependency in EUV) | 7.2 | Strong |
| Rivalry | 6 | 7 (TSMC, Micron pressure) | 6.4 | Moderate-Strong |

**Double diamond verdict**: Strong overall — consistent with observed reality.

---

## 6. Multi-Country Diamond: When to Drop the Single-Country Frame

Rugman's Canadian work led to a broader insight: **some industries have no single-country home base**. The diamond spans borders institutionally, not just via MNC linkages.

Criteria for invoking a multi-country diamond:

1. **Regulatory integration**: industry operates under a unified regulatory framework across countries (EU single market, USMCA automotive rules of origin)
2. **Cluster continuity**: physical cluster spans a border (US-Canada auto corridor, Basel pharma cluster across CH/DE/FR)
3. **Indistinguishable rivalry**: firms in country A and country B face identical competitive pressure from the same rivals

**Procedure for multi-country diamond**:

1. Define the relevant economic zone (e.g., EU, NAFTA/USMCA zone)
2. Aggregate determinant scores across the zone using population or GDP weights
3. Treat cross-border clusters as a single "related industries" node
4. Note which government (which country's policies) matters most for each determinant

**What NOT to do**: do not simply average two national diamonds. The multi-country diamond is a single diamond with a redefined geographic scope.

---

## 7. Limitations of the Extensions

These models address the openness problem but introduce their own constraints:

**Double Diamond / GDD limitations**:
- The α weighting formula is empirically derived from trade ratios, not from the industry being analyzed. A semiconductor cluster in a trade-open country may still be domestically anchored.
- Scoring `I(d)` (international diamond determinants) requires data on foreign customer sophistication, global rival intensity, and international cluster linkages — often harder to gather than domestic data.
- The model does not explain *how* a firm gains access to the international diamond. A small domestic firm in Singapore cannot easily tap hyperscaler demand; an MNC subsidiary can. The firm's organizational form mediates access to the international diamond.

**Multi-country Diamond limitations**:
- Requires political stability of the integration zone. Brexit made UK-EU pharmaceutical clusters analytically ambiguous overnight.
- Obscures distributional questions: who captures the advantage within the multi-country zone?

**Shared limitation with Porter**:
All diamond variants are descriptive and diagnostic, not predictive. They explain why advantage existed, not whether it will persist. For a forward-looking assessment, combine with dynamic capabilities frameworks or technology lifecycle analysis.

---

## Key Sources

- Rugman, A.M. & D'Cruz, J.R. (1993). "The 'Double Diamond' Model of International Competitiveness: The Canadian Experience." *Management International Review*, 33(2), 17–39.
- Moon, H.C., Rugman, A.M., & Verbeke, A. (1998). "A Generalized Double Diamond Approach to the Global Competitiveness of Korea and Singapore." *International Business Review*, 7(2), 135–150.
- Rugman, A.M. & Verbeke, A. (2003). "Extending the Theory of the Multinational Enterprise: Internalization and Strategic Management Perspectives." *Journal of International Business Studies*, 34(2), 125–137.
