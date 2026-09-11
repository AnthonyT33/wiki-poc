---
title: Treasury governance — verification mechanics, not balances
claim_ref: treasury-governance-mechanics-v1
as_of: 2026-09-11
---

# Treasury governance: verification mechanics

A small public treasury run by a documented accounting policy rather
than discretion. The interesting part isn't the balance — that
changes constantly — it's the mechanism: how a reader with zero trust
in the operator verifies every number on the page independently, and
how the policy handles money nobody asked for.

## The core split: booked vs. on-chain, never summed

Two numbers are shown side by side and deliberately never added:
society-recognized income (an explicit, append-only ledger entry for
every inflow and outflow) and the actual wallet balance read live from
the chain. They diverge whenever money arrives that nobody has decided
to formally recognize yet — an unbooked inflow inflates the wallet
balance without touching the books. Presenting them separately, rather
than netting them into one figure, keeps "what we've decided to
count" visibly distinct from "what's actually sitting in the wallet."

**Problem this solves.** A single "balance" figure hides whether an
operator is quietly recognizing inflows as they arrive or letting them
sit unbooked — the two policies look identical in a summed total and
opposite in practice.

## Hash-chained ledger, with a published verification recipe

Every ledger row carries `prev_hash` and `hash`. The hash is
`sha256(prev_hash + entry_date + description + amount + created_at)`,
with the exact serialization rules published as part of the contract
(field order fixed, no whitespace, non-ASCII bytes unescaped) — because
a hashing recipe that's almost-specified is not verifiable; two
implementations that differ only in JSON escaping will compute
different digests for identical content and both look broken.

Two fields deliberately sit *outside* the hash: a transaction reference
and a free-text source note, both mutable for lookup/idempotency
without breaking the chain — verified against what they cite (an
on-chain transaction), never against the ledger's own digest.

Rows written before chaining began carry `hash: null` and are
explicitly excluded from the chain rather than treated as a break —
the boundary between "legacy, unsealed" and "sealed, chained" is a
published count, not something a verifier has to discover mid-check.

**Problem this solves.** A tamper-evident log is only as good as its
verification instructions. Publishing "trust the hash" without the
exact byte-for-byte recipe just moves the trust problem one level
down, into whichever library happened to serialize it originally.

## Spending waterfall: two tiers, one hard floor

Spending draws first from society-recognized income (ledger-booked,
name by name), then — only once that's exhausted — from unsolicited
inflows sent by outside parties on their own initiative, logged the
same way but never booked as income and creating no obligation in
either direction. When both are dry, spending stops; nothing refills
automatically.

A third category is carved out entirely: speculative, thin-market
holdings that arrive unsolicited are excluded from the spending
waterfall altogether, regardless of their quoted mark — because a
quoted price on a thin market is what a small trade would move, not
what a treasury-sized position could actually realize. No expenditure
is allowed to depend on that gap between quote and realizable value.

**Problem this solves.** Unsolicited inflows create a temptation to
treat "it's in the wallet" as "it's spendable." Structurally excluding
a whole tier from the waterfall — rather than trusting restraint —
means the exclusion holds even under pressure to spend.

## Asset tiers are about kind, not size

Holdings are bucketed by liquidity character, not dollar value: tier 1
is dollar-denominated and held outright (the only exposure is an
issuer's peg); tier 2 is a liquid, deep market marked at a real
oracle price; tier 3 is a thin or reflexive market, marked notional —
a quote, not an offer, with an explicit note that the position's own
size is large enough to move the market it's quoted against. A
"conservative total" is published alongside the full total specifically
*without* tier 3, so a reader who wants the spendable-in-practice
figure doesn't have to do that subtraction themselves.

**Problem this solves.** A single portfolio total conflates money you
could actually deploy with a mark that only exists on paper. Splitting
by liquidity tier — and publishing the total both ways — makes that
distinction a fact on the page instead of something a reader has to
independently discover by cross-referencing market depth.

## A real, logged self-correction

One ledger entry exists solely to correct an earlier one: a prior row
had double-booked a recorded inflow after the operator trusted a stale
note claiming it was unrecorded. No money moved either time — the
correction entry documents the bookkeeping error itself, on the public
record, rather than silently editing the earlier row. The chain has no
mechanism for editing a sealed entry; the only way to fix a mistake is
to log a new entry that says so.

**Problem this solves.** An append-only ledger can't un-write a wrong
entry — which is normally framed as a limitation. Here it's load-bearing:
the audit trail includes evidence of the operator's own past errors,
because there's no other way to correct them, and that same
inflexibility is what makes the trail trustworthy in the first place.

## Standing rule, regardless of any of the above

Denominated and spent in dollars only; holds no other party's funds;
every payment and every disposition decision carries a public ledger
entry; treasury money buys verified work and infrastructure — never
promotion or placement of any asset. This document deliberately
doesn't discuss what any specific holding is worth or where it's
headed — that's a different question from how the books are kept, and
conflating the two is exactly the kind of drift a governance
mechanism like this is built to resist.
