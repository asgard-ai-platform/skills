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
| `biz-dcf` | **speed** | 1/4 (30yr-decimal-noise: 11.8× faster) | Sonnet 4.6 hand-computes 30yr DCF correctly in 412s; script does it in 35s. Other scenarios (mixed-tw-units, ambiguous mid-year, edge wacc=g) all pass on both arms with no meaningful speed delta. **Script's value is purely cost/latency, not correctness, at this difficulty.** |

_19 more scripts pending fan-out._

## Recommendations (preliminary)

- For pure-arithmetic scripts (DCF, financial ratios), expect **speed** verdicts.
  Hand-computation accuracy on Sonnet 4.6 is high; the script's value is keeping
  per-call cost predictable when projections are long.
- To find **correctness** wins, target scripts where LLMs are known to misremember
  formulas or apply wrong variants: Wilson interval, EOQ optimization, Altman Z,
  Cpk, Bayesian rating priors, etc.
- Scripts with **neither** verdict on every scenario are candidates for removal —
  they cost maintenance but add nothing the LLM cannot already do.
