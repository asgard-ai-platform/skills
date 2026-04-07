---
name: "algo-mfg-fmea"
description: "Conduct FMEA to systematically identify, prioritize, and mitigate potential failure modes. Use this skill when the user needs to assess product or process risks, prioritize corrective actions, or build a risk register — even if they say 'failure mode analysis', 'risk assessment', 'what could go wrong', or 'RPN calculation'."
metadata:
  category: "WP-48 製造演算法"
  tags: ["manufacturing", "fmea", "risk-analysis", "quality"]
---

# FMEA (Failure Mode and Effects Analysis)

## Overview

FMEA systematically identifies potential failure modes, their effects, causes, and current controls. Each failure is scored on Severity (S), Occurrence (O), and Detection (D) on 1-10 scales. RPN = S × O × D prioritizes which risks to address first. AIAG-VDA FMEA (2019) replaces RPN with Action Priority (AP) matrix.

## When to Use

**Trigger conditions:**
- Designing new products/processes and identifying risks proactively
- Systematically evaluating existing failure modes for prioritization
- Meeting automotive (IATF 16949) or medical device (ISO 13485) quality requirements

**When NOT to use:**
- For root cause analysis of a known problem (use fishbone/5-why)
- For statistical analysis of defect data (use SPC or Pareto)

## Algorithm

```
IRON LAW: Severity Can NEVER Be Reduced by Design Changes
Severity is determined by the EFFECT on the customer. A brake failure
is always severity 10, regardless of how unlikely or detectable it is.
FMEA reduces risk by: lowering Occurrence (better design/process) or
improving Detection (better testing/inspection). NEVER inflate
Detection scores to lower RPN artificially.
```

### Phase 1: Input Validation
Define scope: Design FMEA (DFMEA) or Process FMEA (PFMEA). Assemble cross-functional team. Prepare: process flow diagram or system block diagram.
**Gate:** Scope defined, team assembled, reference diagrams available.

### Phase 2: Core Algorithm
1. List all potential failure modes for each function/process step
2. For each failure mode, identify: effect on customer, root cause(s), current prevention controls, current detection controls
3. Score: Severity (1-10), Occurrence (1-10), Detection (1-10)
4. **Classic RPN:** RPN = S × O × D. Prioritize high RPNs.
5. **AIAG-VDA AP:** Use the S-O-D combination matrix to assign Action Priority: High, Medium, Low.
6. Define recommended actions for High-priority items with responsibility and target dates

### Phase 3: Verification
Review: are all functions/steps covered? Do severity scores match actual customer impact? Are detection scores realistic (not overly optimistic)?
**Gate:** Complete coverage, realistic scoring, actions assigned for high-priority items.

### Phase 4: Output
Return FMEA register with prioritized actions.

## Output Format

```json
{
  "fmea_items": [{"failure_mode": "seal leak", "effect": "water damage", "cause": "material degradation", "severity": 8, "occurrence": 4, "detection": 6, "rpn": 192, "ap": "high", "action": "add pressure test at final inspection"}],
  "summary": {"total_modes": 45, "high_priority": 8, "medium": 15, "low": 22},
  "metadata": {"type": "PFMEA", "scope": "assembly line 3"}
}
```

## Examples

### Sample I/O
**Input:** Coffee machine brewing module, function: "heat water to 93°C"
**Expected:** Failure modes: overheating (S=7, O=3, D=4, RPN=84), under-heating (S=5, O=4, D=3, RPN=60), no heating (S=8, O=2, D=2, RPN=32).

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| S=10, any O and D | Always high priority | Safety-critical failures require action regardless of RPN |
| RPN=100 (S=10,O=1,D=10) vs (S=1,O=10,D=10) | Same RPN, very different risk | This is why AIAG-VDA AP replaces pure RPN |
| No current controls | D=10 (no detection) | Honest assessment drives improvement |

## Gotchas

- **RPN is misleading**: RPN=100 from S=10,O=1,D=10 (catastrophic but rare, undetectable) is very different from S=1,O=10,D=10 (trivial but frequent). AIAG-VDA AP matrix addresses this flaw.
- **Scoring consistency**: Without calibration, different team members score differently. Use scoring rubrics with examples and calibrate as a team.
- **Detection ≠ prevention**: A low Detection score (good detection) doesn't prevent the failure — it only catches it. Prioritize Occurrence reduction over Detection improvement.
- **Living document**: FMEA must be updated when design/process changes, new failure data appears, or corrective actions are implemented. A static FMEA provides diminishing value.
- **Scope creep**: An FMEA that tries to cover everything becomes unmanageable. Focus on the critical functions or highest-risk areas first.

## References

- For AIAG-VDA AP matrix and scoring tables, see `references/aiag-vda-ap.md`
- For S/O/D scoring rubrics, see `references/scoring-rubrics.md`
