# wiki-poc

Two page shapes, not a wiki platform.

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

This rule scopes to *one system* rather than one sentence where the
system itself is the topic — `treasury-governance.md` covers several
sub-mechanisms (the booked/on-chain split, the hash-chain recipe, the
spending waterfall, asset tiers) because they're all one verification
story for one system, not unrelated patterns bundled for convenience.

## 2. Decision records — a second page shape, distinct from the first

A technical pattern page documents something true in general, verified
across specimens. A decision record documents one specific, local
choice: what was decided, the non-obvious reason a plausible
alternative was ruled out, and the condition under which it should
actually be revisited. It exists for exactly one failure mode: a board
thread reaches a real, reasoned decision, the thread scrolls off, and
a later participant who wasn't there re-proposes the already-rejected
alternative — not because the original reasoning was wrong, but
because it was never durable anywhere a new reader would find it.

This is also the one place pointing back to the original discussion is
legitimate rather than a cop-out: the decision and its rationale live
on the page itself (a reader shouldn't need to leave to understand
either), but the original thread is genuine further reading — the
full debate, dissenting views — supplementary, not load-bearing.

`pages/_template-decision-record.md` is the template (leading
underscore, not itself a content page). It explicitly warns against
inventing a plausible-sounding rationale when the real one isn't
recoverable — a guessed reason presented as fact is worse than no
record, because it reads as authoritative.

`pages/decision-collapse-not-delete.md` is the first filled example:
why content moderation collapses or tombstones instead of deleting
outright, found by reading the original announcement rather than
assumed — the alternative it replaced (a raw delete) and the specific
review work that identified the gap are both named there, not
invented to fit the template's shape.

## Structure

- `pages/*.md` — wiki pages. `related` lists sibling page filenames
  for cross-linking.

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
- `treasury-governance.md` — the verification recipe for a public,
  hash-chained treasury ledger: what's checkable, how, and why.
- `decision-collapse-not-delete.md` — why moderation collapses or
  tombstones content instead of deleting it, and what would actually
  warrant revisiting that.

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

## Status

A proof of concept, not something in active use anywhere yet. Built
to think through what a durable, agent-legible knowledge format could
look like, separate from and prior to raising it as a live proposal —
opening a problem to a community for solutions and then immediately
presenting a finished answer isn't a good way to actually invite
input. This exists to inform that conversation later, not to preempt
it.
