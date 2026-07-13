---
name: plan-doc-do-follow
description: Structured product development workflow from planning through execution. Manages epics, features, and tasks with single-source-of-truth status tracking, business reviews, scope changes, and clear routing from product vision to delivery. Use when the user references plan or do commands related to project planning, documentation, execution, scope changes, status synchronization, or verification.
license: Apache-2.0
---

# Plan-Doc-Do-Follow Skill

Product development workflow: **Plan** → **Doc** → **Do** → **Follow**. Guides a project from product vision through specification, architecture, task breakdown, execution and verification, with business review checkpoints. Also great for structured vibe coding sessions.

## How to use this skill

1. Match the user's intent to a route below (first match wins).
2. Read the route's playbook file in `routes/` and follow it exactly.
3. Apply the Global Invariants and the Status Model on every route.
4. **Token economy**: read only the route file you need plus the templates in `templates/` it references. Never load all routes or all templates.

## Route Reference

### Planning Phase

| User intent                                                                          | Route              | Playbook                     | Parameters            |
| ------------------------------------------------------------------------------------ | ------------------ | ---------------------------- | --------------------- |
| Plan a project by extracting epics from product vision                               | `plan/proj`        | `routes/plan-proj.md`        |                       |
| Validate epics with stakeholders                                                     | `plan/proj-review` | `routes/plan-proj-review.md` |                       |
| Create epic PRD and tracking                                                         | `plan/epic`        | `routes/plan-epic.md`        | E{n}                  |
| Validate epic spec or architecture with stakeholders                                 | `plan/epic-review` | `routes/plan-epic-review.md` | E{n} {prd\|arch}      |
| Design technical architecture for an epic                                            | `plan/epic-arch`   | `routes/plan-epic-arch.md`   | E{n}                  |
| Create feature PRD                                                                   | `plan/feat`        | `routes/plan-feat.md`        | E{n} F{n}             |
| Validate feature spec or architecture with stakeholders                              | `plan/feat-review` | `routes/plan-feat-review.md` | E{n} F{n} {prd\|arch} |
| Design feature architecture (exception cases only — see playbook)                    | `plan/feat-arch`   | `routes/plan-feat-arch.md`   | E{n} F{n}             |
| Break a feature into implementation tasks                                            | `plan/tasks`       | `routes/plan-tasks.md`       | E{n} F{n}             |
| Change scope: add or update a feature/epic, including on an already implemented epic | `plan/change`      | `routes/plan-change.md`      | change description    |
| Migrate a project documented with skill v2 to this v3 structure (one-shot)           | `plan/migrate`     | `routes/plan-migrate.md`     |                       |

### Execution Phase

| User intent                                      | Route            | Playbook                   | Parameters     |
| ------------------------------------------------ | ---------------- | -------------------------- | -------------- |
| Execute an individual task                       | `do/task`        | `routes/do-task.md`        | E{n} F{n} T{n} |
| Execute all tasks for a feature                  | `do/all-tasks`   | `routes/do-all-tasks.md`   | E{n} F{n}      |
| Verify completed work meets requirements         | `do/verify`      | `routes/do-verify.md`      | E{n} F{n}      |
| Recompute and repair all statuses from documents | `do/sync-status` | `routes/do-sync-status.md` |                |
| Memorize good practices and patterns             | `do/memorize`    | `routes/do-memorize.md`    |                |

## Global Invariants (all routes)

1. **Spirit check**: stay aligned with `docs/product.md`. The Product Spirit block (top of `docs/project-status.md`) must be included verbatim in every planning route's working context and in every reviewer subagent brief.
2. **User's will**: user answers given during reviews are recorded in `docs/decisions.md` and are binding. Reviewers may confront a design with the state of the art, but any deviation from a recorded decision must be raised as a question — never applied silently.
3. **Business first**: specification review before proceeding to the next phase.
4. **Architecture check**: stay aligned with `docs/global_architecture.md` and `docs/technical-stack.md`.
5. **One fact, one file**: every status and every fact has exactly one owning file (see Status Model). Other documents link to it — they never copy it.
6. **Plain language for humans**: anything a human must read or validate is written in complete, self-contained sentences with no unexplained abbreviations. Every checklist or decision item must be understandable without opening another document.
7. **No empty scaffolding**: delete template sections that do not apply. Never write "N/A" or leave placeholder text in a generated document.
8. **No guessing**: on blocking ambiguity, ask before generating output. Label questions blocking / important / minor.
9. **Traceability**: each document references its parent; stories ↔ requirements ↔ tasks ↔ tests stay linked.
10. **Living global docs**: `docs/data-model.md`, `docs/ui-map.md`, and `docs/decisions.md` are updated in the same change that affects them, never "later".
11. **Model tiering**: `plan/*` routes and reviewer subagents assume a strong model. Every task produced by `plan/tasks` must be executable by a weaker model without opening the PRD.
12. **Status Sync**: every route that changes any status ends by running the Status Sync procedure below.
13. **Handoff format**: end every route with a short summary, current progress, the exact next command, and open questions.
14. **Scoped subagents**: reviewer subagents receive only the inputs listed in their brief (`reviewers.md`), never "read everything".

## Status Model

Legend: `⚪ TODO` not started · `🟡 SPEC` specified · `🟣 PLAN` tasks generated · `🔵 DEV` in progress · `🟢 DONE` completed and verified.

### Status ownership — the single source of truth

| Fact                        | Owning file (the ONLY place it is written)    |
| --------------------------- | --------------------------------------------- |
| Task status                 | `feat-tasks.md` — Task Summary table          |
| Feature status and progress | `epic-status.md` — Feature table              |
| Epic status and progress    | `docs/project-status.md` — Epic Roadmap table |
| Project progress            | `docs/project-status.md` — Progress section   |

There is **no `feat-status.md` file**. Per-task sections in `feat-tasks.md` carry no status line. Mermaid diagrams are decorative: regenerated from the owning tables, never hand-maintained, never a source of truth.

### Derivation rules

- **Feature**: no `feat-prd.md` → ⚪ · `feat-prd.md` exists → 🟡 · `feat-tasks.md` exists, no task beyond TODO → 🟣 · any task DEV or DONE → 🔵 · 🟢 is set **only** by `do/verify`. If tasks are added to a 🟢 feature (via `plan/change`), it reverts to 🔵.
- **Epic**: no `epic-prd.md` → ⚪ · `epic-prd.md` exists → 🟡 · all features ≥ 🟣 → 🟣 · any feature 🔵 or 🟢 (but not all 🟢) → 🔵 · all features 🟢 → 🟢.
- **Project**: same aggregation over epics.
- **Progress**: feature = done tasks / total tasks; epic and project = sum of done tasks / sum of total tasks (0 if no tasks).

### Status Sync procedure

Run at the end of any route that changed a status, or standalone via `do/sync-status`:

1. Read the Task Summary tables of the affected feature(s) (`do/sync-status`: all features of all epics).
2. Recompute each feature's status and progress with the derivation rules; update its row in `epic-status.md`.
3. Recompute each affected epic's status and progress; update its row, the Progress section, the pie chart, and the changelog in `docs/project-status.md`.
4. Report any drift found (a stored status that did not match the derived one) in the handoff.

The procedure is deterministic and idempotent: running it twice changes nothing.

## Reviewer subagents

Briefs live in `reviewers.md`: **PRD Critic**, **Arch Critic**, **UI Consistency Reviewer**, **Task Self-Containment Check**, **Doc Coherence Reviewer**. Routes state which reviewer to run and when. Pass each reviewer exactly the inputs its brief lists, always including the Product Spirit block. Apply their comments or record in the handoff why a comment was rejected.

## Human review UX

Review documents separate what the AI verified from what only the human can decide:

- Mechanical/structural checks are auto-verified by the AI and collapsed to one summary line.
- The human sees a **"Decisions requiring your validation"** section: at most 10 plain-sentence statements (e.g. "Users will log in with email only; social login is out of scope for V1. Confirm?"), plus open questions labeled blocking / important / minor.
- Every validated decision is appended to `docs/decisions.md`.

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
        └── features/
            └── f{n}-{feat-name}/            (slug e.g. f3-backend-api)
                ├── feat-prd.md              (from plan/feat; includes Entry Points and Architecture Delta)
                ├── feat-arch.md             (from plan/feat-arch — exception cases only)
                ├── feat-tasks.md            (owning file: task statuses)
                └── feat-review.md           (from plan/feat-review)
```

## Platform integration (environment-agnostic)

For repository conventions and coding standards, use whichever of these exist, in this order of precedence: `CLAUDE.md` · `AGENTS.md` · `.github/copilot-instructions.md` · `.cursor/rules/` · `.github/instructions/`. When `do/memorize` writes back, it updates the platform-native file(s) actually present in the repository.

## Templates

All templates live in `templates/` (no `template-` prefix; names mirror output files).

Project: `templates/proj-status.md`, `templates/proj-review.md`, `templates/decisions.md`, `templates/data-model.md`, `templates/ui-map.md`, `templates/design-guidelines.md`
Epic: `templates/epic-brief.md`, `templates/epic-prd.md`, `templates/epic-status.md`, `templates/epic-review.md`, `templates/epic-arch.md`
Feature: `templates/feat-prd.md`, `templates/feat-review.md`, `templates/feat-arch.md`, `templates/feat-tasks.md`
