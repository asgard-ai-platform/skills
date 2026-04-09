# Fractional Factorial Design Tables

## Resolution Definitions

Resolution determines which effects are confounded (aliased) with which:

| Resolution | Abbreviation | Main Effects Aliased With | Two-Factor Interactions (2FI) Aliased With |
|------------|-------------|--------------------------|---------------------------------------------|
| III        | Res III     | Other 2FIs               | Each other or 3FIs                          |
| IV         | Res IV      | 3FIs only                | Other 2FIs                                  |
| V          | Res V       | 4FIs only                | 3FIs only                                   |

**Practical rule**: Use Res III for screening (identifying which main effects matter). Use Res IV or V when 2FIs are suspected to be important.

---

## Standard 2^(k−p) Design Tables

### 2^(3−1) — 4 runs, 3 factors, Resolution III

**Generator:** C = AB

| Run | A  | B  | C=AB |
|-----|----|----|------|
| 1   | −1 | −1 | +1   |
| 2   | +1 | −1 | −1   |
| 3   | −1 | +1 | −1   |
| 4   | +1 | +1 | +1   |

**Alias structure:**
```
A  ≡  BC
B  ≡  AC
C  ≡  AB
```

**Warning**: Every main effect is aliased with a 2FI. This design is Res III — adequate only for initial screening when you assume 2FIs are negligible.

---

### 2^(4−1) — 8 runs, 4 factors, Resolution IV

**Generator:** D = ABC

| Run | A  | B  | C  | D=ABC |
|-----|----|----|----|----- |
| 1   | −1 | −1 | −1 | −1   |
| 2   | +1 | −1 | −1 | +1   |
| 3   | −1 | +1 | −1 | +1   |
| 4   | +1 | +1 | −1 | −1   |
| 5   | −1 | −1 | +1 | +1   |
| 6   | +1 | −1 | +1 | −1   |
| 7   | −1 | +1 | +1 | −1   |
| 8   | +1 | +1 | +1 | +1   |

**Alias structure:**
```
A  ≡  BCD
B  ≡  ACD
C  ≡  ABD
D  ≡  ABC
AB ≡  CD
AC ≡  BD
AD ≡  BC
```

Main effects are clear (only aliased with 3FIs, which are usually negligible). But 2FIs are confounded with other 2FIs — you cannot tell AB from CD if both are nonzero.

---

### 2^(5−1) — 16 runs, 5 factors, Resolution V

**Generator:** E = ABCD

**Alias structure (partial):**
```
A  ≡  BCDE
B  ≡  ACDE
...
AB ≡  CDE
AC ≡  BDE
AD ≡  BCE
AE ≡  BCD
BC ≡  ADE
BD ≡  ACE
BE ≡  ACD
CD ≡  ABE
CE ≡  ABD
DE ≡  ABC
```

All main effects and all 2FIs are estimable independently. Use Res V when you need to study 2FIs without folding.

---

### 2^(5−2) — 8 runs, 5 factors, Resolution III

**Generators:** D = AB, E = AC

| Run | A  | B  | C  | D=AB | E=AC |
|-----|----|----|----|----- |------|
| 1   | −1 | −1 | −1 | +1   | +1   |
| 2   | +1 | −1 | −1 | −1   | −1   |
| 3   | −1 | +1 | −1 | −1   | +1   |
| 4   | +1 | +1 | −1 | +1   | −1   |
| 5   | −1 | −1 | +1 | +1   | −1   |
| 6   | +1 | −1 | +1 | −1   | +1   |
| 7   | −1 | +1 | +1 | −1   | −1   |
| 8   | +1 | +1 | +1 | +1   | +1   |

**Alias structure (main effect chains):**
```
A  ≡  BD  ≡  CE
B  ≡  AD  ≡  ...
C  ≡  AE  ≡  ...
D  ≡  AB  ≡  ...
E  ≡  AC  ≡  ...
```

---

### 2^(6−1) — 32 runs, 6 factors, Resolution VI

**Generator:** F = ABCDE

All main effects and all 2FIs are estimable. 2FIs aliased only with 4FIs. Use when you have 6 factors and budget for 32 runs.

---

### 2^(6−2) — 16 runs, 6 factors, Resolution IV

**Generators:** E = ABC, F = BCD

**Alias structure (2FI pairs):**
```
AB ≡  CE  ≡  DF  ≡  ...
AC ≡  BE  ≡  ...
AF ≡  BD  ≡  ...
```

2FIs aliased with other 2FIs. Requires follow-up (fold-over or partial fold) to de-alias if multiple 2FIs are significant.

---

### 2^(7−1) — 64 runs, 7 factors, Resolution VII

**Generator:** G = ABCDEF

All main effects and 2FIs are estimable. 2FIs aliased only with 5FIs.

---

### 2^(7−2) — 32 runs, 7 factors, Resolution IV

**Generators:** F = ABCD, G = ABDE

---

### 2^(7−3) — 16 runs, 7 factors, Resolution IV

**Generators:** E = ABC, F = ABD, G = ACD

**Alias structure (2FIs aliased with 2FIs):**
```
AB ≡  CE  ≡  DF  ≡  ...
AC ≡  BE  ≡  DG  ≡  ...
```

---

### Quick Reference: Minimum Run Designs

| Factors (k) | Res III (min runs) | Design       | Res IV (min runs) | Design       | Res V (min runs) | Design       |
|-------------|-------------------|--------------|-------------------|--------------|-----------------|--------------|
| 3           | 4                 | 2^(3−1)_III  | 8 (full)          | 2^3          | 8 (full)        | 2^3          |
| 4           | 8                 | 2^(4−1)_III* | 8                 | 2^(4−1)_IV  | 16 (full)       | 2^4          |
| 5           | 8                 | 2^(5−2)_III  | 16                | 2^(5−1)_IV  | 16              | 2^(5−1)_V   |
| 6           | 8                 | 2^(6−3)_III  | 16                | 2^(6−2)_IV  | 32              | 2^(6−1)_VI  |
| 7           | 8                 | 2^(7−4)_III  | 16                | 2^(7−3)_IV  | 64 (full)       | 2^7          |
| 8           | 16                | 2^(8−4)_IV  | 32                | 2^(8−3)_V  | —               | —            |

*The 2^(4−1) with generator D=ABC is actually Res IV, not III.

---

## How to Read and Construct a Design from Generators

Given generators, you can construct any design matrix:

**Step 1: Assign base factors.** For a 2^(k−p) design, the first k−p columns are independent base factors. Write them out as a full 2^(k−p) matrix using standard order (all combinations of −1 and +1, cycling from the rightmost column).

**Standard order for k−p = 3 (8 runs):**

| Run | A  | B  | C  |
|-----|----|----|-----|
| 1   | −1 | −1 | −1 |
| 2   | +1 | −1 | −1 |
| 3   | −1 | +1 | −1 |
| 4   | +1 | +1 | −1 |
| 5   | −1 | −1 | +1 |
| 6   | +1 | −1 | +1 |
| 7   | −1 | +1 | +1 |
| 8   | +1 | +1 | +1 |

**Step 2: Apply generators.** For each added factor, multiply the specified columns element-wise. Sign rule: (−1)(−1) = +1, (+1)(−1) = −1.

**Example:** Generator D = ABC for 2^(4−1):
- Run 1: D = (−1)(−1)(−1) = −1
- Run 2: D = (+1)(−1)(−1) = +1
- Run 3: D = (−1)(+1)(−1) = +1
- Run 4: D = (+1)(+1)(−1) = −1
- etc.

**Step 3: Randomize.** Shuffle run order before execution. Never run in standard order — time trends will confound with factor effects.

---

## Computing the Alias Structure

The alias structure follows from the **defining relation** I.

**Defining relation from generators:**

For 2^(4−1) with generator D = ABC:
```
I = ABCD
```

To find what any effect is aliased with, multiply it by every word in the defining relation:
```
A × ABCD = A²BCD = BCD    →  A ≡ BCD
B × ABCD = AB²CD = ACD    →  B ≡ ACD
AB × ABCD = A²B²CD = CD   →  AB ≡ CD
```

Rule: any letter squared = I (identity), so drops out.

**For two generators**, the defining relation includes the product of the two generators as well:

2^(5−2) with E = ABC, F = ACD:
```
I = ABCE = ACDF = BCDEF (product of generators: ABCE × ACDF = A²BC²DEF = BDEF... recalculate)
```

Actually: ABCE × ACDF = A²BC²DEF = BDEF, so:
```
I = ABCE = ACDF = BDEF
```

All effects aliased with: multiply the effect by each word in {ABCE, ACDF, BDEF}.

---

## Decision Framework: Which Design to Choose

```
How many factors?
│
├── 2-4 factors
│     → Run full factorial (2^k = 4, 8, or 16 runs)
│     → Add center points (3-5) to detect curvature
│
├── 5-7 factors, goal = screening
│     → How many runs can you afford?
│     │
│     ├── 8 runs → Plackett-Burman (if only main effects matter)
│     │          → 2^(k−p) Res III (if you need some 2FI info)
│     │
│     └── 16 runs → 2^(k−p) Res IV (main effects clear, some 2FIs estimable)
│
├── 5-7 factors, goal = optimization
│     → Run Res V design (2^5-1 = 16, 2^6-1 = 32)
│     → Or: screen first with Res III, then optimize survivors
│
└── 8+ factors
      → Use Plackett-Burman (12, 20, or 24 runs) for pure screening
      → Fractional factorial becomes impractical for optimization
```

---

## Worked Example: Selecting and Constructing a 2^(5−2) Design

**Scenario:** 5 process factors (A=temperature, B=pressure, C=time, D=catalyst_conc, E=pH). Budget: 8 runs. Goal: screen for significant main effects.

**Step 1: Select design.** 5 factors, 8 runs → 2^(5−2)_III. Accept Res III (main effects estimable, 2FIs confounded with main effects — OK for screening).

**Step 2: Choose generators.** Standard choice: D = AB, E = AC.

**Step 3: Construct matrix.**

Base (A, B, C in standard order) + compute D = AB, E = AC:

| Run | A  | B  | C  | D=AB | E=AC | Temperature | Pressure | Time | Catalyst | pH  |
|-----|----|----|----|----- |------|-------------|----------|------|----------|-----|
| 1   | −  | −  | −  | +    | +    | 160         | 40       | 20   | 2%       | 6.5 |
| 2   | +  | −  | −  | −    | −    | 200         | 40       | 20   | 1%       | 5.5 |
| 3   | −  | +  | −  | −    | +    | 160         | 60       | 20   | 1%       | 6.5 |
| 4   | +  | +  | −  | +    | −    | 200         | 60       | 20   | 2%       | 5.5 |
| 5   | −  | −  | +  | +    | −    | 160         | 40       | 40   | 2%       | 5.5 |
| 6   | +  | −  | +  | −    | +    | 200         | 40       | 40   | 1%       | 6.5 |
| 7   | −  | +  | +  | −    | −    | 160         | 60       | 40   | 1%       | 5.5 |
| 8   | +  | +  | +  | +    | +    | 200         | 60       | 40   | 2%       | 6.5 |

**Step 4: Randomize run order** before execution. Example: shuffle to order [3, 7, 1, 5, 8, 2, 6, 4].

**Step 5: Check alias structure** before running. With I = ABD = ACE = BCDE:
```
A ≡ BD ≡ CE ≡ ABCDE
B ≡ AD ≡ CDE ≡ ...
C ≡ AE ≡ BDE ≡ ...
D ≡ AB ≡ BCE ≡ ...
E ≡ AC ≡ BCD ≡ ...
```

If temperature (A) appears significant, it could actually be the BD or CE interaction. To de-alias, fold the design (add 8 more runs with A signs reversed) if required.

---

## Fold-Over: De-Aliasing After Res III Screening

When a Res III result is ambiguous (e.g., A is significant but BD or CE may be the true cause), add a fold-over block:

**Fold-over rule:** In the fold block, reverse the sign of **all factors** (complete fold) or one specific factor (single-factor fold).

**Complete fold-over of 2^(5−2):** Negate all columns in the original 8 runs. The combined 16-run design has Res IV — main effects now clear of all 2FIs.

**Single-factor fold on A:** Negate only column A. This de-aliases A from all its 2FI aliases (BD, CE) but leaves other main effects still confounded.

Use complete fold when multiple factors are ambiguous; single-factor fold when only one factor's aliases are in question.

---

## Plackett-Burman Designs (Screening Only, Not Covered by Standard 2^(k−p) Tables)

For k = 11 factors in 12 runs, or k = 19 factors in 20 runs, use Plackett-Burman (PB) designs. These are **not** 2^(k−p) designs — they have complex, partial aliasing where each main effect is partially confounded with every 2FI, not fully aliased with a small number.

**12-run PB base row** (cycle to generate matrix):
```
+ + − + + + − − − + −
```

Cyclic construction: shift this row left by one position for each subsequent run; last run is all minus signs.

**Warning**: PB designs cannot estimate 2FIs at all — each 2FI is partially confounded across all main effects. Use PB only when you are confident 2FIs are negligible and you need to screen many factors cheaply.

---

## Confounding Pattern Comparison

| Design         | Runs | Factors | Main Effects Clear? | 2FIs Estimable?            | Use For          |
|----------------|------|---------|--------------------|-----------------------------|------------------|
| 2^(4−1) Res IV | 8    | 4       | Yes (vs 3FIs)      | No (2FIs aliased w/ 2FIs)   | Screening        |
| 2^(5−1) Res V  | 16   | 5       | Yes                | Yes (vs 3FIs)               | Optimization     |
| 2^(5−2) Res III| 8    | 5       | No (vs 2FIs)       | No                          | Coarse screen    |
| 2^(6−2) Res IV | 16   | 6       | Yes                | No (2FIs aliased w/ 2FIs)   | Screening        |
| 2^(7−3) Res IV | 16   | 7       | Yes                | No                          | Screening        |
| PB 12-run      | 12   | 11      | Partial aliasing   | No                          | Mass screening   |
