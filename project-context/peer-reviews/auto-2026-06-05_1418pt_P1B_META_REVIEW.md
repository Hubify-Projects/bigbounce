# P1B auto-2026-06-05_1418pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 372.8s

---

Meta-review: new issues not caught by the 5 prior referees

P1B-META-E1
- Severity: ESSENTIAL
- Location: Table I footnote a (p. 3) and Sec. V.A dataset/likelihood description
- Why it was missed: Reviewers noted dataset-label inconsistencies, but none audited the nuisance-parameter list against the named high-ℓ likelihood.
- Problem (quote): “17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb for the SNIa absolute magnitude).”
  - Mb is not a Planck likelihood nuisance; it belongs to the SN likelihood.
  - Aplanck is a Plik-specific amplitude calibration parameter and is not part of CamSpec’s nuisance set. The text claims “CamSpec.TTTEEE” yet lists Plik-style nuisance parameters.
- Required fix:
  - Provide the exact high-ℓ likelihood used (Plik vs CamSpec) and list its canonical nuisance parameters. If CamSpec was used, remove Aplanck and supply the correct CamSpec calibration parameters. If Plik was used, correct all CamSpec references accordingly.
  - Reclassify Mb as an SN nuisance (and not a Planck parameter), and update all parameter-count splits consistently.

P1B-META-E2
- Severity: ESSENTIAL
- Location: Sec. III (ΛCDM+ΔNeff MCMC), Table I (p. 3); no mention elsewhere
- Why it was missed: Reviewers asked for ΔNeff priors but not the thermodynamic/BBN conditioning that materially changes ΔNeff bounds.
- Problem: The paper does not state the treatment of Yp (primordial helium) under ΔNeff variations (BBN-consistent vs. fixed Yp) or the neutrino mass prior (Σmν fixed at 0.06 eV vs. free). Both materially affect ΔNeff, H0, and ns constraints and reproducibility.
- Required fix:
  - Explicitly state the Yp treatment (BBN consistency on/off, BBN module/version) and the Σmν prior (value and whether varied). If BBN consistency is used, state the ΔNeff bounds ensuring physical Yp.
  - Add these to the YAML summary in the text or an appendix.

P1B-META-E3
- Severity: ESSENTIAL
- Location: Sec. VI “MCMC parameter estimation” (p. 7) and Appendix A “What is NOT included” (p. 8)
- Why it was missed: Reviewers flagged estimator/likelihood details but not the direct contradiction on code availability.
- Problem (quotes):
  - “Both fits use the Planck PR4 + ACT DR6 EB-spectrum likelihoods… The MCMC engine is Cobaya v3.6.1…”
  - Appendix A: “No CMB polarization map analysis code is provided beyond the NaMaster driver script; all published birefringence values are literature citations.”
  This is a reproducibility contradiction: an internal EB-spectrum likelihood was used for ALP MCMC, but the paper provides no code or sufficient specification to reproduce it.
- Required fix:
  - Provide the EB likelihood code or, at minimum, a fully specified likelihood definition (data vector, ℓ-bins, covariance, calibration modeling) and an archived, citable package with scripts. Otherwise, remove all ALP-EB MCMC results from the manuscript.

P1B-META-M1
- Severity: MAJOR
- Location: Sec. V.A (p. 6) vs Table II header (p. 4) and elsewhere
- Why it was missed: Reviewers caught PR3/PR4 and DESI DR1/DR2 discrepancies, but not the DES Y3 vs DES-Y5 conflict.
- Problem (quotes):
  - Sec. V.A: “… +SH0ES H0 prior + DES Y3 S8.”
  - Table II header: “… + DES-Y5 + Pantheon+.”
  The manuscript alternates between DES Y3 and DES-Y5 for weak-lensing/clustering constraints.
- Required fix:
  - State clearly which DES data release/year is used in each run (Y3 vs Y5), with exact likelihood names/versions. Harmonize the text, tables, and conclusions.

P1B-META-M2
- Severity: MAJOR
- Location: Sec. V.A (p. 6) vs Table I (p. 3) and Abstract
- Why it was missed: One reviewer noted the Planck-only chain absence; none flagged that 4 dataset combinations are promised while only 2 are reported.
- Problem: Sec. V.A says “We analyze four dataset combinations,” but Table I reports only two combinations. The third “Planck-only” is referenced in prose but not tabulated; the fourth is not presented at all.
- Required fix:
  - Either add results (posteriors and diagnostics) for all four combinations, or reduce the scope to exactly the combinations you report and adjust the abstract/body accordingly.

P1B-META-M3
- Severity: MAJOR
- Location: Sec. III/Table I and Sec. V/Table II (lensing handling)
- Why it was missed: Reviewers flagged dataset naming; none examined lensing likelihood version control.
- Problem: The paper uses “lensing.native” with mixed PR4/PR3 references elsewhere, but does not state which Planck lensing likelihood (2018 PR3 vs PR4/NPIPE) is used. These have different bandpowers, covariances, and normalization conventions.
- Required fix:
  - Specify the exact lensing likelihood (release, version, multipole range). Confirm compatibility with the chosen high-ℓ likelihood and low-ℓ sets.

P1B-META-M4
- Severity: MAJOR
- Location: Sec. VI “ALP field evolution” and Eq. (2) narrative (p. 6–7)
- Why it was missed: Reviewers challenged scaling claims but not initial-condition specification.
- Problem: The text reports “field displacement from recombination to today,” but does not specify the initial redshift/scale factor (e.g., z=1100? 2000?), the initial field velocity, or whether radiation-era evolution is included. Δφ/fa for m ~ H0 is sensitive to the chosen start and initial conditions.
- Required fix:
  - State the initial conditions (zstart, θi definition at that z, initial ϕ̇), include whether radiation-era evolution is included, and quantify the sensitivity of Δφ/fa to these choices (e.g., a small table or figure). Update the Δφ/fa prior envelope if needed.

P1B-META-M5
- Severity: MAJOR
- Location: Sec. VI/App. C (p. 6–9)
- Why it was missed: Reviewers focused on spectator vs DE regimes, not on the topology and periodicity of θi.
- Problem: θi is sampled uniformly on [0.5, 2] with no justification of the angular domain’s topology. Misalignment angles are periodic on [−π, π) (or [0, 2π)), and priors should respect periodicity. Choosing a linear prior on a non-periodic sub-interval can bias Δφ/fa and Caγ inferences.
- Required fix:
  - Justify the restricted interval and the non-periodic prior. Prefer a circular (periodic) prior on θi over [−π, π) with appropriate Jacobian, then show how restricting to the spectator subdomain (|θi| ≪ 1) changes results. Report sensitivity to the θi prior choice.

P1B-META-M6
- Severity: MAJOR
- Location: Sec. IV (p. 5–6) and Sec. VI (p. 7)
- Why it was missed: Reviewers questioned SNR but not its propagation to later β results.
- Problem: The paper adopts a “NaMaster systematic floor” of ~0.04° from the pipeline test, but does not propagate any comparable systematic into its internal βfree fit (0.344° ± 0.096°). If the same pseudo-Cℓ machinery or masking is used in the EB likelihood, a comparable configuration-dependent bias may apply.
- Required fix:
  - Either (a) demonstrate that the βfree likelihood analysis is immune to the mask/purification bias measured in Sec. IV (e.g., different estimator), or (b) include an estimator-appropriate systematic in quadrature and update βfree accordingly.

P1B-META-M7
- Severity: MAJOR
- Location: Table II “Age [Gyr] = 13.763 ± 0.019” (p. 4)
- Why it was missed: Reviewers focused on model comparison, not parameter realism.
- Problem: An age uncertainty of 0.019 Gyr (≈ 19 Myr) for a w0wa cosmology combining DESI DR2 + Planck + SN seems implausibly tight given the quoted H0 uncertainty (±0.455 km s−1 Mpc−1) and DE dynamics freedom. This suggests either (i) a unit/rounding slip, (ii) a hidden conditioning (e.g., very tight priors) not disclosed, or (iii) a reporting artifact (posterior mean-of-means vs at-MAP evaluation).
- Required fix:
  - Recompute and report Age with an explicit definition (posterior mean and 68% CI; or mean ± sd), state priors that affect it (Ωk fixed, w0wa priors), and verify consistency with the H0, Ωm, and w0wa posteriors. If 0.019 Gyr is correct, provide a brief rationale.

P1B-META-m1
- Severity: MINOR
- Location: Sec. IV (p. 5) choice of Nside and ℓmax
- Why it was missed: Reviewers focused on pre-smoothing and estimator but not information loss.
- Problem: The pipeline degrades to Nside=512 and caps at ℓmax=1024 while adopting a 5′ beam. With such pixelization, a significant fraction of the angular information content is thrown away, potentially altering EB-based β sensitivity and bias. This choice is not justified.
- Required fix:
  - Justify the Nside=512/ℓmax=1024 choice by showing stability vs a higher-resolution variant (e.g., Nside=1024, ℓmax=2000) or by demonstrating negligible impact on β-bias/σ(β̂).

P1B-META-m2
- Severity: MINOR
- Location: Appendix A (“reproduce cosmology.sh (∼4–12 h per configuration on 4 CPU cores)”)
- Why it was missed: Others focused on scientific content, not practical reproducibility claims.
- Problem: The claimed run-time for Planck TTTEEE + BAO + SN + SH0ES MCMC on 4 CPU cores (4–12 h) is not credible at the reported sample counts and convergence criteria. This undermines the reproducibility guidance.
- Required fix:
  - Provide realistic wall-time estimates (per dataset, hardware class), sampler settings (proposal covariances, acceptance rates), and any speed-ups (fast-slow splitting, power-spectrum caching).

P1B-META-m3
- Severity: MINOR
- Location: Sec. III “MB–H0 joint-posterior offset check” (p. 4)
- Why it was missed: Reviewers accepted the algebra.
- Problem: The statement that “sn.pantheonplus enforces a soft constraint on MB − 5 log10 H0 ≈ const along the SN distance-modulus degeneracy” is an oversimplification; Pantheon+ marginalizes over light-curve nuisance parameters and calibration systematics that break the perfect MB–H0 degeneracy. Presenting it as a hard 1D degeneracy risks overinterpretation of the 0.155 mag offset mapping.
- Required fix:
  - Rephrase as an approximation and note that color/stretch/calibration systematics widen the effective degeneracy. Avoid implying exact one-parameter degeneracy unless conditioning assumptions are stated.

P1B-META-m4
- Severity: MINOR
- Location: Sec. VI “Across the natural parameter range … Δϕ/fa ∈ [0.2, 1.1]” (p. 6–7)
- Why it was missed: Reviewers questioned scaling and spectator status but not envelope construction.
- Problem: The Δϕ/fa envelope is reported without showing how the extremes co-vary with (m/H0, θi). As stated, it is unclear whether [0.2, 1.1] comes from coupled trajectories or independent extrema; this affects the derived Caγ range.
- Required fix:
  - Provide a small table/figure showing Δϕ/fa vs. (m/H0, θi) and confirm that the quoted Caγ range arises from trajectory-consistent combinations (not independent extrema).

Meta-review recommendation
REJECT

Given the union of all six reviews, there are multiple essential blockers: fabricated or non-traceable external citations, inconsistent/incorrect likelihood and nuisance-parameter specification (including a Plik-vs-CamSpec mismatch and misclassification of Mb), missing specification of BBN/Σmν assumptions critical to ΔNeff inference, and unreproducibility of the ALP EB-likelihood MCMC. There are also substantial methodological omissions in the birefringence estimator and masking choices. My confidence that the paper would survive external, non–program-related peer review is low: there are at least 6–8 essential/major blockers that require a substantial rewrite, corrected bibliographic anchors, clarified likelihood configurations, and provision of missing code before a fair reassessment.