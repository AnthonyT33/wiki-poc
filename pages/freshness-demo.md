---
title: Freshness-check demo
claim_ref: freshness-demo-v1
last_verified: 2026-09-11
depends_on:
  - repo: this-repo
    path: README.md
    verified_sha: 7f38708f97cb5ec5a9f0ff12adc8318df9605c00
---

# Freshness-check demo

This page exists to be checked, not read for content. It declares one
dependency: `README.md` in `this-repo`, pinned to the commit that was
current when this page was written.

Run from the repo root:

```
python3 check_freshness.py pages/ --repo this-repo=.
```

Right now it reports FRESH. Edit `README.md` (any change, even
whitespace) and commit it, then re-run — this page will report STALE,
because the file it depends on moved and this page's pin didn't. That
divergence is the entire mechanism problem #8 in
`self-monitoring-failure-modes.md` describes: this page's own hash
staying unchanged would prove nothing about whether `README.md` is
still what it was pinned against. The dependency pin is what makes
that checkable instead of assumed.
