---
title: An event-driven count hides the rule that never fired
claim_ref: absent-rule-reads-as-zero-v1
as_of: 2026-09-30
related: [silent-non-selection, testimony-vs-trace]
---

# An event-driven count hides the rule that never fired

**Problem.** An endpoint reports how many writes each screening rule
has refused, built by grouping the refusal events by rule. A rule that
has never refused anything has no events, so it does not appear at all.
Absent and zero then read the same. Worse, two readings taken a day
apart cannot be compared row by row: a rule that was always in the
screen and fired for the first time looks identical, in the payload, to
a rule added yesterday that fired once. The answer exists, but in the
source history, which the payload does not point at.

The sharpest case is the rule whose published meaning is "the screen
itself failed and the write published unscreened." Its absence reads as
the reassuring answer. It is wired, but the insert that records it sits
inside a deliberately bare error handler, because that rule names the
state in which writing is already failing. So the absence proves that no
row was recorded, not that the branch never ran. It is also silent about
the period before the wiring landed, when the failure branch returned
quietly.

**Repair.** Serve the whole roster, zeros included, so that a rule that
has never fired reads 0 and an absent rule means there is no such rule.
Each row carries a `retired` flag, so removal is also visible. Four
details decided whether the fix was honest:

- Derive the roster from the same source the screen itself uses.
  Otherwise the roster and the screen drift apart and the field lies in a
  new way.
- Add a secondary sort key once zeros make ties common.
- Keep separate rosters for rules that can refuse and rules that can
  never gate. Rules filtered out before the refusal step can never
  produce a row, and listing them at 0 would claim a capability the
  endpoint's own description denies and put two meanings of zero in one
  array.
- Review found the same defect in a neighbouring counter and fixed it in
  the same change.

A denominator (how many writes were screened) is a separate request. Zeros
fix the roster and a denominator fixes the scale, and neither substitutes
for the other.

**What this doesn't close.** Zero on the failure rule still means "no row
was recorded," not "never ran," because the recording is best-effort by
design. The count can be short while the action is not, and that fact
lives in the source, not in the payload.

**Environment.** Any summary endpoint or dashboard that counts events per
category with a grouping query, where a category with no events disappears.
Read against the live payload on 2026-09-30: the roster serves every rule
with a count and a `retired` flag, and the failure rule reads 0.
