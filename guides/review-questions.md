# Writing Review Questions for Humans

Load whenever writing or presenting **Decisions Requiring Your Validation** or **Open Questions** in any `*-review.md` (plan/proj, plan/epic, plan/epic-arch, plan/feat, plan/feat-arch, plan/redesign, plan/change, all `*-review` routes). Applies to every model — no house style beyond this file

## Who reads

- **PRD gate** → product owner: knows users and business, not code
- **Architecture gate** → tech lead / architect: knows technology, not your draft, not this codebase's internals
- Neither has read the code, the critic exchange, or draft history. Each item must be answerable in **under two minutes**, **without opening another document**, and **without asking "what does that mean?" or "why do I care?"**

## Ask only real decisions

Ask only when all three hold — otherwise decide yourself and write the choice into the document:

1. At least two reasonable options exist
2. The choice changes what users get, cost, delay, risk, or how hard it is to change later
3. Approved documents (Product Spirit, `docs/product.md`, parent PRD/architecture, earlier review answers) do not already settle it

Never: re-confirm what the user already said · items "for information" or "nothing needed from you" · two decisions in one item · questions about the document's own wording or format

## Item format — mandatory

```markdown
### D{n} — {the choice, in plain words}            ← heading level as in the review template

**Situation**: {1–2 sentences: which user, business process, or moment this touches — start from the user, not the technology}
**Options**: A — {plain words} · B — {plain words}            ← omit for a pure yes/no
**Impact**:
- **If yes** (or **If A**): {concrete consequence — what users see or can do, effort, cost, risk, data kept}
- **If no** (or **If B**): {same, just as concrete}
**Recommendation**: {option + one-sentence reason} · {Easy to change later | Hard to change later — why}
**Technical detail**: {names, tables, libraries — one line, architecture gate only, optional}

**Confirm?** {one explicit question, answerable by yes/no or by picking A/B}
> **Your answer**:
```

The bold **Confirm?** line is the question the human answers — a full question, never a bare "Confirm?"

## Language rules

- Plain everyday words, complete sentences
- Each technical term replaced ("background job", not "Celery task"; "kept for good", not "persisted") or explained in brackets at first use
- Code identifiers (file paths, table/class/function names, `snake_case`, endpoints) never in Situation, Impact, or **Confirm?** — only in Technical detail
- Architecture gate may use terms a tech lead knows (cache, queue, index, transaction) but still states the user or business impact
- Quantify when known (users, records, seconds, euros, days of work); never invent numbers — unknown figure → open question
- Neutral: state the recommendation, never hide the alternative's strengths

## Self-check — every item, before writing it down

1. Could the reader answer without a follow-up question?
2. Does each answer's consequence say what changes for users or the business?
3. Is the **Confirm?** line a real question with an obvious answer form?

Any "no" → rewrite. Cannot make it plain → probably not this reader's decision: decide yourself, or move it to the other gate

## Examples (fictional product — never copy into a real review)

### Bad — never write these

1. `Use soft-delete with deleted_at + partial unique index on (owner_id, name)? **Confirm?**` — jargon only, no situation, reader cannot tell why it matters
2. `Celery chord or APScheduler fan-out for the nightly refresh?` — tool names, no business stake, no impact per answer
3. `Confirm F2 follows the pattern of section 4.3.` — needs another document; not a choice
4. `Validate the error-handling strategy.` — no options, no question

### Good — PRD gate, yes/no

```markdown
### D1 — Can a deleted garden plan be recovered?

**Situation**: Gardeners sometimes delete a plan by mistake — often one they spent an evening drawing.
**Impact**:
- **If yes**: deleted plans stay 30 days in a "Recently deleted" area, then disappear for good. Mistakes can be undone. The privacy notice must mention the 30-day retention. About one extra day of work.
- **If no**: deletion is immediate and final. Simpler to build, but one wrong click loses the user's work for good.
**Recommendation**: Yes — losing an evening of work is the kind of frustration that makes people leave · Easy to change later

**Confirm?** Should deleted plans stay recoverable for 30 days before being erased for good?
> **Your answer**:
```

### Good — Architecture gate, A/B

```markdown
### D2 — How the nightly weather update runs

**Situation**: Every night the app fetches the forecast for about 4,000 gardens so watering reminders are ready at 7 am. The weather service sometimes answers slowly or fails for some gardens.
**Options**: A — one job processes all gardens one after another · B — the work is split into small batches that run in parallel and are retried separately
**Impact**:
- **If A**: simplest to build and to read; a slow weather service can push every reminder past 7 am, and one failure stops all remaining gardens.
- **If B**: reminders ready in about 10 minutes even when some batches fail, and failed batches retry alone. Uses the job queue the app already runs for e-mails; the admin dashboard needs one more line to show failed batches.
**Recommendation**: B — a reminder arriving after people left for work is useless · Hard to change later once other jobs copy the pattern
**Technical detail**: batches of 200 gardens on the existing `jobs` queue, 3 retries with back-off

**Confirm?** Should the nightly update run as one sequential job (A) or as parallel retried batches (B)?
> **Your answer**:
```

## Open questions

Same language rules. One line each, blocking first:

`- [blocking|important|minor] {plain question} — Why it matters: {what stays undecided or blocked} — For: {product owner | tech lead}`
