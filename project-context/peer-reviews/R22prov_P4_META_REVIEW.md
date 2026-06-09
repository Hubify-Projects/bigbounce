# P4 R22prov — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 908.2s

---

META-REVIEW — new issues not caught by the five prior referees

P4-META-E1
Severity: ESSENTIAL
Section/page: Appendix A(a–b), pp. 10–11; Sec. IV D (and Abstract)
Why others missed it: Everyone focused on σ inconsistencies but not on the MASTER algebra itself.
Problem: The manuscript claims “MASTER mode-coupling deconvolution removes the leakage,” yet Appendix A(a) explicitly states that the MASTER mode-coupling matrix does NOT include ℓ = 0 on either the input or output side, while the leakage under discussion is precisely monopole (ℓ=0) leakage into ℓ=1. If ℓ=0 is excluded from the coupling matrix, deconvolution cannot remove ℓ=0→ℓ=1 coupling; what actually removes it is the prior monopole subtraction in the data vector, not MASTER per se. This is a methodological contradiction in the chain “monopole leakage → MASTER deconvolution → leakage removed.”
Required fix: Reconcile the pipeline description with the math. Either (a) include ℓ=0 in the coupling matrix and demonstrate that MASTER deconvolution reduces the leaked ℓ=1 when ℓ=0 is retained in the input field, or (b) correct the text to say that “monopole subtraction removes the leakage channel; MASTER then decouples higher-ℓ mask mixing,” and present a test that isolates the effect of monopole subtraction versus deconvolution. Show both cases explicitly on the same catalog and mask.

P4-META-E2
Severity: ESSENTIAL
Section/page: §II.B Training Labels, p. 3
Why others missed it: Reviewers focused on systematics, not book-keeping.
Problem: The training-set composition does not add up. The text lists 6,637 (GZ1) + 17,153 (CE‑ResNet) + 2,000 (synthetic) = 25,790 images, but then states “The combined training set contains 26,636 images.” The 846-image discrepancy is unexplained.
Required fix: Recompute and report exact counts, including any additional sources (duplicates, augmentations saved as separate files, or withheld sets). Add a small table with per-source counts after de-duplication and the split into train/validation.

P4-META-E3
Severity: ESSENTIAL
Section/page: Abstract p. 1; §IV D p. 7; Table IV p. 8; Appendix C p. 12
Why others missed it: Prior reviews noted pLEE ambiguity but not the internal double counting.
Problem: Hemisphere “look-elsewhere” significance is double-counted. The text reports a direct-MC look‑elsewhere pLEE ≤ 10−4 and then further applies Bonferroni/BH over ~650 directions, yielding “post-LEE significance < 1σ.” A direct max-statistic MC already incorporates the look-elsewhere scan; adding Bonferroni/BH constitutes a second, extraneous penalty. Compounding this, Table IV lists a pre‑LEE z = +4.42 while Appendix C quotes 3.05σ for the very same scan, with no reconciliation.
Required fix: Use one and only one LEE correction. Report (i) the raw max-statistic, (ii) the direct-MC LEE‑corrected p-value with its uncertainty, and (iii) the corresponding Gaussian-equivalent σ (specifying one- or two-sided). Reconcile the 3.05σ vs 4.42σ inconsistency by giving the exact estimator, grid, and null used in each case.

P4-META-M4
Severity: MAJOR
Section/page: §VI.A (Sensitivity), p. 9; Abstract p. 1; Table I row (vii)
Why others missed it: They asked for more injections but not the estimator/sample/null mismatch.
Problem: The quoted A50≈0.75% and A95≈1.5–2% thresholds come from injections on the high‑confidence (HC) subsample (N=471,049) under a per‑pixel label‑shuffle null, yet these thresholds are used to frame falsification for the headline real-space dipole estimator on the full sample (N=3.2 M) under an isotropic-bootstrap null. Sensitivity depends on sample size, mask, estimator, and null; mixing all three invalidates the stated A50/A95 as headline thresholds.
Required fix: Repeat the injection–recovery using the exact headline estimator, mask, and null (full Nspiral sample; isotropic-rotation/bootstrap null), and report A50/A95 with uncertainties. If you keep the HC-based thresholds, clearly state they apply only to the HC estimator and do not directly translate to the full-sample headline result.

P4-META-M5
Severity: MAJOR
Section/page: Table III p. 7 and caption; surrounding text §IV C/D
Why others missed it: Focus stayed on σ magnitudes, not dof accounting.
Problem: Table III reports “Joint χ²/dof (38 bandpowers) = 161.2/38,” but the table only shows 1 single-ℓ entry plus 5 bandpowers. The provenance of “38 bandpowers” is neither shown nor referenced (binning scheme, ℓ ranges, mask/weights).
Required fix: Either (a) list all 38 bandpowers (or provide them in a supplementary table) with their ℓ ranges and masks/weights, or (b) remove the χ² line from Table III and place it in an appendix with full details. Ensure the dof match the displayed or referenced bandpowers.

P4-META-M6
Severity: MAJOR
Section/page: Table I row (iv) p. 4; Appendix A(c) p. 11
Why others missed it: They commented on effective fsky, not the sum-of-weights inconsistency.
Problem: Row (iv) (apodized MASTER diagnostic) quotes Nmap weighted = 8,474,531 while also stating that a C2 2° apodization is applied. With apodization, Σp Wp should no longer equal the total object count; quoting the un-apodized sum side-by-side with apodized results is misleading.
Required fix: Report both (i) the geometric fsky of the binary footprint, (ii) the effective fsky after apodization and weighting (⟨W⟩²/⟨W²⟩), and (iii) the sum of the actually used weights Σp Wp (post-apodization), not the catalog count. Amend Table I accordingly.

P4-META-M7
Severity: MAJOR
Section/page: §IV C–D and Table III p. 7; Appendix A(a) p. 11
Why others missed it: Everyone focused on null comparability, not the spectral-noise model.
Problem: No shot-noise (Nℓ) debias is applied to the Ap auto-spectrum; yet absolute Cℓ amplitudes (×10−6 sr) are quoted. Using per-pixel fractions with variable denominators (Nspiral or Nall) induces pixel-dependent sampling noise that biases the auto-spectrum upward. While label-shuffle nulls can provide a significance, the reported Cℓ values are not interpretable as noise‑debiased amplitudes.
Required fix: Provide and subtract an MC-estimated Nℓ (from many label shuffles) or present MASTER results strictly as significance relative to the null, omitting the amplitude unless Nℓ is removed. State clearly which Ap normalization is used in each spectrum.

P4-META-M8
Severity: MAJOR
Section/page: §III C p. 3; Appendix B d. p. 11; §V.B p. 8
Why others missed it: The CE‑ResNet cross‑use was acknowledged but not stress‑tested.
Problem: Potential footprint/systematics imprint via training labels is untested. 67.6% of training labels come from CE‑ResNet predictions on DESI DR8, i.e., drawn from the same survey footprint used for inference. If CE‑ResNet had leg‑dependent biases, they can transfer into the ViT and survive 2‑fold TTA. No “train-on-leg A, test-on-leg B” or sky–jackknife training/evaluation is reported.
Required fix: Perform spatially segregated training/testing (e.g., leave‑one‑leg‑out: train on DECaLS+BASS, test on DES; then rotate). Report performance and chirality fractions per leg. If impractical, show that re‑training with GZ1‑only labels produces consistent headline nulls.

P4-META-M9
Severity: MAJOR
Section/page: §IV C p. 6 vs §IV C/D and Appendix D/E
Why others missed it: They noted mask mismatches generally, not this precise threshold inconsistency.
Problem: The real‑space dipole uses pixels “containing > 10 spiral galaxies,” while the canonical‑mask MASTER analyses use Nspiral(p) ≥ 5. The threshold change is not justified and can alter sky coverage and dipole variance in subtle ways.
Required fix: Harmonize the per-pixel spiral-count threshold across estimators, or show a sensitivity curve for the real‑space dipole versus threshold (e.g., 5/10/20/50), including amplitude, direction, and p-value stability.

P4-META-M10
Severity: MAJOR
Section/page: Abstract p. 1 (“pMC = 0.030, i.e. ≈1.9σ”); also §IV D
Why others missed it: They asked to state sidedness but did not check the mapping numerically.
Problem: The mapping p = 0.030 → “≈1.9σ Gaussian‑equivalent” is only true for a one‑sided conversion. Two‑sided p = 0.03 corresponds to ≈2.17σ. The paper never states sidedness here; the abstract thus understates (two‑sided) significance while elsewhere σ’s are generally treated as two‑sided.
Required fix: State explicitly whether Gaussian equivalents are one‑ or two‑sided. If two‑sided is standard in the paper, correct 1.9σ to ≈2.17σ for p = 0.030.

P4-META-m11
Severity: MINOR
Section/page: Table IV p. 8 vs Appendix C p. 12
Why others missed it: Hemispheric numbers appear in different places with different contexts.
Problem: Hemisphere max-statistic inconsistencies: Table IV reports z = +4.42 for NSIDEdir = 8, while Appendix C states “maximum asymmetry 3.05σ” for the hemisphere scan. They are presented as the same diagnostic but differ by ~1.4σ.
Required fix: Present both numbers in one place with exact definitions (grid, estimator, null, one‑ vs two‑sided), or replace one. A single, consistent hemisphere result should remain in the paper.

P4-META-m12
Severity: MINOR
Section/page: Appendix D(f) p. 13 (WLS fit)
Why others missed it: The focus was on the final z-scores, not the regression design.
Problem: Potential collinearity in the WLS template fit is not addressed (constant term + leg fractions + density and density²). Without reporting condition numbers, orthogonalization, or SVD/ridge handling, the quoted uncertainties and extreme z-values (|z|~250 pre‑bootstrap) could be artifacts of near-collinear design columns.
Required fix: Report design-matrix condition numbers and VIFs; if large, orthogonalize the nuisance templates or regularize the fit. Provide bootstrap/JK diagnostics demonstrating stable parameter posteriors under template re-parameterizations.

P4-META-m13
Severity: MINOR
Section/page: Table I p. 4; Appendix A(c) p. 11
Why others missed it: They noted fsky presentation, but not the nomenclature drift.
Problem: The notation “C2 2° apodization” is undefined and non-standard in PRD context. It is unclear whether this is a cosine‑squared roll‑off with a 2° apodization length, a Tukey window, or something else.
Required fix: Define precisely the apodization kernel and scale (equation or code reference) and ensure the same kernel is used wherever “C2 2°” is cited.

P4-META-m14
Severity: MINOR
Section/page: Data Availability p. 14
Why others missed it: They focused on length and clarity, not repository logistics.
Problem: The catalog “release tag: v2026.04” and model link may not exist at review time (future-stamped), undermining immediate reproducibility.
Required fix: Provide a permanent DOI (e.g., Zenodo) or a time‑stamped tag/commit hash that is already live. If embargoed, supply an internal link to PRD editors or include an archival checksum.

P4-META-m15
Severity: MINOR
Section/page: §IV C–D p. 6–7; Appendix A(a) p. 11
Why others missed it: Discussions centered on null types, not weighting biases.
Problem: The “depth‑stratified null” permutes labels within Nall(p) deciles, preserving only the marginal depth distribution, not the joint spatial/depth structure. Given known leg‑dependent systematics, this null can be anti‑conservative (or over‑conservative) depending on decile geography.
Required fix: Add a spatially constrained null (e.g., shuffle within large HEALPix superpixels and within Nall deciles simultaneously, or within each imaging leg) and report how the ℓ=1 diagnostic changes. This addresses hidden conditioning tied to footprint geometry.

P4-META-m16
Severity: MINOR
Section/page: §III A p. 3; Appendix A(a) p. 11
Why others missed it: They flagged A-definition drift but not the impact on noise statistics.
Problem: Two definitions of Ap are used (spiral‑denominator vs all‑galaxies denominator) with different shot‑noise properties, but the paper never quantifies the induced change in variance and effective fsky across estimators.
Required fix: Introduce explicit symbols (e.g., Asp and Aall) and provide a short derivation or MC demonstrating their different noise levels and how this impacts the quoted σ for each estimator.

## Meta-review recommendation
MAJOR REVISIONS

Considering the union of all six reviews, there are multiple essential and major blockers: a core methodological contradiction in the MASTER/monopole‑leakage chain (E1), a hard accounting error in training-set size (E2), inconsistent and double‑counted hemisphere statistics (E3), and a mis‑matched injection‑recovery sensitivity claim (M4). Additional major issues concern spectrum noise debias, weighting/apodization accounting, and null conditioning relative to footprint geometry. My confidence that the work can survive external peer review is moderate if the authors address these points rigorously; as it stands, the paper requires a careful rewrite, additional controlled tests, and end‑to‑end consistency checks before it is ready for PRD.