# Modeling Best Practices

Structural and mechanical standards for three-statement models. These practices exist to prevent the most common failure modes: models that break when assumptions change, models where errors hide in formulas, and models that no one else can audit.

---

## Color Coding Convention

Every professional model uses a color system so anyone opening the file immediately knows what they can touch.

| Color | Meaning | Examples |
|-------|---------|---------|
| **Blue text** | Hard-coded input (changeable) | Growth rate, tax rate, initial revenue |
| **Black text** | Formula (never type a number here) | Revenue = Prior × (1 + Growth) |
| **Green text** | Link from another sheet | IS Net Income → BS Retained Earnings |
| **Red fill** | Error or balance check failure | BS doesn't balance |
| **Grey fill** | Structural / label cells | Row headers, section dividers |

**Rule**: If you ever type a number into a black-text cell, you've broken the model. The assumption belongs on the assumptions page, and the formula cell should reference it.

---

## Sheet Structure

Recommended tab order, left to right:

```
ASSUMPTIONS → IS → BS → CF → OUTPUTS → (CHECKS)
```

- **ASSUMPTIONS**: All blue-text inputs live here. Zero formulas that depend on IS/BS/CF.
- **IS / BS / CF**: Formula-only (black and green). No hard-coded numbers except possibly a base-period actuals column.
- **OUTPUTS**: DCF, returns summary, scenario comparison — all pull from the three statements.
- **CHECKS**: Optional dedicated tab for balance checks and sanity tests (some modelers embed checks directly in IS/BS/CF instead).

Never mix inputs with outputs on the same sheet. A common mistake is embedding a growth rate assumption directly in the revenue cell of the IS. Six months later, no one can find it.

---

## Assumption Page Layout

Each input row should have four columns:

```
| Assumption Label | Unit | Value(s) | Source / Rationale |
```

Example:

```
| Revenue Growth Rate (Y1-Y3) | % per year | 35% | Management guidance, comparable SaaS peers at Series B |
| Revenue Growth Rate (Y4-Y5) | % per year | 20% | Mean reversion toward industry average (18-22%) |
| Gross Margin               | %          | 68% | Current trailing 12M actual; held flat (SaaS benchmark: 65-75%) |
| DSO (Days Sales Outstanding)| days       | 45  | Current AR/Revenue×365; industry avg 30-60 |
| Effective Tax Rate          | %          | 21% | US federal statutory; no state taxes modeled |
```

**Decision rule for the Source column**: If you'd be embarrassed to explain the source to a skeptical CFO, the assumption needs more work. "Gut feeling" is not a source. "Management guidance, cross-checked against 3 publicly traded comps (VEEV, HUBS, ZI), median = 32%, management claims 35% due to TAM expansion" is a source.

---

## Formula Discipline

### One Formula, Copy Across

Build every row as a single formula in column Y1, then copy right through Y5. Never manually enter different values in different year columns. If you need a step-change in Year 3, express it as a conditional in the assumption, not by hard-coding Year 3's cell.

**Wrong**:
```
Y1: =ASSUMPTIONS!B5        ← 35%
Y2: =ASSUMPTIONS!B5        ← 35%
Y3: 0.20                   ← manually typed
Y4: 0.20
Y5: 0.20
```

**Right** (assumption page has both rates, and a step-down year):
```
Y1: =IF(ASSUMPTIONS!$B$2>=1, ASSUMPTIONS!$B$3, ASSUMPTIONS!$B$4)
```
Or more simply, two rows on assumptions ("Early growth rate" and "Mature growth rate") with a toggle year, and the IS formula picks the right one.

### Avoid Cross-Sheet Formulas Buried in Cells

A formula `='Income Statement'!B15` buried three sheets deep is invisible. Use named ranges or build an explicit "Bridge" section at the top of each sheet showing what's being pulled in.

### Absolute vs. Relative References

- Assumptions references: always absolute (`$B$5`) — they should not shift when copying across years
- Period references (prior year): mixed (`B$10`) — row locked, column shifts when copying right

---

## The Three Balance Checks

Embed these as visible cells, not hidden in a back corner.

### Check 1: Balance Sheet Identity

```
CHECK_BS = Total Assets - (Total Liabilities + Total Equity)
```

Target: **0.00** for every period column.

If non-zero, the error is almost always in one of:
1. Retained earnings not picking up net income correctly
2. A working capital item double-counted (e.g., accounts payable in both BS and CF)
3. A financing row (debt repayment) that updates the liability but not cash

### Check 2: Cash Bridge

```
CHECK_CF = CF_Ending_Cash - BS_Cash_Line
```

Target: **0.00** for every period column.

If non-zero, a cash flow item is missing or double-counted. The most common culprit: short-term debt classified as a current liability on the BS but not reflected in the financing section of the CF.

### Check 3: Retained Earnings Roll

```
RE_End = RE_Begin + Net_Income - Dividends
```

Verify that BS Retained Earnings (end) equals this formula. If not, equity doesn't foot and the BS check will also fail.

**Implementation**: Put all three checks in a bright red cell that displays "OK" or "ERROR":

```excel
=IF(ABS(CHECK_BS) < 0.01, "OK", "ERROR: " & TEXT(CHECK_BS, "#,##0"))
```

The `< 0.01` tolerance handles floating-point rounding in Excel.

---

## Working Capital Mechanics

Working capital is the most frequently botched section. These are the standard formulas:

| Item | Balance Sheet Formula | Cash Flow Impact |
|------|----------------------|-----------------|
| Accounts Receivable | `= Revenue × (DSO / 365)` | ΔAR = AR_end − AR_begin; **positive ΔAR = cash outflow** |
| Inventory | `= COGS × (DIO / 365)` | ΔInv = Inv_end − Inv_begin; **positive ΔInv = cash outflow** |
| Accounts Payable | `= COGS × (DPO / 365)` | ΔAP = AP_end − AP_begin; **positive ΔAP = cash inflow** |

The CF statement working capital section:

```
Change in AR:      − (AR_end − AR_begin)
Change in Inventory: − (Inv_end − Inv_begin)
Change in AP:      + (AP_end − AP_begin)
Net WC Change:     sum of above
```

**Worked Example**: Company with $10M Y1 revenue growing to $20M Y2, DSO = 45 days.

```
AR_Y1 = $10M × (45/365) = $1.23M
AR_Y2 = $20M × (45/365) = $2.47M
ΔAR   = $2.47M − $1.23M = $1.23M cash outflow

On the CF, this appears as: −$1.23M
```

A company doubling revenue with 45-day DSO will consume $1.23M in working capital just from receivables — before any inventory build or capex. This is why fast-growing, profitable companies run out of cash.

---

## Depreciation and Fixed Asset Roll

Fixed assets (PP&E) roll forward as:

```
PP&E_end = PP&E_begin + CapEx − Depreciation
```

Depreciation methods:

| Method | Formula | Use When |
|--------|---------|---------|
| Straight-line | `Asset_Cost / Useful_Life` | Default for most models |
| % of revenue | `Revenue × CapEx_pct` (then separate depr schedule) | Asset-light businesses |
| Declining balance | `PP&E_begin × Rate` | Tax modeling, not GAAP modeling |

For a simple model, use straight-line on an aggregated asset base:

```
Depreciation = PP&E_Average × (1 / Avg_Useful_Life)
PP&E_Average = (PP&E_begin + PP&E_end) / 2
```

Note: this creates a mild circularity (PP&E_end depends on depreciation, depreciation depends on PP&E_end). Resolve by using PP&E_begin only for depreciation in simple models, or accept one iteration.

---

## Handling Circular References

The interest expense circularity is the most common structural trap:

```
Interest Expense = Debt_Balance × Interest_Rate
Debt_Balance     = Prior_Debt + New_Borrowing − Repayment
Repayment        = f(Cash_Available)
Cash_Available   = f(Net_Income, which includes Interest_Expense)
```

**Three options**, in order of preference:

1. **Prior-period debt**: Calculate interest on beginning-of-period debt, not ending. Slightly less accurate but eliminates circularity. Acceptable for most models.

   ```
   Interest_Expense_Y2 = Debt_Balance_Y1_End × Interest_Rate
   ```

2. **Average debt**: Use `(Debt_begin + Debt_end) / 2`. Enables Excel's iterative calculation setting. Turn on: File → Options → Formulas → Enable iterative calculation (max iterations: 100, tolerance: 0.001).

3. **Revolver as the plug**: Model a revolving credit facility as the balancing item. If the model projects a cash shortfall, the revolver draws. If surplus, it repays. This is structurally correct and removes the circularity by making cash the residual.

---

## Scenario Architecture

Do not build separate tabs for each scenario. Use a single model with a scenario toggle on the assumptions page.

**Structure**:

```
ASSUMPTIONS page:
  Scenario selector: [Base / Bull / Bear]   ← single dropdown cell, e.g., $B$1

  Revenue Growth (Y1):
    Base:  35%   (in cell D5)
    Bull:  45%   (in cell E5)
    Bear:  20%   (in cell F5)
    Active: =CHOOSE(scenario_index, D5, E5, F5)   (in cell C5, blue)
```

Where `scenario_index` is `=MATCH($B$1, {"Base","Bull","Bear"}, 0)`.

Every assumption row has three scenario columns (D, E, F) and one active column (C). The IS/BS/CF formulas only ever reference column C. Switching the dropdown instantly re-runs the entire model.

**Avoid**: Hardcoding scenario outputs in a separate "Scenario Summary" tab that requires manual copy-paste. This is always stale within a week.

---

## Granularity by Time Horizon

| Period | Granularity | Rationale |
|--------|------------|-----------|
| Year 1 | Monthly | Budget-level precision; management can actually forecast this |
| Year 2 | Quarterly | Semi-forecast; useful for board reporting |
| Years 3–5 | Annual | Directional only; monthly precision is false |
| Years 6–10 (DCF terminal) | Single terminal year | Extrapolated; don't model 10 detailed years |

**Implementation**: Build a monthly IS, then use `SUMIF` or column grouping to roll up to quarterly and annual views. Do not build three separate models at different granularities — they will diverge.

---

## Common Errors and Diagnosis

| Symptom | Likely Cause | Diagnostic |
|---------|-------------|------------|
| BS doesn't balance by a fixed amount | Missing or double-counted item | Trace the amount — if it equals net income, check retained earnings roll |
| BS doesn't balance and the gap grows each year | Accumulating error in equity or debt schedule | Check the roll-forward for each item (RE, debt, PP&E) |
| CF ending cash ≠ BS cash | CF missing a BS item | Reconcile BS period changes against CF line items one by one |
| Model breaks when you change one assumption | Hard-coded number somewhere in formulas | Search for non-formula cells in IS/BS/CF using Excel's "Go To Special → Constants" |
| Negative retained earnings in early years | Expected if company is unprofitable; check that it's not a formula error | Confirm RE_begin + NI − Dividends = RE_end |
| CapEx not showing as cash outflow | CapEx row has wrong sign | CapEx should be negative in the investing section of CF |

---

## Naming Conventions for Cell References

If using named ranges (recommended for readability):

```
rev_growth_y1     Revenue growth rate, Year 1
gross_margin      Gross margin percentage
dso_days          Days sales outstanding
tax_rate_eff      Effective tax rate
capex_pct_rev     CapEx as % of revenue
```

Prefix conventions:
- `rev_` — revenue-related
- `cogs_` — cost of goods sold
- `opex_` — operating expense
- `wc_` — working capital
- `fa_` — fixed assets
- `debt_` — debt schedule
- `tax_` — tax items

Consistent naming means a formula like `=rev_growth_y1 * prior_revenue` is self-documenting.
