---
title: A placeholder identity can collide with a real one
claim_ref: placeholder-identity-reserved-domain-v1
as_of: 2026-09-30
related: []
---

# A placeholder identity can collide with a real one

**Problem.** A system mints a placeholder identity for an automated
actor, commonly an email address in a conventional-looking format,
on the assumption that an invented string in that format is safe
because nobody else would plausibly hold it. But some platforms
publicly link a displayed identity to whichever real account has that
exact string verified, and an older or differently formatted address
in the same general convention can already be registered to an
unrelated real person. The result: every action taken under the
placeholder identity displays as attributed to a stranger's real,
verified account, with no warning at the point of use. Invented but
plausible is not the same as guaranteed unclaimed.

**Repair.** Build the placeholder identity from a domain reserved by
standard for exactly this purpose, so that no real account can hold it.
RFC 2606 reserves `.invalid` for names that are "sure to be invalid and
which it is obvious at a glance are invalid"; `.example` (documentation)
and `.test` (testing) serve the same role for other placeholder needs.
A reserved name cannot be registered, so no mailbox exists behind it
and no account can complete the email verification that these
platforms rely on to link an identity. That is a structural guarantee
rather than a probabilistic one.

Once a collision like this is found, fix forward: change the identity
going forward rather than rewriting history to correct already
published actions taken under the wrong one. Altering a public,
already-reviewed record costs more than the original misattribution,
and the fix should say so plainly rather than quietly rewrite around it.

**What this doesn't close.** The guarantee rests on the platform
requiring verification. A platform that attributes by an unverified
string match would need its own check, and a reserved domain does not
help with a collision that has already been published.

**Environment.** Any automated actor (a bot, an agent, a service
account) that needs to mint its own placeholder identity (a commit
author, a support-ticket requester, a test-fixture email) on a
platform that publicly links a displayed identity to whichever real
account verifies the matching string. RFC 2606 text checked against
the RFC editor's copy on 2026-09-30.
