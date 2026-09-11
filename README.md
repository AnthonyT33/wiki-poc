# wiki-poc

Two small, working prototypes, not a wiki platform.

## 1. A reference-doc format for compressed, agent-legible knowledge

`pages/self-monitoring-failure-modes.md` distills a recurring pattern
observed across unrelated self-checking systems (schedulers,
validators, audit logs, consensus checks): a mechanism's own passing
signature turns out indistinguishable from it having quietly done
nothing. Eleven specific instances, each a Problem → Repair pair,
tagged with the environment it applies to.

The point of this format: the page **is** the knowledge, not a pointer
to where the knowledge lives. A page that mostly says "see this other
thread/file for the real content" costs a reader a context-switch to
somewhere they may not even have access to, and defeats the purpose of
writing a wiki page at all. Dense, self-contained, and written to be
read once — no external thread or private source required to trust or
use it.

## 2. A freshness contract that's actually checkable — not just a hash

The load-bearing idea from problem #8 in that page: a document staying
byte-identical (same hash, untouched) proves nothing about whether the
thing it *describes* is still true — only that nobody touched the
document. If a page's claims rest on some external, versioned thing,
that dependency should be declared explicitly and pinned to a
checkable state, with a mechanism that re-resolves the *current* state
and flags drift.

`check_freshness.py` implements the minimal version: a page's
frontmatter names a `(repo-key, path, pinned-sha)` triple; the script
resolves the current commit SHA for that path in a given local clone
and reports FRESH or STALE. `pages/freshness-demo.md` demonstrates it
against a file in *this same repo* — deliberately self-referential, so
the demo is checkable by anyone who clones this repo, with no access
to anything else required.

## Structure

- `pages/*.md` — wiki pages. Frontmatter may carry `depends_on`, a list
  of `{repo, path, verified_sha}` triples pinned at last-verification
  time. Pages that are self-contained knowledge (like #1 above) don't
  need this at all.
- `check_freshness.py` — for each page with declared dependencies,
  resolves each one's *current* commit SHA (via a local clone passed
  on the command line) and compares it to the pinned `verified_sha`.

Current pages:

- `self-monitoring-failure-modes.md` — eleven Problem → Repair entries
  on self-checking mechanisms whose passing signature is
  indistinguishable from doing nothing.
- `freshness-demo.md` — the runnable freshness-check demo, self-referential
  to this repo.
- `treasury-governance.md` — verification mechanics for a public,
  hash-chained treasury ledger: what's checkable, how, and why.
- `sybil-resistance-gap.md` — a case study in a decided, numbered fix
  where half the items silently never shipped, and how that stayed
  invisible until someone checked the live system against the decision.
- `restoration-power-audit.md` — an audit power with a perfect record
  of never having been used, and why that's genuinely ambiguous rather
  than reassuring.

## Try it

```
python3 check_freshness.py pages/ --repo this-repo=.
```

Run from the repo root. `pages/freshness-demo.md` depends on
`README.md` in `this-repo` — edit this file and re-run to see it flip
to STALE.

## Honest limits

- Single dependency type implemented: "a file in a git repo, pinned to
  a SHA." A live API response, a stated claim, or a moving consensus
  would each need a different resolver.
- The checker needs a local clone passed explicitly; it doesn't fetch
  anything itself.
- Nothing here runs on a schedule. A freshness checker nobody re-runs
  is exactly the fail-open cadence blindness described as problem #3
  in the reference doc — the check has to actually get invoked,
  regularly, by something, or the contract is just prose again.
