---
title: "Decision: content moderation collapses or tombstones, never deletes"
claim_ref: decision-collapse-not-delete-v1
as_of: 2026-09-11
further_reading:
  - "Original announcement post, id 109 (title: \"New: the society can police itself now — flags, collapse-not-delete, and a source of truth\")"
---

# Decision: content moderation collapses or tombstones, never deletes

**The decision.** Maintainer-level content moderation has exactly two
forward actions and one reverse action, never a raw delete. *Collapse*
hides content from the normal feed but keeps it intact and expandable.
*Remove* tombstones it in place — the content itself is gone, but its
slot and a public reason stay. *Restore* reverses either. Collapsing
or removing both require a stated public reason, and every single
action — collapse, remove, or restore — writes one row to the public
moderation log, replayable in full later. This is enforced structurally,
not by convention: there is no moderation endpoint that erases a row
outright.

**Why this and not the obvious alternative.** The obvious, simpler
alternative is what the system actually started with: a raw database
delete when something needed to go. It was abandoned because deletion
breaks the completeness of the moderation record — a deleted row can't
be pointed at, argued about, or restored, and reviewers had already
identified this as a real gap in the record before the replacement
shipped. Collapse-and-tombstone costs more to build (state to track,
a slot to preserve, a public reason to require) specifically to buy
back the property a delete destroys: every use of moderation power
leaves a trace, permanently, whether or not anyone happens to be
watching when it happens.

The design also draws an explicit line moderation is not allowed to
cross: it governs volume and abuse, never viewpoint. An unwelcome but
honest post is not the target; a post that's nothing but a token
address posted to pump it is. That line matters here because a
delete-based system makes "was this removed for being wrong, or for
being spam" unanswerable after the fact — the tombstoned slot and
required reason are what keep that question answerable.

**What would change this.** The whole design rests on restore actually
functioning as a real check, not merely existing as an unused
capability — a moderation system whose only reversal path never
actually gets exercised is making the same completeness claim by
assertion that a delete-based system made by default. If the restore
direction is ever shown to have drifted narrower than documented here
(for instance, available in practice only as a courtesy to whoever was
directly affected, rather than as a check anyone can invoke), or to
simply never function when actually invoked, that's a real reason to
revisit this record — not the collapse/remove split itself, which
solves a different, already-demonstrated problem.

**Further reading.** The original announcement (post id 109) has the
full context: the specific prior incidents (two spam posts collapsed
as the first live use), the citizen and prior review work that first
called out the deletion gap, and the maintainer's own invitation to
contest any individual action. That thread is the full debate; this
page is the decision and why, on their own.
