#!/usr/bin/env python3
"""Eval runner — strict eval of Tier 1+2 scripts via headless `claude` CLI.

For each scenario in a case YAML, spawns two subagents:
  - with_script:    --tools "Bash,Read"  (settings.json permits Bash(python *))
  - without_script: --tools "Read"        (must compute by hand)

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
TIMEOUT_SEC = 240

ARM_TOOLS = {
    "with_script": "Bash,Read",
    "without_script": "Read",
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
    methodology = skill_methodology(case["skill"])
    arm_directive = (
        f"You MAY execute the calculator at: `{case['script_cmd']}`. "
        "Use it; do not recompute by hand."
        if arm == "with_script"
        else (
            "You MUST compute by hand. Do not run any scripts. "
            "Show your reasoning, then give the final answer."
        )
    )
    return f"""You are evaluating a financial / analytical scenario for the skill `{case['skill']}`.

## Methodology (from SKILL.md)

{methodology}

---

## Scenario

{scenario['prompt']}

## Constraints for this run

{arm_directive}

## Output

Return your final answer as a JSON object on the LAST line of your response,
matching the keys in the scenario's expected fields. Example:

  {{"enterprise_value_m": 1234.5, "equity_value_m": 1100.0, "per_share": 25.5}}

Use null for fields you cannot compute. Show reasoning above the JSON line."""


def run_arm(case: dict, scenario: dict, arm: str) -> dict:
    prompt = build_prompt(case, scenario, arm)
    cmd = [
        "claude",
        "-p",
        prompt,
        "--model",
        MODEL,
        "--output-format",
        "json",
        "--no-session-persistence",
        "--add-dir",
        str(REPO_ROOT),
        "--tools",
        ARM_TOOLS[arm],
    ]
    started = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SEC,
        )
        elapsed = round(time.time() - started, 2)
        return {
            "arm": arm,
            "elapsed_sec": elapsed,
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }
    except subprocess.TimeoutExpired:
        return {
            "arm": arm,
            "elapsed_sec": TIMEOUT_SEC,
            "returncode": -1,
            "stdout": "",
            "stderr": f"TIMEOUT after {TIMEOUT_SEC}s",
        }


def extract_final_json(stdout: str) -> dict | None:
    """Pull the last JSON object from the model's text response."""
    try:
        envelope = json.loads(stdout)
        text = envelope.get("result") or envelope.get("response") or ""
    except json.JSONDecodeError:
        text = stdout
    # Find the last {...} block
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
        for arm in ("with_script", "without_script"):
            sys.stderr.write(f"    arm: {arm} ... ")
            sys.stderr.flush()
            result = run_arm(case, scenario, arm)
            result["parsed"] = extract_final_json(result["stdout"])
            scenario_record["arms"][arm] = result
            sys.stderr.write(f"{result['elapsed_sec']}s rc={result['returncode']}\n")
        record["scenarios"].append(scenario_record)

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
