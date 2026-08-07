# do/sync-status — Recompute All Statuses

**Purpose**: recompute every status and progress figure from document reality; repair drift. Run when statuses look wrong, after manual edits, crashed session, or work by another tool/AI

**Mindset**: accountant — deterministic application of derivation rules, no interpretation. Standard model

**Inputs**: all `feat-tasks.md` Task Summary tables · all `epic-status.md` files · `docs/project-status.md`

**Outputs**: repaired owning tables at every level · drift report

## Steps

1. Enumerate epics and features from `docs/epics/` tree (tree, not status files, defines what exists)
2. For every feature, apply Status Model derivation rules (SKILL.md). Preserve stored 🟢 only if no TODO/DEV tasks added after verification; otherwise downgrade to 🔵
3. Rewrite each feature row in its `epic-status.md`, then each epic row, Progress section, and pie chart in `docs/project-status.md` (no changelog entry)
4. Report drift: each stored value that differed, as "X was recorded as {old}, derived {new} because {reason}"
5. Handoff with most useful next command (typically first unblocked `do/task` or `do/verify`)
