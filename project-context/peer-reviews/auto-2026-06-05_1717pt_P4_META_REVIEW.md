# P4 auto-2026-06-05_1717pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 347.1s

---

P4-META-E1
Severity: ESSENTIAL
Section + page: Abstract p.1; Table I p.4; Appendix A.c p.7
Why others missed it: All five focused on internal arithmetic and null procedures; none sanity-checked fsky against the known DESI Legacy footprint.
Problem: Implausible sky fractions. The paper repeatedly states “fsky = 0.659” for the headline “subsample mask” and “fsky = 0.49005” for the “canonical mask.” DESI Legacy DR8’s imaging footprint is O(10^4) deg^2 (≲ 0.4 of the sky). fsky ≈ 0.66 implies ≈27,000 deg^2, far larger than the DESI Legacy footprint. Quote examples:
- Abstract: “strict-superset subsample mask (n=5,547,858, fsky = 0.659)”
- Sec. IV D: “(fsky = 0.49005, Nspiral = 3,201,160)”
- Appendix A.c: “Analysis subsample mask: fsky = 0.659 … Canonical-N mask: fsky = 0.49005”
Required fix: Provide the actual masked footprint areas (deg^2) and recompute fsky from (# unmasked pixels)/Npix at NSIDE=64. If fsky was accidentally computed as a fraction of galaxies retained rather than area, correct throughout. If the mask includes area beyond DESI LS, explicitly justify why and how (and show the mask image). Update all MASTER results that depend on fsky if the mask changes.

P4-META-E2
Severity: ESSENTIAL
Section + page: Sec. IV D p.5; Appendix A.c p.7
Why others missed it: Reviewers checked pre-MASTER leakage reproduction but not the deconvolution closure itself.
Problem: Missing post-MASTER generative-null closure. The paper claims “MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage,” but only demonstrates that a monopole-only generator reproduces the pre-MASTER pseudo-Cℓ. There is no demonstration that the same monopole-only simulations, run through the identical MASTER pipeline, yield a near-zero deconvolved C1 on either mask.
Required fix: Run the N = 500 (or more) monopole-only realizations through the exact MASTER analysis for both masks and report the deconvolved ℓ=1 null mean and scatter (and compare to the data). Without this, the central claim that MASTER “removes the leakage” is not established.

P4-META-M1
Severity: MAJOR
Section + page: Table I p.4 vs. Sec. IV C p.4
Why others missed it: Everyone examined the real-space estimator’s p-value but not its mask contradiction.
Problem: Mask contradiction for the “none” mask real-space estimator. Table I lists for (i) “real-space dipole … Mask: none.” Yet Sec. IV C states: “We pixelize the sky at NSIDE = 64 … In each pixel p containing > 10 spiral galaxies, we compute Ap …” That is a mask-based selection.
Required fix: Clarify the real-space estimator’s exact mask/selection (pixel threshold, sky coverage), and correct Table I to reflect the mask used. Provide a mask file or precise construction so the +0.43σ, p=0.30 result is reproducible.

P4-META-M2
Severity: MAJOR
Section + page: Abstract p.1; Sec. IV D p.5
Why others missed it: Others flagged finite-MC precision and σ non-comparability, but not the internal inconsistency of dual significance metrics for the same result.
Problem: Mixed significance metrics for the same canonical result. The canonical ℓ=1 result is simultaneously described as “+3.64σ (z = Δ/σnull moment-ratio)” and “empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent.” These are not consistent ways to summarize the same detection and can mislead readers.
Required fix: Choose one primary reporting convention (prefer empirical rank pMC with binomial CI), and present z=(Δ/σnull) only as a descriptive moment ratio, explicitly noting the discrepancy in tail calibration for NMC=500. Interpret the result consistently (it is not “3.6σ” in a frequentist sense if pMC≈0.03).

P4-META-M3
Severity: MAJOR
Section + page: Table III p.5; Table IV p.5
Why others missed it: They checked internal arithmetic but not cross-table unit consistency.
Problem: Unit inconsistency across power-spectrum tables. Table III reports “Cℓ × 10^6 (sr),” while Table IV reports pre-MASTER pseudo-Cℓ values like “1.696×10−2” with no units or scaling. These cannot be compared or interpreted without a clear unit map; the magnitudes differ by orders.
Required fix: Add explicit units to Table IV (and any other power entries). If different normalizations are used (pseudo-Cℓ vs deconvolved Cℓ), state both units and the expected numerical scale relation. Ensure consistent unit usage across tables.

P4-META-M4
Severity: MAJOR
Section + page: Table III p.5 (“Joint χ2/dof (38 bandpowers) = 161.2/38”); Appendix A p.7
Why others missed it: Others questioned missing bin specifics, but not the covariance structure underlying χ2.
Problem: Unspecified covariance in joint χ2. The paper quotes a joint χ2 over 38 bandpowers but does not state whether a full MC covariance (including off-diagonals from mask coupling) was used. Using diagonal variances only would inflate χ2 and the “dominated by mask-coupled monopole” interpretation.
Required fix: Specify the exact covariance matrix used (MC-based, size 38×38), provide its construction (number of realizations, regularization), and recompute χ2 with the full covariance. Supply the covariance (e.g., as a supplemental file) for reproducibility.

P4-META-M5
Severity: MAJOR
Section + page: Sec. IV C Eq. (3) p.4; Appendix A p.7; Sec. II–III p.2–3
Why others missed it: The denominator mismatch was caught elsewhere, but not this orthogonal ambiguity.
Problem: Hard vs. soft counts ambiguity in N(p)CW and N(p)CCW. The text never states whether N values are hard argmax labels or sums of soft probabilities P_eq. This choice materially affects noise, nulls, and map variance.
Required fix: State explicitly whether A_p uses hard counts or probabilistic sums, apply that choice consistently across all analyses, and add a sensitivity test showing that the headline dipole result is stable under the alternative.

P4-META-M6
Severity: MAJOR
Section + page: Sec. VI A p.6
Why others missed it: Others accepted the 2-class mapping; none checked the 3-class implications.
Problem: Dilution factor g = 2a − 1 applied to a 3-class pipeline. The sensitivity mapping assumes binary CW/CCW accuracy a=0.6991, but the actual classifier has a third “not spiral” class and the analysis discards/admits objects based on that. The effective dilution depends on the full 3×3 confusion matrix (including type contamination), not just binary flips.
Required fix: Either (a) compute and report the 3-class confusion matrix and derive the correct mapping from true to observed asymmetry under your selection, or (b) explicitly caveat that g≈2a−1 is an approximation and provide bounds showing the headline sensitivity is robust to plausible 3-class effects.

P4-META-m1
Severity: MINOR
Section + page: Abstract p.1; Sec. III A p.3; Appendix A p.7
Why others missed it: They focused on nomenclature consistency generally, not this contradictory phrase.
Problem: “strict-superset subsample mask” is self-contradictory. A “subsample mask” cannot be a “strict superset” in ordinary usage.
Required fix: Rename to two clearly distinct masks (e.g., “analysis mask” and “canonical mask”), and explicitly state the set relationship between them (subset/superset in area), with a figure of both masks overlaid.

P4-META-m2
Severity: MINOR
Section + page: Sec. II A p.2
Why others missed it: Attention was on downstream analysis, not this upstream reproducibility detail.
Problem: Cross-match procedure under-specified. “Sky coordinates are obtained by cross-matching against the Galaxy Zoo DESI predictions catalog” without a radius, matching key, or duplicate-resolution rule risks positional/ID mismatches that can propagate into the maps.
Required fix: Provide the exact cross-match key(s), angular radius and tie-break policy; report the duplicate rate before/after and its impact (if any) on the final catalog.

P4-META-m3
Severity: MINOR
Section + page: Appendix B.c p.7
Why others missed it: They flagged the need to bound D4 vs Z2 on the full set but not the contradictory magnitudes.
Problem: The D4 hold-out shows mean argmax-CW-fraction shifts of −1.35% and +2.11% on two small sets, yet the text concludes these are “sample-noise.” These shifts are large relative to the 0.75% amplitude sensitivity target and deserve a quantitative bound on the induced dipole.
Required fix: Quantify the maximum induced dipole change between Z2 and D4-TTA on a large representative subset, or bound it analytically. If the effect could masquerade as ∼1% dipole under realistic depth modulation, state that and justify the chosen TTA strategy accordingly.

P4-META-m4
Severity: MINOR
Section + page: Appendix A.a p.7
Why others missed it: Others focused on mask/weight interplay; this is a separate algorithmic detail.
Problem: “the MASTER mode-coupling matrix does NOT include ℓ=0 on either the input or output side.” NaMaster typically handles ℓ ranges explicitly; removing ℓ=0 by pre-subtraction is fine, but excluding ℓ=0 from the coupling matrix should be documented with exact code options and checked for side effects at ℓ=1.
Required fix: Specify the exact NaMaster options used to exclude ℓ=0 (and confirm that no leakage from the removed monopole re-enters ℓ=1 through binning or apodization choices). Provide a short MC demonstration that the ℓ=1 estimate is unchanged by whether ℓ=0 is included in the coupling matrix if the field is mean-subtracted.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential/major blockers: incorrect or implausible fsky values, lack of a post-MASTER generative-null closure test, inconsistent significance reporting for the same canonical result, missing definition of the real-space mask, units inconsistency across tables, unspecified χ2 covariance, and the binary dilution factor applied to a 3-class pipeline. My estimate is ≥10 genuine blockers across reviews (including mine). Confidence that the paper would survive external peer review after addressing all blockers is moderate: the core analysis appears salvageable, but the mask/fsky and closure-test issues must be resolved quantitatively, with corrected numbers and added simulations.