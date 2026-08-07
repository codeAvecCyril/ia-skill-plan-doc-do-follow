# plan/tasks E{n} F{n} — Task Breakdown

**Purpose**: break feature into self-contained tasks executable by weaker model (Invariant 11)

**Mindset**: tech lead writing instructions for junior who cannot ask questions — everything explicit, nothing assumed · strong model

**Inputs**: `feat-prd.md` (incl. Architecture Delta) · `feat-arch.md` if it exists · `epic-arch.md` · `docs/patterns/` · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: `{feat-slug}/feat-tasks.md` — owns task statuses

## Task quality bar — task-checker verifies exactly these five checks

1. **Self-contained**: executable from task text alone, PRD and architecture closed — WHAT / WHERE / HOW / WHY / DONE all explicit
2. **Precise**: exact file paths, concrete steps, validation commands runnable as written
3. **No external references**: never "as described in the PRD" / "see architecture" — inline content instead
4. **Testable DONE**: observable outcomes (command passes, file exists, behavior exercisable), not intentions
5. **Sized**: one concern, 30–60 minutes

## Steps

1. Verify feature is 🟡 in `epic-status.md` · if Architecture Delta flagged `plan/feat-arch` trigger and no `feat-arch.md` exists, recommend running it first
2. Read inputs; extract requirements and acceptance criteria
3. Build dependency DAG: data → business logic → API → UI, tests interleaved · identify parallelizable tasks
4. If change can break existing tests, add task to adapt them
5. Generate `feat-tasks.md` from `templates/feat-tasks.md` against quality bar · **Task Summary table is single source of truth for task status** — per-task sections carry no status line · solo mode: omit effort/owner columns
6. **Self-review before checking**: re-read every task against five checks and fix gaps yourself
7. Run **task-checker** subagent · fix every FAIL, re-run **at most once** on previously failing tasks only · if anything still fails, fix against checker's quoted gaps and proceed — note it in handoff · MINOR notes optional polish, never re-run triggers
8. Run Status Sync (feature 🟣; epic may follow) · **no changelog entry** (changelog hard rule); checker exchange never appears anywhere (Invariant 16) · Handoff: `do/task E{n} F{n} T1` (first unblocked task)
