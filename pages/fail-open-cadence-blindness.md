---
title: Fail-open cadence blindness
claim_ref: fail-open-cadence-blindness-v1
as_of: 2026-09-11
related: [testimony-vs-trace, silent-non-selection]
---

# Fail-open cadence blindness

**Problem.** Even with a complete row written on every pass (see
`testimony-vs-trace.md`), a reader still can't distinguish "this
mechanism writes every evaluation" from "this mechanism writes on
failure only" by reading the record's content alone. Under an
only-fail write policy, the best hour on record and the hour the
watcher quietly died produce the exact same output: nothing.

**Repair.** Publish the interval a row is *owed* — the expected
cadence — as an explicit, separate part of the contract, distinct from
schema (what a row contains) and write-policy (when a row gets
written). Given that published interval, an outside reader can judge
staleness purely from elapsed time, without needing any internal
access to the mechanism itself.

**Environment.** Heartbeats, periodic health checks, any watcher whose
prolonged absence should itself be informative rather than silently
ambiguous.
