# do/init — Token-Saving Tooling Setup

**Purpose**: set up, once per project, tooling that reduces token consumption on every later route. Idempotent — re-running reports what exists and recommends only what is missing

**Mindset**: pragmatic toolsmith — recommend only what this project will actually use; never install without user confirmation

**Inputs**: repository tree (languages, build/test commands) · repository instruction file(s) (SKILL.md → Platform integration) · environment's plugin/LSP capabilities

**Outputs**: user-approved tooling installed/configured · short **Tooling** section in repository instruction file

## Steps

1. Detect project's languages and commands producing long outputs (tests, builds, linters, package managers)
2. **LSP** — check language server per detected language (e.g. Claude Code plugins `pyright-lsp`, `typescript-lsp`, `rust-analyzer`); recommend missing ones
3. **CLI output filters** — recommend compression proxy for long-output commands: `rtk` (Rust, zero config) or `snip` (Go, YAML filters), with prefix convention (e.g. `rtk git diff`)
4. **Code graph / semantic index** — large codebases only, if environment supports MCP; skip for small repositories (inline-first / Cost gate)
5. **Subagent economy profile** — present `strict` | `balanced` | `quality` (SKILL.md → Economy profile); recommend `strict` when token cost dominates, `balanced` as default, `quality` only if user prioritizes isolated review over tokens. Record chosen value
6. Present recommendations one line each with expected saving; install only what user approves
7. Record adopted tooling in repository instruction file — one short **Tooling** section: active LSPs · filter prefix and target commands · index/graph tool if any · `Subagent economy: {strict|balanced|quality}`. Every route and every subagent brief reads this file
8. Handoff: resume interrupted route, or `plan/proj` for fresh project
