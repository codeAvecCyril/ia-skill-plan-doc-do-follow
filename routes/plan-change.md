# plan/change — Scope Change

**Purpose**: apply scope change across all docs — including existing (even 🟢) epic · only route that reopens completed work

**Mindset**: change manager — impact analysis before any edit · user validation before any application · strong model, deep thinking

**Inputs**: change request · Product Spirit block · `docs/decisions.md` · `docs/project-status.md` · impacted epic/feature docs · `docs/ui-map.md` and `docs/data-model.md` if they exist

**Outputs**: updated brief/PRDs/architecture/tasks for impacted scope · updated living docs · recorded decision · statuses reopened via Status Sync

## Steps

1. **Capture and classify.** Restate change in complete sentences: (a) new epic · (b) new feature in existing epic (even 🟢) · (c) change to specified-but-not-implemented feature · (d) change to implemented feature · (e) epic-level scope change · (f) removal/descoping
2. **Check recorded decisions.** If change contradicts Product Spirit block or `docs/decisions.md`, surface conflict and ask before anything else
3. **Impact analysis, top-down.** Identify every impacted document and code area · for (d), establish what implementation actually does — read it, or for large surface run SKILL.md inline-first (scout-lite or **repo-scout**)
4. **Present change plan for validation**: ≤10 plain-sentence items — what gets updated, reopened, and new work · wait for approval
5. **Record decision** in `docs/decisions.md` (date, decision, why, decided by)
6. **Apply, by classification**:
   - (a) follow `plan/epic` · check whether project-wide docs need updating
   - (b) assign next `F{n}`, add to epic PRD feature list and `epic-status.md` as ⚪, then follow `plan/feat`
   - (c) update `feat-prd.md` (and `feat-tasks.md` if it exists) in place
   - (d) update `feat-prd.md`, marking changed requirements (e.g. `FR-3 (revised {date})`); **append** new tasks `T{next}…` to `feat-tasks.md` — never rewrite or delete completed task history; update Architecture Delta; run `plan/feat-arch` if triggered
   - (e)/(f) update `epic-prd.md`/`epic-arch.md`; for removals, mark descoped with link to decision — don't delete documents
7. **Sync living docs** in same change: `docs/ui-map.md`, `docs/data-model.md`
8. **Run Status Sync.** Reopening automatic: appended TODO tasks put 🟢 feature back to 🔵, cascading upward · scope change earns one changelog line (≤25 words, hard rule)
9. Run **doc-coherence-reviewer** subagent and fix reported drift
10. Handoff: `plan/feat E{n} F{n}` for new feature, `plan/tasks E{n} F{n}` if spec changed, or `do/task E{n} F{n} T{n}` if tasks were appended
