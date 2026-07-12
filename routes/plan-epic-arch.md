# plan/epic-arch E{n} — Epic Architecture

**Purpose**: design the technical architecture for an epic. This is the primary architecture level — features inherit from it and normally only declare deltas.

**Inputs**: `epic-prd.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · `docs/data-model.md` (if it exists) · related epic architectures if applicable.

**Outputs**: `epic-arch.md` · updated `docs/data-model.md` (new entities/relations) · updated `docs/ui-map.md` (new navigation sections/screens, if UI).

## Steps

1. Verify `docs/project-status.md` contains `E{n}` and read `epic-prd.md`.
2. Design: components, data model, APIs, integration points, risks, metrics. Where a topic does not differ from `docs/global_architecture.md`, write one sentence referencing it instead of restating it.
3. Ask interactive questions for any ambiguity in architectural decisions or constraints.
4. Generate `epic-arch.md` from `template-epic-arch.md`. Delete non-applicable sections.
5. Sync the living docs in the same change (Invariant 10):
   - New or changed entities → `docs/data-model.md` (the global truth; `epic-arch.md` only describes the delta and links to it).
   - New screens or navigation sections → `docs/ui-map.md`.
6. Run the **Arch Critic** subagent (`reviewers.md`) with its scoped inputs; apply its comments or record why they were rejected.
7. Handoff with `@plan/epic-review E{n} arch` (or `@plan/feat E{n} F1` if the user skips reviews) as default next command.
