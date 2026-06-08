# P4 auto-2026-06-08_1354pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 420.1s

---

P4-META-E1
Severity: ESSENTIAL
Section + page: Table III (p. 5) vs. Table IV (p. 5)
Why others missed it: Several reviewers flagged general unit issues for Cℓ, but none compared the absolute scales across tables.
Specific problem (quote the text): 
- Table III header: “Cℓ × 10^6 (sr)” with ℓ = 1 giving 1.494 × 10^−6.
- Table IV first row: “Pre-MASTER pseudo-C(ℓ=1)ℓ (canonical mask) 1.696×10^−2”.
These two ℓ=1 “Cℓ” numbers differ by four orders of magnitude, yet are discussed as if they measure the same quantity; the normalization and/or definition have changed without disclosure (e.g., inclusion of ℓ(ℓ+1)/2π, different field normalization, or different map definition).
Required fix: State explicitly and consistently the exact definition and normalization of every “Cℓ” reported (pseudo vs. deconvolved; whether multiplied by ℓ(ℓ+1)/2π; what field normalization is used). Add a column indicating the normalization used in each table and reconcile the apparent 10^4 discrepancy. If Table IV is reporting a different statistic, rename it and define it precisely.

P4-META-E2
Severity: ESSENTIAL
Section + page: Abstract (p. 1) and Sec. IV C.b (p. 4–5)
Why others missed it: Reviewers noted significance reporting issues but not this terminology contradiction.
Specific problem (quote the text): “MASTER-deconvolved single-mode pseudo-C1 … yields −0.122σ.” Pseudo-Cℓ refers to the masked (not deconvolved) spectrum; once MASTER deconvolution is applied it is no longer “pseudo.” 
Required fix: Correct the terminology throughout: use “pseudo-Cℓ” for masked (pre-deconvolution) spectra and “MASTER-deconvolved Cℓ” (or simply Cℓ) for deconvolved quantities. Fix the abstract and any other locations where “deconvolved pseudo-Cℓ” is used.

P4-META-E3
Severity: ESSENTIAL
Section + page: Sec. IV D, footnote 1 (p. 4)
Why others missed it: Others flagged the “in queue” rerun, but not the internal logical contradiction specific to pre-MASTER quantities.
Specific problem (quote the text): “A parallel rerun on N(all)-trial draws … is expected to shift … with a sub-0.1σ effect on the headline pre-MASTER reproduction figure because mode-coupling decoupling absorbs the trial-count normalization.” Deconvolution (mode-coupling) cannot “absorb” normalization for a pre-MASTER (masked) statistic; the justification is internally inconsistent with the stated pre-MASTER target.
Required fix: Remove the claim that MASTER deconvolution affects a pre-MASTER statistic. Either run the N(all)-trial generative null and report its actual impact on the pre-MASTER reproduction, or provide a correct analytic variance argument for why N(all) vs. N(spiral) has negligible effect on the specific pre-MASTER leakage observable.

P4-META-M1
Severity: MAJOR
Section + page: Abstract (p. 1) vs. Appendix A (p. 7)
Why others missed it: Prior reviews noted null-procedure ambiguity generally, but not this within-channel inconsistency for the same mask/result.
Specific problem (quote the text):
- Abstract: “+3.64σ … 500-MC binomial per-pixel-shuffle null.”
- Appendix A: “Null distribution: 500 per-pixel random-label permutation realizations.”
The canonical-mask post-MASTER residual’s significance is reported against two different null families (binomial draws vs. permutation), yet the numbers are compared as if interchangeable.
Required fix: Use a single, well-defined null for each estimator and mask throughout the paper. For the canonical-mask post-MASTER residual, pick one (binomial or permutation), justify it, and recompute all quoted σ and p-values under that null. If both are shown, present them side-by-side and discuss any differences.

P4-META-M2
Severity: MAJOR
Section + page: Sec. IV D (p. 5) and Appendix D.f (p. 9)
Why others missed it: Reviewers noted extreme z-scores but not the missing mapping that underlies the 1.7% amplitude benchmark.
Specific problem (quote the text): 
- “Interpretation (i) … a clean real cosmological dipole at amplitude ∼ 1.7%.”
- “the joint fit recovers Abest_dipole = 4.55×10^−3 (0.23% in fCW units), with the interpretation (i) reference amplitude 1.7% at z = −264.5…”
No derivation is provided for converting from the measured C1 (or regression coefficients) to a sky-dipole amplitude in percent. The 1.7% figure is used repeatedly as a reference without a formula connecting C1 and A_dipole, nor is the A↔C1 mapping stated anywhere.
Required fix: Provide the explicit formula relating a real-space dipole amplitude A (in fraction or percent units) to C1 under your field definition, mask, and weighting (e.g., C1 ≈ 4π A^2/9 for full sky, modified by MASTER coupling on a cut sky). Show how 1.7% is obtained from your measured canonical-mask C1, and recompute all amplitude-based z-scores accordingly.

P4-META-M3
Severity: MAJOR
Section + page: Appendix C.c (p. 8)
Why others missed it: Others discussed LEE handling but did not assess grid-phase dependence of the hemisphere scan.
Specific problem (quote the text): “Testing all hemisphere-pairs at 10° increments: maximum asymmetry 3.05σ.” The maximum-hemisphere statistic is sensitive to the choice and phase of the scan grid; no robustness test is reported for rotations or refinements of the hemisphere-center grid.
Required fix: Demonstrate grid-phase robustness of the hemisphere search by repeating the scan with (i) rotated HEALPix NSIDE=8 grids and (ii) a denser grid (e.g., NSIDE=16) and showing stability of the max-statistic under the same null. Report any changes in max |A| and in the (r+1)/(N+1) MC p-value.

P4-META-M4
Severity: MAJOR
Section + page: Sec. IV C (p. 4–5); Appendix A (p. 7)
Why others missed it: Weighting-mismatch was noted, but not the specific bias introduced by using N_all weights in the monopole subtraction for an Ap field defined on spirals only.
Specific problem (quote the text): “The NaMaster weight (mask) map assigns Wp = N_all(p)… The asymmetry field is Ap = (NCW − NCCW)/(NCW + NCCW)… The galaxy-weighted mask-mean ⟨A⟩mask,gw is subtracted before field construction.” Using Wp = N_all to compute the mean of Ap (which has binomial variance proportional to N_spiral, not N_all) yields a biased/unoptimal monopole estimator if depth (hence N_all) correlates with Ap through systematics.
Required fix: Recompute the monopole subtraction using Wp = N_spiral (or analytically optimal inverse-variance weights for Ap), and quantify the impact on C1 and σnull for both the subsample and canonical masks. If results materially change, standardize on the variance-appropriate weighting and update all affected conclusions.

P4-META-M5
Severity: MAJOR
Section + page: Sec. IV C (p. 4) and Appendix A (p. 7)
Why others missed it: Null clarity was criticized, but not resolution dependence.
Specific problem (quote the text): The analysis fixes NSIDE = 64 throughout; no robustness to changing angular resolution is reported. Given the per-pixel minimum (≥10 spirals) and depth variations, estimator stability can depend on NSIDE.
Required fix: Provide an NSIDE robustness test (e.g., NSIDE = 32 and 128) for the two primary estimators (real-space dipole and subsample-mask MASTER C1). Report any change in C1, σnull, and z to demonstrate stability against pixelization scale.

P4-META-m1
Severity: MINOR
Section + page: Sec. IV B (p. 4)
Why others missed it: Others challenged the suppression factor numerics; this adds a missing-coordinates angle.
Specific problem (quote the text): “The Catalog C residual … is spatially uniform across 7 equatorial coordinate slabs…” Testing “uniformity” in equatorial slabs alone is not coordinate-agnostic, and survey systematics align with equatorial, Galactic, and ecliptic frames differently.
Required fix: Repeat and report the slab uniformity test in Galactic and ecliptic coordinates (same number of slabs and thresholds). If results differ materially across frames, discuss implications for the monopole–mask leakage interpretation; otherwise, state the uniformity is frame-robust.

P4-META-m2
Severity: MINOR
Section + page: Sec. III C (p. 3)
Why others missed it: Prior reviews focused on calibration but not on the exactness claim.
Specific problem (quote the text): “This procedure enforces flip-equivariance of the output protocol (flip-swap correlation = 1.000).” TTA enforces equivariance at the protocol level, but only up to floating-point and model stochasticity; claiming exactly 1.000 correlation suggests it was computed on the constructed outputs rather than independently.
Required fix: Clarify how the “1.000” correlation was computed (population, numerical precision). Replace the exactness claim with a tolerance-bound statement (e.g., r ≥ 0.9999 on the evaluation set) and provide the sample size.

P4-META-m3
Severity: MINOR
Section + page: Sec. II A (p. 2)
Why others missed it: Others did not examine provenance/selection-chain rigor for the parent dataset.
Specific problem (quote the text): “Our parent sample is the Smith42/galaxies dataset on HuggingFace… The parent-sample selection function inherits from Galaxy Zoo DESI: photometric types REX/DEV/EXP/SER, r ≤ 19.0, half-light radius ≥ 3″.” It is unclear whether the HuggingFace dataset strictly enforces those cuts (selection inherited by reference), or if they were re-applied/verified in this work.
Required fix: Document explicitly how the selection function was enforced on the Smith42/galaxies dataset (including any re-selection by DR8 metadata) and quantify any deviations from the Galaxy Zoo DESI cuts (e.g., counts and percentages failing each cut if re-applied).

P4-META-m4
Severity: MINOR
Section + page: Appendix C.e (p. 8) vs. Sec. IV A (p. 4)
Why others missed it: Others noted odd confidence statistics but not this internal tension.
Specific problem (quote the text): “Mean classification confidence is 0.951, median 0.9997.” Later: “The +3.3σ signal in the 1.87M-galaxy [0.5, 0.6) confidence bin…” Having ~1.87M objects at confidence 0.5–0.6 coexisting with a median of 0.9997 over 8.47M suggests a highly bimodal distribution; the population (all classes vs. spirals-only) used for each statistic is not stated.
Required fix: State for each confidence statistic the population used (all classes vs. spirals-only) and provide a confidence histogram (or quantiles) by class so the apparent bimodality can be assessed.

P4-META-N1
Severity: NIT
Section + page: Sec. III B (p. 3)
Why others missed it: Focus was on architecture accuracy, not notation style.
Specific problem (quote the text): “LayerNorm → 384→512 … → 256→3 (softmax). (1)” This is an architecture block, not an equation; numbering it as Eq. (1) is misleading.
Required fix: Remove the equation number for the architecture block or relabel it as a figure/listing.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple blockers: (i) unresolved contradictions in the definition/normalization of the analyzed field and its spectra; (ii) inconsistent null procedures applied to the same diagnostic; (iii) contradictory or imprecise significance reporting (moment-based z vs. permutation p); (iv) undisclosed/post-hoc mask choices; (v) arithmetic inconsistencies; and (vi) several missing robustness tests (grid-phase for hemispheres, NSIDE dependence, coordinate-frame uniformity). I count at least 10 essential/major issues (including those raised by the other referees) that must be fixed. My confidence that the paper would survive external, non-project peer review after addressing these is moderate: the core analysis appears sound, but the presentation and statistical hygiene need a thorough, disciplined cleanup and some recomputations to meet PRD standards.