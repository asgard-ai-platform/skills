#!/usr/bin/env python3
"""Eval runner — strict eval of Tier 1+2 scripts via headless `claude` CLI.

For each scenario in a case YAML, spawns two subagents:
  - with_skill:    full SKILL.md methodology + Bash+Read (script executable)
  - without_skill: vanilla LLM, no methodology, no tools — baseline

Both arms are given the same prompt + the methodology section of the
skill's SKILL.md. Only the script execution capability differs.

Outputs are written to eval/results/<skill>__<scenario>__<arm>__<ts>.json.

Usage:
    python3 eval/runner.py --case eval/cases/biz-dcf.yaml
    python3 eval/runner.py --all
    python3 eval/runner.py --report
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import time
from pathlib import Path

EVAL_ROOT = Path(__file__).parent
REPO_ROOT = EVAL_ROOT.parent
CASES_DIR = EVAL_ROOT / "cases"
RESULTS_DIR = EVAL_ROOT / "results"

MODEL = "claude-sonnet-4-6"

# Skill-ablation eval:
#   with_skill    — full SKILL.md methodology in prompt, Bash+Read, --add-dir repo
#                   (agent can execute the bundled script and read examples/references)
#   without_skill — NO methodology, no tools, no repo access
#                   (vanilla LLM on the raw user question — baseline)
ARMS = ("with_skill", "without_skill")

ARM_TOOLS = {
    "with_skill": "Bash,Read",
    "without_skill": "",  # empty string disables all tools
}

ARM_TIMEOUT = {
    "with_skill": 180,
    "without_skill": 720,
}

ARM_INCLUDE_METHODOLOGY = {
    "with_skill": True,
    "without_skill": False,
}

ARM_ADD_DIR = {
    "with_skill": True,
    "without_skill": False,
}


def load_case(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def skill_methodology(skill: str) -> str:
    """Extract the SKILL.md body (sans frontmatter) so both arms see methodology."""
    skill_md = REPO_ROOT / skill / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    # Strip frontmatter
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :].lstrip("\n")
    return text


def build_prompt(case: dict, scenario: dict, arm: str) -> str:
    # Build the output JSON template from expected keys so the agent uses
    # exact key names the scorer expects.
    expected = scenario["expected"]
    template_pairs = []
    for k, v in expected.items():
        if isinstance(v, (int, float)):
            template_pairs.append(f'"{k}": <number>')
        elif isinstance(v, str):
            template_pairs.append(f'"{k}": "<text or null>"')
        else:
            template_pairs.append(f'"{k}": null')
    template = "{" + ", ".join(template_pairs) + "}"

    user_question = scenario["prompt"]
    output_block = f"""## Required output

Show your reasoning, then on the LAST line of your response output a single JSON
object with EXACTLY these keys (do not rename, do not nest, do not add extra keys):

  {template}

Use null for any field you cannot compute. The keys above are required and must
match character-for-character."""

    if ARM_INCLUDE_METHODOLOGY[arm]:
        methodology = skill_methodology(case["skill"])
        script_hint = (
            f"\n\nYou have access to the bundled calculator at "
            f"`{case['script_cmd']}` via Bash. Prefer running it over hand computation."
        )
        return f"""You are answering a user question. You have access to the `{case['skill']}` skill.

## Skill methodology (from SKILL.md)

{methodology}
{script_hint}

---

## User question

{user_question}

{output_block}"""
    else:
        # Baseline: vanilla LLM, no skill, no tools.
        return f"""Answer the following user question using your own knowledge. You have no
tools and no reference material — just your training.

## User question

{user_question}

{output_block}"""


def _is_transient_failure(result: dict) -> bool:
    """Detect Anthropic 5xx / overload / transient timeouts worth retrying."""
    if result["returncode"] == -1:  # timeout
        return True
    out = result.get("stdout", "")
    markers = (
        "overloaded_error",
        "Overloaded",
        "api_error",
        "Internal server error",
        '"status":5',
        "API Error: 5",
    )
    return any(m in out for m in markers)


def run_arm(case: dict, scenario: dict, arm: str, max_retries: int = 2) -> dict:
    prompt = build_prompt(case, scenario, arm)
    timeout_sec = ARM_TIMEOUT[arm]
    cmd = [
        "claude",
        "-p",
        prompt,
        "--model",
        MODEL,
        "--output-format",
        "json",
        "--no-session-persistence",
        "--tools",
        ARM_TOOLS[arm] or '""',
    ]
    if ARM_ADD_DIR[arm]:
        cmd.extend(["--add-dir", str(REPO_ROOT)])

    attempt = 0
    while True:
        attempt += 1
        started = time.time()
        try:
            proc = subprocess.run(
                cmd,
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                timeout=timeout_sec,
            )
            elapsed = round(time.time() - started, 2)
            result = {
                "arm": arm,
                "elapsed_sec": elapsed,
                "returncode": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "attempts": attempt,
            }
        except subprocess.TimeoutExpired:
            result = {
                "arm": arm,
                "elapsed_sec": timeout_sec,
                "returncode": -1,
                "stdout": "",
                "stderr": f"TIMEOUT after {timeout_sec}s",
                "attempts": attempt,
            }

        if not _is_transient_failure(result) or attempt > max_retries:
            return result

        backoff = 15 * attempt
        sys.stderr.write(f"(transient failure, retry {attempt}/{max_retries} in {backoff}s) ")
        sys.stderr.flush()
        time.sleep(backoff)


def extract_response_text(stdout: str) -> str:
    """Pull the model's prose response from the CLI envelope."""
    try:
        envelope = json.loads(stdout)
        return envelope.get("result") or envelope.get("response") or ""
    except json.JSONDecodeError:
        return stdout


def extract_final_json(text: str) -> dict | None:
    """Pull the last JSON object from a text response."""
    depth = 0
    end = -1
    for i in range(len(text) - 1, -1, -1):
        c = text[i]
        if c == "}":
            if depth == 0:
                end = i
            depth += 1
        elif c == "{":
            depth -= 1
            if depth == 0 and end != -1:
                try:
                    return json.loads(text[i : end + 1])
                except json.JSONDecodeError:
                    end = -1
                    depth = 0
    return None


# ---------- Scoring ----------

WITHIN_PCT = 0.01  # 1% tolerance


def _within_pct(actual, expected, pct=WITHIN_PCT) -> bool:
    if actual is None or expected is None:
        return False
    try:
        if expected == 0:
            return abs(actual) <= pct
        return abs(actual - expected) / abs(expected) <= pct
    except (TypeError, ValueError):
        return False


def _numeric_keys_match(parsed: dict | None, expected: dict, pct=WITHIN_PCT) -> tuple[bool, list[str]]:
    if not parsed:
        return False, ["no parsed JSON"]
    misses = []
    for k, v in expected.items():
        if not isinstance(v, (int, float)):
            continue
        a = parsed.get(k)
        if not _within_pct(a, v, pct):
            misses.append(f"{k}: got {a!r} expected {v}")
    return (len(misses) == 0), misses


def score_arm(scenario: dict, arm_result: dict) -> dict:
    rubric = scenario.get("rubric", "within_1_percent")
    expected = scenario["expected"]
    parsed = arm_result.get("parsed")
    text = arm_result.get("response_text", "") or ""
    text_lower = text.lower()

    if rubric in ("within_1_percent", "within_1_percent_AND_units_consistent"):
        ok, misses = _numeric_keys_match(parsed, expected)
        return {"verdict": "pass" if ok else "fail", "notes": misses}

    if rubric == "judge_flagged_assumption":
        ok, misses = _numeric_keys_match(parsed, expected)
        flag_phrase = expected.get("must_flag", "").lower()
        flagged = bool(flag_phrase) and any(
            kw in text_lower for kw in (flag_phrase, "convention", "mid-year", "assumption")
        )
        if ok and flagged:
            return {"verdict": "pass", "notes": []}
        if ok and not flagged:
            return {"verdict": "partial", "notes": ["numbers correct but assumption not flagged"]}
        return {"verdict": "fail", "notes": misses + (["flag missing"] if not flagged else [])}

    if rubric == "must_raise_or_refuse":
        err_phrase = expected.get("error", "").lower()
        en_kw = ["error", "cannot", "diverge", "must be greater", "invalid",
                 "refuse", "undefined", "infinity", "divide by zero"]
        zh_kw = ["除以零", "無窮", "无穷", "無解", "无解", "無法計算", "无法计算",
                 "違反", "违反", "不成立", "未定義", "未定义"]
        keywords = en_kw + zh_kw
        if err_phrase:
            keywords.append(err_phrase[:20])
        raised = any(kw in text_lower for kw in keywords)
        # Fallback: parsed all-null + mentions wacc/growth/terminal counts as a refusal.
        if not raised and parsed and all(v is None for v in parsed.values()):
            if any(kw in text_lower for kw in ("wacc", "growth", "terminal", "終值", "终值")):
                raised = True
        return {
            "verdict": "pass" if raised else "fail",
            "notes": [] if raised else ["did not raise/refuse"],
        }

    return {"verdict": "unknown", "notes": [f"unknown rubric: {rubric}"]}


SPEED_RATIO_THRESHOLD = 3.0  # without_skill/with_skill ratio considered a "speed win"


def _classify_scenario(s: dict) -> str:
    """Per-scenario value class: correctness / speed / both / neither.

    correctness: with_skill passed AND without_skill failed
    speed:       both passed AND without_skill took >= 3x longer
    both:        correctness AND speed
    neither:     both passed at similar speed (script adds no measurable value)
    inconclusive: with_skill failed (script itself broken — needs investigation)
    """
    ws = s["arms"]["with_skill"]
    wo = s["arms"]["without_skill"]
    ws_v = ws["score"]["verdict"]
    wo_v = wo["score"]["verdict"]
    if ws_v != "pass":
        return "inconclusive"
    correctness_win = wo_v != "pass"
    ws_t = max(ws["elapsed_sec"], 0.1)
    wo_t = wo["elapsed_sec"]
    speed_win = wo_t / ws_t >= SPEED_RATIO_THRESHOLD
    if correctness_win and speed_win:
        return "both"
    if correctness_win:
        return "correctness"
    if speed_win:
        return "speed"
    return "neither"


def _print_summary(record: dict) -> None:
    sys.stderr.write(f"\n  --- summary: {record['skill']} ---\n")
    header = f"  {'scenario':<32} {'with':<10} {'without':<10} {'ratio':>6} {'value':<12}\n"
    sys.stderr.write(header)
    classes = []
    for s in record["scenarios"]:
        ws = s["arms"]["with_skill"]
        wo = s["arms"]["without_skill"]
        ws_v = ws["score"]["verdict"]
        wo_v = wo["score"]["verdict"]
        ratio = wo["elapsed_sec"] / max(ws["elapsed_sec"], 0.1)
        cls = _classify_scenario(s)
        s["value_class"] = cls
        classes.append(cls)
        sys.stderr.write(
            f"  {s['id'][:32]:<32} {ws_v:<10} {wo_v:<10} {ratio:>5.1f}x {cls:<12}\n"
        )
    # Case-level rollup: pick the strongest signal
    rollup = (
        "both" if "both" in classes
        else "correctness" if "correctness" in classes
        else "speed" if "speed" in classes
        else "neither" if all(c == "neither" for c in classes)
        else "mixed"
    )
    record["case_verdict"] = rollup
    sys.stderr.write(f"  → case verdict: {rollup}\n\n")


def run_case(case_path: Path) -> Path:
    case_path = case_path.resolve()
    case = load_case(case_path)
    skill = case["skill"]
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = RESULTS_DIR / f"{skill}__{ts}.json"

    record: dict = {
        "skill": skill,
        "case_file": str(case_path.relative_to(REPO_ROOT)),
        "model": MODEL,
        "started": ts,
        "scenarios": [],
    }

    for scenario in case["scenarios"]:
        sid = scenario["id"]
        sys.stderr.write(f"  scenario: {sid}\n")
        scenario_record = {
            "id": sid,
            "dimension": scenario.get("dimension"),
            "expected": scenario["expected"],
            "rubric": scenario.get("rubric"),
            "arms": {},
        }
        for arm in ("with_skill", "without_skill"):
            sys.stderr.write(f"    arm: {arm} ... ")
            sys.stderr.flush()
            result = run_arm(case, scenario, arm)
            result["response_text"] = extract_response_text(result["stdout"])
            result["parsed"] = extract_final_json(result["response_text"])
            result["score"] = score_arm(scenario, result)
            scenario_record["arms"][arm] = result
            sys.stderr.write(
                f"{result['elapsed_sec']}s rc={result['returncode']} "
                f"verdict={result['score']['verdict']}\n"
            )
        record["scenarios"].append(scenario_record)

    _print_summary(record)

    out_path.write_text(json.dumps(record, indent=2, ensure_ascii=False))
    sys.stderr.write(f"  wrote {out_path.relative_to(REPO_ROOT)}\n")
    return out_path


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--case", type=Path, help="Run a single case JSON")
    p.add_argument("--all", action="store_true", help="Run every case in cases/")
    p.add_argument("--report", action="store_true", help="Aggregate results (TODO)")
    args = p.parse_args()

    RESULTS_DIR.mkdir(exist_ok=True)

    if args.case:
        sys.stderr.write(f"running {args.case.name}\n")
        run_case(args.case)
        return 0

    if args.all:
        for path in sorted(CASES_DIR.glob("*.json")):
            sys.stderr.write(f"running {path.name}\n")
            run_case(path)
        return 0

    if args.report:
        sys.stderr.write("--report not yet implemented\n")
        return 1

    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
