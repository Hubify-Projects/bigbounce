# P1B auto-2026-06-05_1617pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 310.9s

---

Meta-review — focus on blind spots none of the five referees identified

P1B-META-E1
- Severity: ESSENTIAL
- Section + page: Sec. IV “Data Methods: CMB E–B Analysis”, p. 5–6
- Why others missed it: Reviewers questioned SNR definition and noted multiplicative bias but did not trace it to a concrete missing step.
- Specific problem (quote): “Mode-coupling matrix.—The Mℓℓ′ matrix is computed via NmtWorkspace.compute coupling matrix … Spectra are band-power-binned…”
- Required fix: The text never states that the pseudo-Cl spectra were deconvolved with NmtWorkspace.decouple_cell (the MASTER inversion). Failing to decouple yields a multiplicative suppression (exactly what is observed: ≈0.88 for both injections) and invalidates the “pipeline-recovery bias” interpretation. Amend methods to (a) explicitly perform and document decoupling, or (b) calibrate a transfer function from MC and apply it to all reported β estimates, and re-report the corrected recovery factors with uncertainty.

P1B-META-E2
- Severity: ESSENTIAL
- Section + page: Sec. IV “Foreground and noise model”, p. 5–6
- Why others missed it: Several reviewers challenged SNR interpretation, but none pointed out the “frozen-sky” conditioning error.
- Specific problem (quote): “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin… The β injections rotate Q+iU via e^{2iβ}(Q+iU) before adding noise.”
- Required fix: All 500 MC realizations reuse the same sky (Commander map) and vary only noise, thereby omitting CMB sample variance (E-mode CV and lensing-B variance) in σβ. This dramatically underestimates σβ and inflates SNR. Re-run the MC with full CMB realizations (signal+noise) drawn from a fiducial theory spectrum under the mask and beam, or clearly state that σβ excludes sample variance and remove SNR claims. Provide σβ values with and without CV to demonstrate the impact.

P1B-META-E3
- Severity: ESSENTIAL
- Section + page: Table I footnote a (p. 3) and Sec. V.A (p. 6)
- Why others missed it: Prior reviews noted “incomplete nuisances,” but not the specific mismatch to the stated CamSpec likelihood.
- Specific problem (quote): “…10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE…”
- Required fix: These nuisance names are the Plik (or Plik-like) set, not CamSpec’s. If CamSpec TTTEEE was used, list the correct CamSpec nuisance parameters (per-frequency dust amplitudes and calibrations) and remove A_planck and the “amp×/n×” Plik terms; if Plik was used, correct the text/headers to “Plik” everywhere and update references. Provide the exact nuisance list per likelihood and verify the YAML matches the claim.

P1B-META-E4
- Severity: MAJOR
- Section + page: Sec. VI (p. 6–7), Appendix C (p. 9)
- Why others missed it: Reviewers flagged “shared calibration covariance” vagueness but not the identifiability issue.
- Specific problem (quote): “model-independent MCMC fit … with β as a free parameter … combined with shared calibration covariance.”
- Required fix: A robust EB birefringence likelihood must include explicit per-experiment/channel polarization-angle calibration parameters αi along with β, with priors/covariances tying αi to lab/planet calibrations. A “shared calibration covariance” alone is insufficient to identify β. Add α-parameterization (per-instrument/channel) to the likelihood with stated priors, or remove the internal βfree result. Document how β–α degeneracy is handled.

P1B-META-M1
- Severity: MAJOR
- Section + page: Table II, “Age [Gyr] 13.763 ± 0.019” (p. 4)
- Why others missed it: Age is rarely scrutinized; focus was on w0–wa σ-distances.
- Specific problem (quote): “Age [Gyr] 13.763 ± 0.019”
- Required fix: For a w0wa chain with Planck+DESI+SN the age uncertainty at the 20 Myr level is implausibly tight; typical w0wa analyses degrade age precision relative to ΛCDM. Verify computation and provenance of the quoted age (e.g., is it inadvertently taken from a ΛCDM chain?). Recompute t0 with the sampled w0wa posterior and report uncertainty consistent with that model space, including method used to calculate t0.

P1B-META-M2
- Severity: MAJOR
- Section + page: Sec. IV “Beam and pixel window.” (p. 5)
- Why others missed it: Beam wording was questioned, but not the degrade/beam double-counting risk.
- Specific problem (quote): “The Planck Commander Q/U maps are provided at Nside = 2048 with the Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz); we degrade to Nside = 512 and apply the corresponding pixel window function. NaMaster’s NmtField is initialized with beam = b^Planck_ℓ w^pix_ℓ.”
- Required fix: Commander is a component-separated CMB product with its own effective polarization beam, not a “143 GHz 5′” map. Degrading to Nside=512 without matched Gaussian smoothing risks aliasing, and passing b_ℓ × w_ℓ as a beam can double-count smoothing. Specify (a) the actual Commander effective beam used, (b) any additional smoothing applied before degrading to Nside=512 to avoid aliasing, and (c) exactly what beam window was passed to NaMaster. Re-generate results if a beam/pixel mismatch is found.

P1B-META-M3
- Severity: MAJOR
- Section + page: Sec. VI, “Summary-likelihood combination (auxiliary cross-check).” (p. 7)
- Why others missed it: They focused on calibration-sharing but not cosmic variance sharing.
- Specific problem (quote): “Combining β = 0.30° ± 0.11° (Planck) and β = 0.215° ± 0.074° (ACT DR6) via inverse-variance weighting… (This neglects shared calibration systematics...)”
- Required fix: In addition to calibration, Planck and ACT EB constraints share CMB sample variance over overlapping multipoles and sky regions. The IVW combination overstates significance by ignoring CV covariance. Either (a) provide a combined estimate that includes an approximate CV covariance term (e.g., via analytic mode-counting for the overlap), or (b) present the combination strictly as a didactic arithmetic exercise and explicitly state it ignores both calibration and CV correlations and is therefore not statistically valid.

P1B-META-M4
- Severity: MAJOR
- Section + page: Sec. V / Table II, “wpivot” (p. 4)
- Why others missed it: Attention was on w0–wa distances; the pivot-redshift definition wasn’t checked.
- Specific problem (quote): “wpivot −1.0344 ± 0.0301” with no definition of zp.
- Required fix: Define the pivot redshift (or scale factor) zp used to compute wpivot, and state how zp was determined (e.g., minimizing σ(wp) or using a conventional value). Provide zp and the w(z) parameterization explicitly (CPL w(a)=w0+wa(1−a) or w(z)=w0+wa z/(1+z)), so wpivot can be reproduced.

P1B-META-m1
- Severity: MINOR
- Section + page: Appendices, p. 9–10
- Why others missed it: Focus stayed on Table III’s taxonomy; the appendix promised content wasn’t checked.
- Specific problem (quote): “Appendix B: Claims Classification” heading appears, but the appendix body is empty; the only content is a separate Table III on the next page.
- Required fix: Either populate Appendix B with the intended classification content and link it to Table III, or remove the appendix heading and integrate Table III into the main text with an explanatory caption.

P1B-META-m2
- Severity: MINOR
- Section + page: Sec. IV “E/B leakage and purification.” (p. 5–6)
- Why others missed it: They observed bias/SNR issues but not the asymmetry’s likely effect.
- Specific problem (quote): “purify_b = True, purify_e = False”
- Required fix: For EB-based β estimation under a mask, asymmetric purification (B-only) can leave E-mode leakage pathways that scale with the signal and contribute to the observed ≈0.88 multiplicative deficit. Either justify B-only purification with a reference demonstrating negligible impact on EB amplitude, or enable purify_e as well and quantify the effect on the recovery factor.

P1B-META-m3
- Severity: MINOR
- Section + page: Sec. VI, “Range [0.17,0.43]° … obtained from a joint-trajectory scan” (p. 7)
- Why others missed it: Others questioned consistency/priors but not how the envelope was generated.
- Specific problem (quote): “obtained from a joint-trajectory scan over the coupled (Caγ, m/H0, θi) space … not from an independent-extremes product”
- Required fix: Document the scan procedure: grid or MCMC? spacing and bounds? correlation model linking ∆φ/fa to (m/H0, θi)? Provide enough detail so an independent reader can reproduce the [0.17,0.43]° envelope and understand why the lower bound differs from the naive extremes.

P1B-META-m4
- Severity: MINOR
- Section + page: Sec. III “Independent cross-validation” (p. 5)
- Why others missed it: They asked for the numbers from Liu et al.; a second, subtler fairness issue remains.
- Specific problem (quote): “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.”
- Required fix: In addition to adding comparative numbers, ensure like-with-like comparison: match the Planck likelihood version, BAO release, and SN stack to Liu et al., or explicitly state the differences and adjust the comparison (e.g., via reweighting or by quoting the expected shift). Otherwise the “0.5σ/0.4σ” agreement is not a fair comparison.

P1B-META-n1
- Severity: NIT
- Section + page: Sec. IV and Figure 1 (p. 5)
- Why others missed it: They asked for axis units; a label ambiguity remains.
- Specific problem (quote): “Neff” on the triangle plot likely denotes ΔNeff; nearby text uses “∆Neff”.
- Required fix: Harmonize the symbol in the figure and text to “ΔNeff” to avoid confusion with Neff,total.

Meta-review recommendation
REJECT

Given the union of all six reviews, there are multiple independent essential blockers: fabricated/future citations, inconsistent dataset/likelihood versioning, an unadvertised and under-documented w0–wa analysis, undefined/incorrect NaMaster deconvolution (missing decoupling), frozen-sky MC inflating SNR, mismatched nuisance sets to the stated Planck likelihood, and an implausibly tight age error. My confidence that the manuscript would survive external peer review in its current form is low. Addressing the combined blocker set will require substantial re-analysis, careful methodological rewrites, and bibliographic corrections before the paper can be reconsidered.