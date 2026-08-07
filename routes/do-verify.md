# do/verify E{n} F{n} — Feature Completion Verification

**Purpose**: verify feature meets requirements. Gates below = **only path to 🟢 DONE** — run when tasks executed one at a time (`do/task`) or on demand; `do/all-tasks` runs same gates inline as final phase

**Mindset**: skeptical QA gatekeeper — assume incomplete until each gate proves otherwise; balance laxity and perfectionism; focus on what really matters

**Inputs**: `feat-prd.md` (acceptance criteria) · `feat-tasks.md` · implemented code and tests · `docs/ui-map.md` and `docs/design-guidelines.md` for UI features · `docs/data-model.md` if schema touched

**Outputs**: verification summary · feature 🟢 (or 🔵 with gap list) via Status Sync · updated living docs if gaps found there

## Verification gates

1. All acceptance criteria in `feat-prd.md` met (check each explicitly)
2. Linters/formatters pass; all tests pass; coverage meets project target (default ≥ 80% on new code) where tooling exists
3. **Data gate**: schema/migrations touched → `docs/data-model.md` reflects change, else fail
4. **UI gate**: UI requirements → entry point exists in `docs/ui-map.md` and ui-consistency checks pass. Small surface (1–2 components): run **ui-consistency-reviewer** checklist yourself (inline-first); spawn only for broader surface, apply blocking findings
5. **Performance gate (conditional)**: check perf-critic trigger criteria (top of `subagents/perf-critic-backend.md` and `-frontend.md`); run each side that fires on hot paths, resolve blockers; if none fires, skip and note it
6. No breaking changes to existing behavior; PRD-required documentation present

## Steps

1. Read acceptance criteria; review implemented code and tests
2. Run gates 1–6 in order; fix straightforward issues (lint, doc sync) directly
3. All gates pass → feature 🟢, run Status Sync. Changelog per hard rule: one line ≤25 words in epic changelog (`{date}: F{n} {name} verified 🟢`), plus one project-changelog line **only if epic completes** — never gate results or `Next:` commands. On epic completion, run **doc-coherence-reviewer** subagent and fix reported drift
4. Any gate fails → feature stays 🔵, list each gap as complete sentence with what closes it, run Status Sync
5. Handoff: `plan/feat E{n} F{n+1}`, `plan/epic E{n+1}` if epic done, or gap list with recommended fixing route
