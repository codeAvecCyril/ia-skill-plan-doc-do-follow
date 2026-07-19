# do/sync-status — Recompute All Statuses

**Purpose**: recompute every status and progress figure from document reality and repair drift. Run it any time statuses look wrong, after manual edits, after a crashed session, or after work done by another tool/AI

**Mindset**: accountant — deterministic application of the derivation rules, no interpretation. A standard model suffices

**Inputs**: all `feat-tasks.md` Task Summary tables · all `epic-status.md` files · `docs/project-status.md`

**Outputs**: repaired owning tables at every level · a drift report

## Steps

1. Enumerate the epics and features from the `docs/epics/` tree (the tree, not the status files, defines what exists)
2. For every feature, apply the Status Model derivation rules (SKILL.md) from its documents and Task Summary table. Preserve a stored 🟢 only if no TODO/DEV tasks were added after verification; otherwise downgrade to 🔵
3. Rewrite each feature row in its `epic-status.md`, then each epic row, the Progress section, and the pie chart in `docs/project-status.md`. Add one changelog line summarizing the sync
4. Report the drift found: each stored value that differed from the derived one, as "X was recorded as {old}, derived {new} because {reason}"
5. Handoff with the most useful next command given the repaired state (typically the first unblocked `do/task` or `do/verify`)
