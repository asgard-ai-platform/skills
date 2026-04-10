我目前沒有直接寫入檔案的工具（這個介面沒有 Write/Bash 工具）。以下是完整的 `sample_scenario.md` 內容，請你複製並貼上到 `grad-oli/examples/sample_scenario.md`：

```markdown
# Example: Taiwanese PCB Manufacturer Evaluating FDI in Northern Vietnam

## Scenario

**Company**: Apex Circuit Technology (ACT), a mid-sized Taiwanese printed circuit board (PCB) manufacturer headquartered in Taoyuan. Annual revenue NT$8.2B (~USD 260M). Primary customers are Tier-1 ODMs supplying Apple, Dell, and Lenovo.

**Situation (2025 Q3)**: ACT's two largest ODM customers have issued supply chain diversification mandates, requiring suppliers to establish "China+1" or "Taiwan+1" production capacity outside Greater China by end of 2026. ACT currently exports from its Taoyuan plant. Labour costs in Taiwan have risen 18% over three years. Vietnam (Haiphong / Quảng Ninh SEZ) has been shortlisted by ACT's strategy team.

**User question**: Should ACT set up a wholly-owned subsidiary (greenfield) in Vietnam, enter a joint venture with local manufacturer Viet Tech PCB Co., or simply source via a contract manufacturer and license ACT's process technology to them?

---

## Analysis

### Step 1: Assess Ownership Advantages (O)

**Asset-based (Oa)**
- **Process IP**: ACT holds 14 active patents in high-density interconnect (HDI) and buried-via PCB fabrication — processes Viet Tech and most Vietnamese PCB makers do not possess.
- **Brand / qualification**: ACT holds IATF 16949, UL, and three ODM vendor qualifications that took 3–5 years to earn. These are non-transferable assets.
- **Customer relationships**: ACT has embedded engineering teams co-located with two ODM customers; relationship switching cost is high.

**Transaction-based (Ot)**
- Yield management know-how: ACT achieves 97.4% yield on 12-layer HDI boards vs. industry average ~93%. This is tacit, embedded in operator routines and real-time SPC systems.
- Procurement leverage: ACT's scale allows it to negotiate copper foil and prepreg pricing ~8% below spot.

**O assessment: Strong** — ACT has durable, firm-specific advantages that Vietnamese competitors cannot easily replicate.

---

### Step 2: Assess Location Advantages (L)

**Motivation type: Efficiency-seeking + Market-access/compliance**

| Factor | Home (Taiwan) | Vietnam (Haiphong SEZ) |
|--------|--------------|------------------------|
| Direct labour cost (operator/hr) | USD 8.50 | USD 2.10 |
| Corporate tax rate | 20% | 9% (SEZ, first 15 yrs) |
| Land/factory lease (USD/m²/yr) | 180 | 38 |
| ODM customer proximity | n/a | 3 of 5 target ODMs building VN plants |
| Trade tariffs to US market | 0% | 0% (MFN) — avoids 25% China tariff |

- Labour cost reduction alone saves ~USD 6M/yr at projected 300K m² annual output.
- Three ODM customers are constructing Vietnam assembly plants by 2026 — local PCB sourcing will be strongly preferred to reduce logistics lead time from 7 days (Taiwan air) to 1 day (truck).
- Vietnam–US trade relations benefit from CPTPP and bilateral trade agreements, making VN-origin PCBs immune to the China-specific Section 301 tariffs ACT's competitors face.

**L assessment: Strong** — Labour cost, tax, proximity to customer expansion, and tariff avoidance all converge on Vietnam as the superior production location.

---

### Step 3: Assess Internalization Advantages (I)

**Transaction cost drivers**
- **Tacit yield know-how**: ACT's 97.4% yield is embedded in operator training, real-time SPC tooling, and undocumented heuristics. Licensing this to Viet Tech would require ACT to codify and transfer knowledge it cannot fully articulate — classic tacit knowledge problem.
- **Contractual incompleteness**: A licensing contract cannot cover all contingencies affecting yield, delivery reliability, or handling of customer-specific engineering changes.

**Opportunism risk**
- Viet Tech PCB Co. currently supplies ACT's direct competitor (Pinnacle Board). Licensing ACT's HDI process to Viet Tech risks reverse engineering of core IP within 2–3 years, directly empowering a competitor's supplier.
- Customer qualifications (IATF 16949) are entity-specific; Viet Tech would require 18–24 months re-qualification, eliminating the time advantage of licensing.

**Quality control**
- ODM customers require ACT's own quality engineers on-site. A contract manufacturing arrangement cannot satisfy this requirement.

**I assessment: Strong** — Licensing is foreclosed by tacit knowledge, opportunism risk, and customer qualification lock-in.

---

### Step 4: Determine Entry Mode

| OLI Factor | Rating | Evidence |
|------------|--------|----------|
| Ownership (O) | Strong | HDI patents, yield know-how, ODM qualifications |
| Location (L) | Strong | Labour cost, tax, customer proximity, tariff |
| Internalization (I) | Strong | Tacit IP, Viet Tech conflict of interest, quality control |

**OLI Configuration: O + L + I (all strong)**

Per the OLI framework: wholly-owned subsidiary is optimal. A joint venture with Viet Tech is ruled out because (a) Viet Tech's customer overlap creates direct opportunism risk and (b) ACT's I advantages are specifically driven by the need to keep tacit process knowledge inside the firm boundary.

---

## Result

# OLI Assessment: Apex Circuit Technology → Vietnam (Haiphong SEZ)

## Ownership Advantages (O)
- Asset-based: 14 HDI/buried-via patents (Strong); IATF 16949 + UL + ODM qualifications (Strong); 10-year ODM customer relationships (Strong)
- Transaction-based: 97.4% yield tacit know-how (Strong); copper foil / prepreg procurement leverage ~8% below spot (Moderate)
- **O assessment: Strong**

## Location Advantages (L)
- Motivation: Efficiency-seeking (labour, tax, land) + market-access compliance (China+1 mandate, ODM co-location)
- Key L factors: Labour cost USD 2.10/hr vs. USD 8.50 (Taiwan); SEZ CIT 9%; 3 of 5 ODM customers building VN plants by 2026; tariff-free US market access vs. 25% China tariff
- **L assessment: Strong**

## Internalization Advantages (I)
- Transaction cost drivers: Tacit yield know-how uncodifiable; contractual incompleteness around ECs and quality events; customer qualifications non-transferable
- Opportunism risk: **High** — Viet Tech Co. is a supplier to ACT's direct competitor; licensing would externalize core IP
- **I assessment: Strong**

## OLI Configuration: O + L + I (all strong)

## Recommended Entry Mode: Wholly-Owned Subsidiary (Greenfield)

**Rationale**: All three OLI conditions are strong and simultaneous. Joint venture with Viet Tech is disqualified by opportunism risk (shared competitor exposure). Licensing is disqualified by tacit knowledge and customer qualification requirements. Export-only from Taiwan is disqualified by the ODM mandate and cost structure. ACT should proceed with a greenfield WOS in Haiphong SEZ, targeting production start by Q3 2026 to meet the ODM deadline.

**Suggested next steps** (outside OLI scope):
- Combine with Uppsala model (grad-uppsala) to sequence the ramp — start with a single product line transfer before full capacity migration.
- Conduct detailed L sensitivity analysis: re-run if Vietnam SEZ tax holiday terms change post-2030.
```
