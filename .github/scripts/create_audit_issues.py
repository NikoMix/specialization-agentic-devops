#!/usr/bin/env python3
"""Create the GitHub issues that track an Agentic DevOps specialization audit cycle.

The issue set is derived from the audit guide itself (``content/docs/``) rather
than from a hand-maintained list, so the issues cannot drift away from the
published guidance:

* the pre-qualification gate comes from ``requirements.md``
* one issue per control comes from ``module-a/`` and ``module-b/``
* one issue per **Module B** evidence item comes from each Module B control's
  "Required Evidence Checklist" table, because Module B is the part of the audit
  that cannot be satisfied with evidence reused from another specialization

Every issue is created at most once per audit cycle: existing titles carrying
the cycle label are read back first and skipped.

Usage::

    python .github/scripts/create_audit_issues.py --repo owner/name --year 2026
    python .github/scripts/create_audit_issues.py --repo owner/name --dry-run
    python .github/scripts/create_audit_issues.py --repo owner/name --scope module-b
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

DOCS = Path("content/docs")
SITE_BASE = "https://nikomix.github.io/specialization-agentic-devops"

# A control page is titled e.g.  A.1.1 – Organisational Data
CONTROL_TITLE = re.compile(r'^title:\s*"(?P<ref>[AB]\.\d+\.\d+)\s*[–-]\s*(?P<name>.+?)"\s*$', re.M)
DESCRIPTION = re.compile(r'^description:\s*"(?P<text>.+?)"\s*$', re.M)
EVIDENCE_HEADER = re.compile(r"^\|\s*#\s*\|\s*Evidence Item\s*\|", re.I)
TABLE_ROW = re.compile(r"^\|(?P<cells>.+)\|\s*$")
CHECKLIST_ITEM = re.compile(r"^- \[[ xX]\]\s+(?P<text>.+?)\s*$", re.M)

# Guards: if the guide is restructured and parsing silently degrades, fail loudly
# rather than opening a partial and misleading set of audit issues.
EXPECTED_MODULE_A_CONTROLS = 7
EXPECTED_MODULE_B_CONTROLS = 6
MIN_EVIDENCE_ITEMS_PER_CONTROL = 3


@dataclass
class Control:
    ref: str
    name: str
    description: str
    slug: str
    module: str
    evidence: list[str] = field(default_factory=list)

    @property
    def url(self) -> str:
        return f"{SITE_BASE}/docs/module-{self.module.lower()}/{self.slug}/"


@dataclass
class IssueSpec:
    title: str
    body: str
    labels: list[str]
    key: str = ""
    parent_key: str = ""


# ─── Parsing the audit guide ────────────────────────────────────────────────


def strip_markup(text: str) -> str:
    """Flatten the inline Markdown used in the evidence tables to plain text."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\([^)]*\)", r"\1", text)
    return text.strip()


def parse_evidence_items(body: str) -> list[str]:
    """Read the first '| # | Evidence Item | ... |' table on the page."""
    lines = body.splitlines()
    items: list[str] = []
    inside = False
    for line in lines:
        if not inside:
            if EVIDENCE_HEADER.match(line):
                inside = True
            continue
        match = TABLE_ROW.match(line)
        if not match:
            break
        cells = [c.strip() for c in match.group("cells").split("|")]
        if not cells or set("".join(cells)) <= set("-: "):
            continue  # delimiter row
        if len(cells) < 2 or not cells[0].isdigit():
            break
        formats = strip_markup(cells[2]) if len(cells) > 2 else ""
        item = strip_markup(cells[1])
        items.append(f"{item} — accepted formats: {formats}" if formats else item)
    return items


def load_controls(module: str) -> list[Control]:
    directory = DOCS / f"module-{module.lower()}"
    controls: list[Control] = []
    for path in sorted(directory.glob("*.md")):
        if path.name == "_index.md":
            continue
        text = path.read_text(encoding="utf-8")
        title = CONTROL_TITLE.search(text)
        if not title:
            print(f"::warning::no control reference found in {path}", file=sys.stderr)
            continue
        description = DESCRIPTION.search(text)
        controls.append(
            Control(
                ref=title.group("ref"),
                name=title.group("name").strip(),
                description=strip_markup(description.group("text")) if description else "",
                slug=path.stem,
                module=module.upper(),
                evidence=parse_evidence_items(text),
            )
        )
    return controls


def load_prequalification() -> list[str]:
    path = DOCS / "requirements.md"
    text = path.read_text(encoding="utf-8")
    marker = text.find("## Quick Readiness Checklist")
    if marker == -1:
        raise SystemExit(f"{path}: 'Quick Readiness Checklist' section not found")
    return [strip_markup(m.group("text")) for m in CHECKLIST_ITEM.finditer(text[marker:])]


# ─── Issue bodies ───────────────────────────────────────────────────────────


def checklist(items: list[str]) -> str:
    return "\n".join(f"- [ ] {item}" for item in items)


def prequalification_issue(items: list[str], year: int) -> IssueSpec:
    body = f"""## Pre-Qualification Gate — {year} audit cycle

Confirm every pre-qualification requirement **before** requesting the Agentic DevOps
audit from Partner Center. Requesting early is the most common cause of a failed cycle.

📖 [Pre-Qualification Requirements]({SITE_BASE}/docs/requirements/)

> [!WARNING]
> The Agentic DevOps specialization is newly framed by Microsoft + GitHub. The
> thresholds, ACR pillars and certification list in the guide are drafts based on the
> closest published guidance. Confirm every figure with your PDM before relying on it.

### Readiness checklist

{checklist(items)}

### Exit criteria

- [ ] Every box above is ticked and evidenced
- [ ] PDM has confirmed the ACR figures in writing
- [ ] Audit requested via Partner Center → Benefits → Advanced Specializations

Close this issue once the audit has been requested.
"""
    return IssueSpec(
        title=f"🎯 Pre-Qualification Gate ({year})",
        body=body,
        labels=["pre-qualification"],
        key="prequal",
    )


def control_issue(control: Control, year: int, child_titles: list[str]) -> IssueSpec:
    emoji = "📋" if control.module == "A" else "🤖"
    module_label = "Module A – General Requirements" if control.module == "A" else "Module B – Agentic DevOps"

    sections = [
        f"## {control.ref} — {control.name}",
        "",
        control.description,
        "",
        f"📖 [Full guidance]({control.url})",
        "",
        "### Evidence to collect",
        "",
        checklist(control.evidence) if control.evidence else "_No evidence table found on the guide page._",
    ]

    if child_titles:
        sections += [
            "",
            "### Tracked evidence issues",
            "",
            "Each evidence item below is tracked in its own issue so it can be assigned and",
            "scheduled independently. This list is populated once the child issues exist.",
            "",
            "<!-- audit-children -->",
        ]

    sections += [
        "",
        "### Submission",
        "",
        f"- [ ] Files named `{control.ref}_<DocumentType>_v<N>.pdf`",
        "- [ ] Uploaded to the engagement evidence folder",
        f"- [ ] [Evidence Tracker]({SITE_BASE}/docs/evidence-tracker/) row updated",
        "",
        f"_Audit cycle {year} · {module_label}_",
    ]

    return IssueSpec(
        title=f"{emoji} {control.ref} {control.name}",
        body="\n".join(sections),
        labels=[f"module-{control.module.lower()}", "audit-control"],
        key=control.ref,
    )


def evidence_issue(control: Control, index: int, item: str, year: int) -> IssueSpec:
    headline, _, formats = item.partition(" — accepted formats: ")
    body = f"""## {control.ref} evidence item {index} — {headline}

Part of control **{control.ref} — {control.name}**.

📖 [Control guidance]({control.url})

### What to produce

- [ ] {headline}
{f"- [ ] Saved in an accepted format: {formats}" if formats else ""}
- [ ] Anonymised where the source contains customer-identifying detail
- [ ] Named `{control.ref}_<DocumentType>_v<N>` and added to the evidence folder
- [ ] [Evidence Tracker]({SITE_BASE}/docs/evidence-tracker/) row updated

### Definition of done

The auditor can open this artefact and match it to control {control.ref} without
asking a follow-up question.

_Audit cycle {year} · Module B evidence item_
"""
    return IssueSpec(
        title=f"🧾 {control.ref}.{index} {headline}",
        body=body,
        labels=["module-b", "audit-evidence"],
        key=f"{control.ref}.{index}",
        parent_key=control.ref,
    )


# ─── GitHub plumbing ────────────────────────────────────────────────────────


def gh(args: list[str], *, check: bool = True) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8")
    if check and result.returncode != 0:
        raise SystemExit(f"gh {' '.join(args)} failed ({result.returncode}):\n{result.stderr.strip()}")
    return result.stdout.strip()


LABELS = [
    ("pre-qualification", "0e8a16", "Pre-qualification gate"),
    ("module-a", "e4e669", "Module A – General Requirements"),
    ("module-b", "d73a4a", "Module B – Agentic DevOps specific"),
    ("audit-control", "5319e7", "One audit control"),
    ("audit-evidence", "c2e0c6", "One evidence artefact within a control"),
]


def ensure_labels(repo: str, cycle_label: str, year: int, dry_run: bool) -> None:
    wanted = LABELS + [(cycle_label, "0075ca", f"Audit cycle {year}")]
    for name, colour, description in wanted:
        if dry_run:
            print(f"  [dry-run] label {name}")
            continue
        gh(["label", "create", name, "--color", colour, "--description", description,
            "--repo", repo, "--force"])


def ensure_milestone(repo: str, year: int, dry_run: bool) -> str:
    title = f"Audit {year}"
    if dry_run:
        return title
    existing = gh(["api", f"repos/{repo}/milestones?state=all&per_page=100"])
    for milestone in json.loads(existing or "[]"):
        if milestone["title"] == title:
            return title
    gh(["api", f"repos/{repo}/milestones", "--method", "POST",
        "--field", f"title={title}",
        "--field", f"due_on={year}-06-30T00:00:00Z",
        "--field", f"description=Agentic DevOps Advanced Specialization – {year} audit cycle"])
    return title


def existing_titles(repo: str, cycle_label: str) -> set[str]:
    raw = gh(["issue", "list", "--repo", repo, "--state", "all",
              "--label", cycle_label, "--limit", "1000", "--json", "title"])
    return {issue["title"] for issue in json.loads(raw or "[]")}


def create_issue(repo: str, spec: IssueSpec, cycle_label: str, milestone: str) -> int:
    url = gh(["issue", "create", "--repo", repo,
              "--title", spec.title,
              "--body", spec.body,
              "--milestone", milestone,
              "--label", ",".join([*spec.labels, cycle_label])])
    return int(url.rstrip("/").rsplit("/", 1)[-1])


def link_children(repo: str, parent: int, children: list[int]) -> None:
    """Replace the placeholder in the parent body with a task list of children."""
    body = json.loads(gh(["api", f"repos/{repo}/issues/{parent}"]))["body"] or ""
    if "<!-- audit-children -->" not in body:
        return
    task_list = "\n".join(f"- [ ] #{number}" for number in children)
    gh(["api", f"repos/{repo}/issues/{parent}", "--method", "PATCH",
        "--field", f"body={body.replace('<!-- audit-children -->', task_list)}"])


# ─── Entry point ────────────────────────────────────────────────────────────


def main() -> int:
    # Issue titles carry emoji; a non-UTF-8 console must not crash the run.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="owner/name")
    parser.add_argument("--year", type=int, default=dt.datetime.now(dt.timezone.utc).year)
    parser.add_argument("--scope", default="all",
                        choices=["all", "pre-qualification", "module-a", "module-b"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not DOCS.is_dir():
        raise SystemExit(f"{DOCS} not found — run this from the repository root")

    module_a = load_controls("a")
    module_b = load_controls("b")

    if len(module_a) != EXPECTED_MODULE_A_CONTROLS:
        raise SystemExit(f"parsed {len(module_a)} Module A controls, expected {EXPECTED_MODULE_A_CONTROLS}")
    if len(module_b) != EXPECTED_MODULE_B_CONTROLS:
        raise SystemExit(f"parsed {len(module_b)} Module B controls, expected {EXPECTED_MODULE_B_CONTROLS}")
    for control in module_b:
        if len(control.evidence) < MIN_EVIDENCE_ITEMS_PER_CONTROL:
            raise SystemExit(
                f"{control.ref}: parsed only {len(control.evidence)} evidence items — "
                "the Required Evidence Checklist table did not parse"
            )

    cycle_label = f"audit-{args.year}"
    specs: list[IssueSpec] = []

    if args.scope in ("all", "pre-qualification"):
        specs.append(prequalification_issue(load_prequalification(), args.year))

    if args.scope in ("all", "module-a"):
        specs += [control_issue(c, args.year, []) for c in module_a]

    if args.scope in ("all", "module-b"):
        for control in module_b:
            children = [evidence_issue(control, i, item, args.year)
                        for i, item in enumerate(control.evidence, start=1)]
            specs.append(control_issue(control, args.year, [c.title for c in children]))
            specs += children

    print(f"repo={args.repo} cycle={cycle_label} scope={args.scope} issues={len(specs)}")

    if args.dry_run:
        for spec in specs:
            print(f"  [dry-run] {spec.title}  labels={spec.labels + [cycle_label]}")
        print(f"dry run complete: {len(specs)} issue(s) would be created")
        return 0

    ensure_labels(args.repo, cycle_label, args.year, args.dry_run)
    milestone = ensure_milestone(args.repo, args.year, args.dry_run)
    already = existing_titles(args.repo, cycle_label)

    numbers: dict[str, int] = {}
    children_by_parent: dict[str, list[int]] = {}
    created = skipped = 0

    for spec in specs:
        if spec.title in already:
            print(f"  skip (exists): {spec.title}")
            skipped += 1
            continue
        number = create_issue(args.repo, spec, cycle_label, milestone)
        numbers[spec.key] = number
        if spec.parent_key:
            children_by_parent.setdefault(spec.parent_key, []).append(number)
        created += 1
        print(f"  created #{number}: {spec.title}")

    for parent_key, child_numbers in children_by_parent.items():
        parent_number = numbers.get(parent_key)
        if parent_number:
            link_children(args.repo, parent_number, child_numbers)
            print(f"  linked {len(child_numbers)} evidence issue(s) to #{parent_number}")

    print(f"done: {created} created, {skipped} skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
