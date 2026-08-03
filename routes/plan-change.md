# plan/change — Scope Change

**Purpose**: handle a scope change consistently across all documents — including on an existing (even 🟢) epic. The only route that reopens completed work

**Mindset**: change manager — impact analysis before any edit, user validation before any application. Strong model, deep thinking

**Inputs**: the change request · Product Spirit block · `docs/decisions.md` · `docs/project-status.md` · impacted epic/feature documents · `docs/ui-map.md` and `docs/data-model.md` if they exist

**Outputs**: updated brief/PRDs/architecture/tasks for the impacted scope · updated living docs · a recorded decision · statuses reopened via Status Sync

## Steps

1. **Capture and classify.** Restate the change in complete sentences: (a) new epic · (b) new feature in an existing epic (even 🟢) · (c) change to a specified-but-not-implemented feature · (d) change to an implemented feature · (e) epic-level scope change · (f) removal/descoping
2. **Check recorded decisions.** If the change contradicts the Product Spirit block or `docs/decisions.md`, surface the conflict and ask before anything else
3. **Impact analysis, top-down.** Identify every impacted document and code area. For (d), establish what the implementation actually does — read it, or for a large surface send precise questions to a **repo-scout** subagent
4. **Present the change plan for validation**: ≤10 plain-sentence items — what gets updated, reopened, and the new work. Wait for approval
5. **Record the decision** in `docs/decisions.md` (date, decision, why, decided by)
6. **Apply, by classification**:
   - (a) follow `plan/epic`; check whether project-wide docs need updating
   - (b) assign the next `F{n}`, add to the epic PRD's feature list and `epic-status.md` as ⚪, then follow `plan/feat`
   - (c) update `feat-prd.md` (and `feat-tasks.md` if it exists) in place
   - (d) update `feat-prd.md`, marking changed requirements (e.g. `FR-3 (revised {date})`); **append** new tasks `T{next}…` to `feat-tasks.md` — never rewrite or delete completed task history; update the Architecture Delta; run `plan/feat-arch` if triggered
   - (e)/(f) update `epic-prd.md`/`epic-arch.md`; for removals, mark descoped with a link to the decision — don't delete documents
7. **Sync living docs** in the same change: `docs/ui-map.md`, `docs/data-model.md`
8. **Run Status Sync.** Reopening is automatic: appended TODO tasks put a 🟢 feature back to 🔵, cascading upward. A scope change earns one changelog line (≤25 words, hard rule)
9. Run the **doc-coherence-reviewer** subagent and fix reported drift
10. Handoff: `plan/feat E{n} F{n}` for a new feature, `plan/tasks E{n} F{n}` if a spec changed, or `do/task E{n} F{n} T{n}` if tasks were appended
