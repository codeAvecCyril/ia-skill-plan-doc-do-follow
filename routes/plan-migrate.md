# plan/migrate — One-Shot Migration from Skill v2

**Purpose**: migrate v2-documented project to v3 structure in one pass, epics/features in any state · documentation only — never touches code · idempotent

**Mindset**: careful archivist — preserve history · resolve conflicts by evidence · never rewrite what still works · strong model

**Inputs**: `docs/` tree · `docs/product.md` · old review files · implemented code (read-only, to reverse-engineer schema and navigation)

**Outputs**: consolidated owning tables · `feat-status.md` files removed · Product Spirit block · living docs bootstrapped · migration report

## Steps

1. **Inventory.** Enumerate epics/features from `docs/epics/` · detect v2 artifacts: `feat-status.md` files, per-task `**Status**:` lines, duplicated task tables, status legends/boilerplate
2. **Consolidate task statuses.** Collect each task's status from all v2 locations; resolve disagreements **most-advanced-wins** (⚪ < 🟡 < 🟣 < 🔵 < 🟢), with one guard: before accepting disputed 🟢, spot-check task's files/tests exist in code; if not, keep lower status and flag it · write into Task Summary table (sole owner from now on), strip per-task status lines · list every conflict + resolution in report
3. **Remove `feat-status.md` files.** Create/complete `epic-status.md` Feature table where missing (from `templates/epic-status.md`); carry over blockers/notes worth keeping first
4. **Distill Product Spirit block** from `docs/product.md` (5–10 complete sentences) at top of `docs/project-status.md` · determine mode (solo/team) — ask only if ambiguous
5. **Bootstrap living docs** (skip those that do not apply): `docs/decisions.md` seeded from sign-offs, answered questions, and validated changes in old reviews · `docs/data-model.md` reverse-engineered from actual schema (migrations, ORM models — code is truth for implemented half; may start as pointer to existing schema docs) · `docs/ui-map.md` from actual routing/navigation code, plus planned screens from PRDs marked with status · `docs/design-guidelines.md` pointing to existing design system, else minimal from template
6. **Do not rewrite legacy documents.** Missing v3 sections (Entry Points, Architecture Delta) filled **lazily** first time route touches that feature · list these in report
7. **Run Status Sync** over everything, then **doc-coherence-reviewer** subagent; fix reported drift
8. **Produce migration report**: status conflicts/resolutions · statuses changed (old → new, reason) · living docs created and their seeds · documents pending lazy migration · open questions (blocking first)
9. Handoff with most useful next command (typically first unblocked `do/task`, or `do/verify` for feature whose tasks are all 🟢)
