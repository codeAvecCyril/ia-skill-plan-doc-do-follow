# Task Breakdown — {feature-name}

> **Feature**: F{n} — {feature-name}
>
> **Epic**: E{n} — {epic-name}
>
> **Last Updated**: {date}

<!-- Delete any section that does not apply. Never write "N/A".
     In solo mode, omit the Effort column. -->

## Task Summary

<!-- OWNING TABLE: this is the SINGLE source of truth for task status.
     Per-task sections below carry NO status — update only this table. -->

| Code | Task    | Type                                        | Depends on | Status |
| ---- | ------- | ------------------------------------------- | ---------- | ------ |
| T1   | {title} | Database/Backend/API/Frontend/Test/Config   | —          | ⚪     |
| T2   | {title} | {type}                                      | T1         | ⚪     |

**Parallelizable**: {e.g. T2 and T3 are independent}
**Critical path**: {e.g. T1 → T2 → T4}

## Dependency Graph (optional, decorative)

<!-- Regenerated from the Task Summary table; never a source of truth. -->

```mermaid
graph TD
    T1[T1: title] --> T2[T2: title]
```

---

## Task Details

<!-- Every task must be executable by a weaker model WITHOUT opening the PRD
     or any other document: WHAT / WHERE / HOW / WHY / DONE all explicit. -->

### T1: {title}

**Objective (WHAT/WHY)**: {one complete sentence: what is built and why}
**Context**: {2–3 sentences of everything needed to work standalone}

**Files (WHERE)**:
- Create: `exact/path/to/file`
- Modify: `exact/path/to/file`

**Steps (HOW)**:
1. {concrete step}
2. {concrete step}

**Pattern reference**: `docs/patterns/{pattern}.md` (if one applies)

**Done when (DONE)**:
- [ ] {verifiable criterion}
- [ ] Tests: {what to test and how}
- [ ] Validation command(s): `{runnable command}`

**Notes**: {known pitfalls — delete if none}

---

### T2: {title}

{same structure}

---

## Blockers

- [ ] {blocker, as a complete sentence — delete section if none}

## Risks (optional)

| Risk | Likelihood | Impact | Mitigation |
| ---- | ---------- | ------ | ---------- |
