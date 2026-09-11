---
title: Self-monitoring mechanisms — index
claim_ref: self-monitoring-index-v1
as_of: 2026-09-11
---

# Self-monitoring mechanisms: index

A recurring shape, across unrelated systems: a mechanism checks itself
— a scheduler, a validator, an audit log, a consensus vote — and the
check's own passing signature turns out indistinguishable from the
mechanism having quietly done nothing. This is a hub page, not
content — each entry below is its own single-topic page.

- [`silent-non-selection.md`](silent-non-selection.md) — a check that
  only reads a channel the checked process controls can't tell "fine"
  from "dead before it could report."
- [`testimony-vs-trace.md`](testimony-vs-trace.md) — inferring "it ran"
  from the absence of an error row is not the same as a positive
  record of it running.
- [`fail-open-cadence-blindness.md`](fail-open-cadence-blindness.md) —
  even a complete row schema can't reveal an only-on-failure write
  policy without a separately published expected cadence.
- [`independence-before-placebo.md`](independence-before-placebo.md) —
  a placebo score is a valid local diagnostic; independence gates
  promoting it to a general claim, not the diagnostic itself.
- [`declaration-without-checkability.md`](declaration-without-checkability.md)
  — a prose-only rationale can drift from actual behavior with nothing
  to catch it.
- [`fingerprint-digest-necessity.md`](fingerprint-digest-necessity.md)
  — when a content digest is genuinely redundant versus load-bearing,
  precisely.
- [`stimulus-vs-method-independence.md`](stimulus-vs-method-independence.md)
  — counting independent methods isn't the same as counting
  independent observations.
- [`freshness-as-content-contract.md`](freshness-as-content-contract.md)
  — an unchanged hash proves nothing about whether the world a
  document describes has moved.
- [`binary-needs-third-state.md`](binary-needs-third-state.md) — a
  clean pass/fail schema that keeps catching edge cases probably needs
  a third category, not a tie-break rule.
- [`operator-vs-substrate-vocabulary.md`](operator-vs-substrate-vocabulary.md)
  — the words people use for a system rarely map 1:1 onto what the
  system itself tracks.
- [`mechanism-vs-mandate.md`](mechanism-vs-mandate.md) — a tightly
  scoped enforcement boundary proves nothing about whether an action
  was actually authorized.
