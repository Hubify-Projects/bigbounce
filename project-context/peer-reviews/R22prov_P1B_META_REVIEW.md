# P1B R22prov — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 544.0s

---

Meta-referee report on “Technical Verification Companion to the ECH Spin-Torsion Program”

Below are issues I found that none of the five prior referees identified. I focus on end-to-end arithmetic, cross-reference integrity, hidden assumptions, and missing stress tests that materially affect the conclusions.

P1B-META-E1
- Severity: ESSENTIAL
- Section/page: ΛCDM+ΔNeff MCMC configuration (Secs. II–III; V.A; Table I)
- Why missed: All five reviews focused on dataset-version inconsistencies and model-comparison omissions, not on light-element assumptions that directly condition ΔNeff constraints.
- Problem: The helium fraction Yp treatment is never stated. ΔNeff constraints depend sensitively on whether Yp is fixed, BBN-consistent, or free. CAMB/Cobaya can either (i) impose BBN consistency Yp(Ωbh2, Neff) using a specific BBN code/rates, or (ii) fix Yp. The manuscript does not specify which path was used, which BBN engine/version or reaction rates (if any), or whether Yp was freed. This omission makes the headline ΔNeff posteriors not reproducible and potentially biased.
- Required fix: State explicitly the helium prescription used in every ΔNeff run (BBN-consistent vs fixed vs free), the BBN code and version (e.g., PArthENoPE/AlterBBN), the nuclear network settings, and provide a short prior-sensitivity check (e.g., compare ΔNeff posterior width/mean under fixed-Yp vs BBN-consistent assumptions).

P1B-META-E2
- Severity: ESSENTIAL
- Section/page: ΛCDM+ΔNeff MCMC configuration (Secs. II–III; V.A; Table I)
- Why missed: Prior reviews did not probe neutrino-sector assumptions underlying ΔNeff.
- Problem: The neutrino-mass scheme and prior are not specified. ΔNeff constraints depend on the assumed Σmν (and hierarchy or effective mass splitting). CAMB’s defaults (e.g., one massive + two massless, Σmν = 0.06 eV) vs different schemes (three degenerate, varied Σmν) alter H0/ns/ΔNeff degeneracies. Without stating Σmν, number of massive species, and priors, the ΔNeff results lack necessary context.
- Required fix: Document the neutrino-mass model (number of massive species, hierarchy assumption), the prior and value for Σmν (fixed vs sampled), and quantify the ΔNeff sensitivity to this choice (e.g., a brief comparison chain or citation to a validated setting).

P1B-META-E3
- Severity: ESSENTIAL
- Section/page: Table II, “Age [Gyr] 13.763 ± 0.019”
- Why missed: Other reviewers focused on wpivot algebra; none sanity-checked the Age error bar against the reported H0 uncertainty and w0wa freedom.
- Problem: The quoted Age uncertainty (±0.019 Gyr) is implausibly small for a w0–wa fit with H0 = 67.185 ± 0.455 km/s/Mpc. A 0.67% fractional H0 error alone would induce ≳0.09 Gyr Age uncertainty even in ΛCDM; allowing w(z) to vary (w0, wa free) normally widens Age further. The 19 Myr error bar is inconsistent with the rest of the reported posterior widths, suggesting Age was computed under ΛCDM or mis-reported for the w0wa run.
- Required fix: Recompute and report Age from the actual w0wa posterior with proper propagation, or correct the table if a ΛCDM Age was mistakenly inserted. Provide the method (e.g., CAMB background integral per sample) and confirm the uncertainty is consistent with the H0 and w0wa posteriors.

P1B-META-M1
- Severity: MAJOR
- Section/page: Table II, “χ2_BAO 10.6 ± 1.8 (DESI DR2)”
- Why missed: Reviewers flagged dataset mixing but not the goodness-of-fit magnitude.
- Problem: A total χ2 ≈ 10.6 for DESI DR2 BAO appears anomalously low given the number of BAO measurements typically included in DR2 analyses (order tens). Either (i) only a tiny BAO subset is being fit, (ii) χ2 is being reported after internal rescaling/marginalization that is not described, or (iii) there is a bookkeeping error. As written, the χ2 contribution is uninterpretable without the number of BAO data points and the precise likelihood variant.
- Required fix: Specify the exact DESI DR2 BAO data vector (list the entries or point to a manifest), the DOF, and the form of the likelihood (covariance, nuisance treatment). Report χ2/DOF, not just χ2, so readers can assess fit quality.

P1B-META-M2
- Severity: MAJOR
- Section/page: Sec. V.A and Table I footnote (Planck likelihood stack and nuisance parameters)
- Why missed: One reviewer asked for justification of PR4+2018 mixing; none examined calibration-link consistency.
- Problem: The stack mixes Planck PR4 CamSpec high-ℓ TTTEEE with Planck 2018 low-ℓ TT/EE and 2018 lensing while sampling Aplanck and several CamSpec-specific calibration nuisance parameters. This cross-release mix risks inconsistent absolute calibration and beam/window modeling across low-ℓ and high-ℓ likelihoods (Aplanck meaning differs across Plik/CamSpec/PR3 vs PR4). The paper does not document how absolute calibration is tied between PR4 high-ℓ and PR3 low-ℓ+lensing, nor whether duplicate or inconsistent calibration priors are applied.
- Required fix: Document the calibration link explicitly (which likelihood carries Aplanck; how low-ℓ TT/EE and lensing are tied; whether any cross-calibration priors are imposed or disabled). Provide a cross-check run using a fully PR3 stack or a fully PR4-consistent low-ℓ+lensing pair to show negligible calibration-induced shifts in ΔNeff/H0.

P1B-META-M3
- Severity: MAJOR
- Section/page: ΔNeff analysis description (Secs. II–III; V.A; Fig. 2)
- Why missed: Reviewers flagged mislabeled axes and overlays; none checked the ΔNeff prior itself.
- Problem: The prior on ΔNeff (range and form) is not stated. A flat prior on ΔNeff with finite bounds materially shapes posteriors when the result is “consistent with zero.” Without declaring the prior (e.g., uniform on ΔNeff ∈ [−1,3] or similar), the marginal in Fig. 2 cannot be reproduced and the robustness of the “null-consistency” claim cannot be evaluated.
- Required fix: State the ΔNeff prior (type and bounds) used in every run, and add a brief prior-robustness note (e.g., show that widening/narrowing the bounds does not move the mean or 1σ appreciably).

P1B-META-M4
- Severity: MAJOR
- Section/page: Sec. IV, “Foreground and noise model” and pipeline validation scope
- Why missed: Others focused on mask, SNR, map choice; none flagged missing adversarial tests for estimator linearity and sign.
- Problem: No tests of estimator linearity and sign symmetry are shown. The pipeline is validated on only three β injections (0, 0.27°, 0.342°), all positive. Without a grid (e.g., ±0.1°, ±0.2°, ±0.4°) it is not demonstrated that the estimator is linear across amplitude and unbiased with respect to sign under the stated mask/apodization.
- Required fix: Add a small injection grid including negative β values to demonstrate linear, sign-symmetric recovery and to verify that the additive bias remains constant (or quantify any multiplicative component). Report slopes and intercepts with uncertainties.

P1B-META-M5
- Severity: MAJOR
- Section/page: Sec. IV, “E/B leakage and purification” and “Mode-coupling”
- Why missed: Prior reviews did not examine E/B purification choices beyond noting the presence of purify_b.
- Problem: Only B-mode purification is enabled (purify_b=True, purify_e=False). In partial-sky EB estimators, asymmetric purification choices can leave residual E contamination in B and vice versa in bandpowers feeding a rotation estimator. No robustness test is provided for toggling purify_e or using symmetric purification.
- Required fix: Provide a robustness check showing β recovery is stable when enabling purify_e and/or using symmetric purification; quantify any change in bias and variance. If asymmetric purification is intentionally preferred, justify it (e.g., variance reduction) and show it does not induce estimator bias at the 0.04° floor.

P1B-META-M6
- Severity: MAJOR
- Section/page: Sec. IV, “Beam and pixel window. … we degrade to Nside = 512 and apply the corresponding pixel window function.”
- Why missed: One reviewer asked about anti-alias pre-smoothing at downgrade; none noted that the effective beam of Commander is not a simple 5′ Gaussian at 143 GHz.
- Problem: The Commander map’s effective beam is not just “5′ at 143 GHz”; Commander is a component-separated CMB map with its own effective transfer function that is frequency- and algorithm-dependent. Treating it as a simple Gaussian 5′ beam may bias pseudo-Cℓ and EB-derived β unless the actual Commander effective beam is used. The text suggests a 143-GHz beam proxy was assumed.
- Required fix: Replace the 143-GHz Gaussian proxy with the published Commander effective beam (or cite the specific transfer function used) and demonstrate that using the correct beam vs a 5′ Gaussian proxy does not change β recovery beyond the quoted 0.04° floor.

P1B-META-M7
- Severity: MAJOR
- Section/page: Sec. III, “MB–H0 joint-posterior offset check”
- Why missed: Others highlighted the “exactly 3.6σ” wording; none caught the citation mismatch on MB.
- Problem: The MB prior used is repeatedly labeled “H0.riess2020Mb” with MB = −19.253 ± 0.027 mag, yet the H0 prior/reference cited is Riess et al. 2022 (Ref. [7]). Mixing a 2020 MB anchor with a 2022 H0 prior without stating this choice and its justification is inconsistent and can shift the MB–H0 degeneracy audit.
- Required fix: Clarify the exact SH0ES inputs used: specify that the MB prior is from the 2020 calibration (give the proper citation) while H0 is from 2022 (if so), or update both to a single consistent release. Recompute the MB–H0 constant difference with consistent inputs.

P1B-META-M8
- Severity: MAJOR
- Section/page: Sec. IV, choice of ℓ-binning and range (ℓmin = 30, ℓmax = 1024)
- Why missed: Prior reviewers did not request ℓ-range robustness.
- Problem: No robustness test is provided for the choice of ℓmin/ℓmax and Δℓ = 20. The EB-based β estimator’s variance and leakage sensitivity depend on the ℓ-range and binning. Without a sensitivity check (e.g., ℓmin = 20/50; ℓmax = 800/1200; Δℓ = 10/30), the stability of the 0.032°–0.040° bias floor is unverified.
- Required fix: Add a compact robustness table/figure showing β recovery and bias under reasonable ℓ-range/binning variations, with the conclusion that the 0.04° floor is stable.

P1B-META-m1
- Severity: MINOR
- Section/page: Fig. 1 caption and footnote 1 context
- Why missed: Others focused on sample counts; this is a narrower statistical-definition issue.
- Problem: The corner plot includes S8, but neither the definition (S8 ≡ σ8(Ωm/0.3)1/2) nor whether S8 is derived per-sample or imposed via a Gaussian prior (in the full-tension stack) is stated in connection with the figure. This can mislead readers about what is a measured posterior vs a prior-constrained quantity.
- Required fix: In the figure caption or a brief note, state that S8 is derived per sample (formula) and, for the full-tension run, clarify that the DES Y3 S8 prior is active so the plotted S8 includes prior information.

P1B-META-m2
- Severity: MINOR
- Section/page: Sec. IV, SNR definitions (footnote 3)
- Why missed: One reviewer flagged a numerical inconsistency; none pointed out the definition inconsistency.
- Problem: The definitions mix β̂ (recovered mean) in SNRSE and β (injected) in SNRreal, which makes the mapping SNRreal = SNRSE/√N ill-posed if a multiplicative under-recovery exists. Either both should use β̂ (estimator performance) or β (truth-referenced detectability), but not a hybrid.
- Required fix: Adopt a consistent convention (either estimator-centric or truth-centric) for both SNR metrics and recompute the quoted values accordingly; state clearly which is used and why.

P1B-META-m3
- Severity: MINOR
- Section/page: Sec. IV, “Foreground and noise model”
- Why missed: Attention went to Commander-vs-SMICA; this is a modeling subtlety.
- Problem: The pipeline validation uses ACT-like white polarization noise, but does not note that Commander’s pixel-space noise is non-white and anisotropic. For a pure pipeline test this may be acceptable, but the text should acknowledge the simplification and its implication for per-realization σβ scaling.
- Required fix: Add a one-sentence note acknowledging that ACT-level white-noise draws are a simplification relative to Commander-like anisotropic noise, and that the test targets estimator calibration rather than sky realism.

P1B-META-N1
- Severity: NIT
- Section/page: Sec. IV equations for Q+iU rotation
- Why missed: Reviewers focused on higher-level issues.
- Problem: The text “rotate Q+iU via e 2iβ(Q + iU)” appears without a superscript; as written it can be misconstrued as a product. It should be e^{2iβ}(Q + iU).
- Required fix: Typeset the rotation explicitly as (Q + iU) → e^{2iβ} (Q + iU).

Meta-review recommendation
REJECT

Rationale: Considering the union of all six reviews (the five prior referees plus this meta-review), there are multiple essential blockers: incorrect wpivot algebra; dataset-version and figure-label inconsistencies; ambiguous or placeholder citations; mismatched Commander/SMICA labeling; unreported Planck-only chain; inconsistent SNR definitions; unclear ΔNeff prior; unspecified helium and neutrino-mass assumptions; and an implausibly small Age uncertainty in the w0wa fit. Even if scope and novelty concerns were set aside, the methodological and documentation gaps (particularly Yp/Σmν specification and Age error) must be corrected before the results are reproducible and interpretable. My confidence that the paper would withstand external peer review outside the “bigbounce” ecosystem is low given the number and breadth of unresolved methodological issues.