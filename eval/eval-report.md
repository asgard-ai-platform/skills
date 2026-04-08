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

_9 more scripts pending fan-out._

## Cumulative tally (11/20)

| Verdict class | Count | Skills |
|---------------|------:|--------|
| correctness ⭐ | 1 | `algo-risk-altman-z` |
| speed | 4 | `algo-rank-wilson`, `biz-dcf`, `algo-rank-elo`, `mkt-ab-testing` |
| neither | 6 | `algo-mfg-cpk`, `algo-rank-bayesian`, `algo-sc-eoq`, `biz-cac-ltv`, `biz-dupont`, `algo-sc-newsvendor` |

**Hit rate so far: ~45% provide some measurable value.**

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
