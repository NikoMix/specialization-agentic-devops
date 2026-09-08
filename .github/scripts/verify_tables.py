"""Verify every Markdown table in content/ reaches the built HTML as a <table>.

Counts the delimiter rows (|---|---|) per source page, counts <table> elements in
the corresponding built page, and reports any mismatch.  Exit code 1 on mismatch.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CONTENT = Path("content")
PUBLIC = Path("public")

DELIM = re.compile(r"^\s*\|(?:\s*:?-{2,}:?\s*\|)+\s*$")
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def source_tables(md: Path) -> int:
    text = FRONTMATTER.sub("", md.read_text(encoding="utf-8"))
    fenced, count = False, 0
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced and DELIM.match(line):
            count += 1
    return count


def built_page(md: Path) -> Path:
    rel = md.relative_to(CONTENT)
    if rel.name == "_index.md":
        return PUBLIC / rel.parent / "index.html"
    return PUBLIC / rel.parent / rel.stem / "index.html"


def main() -> int:
    total_src = total_html = 0
    failures: list[str] = []
    checked = 0

    for md in sorted(CONTENT.rglob("*.md")):
        expected = source_tables(md)
        if expected == 0:
            continue
        html_path = built_page(md)
        if not html_path.is_file():
            failures.append(f"{md.as_posix()}: expected {expected} tables, built page missing ({html_path})")
            continue
        html = html_path.read_text(encoding="utf-8")
        actual = len(re.findall(r"<table[\s>]", html))
        checked += 1
        total_src += expected
        total_html += actual
        if actual != expected:
            failures.append(f"{md.as_posix()}: {expected} markdown tables -> {actual} <table> in {html_path.as_posix()}")

    print(f"pages with tables: {checked}")
    print(f"markdown tables:   {total_src}")
    print(f"rendered <table>:  {total_html}")

    if not checked:
        print("FAIL: no pages with tables were examined at all", file=sys.stderr)
        return 1

    for line in failures:
        print(f"MISMATCH {line}", file=sys.stderr)
    if failures:
        print(f"FAIL: {len(failures)} page(s) mismatched", file=sys.stderr)
        return 1

    print("PASS: every markdown table rendered")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
