# plan/proj-review — Project Review

**Purpose**: validate extracted epics with stakeholders

**Mindset**: review facilitator — protect human's time · surface only genuine judgment calls, in plain sentences

**Inputs**: `docs/project-status.md` · epic briefs · `docs/project-review.md`

**Outputs**: updated `docs/project-status.md` and briefs · signed-off review · decisions in `docs/decisions.md`

## Steps

1. Verify `docs/project-review.md` exists and read it
2. Auto-verify mechanical items (documents exist, value statements present, dependency graph valid, no orphan references); collapse to one summary line
3. Present **Decisions requiring your validation** (≤10 plain sentences: epic scope/sizing, priority sequencing, timeline realism) plus open questions, blocking first
4. Apply answers **as written**: adjust scopes, priorities, phases — record verbatim, never paraphrase, never re-ask (if ambiguous, ask only clarification)
5. Append each validated decision to `docs/decisions.md` (date, decision, why, decided by)
6. Mark review signed off
7. Run Status Sync · Handoff: `plan/epic E{n}` (highest-priority unblocked epic)
