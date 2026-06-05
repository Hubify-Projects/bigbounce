# P1B R10v3p1 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 361.3s

---

Meta-referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Below are issues that, to the best of my reading, none of the five prior referees caught. I focus on hidden conditioning, chain-of-derivation integrity, cross-reference/internal-consistency problems, and subtle methodology gaps.

P1B-META-E1
- Severity: ESSENTIAL
- Location: Sec. IV (Data Methods: CMB E–B Analysis), p. 5–6
- Why others missed it: Reviewers asked for estimator details and noise choices but did not spot the conditioning on a fixed CMB realization.
- Specific problem (quote): “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin… The Commander map is a foreground-cleaned CMB-only product… The β = 0.27°, β = 0.342°, and β = 0 injections rotate Q+iU via e^{2iβ}(Q+iU) before adding noise.”
- Diagnosis: The MC uses a single, fixed CMB sky (Commander) and varies only the instrument noise. This omits cosmic variance of the E-mode field, so the scatter of β̂ (and thus the reported “pipeline-recovery SNR” ~20–26) is artificially small. The resulting SNR is a conditional-on-sky metric, not a sky-marginalized uncertainty. This hidden conditioning materially changes the interpretation of the “bias” and SNR.
- Required fix: Re-run the MC drawing both noise AND CMB realizations from a fiducial EE spectrum (and appropriate TE/BB as needed) with the same mask/beam/binning to obtain a sky-marginalized σ(β̂). Report both conditional-on-sky and marginalized results, clearly labeled. If the intent is a pure software unit test, drop “SNR” entirely and report only the mean recovery and multiplicative response with proper caveats.

P1B-META-M2
- Severity: MAJOR
- Location: Sec. IV (Data Methods: CMB E–B Analysis), p. 5–6
- Why others missed it: Estimator specification was flagged, but the specific purification-response issue was not.
- Specific problem (quote): “We use NaMaster’s spin-2 B-mode purification (purify_b=True, purify_e=False)… Injecting the spectator-ALP fiducial β = 0.27° recovers β̂ = 0.238°… The bias is 0.032°… The deconvolution is therefore unbiased at the 0.04° level…”
- Diagnosis: With purify_b=True, the estimator’s normalization (response) to a true β is modified; a multiplicative response R(β, mask, purify) must be calibrated (or analytically accounted for) to avoid misinterpreting a systematic deficit as “mask bias.” Simply inverting the MASTER coupling without calibrating the purification response can produce a multiplicative suppression of EB. The observed ~12% amplitude deficit could be a response factor, not an additive bias.
- Required fix: Quantify and report the multiplicative response R by (i) injecting several β values of both signs and measuring β̂/β vs β to check linearity near zero; (ii) verifying that the NaMaster workspace used is the purified one; and (iii) applying the calibrated response to de-bias β̂. Distinguish multiplicative response from additive bias.

P1B-META-E3
- Severity: ESSENTIAL
- Location: Table I, footnote a (p. 3) and Sec. V.A (p. 6)
- Why others missed it: Dataset/likelihood naming inconsistencies were noted, but the Planck-nuisance set mismatch itself was not identified.
- Specific problem (quote): “17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb…) … likelihoods: Planck NPIPE CamSpec TTTEEE…”
- Diagnosis: The nuisance parameter names listed (Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE) are characteristic of Plik-style parameterizations, not CamSpec’s standard nuisance set. Labeling the high-ℓ likelihood as “CamSpec” while listing Plik-like nuisance parameters is a reproducibility error: readers cannot reconstruct the actual likelihood stack.
- Required fix: Correctly identify the high-ℓ likelihood used (Plik vs CamSpec) and provide the full, exact nuisance parameter list and priors from the YAML. If CamSpec was in fact used, replace the nuisance list with the proper CamSpec set; if Plik was used, relabel accordingly everywhere.

P1B-META-M4
- Severity: MAJOR
- Location: Table II and caption (p. 4), and paragraph “Goodness-of-fit decomposition”
- Why others missed it: Reviewers focused on the absence of Bayes factors; none flagged the use of absolute χ² mixtures with arbitrary additive constants.
- Specific problem (quote): “χ²total 14037.4 ± 5.6… χ²BAO 10.6 ± 1.8 (DESI DR2); χ²CMB 10983.9 ± 5.3 (Planck PR4 + lensing); χ²SN 3043.0 ± 1.6… the two are formally identical to within sampling precision.”
- Diagnosis: These values mix absolute −2 ln L contributions from heterogeneous likelihoods, each with its own arbitrary additive constant. Reporting their absolute sum and decomposing into “χ² channel” terms is not statistically meaningful unless constants are removed (i.e., working with Δχ² relative to a common maximum-likelihood baseline per likelihood). The reported “±” as a posterior-mean spread across samples further obfuscates interpretation (a spread in posterior space is not an uncertainty on χ²).
- Required fix: Re-express goodness-of-fit as Δχ² relative to a common best fit for each likelihood (or report per-likelihood −2Δln L), and provide dof only where well-defined. Do not sum absolute χ² across likelihoods with different baselines. Remove the ± errors on χ² means or clarify they are posterior spreads, not uncertainties.

P1B-META-E5
- Severity: ESSENTIAL
- Location: Sec. VI (Cosmic Birefringence: Spectator ALP Consistency Check), p. 6–7 and Appendix C, p. 9
- Why others missed it: Reproducibility gaps were noted, but not the internal contradiction in sample counting and run types.
- Specific problem (quote): “Dedicated MCMC sampling … yields: βALP = 0.336° ± 0.107° (Caγ = 8 fixed), consistent with the model-independent fit βfree = 0.344° ± 0.096° (our internal model-independent MCMC fit to the Planck PR4 + ACT DR6 EB-spectrum likelihoods with β as a free parameter, 9,720 accepted samples across the 3 ALP-MCMC configurations described in Sec. VI (configurations Caγ = 4, 8, 12 … with β as a free parameter)…).”
- Diagnosis: The text assigns the same total sample count (9,720) “across the 3 ALP-MCMC configurations” to both the ALP-parametrized fit (m/H0, θi with Caγ fixed) and a “model-independent” βfree fit. These are distinct likelihood parametrizations and cannot share the same triad of Caγ configurations or the same counting unless there are two separate triplets of chains. As written, the chain accounting is contradictory.
- Required fix: Separate and enumerate the two sets of runs unambiguously (ALP-parametrized vs βfree), with distinct sample counts and repository pointers for each. If only one of the two was actually run, remove claims about the other.

P1B-META-m6
- Severity: MINOR
- Location: Table II, “wpivot” row and surrounding text (p. 4)
- Why others missed it: Focus was on the σ-distances and evidence deferral, not the definition of wpivot.
- Specific problem (quote): “wpivot −1.0344 ± 0.0301 … the effective equation of state at the pivot redshift zp…”
- Diagnosis: The pivot redshift zp is not specified. Without zp (and the definition used to obtain wpivot from w0, wa), the statement “wpivot is consistent with −1 at −1.1σ” cannot be interpreted or reproduced.
- Required fix: Specify the pivot definition and value zp used by the likelihood (e.g., the decorrelation pivot from the Fisher/posterior covariance), and report it explicitly alongside wpivot.

P1B-META-M6
- Severity: MAJOR
- Location: Sec. IV (Data Methods: CMB E–B Analysis), p. 5
- Why others missed it: Noise/apodization details were discussed, but not the band-limiting/aliasing implication of map degradation.
- Specific problem (quote): “Planck Commander Q/U maps are provided at Nside = 2048… we degrade to Nside = 512 and apply the corresponding pixel window function.”
- Diagnosis: Down-grading from Nside=2048 to 512 without explicitly applying extra Gaussian smoothing to band-limit the map before degrading risks aliasing (especially with ℓmax=1024). Applying only the Nside=512 pixel window does not by itself prevent high-ℓ power from aliasing into lower ℓ. This can bias EB and the β estimator.
- Required fix: Apply a pre-degradation smoothing kernel to band-limit the map safely below ℓmax=1024 (e.g., Gaussian smoothing yielding an effective beam ≥ 10–15 arcmin before downgrading), and demonstrate that aliasing is negligible by comparing spectra pre-/post-degradation.

P1B-META-m7
- Severity: MINOR
- Location: Sec. IV (Data Methods: CMB E–B Analysis), p. 5–6
- Why others missed it: They questioned estimator details but not pre-specification of mask choices.
- Specific problem (quote): “fsky = 0.32, 2° C2 apodization … The mask uses C2 apodization at 2° scale.”
- Diagnosis: The mask footprint and the 2° apodization scale are presented without pre-registration or robustness checks. Post-hoc mask tuning can materially change leakage properties and β recovery.
- Required fix: Justify the mask and apodization scale by either (i) citing a pre-registered, standard choice; or (ii) reporting stability tests (e.g., 1°, 2°, 3° apodizations; alternative masks) showing β̂ and bias are stable within quoted systematic floors.

P1B-META-m8
- Severity: MINOR
- Location: Sec. VI, Eq. (2) and surrounding discussion (p. 6–7)
- Why others missed it: They focused on coupling ranges and tuning, not on the dynamical regime.
- Specific problem (quote): “Δϕ/fa ≈ 0.65 (m = H0, θi = 1)… along the underdamped trajectory, Δϕ/fa ∝ θi…”
- Diagnosis: For m ~ H0, the field is near the critical/transition regime between frozen and oscillating; assuming a strictly underdamped, linear-in-θi scaling over z ∈ [zrec, 0] needs justification. The paper does not show the regime check or sensitivity of Δϕ/fa to the damping transition.
- Required fix: Show the (m/H0, θi) dependence of Δϕ/fa across the underdamped-to-oscillatory transition for the adopted H(z), or bound the error from using the “∝ θi” approximation in the quoted parameter range.

P1B-META-M7
- Severity: MAJOR
- Location: Sec. III (Stock-CAMB ΛCDM+ΔNeff MCMC), p. 3 and Fig. 1 (p. 5)
- Why others missed it: Several reviewers flagged figure labeling and Neff/ΔNeff ambiguity, but not the more basic reproducibility problem below.
- Specific problem (quote): “CAMB v1.6.5, stock; no torsion modifications… NPIPE CamSpec TTTEEE + low-ℓ + lensing…”
- Diagnosis: CAMB v1.6.5 can be built with different nonlinear prescriptions (Halofit/HMcode) and recombination modules affecting σ8/S8; nothing in the manuscript states these choices. Given S8 is quoted and compared to DES-Y3 priors, this matters for reproducibility.
- Required fix: State explicitly the nonlinear power prescription (e.g., Halofit revision or HMcode version) and recombination module options used in CAMB v1.6.5. Deposit the YAML and CAMB parameter files specifying these choices.

## Meta-review recommendation
REJECT

Given the union of all six reviews, the blocker count is high: multiple ESSENTIAL issues (scope misrepresentation, unverifiable/forward-dated citations, broken table references, undefined estimators/likelihoods) plus additional ESSENTIAL/Major problems identified here (hidden conditioning in the NaMaster MC; likelihood–nuisance mismatch; χ² decomposition misuse; contradictory ALP MCMC sample accounting). My confidence that the paper would survive independent, external peer review is low. Even with major rewrites, the work would need substantial methodological clarifications, corrected dataset/likelihood attributions, and fully reproducible artifacts before it could be reconsidered.