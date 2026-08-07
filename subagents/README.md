# Subagent Definitions

One file per subagent. Caller route names subagent · principal reads file · assembles scoped inputs listed · spawns generic subagent with file body as system prompt + inputs as context. Works on any platform that spawns task/subagent — no platform-specific agent registry required

## Portable format

Each definition: **Markdown with YAML frontmatter** — shape major platforms converge on (Claude Code `.claude/agents/*.md`, GitHub Copilot `.github/agents/*.agent.md`, Cursor `.cursor/agents/*.md`, OpenCode `.opencode/agents/*.md`). Only two frontmatter fields universal; only those required:

```yaml
---
name: kebab-case-identifier
description: Trigger-style sentence — what it does AND when to invoke
model_class: reasoning | standard   # advisory: capability class, never a model id
thinking: deep | brief              # advisory: deliberation the job deserves
capabilities: read-only | read-write | read-run-write   # advisory: what it may touch
---
```

`model_class`, `thinking`, `capabilities` = **advisory hints**, named to avoid platform reserved keys (platforms ignore unknown frontmatter). Describe *kind* of model and access needed — never a vendor model name. Model names change monthly; capability classes don't

- `model_class: reasoning` — critics and architects: strong model with real judgment
- `model_class: standard` — mechanical checks and packet execution: any competent coding model
- `thinking: deep` — enable extended thinking / high reasoning effort where platform supports it
- `capabilities` — caller must not grant more: `read-only` critic gets no edit or execute tools

## Installing natively (optional)

Prefer **`do/init`** — detects platform(s), asks install y/n, proposes critic/standard model tiers (optional per-agent override), writes native frontmatter per target, records `Native agents:` in Tooling. Manual copy only if skipping `do/init`. Full write rules + **Model Auto vs agent Auto**: `routes/do-init.md`

| Platform | Path | Native keys (keep `description`; `name` where applicable) |
| --- | --- | --- |
| Cursor | `.cursor/agents/{name}.md` | `model` (`inherit` only — **not** `auto`), `readonly`, `is_background` |
| Claude Code | `.claude/agents/{name}.md` | `model` (`inherit` / aliases), `tools` (comma allowlist) |
| GitHub Copilot | `.github/agents/{name}.agent.md` | omit `model` for session Auto · optional pin · `tools` (YAML array) · optional `disable-model-invocation` |
| OpenCode | `.opencode/agents/{name}.md` | `mode: subagent` · omit `model` to follow parent · `permission` map |

### Capability → tools / readonly / permission

| Portable `capabilities` | Cursor | Claude Code `tools` | Copilot `tools` | OpenCode `permission` |
| --- | --- | --- | --- | --- |
| `read-only` | `readonly: true` | `Read, Grep, Glob` | `['read', 'search', 'codebase']` | `edit: deny` · `bash: deny` · `task: deny` |
| `read-write` | `readonly: false` | `Read, Grep, Glob, Edit, Write` | `['read', 'search', 'codebase', 'edit']` | `edit: allow` · `bash: deny` · `task: deny` |
| `read-run-write` | `readonly: false` | `Read, Grep, Glob, Edit, Write, Bash` | `['read', 'search', 'codebase', 'edit', 'terminal']` | `edit: allow` · `bash: allow` · `task: deny` |

### Tiers

- **critics** (`model_class: reasoning`): `prd-critic`, `arch-critic`, `perf-critic-backend`, `perf-critic-frontend`, `ui-consistency-reviewer`
- **standard** (`model_class: standard`): `repo-scout`, `task-checker`, `feature-coder`, `doc-coherence-reviewer`

Drop `model_class` / `thinking` / `capabilities` from every native file. Never hardcode vendor model ids in portable skill files — map at install time. Never write Cursor `model: auto`. Never use Copilot `tools: ['*']` or omit tools for `read-only` agents


## Roster

| Subagent | Kind | Called by |
| --- | --- | --- |
| `repo-scout` | research | planning routes needing ground truth from code |
| `prd-critic` | reviewer | `plan/epic`, `plan/feat` |
| `arch-critic` | reviewer | `plan/epic-arch`, `plan/feat-arch` |
| `perf-critic-backend` | reviewer (conditional) | `plan/epic-arch`, `plan/feat-arch`, `do/verify` |
| `perf-critic-frontend` | reviewer (conditional) | `plan/epic-arch`, `plan/feat-arch`, `do/verify` |
| `task-checker` | reviewer | `plan/tasks` |
| `feature-coder` | executor | `do/all-tasks` (one per parallelizable task) |
| `ui-consistency-reviewer` | reviewer | `do/verify` (UI features) |
| `doc-coherence-reviewer` | reviewer | `do/verify` (epic completion), `plan/change`, `plan/migrate` |

## Rules for all subagents

- **Scoped context** (Invariant 14): caller passes exactly inputs definition lists — never "read everything". Reviewer briefs always include Product Spirit block and relevant `docs/decisions.md` lines
- **Tooling injection**: every brief includes Tooling one-liner from repo instruction file (CLI filter, LSP preference, `Subagent economy`). Subagent obeys it. Long-output Shell → use declared filter prefix
- **Return-payload cap**: scout ≤15 lines · critics ≤25 lines · no preamble/summary · principal never pastes raw returns into docs
- **Model hints**: honor `model_class` / `thinking` — never elevate above definition; prefer cheapest capable model platform allows for `standard` + `brief`
- **Respect recorded decisions**: conflict with recorded user decision → raise as question for user, never apply as change
- **Reviewer output format**: numbered, actionable findings, ordered by severity · each states problem, why it matters, concrete suggestion. No praise, no restating document, no preamble or closing summary
- **Reviewer calibration**: flag as blocking only what would change behavior, contract, or human decision · style, verbosity, formatting = minor at most. At most 10 findings — keep most consequential
- **Convergence**: reviewer runs once per document · one scoped re-run maximum, limited to previously blocking findings · new remarks on re-run accepted only if blocking · never a third run
- **Main agent duty**: judge each finding by impact — apply if consequential, drop futile or cosmetic silently · if rejected and disagreement is genuine judgment call, surface as decision question for human. Critic exchange itself never replayed in review documents or handoffs (Invariant 16)
- **Caller duty**: run SKILL.md inline-first before spawn; for `repo-scout` prefer scout-lite when gate says inline
