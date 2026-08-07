# Feature Architecture — {feature-name}

> **Code**: E{n} F{n}
>
> **Slug**: e{n}-{epic-name}/f{n}-{feat-name}
>
> **Trigger**: {which criterion from routes/plan-feat-arch.md justified this document}
>
> **Last Updated**: {date}

<!-- Exists only for exception cases (see routes/plan-feat-arch.md)
     Describe ONLY delta vs epic-arch.md; reference it for everything else
     Delete unused sections — never "N/A" -->

## Design Delta

{Diagram or description of what this feature adds or changes within epic architecture}

## New Components & Modules

1. **{Module}**: {purpose, responsibilities, interactions}

## Data Model Delta

<!-- docs/data-model.md = global truth — update it in same change -->

- {new/changed entity or field}: {description} → recorded in `docs/data-model.md#{anchor}`

## API / Interface Delta

### {METHOD} /api/{path} (or function signature)

- **Purpose** · **Request/Parameters** · **Response/Returns** · **Errors**

## Technology Decisions

{Only decisions specific to this feature, each with one-sentence rationale; else reference `docs/technical-stack.md`}

## Security Considerations

{Only if feature opens new security surface: input validation, authorization, data protection}

## Error Handling & Observability

{Key error scenarios, what to log, what to monitor — only where feature-specific}

## Testing Strategy

{Approach for delta: unit / integration / end-to-end coverage needed}

## Known Constraints & Trade-offs

- {constraint}: {impact, why accepted}
