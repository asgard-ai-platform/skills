# Cross-Price Elasticity

Cross-price elasticity of demand measures how the quantity demanded of product A responds to a price change in product B.

```
E_AB = %ΔQ_A / %ΔP_B = (dQ_A/dP_B) × (P_B/Q_A)
```

**Sign interpretation:**
- **E_AB > 0** → substitutes (B more expensive → more demand for A)
- **E_AB < 0** → complements (B more expensive → less demand for A)
- **E_AB ≈ 0** → unrelated goods

This matters for portfolio pricing: changing price on product B affects revenue on product A even when A's price stays fixed.

---

## Arc Formula (No Regression Data)

When you only have two observed price-quantity pairs:

```
E_AB = [(Q_A2 − Q_A1) / ((Q_A2 + Q_A1) / 2)]
       ÷
       [(P_B2 − P_B1) / ((P_B2 + P_B1) / 2)]
```

**Worked example — substitute pair (coffee vs tea):**

| Period | Price of Tea (P_B) | Units of Coffee Sold (Q_A) |
|--------|-------------------|---------------------------|
| Before | $3.00 | 1,200 |
| After  | $4.50 | 1,560 |

```
ΔQ_A = 1560 − 1200 = 360
avg Q_A = (1560 + 1200) / 2 = 1380
%ΔQ_A = 360 / 1380 = 0.2609

ΔP_B = 4.50 − 3.00 = 1.50
avg P_B = (4.50 + 3.00) / 2 = 3.75
%ΔP_B = 1.50 / 3.75 = 0.4000

E_AB = 0.2609 / 0.4000 = +0.65
```

**Interpretation:** A 1% increase in tea price raises coffee demand by 0.65%. Moderate substitutes.

**Worked example — complement pair (printer vs ink cartridge):**

| Period | Price of Printer (P_B) | Ink Cartridge Sales (Q_A) |
|--------|----------------------|--------------------------|
| Before | $120 | 8,400 |
| After  | $180 | 6,300 |

```
%ΔQ_A = (6300 − 8400) / ((6300 + 8400) / 2) = −2100 / 7350 = −0.2857
%ΔP_B = (180 − 120) / ((180 + 120) / 2) = 60 / 150 = 0.4000

E_AB = −0.2857 / 0.4000 = −0.71
```

**Interpretation:** Complements confirmed. A 10% printer price increase cuts cartridge demand by ~7%.

---

## Regression Method (Multiple Products)

When you have panel or time-series data, estimate a log-log system:

```
log(Q_A) = α + β_AA × log(P_A) + β_AB × log(P_B) + β_AC × log(P_C) + controls + ε
```

- `β_AA` = own-price elasticity of A
- `β_AB` = cross-price elasticity of A with respect to B
- `β_AC` = cross-price elasticity of A with respect to C

Coefficients are directly interpretable as elasticities (constant elasticity model — same assumption as in the parent SKILL.md).

**Minimum data requirements:**
- At least 20 observations per product in the system
- Sufficient price variation in P_B (ideally >5% range)
- Include own-price, all cross-prices, and at least one control (time trend or seasonality dummy)

**Python skeleton:**

```python
import numpy as np

def estimate_cross_price_elasticity(log_qa, log_pa, log_pb):
    """
    OLS log-log regression for cross-price elasticity.
    
    Parameters
    ----------
    log_qa : array-like, shape (n,)  — log quantity of product A
    log_pa : array-like, shape (n,)  — log price of product A
    log_pb : array-like, shape (n,)  — log price of product B
    
    Returns
    -------
    dict with beta_aa (own), beta_ab (cross), r_squared
    """
    n = len(log_qa)
    # Design matrix: [intercept, log_pa, log_pb]
    X = np.column_stack([np.ones(n), log_pa, log_pb])
    y = np.array(log_qa)
    
    # OLS: (X'X)^-1 X'y
    coeffs = np.linalg.lstsq(X, y, rcond=None)[0]
    alpha, beta_aa, beta_ab = coeffs
    
    y_hat = X @ coeffs
    ss_res = np.sum((y - y_hat) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - ss_res / ss_tot
    
    return {
        "beta_aa": round(beta_aa, 4),   # own-price elasticity
        "beta_ab": round(beta_ab, 4),   # cross-price elasticity A w.r.t. B
        "r_squared": round(r_squared, 4)
    }
```

---

## Revenue Impact Across a Two-Product Portfolio

When products are substitutes or complements, a price change on B creates a **spillover revenue effect** on A.

**Notation:**
- `R_A = P_A × Q_A`, `R_B = P_B × Q_B`
- `E_AA` = own-price elasticity of A
- `E_BB` = own-price elasticity of B
- `E_AB` = cross-price elasticity of A w.r.t. B
- `E_BA` = cross-price elasticity of B w.r.t. A

**Revenue change when P_B increases by δ% (P_A held fixed):**

```
ΔR_A ≈ R_A × E_AB × δ          ← spillover on A's revenue
ΔR_B ≈ R_B × (1 + E_BB) × δ    ← direct effect on B's revenue
ΔR_total = ΔR_A + ΔR_B
```

**Worked numbers — substitute case:**

Assume:
- Product A (coffee): R_A = $120,000/month, E_AB = +0.65
- Product B (tea): R_B = $60,000/month, E_BB = −1.2
- Proposed P_B increase: δ = +10%

```
ΔR_A = 120,000 × 0.65 × 0.10 = +$7,800
ΔR_B = 60,000 × (1 + (−1.2)) × 0.10 = 60,000 × (−0.2) × 0.10 = −$1,200
ΔR_total = +$7,800 − $1,200 = +$6,600
```

Raising tea's price *increases* total portfolio revenue even though tea revenue itself drops, because coffee absorbs the displaced demand. This decision is invisible if you optimize each product independently.

**Complement case warning:** The same formula applies, but E_AB < 0, so raising P_B *reduces* R_A. Discounting an anchor product (printer) should show positive cross-elasticity lift on cartridges.

---

## Symmetry vs. Asymmetry

Theoretical demand systems (e.g., AIDS model) impose the Slutsky symmetry condition:

```
P_A × E_AB = P_B × E_BA   (in expenditure share terms)
```

In practice, estimated E_AB ≠ E_BA due to:
1. Different market positions (A is niche, B is mass-market)
2. Asymmetric awareness or switching costs
3. Sampling noise in short panels

**Do not assume E_BA = E_AB.** Always estimate both directions separately when the decision requires knowing the reverse spillover.

---

## Classifying Product Relationships

| E_AB Range | Label | Pricing implication |
|------------|-------|---------------------|
| > 2.0 | Strong substitutes | Price coordination critical; undercutting B cannibalizes A |
| 0.5 – 2.0 | Moderate substitutes | Portfolio bundles can capture switching demand |
| −0.1 – 0.5 | Weak / unrelated | Price independently |
| −2.0 – −0.1 | Moderate complements | Bundle discount increases joint demand |
| < −2.0 | Strong complements | Price anchor low to drive high-margin accessory |

These thresholds are rules of thumb, not statistical boundaries. Always report confidence intervals.

---

## Common Failure Modes

**1. Omitted own-price in cross-price regression**
If you regress Q_A on P_B without including P_A, and P_A is correlated with P_B (common in promotional calendars), E_AB absorbs own-price effects and is biased. Always include P_A.

**2. Confusing category-level with SKU-level cross-elasticity**
Cross-price elasticity between SKU variants of the same product (e.g., 250ml vs 500ml of the same drink) behaves differently from cross-elasticity between genuinely different products. SKU-level switching is faster and more extreme.

**3. Using cross-price elasticity across non-overlapping customer segments**
E_AB = 0 does not mean products are unrelated — it may mean they serve different segments that never compete. Segment-level analysis is necessary before concluding independence.

**4. Ignoring inventory constraints**
If product A is supply-constrained, observed Q_A cannot rise even when P_B increases. Estimate elasticity only on periods with unconstrained availability.

**5. Multicollinearity in promotional data**
P_A and P_B often move together during coordinated promotions (e.g., Black Friday). High multicollinearity inflates standard errors; estimates become unreliable. Use variance inflation factor (VIF > 10 = problem). Consider ridge regression or staggered natural experiments instead.

---

## Decision Checklist Before Using Cross-Price Estimates

```
[ ] Own-price elasticity of each product estimated and validated separately
[ ] Cross-price regression includes own-price as a control
[ ] Price variation in P_B is sufficient (>5% range across observations)
[ ] Promotional periods flagged and handled (dummy variable or exclusion)
[ ] VIF checked — no severe multicollinearity
[ ] Confidence interval on E_AB reported, not just point estimate
[ ] Both directions (E_AB and E_BA) estimated if decision involves pricing both products
[ ] Revenue impact calculation uses portfolio-level ΔR, not product-in-isolation ΔR
```
