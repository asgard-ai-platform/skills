# SEM Mathematical Notation and Estimation

## Model Specification

SEM combines a **measurement model** (relating latent variables to observed indicators) with a **structural model** (relating latent variables to each other).

### Measurement Model

For each latent variable η with p indicators y:
```
y = Λ_y × η + ε
```
where:
- y: p × 1 vector of observed indicators
- Λ_y: p × m matrix of factor loadings
- η: m × 1 vector of latent variables
- ε: p × 1 vector of measurement errors (E[ε] = 0, Cov(ε) = Θ_ε)

Similarly for exogenous latent variables ξ with indicators x:
```
x = Λ_x × ξ + δ
```

### Structural Model

```
η = B × η + Γ × ξ + ζ
```
where:
- B: m × m matrix of relationships among endogenous latents
- Γ: m × n matrix of effects of exogenous on endogenous
- ζ: structural disturbances (E[ζ] = 0, Cov(ζ) = Ψ)

## Model-Implied Covariance Matrix

The key insight of SEM: given the parameters (Λ, B, Γ, Θ, Ψ), we can derive the covariance matrix Σ that the model IMPLIES the data should have:

```
Σ(θ) = [Σ_yy  Σ_yx]
       [Σ_xy  Σ_xx]
```

where each block is a function of the model parameters θ = {Λ_y, Λ_x, B, Γ, Φ, Ψ, Θ_ε, Θ_δ}.

## Estimation: Maximum Likelihood

Under multivariate normality, the ML fit function is:
```
F_ML(θ) = log|Σ(θ)| + tr(S × Σ(θ)^(-1)) - log|S| - p
```

where S is the sample covariance matrix and p is the number of observed variables. Minimize F_ML over θ to get parameter estimates.

## Fit Indices

Given estimated parameters, compare Σ(θ̂) to S:

| Index | Formula | Good Fit Threshold |
|-------|---------|-------------------|
| **Chi-square** | χ² = (N-1) × F_ML(θ̂) | p > 0.05 (often fails in large samples) |
| **CFI** | 1 - max(χ² - df, 0) / max(χ²_null - df_null, χ² - df, 0) | ≥ 0.95 (excellent), ≥ 0.90 (acceptable) |
| **TLI** | (χ²_null/df_null - χ²/df) / (χ²_null/df_null - 1) | ≥ 0.95 |
| **RMSEA** | √(max(χ²-df, 0) / (df × (N-1))) | ≤ 0.06 (good), ≤ 0.08 (acceptable) |
| **SRMR** | standardized root mean squared residual | ≤ 0.08 |

## Identification

A model is identified if the parameters can be uniquely solved from the population covariance matrix. Check:
- **Order condition** (necessary): number of free parameters ≤ number of unique elements in S = p(p+1)/2
- **Rank condition** (sufficient): Jacobian of Σ(θ) has full column rank

Underidentified models cannot be estimated. Just-identified models fit perfectly (no degrees of freedom to test). Overidentified models allow hypothesis testing.

## Non-Normal Data

When multivariate normality fails:
- Use **robust ML** (Satorra-Bentler corrected χ² and standard errors)
- Use **WLSMV** for categorical indicators
- Bootstrap for confidence intervals on indirect effects

## Sample Size Rules of Thumb

- Minimum N = 200 for simple models
- N ≥ 10 observations per estimated parameter (Bentler & Chou, 1987)
- N ≥ 20 per parameter for complex models or non-normal data

## References

- Jöreskog, K. G. (1973). *A general method for estimating a linear structural equation system*.
- Bollen, K. A. (1989). *Structural Equations with Latent Variables*.
- Kline, R. B. (2015). *Principles and Practice of Structural Equation Modeling* (4th ed.).
