# plan/change — Scope Change

**Purpose**: handle a scope change consistently across all documents — including adding or updating an epic or feature on an existing (even 🟢) epic. The only route that reopens completed work

**Mindset**: change manager — impact analysis before any edit, user validation before any application. Strong model, deep thinking

**Inputs**: the change request · Product Spirit block · `docs/decisions.md` · `docs/project-status.md` · the impacted epic/feature documents · `docs/ui-map.md` and `docs/data-model.md` if they exist

**Outputs**: updated brief/PRDs/architecture/tasks for the impacted scope · updated living docs · a recorded decision · statuses reopened via Status Sync

## Steps

1. **Capture and classify.** Restate the change request in complete sentences and classify it:
   - (a) new epic
   - (b) new feature in an existing epic (including a 🟢 DONE epic)
   - (c) change to a specified-but-not-implemented feature
   - (d) change to an implemented feature
   - (e) epic-level scope change
   - (f) removal / descoping
2. **Check recorded decisions.** If the change contradicts the Product Spirit block or `docs/decisions.md`, surface the conflict and ask for confirmation before anything else
3. **Impact analysis, top-down.** Identify every impacted document (epic-prd, epic-arch, feat-prds, feat-tasks, `docs/ui-map.md`, `docs/data-model.md`) and the impacted code areas. For (d), establish what the implementation actually does — read it directly or, when the surface is large, send precise questions to a **repo-scout** subagent
4. **Present the change plan for validation**: at most 10 plain-sentence items — what gets updated, what gets reopened, what the new work is. Wait for approval
5. **Record the decision** in `docs/decisions.md` (date, decision, why, decided by)
6. **Apply, by classification**:
   - (a) follow the `plan/epic` playbook and check whether project-wide global documents need updating
   - (b) assign the next `F{n}`, add it to the epic PRD's feature list and to `epic-status.md` as ⚪, then run the `plan/feat` playbook
   - (c) update `feat-prd.md` (and `feat-tasks.md` if it exists) in place
   - (d) update `feat-prd.md`, marking changed requirements (e.g. `FR-3 (revised {date})`); **append** new tasks `T{next}…` to `feat-tasks.md` — never rewrite or delete completed task history; update the Architecture Delta and run `plan/feat-arch` if its triggers fire
   - (e)/(f) update `epic-prd.md` and `epic-arch.md`; for removals, mark the scope descoped with a link to the decision rather than deleting documents
7. **Sync living docs** in the same change: `docs/ui-map.md` (entry points), `docs/data-model.md` (schema deltas)
8. **Run Status Sync.** Reopening is automatic from the derivation rules: appended TODO tasks put a 🟢 feature back to 🔵, which cascades upward
9. Run the **doc-coherence-reviewer** subagent and fix any drift it reports
10. Handoff: `plan/feat E{n} F{n}` for a new feature, `plan/tasks E{n} F{n}` if a spec changed, or `do/task E{n} F{n} T{n}` if tasks were appended
