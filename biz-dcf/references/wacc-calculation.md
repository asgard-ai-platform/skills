# WACC Calculation Reference

WACC (Weighted Average Cost of Capital) is the discount rate used in DCF. It represents the blended required return across all capital providers — equity holders and debt holders — weighted by their proportion in the capital structure.

```
WACC = (E/V × Re) + (D/V × Rd × (1 - Tax))
```

| Symbol | Meaning |
|--------|---------|
| E | Market value of equity (market cap) |
| D | Market value of debt (book value is acceptable proxy) |
| V | E + D (total capital) |
| Re | Cost of equity |
| Rd | Cost of debt (pre-tax) |
| Tax | Effective corporate tax rate |

---

## Step 1: Cost of Equity (Re) via CAPM

```
Re = Rf + β × ERP + CRP
```

| Component | Symbol | Description |
|-----------|--------|-------------|
| Risk-free rate | Rf | Yield on long-term government bond |
| Beta | β | Systematic risk relative to market |
| Equity risk premium | ERP | Expected excess return of equities over risk-free |
| Country risk premium | CRP | Add-on for non-US/non-developed markets |

### Choosing Rf

Use the **10-year government bond yield** in the company's home currency.

| Market | Typical Rf (2024-2025) |
|--------|------------------------|
| Taiwan (10Y govt) | 1.5 – 2.0% |
| US Treasury 10Y | 4.0 – 4.5% |
| Eurozone (Bund 10Y) | 2.0 – 2.5% |

Do not mix currencies: if projecting FCF in NTD, use NTD risk-free rate.

### Estimating Beta

**Option A — Public company (preferred):** Use 2-year weekly or 5-year monthly regression of stock returns vs. index returns. Adjust with Blume's formula to reduce extremes:

```
Adjusted β = 0.67 × Raw β + 0.33 × 1.0
```

**Option B — Private company:** Use industry peer beta. Steps:
1. Collect betas for 5–10 public peers
2. Unlever each: `βu = β / (1 + (1 - Tax) × D/E)`
3. Average the unlevered betas
4. Re-lever using the subject company's target D/E: `β = βu × (1 + (1 - Tax) × D/E)`

**Industry beta benchmarks (Taiwan tech sector, 2024 approximate):**

| Sub-sector | Unlevered β range |
|------------|-------------------|
| Fabless semiconductor | 1.0 – 1.4 |
| OSAT / IC packaging | 0.8 – 1.1 |
| Enterprise SaaS | 0.9 – 1.3 |
| E-commerce platform | 0.9 – 1.2 |
| Traditional manufacturing | 0.5 – 0.8 |

### Equity Risk Premium (ERP)

Damodaran's implied ERP is the standard reference. Common values:

| Market | ERP |
|--------|-----|
| US (mature market baseline) | 4.5 – 5.5% |
| Taiwan | 5.0 – 6.0% |
| China / emerging markets | 6.0 – 8.0% |

### Country Risk Premium (CRP)

Add CRP when valuing companies in markets where government default risk or institutional uncertainty is non-trivial. Damodaran's formula:

```
CRP = Default Spread × (σEquity / σBonds)
```

Where σEquity/σBonds is the relative volatility of equity vs. bond returns (typically 1.5× for emerging markets).

**Simpler proxy:** Look up Damodaran's "Country Default Spreads and Risk Premiums" table directly. For Taiwan, CRP is typically 0–0.5% given strong sovereign credit rating (AA).

---

## Step 2: Cost of Debt (Rd)

Rd is the **pre-tax** expected cost of new borrowing, not the historical average on existing debt.

**Priority order for estimation:**

1. **Marginal borrowing rate**: If the company recently issued debt or has a credit facility, use that coupon rate.
2. **Synthetic credit rating**: For companies without rated debt, estimate the credit rating from interest coverage ratio:

| Interest Coverage (EBIT/Interest) | Implied Rating | Spread over Rf |
|----------------------------------|----------------|----------------|
| > 8.5× | AAA | +0.5% |
| 6.5 – 8.5× | AA | +0.8% |
| 5.5 – 6.5× | A+ | +1.0% |
| 4.25 – 5.5× | A | +1.2% |
| 3.0 – 4.25× | A− | +1.5% |
| 2.5 – 3.0× | BBB | +2.0% |
| 2.0 – 2.5× | BB | +3.0% |
| < 2.0× | B or below | +4.0%+ |

3. **Book value proxy**: Use total interest expense / average total debt. Only acceptable for stable, mature companies with fixed-rate debt.

**After-tax cost of debt:**
```
Rd (after-tax) = Rd × (1 - Tax Rate)
```

---

## Step 3: Capital Structure Weights (E/V, D/V)

**Use target capital structure, not current snapshot.** Reasons:
- Current capital structure may be temporarily distorted (pre-IPO, mid-restructuring)
- DCF values the business going-forward, not at a frozen point in time

**How to determine target:**
1. Use management's stated leverage target (e.g., "maintain net debt/EBITDA < 2×")
2. Use industry median D/(D+E) from comparable public companies
3. If no clear guidance, iterate: estimate → compute DCF → check implied D/E → adjust

**Circular reference warning:** WACC requires equity value (market cap), but DCF produces equity value. Solutions:

- For public companies: use current market cap as starting point, iterate 2–3 rounds until stable
- For private companies: use peer median D/E ratios as target structure
- Accept the approximation if the D/E ratio is stable and small

---

## Worked Example: Taiwan SaaS Company

**Company profile:**
- Public company, NT$2.0B market cap
- NT$300M total debt (bank loans)
- EBIT NT$120M, Interest NT$15M → Coverage 8.0×
- Tax rate 20% (Taiwan corporate tax)
- Beta (5-year monthly vs. TAIEX): 1.15 raw → adjusted: 0.67 × 1.15 + 0.33 = 1.10

**Step 1: Cost of Equity**

```
Rf   = 1.8% (Taiwan 10Y govt bond)
β    = 1.10 (adjusted)
ERP  = 5.5% (Taiwan market, Damodaran 2024)
CRP  = 0.3% (Taiwan sovereign, minimal)

Re = 1.8% + 1.10 × 5.5% + 0.3%
   = 1.8% + 6.05% + 0.3%
   = 8.15%
```

**Step 2: Cost of Debt**

```
Coverage = 120 / 15 = 8.0× → Implied AA → Spread +0.8%
Rd (pre-tax)  = 1.8% + 0.8% = 2.6%
Rd (after-tax) = 2.6% × (1 - 0.20) = 2.08%
```

Cross-check: actual interest / debt = 15 / 300 = 5.0%. This is higher than the implied 2.6%, suggesting existing debt is at above-market rates (legacy fixed loans). Use the **marginal rate** (2.6%) for WACC since DCF projects forward value.

**Step 3: Capital Structure**

```
E = NT$2,000M (market cap)
D = NT$300M (book value proxy)
V = NT$2,300M

E/V = 2,000 / 2,300 = 86.96%
D/V = 300 / 2,300 = 13.04%
```

**Step 4: WACC**

```
WACC = (86.96% × 8.15%) + (13.04% × 2.08%)
     = 7.09% + 0.27%
     = 7.36%

Round to: 7.5% (use round numbers to avoid false precision)
```

**Sanity check:** For a Taiwan listed SaaS with low leverage, 7–9% WACC is normal. If you get 12%+, re-examine beta or ERP inputs.

---

## WACC Sanity Check Table

Use this to spot obvious errors before running DCF.

| Company Profile | Expected WACC Range |
|----------------|---------------------|
| Taiwan large-cap, stable, low debt | 6 – 8% |
| Taiwan growth tech, no debt | 8 – 11% |
| Taiwan mid-cap manufacturing | 7 – 10% |
| High-yield / distressed debt | 12 – 18% |
| US large-cap S&P500 company | 8 – 11% |
| Emerging market company | 10 – 15% |

If WACC is below the risk-free rate, something is wrong.  
If WACC exceeds 20% for a going-concern profitable company, re-examine beta and debt inputs.

---

## Common Errors

**Using book value of equity instead of market cap for weights**  
Book equity can be tiny (retained losses, accounting write-downs) or inflated vs. intrinsic value. Always use market cap. For private companies, use the equity value implied by peer EV/EBITDA multiples.

**Using historical average Rd instead of marginal cost**  
A company with 8% fixed bonds issued in a high-rate environment does NOT have Rd = 8% for DCF purposes if current market rates are 4%. The DCF discounts future cash flows at the rate a rational investor requires today.

**Ignoring tax shield on debt**  
The `(1 - Tax)` term in WACC captures the interest tax deduction. Omitting it overstates WACC and understates value. Exception: companies with NOL carryforwards that don't actually benefit from the tax shield in the near term.

**Using total assets instead of V (total capital) for weights**  
Total assets include operating liabilities (accounts payable, accrued expenses) that are not financial capital. V = Interest-bearing debt + Equity only.

**Applying a single WACC to a multi-segment company**  
If the company has divisions with fundamentally different risk profiles (e.g., stable utility + high-growth SaaS), each segment should use a segment-specific WACC. Using one blended rate misprices both.

**Mis-specifying beta for unquoted companies**  
Re-levering beta with the wrong tax rate or using total liabilities instead of financial debt in the D/E ratio. Always use: `D = interest-bearing financial debt only`.

---

## Quick Reference: WACC Sensitivity

For a company with Re ≈ 9%, Rd ≈ 3%, tax 20%, and 80/20 equity/debt split:

```
Base WACC = (0.80 × 9.0%) + (0.20 × 3.0% × 0.80)
          = 7.20% + 0.48%
          = 7.68%
```

| Scenario | Change | WACC Impact |
|----------|--------|-------------|
| Beta +0.2 | Re +1.1% | WACC +0.88% |
| ERP +1% | Re +1.0% × β | WACC +0.80% |
| Leverage 20% → 40% D/V | Re↑ (re-lever β), Rd weight↑ | WACC ↓ slightly (tax shield) |
| Tax rate 20% → 30% | Rd after-tax drops | WACC ↓ ~0.06% |

The dominant sensitivity is **equity cost**, because equity is almost always the majority of V.
