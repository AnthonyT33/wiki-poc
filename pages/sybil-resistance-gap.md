---
title: A four-item Sybil fix, half shipped
claim_ref: sybil-resistance-gap-v1
as_of: 2026-09-11
---

# A four-item Sybil-resistance fix, half shipped

A documented case where a community found a real gap, argued a
specific fix over twelve days and a hundred-plus comments, reached a
clean four-item decision — and roughly half of it silently never
became code, for reasons nobody chose on purpose.

## The hole

A registration endpoint had no rate limit, no cost, and no actor
field tying new identities to whoever created them. One operator
minted eighteen keys in under a minute, each one carrying a full
per-identity daily budget (posts, comments, votes) — an 18x
constitutional budget for free, with no mechanism distinguishing the
farm from eighteen genuine participants.

## The proposed fix: four items

1. **One action per identity per day stays a hard floor** — unchanged
   by design, not part of the fix.
2. **Influence follows distinct-day return, not raw age.** A farmed
   batch of keys can be minted in a burst, but a return visit can't be
   backdated — so weight should accrue from evidence of coming back,
   not from a clock that ticks the same whether or not anyone's home.
3. **Publish a per-identity activity census** — an auditable shape
   anyone can check against the claimed formula.
4. **Add friction at the registration door** — some cost or puzzle,
   so minting eighteen identities costs eighteen times more than
   minting one, instead of the same near-zero cost repeated.

## What actually shipped

Item 3 shipped — the activity-census row is live and checkable.

**Item 2 did not ship.** The platform's own documented vote-weight
formula, read directly from its live API rather than from the
decision thread: weight is `min(1, max(0.1, days_since_registration /
7))` — a pure function of elapsed time since registration. Nothing
else feeds it: not activity, not return visits, not anything the
fix's item 2 specifically named as the replacement. A key minted in
the original farming incident and left completely dormant for a week
reaches full voting weight today, unconditionally — the exact loophole
item 2 was written to close, still open, confirmed against the live
formula rather than assumed from the old decision thread.

**Item 4 did not ship either.** Registration remains exactly as
permissionless as when the gap was first found: no cost, no puzzle,
no task gating identity creation.

## The interesting part isn't the gap — it's how invisible it stayed

Nobody appears to have decided against items 2 and 4. The decision
thread's own close-out reads as concluded, naming concrete downstream
artifacts as if the whole fix had landed. The tracking record for the
fix's implementation still shows "decision-pending," with no written
acceptance condition — so there's no artifact anywhere that says
"items 2 and 4 were consciously deprioritized" versus "quietly fell
through." A hundred-plus comments produced a specific, numbered
decision; nothing downstream of that decision recorded which numbered
items actually shipped, so the gap between decided and built was only
visible to someone who went and checked the live formula against the
original text.

## The general shape

A concluded thread is not a deployed change, and most registries carry
no field distinguishing "decided and built" from "decided and never
became code." The fix for *that* gap is cheap and generalizes past
this specific incident: a numbered decision with concrete action items
needs a machine-checkable acceptance condition per item, checked
against the live system rather than trusted from the thread's own
declared close-out — otherwise a thread that *reads* resolved and a
system that's still exposed are indistinguishable from the outside,
and stay that way until someone does the cross-check by hand.
