# plan/feat-arch E{n} F{n} — Feature Architecture (exception cases only)

**Purpose**: design a dedicated feature architecture. **Most features do not need this route** — the epic architecture plus the Architecture Delta of `feat-prd.md` is normally enough

**Mindset**: staff architect on a scoped delta — design only what the epic architecture does not already cover. Strong model, deep thinking

## Trigger criteria — run only if at least one applies

1. New **external integration** (third-party API, message broker, new infrastructure service)
2. New **data entity** (not just columns on existing entities)
3. New **service, module, or architectural component** not described in `epic-arch.md`
4. New **security surface** (new auth flow, new exposure of sensitive data, new public endpoint class)
5. The **user explicitly requests** a feature architecture

If none applies, say so, keep the Architecture Delta in `feat-prd.md` as the architectural record, and route to `plan/tasks E{n} F{n}`

**Inputs**: `feat-prd.md` · `epic-arch.md` · `docs/technical-stack.md` · `docs/data-model.md` (if it exists)

**Outputs**: `{feat-slug}/feat-arch.md` · updated `docs/data-model.md` and `docs/ui-map.md` if affected

## Steps

1. Verify `E{n}`/`F{n}` exist and state which trigger criterion fired
2. Design **only the delta** relative to `epic-arch.md`; where a topic is already covered, write one sentence referencing it. Ground unverified assumptions about existing code via a **repo-scout** subagent
3. Ask questions on any ambiguity in architectural decisions or constraints (Invariant 8)
4. Generate `feat-arch.md` from `templates/feat-arch.md`
5. Sync the living docs in the same change: new entities → `docs/data-model.md`; new screens/navigation → `docs/ui-map.md`
6. Run the **arch-critic** subagent and handle its findings (SKILL.md → Subagents). Then check the perf-critic trigger criteria (top of `subagents/perf-critic-backend.md` and `-frontend.md`): run each side that fires on the design and resolve its blocker findings; if none fires, skip and note it
7. **Update `feat-review.md`** (create from `templates/feat-review.md` if missing): auto-verify the architecture checklist and collapse it to one summary line; add an **"Architecture — Decisions Requiring Your Validation"** subsection (max 10 plain sentences) plus arch-specific open questions; add or reset the Technical Lead sign-off row to ⚪ pending. Leave any PRD-review content untouched
8. Handoff: `plan/feat-review E{n} F{n} arch` or `plan/tasks E{n} F{n}`
