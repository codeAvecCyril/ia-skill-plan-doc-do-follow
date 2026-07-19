# do/memorize — Document Good Practices

**Purpose**: capture good practices, patterns, fixes for recurring blockers, and project-specific usage (test commands, launch commands, dependency installation) for future reference

**Mindset**: librarian — one pattern, one file; generalize the lesson, keep the concrete example

**Inputs**: the practice/pattern/fix observed · existing `docs/patterns/` · the repository instruction file(s) present (resolution order in SKILL.md → Platform integration)

**Outputs**: a pattern file in `docs/patterns/` · a reference added to the platform-native instruction file(s)

## Steps

1. Read the existing `docs/patterns/` index and check whether the practice is already documented
2. If it is, update it with the new insight or example. If not, create `docs/patterns/{pattern-name}.md` with: description, when to use it, a concrete example, benefits and trade-offs, links to related docs or standards
3. Reference the pattern from whichever instruction files exist in the repository (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.cursor/rules/` — update all that are present so every AI environment sees it), with one line saying when to apply it
4. Handoff with the next command based on the current workflow stage
