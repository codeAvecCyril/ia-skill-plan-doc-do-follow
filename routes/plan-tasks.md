# plan/tasks E{n} F{n} — Task Breakdown

**Purpose**: break a feature into self-contained implementation tasks executable by a weaker model (Invariant 11)

**Mindset**: tech lead writing instructions for a junior who cannot ask questions — everything explicit, nothing assumed. Strong model; the intelligence goes into the tasks so execution doesn't need it

**Inputs**: `feat-prd.md` (including its Architecture Delta) · `feat-arch.md` if it exists · `epic-arch.md` · `docs/patterns/` · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: `{feat-slug}/feat-tasks.md` — the owning file for task statuses

## Task quality bar — the task-checker verifies exactly these five checks

Write every task to pass them on the first draft:

1. **Self-contained**: executable from the task text alone, PRD and architecture closed — WHAT / WHERE / HOW / WHY / DONE all explicit
2. **Precise**: exact file paths, concrete steps, validation commands runnable as written
3. **No external references**: never "as described in the PRD" / "see architecture" — inline the needed content in the task instead
4. **Testable DONE**: observable outcomes (a command passes, a file exists, behavior can be exercised), not intentions
5. **Sized**: one concern, 30–60 minutes

## Steps

1. Verify the feature is 🟡 in `epic-status.md`; if the Architecture Delta flagged a `plan/feat-arch` trigger and no `feat-arch.md` exists, recommend running it first
2. Read the inputs; extract requirements and acceptance criteria
3. Build the dependency DAG: data → business logic → API → UI, tests interleaved; identify parallelizable tasks
4. If the change can break existing tests from previous features, add a task to adapt them
5. Generate `feat-tasks.md` from `templates/feat-tasks.md`, writing each task against the quality bar. The **Task Summary table is the single source of truth for task status** — per-task sections carry no status line. Solo mode: omit effort/owner columns
6. **Self-review before checking**: re-read every task against the five checks and fix gaps yourself — the checker is a safety net, not the editor
7. Run the **task-checker** subagent on `feat-tasks.md`. Fix every FAIL, then re-run **at most once**, passing only the previously failing tasks. If anything still fails after the second run, fix it against the checker's quoted gaps and proceed — note it in the handoff. Never loop further; MINOR notes are optional polish, not re-run triggers
8. Run Status Sync (feature 🟣; epic may follow). Handoff: `do/task E{n} F{n} T1` (first unblocked task)
