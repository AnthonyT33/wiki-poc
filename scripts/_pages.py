"""Shared frontmatter/body parsing for pages/*.md. Pure stdlib, no deps.

Only handles the single-line scalar fields every page actually uses
(title, claim_ref, as_of) -- list fields like `related` or
`further_reading` aren't needed by gen_index.py or search.py and
are left unparsed rather than adding YAML-list handling nothing here
uses.
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(REPO_ROOT, "pages")

_SCALAR_FIELD_RE = re.compile(r'^([a-z_]+):\s*(.*)$')


def _unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def parse_frontmatter(text):
    """Return (fields dict, body str). Skips multi-line list values."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    fields = {}
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
        m = _SCALAR_FIELD_RE.match(line)
        if m and not line.startswith((" ", "\t")):
            key, value = m.group(1), m.group(2)
            if value == "" or value.startswith("-"):
                continue  # multi-line list field (e.g. further_reading:) -- skip
            fields[key] = _unquote(value)
    if end is None:
        return {}, text
    body = "\n".join(lines[end + 1:])
    return fields, body


def iter_pages():
    """Yield (filename, fields dict, body str) for every real page.

    Skips files starting with `_` (templates, not content).
    """
    for name in sorted(os.listdir(PAGES_DIR)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        path = os.path.join(PAGES_DIR, name)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        fields, body = parse_frontmatter(text)
        yield name, fields, body
