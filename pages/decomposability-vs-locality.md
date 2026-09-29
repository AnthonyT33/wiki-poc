---
title: Decomposability, locality, and append-stability are separate properties
claim_ref: decomposability-vs-locality-v1
as_of: 2026-09-29
related: [freshness-producer-consumer-split, reproducibility-vs-completeness]
---

# Decomposability, locality, and append-stability are separate properties

**Problem.** A delta check over an append-only corpus — re-verify only
what changed, not the whole dataset — usually gets one loose label
("row-local," "per-row," "unary") meaning "cheap and independent." That
label hides three separate properties, and a cost claim goes wrong when
any one of them is assumed instead of stated. The classic slip: a check
looks per-row but resolves itself by reading a *different* row's fields
— an external lookup, not a self-contained fact.

**Repair.** State each property on its own.

- **Decomposability** — is checking row X independent of checking row Y?
  If so, N new rows are N independent checks, not one check whose cost
  grows with N.
- **Locality** — how much data outside row X does X's check read? None
  (self-contained, "row-local"); a small fixed-size neighborhood that does
  not grow with the corpus ("bounded"); or a neighborhood whose size is
  not fixed, up to the whole existing population for that row's subject
  ("unbounded").
- **Append-stability** — once row X has been checked, can a later append
  change what X's check read? If it can, old results go stale and old rows
  need re-checking; the delta shortcut fails however decomposable or local
  the check is.

"We only need to re-check the N new rows" is a cost claim that needs all
three: independent checks, a bounded neighborhood each, and neighborhoods
that no later append can change. Each can fail alone. A check can be
decomposable with an unbounded neighborhood — for example, walking a
row's ancestry to the root: independent per row and parallelizable, but
each check's size varies with depth, so it is not cheap in the fixed-size
sense. And a check against the existing corpus state for a subject fails
on every count: it is not independent of that state, its neighborhood is
the whole existing set for the subject, and that set grows with every
append. There the delta shortcut is unavailable, and a re-walk is the
honest cost.

**The resulting count is a bound, not a value.** A decomposable, bounded,
append-stable check over N new rows costs at most N neighborhoods — not
exactly N. Two new rows that share a lookup target need one lookup
between them, so the actual cost is the number of distinct targets:
O(distinct targets), bounded by O(new rows). Budget for the worst case;
don't expect it.

**Environment.** Incremental/delta verification over an append-only
corpus, any "we only need to re-check what changed" cost claim, cache
invalidation reasoning, streaming validators over growing datasets.
