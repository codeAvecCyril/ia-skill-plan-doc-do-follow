# do/task E{n} F{n} T{n} — Task Execution

**Purpose**: execute one task. Tasks are self-contained — the task text is the primary context; open other documents only if the task itself proves ambiguous (and report that as a task-quality defect in the handoff).

**Mindset**: implementer — precise and minimal, exactly the DONE criteria, no scope creep, no drive-by refactoring. A standard model suffices; adopt the discipline of `subagents/feature-coder.md`.

**Inputs**: the task and its dependencies from `feat-tasks.md` · the code pattern(s) and target files it references · repository instruction file(s) (see Platform integration in SKILL.md).

**Outputs**: implemented code and tests · task row set to 🟢 in the Task Summary table · statuses cascaded via Status Sync.

## Steps

1. Read the full task and its dependency tasks in `feat-tasks.md`; verify dependencies are 🟢.
2. Read the referenced code pattern and target files.
3. Implement minimally and precisely — exactly what the task's DONE criteria require, nothing more.
4. Run the task's validation commands; fix until they pass, or report the blocker.
5. Update **only** the task's row in the Task Summary table of `feat-tasks.md` to 🟢 (or 🔵 if blocked mid-way, with the blocker noted in the Blockers section).
6. Run Status Sync (feature → 🔵 on first task; epic and project rows follow).
7. Handoff with the next unblocked `@do/task E{n} F{n} T{n}`, or `@do/verify E{n} F{n}` if all tasks are 🟢.
