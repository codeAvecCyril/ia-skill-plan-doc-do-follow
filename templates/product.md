# {Product name} — Product Vision

<!-- docs/product.md — project-level PRD. Human document: complete sentences, no unexplained abbreviations
     Read by plan/proj: §1–§4 distill the Product Spirit block · §6–§7 become epics · §5 + §9 frame every later review
     Describe problems and outcomes, not solutions: no tables, endpoints, or libraries here (→ docs/global_architecture.md)
     Delete sections that do not apply — never "N/A". Examples in comments use a fictional app ("GreenPlot",
     community-garden plot sharing); never copy them -->

> **Owner**: {name, role}
>
> **Status**: Draft | Validated
>
> **Last updated**: {date}
>
> **Architecture**: see [global_architecture.md](./global_architecture.md)

## 1. Vision

{One short paragraph: what the product is, for whom, and the change it brings to their life or work.}

<!-- e.g. "GreenPlot lets people without a garden grow their own vegetables on a shared plot near home.
     It matches gardeners with free plots, plans the season with them, and reminds them when to water,
     so that a first-time gardener harvests something in their first year." -->

## 2. Problem

**Who has the problem**: {user group}
**What hurts today**: {the pain, in their words}
**How they cope today**: {current workaround and why it falls short}
**Evidence**: {interviews, numbers, own experience — say which; "assumption" is an honest answer}

<!-- e.g. Who: city dwellers who want to grow food but have no garden.
     Pain: shared plots exist, but finding one means calling the town hall; half of new gardeners give up
     in the first summer because they water at the wrong time or plant too late.
     Coping: paper waiting lists, gardening forums, a group chat per garden. Evidence: 12 interviews in two gardens -->

## 3. Users and Stakeholders

| Who | What they need from the product | What they are responsible for |
| --- | ------------------------------- | ----------------------------- |
| {primary user} | {need} | {responsibility} |

<!-- e.g. | Gardener | find a plot, know what to do this week | tending their plot |
          | Garden coordinator | fill plots fairly, see who is inactive | rules of the garden |
          | Administrator | keep the service running | data, accounts, support | -->

## 4. Value Proposition and Positioning

**Jobs to be done**: {"When …, I want to …, so that …" — 2 to 4 jobs}
**Why us**: {what this product does that the alternatives do not}
**What this product is not**: {deliberate exclusions that protect its identity — the most important lines for the Product Spirit}

<!-- e.g. Job: "When I start my first season, I want a week-by-week plan for my plot, so that I do not miss
     planting dates." Not: a marketplace for selling produce · a social network · a tool for professional farms -->

## 5. Goals and Success Metrics

| Goal (outcome, not feature) | Metric | Target | Guardrail (must not get worse) |
| --------------------------- | ------ | ------ | ------------------------------ |
| {goal} | {how measured} | {value + date} | {counter-metric} |

<!-- e.g. | First-year gardeners keep going | share of new gardeners still active in September | 70% by end of season 1 | coordinator time spent per gardener |
     Prefer 2–4 goals. A goal nobody can measure becomes an open question (§10) -->

## 6. Product Principles

{3–5 tie-breakers the team uses when two good options conflict — each one sentence.}

<!-- e.g. "A beginner must succeed without reading help." · "Reminders are rare and always actionable." ·
     "Coordinators decide; the product only suggests." -->

## 7. Capabilities

<!-- What users can do, grouped by theme, as user stories. Priority: Must (first release cannot ship without it),
     Should, Could. plan/proj turns themes into epics — keep each theme one coherent outcome -->

### 7.1 {Theme}

- **{Must|Should|Could}** — As a {user}, I want to {action}, so that {benefit}.

<!-- e.g. ### 7.2 Season planning
     - Must — As a gardener, I want a weekly to-do list for my plot, so that I know what to do this weekend.
     - Should — As a gardener, I want to be reminded to water when no rain is forecast, so that my plants survive heatwaves. -->

## 8. Key User Journeys

{The 2–4 journeys that matter most, each told start to finish as numbered steps: who starts it, what they see, what the system does, what they get at the end. A diagram is welcome.}

<!-- e.g. Journey "First harvest": 1. Lena signs up and gives her neighborhood · 2. She sees three free plots
     nearby and requests one · 3. The coordinator approves; Lena gets the plot code · 4. She picks tomatoes and
     beans; the app builds a week-by-week plan · 5. Each Friday she gets the weekend to-do; on dry weeks a
     watering reminder · 6. In August she records her first harvest -->

## 9. Constraints

{Business, legal, budget, platform, and organizational limits the solution must respect — one line each with the reason.}

<!-- e.g. Free for gardeners; hosting under 50 €/month · personal data stays in the EU (GDPR) ·
     works on a five-year-old phone with poor network in the garden -->

## 10. Risks, Assumptions, and Open Questions

| Type | Statement | How we will find out |
| ---- | --------- | -------------------- |
| {Value / Usability / Feasibility / Viability risk, or Assumption, or Question} | {statement} | {test, interview, prototype, decision owner} |

<!-- Value = will they want it · Usability = can they use it · Feasibility = can we build it · Viability = does it
     work for the business/organization. e.g. | Assumption | Coordinators will approve requests within 48 hours | pilot in two gardens | -->

## 11. Release Horizons

| Horizon | Outcome delivered | Main capabilities |
| ------- | ----------------- | ----------------- |
| Now | {what users can do at the end} | {themes from §7} |
| Next | {…} | {…} |
| Later | {…} | {…} |

<!-- Outcomes, not dates. Detailed sequencing lives in docs/project-status.md once plan/proj has run -->

## 12. Glossary

| Term | Meaning |
| ---- | ------- |
| {domain word} | {plain definition; translation if the team works in two languages} |
