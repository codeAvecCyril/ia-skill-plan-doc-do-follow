# do/init — Token-Saving Tooling Setup

**Purpose**: set up, once per project, the tooling that reduces token consumption on every later route. Idempotent — re-running reports what exists and recommends only what is missing

**Mindset**: pragmatic toolsmith — recommend only what this project will actually use; never install without user confirmation

**Inputs**: the repository tree (languages, build/test commands) · repository instruction file(s) (SKILL.md → Platform integration) · the environment's plugin/LSP capabilities

**Outputs**: user-approved tooling installed/configured · a short **Tooling** section in the repository instruction file

## Steps

1. Detect the project's languages and the commands producing long outputs (tests, builds, linters, package managers)
2. **LSP** — check for a language server per detected language (e.g. Claude Code plugins `pyright-lsp`, `typescript-lsp`, `rust-analyzer`); recommend the missing ones
3. **CLI output filters** — recommend a compression proxy for long-output commands: `rtk` (Rust, zero config) or `snip` (Go, YAML filters), with the prefix convention (e.g. `rtk git diff`)
4. **Code graph / semantic index** — large codebases only, if the environment supports MCP; skip for small repositories (Cost gate)
5. Present recommendations one line each with expected saving; install only what the user approves
6. Record the adopted tooling in the repository instruction file — one short **Tooling** section: active LSPs, filter prefix and target commands, index/graph tool. Every route reads this file
7. Handoff: resume the interrupted route, or `plan/proj` for a fresh project
