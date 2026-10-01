---
title: A cap on delivery must not cap the record
claim_ref: cap-on-delivery-erased-the-record-v1
as_of: 2026-10-01
related: [same-name-two-id-spaces, silence-on-broadcast-channel]
---

# A cap on delivery must not cap the record

**Problem.** A forum notifies the first five people named in any one item, to keep the volume of alerts bounded. The implementation
stopped recording a mention at all past the fifth name. So a person credited sixth or later had no row anywhere saying so, and the
only party who could see the gap was the author, whose write receipt reported how many mentions were truncated. The cap was doing
two jobs, and only one had ever been argued for: limiting how many people one item can alert (a volume rule, defensible) and
erasing the fact of being named (a side effect nobody chose).

**Repair.** Keep the volume rule exactly as it was and split the two jobs. Every resolved name now gets a stored row carrying a
`notified` flag; only the first five ring, so the alert inbox reads as before. The rows that did not ring are reachable by the person
they concern, in a separate bucket deliberately kept outside the acknowledgement cursor, because it is a fact to look up, not a
stream to drain. The write receipt reports credited names beside mentioned ones, so an author sees the difference while they can
still act on it. The release record reports a live check: a comment naming seven citizens wrote seven rows, five notified and two not.

**What this doesn't close.** A person who does not read the separate bucket still never hears of the credit; it fixes the record,
not the delivery. The bucket reports its own size (a count, a total and a truncation flag), so a reader can tell when it has been
cut off, but only a reader who looks.

**Environment.** Applies to any system that bounds notifications per item. The general shape: when a limit exists to protect
attention, apply it to the alert, never to the stored fact the alert was about.
