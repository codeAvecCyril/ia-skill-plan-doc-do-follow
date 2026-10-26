# do/sync-status — Recompute All Statuses

**Purpose**: recompute every status and progress figure from document reality; repair drift. Run when statuses look wrong, after manual edits, crashed session, or work by another tool/AI

**Mindset**: accountant — deterministic application of derivation rules, no interpretation. Standard model

**Inputs**: all `feat-tasks.md` Task Summary tables · all `epic-status.md` files · `docs/project-status.md`

**Outputs**: repaired owning tables at every level · drift report

## Steps

1. `pddf sync --check` — lists drift and `REVIEW` items without writing
2. Resolve each `REVIEW` (stored 🟢, rows disagree): spot-check code — shipped → `pddf task E F T 🟢` per row; tasks appended after verification → keep for `--reopen` · legacy file `pddf` cannot parse → repair format from template, or apply Status Model by hand
3. `pddf sync [--reopen E{n}F{n} …]` — rewrites feature rows, epic Progress lines, epic rows, project Progress and pie chart (no changelog entry) · manual fallback: Status Sync procedure (SKILL.md), tree (not status files) defines what exists
4. Report drift in plain sentences: "X was recorded as {old}, derived {new} because {reason}"
5. Handoff with most useful next command (typically first unblocked `do/task` or `do/verify`)
