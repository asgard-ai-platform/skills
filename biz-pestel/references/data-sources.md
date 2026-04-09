# PESTEL Data Sources

Every PESTEL factor must be grounded in observable data, trends, or events (Iron Law: Evidence-Based, Not Speculative). This reference maps each PESTEL dimension to authoritative, publicly accessible sources — with notes on what each source actually provides, its update cadence, and where it falls short.

---

## Quick-Reference Table

| Dimension | Primary Go-To | Secondary | Caveat |
|-----------|--------------|-----------|--------|
| Political | Freedom House / EIU | World Bank WGI | EIU behind paywall |
| Economic | World Bank Open Data | IMF WEO | National stats bureaus for local detail |
| Social | UN Population Division | WHO | Census data often 5+ years lagged |
| Technological | ITU / GSMA | Gartner | Gartner forecasts are estimates |
| Environmental | Climate Risk Index / CDP | IPCC reports | IPCC is scientific, not business-focused |
| Legal | Doing Business indicators | Local law firm country guides | Free sources skip sector-specific regs |

---

## P — Political

### World Bank Worldwide Governance Indicators (WGI)
- **URL**: `data.worldbank.org/data-catalog/worldwide-governance-indicators`
- **What it measures**: 6 dimensions — Voice & Accountability, Political Stability, Government Effectiveness, Regulatory Quality, Rule of Law, Control of Corruption
- **Update cadence**: Annual, ~1-year lag
- **How to use it**: Compare percentile rank vs. peer countries; a score below 25th percentile on Political Stability flags elevated operational risk

**Example reading:**
```
Vietnam: Political Stability 2023 → 54th percentile
Philippines: Political Stability 2023 → 22nd percentile
→ Vietnam carries lower political disruption risk than Philippines for FDI
```

### Freedom House — Freedom in the World
- **URL**: `freedomhouse.org/report/freedom-world`
- **What it measures**: Political rights (7 indicators) + Civil liberties (15 indicators), scored 1-7 per category
- **Best for**: Binary flag on regime type; "Free / Partly Free / Not Free" classification is broadly cited and useful for investor communications
- **Limitation**: Political bias acknowledged in methodology; use as directional signal, not sole arbiter

### Transparency International — Corruption Perceptions Index (CPI)
- **URL**: `transparency.org/en/cpi`
- **What it measures**: Perceived level of public sector corruption, 0 (most corrupt) to 100 (least corrupt)
- **Update cadence**: Annual, released January
- **PESTEL use**: A CPI below 40 typically signals high regulatory unpredictability and informal compliance costs — factor this into market entry cost models

### Economist Intelligence Unit (EIU) Country Risk Service
- **Paywall**: Yes (institutional subscription ~$3,000/yr; often accessible via university libraries)
- **What it provides**: Operational Risk Ratings, Political Risk Score, 5-year country outlook
- **Free alternative**: EIU publishes summary risk ratings by country at no cost; full reports require subscription

---

## E — Economic

### World Bank Open Data
- **URL**: `data.worldbank.org`
- **What it provides**: GDP, GDP growth, GNI per capita, inflation (CPI), unemployment, FDI inflows, trade as % of GDP — 200+ economies, 60-year history
- **Update cadence**: Annual (quarterly for some indicators); typically 6-18 month lag
- **Key indicators for PESTEL**:
  - `NY.GDP.MKTP.KD.ZG` — GDP growth (annual %)
  - `FP.CPI.TOTL.ZG` — Inflation (CPI %)
  - `SL.UEM.TOTL.ZS` — Unemployment rate
  - `BX.KLT.DINV.WD.GD.ZS` — FDI net inflows (% of GDP)

**How to cite in a PESTEL table:**
> "Vietnam GDP growth 6.5% (2024) — World Bank national accounts data, accessed 2025"

### IMF World Economic Outlook (WEO)
- **URL**: `imf.org/en/Publications/WEO`
- **What it adds over World Bank**: 5-year forward projections, regional comparisons, scenario analysis (upside/downside)
- **Update cadence**: Twice yearly (April and October)
- **When to prefer IMF**: Forward-looking factors ("GDP projected at 4.8% through 2028") — IMF projections are more frequently cited in financial contexts

### National Statistics Bureaus

Use national bureaus for **current-year** or **sub-national** data that World Bank hasn't yet incorporated:

| Country | Bureau | URL |
|---------|--------|-----|
| Taiwan | DGBAS | `stat.gov.tw` |
| Vietnam | GSO | `gso.gov.vn/en` |
| Japan | Statistics Japan | `stat.go.jp/english` |
| South Korea | KOSTAT | `kostat.go.kr/eng` |
| Thailand | NSO Thailand | `nso.go.th/en` |
| Indonesia | BPS | `bps.go.id/en` |

**When to use**: Exchange rate trends, monthly CPI, regional GDP breakdowns, consumer confidence indices.

### Trading Economics
- **URL**: `tradingeconomics.com`
- **What it provides**: Real-time and historical macro data aggregated from national sources, IMF, World Bank
- **Useful for**: Quick cross-country comparison, visual trend lines, recent data points
- **Caveat**: Not primary source — always trace back to the original issuer before citing

---

## S — Social

### UN Population Division — World Population Prospects
- **URL**: `population.un.org/wpp`
- **What it provides**: Historical and projected population by age cohort, fertility rates, life expectancy, urbanization, median age — to 2100
- **Key indicators for PESTEL**:
  - Median age → consumer base maturity, workforce age profile
  - Urban population % → distribution channel implications
  - Working-age population (15-64) growth → labor supply outlook

**Worked example:**
```
Vietnam 2025 data (UN WPP):
  Median age: 31.9 years
  Urban population: 39.5%
  Working-age growth rate: +0.8% annually (slowing)
→ Young urban consumer base, but labor market tightening by 2030
```

### WHO Global Health Observatory
- **URL**: `who.int/data/gho`
- **What it provides**: Health indicators — obesity rates, disease burden, health expenditure per capita, mental health prevalence
- **PESTEL use**: Social dimension factors for health-adjacent industries (food, pharma, insurance, fitness)

### Euromonitor Passport
- **Paywall**: Yes (university libraries often provide access)
- **What it provides**: Consumer lifestyle surveys, income distribution, household expenditure patterns
- **When worth the effort**: Consumer goods PESTEL where buying behavior data is the crux

### Pew Research Center
- **URL**: `pewresearch.org`
- **What it provides**: Attitudinal surveys on religion, politics, social trust, technology adoption — 40+ countries
- **Best for**: Social dimension factors that are attitudinal, not demographic (e.g., "trust in institutions", "views on foreign brands")
- **Limitation**: Coverage varies by country; stronger for US and Europe

---

## T — Technological

### ITU (International Telecommunication Union) — ICT Data
- **URL**: `itu.int/en/ITU-D/Statistics`
- **What it provides**: Mobile broadband penetration, internet users (% of population), fixed broadband subscriptions, 5G readiness indicators
- **Update cadence**: Annual
- **Primary use**: Digital infrastructure baseline for any tech-dependent market entry

### GSMA Intelligence
- **URL**: `gsmacom/resources/research/gsma-intelligence`
- **What it provides**: Mobile market data — 5G rollout timelines, operator market share, smartphone penetration, mobile money adoption
- **Free access**: Summary reports available; full dataset requires registration
- **How to cite**: "5G coverage reaching 70% of urban population by 2026 (GSMA Intelligence, 2024)"

### World Intellectual Property Organization (WIPO) — Global Innovation Index
- **URL**: `wipo.int/global_innovation_index`
- **What it measures**: Innovation inputs (institutions, infrastructure, market sophistication) and outputs (knowledge, technology, creativity) — 132 economies
- **Update cadence**: Annual (usually released September)
- **PESTEL use**: Proxy for R&D ecosystem strength, tech transfer risk, local IP enforcement

### Gartner Hype Cycle Reports
- **Paywall**: Yes (research subscription); summaries publicly available
- **What it provides**: Technology maturity curve for ~2,000 technologies, segmented by industry
- **Use with caution**: Hype Cycle represents Gartner's analytical judgment, not observed data. Cite as "Gartner estimates" not "data shows"
- **When useful**: Flagging emerging technologies that are 2-5 years from mainstream adoption

---

## E — Environmental

### German Watch — Global Climate Risk Index (CRI)
- **URL**: `germanwatch.org/en/cri`
- **What it measures**: Quantified losses from extreme weather events (deaths, GDP loss) — ranked by country for 1-year and 20-year periods
- **Update cadence**: Annual (released at COP)
- **How to use**: High CRI rank = elevated supply chain, facility, and logistics risk

**Example:**
```
Philippines: CRI 2023 rank #4 globally (very high risk)
Vietnam: CRI 2023 rank #13 (high risk)
Taiwan: CRI 2023 rank #35 (moderate risk)
→ Philippine operations require robust disaster recovery; factor into facility insurance cost
```

### CDP (Carbon Disclosure Project)
- **URL**: `cdp.net/en`
- **What it provides**: Corporate climate disclosures, water risk data, supply chain emissions
- **PESTEL use**: Understand what sustainability reporting obligations your target market's customers will face — if customers are CDP-reporting, expect ESG requirements to flow upstream to suppliers

### IPCC Assessment Reports
- **URL**: `ipcc.ch/assessment-report`
- **What it provides**: Scientific consensus on climate projections — temperature, sea level, extreme event frequency by region to 2100
- **Use correctly**: Use for long-horizon (10+ year) environmental factors only. Not a source for near-term business trend data. IPCC informs regulatory direction (governments cite IPCC when setting carbon policy).

### National Environmental Agencies

Use for jurisdiction-specific regulations that aren't yet captured in global indices:

| Country | Agency | Key Source |
|---------|--------|------------|
| Taiwan | EPA (環境部) | `epa.gov.tw` |
| Vietnam | MONRE | `monre.gov.vn` |
| EU markets | EUR-Lex | `eur-lex.europa.eu` (search: CBAM, EU ETS, CSRD) |
| China | MEE | `mee.gov.cn` |

---

## L — Legal

### World Bank — Doing Business (now B-READY)
- **Note**: "Doing Business" was discontinued in 2021 following methodology concerns. Replacement: **Business Ready (B-READY)** launched 2024.
- **URL**: `worldbank.org/en/programs/business-enabling-environment`
- **What it measures**: Regulatory quality across 10 business lifecycle topics — starting a business, dealing with construction permits, registering property, enforcing contracts
- **Limitation**: Measures regulatory framework quality, NOT actual compliance burden. A country can score well on paper and still have slow enforcement in practice.

### Law Firm Country Guides (Free)
Major international law firms publish free country-level regulatory guides:

| Firm | Guide name | URL pattern |
|------|-----------|-------------|
| Baker McKenzie | Global Business Guides | `bakermckenzie.com/en/insight/publications` |
| Linklaters | Country Guides | `linklaters.com/en/insights` |
| Dentons | Insights | `dentons.com/en/insights` |
| Norton Rose Fulbright | Global guides | `nortonrosefulbright.com/en/knowledge` |

**How to use**: Search "[country] + [industry] + regulatory guide + [year]". These guides cover employment law, data privacy, sector licensing, and foreign investment restrictions — with lawyer-reviewed accuracy.

### Data Privacy Regulation Tracker

Data privacy law is often the fastest-changing Legal dimension. Use:

- **IAPP (International Association of Privacy Professionals)**: `iapp.org/resources/global-privacy-directory` — country-by-country privacy law summary
- **DLA Piper Data Protection Laws of the World**: `dlapiperdataprotection.com` — free, updated frequently, covers 100+ jurisdictions

**Key laws to check by region:**
```
EU/EEA:     GDPR (Regulation 2016/679)
Taiwan:     個人資料保護法 (PDPA, 2012, amended 2023)
Thailand:   PDPA (Personal Data Protection Act B.E. 2562)
Vietnam:    Decree 13/2023/ND-CP (Personal Data Protection)
China:      PIPL (Personal Information Protection Law, 2021)
```

### Official Government Gazettes

For market entry, the primary legal source is always the official government gazette or legislative database — law firm summaries can lag by 6-12 months:

| Jurisdiction | Official source |
|--------------|----------------|
| Taiwan | 全國法規資料庫 `law.moj.gov.tw` |
| Vietnam | VBPLaw `vbpl.vn` |
| EU | EUR-Lex `eur-lex.europa.eu` |
| Indonesia | JDIH `jdih.go.id` |

---

## Source Quality Decision Framework

When selecting a source to cite in a PESTEL factor, apply this hierarchy:

```
Tier 1 — Official primary data
  → National statistics bureaus, government ministries, central banks
  → International organization primary datasets (World Bank, IMF, UN, ITU)
  Use when: Citing a specific number or rate

Tier 2 — Curated analytical sources
  → EIU, Freedom House, Transparency International, WIPO GII
  Use when: Comparing across countries or summarizing a trend

Tier 3 — Secondary aggregators
  → Trading Economics, Statista (licensed), news databases
  Use when: Rapid cross-checking; never as the sole citation

Tier 4 — Analyst reports and firm research
  → Gartner, McKinsey Global Institute, law firm country guides
  Use when: Directional support; flag as estimates or professional opinion
```

### What makes a citation valid for PESTEL

A valid PESTEL factor citation has four components:

```
[Specific claim] ([Source name], [Report/dataset name], [Year])

VALID:
  "5G coverage reaching 64% of population (GSMA Intelligence, Mobile Economy 
   Southeast Asia, 2024)"

INVALID:
  "5G is expanding rapidly" — no source, no specificity
  "Technology is changing" — violates Iron Law, not a PESTEL factor
```

---

## Asia-Pacific Specific Resources

Since the SKILL.md example focuses on a Taiwanese manufacturer entering Vietnam, these regional sources are particularly relevant:

### Taiwan-Outbound Investment

- **TAITRA** (Taiwan External Trade Development Council): `taitra.org.tw` — market reports, tariff data, buyer databases for target export markets
- **TIER** (Taiwan Institute of Economic Research): `tier.org.tw` — Taiwan economic outlook, industry forecasts
- **Investment Commission, MOEA**: `moeaic.gov.tw` — outbound FDI statistics, approved investment by country

### ASEAN Market Intelligence

- **ASEAN Stats**: `data.aseanstats.org` — trade, FDI, economic data for 10 ASEAN members
- **VCCI** (Vietnam Chamber of Commerce and Industry): `vcci.com.vn/en` — Vietnam business environment reports cited in SKILL.md example
- **BOI Thailand / BKPM Indonesia / MIDA Malaysia**: Country investment promotion agencies publish free sector-specific guides and approved incentive schedules

### Regional Development Banks

- **ADB (Asian Development Bank)**: `data.adb.org` — development indicators, infrastructure investment data, sector analyses for Asia-Pacific
- **ADB Key Indicators for Asia and the Pacific**: annual statistical publication covering 49 economies

---

## Maintaining Source Currency

PESTEL analysis is a snapshot with a declared time horizon. Document the access date for every source:

```markdown
| Legal | Vietnam food safety registration requires 
        6-month approval cycle (MOIT Circular 48/2019, 
        verified against MOIT website, accessed 2025-03) | High | − |
```

**Recommended refresh cadence by dimension:**

| Dimension | Minimum refresh | Reason |
|-----------|----------------|--------|
| Political | 6 months | Elections, policy reversals |
| Economic | 6 months | IMF/WEO releases twice yearly |
| Social | 12-24 months | Demographic change is slow |
| Technological | 6 months | Infrastructure rollout moves fast |
| Environmental | 12 months | Regulation lag is typically annual |
| Legal | 3-6 months | Regulatory changes can be sudden |
