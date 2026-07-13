# Feature Review — {feature-name} (E{n} F{n})

> **Review Date**: {date}
>
> **Reviewed By**: {stakeholder names}
>
> **Status**: ⚪ Not Started | 🟡 In Review | 🟢 Approved | 🔴 Needs Changes

## Executive Summary

{3–5 complete sentences: what this feature does, how users reach it, and the main open risk.}

## Automated Checks (verified by the AI)

> ✅ {n}/{total} structural checks passed — {one line listing any failures}.

<details><summary>Details — PRD review</summary>

- [ ] User stories are clear and testable; acceptance criteria are specific and measurable
- [ ] Edge cases and error scenarios are documented; out-of-scope is explicit
- [ ] Entry Points & Navigation is filled and registered in `docs/ui-map.md` (UI features)
- [ ] Architecture Delta is present (or explicitly "None")
- [ ] Test strategy is defined
- [ ] Every statement is a complete sentence with no unexplained abbreviations
- [ ] Consistent with the Product Spirit block and `docs/decisions.md`

</details>

<details><summary>Details — Architecture review</summary>

- [ ] The delta fits within the epic architecture
- [ ] APIs are well-defined; data model delta is recorded in `docs/data-model.md`
- [ ] Technology choices specific to this feature are justified
- [ ] Security and performance implications are addressed where real

</details>

## Decisions Requiring Your Validation

<!-- Max 10 self-contained plain sentences. Validated decisions go to docs/decisions.md. -->

1. {Plain-sentence decision statement}. **Confirm?**

## Open Questions

- [blocking] {question}
- [important] {question}
- [minor] {question}

## Sign-Off

| Role            | Scope        | Name   | Date   | Status  |
| --------------- | ------------ | ------ | ------ | ------- |
| Product Manager | PRD          | {name} | {date} | ⚪ ⚡ 🟢 🔴 |
| Technical Lead  | Architecture | {name} | {date} | ⚪ ⚡ 🟢 🔴 |

Legend: ⚪ Pending, ⚡ In Review, 🟢 Approved, 🔴 Needs Changes

## Action Items

| Item     | Owner   | Due Date |
| -------- | ------- | -------- |

## Next Steps

- PRD approved: `@plan/tasks E{n} F{n}` (or `@plan/feat-arch E{n} F{n}` if a trigger criterion fired)
- Architecture approved: `@plan/tasks E{n} F{n}`
- Needs rework: address the items above, then resubmit.
