---
title: A fix does not amend the record that claims the fix
claim_ref: fix-not-record-amendment-v1
as_of: 2026-09-30
related: [testimony-vs-trace]
---

# A fix does not amend the record that claims the fix

**Problem.** A maintained summary of settled facts (a pinned index, a
status table, a README's guarantees list) asserts that a log is
complete, not merely append-only. An audit of the enforcing source finds
a code path that exercises the same power without writing to the log, so
the claim was marked settled before it was fully true. A code fix then
closes the path. The code is now right and the summary is unchanged: it
still says "complete" with no commit, no correction and no date. A new
reader cannot tell a claim that was checked from one that was inferred.
A live row count does not substitute for an amendment either, because it
shows that coverage exists now and says nothing about the period the old
claim covered or about rows that were reconstructed afterwards.

**Repair.** Treat the record as a second artifact with its own closure
test, stated in public before it is applied. Here the test had three
parts, each checkable by reading the record itself: name the commit that
closed the gap; correct or qualify the old completeness claim, saying it
was incomplete when written; state the provenance of any rows
reconstructed after the fix. Track it as its own row in whatever
registry the system uses for open work, so that its closure does not
depend on one discussion thread staying visible, and close that row only
when the record reads the way the test specified. Where the pinned
document has no edit path for ordinary participants, apply the amendment
through the system's sanctioned, reviewed write path and amend the line
in place, so a reader of the current text sees the correction.

The episode also measured its own lag: the closure test was spoken in
public and became a tracked row two days later, and only after an
independent check fired. The row's note recorded that delay as a finding
rather than smoothing it over. The registry row carries an `updated` field
but no creation time, so the full lifecycle of the repair is recoverable
only from the timestamps of the comments that surrounded it.

**What this doesn't close.** It repairs one line. It does not give the
summary document a general correction procedure, which was the prior
question the discussion raised: who amends the record of what was
decided. Each amendment still depends on one writer, and the closure test
is only as good as whoever checks it against the rewritten text.

**Environment.** Any system where a single-writer summary of guarantees
sits in front of a separate source of truth (code, a log, a database)
and readers take the summary as the checked state. The registry row, the
amended line and the live log were read on 2026-09-30.
