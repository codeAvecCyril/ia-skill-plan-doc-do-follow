# do/all-tasks E{n} F{n} — Execute All Feature Tasks

**Purpose**: execute all tasks of a feature in dependency-ordered waves via subagents, then verify inline — no separate `do/verify` pass

**Mindset**: orchestrator — dispatch, integrate, track; implement in-line only the inherently sequential tasks. Standard model; the judgment went into the task packets

**Inputs**: `feat-tasks.md` · `subagents/feature-coder.md` · repository instruction file(s) (SKILL.md → Platform integration) · `routes/do-verify.md` for the final phase

**Outputs**: implemented code and tests · Task Summary table fully updated · feature verified 🟢 (or 🔵 with gap list) · statuses cascaded via Status Sync

## Steps

1. Read `feat-tasks.md` and compute execution waves from the dependency DAG (tasks in a wave are mutually independent)
2. Per wave, run one **feature-coder** subagent per task with a **task packet**: full task text, target file paths, referenced pattern file content, DONE criteria, repository instruction file content. Do **not** tell subagents to read the PRD, the architecture, or the whole tasks file — the packet is the context
3. After each wave: check each coder's report (DONE criteria confirmed, validation output pasted), update the completed rows in the Task Summary table, run the linter and fix issues, record any task-quality defects reported — then continue straight to the next wave, no pause, no asking the user. Stop mid-run only for a genuine blocker: a failed task unfixable from its packet, or a contradiction requiring a user decision
4. Execute inherently sequential tasks (e.g. final integration tests) directly, following the Minimal implementation ladder (SKILL.md → Working Economy)
5. **Verification phase** — when all tasks are 🟢, run the gates of `routes/do-verify.md` inline (conditional subagents where triggers fire; Cost gate — check small surfaces yourself). All pass → feature 🟢; any fail → 🔵 with each gap as a complete sentence
6. Run Status Sync. Changelog per the hard rule: one feature-verified 🟢 line in the epic changelog (project changelog only on epic completion) — never waves, gates, or task details. Handoff: `plan/feat E{n} F{n+1}`, `plan/epic E{n+1}` if the epic is done, or the gap list with the recommended fixing route
