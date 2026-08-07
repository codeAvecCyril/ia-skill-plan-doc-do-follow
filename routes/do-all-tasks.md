# do/all-tasks E{n} F{n} — Execute All Feature Tasks

**Purpose**: execute all feature tasks in dependency-ordered waves via subagents, then verify inline — no separate `do/verify` pass

**Mindset**: orchestrator — dispatch, integrate, track; implement in-line only inherently sequential tasks. Standard model; judgment went into task packets

**Inputs**: `feat-tasks.md` · `subagents/feature-coder.md` · repository instruction file(s) (SKILL.md → Platform integration) · `routes/do-verify.md` for final phase

**Outputs**: implemented code and tests · Task Summary table fully updated · feature verified 🟢 (or 🔵 with gap list) · statuses cascaded via Status Sync

## Steps

1. Read `feat-tasks.md`; compute execution waves from dependency DAG (tasks in wave mutually independent)
2. Per wave, run one **feature-coder** subagent per task with **task packet**: full task text, target file paths, referenced pattern file content, DONE criteria, repository instruction file content. Do **not** tell subagents to read PRD, architecture, or whole tasks file — packet is the context
3. After each wave: check each coder's report (DONE criteria confirmed, validation output pasted), update completed rows in Task Summary table, run linter and fix issues, record any task-quality defects reported — then continue straight to next wave, no pause, no asking user. Stop mid-run only for genuine blocker: failed task unfixable from its packet, or contradiction requiring user decision
4. Execute inherently sequential tasks (e.g. final integration tests) directly, following Minimal implementation ladder (SKILL.md → Working Economy)
5. **Verification phase** — when all tasks 🟢, run gates of `routes/do-verify.md` inline (conditional subagents where triggers fire; inline-first — check small surfaces yourself). All pass → feature 🟢; any fail → 🔵 with each gap as complete sentence
6. Run Status Sync. Changelog per hard rule: one feature-verified 🟢 line in epic changelog (project changelog only on epic completion) — never waves, gates, or task details. Handoff: `plan/feat E{n} F{n+1}`, `plan/epic E{n+1}` if epic done, or gap list with recommended fixing route
