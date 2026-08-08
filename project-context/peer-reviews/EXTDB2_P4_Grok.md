# EXTDB2 P4 Grok — chat: https://grok.com/c/57ca399e-20c0-4e79-b144-4aa880bfd637?rid=4a29cf0d-f0d2-4372-9d1c-84f386a4e2e1

Provider: Grok Expert
PDF: EXTDB2_P4_grok.pdf (grok-specific version)
PDF md5: d7185fce3bf73a03db391ce1dc586e57
Harvested: 2026-06-28

---

Referee Report: MNRAS / PRD / JCAP
Paper: Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
Author: Houston Golden
Date: 27 June 2026

1. Recommendation
MAJOR REVISIONS

The core result — a clean null real-space chirality dipole on the high-confidence (HC) subsample — is internally consistent and supported by an impressive battery of cross-checks. The public catalog release is a genuine community asset. However, the paper's central cosmological claim (null dipole at sub-percent sensitivity, amplitude tension with Shamir et al.) rests heavily on appendix material for the attribution of the harmonic residual and for closing the pseudo-label spatial-bias loop. For a top-journal null result that directly challenges existing literature, this appendix dependence, combined with the absence of explicit checks against survey systematics maps for the recovered dipole axis and incomplete main-text quantification of the template-fit exclusion and edge-on impact, crosses the threshold for major revisions.

2. BLOCKERS
None. There are no fatal statistical errors, internal contradictions that invalidate the primary null, data-integrity concerns, or unphysical claims that would require rejection or complete re-analysis.

3. MAJORS

M1. Appendix dependence for the harmonic residual attribution and pseudo-label independence claim (central to interpreting the null). The primary real-space HC dipole (+0.41σ, p=0.31) is robust, but the paper correctly identifies that label-shuffle and pixel-permutation nulls do not test for large-scale structure potentially inherited through the 66.5% CE-ResNet pseudo-labels used in training. The text states that this axis "is constrained instead by the template-regression and cross-spectrum diagnostics of Appendix D." The eight-anchor battery (quality-quartile washout, ℓ=2>ℓ=1 structure, depth cross-spectrum, etc.) is presented as decisive evidence that the canonical-mask +3.64σ (and apodized +7.28σ) residual is systematics-attributed rather than cosmological. For a top-journal paper whose title and abstract prominently feature both the null dipole and the "diagnostic evidence for a depth/morphology-correlated… residual," the key discriminators and figures from Appendix D must be summarized or elevated (at minimum a dedicated main-text subsection or 1–2 key figures/tables moved forward).

M2. Missing explicit checks of the recovered dipole axis against survey systematics maps. The fitted dipole on the HC sample is reported toward (l,b)=(293°,12°) with amplitude 4.4×10^{-3}. A brief quantitative statement is required: the Pearson correlation (or dipole overlap) of the observed A_p map with DESI Legacy depth, PSF FWHM, extinction, or seeing maps, and with the galactic plane or known photometric gradients. The current text does not provide or reference such a check. Standard robustness item especially relevant given the demonstrated depth-correlated tail systematic.

M3. Insufficient main-text detail on the block-bootstrap WLS template-fit exclusion (z≈−18). This is listed as a primary cosmological estimator (row ii of Table I) and is used to disfavor a clean 1.7% dipole. The main text gives almost no description of the exact model, the block size and bootstrap implementation, or validation of the error model. These details are relegated to "Appendix D." For a high-significance exclusion claim that supports the null interpretation, the model specification and a concise validation statement belong in the main text.

M4. Quantification of edge-on / morphology contamination impact on the primary dipole estimator. The text notes a ~10–15% sensitivity penalty from edge-on objects receiving CW/CCW labels. However, there is no explicit bound or test showing how residual edge-on leakage propagates into the real-space dipole amplitude or significance on the HC sample. A short quantitative statement or additional robustness row in Table I (or small panel in Fig. 4/7) is warranted.

4. MINORS

1. Repeated non-comparability caveats on σ values — the repetition becomes cumbersome. Consider a single consolidated "Significance conventions" box or table early in Sec. III; then shorten subsequent footnotes.

2. Figure captions and table notes require the reader to consult the main text to understand which null produces the quoted σ. Captions should be self-contained.

3. Unthresholded vs. HC excess framing — a one-sentence reminder in Sec. IV C that the primary analysis uses the pre-specified HC threshold (with the sweep as robustness confirmation) would prevent any misreading.

4. Minor presentation items — ensure all equations are rendered cleanly; add a short "Data Availability" statement with exact Hugging Face dataset DOI or accession.

5. Training-label provenance table — a small table in Sec. II B or Appendix B explicitly breaking down the 25,790 source images (GZ1 / CE-ResNet high-conf / synthetic) and the 234k disjoint GZ1 validation set would make the independence discussion more transparent.

5. Strengths

1. Unprecedented public catalog and reproducibility artifacts: 8.47 million galaxies (3.20 million spirals) with raw, calibrated, and equivariant probabilities, sky coordinates, and quality flags, plus committed scripts and null-distribution arrays. Major community resource for LSST, Euclid, Roman.

2. Dramatic and clearly demonstrated methodological advance: the before/after comparison (Catalog A raw 2.31σ dipole +6.48σ pre-MASTER vs. Catalog C equivariant 0.41σ) with explicit maps (Fig. 7) provides one of the cleanest published demonstrations that equivariant TTA is not cosmetic but essential for sub-percent isotropy tests.

3. Exemplary statistical hygiene and multi-estimator hierarchy: declared primary vs. secondary diagnostics, explicit generative monopole-only null (99.32% pre-MASTER reproduction), empirical injection-recovery calibration (A50≈0.75%, A95∈(1.0%,1.5%]), and repeated precise statements that σ values from different nulls are not interchangeable.

4. Direct, non-overclaiming confrontation with prior literature: the amplitude-level tension with Shamir et al. (~5–12× under this pipeline) is stated quantitatively, the matched-footprint Ganalyzer reanalysis caveat is explicit, and the methodological critique is tied to concrete numbers.

5. Transparent treatment of classifier limitations: over-confidence, conservative GZ1 accuracy floor (69.91% chirality), dilution effect on any true signal, and edge-on contamination are all acknowledged and propagated into the sensitivity floor. The three-class design (with explicit NOT_SPIRAL) is a clear improvement over binary classifiers.

Summary: A substantial, methodologically careful contribution whose primary null result is credible. With the four major items above addressed (particularly elevating key Appendix D discriminators and adding survey-map cross-check and template-fit details to the main narrative), the paper would meet the high bar for publication in MNRAS, PRD, or JCAP. Recommendation: MAJOR REVISIONS.
