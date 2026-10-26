# do/task E{n} F{n} T{n} — Task Execution

**Purpose**: execute one task. Tasks self-contained — task text is primary context; open other documents only if task proves ambiguous (report that as task-quality defect in handoff)

**Mindset**: implementer — precise and minimal, exactly DONE criteria, no scope creep, no drive-by refactoring, no redesign (Invariant 19). Standard model, medium thinking; adopt discipline of `subagents/feature-coder.md`

**Inputs**: task and its dependencies from `feat-tasks.md` · pattern(s) and target files it references · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: implemented code and tests · task row 🟢 in Task Summary table · statuses cascaded via Status Sync

## Steps

1. `pddf packet E{n} F{n} T{n}` — task text, its contracts, patterns, dependency warning (never read whole tasks file) · open Design Gap touching task → stop, handoff `plan/redesign E{n} F{n}` · `pddf task E{n} F{n} T{n} 🔵`
2. Read referenced pattern and target files
3. Implement exactly what DONE criteria require, climbing Minimal implementation ladder (SKILL.md → Working Economy)
4. Run task's validation commands; fix until they pass, or report blocker · plan cannot work as written (test: `subagents/feature-coordinator.md` → Escalation triage) → never ask user design questions: record gap in Design Gaps, handoff `plan/redesign E{n} F{n}` · taste disagreement → follow task
5. `pddf task E{n} F{n} T{n} 🟢` (stays 🔵 if blocked, blocker noted in Blockers section)
6. Run Status Sync (`pddf sync`) (feature → 🔵 on first task; epic and project rows follow)
7. Handoff: next unblocked `do/task E{n} F{n} T{n}`, or `do/verify E{n} F{n}` if all tasks 🟢
