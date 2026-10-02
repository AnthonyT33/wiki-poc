---
title: A field that echoes the request cannot disclose a fallback
claim_ref: echo-field-hides-fallback-v1
as_of: 2026-10-02
related: [declaration-without-checkability, fail-open-cadence-blindness]
---

# A field that echoes the request cannot disclose a fallback

**Problem.** A verification route scopes a walk by a cursor the caller sends, and reports in a field named like a landing point the cursor that was sent. When the cursor names a real row, the echo and the landing point are the same number, so nothing looks wrong. When the cursor is past the end of the chain, the route falls back to the tip, and the field names a row that does not exist (the report that opened the case sent 999999 to a chain of 730 rows) beside a status that says the lookup came up empty. The field a reader takes for "where the anchor landed" cannot show that it fell back. The equality holds on every legitimately anchored read, which is exactly why the divergence went unseen.

It was not simply a bug. The field did what its documentation said: it names the anchor that scoped the windowed counts. Its name and position invited a reading as the comparand, and the comparand was a second anchor in the same response, the greatest sealed row at or before the cursor. The case for acting was that one root had now produced two specimens with opposite signs: a cursor of zero with a true head answered "mismatch" on a position the caller never meant, and a past-the-end cursor answered a vacuous "true". The first had been fixed in the payload, by giving the witness its own comparand. The second had been answered in prose, and only the payload fix had removed its class.

**Repair.** Put the resolution in the response. The row the lookup actually landed on is a field of its own, and a second field states whether that row equals the one asked for, so a checker can tell from the payload alone whether the anchor resolved where it asked. Before this, the resolved row was reachable only to a caller who also supplied the witness hash it was trying to obtain. The echo field keeps its own job of scoping the counts. The route's own words for the principle: a field that echoes the request agrees with the world until the moment it matters. At the time of writing, a past-the-end cursor returns the echoed number in the old field, the tip row in the resolved field, and false in the equality field; a cursor on a real row returns the same number in both and true.

**What this doesn't close.** A neighbouring question from the same discussion, whether the match flag should be null instead of true when the status is empty, was not settled by changing the payload. The route answers it with a rule in its prose: it lists the statuses on which the flag carries no information. That is the same substitution of a note for a field that this repair removed for the landing point, one status over. And a checker that only runs normal cursors will never see the echo and the landing point disagree.

**Environment.** Any interface where a response repeats a request parameter in a field whose name suggests a result. The general form: when a field's value is supplied by the caller, it can agree with the world in every ordinary case, so give the value the system found its own field and state the equality in the response.
