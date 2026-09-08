#!/usr/bin/env python3
"""Check every internal link in the built site actually resolves to a file.

The theme's own link render hook only warns about *relative* Markdown links, so
it says nothing about the absolute, site-rooted links this site uses. This walks
the generated HTML instead, which also covers links emitted by shortcodes.

Two failure classes are reported:

``missing``      the target does not exist under public/
``unprefixed``   a root-relative link that omits the site's base path, so it
                 would 404 once the site is served from a subdirectory

Exit code 1 if either class is non-empty.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

PUBLIC = Path("public")
# --minify emits unquoted attribute values, so accept all three quoting styles.
ATTR = r"""(?:"(?P<{0}d>[^"]*)"|'(?P<{0}s>[^']*)'|(?P<{0}u>[^\s"'>]+))"""
HREF = re.compile(r"<a\b[^>]*?\shref=" + ATTR.format("h"), re.I)
CANONICAL = re.compile(
    r"<link\b(?=[^>]*?\srel=(?:\"canonical\"|'canonical'|canonical[\s>]))[^>]*?\shref="
    + ATTR.format("c"),
    re.I,
)


def attr(match: re.Match, prefix: str) -> str:
    return next(
        (match.group(f"{prefix}{kind}") for kind in "dsu" if match.group(f"{prefix}{kind}") is not None),
        "",
    )


SKIP_SCHEMES = ("http:", "https:", "mailto:", "tel:", "javascript:", "data:", "//")


def detect_base() -> tuple[str, str]:
    """Return (host, base_path) from the home page's canonical URL."""
    home = PUBLIC / "index.html"
    if not home.is_file():
        raise SystemExit("public/index.html not found — build the site first")
    match = CANONICAL.search(home.read_text(encoding="utf-8"))
    if not match:
        raise SystemExit("no canonical link on the home page; cannot determine the base path")
    parts = urlsplit(attr(match, "c"))
    base = parts.path if parts.path.endswith("/") else parts.path + "/"
    return parts.netloc, base


def resolves(rel: str) -> bool:
    target = PUBLIC / rel.strip("/")
    if rel.endswith("/") or not target.suffix:
        return (target / "index.html").is_file() or target.is_file()
    return target.is_file()


def main() -> int:
    host, base = detect_base()
    print(f"site host: {host}   base path: {base}")

    missing: list[str] = []
    unprefixed: list[str] = []
    checked = 0

    for page in sorted(PUBLIC.rglob("*.html")):
        source = page.relative_to(PUBLIC).as_posix()
        for match in HREF.finditer(page.read_text(encoding="utf-8")):
            href = attr(match, "h").strip()
            if not href or href.startswith("#") or href.lower().startswith(SKIP_SCHEMES):
                continue
            path = unquote(urlsplit(href).path)
            if not path:
                continue
            if path.startswith("/"):
                if base != "/" and not path.startswith(base):
                    unprefixed.append(f"{source}: {href}")
                    continue
                rel = path[len(base):] if base != "/" else path[1:]
            else:
                rel = (Path(source).parent / path).as_posix()
            checked += 1
            if not resolves(rel):
                missing.append(f"{source}: {href}")

    print(f"internal links checked: {checked}")

    for entry in sorted(set(unprefixed)):
        print(f"UNPREFIXED {entry}", file=sys.stderr)
    for entry in sorted(set(missing)):
        print(f"MISSING    {entry}", file=sys.stderr)

    if not checked:
        print("FAIL: no internal links were examined at all", file=sys.stderr)
        return 1
    if missing or unprefixed:
        print(
            f"FAIL: {len(set(missing))} missing, {len(set(unprefixed))} missing the base path",
            file=sys.stderr,
        )
        return 1

    print("PASS: every internal link resolves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
