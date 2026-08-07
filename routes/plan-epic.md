# plan/epic E{n} — Epic Planning

**Purpose**: create epic PRD and feature tracking

**Mindset**: product manager writing spec stakeholders will sign — complete sentences, scope discipline, questions before assumptions · strong model, deep thinking

**Inputs**: `epic-brief.md` · `docs/product.md` (Spirit block suffices if unchanged) · `docs/global_architecture.md` · `docs/technical-stack.md` · `docs/project-status.md` · `docs/decisions.md`

**Outputs**: `epic-prd.md` · `epic-status.md` (owns feature statuses) · `epic-review.md`

## Steps

1. Verify `docs/project-status.md` contains `E{n}` · if already 🟡 or later, warn and confirm re-specification
2. Read epic brief and Product Spirit block
3. Define features (`F1…`) with slugs `f{n}-{name}` and priorities (P0/P1/P2)
4. Ask on any ambiguity in requirements, scope, or priorities (Invariant 8)
5. Generate `epic-prd.md` from `templates/epic-prd.md` · every requirement complete sentence stakeholder can validate (Invariant 6)
6. Run **prd-critic** subagent and handle findings (SKILL.md → Subagents)
7. Generate `epic-status.md` from `templates/epic-status.md`, all features ⚪
8. Generate `epic-review.md` from `templates/epic-review.md`: auto-check mechanical items; only genuine judgment calls in "Decisions requiring your validation" (max 10); add unanswered questions
9. Run Status Sync (epic → 🟡) · Handoff: `plan/epic-review E{n} prd`
