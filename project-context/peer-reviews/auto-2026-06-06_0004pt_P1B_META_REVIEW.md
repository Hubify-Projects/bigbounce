# P1B auto-2026-06-06_0004pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 335.1s

---

P1B-META-E1
- Severity: ESSENTIAL
- Section + page: Sec. IV (Data Methods: CMB E-B Analysis), pp. 5–6
- Why others missed it: Prior reviews challenged SNR definition and beam/mask details but did not notice the Monte Carlo only varies instrument noise, not the CMB sky.
- Specific problem (quote): “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin… The β = 0.27°, β = 0.342°, and β = 0 injections rotate Q+iU via e^{2iβ}(Q+iU) before adding noise.”
- Required fix: State explicitly whether CMB realizations are resampled or a single fixed Commander map is used. If the latter, re-run the MC with full-sky CMB realizations (sampling cosmic variance) and report per-realization σβ including cosmic variance. Recompute SNR accordingly and clarify that prior SNRs were noise-only forecasts on a fixed sky, not single-sky detectability.

P1B-META-E2
- Severity: MAJOR
- Section + page: Sec. IV (E/B leakage and purification), p. 5
- Why others missed it: Reviewers requested estimator details and bias uncertainties but did not connect B-mode purification to potential removal of the rotation signal itself.
- Specific problem (quote): “We use NaMaster’s spin-2 B-mode purification (purify_b=True, purify_e=False) to suppress E→B leakage…”
- Required fix: Demonstrate that B-purification does not subtract part of the uniform-rotation–induced E→B signal (which is the target). Provide a comparison showing β-recovery with purify_b toggled on/off and, if needed, purify_e toggled, quantifying any amplitude suppression. If purification biases β, adopt an unbiased configuration or correct the bias with a calibration curve and uncertainty.

P1B-META-E3
- Severity: ESSENTIAL
- Section + page: Sec. III (ΛCDM+ΔNeff MCMC), pp. 2–4; Sec. V.A (Datasets and Configuration), p. 6; Table I, p. 3
- Why others missed it: They focused on dataset versions and nuisance parameters, not the ΔNeff–Yp coupling.
- Specific problem (quote): No mention anywhere of the treatment of primordial helium Yp when sampling ΔNeff.
- Required fix: Specify whether BBN consistency is enforced (Yp = YpBBN(ωb, ΔNeff)) or Yp is fixed/freely sampled. This choice materially affects ΔNeff and H0 posteriors. Provide results under the adopted assumption and, ideally, a sensitivity run with the alternative assumption (BBN-consistent vs free Yp), or justify why one is mandated.

P1B-META-E4
- Severity: ESSENTIAL
- Section + page: Sec. III (ΛCDM+ΔNeff MCMC), pp. 2–4; Sec. V.A, p. 6; Table I, p. 3
- Why others missed it: Neutrino mass priors were not discussed by previous reviewers.
- Specific problem (quote): No statement of Σmν prior/treatment in ΔNeff runs.
- Required fix: Declare the assumed neutrino mass model (e.g., minimal normal hierarchy with Σmν = 0.06 eV fixed or a prior on Σmν). Explain how this interacts with ΔNeff constraints and S8. If Σmν is free, provide its posterior; if fixed, justify.

P1B-META-E5
- Severity: MAJOR
- Section + page: Sec. III (footnote a, Table I), p. 3
- Why others missed it: Prior reviews flagged misclassification of Mb as “Planck nuisance,” but not the A_planck applicability to PR4/NPIPE CamSpec.
- Specific problem (quote): “10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb…”
- Required fix: Clarify whether “A_planck” (a PR3 Plik-style absolute calibration parameter) is actually present in the PR4/NPIPE CamSpec stack used here. List the exact nuisance parameters for the precise high-ℓ likelihood (with release and code reference). Remove or correct A_planck if it is not in the active likelihood and update parameter counts accordingly.

P1B-META-E6
- Severity: MAJOR
- Section + page: Sec. IV (Independent verification), pp. 5–6
- Why others missed it: They questioned SNR and bias but not the baseline sky choice for injection.
- Specific problem (quote): “The Planck Commander Q/U maps are provided… we degrade to Nside = 512… Injecting… rotates Q+iU via e^{2iβ}(Q+iU) before adding noise.”
- Required fix: Acknowledge that injecting on a real sky may add rotation on top of an unknown baseline β (and possible α). Either (i) zero out EB on the base map before injection, (ii) switch to synthetic CMB simulations with known β=0 baselines, or (iii) report β̂−βinj (not β̂ alone) and include the βinj=0 mean as the baseline. Provide the quantitative null-injection mean and scatter.

P1B-META-E7
- Severity: MAJOR
- Section + page: Sec. IV (Mask and apodization), p. 5
- Why others missed it: The mask choice was not interrogated for post-hoc selection effects.
- Specific problem (quote): “The mask uses C2 apodization at 2° scale… fsky = 0.32…”
- Required fix: Justify the specific mask and apodization scale a priori or show robustness: repeat the recovery for at least two alternative apodization scales (e.g., 1°, 3°) and a different sky fraction, and tabulate β-bias and σβ. State whether the mask was pre-specified or tuned; if tuned, explicitly mark results as exploratory.

P1B-META-E8
- Severity: MINOR
- Section + page: Sec. V.A (Software versions), p. 6; Sec. III (top), p. 3
- Why others missed it: They flagged versioning generally, but not this internal inconsistency.
- Specific problem (quote): “Cobaya v3.5 original; v3.6.1 verification” vs. earlier “Cobaya v3.6.1… two frozen dataset combinations…”
- Required fix: Harmonize the Cobaya version across the manuscript. If results differ between v3.5 and v3.6.1, state which results come from which version and whether sampler or likelihood API changes affect posteriors.

P1B-META-E9
- Severity: MINOR
- Section + page: Sec. III (MB–H0 degeneracy paragraph), p. 4
- Why others missed it: They focused on the “exactly” wording and significance, not the degeneracy form.
- Specific problem (quote): “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const along the SN distance-modulus degeneracy.”
- Required fix: Write the standard degeneracy precisely (MB − 5 log10 h, with h ≡ H0/100 km s−1 Mpc−1) and note any additive constants implicit in the definition of μ. Recompute the stated constants with the same convention and update the significance accordingly.

P1B-META-M1
- Severity: MAJOR
- Section + page: Sec. IV (Noise model and “worst-case” claim), p. 5
- Why others missed it: One reviewer noted the “worst-case” inconsistency qualitatively but did not identify the root cause.
- Specific problem (quote): “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check).”
- Required fix: Explain how “ACT-like” uniform white noise is combined with a Planck Commander base map with different resolution/noise and why this is “worst-case” for bias. If the base map’s own noise is non-negligible, include it or justify its omission. Provide the resulting Nℓ (after beam/pixel) used in the β estimator so that “worst-case” can be quantitatively assessed.

P1B-META-M2
- Severity: MAJOR
- Section + page: Table II and Sec. II–V (w0–wa chain), pp. 2–6
- Why others missed it: Prior reviews discussed structure/integration, not the statistical conditioning.
- Specific problem (quote): The w0–wa results are given without specifying whether curvature Ωk, relativistic species ΔNeff, and Σmν are fixed or varied jointly during that run (Table II only lists w0–wa “extension”).
- Required fix: Fully specify the parameter hyper-surface for the w0–wa chain (Ωk fixed to 0? ΔNeff fixed to 0? Σmν fixed to 0.06 eV?) and summarize priors. Provide a short sensitivity table showing how w0, wa shift under (i) BBN-consistent vs free Yp, (ii) fixed vs free Σmν (within reasonable priors), and (iii) with/without the SH0ES MB prior.

P1B-META-m1
- Severity: MINOR
- Section + page: Sec. IV (Estimator inputs), p. 5–6
- Why others missed it: They asked if TB was used; none asked whether EE cosmic variance was accounted in the estimator weights.
- Specific problem (quote): No statement of whether the β estimator uses theory EE spectra (and their covariance) for optimal weighting or a flat weight across ℓ-bins.
- Required fix: Specify the weighting scheme (e.g., inverse-variance using theory CEE and noise NEE, binning matrix) used to combine EB/TB into β̂. If flat weights were used, justify and assess the SNR impact.

P1B-META-m2
- Severity: MINOR
- Section + page: Sec. IV (ℓ-ranges vs Nside), p. 5
- Why others missed it: Beam issues were flagged; ℓ–Nside consistency was not.
- Specific problem (quote): “Nside = 512, ℓmax = 1024”
- Required fix: State the rationale for ℓmax selection relative to Nside (e.g., ℓmax ≤ 2Nside to avoid aliasing in PCL context vs 3Nside−1 for SHT). If near the boundary, show that results are stable if ℓmax is truncated to, say, 900.

P1B-META-n1
- Severity: NIT
- Section + page: Sec. IV (API names), p. 5
- Why others missed it: Others spotted purify_* syntax but not apodization-method naming.
- Specific problem (quote): “The mask uses C2 apodization at 2° scale.”
- Required fix: Use NaMaster’s exact API nomenclature for the apodization method (e.g., method='C2', aposize=2 deg), and provide the mask file hash/DOI so the exact mask is retrievable.

## Meta-review recommendation
MAJOR REVISIONS

The paper has multiple new blockers beyond the prior five reports: the ΔNeff analysis lacks critical conditioning disclosures (BBN/helium and neutrino-mass priors); the NaMaster MC omits CMB cosmic variance, leading to inflated SNR; B-mode purification likely suppresses the very rotation signal being tested; and several estimator/mask choices are not pre-registered or robustness-tested. Combined with the already-identified reference and dataset issues, substantial methodological clarification and additional analyses are required.

Given the union of all six reviews, I count at least 10–12 essential/major blockers (dataset/version/citation integrity; ALP likelihood definition; SN covariance/overlap; ΔNeff conditioning; NaMaster estimator, noise and purification; mask robustness; Planck nuisance applicability). My confidence that the paper would survive external peer review at PRD without these being addressed is low. With a thorough revision that (i) fixes the literature/dataset issues, (ii) fully specifies ΔNeff conditioning and neutrino priors, (iii) redoes the NaMaster MC including cosmic variance and purification tests, and (iv) clarifies the w0–wa setup, the manuscript could meet PRD’s methodological standards.