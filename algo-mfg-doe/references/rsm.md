# Response Surface Methodology (RSM)

RSM fits a **curved model** to a response so you can find its optimum — not just rank factor importance. Use RSM when you suspect non-linearity and need a predicted optimum, not just "which factors matter."

---

## When RSM Replaces Full Factorial

| Situation | Use |
|-----------|-----|
| Screening (7+ factors, unknown which matter) | Fractional factorial first |
| Confirmed 2-4 key factors, linear model fits well | 2^k full factorial |
| Center-point test shows curvature (p < 0.05) | **RSM (CCD or Box-Behnken)** |
| Known non-linear physics (e.g., Arrhenius kinetics) | RSM |
| Need a predicted optimum with confidence interval | **RSM** |

The signal to escalate from factorial to RSM: add center points to your 2^k design, fit a model, test the curvature term. If curvature is significant, your linear model is wrong.

---

## The Quadratic Model

RSM fits a second-order polynomial:

```
ŷ = β₀ + Σ βᵢxᵢ + Σ βᵢᵢxᵢ² + Σ βᵢⱼxᵢxⱼ + ε
```

Where:
- `xᵢ` = coded factor levels (−1, 0, +1 scale)
- `βᵢ` = linear (main) effects
- `βᵢᵢ` = quadratic (curvature) effects
- `βᵢⱼ` = interaction effects
- `ε` = random error

**Why coded units?** Coding equalizes scale differences (e.g., temperature 150–200°C vs pressure 1–10 bar). Coded value = (actual − center) / (half-range). Coefficients in coded units are directly comparable.

For 2 factors (temperature `x₁`, pressure `x₂`):

```
ŷ = β₀ + β₁x₁ + β₂x₂ + β₁₁x₁² + β₂₂x₂² + β₁₂x₁x₂
```

Six parameters → need ≥6 distinct design points with variance spread across the surface.

---

## Design Choices: CCD vs Box-Behnken

### Central Composite Design (CCD)

Builds on a 2^k factorial by adding:
1. **Center points** (replicated, 3–5 runs at x=0 for all factors)
2. **Axial (star) points** at ±α on each axis

For k=2 factors, α = 2^(k/4) = 2^0.5 ≈ 1.414 (rotatable design)

```
Design matrix, k=2, α=1.414:

Run   x₁      x₂      Type
1    −1      −1      Factorial corner
2    +1      −1
3    −1      +1
4    +1      +1
5    −1.414   0      Axial
6    +1.414   0
7     0      −1.414
8     0      +1.414
9     0       0      Center (repeat 3–5×)
10    0       0
11    0       0
```

Total: 4 (corners) + 4 (axial) + 3 (centers) = **11 runs** for 2 factors.
For k=3: 8 + 6 + 6 = **20 runs** (vs 8 for a full 2³).

**CCD variants:**
- **Circumscribed (CCC)**: axial points outside cube (α > 1). Allows widest model exploration but requires factor settings beyond factorial range.
- **Inscribed (CCI)**: axial points inside cube (α < 1). Use when factorial corners are at the physical limit.
- **Face-centered (CCF)**: α = 1, axial points on cube faces. Requires only 3 levels per factor. Slightly less estimability of curvature.

### Box-Behnken Design (BBD)

Alternative: midpoints of cube edges + center points. **Never tests factor combinations at corner extremes** (all factors at high or all at low simultaneously).

```
Box-Behnken, k=3 (Temperature T, Pressure P, Time t):

Run   T    P    t
1    −1   −1    0
2    +1   −1    0
3    −1   +1    0
4    +1   +1    0
5    −1    0   −1
6    +1    0   −1
7    −1    0   +1
8    +1    0   +1
9     0   −1   −1
10    0   +1   −1
11    0   −1   +1
12    0   +1   +1
13    0    0    0   (center, repeated 3×)
14    0    0    0
15    0    0    0
```

Total: **15 runs** for k=3 (vs 20 for CCD).

**Choose BBD when:** extreme factor combinations are physically dangerous or impossible (e.g., max temperature + max pressure + max time would destroy the process).

**Choose CCD when:** you can test extreme corners and want better prediction at the edges of the design space.

---

## Worked Example: Injection Molding Yield

**Scenario:** Two factors confirmed significant in 2³ factorial. Center-point curvature test: p=0.02. Upgrade to CCD.

**Factors:**
- Temperature (T): 160°C (−1), 180°C (0), 200°C (+1). Axial: 154.6°C (−1.414), 205.4°C (+1.414)
- Pressure (P): 40 bar (−1), 50 bar (0), 60 bar (+1). Axial: 35.9 bar (−1.414), 64.1 bar (+1.414)

**Collected response (Yield %):**

| Run | x₁(T) | x₂(P) | Yield |
|-----|--------|--------|-------|
| 1   | −1     | −1     | 78.2  |
| 2   | +1     | −1     | 85.1  |
| 3   | −1     | +1     | 82.4  |
| 4   | +1     | +1     | 88.9  |
| 5   | −1.414 |  0     | 76.3  |
| 6   | +1.414 |  0     | 87.8  |
| 7   |  0     | −1.414 | 81.5  |
| 8   |  0     | +1.414 | 86.2  |
| 9   |  0     |  0     | 91.4  |
| 10  |  0     |  0     | 91.0  |
| 11  |  0     |  0     | 91.7  |

**Fitted model (via OLS on coded units):**

```
ŷ = 91.37 + 4.15x₁ + 2.18x₂ − 4.82x₁² − 1.97x₂² + 0.60x₁x₂
```

**ANOVA summary:**

| Term | Coefficient | p-value | Significant? |
|------|-------------|---------|--------------|
| Intercept | 91.37 | — | — |
| T (linear) | 4.15 | 0.001 | Yes |
| P (linear) | 2.18 | 0.018 | Yes |
| T² | −4.82 | 0.002 | Yes |
| P² | −1.97 | 0.041 | Yes |
| T×P | 0.60 | 0.38 | No |

R² = 0.97, R²adj = 0.95. Residuals: normal probability plot OK, no pattern vs run order.

The negative quadratic terms confirm a **maximum** exists inside the design space.

---

## Finding the Optimum

### Canonical Analysis

Set partial derivatives to zero to find the stationary point (maximum/minimum/saddle).

For the example above (dropping the non-significant T×P term):

```
∂ŷ/∂x₁ = 4.15 − 9.64x₁ = 0  →  x₁* = 0.430
∂ŷ/∂x₂ = 2.18 − 3.94x₂ = 0  →  x₂* = 0.553
```

**Decode to actual units:**

```
T* = 180 + 0.430 × 20 = 188.6°C
P* = 50  + 0.553 × 10 = 55.5 bar
```

**Predicted optimum:**

```
ŷ* = 91.37 + 4.15(0.430) + 2.18(0.553) − 4.82(0.430)² − 1.97(0.553)²
   = 91.37 + 1.785 + 1.206 − 0.891 − 0.603
   = 92.87%
```

**Nature of stationary point:** Both quadratic coefficients negative → this is a **maximum** (not a saddle). If signs were mixed, it would be a saddle; eigenvalue analysis of the quadratic coefficient matrix B would then be required.

### Confirmation Runs

Run 3–5 experiments at (188.6°C, 55.5 bar). These must fall within the prediction interval:

```
Prediction interval ≈ ŷ* ± t(α/2, df_error) × √(MSE × (1 + xᵀ(XᵀX)⁻¹x))
```

Practically: if your confirmation runs average within ±2 standard deviations of ŷ*, the model is validated. If they miss, the model is extrapolating, the process drifted, or an uncontrolled noise factor is active.

---

## Model Adequacy Checks

Run these checks before trusting the optimum:

**1. R² and R²adj**
- R² > 0.90 for process optimization
- If R²adj << R², you have insignificant terms inflating R²; drop them

**2. Lack-of-Fit test**
- Requires replicated center points
- H₀: model form is adequate
- Significant lack-of-fit (p < 0.05) = your model is the wrong shape; consider adding terms or transforming the response

**3. Residual plots (mandatory)**
```
Plot 1: Residuals vs fitted values — should show no funnel or pattern
Plot 2: Normal probability plot of residuals — should be linear
Plot 3: Residuals vs run order — should be random (checks for time trends)
```

**4. Check that optimum is inside the design space**
If x* is outside coded [−1.414, +1.414], the model is extrapolating. You need a new experiment centered on the edge, or accept a boundary optimum.

---

## Transformations for Non-Normal Responses

If residuals are skewed or variance scales with the mean:

| Response type | Suggested transform |
|---------------|---------------------|
| Yield (%) near 0 or 100 | Arcsin(√p) or logit |
| Count data | √y or log(y+1) |
| Time-to-event, rate | log(y) |
| Variance scales with mean | Box-Cox λ selection |

**Box-Cox procedure:** try λ ∈ {−2, −1, −0.5, 0, 0.5, 1, 2}; pick λ that maximizes the log-likelihood. λ=0 means log(y); λ=0.5 means √y. If 95% CI for λ includes 1, no transform is needed.

After transforming, the optimum is found in transformed units and back-transformed for interpretation. **Do not back-transform coefficients** — back-transform only the predicted optimal value.

---

## Common Mistakes

**Mistake 1: Optimizing outside the design boundary**
The quadratic model is only valid within the experimental region. Extrapolated maxima are artifacts of the polynomial, not physics. Always verify x* ∈ [−α, +α] for all factors.

**Mistake 2: Ignoring the lack-of-fit test**
A high R² with significant lack-of-fit means your model fits the specific runs well but not the underlying surface. More runs or a different model form are needed.

**Mistake 3: Skipping confirmation runs**
The model predicts ŷ* under the assumption that the process behaves identically to when the experiments were run. Confirmation runs catch: process drift, uncontrolled noise factors, operator effects, and model curvature not captured by the design.

**Mistake 4: Using actual units for coefficient comparison**
A coefficient of 4.15 for temperature (coded) and 0.22 for pressure (coded) means temperature has a bigger effect — only because both are on the [−1, +1] scale. In actual units (°C vs bar), the coefficients are not comparable.

**Mistake 5: Reporting only the optimum, not the ridge**
Near a maximum, the response surface is often flat across a ridge. Reporting only the point optimum misses the practical insight that a range of settings performs nearly as well. Examine contour plots and report a feasible operating window, not just the single point.
