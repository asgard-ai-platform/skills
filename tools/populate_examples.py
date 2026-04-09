#!/usr/bin/env python3
"""Populate examples/ for each skill that lacks them.

For each skill directory containing a SKILL.md, creates one concrete
example file if none exists yet:

  - Skills WITH scripts → examples/sample_input.json
    (JSON payload that can be fed to the script's --input flag)
  - Skills WITHOUT scripts → examples/sample_scenario.md
    (a concrete scenario + expected analysis output)

Usage:
    python3 tools/populate_examples.py --scan          # list skills needing examples
    python3 tools/populate_examples.py --pilot 5       # write first 5
    python3 tools/populate_examples.py --skill biz-dcf # write examples for one skill
    python3 tools/populate_examples.py --all            # full run
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODEL = "claude-sonnet-4-6"
PER_FILE_TIMEOUT = 300


def find_skills_needing_examples() -> list[Path]:
    """Return skill dirs that have SKILL.md but no files in examples/."""
    needs: list[Path] = []
    for skill_md in sorted(REPO_ROOT.glob("*/SKILL.md")):
        skill_dir = skill_md.parent
        ex_dir = skill_dir / "examples"
        if ex_dir.exists():
            real_files = [f for f in ex_dir.iterdir()
                          if f.name not in (".gitignore", ".gitkeep")]
            if real_files:
                continue
        needs.append(skill_dir)
    return needs


def has_script(skill_dir: Path) -> bool:
    scripts_dir = skill_dir / "scripts"
    return scripts_dir.exists() and any(scripts_dir.glob("*.py"))


def build_prompt(skill_dir: Path) -> str:
    skill_md_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    skill_name = skill_dir.name
    is_scripted = has_script(skill_dir)

    if is_scripted:
        script_files = list((skill_dir / "scripts").glob("*.py"))
        script_name = script_files[0].name if script_files else "script.py"
        return f"""You are creating a sample input file for a Claude Agent Skill's
bundled Python script.

## Context: the skill

Skill: `{skill_name}`

```markdown
{skill_md_text}
```

## Your task

Write a realistic `sample_input.json` that can be fed to the script:
  `python {skill_name}/scripts/{script_name} --input examples/sample_input.json`

## Requirements

1. Use realistic, plausible values (not lorem-ipsum or obviously fake data).
2. Include enough data points to exercise the script meaningfully
   (e.g., 10-20 rows for tabular data, 3-5 items for ranking, etc.).
3. Match the exact JSON schema the script expects (check --help output
   in SKILL.md for the input format).
4. Include a brief `"_comment"` key explaining what this example tests.
5. Output ONLY the JSON. No preamble, no code fences, no explanation.
"""
    else:
        return f"""You are creating a sample scenario file for a Claude Agent Skill.

## Context: the skill

Skill: `{skill_name}`

```markdown
{skill_md_text}
```

## Your task

Write `sample_scenario.md` — a concrete, worked example showing this
skill applied to a realistic situation.

## Requirements

1. **Structure**: Start with `# Example: {{short title}}`, then
   `## Scenario` (the user's situation/question), then
   `## Analysis` (the skill applied step by step), then
   `## Result` (the output/recommendation).
2. **Realistic**: Use plausible company names, numbers, dates, and
   domain context. Not a textbook exercise — a case a real user
   would bring.
3. **Concrete**: Show actual numbers, actual frameworks applied,
   actual outputs — not "apply step 1, then step 2" generically.
4. **Concise**: 100-300 lines of markdown. One scenario, fully worked.
5. **Consistent with SKILL.md**: use the same terminology, frameworks,
   and output format as the parent skill.
6. Output ONLY the markdown content. No preamble.
"""


def write_one(skill_dir: Path) -> tuple[bool, str]:
    ex_dir = skill_dir / "examples"
    target = ex_dir / ("sample_input.json" if has_script(skill_dir) else "sample_scenario.md")
    if target.exists():
        return True, "skip (exists)"
    ex_dir.mkdir(parents=True, exist_ok=True)

    prompt = build_prompt(skill_dir)
    cmd = [
        "claude", "-p", prompt,
        "--model", MODEL,
        "--output-format", "text",
        "--no-session-persistence",
        "--tools", "",
    ]
    try:
        proc = subprocess.run(
            cmd, cwd=REPO_ROOT, capture_output=True, text=True,
            timeout=PER_FILE_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return False, f"timeout after {PER_FILE_TIMEOUT}s"

    if proc.returncode != 0:
        return False, f"rc={proc.returncode} stderr={proc.stderr[:200]}"

    content = proc.stdout.strip()
    # Strip code fences if model wrapped
    if content.startswith("```"):
        first_nl = content.index("\n") if "\n" in content else len(content)
        content = content[first_nl + 1:]
        if content.endswith("```"):
            content = content[:-3].rstrip()

    if len(content) < 100:
        return False, f"too short ({len(content)} chars)"

    # Validate JSON for script-based skills
    if target.suffix == ".json":
        try:
            json.loads(content)
        except json.JSONDecodeError as e:
            return False, f"invalid JSON: {e}"

    target.write_text(content.rstrip() + "\n", encoding="utf-8")
    return True, f"wrote {len(content)} chars → {target.name}"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--scan", action="store_true")
    g.add_argument("--pilot", type=int, metavar="N")
    g.add_argument("--skill", metavar="NAME")
    g.add_argument("--all", action="store_true")
    args = p.parse_args()

    needs = find_skills_needing_examples()
    if args.skill:
        needs = [d for d in needs if d.name == args.skill]
    sys.stderr.write(f"skills needing examples: {len(needs)}\n")

    if args.scan:
        for d in needs:
            scripted = "script" if has_script(d) else "scenario"
            print(f"{d.name} ({scripted})")
        return 0

    if args.pilot:
        needs = needs[: args.pilot]

    total = len(needs)
    wrote = skipped = failed = 0
    started = time.time()
    for i, skill_dir in enumerate(needs, 1):
        label = skill_dir.name
        sys.stderr.write(f"[{i}/{total}] {label} ... ")
        sys.stderr.flush()
        ok, msg = write_one(skill_dir)
        if ok and "skip" in msg:
            skipped += 1
        elif ok:
            wrote += 1
        else:
            failed += 1
        sys.stderr.write(f"{msg}\n")

    elapsed = int(time.time() - started)
    sys.stderr.write(
        f"\ndone in {elapsed}s  wrote={wrote}  skipped={skipped}  failed={failed}\n"
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
