---
title: A content hash can be silent about its own scope
claim_ref: seal-scope-hash-v1
as_of: 2026-09-29
related: [declaration-without-checkability, fingerprint-digest-necessity]
---

# A content hash can be silent about its own scope

**Problem.** A tamper-evidence mechanism seals a content hash to a
registry and can be entirely honest about what it proves — "this content
is unchanged since sealed" — while the *scope* it claims to cover (which
files, which fields, what is deliberately excluded) lives only in prose
beside the mechanism, never in the checkable payload. A stranger who
reads the sealed row alone cannot recover what the seal was supposed to
cover. The coverage half (did it seal; does the hash still match) and
the scope half (what is the hash a hash *of*) sit in different places,
and only the first is checkable from the row. The scope statement can
drift, or be edited, with nothing in the sealed payload registering it.

**Repair.** Give the scope statement a version and a hash, and place
that hash where a reader can reach it. Two placements, with different
reach:

- *Beside* — the verifier prints its stated scope as a versioned string
  before any other output, followed by that string's hash, and a test
  pins the hash as a literal. Changing one word without bumping the
  version fails the build. Cheap and useful, but a reader who sees only
  the sealed row still sees no scope.
- *Inside* — the sealed payload carries the scope hash as its own field,
  next to the content hash. "Unchanged since sealed" and "covers the same
  scope as before" become two separately recoverable claims read off the
  row: a moved scope is a moved hash, with no prose reading needed to
  catch it. The verifier reports whether a row's scope is the current
  version, a retired one, or absent.

Version discipline makes either placement usable over time: when the
wording changes, bump the version and keep the retired string and hash,
so rows written under the old sentence remain checkable against the
sentence that was in force when they were written. The cost of a dispute
is then one version bump, one literal changed, and the old literal kept.

**What this does not close.** A scope hash proves the *wording* is under
version control, not that the boundary it states is right: a moved
boundary is a moved hash, and a wrong boundary stays wrong at every
version. A real failure mode: a verifier failed to recover sound rows
because recovery depended on an edge the scope sentence never named (how
a busy source truncates its pages) — the hash was correct and the
sentence was incomplete. Separately, a payload may already carry a
version that versions the wrong axis (the row's *format*, not the *scope
claim*), and adding a hash helps only if it targets the scope statement
specifically. Finally, the two halves of a paired marker (open and
close) should carry the same scope value, and a verifier should check
that they do.

**Environment.** Any tamper-evidence or content-addressed sealing
mechanism whose checkable payload proves unchanged content but not
unchanged scope — audit logs, seal registries, config-drift detectors,
snapshot fingerprints — wherever "what does this proof cover" is a
separate fact from "does the content match" and the first lives only in
documentation a verifier never reads.
