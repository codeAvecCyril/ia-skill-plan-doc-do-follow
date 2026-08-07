# Epic Architecture — {epic-name}

> **Code**: E{n}
>
> **Slug**: e{n}-{epic-name}
>
> **Last Updated**: {date}

<!-- If same as docs/global_architecture.md, ONE sentence ref — never restate
     Delete unused sections — never "N/A" -->
## System Overview

{Diagram or description of components this epic adds or touches}

## Component Breakdown

1. **{Component}**: {purpose, responsibilities, interactions}

## Data Model Delta

<!-- docs/data-model.md = global truth — update it in same change
     Here: only what this epic adds or changes, plus link -->

- {new/changed entity}: {fields, relations} → recorded in `docs/data-model.md#{anchor}`

## API Specifications

### {METHOD} /api/{path}

- **Purpose**: {what it does}
- **Request / Response**: {schema or example}
- **Auth**: {requirement}

## Navigation Impact (UI epics)

{New sections/screens in global nav → recorded in `docs/ui-map.md`}

## Technology Decisions

Reference: `docs/technical-stack.md`. List only decisions **specific to this epic**, each with one-sentence rationale

## Integration Points

- **Integrates with**: {epics/systems} · format {…} · frequency {…} · failure impact {…}

## Performance & Scalability

{Only epic-specific targets and strategies; else reference global architecture}

## Security & Compliance

{Only epic-specific: new auth flows, sensitive data, compliance obligations}

## Deployment, Monitoring & Operations

{Only what differs from project standard approach}

## Known Constraints & Trade-offs

- {constraint or trade-off}: {impact, why chosen}

## Risks

| Risk | Likelihood | Impact | Mitigation |
| ---- | ---------- | ------ | ---------- |
