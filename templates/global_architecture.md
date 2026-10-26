# {Product name} — Global Architecture

<!-- docs/global_architecture.md — system-wide architecture, inspired by arc42 (structure) and C4 (diagrams: context, then containers)
     Readers: tech lead, architect, and every plan/*-arch route. Epic architectures reference this file instead of repeating it
     Scope: decisions that hold for the whole system. Versions and libraries → docs/technical-stack.md · full schema → docs/data-model.md ·
     screens → docs/ui-map.md. Link, never copy (one fact, one file)
     Delete sections that do not apply — never "N/A". Examples in comments use a fictional app ("GreenPlot",
     community-garden plot sharing); never copy them -->

> **Owner**: {name, role}
>
> **Last updated**: {date}
>
> **Product vision**: see [product.md](./product.md) · **Stack**: see [technical-stack.md](./technical-stack.md)

## 1. Quality Goals

{The 3–5 qualities that drive the design, ranked. Each: one sentence on why it matters to users or the business.}

| Rank | Quality | Why it matters |
| ---- | ------- | -------------- |
| 1 | {e.g. reliability of scheduled reminders} | {consequence for users if it fails} |

<!-- e.g. 1 Reliability — a watering reminder that arrives late kills plants and trust · 2 Simplicity of operation —
     run by one volunteer · 3 Mobile usability on poor network — used in the garden -->

## 2. Constraints

| Constraint | Source | Consequence for the design |
| ---------- | ------ | -------------------------- |
| {e.g. open-source licences only} | {budget / policy / law / team} | {what it rules out or forces} |

## 3. System Context

{Who and what the system talks to. One diagram (C4 level 1) and one table of external interfaces.}

```mermaid
flowchart LR
  user([{User role}]) --> system[{Product}]
  system --> ext[({External system})]
```

| External actor or system | Direction | Data exchanged | Protocol | If it is down |
| ------------------------ | --------- | -------------- | -------- | ------------- |
| {name} | in / out | {what} | {HTTPS/REST, SMTP, …} | {degraded behavior} |

<!-- e.g. | Weather service | out | 3-day forecast per garden | HTTPS/JSON, nightly | reminders fall back to "check soil" text |
          | Identity provider | in/out | login, roles | OIDC | nobody can log in — accepted risk, provider SLA 99.9% | -->

## 4. Solution Strategy

{5–8 bullets: architectural style and the key approaches, each tied to a quality goal from §1.}

<!-- e.g. Modular monolith (one deployable, modules per domain) → simplicity of operation ·
     All scheduled work in background jobs with retries → reliability · Offline-tolerant web app → mobile usability -->

## 5. Building Blocks

{Deployable units and their responsibilities (C4 level 2). Owning data = only this block writes it.}

```mermaid
flowchart LR
  web[{Web app}] --> api[{API}]
  api --> db[({Database})]
  worker[{Background worker}] --> db
```

| Block | Responsibility | Technology (detail in technical-stack.md) | Owns data |
| ----- | -------------- | ----------------------------------------- | --------- |
| {name} | {one sentence} | {short} | {entities} |

### Code organization

{Layering or module rules every epic must follow — dependency direction, where business logic lives, what may call what.}

## 6. Key Runtime Flows

{The 2–4 end-to-end flows the product depends on, each told start to finish: trigger → processing → stored data → what the user receives. Sequence diagrams welcome. Epic architectures extend these flows; they never contradict them.}

<!-- e.g. Flow "Nightly reminders": 02:00 scheduler enqueues one job per 200 gardens → worker fetches forecast →
     computes watering need per plot → stores reminder rows → 06:30 notification job sends push/e-mail →
     gardener opens app at 7:00 and sees "Water tomatoes today (no rain until Thursday)" -->

## 7. Data Overview

{Main entities, which block owns each, and lifecycle rules (retention, deletion, history). Full schema: docs/data-model.md.}

## 8. Deployment

{Environments, topology, how a release reaches production, backups and restore.}

## 9. Cross-Cutting Concepts

<!-- One short paragraph each; keep only those that apply -->

- **Security**: {authentication, authorization model, secrets, trust boundaries}
- **Privacy**: {personal data kept, retention, user rights}
- **Error handling**: {how failures surface to users and operators}
- **Observability**: {logs, metrics, alerts — who gets woken up}
- **Performance and scale**: {expected volumes, limits}
- **Accessibility and responsiveness**: {standard targeted, devices}
- **Internationalization**: {languages, time zones, currencies}
- **Testing**: {test levels and what each guarantees}

## 10. Key Technical Choices

{Choices that shape the whole system — each with rationale and the strongest rejected alternative. Part of this document, not a log: update a line when a choice changes.}

| Choice | Why | Rejected alternative and why |
| ------ | --- | ---------------------------- |
| {choice} | {reason, tied to §1 or §2} | {alternative — reason} |

<!-- e.g. | Background jobs through a queue | retries per batch keep reminders on time | cron script — one failure stops everything | -->

## 11. Quality Scenarios

{Measurable form of §1: situation → expected response → measure.}

| Quality | Scenario | Measure |
| ------- | -------- | ------- |
| {quality} | {stimulus and context} | {threshold} |

<!-- e.g. | Reliability | weather service fails for 10% of gardens at night | 100% of reminders sent by 07:00, fallback text for affected gardens | -->

## 12. Risks and Technical Debt

| Risk or debt | Impact | Mitigation or acceptance |
| ------------ | ------ | ------------------------ |
| {item} | {consequence} | {plan, or "accepted because …"} |

## 13. Glossary

{Technical terms used in this document; business terms → product.md glossary.}
