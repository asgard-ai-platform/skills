# Perceptual Mapping — Method Reference

Perceptual mapping translates qualitative brand perception into a 2D visual space. This reference covers axis selection, data collection methods, plotting, and interpretation — specifically for use in the `biz-brand-positioning` skill.

---

## The Core Problem: Axes Determine Everything

A perceptual map is only as useful as its axes. Wrong axes produce a map that is visually neat but strategically useless. The axes must reflect the dimensions customers *actually use* to compare brands — not dimensions that are easy to measure or that make your brand look good.

**Common mistake:** Choosing axes that your brand wins on. If you define the axes, you control where everyone lands. This is a positioning exercise for internal morale, not strategy.

**Correct approach:** Derive axes from customer language.

---

## Step 1: Identify Candidate Dimensions

### Method A — Direct Elicitation (interviews / surveys)

Ask customers: *"When choosing between [Brand X] and [Brand Y], what factors matter most to you?"*

Collect raw language. Do not pre-define categories. Common outputs:

- "feels like a real Taiwanese brand"
- "too expensive for what it is"
- "I trust their quality"
- "it's what my parents drink"
- "for young people"

Group responses into themes. The themes with the highest frequency and the highest stated importance become axis candidates.

### Method B — Repertory Grid Technique

Present customers with three brands at a time (a "triad"). Ask: *"Two of these brands are similar; one is different. In what way are the two similar to each other, but different from the third?"*

Repeat with different triads. The constructs customers generate (e.g., "traditional vs modern", "mass vs craft") are the perceptual dimensions. This method surfaces dimensions customers use implicitly — dimensions they might not name if asked directly.

### Method C — Multidimensional Scaling (MDS)

Collect pairwise similarity ratings for all brands in the competitive set (1–9 scale). Run MDS to produce a low-dimensional map where distance = perceived dissimilarity. The axes in an MDS map are unlabeled — you interpret them post-hoc by examining which attributes correlate with position.

MDS is the most rigorous method but requires statistical software (R: `cmdscale()`, Python: `sklearn.manifold.MDS`) and a large enough sample. Use Method A or B when budget or timeline is limited.

---

## Step 2: Select the Final Two Axes

From your candidate dimensions, select two that meet all three criteria:

| Criterion | Test |
|---|---|
| **Customer-relevant** | Customers mention this dimension unprompted when comparing brands |
| **Discriminating** | Brands in your competitive set actually differ on this dimension |
| **Independent** | The two axes are not highly correlated (e.g., "expensive" and "luxurious" would collapse into one axis) |

If your two best dimensions are correlated (r > 0.7), pick the one that is more actionable or replace one with a different dimension that is uncorrelated.

**Typical axis pairs by category:**

| Category | Axis 1 | Axis 2 |
|---|---|---|
| Consumer packaged goods | Price (low→high) | Naturalness (processed→artisan) |
| F&B / beverage | Brand heritage (new→established) | Target age (young→mature) |
| SaaS / tech | Ease of use (complex→simple) | Feature depth (basic→advanced) |
| Retail | Convenience (inconvenient→convenient) | Exclusivity (mass→premium) |
| Education | Formality (informal→institutional) | Outcome focus (process→results) |

These are starting points only. Derive axes from customer data, not from this table.

---

## Step 3: Score Each Brand

For each brand in the competitive set (including your own), assign a score on each axis.

### Scoring methods (choose one):

**Option A — Perception survey**
Ask a representative sample of your target segment to rate each brand on each axis using a 1–7 Likert scale. Average scores across respondents. This is the most defensible method.

Example survey item:
> "On a scale of 1–7, where 1 = 'Very affordable' and 7 = 'Very premium', how would you rate [Brand]?"

**Option B — Expert judgment panel**
Assemble 3–5 people with deep market knowledge. Each independently rates every brand. Average scores. Flag any brand where ratings diverge by more than 2 points — that brand's position is ambiguous or contested.

**Option C — Proxy data**
For price axes: use actual price data. For distribution axes: use availability data. Proxy data is objective but only works when the axis has a clear real-world analogue.

Do not mix methods across axes in the same map — it produces an inconsistent scale.

---

## Step 4: Plot the Map

### Manual plotting (for client presentations)

Normalize all scores to a 0–10 scale for consistent visual spacing. Place the origin (5, 5) at center. Map the axes:

```
Axis 2 (High)
     |
     |   [Brand C]        [Brand A]
     |
     |          [Brand D]
     |
     |   [Brand B]              [Our Brand]
     |
     +---------------------------------- Axis 1 (High)
```

Label each point with the brand name. Do not use logos (they obscure position). Add axis labels at both ends (not just the positive end).

### Python snippet (matplotlib)

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

brands = {
    "島嶼啤酒":   (8.2, 8.5),
    "台灣啤酒":   (2.1, 5.0),
    "Kirin":      (5.0, 2.0),
    "Jim & Dad's": (7.8, 5.5),
}
our_brand = "島嶼啤酒"

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axhline(5, color="gray", linewidth=0.5, linestyle="--")
ax.axvline(5, color="gray", linewidth=0.5, linestyle="--")

for brand, (x, y) in brands.items():
    color = "#D62728" if brand == our_brand else "#1F77B4"
    ax.scatter(x, y, s=120, color=color, zorder=5)
    ax.annotate(brand, (x, y), textcoords="offset points",
                xytext=(8, 4), fontsize=10)

ax.set_xlabel("Price  (Low ← → High)", fontsize=11)
ax.set_ylabel("Local Identity  (Low ← → High)", fontsize=11)
ax.set_title("Perceptual Map — Taiwanese Beer Market", fontsize=13)
plt.tight_layout()
plt.savefig("perceptual_map.png", dpi=150)
```

---

## Step 5: Interpret the Map

### Identify white space

White space = a quadrant or region with no current occupant, *and* where customers would value a brand positioned there.

**Warning:** Not all white space is opportunity. Ask two questions before calling a gap "strategic white space":

1. Is this quadrant empty because no one wants what it represents? (e.g., "high price + low quality" is always empty — it's not a gap, it's a graveyard)
2. Is this quadrant reachable given your capabilities and cost structure?

White space is only actionable if it combines *unmet demand* with *deliverability*.

### Identify crowding

If 3+ brands cluster in the same region, that space is crowded. A new brand entering there must out-execute incumbents to win — positioning alone won't differentiate. In a crowded map, look at the edges and opposite quadrants.

### Check your own position

If your brand plots near the center of the map, it is perceived as undifferentiated — the worst position. The center means "nothing notable in any direction." This often manifests as customers saying "it's fine, I guess."

---

## Worked Example: Taipei Co-Working Spaces

### Research findings (from 15 customer interviews + 40-person survey)

Target segment: freelancers and small teams (1–5 people) in Taipei.

Top dimensions mentioned: cost, vibe/community, location, flexibility of hours. After correlation check, *cost* and *community vibe* emerged as the two least-correlated, most-discriminating axes.

### Survey results (1–7 scale, n=40)

| Brand | Affordability (1=expensive, 7=cheap) | Community (1=transactional, 7=community-driven) |
|---|---|---|
| WeWork Xinyi | 2.1 | 3.8 |
| Regus | 2.5 | 2.2 |
| The Hive | 3.4 | 5.9 |
| Our brand (草地空間) | 5.1 | 6.2 |
| 獨立咖啡廳 (category anchor) | 6.8 | 4.1 |

### Map interpretation

```
Community (High)
     |
     |  草地空間 ●        ● The Hive
     |
     |              ● 獨立咖啡廳
     |
     |  ● WeWork          ● Regus
     |
     +-----------------------------------------
   Cheap                              Expensive
```

**White space identified:** High community + high price quadrant is empty. No brand currently combines premium pricing with strong community. If the target segment would pay a premium for curated community (requires validation), this is a positioning opportunity.

**草地空間's current position:** Affordable + high community. Differentiated from WeWork/Regus (transactional + expensive) and from coffee shops (affordable but no community infrastructure). The position is defensible but the "affordable" end risks being out-competed on price by coffee shops or by new entrants.

---

## When to Rebuild the Map

A perceptual map reflects perception at a point in time. Rebuild when:

- A major competitor enters or exits the market
- A competitor runs a significant repositioning campaign
- You change your own positioning signals (pricing, distribution, communications)
- More than 18 months have passed since the last research

Do not update the map based on internal assumptions ("we launched a new product, so we've probably moved"). Perception changes slowly and lags execution. Validate with new customer data.

---

## Limitations to Disclose

**Two-dimensional constraint.** Real brand perception is multi-dimensional. A 2D map always compresses information. If two brands score identically on your chosen axes but customers perceive them as very different, your axes are missing something important.

**Average obscures variance.** A brand that polarizes customers (some rate it 2, others rate it 9) will plot in the middle of the map — appearing to be a bland, moderate brand. Always look at score distributions, not just means.

**Perception ≠ preference.** A perceptual map shows where brands are perceived to be, not which position customers prefer. A brand can be distinctly positioned in an undesirable quadrant. You need a separate preference analysis (e.g., ideal-point mapping) to know if a white space is desirable.

**Self-perception bias.** Asking customers to rate your brand on a survey they know you commissioned inflates scores. Use blind labeling ("Brand A, Brand B") when possible for the most accurate data.
