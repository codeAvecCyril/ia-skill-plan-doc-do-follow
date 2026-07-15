# plan/feat-arch E{n} F{n} — Feature Architecture (exception cases only)

**Purpose**: design a dedicated feature architecture. **Most features do not need this route** — the epic architecture plus the Architecture Delta section of `feat-prd.md` is normally enough.

**Mindset**: staff architect on a scoped delta — design only what the epic architecture does not already cover. Strong model, deep thinking.

## Trigger criteria — run this route only if at least one applies

1. The feature introduces a **new external integration** (third-party API, message broker, new infrastructure service).
2. The feature introduces a **new data entity** (not just columns on existing entities).
3. The feature introduces a **new service, module, or architectural component** not described in `epic-arch.md`.
4. The feature opens a **new security surface** (new auth flow, new exposure of sensitive data, new public endpoint class).
5. The **user explicitly requests** a feature architecture.

If none applies, say so, keep the Architecture Delta in `feat-prd.md` as the architectural record, and route to `@plan/tasks E{n} F{n}`.

**Inputs**: `feat-prd.md` · `epic-arch.md` · `docs/technical-stack.md` · `docs/data-model.md` (if it exists).

**Outputs**: `features/{feat-slug}/feat-arch.md` · updated `docs/data-model.md` and `docs/ui-map.md` if affected.

## Steps

1. Verify `E{n}`/`F{n}` exist and state which trigger criterion fired.
2. Design **only the delta**: what this feature adds or changes relative to `epic-arch.md`. Where a topic is already covered by the epic architecture, write one sentence referencing it. Ground unverified assumptions about existing code via a **repo-scout** subagent (`subagents/repo-scout.md`).
3. Ask interactive questions for any ambiguity in architectural decisions or constraints.
4. Generate `feat-arch.md` from `templates/feat-arch.md`; delete non-applicable sections.
5. Sync the living docs in the same change: new entities → `docs/data-model.md`; new screens/navigation → `docs/ui-map.md`.
6. Run the **arch-critic** subagent (`subagents/arch-critic.md`) with its scoped inputs; apply its findings or record why they were rejected. Then check the trigger criteria at the top of `subagents/perf-critic-backend.md` and `subagents/perf-critic-frontend.md`: for each side that fires, run that perf critic on the design and resolve its blocker findings; if none fires, skip and note it.
7. **Update `feat-review.md`** (create it from `templates/feat-review.md` if it does not exist yet): auto-verify the architecture checklist and collapse it to one summary line; add an **"Architecture — Decisions Requiring Your Validation"** subsection (max 10 plain sentences) plus arch-specific open questions labeled blocking / important / minor; add or reset the Technical Lead sign-off row to ⚪ pending. Leave any PRD-review content untouched.
8. Handoff with `@plan/feat-review E{n} F{n} arch` or `@plan/tasks E{n} F{n}` as default next command.
