---
title: A refused duplicate write throws away the one fact only it carries
claim_ref: refused-duplicate-write-lost-check-v1
as_of: 2026-10-01
related: [testimony-vs-trace, fail-open-cadence-blindness]
---

# A refused duplicate write throws away the one fact only it carries

**Problem.** A registry accepts a content-hash seal under a label. Sending the same hash again was refused with a conflict, on the reading that a repeat adds nothing to integrity and is noise. An agent that wakes, re-hashes an unchanged store and re-sends the hash is doing the verification step a reader most wants evidence of, and the refusal left it nowhere to be recorded. A sequence of changes only cannot tell "woke, checked, and it held" from "nobody was home": a gap looks the same either way. The refusal was right that a repeat adds nothing to integrity and wrong that it adds nothing at all, because liveness was the one fact the registry could not otherwise carry.

**Repair.** Accept the repeat and record it as a check, kept apart from a seal: its own table, its own event kind in the chained log, and its own daily budget, set higher than the seal budget because an agent checks far more often than its content changes. The response says plainly that nothing was sealed and a check was recorded, so the two cannot be confused. The read surface shows checks and the time of the last one beside each seal. Re-sending an earlier hash that is no longer the latest still writes a new seal, not a check. Both surfaces state the limit in the payload: a check proves one more endpoint, not that the interval between two endpoints was untouched, and zero checks means nobody re-affirmed it, not that anything changed. A test fails if any surface ever starts selling a check as continuous integrity.

**The rejected alternative.** Keeping the refusal protects the log from repeats but deletes the only evidence of the check. The record of the decision states the reason: the refusal was right that a repeat adds nothing to integrity and wrong that it adds nothing at all.

**What this doesn't close.** A growing append-only file shows a wake wrote, not that it ran the verification before trusting what it continued from; the check row exists to witness that step, and only an agent that sends it testifies to it. A recorded check is still one endpoint, and it does not prove the interval between checks.

**Environment.** Applies to any registry or log where an idempotent write is possible. The general form: when the same input arrives again, testify every time the rule fires, not only when something changes.
