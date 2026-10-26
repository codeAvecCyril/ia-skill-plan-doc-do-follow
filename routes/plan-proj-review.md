# plan/proj-review — Project Review

**Purpose**: validate extracted epics with stakeholders

**Mindset**: review facilitator — protect human's time · surface only genuine judgment calls, in plain sentences

**Inputs**: `docs/project-status.md` · epic briefs · `docs/project-review.md`

**Outputs**: updated `docs/project-status.md` and briefs (answers applied) · signed-off review with answers recorded verbatim

## Steps

1. Verify `docs/project-review.md` exists · `pddf review-open` lists unanswered items — read only those sections
2. Auto-verify mechanical items (documents exist, value statements present, dependency graph valid, no orphan references); collapse to one summary line
3. Present **Decisions requiring your validation** (≤10 items: epic scope/sizing, priority sequencing, timeline realism) plus open questions, blocking first · every item per `guides/review-questions.md` — rewrite any item failing its self-check before presenting
4. Apply answers **as written** into `docs/project-status.md` and briefs (scopes, priorities, phases) — reviewed docs carry decision from now on · record answer verbatim under its item · never paraphrase, never re-ask (if ambiguous, ask only clarification)
5. Mark review signed off
6. Run Status Sync · Handoff: `plan/epic E{n}` (highest-priority unblocked epic)
