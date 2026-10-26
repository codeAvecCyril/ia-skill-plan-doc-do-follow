# plan/feat-review E{n} F{n} {prd|arch} — Feature Review

**Purpose**: validate feature specification (prd) or architecture (arch) with stakeholders

**Mindset**: review facilitator — protect human's time · surface only genuine judgment calls, in plain sentences

**Inputs**:
- prd: `feat-prd.md` · `feat-review.md` · epic PRD for context
- arch: `feat-arch.md` (or Architecture Delta of `feat-prd.md`) · `feat-review.md`

**Outputs**: updated `feat-prd.md` or `feat-arch.md` (answers applied) · signed-off review section (PM for prd, Tech Lead for arch) with answers recorded verbatim

## Steps

1. Verify `feat-review.md` exists · `pddf review-open` lists unanswered items — read only those sections
2. Auto-verify mechanical items (stories testable, criteria measurable, edge cases listed, out-of-scope defined, entry point in `docs/ui-map.md` for UI); collapse to one summary line · fix trivial gaps directly
3. Read user answers in **Decisions requiring your validation** (incl. any **Redesign** section from `plan/redesign`) plus open questions, blocking first · unanswered item failing `guides/review-questions.md` self-check → rewrite it before asking
4. Apply answers **as written** into reviewed doc (requirement, acceptance criterion, Architecture Delta) — reviewed doc carries decision from now on · record answer verbatim under its item · never paraphrase, never re-ask (if ambiguous, ask only clarification) · if answer contradicts approved epic docs or earlier answer, surface conflict and ask
5. Mark review signed off
6. Run Status Sync · no changelog entry (changelog hard rule) · Handoff: `plan/tasks E{n} F{n}` (default), or `plan/feat-arch E{n} F{n}` if Architecture Delta flagged trigger criteria
