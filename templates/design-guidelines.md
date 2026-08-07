# Design Guidelines

> **Last Updated**: {date}

<!-- LIVING DOC — UI style contract; ui-consistency-reviewer checks against it at
     do/verify. If design system exists, this file = SHORT pointer to it plus
     project-specific rules — never a duplicate -->

## Design System Reference

{Link to existing design system / component library docs, if any}

## Tokens & Foundations

- **Colors**: {palette or token source; light/dark policy}
- **Typography**: {font, size scale}
- **Spacing**: {scale}
- **Elevation/Radius**: {rules}

## Component Conventions

- **Buttons**: {primary/secondary usage, placement}
- **Forms**: {validation display, label style}
- **Tables/Lists**: {which component, pagination, row actions}
- **Feedback**: {toasts vs dialogs vs inline; confirmation policy}

## Standard States

Every screen implements: empty state · loading state · error state — styled per {reference}

## Terminology

| Concept | Always call it | Never |
| ------- | -------------- | ----- |
| {…}     | {term}         | {synonyms to avoid} |

## Accessibility Baseline

- Keyboard navigable, visible focus states, contrast ≥ 4.5:1, touch targets ≥ 44px
