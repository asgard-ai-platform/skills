# Perceptual Mapping

Perceptual maps visualize how customers perceive brands relative to each other on attributes that matter for purchase decisions. The output is a 2D scatter plot; the strategic value is spotting gaps (underserved positions) and crowding (over-competitive zones).

---

## When a Perceptual Map Is Worth Building

Build one when:
- You have 3+ competitors in the target segment
- You are validating a positioning statement (Step 3 of STP)
- You suspect your brand's perceived position differs from your intended position

Skip it when:
- You have fewer than 3 brands to plot (the map carries no information)
- The segment is so new that no brand awareness exists yet

---

## Axis Selection: The Most Critical Decision

A map is only as useful as its axes. Bad axes produce a map that looks complete but tells you nothing actionable.

### Axis Selection Rules

| Rule | What it means |
|------|---------------|
| Axes must matter to the **target segment** | "Premium vs. Budget" matters to price-sensitive segments; irrelevant to luxury segments where price signals quality |
| Axes must **discriminate** among brands | If all brands score "High Quality", quality is not a useful axis — it cannot separate them |
| Axes should be **uncorrelated** | "Price" and "Luxury" are often nearly identical. Use PCA (see below) to detect redundancy |
| Axes must be **actionable** | If a brand cannot realistically shift on an axis, it has no strategic value |

### Common Axis Pairs by Category

| Category | Axis 1 | Axis 2 |
|----------|--------|--------|
| Food/Beverage | Indulgent ↔ Healthy | Convenient ↔ Premium Experience |
| Software/SaaS | Simple ↔ Feature-Rich | Affordable ↔ Enterprise-Grade |
| Fashion | Casual ↔ Formal | Mass Market ↔ Luxury |
| Financial Services | Safe/Conservative ↔ Aggressive/Growth | Accessible ↔ Exclusive |
| Consumer Packaged Goods | Functional ↔ Lifestyle | Local ↔ International |

These are starting points. Always validate with the target segment — ask customers to rate competitors on candidate attributes before committing to axes.

---

## Two Methods to Build the Map

### Method A: Direct Rating (Simple, Works for Most Cases)

**When to use:** You have customer survey data or can run one quickly. Good for 4-8 brands and 2 clear axes.

**Step-by-step:**

1. **Select 2 axes** (see rules above). Each axis is a bipolar scale (e.g., "Affordable" ↔ "Premium").

2. **Survey the target segment.** Ask customers to rate each brand on each attribute, 1-7 scale.
   - Axis 1: "Rate [Brand X] on: Affordable (1) to Premium (7)"
   - Axis 2: "Rate [Brand X] on: Basic/Functional (1) to Full-Featured (7)"

3. **Average the ratings** per brand per axis.

4. **Plot:** X-axis = Attribute 1 score, Y-axis = Attribute 2 score. Each brand is a point.

**Worked example — Plant-based protein bars in Taiwan:**

Survey of 120 Health-Conscious Office Workers (our target segment from SKILL.md), rating on:
- X-axis: Affordable (1) → Premium (7)
- Y-axis: Meal Replacement (1) → Snack (7)

| Brand | Premium Score (X) | Snack Score (Y) |
|-------|------------------|-----------------|
| 7-Eleven House Brand | 2.1 | 6.3 |
| CLIF Bar | 4.8 | 5.1 |
| Quest Bar | 5.4 | 4.2 |
| Garden of Life | 6.1 | 3.8 |
| **PlantBar (us)** | **3.5** | **2.4** |
| No brand occupies | ~3.5 | ~2.0–2.5 |

Reading the map:
- The bottom-left quadrant (Affordable + Meal Replacement) is **empty except PlantBar**
- This confirms the positioning: "busy professionals who skip meals" at an accessible price point is genuinely unoccupied
- The upper-right cluster (Premium + Snack) is crowded — entering there would require fighting Quest and Garden of Life head-on

### Method B: Principal Component Analysis (Advanced, for Multi-Attribute Data)

**When to use:** You have 8+ rated attributes and want the axes to emerge from the data rather than choosing them manually. Requires a spreadsheet or Python.

**Step-by-step:**

1. Survey customers on N attributes (N ≥ 6 to justify PCA), 1-7 scale per brand.

2. Build an **attribute × brand** matrix. Rows = brands, columns = attributes, cells = mean rating.

3. Run PCA. The first two principal components (PC1, PC2) become your axes.

4. Interpret the axes by looking at loadings — which attributes load heavily on PC1?

**Example loadings (hypothetical):**

| Attribute | PC1 Loading | PC2 Loading |
|-----------|-------------|-------------|
| Protein content | 0.82 | −0.12 |
| All-natural ingredients | 0.74 | 0.21 |
| Low sugar | 0.69 | 0.08 |
| Convenient packaging | −0.11 | 0.79 |
| Available at convenience stores | −0.23 | 0.71 |
| Taste enjoyment | 0.10 | 0.63 |

PC1 ≈ "Nutritional Integrity" (high = healthy, high-protein, clean label)
PC2 ≈ "Convenience & Enjoyment" (high = easy to get, tastes good)

These become your axes — they emerged from what customers actually use to differentiate brands.

**Minimal Python implementation (pure stdlib + numpy):**

```python
import numpy as np

# brands × attributes matrix (rows=brands, cols=attributes)
data = np.array([
    [6.1, 5.8, 5.5, 3.2, 2.1, 4.0],  # Garden of Life
    [5.4, 4.2, 4.8, 4.5, 3.8, 5.1],  # Quest Bar
    [4.8, 3.9, 4.1, 5.1, 5.8, 5.4],  # CLIF Bar
    [2.1, 3.0, 3.5, 6.2, 6.8, 5.9],  # 7-Eleven House Brand
    [5.8, 5.9, 5.7, 4.8, 4.9, 4.2],  # PlantBar (target position)
])

# Standardize (zero mean, unit variance per attribute)
mean = data.mean(axis=0)
std = data.std(axis=0)
data_std = (data - mean) / std

# PCA via SVD
U, S, Vt = np.linalg.svd(data_std, full_matrices=False)
scores = data_std @ Vt.T  # brand scores on each PC

print("PC1 scores (X-axis):", scores[:, 0].round(2))
print("PC2 scores (Y-axis):", scores[:, 1].round(2))
print("Explained variance ratio:", (S**2 / (S**2).sum()).round(3))
```

---

## Reading the Map: Positioning Implications

Once plotted, ask three questions:

### 1. Where is the gap?

A gap is a map region with no brand. Before celebrating, verify:
- Is there a brand there that your survey missed?
- Is the gap empty because customers do not want that combination?

**Gap test:** If you plot a hypothetical brand in the gap and ask survey respondents "Would you buy a brand like this?", a valid gap should generate meaningful purchase intent (>20% "definitely/probably yes" from target segment).

### 2. Where is the cluster?

Clustering means several brands occupy the same perceptual space. Entering a cluster requires either:
- A clear capability advantage on the cluster's dominant axis (to pull customers from incumbents), or
- A repositioning away from the cluster

### 3. Where are YOU vs. where do you WANT to be?

If your brand is already in the market, plot where customers currently perceive you — not where you intend to be. A common error in STP is positioning to where you want to move without acknowledging the repositioning cost.

| Distance from intended position | Strategic implication |
|--------------------------------|----------------------|
| Small gap (< 1 unit on 1-7 scale) | Messaging refinement sufficient |
| Medium gap (1-2 units) | Product or service changes + sustained messaging campaign needed |
| Large gap (> 2 units) | Repositioning is a multi-year effort; consider whether a new brand/sub-brand is faster |

---

## Validation: Is Your Map Trustworthy?

A perceptual map is only as good as the data behind it. Before using it for strategic decisions:

| Check | How to verify |
|-------|---------------|
| **Sample is from the target segment** | Filter survey respondents to the segment defined in the Targeting step — do not use general population data |
| **N ≥ 30 per segment** | Below 30, position estimates are too noisy to act on |
| **Brands are known to respondents** | Ask familiarity screening question; exclude ratings from respondents who don't know the brand |
| **Axes explain adequate variance** | For PCA: PC1 + PC2 should explain ≥ 50% of total variance. Below 50%, a 2D map misrepresents the real competitive space |
| **Positions are stable across subgroups** | If heavy users and light users place brands in completely different positions, segment-specific maps are needed |

---

## Common Mistakes

**Plotting attributes, not perceptions.** A map of "actual protein content" vs. "actual price" is a product comparison chart, not a perceptual map. Perceptual maps reflect how customers *believe* brands differ — which may not match reality.

**Choosing axes that confirm your existing hypothesis.** If you pick "the axes that make our brand look good", the map is useless. Axes must be chosen before you plot your brand's position.

**Treating a 2D map as complete.** Customers use more than two attributes. A 2D map always omits dimensions. It is a simplification for communication and decision-making, not a complete representation of competitive dynamics.

**Using the map without the positioning validation test.** Identifying a gap on the map does not mean you can claim it. A gap position must still pass the three-part positioning test from SKILL.md: Relevance, Differentiation, Credibility.
