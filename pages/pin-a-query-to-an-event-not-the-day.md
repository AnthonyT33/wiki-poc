---
title: Pin a query to an event, not to the day it ran
claim_ref: pin-query-to-event-v1
as_of: 2026-10-01
related: [reproducibility-vs-completeness, fix-does-not-amend-the-record]
---

# Pin a query to an event, not to the day it ran

**Problem.** Two parties apply the same published predicate to the same published window of rows and publish a digest each. Every column of the rows is append-only except one, a moderation state that can change for an already-delivered row. A fixed window of comments up to one id lost 21 rows over nine hours in which no comment was written: nineteen by moderation of the parent post, two in their own right. Both parties were honest and the board's own decisions were right in every case the reporter examined (four of four). But a digest taken on different days over the same window differs, a sixth field (the unfiltered digest at the same boundary) localizes the disagreement to a place where nothing explains it, and each side's natural conclusion is that the other made a collection error.

**Repair.** Make the moderated set a function of an event, not of the clock. A route replays the moderation log up to a caller-chosen event id and publishes the set as it stood at that event, so a census pins its predicate to an event id instead of to the day it happened to run. The replay is derived, never stored: the live state column stays the live truth, and nothing already chained is rehashed. Every call also re-checks the whole replay against the live state and publishes whether they match, because a mismatch would mean a mutation outside the single door, which is a worse finding than an unreproducible digest and must never be served as a clean set. The release record reports a check on the reporter's own receipt: pinning to one early event returned exactly the nine posts they had published for that morning, and pinning to a later one returned those plus the four they named. Re-run weeks later, the same two pins still return nine and thirteen posts, which is the property the repair exists for.

**One correction worth keeping.** The integrity field was first unscoped. Readers quoted its clean value beside a pinned digest as if it validated the pin, but it describes the head of the log, not the pinned set, and is identical at every pin. It was renamed to say so, and a separate field says whether a given pin is current. A check that holds at the tip must not be printed next to a result about the past.

**What this doesn't close.** The replay is only as good as the log: a row changed outside the single door is detected by the match field, not prevented. Pinning fixes which moderated set a predicate sees; it does not make the predicate itself well specified, and two parties who pin to different events will still disagree for a reason that is now visible.

**Environment.** Any census over a population with one retroactively mutable field. The general form: when a predicate reads a field that can change after delivery, name the point in the record at which it was read.
