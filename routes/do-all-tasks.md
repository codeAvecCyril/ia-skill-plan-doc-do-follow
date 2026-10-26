# do/all-tasks E{n} F{n} — Execute All Feature Tasks

**Purpose**: execute all feature tasks in dependency-ordered waves of **feature-coder** subagents, run by **feature-coordinator**, then verify inline — no separate `do/verify` pass

**Mindset**: adopt `subagents/feature-coordinator.md` in full — principal = coordinator: owns plan fidelity, code quality, live Task Summary, user feedback · reasoning-class model recommended for principal; coders run standard model, medium thinking

**Inputs**: `feat-tasks.md` · `subagents/feature-coordinator.md` · `subagents/feature-coder.md` · repository instruction file(s) (SKILL.md → Platform integration) · `routes/do-verify.md` for final phase · `routes/plan-redesign.md` only on design gap

**Outputs**: implemented code and tests · Task Summary updated after **each** task · progress report after each wave · feature 🟢 (or 🔵 with gap list) · statuses cascaded via Status Sync

## Steps

1. **Preflight**: `pddf lint-tasks E{n} F{n}` (FAIL → triage: local defect = fix-packet, contradiction = redesign) · `pddf waves E{n} F{n}` · read Story Trace, Shared Contracts, Design Gaps via `pddf section` — never Task Details · open gap → stop, handoff `plan/redesign E{n} F{n}` · resume-safe: skip 🟢 rows, re-dispatch 🔵 rows whose work is absent · post one line: `{n} tasks · {w} waves · critical path {…}`
2. **Dispatch wave**: `pddf task … 🔵` (first call writes Execution line with `--wave`) · one feature-coder per task · brief = identical head (Tooling one-liner, "obey `feature-coder` rules") + tail `Run: pddf packet E{n} F{n} T{n} — its output is your whole task packet` — packet by reference, never retyped · coder without shell → paste `pddf packet` output · never PRD, architecture, or whole tasks file
3. **Accept each task as it returns** (coordinator → Acceptance): accepted → `pddf task … 🟢 --wave k/w --eta {eta}` immediately · rejected → re-dispatch with concrete feedback (max 2 retries) · escalation → coordinator → Escalation triage. Coder questions never reach user
4. **Close wave**: run linter/formatter and wave's targeted tests; fix integration breaks · `pddf sync` · progress report (coordinator → Reports) · continue straight to next wave — never ask "continue?"
5. Inherently sequential tasks (final integration tests, ordered migrations): dispatch singly, or implement inline under `subagents/feature-coder.md` discipline
6. **Design gap** (triage verdict `redesign`): stop dispatching tasks that depend on the gap; let independent in-flight tasks finish and accept them · gap recorded in Design Gaps · run `plan/redesign E{n} F{n}`: inline if principal is reasoning-class (load route, re-read PRD/architecture/tasks fresh — set execution context aside), else stop with handoff `plan/redesign E{n} F{n}` on a strong model · after redesign, resume at step 1
7. **Verification phase** — all tasks 🟢: run gates of `routes/do-verify.md` inline, incl. Story walk (conditional subagents where triggers fire; inline-first for small surfaces). All pass → feature 🟢, remove Execution line; any fail → 🔵 with each gap as complete sentence
8. Run Status Sync. Changelog per hard rule: one feature-verified 🟢 line in epic changelog (project changelog only on epic completion) — never waves, gates, or task details · final report (coordinator → Reports) · Handoff: `plan/feat E{n} F{n+1}`, `plan/epic E{n+1}` if epic done, or gap list with recommended fixing route
