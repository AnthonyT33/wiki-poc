---
title: Freshness needs two identities, not one
claim_ref: freshness-producer-consumer-split-v1
as_of: 2026-09-13
related: [freshness-as-content-contract, fingerprint-digest-necessity]
---

# Freshness needs two identities, not one

**Problem.** A single declared freshness rule (a producer-set max age
or expiry window) lets a receipt grade itself against staleness —
`CURRENT_WITHIN_DECLARED_WINDOW` vs. `EXPIRED` — but that one field
conflates two different questions: did the producer follow a rule it
fixed in advance, and is the result fit for a particular consumer's
use right now. Collapsing both into one identity creates a silent
promotion risk: a mechanically green freshness status gets read as
"safe to rely on," even though the producer's declared window and the
consumer's actual tolerance are unrelated numbers that happen to share
a field.

**Repair.** Split freshness into two independent identities.
`producer_freshness_policy_ref` + `status_under_producer_policy` audits
only whether the producer followed its own declared rule — unchanged
from a single-identity design. `consumer_required_max_age` +
`status_for_this_use` is new: the reader's own threshold, populated
explicitly rather than silently inherited from the producer's number.
A consumer who never populates the second pair gets an honest
`UNKNOWN`, not a borrowed answer to a question the receipt never
addressed.

**What the split does not close, correctly.** Whether the consumer's
own required threshold is itself a *reasonable* one for the claim at
hand is a domain judgment, not a receipt property. No field can
answer that without reintroducing self-certification one level up —
the mechanism's job ends at making both claims explicit and checkable,
not at approving either of them.

**Environment.** Any system where a producer publishes a value bound
to an as-of timestamp or generator revision — a cache, a snapshot, a
scraped record, a computed report — and different downstream
consumers have different tolerance for how stale that value may be
before it stops being useful to them.
