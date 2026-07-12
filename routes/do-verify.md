# do/verify E{n} F{n} — Feature Completion Verification

**Purpose**: verify a feature meets its requirements. This is the **only route allowed to set a feature to 🟢 DONE**.

**Inputs**: `feat-prd.md` (acceptance criteria) · `feat-tasks.md` · implemented code and tests · `docs/ui-map.md` and `docs/design-guidelines.md` for UI features · `docs/data-model.md` if schema was touched.

**Outputs**: verification summary · feature 🟢 (or 🔵 with gap list) via Status Sync · updated living docs if gaps were found there.

## Verification gates

1. All acceptance criteria in `feat-prd.md` are met (check each one explicitly).
2. Linters/formatters pass; all tests pass; coverage meets the project's target (default ≥ 80% on new code) where coverage tooling exists.
3. **Data gate**: if the feature touched schema or migrations, `docs/data-model.md` reflects the change — otherwise verification fails.
4. **UI gate**: if the feature has UI requirements, its entry point exists in `docs/ui-map.md` and the **UI Consistency Reviewer** subagent (`reviewers.md`) passes; apply its findings before approving.
5. No breaking changes to existing behavior; documentation the PRD required is present.

## Steps

1. Read `feat-prd.md` acceptance criteria and review the implemented code and tests.
2. Run gates 1–5 in order; fix straightforward issues (lint, doc sync) directly.
3. If all gates pass: set the feature to 🟢 and run Status Sync. If the epic thereby completes, run the **Doc Coherence Reviewer** subagent (`reviewers.md`) and fix reported drift.
4. If a gate fails: keep the feature 🔵, list each gap as a complete sentence with what is needed to close it, and run Status Sync.
5. Handoff: `@plan/feat E{n} F{n+1}`, `@plan/epic E{n+1}` if the epic is done, or the gap list with the recommended fixing route.
