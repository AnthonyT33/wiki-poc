---
title: Freshness as a content contract, not a hash
claim_ref: freshness-as-content-contract-v1
as_of: 2026-09-11
related: [fingerprint-digest-necessity]
---

# Freshness as a content contract, not a hash

**Problem.** A document whose own storage stays byte-identical (same
hash, untouched) is not evidence the thing it *describes* is still
true. An unchanged hash proves only that nothing touched the document
— never that the world it describes hasn't moved underneath it.

**Repair.** Where a document's claims rest on an external, versioned
thing, encode that dependency explicitly and pin it to a checkable
state at verification time. A mechanism that re-resolves the
dependency's *current* state and flags drift makes staleness checkable
instead of assumed away.

**Environment.** Documentation, wikis, any cached summary of a live
external system.
