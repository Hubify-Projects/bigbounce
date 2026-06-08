# P1B auto-2026-06-08_1520pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 389.2s

---

Meta-referee report — blind-spot audit

Below are issues that, to the best of my reading, none of the five referees flagged. I focus on end-to-end arithmetic/computational chains, hidden assumptions/conditioning, and reproducibility-critical configuration details.

P1B-META-E1
- Severity: ESSENTIAL
- Location: Sec. IV (NaMaster), pp. 5–6; Abstract p. 1
- Why others missed it: Several reviewers noted sign and amplitude-dependence of the bias, but none diagnosed the bias type.
- Problem: The pipeline “bias” is treated as an additive offset (0.032°–0.040°). The two injections demonstrate a near-constant fractional under-recovery: β̂/β ≈ 0.238/0.270 ≈ 0.882 and 0.302/0.342 ≈ 0.883. That is a ≈−11.7% multiplicative bias (m), not a fixed additive bias (c). Presenting this as an additive 0.03–0.04° bias mischaracterizes the calibration that would be needed on real data and masks the fact that the error scales with the signal amplitude.
- Required fix: Recast the calibration as β̂ = (1 + m) β + c, fit m and c from at least three injected amplitudes, and report both with uncertainties (and their stability vs mask/apodization). Propagate m (not just c) into any stated “systematic floor.”

P1B-META-E2
- Severity: ESSENTIAL
- Location: Sec. IV “Beam and pixel window,” p. 5
- Why others missed it: One reviewer asked for the effective beam/transfer function and downgrade recipe; none connected this to a concrete aliasing/double-application failure mode.
- Problem: The text says “we degrade to Nside = 512 and apply the corresponding pixel window function. NaMaster’s NmtField is initialized with beam = bPlanckℓ wpixℓ.” This is ambiguous and risks double-handling the pixel window and/or omitting the required anti-alias smoothing before downgrade. Without explicit pre-smoothing to the Nside=512 Nyquist and a clear statement of whether wpix is applied to the map or only deconvolved in the likelihood, one can easily induce the observed ~−12% multiplicative bias.
- Required fix: Specify the exact downgrade pipeline (e.g., harmonic-space Gaussian pre-smoothing FWHM, ud_grade or equivalent), state whether wpix was applied to the map or only to the deconvolution, and rerun the MC with a single, self-consistent treatment (pre-smooth to ≥ the target pixel scale; do not double-apply wpix). Report the impact on m and c (see E1).

P1B-META-E3
- Severity: ESSENTIAL
- Location: Sec. III (ΛCDM+ΔNeff MCMC) and Sec. V A (Datasets and configuration), pp. 3 and 6
- Why others missed it: Reviewers focused on dataset naming/citations but not the ΔNeff-specific microphysics settings.
- Problem: The ΔNeff analysis does not state the treatment of primordial helium Yp (BBN consistency vs fixed/free) or the neutrino mass scheme (sum mν and number of massive species). ΔNeff constraints (and the H0 shifts) are sensitive to whether Yp is tied to ΔNeff and ωbh² via BBN consistency. Without this, the ΔNeff posterior is not reproducible and cannot be meaningfully compared.
- Required fix: Declare explicitly: (i) whether BBN consistency is enforced (and which code/relation), or whether Yp is fixed/free (with prior); (ii) the neutrino mass scheme (Σmν value, number of massive/massless species). Provide these in-paper (not only in a repo) for each dataset combination.

P1B-META-E4
- Severity: ESSENTIAL
- Location: Sec. IV (NaMaster), pp. 5–6
- Why others missed it: SNR definition was flagged, but a key null consistency check was not.
- Problem: A constant cosmic rotation generates both EB and TB. The pipeline only reports an EB-based recovery; there is no TB-based estimate, no EB–TB consistency check, and no TB null test. For a rotation estimator on a masked sky, EB and TB consistency is a standard guard against leakage and residual systematics.
- Required fix: Implement and report the TB-based β̂ with the same mask/beam settings, and provide EB–TB consistency (e.g., χ² or difference vs combined estimator). Include a null (β=0) TB test.

P1B-META-E5
- Severity: ESSENTIAL
- Location: Sec. IV (masking choices), p. 5; “Scope note” p. 4; Monte Carlo description p. 5–6
- Why others missed it: Multiple reviewers noted noise/beam issues; none addressed mask selection conditioning.
- Problem: The apodized mask is reported only by fsky = 0.32 and “C2 apodization at 2°.” No rationale, pre-registration, or sensitivity study is provided. Since the reported bias is attributed to the mask/apodization, post-hoc selection of a specific mask/apodization could tune the (m, c) calibration. There is no scan over apodization length, mask threshold, or fsky to demonstrate robustness.
- Required fix: Predefine (or justify) the mask and apodization choices, and provide a sensitivity sweep (e.g., fsky ≈ 0.2–0.6 and apodization 0.5°–3°) showing stability of m and c. If the mask was chosen after seeing the bias, disclose that and report the variation.

P1B-META-M1
- Severity: MAJOR
- Location: Sec. III (Planck likelihood choice) and Sec. V A, pp. 3 and 6
- Why others missed it: Several reviewers flagged dataset inconsistencies but not high-ℓ likelihood choice sensitivity.
- Problem: The analysis fixes the high-ℓ CMB likelihood to CamSpec without justification or cross-check. Different Planck PR4/PR3 high-ℓ likelihoods (CamSpec, Plik, HiLLiPoP) produce measurable shifts in ns, Ωm, σ8, and H0; the ΔNeff posterior width also depends on this choice. No fairness check (e.g., Plik vs CamSpec) is shown.
- Required fix: Either justify the sole use of CamSpec (with a citation to a reproducibility standard) or add a cross-check running at least one alternative Planck high-ℓ likelihood, and quantify the impact on ΔNeff and H0.

P1B-META-M2
- Severity: MAJOR
- Location: Sec. VI (ALP backreaction footnotes and text), pp. 6–7
- Why others missed it: Reviewers discussed fine-tuning but not the small-angle vs large-angle validity of ρa ∝ θi².
- Problem: The backreaction estimate ρa ∼ m² f_a² θ_i² assumes the small-angle harmonic regime (sin θ ≈ θ). The stated prior θ_i ∈ [0.5, 2] rad violates this approximation over most of the prior volume; sin²(θ) deviates O(1) from θ² for θ ≳ 1. Claims about Ωa scaling ∝ θ_i² and the “25×” tuning therefore overstate precision and may be directionally wrong near the upper prior edge.
- Required fix: Replace the small-angle scaling with the exact sin-based expression (or numerical evolution) when discussing backreaction across the stated prior, and recompute the backreaction/tuning statements accordingly.

P1B-META-M3
- Severity: MAJOR
- Location: Sec. VI (ALP ODE integration), p. 6
- Why others missed it: One reviewer noted background choice inconsistency; none asked for redshift-anchoring of β.
- Problem: The β predicted from Δφ/fa depends on the epoch over which the field evolves (recombination to today, or last-scattering to today). The text quotes “from recombination to today” but does not specify the initial condition time/redshift used for θi, nor whether any early-time evolution (z ≫ 1100) is included. For m ~ H0, the phase at z ~ 1100 can shift Δφ/fa by O(10%).
- Required fix: State explicitly the initial redshift for θi, and provide a plot/table of Δφ/fa vs m/H0 for several z_start choices (e.g., z = 1100 and z = 10⁵). Quantify any dependence, or demonstrate insensitivity at the quoted precision.

P1B-META-M4
- Severity: MAJOR
- Location: Sec. III, Table I footnote a, p. 3
- Why others missed it: One reviewer noted mislabeling Mb as “Planck nuisance”; none flagged the missing DES/BAO nuisance accounting.
- Problem: The nuisance-parameter accounting lumps Mb with “Planck likelihood nuisance” and omits any statement about BAO/DES nuisance or covariance parameters (e.g., DESI BAO reconstruction/systematics). It is unclear whether additional nuisance parameters were fixed, marginalized externally, or simply not present. This affects fairness of the parameter count and reproducibility.
- Required fix: Provide a per-likelihood nuisance-parameter list (Planck, BAO, SN), and confirm whether BAO/DES nuisance parameters exist in the stack and how they are treated. Correct the “Planck nuisance” label to separate non-Planck nuisances.

P1B-META-m1
- Severity: MINOR
- Location: Sec. IV (rotation convention), p. 5
- Why others missed it: A reviewer asked for unit conventions; none checked sign conventions explicitly.
- Problem: The rotation is applied as e^{2iβ}(Q+iU) but the sign convention (IAU vs COSMO vs Planck/ACT) is not stated. This affects the sign of EB/TB and the interpretation of β vs α.
- Required fix: State the adopted convention (e.g., Planck/ACT EB convention) and confirm consistency with the likelihoods used elsewhere.

P1B-META-m2
- Severity: MINOR
- Location: Sec. III (lensing likelihood), pp. 3 and 6
- Why others missed it: Dataset labeling concerns focused on DR levels; not on lensing versioning.
- Problem: “lensing.native” is named without version/year. PR3 vs PR4 lensing-likelihood differences are non-negligible; mixing PR4 maps with PR3 lensing has consequences.
- Required fix: Specify the exact Planck lensing likelihood (PR3 vs PR4; native vs bandpower version) and verify it is consistent with the high-ℓ likelihood used.

P1B-META-m3
- Severity: MINOR
- Location: Sec. IV, p. 5–6
- Why others missed it: SNR definition was requested, but not estimator variance accounting.
- Problem: The reported “pipeline SNR” appears to be β_inj/σ(β̂). The sampling error on the mean recovered β̂ across N_MC=500 (i.e., σ/√N_MC) is not given, so the uncertainty on m and c (E1) cannot be assessed.
- Required fix: Report the per-realization σ(β̂), the standard error on the mean across the 500 realizations, and confidence intervals for m and c.

P1B-META-N1
- Severity: NIT
- Location: Sec. IV (bandpower binning), p. 5
- Why others missed it: Considered too low-level.
- Problem: Binning (Δℓ=20) and ℓ-range (30–1024) are stated with no justification or stability check. For rotation, β estimators weight by Cℓ^EE/(S+N); binning choices can bias estimates on a masked sky.
- Required fix: Add a short binning-stability note (e.g., Δℓ=10/20/40; ℓmax = 800/1024) showing negligible change in m, c at the quoted precision.

Meta-review recommendation
REJECT

Rationale: Even aside from the substantial issues already raised by the five referees (nonexistent references, internal arithmetic errors, dataset mislabeling, scope/title mismatch), the additional essential problems above strike at the core reproducibility and validity of the two main analyses: (i) the ΔNeff MCMC lacks the BBN/Yp and neutrino-mass specifications required to interpret or reproduce the posteriors; and (ii) the NaMaster “bias-injection” analysis mis-models the calibration (multiplicative vs additive), uses an ambiguous downgrade/pixel-window procedure that likely induces the observed ≈−12% multiplicative bias, and omits the standard TB cross-check. These are not cosmetic fixes; they require re-analysis.

Given the union of all six reviews, I count well over a dozen load-bearing blockers (≥6 essential from prior reviews, plus the five essentials above), including fabricated or future-dated citations and an explicit arithmetic error in a key footnote. My confidence that the paper, as currently constructed, would survive external peer review unrelated to the “bigbounce” program is very low. A future submission could be viable if it (i) becomes fully self-contained and citable, (ii) corrects the statistical and calibration errors, and (iii) reframes its scope to match what is actually analyzed.