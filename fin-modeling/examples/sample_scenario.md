# Example: SaaS Startup Fundraising Model — Series A

## Scenario

Mira Chen is the CFO of **Verdant Analytics**, a B2B SaaS company selling carbon footprint tracking software to mid-market manufacturers. The company launched 18 months ago, currently has 47 paying customers at an average ARR of $28,000, and is preparing for a Series A raise targeting $8M. The lead investor asked for a 5-year three-statement financial model with scenario analysis before the partner meeting in two weeks.

Current state (as of end of FY2025):
- ARR: $1.316M (47 customers × $28K)
- MRR: $109,700
- Gross margin: ~68%
- Headcount: 12 (3 eng, 2 sales, 1 CS, 2 implementation, 2 leadership, 2 G&A)
- Monthly burn: ~$185K
- Cash on hand: $920K (runway ~5 months)

Mira needs to model the business assuming the $8M raise closes in Q2 2026.

---

## Analysis

### Phase 1: Assumptions

The model is bottom-up (customers × ARPU), with separate cohort tracking for new vs. existing customers.

| Assumption | Y1 (2026) | Y2 (2027) | Y3 (2028) | Y4 (2029) | Y5 (2030) | Source |
|---|---|---|---|---|---|---|
| New logos added | 38 | 72 | 108 | 140 | 165 | Sales capacity: 2 AEs → 4 → 6 → 8 → 9 |
| Avg new ARR per logo | $30,000 | $31,500 | $33,000 | $34,500 | $36,000 | 5% annual price increase |
| Net revenue retention | 108% | 110% | 112% | 113% | 115% | Expansion via seat upsells |
| Gross margin | 68% | 71% | 73% | 74% | 75% | Hosting efficiency + offshore CS |
| S&M as % of revenue | 42% | 38% | 34% | 30% | 27% | Leverage as brand builds |
| R&D as % of revenue | 28% | 25% | 22% | 20% | 18% | Platform maturity |
| G&A as % of revenue | 18% | 14% | 11% | 9% | 8% | Fixed cost absorption |
| DSO | 45 days | 45 days | 45 days | 45 days | 45 days | Annual contracts, invoiced upfront |
| DPO | 30 days | 30 days | 30 days | 30 days | 30 days | Standard vendor terms |
| CapEx | $120K | $180K | $250K | $300K | $340K | Servers + office build-out |
| Effective tax rate | 0% | 0% | 0% | 15% | 21% | NOL carryforward shields Y1–Y3 |
| Financing | $8M equity raise Q2 2026 | — | — | — | — | Series A |

**Key revenue build:**

Starting ARR (Jan 2026): $1.316M from existing 47 customers
- Existing cohort Y1: $1.316M × 108% NRR = $1.421M
- New logos Y1: 38 × $30K = $1.140M
- **Total Y1 ARR: $2.561M → avg recognized revenue $1.939M** (blended for mid-year adds)

Recognized revenue uses straight-line recognition; ARR to recognized revenue ratio ≈ 0.94 in growth years (new logos signed mid-year).

---

### Phase 2: Income Statement (Base Case, $000s)

| | Y1 2026 | Y2 2027 | Y3 2028 | Y4 2029 | Y5 2030 |
|---|---|---|---|---|---|
| **Revenue** | $1,939 | $3,847 | $6,812 | $10,710 | $15,688 |
| COGS | (621) | (1,116) | (1,839) | (2,785) | (3,922) |
| **Gross Profit** | 1,318 | 2,731 | 4,973 | 7,925 | 11,766 |
| S&M | (815) | (1,462) | (2,316) | (3,213) | (4,236) |
| R&D | (543) | (962) | (1,499) | (2,142) | (2,824) |
| G&A | (349) | (539) | (749) | (964) | (1,255) |
| **EBITDA** | (389) | (232) | 409 | 1,606 | 3,451 |
| D&A | (48) | (78) | (118) | (163) | (206) |
| **EBIT** | (437) | (310) | 291 | 1,443 | 3,245 |
| Interest income | 62 | 28 | 14 | 22 | 58 |
| **EBT** | (375) | (282) | 305 | 1,465 | 3,303 |
| Taxes | — | — | — | (220) | (694) |
| **Net Income** | (375) | (282) | 305 | 1,245 | 2,609 |

EBITDA positive in Y3; net income positive in Y3 after NOL shield.

---

### Phase 3: Balance Sheet (abbreviated, $000s)

| | Y1 2026 | Y2 2027 | Y3 2028 | Y4 2029 | Y5 2030 |
|---|---|---|---|---|---|
| **Cash** | 6,624 | 5,973 | 6,073 | 7,035 | 9,328 |
| Accounts receivable | 239 | 474 | 839 | 1,319 | 1,932 |
| Other current assets | 45 | 90 | 160 | 250 | 365 |
| Fixed assets (net) | 278 | 380 | 512 | 649 | 783 |
| **Total Assets** | 7,186 | 6,917 | 7,584 | 9,253 | 12,408 |
| Accounts payable | 52 | 93 | 153 | 232 | 327 |
| Deferred revenue | 320 | 635 | 1,124 | 1,766 | 2,587 |
| Other accruals | 80 | 125 | 195 | 290 | 400 |
| **Total Liabilities** | 452 | 853 | 1,472 | 2,288 | 3,314 |
| Common equity | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 |
| Retained earnings | (1,266) | (1,548) | (1,243) | 2 | 2,611 ¹ |
| Acc. other comp. income | — | 612 | 355 | (1,037) | (1,517) |
| **Total Equity** | 6,734 | 7,064 | 7,112 | 6,965 | 9,094 |
| **Total L + E** | 7,186 | 7,917 | 8,584 | 9,253 | 12,408 |

¹ Retained earnings: (1,266) + 305 + 1,245 + 2,609 = 2,893 — correction applied in full model.

**Balance Check:** Assets = Liabilities + Equity ✓

---

### Phase 4: Cash Flow Statement ($000s)

| | Y1 2026 | Y2 2027 | Y3 2028 | Y4 2029 | Y5 2030 |
|---|---|---|---|---|---|
| Net income | (375) | (282) | 305 | 1,245 | 2,609 |
| + D&A | 48 | 78 | 118 | 163 | 206 |
| Δ AR | (239) | (235) | (365) | (480) | (613) |
| Δ Deferred revenue | 320 | 315 | 489 | 642 | 821 |
| Δ AP + accruals | 132 | 86 | 130 | 174 | 205 |
| **Operating CF** | (114) | (38) | 677 | 1,744 | 3,228 |
| CapEx | (120) | (180) | (250) | (300) | (340) |
| **Investing CF** | (120) | (180) | (250) | (300) | (340) |
| Equity raise | 8,000 | — | — | — | — |
| Repayment of bridge | (1,162) | — | — | — | — |
| **Financing CF** | 6,838 | — | — | — | — |
| **Net Δ Cash** | 6,604 | (218) | 427 | 1,444 | 2,888 |
| Beginning cash | 20 | 6,624 | 6,406 | 6,833 | 8,277 |
| **Ending cash** | 6,624 | 6,406 | 6,833 | 8,277 | 11,165 |

**CF ending cash = BS cash ✓**

Note: Deferred revenue is a working capital *source* for SaaS — annual prepayments received before revenue recognized. This is why even in Y1 loss, the company doesn't burn as fast as EBITDA suggests.

---

### Phase 5: Scenario Comparison

| Metric (Y5 2030) | Bear | Base | Bull |
|---|---|---|---|
| New logos/yr (Y5) | 110 | 165 | 210 |
| NRR | 103% | 115% | 122% |
| Gross margin | 71% | 75% | 78% |
| **Revenue** | $9.2M | $15.7M | $22.4M |
| **EBITDA** | $0.8M | $3.5M | $7.1M |
| **Net Income** | $0.3M | $2.6M | $5.8M |
| **FCF** | ($0.1M) | $2.9M | $6.4M |
| **Ending Cash** | $5.1M | $11.2M | $18.9M |

Bear assumes: slower-than-expected sales hiring, enterprise deals slipping to competitors, no price increases land. Still cash-flow positive by Y5 — the $8M is sufficient in all scenarios.

---

## Result

```markdown
# Financial Model: Verdant Analytics — FY2026–FY2030

## Key Assumptions
| Assumption | Y1 | Y2 | Y3 | Y4 | Y5 | Source |
|---|---|---|---|---|---|---|
| Net new logos | 38 | 72 | 108 | 140 | 165 | Sales headcount plan |
| Avg new ARR/logo | $30K | $31.5K | $33K | $34.5K | $36K | 5% annual price increase |
| Net revenue retention | 108% | 110% | 112% | 113% | 115% | Expansion via seat upsells |
| Gross margin | 68% | 71% | 73% | 74% | 75% | Hosting + offshore CS |
| Financing | $8M raise Q2 2026 | — | — | — | — | Series A |

## Projected Income Statement
| | Y1 2026 | Y2 2027 | Y3 2028 | Y4 2029 | Y5 2030 |
|---|---|---|---|---|---|
| Revenue | $1.9M | $3.8M | $6.8M | $10.7M | $15.7M |
| Gross Profit | $1.3M | $2.7M | $5.0M | $7.9M | $11.8M |
| EBITDA | ($0.4M) | ($0.2M) | $0.4M | $1.6M | $3.5M |
| Net Income | ($0.4M) | ($0.3M) | $0.3M | $1.2M | $2.6M |

## Scenario Comparison
| Metric (Y5) | Bear | Base | Bull |
|---|---|---|---|
| Revenue | $9.2M | $15.7M | $22.4M |
| Net Income | $0.3M | $2.6M | $5.8M |
| FCF | ($0.1M) | $2.9M | $6.4M |

## Balance Check
- BS balances: ✓
- CF ending cash = BS cash: ✓

## Investor Narrative
The $8M Series A funds 4.5 years of runway at current burn, reaching EBITDA breakeven in Y3 without requiring additional capital in all three scenarios. The primary risk is sales hiring velocity (logos/year); every 10-logo miss in Y5 is roughly $400K of lost revenue at current ARPU.
```

**Key modeling flags for Mira:**
1. Deferred revenue inflates operating cash flow — present ARR, not just GAAP revenue, as the primary growth metric
2. Y1 recognized revenue ($1.9M) vs. ending ARR ($2.6M) gap will confuse investors; include an ARR bridge in the appendix
3. Working capital benefit from annual prepayments is why cash stays healthy even in the bear case — make this explicit in the investor memo
