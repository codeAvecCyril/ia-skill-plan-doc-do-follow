# Epic Review Checklist

> **Epic**: {epic-name} (E{n})
>
> **Review Date**: {date}
>
> **Reviewed By**: {stakeholder names}
>
> **Status**: ⚪ Not Started | 🟡 In Review | 🟢 Approved | 🔴 Needs Changes

## Executive Summary

Brief overview of epic, features, and proposed timeline.

## Review Items

### Scope & Features

- [ ] Feature list is complete for epic scope
- [ ] Feature scopes are appropriately sized (3-5 days of work each)
- [ ] Features are prioritized correctly
- [ ] Dependencies between features are clear
- [ ] No critical requirements are missing
- [ ] Scope is achievable within timeline

**Comments**:

### Requirements & Success Criteria

- [ ] User stories are clear and testable
- [ ] Acceptance criteria are specific and measurable
- [ ] Edge cases are documented
- [ ] Non-functional requirements are explicit
- [ ] Success metrics are defined
- [ ] Definition of done is clear

**Comments**:

### Architecture & Technical Design

- [ ] Architecture aligns with system design
- [ ] APIs and data models are appropriate
- [ ] Integration points are clear
- [ ] Technology choices are justified
- [ ] Performance targets are realistic
- [ ] Security requirements are addressed

**Comments**:

### Resources & Timeline

- [ ] Team skillset matches requirements
- [ ] Capacity aligns with timeline
- [ ] Estimate is realistic
- [ ] Parallel work is identified
- [ ] Blockers are understood
- [ ] Dependencies on other teams are minimal

**Comments**:

### Quality & Testing

- [ ] Test strategy is defined
- [ ] Unit/integration/e2e coverage is planned
- [ ] Test scenarios cover edge cases
- [ ] Performance testing is planned
- [ ] Security testing is planned

**Comments**:

### Risks & Dependencies

- [ ] Risks are identified and mitigated
- [ ] External dependencies are documented
- [ ] Team dependencies are minimized
- [ ] Critical path is clear
- [ ] Rollback/contingency plan exists

**Comments**:

## Sign-Off

| Role            | Name   | Date   | Status  |
| --------------- | ------ | ------ | ------- |
| Product Manager | {name} | {date} | ⚪ ⚡ 🟢 🔴 |
| Technical Lead  | {name} | {date} | ⚪ ⚡ 🟢 🔴 |
| Architect       | {name} | {date} | ⚪ ⚡ 🟢 🔴 |

Legend: ⚪ Pending, ⚡ In Review, 🟢 Approved, 🔴 Needs Changes

## Action Items

| Item     | Owner   | Due Date |
| -------- | ------- | -------- |
| {action} | {owner} | {date}   |

## Feedback Summary

### What's Working Well

- {positive feedback item}

### Needs Improvement

- {improvement item}

## Next Steps

If approved:
- [ ] Create full feature PRDs: `@plan/feat E{n} F{n}` for each feature
- [ ] Schedule feature review meetings
- [ ] Kick off first feature

If needs rework:
- [ ] Address feedback items
- [ ] Schedule follow-up review
- [ ] Resubmit for approval

**Approval Status**: {Pending Approval / Approved / Needs Rework}
