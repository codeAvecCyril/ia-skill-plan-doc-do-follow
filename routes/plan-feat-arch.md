# plan/feat-arch E{n} F{n} — Feature Architecture (exception cases only)

**Purpose**: design a dedicated feature architecture. **Most features do not need this** — the epic architecture plus the PRD's Architecture Delta is normally enough

**Mindset**: staff architect on a scoped delta — design only what the epic architecture does not cover. Strong model, deep thinking

## Trigger criteria — run only if at least one applies

1. New **external integration** (third-party API, message broker, new infrastructure service)
2. New **data entity** (not just columns on existing entities)
3. New **service, module, or architectural component** not in `epic-arch.md`
4. New **security surface** (new auth flow, new sensitive-data exposure, new public endpoint class)
5. The **user explicitly requests** it

If none applies: say so, keep the Architecture Delta as the record, route to `plan/tasks E{n} F{n}`

**Inputs**: `feat-prd.md` · `epic-arch.md` · `docs/technical-stack.md` · `docs/data-model.md` (if it exists)

**Outputs**: `{feat-slug}/feat-arch.md` · updated `docs/data-model.md` and `docs/ui-map.md` if affected

## Steps

1. Verify `E{n}`/`F{n}` exist and state which trigger criterion fired
2. Design **only the delta** vs `epic-arch.md`; where covered, one referencing sentence. Ground unverified assumptions about existing code via a **repo-scout** subagent
3. Ask questions on any architectural ambiguity (Invariant 8)
4. Generate `feat-arch.md` from `templates/feat-arch.md`
5. Sync living docs in the same change: entities → `docs/data-model.md`; screens/navigation → `docs/ui-map.md`
6. Run the **arch-critic** subagent and handle its findings (SKILL.md → Subagents). Check the perf-critic trigger criteria (top of their files): run each side that fires, resolve blockers; if none fires, skip and note it
7. **Update `feat-review.md`** (create from `templates/feat-review.md` if missing): auto-verify the architecture checklist, collapse to one line; add **"Architecture — Decisions Requiring Your Validation"** (max 10 plain sentences) plus arch-specific open questions; set the Tech Lead sign-off row to ⚪ pending. Leave PRD-review content untouched
8. Handoff: `plan/feat-review E{n} F{n} arch` or `plan/tasks E{n} F{n}`
