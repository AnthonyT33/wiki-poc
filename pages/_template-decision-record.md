---
title: TEMPLATE — decision record
claim_ref: TEMPLATE
as_of: YYYY-MM-DD
further_reading: []
---

<!--
This is a template, not a page — the leading underscore keeps it out
of any generated index. Copy it, drop the underscore, fill every
section.

WHEN THIS SHAPE FITS: a real choice was made among genuine
alternatives, for reasons that are not obvious from the choice alone,
and a later reader (especially someone who wasn't there) could
reasonably ask "why not the other way?" without this page existing to
answer them. It does NOT fit a live, still-contested question, or a
finding about whether something shipped — those belong in discussion,
not here (see this repo's README, "Scope note").

WHAT MAKES THIS DIFFERENT FROM A TECHNICAL PATTERN PAGE: a pattern
page documents something true in general, verified across specimens.
A decision record documents one specific, local choice — it's fine,
even expected, for the same problem to have a different decision
record in a different system, because the deciding constraints
differed. Don't generalize a decision record into a pattern claim.

DO NOT INVENT THE RATIONALE. If the real reasoning behind a decision
isn't recoverable — nobody wrote it down, or it can't be reconstructed
with confidence — say that plainly rather than filling in something
plausible. A guessed rationale presented as fact is worse than no
record at all, because it looks authoritative and isn't.
-->

# TEMPLATE — decision record

**The decision.** State plainly what was chosen — the actual rule,
policy, or design, in enough detail that someone could implement or
verify it from this sentence alone.

**Why this and not the obvious alternative.** Name the alternative(s)
that a reasonable person would suggest first, and the specific
constraint, tradeoff, or prior incident that ruled each one out. This
is the section a Chesterton's-fence question is actually asking for —
if this section is thin, the record isn't done yet.

**What would change this.** Name the condition under which this
decision should genuinely be revisited — a specific fact, not "if
someone disagrees." If that condition is currently unknown or
unspecified, say so rather than leaving the section implying none
exists.

**Further reading.** Link the original discussion thread(s), if any,
for the full debate and dissenting views. This is supplementary — a
reader should not need to open it to understand the decision or the
rationale above; it's here for whoever wants the argument in full,
not as a substitute for this page's own content.
