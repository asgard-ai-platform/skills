# Example: SaaS Startup First Full Year Tax Planning

## Scenario

Aether Labs Co., Ltd. (以太實驗室有限公司) is a Taiwan-incorporated B2B SaaS startup that completed its first full operating year (2025). The founder asks:

> "We just closed our books for 2025. Revenue was NT$8.2M, mostly from domestic enterprise clients, but we also had two foreign clients (USD-denominated). We pay AWS and a US contractor monthly. What taxes do we owe, when do we file, and are there any breaks we can take?"

**Key financials (2025)**:
- Domestic SaaS revenue: NT$7,400,000
- Foreign client revenue (exported): NT$800,000 (already invoiced in USD)
- AWS monthly spend: ~USD $2,000/month (≈ NT$768,000/year)
- US contractor (design): USD $1,500/month (≈ NT$576,000/year)
- Employee salaries (3 staff): NT$3,600,000
- Office rent: NT$480,000
- R&D software tools + prototype hardware: NT$1,200,000
- Other operating expenses: NT$360,000
- Taxable income before incentives: NT$8,200,000 − NT$6,408,000 = NT$1,792,000 (before R&D deduction)

---

## Analysis

### Step 1 — Identify Applicable Taxes

All three core taxes apply:

| Tax | Applicable? | Reason |
|-----|-------------|--------|
| 營業稅 | Yes | Selling services domestically; VAT-registered |
| 營所稅 | Yes | Profitable; incorporated as 有限公司 |
| 扣繳 | Yes | Paying salaries + foreign vendors |

---

### Step 2 — 營業稅 (VAT) Calculation

**Output tax** (domestic sales only — export is zero-rated):
- NT$7,400,000 × 5% = NT$370,000 collected

**Input tax** (domestic purchases with 統一發票):
- Office rent: NT$480,000 × 5% = NT$24,000
- R&D hardware/tools (domestic): NT$600,000 × 5% = NT$30,000
- Other domestic expenses (with invoices): NT$180,000 × 5% = NT$9,000
- **Total input tax: NT$63,000**

> ⚠️ AWS spend (NT$768,000) is a foreign purchase — no Taiwan VAT input credit available. It is subject to withholding, not VAT input offset.

**Net VAT payable (2025)**: NT$370,000 − NT$63,000 = **NT$307,000**
(spread across 6 bimonthly filings, averaging ~NT$51,167/filing)

**Filing dates**: Jan 15, Mar 15, May 15, Jul 15, Sep 15, Nov 15 (for each prior 2-month period)

---

### Step 3 — 扣繳 (Withholding Tax) — Foreign Vendors

This is the most commonly missed obligation.

**AWS (US corporation, no tax treaty benefit for this structure)**:
- Annual spend: NT$768,000
- Withholding rate: 20% on service fees paid to non-resident entities
- **Withholding required: NT$153,600**
- Aether Labs must gross up payments and remit 20% to 國稅局 by the 10th of each following month

**US contractor (individual, non-resident)**:
- Annual payments: NT$576,000
- Professional service fee withholding: 20%
- **Withholding required: NT$115,200**

> ⚠️ Many startups pay AWS/GCP at face value and don't withhold. This triggers back-taxes + 10% surcharge penalties at audit. Consult your CPA on whether a ruling letter or treaty position is available.

**Domestic employee withholding**:
- NT$3,600,000 in salaries → monthly withholding at applicable bracket (5% if monthly salary > NT$84,501 threshold for 2025)
- Filed monthly by the 10th; annual 扣繳憑單 filed by January 31, 2026

---

### Step 4 — 營所稅 (Corporate Income Tax)

**Revenue**: NT$8,200,000

**Deductions**:
| Item | Amount |
|------|--------|
| Employee salaries | NT$3,600,000 |
| Office rent | NT$480,000 |
| R&D expenses (base) | NT$1,200,000 |
| R&D additional 200% deduction (產創條例) | NT$1,200,000 × 100% extra = NT$1,200,000 |
| AWS + contractor (net of withholding) | NT$1,344,000 |
| Other operating expenses | NT$360,000 |
| **Total deductions** | **NT$8,184,000** |

**Taxable income**: NT$8,200,000 − NT$8,184,000 = **NT$16,000**

NT$16,000 ≤ NT$120,000 → **全額免稅** (zero CIT due)

> The R&D super-deduction under 產創條例 Article 10 cuts taxable income dramatically. Qualifying R&D spend must be documented with project plans, expenditure receipts, and filed for pre-approval with MOEA in some cases — confirm with CPA before claiming.

**Interim tax (暫繳)**: Since 2024 was the first year (no prior-year tax base), no interim filing required in September 2025. For September 2026, interim will be 50% of 2025 final CIT — which is NT$0 here, so again NT$0 due.

**Annual CIT filing deadline**: May 1–31, 2026 (for fiscal year 2025)

---

### Step 5 — Available Incentives Checklist

| Incentive | Eligible? | Benefit |
|-----------|----------|---------|
| 產創條例 R&D 超級扣除 (200%) | **Yes** — software R&D qualifies | NT$1,200,000 extra deduction → effectively NT$0 CIT |
| 天使投資人減稅 | N/A (applies to individual investors, not company) | — |
| ESOP 遞延課稅 | Eligible if options issued to employees | Defers employee tax to exercise date |
| 小規模免稅 (≤NT$120K) | **Yes** — taxable income after deductions = NT$16K | NT$0 CIT |

---

## Result

```markdown
# Taiwan Tax Assessment: Aether Labs Co., Ltd. (FY 2025)

## Tax Obligations
| Tax | Applicable? | Rate | Next Filing |
|-----|-----------|------|------------|
| 營業稅 | Y | 5% | Jan 15, 2026 (Nov–Dec period) |
| 營所稅 | Y | 20% | May 1–31, 2026 |
| 扣繳 | Y | 20% (foreign) / 5% (domestic salary) | 10th of each month |

## Estimated Tax Liability
| Tax | Estimated Amount | Notes |
|-----|-----------------|-------|
| 營業稅 (net) | NT$307,000 / year | Output NT$370K − Input NT$63K |
| 營所稅 | NT$0 | Taxable income NT$16K < NT$120K threshold |
| 扣繳 (AWS) | NT$153,600 | 20% of NT$768K; must gross up |
| 扣繳 (US contractor) | NT$115,200 | 20% of NT$576K |
| 扣繳 (domestic salaries) | ~NT$36,000–72,000 | Bracket-dependent; remit monthly |

## Available Incentives
| Incentive | Eligible? | Estimated Benefit |
|-----------|----------|------------------|
| 產創條例 R&D 超級扣除 | Yes | NT$1,200,000 additional deduction → NT$0 CIT |
| 小規模免稅 | Yes (result of deductions) | NT$0 CIT |
| ESOP 遞延課稅 | Consider issuing | Defers employee income tax |

## Action Items
1. **Immediately**: Set up monthly withholding remittance for AWS and US contractor — back-pay Jan–Dec 2025 amounts and consult CPA on penalty waiver options if not yet done.
2. **January 31, 2026**: File 扣繳憑單 (annual withholding statement) for all 2025 payments.
3. **Before May 31, 2026**: File 營所稅 return; prepare R&D documentation for 產創條例 deduction claim.
4. **For 2026 planning**: Pre-qualify R&D projects with MOEA documentation before spend begins — don't reconstruct records retroactively.
5. **Engage a licensed 會計師**: Foreign vendor withholding and R&D super-deduction both require professional filing; errors carry 10–30% surcharge penalties.
```
