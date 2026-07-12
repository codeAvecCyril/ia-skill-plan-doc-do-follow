# Epic Review — {epic-name} (E{n})

> **Review Date**: {date}
>
> **Reviewed By**: {stakeholder names}
>
> **Status**: ⚪ Not Started | 🟡 In Review | 🟢 Approved | 🔴 Needs Changes

## Executive Summary

{3–5 complete sentences: what this epic delivers, its features, and the main open risk.}

## Automated Checks (verified by the AI)

> ✅ {n}/{total} structural checks passed — {one line listing any failures}.

<details><summary>Details — PRD review</summary>

- [ ] Feature list covers the epic scope; features are sized and prioritized
- [ ] User stories are clear and testable; acceptance criteria are measurable
- [ ] Edge cases and out-of-scope are documented
- [ ] Success metrics are defined
- [ ] Every statement is a complete sentence with no unexplained abbreviations
- [ ] Consistent with the Product Spirit block and `docs/decisions.md`

</details>

<details><summary>Details — Architecture review</summary>

- [ ] End-to-end data path is traced and valid
- [ ] Design fits `docs/global_architecture.md` and `docs/technical-stack.md`
- [ ] Data model delta is recorded in `docs/data-model.md`
- [ ] Navigation impact is recorded in `docs/ui-map.md` (UI epics)
- [ ] Security, performance, and failure modes addressed proportionally to risk

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

- PRD approved: `@plan/epic-arch E{n}`
- Architecture approved: `@plan/feat E{n} F1`
- Needs rework: address the items above, then resubmit.
