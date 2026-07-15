# Moved: subagent definitions now live in `subagents/`

The reviewer briefs formerly in this file are now individual, platform-portable agent definitions — one file per agent with YAML frontmatter (format spec in `subagents/README.md`):

- PRD Critic → `subagents/prd-critic.md`
- Arch Critic → `subagents/arch-critic.md`
- UI Consistency Reviewer → `subagents/ui-consistency-reviewer.md`
- Task Self-Containment Check → `subagents/task-checker.md`
- Doc Coherence Reviewer → `subagents/doc-coherence-reviewer.md`

New in v3.1: `subagents/repo-scout.md`, `subagents/feature-coder.md`, `subagents/perf-critic-backend.md`, `subagents/perf-critic-frontend.md`.

The rules that applied to all reviewers (scoped context, respect recorded decisions, numbered actionable findings, apply-or-record duty) are preserved in `subagents/README.md` and inside each definition.
