# Seasonal Demand Forecasting for Inventory Health

Seasonal products break two assumptions baked into the base formulas: constant average demand and stable variance. This document shows how to detect seasonality, compute seasonal indices, adjust safety stock seasonally, and avoid liquidating product that is merely "off-season".

---

## 1. Detecting Seasonality Before Acting

Before applying any seasonal model, confirm the pattern is real and recurring.

**Minimum data requirement**: at least 2 full years of weekly or monthly sales. One year is not enough — you cannot separate seasonality from a one-time spike.

**Quick visual check**: plot monthly sales for each SKU as a line chart. If peaks and troughs fall in roughly the same calendar months across both years, seasonality is present.

**Quantitative screen — Coefficient of Variation (CV) and Peak-to-Trough Ratio**:

```
CV = σ_monthly / μ_monthly

Peak-to-Trough Ratio = max(monthly sales) / min(monthly sales)
```

| CV | Peak-to-Trough | Verdict |
|----|---------------|---------|
| < 0.3 | < 2× | Stable demand — no seasonal model needed |
| 0.3–0.6 | 2–4× | Moderate seasonality — apply indices |
| > 0.6 | > 4× | Strong seasonality — must model; standard safety stock will be wrong by 2–5× |

**Important**: high CV alone could mean demand is erratic (random noise), not seasonal. The pattern must *repeat* across years. If peaks shift month-to-month each year, use a different forecasting approach (e.g., event-driven).

---

## 2. Seasonal Index Method (Ratio-to-Moving-Average)

This is the standard decomposition method. It separates demand into:

```
Demand = Trend × Seasonal Index × Irregular
```

For inventory purposes you need the **Seasonal Index (SI)** per period.

### Step-by-step procedure

**Input**: Monthly sales data, ≥ 2 years, one SKU at a time.

#### Step 1 — Compute 12-month centered moving average (CMA)

For each month *t*:

```
CMA(t) = [ 0.5×S(t-6) + S(t-5) + ... + S(t) + ... + S(t+5) + 0.5×S(t+6) ] / 12
```

The 0.5 weighting on the endpoints centers the average exactly on month *t*.

This removes seasonality and leaves Trend × Irregular.

#### Step 2 — Compute raw seasonal ratios

```
Raw Ratio(t) = S(t) / CMA(t)
```

#### Step 3 — Average ratios by calendar month

Collect all Raw Ratio(t) values for January across all years, take the median (more robust than mean):

```
SI(Jan) = median( Raw Ratio for all Januaries )
SI(Feb) = median( Raw Ratio for all Februaries )
... (12 values total)
```

#### Step 4 — Normalize so indices sum to 12.00

```
Adjustment = 12.0 / sum(all 12 SI values)
SI_normalized(m) = SI(m) × Adjustment
```

After normalization: `sum(SI_normalized) = 12.0`, and the annual average SI = 1.0.

---

### Worked Example: Outdoor Sunscreen SKU

Monthly sales (units), 2 years:

| Month | Year 1 | Year 2 |
|-------|--------|--------|
| Jan | 120 | 135 |
| Feb | 140 | 150 |
| Mar | 260 | 280 |
| Apr | 480 | 510 |
| May | 820 | 870 |
| Jun | 1,100 | 1,050 |
| Jul | 1,200 | 1,180 |
| Aug | 1,050 | 1,100 |
| Sep | 600 | 580 |
| Oct | 350 | 370 |
| Nov | 200 | 210 |
| Dec | 150 | 160 |
| **Total** | **6,470** | **6,595** |

**Annual average monthly demand** (use for comparison):
```
μ = (6,470 + 6,595) / 2 / 12 = 546 units/month
```

After computing CMA and ratios (abbreviated for brevity), normalized seasonal indices:

| Month | SI | Interpretation |
|-------|----|----------------|
| Jan | 0.23 | 23% of average month |
| Feb | 0.26 | |
| Mar | 0.49 | |
| Apr | 0.91 | |
| May | 1.56 | |
| Jun | 1.98 | |
| Jul | 2.18 | Peak month |
| Aug | 1.97 | |
| Sep | 1.08 | |
| Oct | 0.65 | |
| Nov | 0.37 | |
| Dec | 0.28 | |
| **Sum** | **12.00** | ✓ |

**Seasonal forecast for next July** (assuming flat trend, average monthly base = 550):
```
Forecast(Jul) = Base × SI(Jul) = 550 × 2.18 = 1,199 units
```

---

## 3. Seasonal Safety Stock

The base formula from SKILL.md:

```
Safety Stock = Z × σ_d × √(Lead Time)
```

This uses a *single* σ_d (standard deviation of daily demand). For seasonal products, σ_d varies month-to-month. Using the annual average σ_d causes:

- **Overstock in off-peak months** (safety stock set too high)
- **Stockouts in peak months** (safety stock set too low)

### Seasonal safety stock formula

Compute σ_d separately for each month (or season), then apply:

```
Safety Stock(m) = Z × σ_d(m) × √(Lead Time)
```

Where `σ_d(m)` is the standard deviation of daily demand during month *m*, estimated from historical data for that calendar month.

### Practical shortcut using seasonal indices

If you have limited history, estimate monthly σ_d from annual σ_d:

```
σ_d(m) ≈ σ_d_annual × SI(m)
```

This assumes the coefficient of variation is roughly constant across seasons — a reasonable approximation when you lack month-level data.

**Continued worked example** — sunscreen, 95% service level (Z = 1.65), Lead Time = 14 days:

Suppose annual σ_d = 18 units/day.

| Month | SI | σ_d(m) = 18 × SI | Safety Stock = 1.65 × σ_d(m) × √14 |
|-------|----|------------------|--------------------------------------|
| Jan | 0.23 | 4.1 | **25 units** |
| Jul | 2.18 | 39.2 | **242 units** |
| Annual avg | 1.00 | 18.0 | 111 units |

Using the annual average safety stock of 111 units in July means you are running at effectively only 66% service level during peak. Using 242 units in January means ~$200–300 of unnecessary carrying cost per SKU.

---

## 4. Seasonal Reorder Point

From SKILL.md:

```
Reorder Point = (Average Daily Demand × Lead Time) + Safety Stock
```

For seasonal products, both terms must use the *current-month* values:

```
ROP(m) = [ μ_d × SI(m) × Lead Time ] + Safety Stock(m)
```

Where `μ_d` is the annual average daily demand and `SI(m)` is the month-specific index.

**Sunscreen example**, July, μ_d = 546/30 = 18.2 units/day:
```
ROP(Jul) = (18.2 × 2.18 × 14) + 242
         = 555 + 242
         = 797 units
```

In January:
```
ROP(Jan) = (18.2 × 0.23 × 14) + 25
         = 59 + 25
         = 84 units
```

Set your replenishment triggers accordingly — they should be updated at the start of each month (or each quarter for slower-moving products).

---

## 5. ABC Classification for Seasonal Products

The SKILL.md Iron Law — 20% of SKUs drive 80% of revenue — still holds, but **seasonal products must be reclassified by season, not by annual total alone**.

### Problem with annual-only ABC

A swimsuit SKU may generate $0 revenue in Nov–Mar and $150,000 in Apr–Sep. Classified on annual revenue, it ranks as A. But in January, treating it as an A-item (tight control, high safety stock) wastes capital.

### Seasonal ABC approach

Run ABC classification on a **rolling 13-week revenue window** updated monthly:

```
Revenue_rolling(SKU, month m) = Σ sales revenue for weeks (m-12) to m
```

Classify each month independently. A swimsuit becomes:
- **A-class**: Apr–Sep (peak season)
- **C-class**: Oct–Mar (off-season, hold minimal or zero stock)

**Implementation shortcut** — use seasonal index thresholds:

| SI(m) | Action |
|--------|--------|
| SI ≥ 1.5 | Use peak-season ABC classification |
| 0.7 ≤ SI < 1.5 | Use standard annual ABC classification |
| SI < 0.7 | Reduce safety stock by (1 − SI); freeze reorders if SI < 0.4 |

---

## 6. Pre-Season Inventory Build Plan

For highly seasonal SKUs (Peak-to-Trough > 4×), you cannot rely on in-season replenishment if lead time is long. You must build inventory before peak.

### Build quantity formula

```
Build Target = Σ Forecast(m) for all peak months + Peak Safety Stock − Current Stock

Peak months = months where SI(m) ≥ 1.0
```

**Decision rule for build timing**: place the buy `Lead Time` days before the first peak month (SI ≥ 1.0).

**Sunscreen example** — planning for May–Aug peak, current stock = 400 units, lead time = 45 days:

```
Forecast peak demand = (550×1.56) + (550×1.98) + (550×2.18) + (550×1.97)
                     = 858 + 1,089 + 1,199 + 1,084
                     = 4,230 units

Peak Safety Stock    = 242 units (July value, the highest)

Build Target         = 4,230 + 242 − 400 = 4,072 units

Order placement      = April 1 (first peak month May 1, minus 45-day lead time → March 17; round up to April 1 for supplier cut-off)
```

---

## 7. End-of-Season Liquidation Trigger

Seasonal products that are **not** sold by end of peak season become carry-over inventory — a major source of dead stock and write-downs.

### Liquidation decision rule

At the start of the final month of peak season (SI drops below 1.0 next month):

```
Expected Remaining Demand = Σ Forecast(m) for remaining off-peak months
Expected Remaining Demand = Base × Σ SI(m) for off-peak months
```

If `Current Stock > 2 × Expected Remaining Demand`, begin liquidation (discount, bundle, channel clearance).

**Sunscreen example** — entering October, current stock = 620 units:

```
Off-peak forecast (Oct–Mar):
= 550 × (0.65 + 0.37 + 0.28 + 0.23 + 0.26 + 0.49)
= 550 × 2.28
= 1,254 units  ← still meaningful demand off-season

Threshold = 2 × 1,254 = 2,508 units
620 < 2,508 → no liquidation needed; carry over normally
```

If stock were 3,000 units: `3,000 > 2,508` → liquidate the excess 746 units before April to avoid a second year of carry costs.

---

## 8. Pitfalls Specific to Seasonal Forecasting

**Index calculation requires ≥ 2 years**: with one year you cannot separate trend from seasonality. If you only have one year, use industry seasonal indices as a prior and adjust as data accumulates.

**Promotional spikes inflate indices**: a flash sale in July inflates SI(Jul) permanently. Scrub known promotional periods before computing indices, or they will inflate next year's July safety stock unnecessarily.

**Lead time length relative to seasonal swing**: if lead time (14 days) is short relative to the seasonal cycle (monthly), seasonal safety stock is the right tool. If lead time is 6 months (e.g., ocean freight from Asia for fashion), you are forecasting the *entire season* at order time — use a pre-season buy model with a single probability distribution over total season demand, not monthly rolling reorders.

**Newly launched SKUs have no history**: use category-level seasonal indices from similar established SKUs as a proxy. Do not use flat indices (SI = 1.0) for a known seasonal category — this guarantees stockouts at peak.

**Seasonal index drift**: fashion and lifestyle categories shift their peak month over time (e.g., "back to school" moving earlier). Recompute indices annually; do not reuse indices older than 2 years.
