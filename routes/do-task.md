# do/task E{n} F{n} T{n} — Task Execution

**Purpose**: execute one task. Tasks self-contained — task text is primary context; open other documents only if task proves ambiguous (report that as task-quality defect in handoff)

**Mindset**: implementer — precise and minimal, exactly DONE criteria, no scope creep, no drive-by refactoring. Standard model; adopt discipline of `subagents/feature-coder.md`

**Inputs**: task and its dependencies from `feat-tasks.md` · pattern(s) and target files it references · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: implemented code and tests · task row 🟢 in Task Summary table · statuses cascaded via Status Sync

## Steps

1. Read full task and its dependency tasks; verify dependencies 🟢
2. Read referenced pattern and target files
3. Implement exactly what DONE criteria require, climbing Minimal implementation ladder (SKILL.md → Working Economy)
4. Run task's validation commands; fix until they pass, or report blocker
5. Update **only** task's row in Task Summary table to 🟢 (or 🔵 if blocked, with blocker noted in Blockers section)
6. Run Status Sync (feature → 🔵 on first task; epic and project rows follow)
7. Handoff: next unblocked `do/task E{n} F{n} T{n}`, or `do/verify E{n} F{n}` if all tasks 🟢
