# plan/tasks E{n} F{n} — Task Breakdown

**Purpose**: break feature into self-contained tasks executable by weaker model (Invariant 11) that together tell every user story start to finish (Invariant 18)

**Mindset**: tech lead writing instructions for junior who cannot ask questions — everything explicit, nothing assumed · and storyteller: "to prove the solution, tell its story from start to finish, seamlessly and precisely — trace every process and data flow until the user receives exactly what they expect", for processing logic and for the screen alike · strong model, deep thinking. Executors will follow this plan without questioning it — a hole left here becomes a redesign later

**Inputs**: `feat-prd.md` (incl. Architecture Delta) · `feat-arch.md` if it exists · `epic-arch.md` · `docs/patterns/` · `docs/ui-map.md` if UI · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: `{feat-slug}/feat-tasks.md` — owns task statuses; carries Story Trace and Shared Contracts

## Task quality bar — task-checker verifies exactly these six checks

1. **Self-contained**: executable from task text alone, PRD and architecture closed — WHAT / WHERE / HOW / WHY / DONE all explicit
2. **Precise**: exact file paths, concrete steps, validation commands runnable as written
3. **No external references**: never "as described in the PRD" / "see architecture" — inline content instead
4. **Testable DONE**: observable outcomes (command passes, file exists, behavior exercisable), not intentions
5. **Sized**: one concern, 30–60 minutes
6. **Story continuity**: every acceptance criterion appears in Story Trace · every hop owned by a task · producer and consumer of each hop agree exactly per Shared Contracts · no orphan task

## Steps

1. Verify feature is 🟡 in `epic-status.md` · if Architecture Delta flagged `plan/feat-arch` trigger and no `feat-arch.md` exists, recommend running it first
2. Read inputs; extract user stories and acceptance criteria **verbatim**
3. **Tell each story first, before splitting**: trigger (user action, schedule, external event) → input validation → processing → stored data → read path → API → screen state → exact result the criterion promises. Walk the UX journey too: entry point, loading / empty / error states, feedback after action. Any hop you cannot name concretely (which table, which field, which endpoint, which component) = design hole → close it now from architecture or code (SKILL.md inline-first), or ask user (blocking, per `guides/review-questions.md`) — never leave it to execution
4. **Fix Shared Contracts**: each interface crossing tasks (endpoint + payload, table/columns, event/message, component input/output, config key) defined once — exact names, shapes, units, timezone, null/empty behavior · producer task · consumer tasks
5. Build dependency DAG: data → business logic → API → UI, tests interleaved · identify parallelizable tasks · if change can break existing tests, add task to adapt them
6. Generate `feat-tasks.md` from `templates/feat-tasks.md` against quality bar · Story Trace maps each criterion to its hop chain and tasks · each task inlines the Shared Contract lines it produces or consumes (self-containment) · **Task Summary table = single source of truth for task status** — per-task sections carry no status line · solo mode: omit effort/owner columns
7. **Self-review before checking**: re-read every task against checks 1–5 · then **replay each story through task texts only**, as executors will see them: does each task's output match the next task's input word for word, and does the user end up with exactly what the criterion promises? Fix every break
8. `pddf lint-tasks E{n} F{n} --strict` until 0 FAIL · then run **task-checker** subagent with `feat-tasks.md` + acceptance criteria list verbatim + lint output · fix every FAIL, re-run **at most once** on previously failing items only · if anything still fails, fix against checker's quoted gaps and proceed — note it in handoff · MINOR notes optional polish, never re-run triggers
9. Run Status Sync (feature 🟣; epic may follow) · **no changelog entry** (changelog hard rule); checker exchange never appears anywhere (Invariant 16) · Handoff: `do/all-tasks E{n} F{n}` (or `do/task E{n} F{n} T1`)
