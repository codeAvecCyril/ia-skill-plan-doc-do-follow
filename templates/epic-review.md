# Epic Review — {epic-name} (E{n})

> **Review Date**: {date}
>
> **Reviewed By**: {stakeholder names}
>
> **Status**: ⚪ Not Started | 🟡 In Review | 🟢 Approved | 🔴 Needs Changes

## Executive Summary

{3–5 complete sentences: what this epic delivers, its features, and the main open risk.}

## Automated Checks (verified by the AI)

> ✅ {n}/{total} structural checks passed — {one line listing any failures}

<details><summary>Details — PRD review</summary>

- [ ] Feature list covers the epic scope; features are sized and prioritized
- [ ] User stories are clear and testable; acceptance criteria are measurable
- [ ] Edge cases and out-of-scope are documented
- [ ] Success metrics are defined
- [ ] Every statement is a complete sentence with no unexplained abbreviations
- [ ] Consistent with the Product Spirit block, the epic brief, and earlier review answers

</details>

<details><summary>Details — Architecture review</summary>

- [ ] End-to-end data path is traced and valid
- [ ] Design fits `docs/global_architecture.md` and `docs/technical-stack.md`
- [ ] Data model delta is recorded in `docs/data-model.md`
- [ ] Navigation impact is recorded in `docs/ui-map.md` (UI epics)
- [ ] Security, performance, and failure modes addressed proportionally to risk

</details>

## Decisions Requiring Your Validation

<!-- Write every item per guides/review-questions.md (load it) — mandatory format below
     Only real decisions · plain words · impact of each answer · bold **Confirm?** = full question
     Answer applied into reviewed doc; question + answer stay here verbatim — never rewritten, never re-asked
     Max 10 items PER GATE · plan/epic fills PRD, plan/epic-arch fills Architecture; delete heading with no gate yet -->

### PRD (filled by plan/epic, answered by the product owner)

#### D1 — {the choice, in plain words}

**Situation**: {which user, business process, or moment this touches — plain words}
**Impact**:
- **If yes**: {concrete consequence for users, effort, cost, risk}
- **If no**: {concrete consequence}
**Recommendation**: {option + one-sentence reason} · {Easy | Hard to change later — why}

**Confirm?** {one explicit question, answerable by yes/no or A/B}
> **Your answer**:

### Architecture (filled by plan/epic-arch, answered by the tech lead)

#### A1 — {the choice, in plain words}

**Situation**: {which user, business process, or moment this touches — plain words}
**Impact**:
- **If yes**: {concrete consequence for users, effort, cost, risk}
- **If no**: {concrete consequence}
**Recommendation**: {option + one-sentence reason} · {Easy | Hard to change later — why}

**Confirm?** {one explicit question, answerable by yes/no or A/B}
> **Your answer**:

## Open Questions

<!-- Plain words, blocking first — guides/review-questions.md → Open questions -->

- [blocking] {plain question} — Why it matters: {what stays blocked} — For: {product owner | tech lead}

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
- Needs rework: address the items above, then resubmit
