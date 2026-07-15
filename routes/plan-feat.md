# plan/feat E{n} F{n} — Feature Planning

**Purpose**: create the feature PRD. There is no feat-status file — the feature's status lives in `epic-status.md` (Status Model).

**Mindset**: detail-oriented product manager — user stories a tester can execute, requirements a stakeholder can validate in isolation. Strong model, deep thinking.

**Inputs**: `epic-prd.md` · `epic-arch.md` · `docs/technical-stack.md` · `docs/ui-map.md` and `docs/design-guidelines.md` (if UI) · `docs/decisions.md`.

**Outputs**: `features/{feat-slug}/feat-prd.md` · `features/{feat-slug}/feat-review.md` · updated `docs/ui-map.md` (entry point registered, if UI).

## Steps

1. Verify `epic-prd.md` exists and lists `F{n}`. If the feature is already 🟡 or later in `epic-status.md`, warn and confirm re-specification.
2. Create user stories (`US-{n}`) with Given/When/Then acceptance criteria, and requirements: functional (`FR-{n}` with "shall"), API, UI, data, NFR. Write each as a complete sentence a PM can validate in isolation (Invariant 6).
3. **Entry Points & Navigation** (mandatory for UI features): state where the feature appears in the global menu/navigation, its route/URL, its breadcrumb, and how a first-time user discovers it. Register the entry point in `docs/ui-map.md` in the same change. If you cannot answer this, it is a blocking question for the user.
4. **Architecture Delta** (mandatory): list only what this feature adds or changes relative to `epic-arch.md` — new endpoints, new tables/columns, new components. If nothing, write "None — fully covered by the epic architecture." Check the `plan/feat-arch` trigger criteria and note whether a dedicated feature architecture is needed. When the delta must reference existing code you have not verified (entry points, existing endpoints, reusable components), send precise questions to a **repo-scout** subagent (`subagents/repo-scout.md`) instead of guessing or loading the codebase yourself.
5. Define explicit out-of-scope, dependencies, and test strategy sections.
6. Ask blocking and important questions interactively, with impact labels.
7. Generate `feat-prd.md` from `templates/feat-prd.md`; delete non-applicable sections.
8. Run the **prd-critic** subagent (`subagents/prd-critic.md`) with its scoped inputs; apply its findings or record why they were rejected.
9. Generate `feat-review.md` from `templates/feat-review.md`: auto-check mechanical items; keep only judgment calls in "Decisions requiring your validation".
10. Run Status Sync (feature becomes 🟡 in `epic-status.md`). Handoff with `@plan/feat-review E{n} F{n} prd` as default next command.
