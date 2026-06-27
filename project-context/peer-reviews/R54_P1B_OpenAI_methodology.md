# P1B R54 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R54_P1B/paper1b_mcmc_companion.pdf` md5=0b4a8768 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6845 chars)
**Wall time**: 270.0s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
- Focus: statistical-method validity; internal arithmetic/consistency; estimator declarations; error propagation; dimensional analysis; figure/table numerics; abstract-to-body fidelity.
- I audited all scalars in the abstract and conclusions, re-computing quoted σ/tension values from the paper’s own numbers; checked equations for dimensional consistency; examined all figures/tables for consistency with text; and tracked caveats vs. claims.

Overall assessment
- The paper is careful about scope and repeatedly avoids overclaiming. Many computations check out numerically. However, several methodological and presentation issues require correction before PRD publication, including one formula-level notation error, a release-pairing inconsistency in the Planck likelihoods that must be resolved with reruns, and the use of an overlap-uncorrected SN product likelihood in the w0wa analysis while quoting tail σ-distances. Data/artefact provenance must also be finalized (DOIs) for PRD standards.

Findings

ESSENTIAL

P1B-E1
- Location: Sec. VI (LiteBIRD forecast), p. 16, paragraph beginning “LiteBIRD is projected to achieve...”
- Problem: The significance expression misprints the variances: “|0.342 − 0.27|/ √ 0.032 + 0.0942 ≈ 0.7σ”. The intended expression is |Δβ|/sqrt(0.03^2 + 0.094^2). As written, it reads as sqrt(0.032 + 0.0942), which is dimensionally and numerically wrong.
- Required fix: Replace with the correct formula: |0.342° − 0.27°|/sqrt((0.03°)^2 + (0.094°)^2) = 0.072°/0.0987° ≈ 0.73σ. State it explicitly with squares on the uncertainties.

P1B-E2
- Location: Sec. V B (Release-pairing note) p. 11 and throughout Table III notes
- Problem: The “frozen” ΛCDM+ΔNeff results mix Planck PR4/NPIPE high-ℓ CamSpec with Planck 2018 low-ℓ TT/EE and 2018 lensing (.clik). Only one of the two dataset combinations (Planck+BAO+SN) has a PR4-consistent verification rerun (c15), and even there the low-ℓ/lensing pairing differs from the frozen chains. The full-tension combination (which is quoted in the abstract) was not re-run with PR4-consistent low-ℓ EE and lensing.
- Required fix: Re-run both frozen ΛCDM+ΔNeff dataset combinations with a fully consistent PR4 pairing for low-ℓ EE and lensing (e.g., planck 2020 lollipop.lowlE and planckpr4lensing) and report the posteriors. Alternatively, freeze both combinations with the 2018 low-ℓ/lensing set, but then remove PR4 claims. In either case, align pairing across all quoted “frozen” chains and update the abstract numbers to match the final consistent pairing. Provide ΔNeff shifts (in σ units) between the mixed and consistent pairings for both combinations.

P1B-E3
- Location: Sec. III (Caveats), p. 4–5; Sec. V C; Table II
- Problem: The w0wa chain uses an overlap-uncorrected product likelihood of DES-SN5YR and Pantheon+ (∼20% shared SNe with different Malmquist corrections). Despite multiple caveats, the paper still reports +4.3σ (w0) and −3.6σ (wa) tail distances and states “phantom crossing”. For PRD methodology standards, either a joint covariance (or overlap-aware combination) must be used, or the quoted σ-distances must be removed/isolated to avoid misinterpretation.
- Required fix: Provide the two overlap-control runs you already describe (Planck+DESI DR2+Pantheon+ only; Planck+DESI DR2+DES-SN5YR only) and quantify the shift in (w0, wa) and wpivot relative to the overlap-uncorrected product. Alternatively, remove all numerical σ-distance claims (4.3σ, 3.6σ, wpivot = −0.952 ± 0.019 at +2.5σ) and replace with a qualitative statement pending an overlap-corrected analysis. Clearly segregate any numerical tail distances to a supplementary robustness note if the joint covariance is not yet implemented.

P1B-E4
- Location: Sec. IV (NaMaster pipeline) p. 8–11; Abstract
- Problem: The reported “pipeline-recovery bias floor” (worst-case |bias| = 0.040° ± 0.002°) is estimator-dependent. The robustness battery shows ≈80% of this bias disappears if the fit is inverse-variance weighted. In the abstract and conclusions this is called the “observed pipeline bias floor,” which can be construed as a method floor rather than an estimator choice.
- Required fix: In the abstract and all summary text, qualify this as “observed bias for the unweighted χ² template-fit estimator” and explicitly note that inverse-variance weighting reduces the bias to ≈0.006°. If you wish to retain a single headline number, report both: unweighted (−0.032° to −0.040°) and inverse-variance weighted (≈−0.006°) with identical MC settings. Make the estimator choice and its bias consequence explicit in the abstract.

MAJOR

P1B-M1
- Location: Sec. VI, Eq. (9), p. 15; Spectator-subset reporting (Table IV)
- Problem: Eq. (9) uses the potential-dominated approximation ρa(zosc) ≈ m^2 f^2 [1 − cos θi], and then applies a single (1 + zosc)^3 dilution. For zosc close to matter–Λ transition (m/H0 ~ O(1)), the “single-epoch onset” plus instantaneous switch to quadratic oscillations is an approximation. You state this was “verified against full EOM” but provide no quantitative error bound.
- Required fix: Provide a quantitative validation: for representative posterior-supported points at m/H0 ~ 1–5 and θi ~ 0.1–0.3, give the fractional difference between Eq. (9) and the full EOM–integrated ρa(z=0). Report the maximum deviation over the spectator-safe subset (Ωa < 0.01). If >5%, either propagate this additional uncertainty into the Ωa fraction statements (44%, 13%) or adjust the statements.

P1B-M2
- Location: Sec. VI, ALP coupling inference, p. 14–16; Fig. 4
- Problem: You infer a broad Caγ posterior with a flat prior on Caγ ∈ [4, 60] (after truncation was noted for [1, 30]) and flat θi ∈ [0.01, π] (and also present a cos θi-flat rerun). The strong prior-dependence is noted but not quantified in effect size on the headline fractions (e.g., Ωa < 0.01 = 13%). 
- Required fix: Provide a prior-robustness table for the principal reported fractions and medians (e.g., median Caγ and Ωa<0.01 fraction) under at least these two priors: flat θi vs. flat cos θi, and Caγ upper bound 60 vs. 100. Report the differences. If large (>30% relative), state them alongside the headline numbers.

P1B-M3
- Location: Sec. IV, “no beam is applied” and pixel window paragraph, p. 8
- Problem: The validation assumes an identical beam and pixel window between synthetic skies and template so that effects cancel. In a real pipeline, beam mismatch and pixel-window deconvolution residuals can drive EB leakage and estimator bias. You assert cancellation but do not provide a quantitative mismatch test.
- Required fix: Add a short MC battery entry quantifying sensitivity to a plausible Gaussian beam mismatch (e.g., 1–5% FWHM difference between map and template deconvolution) and to modest pixel-window misestimation (e.g., use Nside=512 maps with a template evaluated at an incorrect pixel window by ±1%). Report the induced bias in β̂. If negligible (<0.005°), state it; otherwise update the “bias floor” caveat accordingly.

P1B-M4
- Location: Appendix A (Data and Code Availability), p. 17–19
- Problem: “DOI assignment is pending” for HuggingFace datasets; acceptance in PRD generally requires finalized, citable archival. The text includes internal version tags (“in-tex v1B.0.76”, commit SHAs) and process notes better suited to a README than the manuscript.
- Required fix: Assign DOIs for all three public datasets and cite the final DOIs in the paper. Replace the mutable commit-hash prose with a stable release tag (e.g., Zenodo DOI with GitHub archive). Move the process-oriented “column-permutation warning” and CHANGELOG references to the repository; keep the manuscript’s Data Availability concise and stable.

P1B-M5
- Location: Sec. III (MB–H0 posterior-offset check), p. 7
- Problem: The 3.2σ “offset along the Pantheon+ constraint axis” normalizes by σMB alone. You correctly state it’s descriptive and not a conditioned tension. However, the presentation risks reader confusion between this and the canonical H0 tension.
- Required fix: Add the 2D-conditioned offset along the MB–H0 degeneracy direction or remove the “3.2σ” numerical value altogether and keep only the qualitative statement that it is the same underlying H0 tension.

MINOR

P1B-m1
- Location: Abstract, first paragraph; Sec. III and V, Table I
- Problem: Reported “309,189 frozen samples across two converged dataset combinations” is load-bearing for convergence. You later use 30% burn-in uniformly; GetDist used 20% in one diagnostic. This is described at length in fn. 1, but a single authoritative post–burn-in sample count for the headline combinations would help.
- Required fix: Add a concise parenthetical in Table I or Sec. III stating the uniform post–burn-in sample counts used for all reported numbers (e.g., “216,432 post–burn-in samples across both frozen chains under a 30% cut”).

P1B-m2
- Location: Sec. IV, footnote 4 (SNR), p. 10
- Problem: The definition SNRtmpl uses σb from MC realizations; this is fine, but please define whether σb is computed on CEB,decoupled or on the un-decoupled pseudo-Cℓ and clarify whether inter-bin covariance is neglected (as it appears).
- Required fix: Add one sentence: “σb denotes the per-bin standard deviation of the decoupled EB bandpower across the 500 realizations; inter-bin covariance is neglected in SNRtmpl.”

P1B-m3
- Location: Sec. VI, Fig. 4 caption and text, p. 18
- Problem: Multiple significant figures (e.g., H0 = 1.44×10−33 eV) and percentiles reported to unnecessary precision.
- Required fix: Round to two significant figures for constants and to the precision supported by the chains (e.g., Caγ 16–84% to one decimal).

P1B-m4
- Location: Acknowledgments, p. 17
- Problem: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant...” This is atypical for PRD and unnecessary.
- Required fix: Remove this sentence from the manuscript.

P1B-m5
- Location: Throughout (e.g., Sec. IV, p. 8–11)
- Problem: Occasional hyphenation/line-break artifacts from typesetting (per‑realization, ex‑plicitly).
- Required fix: Clean up hyphenation/line breaks in the final typeset version.

NITS

P1B-n1
- Location: Sec. IV, mask description, p. 8–9
- Problem: “ACT-like footprint” is vague.
- Required fix: Provide the exact RA/Dec cuts as a set/footprint figure or include a mask image in the supplementary material.

P1B-n2
- Location: Table II footer note (b), p. 6
- Problem: “numerically coincident with, and unrelated to, the §IV injection angle β = 0.27°” — helpful but could be tighter.
- Required fix: Rephrase to “coincidental numerical similarity; unrelated quantities.”

P1B-n3
- Location: Table I, S8 overlap integral, p. 5
- Problem: You present an overlap integral value (0.05) computed on a trapezoidal grid. It’s fine, but an exact two-Gaussian overlap has a known form.
- Required fix: Optionally add the analytic two-Gaussian overlap number as a cross-check or drop “trapezoidal grid” implementation details.

Abstract-last drift sweep
- The abstract’s ΔNeff, H0 values match Table I exactly; the “~3.6σ” H0 tension recomputes to 3.61σ from quoted numbers — OK.
- NaMaster bias numbers (−0.032°, −0.040°) match Sec. IV; add the “unweighted estimator” qualifier (P1B-E4).
- ALP: “posterior-supported fixed-coupling (Caγ = 8) accommodation shifts to m ≫ H0 (median ≃ 36 H0)” matches Sec. VI; spectator tuning caveat matches body. OK.

Figures and tables audit
- Fig. 1 (corner): axes labeled; numbers consistent with Table I.
- Fig. 2: ΔNeff posteriors consistent with means/σ. 
- Fig. 3: Panel (a) shows biases 0, −0.032°, −0.040°; Panel (b) fsky sweep consistent with text; σβ scaling checked (√fsky) via footnote 4 — numerically correct. Axes have degrees; OK.
- Fig. 4: Parameter triangle consistent with text; caption clear about priors. 
- Table I: numbers and R̂, ESS consistent across text.
- Table II: recomputed tail distances and wpivot match; χ² channel sums consistent with total within rounding.
- Table III: likelihood stacks listed; the mixed PR4/2018 pairing inconsistency must be resolved (P1B-E2).
- Table IV: posterior-mass fractions and β medians consistent with text; the “∼O(1)” for m/H0 in the θi≤0.1 sliver is vague (P1B-m3 asks for rounding; optional to add a numeric range).

Bibliography spot-check
- [3] Planck PR4 birefringence value β = 0.30° ± 0.11° matches cited paper’s abstract.
- [5] Eskilt & Komatsu β = 0.342° ± 0.094° matches; 3.6σ = 0.342/0.094 = 3.64 — OK.
- [9] SH0ES 73.04 ± 1.04 km s−1 Mpc−1 matches the 2022 ApJL.
- [20] NaMaster ref correct.
- Ensure ACT DR6 preprint entry [4] has a stable arXiv ID; at acceptance, verify bibliographic details.

Length and focus
- 21 pages for a methods companion paper with three distinct analyses is on the long side. The content is dense but some implementation-process details (internal file paths, CHANGELOG prose) can be removed. Recommended target: ≤18 pages by moving repository/process-specific details to supplemental or the repository.

## Summary recommendation
MAJOR REVISIONS

The paper is careful and numerically consistent in most places, but it must (i) correct a notation error affecting a significance formula; (ii) eliminate the Planck likelihood release-pairing inconsistency by re-running both frozen ΛCDM+ΔNeff combinations with consistent low-ℓ/lensing (and update the abstract accordingly); (iii) either provide the promised overlap-control SN runs for the w0wa chain or remove numerical σ-distance claims; (iv) qualify the NaMaster “bias floor” as estimator-specific and add a brief beam/pixel-window mismatch sensitivity test; and (v) finalize data/artefact DOIs and streamline the Data Availability section. Addressing these will bring the manuscript up to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P1B-E5
- Location: Sec. IV, “Noise model and injections” (p. 8) vs Eq. (1) (p. 9)
- Problem: The template is described as sin(2β) cos(2β) CEEb in prose, but Eq. (1) uses ½ sin(4β) CEEb. These are mathematically identical, but the switch in notation without stating the identity is easy to misread as a change of model.
- Required fix: Add a one-line identity after Eq. (1): “Note sin(2β) cos(2β) = (1/2) sin(4β); we use the latter in Eq. (1).”

MAJOR

P1B-M6
- Location: Sec. IV, “Canonical estimator choice” (p. 11) and earlier pipeline description
- Problem: The manuscript asserts that the unweighted χ² template-fit is the “canonical baseline to match the estimator configuration used in the public NaMaster driver scripts (e.g., [5])”. This is consequential because the reported “bias floor” depends strongly on the weighting. However, no concrete code reference (file/line) from the cited public pipeline is provided to verify that those analyses used unweighted (not inverse-variance–weighted) fits.
- Required fix: Provide a precise citation to the public code (repository commit and file/line) demonstrating the unweighted χ² usage in [5] (or ACT DR6), or rephrase to “we adopt an unweighted χ² for simplicity” and treat the unweighted vs. weighted choice explicitly as a design choice rather than a match to prior work.

P1B-M7
- Location: Sec. III, “Sampling configuration” (p. 3); BBN consistency statement
- Problem: The analysis relies on CAMB’s PArthENoPE BBN-consistency module across a prior Neff ∈ [2.046, 5.046] and states this is “within the calibrated domain.” CAMB/PArthENoPE emulators are commonly calibrated around Neff ≈ 3; support at Neff ≲ 2.1 can be model/version dependent.
- Required fix: Document the validity range for YHe(Neff) for the specific CAMB version used (v1.6.5) and PArthENoPE predictor, with a reference to the emulator’s calibration domain. Add a robustness check: a short control chain with free YHe (BBN-consistency off) to quantify the impact on ΔNeff (report the mean shift in units of σ). If non-negligible (>0.2σ), include it as a systematic or adopt free-YHe for the headline.

P1B-M8
- Location: Sec. III, “Sampling configuration” (p. 3) and Table I
- Problem: ΔNeff constraints can shift depending on the neutrino-mass prior. The analysis fixes Σmν = 0.06 eV with one massive eigenstate; no robustness test is reported against a free Σmν or three-degenerate-mass assumption.
- Required fix: Provide a robustness chain allowing Σmν to vary with a standard prior (e.g., Σmν ≥ 0.06 eV) and/or using three degenerate massive neutrinos. Quote the ΔNeff and H0 shifts (in σ units). If shifts exceed ~0.2σ, state this systematic in the abstract/body.

P1B-M9
- Location: Sec. V C (p. 12), Table II footer; Release-pairing note
- Problem: The w0wa “iter2” chain mixes PR4/NPIPE high-ℓ CamSpec with a Planck 2018 lensing.native likelihood; a PR4-consistent low-ℓ/lensing swap test is “left to a post-submission follow-up.” Given the prominence of the tail-distance discussion (even caveated), the pairing inconsistency should be resolved now.
- Required fix: Re-run the iter2 stack with PR4-consistent low-ℓ EE and lensing (e.g., planck 2020 lollipop.lowlE and planckpr4lensing) and report the changes to (w0, wa, wpivot). Alternatively, if keeping 2018 low-ℓ/lensing, state explicitly that the w0wa chain also uses 2018 low-ℓ/lensing and remove PR4 language from this chain.

P1B-M10
- Location: Sec. IV, “Mode-coupling matrix and binning” and “Only this single binning/ℓ-range configuration is exercised” (p. 8–9)
- Problem: Only a single ℓ-range/binning is used for the bias characterization. E/B leakage and estimator curvature can be ℓ-dependent, especially at low ℓ where mask coupling is strongest.
- Required fix: Add a minimal ℓ-range robustness sweep (e.g., refit using ℓ ∈ [60, 1024] and [100, 1024]) and report the change in β̂ and bias for the canonical fsky = 0.32, βinj = 0.27° case. If the shift is >0.005°, note it in the abstract’s estimator-qualification sentence; if <0.005°, state that explicitly.

P1B-M11
- Location: Sec. VI, “H0 marginalization note” within spectator-subset readout (p. 15)
- Problem: The claim “Marginalizing H0 over the Planck 1σ interval shifts Ωa by ≲ 3% (Ωa ∝ H0^−2)” omits the fact that zosc in Eq. (7) also shifts with H0 (via H(z)). Without a quantification on representative points, “≲ 3%” is unsupported.
- Required fix: Provide a quantitative check at a few posterior-supported spectator points (e.g., m/H0 ~ 2–5, θi ~ 0.1–0.3): compute Ωa at H0 ± 1σ, solving zosc each time, and report the fractional change. If the bound exceeds 3% anywhere in Ωa < 0.01, update the stated bound.

MINOR

P1B-m6
- Location: Abstract, first paragraph (H0 tension sentence)
- Problem: “the ΔNeff extension does not reduce the residual ∼3.6σ tension with SH0ES...” For the Planck+BAO+SN combination, the tension from quoted numbers is ≈3.5σ, not 3.6σ.
- Required fix: Either specify the tension separately for the two combinations (3.61σ and 3.49σ) or say “∼3.5–3.6σ” to avoid implying both are 3.6σ.

P1B-m7
- Location: Sec. IV, footnote 4 and “Sky-fraction sweep” paragraph (p. 10)
- Problem: The phrase “per-realization angle-recovery ratio β/σβ” uses β to denote the recovered mean but “β” elsewhere denotes the injected angle. This is easy to misread.
- Required fix: Clarify notation: replace with “|β̂|/σβ per realization (where β̂ is the recovered angle)” in both places.

P1B-m8
- Location: Sec. VI, “three committed configurations totaling 9,720 accepted samples” (p. 14) vs. continuous-prior chain usage (Fig. 4; Table IV)
- Problem: The headline “9,720 accepted samples” refers to three configurations that exclude the continuous-prior c5 chain (8,955 accepted) used for Fig. 4 and Table IV. Readers can misinterpret the total sampling depth.
- Required fix: Add a clarifying sentence: “Including the continuous-prior chain used for Fig. 4/Table IV brings the total ALP accepted samples to 18,675.”

NITS

P1B-n4
- Location: Sec. IV, estimator weighting and covariance (related to footnote 4)
- Problem: SNRtmpl implicitly neglects inter-bin covariance (likely small, but not stated). While you mention this in a minor fix (P1B-m2 from the initial review), the body text where SNRtmpl is first defined does not.
- Required fix: Add “Inter-bin covariance is neglected in SNRtmpl; we estimate σb from the per-bin scatter of the decoupled EB bandpowers across MC realizations.”

Explanation
These items focus on estimator-definition clarity, BBN/Σmν robustness for ΔNeff, consistent Planck release pairing in the w0wa chain, minimal ℓ-range robustness for the NaMaster bias, and a few remaining arithmetic/notation clarifications. They are distinct from, and additive to, the original review’s findings.