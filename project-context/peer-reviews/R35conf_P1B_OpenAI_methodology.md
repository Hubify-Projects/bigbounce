# P1B R35conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.61.pdf` md5=56ec3f27 pages=19
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6298 chars)
**Wall time**: 396.5s

---

Referee report on: “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall scope
- I reviewed the full 19-page manuscript, including abstract, figures, tables, equations, and appendices. I audited all headline numbers, effect sizes, and most internal arithmetic claims where derivable from the text. I focused on statistical methodology, estimator declarations, significance reporting, consistency and reproducibility claims, and dimensional checks.

Strengths (context only; not a substitute for required fixes)
- The paper clearly scopes three separate analyses and repeatedly avoids overclaiming: ΔNeff runs are framed as a null proxy, the NaMaster exercise is framed as a pipeline-validation MC rather than a sky detection, and the ALP section is framed as a consistency check with disclosed fine-tuning.
- Many numerical statements are arithmetically consistent on spot checks (e.g., 12% multiplicative bias from 0.238/0.27 ≈ 0.882; β product CaγΔφ/fa ≈ 10.3 from βobs; H0 tension ≈ 3.6σ).

However, for Physical Review D standards, several issues must be addressed before the work can be considered. Below I list all findings with severity, precise locations, the problem, and required fixes.

Findings

ESSENTIAL

P1B-E1 — Abstract footnote in abstract (p. 1, immediately under abstract)
- Problem: The abstract carries a lettered footnote “a Eskilt & Komatsu 2022 disambiguation: …” occupying a multi-line paragraph under the author block. PRD generally does not allow footnotes in the abstract; moreover, key dataset/likelihood provenance belongs in the body or Data/Methods.
- Required fix: Remove the footnote from the abstract. Move the full content into Section IV or VI (where the birefringence datasets are discussed) and/or into a dedicated footnote in the main text. Ensure the abstract contains no footnotes.

P1B-E2 — SN overlap acknowledged but uncorrected while reporting “σ” departures (Sec. III, pp. 4–5; Table II p. 18)
- Problem: The DES-SN5YR and Pantheon+ product-likelihood stack contains ~20% overlapping SNe with different Malmquist corrections. While the text flags this, it still reports quantitative deviations from ΛCDM (+4.3σ for w0, −3.6σ for wa; phantom crossing) as headline marginal-tail distances. This is not acceptable without a joint-covariance or no-overlap reanalysis, because the quoted “σ” are sensitive to double-counting and shared systematics.
- Required fix: Either (a) re-run the w0wa chain with an overlap-aware joint covariance (or remove one of the SN sets) and update all quoted significances accordingly; or (b) move all w0wa “σ” distances out of the main text into a clearly marked exploratory appendix and remove σ-quantification from the main narrative. In either case, do not report σ-levels from the overlap-contaminated product likelihood as if they were publication-grade.

P1B-E3 — Figure 2(b) axis labeling unclear (Fig. 2, p. 6)
- Problem: The x-axis label in panel (b) reads ambiguously in the rendered figure (“(x xfull_tension) / full_tension”) with missing minus sign and σ, making the normalization unclear.
- Required fix: Correct the axis label to a precise, self-explanatory form, e.g., “(x − xfull_tension)/σfull_tension” for each parameter, and ensure legible typography.

P1B-E4 — Reproducibility: permanent archival and version pin (Appendix A, p. 13; Data and Code Availability, p. 13)
- Problem: The paper states “DOI assignment is pending” for the HuggingFace datasets and relies on a mutable GitHub repository with a version-string in the TeX. PRD requires citable, immutable archival of data/code used to produce the published results.
- Required fix: Deposit all frozen artifacts (chains, NaMaster MC outputs, ALP MCMC chains, YAMLs) in a permanent archive with DOI (e.g., Zenodo or institutional repository). Replace “pending” with final DOIs. Provide a tagged Git commit hash matching the deposited snapshot.

P1B-E5 — Mixed Planck PR4 high-ℓ with 2018 low-ℓ and lensing without a release-consistency test (Sec. III, p. 3; Sec. V.A, p. 8; Table III, p. 18)
- Problem: The ΔNeff results mix PR4 CamSpec high-ℓ with 2018 low-ℓ EE/TT and lensing. Although labeled as “the standard pairing,” the manuscript explicitly states no pairing-swap test was performed and any induced bias is “unquantified.” Given that ΔNeff and H0 are the load-bearing outputs, leaving this untested is not up to PRD standards.
- Required fix: Run a control chain with a fully PR3/2018-consistent highℓ/lowℓ/lensing set (or a fully PR4-consistent stack if available) and report the shift on ΔNeff and H0. If computationally expensive, at minimum provide a limited-sample diagnostic demonstrating that the differences are negligible at the quoted precision.

MAJOR

P1B-M1 — Adoption of a known biased estimator as the “canonical” choice (Sec. IV, pp. 7–8; Fig. 3)
- Problem: The unweighted χ2 template-fit estimator is retained as the “canonical baseline,” even though the robustness tests show it induces an ~12% multiplicative under-recovery, with ≈80% of the bias attributable to the equal weighting of noise-dominated high-ℓ bins. While the paper states this is for comparability with public drivers, endorsing a known-biased estimator is not methodologically sound for a validation study.
- Required fix: Make the inverse-variance–weighted estimator the primary baseline in the validation (with the unweighted estimator moved to a comparison), and report all MC recovery metrics for both. If you keep the unweighted estimator for comparison, lead with the weighted results and clearly caution users about the bias if they adopt the unweighted form.

P1B-M2 — Missing “analytic −CBB” bias estimate that is referenced (Sec. IV, p. 8)
- Problem: The text states “consistent with the analytic −CBB template-mismatch estimate above (≈5 percentage points of the 12%).” No such analytic derivation appears “above.” This is an unsubstantiated quantitative claim.
- Required fix: Provide the explicit analytic derivation quantifying the expected bias contribution from omitting the −CBB term (e.g., start from EB = 0.5 sin 4β [CEE − CBB], linearize in β, show the fractional bias term for your bandpowers) or remove the “analytic estimate” claim and keep the empirical robustness-only statement.

P1B-M3 — Data availability language includes internal debugging artifacts (Appendix A, p. 13)
- Problem: Data availability includes explicit discussion of an “off-by-one column-index bug” in an export, with a corrected JSON and a README mapping fix. While transparent, the published record should not depend on buggy artifacts.
- Required fix: Replace discussion of the buggy export with a clean archival snapshot in which only corrected, verified artifacts are present. If you insist on keeping the note, move it to a changelog in the repository, not in the paper’s Data Availability section.

P1B-M4 — Overlap-integral S8 tension statistic without methodological specifics (Table I footnote, p. 17)
- Problem: You quote posterior-overlap integrals (0.05, 0.12) between Gaussians or 1D marginals but do not specify the exact numerical method (e.g., kernel, grid resolution, whether the marginal is Gaussian-summarized or sampled).
- Required fix: Either remove the overlap-integral numbers or add a short methods line: exact formula, resolution, and whether the marginals are Gaussianized or taken from GetDist KDE.

P1B-M5 — Release-pairing caveat belongs in Results summary (Sec. VII, p. 12)
- Problem: The known limitation of PR4/2018 pairing is mentioned in Sec. III but not repeated where ΔNeff/H0 are summarized in Conclusions. Readers may miss an important caveat.
- Required fix: In VII. Conclusions, add a single-sentence limitation that the ΔNeff results use PR4 high-ℓ + 2018 low-ℓ/lensing without a pairing-swap test and that a consistency check is planned or now provided per P1B-E5.

MINOR

P1B-n1 — Inverse-variance combination of β (Sec. VI, p. 10, Eq. 4)
- Problem: Your quoted inverse-variance average is βcombined = 0.241° ± 0.061°. A direct recompute using 0.300±0.110 and 0.215±0.074 yields ≈0.243° ± 0.061°. The difference is tiny but exceeds rounding in the mean.
- Required fix: Recompute with precise central values and uncertainties; report 0.243° or clarify if you used more precise internal values (e.g., 0.2995). Note explicitly the mean and σ were computed with inverse-variance weights 1/σ2.

P1B-n2 — Clarify template choice and bandlimit handling (Sec. IV, p. 8)
- Problem: You state “Restricting the fit to bins with ℓ ≤ 1024 changes nothing (0.238°) — the noise-only bins above the band limit carry zero template weight.” This is plausible but depends on how CEEb (template) is constructed.
- Required fix: Add one sentence clarifying that the template’s CEEb is set to zero for bins with central ℓ above 1024, hence zero template weight, and that the decoupled EB estimates for those bins were excluded or included with zero template weight.

P1B-n3 — Validity range of BBN Yp(Neff,Ωbh2) predictor (Sec. III, p. 3)
- Problem: You assert the prior range Neff ∈ [2.046, 5.046] is “within the calibrated domain of the CAMB BBN module” without a citation.
- Required fix: Cite CAMB’s BBN predictor documentation or a PArthENoPE range reference that explicitly states the valid Neff interval for Yp consistency. Alternatively, soften to “within the commonly used domain” if a range is not documented.

P1B-n4 — Units consistency (global)
- Problem: H0 units appear as “km s−1 Mpc−1” and “km/s/Mpc” in different places.
- Required fix: Standardize to “km s−1 Mpc−1” throughout.

P1B-n5 — Small typographical issues (multiple pages)
- Problem: Examples include spacing around degree symbols (e.g., “0.27◦injec­tion”), spurious ligatures/hyphenation in a few places, and an extra space in “σ ˆβ.”
- Required fix: Run a careful proof to eliminate these minor typesetting artifacts.

P1B-n6 — Standalone-reader test (Introduction, p. 2)
- Problem: The introduction leans heavily on “Paper I(a)” for the scientific motivation and on “Paper II–IV” for other results. While the scope statement says those are out of scope, a standalone reader would benefit from a 2–3 sentence self-contained motivation for why each of the three analyses here is necessary and sufficient for “technical verification.”
- Required fix: Add a short paragraph that restates, without external cross-reference, what each of the three analyses verifies and what it does not, in terms that do not depend on companion papers.

NIT

P1B-N1 — Reference details (Bibliography)
- Problem: Ref. [4] (ACT DR6) is cited as an arXiv preprint with a future-year arXiv ID; ensure the authorship and title match the version you used and that the identifier is correct.
- Required fix: Verify and update the bibliographic entry with the latest arXiv version and author list.

P1B-N2 — Figure utility
- Problem: Fig. 1 (corner) and Fig. 2 (ΔNeff comparison) are useful; ensure all axes have units where appropriate (H0 axis in Fig. 1 should include “km s−1 Mpc−1”).
- Required fix: Add units in figure axes where missing.

P1B-N3 — Effect-size context (Sec. III, pp. 4–5)
- Problem: Where σ-levels are given for w0, wa, you correctly caution on evidences. Adding one line quantifying the fractional shift (e.g., wpivot +2.5σ corresponds to Δw ≈ 0.048 at zp ≈ 0.27) would clarify absolute effect size.
- Required fix: Optional one-liner; not mandatory if the overlap issue is addressed per P1B-E2.

Arithmetic and dimensional checks performed
- ΔNeff means/σ (Table I) are self-consistent; one-sided 95% limits (0.31; 0.39) are plausible given the two-sided posteriors and renormalization under ΔNeff ≥ 0.
- H0 tension with Riess (67.68 ± 1.06 vs 73.04 ± 1.04) → Δ = 5.36; σcomb ≈ 1.48; Δ/σ ≈ 3.62: consistent with “3.6σ.”
- MB−5log10 h constants: recomputed to within 0.002 mag of quoted.
- S8 two-Gaussian combination: 0.827±0.010 ⊗ 0.776±0.017 → 0.814±0.0086: in line with 0.814±0.009; tension of DES-Y3 vs Planck+BAO+SN ≈ 2.5–2.6σ matches text.
- NaMaster multiplicative bias ~12% verified from 0.238/0.27 and 0.302/0.342; template-fit SNR scaling with √fsky matches within 0.5%.
- Noise per pixel at Nside=512 from ΔP=10 μK·arcmin: σpix=1.455 μK as stated.
- EB rotation template sin 2β cos 2β CEE = 0.5 sin 4β CEE matches the exact uniform-rotation relation.
- ALP β calculation: αEM/(4π) ≈ 5.81×10−4; with Caγ=8, Δφ/fa=1.06 gives 4.93×10−3 rad ≈ 0.282°, consistent with 0.28°.
- CaγΔφ/fa ≈ β/[αEM/(4π)] ≈ 0.005966/5.81×10−4 ≈ 10.27: consistent with “≈10.3.”
- Caγ range 8.6–160 from Δφ/fa ∈ [1.19, 0.064] consistent with quoted bounds.

Scope and claims
- The manuscript generally distinguishes between incomparable σ-like quantities (pipeline template-fit SNR vs sky-detection σ; 3.9σ inverse-variance auxiliary vs 3.6σ joint analysis). Where side-by-side mentions occur (Sec. IV, Sec. VI), the text states they are not directly comparable—this is appropriate.
- The ΔNeff proxy is correctly framed as not a test of torsion theory.
- The ALP is correctly framed as “not distinctive to ECH” and the misalignment/coupling tunings are disclosed.

Length
- For the stated contribution (three verification analyses), 19 pages is borderline long due to extended runbook/log details. Consider trimming internal bookkeeping (e.g., long sample-count reconciliation footnote) once reproducibility DOIs are provided, to 15–16 pages without loss of substance.

## Summary recommendation
MAJOR REVISIONS

Justification: The paper is careful in scope and numerically consistent on many fronts, but it does not yet meet PRD methodological and archival standards. Essential issues include removing the abstract footnote; resolving or quarantining σ-level claims from the SN-overlap product-likelihood; providing a pairing-consistency check for the Planck likelihood mix; and stabilizing the data/code with permanent DOIs. Methodologically, adopting a known-biased unweighted estimator as “canonical” in a validation study should be reversed or at least subordinated to a weighted baseline with clear guidance. Addressing these items will likely require modest additional computations (one or two control chains) and editorial restructuring, after which the work could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (second-pass audit)

Essential

P1B-E6 — One-sided 95% ΔNeff limit (Planck+BAO+SN) is numerically inconsistent with the stated definition (Sec. III, p. 3)
- Problem: You define the one-sided 95% limit as “the 95th percentile of the posterior renormalised on ΔNeff ≥ 0.” For the Planck+BAO+SN chain (μ = +0.058, σ = 0.179), the renormalised 95th percentile is ≈0.27, not 0.39. Specifically, Ftrunc(x) = [Φ((x−μ)/σ) − Φ((0−μ)/σ)] / [1 − Φ((0−μ)/σ)], so the 95th quantile solves Φ(z) = Φ(−0.324) + 0.95[1 − Φ(−0.324)] = 0.373 + 0.95×0.627 = 0.96865, giving z ≈ 1.85 and x = μ + zσ ≈ 0.058 + 1.85×0.179 ≈ 0.27. The quoted 0.39 corresponds roughly to μ + 1.96σ without truncation.
- Required fix: Recompute and correct the Planck+BAO+SN one-sided 95% bound under your stated truncation-and-renormalisation definition (≈0.27). If you intend a different convention, restate it clearly and update both limits for internal consistency.

Major

P1B-M6 — Heterogeneous analysis software and lensing hooks across chains (Sec. V.A, Table III; Appendix A)
- Problem: Different chains use different Cobaya versions (v3.5 “original” vs v3.6.1 “verification”), and the iter2 w0wa chain swaps planck 2018 lensing.clik for planck 2018 lensing.native. These choices can induce small but non-negligible shifts, especially in parameters like τ, As, and derived σ8/S8, and thus in ΔNeff/H0 when low-ℓ/lensing constraints feed back.
- Required fix: Standardize on one Cobaya version and one lensing interface across all production chains, or provide a controlled A/B test showing that version and .clik/.native choices produce shifts negligible at your quoted precision for ΔNeff, H0, and S8.

P1B-M7 — Extremely small-sample quantiles reported for the θi ≤ 0.1 “strict spectator” sliver (Table IV; Sec. VI, p. 11)
- Problem: You quote weighted 16/50/84 percentiles of Caγ in the θi ≤ 0.1 subset based on only 42 raw samples (0.47% raw; 0.33% by weight). Even with the “indicative only” caveat, publishing quantiles from such a tiny, highly weighted-degenerate subset is not statistically robust.
- Required fix: Either (a) perform targeted sampling (e.g., importance resampling/nested sampling) to adequately populate the θi ≤ 0.1 region and then report stable posterior summaries; or (b) remove the sliver quantiles and retain only the qualitative statement that the required Caγ increases substantially in this tuned corner.

P1B-M8 — “Common beam would cancel” assertion is untested (Sec. IV, p. 6)
- Problem: The text asserts that a common instrumental beam applied to both simulated maps and the recovery template “would cancel in the β estimate,” but no test with a nontrivial beam is shown. In pseudo-Cℓ pipelines, beam and pixel-window effects can interplay with masking and binning and need not cancel perfectly in finite-ℓ bins, especially under unweighted fits.
- Required fix: Either add a short MC control (repeat the β = 0.27° injection with a realistic Gaussian beam, with and without deconvolution) demonstrating negligible impact on recovered β within your quoted bias floor, or remove/soften the “would cancel” claim.

Minor

P1B-m7 — Figure 2(a) SM marker mislabeled (Fig. 2, p. 6)
- Problem: The panel (a) annotation shows “SM (Neff = 0)”. The Standard Model reference here is ΔNeff = 0, not Neff = 0.
- Required fix: Change the marker text to “SM (ΔNeff = 0)” and verify consistency with the figure caption and main text.

P1B-m8 — Binning-edge specification is ambiguous for integer binning (Sec. IV, p. 6)
- Problem: You state “20 linear integer-edge bins from np.linspace(30, 1536, 21).” linspace returns floats; it is unclear how these were converted to integer edges (floor/round/ceil), which affects band definitions near ℓ = 1024 and 1536.
- Required fix: Specify the exact rounding/casting rule applied to define integer bin edges, and confirm that bins with central ℓ > 1024 carry zero template weight (see P1B-n2 in the first report) to avoid hidden leverage from noise-only bins under the unweighted fit.

P1B-m9 — ALP sliver statistics presented despite low ESS (Appendix C, ESS table; Table IV)
- Problem: The derived-parameter ESS for β is adequate, but ESS in narrow derived subsets (e.g., Ωa ≤ 0.01; θi ≤ 0.1) is not reported and could be very low. Table IV mixes “indicative only” language with numerical summaries that suggest precision.
- Required fix: Report subset-specific ESS (or effective posterior mass) alongside any quoted summary statistics for derived slivers, and suppress or clearly de-emphasize numeric summaries where ESS is insufficient.

Nits

P1B-N4 — Figure 1 axis units (Fig. 1, p. 6)
- Problem: The H0 axis in the corner plot appears unitless in the rendered figure (the table provides units). For a standalone figure, unit labels should be explicit.
- Required fix: Add “km s−1 Mpc−1” to the H0 axis (and ensure all other axes with physical units are labeled accordingly).

P1B-N5 — Inconsistent nomenclature for ΔNeff across text and figures (global; Fig. 2)
- Problem: Some places say “Neff” when the plotted variable is ΔNeff (e.g., Fig. 2(a) marker; see P1B-m7), which can confuse readers.
- Required fix: Audit figures and captions to ensure ΔNeff is consistently labeled when that offset is the sampled parameter.

P1B-N6 — Minor clarity on mask fsky “Planck-like” label (Sec. IV, p. 8)
- Problem: The fsky = 0.85 mask is described as “Planck-like,” which could be misread as matching an official Planck polarization mask. Since this is a synthetic galactic cut with apodization, it is only broadly similar.
- Required fix: Rephrase to “Planck-scale sky fraction (fsky ≈ 0.85) using a simple galactic cut,” to avoid implying identity with an official Planck mask.

Explanation
This second-pass audit focused on recomputing every stated bound and cross-checking figure labels and software consistency. The main new substantive issue is the Planck+BAO+SN one-sided ΔNeff bound (P1B-E6), which does not match your stated truncation-and-renormalisation definition. Additional methodological clarity is needed around heterogeneous software/lensing hooks (P1B-M6), small-sample sliver quantiles (P1B-M7), and the untested “beam cancellation” assertion (P1B-M8). The remaining items are labeling/clarity nits to prevent reader confusion.