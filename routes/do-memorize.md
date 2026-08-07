# do/memorize — Document Good Practices

**Purpose**: capture good practices, patterns, fixes for recurring blockers, project-specific usage (test/launch commands, dependency installation)

**Mindset**: librarian — one pattern, one file; generalize lesson, keep concrete example

**Inputs**: practice/pattern/fix observed · existing `docs/patterns/` · repository instruction file(s) (SKILL.md → Platform integration)

**Outputs**: pattern file in `docs/patterns/` · reference in platform-native instruction file(s)

## Steps

1. Check practice already documented in `docs/patterns/`
2. If yes, update with new insight. If not, create `docs/patterns/{pattern-name}.md`: description, when to use, concrete example, benefits/trade-offs, related links
3. Reference pattern from every instruction file present (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.cursor/rules/`), one line saying when to apply
4. Handoff with next command based on current workflow stage
