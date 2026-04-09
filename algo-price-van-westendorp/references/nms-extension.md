# Newton-Miller-Smith Purchase Intent Extension

Van Westendorp alone tells you *where* prices are perceived as acceptable — it says nothing about what fraction of respondents would actually buy. The Newton-Miller-Smith (NMS) extension adds two purchase-intent questions that convert the PSM range into revenue-comparable estimates at OPP and IPP.

## What NMS Adds

Standard Van Westendorp produces PMC, OPP, IPP, PME. None of these come with a demand estimate. NMS patches this by asking respondents two additional questions — one at OPP, one at IPP — using a 5-point intent scale:

| Scale point | Label |
|-------------|-------|
| 5 | Definitely would buy |
| 4 | Probably would buy |
| 3 | Might or might not buy |
| 2 | Probably would not buy |
| 1 | Definitely would not buy |

The questions are asked **after** the four VW questions, at price points you compute from the VW intersections:

> *"If [product] were priced at \$OPP, how likely would you be to purchase it?"*
> *"If [product] were priced at \$IPP, how likely would you be to purchase it?"*

## Hypothetical Bias Correction

Raw purchase intent overstates actual buying. NMS uses Juster-style deflation coefficients:

| Scale point | Raw intent | Deflated probability |
|-------------|------------|----------------------|
| 5 — Definitely would buy | 1.00 | 0.80 |
| 4 — Probably would buy | 0.75 | 0.30 |
| 3 — Might or might not | 0.50 | 0.05 |
| 2 — Probably would not | 0.25 | 0.01 |
| 1 — Definitely would not | 0.00 | 0.00 |

These coefficients (0.80, 0.30, 0.05, 0.01, 0.00) are the empirically calibrated defaults from the original Newton-Miller-Smith methodology. Some practitioners use slightly different values (0.75 / 0.25 / 0.10 / 0.02 / 0.00); the exact coefficients matter less than applying them consistently and sourcing them explicitly in your report.

### Adjusted Purchase Intent Formula

For each price point (OPP or IPP), let n₁ through n₅ be the number of respondents choosing each scale level, and N be total respondents:

```
API = (n₅ × 0.80 + n₄ × 0.30 + n₃ × 0.05 + n₂ × 0.01 + n₁ × 0.00) / N
```

API = Adjusted Purchase Intent, expressed as a proportion (0–1).

## Worked Example

**Setup:** 200 respondents for a SaaS product. VW analysis returned:

```
PMC = $12 / OPP = $18 / IPP = $22 / PME = $35
```

**Purchase intent responses at OPP ($18):**

| Scale | n | Coefficient | Contribution |
|-------|---|-------------|--------------|
| 5 — Definitely | 52 | 0.80 | 41.6 |
| 4 — Probably | 68 | 0.30 | 20.4 |
| 3 — Might | 44 | 0.05 | 2.2 |
| 2 — Probably not | 24 | 0.01 | 0.24 |
| 1 — Definitely not | 12 | 0.00 | 0.0 |
| **Total** | 200 | | **64.44** |

```
API_OPP = 64.44 / 200 = 0.3222  →  32.2% adjusted purchase intent
```

**Purchase intent responses at IPP ($22):**

| Scale | n | Coefficient | Contribution |
|-------|---|-------------|--------------|
| 5 — Definitely | 38 | 0.80 | 30.4 |
| 4 — Probably | 55 | 0.30 | 16.5 |
| 3 — Might | 52 | 0.05 | 2.6 |
| 2 — Probably not | 38 | 0.01 | 0.38 |
| 1 — Definitely not | 17 | 0.00 | 0.0 |
| **Total** | 200 | | **49.88** |

```
API_IPP = 49.88 / 200 = 0.2494  →  24.9% adjusted purchase intent
```

## Revenue Index Comparison

With API values you can compute a **Revenue Index (RI)** — a relative comparison across price points that helps decide between OPP and IPP:

```
RI(price) = price × API(price)
```

Using the worked example:

```
RI_OPP = $18 × 0.322 = $5.80 per potential respondent
RI_IPP = $22 × 0.249 = $5.48 per potential respondent
```

OPP yields higher revenue index in this case, which suggests pricing closer to $18 captures more revenue than the psychologically "safe" $22. This is not always the result — IPP sometimes wins when the intent drop-off between OPP and IPP is small.

### Decision Table

| RI_OPP vs RI_IPP | Interpretation | Recommended anchor |
|------------------|----------------|--------------------|
| RI_OPP > RI_IPP by >10% | Strong case for aggressive pricing | OPP |
| Within 10% | Toss-up; let cost structure and brand decide | Either |
| RI_IPP > RI_OPP | Demand is more price-tolerant than VW implies | IPP or above |

## Output Format Extension

Add an `nms` block to the standard VW JSON output:

```json
{
  "price_points": {"opp": 18, "ipp": 22, "pmc": 12, "pme": 35},
  "acceptable_range": {"min": 12, "max": 35},
  "nms": {
    "api_opp": 0.322,
    "api_ipp": 0.249,
    "revenue_index_opp": 5.80,
    "revenue_index_ipp": 5.48,
    "recommended_anchor": "opp",
    "deflation_coefficients": [0.80, 0.30, 0.05, 0.01, 0.00]
  },
  "metadata": {"respondents": 200, "currency": "USD", "product": "SaaS subscription"}
}
```

Always report the deflation coefficients used. If a client has proprietary calibration data, replace the defaults.

## Survey Design Constraints

**Question placement matters.** Ask the four VW questions first — in random order — then reveal the OPP and IPP values you computed (rounded to psychologically clean numbers, e.g., $18 not $17.83) and ask purchase intent for each. Revealing the computed prices before the VW questions anchors respondents and invalidates both datasets.

**Rounding OPP and IPP.** VW intersections rarely fall on round numbers. Round to the nearest $1 for low-price products, nearest $5 or $10 for higher-priced items. State the rounded values in the survey and in the output; note the raw computed values in metadata.

**Minimum sample for stable NMS.** The intent distribution at each price point needs enough respondents in each scale bucket to be stable. With N < 100, the API estimate has wide confidence intervals. At N = 200 the 95% CI on API is roughly ±7 percentage points; at N = 400 it narrows to ±5pp.

## Limitations

**Two-point demand curve is thin.** NMS gives you intent at exactly two prices — OPP and IPP. You cannot fit a full demand curve from two points. If you need elasticity estimates across a range, use a conjoint study or Gabor-Granger instead.

**Deflation coefficients are context-dependent.** The 0.80/0.30/0.05/0.01 defaults were calibrated on consumer packaged goods. B2B software, luxury goods, and regulated products may require different factors. If your organization has past launch data, calibrate your own coefficients by regressing actual purchase rates against pre-launch intent scores.

**No competitive framing.** Like standard Van Westendorp, NMS asks about your product in isolation. The API at OPP may overstate real-world penetration if a strong competitor is priced nearby.

**IPP < OPP edge case.** When the VW data produces IPP < OPP (see SKILL.md edge cases), asking purchase intent at both becomes ambiguous — the "cheaper" price (IPP) is the reference point for "average quality," not a discount. In this case, discard the NMS extension and note the data quality issue.
