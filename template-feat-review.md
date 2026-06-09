# Feature Review Checklist

> **Feature**: {feature-name} (F{n})
>
> **Epic**: {epic-name} (E{n})
>
> **Review Date**: {date}
>
> **Reviewed By**: {stakeholder names}
>
> **Status**: ⚪ Not Started | 🟡 In Review | 🟢 Approved | 🔴 Needs Changes

## Executive Summary

Brief overview of feature, acceptance criteria, and proposed implementation approach.

## Review Items

### Scope & Requirements

- [ ] User stories are clear and testable
- [ ] Acceptance criteria are specific and measurable
- [ ] Edge cases are documented
- [ ] Out-of-scope is clearly defined
- [ ] Requirements are complete
- [ ] No ambiguities remain

**Comments**:

### Remaining functionnal questions
- {remaining questions}

**Answers**:

### Technical Design (for arch review only)

- [ ] Architecture fits within epic design
- [ ] APIs are well-defined
- [ ] Data model is appropriate
- [ ] Technology choices are justified
- [ ] Performance considerations are addressed
- [ ] Security requirements are met

**Comments**:

### Implementation Approach (for arch review only)

- [ ] Tasks are appropriately sized
- [ ] Task breakdown is logical
- [ ] Dependencies are minimal and clear
- [ ] Parallelization opportunities are identified
- [ ] Estimation is realistic
- [ ] Team has required skills

**Comments**:

### Testing & Quality

- [ ] Test strategy is defined
- [ ] Unit test approach is clear
- [ ] Integration test approach is clear
- [ ] E2E test scenarios are identified
- [ ] Edge cases are covered
- [ ] Performance testing is planned

**Comments**:

### Integration & Accessibility (for arch review only)

- [ ] Integration points are clear
- [ ] No breaking changes
- [ ] Backward compatibility is maintained
- [ ] Accessibility requirements are addressed
- [ ] Localization needs are considered

**Comments**:

### Risks & Blockers

- [ ] Risks are identified
- [ ] Mitigation strategies exist
- [ ] External dependencies are documented
- [ ] No critical blockers
- [ ] Contingency plans are in place

**Comments**:

### Remaining architecture and technical questions
- {remaining questions}

**Answers**:

## Sign-Off

| Role            | Name   | Date   | Status  |
| --------------- | ------ | ------ | ------- |
| Product Manager | {name} | {date} | ⚪ ⚡ 🟢 🔴 |
| Technical Lead  | {name} | {date} | ⚪ ⚡ 🟢 🔴 |

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

If PRD approved:
- [ ] Create feature architecture: `@plan/feat-arch E{n} F{n}`

If architecture approved:
- [ ] Break down into tasks: `@plan/tasks E{n} F{n}`
- [ ] Start implementation

If needs rework:
- [ ] Address feedback items
- [ ] Update feature PRD
- [ ] Schedule follow-up review
- [ ] Resubmit for approval

**Approval Status**: {Pending Approval / Approved / Needs Rework}
