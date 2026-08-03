# plan/proj — Project Planning

**Purpose**: extract epics from product vision and bootstrap the living docs

**Mindset**: product strategist — distill identity before structure; every epic must earn its place in the vision. Strong model, deep thinking

**Inputs**: `docs/product.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · existing `docs/project-status.md` (optional)

**Outputs**: `docs/project-status.md` · one `docs/epics/{epic-slug}/epic-brief.md` per epic · `docs/project-review.md` · `docs/decisions.md` · living docs (step 6)

## Steps

1. Verify the input files exist; ask for the missing ones
2. Distill the **Product Spirit block**: 5–10 complete sentences — what the product is, who it is for, what makes it different, what it deliberately is *not*. Top of `docs/project-status.md`
3. Determine the **mode**: `solo` (default — no owners/estimates/velocity) or `team` (effort/owner columns). Ask only if ambiguous. Record in the project-status header
4. Extract stack, patterns, constraints. Build epics with codes (`E1…`), slugs `e{n}-{name}`, briefs from `templates/epic-brief.md`. Map dependencies and phases
5. Ask questions on scope/priority/stack ambiguity (Invariant 8)
6. Bootstrap the living docs that apply (skip the rest — Invariant 7): `docs/decisions.md` (always) · `docs/data-model.md` if the project persists data (may start as a pointer to existing schema docs) · `docs/ui-map.md` + `docs/design-guidelines.md` if UI (reference an existing design system instead of writing a new one)
7. Generate `docs/project-status.md` from `templates/proj-status.md` (Spirit block, mode, epic roadmap, pie chart, dependency graph)
8. Generate `docs/project-review.md` from `templates/proj-review.md`
9. Run Status Sync. Handoff: `plan/proj-review`
