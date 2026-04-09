# Born Global Empirical Criteria and Classification Thresholds

## Canonical Thresholds

Three independent research streams have each proposed operational criteria. They converge on two core dimensions: **speed** (how quickly after founding) and **depth** (what share of revenue is foreign).

| Source | Foreign Revenue Threshold | Time Threshold | Geographic Scope |
|--------|--------------------------|----------------|------------------|
| Rennie (1993) — McKinsey Australia study | ≥ 25% of total sales | Within 2 years of founding | ≥ 2 foreign markets |
| Knight & Cavusgil (1996, 2004) | ≥ 25% of total sales | Within 3 years of founding | Not specified |
| Oviatt & McDougall (1994) — INV definition | "Significant" foreign activity | At or near founding | ≥ 2 countries across value chain |

**Working definition used in this skill:** ≥ 25% foreign revenue within 3 years of founding. Knight & Cavusgil (2004) is the most widely cited operationalization in the empirical literature.

### Why 25%, Not 50%?

The 25% threshold reflects the resource constraint: a genuinely born global firm cannot be evaluated by MNC standards. For most SMEs operating domestically, 0% foreign revenue is the baseline. Even 25% signals a fundamentally different strategic orientation. Some studies use 50% as a "strong born global" sub-category (Madsen & Servais, 1997), but this risks excluding firms in industries with high fixed domestic overhead (e.g., hardware with mandatory local compliance costs).

---

## Classification Decision Tree

```
Is the firm ≤ 3 years old at first foreign sale?
│
├─ YES → Does foreign revenue ≥ 25% of total within 3 years of founding?
│        │
│        ├─ YES → Does the firm serve ≥ 2 distinct foreign markets?
│        │        │
│        │        ├─ YES → BORN GLOBAL (full criteria met)
│        │        │
│        │        └─ NO  → BORN REGIONAL (partial; common in EU, ASEAN blocs)
│        │
│        └─ NO  → EARLY INTERNATIONALIZER (some foreign activity; not born global)
│
└─ NO  → First foreign sale > 3 years post-founding
         │
         ├─ Uppsala-path firm (gradual, stage-based)
         │
         └─ Late globalizer (re-evaluate if external shock triggered entry)
```

**Born Regional** is not a failure mode — it is a valid intermediate finding. Nordic SaaS firms often saturate Scandinavia first (linguistically homogeneous, small individual markets) before the 3-year window closes.

---

## Five-Factor Eligibility Scoring

Operationalizes the eligibility check in the parent SKILL.md. Score 0–2 per factor:

| Factor | 0 (Absent) | 1 (Partial) | 2 (Strong) |
|--------|-----------|-------------|------------|
| **Knowledge intensity** | Generic service/product; easily replicated | Some proprietary process or soft IP | Patent, trade secret, or rare expertise; >2 years to imitate |
| **Founder international experience** | All founders domestic-only background | One founder with foreign education or work (≤ 3 years) | At least one founder with sustained international career or foreign network of ≥ 50 professional contacts |
| **Niche market orientation** | Addresses a broad horizontal market | Defined niche but contested by regional players | Global niche with addressable market < $500M (too small for MNC focus) |
| **Digital / scalable delivery** | Physical product requiring local warehousing or service delivery | Hybrid: core is digital, some physical component | Fully digital; zero marginal cost of delivering to additional country |
| **Home market limitation** | Large domestic market (e.g., US, China) with many years of runway | Mid-size domestic market; may support 2–3 years of growth | Small domestic market (population < 20M or TAM < $50M); cannot sustain the business long-term |

**Interpretation:**

| Total Score | Verdict |
|-------------|---------|
| 8–10 | Born global path strongly supported |
| 5–7 | Born global viable; resource plan must address missing factors |
| 3–4 | Early internationalization is high-risk; consider Uppsala for initial market |
| 0–2 | Born global premature; domestic-first recommended |

### Worked Example: Taiwanese B2B SaaS for Semiconductor QC

| Factor | Score | Evidence |
|--------|-------|----------|
| Knowledge intensity | 2 | Proprietary defect-detection algorithm trained on 3 years of fab data; patent pending |
| Founder international experience | 2 | CEO spent 6 years at ASML Netherlands; TSMC and Samsung contacts |
| Niche market orientation | 2 | Global TAM for advanced-node QC SaaS ≈ $180M; Intel/Applied Materials build custom tools, don't sell |
| Digital/scalable delivery | 1 | Core model is cloud-delivered; onboarding requires 2-week on-site calibration |
| Home market limitation | 2 | Taiwan market = TSMC + a handful of IDMs; can sustain Y1 revenue but not growth |
| **Total** | **9** | **Born global path strongly supported** |

**Note on the partial score for digital delivery:** The 2-week on-site requirement raises entry cost per new country. The firm must budget for 2–3 full calibration trips per market and price the onboarding fee accordingly. This does not disqualify born global status, but it changes the entry mode toward partnerships with local distributors who can provide on-site support (reducing the founder's direct travel burden).

---

## Foreign Revenue Ratio: Calculation and Common Errors

### Formula

$$\text{FRR} = \frac{\text{Revenue from all non-home-country customers}}{\text{Total revenue}} \times 100$$

**What counts as foreign revenue:**
- Sales to foreign customers regardless of billing currency
- License fees paid by foreign entities
- Revenue from foreign subsidiaries of home-country MNCs only if the contract is with the foreign entity

**What does NOT count:**
- Domestic sales to export intermediaries (the intermediary's foreign resale is not the firm's foreign revenue)
- Foreign-denominated sales to domestic customers
- Grant funding from foreign government programs

### Error: Confusing Contract Location with Customer Location

A Singaporean startup selling to a US enterprise's Singapore regional HQ is making a **domestic** sale if the legal entity and decision-maker are in Singapore. If the US parent is the contracting entity and the work is delivered to US users, it is a **foreign** sale. When in doubt: where is the invoice sent, and where does the economic benefit flow?

### Measurement Period

The 3-year window starts at the date of first revenue (not incorporation). Incorporation-to-revenue lag in deep-tech can be 12–24 months; using the incorporation date would unfairly classify early-stage firms as Uppsala-path.

---

## Industry Context: Where Born Globals Are Empirically Most Common

The Knight & Cavusgil (2004) survey and subsequent replication studies identify clustering by industry. Knowing the base rate helps calibrate whether a born global assessment is plausible.

| Industry | Born Global Frequency | Primary Enabler |
|----------|-----------------------|-----------------|
| Software / SaaS | Very high | Zero marginal delivery cost; English as de facto standard |
| Medical devices / diagnostics | High | Regulatory arbitrage; niche patient populations require global patient pool |
| Environmental technology (cleantech) | High | Policy-driven demand in multiple markets simultaneously |
| Advanced materials | Moderate-high | Few global buyers; must reach all of them to achieve viable revenue |
| Industrial machinery | Moderate | High capital cost; fewer units; each foreign sale is large |
| Consumer goods (non-digital) | Low | Logistics, localization, and retail relationships favor staged entry |
| Construction / real estate | Very low | Non-tradeable; physical presence required per market |

**Implication for assessment:** If a firm is in the "Low" or "Very Low" rows, extra scrutiny is warranted. Born global is not impossible in consumer goods (premium, digitally-native DTC brands have done it), but the resource model is harder and the eligibility score must be 8+ to justify the recommendation.

---

## The "Born Again Global" Exception

Some studies (Bell, McNaughton & Young, 2001) document firms that were founded domestically, operated locally for years, then internationalized rapidly following a triggering event:

- Death of the domestic market (regulatory change, technology disruption)
- Acquisition of a key customer that is itself a multinational
- Founder succession bringing in an internationally-experienced CEO

These firms are **not** born globals under canonical criteria (first foreign sale occurred > 3 years post-founding). They should be classified as "born again globals" and analyzed separately. The born global SKILL.md methodology applies to their *rapid internationalization phase*, but their resource base and risk profile differ — they typically have more domestic cash flow to fund international entry than a genuine born global.

---

## Thresholds Under Debate

Two threshold choices remain contested in the literature; document the firm's position relative to both when the classification is borderline.

**1. The 25% floor vs. the 50% floor**

Madsen & Servais (1997) argue 25% is too permissive — a firm generating 26% foreign revenue from one large export customer is not strategically international. They propose 50% as the threshold for "committed born globals." Practice: use 25% as the minimum for born global eligibility; flag firms at 25–49% as "borderline" and check whether the foreign revenue is concentrated (1 customer) or distributed (≥ 3 customers in ≥ 2 countries).

**2. The 3-year window vs. the "at founding" standard**

Oviatt & McDougall (1994) define INVs as firms that internationalize "from inception," which some interpret as Year 0–1. Knight & Cavusgil's 3-year window is an empirical relaxation based on observed firm behavior. For policy and competitive analysis, the stricter "at inception" definition identifies a smaller, more extreme set of firms with qualitatively different founder profiles (serial international entrepreneurs, diaspora founders). When the distinction matters, report both classifications.

---

## Quick-Reference Checklist

Use this checklist before finalizing a born global assessment:

```
□ First foreign sale date documented (not estimated)
□ Foreign revenue ratio calculated using correct formula (see above)
□ Measurement period starts at first revenue, not incorporation
□ ≥ 2 distinct foreign markets confirmed (not just 1 export customer in 1 country)
□ Industry base rate noted (high / moderate / low born global frequency)
□ Five-factor eligibility score computed and recorded
□ "Born again global" trigger event ruled out (or documented if present)
□ If FRR is 25–49%: foreign revenue concentration checked (single vs. multiple customers)
```
