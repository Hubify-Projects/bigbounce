# Pattern 068 — preemptive-rebuttal-hardening (stop recurring re-flags at the source)

**Class:** review-methodology / convergence-acceleration
**Discovered:** 2026-06-30 (INT-M2 round — all 6 paper-owner agents independently converged on this technique)

## Symptom

At convergence, external/internal reviewers stop finding NEW real defects but
keep re-flagging the SAME already-disclosed caveats every round (e.g. "companion-
reliance", "σ values not comparable", "Zenodo DOI not minted", "abstract
overstates"). Each round burns effort re-truth-auditing the same dismissals to
the same FALSIFIED/STALE verdict. The gap is at zero on substance but the
verdict tally stays MAJOR/MINOR-dominant — an asymptote.

## Root cause

A disclosed caveat buried mid-paragraph, or stated once, is easy for a fresh
referee (or a fresh LLM context) to miss — so they re-flag it as if new. The
paper is correct; the DISCLOSURE is just not prominent or explicit enough to
preempt the re-flag.

## The technique (what to DO each round — this is the per-round improvement)

When a finding truth-audits to STALE-already-disclosed or FALSIFIED **and it
recurs across ≥2 rounds**, do NOT just dismiss it again. Instead **add an
explicit in-paper rebuttal/clarification** that a future referee will hit before
they can re-flag:

- Make the buried caveat prominent (move to abstract/section-head, or add a
  one-line "Note: X is intentional because Y").
- For a recurring math-misread (extraction artifact), add an explicit
  dimensional-accounting or identity line next to the equation.
- For a recurring "should be N²/structural" error, state the correct scaling
  inline so the wrong premise is visibly answered.

This converts each round's effort into a PERMANENT reduction of the re-flag
surface — the next pass has no foothold. NEVER fabricate: every rebuttal must be
source-grounded and must not strengthen a claim (for null results, hardening
makes the null MORE conservative).

## Evidence

INT-M2 (2026-06-30): 0 genuinely-new MAJORs across all 6 papers, but rebuttal-
hardening added to every paper (mass-dimension accounting P1A; double-angle note
P1B; N³-scaling clause P2; dedup-sum chain P3; σ-juxtaposition-is-diagnostic-not-
detection P4; exact-integer-σ note P5). Reviewer-prompt rule 28: "for a finding
that recurs ≥2 rounds as STALE/FALSIFIED, add an in-paper rebuttal, don't just
re-dismiss." This is how a converged review keeps producing real improvement.
