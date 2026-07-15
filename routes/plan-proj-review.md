# plan/proj-review — Project Review

**Purpose**: validate the extracted epics with stakeholders.

**Mindset**: review facilitator — protect the human's time; surface only genuine judgment calls, in plain sentences.

**Inputs**: `docs/project-status.md` · epic briefs · `docs/project-review.md`.

**Outputs**: updated `docs/project-status.md` and epic briefs · completed review with sign-off · decisions recorded in `docs/decisions.md`.

## Steps

1. Verify `docs/project-review.md` exists and read it.
2. Auto-verify the mechanical items (documents exist, epics have value statements, dependencies form a valid graph, no orphan references) and collapse them to one summary line in the review document.
3. Present the **Decisions requiring your validation** section to the user: at most 10 plain-sentence statements covering epic scope and sizing, priority sequencing, and timeline realism. Ask the open questions (blocking first).
4. Apply the feedback: adjust epic scopes, priorities, and phases in `docs/project-status.md` and the briefs.
5. Append each validated decision to `docs/decisions.md` (one line: date, decision, why, decided by).
6. Mark the review as signed off.
7. Run Status Sync. Handoff with `@plan/epic E{n}` (highest-priority unblocked epic) as default next command.
