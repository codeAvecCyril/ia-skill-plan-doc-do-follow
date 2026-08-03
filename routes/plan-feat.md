# plan/feat E{n} F{n} — Feature Planning

**Purpose**: create the feature PRD (feature status lives in `epic-status.md` — no feat-status file)

**Mindset**: detail-oriented product manager — user stories a tester can execute, requirements a stakeholder can validate in isolation. Strong model, deep thinking

**Inputs**: `epic-prd.md` · `epic-arch.md` · `docs/technical-stack.md` · `docs/ui-map.md` and `docs/design-guidelines.md` (if UI) · `docs/decisions.md`

**Outputs**: `{feat-slug}/feat-prd.md` · `{feat-slug}/feat-review.md` · updated `docs/ui-map.md` (entry point, if UI)

## Steps

1. Verify `epic-prd.md` exists and lists `F{n}`. If already 🟡 or later in `epic-status.md`, warn and confirm re-specification
2. Create user stories (`US-{n}`) with Given/When/Then acceptance criteria, and requirements: functional (`FR-{n}` with "shall"), API, UI, data, NFR — each a complete sentence validatable in isolation (Invariant 6)
3. **Entry Points & Navigation** (mandatory for UI features): menu placement, route/URL, breadcrumb, first-time discovery. Register the entry point in `docs/ui-map.md` in the same change. If unanswerable, it is a blocking question
4. **Architecture Delta** (mandatory): only what this feature adds/changes vs `epic-arch.md` — endpoints, tables/columns, components. If nothing: "None — fully covered by the epic architecture." Check the `plan/feat-arch` trigger criteria and note whether a feat-arch is needed. For unverified existing code, send precise questions to a **repo-scout** subagent instead of guessing or loading the codebase
5. Define out-of-scope, dependencies, and test strategy
6. Ask blocking and important questions interactively (Invariant 8)
7. Generate `feat-prd.md` from `templates/feat-prd.md`
8. Run the **prd-critic** subagent and handle its findings (SKILL.md → Subagents)
9. Generate `feat-review.md` from `templates/feat-review.md`: auto-check mechanical items; only judgment calls in "Decisions requiring your validation"
10. Run Status Sync (feature → 🟡). Handoff: `plan/feat-review E{n} F{n} prd`
