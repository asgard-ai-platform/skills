# OLI Formalization: Mathematical Structure and Extensions

## Core Formalization (Dunning 1981, 1988)

Dunning expressed the FDI decision as a net advantage condition. Let:

- **O** = firm-specific ownership advantage (net of acquisition cost)
- **L** = location advantage of foreign site relative to home country
- **I** = internalization advantage (internalizing O vs. licensing it to a foreign firm)

FDI is chosen over alternatives if and only if:

```
FDI is optimal ⟺  O > 0  AND  L > 0  AND  I > 0
```

This tri-condition is not additive. Each must independently be positive — a strong O cannot compensate for zero L.

### Formal Profit Comparison

Let π denote expected profit for each entry mode:

```
π_FDI      = R(O, L) − C_internal
π_Export   = R(O, L_home) − T            (T = transport + tariff costs)
π_License  = Royalty(O) − C_contract     (C_contract = monitoring + enforcement)
π_NoEntry  = 0
```

FDI is preferred when:

```
π_FDI > max(π_Export, π_License, π_NoEntry)
```

Substituting and simplifying:

```
R(O, L) − C_internal > R(O, L_home) − T     →  L advantage condition
R(O, L) − C_internal > Royalty(O) − C_contract  →  I advantage condition
R(O, L) − C_internal > 0                        →  O advantage condition
```

The three inequalities correspond exactly to the O, L, and I conditions. Missing any one flips the inequality and a different mode dominates.

---

## Transaction Cost Interpretation of I

The internalization advantage is derived from Williamson's transaction cost economics (TCE). Dunning borrowed this to operationalize *why* a firm internalizes rather than contracts.

Define transaction costs for licensing as:

```
C_contract = C_search + C_negotiation + C_monitoring + C_enforcement + C_opportunism
```

Where:

| Cost Component | Driver |
|----------------|--------|
| C_search | Finding a qualified licensee |
| C_negotiation | Bargaining under information asymmetry |
| C_monitoring | Verifying licensee quality and effort |
| C_enforcement | Legal costs when contract is breached |
| C_opportunism | Expected loss from licensee free-riding or knowledge leak |

Internalization is preferred when:

```
C_contract > (C_internal − C_internal_optimal)
```

i.e., the excess cost of managing an internal foreign operation over the optimal home operation is less than the transaction costs of contracting.

### Tacitness Coefficient

Kogut & Zander (1993) operationalized the hardest-to-contract component — tacit knowledge — as a tacitness coefficient **τ ∈ [0, 1]**:

- τ = 0: fully codifiable knowledge (blueprint, manual) → cheap to license
- τ = 1: fully tacit knowledge (embedded in team routines) → market failure, internalize

In practice, estimate τ by asking: *Can the knowledge be fully specified in a contract without losing value?* If no, τ is high, and I advantage is strong.

```
I_advantage ≈ f(τ, asset_specificity, frequency, uncertainty)
```

This is the TCE "fundamental transformation" applied to knowledge assets.

---

## Location Advantage Decomposition (Dunning 1998 OLI-IP)

Dunning later decomposed L into four motivational sub-types, each with distinct measurable proxies:

### L₁: Market-Seeking

```
L₁ = α₁·MarketSize + α₂·GrowthRate + α₃·TariffBarrier
```

- **MarketSize**: GDP or industry TAM in target country
- **GrowthRate**: CAGR of relevant demand segment
- **TariffBarrier**: ad valorem tariff equivalent; high tariff → export is blocked → L₁ increases

Proxy threshold: L₁ is strong if TariffBarrier > 15% OR MarketSize places target in top-10 globally for the sector.

### L₂: Resource-Seeking

```
L₂ = β₁·(w_home − w_foreign)/w_home + β₂·ResourceRent + β₃·SkillAvailability
```

- **w_home − w_foreign**: wage differential (positive = foreign cheaper)
- **ResourceRent**: differential access to raw material rents unavailable at home
- **SkillAvailability**: specialized talent concentration (e.g., semiconductor engineers in Taiwan)

### L₃: Efficiency-Seeking

```
L₃ = γ₁·ScaleEconomy + γ₂·TaxDifferential + γ₃·RegulatoryBurden
```

Efficiency-seeking L often dominates after the firm already has market or resource operations — it is an optimization motive, not an initial entry motive.

### L₄: Strategic Asset-Seeking

```
L₄ = δ₁·ClusterDensity + δ₂·R&DSpillover + δ₃·PartnerAccess
```

- **ClusterDensity**: concentration of industry peers, suppliers, research institutions
- **R&DSpillover**: patent output in target region for the firm's technology class
- **PartnerAccess**: availability of acquisition targets or alliance partners with complementary assets

**Note**: L₄ is qualitatively different from L₁–L₃. The firm is not exploiting an existing O advantage in a favorable location — it is *acquiring* new O advantages through FDI itself. This creates a feedback loop: FDI builds O, which enables future FDI.

---

## OLI Configuration Matrix (Formal)

Mapping all 8 binary combinations of {O, L, I} ∈ {0,1}:

| O | L | I | Implication | Recommended Mode |
|---|---|---|-------------|-----------------|
| 1 | 1 | 1 | Full FDI conditions met | WOS or JV (see I strength) |
| 1 | 1 | 0 | No internalization advantage | Licensing or franchising |
| 1 | 0 | 1 | No location pull | Produce at home, export |
| 1 | 0 | 0 | Only ownership advantage | Export (lowest commitment) |
| 0 | 1 | 1 | Location and I but no O | Do not invest; partner with local firm that has O |
| 0 | 1 | 0 | Location only | Local sourcing, not FDI |
| 0 | 0 | 1 | Internalization only | Internal restructuring, not internationalization |
| 0 | 0 | 0 | No advantages | Stay domestic |

The (O=0, L=1, I=1) case is often missed: a firm should not attempt FDI just because the location is attractive and it fears opportunism — without O it has nothing to exploit or protect.

---

## Entry Mode Selection Within O+L+I = 1

When all three conditions hold, a secondary decision distinguishes Wholly-Owned Subsidiary (WOS) from Joint Venture (JV). This depends on the *strength* of I and *level of country risk*:

```
Mode = WOS   if  I_strength = HIGH  AND  Country_Risk = LOW
Mode = JV    if  I_strength = MODERATE  OR  Country_Risk = HIGH
```

Formalized as a 2×2:

|  | Country Risk LOW | Country Risk HIGH |
|--|-----------------|------------------|
| **I Strong** | WOS (full control, stable) | Acquisition with local JV clause (hedge) |
| **I Moderate** | JV majority stake | JV 50/50 or minority |

**JV Caution**: JV is not merely a "safer" FDI. It carries knowledge spillover risk (O may leak to partner), governance conflicts, and slower decision-making. Choose JV when the *partner's L knowledge* (market access, regulatory relationships) is essential and cannot be acquired cheaply.

---

## Worked Example: Taiwanese Semiconductor Firm → Germany

**Firm**: mid-tier fabless chip designer, strong in automotive-grade MCUs.

### Step 1 — O Assessment

| O Type | Evidence | Strength |
|--------|----------|----------|
| Oa: Patent portfolio | 340 granted patents in automotive MCU; ISO 26262 certified processes | High |
| Oa: Brand | Qualified by 3 Tier-1 EU auto suppliers | Moderate |
| Ot: Manufacturing know-how | 12-year customer co-development relationships; tacit τ ≈ 0.7 | High |

O assessment: **Strong**

### Step 2 — L Assessment

| L Type | Evidence | Strength |
|--------|----------|----------|
| L₁ Market | EU auto production ~12M vehicles/year; local presence required by OEM procurement rules | High |
| L₂ Resource | German labor costs 3× Taiwan → negative | Absent |
| L₃ Efficiency | None; not consolidating global operations | Absent |
| L₄ Strategic | Munich/Stuttgart automotive cluster; Bosch, ZF, Continental as potential partners; access to EU R&D grants | High |

L assessment: **Strong** (driven by L₁ + L₄, not cost)

### Step 3 — I Assessment

| I Factor | Evidence | Strength |
|----------|----------|----------|
| Tacitness | τ ≈ 0.7 (co-development routines hard to document) | High |
| Quality control | OEM qualification requires direct engineering liaison | High |
| Opportunism | German partner could reverse-engineer and license independently | High |
| Contract completeness | Automotive product cycles 5–7 years; too many contingencies to contract | High |

I assessment: **Strong**

### Step 4 — Entry Mode

```
OLI: O=Strong, L=Strong, I=Strong
Country risk: Germany LOW
→ WOS recommended (design center + application engineering hub)
```

Rationale: Tacit co-development routines (τ = 0.7) cannot be licensed without losing the O advantage. Germany's L₁ market barrier (OEM sourcing preference for local presence) and L₄ cluster access reinforce. Internal governance is necessary to protect IP and manage multi-year OEM qualification cycles.

**JV rejected**: No German partner offers L-knowledge that cannot be acquired through hiring. JV would expose the patent portfolio and co-development IP to a future competitor.

---

## Extensions and Critiques

### Dynamic OLI (Dunning & Lundan 2008)

Static OLI treats advantages as given at decision time. The dynamic extension recognizes:

```
O(t+1) = O(t) + ΔO_FDI
```

Where ΔO_FDI is the new ownership advantage *created by* operating in the foreign location (knowledge acquired, brand built, technology absorbed from L₄ spillovers). This is especially relevant for strategic asset-seeking FDI where the goal is O augmentation, not O exploitation.

Implication for analysis: If L₄ is the primary motivation, the static OLI output ("FDI recommended") is correct but the *reason* is different — the firm expects post-entry O gains to justify the investment, not current O exploitation.

### IDP (Investment Development Path)

Dunning (1981) linked OLI to macro-level country development via the Investment Development Path:

| Stage | GDP per capita | Inward FDI | Outward FDI |
|-------|---------------|------------|-------------|
| 1 | Low | Low (weak L, no local O) | None |
| 2 | Rising | Growing (L₁, L₂ attractive) | Minimal |
| 3 | Middle income | Strong | Emerging (O develops) |
| 4 | High income | Selective | Strong outward |
| 5 | Advanced | Two-way asset-seeking | Two-way |

Taiwan circa 2000–2015 exemplifies Stage 3→4: strong inward FDI for technology in early periods, then outward FDI as Taiwanese firms developed O advantages.

**IDP is not a prediction tool** for individual firms — it contextualizes national O+L trajectories. A firm in a Stage 2 country can still have strong individual O advantages.

### Limits of the Formalization

- **O, L, I are not independently measurable** in practice. The decompositions above are approximations; no agreed-upon scale exists.
- **Weights α, β, γ, δ are industry- and firm-specific** and cannot be estimated without comparable transaction data.
- **The model is cross-sectional**: it compares entry modes at one point. For sequential entry (export → JV → WOS), combine with the Uppsala Model's psychic distance logic.
- **Political risk is underweighted**: L assessment typically captures regulatory environment but political risk (expropriation, sudden policy reversal) enters as a country risk discount on all L values, not a separate variable.

---

## Quick Reference: OLI Strength Rating Rubric

Use this rubric to convert qualitative evidence into the three-tier (Strong / Moderate / Weak) ratings used in the SKILL.md output format:

### O Strength

| Rating | Criteria |
|--------|----------|
| Strong | Legally protected (patent, trademark) OR demonstrated market share premium OR τ > 0.6 with no codifiable substitute |
| Moderate | Operational advantage replicable within 3–5 years by a well-resourced competitor |
| Weak | Cost advantage only, no IP, easily replicated |

### L Strength

| Rating | Criteria |
|--------|----------|
| Strong | TWO or more L sub-types (L₁–L₄) are positive, OR one is dominant (e.g., tariff > 20% blocking export, or cluster access unavailable elsewhere) |
| Moderate | One L sub-type positive, others neutral |
| Weak | Single marginal L factor; exporting from home remains viable |

### I Strength

| Rating | Criteria |
|--------|----------|
| Strong | τ > 0.6 AND at least one of: multi-year relationship cycles, brand quality risk, direct competitor risk |
| Moderate | τ ∈ [0.3, 0.6] OR contractual protection feasible but costly |
| Weak | Knowledge is codifiable, market is thick, standard licensing contracts are enforceable |
