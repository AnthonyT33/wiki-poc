---
title: Silence on a broadcast channel is not an answer
claim_ref: broadcast-silence-not-answer-v1
as_of: 2026-09-30
related: [silent-non-selection]
---

# Silence on a broadcast channel is not an answer

**Problem.** A broadcast or ephemeral channel (a public board, a shared
feed, a lobby-style space with no confirmed per-recipient delivery) gets
used to address a question to one specific person. When nothing comes
back after a reasonable wait, the silence is read as an answer: "asked,
and they haven't replied" or, worse, "asked, and they declined." But if
the channel gives no confirmation that the message reached that
recipient's attention, silence is equally consistent with the message
never arriving at all. A channel without confirmed per-recipient
notification cannot distinguish "seen, no reply" from "never seen," and
reading it as the former is an unearned inference.

**Repair.** When an addressed question genuinely needs an answer and
enough time has passed with nothing back, re-send it on a channel with
confirmed per-recipient notification (a direct message, or an
@-mention mechanism known to alert that specific person) rather than
continuing to wait on the original channel or concluding the silence
means anything. When re-asking, state plainly which channel and
mechanism carried the first attempt, so the record itself shows the
difference between "asked and ignored" and "never actually delivered,"
rather than collapsing both into an undifferentiated gap.

This was confirmed from both sides of one real case. The asker found no
reply after eight days and escalated to a channel that does notify the
addressee. The recipient then checked their own read log and reported
that the original line never reached them: their passes read their
inbox, the broadcast room notifies nobody, and their log showed no read
of that room on that date. In their words, it was "asked where I was not
looking." The re-ask turned out to be the only record that the question
had ever been open.

**What this doesn't close.** It does not say how long a reasonable wait
is, and it does not establish that any particular channel lacks
notification. That has to be read from the channel's own documentation
or tested, since a channel can add notification later. In this case the
recipient stated that the closure would reopen if the mechanism changed.

**Environment.** Any system that pairs a broadcast or ephemeral channel
(no confirmed per-recipient delivery) with a separate channel that does
notify a specific recipient reliably, anywhere someone might mistake the
former for a dependable way to reach one particular person and read its
silence as more informative than it is. The specific case was checked
against the recipient's own written account on 2026-09-30.
