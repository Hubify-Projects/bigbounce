# P4 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint-v2_P4_v1_0_138
**Wall time**: 15.6s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=96303, completion=1824, reasoning=1089, total=98127

---

**PAPER-GRO-B1**  
**BLOCKER** — Title + abstract (lines 1-3, abstract para 1)  
Title and abstract frame the result as a test of "Large-Scale Parity Violation," but the paper explicitly states the \(\ell=1\) dipole is parity-EVEN axial-vector and "NOT a direct parity-violation test." This is a direct mismatch between headline framing and the observable's symmetry class.  
**Fix:** Retitle to "No Evidence for Large-Scale Isotropy Breaking in Galaxy Chirality Dipole" (or equivalent) and remove "parity violation" language from abstract and keywords.

**PAPER-GRO-B2**  
**BLOCKER** — Abstract + §VI.D (joint nuisance fit paragraph)  
Claims "FORMALLY EXCLUDED AT 99% CONFIDENCE" for interpretation (i) at 1.7% via the 9-template (and 24-template) fit, yet the canonical-mask residual remains +3.64σ under the binomial null and the fit marginalizes over imaging-leg + density templates that are themselves the dominant systematic. The exclusion is conditional on the nuisance model being complete; the paper does not demonstrate that.  
**Fix:** Downgrade to "disfavored at >5σ under the joint nuisance model; a clean dipole-only explanation is excluded only within the assumed 9/24-template basis."

**PAPER-GRO-M1**  
**MAJOR** — Abstract sensitivity claim + §IX.J (injection sweep)  
Headline "sub-percent sensitivity" and "Fisher-floor ~0.29%" are presented as the operational number, while the load-bearing empirical 50%-recovery-at-3σ threshold is 0.75% (HC subsample) and the full-catalog sweep is only reported as "better than 0.50%." The 0.29% figure is an ideal-statistical asymptote, not the demonstrated threshold.  
**Fix:** State the empirical threshold as the primary sensitivity number in abstract and conclusions; move Fisher value to a footnote.

**PAPER-GRO-M2**  
**MAJOR** — §I + §X (comparison with Shamir)  
States the result is "inconsistent in amplitude with Shamir's ~3% asymmetry by a factor of ~6-12" under the present pipeline, then immediately adds the matched-footprint Ganalyzer reanalysis caveat. The amplitude comparison is presented as a substantive result while the actual exclusion claim is disclaimed.  
**Fix:** Remove the numerical factor claim or qualify it as "under the present ViT/TTA pipeline only; no likelihood-level exclusion of Shamir's estimator is performed."

**PAPER-GRO-m1**  
**minor** — Version-history comments (entire preamble)  
~200 lines of reviewer-ID closure narrative, R-round counts, and "drive-to-100 fire" timestamps are embedded in the source. While stripped from the PDF, this is visible in the arXiv source and creates an impression of defensive engineering rather than clean science.  
**Fix:** Move all version-history and reviewer-response text to a separate supplementary note or GitHub release notes.

**PAPER-GRO-n1**  
**nit** — Table II footnote b + Table III caption  
Multiple overlapping null models (monopole-only generative, per-pixel-shuffle, bootstrap) with different MC sizes and different masks are described in dense footnotes. The reader cannot tell at a glance which null applies to which row without cross-referencing.  
**Fix:** Add a one-line "Null model" column to Table II or a short legend above the table.
