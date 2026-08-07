# do/init — Token-Saving Tooling Setup

**Purpose**: set up, once per project, tooling that reduces token consumption on every later route. Idempotent — re-running reports what exists and recommends only what is missing

**Mindset**: pragmatic toolsmith — recommend only what this project will actually use; never install without user confirmation

**Inputs**: repository tree (languages, build/test commands) · repository instruction file(s) (SKILL.md → Platform integration) · environment's plugin/LSP capabilities · `subagents/*.md` portable defs

**Outputs**: user-approved tooling installed/configured · optional native agent files · short **Tooling** section in repository instruction file

## Steps

1. Detect project's languages and commands producing long outputs (tests, builds, linters, package managers)
2. **LSP** — check language server per detected language (e.g. Claude Code plugins `pyright-lsp`, `typescript-lsp`, `rust-analyzer`); recommend missing ones
3. **CLI output filters** — recommend compression proxy for long-output commands: `rtk` (Rust, zero config) or `snip` (Go, YAML filters), with prefix convention (e.g. `rtk git diff`)
4. **Code graph / semantic index** — large codebases only, if environment supports MCP; skip for small repositories (inline-first / Cost gate)
5. **Subagent economy profile** — present `strict` | `balanced` | `quality` (SKILL.md → Economy profile); recommend `strict` when token cost dominates, `balanced` as default, `quality` only if user prioritizes isolated review over tokens. Record chosen value
6. **Native agents (optional)** — see section below; skip entirely if user declines
7. Present recommendations one line each with expected saving; install only what user approves
8. Record adopted tooling in repository instruction file — one short **Tooling** section: active LSPs · filter prefix and target commands · index/graph tool if any · `Subagent economy: {strict|balanced|quality}` · if native agents installed: one line per platform, e.g. `Native agents (cursor): .cursor/agents (9) · critics=inherit · standard=inherit` · `Native agents (claude): …` · `Native agents (copilot): …` · `Native agents (opencode): …`. Every route and every subagent brief reads this file
9. Handoff: resume interrupted route, or `plan/proj` for fresh project

## Native agents install / sync

Do **not** block other steps if skipped. Portable skill files stay untouched — never write platform-only keys into `subagents/*.md`

### Detect platform

Offer every target that applies (user may pick more than one):

| Signal | Target path pattern |
| ------ | ------------------- |
| `.cursor/` present, or user on Cursor | `.cursor/agents/{name}.md` |
| `.claude/` present, or user on Claude Code | `.claude/agents/{name}.md` |
| `.github/` present, or user on GitHub Copilot | `.github/agents/{name}.agent.md` |
| `.opencode/` present, or user on OpenCode | `.opencode/agents/{name}.md` |
| None of the above | ask which platform(s), or skip |

### Ask (blocking — wait for answers)

1. Install/sync native agents from skill `subagents/*.md`? **y/n** (idempotent: if target dir exists, report count + offer refresh)
2. If **n** → skip rest of this section
3. Which platform(s)? (only those detected / user-confirmed)
4. Propose **tier defaults** (one question per platform if model vocab differs — not nine agents):
   - **critics** (`model_class: reasoning`): default platform "follow session" (see Model Auto below) — `prd-critic`, `arch-critic`, `perf-critic-*`, `ui-consistency-reviewer`
   - **standard** (`model_class: standard`): same default — `repo-scout`, `task-checker`, `feature-coder`, `doc-coherence-reviewer`
5. Optional: "Customize per agent?" **y/n** — only if **y**, list roster; user may set model per file. Accept only values allowed for that platform (below) — never invent ids
6. Confirm write path(s) and proceed

### Model Auto vs agent Auto (important)

UI **"Auto"** (Cursor / Copilot chat model picker) is **not** the same as a frontmatter string `auto`:

| Meaning | Cursor | GitHub Copilot | Claude Code | OpenCode |
| ------- | ------ | -------------- | ----------- | -------- |
| **Model Auto** — platform picks / follows session model | **Do not** write `model: auto` (undocumented; may fail to load). Use `model: inherit` or **omit** `model` (defaults to inherit) | **Omit** `model` → inherits session/default model (closest to Auto). Do not invent `auto` unless user confirms their Copilot build accepts it | `model: inherit` or omit | **Omit** `model` → subagent uses invoking parent's model |
| **Agent Auto** — platform may auto-delegate to this agent | Driven by strong `description` + Task routing — no frontmatter flag | Leave `infer` unset/`true` (default). Set `disable-model-invocation: true` only if user wants **manual-only** selection | Driven by `description` | Driven by `description` + `mode: subagent` |

**Recommendation for tiers**: default = follow session (`inherit` / omit). Pin a specific model only when user names a picker id. Never write literal `auto` into Cursor agent files

### Shared write invariants (all platforms)

For each `subagents/{name}.md` except `README.md`:

1. Keep Markdown **body** as-is (system prompt)
2. Keep portable `name` + `description` as the native identity/description (OpenCode: filename = id; still set `description`)
3. Drop portable-only keys: `model_class`, `thinking`, `capabilities` — never copy them into native files
4. `model` = tier default or per-agent override from Ask steps (or omit where platform default = follow session)
5. Overwrite existing same-name roster files on refresh; never delete user-added agents outside the roster
6. Create target directory if missing (after user confirmed that platform)

### Write rules (Cursor) → `.cursor/agents/{name}.md`

Frontmatter **only**:

```yaml
---
name: {name}
description: {description}
model: inherit
readonly: {true|false}
is_background: false
---
```

Map:

| Portable | Cursor |
| -------- | ------ |
| `capabilities: read-only` | `readonly: true` |
| `capabilities: read-write` / `read-run-write` | `readonly: false` |
| `model_class` / `thinking` | drop |

`model`: **`inherit`** (recommended default) or exact id from Cursor picker. **Forbidden**: `auto`, `fast`, or other undocumented aliases. Omitting `model` is OK (same as inherit)

### Write rules (Claude Code) → `.claude/agents/{name}.md`

Frontmatter **only** (minimum set; omit unused optional fields):

```yaml
---
name: {name}
description: {description}
tools: {comma-separated allowlist}
model: inherit
---
```

Map `capabilities` → `tools` allowlist (do **not** omit `tools` for read-only agents — omit inherits everything):

| Portable `capabilities` | Claude Code `tools` |
| ----------------------- | ------------------- |
| `read-only` | `Read, Grep, Glob` (add `LSP` only if project Tooling says LSP plugins are active and user wants it) |
| `read-write` | `Read, Grep, Glob, Edit, Write` |
| `read-run-write` | `Read, Grep, Glob, Edit, Write, Bash` |

Optional (only if user asks): `disallowedTools`, `permissionMode`, `maxTurns`, `background: false`

`model`: prefer `inherit`, or Claude aliases `sonnet` / `opus` / `haiku` / `fable`, or a full id the user confirms — never invent. No Cursor-style `auto`

### Write rules (GitHub Copilot) → `.github/agents/{name}.agent.md`

Filename **must** end with `.agent.md`. Frontmatter:

```yaml
---
name: {name}
description: {description}
tools: [{allowlist}]
---
```

Map `capabilities` → `tools` YAML array (Copilot tool aliases; restrict read-only agents):

| Portable `capabilities` | Copilot `tools` |
| ----------------------- | --------------- |
| `read-only` | `['read', 'search', 'codebase']` — no `edit`, no `terminal` unless user explicitly widens |
| `read-write` | `['read', 'search', 'codebase', 'edit']` |
| `read-run-write` | `['read', 'search', 'codebase', 'edit', 'terminal']` |

Notes:

- **Model Auto**: omit `model` (session/default). Only set `model:` to a user-confirmed Copilot model string/slug. Do not write `auto` unless user verifies their Copilot surface accepts it
- **Agent Auto**: leave default (`infer` unset). If user wants the agent **never** auto-picked, add `disable-model-invocation: true`
- `name` optional for Copilot — still write it for roster parity
- Do not copy Cursor `readonly` / `is_background` or Claude comma-string `tools` — use YAML array
- `tools: ['*']` or omitting `tools` = all tools — **forbidden** for `read-only` agents

### Write rules (OpenCode) → `.opencode/agents/{name}.md`

Path is `.opencode/agents/` (project) or `~/.config/opencode/agents/` (user) — prefer project. Filename stem = agent id (no separate `name` field required)

```yaml
---
description: {description}
mode: subagent
permission:
  edit: deny
  bash: deny
---
```

Map `capabilities` → `permission` (prefer `permission` over deprecated `tools:`):

| Portable `capabilities` | OpenCode `permission` |
| ----------------------- | --------------------- |
| `read-only` | `edit: deny` · `bash: deny` · leave `read`/`grep`/`glob`/`list` allow (default allow if unset) · `task: deny` (no nested subagents) |
| `read-write` | `edit: allow` · `bash: deny` · `task: deny` |
| `read-run-write` | `edit: allow` · `bash: allow` · `task: deny` |

Notes:

- Always `mode: subagent` for skill roster agents (invoked by primary / `@`, not Tab primary)
- **Model Auto / follow parent**: **omit** `model` — OpenCode subagents then use the invoking parent's model. If user pins: `model: {provider}/{model-id}` they confirm (e.g. `anthropic/claude-sonnet-4-20250514`) — never invent
- Optional: `temperature: 0.1` for critics if user wants; skip by default
- Do not copy Cursor/Claude/Copilot frontmatter keys into OpenCode files
- If both `.opencode/agent/` (legacy singular) and `.opencode/agents/` exist, prefer `agents/` per current OpenCode docs

### Idempotent refresh

Re-run: compare skill roster vs each chosen target dir · report missing / stale (body hash or mtime) · offer sync with same tier questions (pre-fill last Tooling `Native agents:` values if present) · refresh may target one platform without touching others
