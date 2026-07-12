# do/all-tasks E{n} F{n} — Execute All Feature Tasks

**Purpose**: execute all tasks of a feature in dependency-ordered waves, using subagents for parallelizable tasks.

**Inputs**: `feat-tasks.md` · repository instruction file(s) (see Platform integration in SKILL.md).

**Outputs**: implemented code and tests · Task Summary table fully updated · statuses cascaded via Status Sync.

## Steps

1. Read `feat-tasks.md` and compute execution waves from the dependency DAG (tasks in a wave are mutually independent).
2. For each wave, run one subagent per task with a **task packet**: the full task text, its target file paths, the referenced pattern file content, and the DONE criteria. Do **not** tell subagents to read the PRD, the architecture, or the whole tasks file — the packet is the context (this is what keeps token cost linear).
3. After each wave: update the completed rows in the Task Summary table, run the linter and fix issues, then briefly report and ask the user whether to continue to the next wave.
4. Execute inherently sequential tasks (e.g. final integration tests) directly, one by one.
5. When all tasks are 🟢, run Status Sync (feature 🔵, cascades upward).
6. Handoff with `@do/verify E{n} F{n}`.
