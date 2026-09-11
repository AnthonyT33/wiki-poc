---
title: Operator vocabulary vs. substrate vocabulary
claim_ref: operator-vs-substrate-vocabulary-v1
as_of: 2026-09-11
related: [mechanism-vs-mandate]
---

# Operator vocabulary vs. substrate vocabulary

**Problem.** The words an operator or user uses to describe a system —
"session," "run," "instance" — often have no 1:1 correspondence to any
concept the underlying substrate actually tracks. The mapping between
the two vocabularies is usually an unrecorded assumption, not a
checked fact, and can silently stop holding when either layer changes.

**Repair.** Record the mapping between operator-level terms and
substrate-level primitives as its own explicit, checkable artifact,
rather than assuming the correspondence is obvious or stable across
changes to either layer.

**Environment.** Any system where people describe machine behavior in
higher-level terms than the machine's own logs use.
