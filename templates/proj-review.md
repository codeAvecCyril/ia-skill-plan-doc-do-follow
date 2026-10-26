# Project Review — {project-name}

> **Review Date**: {date}
>
> **Reviewed By**: {stakeholder names}
>
> **Status**: ⚪ Not Started | 🟡 In Review | 🟢 Approved | 🔴 Needs Changes

## Executive Summary

{3–5 complete sentences: what is being built, the proposed epics, the proposed sequencing, and the main risk.}

## Automated Checks (verified by the AI)

> ✅ {n}/{total} structural checks passed — {one line listing any failures}

<details><summary>Details</summary>

- [ ] Every epic has a brief with a clear business value statement
- [ ] Epic dependency graph is valid (no cycles, no orphan references)
- [ ] Epics are sized consistently and cover the whole product vision with no overlap
- [ ] The technical stack supports every proposed epic
- [ ] The Product Spirit block is present and consistent with `docs/product.md`

</details>

## Decisions Requiring Your Validation

<!-- Write every item per guides/review-questions.md (load it) — mandatory format below
     Only real decisions · plain words · impact of each answer · bold **Confirm?** = full question
     Answer applied into reviewed doc; question + answer stay here verbatim — never rewritten, never re-asked
     Max 10 items: epic scope and sizing, sequencing, timeline realism -->

### D1 — {the choice, in plain words}

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

| Role            | Name   | Date   | Status  |
| --------------- | ------ | ------ | ------- |
| Product Manager | {name} | {date} | ⚪ ⚡ 🟢 🔴 |
| Technical Lead  | {name} | {date} | ⚪ ⚡ 🟢 🔴 |

Legend: ⚪ Pending, ⚡ In Review, 🟢 Approved, 🔴 Needs Changes

## Action Items

| Item     | Owner   | Due Date |
| -------- | ------- | -------- |

## Next Steps

- If approved: `@plan/epic E{n}` for the highest-priority epic
- If needs rework: address the items above, then resubmit
