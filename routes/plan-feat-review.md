# plan/feat-review E{n} F{n} {prd|arch} — Feature Review

**Purpose**: validate the feature specification (prd) or architecture (arch) with stakeholders

**Mindset**: review facilitator — protect the human's time; surface only genuine judgment calls, in plain sentences

**Inputs**:
- prd: `feat-prd.md` · `feat-review.md` · epic PRD for context
- arch: `feat-arch.md` (or the Architecture Delta of `feat-prd.md`) · `feat-review.md`

**Outputs**: updated `feat-prd.md` or `feat-arch.md` · signed-off review section (PM for prd, Tech Lead for arch) · decisions in `docs/decisions.md`

## Steps

1. Verify `feat-review.md` exists and read it
2. Auto-verify the mechanical items (stories testable, criteria measurable, edge cases listed, out-of-scope defined, entry point in `docs/ui-map.md` for UI); collapse to one summary line. Fix trivial gaps directly
3. Read user answers in **Decisions requiring your validation** plus open questions, blocking first
4. Apply the answers **as written** — record verbatim, never paraphrase, never re-ask (if ambiguous, ask only the clarification). If a change contradicts `docs/decisions.md`, surface the conflict and ask
5. Append validated decisions to `docs/decisions.md`
6. Mark the review signed off
7. Run Status Sync. No changelog entry (changelog hard rule). Handoff: `plan/tasks E{n} F{n}` (default), or `plan/feat-arch E{n} F{n}` if the Architecture Delta flagged trigger criteria
