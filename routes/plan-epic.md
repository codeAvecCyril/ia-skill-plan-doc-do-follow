# plan/epic E{n} — Epic Planning

**Purpose**: create the epic PRD and establish feature tracking

**Mindset**: product manager writing a spec stakeholders will sign — complete sentences, scope discipline, questions before assumptions. Strong model, deep thinking

**Inputs**: `docs/epics/{epic-slug}/epic-brief.md` · `docs/product.md` (Spirit block suffices if unchanged) · `docs/global_architecture.md` · `docs/technical-stack.md` · `docs/project-status.md` · `docs/decisions.md`

**Outputs**: `epic-prd.md` · `epic-status.md` (owning file for feature statuses) · `epic-review.md`

## Steps

1. Verify `docs/project-status.md` exists and contains `E{n}`. If the epic is already 🟡 or later, warn and confirm re-specification
2. Read the epic brief and the Product Spirit block
3. Define features (`F1…`) with slugs `f{n}-{name}` (e.g. `f3-backend-api`) and priorities (P0/P1/P2)
4. Ask interactive questions for any ambiguity in requirements, scope, or priorities (label blocking / important / minor)
5. Generate `epic-prd.md` from `templates/epic-prd.md`. Write every requirement as a complete sentence a stakeholder can validate (Invariant 6). Delete non-applicable sections
6. Run the **prd-critic** subagent (`subagents/prd-critic.md`) with its scoped inputs; apply its findings or record why they were rejected
7. Generate `epic-status.md` from `templates/epic-status.md` with all features ⚪
8. Generate `epic-review.md` from `templates/epic-review.md`: auto-check the mechanical items yourself; put only genuine judgment calls in "Decisions requiring your validation" (max 10); add unanswered questions
9. Run Status Sync (epic becomes 🟡 in the project roadmap). Handoff with `plan/epic-review E{n} prd` as default next command
