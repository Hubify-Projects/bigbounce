# P4 2026-06-04_R4fixed — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 28.2s

---

PRD-REFEREE REPORT  
Manuscript: P4 – “Survey-Scale Galaxy Chirality … DESI Legacy Galaxies”  
Round: 2026-06-04_R4fixed  
Length: 56 pages  

I have audited the statistical methodology, the chain of derivations and every scalar quoted in the Abstract/Conclusions.  
Below I list all issues found.  “σ” means standard deviations; “fCW” the CW fraction; all section/page numbers refer to the pdf as supplied.

------------------------------------------------------------------
FINDINGS
------------------------------------------------------------------

ESSENTIAL
---------

P4-E1  (Sec. III A, p.7; Abstract 1st para)  
Problem:  The “analysis hierarchy” was fixed only after the first catalogue results (v1.0.76).  This is data-dependent choice of the primary estimator.  The paper calls it “declared” but not “pre-registered”.  All subsequent significances use this post-hoc hierarchy.  
Fix:  Re-analyse with the hierarchy specified in a blinded way (e.g. split sky, freeze criteria on first half, apply to second) OR downgrade every quoted significance by the look-elsewhere factor implied by the hierarchy search (must be computed explicitly).  Clarify in the Abstract that no pre-registration was performed.

P4-E2  (many places, Table II, Abstract, Sec. IV C)  
Problem:  σ values from four mutually incommensurable null procedures (per-pixel shuffle, label shuffle, binomial-monopole, bootstrap) are presented in the same units without a conversion factor; in several places they are visually compared (e.g. “+3.64 σ residual vs −0.12 σ null”) as if on a common scale.  The disclaimer paragraph is insufficient—the practice violates instruction #7.  
Fix:  For every σ printed, attach the null label in the text (σshuffle, σmono …) and forbid cross-comparison.  Alternately translate all results to p-values and quote those.

P4-E3  (Sec. VI C, Table XVI, Abstract)  
Problem:  The “≥ 0.75 % 50 %-recovery-at-3 σ” threshold is used as the catalogue sensitivity, but the injection study is done on the HC subsample (471 k) while the headline dipole null is on the full 3.20 M spirals.  Sensitivity of the analysis actually applied is therefore unknown.  
Fix:  Repeat the injection-recovery on the exact estimator/mask used for the −0.12 σ result and quote that number in the Abstract.

P4-E4  (Sec. III E, 1st para; Sec. VI D)  
Problem:  The authors claim test–time 2-fold TTA “guarantees equivariance” yet show a per-galaxy arg-max flip rate of 21.4 %.  That is **not** equivariance; it is model instability.  Consequently the stated CW bias suppression factor 3.86× is not reliable.  
Fix:  Provide the dipole analysis using the soft-probability map only (no hard labels anywhere) or run the full D4 TTA on the complete catalogue.  Until that is done all hard-label results must be removed from the manuscript.

P4-E5  (Sec. IV D, Table VII)  
Problem:  Moment-z of +3.64 σ is quoted, but the correct significance against the MC null is p=0.030 (~2.17 σ two-sided).  The text continues to call this a “3.6 σ residual”.  
Fix:  Report the empirical rank significance (2.17 σ) everywhere; do not mix with the Gaussian moment.

P4-E6  (Eq. 5, Sec. IV F; Table XII)  
Problem:  The two-point statistic uses 10 angular bins chosen *after* inspecting the data (brick scale mentioned).  No correction for that choice is applied.  
Fix:  Supply a pre-defined bin set or Bonferroni/GV correction; update all quoted σ.

P4-E7  (p. 36, falsification criterion)  
Problem:  Criterion refers to the full amplitude A but all earlier floors are for the half-modulation.  Numerical value therefore off by factor 2.  
Fix:  State clearly which convention is used and recompute.

MAJOR
-----

P4-M1  (length)  56 pages ≫ PRD format.  Methods catalogue papers typically ≤ 30 pp.  Recommend compressing Tables I/II/VIII-XI into an online appendix and removing repeated narrative (≥15 pages redundant).

P4-M2  (Sec. III F, Table IV)  
Problem:  Bias test T5 “|corr(PCW,RA/Dec)|<0.10” is passed only because a monopole can have zero Pearson r with coordinates.  A dipole aligned with Dec will also pass.  
Fix:  Replace with spherical-harmonic aℓm test (ℓ=1, m=0 and ±1 separately).

P4-M3  (Sec. IV I, Table XIV)  
Problem:  Imaging-leg split uses heuristic RA/Dec cuts; DES overlap region partly contained in DECaLS leg.  Cross-contamination biases the leg comparison.  
Fix:  Re-derive using the official DR8 tractor “survey” bit.

P4-M4  (Sec. II B)  
Problem:  67 % of training labels come from CE-ResNet predictions (circular).  No independent validation of those labels is given except GZ1 overlap which itself is biased.  
Fix:  Provide accuracy on a *fully* independent manually inspected set (≥ 1 000 galaxies).

P4-M5  (Sec. IV B)  
Problem:  The global monopole uncertainty σ=0.000279 is treated as independent counts.  Spiral classifications are spatially correlated (seeing).  
Fix:  Estimate Neff from the pixel covariance and propagate to σ.

P4-M6  (Sec. VI D, edge-on)  
Problem:  59 % of b/a<0.3 galaxies classified spiral.  Stated that this “only dilutes S/N”, but may introduce systematic if b/a distribution is depth dependent.  
Fix:  Re-run dipole on b/a>0.5 subset and quote result.

P4-M7  (Sec. VI G)  
Problem:  Axis-alignment calculation missing formal statistic; “random” stated qualitatively.  
Fix:  Provide Monte-Carlo isotropic distribution of mis-alignment angle.

P4-M8  (Sec. VIII)  
Problem:  Reason for using NaMaster with coarse ℓmax=191 not justified.  Resolution NSIDE=64 can support 3Nside=192 but signal may leak from ℓ=1 into 2.  Need convergence test with NSIDE = 128.  
Fix:  Provide check that C1 is stable.

MINOR
-----

P4-m1  (Abstract)  “−0.12 σ … fully consistent with null” – state null model in abstract (label shuffle).  
P4-m2  Duplicate phrase “canonical canonical-mask” p. 17 line 3.  
P4-m3  Fig 3 colour bar lacks units.  
P4-m4  Some footnotes > 150 words: move to main text.  
P4-m5  Table X row ordering inconsistent with legend.  
P4-m6  Eq. 7 uses √3 but text says “factor 3”.  Correct.  
P4-m7  Data-release DOI not yet provided.  Must supply final DOI before acceptance.  
P4-m8  Typos: “monopole-substracted”, “anal- ysis”.

NIT
---

P4-n1  PACS numbers obsolete; replace with Physics and Astronomy Classification Scheme 2010 or arXiv categories.  
P4-n2  Author email footnotemark renders “houston@hubify.com” twice.  
P4-n3  Strip “wave14”, “pod3” internal run tags from caption text.  
P4-n4  Long dashes rendered as “–” in pdf metadata string.  
P4-n5  Reference [31] year missing (2019).

------------------------------------------------------------------
SUMMARY RECOMMENDATION  
------------------------------------------------------------------
MAJOR REVISIONS  

The catalogue is potentially very valuable, but several methodological points must be fixed before the scientific conclusions can be trusted.  Chief among them are (i) replacement of the post-hoc estimator choice with a pre-defined or trials-corrected one, (ii) consistent treatment of null variances, (iii) clarification of the sensitivity floor and injection test, and (iv) proper handling of the 21 % rotation-flip uncertainty.  Once these are addressed the manuscript can be reconsidered.