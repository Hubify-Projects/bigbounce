# P1B auto-2026-06-06_0021pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 374.3s

---

Meta-review: new issues none of the five referees caught

P1B-META-E1
- Severity: MAJOR
- Section/page: Table II and surrounding text (p. 4); Sec. V.B (p. 6)
- Why others missed it: Reviewers focused on dataset labeling and significance statements, not on parameter-definition completeness.
- Specific problem: The paper reports wpivot = −1.0344 ± 0.0301 “−1.1σ from −1” but never defines the pivot redshift zp or the construction of wpivot (e.g., decorrelation procedure, choice of zp, dependence on the chosen dataset stack).
- Required fix: Add a precise definition of wpivot, the method used to determine the pivot redshift (and its value), and demonstrate robustness of wpivot to reasonable changes in zp for the given likelihood stack.

P1B-META-E2
- Severity: ESSENTIAL
- Section/page: Sec. III/Table I (pp. 2–3), Fig. 1 (p. 5)
- Why others missed it: Attention was on convergence counts and dataset names; the prior structure for ΔNeff was not examined.
- Specific problem: The prior on ΔNeff is never stated. Since ΔNeff is often constrained to be ≥ 0 (physical “extra” radiation) but many analyses allow ΔNeff < 0 as a phenomenological extension, the absence of an explicit prior specification makes the reported ΔNeff posterior (centered near zero, spanning negatives) uninterpretable with respect to prior dependence.
- Required fix: State the exact prior on ΔNeff (type and bounds). If negative values are allowed, justify physically and report how the inferred mean/σ change under a nonnegative prior; otherwise, re-run with a clearly documented prior reflecting the intended physical interpretation.

P1B-META-E3
- Severity: MAJOR
- Section/page: Appendix C (p. 9), Sec. VI (pp. 6–7)
- Why others missed it: Reviewers challenged the spectator prior on θi, but not the adequacy of sampling itself.
- Specific problem: The ALP MCMC uses only 9,720 accepted samples across three configurations (≈3,240 per configuration) yet claims R̂ − 1 < 0.01. No number of chains, per-chain lengths, or trace/density diagnostics are shown. Achieving R̂ < 0.01 with ~3k samples per configuration is unlikely without multiple well-mixed chains; under-sampling risks unstable posteriors and unreliable uncertainties.
- Required fix: Report the number of chains per configuration, per-chain lengths, and standard convergence diagnostics (trace plots, autocorrelation times, effective sample sizes per parameter). If necessary, increase samples and re-run to demonstrate stable posteriors and R̂ < 0.01.

P1B-META-E4
- Severity: MAJOR
- Section/page: Sec. IV (pp. 5–6)
- Why others missed it: They critiqued estimator definition and noise model but not calibration-angle conditioning.
- Specific problem: Hidden conditioning on polarization-angle calibration. All β-injection MCs implicitly set the instrument polarization-angle miscalibration α to zero and do not marginalize over α. Because EB-based birefringence is exactly degenerate with α in CMB-only analyses, the quoted “systematic floor” (0.032–0.040°) cannot be generalized to real data where α ≠ 0 and is uncertain; any coupling of α with mask-induced EB can bias β.
- Required fix: Introduce calibration-angle nuisance parameters (α per experiment) with realistic priors/covariances in the MC and report how the β bias and variance change when marginalizing over α. Alternatively, state explicitly that the reported floor is conditional on α=0 and is not a detector-calibration-aware systematic bound.

P1B-META-M5
- Severity: MAJOR
- Section/page: Sec. IV (p. 5), “E/B leakage and purification” and mask paragraph
- Why others missed it: They flagged beam and aliasing but not selection effects for the apodization.
- Specific problem: Possible post-hoc selection of the apodization scale (C2, 2°) without a pre-registered rationale. The reported bias (0.032–0.040°) depends sensitively on mask apodization; selecting a single 2° value without a scan risks underestimating the method’s true systematic envelope.
- Required fix: Scan apodization types/scales (e.g., C2/C1 at 0.5°, 1°, 2°, 3°) and report β̂ bias vs. apodization. Define and adopt a pre-registered choice or marginalize over mask choices to quote a robust systematic floor.

P1B-META-M6
- Severity: MAJOR
- Section/page: Sec. IV (pp. 5–6)
- Why others missed it: Focus remained on EB-only estimator definition and SNR accounting, not on complementary estimators.
- Specific problem: No TB–EB cross-check. For isotropic birefringence, TB and EB carry essentially the same rotation signal (with different noise/systematics couplings). A TB-based β estimator is a standard control; omitting it weakens the method validation.
- Required fix: Implement a parallel TB-based β estimator in the same NaMaster framework and demonstrate consistency with EB across the three injection levels, including bias and variance comparisons.

P1B-META-M7
- Severity: MINOR
- Section/page: Table II (p. 4)
- Why others missed it: They checked arithmetic but not interpretability of χ² numbers.
- Specific problem: χ² contributions are quoted without degrees of freedom or a clear definition (is “χ²” actually −2 ln L for each likelihood?). For example, “χ² BAO 10.6 ± 1.8” is not interpretable without Npoints and the precise definition used.
- Required fix: For each likelihood block, state whether “χ²” is truly χ² or −2 ln L, and list the approximate number of data points (or effective dof). Add a sentence explaining how the block-wise means/variances are computed from the posterior.

P1B-META-M8
- Severity: MAJOR
- Section/page: Sec. III, footnote 2 (p. 3)
- Why others missed it: They focused on dataset/likelihood hygiene rather than torsion EFT details.
- Specific problem: The strong-coupling scale for torsion is written “Λstrong ∼ MPl/√γBI set by the inverse Barbero–Immirzi parameter γBI.” This is dimensionally and conceptually unclear: γ (the Immirzi parameter) is dimensionless, and calling γBI “inverse Barbero–Immirzi parameter” while using γBI (not 1/γ) in the denominator is contradictory. No citation is provided for this exact scaling.
- Required fix: Provide a correct, cited expression for the torsion strong-coupling (or cutoff) scale consistent with the Holst sector and the four-fermion operator matching, with explicit dependence on γ and κ. If the scale is only schematic, label it as such and remove misleading “inverse” phrasing.

P1B-META-m9
- Severity: MAJOR
- Section/page: Table II (p. 4)
- Why others missed it: Arithmetic was checked but plausibility was not questioned.
- Specific problem: The quoted Age = 13.763 ± 0.019 Gyr for a w0–wa extension with multiple datasets is implausibly tight. In extended DE models, age usually degrades relative to ΛCDM; ~0.019 Gyr (≈19 Myr) suggests the age may have been computed under ΛCDM assumptions or with incomplete covariance propagation.
- Required fix: Document how Age is computed (derived parameter formula and code path) and verify that full parameter covariance, including w0 and wa, is propagated. Provide a validation plot showing Age uncertainty vs. ΛCDM and confirm that 0.019 Gyr is not an artifact.

P1B-META-m10
- Severity: MINOR
- Section/page: Sec. III, “MB–H0 joint-posterior offset check” (pp. 4–5)
- Why others missed it: They checked the arithmetic but not the dimensional form.
- Specific problem: The paper states “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const.” The SN degeneracy is defined with h ≡ H0/(100 km s−1 Mpc−1) (i.e., MB − 5 log10 h), not H0; using H0 changes the constant and can confuse units.
- Required fix: Recast the relation in terms of MB − 5 log10 h and state explicitly that the constant shift cancels in differences; clarify units so readers can reproduce the numbers unambiguously.

P1B-META-m11
- Severity: MINOR
- Section/page: Sec. IV (pp. 5–6); Sec. VI (pp. 6–7)
- Why others missed it: Focus was on estimator mathematics and dataset labels, not sign conventions.
- Specific problem: The sign convention for β is not defined (e.g., IAU polarization angle convention, positive rotation direction) and no check with negative-β injections is shown. This leaves ambiguity in comparing signs across Planck, ACT, and the MC injections.
- Required fix: State the polarization-angle convention used (IAU/HEALPix), define the sign of β and α, and add a negative-β injection to demonstrate sign handling and linearity.

P1B-META-m12
- Severity: MINOR
- Section/page: Sec. III (p. 5), “Independent cross-validation.”
- Why others missed it: They asked for numbers, but not for fairness of the comparison.
- Specific problem: The paper compares its ΛCDM+ΔNeff proxy results to Liu et al.’s torsion cosmology and claims agreement at 0.5σ in H0 and 0.4σ in σ8. This is an apples-to-oranges comparison across different models and likelihood stacks; such numerical proximity is not a validation.
- Required fix: Reframe this as a rough consistency check with caveats about different model spaces and datasets, or remove the σ-level comparison entirely.

P1B-META-m13
- Severity: MINOR
- Section/page: Sec. III (p. 3), “a. Scope of the ΔNeff proxy…”
- Why others missed it: Attention was on ΔNeff posterior results.
- Specific problem: The claim “The minimal matter-bounce class… predicts ΔNeff ≈ 0 by construction” is not supported by the cited reference [10], which is about non-Gaussianity, not ΔNeff. A dedicated citation is needed.
- Required fix: Cite a source that actually demonstrates ΔNeff ≈ 0 for the stated minimal matter-bounce class, or soften the statement to a qualitative expectation and remove the “by construction” language.

P1B-META-m14
- Severity: MINOR
- Section/page: Sec. IV (p. 5–6)
- Why others missed it: They critiqued low-noise choice but not noise anisotropy/ℓ-dependence.
- Specific problem: The MC uses white, isotropic ΔP = 10 μK·arcmin noise. Real Planck/ACT noise is anisotropic and ℓ-dependent. The bias floor and SNR can depend on anisotropy, especially with purification and masking.
- Required fix: Add a test with an anisotropic/ℓ-dependent noise model representative of Planck and/or ACT (or cite a study showing negligible impact on β̂ bias at the reported scales).

P1B-META-m15
- Severity: MINOR
- Section/page: Sec. IV (p. 5)
- Why others missed it: They questioned the beam choice but not its uncertainty propagation.
- Specific problem: No propagation of beam or pixel-window uncertainties into the β response. Even if the effective beam choice is justified, ignoring beam uncertainty prevents a complete systematics budget for the claimed 0.032–0.040° floor.
- Required fix: Include beam (and pixel-window) uncertainty in the response calibration, or bound its effect by sensitivity tests; incorporate it into the quoted systematic floor if non-negligible.

P1B-META-m16
- Severity: MINOR
- Section/page: Sec. IV (p. 5–6)
- Why others missed it: Estimator definition critiques didn’t mention mask-induced EB mean fields.
- Specific problem: Pseudo-Cℓ EB on a cut sky can have a non-zero mask-induced mean. The paper does not mention estimating/subtracting an EB mean field from simulations before fitting β, which can bias β̂ at O(10−2 deg) depending on mask/apodization.
- Required fix: Explicitly estimate the EB mean field from the MC ensemble and subtract it (or show it is negligible relative to the 0.032–0.040° bias).

## Meta-review recommendation
REJECT

Given the union of all six reviews, the manuscript faces multiple essential and major issues: bibliographic integrity problems (non-existent references), inconsistent dataset/likelihood attributions, underspecified estimators/likelihoods, arithmetic inconsistencies, and numerous methodological omissions. The additional blind spots identified here (missing ΔNeff prior, undefined wpivot/zp, calibration-angle conditioning in MC, dubious age precision, unclear torsion cutoff scaling, insufficient ALP MCMC sampling, and lack of key EB/TB/apodization robustness tests) further erode confidence. Blockers: at least 10 essential/major issues across physics, statistics, and documentation. Confidence of surviving an external, independent PRD review without a substantial rewrite is low.