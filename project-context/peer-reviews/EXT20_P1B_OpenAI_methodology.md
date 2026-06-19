# P1B EXT20 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7138 chars)
**Wall time**: 414.2s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

General assessment
This submission is framed as a methods/verification companion. The manuscript is careful in many places to avoid over-claiming (e.g., ΔNeff proxy explicitly not a torsion-module test; pseudo-Cl Monte Carlo not a sky measurement; SN-overlap caveat for w0wa). However, several aspects fall short of PRD methodological standards:

- Reproducibility surfacing is mixed into the main text as internal paths, run logs, and version chatter; this must be confined to a data-availability appendix or external repository notes.
- Key data/software artifacts lack permanent DOIs; “pending” is not acceptable at PRD.
- A central derived quantity (Ωa) is computed with an approximation for which no quantitative error budget is shown across the posterior; the paper draws posterior-mass inferences (13% with Ωa < 0.01) that require a documented accuracy assessment.
- The pseudo-Cl “pipeline bias floor” is defined for an unweighted estimator that the authors themselves show is sub-optimal; estimator-specific bias must be stated and, for a methods paper, the baseline should be the statistically efficient inverse-variance-weighted estimator or both must be reported side-by-side.
- A figure (Fig. 3) is intentionally published with a missing uncertainty for the canonical point—even though the rerun exists—impeding a direct appraisal of precision at the very reference mask.

Below I list detailed findings with classification, location, citation of the offending text, and concrete required fixes.

Findings

ESSENTIAL

P1B-E1 (Abstract; p. 1 and Data and Code Availability; pp. 15–16)
Problem: Permanent archival identifiers are missing. The manuscript repeatedly states “DOI assignment is pending” for the three HuggingFace datasets and relies on a mutable Git commit hash in the main text (e.g., “current snapshot commit: b22f8cc9”, “v1B.0.74”).
Required fix: Before acceptance, deposit immutable archives (e.g., Zenodo or similar with versioned DOIs) for all code and data needed to reproduce the frozen chains, NaMaster MC artifacts, and ALP chains. Replace all “pending” placeholders with minted DOIs and move commit-level details to a Data Availability appendix only.

P1B-E2 (Throughout, multiple sections; e.g., Sec. IV pp. 7–9; Sec. V p. 10; Appendix A pp. 15–16)
Problem: Intrusive internal bookkeeping appears in the body text: local file paths (“reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py”, “pod run pipelines/h200 results/…”), artifact filenames (e.g., c9f_negative_beta.json; c10_robustness_battery.json), and seed settings (“seed_base=42”). PRD style discourages operational logging in the scientific narrative.
Required fix: Remove all internal paths, filenames, runpod/pod references, and seed settings from the body. Retain these details only in a Reproducibility appendix or external README linked by DOI. Keep the main text readable and self-contained.

P1B-E3 (Sec. IV; Fig. 3 panel (b) and caption; p. 7)
Problem: The canonical fsky=0.32 point is plotted without uncertainty bars; the caption admits σβ was “not recorded” and later claims a rerun measured σβ=0.046°. Publishing a reference point without its uncertainty undermines the quantitative message of the figure.
Required fix: Replace Fig. 3 with the rerun point including (i) per-realization σβ and (ii) the standard error of the 500-MC mean at fsky=0.32, so that all three points display both uncertainties consistently. State the numerical σβ and SEM for each point directly in the caption.

P1B-E4 (Sec. VI; “ALP dark-energy fraction Ωa: definition and computation”; pp. 12–13)
Problem: The Ωa calculation uses onset condition 3H=ma and potential-dominated energy at onset, but the paper provides no quantitative validation of this approximation versus full EOM across the posterior support. The paper relies on Ωa to define “spectator-safe” subsets (e.g., 13% with Ωa<0.01).
Required fix: Provide a quantitative cross-check against full EOM integration for a representative posterior sample (or a grid), reporting the fractional error in Ωa introduced by the approximation across the posterior 68% and 95% credible regions. Include a table or figure with the error distribution and confirm that the Ωa<0.01 and Ωa<0.1 posterior-mass fractions are stable within those errors. If not, update those fractions.

P1B-E5 (Sec. IV; Eq. (1), robustness discussion; pp. 8–9)
Problem: The “pipeline bias floor” (|Δβ̂|=0.040°) is established for an unweighted template fit that the authors show is biased and sub-optimal; the inverse-variance-weighted estimator reduces the bias by ~80% (to −0.006°). For a methods paper, the baseline bias characterization must be estimator-appropriate and clearly labeled.
Required fix: Report estimator-specific bias floors explicitly: (i) unweighted χ² estimator bias and (ii) inverse-variance-weighted estimator bias, both with uncertainties on the mean bias from the 500-MC. State clearly in the abstract and conclusions that 0.040° is for the unweighted estimator only, and provide the corresponding number (and uncertainty) for the weighted estimator. If the unweighted estimator is retained as “canonical,” justify scientifically why a demonstrably sub-optimal estimator is the baseline for bias accounting.

P1B-E6 (Sec. V.B and Independent re-run cross-check; p. 10; Table I p. 19)
Problem: The frozen chains mix Planck PR4 (NPIPE) high-ℓ with Planck 2018 low-ℓ EE and lensing; the c15 verification uses PR4-consistent low-ℓ/lensing. The paper asserts 0.04σ agreement in ΔNeff but does not tabulate the PR4-consistent results alongside the frozen ones.
Required fix: Either (a) re-run the frozen results with PR4-consistent low-ℓ EE and lensing and report those as the primary results (recommended), or (b) add a new column to Table I with the PR4-consistent re-run posteriors (ΔNeff, H0, S8, etc.), with sample sizes and R̂, and an explicit quantitative comparison (Δ/σ) for each parameter.

P1B-E7 (Sec. VI; ALP posterior summaries; pp. 12–14)
Problem: The fixed-coupling (Caγ=8) inference quotes a median m≃36 H0 but lacks credible intervals; the continuous-prior run provides Caγ ranges but does not report credible intervals for m/H0 or θi under the fixed-coupling case referenced in the abstract.
Required fix: Provide 16–84% credible intervals for m/H0 and θi in the fixed-coupling (Caγ=8) inference used in the abstract, and ensure consistency between abstract and body. Where the posterior mass piles against prior edges (e.g., ma), disclose the prior sensitivity explicitly for those intervals.

MAJOR

P1B-M1 (Sec. III–V; SN overlap caveat; pp. 4–5, 10; Table II p. 20)
Problem: The w0wa results are derived from a product likelihood that double-counts ~20% shared SNe (DES-SN5YR × Pantheon+), acknowledged as a systematic. Yet, the main text and Table II present high-significance marginal-tail distances (+4.3σ, −3.6σ) and “phantom crossing” conclusions from this chain.
Required fix: Move the w0wa results to an appendix unless you present the two promised control chains (DESI+Planck+Pantheon+-only and DESI+Planck+DES-SN5YR-only) with quantitative shifts relative to the combined chain. Alternatively, add a prominent warning banner in Table II and in the body text above the table stating that these are overlap-uncorrected diagnostics only, not suitable for model selection or headline tensions. PRD will not accept phantom-crossing narratives based on a knowingly overlapped SN product likelihood without the control runs.

P1B-M2 (Sec. IV; pseudo-Cℓ binning; p. 8)
Problem: The fit includes 20 bins up to ℓ=1536 although the map band-limit is 1024; the authors state “changes nothing” when restricting to ℓ≤1024 but provide no numbers in the body.
Required fix: Report the recovered β̂ (and its uncertainty) for the ℓ≤1024 restriction in the main text (not only in an external artifact), and quantify the difference relative to the canonical result.

P1B-M3 (Sec. V; lensing likelihood variant; p. 15)
Problem: For the w0wa iter2 chain, the paper notes the use of planck 2018 lensing.native instead of .clik and that no release-pairing swap test was done.
Required fix: Perform and report a release-pairing swap test for w0wa (native vs clik) quantifying the impact on (w0, wa) and the derived wpivot, or revert to a single consistent lensing likelihood across chains and re-run.

P1B-M4 (Sec. VI; “25× fine-tuning” claim; pp. 11–13)
Problem: The “~25× misalignment tuning” is referenced to θi=0.5 versus θi≈0.1. This choice of “natural-prior midpoint” is arbitrary and prior dependent; the authors do later consider a sinθ prior, but the 25× headline remains anchored to a flat-θ midpoint.
Required fix: Define the tuning metric rigorously (e.g., relative prior volume fraction, or a Kullback–Leibler divergence toward the spectator-safe region) and compute it under both flat-θ and sinθ priors. Replace the single “25×” figure with a prior-explicit measure (e.g., “fractional prior volume of spectator-safe region”) and report its numerical value(s).

P1B-M5 (Sec. IV; estimator declaration; p. 8)
Problem: The estimator is introduced mid-paragraph. For a methods paper, the primary estimator and its weighting should be pre-declared at the start of the section.
Required fix: Recast Sec. IV to begin with an explicit “Estimator” subsection that (i) defines the pseudo-Cℓ workflow, (ii) states the canonical unweighted and the inverse-variance-weighted fits a priori, and (iii) states the physics of the template (with/without CBB) and why.

MINOR

P1B-n1 (Sec. IV; description of bias reduction; p. 9)
Problem: “≈5 percentage-point reduction in bias” is ambiguous (percentage of what). The text couples absolute bias in degrees and multiplicative bias in percent.
Required fix: Quantify both absolute and multiplicative biases explicitly (e.g., “absolute bias reduced from 0.032° to 0.019°; multiplicative under-recovery from 12% to 7%”).

P1B-n2 (Sec. III; MB–H0 offset; p. 5)
Problem: The 3.2σ offset is normalized by σMB only; the text states it’s “not a properly conditioned tension statistic”, which is correct, but the presentation is lengthy.
Required fix: Condense this subsection to a single sentence and move the derivation to an appendix or footnote. Keep the primary, properly conditioned H0-axis tension as the only quantitative statement in the body.

P1B-n3 (Fig. 1 and Table I; pp. 6, 19)
Problem: Fig. 1 caption references “119,617 post-burnin samples”; Table I lists total raw samples. While consistent, readers benefit from a single place summarizing raw, post-burnin, and effective sizes.
Required fix: Add a small table note in Table I with raw/post-burnin/effective sample counts for each frozen chain, or provide a one-line reference to the convergence CSV that lists these numbers.

P1B-n4 (Sec. IV; noise model; p. 7)
Problem: The per-pixel noise derivation is correct; add the exact Ωpix used to confirm 47.21 arcmin² for Nside=512.
Required fix: Add Ωpix = 4π/(12 Nside²) × (180/π × 60)² = 47.21 arcmin² inline for completeness.

P1B-n5 (Sec. VI; β periodicity; p. 12)
Problem: The Gaussian summary likelihood is justified by |β| ≪ 90°, but consider adding one sentence noting that the wrapped likelihood has negligible support beyond |β| ≳ 3σ ≈ 0.3° here.
Required fix: Add that short clarification to reassure readers unfamiliar with the periodicity point.

NIT

P1B-t1 (Throughout)
Problem: Occasional informal phrasing (“pod,” “anchor,” “artifact”) in the scientific narrative.
Required fix: Replace with neutral terms (“compute node,” “reference configuration,” “data product”) where they remain in the main text after E2 is addressed.

P1B-t2 (Typos/hyphenation)
Problem: Minor inconsistent hyphenation (“high-ℓ TTTEEE”, “low-ℓ/lensing,” etc.).
Required fix: Harmonize hyphenation per PRD style.

Arithmetic and internal consistency spot-checks
- ΔNeff posteriors in abstract match Table I: −0.020±0.169 and +0.058±0.179 (OK).
- H0 posteriors in abstract match Table I: 67.68±1.06 and 67.78±1.09 (OK).
- Hubble tension vs SH0ES: (73.04−67.68)/sqrt(1.06²+1.04²)=3.61σ (OK for “∼3.6σ”).
- S8 tension vs DES-Y3: (0.8245−0.776)/sqrt(0.017²+0.0089²)=2.53σ (OK for “2.6σ”).
- NaMaster noise conversion: ∆P=10 μK·arcmin; Ωpix=47.21 arcmin² gives σpix=1.455 μK (OK).
- Multiplicative under-recovery: 0.238/0.27=0.881; 0.302/0.342=0.883 (OK, ~12%).
- Template-fit SNR scaling with √fsky: 20.32×√(0.85/0.32)=33.1 vs reported 32.98 (OK).
- ALP birefringence: α/(4π)=5.81×10⁻⁴; ×8×1.06=4.93×10⁻³ rad=0.282° (OK).
- CaγΔφ/fa for βobs=0.342°: 0.342°=5.97×10⁻³ rad; divide by 5.81×10⁻⁴ gives ≈10.3 (OK).
- wpivot derivation: ap=0.790, zp=0.27; wpivot=−0.952±0.019 (OK).

Scope and novelty
The paper is careful not to over-claim on ΔNeff or the birefringence pipeline and flags the SN-overlap caveat for w0wa. However, for PRD, the pseudo-Cl bias characterization must be tied to an estimator that a practitioner would actually adopt, and critical reproducibility elements must be finalized and moved out of the narrative. The Ωa-based “spectator-safe fraction” requires a quantitative approximation error budget.

Recommended page-length
The manuscript is dense but not obviously bloated for its three-method scope (21 pages). After removing operational path/log chatter from the body (E2), the length will be more appropriate. No hard reduction requested beyond that cleanup.

## Summary recommendation
MAJOR REVISIONS

The submission contains solid technical work, and most numerical claims check out. However, PRD acceptance requires (i) final, DOI-minted reproducibility artifacts, (ii) removal of internal operational chatter from the main text, (iii) a quantitative error budget for the Ωa approximation that underpins the “spectator-safe” percentages, (iv) estimator-appropriate reporting of the pseudo-Cl bias floor, and (v) either consolidating Planck likelihood pairing or tabulating both variants. The w0wa SN-overlap issue must be demoted or accompanied by the promised control chains. Addressing these will bring the paper to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P1B-E8 (Conclusions; p. 14; Table IV vs Sec. VI text)
Problem: In Conclusions, the text mixes the fixed-coupling and continuous-prior results for the ALP mass scale. It states “posterior median m ≃ 40.5 H0 … the posterior-supported fixed-Caγ = 8 fit shifts well above the prior midpoint,” but 40.5 H0 is the median within the Ωa ≤ 0.01 spectator-safe subset of the continuous-prior run (Table IV), not the fixed-Caγ = 8 chain (median ≃ 36 H0).
Required fix: Disambiguate chain configurations in Conclusions. Quote m/H0 medians with 16–84% credible intervals separately for (i) fixed-Caγ = 8 and (ii) the continuous-prior run (and, if shown, for the Ωa ≤ 0.01 subset). Avoid attributing 40.5 H0 to the fixed-coupling inference.

P1B-E9 (Sec. IV; Eq. (1) and text around L223; pp. 7–8)
Problem: The objective function is labeled “χ²(β)” but is an unweighted squared residual of bandpowers without a covariance (it carries units of µK^4). Calling it “χ²” implies a statistically normalized quadratic form.
Required fix: Rename Eq. (1) to a unit-bearing “squared-residual cost function” (or normalize explicitly by an estimate of Var[C^EB_b] to make it a proper χ²). State units and, if kept unnormalized, clarify that only the argmin is used, not its value.

MAJOR

P1B-M6 (Sec. IV; pixel window handling; pp. 7–8)
Problem: The manuscript asserts that the Nside = 512 pixel window “cancels identically” because the template is evaluated at Nside = 512, but it does not document whether NaMaster decoupling included any beam/pixel transfer, nor verify that the returned C^EB_b and the template C^EE_b are consistently convolved.
Required fix: Explicitly document the NaMaster transfer handling (beam/pixel) and add a quantitative check showing that using pixel-window–deconvolved spectra vs convolved spectra yields indistinguishable β̂ within the MC error (e.g., run two 500-MC configurations with and without explicit pixel-window deconvolution of both data and template).

P1B-M7 (Sec. IV; purification test; p. 9)
Problem: Turning on B-mode purification (purify_b=True) produces an identical β̂ (0.238°), suggesting either (i) negligible E→B leakage under this mask/noise, or (ii) a configuration issue.
Required fix: Demonstrate purification efficacy by plotting the mean leakage C^BB (or EB leakage proxy) before/after purification, or by reporting Δβ̂ and its uncertainty under a deliberately more aggressive apodization (short taper) where leakage is known to be larger. Confirm that the field/mask options in NaMaster indeed enabled purification.

P1B-M8 (Sec. IV; weighted fit; p. 9)
Problem: The inverse-variance-weighted fit seems to use σ_b estimated from the same 500-MC ensemble being fit. Using the same MC to derive weights can induce noise-weight bias.
Required fix: Derive weights from an independent MC set or from an analytic covariance model, and re-quote the weighted-estimator bias and its uncertainty. State explicitly how σ_b is obtained and confirm stability when weights are varied.

P1B-M9 (Sec. IV; ℓ-range/workspace; pp. 7–9)
Problem: The binning extends to ℓ = 1536 while the map band-limit is 1024. Although the text argues this “changes nothing,” the workspace still couples modes near the cutoff, and aliasing/ringing could affect decoupled bandpowers.
Required fix: Rebuild the NaMaster workspace and binning with ℓmax = 1024 and re-run the 500-MC for βinj = 0.27°. Report β̂ ± SEM and the shift relative to the canonical configuration in the body text (not only in an external artifact). Confirm that the high-ℓ bins carry no leverage on β̂ (i.e., identical minima up to numerical tolerance).

P1B-M10 (Secs. III, V; ΔNeff robustness to BBN prior; pp. 3–6, 9–10; Table I)
Problem: The ΔNeff constraints rely on the CAMB PArthENoPE BBN-consistency track (Yp = Yp(Neff, ωb) by construction). It is well known that allowing Yp to float weakens Neff constraints.
Required fix: Add a control chain with free Yp (flat prior over a standard physical interval) to quantify the robustness of ΔNeff, H0, and S8. Report the shift and uncertainty broadening relative to Table I.

P1B-M11 (Secs. III, V; neutrino mass; pp. 3–6, 9–10; Table I)
Problem: Σmν is fixed at 0.06 eV. ΔNeff posteriors can be correlated with neutrino mass assumptions.
Required fix: Add a robustness chain with Σmν varied (e.g., one-parameter prior 0.06–0.3 eV) and report the impact on ΔNeff and H0. If computationally heavy, at least provide a literature-backed prior-sensitivity estimate and justify the fixed-Σmν choice for a ΔNeff proxy analysis.

MINOR

P1B-n6 (Secs. IV; mask definitions; pp. 6–8)
Problem: Declination cuts differ between configurations: canonical ACT-like mask uses dec ∈ [−65°, +25°], while the fsky = 0.65 sweep uses dec ∈ [−60°, +25°]. This can confuse direct comparability.
Required fix: Tabulate the exact sky cuts and the resulting fsky for each mask (canonical, 0.65, 0.85) in the main text or figure caption, and note explicitly that the dec cuts differ by design.

P1B-n7 (Table IV; p. 21)
Problem: For the “full chain,” the m/H0 entry reads “median ≃ 36, broad” without credible intervals, unlike other rows which provide percentiles.
Required fix: Replace the “broad” descriptor with 16–84% credible intervals for m/H0 in the full chain for consistency with other table entries.

P1B-n8 (Appendix C; β units in likelihood; p. 17)
Problem: The Gaussian summary likelihood for βobs is specified numerically but the units of β in the sampling code (degrees vs radians) are only implicit.
Required fix: Add a one-line declaration that the likelihood and sampled β are in degrees, and that the ALP-predicted β is converted to degrees before likelihood evaluation (to preclude silent unit mismatches).

P1B-n9 (Table II; χ² context; p. 20)
Problem: χ² totals are given with uncertainties, but the total number of data points (and effective dof) going into χ²_total is not summarized.
Required fix: Add a brief note summarizing the number of data points in each likelihood and the approximate total dof, so readers can contextualize χ²_total.

NIT

P1B-t3 (Sec. VI; anharmonic corrections in Ωa; pp. 12–13)
Problem: The Ωa estimate notes O(θi²/12) anharmonicity but does not reference the standard correction factors used in the axion literature for large θi.
Required fix: Either cite and adopt a standard anharmonic-correction factor (e.g., Marsh 2016 review) in Eq. (9) or state quantitatively (with a plot/table) that your full-EOM cross-check in E4 bounds the anharmonic error well below the decision thresholds for the Ωa cuts.

Rationale for only-new findings
These items were not raised in the initial review. They focus on (i) a configuration/summary mismatch between ALP chains (E8), (ii) nomenclature/units rigor for the estimator (E9), (iii) pseudo-Cℓ technicalities that affect bias attribution (M6–M9), (iv) key ΔNeff robustness tests standard in the literature (M10–M11), and (v) clarity/consistency improvements in tables, masks, and units (n6–n9, t3). All arithmetic spot-checks not mentioned here matched the manuscript’s numbers within rounding.