# Altman Z-Score Variants

Three calibrations of Altman's discriminant model exist. Using the wrong one for a
given firm type produces systematically misleading results — a non-manufacturing SaaS
firm scored with the original Z will look safer than it is, because the X₅ (sales /
assets) term rewards asset-light business models the original calibration never saw.

## Which variant to use

| Firm type | Variant | Why |
|-----------|---------|-----|
| Public, **manufacturing** | Original Z | Calibrated on 1946–1965 US public manufacturers |
| **Private** manufacturing (no market cap) | Z' | Replaces X₄ market cap with book equity |
| **Non-manufacturing** (SaaS, services, retail, tech, emerging markets) | Z'' | Drops X₅ to remove asset-turnover bias |

Rule of thumb: if the firm has no publicly traded equity, it's Z'. If its business model
is not making physical goods, it's Z''. If both — private non-manufacturing — Z'' still
wins because the asset-turnover distortion matters more than the equity valuation gap.

## Formulas

### Original Z (public manufacturing)

```
Z = 1.2·X₁ + 1.4·X₂ + 3.3·X₃ + 0.6·X₄ + 1.0·X₅

X₁ = Working Capital / Total Assets
X₂ = Retained Earnings / Total Assets
X₃ = EBIT / Total Assets
X₄ = Market Value of Equity / Total Liabilities
X₅ = Sales / Total Assets

Zones:  Z > 2.99  safe
        1.81–2.99  grey
        Z < 1.81  distress
```

### Z' (private manufacturing)

```
Z' = 0.717·X₁ + 0.847·X₂ + 3.107·X₃ + 0.420·X₄ + 0.998·X₅

X₁–X₃, X₅ same as original.
X₄ = BOOK value of equity / Total Liabilities   (not market cap)

Zones:  Z' > 2.9   safe
        1.23–2.9   grey
        Z' < 1.23  distress
```

### Z'' (non-manufacturing / emerging markets)

```
Z'' = 6.56·X₁ + 3.26·X₂ + 6.72·X₃ + 1.05·X₄

X₁ = Working Capital / Total Assets
X₂ = Retained Earnings / Total Assets
X₃ = EBIT / Total Assets
X₄ = Book Value of Equity / Total Liabilities

NOTE: X₅ (sales / assets) is DROPPED entirely, and the remaining
coefficients are re-estimated. Z'' is NOT "Z with X₅ = 0".

Zones:  Z'' > 2.6   safe
        1.1–2.6     grey
        Z'' < 1.1   distress
```

## Worked example — non-manufacturing tech firm

A publicly traded SaaS company: Working Capital $320M, Retained Earnings $950M,
EBIT $280M, Market Cap $4,500M, Total Liabilities $1,600M, Sales $3,800M,
Total Assets $4,200M.

If you apply **original Z** (wrong variant):

```
X₁ = 320/4200 = 0.0762
X₂ = 950/4200 = 0.2262
X₃ = 280/4200 = 0.0667
X₄ = 4500/1600 = 2.8125
X₅ = 3800/4200 = 0.9048
Z  = 1.2(0.0762) + 1.4(0.2262) + 3.3(0.0667) + 0.6(2.8125) + 1.0(0.9048)
   = 3.22 → "safe"
```

If you apply **Z''** (correct variant):

```
X₁ = 0.0762
X₂ = 0.2262
X₃ = 0.0667
X₄ = 4500/1600 = 2.8125    (or use book equity 2600/1600 = 1.625 if more conservative)
Z'' = 6.56(0.0762) + 3.26(0.2262) + 6.72(0.0667) + 1.05(2.8125)
    = 0.500 + 0.737 + 0.448 + 2.953
    = 4.64 → "safe" but for very different reasons
```

Both land in "safe" here, but the **component contributions are different**, and in
borderline cases the variant choice flips the zone. Do not short-circuit by reporting
original Z when the firm is clearly non-manufacturing.

## Script usage

The bundled calculator takes `--variant {original,private,non_manufacturing}`:

```bash
python algo-risk-altman-z/scripts/altman_z.py \
    --working-capital 320 --retained-earnings 950 --ebit 280 \
    --market-cap 4500 --total-liab 1600 --sales 3800 --total-assets 4200 \
    --variant non_manufacturing
```

When in doubt about which variant to use, run the script with each and compare — the
zone thresholds differ (2.99 vs 2.9 vs 2.6), so it is not enough to just compare raw
numbers.
