# plan/redesign E{n} F{n} — Close Design Gap Found During Execution

**Purpose**: resolve gap(s) recorded in `feat-tasks.md` → Design Gaps with one holistic re-plan, so the fix stays consistent across every task and story · feature scope unchanged — scope change → `plan/change`

**Mindset**: staff architect returning to own plan with fresh eyes — re-tell the whole story, not just the broken sentence · strong model, deep thinking · fresh context: ignore execution chatter, re-read documents and code

**Inputs**: open gap records · `feat-prd.md` (stories, acceptance criteria, Architecture Delta) · `feat-arch.md` if it exists · `epic-arch.md` · whole `feat-tasks.md` (done and pending) · code written by 🟢 tasks (SKILL.md inline-first) · `docs/data-model.md` / `docs/ui-map.md` if touched

**Outputs**: amended Architecture Delta or `feat-arch.md` · pending tasks amended + corrective tasks appended · Story Trace and Shared Contracts updated · gaps closed · living docs synced · if user-visible behavior must change: decision items in `feat-review.md`

## Steps

1. **Confirm each gap**: restate in two plain sentences — what plan assumed · what reality is · open cited evidence yourself. Not confirmed → close gap as `follow-plan` with one-line reason, handoff `do/all-tasks E{n} F{n}`
2. **Re-tell every impacted story end to end** with reality as it is: trigger → processing → stored data → screen → user result. Mark each hop unchanged / changed / new · look beyond reported gap: same wrong assumption elsewhere?
3. **Classify**:
   - (a) **design-only** — user still gets exactly what PRD promises → step 4
   - (b) **behavior change** — a PRD promise cannot hold as written → add "Redesign — Decisions Requiring Your Validation" to `feat-review.md` per `guides/review-questions.md` (what users would get differently, options, impact of each, recommendation) · leave tasks untouched · Status Sync · handoff `plan/feat-review E{n} F{n} prd`, then `plan/redesign` again · real scope change → `plan/change`
4. **Design the fix once, globally**: simplest change closing every confirmed gap while keeping every story whole · check against `epic-arch.md` and Shared Contracts · update Architecture Delta (or `feat-arch.md`) and living docs in same change (Invariant 10)
5. **Amend tasks**: pending tasks (⚪, or 🔵 not accepted) edited in place · 🟢 tasks never rewritten — append corrective tasks `T{next}…` depending on what they fix · update Task Summary, Story Trace, Shared Contracts · every amended or new task meets `plan/tasks` quality bar
6. **Self-review**: replay each impacted story through task texts only · `pddf lint-tasks E{n} F{n}` until 0 FAIL · run **task-checker** on amended + new tasks with acceptance criteria list · one re-run max
7. **Close gaps**: `G{n} … · closed {date}: {one-line fix} → T{…}` · Status Sync (appended ⚪ tasks keep feature 🔵) · no changelog entry (scope unchanged)
8. Handoff: `do/all-tasks E{n} F{n}` (resumes from Task Summary)
