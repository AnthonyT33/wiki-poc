---
title: Independence-before-placebo
claim_ref: independence-before-placebo-v1
as_of: 2026-09-11
related: [stimulus-vs-method-independence]
---

# Independence-before-placebo

**Problem.** A placebo/control comparison — run a detector against
real input and against randomized input, compare the scores — looks
rigorous, but is worthless as evidence about the detector if the
*ground truth* used to score both runs shares its source with the
thing being tested. The comparison then measures the shared
substrate's own variance, not the detector's actual discriminating
power.

**The result is locally real, just not portable.** A placebo score
computed this way isn't meaningless — it's a fully interpretable
statement about the matcher's behavior *on this substrate*: it can
correctly reveal that a detector's trigger condition is too broad, too
narrow, or non-distinctive for the data it's actually seeing. What it
can't do, without independence, is license generalizing that number
into a claim about the detector's validity anywhere else. Independence
is the gate on *promoting* a local diagnostic to a general claim, not
a precondition for the diagnostic having any value at all.

**Repair.** Run the placebo, trust what it says about this substrate,
and stop there until ground-truth independence is established.
Promoting "non-distinctive here" to "non-distinctive as a detector"
needs the independent check; the local diagnostic doesn't.

**Environment.** Validating classifiers/detectors, any self-graded
evaluation pipeline.
