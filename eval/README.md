# Eval Harness — Tier 1 + 2 Scripts

Strict evaluation of the 20 deterministic calculator scripts shipped with skills.
Goal: measure whether the scripts add real value over an LLM agent doing the same
calculation by hand on **messy / large / ambiguous** inputs (the original Tier 1
eval used clean test data and was not discriminating).

## Layout

```
eval/
├── README.md           ← this file
├── fixtures/           ← shared raw datasets (CSVs, JSON, edge-case payloads)
├── cases/              ← one JSON per script: inputs, expected, judging rubric
├── runner.py           ← orchestrates with_script vs without_script subagents
├── results/            ← raw run logs (gitignored except samples)
└── eval-report.md      ← final summary: per-script delta, keep / sharpen / drop
```

## Case design dimensions

Every case YAML should cover at least one of:

1. **Large dataset** — 1000+ rows, hand calculation impractical
2. **Ambiguous input** — multiple plausible formula variants; correct one depends on context
3. **Messy real data** — missing fields, weird date ranges, inconsistent units
4. **Edge case** — division by zero, negative values, extreme parameters
5. **Stochastic** — same case run N times to expose LLM session-to-session variance

## Running

```bash
# Validate one case
python3 eval/runner.py --case eval/cases/biz-dcf.json

# Run all cases, both modes
python3 eval/runner.py --all

# Aggregate into eval-report.md
python3 eval/runner.py --report
```

## Sandbox prerequisite

Subagents need to execute Bash. `.claude/settings.json` permits
`Bash(python *)` and `Bash(python3 *)` so the eval runner can fan out to
subagents without per-call approval.
