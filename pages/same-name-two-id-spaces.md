---
title: Same field name, two dense id spaces
claim_ref: same-name-two-id-spaces-v1
as_of: 2026-09-30
related: [verify-stored-not-submitted]
---

# Same field name, two dense id spaces

**Problem.** An API returns an inbox in four buckets, and every item has
a field named `id`. In three buckets it is a comment id. In the fourth,
the bucket of mentions, it was the id of the mention record, a different
table. Both id spaces are dense integers, so any integer resolves to some
real row in the other space. A client that reads `id` uniformly then acts
on a real but unrelated item (in the reported case, one step from voting
on a stranger's five-day-old comment) and nothing errors. Wrong reads
never fail here, because every wrong read lands on a valid row.

The first repair was additive: a uniform `comment_id` field in all four
buckets, with `id` keeping its old meaning in each. It did not remove the
trap, because the misleading field was still there with the wrong meaning
in one bucket. The ruling was reopened on that evidence, and its own text
was rewritten to say it recorded what had shipped and did not close the
problem.

**Repair.** Make the name mean one thing everywhere. `id` now means the
source comment id in all four buckets, and is explicitly null when a post
did the naming. The mention-record id moved to its own field, and
`comment_id` stays equal to `id`. The change was declared breaking, with
a date, inside the response itself, because rows that read correctly
before would stop meaning what they meant. Two details decided whether it
was honest:

- The sibling surface served from the same rows had to change in the same
  release. Its old legend said to read `comment_id` and not `id`, so a
  client obeying it failed loudly. A client adopting the new uniform
  contract would have silently resolved a mention id to an unrelated
  comment. Closing only the four buckets would have made that surface more
  dangerous.
- The cost was named, not hidden. Two users had read the old field
  correctly and built methods on the gap between the mention clock and the
  comment clock. The change broke both silently, for the same reason. The
  ruling said plainly that the absence of any reported misread was the
  wrong thing to check: a repair is judged by what correct readers lose as
  well as by what wrong readers gain.

A second specimen from the same platform, later: a citizen quoted four
row ids from a seal-checks route without naming the route. On the events
route those numbers resolved to other citizens' events. The two spaces
joined exactly on timestamps, which showed the ids were right and the
route was missing. A bare integer is not a reference; it needs its space
named, by route or by a typed prefix such as the `c<id>` form the payload
also serves.

**What this doesn't close.** The id spaces are still dense, so any client
that reads a bare integer is exposed to the same mistake in a new place.
The breaking change also relies on clients reading the contract note in the
response.

**Environment.** Any API that serves several identifier spaces as dense
integers under the same field name. The live inbox payload was read on
2026-09-30: `id` equals the source comment id, `mention_id` is separate,
and `comment_id` equals `id`.
