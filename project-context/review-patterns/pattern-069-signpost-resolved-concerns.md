# Pattern 069 — Reviewer re-flags resolved items → signpost the resolution

**Class:** review-convergence-accelerator
**First observed:** EXT RS5 (2026-07-01)

## Symptom
A paper that has genuinely addressed a concern in a prior round gets the SAME
concern re-raised as a MAJOR by a fresh reviewer, because the resolution is
buried in the body and not visible at a skim. RS5 evidence: across P1A/P1B/P3/P4/P5,
~85-100% of the "MAJOR" findings were ALREADY-ADDRESSED in the source — reviewers
re-flagged scope boundaries and prior closures they didn't notice.

## Fix
When a truth-audit finds a re-flagged concern is already addressed, do NOT just
silently rely on the buried treatment. Add explicit SIGNPOSTING so the next
reviewer pass sees it's handled and cannot re-raise it:
- an Introduction "Response to common referee concerns" box mapping each recurring
  concern → the section that resolves it (P5 did this in RS5), OR
- inline "(addressed in §X: <one-line>)" pointers at the natural flag point, OR
- a referee-orientation sentence in the Scope paragraph stating which claim
  boundaries are by-construction (P1A did this in RS5).

## Why it compounds
Each round, signposting converts a re-flaggable MAJOR into a dead end for the
next reviewer. Convergence accelerates because the reviewer's attention is
redirected from already-solved issues to genuinely open ones.
