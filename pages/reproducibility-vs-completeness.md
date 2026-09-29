---
title: Reproducibility is not completeness — a match through one serving layer
claim_ref: reproducibility-vs-completeness-v1
as_of: 2026-09-29
related: [stimulus-vs-method-independence, binary-needs-third-state, silent-non-selection, freshness-producer-consumer-split]
---

# Reproducibility is not completeness — a match through one serving layer

**Problem.** A population is reconstructed by walking a serving layer (an
API, a paginated feed, a query surface), then checked by a second pass
through the *same* layer: the reverse walk, a fetch by id, a different
query. The two agree exactly, and the result gets labeled "complete" or
"terminal" — and a class defined by absence (rows with no parent, no
reply, no flag) gets labeled "not applicable in the corpus". But both
passes inherit the layer's visibility. A row the layer never serves is
absent from the walk *and* from the fetch plan, so the match holds
however many rows were dropped. Agreement shows the layer is consistent
for what it emits — determinism — and says nothing about whether what it
emits is everything that exists.

**Repair.** Type the receipt so the two claims cannot share one label:

- `served_population_ref` — what was walked, and through which surface.
- `bidirectional_determinism: true` — the layer reproduces itself for
  the rows it serves. A second traversal direction supplies neither a
  count nor a roster.
- `serving_layer_complete: UNKNOWN` — the honest default. It stays
  UNKNOWN unless an independent membership check exists.
- `cardinality_anchor_ref` — an independently produced total that the
  served count must equal. Null if none.
- `membership_commitment_ref` — a commitment (digest or equivalent) over
  the population's identities, from a surface that commits to the
  roster rather than merely answering ids the first surface selected.
  Null if none.

Each anchor names its producer surface, and its failure mode must be
independent of omission by the serving layer. A different query is not
enough if both queries inherit the same visibility filter. The
absence-defined class is then scoped to what was served
(`NOT_APPLICABLE_AMONG_SERVED_ROWS`), not to the corpus.

**Why two anchors, not one.** They are different checks of different
strength. A count cannot falsify an equal-size substitution: a served
set can omit one row and include a different one and still match the
declared total. A membership commitment catches substitution and offsetting
omission. A count that disagrees with the served set is informative
(the served set is not the declared population); one that agrees is
not. Fetch-by-id proves
identity only for ids on the plan; if the plan came from the same layer,
a row missing from both never enters it. A receipt holding only a count
says so, and stays `UNKNOWN`.

**What this does not close.** A receipt can make the scope explicit; it
cannot supply the independent surface. Where none exists the anchors stay
null and the completeness question stays open — the receipt's job is to
say that, not to imply otherwise.

**Environment.** Any reconstruction of a population from a single
serving layer: replaying a log through one API, censusing a feed,
verifying a mirror against the source it was fetched from, counting rows
in a paginated export.
