# plan-doc-do-follow Skill

A comprehensive product development workflow: **Plan** your product → **Doc**ument specifications → **Do** the work → **Follow** up with verification.

Structured planning with built-in business reviews, single-source-of-truth status tracking, scope-change management, and clear routing from product vision to shipped features. Project- and environment-agnostic: works for backend, frontend, fullstack, mobile, SaaS, or batch projects, in Claude Code, Cursor, GitHub Copilot, or any AI environment that reads skills.

## Installation

### Cursor (project skill)

```bash
git submodule add git@github.com:codeAvecCyril/ia-skill-plan-doc-do-follow.git .claude/skills/plan-doc-do-follow
mkdir -p .cursor/skills/plan-doc-do-follow
```

Create `.cursor/skills/plan-doc-do-follow/SKILL.md` pointing to `.claude/skills/plan-doc-do-follow/SKILL.md`.

### Cursor (personal skill)

```bash
git clone git@github.com:codeAvecCyril/ia-skill-plan-doc-do-follow.git ~/.cursor/skills/plan-doc-do-follow
```

### Claude Code (project skill)

```bash
git submodule add git@github.com:codeAvecCyril/ia-skill-plan-doc-do-follow.git .claude/skills/plan-doc-do-follow
```

### Project prerequisites

- `docs/product.md` — product vision
- `docs/global_architecture.md` — system architecture
- `docs/technical-stack.md` — technology decisions
- A repository instruction file, whichever your environment uses: `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, or `.cursor/rules/` (optional)

## Design principles

- **One fact, one file.** Each status is written in exactly one owning table: task status in `feat-tasks.md`, feature status in `epic-status.md`, epic status in `docs/project-status.md`. No `feat-status.md` file, no per-task status lines, no duplicated legends. Nothing to keep in sync means nothing drifts.
- **Status Sync.** One deterministic, idempotent procedure recomputes every level bottom-up from document reality. Every status-changing route ends with it, and `do/sync-status` repairs any drift on demand.
- **Epic-first architecture.** The epic architecture is the real design level. Features carry a short "Architecture Delta" in their PRD; a dedicated `feat-arch.md` exists only when explicit trigger criteria fire (new integration, new entity, new component, new security surface).
- **Living global docs.** `docs/data-model.md` (schema truth), `docs/ui-map.md` (navigation truth), `docs/design-guidelines.md` (style contract), and `docs/decisions.md` (binding user decisions) are updated in the same change that affects them — `do/verify` enforces the data and UI gates.
- **Reviews built for humans.** The AI auto-verifies mechanical checks and collapses them to one line; the human validates at most 10 plain-sentence decisions per review. Validated decisions are recorded and respected by every later route.
- **Product Spirit.** A 5–10 sentence distillation of the product's identity sits at the top of `project-status.md` and is injected into every planning route and reviewer, so the vision never dissolves into generic AI knowledge.
- **Model tiering.** Planning routes and reviewers assume a strong model; `plan/tasks` produces tasks a weaker model can execute without opening the PRD, verified by a self-containment check.
- **Token economy.** `SKILL.md` is a thin router; each route's playbook loads on demand from `routes/`; document scaffolds load from `templates/`; subagent definitions load on demand from `subagents/` with scoped inputs, not "read everything"; execution subagents get self-contained task packets.

## 16 Routes, 2 Phases

**Plan Phase**:
- `plan/proj` — Extract epics from product vision, bootstrap living docs
- `plan/proj-review` — Validate epics
- `plan/epic` — Create epic PRD
- `plan/epic-review` — Validate epic PRD or architecture
- `plan/epic-arch` — Design epic architecture
- `plan/feat` — Create feature PRD (with Entry Points and Architecture Delta)
- `plan/feat-review` — Validate feature PRD or architecture
- `plan/feat-arch` — Design feature architecture (exception cases only)
- `plan/tasks` — Break into self-contained tasks
- `plan/change` — Scope change: add or update a feature/epic, **including on an already implemented epic**
- `plan/migrate` — One-shot migration of a v2-documented project to the v3 structure

**Do Phase**:
- `do/task` — Implement a task
- `do/all-tasks` — Implement all feature tasks in parallel waves
- `do/verify` — Verify completion (the only route that sets 🟢 DONE)
- `do/sync-status` — Recompute all statuses from reality, repair drift
- `do/memorize` — Document patterns and best practices

## Subagents

Defined in `subagents/` — one portable Markdown + YAML-frontmatter file per agent, each with a scoped input list, an output contract, and advisory `model_class` / `thinking` / `capabilities` hints (never a vendor model id — see `subagents/README.md` for the format and the mapping to Claude Code, GitHub Copilot, and opencode native registries):

- **repo-scout** — read-only codebase researcher; grounds plans in what actually exists (planning routes, on demand)
- **prd-critic** — vision fit, differentiating vs unnecessary features, user journey, clarity of sentences
- **arch-critic** — data-path validity, global-architecture fit, alternatives, simplification
- **perf-critic-backend / perf-critic-frontend** — conditional performance reviews at design time and verify time, invoked only when their trigger criteria fire (unbounded data, hot request paths, large lists, real-time flows, explicit NFRs)
- **task-checker** — every task executable without opening the PRD (runs at `plan/tasks`)
- **feature-coder** — executes one self-contained task packet per instance (runs in `do/all-tasks` waves)
- **ui-consistency-reviewer** — entry point reachable, style/terminology/states consistent with the design guidelines (runs at `do/verify` for UI features)
- **doc-coherence-reviewer** — statuses, living docs, and links match reality (runs at epic completion, after `plan/change`, after `plan/migrate`)

Each route also opens with a one-line **Mindset** that specializes the principal agent (product strategist, staff architect, orchestrator, skeptical QA gatekeeper, …) without any platform-specific model switching.

## Output Files

```
docs/
├── project-status.md          ← Product Spirit + epic statuses (owning table)
├── project-review.md
├── decisions.md               ← binding user decisions (living)
├── data-model.md              ← global schema truth (living)
├── ui-map.md                  ← global navigation truth (living, UI projects)
├── design-guidelines.md       ← UI style contract (living, UI projects)
├── patterns/                  ← from do/memorize
└── epics/e{n}-{epic-name}/
    ├── epic-brief.md
    ├── epic-prd.md
    ├── epic-status.md         ← feature statuses (owning table)
    ├── epic-arch.md
    ├── epic-review.md
    └── features/f{n}-{feat-name}/
        ├── feat-prd.md        ← includes Entry Points & Architecture Delta
        ├── feat-arch.md       ← exception cases only
        ├── feat-tasks.md      ← task statuses (owning table)
        └── feat-review.md
```

## Status Tracking

| Status | Emoji | Meaning                    |
| ------ | ----- | -------------------------- |
| TODO   | ⚪    | Not started                |
| SPEC   | 🟡    | Specified                  |
| PLAN   | 🟣    | Tasks generated            |
| DEV    | 🔵    | Implementation in progress |
| DONE   | 🟢    | Verified complete          |

Statuses are **derived, not maintained**: the Status Model in `SKILL.md` defines how each level is computed from the level below, and Status Sync applies it.

## Typical Usage

**New project:** `plan/proj → plan/epic → plan/epic-arch → plan/feat → plan/tasks → do/task → do/verify`

**New feature on a shipped epic:** `plan/change` (classifies, reopens statuses, routes to `plan/feat`)

**Changed my mind about an implemented feature:** `plan/change` (appends tasks, never rewrites history)

**Statuses look wrong:** `do/sync-status`

## Migrating from v2

Run `plan/migrate` once — it works even with epics and features half implemented. It consolidates task statuses from all the v2 locations into the owning tables (most-advanced-wins, with 🟢 spot-checked against the code), removes `feat-status.md` files, distills the Product Spirit block, bootstraps the living docs (seeding `docs/decisions.md` from old review sign-offs and reverse-engineering `docs/data-model.md` and `docs/ui-map.md` from the implemented code), runs Status Sync plus the Doc Coherence Reviewer, and hands you a migration report. Legacy PRDs are not rewritten: missing v3 sections are filled lazily the first time a route touches that feature.

---

**Version**: 3.1 (single-source status, scope changes, v2 migration, living docs, token-optimized routing, portable subagent definitions in `subagents/`, conditional performance critics, per-route Mindset)
**License**: Apache-2.0 — see [LICENSE](LICENSE)

**The philosophy**: Plan well, document clearly, execute focused, follow up consistently. Build great products.
