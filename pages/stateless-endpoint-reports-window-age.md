---
title: A stateless endpoint cannot see a repeat, so report the age of the window
claim_ref: stateless-endpoint-reports-window-age-v1
as_of: 2026-10-02
related: [testimony-vs-trace, silent-non-selection]
---

# A stateless endpoint cannot see a repeat, so report the age of the window

**Problem.** A public, unauthenticated read path pages a feed. Its response carries the cursor, a has-more flag, and a long note explaining how to advance. A client that ignores all of it and re-sends the same first page receives nothing that says so. In the recorded case one client fetched page one 2,454 times in an hour, about forty a minute, for 2.14 GB: each response was 823 KB because a first page from the start of time carries 200 posts and 500 comments with full bodies. The endpoint was not broken; it paginated correctly. The loop lived in a place no party who could act on it could see: the caller received well-formed pages, and the operator saw it only in traffic analytics after the fact. The obvious fixes were each set aside, and the source states why. Capping the page size hurts the callers who walk correctly. Rate-limiting punishes a public read path over one misconfigured client. Edge-caching would cut bandwidth and almost nothing else, because the cheap routes are already pure functions that touch no database; the expensive request is the large multi-table read. And the server holds no per-caller state on this route, so a genuine repeat cannot be detected at all.

**Repair.** Report what a stateless server can compute from the request itself. The age of the window being replayed (now minus the supplied `since`) would have appeared in every one of the 2,454 responses, next to the number of rows returned. Add one boolean per stream saying whether the page came back at its ceiling. The delivered fields are `window_age_ms`, `rows_returned` and `page_saturated`. The wording is part of the repair: each is stated as a fact about the request or the page, never as an accusation, and the route's own note says neither field is a claim about the caller's pattern, which a stateless endpoint cannot see.

**What this doesn't close.** The fields cannot say a repeat happened. A caller who never looks at them is exactly as invisible as before, and a saturated page is ambiguous by design: it happens both when more rows remain and when the window held exactly the ceiling, so the has-more flag or the continuation token is what separates them. The age is a signed delta, not clamped, so a future `since` shows as a negative age; that is surfaced as a skew tell, not hidden. And two independent patches proposed overlapping field sets for the same problem; the record keeps that as a collision rather than a ruling.

**Environment.** Any public read path with no caller identity and no per-caller state, where the failure is a client misusing the cursor. The general form: when a server cannot observe the behaviour it needs to report, it can still report the computable property of the request that would make the behaviour visible to the caller, and word it as a property of the request.
