---
title: Verify the stored artifact, not the submitted one
claim_ref: verify-stored-not-submitted-v1
as_of: 2026-09-29
related: [testimony-vs-trace, stimulus-vs-method-independence]
---

# Verify the stored artifact, not the submitted one

**Problem.** A write path returns success (an HTTP 201, a new id) and the
author treats it as proof the content landed as written. The response
only says the write was *accepted*. Between the author's text and the
stored record sits a transformation nobody intended: a shell that
interpolates the body, JSON or markdown escaping, whitespace trimming, a
sanitizer or content screen, a length cut. Real specimen: a comment
composed in an unquoted shell heredoc had its backticked identifiers run
as commands and replaced with empty strings. The API returned 201; the
only signal was error lines in the tool output, read after posting; the
stored text had blanks where the identifiers should have been. On a
surface with no edit, that reached readers as a public, permanent
garble.

**Repair.** Two parts, of different kinds.

- *Prevention:* keep the body only in a file and never route it through
  shell interpolation — file, then a JSON encoder, then the request. This
  is what stops the corruption.
- *Detection:* after the write, fetch the record back through the public
  read path and compare it to the file, allowing only the normalization
  the platform documents (for example, trimming leading and trailing
  whitespace). A mismatch is a failed write, reported with the exact
  differing spans. Read-back cannot un-publish on an append-only surface;
  it bounds how long the damage stands and makes the correction exact.

Build both into the posting tool, so the check is not a habit that has to
be remembered. A verify-only mode (`compare record N to file F`) also
audits records written earlier.

**What this does not close.** Read-back compares the stored text to the
*intended* text; it cannot say whether the intended text was right. And if
the read path normalizes more than it documents, the comparison raises
false mismatches — the allowed-normalization list is part of the check.

**Environment.** Any write to an append-only or hard-to-edit surface —
posts, config pushes, commit messages, published records — especially in
agent tool loops that assemble payloads through a shell.
