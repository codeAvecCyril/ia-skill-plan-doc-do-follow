# plan/epic-arch E{n} — Epic Architecture

**Purpose**: design the technical architecture for an epic. This is the primary architecture level — features inherit from it and normally only declare deltas

**Mindset**: staff architect — trace every data path end to end, prefer the simplest design that survives the stated scale, justify choices against alternatives. Strong model, deep thinking

**Inputs**: `epic-prd.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · `docs/data-model.md` (if it exists) · related epic architectures if applicable

**Outputs**: `epic-arch.md` · updated `docs/data-model.md` (new entities/relations) · updated `docs/ui-map.md` (new navigation sections/screens, if UI) · updated `epic-review.md` (Architecture review gate prepared for the Tech Lead)

## Steps

1. Verify `docs/project-status.md` contains `E{n}` and read `epic-prd.md`
2. Design: components, data model, APIs, integration points, risks, metrics. Where a topic does not differ from `docs/global_architecture.md`, write one sentence referencing it instead of restating it. In a brownfield codebase, ground the design first: send precise questions about existing patterns, schema, and integration points to a **repo-scout** subagent (`subagents/repo-scout.md`)
3. Ask interactive questions for any ambiguity in architectural decisions or constraints
4. Generate `epic-arch.md` from `templates/epic-arch.md`. Delete non-applicable sections
5. Sync the living docs in the same change (Invariant 10):
   - New or changed entities → `docs/data-model.md` (the global truth; `epic-arch.md` only describes the delta and links to it)
   - New screens or navigation sections → `docs/ui-map.md`
6. Run the **arch-critic** subagent (`subagents/arch-critic.md`) with its scoped inputs; apply its findings or record why they were rejected. Then check the trigger criteria at the top of `subagents/perf-critic-backend.md` and `subagents/perf-critic-frontend.md`: for each side that fires, run that perf critic on the design and resolve its blocker findings; if none fires, skip and note it
7. **Update `epic-review.md`** (the same file as the PRD review — one review file per epic, one section per gate): auto-verify the "Details — Architecture review" checklist and collapse it to one summary line; add an **"Architecture — Decisions Requiring Your Validation"** subsection (max 10 plain sentences a tech lead can validate in isolation: end-to-end data path, API contracts, data model choices, technology choices, trade-offs) plus arch-specific open questions labeled blocking / important / minor; add or reset the Technical Lead sign-off row to ⚪ pending. Leave every PRD-review section untouched
8. Handoff with `plan/epic-review E{n} arch` (or `plan/feat E{n} F1` if the user skips reviews) as default next command
