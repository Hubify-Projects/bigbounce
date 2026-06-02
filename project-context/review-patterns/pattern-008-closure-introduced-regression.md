# Pattern 008 — Closure landed in round N introduces a new error caught in round N+1

**First seen**: P1B R2 closure (Planck+ACT→WMAP+Planck) introduced PR4/PR3 confusion caught in R3
**Severity**: high (every closure can introduce regressions; without
cross-round audit, errors propagate)
**Frequency**: 5 (P1B R2→R3 Eskilt dataset, P1B R3→R4 PR4 vs PR3, P5 R3 in-text "Douglass" lingered after bibitem fix, P5 R4 false "Douglass" reset, P1A R2 PER-B1/M1/M2 attribution chain)
**Detection**: a closure-prose edit in round N introduces a new factually
incorrect claim that round N+1 catches.
**Prevention**: after any text closure, GREP THE ENTIRE PAPER for the property
being changed so all occurrences move together.

## What it looks like

Round 2 closure: change "Planck+ACT" → "WMAP+Planck" (correct).
But the closure prose also added "(PR4 NPIPE + WMAP)" — correct.
Round 3 closure: change "PR4 NPIPE + WMAP" → "WMAP9 + Planck 2018 (PR3)"
(WRONG — reviewer transposed DiegoPalazuelos 2022's dataset onto Eskilt 2022).
Round 4 closure: change back to "WMAP9 + Planck PR4/NPIPE" via repo cross-check.

## Truth-audit verdict

The original closure VERIFIED, but the *next round catches the regression
introduced by the closure prose*. This is the textbook case for cascaded
R-rounds.

## Examples observed

- **P1B R2 closure introduced R3 regression**: "joint Planck+ACT" → "joint
  WMAP+Planck (PR4 NPIPE + WMAP analysis; ACT DR6 enters only via the separate
  DiegoPalazuelos2025 measurement)". R3 PER3-B2 caught the implicit "Eskilt uses
  PR3" claim. R3 then over-corrected to PR3, which R4 caught.
- **P1B R3 closure introduced R4 regression**: "PR4 NPIPE + WMAP" → "WMAP9 +
  Planck 2018 (PR3)". WRONG. R4 PER4-B2 verified via the Eskilt+Komatsu
  reproduction repo and restored "WMAP9 + Planck PR4/NPIPE".
- **P5 R3 closure introduced R4 regression**: DESIVAST2025 bibitem corrected
  from "Douglass" first-author to "Rincon" first-author, but in-text line 1218
  still read "(Douglass et al. 2025, ApJ 982, 38)". P5 R4 GRO-m2 VERIFIED:
  in-text "Douglass" corrected to "Rincon".
- **P1A R2 closures**: 4 of 5 closures were attribution-strength corrections.
  None introduced regressions (clean attributions). But the R2 PER-B1 closure
  ("Following Mercuri & Capozziello" → "Motivated by (but not literally derived
  in)") restated for 3 more rounds before fully settling.

## Root cause

LLM-generated closure prose tends to over-stake a position. When a reviewer
points out a smaller wrong attribution, the closure-author often overcorrects
the dataset / version / volume number in a direction that creates a different
small error. The new error wears the "this was just fixed!" halo and survives
into the next round.

## Pre-review check

After any closure that edits a dataset, version number, journal volume, or
author name:

1. **GREP THE ENTIRE PAPER** for the OLD value AND the NEW value:
   ```bash
   grep -n "OLD_VALUE\|NEW_VALUE" paper.tex
   ```
   Verify all old occurrences are replaced AND all new occurrences are
   consistent.
2. **Cross-vendor verification**: for dataset/version claims, run a second
   independent check (repo README, NASA-ADS metadata) BEFORE accepting the
   reviewer-proposed fix.
3. **Co-located edits**: every claim that moves should move at every site it
   appears (abstract, body, table, caption, bibitem comment).
4. **Closure audit-log block**: every closure documents in the .tex audit-log
   block (`% v1B.0.34 (R-multi-round4): PR3 → PR4/NPIPE because...`). The next
   round's audit reads this block first and prevents reverse-regression.

Standing protocol: every R-round MUST run a previous-round-closure audit
**before** processing new findings, to detect regression-introduced new errors.
