# plan/migrate — One-Shot Migration from Skill v2

**Purpose**: migrate a project documented with skill v2 to the v3 structure in one pass, safely, with epics and features in any state of completion. Documentation only — this route never touches code. Run once; it is idempotent (re-running on a migrated project finds nothing to do)

**Mindset**: careful archivist — preserve history, resolve conflicts by evidence, never rewrite what still works. Strong model

**Inputs**: the whole `docs/` tree · `docs/product.md` · old review files · the implemented code (read-only, to reverse-engineer schema and navigation)

**Outputs**: consolidated owning tables · `feat-status.md` files removed · Product Spirit block · living docs bootstrapped (`decisions.md`, `data-model.md`, `ui-map.md`, `design-guidelines.md`) · a migration report

## Steps

1. **Inventory.** Enumerate epics and features from the `docs/epics/` tree. Detect v2 artifacts: `feat-status.md` files, per-task `**Status**:` lines in `feat-tasks.md`, duplicated task tables, status legends and formula boilerplate in generated docs
2. **Consolidate task statuses.** For each feature with a `feat-tasks.md`, collect every task's status from all v2 locations (Task Summary table, per-task status lines, the task table in `feat-status.md`). Resolve disagreements with **most-advanced-wins** (⚪ < 🟡 < 🟣 < 🔵 < 🟢), with one guard: before accepting a disputed 🟢, spot-check that the task's files/tests actually exist in the code; if they do not, keep the lower status and flag it. Write the result into the Task Summary table — the sole owner from now on — and strip the per-task status lines. List every conflict and its resolution in the migration report
3. **Remove `feat-status.md` files.** Feature status now lives in the `epic-status.md` Feature table; create or complete that table (from `templates/epic-status.md`) where v2 left it missing. Carry over any blockers or notes worth keeping before deleting
4. **Distill the Product Spirit block** from `docs/product.md` (5–10 complete sentences) and place it at the top of `docs/project-status.md`. Determine the mode (solo/team) — ask only if ambiguous
5. **Bootstrap the living docs** (skip those that do not apply):
   - `docs/decisions.md`: seed from the sign-offs, answered questions, and validated changes found in existing review files, so past user decisions stay binding
   - `docs/data-model.md`: reverse-engineer from the actual schema (migrations, ORM models) — the implemented code, not the PRDs, is the truth for the implemented half. May start as a pointer to existing schema docs plus a change log
   - `docs/ui-map.md`: build from the actual routing/navigation code for implemented screens; add planned screens from the feature PRDs, marked with their status
   - `docs/design-guidelines.md`: point to the existing design system if the repo has one; otherwise write the minimal version from `templates/design-guidelines.md`
6. **Do not rewrite legacy documents.** Old PRDs, architecture docs, and completed reviews stay as they are. Missing v3 sections (Entry Points & Navigation, Architecture Delta) are filled **lazily** — the first time a v3 route touches that feature. List these pending documents in the migration report
7. **Run Status Sync** over everything, then the **doc-coherence-reviewer** subagent (`subagents/doc-coherence-reviewer.md`); fix the drift it reports
8. **Produce the migration report**: status conflicts and how each was resolved · statuses changed by the sync (old → new, with reason) · living docs created and what seeded them · legacy documents pending lazy migration · open questions for the user (blocking first)
9. Handoff with the most useful next command given the repaired state (typically the first unblocked `do/task`, or `do/verify` for a feature whose tasks are all 🟢).
