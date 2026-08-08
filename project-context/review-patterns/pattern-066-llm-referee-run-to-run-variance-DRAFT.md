# Pattern 066 — llm-referee-run-to-run-variance (single-sweep tally is not a stable signal)

**Class:** review-methodology / oracle-noise
**Discovered:** 2026-06-29/30 (Round B EXT was MINOR-dominant; Round C EXT was MAJOR-dominant on the SAME, slightly-improved papers)

## Symptom

The same paper, at the same or a slightly-better version, draws materially
different external verdicts across two browser-tier sweeps days apart — e.g.
P1A/P3 swung from MINOR-tier (Round B) to 3/3 MAJOR (Round C) with no
regression in the source. Treating any single sweep's verdict tally as ground
truth produces whiplash and false "the papers got worse" conclusions.

## Root cause

Frontier fast-tier LLM referees (ChatGPT/Grok/Gemini browser tiers) have high
run-to-run output variance: temperature, context-window framing, and which
caveats they happen to fixate on vary per session. The verdict is a noisy draw,
not a deterministic measurement.

## How to handle (prevention)

1. **Never close/declare on one sweep.** Require a finding to recur across ≥2
   independent sweeps (or INT+EXT corroboration) before treating it as real.
2. **Truth-audit every MAJOR individually** against source (patterns 061-064) —
   a 3/3-MAJOR sweep with 0 genuinely-new findings on truth-audit is noise, not
   a quality drop.
3. **Report the variance explicitly** on the site (the verdict matrix shows the
   per-sweep swing; the campaign-observations panel names it) so a reader
   doesn't read one harsh sweep as "the papers are broken."
4. **The all-3-ACCEPT-zero-MINOR gate is an asymptote** against this noise —
   convergence is measured by "0 genuinely-new real findings on truth-audit
   across a full round," not by a single all-ACCEPT sweep.

## Evidence

Round B EXT vs Round C EXT verdict matrices (externalVerdictRounds in
reviewTimeline.ts): same papers, opposite-leaning tallies, 0 new real findings
in the Round C truth-audit (RCEXT_P1A_P3_TRUTH_AUDIT.md).
