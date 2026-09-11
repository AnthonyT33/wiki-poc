---
title: Testimony vs. trace
claim_ref: testimony-vs-trace-v1
as_of: 2026-09-11
related: [silent-non-selection, fail-open-cadence-blindness]
---

# Testimony vs. trace

**Problem.** "The check ran and passed" is often reconstructed after
the fact from the *absence* of an error row — that's testimony, an
inference from silence, not a trace, a positive record written at the
time the check actually ran. A pass that writes nothing collapses two
very different histories — "evaluated and fine" and "never evaluated
at all" — into the same empty shape, and nothing in the record can
tell them apart later.

**Repair.** Write a row on every evaluation, pass or fail — not error
rows only. Each row carries the evaluated value (or range) and the
verdict together, so a reader can tell "checked, passed" from "never
checked" by reading the record directly, without inferring anything
from what's missing.

**Environment.** Audit logs, health checks, any compliance or
monitoring record that by convention only logs exceptions.
