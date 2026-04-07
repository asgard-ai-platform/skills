# Asgard Skills — Repository Context

This repository is the **raw ingredient pantry** for Asgard AI Platform plugins: 263 coding agent skills organized by topic prefix.

## Repository Purpose

- **NOT** a plugin: this repo holds raw skill files; plugins are assembled elsewhere by combining curated skills + MCPs
- **NOT** a template: see [`skill-template`](https://github.com/asgard-ai-platform/skill-template) for the plugin scaffolding
- **IS** a versioned library of methodology + judgment + gotchas, packaged as Claude Agent Skills

## Skill Anatomy

Every skill is a directory at the repo root, named `{category}-{slug}`, containing:

```
{category}-{slug}/
├── SKILL.md           ← REQUIRED: frontmatter + methodology body
├── examples/          ← REQUIRED: directory must exist (uses .gitignore trick for empty dirs)
├── references/        ← REQUIRED: directory must exist; populated when SKILL.md offloads heavy content
└── scripts/           ← OPTIONAL: only present when the skill has executable scripts
```

## Naming Convention

Skills use **topic-based prefixes** (no `skill-` prefix). The 21 categories:

```
grad-      Graduate-level theoretical models
algo-      Algorithms
biz-       Business school frameworks
hum-       Humanities / critical reasoning
tw-        Taiwan-specific knowledge
ecom-      E-commerce practical
econ-      Economics fundamentals
meta-      Interdisciplinary mental models
ops-       Business operations
law-       Legal frameworks
pr-        PR & brand communications
cs-        Customer service
data-      Data analytics
mfg-       Manufacturing
mkt-       Digital marketing
soc-       Social science
stat-      Statistical methodology
tech-      General tech (API, prompt eng, MCP)
ux-        Design / UX methodology
fin-       Finance practical
xborder-   Cross-border commerce
```

The `{{SKILL_NAME}}/` directory is a template skeleton — leave it untouched.

## SKILL.md Rules

1. **Frontmatter** (`name`, `description` required; `metadata` optional)
2. **Description**: WHAT + WHEN, imperative tone, < 1024 chars, no XML angle brackets, includes trigger phrases
3. **Body**: < 500 lines / < 5,000 tokens — offload heavy content to `references/`
4. **IRON LAW block**: every skill must declare one non-obvious constraint
5. **Output Format**: a Markdown or JSON template the agent should follow
6. **Gotchas**: 5-6 specific, actionable pitfalls (not generic advice)
7. **Skill name must not contain**: `claude` or `anthropic` (reserved)

## Design Patterns by Section

| Section | Primary patterns |
|---------|-----------------|
| Industry skills (ecom, mkt, mfg, ops, ...) | Phase-Gate, Hub-and-Spoke |
| Methodology (biz, hum, soc, econ, meta, law, ux, stat) | Concrete Verification, Iron Law |
| Graduate theory (grad-) | Hub-and-Spoke (HEAVY), assumptions as Iron Law |
| Algorithms (algo-) | Phase-Gate, Concrete Verification, complexity as Iron Law |

## Scripts (Deterministic Calculators)

20 skills ship pure-stdlib Python scripts. Standards:

- Single file in `{skill}/scripts/`
- `--help`, `--input <json>`, `--verify` (self-test) flags
- Outputs JSON to stdout
- Pure stdlib (no numpy/scipy/etc. unless documented)
- Errors as JSON to stderr
- Built-in `verify()` function with assertions on known input/output pairs

When adding a new script:
1. Implement `compute()` with type-checked inputs
2. Implement `verify()` with at least 3 assertions covering happy path, edge case, and error case
3. Wire up `main()` with `argparse`
4. Update the SKILL.md `## Scripts` section with usage example

## Quality Audit Anti-Patterns to Avoid

When writing or modifying a skill, watch for:

1. **Phantom Trigger** — description over-matches (e.g., "everything is connected" triggers on any vague reference)
2. **Kitchen Sink** — SKILL.md crammed with everything; should offload to `references/`
3. **Over-Teaching** — explaining basics the agent already knows (regression, p-values, prompt engineering)
4. **Missing Gotchas** — generic advice instead of specific traps the agent would fall into
5. **Procedural Straitjacket** — too rigid where judgment is needed; or too vague where precision matters
6. **Truism Iron Law** — Iron Law that any competent agent would already follow ("be specific", "look at the data first")
7. **Non-verifiable Sample I/O** — algo skills must have exact computable input → output, not approximate ranges
8. **Broken references/ pointers** — SKILL.md references files that don't exist

## Working in This Repo

- Test scripts after editing: `python <skill>/scripts/<script>.py --verify`
- Cross-skill references should use the new naming (no `skill-` prefix)
- The repository is published under MIT license; do not check in proprietary content
- See [`TODO.md`](TODO.md) for current work in progress and pending items

## See Also

- [`skill-template`](https://github.com/asgard-ai-platform/skill-template) — Plugin template repo
- [Asgard MCPs](https://github.com/orgs/asgard-ai-platform/repositories?q=mcp-) — Data-provider MCPs
- [Claude Agent Skills documentation](https://docs.claude.com/en/docs/claude-code/skills)
