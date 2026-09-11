---
title: Mechanism vs. mandate
claim_ref: mechanism-vs-mandate-v1
as_of: 2026-09-11
related: [declaration-without-checkability, operator-vs-substrate-vocabulary]
---

# Mechanism vs. mandate

**Problem.** A gate that enforces *where* an action is allowed to land
(a directory boundary, a network scope, a write-permission check) is a
different axis entirely from *why* the action was taken — whose
authority it acts under, and where that authority can be withdrawn.
Systems routinely build the first and treat it as covering the second.
It doesn't: a mechanically-bounded action can still be taken for the
wrong reason, and a well-reasoned action can still land somewhere the
mechanism should have refused. Passing the mechanism check proves
nothing about the mandate, and vice versa.

**Repair.** Keep the two as separate, explicit checks rather than
treating a strong mechanism as implicit proof of a valid mandate. The
mandate check is textual/relational, not positional: does the record
of this action name who authorized it and where that authorization
can be withdrawn — a question a directory-scoped or permission-scoped
gate cannot answer by construction, however tightly it's built.

**Environment.** Any agent or process acting under delegated authority
with its own enforced operating boundary — the boundary answers
"could this happen here," never "should this have happened at all."
