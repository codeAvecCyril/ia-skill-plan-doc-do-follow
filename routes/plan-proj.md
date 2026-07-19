# plan/proj — Project Planning

**Purpose**: extract epics from product vision and bootstrap the project's living documentation

**Mindset**: product strategist — distill identity before structure; every epic must earn its place in the vision. Strong model, deep thinking

**Inputs**: `docs/product.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · existing `docs/project-status.md` (optional)

**Outputs**: `docs/project-status.md` · one `docs/epics/{epic-slug}/epic-brief.md` per epic · `docs/project-review.md` · `docs/decisions.md` · living docs bootstrapped (step 6)

## Steps

1. Verify the input files exist; ask for the missing ones
2. Distill the **Product Spirit block**: 5–10 complete sentences stating what the product is, who it is for, what makes it different, and what it deliberately is *not*. It goes at the top of `docs/project-status.md` and is reused by every route and reviewer
3. Determine the **mode**: `solo` (default — no owners, estimates, or velocity anywhere) or `team` (effort/owner columns enabled). Ask only if ambiguous. Record it in the project-status header
4. Extract stack, patterns, and constraints. Build epics with codes (`E1…`), slugs `e{n}-{name}` (e.g. `e2-orm-discovery`), and briefs from `templates/epic-brief.md`. Map dependencies and phases
5. Ask questions on scope/priority/stack ambiguity (Invariant 8)
6. Bootstrap the living docs that apply (skip the rest — Invariant 7):
   - `docs/decisions.md` from `templates/decisions.md` (always)
   - If the project persists data: `docs/data-model.md` from `templates/data-model.md` (may start as a pointer to existing schema docs)
   - If the project has a UI: `docs/ui-map.md` and `docs/design-guidelines.md` from their templates — if a design system already exists in the repo, reference it instead of writing a new one
7. Generate `docs/project-status.md` from `templates/proj-status.md` (Spirit block, mode, epic roadmap table, pie chart, dependency graph)
8. Generate `docs/project-review.md` from `templates/proj-review.md`
9. Run Status Sync. Handoff: `plan/proj-review`
