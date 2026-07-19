# plan/tasks E{n} F{n} — Task Breakdown

**Purpose**: break a feature into self-contained implementation tasks executable by a weaker model (Invariant 11)

**Mindset**: tech lead writing instructions for a junior who cannot ask questions — everything explicit, nothing assumed. Strong model; the intelligence goes into the tasks so execution doesn't need it

**Inputs**: `feat-prd.md` (including its Architecture Delta) · `feat-arch.md` if it exists · `epic-arch.md` · `docs/patterns/` · repository instruction file(s) (see Platform integration in SKILL.md)

**Outputs**: `{feat-slug}/feat-tasks.md` (direct child of the epic directory — never under an intermediate `features/` directory) — the owning file for task statuses

## Task quality bar

- Size: 30–60 minutes. Scope: one concern
- Each task states WHAT / WHERE / HOW / WHY / DONE with exact file paths, concrete steps, a real code-pattern reference from `docs/patterns/` when one exists, and runnable validation commands
- Executable **without opening the PRD or any other document**

## Steps

1. Verify the feature is 🟡 in `epic-status.md`; if the Architecture Delta flagged a `plan/feat-arch` trigger and no `feat-arch.md` exists, recommend running it first
2. Read the inputs and extract requirements and acceptance criteria
3. Build the dependency DAG in this order: data → business logic → API → UI, with tests interleaved. Identify parallelizable tasks
4. Detect if existing tests from previous features could go wrong with what we changed and create a task to adapt then consequently   
5. Generate `feat-tasks.md` from `templates/feat-tasks.md`. The **Task Summary table is the single source of truth for task status** — per-task sections carry no status line. In solo mode, omit effort/owner columns
6. Run the **task-checker** subagent (`subagents/task-checker.md`): pass it `feat-tasks.md` only. Fix every task it flags and re-run until none fail
7. Run Status Sync (feature becomes 🟣; epic may become 🟣). Handoff with `do/task E{n} F{n} T1` (first unblocked task) as default next command
