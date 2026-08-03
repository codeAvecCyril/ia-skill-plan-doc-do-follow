# plan/migrate — One-Shot Migration from Skill v2

**Purpose**: migrate a v2-documented project to the v3 structure in one pass, epics/features in any state. Documentation only — never touches code. Idempotent

**Mindset**: careful archivist — preserve history, resolve conflicts by evidence, never rewrite what still works. Strong model

**Inputs**: the `docs/` tree · `docs/product.md` · old review files · the implemented code (read-only, to reverse-engineer schema and navigation)

**Outputs**: consolidated owning tables · `feat-status.md` files removed · Product Spirit block · living docs bootstrapped · a migration report

## Steps

1. **Inventory.** Enumerate epics/features from `docs/epics/`. Detect v2 artifacts: `feat-status.md` files, per-task `**Status**:` lines, duplicated task tables, status legends/boilerplate
2. **Consolidate task statuses.** Collect each task's status from all v2 locations; resolve disagreements **most-advanced-wins** (⚪ < 🟡 < 🟣 < 🔵 < 🟢), with one guard: before accepting a disputed 🟢, spot-check the task's files/tests exist in the code; if not, keep the lower status and flag it. Write into the Task Summary table (sole owner from now on), strip per-task status lines. List every conflict + resolution in the report
3. **Remove `feat-status.md` files.** Create/complete the `epic-status.md` Feature table where missing (from `templates/epic-status.md`); carry over blockers/notes worth keeping first
4. **Distill the Product Spirit block** from `docs/product.md` (5–10 complete sentences) at the top of `docs/project-status.md`. Determine mode (solo/team) — ask only if ambiguous
5. **Bootstrap the living docs** (skip those that do not apply): `docs/decisions.md` seeded from sign-offs, answered questions, and validated changes in old reviews · `docs/data-model.md` reverse-engineered from the actual schema (migrations, ORM models — code is the truth for the implemented half; may start as a pointer to existing schema docs) · `docs/ui-map.md` from the actual routing/navigation code, plus planned screens from PRDs marked with status · `docs/design-guidelines.md` pointing to an existing design system, else minimal from template
6. **Do not rewrite legacy documents.** Missing v3 sections (Entry Points, Architecture Delta) are filled **lazily** the first time a route touches that feature. List these in the report
7. **Run Status Sync** over everything, then the **doc-coherence-reviewer** subagent; fix reported drift
8. **Produce the migration report**: status conflicts/resolutions · statuses changed (old → new, reason) · living docs created and their seeds · documents pending lazy migration · open questions (blocking first)
9. Handoff with the most useful next command (typically the first unblocked `do/task`, or `do/verify` for a feature whose tasks are all 🟢)
