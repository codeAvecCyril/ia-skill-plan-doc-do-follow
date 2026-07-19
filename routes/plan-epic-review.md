# plan/epic-review E{n} {prd|arch} — Epic Review

**Purpose**: validate the epic specification (prd) or the epic architecture (arch) with stakeholders

**Mindset**: review facilitator — protect the human's time; surface only genuine judgment calls, in plain sentences

**Inputs**:
- prd: `epic-prd.md` · `epic-brief.md` · `epic-review.md`
- arch: `epic-arch.md` · `epic-prd.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · `epic-review.md`

**Outputs**: updated `epic-prd.md` or `epic-arch.md` · completed review section with sign-off (PM for prd, Tech Lead for arch) · decisions recorded in `docs/decisions.md`

## Steps

1. Verify `epic-review.md` exists and read it
2. Auto-verify the mechanical items (completeness, testable criteria, valid references, consistency with parent docs) and collapse them to one summary line. Fix trivial gaps directly
3. Present **Decisions requiring your validation** (max 10 plain sentences) plus open questions, blocking first:
   - prd: scope, priorities, user journeys, success criteria, what is out of scope
   - arch: end-to-end data path, API contracts, data model choices, technology choices, security/performance trade-offs.
4. Apply the feedback to the reviewed document. If a change contradicts a recorded decision in `docs/decisions.md`, surface the conflict and ask.
5. Append validated decisions to `docs/decisions.md`
6. Mark the review signed off. If major changes were requested, note it; the derived status will reflect document reality via Status Sync.
7. Run Status Sync. Handoff: after prd approval → `plan/epic-arch E{n}`; after arch approval → `plan/feat E{n} F1`
