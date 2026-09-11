---
title: Silent non-selection (the green-child pattern)
claim_ref: silent-non-selection-v1
as_of: 2026-09-11
related: [testimony-vs-trace, fail-open-cadence-blindness]
---

# Silent non-selection (the green-child pattern)

**Problem.** A check's PASS predicate reads only a channel the checked
process itself controls. If that process dies before writing anything
— crashes on its first line, never gets scheduled, silently loses a
race — the channel shows nothing, which is exactly the same signature
as a healthy process that simply had nothing to report. The check
can't distinguish "nothing went wrong" from "nothing ran."

**Repair.** The witness must live outside the process being checked: a
channel that process cannot itself go silent on. An external
dead-man's-switch, an OS-level timer independent of the checked code
path, or a third party that expects a periodic ping and alerts on its
absence, all work because none of them depend on the checked process
being alive to report its own death.

**Environment.** Cron jobs, schedulers, any "runs periodically and
reports if something's wrong" design where the reporting channel and
the checked process share a failure domain.
