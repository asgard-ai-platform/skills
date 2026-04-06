# CAPM Derivation from Mean-Variance Optimization

## Setup

Assume N risky assets with returns r_i, expected returns E(r_i), and covariance matrix Σ. A risk-free asset exists with return r_f. Investors are mean-variance optimizers (Markowitz, 1952).

## The Tangency Portfolio

Every mean-variance optimizer chooses a portfolio on the efficient frontier. With a risk-free asset, the efficient frontier becomes a straight line (Capital Market Line) tangent to the risky-asset frontier at the tangency portfolio T.

**Two-fund separation theorem:** Every investor holds some combination of the risk-free asset and the tangency portfolio. Only the MIX varies by risk aversion, not the composition of the risky portfolio.

## Market Equilibrium

In equilibrium, if every investor holds T, then T MUST equal the market portfolio M (value-weighted portfolio of all risky assets). Otherwise some assets would be in excess demand or supply.

## Deriving the SML

For any asset i and the market portfolio M, the covariance is:
```
Cov(r_i, r_M) = Σ w_j × Cov(r_i, r_j)    where w_j are market weights
```

Mean-variance optimization of M with respect to its weights gives the first-order condition:
```
E(r_i) - r_f = λ × Cov(r_i, r_M)    for all i
```
where λ is a Lagrange multiplier.

Applied to M itself:
```
E(r_M) - r_f = λ × Var(r_M)
→ λ = (E(r_M) - r_f) / Var(r_M)
```

Substituting back:
```
E(r_i) - r_f = [Cov(r_i, r_M) / Var(r_M)] × (E(r_M) - r_f)
```

Defining **beta** as:
```
β_i = Cov(r_i, r_M) / Var(r_M)
```

Yields the **Security Market Line (SML)**:
```
E(r_i) = r_f + β_i × (E(r_M) - r_f)
```

## Interpretation

- β_i measures the asset's contribution to market portfolio variance.
- Only systematic risk (covariance with the market) is priced.
- Idiosyncratic risk is diversified away in M and earns no premium.
- The risk premium (E(r_M) - r_f) compensates for bearing systematic risk.

## Assumptions Used

1. Investors are mean-variance optimizers
2. Homogeneous expectations (everyone agrees on E, Σ)
3. Risk-free lending and borrowing at the same rate
4. No taxes, transaction costs, or short-sale constraints
5. Assets are infinitely divisible and marketable

Violating ANY of these breaks the clean SML relationship — which is why empirical tests of CAPM fail (Roll's critique, 1977).

## References

- Sharpe (1964), Lintner (1965), Mossin (1966) — original CAPM
- Markowitz (1952) — mean-variance foundation
- Roll (1977) — critique and testability problems
