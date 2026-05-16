# P4_v1093 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0030pt_P4_v1093_R12_R-round_real
**Wall time**: 25.6s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=73298, completion=3130, reasoning=2082, total=76428

---

**PAPER-GRO-B1**

**Section:** Table in §sec:signal_hunt (confidence-stratified dipole table) + associated caption

**Issue:** The 4,758-galaxy shortfall between the summed high-confidence bins and the canonical HC-spiral cut is explained only as "boundary-edge handling" and "strict half-open binning vs abs(p_cw_eq)>0.6". This predicate mismatch (max(p_cw_eq, p_ccw_eq) > 0.6 vs the production cut) is not a trivial rounding artifact and creates a reproducibility hole: downstream users cannot exactly replicate the HC subsample from the published binning logic.

**Fix:** Replace the ad-hoc explanation with a single, machine-readable predicate used everywhere (e.g., `max(p_cw_eq, p_ccw_eq) > 0.6` and `class_eq in {CW,CCW}`) and recompute the table from that definition. Add the exact SQL/ pandas filter to the reproducibility artifact.

**PAPER-GRO-B2**

**Section:** Abstract + §sec:sensitivity + Conclusions (Fisher vs empirical threshold language)

**Issue:** The abstract and sensitivity section now correctly locate the 0.75 % empirical threshold on the N=471 k HC subsample and note it tracks the subsample Fisher floor rather than a full-catalog degradation. However, the Conclusions still juxtapose the "statistical-only Fisher full-amplitude floor ∼0.29 %" with the empirical 0.75 % number without an explicit statement that the 0.29 % figure has never been demonstrated on the full 3.2 M sample. This preserves the original reviewer concern that the headline sensitivity claim mixes two different samples.

**Fix:** In Conclusions, add one sentence: "The 0.29 % Fisher floor is an ideal-statistical limit on the full catalog; the operational 50 %-recovery threshold remains the 0.75 % value measured on the HC subsample. A full-catalog injection sweep is deferred."

**PAPER-GRO-B3**

**Section:** §sec:hemisphere + abstract (LEE framing)

**Issue:** The abstract now states the Bonferroni/BH bound reduces the local significance to <1 σ while separately noting the direct-MC random-label null is rejected at p_LEE ≤ 10^{-4}. The two statements are not reconciled in one place; the reader is left to decide which null is primary. This is exactly the "direct-MC primary + Bonferroni demoted" framing the round context required, but it is split across abstract and body without a single load-bearing sentence.

**Fix:** Add one sentence in the abstract after the <1 σ clause: "The direct-MC random-label null is rejected at p_LEE ≤ 10^{-4}, but this is attributed to the same sub-percent monopole leakage already quantified in the MASTER analysis rather than a primordial dipole."

**PAPER-GRO-B4**

**Section:** §sec:comparison (Shamir sample-size claim) + bib entry for Shamir:2022DESI

**Issue:** The text repeatedly cites Shamir 2022 as analyzing "nearly 1.3 × 10^6 spiral galaxies." The bib note itself records that the published abstract says "nearly 1.3 × 10^6 galaxies" and that not all are classified as spirals. The mismatch is a citation-forensics error that inflates the apparent sample-size advantage.

**Fix:** Change every instance to "nearly 1.3 × 10^6 galaxies, of which a subset were classified as spirals by Ganalyzer" and update the bib note to be the authoritative source.

**PAPER-GRO-M1**

**Section:** §sec:tta (TTA softening language)

**Issue:** The section now correctly states that TTA guarantees output-level flip-equivariance but does not cancel hard-label bias or the 9.5 σ monopole, and cites the 1.35 % D4 shift + 21 % argmax-flip rate. However, the phrase "flip-equivariance at soft-probability level" still appears in the figure caption and nearby prose, which is the exact softening the round context required but remains attached to a figure that shows the residual monopole. This is minor but leaves a small residual overclaim site.

**Fix:** Change the figure caption to "Demonstration of test-time flip averaging; residual 9.5 σ monopole and 21 % argmax-flip rate demonstrate that hard-label bias is not cancelled."

**PAPER-GRO-N1**

**Section:** Title + abstract opening

**Issue:** The title frames the work as demonstrating a "quantifiable monopole-mask leakage channel" that "can mimic" prior dipoles. This is accurate for the pre-MASTER stage but the post-MASTER headline is a null. The title therefore over-promises explanatory power relative to the actual matched-pipeline caveat stated in the abstract.

**Fix:** Shorten title to "Monopole-Mask Leakage Can Inflate Raw Pseudo-C_ℓ Chirality Dipoles: Equivariant Re-Analysis of 8.47 M DESI Legacy Galaxies at Sub-Percent Sensitivity."
