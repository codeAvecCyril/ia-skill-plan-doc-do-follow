# plan/epic-review E{n} {prd|arch} — Epic Review

**Purpose**: validate epic specification (prd) or architecture (arch) with stakeholders

**Mindset**: review facilitator — protect human's time · surface only genuine judgment calls, in plain sentences

**Inputs**:
- prd: `epic-prd.md` · `epic-brief.md` · `epic-review.md`
- arch: `epic-arch.md` · `epic-prd.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · `epic-review.md`

**Outputs**: updated `epic-prd.md` or `epic-arch.md` (answers applied) · signed-off review section (PM for prd, Tech Lead for arch) with answers recorded verbatim

## Steps

1. Verify `epic-review.md` exists · `pddf review-open` lists unanswered items — read only those sections
2. Auto-verify mechanical items (completeness, testable criteria, valid references, consistency with parents); collapse to one summary line · fix trivial gaps directly
3. Present **Decisions requiring your validation** (max 10 items) plus open questions, blocking first · every item per `guides/review-questions.md` — rewrite any item failing its self-check before presenting — prd: scope, priorities, user journeys, success criteria, out of scope; arch: data path, API contracts, data model, technology choices, trade-offs
4. Apply answers **as written** into reviewed doc (requirement, scope line, design section) — reviewed doc carries decision from now on · record answer verbatim under its item · never paraphrase, never re-ask (if ambiguous, ask only clarification) · if answer contradicts approved parent doc or earlier answer, surface conflict and ask
5. Mark review signed off
6. Run Status Sync · no changelog entry (changelog hard rule) · Handoff: prd approved → `plan/epic-arch E{n}`; arch approved → `plan/feat E{n} F1`
