#!/usr/bin/env python3
"""
Walk wiki pages, compare each declared dependency's pinned SHA against
its current SHA in a local clone, report FRESH or STALE per page.

Usage:
    check_freshness.py <pages_dir> --repo <owner/name>=<local_clone_path> [--repo ...]

The pinned SHA is the last commit that touched the dependency's `path`
at verification time (git log -1 --format=%H -- <path>), not the repo's
HEAD -- an unrelated commit elsewhere in the dependency repo must not
flag a page as stale.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text):
    """Minimal YAML-subset parser -- just enough for this PoC's schema.
    Not a general YAML parser; do not extend without switching to a
    real one."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = {}
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("depends_on:"):
            deps = []
            i += 1
            while i < len(lines) and lines[i].startswith("  - "):
                dep = {}
                dep_line = lines[i][4:]
                key, _, val = dep_line.partition(":")
                dep[key.strip()] = val.strip()
                i += 1
                while i < len(lines) and lines[i].startswith("    "):
                    k, _, v = lines[i].strip().partition(":")
                    dep[k.strip()] = v.strip()
                    i += 1
                deps.append(dep)
            fm["depends_on"] = deps
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
        i += 1
    return fm


def current_sha(local_clone, path):
    result = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--", path],
        cwd=local_clone,
        capture_output=True,
        text=True,
        check=True,
    )
    sha = result.stdout.strip()
    if not sha:
        raise FileNotFoundError(f"no commit history for {path} in {local_clone}")
    return sha


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pages_dir")
    ap.add_argument(
        "--repo",
        action="append",
        default=[],
        metavar="OWNER/NAME=LOCAL_PATH",
        help="map a dependency repo to a local clone, e.g. "
        "owner/repo-name=/path/to/clone",
    )
    args = ap.parse_args()

    repo_map = {}
    for entry in args.repo:
        name, _, local_path = entry.partition("=")
        repo_map[name] = local_path

    pages = sorted(Path(args.pages_dir).glob("*.md"))
    if not pages:
        print(f"no pages found in {args.pages_dir}", file=sys.stderr)
        sys.exit(1)

    any_stale = False
    for page in pages:
        text = page.read_text()
        fm = parse_frontmatter(text)
        deps = fm.get("depends_on", [])
        if not deps:
            print(f"{page.name}: no dependencies declared (nothing to check)")
            continue

        page_stale = False
        for dep in deps:
            repo = dep.get("repo")
            path = dep.get("path")
            pinned = dep.get("verified_sha")
            if repo not in repo_map:
                print(f"{page.name}: SKIP -- no local clone given for {repo} "
                      f"(pass --repo {repo}=/path/to/clone)")
                continue
            try:
                actual = current_sha(repo_map[repo], path)
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                print(f"{page.name}: ERROR resolving {repo}:{path} -- {e}")
                page_stale = True
                continue
            if actual != pinned:
                print(f"{page.name}: STALE -- {repo}:{path} moved "
                      f"{pinned[:12]} -> {actual[:12]}")
                page_stale = True
            else:
                print(f"{page.name}: fresh on {repo}:{path} ({pinned[:12]})")

        if page_stale:
            any_stale = True

    sys.exit(1 if any_stale else 0)


if __name__ == "__main__":
    main()
