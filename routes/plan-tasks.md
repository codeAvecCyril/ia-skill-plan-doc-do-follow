# plan/tasks E{n} F{n} — Task Breakdown

**Purpose**: break feature into self-contained tasks executable by weaker model (Invariant 11) that together tell every user story start to finish (Invariant 18) — and finish fast: optimize whole-feature velocity, not per-task thoroughness

**Mindset**: tech lead writing instructions for junior who cannot ask questions — everything explicit, nothing assumed · and storyteller: "to prove the solution, tell its story from start to finish, seamlessly and precisely — trace every process and data flow until the user receives exactly what they expect", for processing logic and for the screen alike · strong model, deep thinking. Executors will follow this plan without questioning it — a hole left here becomes a redesign later

**Inputs**: `feat-prd.md` (incl. Architecture Delta) · `feat-arch.md` if it exists · `epic-arch.md` · `docs/patterns/` · `docs/ui-map.md` if UI · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: `{feat-slug}/feat-tasks.md` — owns task statuses; carries Story Trace, Shared Contracts, Lanes

## Test strategy — verify once, at the right place

Repeating the same verification in every task = slowest path. Split:

- **Implementation task**: DONE = behavior + **Smoke check** — one fast command proving code loads and the happy path runs (typecheck/lint of touched files, one happy-path test, or touched module's existing tests) · scoped, seconds to ~2 min · never full suite, never edge-case matrix
- **Test task** (Type `Test`): owns edge cases, error paths, empty states, story-level/integration tests · **Covers** list = criteria ids + edge cases it proves · one per story slice or layer, not one per implementation task · depends on its producers only, so it runs in parallel with downstream implementation
- **Risk-critical step** (money math, migration, data loss, security, trust-boundary validation): mark `risk-critical` in task, test it in same task — a defect there corrupts data before any Test task runs
- Change can break existing tests → one Test task adapts them
- Full suite: once, verification phase — never in a task

### Test tiers — fast suite stays fast (Invariant 20)

- Every Test task declares `**Tier**: fast | slow` · threshold + tag mechanism from Tooling `Slow tests:` line (missing → 2 s per test, tag `slow`)
- **slow** = performance, load, volume/large dataset, real timing or sleep, real network, anything inherently over threshold · always its own Test task, never mixed with fast tests · states `**Expected runtime**: ~N min` (whole validation command) · every test tagged with project's slow mechanism
- **fast** = everything else · Smoke checks always fast · fast test needing big data → smallest dataset proving the rule; volume proof goes to a slow task
- Slow Test task depends only on its producers, off critical path, never in a lane with fast work

## Lanes — dispatch units

Task = unit of status, acceptance, retry, handover (stays 30–60 min). **Lane** = ordered chain of tasks one coder runs back to back, reusing its context: fewer cold starts, internal interfaces held by one mind

- Lane = `T{a} → T{b} → …` where each next task depends on previous · listed contiguous, in order, in Task Summary · `Lane` column `L{n}`, `—` for solo task
- Merge into lane: every link where producer has one successor and consumer one predecessor, same layer + toolchain · join (task with several predecessors) may extend lane whose branch finishes last — other branch expected done first
- Never in one lane: backend + frontend (different toolchain) · Test task + its producers (tests need independent eyes — Test tasks may form own lane) · fast + slow tier · more than 4 tasks or ~2 h estimated work
- Shared Contracts still list in-lane interfaces: lane may be split on retry
- Example: T1 → T2 → T3 · T3 → T4 → T5 · T3 → T6 · T5,T6 → T7 ⇒ L1 = T1–T3 · L2 = T4, T5, T7 (if T6 shorter) · T6 solo

## Task quality bar — task-checker verifies exactly these eight checks

1. **Self-contained**: executable from task text alone, PRD and architecture closed — WHAT / WHERE / HOW / WHY / DONE all explicit
2. **Precise**: exact file paths, concrete steps, validation commands runnable as written
3. **No external references**: never "as described in the PRD" / "see architecture" — inline content instead
4. **Testable DONE**: observable outcomes (command passes, file exists, behavior exercisable), not intentions
5. **Sized**: one concern, 30–60 minutes
6. **Story continuity**: every acceptance criterion appears in Story Trace · every hop owned by a task · producer and consumer of each hop agree exactly per Shared Contracts · no orphan task
7. **Test placement**: every Story Trace row names its Test task in **Tested by** · implementation tasks carry Smoke check only, except risk-critical steps · no verification repeated across tasks · every Test task has Tier; slow work never in fast tier
8. **Lanes**: each lane a sequential chain, one layer/toolchain, ≤4 tasks · no Test task with its producer · no obvious chain left unmerged

## Steps

1. Verify feature is 🟡 in `epic-status.md` · if Architecture Delta flagged `plan/feat-arch` trigger and no `feat-arch.md` exists, recommend running it first
2. Read inputs; extract user stories and acceptance criteria **verbatim**
3. **Tell each story first, before splitting**: trigger (user action, schedule, external event) → input validation → processing → stored data → read path → API → screen state → exact result the criterion promises. Walk the UX journey too: entry point, loading / empty / error states, feedback after action. Any hop you cannot name concretely (which table, which field, which endpoint, which component) = design hole → close it now from architecture or code (SKILL.md inline-first), or ask user (blocking, per `guides/review-questions.md`) — never leave it to execution
4. **Fix Shared Contracts**: each interface crossing tasks (endpoint + payload, table/columns, event/message, component input/output, config key) defined once — exact names, shapes, units, timezone, null/empty behavior · producer task · consumer tasks
5. Build dependency DAG: data → business logic → API → UI · place Test tasks per Test strategy and Test tiers, right after their producers, off the critical path where possible · identify parallelizable tasks · group chains into Lanes
6. Generate `feat-tasks.md` from `templates/feat-tasks.md` against quality bar · Story Trace maps each criterion to its hop chain, tasks, and Test task (**Tested by**) · each task inlines the Shared Contract lines it produces or consumes (self-containment) · **Task Summary table = single source of truth for task status** — per-task sections carry no status line · solo mode: omit effort/owner columns
7. **Self-review before checking**: re-read every task against checks 1–5, 7, 8 · then **replay each story through task texts only**, as executors will see them: does each task's output match the next task's input word for word, and does the user end up with exactly what the criterion promises? Fix every break
8. `pddf lint-tasks E{n} F{n} --strict` until 0 FAIL · then run **task-checker** subagent with `feat-tasks.md` + acceptance criteria list verbatim + lint output · fix every FAIL, re-run **at most once** on previously failing items only · if anything still fails, fix against checker's quoted gaps and proceed — note it in handoff · MINOR notes optional polish, never re-run triggers
9. Run Status Sync (feature 🟣; epic may follow) · **no changelog entry** (changelog hard rule); checker exchange never appears anywhere (Invariant 16) · Handoff: `do/all-tasks E{n} F{n}` (or `do/task E{n} F{n} T1`)
