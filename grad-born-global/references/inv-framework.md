# International New Ventures (INV) Framework — Oviatt & McDougall (1994)

## Source

Oviatt, B. M., & McDougall, P. P. (1994). Toward a theory of international new ventures. *Journal of International Business Studies*, 25(1), 45–64.

This paper is the theoretical foundation for the born global literature. It predates Rennie (1993) and Knight & Cavusgil (1996) but provides the only formal theoretical model explaining *why* and *how* new ventures internationalize at founding.

---

## Why INV ≠ Born Global

These terms are frequently conflated. The distinction matters for diagnosis:

| Dimension | Born Global | International New Venture (INV) |
|-----------|-------------|----------------------------------|
| Origin | Empirical observation (revenue thresholds) | Theoretical construct (conditions) |
| Definition | 25%+ foreign sales within 3 years | New firm with value-creating activity in ≥2 countries at/near founding |
| Emphasis | Speed and scope of international sales | Resource control without ownership; transaction cost minimization |
| Diagnostic use | Revenue milestone screening | Structural analysis of how early internationalization is *sustainable* |

**Practical implication**: A firm can appear born global (hit the revenue threshold) without meeting INV conditions — and then fail when imitation catches up. Use INV conditions to assess *structural durability*, not just timing.

---

## The Four Necessary and Sufficient Conditions

Oviatt & McDougall specify four conditions that must *all* be present for a sustainable INV:

### Condition 1: Organizational Formation by Internalization of Some Transactions

The firm must own at least some value-creating activities. Pure market transactions (arms-length import/export with no proprietary element) do not constitute an INV because they confer no defensible advantage.

**Test**: Does the firm control unique knowledge, a proprietary process, or a differentiated capability — not merely arbitrage a price difference?

- Pass: A SaaS firm with proprietary NLP models selling to foreign enterprises → yes, the model is internalized
- Fail: A trading company reselling generic electronics across borders → no, purely market transactions

### Condition 2: Strong Reliance on Alternative Governance Structures

INVs cannot afford full ownership of foreign operations. They use hybrid governance: licensing, strategic alliances, franchising, joint ventures, and distribution partnerships. The firm *controls* without *owning*.

**Transaction Cost Logic**: An INV uses alternative structures where:

```
Cost of internalization (subsidiary) > Cost of opportunism risk (partner)
```

When asset specificity is moderate (not generic, not fully unique), hybrids dominate. INVs deliberately choose governance structures that:
- Reduce capital requirements
- Transfer local market knowledge risk to the partner
- Preserve flexibility to exit or upgrade commitment

**Worked Example**: A Finnish cybersecurity startup (5 employees) enters the Japanese market via a local IT distributor. The startup owns the detection algorithm (Condition 1). The distributor provides customer relationships, regulatory navigation, and local support (alternative governance). The startup does not attempt a wholly-owned subsidiary — that would consume 18+ months and €2M+ in setup costs.

### Condition 3: Establishment of Foreign Location Advantages

The INV must have a reason to operate in a specific foreign location beyond home-market saturation. Oviatt & McDougall draw from Dunning's OLI: location advantages (L) must be present, but unlike MNCs, INVs can access L advantages through partners rather than ownership.

**Location advantage sources for INVs:**

| Source | INV Access Mechanism |
|--------|---------------------|
| Customer proximity | Distributor or agent in target market |
| Regulatory arbitrage | Local partner handles compliance |
| Lead market access | Conference presence, pilot customers |
| Talent or input cost | Remote work, contractor networks |
| Infrastructure | Cloud providers with regional nodes |

**Key diagnostic question**: Why *that* market specifically? If the answer is "because our founder knows someone there," that is a network-based location advantage — valid, but fragile (see Condition 4 below).

### Condition 4: Unique Resources Spanning National Borders

The INV's competitive advantage must rest on resources that:
1. Are rare or inimitable in target markets
2. Can be leveraged across multiple national contexts without proportional cost increase

This is the closest condition to the SKILL.md Iron Law. The resource must be knowledge-intensive by nature:

**Resource durability test:**

```
Durability = f(Tacitness, Complexity, Context-specificity)

High tacitness    → hard to imitate by observation alone
High complexity   → requires bundling of multiple capabilities
High context-specificity → embedded in team routines, not codifiable
```

A patent provides some protection but is not sufficient alone — patents can be worked around. The most durable INV resources are tacit, complex, and team-embedded.

---

## INV Typology: Four Archetypes

Oviatt & McDougall classify INVs along two axes:

- **Geographic scope**: Few countries vs. Many countries
- **Value chain activities coordinated**: Few (sales/marketing only) vs. Many (R&D, production, sales)

```
                    FEW VALUE CHAIN          MANY VALUE CHAIN
                    ACTIVITIES               ACTIVITIES
                 ┌─────────────────────┬─────────────────────┐
MANY COUNTRIES   │  Export/Import       │  Multinational       │
                 │  Startup             │  Trader              │
                 │  (Type I)            │  (Type II)           │
                 ├─────────────────────┼─────────────────────┤
FEW COUNTRIES    │  Geographically      │  Global Start-up     │
                 │  Focused Start-up    │                      │
                 │  (Type III)          │  (Type IV)           │
                 └─────────────────────┴─────────────────────┘
```

### Type I: Export/Import Startup
- Sells to many countries but only conducts sales/marketing internationally
- Production, R&D remain at home
- Example: A Taiwanese handmade goods brand selling via Etsy to 30+ countries
- **INV durability concern**: Low barriers to imitation; advantage rests primarily on founder energy, not structural capability

### Type II: Multinational Trader
- Coordinates many value chain activities across many countries
- Requires substantial networks from day one
- Rare in early-stage firms; usually founders with prior MNC careers
- Example: A supply chain arbitrage firm simultaneously sourcing from Vietnam, finishing in Taiwan, selling to EU retailers

### Type III: Geographically Focused Startup
- Deep coordination across value chain but in a small number of countries
- Most common among technical B2B INVs targeting 1–3 lead markets
- Example: An Israeli AI startup with R&D in Tel Aviv, first customers in Germany and UK
- **This is the most sustainable early-stage INV archetype**

### Type IV: Global Startup
- Coordinates many activities across many countries simultaneously from founding
- Requires exceptionally strong founder networks and prior international experience
- Example: Skype (founded with Estonian engineers, Swedish/Danish founders, UK sales)
- **Highest capability requirement; premature global startups frequently fail**

---

## Decision Framework: Which INV Type Should a Firm Target?

```
START
  │
  ▼
Does the firm have prior international networks in >3 countries?
  │
  ├── YES → Does the product require localization per market?
  │            ├── YES → Type III (Geographically Focused) first, expand later
  │            └── NO  → Type IV (Global Startup) potentially viable
  │
  └── NO  → Does the product have meaningful local sales complexity?
               ├── YES → Type III (1-2 markets, deep entry)
               └── NO  → Type I (Export/Import) to validate demand broadly
```

**Default recommendation for most early-stage INVs**: Begin as Type III. Depth in 1–2 markets builds the proof points needed to justify broader expansion and attracts the network contacts required for Types II or IV.

---

## Worked Diagnostic: Applying INV Conditions to a Real Case

**Firm**: Gradient Medical (fictitious), a 3-person Taiwan startup selling an AI-based radiology triage tool.

**Condition 1 — Internalization check:**
The firm owns a proprietary model trained on 500K+ annotated chest X-rays. The annotation pipeline and model weights are wholly owned. → **PASS**

**Condition 2 — Alternative governance check:**
For Japan, they partner with a local medical device distributor (handles PMDA regulatory approval). For Germany, they white-label through a hospital software vendor (handles GDPR compliance). Zero wholly-owned foreign offices. → **PASS**

**Condition 3 — Location advantage:**
Japan: highest CT-per-capita in the world; radiologist shortage creates urgent demand. Germany: EU reference market; regulatory approval unlocks 27 additional markets via mutual recognition. Both choices are deliberately justified. → **PASS**

**Condition 4 — Unique cross-border resource:**
The training data pool represents 5 years of partnership with 8 Taiwan hospitals — no competitor has equivalent annotated data in this category. The data moat is tacit (curation judgment), complex (multi-hospital coordination), and context-specific (team routines). → **PASS**

**INV Verdict**: All four conditions met. Archetype: **Type III** (two geographically focused markets, multi-activity coordination: R&D in Taiwan + regulatory + sales via partners abroad).

**Recommended next step**: Deepen Japan and Germany before adding markets. EU mutual recognition in Germany may unlock Type I expansion (many countries, fewer coordination needs) in years 2–3 at low incremental cost.

---

## Where INV Theory Fails to Predict

Oviatt & McDougall's model has documented limitations:

1. **Network quality is assumed, not modeled**: The theory says networks matter but does not specify how strong or how accessible they must be. Two firms with nominally similar networks can have dramatically different outcomes depending on network position (structural holes vs. closure).

2. **Digital products break Condition 3**: For pure software products deliverable globally at zero marginal cost, location advantages collapse — the firm can serve all markets equally. INV theory underspecifies this case. The born global empirical literature handles digital-native firms better.

3. **The model is static**: It describes conditions at founding, not how firms transition between archetypes over time. In practice, most Type I firms either die or upgrade to Type III; the path is not theorized.

4. **Condition 4 measurement is qualitative**: There is no standardized instrument for measuring "tacitness" or "inimitability" of knowledge resources. Practitioners must use proxy indicators (patent counts, team tenure, proprietary dataset size) and accept that this is judgment-dependent.

---

## Relationship to Uppsala Model

INV theory was explicitly constructed as a *challenge* to Uppsala's stage model. The key dispute:

| Claim | Uppsala | INV / Born Global |
|-------|---------|-------------------|
| Internationalization sequence | Gradual stages, psychic distance ordering | Non-linear; rapid entry into distant markets possible |
| Resource requirement | Accumulate resources before international commitment | Resources accessed through networks, not owned |
| Risk management | Incremental commitment reduces uncertainty | Network relationships and knowledge intensity substitute for experience accumulation |
| Empirical basis | Large Scandinavian MNCs (1970s) | Knowledge-intensive SMEs (1990s–present) |

These are not mutually exclusive: a firm can be born global initially and then follow Uppsala dynamics as it deepens commitment in established markets. The frameworks apply at different *phases* of firm development and different *types* of international activity.
