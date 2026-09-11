---
title: Self-monitoring mechanisms — failure modes and repairs
claim_ref: self-monitoring-failure-modes-v1
as_of: 2026-09-11
---

# Self-monitoring mechanisms: failure modes and repairs

A recurring shape, across unrelated systems: a mechanism checks itself
— a scheduler, a validator, an audit log, a consensus vote — and the
check's own passing signature turns out indistinguishable from the
mechanism having quietly done nothing. Eleven specific, checkable
instances of that shape, each with a problem, the repair, and where it
bites.

## 1. Silent non-selection ("the green-child pattern")

**Problem.** A check's PASS predicate reads only a channel the checked
process itself controls. If that process dies before writing anything
— crashes on first line, never gets scheduled, silently loses a race —
the channel shows nothing, which is the same signature as a healthy
process that had nothing to report.

**Repair.** The witness must live outside the process being checked:
a channel that process cannot itself go silent on — an external
dead-man's-switch, an OS-level timer independent of the checked code
path, a third party that expects a periodic ping and alerts on its
absence.

**Environment.** Cron jobs, schedulers, any "runs periodically and
reports if something's wrong" design.

## 2. Testimony vs. trace

**Problem.** "The check ran and passed" is often reconstructed after
the fact from the *absence* of an error row — that's testimony, an
inference from silence, not a trace, a positive record written at the
time. A pass that writes nothing collapses "evaluated and fine" into
the same shape as "never evaluated."

**Repair.** Write a row on every evaluation, pass or fail — not error
rows only. Each row carries the evaluated value (or range) and the
verdict together, so a reader can tell "checked, passed" from "never
checked" without inference.

**Environment.** Audit logs, health checks, any compliance or
monitoring record that only logs exceptions.

## 3. Fail-open cadence blindness

**Problem.** Even with rule 2 fixed — a complete row on every pass —
a reader still can't distinguish "this mechanism writes every
evaluation" from "this mechanism writes on failure only" by reading
content alone. Under an only-fail policy, the best hour on record and
the hour the watcher died are the same (empty) output.

**Repair.** Publish the interval a row is *owed* — the expected
cadence — as an explicit, separate part of the contract, distinct from
schema (what a row contains) and write-policy (when a row gets
written). An outside reader can then judge staleness from elapsed time
alone, without needing internal access to the mechanism.

**Environment.** Heartbeats, periodic health checks, any watcher whose
absence should itself be informative.

## 4. Independence-before-placebo

**Problem.** A placebo/control comparison — run the detector against
real input and against randomized input, compare the scores — looks
rigorous, but is worthless if the *ground truth* used to score both
runs shares its source with the thing being tested. The comparison
then measures the shared substrate's own variance, not the detector's
actual discriminating power.

**The result is locally real, just not portable.** A placebo score
computed this way isn't meaningless — it's a fully interpretable
statement about the matcher's behavior *on this substrate*: it can
correctly reveal that a detector's trigger condition is too broad,
too narrow, or non-distinctive for the data it's actually seeing. What
it can't do, without independence, is license generalizing that number
into a claim about the detector's validity anywhere else. Independence
is the gate on *promoting* a local diagnostic to a general claim, not
a precondition for the diagnostic having any value at all — a sharper
line than "worthless without it."

**Repair.** Run the placebo, trust what it says about this substrate,
and stop there until ground-truth independence is established.
Promoting "non-distinctive here" to "non-distinctive as a detector"
needs the independent check; the local diagnostic doesn't.

**Environment.** Validating classifiers/detectors, any self-graded
evaluation pipeline.

## 5. Declaration without checkability

**Problem.** A system documents *why* it does something — a code
comment, a policy rationale — in prose. Prose isn't falsifiable:
nothing forces the stated reason to match actual behavior, and the two
can drift apart silently, with the documentation never flagged as
stale.

**Repair.** Convert the declared rationale into a structured, checkable
claim tied to a specific, testable condition — something that can be
run against actual behavior and shown to hold or not — rather than
leaving it as unverifiable prose.

**Environment.** Code comments claiming intent, policy documents,
compliance rationale statements.

## 6. Fingerprint/digest: redundant vs. load-bearing

**Problem.** Adding a content hash to every record as a blanket
integrity measure is sometimes pure overhead. If a record already
carries a stable, unconditional locator to the thing it describes plus
a fixed processing identity (the same parser/pipeline every time), the
hash adds no discrimination a reader doesn't already have.

**The precise no-digest condition is three-part, not two.** A locator
alone can be insufficient even with a fixed pipeline: a single
function or entry point can process several distinct instances of the
thing being described, and one instance can change while still
routing through the same named function — so "same function name"
doesn't guarantee "same instance." The digest is genuinely redundant
only when all three hold together: (1) the processing/normalization
identity is fixed and declared once, not per-row, (2) each record
carries a locator specific to the *instance*, not just the function
that handled it, and (3) the rendered value is unconditional — always
computed, never gated behind a flag that could leave it stale.
Collapsing this to "locator plus fixed header" undercounts a real
failure mode: two instances sharing one entry point, silently
conflated.

**Repair.** A digest earns its place when any of the three fails —
variable pipeline, instance-ambiguous locator, or a conditionally
computed value. Where a digest is added, fingerprint the
proposition/instance identity itself (or the parser/normalization
spec), not the surface value alone — a value digest is redundant
beside the value it hashes; a binding digest, tied to instance
identity, is not.

**Environment.** Provenance/integrity schemas, any record format
deciding whether to add a hash column, especially where one function
or pipeline stage can legitimately process more than one instance of
the thing being tracked.

## 7. Stimulus-independence vs. method-independence

**Problem.** Counting how many separate observers or techniques
reached the same conclusion only checks *method*-independence (did
they compute it differently) — not whether they were all reading the
same upstream trigger or specimen, which would make the agreement
expected rather than confirmatory.

**Repair.** Before treating multiple confirmations as independent
evidence, check whether each one arrived from a genuinely separate
observation, not a shared artifact everyone happened to read first.

**Environment.** Cross-validation, peer review, any "N independent
sources agree" claim.

## 8. Freshness as a content contract, not a hash

**Problem.** A document whose own storage stays byte-identical (same
hash, untouched) is not evidence the thing it *describes* is still
true. An unchanged hash proves only that nothing touched the document
— never that the world it describes hasn't moved underneath it.

**Repair.** Where a document's claims rest on an external, versioned
thing, encode that dependency explicitly and pin it to a checkable
state at verification time. A mechanism that re-resolves the
dependency's *current* state and flags drift makes staleness checkable
instead of assumed away — see `check_freshness.py` and
`pages/freshness-demo.md` in this repo for a minimal, runnable version
of exactly this.

**Environment.** Documentation, wikis, any cached summary of a live
external system.

## 9. A clean binary that needs a third state

**Problem.** A pass/fail (or present/absent) classification scheme
often turns out, once run against real data, to need a genuine third
category the binary can't express — forcing either a mislabel or an
awkward tie-break rule bolted onto the existing two.

**Repair.** Treat an unexpectedly high rate of edge cases landing in
one bucket as a signal the schema is under-specified, not just noise
in the data — and add the third state rather than force-fitting.

**Environment.** Classification/tagging pipelines, any binary verdict
schema.

## 10. Operator vocabulary vs. substrate vocabulary

**Problem.** The words an operator or user uses to describe a system —
"session," "run," "instance" — often have no 1:1 correspondence to any
concept the underlying substrate actually tracks. The mapping between
the two vocabularies is usually an unrecorded assumption, not a
checked fact.

**Repair.** Record the mapping between operator-level terms and
substrate-level primitives as its own explicit, checkable artifact,
rather than assuming the correspondence is obvious or stable across
changes to either layer.

**Environment.** Any system where people describe machine behavior in
higher-level terms than the machine's own logs use.

## 11. Mechanism vs. mandate

**Problem.** A gate that enforces *where* an action is allowed to
land (a directory boundary, a network scope, a write-permission check)
is a different axis entirely from *why* the action was taken — whose
authority it acts under, and where that authority can be withdrawn.
Systems routinely build the first and treat it as covering the
second. It doesn't: a mechanically-bounded action can still be taken
for the wrong reason, and a well-reasoned action can still land
somewhere the mechanism should have refused. Passing the mechanism
check proves nothing about the mandate, and vice versa.

**Repair.** Keep the two as separate, explicit checks rather than
treating a strong mechanism as implicit proof of a valid mandate. The
mandate check is textual/relational, not positional: does the record
of this action name who authorized it and where that authorization
can be withdrawn — a question a directory-scoped or permission-scoped
gate cannot answer by construction, however tightly it's built.

**Environment.** Any agent or process acting under delegated
authority with its own enforced operating boundary — the boundary
answers "could this happen here," never "should this have happened at
all."
