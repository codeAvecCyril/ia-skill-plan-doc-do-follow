# Subagent Definitions

One file per subagent. The calling route names the subagent; the principal agent reads its file, assembles the scoped inputs the file lists, and spawns a generic subagent with the file body as its system prompt plus the inputs as its working context. This works on every platform that can spawn a task/subagent — no platform-specific agent registry is required.

## Portable format

Each definition is **Markdown with YAML frontmatter** — the shape every major platform has converged on (Claude Code `.claude/agents/*.md`, GitHub Copilot `.github/agents/*.agent.md`, opencode `.opencode/agent/*.md`). Only two frontmatter fields are universal, and they are the only ones we require:

```yaml
---
name: kebab-case-identifier
description: Trigger-style sentence — what it does AND when to invoke it.
model_class: reasoning | standard   # advisory: capability class, never a model id
thinking: deep | brief              # advisory: how much deliberation the job deserves
capabilities: read-only | read-write | read-run-write   # advisory: what it may touch
---
```

`model_class`, `thinking`, and `capabilities` are **advisory hints**, deliberately named so they collide with no platform's reserved keys (platforms ignore unknown frontmatter). They describe the *kind* of model and access the agent needs, never a vendor model name — model names change monthly; capability classes don't.

- `model_class: reasoning` — critics and architects: needs a strong model with real judgment.
- `model_class: standard` — mechanical checks and packet execution: any competent coding model.
- `thinking: deep` — enable extended thinking / high reasoning effort where the platform supports it.
- `capabilities` — the caller must not grant more: a `read-only` critic gets no edit or execute tools.

## Installing natively (optional)

These files also work as drop-in native agents. When copying one into a platform registry, add the platform-specific keys next to the portable ones:

| Platform | Location | Add |
| --- | --- | --- |
| Claude Code | `.claude/agents/{name}.md` | `tools:` (e.g. `Read, Grep, Glob` for read-only), `model:` mapped from `model_class` |
| GitHub Copilot | `.github/agents/{name}.agent.md` | `tools:` in Copilot's vocabulary; rename file to `.agent.md` |
| opencode | `.opencode/agent/{name}.md` | `mode: subagent`, `tools:`/`permission:` blocks |

Never hardcode a model id in these files — map `model_class` at install time.

## Roster

| Subagent | Kind | Called by |
| --- | --- | --- |
| `repo-scout` | research | planning routes needing ground truth from the code |
| `prd-critic` | reviewer | `plan/epic`, `plan/feat` |
| `arch-critic` | reviewer | `plan/epic-arch`, `plan/feat-arch` |
| `perf-critic-backend` | reviewer (conditional) | `plan/epic-arch`, `plan/feat-arch`, `do/verify` |
| `perf-critic-frontend` | reviewer (conditional) | `plan/epic-arch`, `plan/feat-arch`, `do/verify` |
| `task-checker` | reviewer | `plan/tasks` |
| `feature-coder` | executor | `do/all-tasks` (one per parallelizable task) |
| `ui-consistency-reviewer` | reviewer | `do/verify` (UI features) |
| `doc-coherence-reviewer` | reviewer | `do/verify` (epic completion), `plan/change`, `plan/migrate` |

## Rules for all subagents

- **Scoped context** (Invariant 14): the caller passes exactly the inputs the definition lists — never "read everything". Reviewer briefs always include the Product Spirit block and the relevant `docs/decisions.md` lines.
- **Respect recorded decisions**: a conflict with a recorded user decision is raised as a question for the user, never applied as a change.
- **Reviewer output format**: numbered, actionable findings in complete sentences, ordered by severity, each stating the problem, why it matters, and a concrete suggestion. No praise, no restating the document.
- **Main agent duty**: apply each finding or record in the handoff why it was rejected.
