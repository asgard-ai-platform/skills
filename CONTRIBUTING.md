# Contributing to Asgard Skills

Thanks for contributing. This repo is a versioned library of coding-agent methodology — 263+ flat `{category}-{slug}/` skill directories at the repo root. Read [`AGENTS.md`](AGENTS.md) first; it is the source of truth for repo conventions.

## Quick start — add a new skill

1. Pick a name: `{category}-{slug}`, all lowercase, hyphen-separated. Categories are listed in `AGENTS.md`.
2. Create the directory with the required sub-structure:
   ```bash
   mkdir -p <category>-<slug>/{references,examples}
   touch <category>-<slug>/{references,examples}/.gitkeep
   ```
3. Write `<category>-<slug>/SKILL.md`. Required sections:
   - YAML frontmatter: `name`, `description`, `metadata` (with `tags`; optional `domain`, `layer`, `related_mcps`, `related_skills`, `last_verified`)
   - Body ≤ 500 lines / 5,000 tokens
   - IRON LAW block (non-obvious constraint, not a truism)
   - Output Format template
   - Gotchas section (5-6 specific, actionable pitfalls — not generic advice)
4. Offload heavy content to `references/*.md`. Put runnable samples in `examples/sample_scenario.md`.
5. If the skill fits an existing domain, update that domain's `docs/domains/*.md` index.

## Quality bar

Skills are reviewed against the 8 anti-patterns documented in `AGENTS.md` §"Quality Audit Anti-Patterns to Avoid":

1. Phantom Trigger — description over-matches
2. Kitchen Sink — body crammed with everything
3. Over-Teaching — explains basics the agent already knows
4. Missing Gotchas — generic advice, not specific traps
5. Procedural Straitjacket — too rigid where judgment is needed
6. Truism Iron Law — rule any competent agent would already follow
7. Non-verifiable Sample I/O — algo skills must have exact computable I/O
8. Broken `references/` pointers — SKILL.md references files that don't exist

If your skill fails any of these, the PR will be sent back.

## Frontmatter reference

```yaml
---
name: "category-slug"
description: "WHAT the skill does + WHEN to use it + triggering phrases. Under 1024 chars. No XML angle brackets."
metadata:
  category: "WP-XX <category label>"
  tags: ["topic", "keyword"]
  # Optional domain/layer fields, used when the skill is part of a curated domain:
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: ["mcp-shopline"]
  related_skills: ["other-skill-name"]
  last_verified: "2026-04"
---
```

Reserved — do NOT use in skill names: `claude`, `anthropic`.

Not a repo convention — do NOT add: per-skill `license:` field (repo-wide MIT applies).

## Skeletons

A skeleton is a frontmatter + "When to use" only SKILL.md, with `status: skeleton` in the metadata. Skeletons exist to reserve a slot in a domain while content is pending. They must include:

- A `> **STATUS: SKELETON** — body pending.` banner at the top of the body
- Recommendation to the agent to prefer a named alternative (usually the nearest complete reference skill)
- `TODO` placeholder sections (not deleted — the structure stays so the filler knows what to write)

Skeletons are acceptable in a PR if they belong to an approved domain roadmap. Otherwise, ship content-complete skills only.

## Deterministic scripts

If a skill ships a calculator script, follow `AGENTS.md` §"Scripts":

- Single file in `<skill>/scripts/`
- `--help`, `--input <json>`, `--verify` flags
- Pure stdlib unless documented
- Built-in `verify()` with ≥ 3 assertions

Test: `python <skill>/scripts/<script>.py --verify`

## Domain docs

A domain (e.g., `docs/domains/tw-ecommerce.md`) is a **navigation hub**, not a skill. It indexes new + existing skills that apply to a workflow. When you add a skill that belongs to an existing domain, update the index in the same PR.

## Pull requests

- Branch from `main`.
- One coherent change per PR — either one content-complete skill, or one domain bootstrap (infra + skeletons + a couple of reference skills), not a grab-bag.
- Commit messages: `<type>(<scope>): <subject>`. Types: `feat`, `docs`, `fix`, `chore`. Scope examples: `tw-ecom`, `algo-ecom`, `repo`.
- Reference the design spec in `docs/superpowers/specs/` if the PR implements one.
- Run the verification commands listed in the plan (frontmatter parse, description length, line count) before pushing.

## Getting help

Open an issue with `question` label, or reference the design spec for the domain you're working in.
