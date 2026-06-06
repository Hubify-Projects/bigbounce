# P1B auto-2026-06-06_0004pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6726 chars)
**Wall time**: 323.4s

---

Referee report on P1B: “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall scope and standard
- This manuscript presents three technical checks: (i) stock-CAMB ΛCDM+ΔNeff MCMC posteriors; (ii) a NaMaster pseudo-Cl pipeline bias-injection validation; (iii) an ALP-birefringence consistency check. It explicitly avoids model-evidence comparisons and stresses scope limitations. That is acceptable in principle for a methods companion, but PRD still requires full methodological clarity and internal consistency.
- I audited every scalar in the abstract and conclusions for traceability within the body; checked arithmetic where possible; and scrutinized statistical definitions and dataset configurations.

Findings

ESSENTIAL

P1B-E1 (Sec. III, p. 3; Table I reference in fn. 1)
- Problem: The text states: “The third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating samples, is reported separately in Table I...” But Table I has only two columns (Full-tension; Planck+BAO+SN) and does not report a Planck-only run.
- Required fix: Remove the claim that the Planck-only run is reported in Table I, or add a third column with the Planck-only summary (including R̂ − 1, ESS, means ±1σ for all listed parameters) and ensure all counts are consistent with the chain stratification footnote.

P1B-E2 (Sec. IV, pp. 5–6; NaMaster pipeline; estimator and SNR definition)
- Problem: The primary estimator for β from pseudo-Cl spectra is not specified. The text reports “β̂NaMaster = 0.238° (pipeline-recovery SNR = 20.32)” without defining:
  - how β̂ is computed from the EB/TB pseudo-Cl (D-estimator? angle maximizing EB likelihood? linearized small-angle estimator? spectral range and weights?),
  - what “SNR” means (mean(β̂)/std(β̂) across realizations? mean/SEM? single-realization forecast?).
  - the per-realization uncertainty σβ (the scatter across the 500 MCs) and the standard error on the mean.
- Required fix: Pre-declare the estimator including the exact formula, multipole range and binning, weighting, and treatment of purification. Report the sampling distribution of β̂ across 500 MC: mean, standard deviation per realization, and SEM. Define SNR unambiguously and avoid reporting a “mean/SEM” significance as if it reflected single-sky detectability. Provide the numerical σβ used to compute the quoted SNR.

P1B-E3 (Dataset consistency; Sec. II p. 2; Sec. III pp. 3–4; Sec. V A p. 6; Table II p. 4)
- Problem: The manuscript mixes DESI BAO releases inconsistently:
  - Sec. III “Physics interpretation (Table II)” and Table II caption use DESI DR2.
  - Sec. V A “Datasets” lists DESI 2024 DR1 BAO [18].
  - References include both DR1 [18] (2024) and DR2 [12] (2025).
- Required fix: Unify dataset versions throughout. If Table II uses DR2, state DR2 everywhere Table II is referenced and in Sec. V A. If any other analysis used DR1, clearly segregate results by release. Likewise clarify Planck data release consistency (PR3 vs PR4/NPIPE; the text alternates “Planck 2018” and “PR4/NPIPE CamSpec”). Provide a compact table mapping each result to the exact release, likelihood names, and versions.

P1B-E4 (Bibliography; p. 10, Ref. [15])
- Problem: Reference [15] includes internal editorial/bookkeeping text: “the value used at L256/L416 of P1B...”. This is not acceptable in a published reference and violates the “no internal logs” rule.
- Required fix: Remove all internal line-number, draft, or repository bookkeeping language from references. Keep only standard bibliographic information.

P1B-E5 (SN combination methodology; Sec. III–IV pp. 3–6; Table II p. 4)
- Problem: The paper combines DES-Y5 SNe with Pantheon+. These samples overlap significantly in redshift and may share calibration systematics. The manuscript does not describe how overlap and cross-covariances are handled, nor whether duplicated objects are removed, nor how shared nuisance parameters are treated, which directly affects Table II and related claims (e.g., w0, wa).
- Required fix: Provide explicit methodology for combining DES-Y5 and Pantheon+: overlap handling, covariance treatment, and nuisance parameter strategy. If no cross-covariance is available, state the approximation and quantify its impact via a sensitivity test (e.g., re-run without Pantheon+ or without DES-Y5 and compare Table II posteriors). Otherwise, remove one of the two SN samples to avoid double counting.

P1B-E6 (ALP EB-likelihood specification; Sec. VI p. 6–7; App. C pp. 9–10)
- Problem: The ALP-MCMC uses “Planck PR4 + ACT DR6 EB-spectrum likelihoods combined with shared calibration covariance,” but the functional form, ℓ-ranges, frequency cross-spectra, mask/apodization, covariance construction, and calibration treatment are not specified, nor is a code DOI/commit provided for reproducibility. With only 3,240 accepted samples per configuration, convergence claims alone are insufficient without exact likelihood definition.
- Required fix: Specify the EB/TB likelihood exactly (data vectors, ℓmin/ℓmax, binning, frequency pairs, cross/auto choices, covariance estimation, calibration priors/constraints, and treatment of β–α degeneracy). Provide a permanent, versioned code link (commit hash or DOI) that reproduces the likelihood build. Report ESS and acceptance rates for these chains.

MAJOR

P1B-M1 (NaMaster bias characterization; Sec. IV pp. 5–6)
- Problem: The bias is reported as 0.032° (β=0.27°) and 0.040° (β=0.342°) with no uncertainty on the bias estimate, no plot of bias vs amplitude, and no per-realization scatter. With NMC=500, the bias precision depends on σβ/√NMC; without σβ this “systematic floor” cannot be evaluated.
- Required fix: Report bias uncertainty (e.g., bootstrap or SEM), provide σβ, and include a small table or figure of bias vs injected β with error bars. If adopting 0.040° as a floor, demonstrate that amplitude-dependence and sampling error are subdominant to this value.

P1B-M2 (MB–H0 “corresponds exactly” phrasing; Sec. III p. 4)
- Problem: The text states the MB–H0 offset “corresponds exactly to the canonical 3.6σ Hubble tension,” but the numeric example gives ~3.2σ using σMB only and neglects covariances along the SN degeneracy direction.
- Required fix: Rephrase to remove “exactly”; compute the significance properly along the SN degeneracy direction with the joint covariance of (MB, H0) as constrained by the active likelihoods, or present the correct combined-sigma computation explicitly.

P1B-M3 (Strong-coupling scale dimensionality; Sec. III fn. 2, p. 3)
- Problem: The statement “Λstrong ∼ MPl/√γBI set by the inverse Barbero–Immirzi parameter γBI” is dimensionally and conceptually unclear (γ is dimensionless). As written, it asserts a parametric scale without derivation or citation justifying this dependence for the Holst sector with fermions.
- Required fix: Provide a derivation or a precise literature citation supporting this scaling, or remove the claim. Clarify what is meant by “torsion-resolution scale” in the effective theory and under what assumptions.

P1B-M4 (Nuisance-parameter classification; Table I footnote, p. 3)
- Problem: The footnote lists “10 Planck likelihood nuisance: ... Mb for the SNIa absolute magnitude.” MB is not a Planck nuisance parameter; it belongs to the SN likelihood.
- Required fix: Correct the classification. Provide a clean list of nuisance parameters per likelihood (Planck, BAO, SN, H0 prior) and ensure the counts sum to the stated total dimensionality in each dataset combination.

P1B-M5 (Convergence diagnostics for ALP MCMC; Sec. VI p. 7; App. C p. 10)
- Problem: Only R̂−1 < 0.01 is reported. With ~3,240 accepted samples per configuration and a Metropolis–Hastings sampler, reporting ESS and acceptance rates is necessary to support the quoted ±0.107° uncertainties.
- Required fix: Add ESS, autocorrelation times, and acceptance rates for each ALP configuration. If ESS is low, extend chains until ESS per parameter exceeds standard thresholds (e.g., >1000) or report conservative error inflation.

P1B-M6 (Code and data versioning; App. A p. 8)
- Problem: The repository is referenced but no commit hash/DOI is given; several critical results (e.g., EB-likelihood build) depend on external code. PRD reproducibility standards require stable artifacts.
- Required fix: Provide permanent DOIs (e.g., Zenodo) or immutable commit hashes for the repository version used to generate all results; list exact package versions (Cobaya, CAMB, NaMaster) and any patches.

MINOR

P1B-n1 (Figure labeling; Fig. 1, p. 5)
- Problem: The axis label reads “Neff” though the parameter sampled is ΔNeff. H0 axis lacks units.
- Required fix: Relabel the parameter as “ΔNeff” and add units “[km s−1 Mpc−1]” to the H0 axis. Ensure all figure axes have correct symbols and units.

P1B-n2 (Bias sign; Sec. IV p. 6)
- Problem: The “pipeline-recovery bias 0.032°” is stated without sign. The recovered mean is below the injected value, implying a negative bias.
- Required fix: Report bias with sign (e.g., −0.032° at β=0.27°) and adopt a consistent convention. If quoting absolute bias for a “floor,” say so explicitly.

P1B-n3 (API syntax; Sec. IV p. 5)
- Problem: The NaMaster options are printed as “purify b=True, purify e=False,” which does not match the API names and may confuse readers.
- Required fix: Use the exact API names “purify_b=True, purify_e=False.”

P1B-n4 (Noise level mapping; Sec. IV p. 5)
- Problem: ΔP=10 μK·arcmin is quoted at map level but no conversion to per-pixel/pseudo-Cl noise or beam-deconvolved Nℓ is provided, hindering reproducibility of the SNR.
- Required fix: State how ΔP is converted to Nℓ (after beam and pixel windows) and specify whether white noise is added in Q/U at Nside=512 before pseudo-Cl estimation.

P1B-n5 (Angle units in Eq. (3); Sec. VI p. 7)
- Problem: Eq. (3) is evaluated in radians but reported in degrees without an explicit note.
- Required fix: Add a note “angles in Eq. (3) are in radians; we convert to degrees for the numerical value.”

P1B-n6 (Independent cross-validation claim; Sec. III p. 5)
- Problem: “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8” vs. Liu et al. [11] is not supported by quoted numbers.
- Required fix: Provide the Liu et al. central values and errors alongside yours and compute the differences explicitly.

NIT

P1B-t1 (Stylistic; Acknowledgments, p. 8)
- Problem: Operational details (“RunPod H200 instances”; “use of Claude as an AI assistant”) are editorially non-standard in PRD.
- Required fix: Consider trimming to a concise, standard acknowledgment without operational vendor details.

P1B-t2 (Minor duplication/wording; throughout)
- Problem: Some repetitive scope disclaimers and emphatic wording (“fails catastrophically”) are not necessary for PRD style.
- Required fix: Tighten language for concision and neutrality.

Arithmetic and dimensional checks performed
- ΔNeff and H0 values in the abstract match Table I.
- S8 recomputed from Table I σ8 and Ωm matches to rounding.
- MB–H0 constant calculation: −28.571 (Riess anchor) vs −28.416 (chain mean), difference 0.155 mag; 0.155/0.049 ≈ 3.16σ, not “exactly 3.6σ.”
- Inverse-variance combination of Planck NPIPE (0.30 ± 0.11) and ACT DR6 (0.215 ± 0.074) gives 0.242 ± 0.061, ~3.94σ: consistent with the text’s 0.241 ± 0.061 (3.9σ) and clearly labeled as auxiliary, with appropriate caveats.
- Birefringence formula β = [αEM/(4π)] Caγ (Δφ/fa) is dimensionally correct. Numerical products:
  - αEM/(4π) ≈ 5.81×10−4; with Caγ=8, Δφ/fa=1.07 gives β ≈ 0.285°, consistent with 0.29°.
  - For β=0.342°, Caγ Δφ/fa ≈ 0.00597 / 5.81×10−4 ≈ 10.3, consistent.
  - Required Caγ range 9–51 from Δφ/fa ∈ [1.1, 0.2] is consistent.
- Chain-sample arithmetic in fn. 1 checks out.

Use of distinct σ’s and cautions
- The manuscript generally keeps distinct significances separate (sky detections vs MC pipeline SNR) and includes warnings. However, the SNR needs a formal definition (P1B-E2) and the “exactly” wording for the MB–H0 correspondence must be corrected (P1B-M2).

Length
- For a methods companion, 10 pages are acceptable if the essential methodological clarifications (above) are incorporated. No need to shorten; focus on fixes.

## Summary recommendation
MAJOR REVISIONS

The core numerical values are mostly arithmetically consistent and the scope limitations are clearly stated, but several methodological and internal-consistency issues must be addressed for PRD standards: misstatement about Table I contents; insufficient specification of the β estimator and SNR in the NaMaster pipeline; inconsistent dataset attributions (DESI DR1 vs DR2; Planck PR3 vs PR4 terminology); incomplete methodology for combining overlapping SN samples; and inadequate specification of the ALP EB-likelihood. Addressing these, along with the listed major/minor corrections, will make the paper reproducible and methodologically sound.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (additional to prior report)

ESSENTIAL

P1B-E7 (Convergence threshold inequality; Table I footnote vs tabulated value)
- Issue: The footnote states “all 17 sampled parameters … satisfy R̂ − 1 < 3 × 10−3 across both frozen combinations,” but the Planck+BAO+SN column lists a worst R̂ − 1 = 0.003, which is equal to 3 × 10−3, not strictly less.
- Required fix: Change the statement to “≤ 3 × 10−3” or provide the precise value (e.g., 2.99 × 10−3) to justify the strict inequality.

P1B-E8 (Claims-classification table cites a non-existent “MC bias table”; Table III, p. 10)
- Issue: Table III references “MC bias table,” but no such table or figure appears in the manuscript.
- Required fix: Either add the referenced table/figure quantifying the MC bias or remove the claim in Table III.

P1B-E9 (SH0ES prior naming/version inconsistency; Sec. III, p. 4; Refs.)
- Issue: The text refers to an active likelihood “H0.riess2020Mb” while citing Riess et al. (2022) for H0 and quoting MB = −19.253 ± 0.027. This mixes a 2020 alias with 2022 values and reference.
- Required fix: Align the alias, reference, and numbers. State explicitly which SH0ES release (year, DOI) is used in the YAML, and update the alias and citation accordingly.

P1B-E10 (Pivot-redshift definition missing for wpivot; Table II and surrounding text)
- Issue: The manuscript quotes wpivot = −1.0344 ± 0.0301 but does not specify the pivot redshift zp or how it was chosen (e.g., to minimize corr(w0, wa)).
- Required fix: Provide the definition and numerical value of the pivot redshift zp, and describe the pivoting convention used.

P1B-E11 (ALP ODE integration reproducibility; Sec. VI, Eq. (2))
- Issue: The EOM integration yielding Δφ/fa ≈ 0.65 (m = H0, θi = 1) lacks algorithmic details (ODE solver, time variable, initial conditions, start redshift, step-size control, tolerances, H(z) expression, parameter values used for Ωm, Ωr, ΩΛ). No numerical-error estimate is given.
- Required fix: Document the full integration setup and provide a code/commit/DOI that reproduces Eq. (2). Quantify the numerical uncertainty on Δφ/fa.

P1B-E12 (Corner-plot sample-count/thinning not documented; Fig. 1 vs Sec. III fn. 1)
- Issue: For the full-tension chain the post–burn-in count is stated as ≈123,129, but Fig. 1 reports 119,617 post–burn-in samples, attributed to “getdist-thinning” without specifying the thinning rule.
- Required fix: State the exact thinning scheme and factor (e.g., effective-sample-weight thinning, stride), and reconcile the counts explicitly.

P1B-E13 (Noise/SNR consistency; Sec. IV, pp. 5–6)
- Issue: The text calls ΔP = 10 μK·arcmin “a conservative worst-case bias check,” yet reports very high pipeline SNRs (20–26). If the noise is truly worst-case for ACT-like maps, one would expect lower recoverability. This may be a definitional issue (SNR across MC means vs single-sky detectability) but is not explained.
- Required fix: Clarify why this noise level is labeled “worst-case,” and reconcile it with the large SNR values by (i) defining SNR precisely (see also P1B-E2 in the prior report) and (ii) showing how single-realization uncertainties map to the reported SNR.

MAJOR

P1B-M7 (Arithmetic: bias amplitude-dependence misquoted; Sec. IV, p. 6)
- Issue: The bias increase from 0.032° (βinj=0.27°) to 0.040° (βinj=0.342°) is described as “∼12%.” The relative change is actually 0.040/0.032 − 1 = 25%.
- Required fix: Correct the percentage and specify whether the percentage refers to absolute bias change, fractional change relative to the lower-bias case, or scaling per unit β.

P1B-M8 (Commander effective beam specification; Sec. IV, p. 5)
- Issue: The analysis assumes a 5′ Gaussian “Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz)” for the Commander CMB map. Component-separated maps (Commander/SMICA/NILC/SEVEM) have their own effective beams; applying a single 143 GHz beam can be mismatched unless justified by the product documentation for the exact release used (PR4/NPIPE).
- Required fix: Cite the Commander-product beam for the release you used (PR4 if applicable), or justify the 5′ Gaussian approximation quantitatively by showing that β recovery and the bias are insensitive at the <0.01° level to plausible beam variations.

P1B-M9 (Goodness-of-fit interpretability; Table II, p. 4)
- Issue: χ2 values are quoted for BAO, CMB, and SN without stating the number of data points or degrees of freedom per block. Without ν, χ2 cannot be interpreted.
- Required fix: Provide Ndof (or Ndata and Npars contributing to each block) so that χ2/ν is meaningful.

MINOR

P1B-m7 (Footnote claims a “k = 7” reference elsewhere; Table I footnote, p. 3)
- Issue: The footnote says “references to k=7 elsewhere in this paper…,” but no such references are evident.
- Required fix: Either add the missing references or delete this sentence.

P1B-m8 (wpivot definition completeness)
- Issue: Beyond providing zp (P1B-E10), specify the pivoting scheme (e.g., CPL pivot, DETF pivot), how zp is determined (minimizing corr(w0, wa)), and confirm that reported wpivot corresponds to that zp.

P1B-m9 (Null-injection quantitative result; Sec. IV, p. 5–6)
- Issue: The βinj=0 null test is mentioned as “consistent with zero,” but no numerical mean and scatter are given.
- Required fix: Report the mean and standard deviation of β̂ across the 500 MC realizations for βinj=0.

P1B-m10 (TB usage in β estimation; Sec. IV)
- Issue: It is unclear whether TB information is used alongside EB for β estimation, or whether TB is set to zero/ignored.
- Required fix: State explicitly whether TB enters the estimator, with the same ℓ-range/bins/weights as EB, and how it is combined.

P1B-m11 (SN and lensing naming consistency; throughout)
- Issue: The manuscript uses “DES-Y5,” “DES-SN5YR,” and “DES-Y3 S8” inconsistently. The latter is a weak-lensing prior, not a SN sample.
- Required fix: Standardize the naming and clearly distinguish DES SN samples (Y5/SN5YR) from DES Y3 weak-lensing S8 constraints.

P1B-m12 (Equation formatting; Sec. IV)
- Issue: The labeled “(1)” for β̂NaMaster appears as an inline sentence rather than a displayed equation.
- Required fix: Format β̂NaMaster as a displayed equation if it is to be numbered, or remove the equation number.

EXPLANATION

These items were not covered in the initial review because they require a second-pass reconciliation of fine-print consistency (inequality thresholds, internal table references), closer scrutiny of labeling/versioning conventions for external datasets (SH0ES alias/year; Commander beam), and a deeper audit of the numerical claims in the NaMaster section (percentage changes, null-test quantification, and noise/SNR consistency).