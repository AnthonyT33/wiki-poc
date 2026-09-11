---
title: A clean binary that needs a third state
claim_ref: binary-needs-third-state-v1
as_of: 2026-09-11
related: []
---

# A clean binary that needs a third state

**Problem.** A pass/fail (or present/absent) classification scheme
often turns out, once run against real data, to need a genuine third
category the binary can't express — forcing either a mislabel or an
awkward tie-break rule bolted onto the existing two.

**Repair.** Treat an unexpectedly high rate of edge cases landing in
one bucket as a signal the schema is under-specified, not just noise
in the data — and add the third state rather than force-fitting
borderline cases into whichever of the two existing labels is less
wrong.

**Environment.** Classification/tagging pipelines, any binary verdict
schema applied to real, messy input for the first time.
