# Reviewer Subagent Briefs

Rules for all reviewers:

- **Scoped context**: give the reviewer exactly the inputs listed in its brief — nothing more. Always prepend the Product Spirit block from `docs/project-status.md` and the relevant lines of `docs/decisions.md`.
- **Respect recorded decisions**: reviewers may challenge a design against the state of the art, but a conflict with a recorded user decision is raised as a question for the user, never as a change to apply.
- **Output format**: numbered, actionable comments in complete sentences, ordered by importance, each stating the problem, why it matters, and a concrete suggestion. No vague praise, no restating the document.
- **Main agent duty**: apply each comment or record in the handoff why it was rejected.

---

## PRD Critic

Run by: `plan/epic` (on epic-prd), `plan/feat` (on feat-prd).

**Inputs**: Product Spirit block · the PRD under review · its parent document (epic-brief for an epic PRD, epic-prd for a feature PRD) · relevant `docs/decisions.md` lines.

**Review questions**:
1. Does the PRD respect the product vision and stay within the parent's scope?
2. Which features/requirements are the truly differentiating ones, and which are unnecessary and could be cut or deferred?
3. Is the user journey optimal — intuitive, comfortable, efficient? How could it be improved?
4. How could the whole be simplified while keeping the real added value?
5. Are all statements written in complete, unambiguous sentences a stakeholder can validate without guessing? Flag every abbreviation or compressed idea that could be misread.
6. For UI features: is the Entry Points & Navigation section present, and does it place the feature coherently in `docs/ui-map.md`?

## Arch Critic

Run by: `plan/epic-arch` (on epic-arch), `plan/feat-arch` (on feat-arch).

**Inputs**: Product Spirit block · the architecture document under review · the corresponding PRD · `docs/global_architecture.md` · `docs/technical-stack.md` · `docs/data-model.md` (if it exists) · relevant `docs/decisions.md` lines.

**Review questions**:
1. Is the end-to-end data path valid and robust (every flow traced from entry to persistence and back)?
2. Does the design respect the global architecture, the technical stack, and existing patterns?
3. What alternative designs exist, and what are the pros and cons of each? Is the chosen one justified?
4. How could the architecture be simplified while staying robust, scalable, and maintainable?
5. Do data model changes extend `docs/data-model.md` consistently (naming, relations, conventions), rather than forking it?
6. Are security, performance, and failure modes addressed proportionally to the actual risk (no boilerplate, no blind spots)?

## UI Consistency Reviewer

Run by: `do/verify` — only for features with UI requirements.

**Inputs**: Product Spirit block · the feature PRD's UI Requirements and Entry Points & Navigation sections · `docs/ui-map.md` · `docs/design-guidelines.md` · the implemented UI code (components, styles, routing) for this feature.

**Review questions**:
1. Is the feature reachable exactly as declared in `docs/ui-map.md` (menu entry, route, breadcrumb)? Can a first-time user discover it?
2. Do components, spacing, colors, and typography follow `docs/design-guidelines.md` and match sibling screens?
3. Is terminology (labels, buttons, messages) consistent with the rest of the application?
4. Are empty, loading, and error states present and styled like the rest of the app?
5. Are accessibility basics respected (keyboard navigation, focus states, contrast, touch targets)?

## Task Self-Containment Check

Run by: `plan/tasks`, after the task breakdown is drafted.

**Inputs**: `feat-tasks.md` only — deliberately **without** the PRD or architecture documents.

**Review questions** (for each task):
1. Could a weaker model execute this task using only its text? WHAT / WHERE / HOW / WHY / DONE must all be explicit.
2. Are file paths exact, steps concrete, and validation commands runnable as written?
3. Are there references ("as described in the PRD", "see architecture") that require opening another document? Each one is a failure.

**Output**: the list of tasks that fail, and exactly what is missing from each.

## Doc Coherence Reviewer

Run by: `do/verify` when an epic completes · `plan/change` after applying a change · on demand.

**Inputs**: `docs/project-status.md` · all `epic-status.md` files · all `feat-tasks.md` Task Summary tables · `docs/ui-map.md` · `docs/data-model.md` · `docs/decisions.md`.

**Review questions**:
1. Does every stored status match the value derived by the Status Model rules?
2. Does `docs/data-model.md` match the schema actually implemented (migrations, models)?
3. Does `docs/ui-map.md` list every shipped screen and entry point, and nothing that does not exist?
4. Are recorded decisions still respected by the current documents?
5. Are all inter-document links valid?

**Output**: a drift list; the calling route fixes each item via Status Sync or targeted doc updates.
