# P4 2026-06-04_1920pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 20.0s

---

Referee report on P4, v 1.0.152 (4 June 2026)  
Role: methodology / statistical-rigour

====================================================================
GENERAL ASSESSMENT
====================================================================
The manuscript is an unusually long (56 pp) description of a galaxy-chirality measurement with a bespoke ML classifier and a complicated hierarchy of null tests.  The authors invest considerable effort in bias checks, but several methodological points remain unclear or internally inconsistent, and key numerical claims cannot be traced to single, unequivocal data vectors.  Before publication in PRD the paper must be shortened, the estimator hierarchy frozen, the null-model bookkeeping cleaned up, and the statistical interpretation clarified.

====================================================================
ESSENTIAL FINDINGS  (paper cannot be accepted without fix)
====================================================================
ID  |  Sect./page  |  Problem  |  Required fix
----|--------------|-----------|-------------
P4-E1 | §I, Abstract p 1 | σ–units from four different null procedures (label shuffle, pixel shuffle, monopole-only, bootstrap) are quoted side-by-side (e.g. “−0.12 σ”, “+0.43 σ”, “+3.64 σ”) without always specifying which null applies.  This violates instruction #7. | Every σ or p in the abstract and conclusions must be qualified by the exact null procedure and mask used, or expressed directly as p-value.  A single summary table in the main text is not sufficient – the abstract must stand alone.
P4-E2 | §III A & throughout | The “declared estimator hierarchy” was fixed only after inspecting the data (v1.0.76).  That is post-hoc and constitutes undisclosed model selection. | Provide a dated, publicly time-stamped preregistration (e.g. OSF) predating any look at the DR8 data, or re-phrase all significance statements as exploratory (no σ).  Otherwise the paper does not meet PRD methodological standards.
P4-E3 | §IV D pp 21-24 | The canonical-mask +3.64 σ result is attributed to “systematics”, yet is still quoted in σ units of a random-label null that does not model those systematics.  Mixing calibrated and un-calibrated σ gives a misleading impression of residual significance. | Either (i) provide a systematics-preserving null and recompute the significance, or (ii) stop quoting the +3.64 σ figure altogether and replace by the empirical p = 0.03 (rank count 15/500).
P4-E4 | §VI C pp 34-37 | Minimum-detectable-dipole is variously stated as 0.2 %, 0.29 %, 0.4 % and 0.75 %.  Units (half-modulation vs full amplitude) are mixed. | Choose one convention (full-amplitude Adip) and quote a single statistical floor (Fisher) and a single systematic-inclusive empirical floor (injection).  Re-derive both, show equations once.
P4-E5 | §III E / Fig. 4 | The 21 % per-galaxy argmax flip rate means the hard-label diagnostics underestimate their own noise by ≈29 %.  Only an approximate 1.21× factor is added by hand. | Re-compute all hard-label binomial errors including the measured flip covariance (or remove the hard-label plots).
P4-E6 | whole ms | 56 pages is almost double PRD normal length for a methods/catalogue paper. | Reduce to ≤ 30 pages main text + ≤ 10 pages appendix.  All code-listing narrative, version-history prose, and footnote digressions should move to a Zenodo “analysis note”.

====================================================================
MAJOR FINDINGS  (significant revision)
====================================================================
ID | Sect./page | Problem | Required fix
----|-----------|---------|-----------
P4-M1 | §IV C Table VI | The ℓ=1 value is sometimes reported after MASTER decoupling, sometimes before; this causes confusion. | Give a two-column table (pre-MASTER, post-MASTER) or suppress the pre-MASTER numbers in the main text.
P4-M2 | §III F Table IV | Several audit tests (T5 metadata leakage, T6 hemispheric) use ad-hoc pass thresholds (10 %).  These are not justified relative to the claimed 0.29 % sensitivity. | Re-run with thresholds tied to the statistical floor (e.g. <0.1 % for global-balance tests) or explain why a 100× looser threshold is acceptable.
P4-M3 | §IV E & Table X | Confidence-stratified analysis mixes spiral-only and “spiral+not-spiral” definitions across sections. | Use one definition consistently and recount the bins.
P4-M4 | §IV I Table XIV | Imaging-leg split employs a hand-drawn RA/Dec box for DES rather than the official DES footprint. | Replace by a mask defined from the survey tiling header or provide the footprint file.
P4-M5 | Fig. 11 | Seven-region test shows 0.26 % uniform offset but no uncertainty propagation from photo-z or Neff. | Add error bars that include spatial covariance or remove the figure.
P4-M6 | Appendices | The public catalogue does not include the per-object axis ratio needed to reproduce the edge-on test. | Supply a merged “value-added” parquet or drop the edge-on discussion.

====================================================================
MINOR FINDINGS  (editor may require)
====================================================================
ID | Sect. | Problem | Suggestion
----|-------|---------|-----------
P4-m1 | Abstract | “no dipole at −0.12 σ” sounds like a negative significance. | State “0.12 σ from null”.
P4-m2 | §II A | 8.47 M sources but later 8.474 531 – inconsistent rounding. | Pick one.
P4-m3 | §III E footnote | Two different hold-out sizes (1 558 and 1 988) are compared without stating why. | Clarify.
P4-m4 | §VI D | cite “59.4 % spiral rate” but earlier “65.7 %”. | Re-check.
P4-m5 | Footnotes | Many footnotes contain version history.  Remove per instruction #2. |
P4-m6 | Typos | Multiple duplicated phrases (“canonical canonical-mask”, “per-pixel per-pixel”). | Spell-check.

====================================================================
NITPICKS
====================================================================
P4-n1: inconsistent use of degrees (°) and “deg” in tables.  
P4-n2: Fig. 10 colour bar has no units.  
P4-n3: §III C “1.2 pp” should be “1.2 percentage points”.  

====================================================================
SUMMARY RECOMMENDATION
====================================================================
MAJOR REVISIONS

The work contains an interesting and potentially important demonstration of mask-induced leakage, but the present version mixes incomparable σ’s, lacks a pre-registered estimator, and is almost twice the normal length.  After the essential clarifications and a substantial condensation it could become a useful reference catalogue and methodology paper.