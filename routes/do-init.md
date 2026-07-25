# do/init — Token-Saving Tooling Setup

**Purpose**: set up, once per project, the tooling that reduces token consumption on every later route. Idempotent — re-running reports what is already in place and recommends only what is missing

**Mindset**: pragmatic toolsmith — recommend only what this project will actually use; never install anything without the user's confirmation

**Inputs**: the repository tree (languages, build/test commands) · repository instruction file(s) (SKILL.md → Platform integration) · the environment's plugin/LSP capabilities

**Outputs**: user-approved tooling installed/configured · a short **Tooling** section in the repository instruction file so every future route (and every AI environment) uses it

## Steps

1. Detect the project's languages and the commands that produce long outputs (test suites, builds, linters, package managers)
2. **LSP** — check whether the environment has a language server for each detected language (e.g. Claude Code plugins `pyright-lsp`, `typescript-lsp`, `rust-analyzer`); recommend installing the missing ones. Semantic navigation (definition, references, symbols, diagnostics) replaces whole-file reads and grep sweeps
3. **CLI output filters** — recommend a compression proxy for long-output commands: `rtk` (Rust single binary, zero config, 100+ commands) or `snip` (Go, declarative YAML filters), with the prefix convention (e.g. `rtk git diff`, `rtk npm test`)
4. **Code graph / semantic index** (large codebases only) — where find/grep exploration is expensive, suggest a tree-sitter-based repo map or code-graph MCP server if the environment supports MCP; skip for small repositories (Cost gate)
5. Present the recommendations as one line each with the expected saving; install only what the user approves
6. Record the adopted tooling in the repository instruction file — one short **Tooling** section: which LSPs are active, which filter prefix to use and on which commands, which index/graph tool exists. Every route reads this file, so the convention propagates automatically
7. Handoff: resume the interrupted route, or `plan/proj` for a fresh project
