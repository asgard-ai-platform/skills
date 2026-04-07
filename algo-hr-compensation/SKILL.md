---
name: "algo-hr-compensation"
description: "Conduct compensation benchmarking analysis to position salaries against market data. Use this skill when the user needs to assess pay competitiveness, build salary bands, or analyze pay equity — even if they say 'are we paying market rate', 'salary benchmarking', or 'compensation analysis'."
metadata:
  category: "WP-42 HR 演算法"
  tags: ["hr", "compensation", "benchmarking", "salary-analysis"]
---

# Compensation Benchmarking

## Overview

Compensation benchmarking compares internal pay levels against external market data to assess competitiveness. Uses compa-ratio (actual pay / market midpoint) and percentile positioning. Informs salary band design, pay adjustments, and equity analysis.

## When to Use

**Trigger conditions:**
- Evaluating whether current salaries are competitive with the market
- Designing or updating salary bands and pay structures
- Identifying pay equity gaps across demographics or roles

**When NOT to use:**
- For individual performance-based pay decisions (use performance management)
- When no market data is available (need at least survey benchmarks)

## Algorithm

```
IRON LAW: Benchmarking Is Only Valid With COMPARABLE Jobs
Matching by job TITLE alone is unreliable — "Senior Engineer" means
vastly different things at different companies. Match by: job content
(duties, scope), level (IC vs manager, experience band), industry,
geography, and company size. Poor job matching produces misleading
market rates.
```

### Phase 1: Input Validation
Collect: internal compensation data (base, bonus, equity), market survey data (P25, P50, P75 by role), job matching between internal roles and survey benchmarks.
**Gate:** Jobs properly matched, survey data current (< 18 months).

### Phase 2: Core Algorithm
1. Match internal jobs to market benchmarks by content, level, and scope
2. Age survey data to current date: apply projected market movement rate
3. Compute compa-ratio per employee: actual base / market P50
4. Compute percentile positioning: where does actual pay fall in market distribution
5. Analyze: by department, level, tenure, demographics for equity gaps

### Phase 3: Verification
Check: compa-ratios cluster around 0.85-1.15 (normal range). Flag outliers (< 0.80 underpaid, > 1.20 overpaid). Test demographic equity.
**Gate:** Distribution reasonable, equity analysis completed.

### Phase 4: Output
Return benchmarking results with band recommendations.

## Output Format

```json
{
  "summary": {"avg_compa_ratio": 0.97, "below_band_pct": 12, "above_band_pct": 8},
  "by_role": [{"role": "Software Engineer", "market_p50": 1800000, "avg_actual": 1750000, "compa_ratio": 0.97}],
  "equity_flags": [{"dimension": "gender", "gap_pct": 3.2, "statistically_significant": true}],
  "metadata": {"employees": 500, "survey_source": "Mercer", "survey_date": "2025-H2"}
}
```

## Examples

### Sample I/O
**Input:** 50 engineers, market P50=NT$1.8M, actual range NT$1.5M-2.1M
**Expected:** Avg compa-ratio ~0.97, some below-band employees flagged for adjustment.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Hot market (tech boom) | Market data rapidly outdated | Apply higher aging factor |
| Remote work mixed | Location-adjusted bands needed | SF vs Taipei market rates differ 2-3x |
| Small company, no survey match | Use broader industry proxies | Imperfect but better than nothing |

## Gotchas

- **Total compensation**: Base salary benchmarking alone misses equity, bonuses, and benefits. Compare total comp for accurate positioning.
- **Survey data lag**: Published surveys reflect data collected 6-18 months ago. In fast-moving markets, age the data forward.
- **Internal equity vs external competitiveness**: Aligning with market may create internal inequities (new hire paid more than tenured employee). Balance both.
- **Geographic differentials**: Remote work complicates location-based pay. Define a clear policy: pay by HQ location, employee location, or hybrid.
- **Pay equity legal risk**: Unexplained demographic pay gaps expose legal liability. Conduct regression-based equity analysis controlling for legitimate factors (experience, performance, level).

## References

- For salary band design methodology, see `references/band-design.md`
- For pay equity regression analysis, see `references/pay-equity.md`
