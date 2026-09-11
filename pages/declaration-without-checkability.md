---
title: Declaration without checkability
claim_ref: declaration-without-checkability-v1
as_of: 2026-09-11
related: [mechanism-vs-mandate]
---

# Declaration without checkability

**Problem.** A system documents *why* it does something — a code
comment, a policy rationale — in prose. Prose isn't falsifiable:
nothing forces the stated reason to match actual behavior, and the two
can drift apart silently, with the documentation never flagged as
stale because nothing ever checks it against reality.

**Repair.** Convert the declared rationale into a structured, checkable
claim tied to a specific, testable condition — something that can be
run against actual behavior and shown to hold or not — rather than
leaving it as unverifiable prose that only a human re-reading it can
judge, and only if they think to.

**Environment.** Code comments claiming intent, policy documents,
compliance rationale statements.
