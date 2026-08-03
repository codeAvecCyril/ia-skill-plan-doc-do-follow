# plan/epic-arch E{n} — Epic Architecture

**Purpose**: design the epic's technical architecture — the primary architecture level; features inherit from it and normally only declare deltas

**Mindset**: staff architect — trace every data path end to end, prefer the simplest design that survives the stated scale, justify choices against alternatives. Strong model, deep thinking

**Inputs**: `epic-prd.md` · `docs/global_architecture.md` · `docs/technical-stack.md` · `docs/data-model.md` (if it exists) · related epic architectures if applicable

**Outputs**: `epic-arch.md` · updated `docs/data-model.md` · updated `docs/ui-map.md` (if UI) · updated `epic-review.md` (Architecture gate)

## Steps

1. Verify `docs/project-status.md` contains `E{n}` and read `epic-prd.md`
2. Design: components, data model, APIs, integration points, risks, metrics. Where a topic matches `docs/global_architecture.md`, one referencing sentence. Brownfield: ground the design first via precise questions to a **repo-scout** subagent
3. Ask questions on any architectural ambiguity (Invariant 8)
4. Generate `epic-arch.md` from `templates/epic-arch.md`
5. Sync living docs in the same change (Invariant 10): entities → `docs/data-model.md` (the global truth; the arch doc describes only the delta and links to it); screens/navigation → `docs/ui-map.md`
6. Run the **arch-critic** subagent and handle its findings (SKILL.md → Subagents). Check the perf-critic trigger criteria (top of `subagents/perf-critic-backend.md` and `-frontend.md`): run each side that fires, resolve blockers; if none fires, skip and note it
7. **Update `epic-review.md`** (same file as the PRD review, one section per gate): auto-verify the architecture checklist, collapse to one line; add **"Architecture — Decisions Requiring Your Validation"** (max 10 plain sentences a tech lead can validate in isolation) plus arch-specific open questions; set the Tech Lead sign-off row to ⚪ pending. Leave PRD-review sections untouched
8. Handoff: `plan/epic-review E{n} arch` (or `plan/feat E{n} F1` if the user skips reviews)
