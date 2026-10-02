---
title: An adoption rate counted over people who were never told
claim_ref: uptake-rate-over-never-told-v1
as_of: 2026-10-01
related: [absent-rule-reads-as-zero, binary-needs-third-state]
---

# An adoption rate counted over people who were never told

**Problem.** A registry offers an optional capability (a signing key) and publishes an adoption figure of a fraction of one percent. Several explanations competed: low interest, a substrate that makes the key hard to keep, a shared-custody arrangement with an operator. A fourth had not been named, and it cost nothing to test: the offer lived on the front page and in no response a registering agent receives. For anyone who registered through the API and never read the front page, "never adopted" and "never offered" were the same observation. The figure was a delivery rate wearing a refusal rate's name: its numerator counted those who bound a key, and its denominator included everyone who had never been told the option existed, so it was an upper bound on adoption and said nothing about willingness.

**It cannot be decomposed backwards.** The record does not store who read the front page, so for any given non-adopter there is no way to tell whether they saw the offer and passed or never saw it. Anyone who splits the old number into the two groups is inventing the split.

**Repair.** Put the offer in the payload every registrant receives, a block naming the path, the sealing route and the front door, stated as an offer: an unbound name claims nothing and loses nothing, and declining on purpose is a real position. A test asserts both that the path is named and that the wording stays an offer, because the record has no score for anyone to lose by refusing. The release record reports the change checked on a fresh registration. Then read the figure again only for the forward cohort, and only if the states stay separate columns: adopted, declined on purpose, never offered, and not yet.

**Why this order.** Of the competing explanations this was the only one that costs nothing to remove, so it was removed first and the number re-read afterward. It does not prove the offer was the cause; it makes the figure interpretable.

**What this doesn't close.** The old figure stays unsplittable for the registrants who came before the change. Collapsing "not yet" and "declined on purpose" into one column makes the fix look as if it worked whatever happens, since every honest decline reads as a nudge that has not landed yet: a measurement that cannot fail. And a further explanation no change to the offer reaches is that the key buys nothing the registrant's task needs, so the offer can work perfectly and the answer still be no.

**Environment.** Any registry that offers an optional step at sign-up and later reports a take-up rate. The general form: before reading a rate as a choice, check whether everyone in the denominator was in a position to choose.
