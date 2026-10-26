# {Product name} — Technical Stack

<!-- docs/technical-stack.md — exact technologies, versions, commands, and conventions. Read by every plan/*-arch route,
     plan/tasks (validation commands, file layout), and executors through task packets
     Scope: WHAT is used and HOW to build, run, test, and extend it. WHY the system is shaped this way → docs/global_architecture.md
     (link, never copy). Commands must be runnable as written — plan/tasks copies them into tasks
     Delete sections that do not apply — never "N/A". Examples in comments use a fictional app ("GreenPlot",
     community-garden plot sharing); never copy them -->

> **Owner**: {name, role}
>
> **Last updated**: {date}
>
> **Architecture**: see [global_architecture.md](./global_architecture.md)

## 1. Stack Overview

| Layer | Technology | Version | Licence | Role in one line |
| ----- | ---------- | ------- | ------- | ---------------- |
| {layer} | {technology} | {pinned major.minor} | {licence} | {what it does here} |

<!-- e.g. | API | NestJS (Node 22) | 11.x | MIT | REST API, validation, auth guards |
          | Jobs | BullMQ + Redis | 5.x / 7.2 | MIT / BSD | nightly forecast batches, reminder sending |
          | Database | PostgreSQL | 16 | PostgreSQL | all persistent data |
          | Web | React + Vite | 19 / 6 | MIT | mobile-first web app | -->

## 2. Dependency Rules

{Rules a new library must pass before it is added — licence, maintenance activity, size, overlap with what exists.}

<!-- e.g. Permissive licence only (MIT, Apache-2.0, BSD) · release in the last 12 months · no second library for a job an
     existing one already does (one date library, one HTTP client) · tech lead approves any new runtime dependency -->

## 3. Layers in Detail

<!-- One subsection per layer that has choices worth knowing: key libraries and what each is used for,
     configuration conventions, known pitfalls. Keep tables short; link docs/patterns/* for recurring solutions -->

### 3.1 {Layer}

| Library | Used for | Note |
| ------- | -------- | ---- |
| {library} | {purpose} | {pitfall or convention} |

## 4. Project Layout

```
{repository tree, two or three levels: where each layer's code, tests, migrations, and config live}
```

{Placement rules: where a new endpoint, entity, job, screen, or test goes.}

## 5. Dependency Management

| Ecosystem | Tool | Lock file | Add a dependency | Install |
| --------- | ---- | --------- | ---------------- | ------- |
| {language} | {tool} | {file} | `{command}` | `{command}` |

## 6. Build and Run

| Goal | Command | Result |
| ---- | ------- | ------ |
| Local development | `{command}` | {URL or process started} |
| Production-like run | `{command}` | {…} |
| Database migration | `{command}` | {…} |
| Seed / sample data | `{command}` | {…} |

{Required environment variables: prefix, example file to copy, which ones are secrets.}

## 7. Testing

| Level | Tool | Location | Command | What it guarantees |
| ----- | ---- | -------- | ------- | ------------------ |
| Unit | {tool} | {path} | `{command}` | {…} |
| Integration | {tool} | {path} | `{command}` | {…} |
| End-to-end | {tool} | {path} | `{command}` | {…} |

{Coverage target, test data rules (isolation, cleanup), how to run one file or one test, slow suites to avoid running in parallel.}

## 8. Coding Conventions

<!-- Per language: typing rules, naming, error handling, async rules, forbidden patterns. One line each.
     Recurring solutions → docs/patterns/{name}.md, linked here -->

- **{Language}**: {convention}

## 9. Code Quality and CI

| Check | Tool | Command | Blocks merge |
| ----- | ---- | ------- | ------------ |
| Format | {tool} | `{command}` | yes / no |
| Lint | {tool} | `{command}` | yes / no |
| Type check | {tool} | `{command}` | yes / no |
| Tests | {tool} | `{command}` | yes / no |

{Order that matters (e.g. format before lint), pre-push command, what CI runs on a pull request.}

## 10. Upgrade Policy

{How and when versions move: who bumps, cadence, how a major upgrade is planned, supported runtime versions.}
