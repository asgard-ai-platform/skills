# Tier 1 + 2 Strict Eval — Results

_Last updated: 2026-04-07. Model: `claude-sonnet-4-6`._

## Method

- 20 scripts × N scenarios each (large / ambiguous / edge / messy_units dimensions)
- Two arms per scenario:
  - `with_script` — subagent has Bash + Read; can execute the calculator (180s timeout)
  - `without_script` — subagent has Read only; must compute by hand (720s timeout)
- Both arms get the same SKILL.md methodology in the prompt; only tool access differs
- Scoring rubrics: `within_1_percent`, `within_1_percent_AND_units_consistent`,
  `judge_flagged_assumption`, `must_raise_or_refuse`

## Per-scenario value classes

- **correctness** — with_script passes, without_script fails → script prevents wrong answers
- **speed** — both pass, but without_script ≥ 3× slower → script saves time/cost
- **both** — correctness AND speed
- **neither** — both pass at similar speed → script adds no measurable value
- **inconclusive** — with_script itself failed (script broken or scenario malformed)

## Results

| Skill | Case verdict | Discriminating scenarios | Notes |
|-------|--------------|--------------------------|-------|
| `algo-risk-altman-z` | **correctness** ⭐ | non-manufacturing-tech-firm: with_script pass, without_script fail | Sonnet 4.6 picks the wrong Altman variant (uses original Z instead of Z'') for a non-manufacturing firm. The script forces explicit `--variant` selection, eliminating the error. Strongest validated correctness win so far. |
| `algo-rank-wilson` | speed | 1/4 (ambiguous-confidence-99: 3.6× faster) | Tiny-sample, zero-positive, and 8/10 scenarios all pass on both arms with no speed delta. Only the 99% confidence case showed a meaningful speed advantage. |
| `biz-dcf` | speed | 1/4 (30yr-decimal-noise: 11.8× faster) | Sonnet 4.6 hand-computes 30yr DCF correctly in 412s; script does it in 35s. Other scenarios (mixed-tw-units, ambiguous mid-year, edge wacc=g) all pass on both arms with no meaningful speed delta. Script's value is purely cost/latency, not correctness, at this difficulty. |
| `algo-mfg-cpk` | neither | 0/3 | Off-center process, single-sided spec (USL only), zero-sd refusal — Sonnet handles all three by hand. Strong candidate for **removal**. |
| `algo-rank-bayesian` | neither | 0/3 | All 3 scenarios pass on both arms after fixing scorer to require exact key names. Notably, small-n-trap shows ratio 0.2× — `with_script` is 5× SLOWER than hand because Bash/tool overhead dominates trivial arithmetic. Strong candidate for **removal**. |
| `algo-sc-eoq` | neither | 0/3 | Both arms compute basic EOQ, holding-cost-from-percentage, and edge zero-H refusal correctly. Strong candidate for **removal**. |
| `mkt-ab-testing` | **speed (strong)** | 3/3 (4.2× / 4.5× / 11.0×) | Two-proportion z-test arithmetic — especially p-value via normal CDF — is slow enough by hand (80–228s) that the script is uniformly faster across scenarios. Best speed result so far. **Keep**. |
| `algo-rank-elo` | speed | 1/3 (draw-higher-rated-loses-points: 3.1×) | Basic win/loss updates and elite-upset-low-K both pass with no delta. Only the draw scenario (where the higher-rated player loses points) showed a meaningful speed advantage. |
| `biz-cac-ltv` | neither | 0/3 | Sonnet correctly handles basic SaaS, annual-vs-monthly time conversion, and the margin-vs-revenue trap. Marginal removal candidate. |
| `biz-dupont` | neither | 0/2 | Both 3-factor and 5-factor decompositions hand-computed correctly. Marginal removal candidate. |
| `algo-sc-newsvendor` | neither | 0/3 | All three critical-ratio scenarios (Q\*>mean, Q\*<mean, Q\*>>mean) pass on both arms. Marginal removal candidate. |

| `algo-ecom-bm25` | **correctness** ⭐ | 1/1 (rank-4-docs) | `top_doc_id` correct on both arms but `without_script` produced `top_score = 1.9785` vs script's `2.0484` — 3.5% off, exceeding the 1% tolerance. Likely a BM25/IDF formula-variant mismatch (BM25+/BM25L/different IDF smoothing). Script forces a single canonical formula. |
| `biz-financial-ratios` | **correctness** ⭐ | 1/1 (full-ratio-pack) | `without_script` computed `debt_to_equity = 0.827` (long_term_debt/equity) where script returned `1.467` (total_liabilities/equity). The "debt to equity" definition is genuinely ambiguous in textbooks; script forces the canonical interpretation. (Three other ratios were also wrong but only because of decimal-vs-percent unit choice — not a real formula error.) |
| `ecom-rfm-analysis` | speed | 1/1 (10-customer-segmentation: 4.8×) | Quantile-edge computation across 10 customers and segment label assignment is mechanically correct on both arms, but `without_script` takes 235s vs script's 49s. |
| `algo-sc-safety-stock` | neither | 0/2 | Both 95% and 99% service levels (with combined demand + lead-time variance) computed correctly by hand. |
| `algo-seo-tfidf` | neither | 0/1 | 3-doc top-term ranking handled correctly. |
| `biz-unit-economics` | neither | 0/1 | NRR/GRR/Magic Number/Burn Multiple all computed correctly by hand. |
| `algo-price-elasticity` | neither | 0/2 | Arc midpoint formula and point elasticity both computed correctly. (Initial run showed "both" verdict; that was an Anthropic API 529 overload during the without_script call — corrected after retry-with-backoff was added to runner.) |
| `biz-breakeven` | neither | 0/2 | Basic and target-profit cases both pass. (Initial run showed "both"; same API 529 issue as elasticity — corrected after retry.) |
| `grad-capm` | neither | 0/2 | Basic + alpha and negative-beta cases both pass. (Initial run showed "mixed"; same API issue.) |

## Cumulative tally — final (20/20)

| Verdict class | Count | Skills |
|---------------|------:|--------|
| correctness ⭐ | **3** | `algo-risk-altman-z`, `algo-ecom-bm25`, `biz-financial-ratios` |
| speed | **5** | `algo-rank-wilson`, `biz-dcf`, `algo-rank-elo`, `mkt-ab-testing`, `ecom-rfm-analysis` |
| neither | **12** | `algo-mfg-cpk`, `algo-rank-bayesian`, `algo-sc-eoq`, `biz-cac-ltv`, `biz-dupont`, `algo-sc-newsvendor`, `algo-sc-safety-stock`, `algo-seo-tfidf`, `biz-unit-economics`, `algo-price-elasticity`, `biz-breakeven`, `grad-capm` |

**Hit rate: 8/20 = 40% of scripts provide measurable value.**

## Final recommendations

### Keep — strong value (3 scripts)
The three correctness winners stop the agent from making concrete, hard-to-detect formula
mistakes. Recommended to keep regardless of cost:

- `algo-risk-altman-z` — variant selection (Z / Z' / Z'') under implicit firm-type cues
- `algo-ecom-bm25` — multiple BM25 / IDF formula variants in the wild
- `biz-financial-ratios` — debt/leverage definition ambiguity (book vs total liabilities)

### Keep — speed value (5 scripts)
These provide cost / latency wins on hand-intractable cases. Keep, but document that the
value is purely operational (not correctness):

- `mkt-ab-testing` — strongest speed result; uniformly 4–11× faster
- `biz-dcf` — long-horizon projections (10+ years) become 10× slower by hand
- `ecom-rfm-analysis` — quantile assignment over many customers
- `algo-rank-wilson` — high-confidence intervals
- `algo-rank-elo` — draw scenarios

### Consider removing or downgrading — no measurable value (12 scripts)
Sonnet 4.6 hand-computes these reliably and (often) faster than calling the script. The
script costs maintenance with no validated upside at the difficulties tested:

`algo-mfg-cpk`, `algo-rank-bayesian`, `algo-sc-eoq`, `biz-cac-ltv`, `biz-dupont`,
`algo-sc-newsvendor`, `algo-sc-safety-stock`, `algo-seo-tfidf`, `biz-unit-economics`,
`algo-price-elasticity`, `biz-breakeven`, `grad-capm`.

Caveat: this list reflects Sonnet 4.6 capabilities at the scenario difficulties used.
A script in this list might still provide value if (a) the model used is weaker, (b) the
calculation is part of a much larger pipeline where hand-math compounds errors, or (c) cases
not covered here would discriminate. **Suggest spot-checking 2–3 of these against
harder/longer scenarios before final removal.**

## Method-level lessons learned

- **Anthropic API 529 overload** during eval runs causes false-positive correctness/speed
  verdicts. Runner now retries transient failures (timeout, 5xx, "Overloaded") with
  exponential backoff (15s × attempt, max 2 retries). Three Batch 3 cases were initially
  misclassified as "both" or "mixed" before this fix.
- **Strict key naming in prompts is essential.** Agents will invent natural-language key
  variants (`top_item_bayesian_avg` vs `top_bayesian_avg`); the runner now templates the
  exact expected keys into the prompt.
- **Decimal vs percent ambiguity** is a recurring scoring pitfall. Always specify "report
  as decimal (0.05 not 5)" in CAPM-style prompts.
- **Tool overhead can dominate trivial math.** Several scripts show ratios well below 1.0×
  — calling Bash to run a one-line formula is slower than computing it directly. This is
  a structural disadvantage for any script whose computation is itself trivial.

## Batch 1 take-aways

- **Hit rate so far**: 1 correctness + 2 speed + 3 neither out of 6 scripts (~50% provide some
  measurable value at the difficulties tested).
- **Tool overhead can dominate** when the math is trivial (`algo-rank-bayesian` small-n-trap).
  Scripts whose computation is a one-line formula are at risk of negative net value.
- **Strict key naming matters**: agents will invent natural-language key variants
  (`top_item_bayesian_avg` vs `top_bayesian_avg`). The runner now templates the exact keys
  into the prompt to avoid scorer false negatives.
- **Variant-selection scripts win on correctness** — agents know how to compute Altman Z but
  pick the wrong variant under pressure. Likely the same pattern for any script with
  multiple formula choices (Cpk vs Pp/Ppk maybe; check Tier 2 candidates).

## Recommendations (preliminary)

- For pure-arithmetic scripts (DCF, financial ratios), expect **speed** verdicts.
  Hand-computation accuracy on Sonnet 4.6 is high; the script's value is keeping
  per-call cost predictable when projections are long.
- To find **correctness** wins, target scripts where LLMs are known to misremember
  formulas or apply wrong variants: Wilson interval, EOQ optimization, Altman Z,
  Cpk, Bayesian rating priors, etc.
- Scripts with **neither** verdict on every scenario are candidates for removal —
  they cost maintenance but add nothing the LLM cannot already do.
