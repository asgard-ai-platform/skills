#!/usr/bin/env python3
"""Populate missing references/*.md files for each skill.

Scans every SKILL.md for `references/<file>.md` pointers, checks if the
target file exists, and spawns a headless `claude -p` subprocess per
broken pointer to generate the content. Idempotent — skips files that
already exist.

Usage:
    python3 tools/populate_references.py --scan              # list broken refs
    python3 tools/populate_references.py --pilot 5           # write 5 as a test
    python3 tools/populate_references.py --skill biz-dcf     # write all refs for one skill
    python3 tools/populate_references.py --all               # full run (LONG)
    python3 tools/populate_references.py --resume            # same as --all, skip existing
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODEL = "claude-sonnet-4-6"
PER_FILE_TIMEOUT = 300  # 5 min per reference file

REF_PATTERN = re.compile(r'references/([A-Za-z0-9_\-./]+\.md)')


def find_broken_refs(skill_filter: str | None = None) -> list[tuple[Path, Path]]:
    """Return list of (skill_dir, ref_target_path) for every broken reference."""
    broken: list[tuple[Path, Path]] = []
    seen: set[Path] = set()
    for skill_md in sorted(REPO_ROOT.glob("*/SKILL.md")):
        skill_dir = skill_md.parent
        if skill_filter and skill_dir.name != skill_filter:
            continue
        text = skill_md.read_text(encoding="utf-8")
        for rel in REF_PATTERN.findall(text):
            target = skill_dir / "references" / rel
            if target in seen:
                continue
            seen.add(target)
            if not target.exists():
                broken.append((skill_dir, target))
    return broken


def build_prompt(skill_dir: Path, target: Path) -> str:
    """Build the prompt handed to the subagent for one reference file."""
    skill_md_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    ref_filename = target.name
    ref_stem = target.stem
    return f"""You are writing ONE reference document for a Claude Agent Skill.

## Context: the skill it belongs to

The skill lives in `{skill_dir.name}/` and its SKILL.md is below. Your
reference file will be cited from this SKILL.md.

```markdown
{skill_md_text}
```

## Your task

Write the content of `{skill_dir.name}/references/{ref_filename}`.

The filename `{ref_stem}` is a strong hint about the topic. Produce a
focused, concrete reference doc that expands on ONE specific aspect of the
parent skill — the aspect the filename names. Do NOT try to restate the
whole skill.

## Requirements

1. **Scope**: 200-800 lines of markdown, single topic, no tangents.
2. **Depth over breadth**: prefer one worked example, formula, or
   decision framework over a wide survey.
3. **Concrete**: include actual formulas, step-by-step procedures, worked
   numbers, code snippets, decision tables, or named frameworks — NOT
   vague "considerations" paragraphs.
4. **Self-contained**: reader opens only this file; do not require
   reading other references.
5. **Consistent with SKILL.md**: use the same terminology, variable
   names, and conventions as the parent SKILL.md. If the parent IRON
   LAW applies, reinforce it rather than contradicting it.
6. **No fluff**: no "Introduction" or "Conclusion" headings with
   pleasantries. No "Table of Contents". No marketing language.
7. **Honest about uncertainty**: if a topic has multiple valid schools
   of thought, say so. If you don't have strong material, write less
   rather than inventing content.
8. **Traditional Chinese is fine** if the parent SKILL.md is in Chinese
   or mixed; otherwise English.

## Output format

Output ONLY the markdown content of the reference file. No preamble, no
"Here is the file:", no code fences around the entire output. Start
directly with the first heading (e.g. `# {ref_stem.replace('-', ' ').title()}`).
"""


def write_one(skill_dir: Path, target: Path) -> tuple[bool, str]:
    """Spawn a subagent to generate one reference file. Returns (ok, message)."""
    if target.exists():
        return True, "skip (exists)"
    target.parent.mkdir(parents=True, exist_ok=True)

    prompt = build_prompt(skill_dir, target)
    cmd = [
        "claude",
        "-p",
        prompt,
        "--model",
        MODEL,
        "--output-format",
        "text",
        "--no-session-persistence",
        "--tools",
        "",
    ]
    try:
        proc = subprocess.run(
            cmd,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=PER_FILE_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return False, f"timeout after {PER_FILE_TIMEOUT}s"

    if proc.returncode != 0:
        return False, f"rc={proc.returncode} stderr={proc.stderr[:200]}"

    content = proc.stdout.strip()
    # Strip leading code fence if the model wrapped it
    if content.startswith("```markdown"):
        content = content[len("```markdown"):].lstrip("\n")
        if content.endswith("```"):
            content = content[:-3].rstrip()
    elif content.startswith("```"):
        content = content.split("\n", 1)[1] if "\n" in content else content
        if content.endswith("```"):
            content = content[:-3].rstrip()

    if len(content) < 200:
        return False, f"too short ({len(content)} chars)"

    target.write_text(content.rstrip() + "\n", encoding="utf-8")
    return True, f"wrote {len(content)} chars"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--scan", action="store_true", help="list broken refs")
    g.add_argument("--pilot", type=int, metavar="N", help="write first N broken refs")
    g.add_argument("--skill", metavar="NAME", help="write all refs for one skill")
    g.add_argument("--all", action="store_true", help="write every broken ref")
    g.add_argument("--resume", action="store_true", help="alias for --all (idempotent)")
    args = p.parse_args()

    skill_filter = args.skill
    broken = find_broken_refs(skill_filter)
    sys.stderr.write(f"broken references: {len(broken)}\n")

    if args.scan:
        for sdir, tgt in broken:
            print(f"{sdir.name}/references/{tgt.name}")
        return 0

    if args.pilot:
        broken = broken[: args.pilot]
    # --all, --resume, --skill all proceed with the full (filtered) list

    total = len(broken)
    wrote = 0
    failed = 0
    skipped = 0
    started = time.time()
    for i, (sdir, tgt) in enumerate(broken, 1):
        label = f"{sdir.name}/references/{tgt.name}"
        sys.stderr.write(f"[{i}/{total}] {label} ... ")
        sys.stderr.flush()
        ok, msg = write_one(sdir, tgt)
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
