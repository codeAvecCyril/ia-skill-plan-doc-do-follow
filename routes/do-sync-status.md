# do/sync-status — Recompute All Statuses

**Purpose**: recompute every status and progress figure from document reality and repair drift. Run when statuses look wrong, after manual edits, a crashed session, or work by another tool/AI

**Mindset**: accountant — deterministic application of the derivation rules, no interpretation. Standard model

**Inputs**: all `feat-tasks.md` Task Summary tables · all `epic-status.md` files · `docs/project-status.md`

**Outputs**: repaired owning tables at every level · a drift report

## Steps

1. Enumerate epics and features from the `docs/epics/` tree (the tree, not the status files, defines what exists)
2. For every feature, apply the Status Model derivation rules (SKILL.md). Preserve a stored 🟢 only if no TODO/DEV tasks were added after verification; otherwise downgrade to 🔵
3. Rewrite each feature row in its `epic-status.md`, then each epic row, the Progress section, and the pie chart in `docs/project-status.md` (no changelog entry)
4. Report the drift: each stored value that differed, as "X was recorded as {old}, derived {new} because {reason}"
5. Handoff with the most useful next command (typically the first unblocked `do/task` or `do/verify`)
