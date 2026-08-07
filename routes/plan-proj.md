# plan/proj — Project Planning

**Purpose**: extract epics from product vision and bootstrap living docs

**Mindset**: product strategist — distill identity before structure · every epic must earn its place in vision · strong model, deep thinking

**Inputs**: `docs/product.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · existing `docs/project-status.md` (optional)

**Outputs**: `docs/project-status.md` · one `docs/epics/{epic-slug}/epic-brief.md` per epic · `docs/project-review.md` · `docs/decisions.md` · living docs (step 6)

## Steps

1. Verify input files exist; ask for missing ones
2. Distill **Product Spirit block**: 5–10 complete sentences — what product is, who it is for, what makes it different, what it deliberately is *not* · top of `docs/project-status.md`
3. Determine **mode**: `solo` (default — no owners/estimates/velocity) or `team` (effort/owner columns) · ask only if ambiguous · record in project-status header
4. Extract stack, patterns, constraints · build epics with codes (`E1…`), slugs `e{n}-{name}`, briefs from `templates/epic-brief.md` · map dependencies and phases
5. Ask on scope/priority/stack ambiguity (Invariant 8)
6. Bootstrap living docs that apply (skip rest — Invariant 7): `docs/decisions.md` (always) · `docs/data-model.md` if project persists data (may start as pointer to existing schema docs) · `docs/ui-map.md` + `docs/design-guidelines.md` if UI (reference existing design system instead of writing new one)
7. Generate `docs/project-status.md` from `templates/proj-status.md` (Spirit block, mode, epic roadmap, pie chart, dependency graph)
8. Generate `docs/project-review.md` from `templates/proj-review.md`
9. Run Status Sync · Handoff: `plan/proj-review`
