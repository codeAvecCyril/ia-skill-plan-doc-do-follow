---
name: plan-doc-do-follow
description: Structured product development workflow from planning through execution. Manages epics, features, and tasks with single-source-of-truth status tracking, business reviews, scope changes, and clear routing from product vision to delivery. Use when the user references plan or do commands related to project planning, documentation, execution, scope changes, status synchronization, or verification.
license: Apache-2.0
---

# Plan-Doc-Do-Follow Skill

Product development workflow: **Plan** → **Doc** → **Do** → **Follow**.

Use: match the user's intent to a route below (first match wins) → read `routes/a-b.md` (route `a/b`) and follow it → apply the Global Invariants and the Status Model. Load only the route file needed, the templates it references, and the subagents it invokes — never all of them.

## Routes

### Planning

| Intent | Route | Params |
| --- | --- | --- |
| Extract epics from product vision | `plan/proj` | |
| Validate epics with stakeholders | `plan/proj-review` | |
| Create epic PRD and tracking | `plan/epic` | E{n} |
| Validate epic spec or architecture | `plan/epic-review` | E{n} {prd\|arch} |
| Design epic architecture | `plan/epic-arch` | E{n} |
| Create feature PRD | `plan/feat` | E{n} F{n} |
| Validate feature spec or architecture | `plan/feat-review` | E{n} F{n} {prd\|arch} |
| Feature architecture (exception cases only) | `plan/feat-arch` | E{n} F{n} |
| Break a feature into tasks | `plan/tasks` | E{n} F{n} |
| Scope change — add/update feature or epic, even implemented | `plan/change` | description |
| Migrate a v2-documented project to v3 (one-shot) | `plan/migrate` | |

### Execution

| Intent | Route | Params |
| --- | --- | --- |
| Set up token-saving tooling (LSP, output filters) | `do/init` | |
| Execute one task | `do/task` | E{n} F{n} T{n} |
| Execute all feature tasks, verify inline | `do/all-tasks` | E{n} F{n} |
| Verify completed work (task-at-a-time path) | `do/verify` | E{n} F{n} |
| Recompute and repair all statuses | `do/sync-status` | |
| Memorize good practices | `do/memorize` | |

## Global Invariants (all routes)

1. **Spirit check**: stay aligned with `docs/product.md`; the Product Spirit block (top of `docs/project-status.md`) goes verbatim into every planning route's context and every reviewer brief
2. **User's will**: decisions recorded in `docs/decisions.md` are binding; any deviation is raised as a question, never applied silently
3. **Business first**: specification review before the next phase
4. **Architecture check**: stay aligned with `docs/global_architecture.md` and `docs/technical-stack.md`
5. **One fact, one file**: every status and fact has one owning file (Status Model); other documents link to it, never copy it
6. **Plain language**: anything a human must read or validate is complete, self-contained sentences — no unexplained abbreviations
7. **No empty scaffolding**: delete template sections that do not apply; never "N/A" or placeholders
8. **No guessing**: on blocking ambiguity, ask before generating output; label questions blocking / important / minor
9. **Traceability**: each document references its parent; stories ↔ requirements ↔ tasks ↔ tests stay linked
10. **Living global docs**: `docs/data-model.md`, `docs/ui-map.md`, `docs/decisions.md` are updated in the same change that affects them, never "later"
11. **Model tiering**: `plan/*` routes and reviewers assume a strong model; every task from `plan/tasks` must be executable by a weaker model without opening the PRD
12. **Status Sync**: every status-changing route ends with the Status Sync procedure
13. **Handoff format**: end every route with a short summary, current progress, the exact next command, and open questions
14. **Scoped subagents**: subagents receive only the inputs their definition lists
15. **Mindset per route**: adopt the working posture in the route's Mindset line
16. **Deliberation stays internal**: critic exchanges (findings, fixes, iteration counts) never appear in documents or handoffs — the human sees only the final result and what they must validate
17. **Economy everywhere**: the Working Economy rules apply to every route and every subagent

## Status Model

`⚪ TODO` · `🟡 SPEC` specified · `🟣 PLAN` tasks generated · `🔵 DEV` in progress · `🟢 DONE` completed and verified.

### Ownership — single source of truth

| Fact | Owning file (the ONLY place it is written) |
| --- | --- |
| Task status | `feat-tasks.md` — Task Summary table |
| Feature status and progress | `epic-status.md` — Feature table |
| Epic status and progress | `docs/project-status.md` — Epic Roadmap table |
| Project progress | `docs/project-status.md` — Progress section |

There is **no `feat-status.md` file**. Per-task sections carry no status line. Mermaid diagrams are decorative: regenerated from the owning tables, never a source of truth.

### Derivation rules

- **Feature**: no `feat-prd.md` → ⚪ · PRD exists → 🟡 · `feat-tasks.md` exists, no task beyond TODO → 🟣 · any task DEV/DONE → 🔵 · 🟢 **only** via the verification gates (`do/verify`, or the final phase of `do/all-tasks`). Tasks added to a 🟢 feature revert it to 🔵
- **Epic**: no `epic-prd.md` → ⚪ · PRD exists → 🟡 · all features ≥ 🟣 → 🟣 · any feature 🔵/🟢 (not all 🟢) → 🔵 · all 🟢 → 🟢
- **Project**: same aggregation over epics
- **Progress**: done tasks / total tasks (0 if no tasks), summed at epic and project level

### Status Sync procedure

At the end of any status-changing route (standalone: `do/sync-status`, over all epics):

1. Read the Task Summary tables of the affected feature(s)
2. Recompute each feature's status and progress; update its row in `epic-status.md`
3. Recompute each affected epic; update its row, the Progress section, and the pie chart in `docs/project-status.md`. Status Sync never writes a changelog entry — only the events named by the changelog hard rule (Document style) get one, written by the route that produced the milestone
4. Report any drift (stored ≠ derived) in the handoff

Deterministic and idempotent.

## Subagents

Definitions in `subagents/` — one file per agent (format: `subagents/README.md`). To invoke: read its file, assemble exactly the inputs it lists (reviewers always get the Product Spirit block), spawn a subagent with the file body as its system prompt.

**Before any spawn**:

- **Cost gate**: skip the subagent and check inline when the brief would approach the size of the work itself, the needed facts are already in context, or the expected findings are cosmetic
- **Precise brief**: state the exact questions/checks, the standards the work was built against, and what is out of scope
- **Front-load the bar**: before drafting a document, read the Review questions of the critic that will review it and draft to pass them on the first try

**Handling critic findings**: apply a finding if it changes behavior, a contract, or a human decision; drop futile or cosmetic ones silently. A rejected finding that is a genuine judgment call becomes a decision question for the human. **Convergence**: one run per document; at most one re-run, only after substantial rework of blocking findings and scoped to them — re-run findings accepted only if blocking; never a third run. Never report the exchange itself (Invariant 16).

| Subagent | Kind | Called by | When |
| --- | --- | --- | --- |
| `repo-scout` | research | `plan/epic-arch`, `plan/feat`, `plan/feat-arch`, `plan/change` | plan must be grounded in existing code |
| `prd-critic` | reviewer | `plan/epic`, `plan/feat` | always |
| `arch-critic` | reviewer | `plan/epic-arch`, `plan/feat-arch` | always |
| `perf-critic-backend` / `-frontend` | reviewer | arch routes, verification gates | only when their trigger criteria (top of their files) fire |
| `task-checker` | reviewer | `plan/tasks` | after self-review; max two runs |
| `feature-coder` | executor | `do/all-tasks` | one per parallelizable task per wave |
| `ui-consistency-reviewer` | reviewer | verification gates | UI features with a non-trivial surface |
| `doc-coherence-reviewer` | reviewer | verification gates · `plan/change` · `plan/migrate` | epic completion · after a change · after migration |

The verification gates (and their subagents) run in `do/verify` or inline as the final phase of `do/all-tasks`.

## Human review UX

Reviews present conclusions, not process: mechanical checks auto-verified and collapsed to one summary line; a **"Decisions requiring your validation"** section of at most 10 plain-sentence statements plus open questions labeled blocking/important/minor; validated decisions appended to `docs/decisions.md`; stakeholder answers recorded **verbatim** and applied as written — never paraphrased, never re-asked (if genuinely ambiguous, ask only the clarification).

## Working Economy (Invariant 17)

### Input economy

- Prefer LSP/semantic navigation over whole-file reads; read scoped line ranges
- Route long CLI outputs (tests, builds, git, package managers) through the output filter the repository instruction file declares (e.g. `rtk`, `snip`) — `do/init` sets it up
- Never re-read what is already in context; never load a document "for safety"

### Output style (principal and subagents)

- No preamble, no restating the request, no trailing summary
- Code changes as diffs or targeted edits, never full-file listings unless asked
- Research answers ≤10 lines unless depth is requested
- The Handoff (Invariant 13) is the only closing block: ≤5 lines

### Minimal implementation (do routes and feature-coder)

Understand the problem fully, then stop at the first rung that holds:

1. Doesn't need to exist → skip (YAGNI) · 2. Already in the codebase → reuse · 3. Stdlib does it → use it · 4. Native platform feature → use it · 5. Installed dependency → use it · 6. One line suffices → one line · 7. Only then write the minimum that works.

Never cut: trust-boundary validation, data-loss handling, security, accessibility.

### Document style (all generated documents)

- State decisions and facts, never the process that produced them — "the reviewer suggested…", "after discussion we changed…" never appear
- Justify a choice only where a future reader needs the why (a trade-off, a scope cut): 1–2 sentences
- **Changelog hard rule**: an entry is one line, `{date}: {fact}`, ≤25 words. Eligible events only — project changelog: epic completed, major scope change, migration; epic changelog: feature verified 🟢, scope change. Every other event (tasks generated, PRD drafted/approved, waves, syncs, drift repairs) gets **no entry**. Never include: critic/subagent exchanges (Invariant 16), task lists, gate results, progress numbers, `Next:` commands
- Existing verbose changelog entries are legacy, never precedent — still write only the single eligible line, or nothing

## File Organization

```
docs/
├── product.md                 (input: product vision)
├── global_architecture.md     (input: architecture overview)
├── technical-stack.md         (input: technology decisions)
├── project-status.md          (owning: Product Spirit, epic statuses, progress)
├── project-review.md
├── decisions.md               (living: binding user decisions, one line each)
├── data-model.md              (living: global data schema, if any)
├── ui-map.md                  (living: global navigation map, if UI)
├── design-guidelines.md       (living: UI style conventions, if UI)
├── patterns/{pattern-name}.md (from do/memorize)
└── epics/e{n}-{epic-name}/            (slug e.g. e2-orm-discovery)
    ├── epic-brief.md                  (plan/proj)
    ├── epic-prd.md                    (plan/epic)
    ├── epic-status.md                 (owning: feature statuses)
    ├── epic-arch.md                   (plan/epic-arch)
    ├── epic-review.md                 (plan/epic-review)
    └── f{n}-{feat-name}/              (direct child — no features/ level)
        ├── feat-prd.md                (plan/feat; has Entry Points + Architecture Delta)
        ├── feat-arch.md               (plan/feat-arch — exceptions only)
        ├── feat-tasks.md              (owning: task statuses)
        └── feat-review.md             (plan/feat-review)
```

## Platform integration

For repository conventions use whichever exists, in this precedence: `CLAUDE.md` · `AGENTS.md` · `.github/copilot-instructions.md` · `.cursor/rules/` · `.github/instructions/`. `do/memorize` writes back to the file(s) actually present.

## Templates

In `templates/` — names mirror output files.
