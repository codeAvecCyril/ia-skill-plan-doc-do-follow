# plan/tasks E{n} F{n} — Task Breakdown

**Purpose**: break a feature into self-contained tasks executable by a weaker model (Invariant 11)

**Mindset**: tech lead writing instructions for a junior who cannot ask questions — everything explicit, nothing assumed. Strong model

**Inputs**: `feat-prd.md` (incl. Architecture Delta) · `feat-arch.md` if it exists · `epic-arch.md` · `docs/patterns/` · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: `{feat-slug}/feat-tasks.md` — owning file for task statuses

## Task quality bar — the task-checker verifies exactly these five checks

1. **Self-contained**: executable from the task text alone, PRD and architecture closed — WHAT / WHERE / HOW / WHY / DONE all explicit
2. **Precise**: exact file paths, concrete steps, validation commands runnable as written
3. **No external references**: never "as described in the PRD" / "see architecture" — inline the content instead
4. **Testable DONE**: observable outcomes (command passes, file exists, behavior exercisable), not intentions
5. **Sized**: one concern, 30–60 minutes

## Steps

1. Verify the feature is 🟡 in `epic-status.md`; if the Architecture Delta flagged a `plan/feat-arch` trigger and no `feat-arch.md` exists, recommend running it first
2. Read the inputs; extract requirements and acceptance criteria
3. Build the dependency DAG: data → business logic → API → UI, tests interleaved; identify parallelizable tasks
4. If the change can break existing tests, add a task to adapt them
5. Generate `feat-tasks.md` from `templates/feat-tasks.md` against the quality bar. The **Task Summary table is the single source of truth for task status** — per-task sections carry no status line. Solo mode: omit effort/owner columns
6. **Self-review before checking**: re-read every task against the five checks and fix gaps yourself
7. Run the **task-checker** subagent. Fix every FAIL, re-run **at most once** on the previously failing tasks only. If anything still fails, fix it against the checker's quoted gaps and proceed — note it in the handoff. MINOR notes are optional polish, never re-run triggers
8. Run Status Sync (feature 🟣; epic may follow). **No changelog entry** (changelog hard rule); the checker exchange never appears anywhere (Invariant 16). Handoff: `do/task E{n} F{n} T1` (first unblocked task)
