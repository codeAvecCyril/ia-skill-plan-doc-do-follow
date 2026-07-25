---
name: plan-doc-do-follow
description: Structured product development workflow from planning through execution. Manages epics, features, and tasks with single-source-of-truth status tracking, business reviews, scope changes, and clear routing from product vision to delivery. Use when the user references plan or do commands related to project planning, documentation, execution, scope changes, status synchronization, or verification.
license: Apache-2.0
---

# Plan-Doc-Do-Follow Skill

Product development workflow: **Plan** → **Doc** → **Do** → **Follow** — from product vision through specification, architecture, task breakdown, execution and verification, with business review checkpoints. Also great for structured vibe coding sessions.

## How to use this skill

1. Match the user's intent to a route below (first match wins)
2. Read the route's playbook in `routes/` and follow it exactly
3. Apply the Global Invariants and the Status Model on every route
4. **Economy**: apply the Working Economy rules (section below) on every route — load only the route file you need, the templates it references, and the subagents it invokes, never all of them

## Route Reference

Playbook path: route `a/b` → `routes/a-b.md` (e.g. `plan/epic-arch` → `routes/plan-epic-arch.md`)

### Planning Phase

| User intent                                                                          | Route              | Parameters            |
| ------------------------------------------------------------------------------------ | ------------------ | --------------------- |
| Plan a project by extracting epics from product vision                               | `plan/proj`        |                       |
| Validate epics with stakeholders                                                     | `plan/proj-review` |                       |
| Create epic PRD and tracking                                                         | `plan/epic`        | E{n}                  |
| Validate epic spec or architecture with stakeholders                                 | `plan/epic-review` | E{n} {prd\|arch}      |
| Design technical architecture for an epic                                            | `plan/epic-arch`   | E{n}                  |
| Create feature PRD                                                                   | `plan/feat`        | E{n} F{n}             |
| Validate feature spec or architecture with stakeholders                              | `plan/feat-review` | E{n} F{n} {prd\|arch} |
| Design feature architecture (exception cases only — see playbook)                    | `plan/feat-arch`   | E{n} F{n}             |
| Break a feature into implementation tasks                                            | `plan/tasks`       | E{n} F{n}             |
| Change scope: add or update a feature/epic, including on an already implemented epic | `plan/change`      | change description    |
| Migrate a project documented with skill v2 to this v3 structure (one-shot)           | `plan/migrate`     |                       |

### Execution Phase

| User intent                                                        | Route            | Parameters     |
| ------------------------------------------------------------------ | ---------------- | -------------- |
| Set up token-saving tooling for the project (LSP, output filters)  | `do/init`        |                |
| Execute an individual task                                         | `do/task`        | E{n} F{n} T{n} |
| Execute all tasks for a feature (ends with the verification gates) | `do/all-tasks`   | E{n} F{n}      |
| Verify completed work (when tasks were run one at a time)          | `do/verify`      | E{n} F{n}      |
| Recompute and repair all statuses from documents                   | `do/sync-status` |                |
| Memorize good practices and patterns                               | `do/memorize`    |                |

## Global Invariants (all routes)

1. **Spirit check**: stay aligned with `docs/product.md`; the Product Spirit block (top of `docs/project-status.md`) goes verbatim into every planning route's context and every reviewer brief
2. **User's will**: review answers are recorded in `docs/decisions.md` and binding; any deviation from a recorded decision is raised as a question, never applied silently
3. **Business first**: specification review before the next phase
4. **Architecture check**: stay aligned with `docs/global_architecture.md` and `docs/technical-stack.md`
5. **One fact, one file**: every status and fact has one owning file (see Status Model); other documents link to it, never copy it
6. **Plain language for humans**: anything a human must read or validate is complete, self-contained sentences — no unexplained abbreviations, understandable without opening another document
7. **No empty scaffolding**: delete template sections that do not apply; never write "N/A" or leave placeholders
8. **No guessing**: on blocking ambiguity, ask before generating output; label questions blocking / important / minor
9. **Traceability**: each document references its parent; stories ↔ requirements ↔ tasks ↔ tests stay linked
10. **Living global docs**: `docs/data-model.md`, `docs/ui-map.md`, and `docs/decisions.md` are updated in the same change that affects them, never "later"
11. **Model tiering**: `plan/*` routes and reviewer subagents assume a strong model; every task from `plan/tasks` must be executable by a weaker model without opening the PRD
12. **Status Sync**: every route that changes a status ends with the Status Sync procedure
13. **Handoff format**: end every route with a short summary, current progress, the exact next command, and open questions
14. **Scoped subagents**: subagents receive only the inputs their definition lists, never "read everything"
15. **Mindset per route**: each playbook opens with a **Mindset** line — the working posture and model class the principal adopts for that route
16. **Deliberation stays internal**: exchanges with critic subagents (findings, fixes, iteration count) are working material — never replayed in review documents or handoffs; the human sees only the final result and what they must validate
17. **Economy everywhere**: the Working Economy rules (input, subagent invocation, output style, document style) apply to every route and every subagent

## Status Model

Legend: `⚪ TODO` not started · `🟡 SPEC` specified · `🟣 PLAN` tasks generated · `🔵 DEV` in progress · `🟢 DONE` completed and verified.

### Status ownership — the single source of truth

| Fact                        | Owning file (the ONLY place it is written)    |
| --------------------------- | --------------------------------------------- |
| Task status                 | `feat-tasks.md` — Task Summary table          |
| Feature status and progress | `epic-status.md` — Feature table              |
| Epic status and progress    | `docs/project-status.md` — Epic Roadmap table |
| Project progress            | `docs/project-status.md` — Progress section   |

There is **no `feat-status.md` file**. Per-task sections in `feat-tasks.md` carry no status line. Mermaid diagrams are decorative: regenerated from the owning tables, never a source of truth.

### Derivation rules

- **Feature**: no `feat-prd.md` → ⚪ · `feat-prd.md` exists → 🟡 · `feat-tasks.md` exists, no task beyond TODO → 🟣 · any task DEV or DONE → 🔵 · 🟢 is set **only** by the verification gates (`do/verify`, or the final phase of `do/all-tasks`). Tasks added to a 🟢 feature (via `plan/change`) revert it to 🔵
- **Epic**: no `epic-prd.md` → ⚪ · `epic-prd.md` exists → 🟡 · all features ≥ 🟣 → 🟣 · any feature 🔵 or 🟢 (but not all 🟢) → 🔵 · all features 🟢 → 🟢
- **Project**: same aggregation over epics
- **Progress**: feature = done tasks / total tasks; epic and project = sum of done tasks / sum of total tasks (0 if no tasks)

### Status Sync procedure

Run at the end of any route that changed a status, or standalone via `do/sync-status`:

1. Read the Task Summary tables of the affected feature(s) (`do/sync-status`: all features of all epics)
2. Recompute each feature's status and progress with the derivation rules; update its row in `epic-status.md`
3. Recompute each affected epic's status and progress; update its row, the Progress section, and the pie chart in `docs/project-status.md` (changelogs record milestones only — see Document style)
4. Report any drift found (stored status ≠ derived) in the handoff

The procedure is deterministic and idempotent: running it twice changes nothing.

## Subagents

Definitions live in `subagents/` — one file per agent, portable YAML frontmatter (format spec in `subagents/README.md`). To invoke one: read its file, assemble exactly the inputs it lists (always including the Product Spirit block for reviewers), and spawn a subagent with the file body as its system prompt.

**Before invoking any subagent** (all routes):

- **Cost gate**: weigh the expected value against the context the brief requires. If the brief would approach the size of the work itself, the needed facts are already in your context, or the expected findings are cosmetic, do the check inline yourself and skip the subagent — deciding *not* to spawn is a normal, good outcome
- **Precise brief**: state the exact questions or checks, the standards the work was built against, and what is out of scope. A subagent judging by rules the author never saw produces rework, not quality
- **Front-load the bar**: before drafting a document, read the Review questions of the critic that will review it and draft to pass them on the first try. The critic is a safety net, not the place to discover the rules

**Handling critic findings** (all routes): judge each finding by impact — apply it if it changes behavior, a contract, or a decision the human must make; drop futile or cosmetic ones silently, without a re-check. If you reject one and the disagreement is a genuine judgment call, surface it as a decision question for the human. **Convergence**: a critic runs once per document; re-run at most once, only after substantial rework of blocking findings, and scope the re-run to those findings — new remarks appearing on a re-run are accepted only if blocking, and there is never a third run. Per Invariant 16, never report the critic exchange itself.

| Subagent                  | Kind     | Called by                                                      | When                                               |
| ------------------------- | -------- | -------------------------------------------------------------- | -------------------------------------------------- |
| `repo-scout`              | research | `plan/epic-arch`, `plan/feat`, `plan/feat-arch`, `plan/change` | when the plan must be grounded in existing code    |
| `prd-critic`              | reviewer | `plan/epic`, `plan/feat`                                       | always                                             |
| `arch-critic`             | reviewer | `plan/epic-arch`, `plan/feat-arch`                             | always                                             |
| `perf-critic-backend`     | reviewer | `plan/epic-arch`, `plan/feat-arch`, `do/verify`                | only when its trigger criteria fire                |
| `perf-critic-frontend`    | reviewer | `plan/epic-arch`, `plan/feat-arch`, `do/verify`                | only when its trigger criteria fire                |
| `task-checker`            | reviewer | `plan/tasks`                                                   | after self-review; max two runs                    |
| `feature-coder`           | executor | `do/all-tasks`                                                 | one per parallelizable task in a wave              |
| `ui-consistency-reviewer` | reviewer | `do/verify`                                                    | features with UI requirements                      |
| `doc-coherence-reviewer`  | reviewer | `do/verify` · `plan/change` · `plan/migrate`                   | epic completion · after a change · after migration |

The perf critics are **conditional**: the calling route checks the trigger criteria at the top of each definition and skips the review when none applies.

The verification gates (and their subagents) run in `do/verify` or inline as the final phase of `do/all-tasks` — wherever the table above says `do/verify`, both apply.

## Human review UX

Review documents present conclusions, not the process that produced them:

- Mechanical/structural checks are auto-verified by the AI and collapsed to one summary line
- The human sees a **"Decisions requiring your validation"** section: at most 10 plain-sentence statements (e.g. "Users will log in with email only; social login is out of scope for V1. Confirm?"), plus open questions labeled blocking / important / minor
- Every validated decision is appended to `docs/decisions.md`
- Stakeholder answers are recorded **verbatim** and applied as written — never paraphrased, never re-asked once answered; if an answer is genuinely ambiguous, ask only the clarification

## Working Economy (Invariant 17)

Token discipline is a feature of this skill. Four rule sets, applied by every route and every subagent.

### Input economy

- Prefer LSP/semantic navigation (go-to-definition, references, symbols) over reading whole files when the environment provides it; read scoped line ranges, not entire files
- Route long CLI outputs (tests, builds, git, package managers) through the output filter the repository instruction file declares (e.g. `rtk`, `snip`) — `do/init` sets this up once per project
- Never re-read what is already in context; never load a document "for safety"

### Output style (principal and subagents)

- Go straight to the point: no preamble, no restating the request, no trailing summary of what was just done
- Present code changes as diffs or targeted edits, never full-file listings unless asked
- Answer research questions in 10 lines or fewer unless depth is requested
- The Handoff (Invariant 13) is the only closing block: 5 lines maximum

### Minimal implementation (do routes and feature-coder)

Lazy about the solution, never about reading: understand the problem fully, then climb this ladder and stop at the first rung that holds.

1. Does it need to exist? No → skip it (YAGNI)
2. Already in the codebase? → reuse it
3. Standard library does it? → use it
4. Native platform feature? → use it
5. Installed dependency does it? → use it
6. One line suffices? → one line
7. Only then: write the minimum that works

Never on the chopping block: trust-boundary validation, data-loss handling, security, accessibility.

### Document style (all generated documents)

- State decisions and facts, never the process that produced them — "the reviewer suggested…", "after discussion we changed…" never appear in a document
- Justify a choice only where a future reader needs the why (an architecture trade-off, a scope cut): one or two sentences, no soothing rhetoric
- Changelogs record milestones only (epic completed, scope change, migration) — routine history lives in git, statuses live in the owning tables

## File Organization

```
docs/
├── product.md                 (input: product vision)
├── global_architecture.md     (input: architecture overview)
├── technical-stack.md         (input: technology decisions)
├── project-status.md          (owning file: Product Spirit, epic statuses, project progress)
├── project-review.md          (from plan/proj-review)
├── decisions.md               (living doc: binding user decisions — one line each)
├── data-model.md              (living doc: global database/data schema, if the project has one)
├── ui-map.md                  (living doc: global navigation map, if the project has a UI)
├── design-guidelines.md       (living doc: UI style conventions, if the project has a UI)
├── patterns/                  (from do/memorize)
│   └── {pattern-name}.md
└── epics/
    └── e{n}-{epic-name}/                    (slug e.g. e2-orm-discovery)
        ├── epic-brief.md                    (from plan/proj)
        ├── epic-prd.md                      (from plan/epic)
        ├── epic-status.md                   (owning file: feature statuses)
        ├── epic-arch.md                     (from plan/epic-arch)
        ├── epic-review.md                   (from plan/epic-review)
        └── f{n}-{feat-name}/                (slug e.g. f3-backend-api; direct child of the epic — no intermediate features/ directory)
            ├── feat-prd.md                  (from plan/feat; includes Entry Points and Architecture Delta)
            ├── feat-arch.md                 (from plan/feat-arch — exception cases only)
            ├── feat-tasks.md                (owning file: task statuses)
            └── feat-review.md               (from plan/feat-review)
```

## Platform integration (environment-agnostic)

For repository conventions and coding standards, use whichever of these exist, in this order of precedence: `CLAUDE.md` · `AGENTS.md` · `.github/copilot-instructions.md` · `.cursor/rules/` · `.github/instructions/`. When `do/memorize` writes back, it updates the platform-native file(s) actually present in the repository.

## Templates

All templates live in `templates/` (names mirror output files).

Project: `proj-status.md`, `proj-review.md`, `decisions.md`, `data-model.md`, `ui-map.md`, `design-guidelines.md`
Epic: `epic-brief.md`, `epic-prd.md`, `epic-status.md`, `epic-review.md`, `epic-arch.md`
Feature: `feat-prd.md`, `feat-review.md`, `feat-arch.md`, `feat-tasks.md`
