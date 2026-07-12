# Feature PRD — {feature-name}

> **Code**: E{n} F{n}
>
> **Slug**: e{n}-{epic-name}/f{n}-{feat-name}
>
> **Priority**: P{0|1|2}

<!-- Writing rules: complete sentences a stakeholder can validate in isolation;
     no unexplained abbreviations. Delete sections that do not apply — never "N/A". -->

## Feature Narrative

As a {user role}, I want to {capability} so that {business value}.

{1–2 paragraph overview.}

## User Stories

- **US-1**: As a {role}, I want to {action} so that {benefit}.
  - Given {precondition}, when {action}, then {outcome}.

## Acceptance Criteria

- [ ] {complete, verifiable sentence}
- [ ] {complete, verifiable sentence}

## Edge Cases & Error Handling

- {Scenario} → {expected behavior, as a complete sentence}.

## Entry Points & Navigation (mandatory for UI features)

<!-- If this cannot be filled, it is a BLOCKING question for the user.
     Register the entry point in docs/ui-map.md in the same change. -->

- **Menu placement**: {where in the global navigation the feature appears}
- **Route/URL**: {path}
- **Breadcrumb**: {trail}
- **Discovery**: {how a first-time user finds this feature}

## UI Requirements

{Screens, states (empty/loading/error), and interactions. Follow `docs/design-guidelines.md`.}

## Architecture Delta (mandatory)

<!-- Only what this feature ADDS or CHANGES relative to epic-arch.md.
     If nothing: "None — fully covered by the epic architecture." -->

- **New/changed endpoints**: {…}
- **New/changed data** (sync to `docs/data-model.md`): {…}
- **New components/modules**: {…}
- **feat-arch needed?** {No | Yes — trigger criterion {n} from routes/plan-feat-arch.md}

## Data Requirements

## Non-Functional Requirements

- **Performance**: {only actual, feature-specific requirements}
- **Security**: {authentication, authorization, data protection — if beyond project defaults}
- **Accessibility**: {if beyond project defaults}

## Dependencies

- Depends on: {feature/epic/external — one sentence each}
- Blocks: {…}

## Out of Scope

- {explicitly excluded item, as a complete sentence}

## Test Strategy

{Unit / integration / end-to-end approach and the edge cases to cover.}

## Open Questions

- [{blocking|important|minor}] {question, as a complete sentence}
