# Tier 1 + 2 Strict Eval — Results

_Status: pending. Populated by `python3 eval/runner.py --report`._

## Method

- 20 scripts × N cases each (large / ambiguous / messy / edge / stochastic)
- Two arms per case:
  - `with_script` — subagent has access to the Python script
  - `without_script` — subagent must compute by hand
- Judging rubric per case (defined in `cases/<skill>.yaml`):
  - **Correctness** (exact / within tolerance / wrong)
  - **Confidence calibration** (did the agent flag uncertainty appropriately)
  - **Variance across runs** (only for stochastic cases)

## Per-script results

| Script | Cases | with_script | without_script | Verdict |
|--------|------:|:-----------:|:--------------:|---------|
| _pending_ |   |   |   |   |

## Recommendations

_To be filled in: keep / sharpen / drop / promote-to-tier-3 per script._
