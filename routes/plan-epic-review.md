# plan/epic-review E{n} {prd|arch} — Epic Review

**Purpose**: validate the epic specification (prd) or architecture (arch) with stakeholders

**Mindset**: review facilitator — protect the human's time; surface only genuine judgment calls, in plain sentences

**Inputs**:
- prd: `epic-prd.md` · `epic-brief.md` · `epic-review.md`
- arch: `epic-arch.md` · `epic-prd.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · `epic-review.md`

**Outputs**: updated `epic-prd.md` or `epic-arch.md` · signed-off review section (PM for prd, Tech Lead for arch) · decisions in `docs/decisions.md`

## Steps

1. Verify `epic-review.md` exists and read it
2. Auto-verify the mechanical items (completeness, testable criteria, valid references, consistency with parents); collapse to one summary line. Fix trivial gaps directly
3. Present **Decisions requiring your validation** (max 10 plain sentences) plus open questions, blocking first — prd: scope, priorities, user journeys, success criteria, out of scope; arch: data path, API contracts, data model, technology choices, trade-offs
4. Apply the answers **as written** — record verbatim, never paraphrase, never re-ask (if ambiguous, ask only the clarification). If a change contradicts `docs/decisions.md`, surface the conflict and ask
5. Append validated decisions to `docs/decisions.md`
6. Mark the review signed off
7. Run Status Sync. No changelog entry (changelog hard rule). Handoff: prd approved → `plan/epic-arch E{n}`; arch approved → `plan/feat E{n} F1`
