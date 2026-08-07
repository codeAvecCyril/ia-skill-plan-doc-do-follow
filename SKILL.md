---
name: plan-doc-do-follow
description: Product workflow Plan→Doc→Do→Follow. Epics/features/tasks, single-source status, business reviews, scope change, vision→delivery routing. Use on plan/do commands for planning, docs, execution, status sync, verification
license: Apache-2.0
---

# Plan-Doc-Do-Follow Skill

**Plan** → **Doc** → **Do** → **Follow**

Match intent → first route wins → read `routes/a-b.md` (route `a/b`) → follow it → apply Global Invariants + Status Model. Load only needed route, its templates, its subagents — never all

## Routes

### Planning

| Intent | Route | Params |
| ------ | ----- | ------ |
| Extract epics from product vision | `plan/proj` | |
| Validate epics with stakeholders | `plan/proj-review` | |
| Create epic PRD and tracking | `plan/epic` | E{n} |
| Validate epic spec or architecture | `plan/epic-review` | E{n} {prd\|arch} |
| Design epic architecture | `plan/epic-arch` | E{n} |
| Create feature PRD | `plan/feat` | E{n} F{n} |
| Validate feature spec or architecture | `plan/feat-review` | E{n} F{n} {prd\|arch} |
| Feature architecture (exception only) | `plan/feat-arch` | E{n} F{n} |
| Break feature into tasks | `plan/tasks` | E{n} F{n} |
| Scope change — add/update feature or epic, even implemented | `plan/change` | description |
| Migrate v2 project docs to v3 (one-shot) | `plan/migrate` | |

### Execution

| Intent | Route | Params |
| ------ | ----- | ------ |
| Set up token-saving tooling (LSP, filters, economy, native agents) | `do/init` | |
| Execute one task | `do/task` | E{n} F{n} T{n} |
| Execute all feature tasks, verify inline | `do/all-tasks` | E{n} F{n} |
| Verify completed work (task-at-a-time path) | `do/verify` | E{n} F{n} |
| Recompute and repair all statuses | `do/sync-status` | |
| Memorize good practices | `do/memorize` | |

## Global Invariants (all routes)

1. **Spirit check**: align with `docs/product.md`; Product Spirit (top of `docs/project-status.md`) verbatim in every planning route + reviewer brief
2. **User's will**: `docs/decisions.md` binding; deviation = question, never silent apply
3. **Business first**: spec review before next phase
4. **Architecture check**: align with `docs/global_architecture.md` + `docs/technical-stack.md`
5. **One fact, one file**: status/fact has one owning file (Status Model); others link, never copy
6. **Audience language**: human/business = complete sentences, no unexplained abbreviations; agent-facing = Document style (caveman-concise)
7. **No empty scaffolding**: delete unused template sections; never "N/A" or placeholders
8. **No guessing**: blocking ambiguity → ask first; label blocking / important / minor
9. **Traceability**: each doc references parent; stories ↔ requirements ↔ tasks ↔ tests linked
10. **Living global docs**: `docs/data-model.md`, `docs/ui-map.md`, `docs/decisions.md` updated in same change that affects them — never "later"
11. **Model tiering**: `plan/*` + reviewers = strong model; every `plan/tasks` task executable by weaker model without opening PRD
12. **Status Sync**: every status-changing route ends with Status Sync procedure
13. **Handoff format**: short summary · current progress · exact next command · open questions
14. **Scoped subagents**: only inputs their definition lists
15. **Mindset per route**: adopt route's Mindset line
16. **Deliberation stays internal**: critic exchanges never in docs/handoffs — human sees final result + what to validate
17. **Economy everywhere**: Working Economy on every route and subagent

## Status Model

`⚪ TODO` · `🟡 SPEC` specified · `🟣 PLAN` tasks generated · `🔵 DEV` in progress · `🟢 DONE` completed and verified

### Ownership — single source of truth

| Fact | Owning file (ONLY place written) |
| ---- | -------------------------------- |
| Task status | `feat-tasks.md` — Task Summary table |
| Feature status and progress | `epic-status.md` — Feature table |
| Epic status and progress | `docs/project-status.md` — Epic Roadmap table |
| Project progress | `docs/project-status.md` — Progress section |

**No `feat-status.md`**. Per-task sections: no status line. Mermaid = decorative, regenerated from owning tables, never source of truth

### Derivation rules

- **Feature**: no `feat-prd.md` → ⚪ · PRD exists → 🟡 · `feat-tasks.md` exists, no task beyond TODO → 🟣 · any task DEV/DONE → 🔵 · 🟢 **only** via verification gates (`do/verify`, or final phase of `do/all-tasks`). Tasks added to 🟢 feature → revert to 🔵
- **Epic**: no `epic-prd.md` → ⚪ · PRD exists → 🟡 · all features ≥ 🟣 → 🟣 · any feature 🔵/🟢 (not all 🟢) → 🔵 · all 🟢 → 🟢
- **Project**: same aggregation over epics
- **Progress**: done tasks / total tasks (0 if none), summed at epic and project level

### Status Sync procedure

End of any status-changing route (standalone: `do/sync-status`, all epics):

1. Read Task Summary tables of affected feature(s)
2. Recompute each feature status + progress; update row in `epic-status.md`
3. Recompute each affected epic; update its row, Progress section, pie chart in `docs/project-status.md`. Status Sync never writes changelog — only events named by changelog hard rule (Document style), written by route that produced milestone
4. Report drift (stored ≠ derived) in handoff

Deterministic and idempotent

## Subagents

Defs in `subagents/` — one file per agent (format: `subagents/README.md`). Invoke: read file → assemble exactly listed inputs (reviewers always get Product Spirit) → spawn with file body as system prompt

### Economy profile

Read `Subagent economy:` from repository instruction file **Tooling** section (`do/init` writes it). Missing → `balanced`

| Profile | Behavior |
| ------- | -------- |
| `strict` | Inline-first hard · scout almost always inline · question/tool/return caps enforced · critics still spawn |
| `balanced` | Inline-first as written below · caps enforced · soft warn if >5 scout questions |
| `quality` | Cost gate advisory only · caps still apply to scout tool use and return size |

### Before any spawn (inline-first)

Run in order — first match wins → **do not spawn**:

1. Facts already in principal context → work **inline**
2. Answerable by principal in ≤5 Grep/Glob/Read (or LSP) calls → **inline** (use scout-lite checklist in `subagents/repo-scout.md`)
3. Brief would approach size of expected answer → **inline**
4. Findings likely cosmetic / mechanical checklist on small surface → **inline** (same as today's Cost gate)
5. Else spawn

**repo-scout extra** (under `strict` / `balanced`): spawn only if ≥3 falsifiable questions **and** search spans ≥2 areas principal has not opened, **or** principal context already fat and isolation clearly cheaper. Otherwise scout-lite inline

**When spawning**:

- **Tooling injection**: brief includes one-line Tooling block from repo instruction file (CLI filter prefix, LSP preference, economy profile) — subagent must obey it
- **Precise brief**: exact questions/checks · standards work built against · out of scope · for scout, starting paths/globs when area known · ≤5 questions per scout wave (`balanced`/`strict`; split or inline the rest)
- **Front-load the bar**: before draft, read critic's Review questions; draft to pass first try
- **Return-payload cap**: scout ≤15 lines · critics ≤25 lines · principal keeps only needed facts — never paste scout dumps into docs

**Critic findings**: apply if changes behavior, contract, or human decision; drop futile/cosmetic silently. Rejected judgment-call → decision question for human. **Convergence**: one run per doc; at most one re-run after substantial rework of blocking findings, scoped to them — re-run accepts blocking only; never third run. Never report exchange (Invariant 16)

| Subagent | Kind | Called by | When |
| -------- | ---- | --------- | ---- |
| `repo-scout` | research | `plan/epic-arch`, `plan/feat`, `plan/feat-arch`, `plan/change` | plan must ground in existing code |
| `prd-critic` | reviewer | `plan/epic`, `plan/feat` | always |
| `arch-critic` | reviewer | `plan/epic-arch`, `plan/feat-arch` | always |
| `perf-critic-backend` / `-frontend` | reviewer | arch routes, verification gates | only when trigger criteria (top of their files) fire |
| `task-checker` | reviewer | `plan/tasks` | after self-review; max two runs |
| `feature-coder` | executor | `do/all-tasks` | one per parallelizable task per wave |
| `ui-consistency-reviewer` | reviewer | verification gates | UI features, non-trivial surface |
| `doc-coherence-reviewer` | reviewer | verification gates · `plan/change` · `plan/migrate` | epic completion · after change · after migration |

Verification gates (+ their subagents) run in `do/verify` or inline as final phase of `do/all-tasks`

## Human review UX

Conclusions, not process. Mechanical checks auto-verified → one summary line. **"Decisions requiring your validation"**: ≤10 plain-sentence statements + open questions labeled blocking/important/minor. Validated decisions → `docs/decisions.md`. Stakeholder answers **verbatim** — never paraphrase, never re-ask (if ambiguous, ask only clarification)

## Working Economy (Invariant 17)

### Input economy

- Prefer LSP/semantic nav over whole-file reads; scoped line ranges
- Prefer Grep/Glob/LSP over Shell for code search — Shell only when needed
- Long CLI output (tests, builds, git, package managers) through repo-declared filter (e.g. `rtk`, `snip`) — `do/init` sets up; if Shell used without active hook, prefix manually
- Never re-read what's in context; never load doc "for safety"
- Obey economy profile + inline-first before spawning (Subagents)

### Output style (principal and subagents)

- Caveman-concise (same bar as agent-facing docs): no preamble, no restating request, no trailing summary, no filler/hedging
- Code, commands, paths, errors: byte-exact — never paraphrase
- Code changes as diffs or targeted edits — never full-file listings unless asked
- Research answers ≤10 lines unless depth requested; subagent returns obey Return-payload cap
- Handoff (Invariant 13) = only closing block: ≤5 lines

### Minimal implementation (do routes and feature-coder)

Understand fully, stop at first rung that holds:

1. Doesn't need to exist → skip (YAGNI)
2. Already in codebase → reuse
3. Stdlib does it → use it
4. Native platform feature → use it
5. Installed dependency → use it
6. One line suffices → one line
7. Only then write minimum that works

Never cut: trust-boundary validation, data-loss handling, security, accessibility

### Document style

Two audiences — pick by file purpose, not route mood

**Human / business (full prose)** — PRDs (`epic-prd.md`, `feat-prd.md`), `docs/product.md`, Product Spirit, human review bodies (`*-review.md` decision sections), user-centric docs (`developer-setup`, onboarding, human READMEs). Complete sentences. Stakeholder-readable. No unexplained abbreviations

**Agent-facing (caveman-concise)** — skill playbooks (`SKILL.md`, `routes/`, `subagents/`, template comments), `feat-tasks.md`, `epic-arch.md` / `feat-arch.md`, status tables/notes, living technical docs (`data-model.md`, `ui-map.md`, `decisions.md`), `docs/patterns/*`. Inspired by [caveman](https://github.com/JuliusBrussee/caveman) **full**:

- Facts and orders only — drop articles/filler/hedging when meaning clear; fragments OK
- Short synonyms; pattern `[thing] [action] [reason]` · `[next step]`
- No invented abbreviations (`cfg`/`impl`/`fn`); well-known tech acronyms OK (DB/API/HTTP)
- Paths, symbols, code, commands, error strings: exact
- Never drop `not`/`never`/`no`/`only`/`except`
- No trailing period before linefeed (mid-line periods in multi-clause lines stay)
- Decisions and facts only — never process ("reviewer suggested…", "after discussion…")
- Justify only when future agent needs why (trade-off, scope cut): ≤2 short lines
- Auto-clarity: fuller prose for security warnings, irreversible steps, or fragments that risk misread order/negation — then resume concise

**Changelog hard rule**: one line `{date}: {fact}`, ≤25 words. Eligible only — project: epic completed, major scope change, migration; epic: feature verified 🟢, scope change. All else (tasks generated, PRD drafted/approved, waves, syncs, drift repairs) = **no entry**. Never: critic exchanges (Invariant 16), task lists, gate results, progress numbers, `Next:` commands. Verbose existing entries = legacy, never precedent — write only eligible line, or nothing

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

Repo conventions, precedence: `CLAUDE.md` · `AGENTS.md` · `.github/copilot-instructions.md` · `.cursor/rules/` · `.github/instructions/`. `do/memorize` writes back to file(s) actually present

## Templates

In `templates/` — names mirror output files
