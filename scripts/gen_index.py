#!/usr/bin/env python3
"""Print an index of pages/*.md, generated fresh from frontmatter.

Usage:
    python scripts/gen_index.py

Deliberately not committed as a static INDEX.md: a hand- or once-
generated file goes stale the moment a page is added, renamed, or
removed, and nothing forces it to be regenerated. Running this script
is the index -- it can't drift from the actual page set because it
reads that set directly, every time.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _pages  # noqa: E402


def main():
    rows = []
    for name, fields, _body in _pages.iter_pages():
        title = fields.get("title", "(no title)")
        claim_ref = fields.get("claim_ref", "")
        rows.append((title, name, claim_ref))

    rows.sort(key=lambda r: r[0].lower())

    width = max((len(t) for t, _, _ in rows), default=0)
    for title, name, claim_ref in rows:
        print(f"{title.ljust(width)}  pages/{name}  [{claim_ref}]")

    print(f"\n{len(rows)} pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
