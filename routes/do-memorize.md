# do/memorize — Document Good Practices

**Purpose**: capture good practices, patterns, fixes for recurring blockers, and project-specific usage (test/launch commands, dependency installation)

**Mindset**: librarian — one pattern, one file; generalize the lesson, keep the concrete example

**Inputs**: the practice/pattern/fix observed · existing `docs/patterns/` · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: a pattern file in `docs/patterns/` · a reference in the platform-native instruction file(s)

## Steps

1. Check whether the practice is already documented in `docs/patterns/`
2. If yes, update it with the new insight. If not, create `docs/patterns/{pattern-name}.md`: description, when to use, concrete example, benefits/trade-offs, related links
3. Reference the pattern from every instruction file present (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.cursor/rules/`), one line saying when to apply it
4. Handoff with the next command based on the current workflow stage
