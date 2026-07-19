# plan/migrate — One-Shot Migration from Skill v2

**Purpose**: migrate a v2-documented project to the v3 structure in one pass, with epics and features in any state of completion. Documentation only — never touches code. Idempotent: re-running on a migrated project finds nothing to do

**Mindset**: careful archivist — preserve history, resolve conflicts by evidence, never rewrite what still works. Strong model

**Inputs**: the whole `docs/` tree · `docs/product.md` · old review files · the implemented code (read-only, to reverse-engineer schema and navigation)

**Outputs**: consolidated owning tables · `feat-status.md` files removed · Product Spirit block · living docs bootstrapped · a migration report

## Steps

1. **Inventory.** Enumerate epics and features from `docs/epics/`. Detect v2 artifacts: `feat-status.md` files, per-task `**Status**:` lines in `feat-tasks.md`, duplicated task tables, status legends and formula boilerplate
2. **Consolidate task statuses.** For each feature, collect every task's status from all v2 locations (Task Summary table, per-task status lines, `feat-status.md` table). Resolve disagreements with **most-advanced-wins** (⚪ < 🟡 < 🟣 < 🔵 < 🟢), with one guard: before accepting a disputed 🟢, spot-check that the task's files/tests exist in the code; if not, keep the lower status and flag it. Write the result into the Task Summary table — the sole owner from now on — and strip per-task status lines. List every conflict and its resolution in the migration report
3. **Remove `feat-status.md` files.** Feature status now lives in the `epic-status.md` Feature table; create or complete that table (from `templates/epic-status.md`) where missing. Carry over blockers/notes worth keeping before deleting
4. **Distill the Product Spirit block** from `docs/product.md` (5–10 complete sentences) at the top of `docs/project-status.md`. Determine the mode (solo/team) — ask only if ambiguous
5. **Bootstrap the living docs** (skip those that do not apply):
   - `docs/decisions.md`: seed from sign-offs, answered questions, and validated changes in existing review files, so past decisions stay binding
   - `docs/data-model.md`: reverse-engineer from the actual schema (migrations, ORM models) — the code, not the PRDs, is the truth for the implemented half. May start as a pointer to existing schema docs plus a change log
   - `docs/ui-map.md`: build from the actual routing/navigation code for implemented screens; add planned screens from feature PRDs, marked with their status
   - `docs/design-guidelines.md`: point to the existing design system if the repo has one; otherwise write the minimal version from `templates/design-guidelines.md`
6. **Do not rewrite legacy documents.** Old PRDs, architecture docs, and completed reviews stay as-is. Missing v3 sections (Entry Points & Navigation, Architecture Delta) are filled **lazily** — the first time a v3 route touches that feature. List these in the migration report
7. **Run Status Sync** over everything, then the **doc-coherence-reviewer** subagent; fix the drift it reports
8. **Produce the migration report**: status conflicts and resolutions · statuses changed by the sync (old → new, with reason) · living docs created and what seeded them · legacy documents pending lazy migration · open questions (blocking first)
9. Handoff with the most useful next command given the repaired state (typically the first unblocked `do/task`, or `do/verify` for a feature whose tasks are all 🟢)
