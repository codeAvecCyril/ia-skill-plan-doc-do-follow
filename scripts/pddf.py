#!/usr/bin/env python3
"""pddf — deterministic helpers for the plan-doc-do-follow skill.

Agents call these instead of re-deriving tables or re-reading whole documents:
outputs are short, files are edited in place, exit code 1 means drift or issues.
Stdlib only, Python >= 3.9. Run from the repository root (or pass --docs).

  sync [--check] [--reopen E1F2]   Status Sync: recompute feature/epic/project statuses
  task E1 F2 T3 🟢 [--wave 2/4] [--eta 40m]   set one Task Summary row (+ Execution line)
  waves E1 F2                    pending execution waves, progress, dependency problems
  packet E1 F2 T3|L1             print one task packet, or one lane packet (its pending tasks in order)
  beat E1 F2 [T3 MESSAGE...]     coder: append a progress beat · no task: last beat per task, with age
  lint-tasks E1 F2 [--strict]    mechanical checks on feat-tasks.md (+ Story Trace coverage)
  section FILE HEADING [--replace]   print one Markdown section, or replace it from stdin
  toc FILE                       headings with line numbers
  review-open FILE               unanswered **Confirm?** items in a review file
  find E1 [F2]                   resolve epic/feature directories and list their docs
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

STATUSES = "⚪🟡🟣🔵🟢"
RANK = {s: i for i, s in enumerate(STATUSES)}
WORDS = {"⚪": "TODO", "🟡": "SPEC", "🟣": "PLAN", "🔵": "DEV", "🟢": "DONE"}
WORD_TO_STATUS = {w.lower(): s for s, w in WORDS.items()}
WORD_RE = re.compile(r"\b(TODO|SPEC|PLAN|DEV|DONE)\b")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
EXECUTION_RE = re.compile(r"^\*\*Execution\*\*:.*$", re.M)
TASK = r"T\d+[a-z]?"  # T5a / T5b allowed (split tasks)
LANE = r"L\d+"  # dispatch unit: sequential chain of tasks run by one coder
LANE_MAX = 4
FRACTION_RE = re.compile(r"(\d+)\s*/\s*(\d+)")


def task_key(code: str) -> tuple[int, str]:
    m = re.match(r"T(\d+)([a-z]?)", code)
    return (int(m.group(1)), m.group(2)) if m else (10**9, code)


def same_fraction(old: str, new: str) -> bool:
    """'100% (3/3 features)' and '3/3' state the same progress."""
    a, b = FRACTION_RE.search(old), FRACTION_RE.search(new)
    if a and b:
        return a.groups() == b.groups()
    return (old.split() or [""])[0] == new.strip()
INSTRUCTION_FILES = ("CLAUDE.md", "AGENTS.md", ".github/copilot-instructions.md")


class PddfError(Exception):
    pass


# ---------- Markdown primitives ----------


def split_row(line: str) -> list[str]:
    """Split a table row on unescaped pipes outside backticks; keeps raw cell text."""
    cells, buf, in_code, prev = [], [], False, ""
    for ch in line:
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code and prev != "\\":
            cells.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
        prev = ch
    cells.append("".join(buf))
    return cells  # cells[0] / cells[-1] are the text outside the outer pipes


def set_cell(line: str, col: int, value: str) -> str:
    parts = split_row(line)
    old = parts[col + 1]
    new = f" {value} "
    parts[col + 1] = new.ljust(len(old)) if len(new) <= len(old) else new
    return "|".join(parts)


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """(line index, level, title) for headings outside code fences."""
    out, fence = [], False
    for i, line in enumerate(lines):
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
            continue
        m = None if fence else HEADING_RE.match(line)
        if m:
            out.append((i, len(m.group(1)), m.group(2)))
    return out


def section_bounds(lines: list[str], title: str) -> tuple[int, int]:
    """Section = heading line up to next heading of same or higher level."""
    want = title.lstrip("#").strip().lower()
    hs = headings(lines)
    for n, (i, level, text) in enumerate(hs):
        if text.lower() == want or text.lower().startswith(want):
            end = next((j for j, lv, _ in hs[n + 1 :] if lv <= level), len(lines))
            return i, end
    raise PddfError(f"heading not found: {title}")


class Table:
    """First Markdown table inside a section, located by heading."""

    def __init__(self, lines: list[str], *headings_: str, needs: tuple[str, ...] = ()):
        for heading in headings_:
            try:
                start, end = section_bounds(lines, heading)
                break
            except PddfError:
                continue
        else:
            # legacy docs: first table whose header holds every needed column
            start = next(
                (i - 1 for i, ln in enumerate(lines) if ln.lstrip().startswith("|") and needs
                 and all(any(k in c.lower() for c in split_row(ln)[1:-1]) for k in needs)),
                None,
            )
            if start is None:
                raise PddfError(f"heading not found: {' / '.join(headings_)}")
            end = len(lines)
        i = start + 1
        while i < end and not lines[i].lstrip().startswith("|"):
            i += 1
        if i >= end - 1:
            raise PddfError(f"no table under heading: {heading}")
        self.header = [c.strip().lower() for c in split_row(lines[i])[1:-1]]
        self.rows: list[int] = []
        j = i + 2  # skip separator
        while j < end and lines[j].lstrip().startswith("|"):
            self.rows.append(j)
            j += 1
        self.lines = lines

    def col(self, *keys: str, required: bool = True) -> int | None:
        for key in keys:
            for n, name in enumerate(self.header):
                if key in name:
                    return n
        if required:
            raise PddfError(f"no column {keys} in table header {self.header}")
        return None

    def cell(self, row: int, col: int) -> str:
        return split_row(self.lines[row])[col + 1].strip()

    def set(self, row: int, col: int, value: str) -> None:
        self.lines[row] = set_cell(self.lines[row], col, value)


def status_of(cell: str) -> str | None:
    for ch in cell:
        if ch in RANK:
            return ch
    m = WORD_RE.search(cell)
    return WORD_TO_STATUS[m.group(1).lower()] if m else None


def with_status(cell: str, status: str) -> str:
    old = status_of(cell)
    if old is None or old not in cell:
        return status
    out = cell.replace(old, status, 1)
    return WORD_RE.sub(WORDS[status], out, count=1)


def parse_status(text: str) -> str:
    if text in RANK:
        return text
    if text.lower() in WORD_TO_STATUS:
        return WORD_TO_STATUS[text.lower()]
    raise PddfError(f"unknown status {text!r} — use one of {STATUSES} or {list(WORDS.values())}")


def read(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").split("\n")


def write(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------- Locating documents ----------


def code_num(token: str, prefix: str) -> int:
    m = re.fullmatch(rf"{prefix}(\d+)", token.strip(), re.I)
    if not m:
        raise PddfError(f"expected {prefix.upper()}{{n}}, got {token!r}")
    return int(m.group(1))


def task_code(token: str) -> str:
    m = re.fullmatch(r"t(\d+)([a-z]?)", token.strip(), re.I)
    if not m:
        raise PddfError(f"expected T{{n}}, got {token!r}")
    return f"T{m.group(1)}{m.group(2).lower()}"


def child_dir(parent: Path, prefix: str, n: int) -> Path | None:
    hits = [p for p in parent.iterdir() if p.is_dir() and re.match(rf"{prefix}{n}(-|$)", p.name, re.I)]
    return sorted(hits)[0] if hits else None


def epic_dir(docs: Path, e: str) -> Path:
    found = child_dir(docs / "epics", "e", code_num(e, "e"))
    if not found:
        raise PddfError(f"no directory docs/epics/{e.lower()}-*")
    return found


def feat_dir(docs: Path, e: str, f: str) -> Path:
    edir = epic_dir(docs, e)
    found = child_dir(edir, "f", code_num(f, "f"))
    if not found:
        raise PddfError(f"no directory {edir}/{f.lower()}-*")
    return found


def tasks_file(docs: Path, e: str, f: str) -> Path:
    path = feat_dir(docs, e, f) / "feat-tasks.md"
    if not path.exists():
        raise PddfError(f"missing {path}")
    return path


# ---------- Task Summary ----------


class Task:
    def __init__(self, code: str, title: str, kind: str, deps: list[str], status: str | None, row: int,
                 lane: str | None = None):
        self.code, self.title, self.kind, self.deps, self.status, self.row = code, title, kind, deps, status, row
        self.lane = lane

    @property
    def is_test(self) -> bool:
        return bool(re.search(r"test", self.kind + " " + self.title, re.I))


def load_tasks(lines: list[str]) -> tuple[Table, dict[str, Task]]:
    table = Table(lines, "Task Summary", needs=("code", "status"))
    c_code, c_status = table.col("code", "id", "task"), table.col("status")
    c_title = table.col("task", "title", required=False)
    c_type = table.col("type", required=False)
    c_deps = table.col("depend", required=False)
    c_lane = table.col("lane", required=False)
    tasks: dict[str, Task] = {}
    for row in table.rows:
        m = re.search(rf"\b{TASK}\b", table.cell(row, c_code))
        if not m:
            continue
        deps = re.findall(rf"\b{TASK}\b", table.cell(row, c_deps)) if c_deps is not None else []
        lane = re.search(rf"\b{LANE}\b", table.cell(row, c_lane)) if c_lane is not None else None
        tasks[m.group(0)] = Task(
            m.group(0),
            table.cell(row, c_title) if c_title not in (None, c_code) else "",
            table.cell(row, c_type) if c_type is not None else "",
            deps,
            status_of(table.cell(row, c_status)),
            row,
            lane.group(0) if lane else None,
        )
    return table, tasks


def lanes_of(tasks: dict[str, Task]) -> dict[str, list[str]]:
    """Lane id → member codes in Task Summary order · task without lane = solo lane keyed by its own code."""
    out: dict[str, list[str]] = {}
    for code, task in tasks.items():
        out.setdefault(task.lane or code, []).append(code)
    return out


LAYERS = {"frontend": re.compile(r"front|ui\b|component", re.I), "backend": re.compile(r"back|api|database|db\b|worker", re.I)}


def lane_issues(tasks: dict[str, Task]) -> tuple[list[str], list[str]]:
    """(fails, warnings) for lane shape: sequential chain, size cap, independent Test tasks, one layer."""
    fails: list[str] = []
    warns: list[str] = []
    for lane, members in lanes_of(tasks).items():
        if len(members) < 2:
            continue
        for prev, cur in zip(members, members[1:]):
            if prev not in tasks[cur].deps:
                fails.append(f"{lane}: {cur} must depend on {prev} — lane = sequential chain, in Task Summary order")
        if len(members) > LANE_MAX:
            fails.append(f"{lane}: {len(members)} tasks > {LANE_MAX} — split the lane")
        for code in members:
            if tasks[code].is_test and (prod := [d for d in tasks[code].deps if d in members]):
                fails.append(f"{lane}: Test task {code} shares lane with its producer {', '.join(prod)} — tests need an independent coder")
        layers = {name for name, rx in LAYERS.items() for c in members if rx.search(tasks[c].kind)}
        if len(layers) > 1:
            warns.append(f"{lane}: mixes frontend and backend tasks — split unless one toolchain covers both")
    return fails, warns


def execution_line(tasks: dict[str, Task], wave: str | None, eta: str | None, old: str | None) -> str:
    n = len(tasks)
    done = sum(t.status == "🟢" for t in tasks.values())
    pct = round(100 * done / n) if n else 0
    old_wave = re.search(r"wave ([^·]+?)\s*(·|$)", old or "")
    old_eta = re.search(r"ETA ([^·]+?)\s*$", old or "")
    wave = wave or (old_wave.group(1) if old_wave else "?/?")
    eta = eta or (old_eta.group(1).lstrip("~") if old_eta else "unknown")
    return f"**Execution**: {done}/{n} 🟢 ({pct}%) · wave {wave} · ETA ~{eta}"


def task_section(lines: list[str], code: str) -> tuple[int, int]:
    hs = headings(lines)
    for n, (i, level, text) in enumerate(hs):
        if re.match(rf"{re.escape(code)}\b", text):
            end = next((j for j, lv, _ in hs[n + 1 :] if lv <= level), len(lines))
            while end > i + 1 and lines[end - 1].strip() in ("", "---"):
                end -= 1
            return i, end
    raise PddfError(f"no task section heading starting with {code}")


def compute_waves(tasks: dict[str, Task]) -> tuple[list[list[str]], list[str]]:
    """Waves over pending tasks; returns (waves, problems)."""
    problems = [f"{t.code} depends on unknown {d}" for t in tasks.values() for d in t.deps if d not in tasks]
    done = {c for c, t in tasks.items() if t.status == "🟢"}
    pending = [c for c in tasks if c not in done]
    waves: list[list[str]] = []
    placed = set(done)
    while pending:
        wave = [c for c in pending if all(d in placed or d not in tasks for d in tasks[c].deps)]
        if not wave:
            problems.append("dependency cycle among: " + ", ".join(pending))
            break
        waves.append(wave)
        placed |= set(wave)
        pending = [c for c in pending if c not in wave]
    return waves, problems


# ---------- Status Sync ----------


def aggregate(statuses: list[str], base: str) -> str:
    """Epic/project rule: all 🟢 → 🟢 · any 🔵/🟢 → 🔵 · all ≥🟣 → 🟣 · else base."""
    if not statuses:
        return base
    if all(s == "🟢" for s in statuses):
        return "🟢"
    if any(s in "🔵🟢" for s in statuses):
        return "🔵"
    if all(RANK[s] >= RANK["🟣"] for s in statuses):
        return "🟣"
    return base


def derive_feature(fdir: Path | None, stored: str | None) -> tuple[str, str, str]:
    """Returns (status, 'done/total', reason)."""
    if fdir is None:
        return "⚪", "0/0", "no feature directory"
    tf = fdir / "feat-tasks.md"
    if not tf.exists():
        return ("🟡", "0/0", "PRD, no tasks") if (fdir / "feat-prd.md").exists() else ("⚪", "0/0", "no PRD")
    try:
        _, tasks = load_tasks(read(tf))
    except PddfError as exc:
        raise PddfError(f"{tf}: {exc}") from exc
    states = [t.status or "⚪" for t in tasks.values()]
    done, n = states.count("🟢"), len(states)
    progress = f"{done}/{n}"
    if all(s == "⚪" for s in states):
        return "🟣", progress, "tasks generated, none started"
    if done == n:
        if stored == "🟢":
            return "🟢", progress, "verified"
        return "🔵", progress, "all tasks 🟢 — awaiting do/verify"
    return "🔵", progress, f"{done}/{n} tasks 🟢"


def progress_bar(done: int, total: int) -> str:
    filled = round(10 * done / total) if total else 0
    return "▓" * filled + "░" * (10 - filled)


def sync_epic(edir: Path, today: str, check: bool, drift: list[str], review: list[str], reopen: set[str]) -> tuple[str, str]:
    path = edir / "epic-status.md"
    if not path.exists():
        drift.append(f"{edir.name}: no epic-status.md")
        return ("🟡" if (edir / "epic-prd.md").exists() else "⚪"), "—"
    lines = read(path)
    table = Table(lines, "Feature Table", "Features", needs=("code", "status"))
    c_code, c_status = table.col("code"), table.col("status")
    c_prog = table.col("progress", required=False)
    seen, statuses = set(), []
    for row in table.rows:
        m = re.search(r"F(\d+)", table.cell(row, c_code))
        if not m:
            continue
        seen.add(int(m.group(1)))
        fdir = child_dir(edir, "f", int(m.group(1)))
        stored = status_of(table.cell(row, c_status))
        label = f"{edir.name} F{m.group(1)}"
        try:
            status, progress, why = derive_feature(fdir, stored)
        except PddfError as exc:
            drift.append(f"{label}: cannot parse, stored status kept — {exc}")
            statuses.append(stored or "⚪")
            continue
        key = f"E{code_num(edir.name.split('-')[0], 'e')}F{m.group(1)}"
        if stored == "🟢" and status != "🟢" and key not in reopen:
            # never auto-downgrade a verified feature: stale rows and appended work look identical
            review.append(
                f"{label}: stored 🟢 but {why} — shipped? mark rows 🟢 (`pddf task`) after spot-checking code;"
                f" reopened? `pddf sync --reopen {key}`"
            )
            statuses.append("🟢")
            continue
        statuses.append(status)
        if stored != status:
            drift.append(f"{label}: status {stored or '∅'} → {status} ({why})")
            table.set(row, c_status, with_status(table.cell(row, c_status), status))
        if c_prog is not None:
            old = table.cell(row, c_prog)
            if not same_fraction(old, progress):
                drift.append(f"{label}: progress {old or '∅'} → {progress}")
                table.set(row, c_prog, progress)
    for d in sorted(p for p in edir.iterdir() if p.is_dir() and re.match(r"f\d+", p.name)):
        n = int(re.match(r"f(\d+)", d.name).group(1))
        if n not in seen:
            drift.append(f"{edir.name}: {d.name} has no Feature Table row — add it (plan/change)")
    done, total = statuses.count("🟢"), len(statuses)
    for i, line in enumerate(lines):
        if line.startswith("Progress:") and "feature" in line:
            new = f"Progress: `{progress_bar(done, total)}` {done}/{total} features"
            if line != new:
                lines[i] = new
    if lines != read(path):
        lines = [re.sub(r"(\*\*Last Updated\*\*:).*", rf"\1 {today}", ln) for ln in lines]
        if not check:
            write(path, lines)
    base = "🟡" if (edir / "epic-prd.md").exists() else "⚪"
    return aggregate(statuses, base), (f"{done}/{total}" if total else "—")


def cmd_sync(docs: Path, check: bool, reopen: list[str]) -> int:
    today = dt.date.today().isoformat()
    drift: list[str] = []
    review: list[str] = []
    reopen_keys = {r.upper().replace(" ", "") for r in reopen}
    epics_root = docs / "epics"
    if not epics_root.is_dir():
        raise PddfError(f"no {epics_root}")
    derived: dict[int, tuple[str, str]] = {}
    for edir in sorted(p for p in epics_root.iterdir() if p.is_dir() and re.match(r"e\d+", p.name)):
        n = int(re.match(r"e(\d+)", edir.name).group(1))
        try:
            status, progress = sync_epic(edir, today, check, drift, review, reopen_keys)
        except PddfError as exc:
            drift.append(f"{edir.name}: cannot parse, epic row left as stored — {exc}")
            derived[n] = ("?", "?")
            continue
        derived[n] = (status, progress)
    path = docs / "project-status.md"
    try:
        sync_project(path, derived, today, check, drift, review)
    except PddfError as exc:
        drift.append(f"{path}: cannot parse — {exc}")
    for line in drift:
        print(line)
    for line in review:
        print(f"REVIEW {line}")
    verb = "found" if check else "repaired"
    print(f"{len(drift)} drift item(s) {verb} · {len(review)} need review" if drift or review else "No drift found")
    return 1 if (drift and check) or review else 0


def sync_project(
    path: Path, derived: dict[int, tuple[str, str]], today: str, check: bool, drift: list[str], review: list[str]
) -> None:
    if not path.exists():
        drift.append(f"{path} missing")
        return
    lines = read(path)
    original = list(lines)
    table = Table(lines, "Epic Roadmap", "Epic Status", needs=("code", "status"))
    c_code, c_status = table.col("code"), table.col("status")
    c_prog = table.col("progress", required=False)
    statuses, seen = [], set()
    for row in table.rows:
        m = re.search(r"E(\d+)", table.cell(row, c_code))
        if not m:
            continue
        n = int(m.group(1))
        seen.add(n)
        stored = status_of(table.cell(row, c_status))
        status, progress = derived.get(n, ("⚪", "—"))
        if status == "?":  # epic unparseable: keep stored values
            statuses.append(stored or "⚪")
            continue
        if stored == "🟢" and status != "🟢" and progress == "—":
            review.append(f"E{n}: stored 🟢 but no feature rows to derive from — list its features in epic-status.md")
            statuses.append("🟢")
            continue
        statuses.append(status)
        if stored != status:
            drift.append(f"E{n}: status {stored or '∅'} → {status}")
            table.set(row, c_status, with_status(table.cell(row, c_status), status))
        if c_prog is not None and not same_fraction(table.cell(row, c_prog), progress):
            drift.append(f"E{n}: progress {table.cell(row, c_prog) or '∅'} → {progress}")
            table.set(row, c_prog, progress)
    for n in sorted(set(derived) - seen):
        drift.append(f"E{n}: directory exists but no Epic Roadmap row — add it (plan/change)")
    project = aggregate(statuses, "🟡" if statuses else "⚪")
    done, total = statuses.count("🟢"), len(statuses)
    counts = {WORDS[s]: statuses.count(s) for s in STATUSES}
    for i, line in enumerate(lines):
        m = re.match(r'^(\s*)"(DONE|TODO|SPEC|PLAN|DEV)"\s*:\s*\d+\s*$', line)
        if m:
            lines[i] = f'{m.group(1)}"{m.group(2)}" : {counts[m.group(2)]}'
        elif re.match(r"^Epics done:", line):
            pct = round(100 * done / total) if total else 0
            lines[i] = f"Epics done: {done}/{total} ({pct}%)"
        elif re.match(r"^>\s*\*\*Status\*\*:", line):
            new = re.sub(r"(\*\*Status\*\*:).*", rf"\1 {project}", line)
            if status_of(line) != project:
                drift.append(f"project: status {status_of(line) or '∅'} → {project}")
            lines[i] = new
    if lines != original:
        lines = [re.sub(r"(\*\*Last Updated\*\*:).*", rf"\1 {today}", ln) for ln in lines]
        if not check:
            write(path, lines)


# ---------- Commands ----------


def cmd_task(docs: Path, e: str, f: str, t: str, status: str, wave: str | None, eta: str | None) -> int:
    path = tasks_file(docs, e, f)
    lines = read(path)
    table, tasks = load_tasks(lines)
    code = task_code(t)
    if code not in tasks:
        raise PddfError(f"{code} not in Task Summary of {path}")
    new = parse_status(status)
    c_status = table.col("status")
    old = tasks[code].status
    table.set(tasks[code].row, c_status, with_status(table.cell(tasks[code].row, c_status), new))
    tasks[code].status = new
    text = "\n".join(lines)
    m = EXECUTION_RE.search(text)
    if m or wave or eta:
        line = execution_line(tasks, wave, eta, m.group(0) if m else None)
        if m:
            text = text[: m.start()] + line + text[m.end() :]
            lines = text.split("\n")
        else:
            first_row = Table(lines, "Task Summary").rows[0] - 2  # header line
            lines[first_row:first_row] = [line, ""]
    write(path, lines)
    done = sum(x.status == "🟢" for x in tasks.values())
    print(f"{code} {old or '∅'} → {new} · {done}/{len(tasks)} 🟢")
    return 0


def cmd_waves(docs: Path, e: str, f: str) -> int:
    _, tasks = load_tasks(read(tasks_file(docs, e, f)))
    waves, problems = compute_waves(tasks)
    done = sum(t.status == "🟢" for t in tasks.values())
    print(f"{done}/{len(tasks)} 🟢 · {len(waves)} pending wave(s)")
    for n, wave in enumerate(waves, 1):
        print(f"Wave {n}: " + ", ".join(f"{c}{'' if tasks[c].status in (None, '⚪') else ' ' + tasks[c].status}" for c in wave))
    wave_of = {c: n for n, wave in enumerate(waves, 1) for c in wave}
    for lane, members in lanes_of(tasks).items():
        pending = [c for c in members if tasks[c].status != "🟢"]
        if len(members) < 2 or not pending:
            continue
        joins = sorted({d for c in pending[1:] for d in tasks[c].deps if d in tasks and d not in members
                        and tasks[d].status != "🟢"}, key=task_key)
        print(f"Lane {lane}: {' → '.join(pending)} · starts wave {wave_of.get(pending[0], '?')}"
              + (f" · joins {', '.join(joins)}" if joins else ""))
    for p in problems:
        print(f"PROBLEM: {p}")
    return 1 if problems else 0


def instruction_files(root: Path) -> list[str]:
    found = [p for p in INSTRUCTION_FILES if (root / p).exists()]
    if (root / ".cursor" / "rules").is_dir():
        found.append(".cursor/rules/")
    return found


def contracts_for(lines: list[str], code: str) -> list[str]:
    try:
        table = Table(lines, "Shared Contracts")
    except PddfError:
        return []
    hdr = table.rows[0] - 2
    hits = [lines[r] for r in table.rows if re.search(rf"\b{code}\b", "|".join(split_row(lines[r])[3:]))]
    return [lines[hdr], lines[hdr + 1], *hits] if hits else []


def task_block(lines: list[str], code: str) -> tuple[list[str], set[str]]:
    """Task section + its contracts (if not inlined) · pattern paths it names."""
    start, end = task_section(lines, code)
    body = lines[start:end]
    out = list(body)
    if not any("**Contracts**" in ln for ln in body) and (rows := contracts_for(lines, code)):
        out += ["", f"#### Shared Contracts touching {code} (exact — never change them)", "", *rows]
    return out, set(re.findall(r"docs/patterns/[\w./-]+\.md", "\n".join(body)))


def print_patterns(patterns: set[str], root: Path) -> None:
    if patterns:
        print("\n## Patterns to read before coding\n")
        for p in sorted(patterns):
            print(f"- {p}" + ("" if (root / p).exists() else "  (MISSING — report as task-quality defect)"))


def cmd_packet(docs: Path, e: str, f: str, t: str) -> int:
    path = tasks_file(docs, e, f)
    lines = read(path)
    _, tasks = load_tasks(lines)
    root = docs.parent
    if re.fullmatch(LANE, t.strip().upper()):
        return lane_packet(lines, tasks, path, root, e, f, t.strip().upper())
    code = task_code(t)
    if code not in tasks:
        raise PddfError(f"{code} not in Task Summary of {path}")
    blocked = [d for d in tasks[code].deps if d in tasks and tasks[d].status != "🟢"]
    print(f"# Task packet — {e.upper()} {f.upper()} {code}")
    print(f"Source: {path} (do not open it — this packet is your whole context)")
    if instr := instruction_files(root):
        print("Repository instructions (read and obey): " + ", ".join(instr))
    if blocked:
        print("WARNING: dependencies not 🟢 yet: " + ", ".join(blocked))
    print()
    block, patterns = task_block(lines, code)
    print("\n".join(block).replace("#### Shared Contracts", "## Shared Contracts"))
    print_patterns(patterns, root)
    return 0


def lane_packet(lines: list[str], tasks: dict[str, Task], path: Path, root: Path, e: str, f: str, lane: str) -> int:
    members = lanes_of(tasks).get(lane)
    if not members:
        raise PddfError(f"no task in lane {lane} of {path}")
    pending = [c for c in members if tasks[c].status != "🟢"]
    if not pending:
        raise PddfError(f"lane {lane}: every task already 🟢")
    included: list[str] = []
    stop: tuple[str, list[str]] | None = None
    for code in pending:
        ext = [d for d in tasks[code].deps if d in tasks and d not in members and tasks[d].status != "🟢"]
        if ext and included:
            stop = (code, ext)
            break
        included.append(code)
    print(f"# Lane packet — {e.upper()} {f.upper()} {lane}: {' → '.join(included)}")
    print(f"Source: {path} (do not open it — this packet is your whole context)")
    if instr := instruction_files(root):
        print("Repository instructions (read and obey): " + ", ".join(instr))
    first_ext = [d for d in tasks[included[0]].deps if d in tasks and d not in members and tasks[d].status != "🟢"]
    if first_ext:
        print("WARNING: dependencies not 🟢 yet: " + ", ".join(first_ext))
    print(f"Order: tasks below, one at a time, in order · after each task passes its validation: "
          f"`pddf beat {e.upper()} {f.upper()} T{{n}} done` · Budget resets per task · "
          f"stuck on one task → HANDOVER for that task, stop the lane")
    if stop:
        print(f"Lane pauses before {stop[0]} (waits on {', '.join(stop[1])}): stop after {included[-1]}, return report")
    patterns: set[str] = set()
    for code in included:
        block, pats = task_block(lines, code)
        patterns |= pats
        print()
        print("\n".join(block))
    print_patterns(patterns, root)
    return 0


def run_log(docs: Path, e: str, f: str) -> Path:
    return docs.parent / ".pddf" / "run" / f"e{code_num(e, 'e')}f{code_num(f, 'f')}.log"


BEAT_RE = re.compile(r"^(\S+) (\S+) (.*)$")
ANNOUNCED_RE = re.compile(r"~\s*(\d+)\s*(m|min)\b", re.I)


def cmd_beat(docs: Path, e: str, f: str, t: str | None, message: list[str]) -> int:
    _, tasks = load_tasks(read(tasks_file(docs, e, f)))
    path = run_log(docs, e, f)
    now = dt.datetime.now(dt.timezone.utc)
    if t is not None:
        code = task_code(t)
        if code not in tasks:
            raise PddfError(f"{code} not in Task Summary")
        msg = " ".join(message).strip() or "alive"
        path.parent.mkdir(parents=True, exist_ok=True)
        ignore = path.parent.parent / ".gitignore"
        if not ignore.exists():
            ignore.write_text("*\n", encoding="utf-8")
        with path.open("a", encoding="utf-8") as fh:
            fh.write(f"{now.strftime('%Y-%m-%dT%H:%M:%SZ')} {code} {msg}\n")
        print(f"beat {code}: {msg}")
        return 0
    last: dict[str, tuple[dt.datetime, str]] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if m := BEAT_RE.match(line):
                try:
                    when = dt.datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
                except ValueError:
                    continue
                last[m.group(2)] = (when, m.group(3))
    active = [c for c, task in tasks.items() if task.status == "🔵"]
    for code in sorted(set(last) | set(active), key=task_key):
        if code not in last:
            print(f"{code} 🔵 no beat yet")
            continue
        when, msg = last[code]
        age = (now - when).total_seconds() / 60
        hint = ""
        if a := ANNOUNCED_RE.search(msg):
            hint = " · within announced runtime" if age <= 1.5 * int(a.group(1)) else " · OVER announced runtime ×1.5"
        print(f"{code} {age:.0f}m ago: {msg}{hint}")
    if not last and not active:
        print("no beats")
    return 0


EXTERNAL_REF = re.compile(
    r"(\b(see|as described in|as defined in|refer to|per)\s+(the\s+)?(PRD|architecture|arch\b|spec\b))"
    r"|\b(feat-prd|epic-prd|epic-arch|feat-arch)\.md\b",
    re.I,
)
SETUP_KINDS = re.compile(r"test|config|setup|infra|migration|doc|chore|refactor", re.I)


def cmd_lint_tasks(docs: Path, e: str, f: str, strict: bool) -> int:
    path = tasks_file(docs, e, f)
    lines = read(path)
    _, tasks = load_tasks(lines)
    issues: list[str] = []
    _, problems = compute_waves(tasks)
    issues += problems
    lane_fails, lane_warns = lane_issues(tasks)
    issues += lane_fails
    warnings: list[str] = list(lane_warns)
    for code in tasks:
        try:
            start, end = task_section(lines, code)
        except PddfError:
            issues.append(f"{code}: in Task Summary but no '### {code}' section")
            continue
        text = "\n".join(lines[start:end])
        if not re.search(r"(Create|Modify|Delete)\s*:\s*`", text):
            issues.append(f"{code}: no Files entry with exact path (Create/Modify/Delete: `path`)")
        if not re.search(r"Done when", text, re.I):
            issues.append(f"{code}: no 'Done when' block")
        if not re.search(r"[Vv]alidation[^\n]*`[^`]+`", text):
            issues.append(f"{code}: no validation command in backticks")
        for m in EXTERNAL_REF.finditer(text):
            issues.append(f"{code}: external reference {m.group(0)!r} — inline the content instead")
        if tasks[code].is_test and tasks[code].status != "🟢":
            tier = re.search(r"\*\*Tier\*\*\s*:\s*(fast|slow)\b", text, re.I)
            if not tier:
                (issues if strict else warnings).append(f"{code}: Test task without '**Tier**: fast|slow' line")
            elif tier.group(1).lower() == "slow" and not re.search(r"\*\*Expected runtime\*\*\s*:", text, re.I):
                (issues if strict else warnings).append(f"{code}: slow Test task without '**Expected runtime**: ~N min' line")
    section_codes = {m.group(1) for _, _, h in headings(lines) if (m := re.match(rf"({TASK})\b", h))}
    for code in sorted(section_codes - set(tasks), key=task_key):
        issues.append(f"{code}: has a section but no Task Summary row")
    if strict and len(tasks) > 1 and not any(t.lane for t in tasks.values()):
        try:
            Table(lines, "Task Summary").col("lane")
        except PddfError:
            warnings.append("no Lane column — every task dispatched to its own coder (pre-3.10 format)")
    try:
        s, e_ = section_bounds(lines, "Story Trace")
        trace = "\n".join(lines[s:e_])
    except PddfError:
        trace = None
        if strict:
            issues.append("no Story Trace section")
        else:
            warnings.append("no Story Trace section — pre-3.7 format, story checks skipped (plan/tasks regenerates it)")
    if trace is not None:
        traced = set(re.findall(rf"\b{TASK}\b", trace))
        for code in sorted(traced - set(tasks), key=task_key):
            issues.append(f"Story Trace names unknown task {code}")
        for code, task in tasks.items():
            if code not in traced and not SETUP_KINDS.search(task.kind + " " + task.title):
                warnings.append(f"{code}: not in Story Trace and not a setup/test task — orphan?")
        try:
            st = Table(lines, "Story Trace")
            tcol = st.col("tested by", required=False)
        except PddfError:
            st, tcol = None, None
        if st is not None and tcol is None:
            msg = "Story Trace has no 'Tested by' column — pre-3.9 format, test placement unchecked"
            (issues if strict else warnings).append(msg)
        elif st is not None:
            for r in st.rows:
                cells = split_row(lines[r])[1:-1]
                cell = cells[tcol] if tcol < len(cells) else ""
                testers = re.findall(rf"\b{TASK}\b", cell)
                if not testers:
                    issues.append(f"Story Trace row {cells[0].strip()[:40]!r}: no 'Tested by' task")
                for code in testers:
                    if code in tasks and not re.search(r"test", tasks[code].kind + " " + tasks[code].title, re.I):
                        warnings.append(f"{code} in 'Tested by' is not a Test task — fine only for risk-critical steps")
        prd = path.parent / "feat-prd.md"
        if prd.exists():
            ids = sorted(set(re.findall(r"\b(?:US|AC)-\d+(?:\.\d+)?\b", prd.read_text(encoding="utf-8"))))
            for ident in ids:
                if not re.search(rf"\b{re.escape(ident)}\b", trace):
                    issues.append(f"{ident} (feat-prd.md) missing from Story Trace")
    try:
        table = Table(lines, "Shared Contracts")
        for r in table.rows:
            for code in re.findall(rf"\b{TASK}\b", "|".join(split_row(lines[r])[3:])):
                if code not in tasks:
                    issues.append(f"Shared Contracts row {table.cell(r, 0)!r} names unknown task {code}")
    except PddfError:
        if trace is not None or strict:
            warnings.append("no Shared Contracts table (fine only if no interface crosses tasks)")
    for line in issues:
        print(f"FAIL {line}")
    for line in warnings:
        print(f"WARN {line}")
    print(f"{len(issues)} issue(s), {len(warnings)} warning(s) · {len(tasks)} tasks")
    return 1 if issues else 0


def cmd_section(file: Path, heading: str, replace: bool) -> int:
    lines = read(file)
    start, end = section_bounds(lines, heading)
    if not replace:
        print("\n".join(lines[start:end]).rstrip("\n"))
        return 0
    new = sys.stdin.read().rstrip("\n").split("\n")
    if not HEADING_RE.match(new[0]):
        raise PddfError("stdin must start with the section heading (full section replaces old one)")
    tail = [""] if end < len(lines) else []
    write(file, lines[:start] + new + tail + lines[end:])
    print(f"replaced {heading!r}: {end - start} → {len(new)} lines")
    return 0


def cmd_toc(file: Path) -> int:
    for i, level, text in headings(read(file)):
        print(f"{i + 1:>5}  {'#' * level} {text}")
    return 0


def cmd_review_open(file: Path) -> int:
    lines = read(file)
    hs = headings(lines)
    open_items = 0
    for n, (i, _, title) in enumerate(hs):
        end = hs[n + 1][0] if n + 1 < len(hs) else len(lines)
        block = lines[i:end]
        confirm = next((ln for ln in block if "**Confirm?**" in ln), None)
        if confirm is None:
            continue
        k = next((j for j, ln in enumerate(block) if "Your answer" in ln), None)
        answer = ""
        if k is not None:
            answer = block[k].split("Your answer", 1)[1].lstrip("*:").strip()
            answer += " ".join(ln.lstrip("> ").strip() for ln in block[k + 1 :] if ln.startswith(">"))
        if not answer.strip():
            open_items += 1
            print(f"{i + 1:>5}  {title}\n       {confirm.strip()}")
    print(f"{open_items} unanswered item(s)")
    return 0


def cmd_find(docs: Path, e: str, f: str | None) -> int:
    d = feat_dir(docs, e, f) if f else epic_dir(docs, e)
    print(d)
    for p in sorted(d.iterdir()):
        print(f"  {p.name}{'/' if p.is_dir() else ''}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="pddf", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docs", default="docs", help="docs directory (default: ./docs)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("sync")
    p.add_argument("--check", action="store_true", help="report drift only, write nothing")
    p.add_argument("--reopen", action="append", default=[], metavar="E{n}F{n}",
                   help="allow downgrading this verified 🟢 feature (tasks appended after verification)")
    p = sub.add_parser("task")
    for name in ("epic", "feature", "task", "status"):
        p.add_argument(name)
    p.add_argument("--wave")
    p.add_argument("--eta")
    for name in ("waves", "lint-tasks"):
        p = sub.add_parser(name)
        p.add_argument("epic")
        p.add_argument("feature")
        if name == "lint-tasks":
            p.add_argument("--strict", action="store_true", help="planning mode: missing Story Trace is a FAIL, not a WARN")
    p = sub.add_parser("packet")
    for name in ("epic", "feature"):
        p.add_argument(name)
    p.add_argument("task", help="T{n}, or L{n} for a lane packet")
    p = sub.add_parser("beat")
    p.add_argument("epic")
    p.add_argument("feature")
    p.add_argument("task", nargs="?", help="omit to show last beat per task")
    p.add_argument("message", nargs="*")
    p = sub.add_parser("section")
    p.add_argument("file", type=Path)
    p.add_argument("heading")
    p.add_argument("--replace", action="store_true", help="replace whole section with stdin")
    for name in ("toc", "review-open"):
        sub.add_parser(name).add_argument("file", type=Path)
    p = sub.add_parser("find")
    p.add_argument("epic")
    p.add_argument("feature", nargs="?")
    a = ap.parse_args(argv)
    docs = Path(a.docs)
    try:
        if a.cmd == "sync":
            return cmd_sync(docs, a.check, a.reopen)
        if a.cmd == "task":
            return cmd_task(docs, a.epic, a.feature, a.task, a.status, a.wave, a.eta)
        if a.cmd == "waves":
            return cmd_waves(docs, a.epic, a.feature)
        if a.cmd == "lint-tasks":
            return cmd_lint_tasks(docs, a.epic, a.feature, a.strict)
        if a.cmd == "packet":
            return cmd_packet(docs, a.epic, a.feature, a.task)
        if a.cmd == "beat":
            return cmd_beat(docs, a.epic, a.feature, a.task, a.message)
        if a.cmd == "section":
            return cmd_section(a.file, a.heading, a.replace)
        if a.cmd == "toc":
            return cmd_toc(a.file)
        if a.cmd == "review-open":
            return cmd_review_open(a.file)
        return cmd_find(docs, a.epic, a.feature)
    except (PddfError, OSError) as exc:
        print(f"pddf: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
