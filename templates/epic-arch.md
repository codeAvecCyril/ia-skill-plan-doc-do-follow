# Epic Architecture — {epic-name}

> **Code**: E{n}
>
> **Slug**: e{n}-{epic-name}
>
> **Last Updated**: {date}

<!-- Where a topic does not differ from docs/global_architecture.md, write ONE sentence
     referencing it instead of restating it. Delete sections that do not apply — never "N/A". -->

## System Overview

{High-level diagram or description of the components this epic adds or touches.}

## Component Breakdown

1. **{Component}**: {purpose, responsibilities, interactions}

## Data Model Delta

<!-- docs/data-model.md is the global truth — update it in the same change.
     Here, describe only what this epic adds or changes, and link to it. -->

- {new/changed entity}: {fields, relations} → recorded in `docs/data-model.md#{anchor}`

## API Specifications

### {METHOD} /api/{path}

- **Purpose**: {what it does}
- **Request / Response**: {schema or example}
- **Auth**: {requirement}

## Navigation Impact (UI epics)

{New sections/screens added to the global navigation → recorded in `docs/ui-map.md`.}

## Technology Decisions

Reference: `docs/technical-stack.md`. List only decisions **specific to this epic**, each with a one-sentence rationale.

## Integration Points

- **Integrates with**: {epics/systems} · format {…} · frequency {…} · failure impact {…}

## Performance & Scalability

{Only epic-specific targets and strategies; otherwise reference the global architecture.}

## Security & Compliance

{Only epic-specific concerns: new auth flows, sensitive data, compliance obligations.}

## Deployment, Monitoring & Operations

{Only what differs from the project's standard approach.}

## Known Constraints & Trade-offs

- {constraint or trade-off}: {impact, why chosen}

## Risks

| Risk | Likelihood | Impact | Mitigation |
| ---- | ---------- | ------ | ---------- |
