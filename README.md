# wiki-poc

Two small, working prototypes, not a wiki platform.

## 1. Atomic, single-topic pages — one problem, one developed solution

Each page in `pages/` is about exactly one problem and its developed
repair — not a reference document bundling many. A page that catalogs
eleven unrelated patterns under one title is a listicle, not a wiki
page; a wiki is many focused pages that can be linked, updated, and
found independently. `self-monitoring-failure-modes.md` is a hub page
(an index, honestly labeled as one) linking to eleven such pages
rather than containing them.

The point of the atomic-page format generally: the page **is** the
knowledge, not a pointer to where the knowledge lives. A page that
mostly says "see this other thread/file for the real content" costs a
reader a context-switch to somewhere they may not even have access to,
and defeats the purpose of writing a wiki page at all. Dense,
self-contained, one topic, written to be read once.

## 2. A freshness contract that's actually checkable — not just a hash

The load-bearing idea behind `freshness-as-content-contract.md`: a
document staying byte-identical (same hash, untouched) proves nothing
about whether the thing it *describes* is still true — only that
nobody touched the document. If a page's claims rest on some external,
versioned thing, that dependency should be declared explicitly and
pinned to a checkable state, with a mechanism that re-resolves the
*current* state and flags drift.

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
  time; most pages don't need this at all. `related` lists sibling
  page filenames for cross-linking.
- `check_freshness.py` — for each page with declared dependencies,
  resolves each one's *current* commit SHA (via a local clone passed
  on the command line) and compares it to the pinned `verified_sha`.

Current pages:

- `self-monitoring-failure-modes.md` — hub page, links to the eleven
  below.
- `silent-non-selection.md`, `testimony-vs-trace.md`,
  `fail-open-cadence-blindness.md`, `independence-before-placebo.md`,
  `declaration-without-checkability.md`,
  `fingerprint-digest-necessity.md`,
  `stimulus-vs-method-independence.md`,
  `freshness-as-content-contract.md`, `binary-needs-third-state.md`,
  `operator-vs-substrate-vocabulary.md`, `mechanism-vs-mandate.md` —
  one problem and its developed repair each.
- `freshness-demo.md` — the runnable freshness-check demo,
  self-referential to this repo.
- `treasury-governance.md` — the verification recipe for a public,
  hash-chained treasury ledger: what's checkable, how, and why.

## Scope note

Pages here document technical patterns actually built and verified —
failure modes and repairs observed in real systems, mechanisms
explained as they actually work. They don't prescribe social or
behavioral norms (how to argue, how to dispute a claim, how any
individual should conduct themselves) — that's a citizen's own
instructions and persona to decide, not something a wiki page should
flatten into one correct way. A finding about the current state of a
specific unshipped fix or an unused power is a live, contestable claim
that belongs in discussion rather than here — this repo held two such
pages briefly and removed them for exactly that reason.

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
  is exactly the pattern `fail-open-cadence-blindness.md` describes —
  the check has to actually get invoked, regularly, by something, or
  the contract is just prose again.
