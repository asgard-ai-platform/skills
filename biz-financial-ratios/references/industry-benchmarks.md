# Industry Benchmarks for Financial Ratio Analysis

Benchmarks are the baseline that makes a ratio meaningful. This reference provides concrete ranges across major industries for all five ratio categories, a decision framework for green/yellow/red classification, and a worked comparison example using the Taiwanese electronics scenario from the parent skill.

---

## Why Industry Matters More Than "General" Thresholds

The oft-cited rules of thumb (current ratio > 1.5, D/E < 1.0) are misleading defaults. They approximate manufacturing-era US industrial companies from mid-20th century data. Applied blindly:

- A grocery retailer with current ratio 0.9 looks insolvent → it's actually fine (suppliers extend 30-day terms, customers pay cash)
- A SaaS company with D/E of 3.0 looks dangerous → it may be AAA-rated if the debt is low-cost and ARR is recurring
- A semiconductor fab with 8% net margin looks mediocre → it's performing well (cyclical capex-heavy sector)

**Rule**: always identify the industry and sub-sector before selecting a benchmark set. If the company spans multiple segments, use weighted-average benchmarks or analyze segments separately.

---

## Benchmark Tables by Industry

All values are approximate medians for healthy, publicly-listed companies. "Healthy" means profitable, investment-grade (or equivalent private-market quality), not in distress.

Sources: Damodaran NYU annual industry data, Bloomberg consensus sector data, Taiwan Stock Exchange sector aggregates (for TW-listed companies). Ranges shift ±20% in recession years.

### 1. Software & SaaS

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Gross Margin | < 55% | 70–75% | > 80% | Low gross margin → scaling problem |
| Operating Margin | < 5% | 15–25% | > 30% | GAAP; stock comp depresses this |
| Net Margin | < 5% | 12–20% | > 25% | |
| ROE | < 10% | 20–30% | > 40% | |
| ROA | < 5% | 10–15% | > 20% | |
| Current Ratio | < 1.5 | 2.0–3.5 | > 4.0 | SaaS hoards cash; high is normal |
| Quick Ratio | < 1.5 | 2.0–3.0 | > 3.5 | Minimal inventory |
| Debt-to-Equity | > 1.5 | 0.3–0.7 | < 0.2 | Pure software: low debt |
| Interest Coverage | < 5x | 10–30x | > 50x | |
| Receivables Turnover | < 5x | 6–10x | > 12x | Annual contracts → bunched billings |
| Asset Turnover | < 0.5 | 0.7–1.2 | > 1.5 | Asset-light model |
| P/E | — | 25–50x | — | Growth premium; use EV/Revenue instead |
| EV/EBITDA | — | 20–40x | — | Profitability-stage companies |

**Sub-sector note**: Early-stage SaaS (< $50M ARR) is often unprofitable by design. Net margin and ROE benchmarks don't apply — use Rule of 40 (revenue growth % + FCF margin % ≥ 40) instead.

---

### 2. Semiconductor & Electronics Manufacturing (Taiwan-relevant)

This is the primary reference for TSMC, MediaTek, Foxconn, and their supply chain.

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Gross Margin | < 35% | 40–50% | > 55% | Fabless higher; IDM lower |
| Operating Margin | < 15% | 20–30% | > 35% | |
| Net Margin | < 10% | 15–25% | > 30% | |
| ROE | < 10% | 15–25% | > 30% | Capex-heavy; asset base large |
| ROA | < 5% | 8–15% | > 18% | |
| Current Ratio | < 1.2 | 1.5–2.5 | > 3.0 | |
| Quick Ratio | < 0.8 | 1.0–1.8 | > 2.0 | Inventory matters here |
| Debt-to-Equity | > 1.5 | 0.3–0.8 | < 0.3 | TSMC < 0.3 historically |
| Interest Coverage | < 5x | 8–20x | > 25x | |
| Inventory Turnover | < 4x | 5–8x | > 10x | Cycle time ~60-90 days |
| Receivables Turnover | < 5x | 6–10x | > 12x | |
| Asset Turnover | < 0.4 | 0.5–0.8 | > 0.9 | Fab capex anchors denominator |
| Cash Conversion Cycle | > 90 days | 50–75 days | < 40 days | |
| P/E | — | 15–25x | — | Cyclical discount applies |
| EV/EBITDA | — | 8–15x | — | |

**Cyclicality warning**: Semiconductor ratios swing 30–50% peak-to-trough in down cycles. A single-year snapshot is unreliable. Always use 3-year average or TTM adjusted for cycle position.

---

### 3. Contract Electronics Manufacturing (EMS/ODM)

Foxconn, Pegatron, Compal tier — thin-margin assembly.

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Gross Margin | < 4% | 5–8% | > 10% | Thin by design |
| Operating Margin | < 1% | 2–4% | > 5% | |
| Net Margin | < 1% | 2–3.5% | > 4% | |
| ROE | < 8% | 12–18% | > 20% | Volume compensates margins |
| Inventory Turnover | < 8x | 10–15x | > 18x | Speed is the business model |
| Current Ratio | < 1.0 | 1.1–1.4 | > 1.6 | Negative working capital common |
| Debt-to-Equity | > 1.5 | 0.5–1.0 | < 0.5 | |

---

### 4. Grocery / Food Retail

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Gross Margin | < 20% | 25–30% | > 35% | Private label lifts margins |
| Operating Margin | < 1% | 2–4% | > 5% | |
| Net Margin | < 0.5% | 1–3% | > 3.5% | |
| Current Ratio | < 0.7 | 0.8–1.1 | > 1.3 | Negative WC normal (FMCG terms) |
| Quick Ratio | < 0.3 | 0.4–0.7 | > 0.8 | |
| Inventory Turnover | < 10x | 15–25x | > 30x | Perishables → high turns |
| Receivables Turnover | < 20x | 30–50x | > 60x | Cash sales dominate |
| Debt-to-Equity | > 2.0 | 0.8–1.5 | < 0.8 | Lease obligations inflate |

**Key insight**: A grocery current ratio of 0.9 is not a red flag. Suppliers accept 30-day payables while customers pay instantly — the business is structurally a short-term creditor to suppliers. Never apply the "current ratio > 1.5" rule of thumb here.

---

### 5. Specialty Retail (Apparel, Electronics Stores)

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Gross Margin | < 30% | 40–50% | > 55% | Brand premium matters |
| Operating Margin | < 5% | 8–12% | > 15% | |
| Net Margin | < 3% | 5–9% | > 12% | |
| Current Ratio | < 1.0 | 1.3–1.8 | > 2.0 | More inventory than grocery |
| Inventory Turnover | < 3x | 4–6x | > 8x | Seasonal demand drives variation |
| Debt-to-Equity | > 2.0 | 0.5–1.2 | < 0.5 | |

---

### 6. Automotive Manufacturing (OEM)

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Gross Margin | < 10% | 14–20% | > 22% | |
| Operating Margin | < 3% | 5–10% | > 12% | |
| Net Margin | < 2% | 4–7% | > 9% | |
| Current Ratio | < 0.9 | 1.1–1.5 | > 1.7 | |
| Inventory Turnover | < 6x | 8–12x | > 14x | JIT reduces this |
| Debt-to-Equity | > 2.5 | 1.0–2.0 | < 1.0 | Captive finance arms inflate |
| Interest Coverage | < 3x | 5–10x | > 12x | Cyclical: stress-test at trough |

---

### 7. Healthcare & Pharmaceuticals

Biopharmaceuticals and hospital operators differ significantly — table shows pharma.

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Gross Margin | < 55% | 65–80% | > 85% | Patent-protected products |
| Operating Margin | < 10% | 20–30% | > 35% | R&D expense large |
| Net Margin | < 8% | 15–25% | > 30% | |
| ROE | < 10% | 15–25% | > 30% | |
| Debt-to-Equity | > 1.5 | 0.4–0.9 | < 0.3 | |
| Interest Coverage | < 5x | 8–20x | > 25x | |
| Receivables Turnover | < 4x | 5–8x | > 10x | Payer disputes slow collection |

---

### 8. Telecommunications

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Gross Margin | < 40% | 50–65% | > 70% | |
| Operating Margin | < 8% | 15–25% | > 28% | |
| EBITDA Margin | < 25% | 35–45% | > 50% | Better than net margin here |
| Debt-to-Equity | > 3.0 | 1.5–2.5 | < 1.5 | Network capex funded by debt |
| Interest Coverage | < 3x | 4–7x | > 8x | |
| Asset Turnover | < 0.2 | 0.3–0.5 | > 0.6 | Spectrum + tower assets heavy |
| EV/EBITDA | — | 6–9x | — | Standard telecom valuation |

---

### 9. Commercial Banking

Banks are structurally different — do NOT apply standard leverage ratios.

| Ratio | Weak | Median | Strong | Notes |
|-------|------|--------|--------|-------|
| Net Interest Margin (NIM) | < 2% | 2.5–3.5% | > 4% | Revenue driver |
| Return on Assets (ROA) | < 0.5% | 0.8–1.2% | > 1.5% | Industry-specific interpretation |
| Return on Equity (ROE) | < 8% | 12–16% | > 18% | |
| Efficiency Ratio | > 65% | 50–60% | < 50% | Lower = better (cost/income) |
| Tier 1 Capital Ratio | < 10% | 12–15% | > 15% | Regulatory, not accounting |
| Non-Performing Loan % | > 3% | 1–2% | < 1% | Credit quality |
| Loan-to-Deposit Ratio | > 90% | 70–80% | < 70% | Liquidity risk proxy |

**Do not use D/E for banks** — banks are structurally highly leveraged (10:1+ assets to equity) by design. Use capital adequacy ratios instead.

---

## Red / Yellow / Green Decision Framework

When you have a ratio value and an industry benchmark, use this decision logic:

```
function classify_ratio(value, median, direction):
    # direction: "higher_is_better" or "lower_is_better"
    
    if direction == "higher_is_better":
        band_green  = median * 1.10   # ≥ 110% of median
        band_yellow = median * 0.85   # 85–110% of median
        # below 85% → red
        
        if value >= band_green:  return "🟢"
        if value >= band_yellow: return "🟡"
        return "🔴"
    
    else:  # lower_is_better (D/E, CCC, NPL%)
        band_green  = median * 0.90   # ≤ 90% of median
        band_yellow = median * 1.20   # 90–120% of median
        # above 120% → red
        
        if value <= band_green:  return "🟢"
        if value <= band_yellow: return "🟡"
        return "🔴"
```

**Adjustment rules:**
- Widen bands to ±25% for cyclical industries (semis, auto) — point-in-time variance is high
- Narrow bands to ±10% for stable industries (telecom, utilities) — persistent deviation is more meaningful
- Override with "N/A" if the ratio is structurally inapplicable (e.g., D/E for banks, inventory turnover for pure-service firms)

---

## Worked Example: Taiwanese Electronics Manufacturer

This extends the example in the parent SKILL.md with full benchmark comparison.

**Company**: Mid-tier Taiwan PCB manufacturer (anonymized), FY2023
**Industry**: Electronics Manufacturing / PCB (between Semiconductor and EMS benchmarks)

### Step 1 — Gather Ratios

| Ratio | Company Value |
|-------|--------------|
| Gross Margin | 18% |
| Operating Margin | 8% |
| Net Margin | 5% |
| ROE | 9% |
| ROA | 4% |
| Current Ratio | 1.8 |
| Quick Ratio | 1.2 |
| Debt-to-Equity | 1.2 |
| Interest Coverage | 6x |
| Inventory Turnover | 4.2x |
| Receivables Turnover | 7x |
| Asset Turnover | 0.55 |
| Cash Conversion Cycle | 78 days |

### Step 2 — Apply Benchmarks

PCB manufacturers occupy the middle ground between EMS (thin margins) and full semiconductor. Use Semiconductor & Electronics Manufacturing benchmarks with a 15% downward adjustment on margins.

Adjusted medians for PCB:
- Gross Margin median: 40% × 0.85 = **34%**
- Operating Margin median: **10%**
- Net Margin median: **8%**
- ROE median: **14%**
- Inventory Turnover median: **6x**
- D/E median: **0.7**

### Step 3 — Classify

| Ratio | Company | Benchmark Median | Status | Note |
|-------|---------|-----------------|--------|------|
| Gross Margin | 18% | 34% | 🔴 | 53% of median — far below |
| Operating Margin | 8% | 10% | 🟡 | 80% of median |
| Net Margin | 5% | 8% | 🔴 | 63% of median |
| ROE | 9% | 14% | 🔴 | 64% of median |
| ROA | 4% | 8% | 🔴 | 50% of median |
| Current Ratio | 1.8 | 2.0 | 🟡 | 90% of median — acceptable |
| Quick Ratio | 1.2 | 1.4 | 🟡 | 86% of median |
| D/E | 1.2 | 0.7 | 🔴 | 171% of median — elevated |
| Interest Coverage | 6x | 10x | 🔴 | 60% of median |
| Inventory Turnover | 4.2x | 6x | 🔴 | 70% of median — slow |
| Receivables Turnover | 7x | 8x | 🟡 | 88% of median |
| Asset Turnover | 0.55 | 0.65 | 🟡 | 85% of median |
| Cash Conversion Cycle | 78 days | 62 days | 🔴 | 26% longer than median |

### Step 4 — Synthesize

| Category | Status | Key Metric | Interpretation |
|----------|--------|-----------|----------------|
| Profitability | 🔴 | Gross Margin 18% vs 34% | Severe margin compression; cost structure out of line |
| Liquidity | 🟡 | Current 1.8, Quick 1.2 | Adequate but not comfortable; trending matters |
| Leverage | 🔴 | D/E 1.2 vs 0.7; coverage 6x | Elevated debt at the same time profitability is weak |
| Efficiency | 🔴 | Inventory 4.2x vs 6x; CCC 78d | Slow inventory likely accumulating unsold goods |
| Valuation | N/A | Not provided | Would need market price |

**Verdict**: This company shows a pattern consistent with a **demand slowdown / margin squeeze** cycle:
1. Revenues likely flat or falling (asset turnover declining)
2. Inventory building up (slow turnover) → working capital stress
3. Margins compressed (fixed costs spread over lower volume)
4. Leverage rising (debt taken to bridge cash shortfall)
5. Liquidity still adequate but deteriorating trajectory is the risk

**Red flag trigger**: If inventory turnover falls below 3.5x next quarter AND interest coverage drops below 4x → serious default risk warrants debt covenant review.

---

## How to Source Benchmarks

When working with real companies, use these sources in priority order:

1. **Damodaran Online** (pages.stern.nyu.edu/~adamodar/) — Annual industry-level financial data by sector; free; covers 90+ industries; updated January each year. Download the "Key Statistics by Sector" spreadsheet.

2. **Taiwan Stock Exchange (TWSE) Market Observation Post System** (mops.twse.com.tw) — For TW-listed companies: sector financial ratios by industry classification. Free; quarterly updates. Filter by industry code (e.g., 2300 for electronics).

3. **Bloomberg/FactSet** — If available: use the "COMP" function (Bloomberg) to pull peer group ratios. Most precise; subscription required.

4. **Annual reports of 3 direct peers** — Manual calculation from public filings is slower but most comparable because you control the definition of each ratio.

5. **Industry association reports** — SEMI, IPC (for PCB), Taiwan's TEEMA, etc. — often include margin surveys; useful for private-company comparison.

**When no good benchmark exists**: Use Damodaran's closest adjacent industry. Note the substitution explicitly in your analysis. Never silently extrapolate — a wrong benchmark is worse than no benchmark.

---

## Common Benchmark Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Using a global benchmark for a TW-listed company | Taiwan market has structurally lower margins due to customer concentration (Apple, etc.) | Use TWSE sector data or TW-specific peers |
| Comparing FY2021 company data to current benchmarks | Post-COVID normalization shifted many sector medians 5–10% | Match benchmark year to company data year |
| Using SIC/NAICS codes to select benchmark without checking | A "computer manufacturer" SIC can include both pure fabless chip design and EMS | Verify the benchmark actually matches the business model |
| Treating valuation benchmarks as ratio benchmarks | P/E median of 20x says nothing about whether P/E of 15x is "green" for this company | Valuation ratios require DCF or comparables skill, not ratio analysis |
| Applying manufacturing benchmarks to a platform/marketplace hybrid | Platform gross margins (70%+) are structurally different from product margins | Separate product and platform revenue streams first |

---

## Quick-Reference Card

For rapid field use without the full tables:

| If industry is... | Gross Margin expect | Net Margin expect | D/E expect | Current Ratio expect |
|-------------------|--------------------|--------------------|------------|---------------------|
| Pure SaaS | 70–80% | 12–20% | < 0.5 | 2.5–4.0 |
| Semiconductor (IDM) | 45–55% | 18–28% | 0.3–0.7 | 1.8–2.5 |
| Electronics MFG | 15–35% | 3–10% | 0.4–1.0 | 1.2–2.0 |
| EMS/ODM | 5–8% | 2–3% | 0.5–1.0 | 1.0–1.4 |
| Grocery retail | 25–30% | 1–3% | 0.8–1.5 | 0.8–1.1 |
| Specialty retail | 40–50% | 5–9% | 0.5–1.2 | 1.3–1.8 |
| Auto OEM | 14–20% | 4–7% | 1.0–2.0 | 1.1–1.5 |
| Pharma | 65–80% | 15–25% | 0.4–0.9 | 2.0–3.5 |
| Telecom | 50–65% | 8–15% | 1.5–2.5 | 0.8–1.3 |
| Bank | NIM 2.5–3.5% | ROA 0.8–1.2% | N/A (use capital ratio) | N/A |
