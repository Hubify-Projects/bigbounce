# P1B D2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=b166f4c0 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7705 chars)
**Wall time**: 352.4s

---

Production D2 visual check (camera-ready status)
- Overall: The rendered 21-page PDF looks camera-ready. The D1 issues (squished tables, cramped/missing figures, label overlaps, text overflow) appear resolved.
- Tables: I (p.5), II (p.6), III (p.12), IV (p.16), V (p.20) are full-width, legible, and do not overflow columns. Row spacing and column alignment are clean; no clipped text.
- Figures: Fig. 1–2 (p.7), Fig. 3 (p.8), Fig. 4 (p.17) are well placed with adequate margins. Axis labels and tick labels are readable; legends and annotations are not overlapping. No colorbar or label collisions observed.
- Text and equations: No spill into margins or adjacent columns; no overfull boxes; equations fit within columns.
- Float placement: No half-blank pages or awkward float jumps. No orphaned headings at page tops or bottoms.
Conclusion on visuals: Camera-ready clean. No new visual defects or regressions to flag.

Referee report (methodology/rigor)

ESSENTIAL findings
P1B-E1 (Data/Code availability and persistence) — Sec. “Data and Code Availability” (p.16–18) and Appendix A (p.18–19)
- Issue: The paper relies on external datasets/code repositories (GitHub and HuggingFace) but states “DOI assignment is pending” for the HuggingFace datasets; links are mutable, and there is no frozen release tag/DOI snapshot for the exact version analyzed.
- Required fix: Provide persistent, citable archives with DOIs (e.g., Zenodo DOIs for the exact GitHub commit b22f8cc9 and for each HuggingFace dataset). Insert the DOIs in the manuscript and ensure the archived snapshots contain exactly the frozen chains/artifacts used to generate all quoted numbers (matching the in-paper version tag v1B.0.75 and commit hash).

MAJOR findings
P1B-M1 (Over-emphasis on a non-robust w0–wa chain; release pairing) — Sec. III (p.4–6), Sec. V.C (p.11), Table II (p.6)
- Issue: The w0–wa “iter2” chain uses a mixed Planck PR4 CamSpec high-ℓ with Planck 2018 low-ℓ TT/EE and “lensing.native” rather than PR4-consistent low-ℓ/lensing. The manuscript itself notes no dedicated release-pairing robustness test was performed for this chain, yet it reports large “+4.3σ” and “−3.6σ” tail distances prominently.
- Required fix: Either (a) provide a minimal robustness check by rerunning/spot-checking the iter2 chain with PR4-consistent low-ℓ EE and lensing and show the (w0, wa, wpivot) shifts are negligible at the quoted precision, or (b) demote all quantitative claims based on this chain (notably the “+4.3σ” and “−3.6σ” tail distances and “phantom crossing”) to an appendix or supplementary note, with explicit language in the main text that these are illustrative and not robust. Avoid spotlighting high-σ distances drawn from a chain acknowledged as lacking a pairing-robustness test.

P1B-M2 (Operational repository/process minutiae in the main text) — Sec. IV (p.8–10), Data/Code Availability (p.16–18), Appendix A (p.18–19)
- Issue: The main narrative includes low-level file paths, run-pod pipeline names, commit hashes, seed IDs, JSON artifact filenames, and an internal “column-permutation bug” postmortem. These are appropriate for a repository/SM but distract in a PRD main text.
- Required fix: Move operational details (file paths, pod run names, seed bases, JSON filenames, “column-permutation warning” and mapping) from the main text and Data Availability section into Supplementary Material or a dedicated “Reproducibility Note” hosted in the repository. In the paper, keep only high-level pointers (repository URL, frozen release DOI, brief description of contents).

P1B-M3 (Terminology misuse in bias discussion) — Sec. IV, Robustness battery (p.10)
- Text: “... replacing the crude CBBℓ = 0.05 CEEℓ proxy with a CAMB lensed-ΛCDM BB spectrum recovers βˆ = 0.251° (bias −0.019°), consistent with the empirical −CBBℓ template-mismatch robustness test ...; the ≈5 percentage-point reduction in bias is the empirical effect...”
- Issue: “percentage-point reduction” is inappropriate for an angular bias measured in degrees. The change is 0.013°, corresponding to ≈40% relative reduction from 0.032°.
- Required fix: Replace “≈5 percentage-point reduction in bias” with a quantitatively correct phrasing, e.g., “a 0.013° absolute reduction (~40% relative).”

P1B-M4 (Unconverged chain mention in the body) — Sec. III (p.3, footnote/paragraph)
- Issue: The in-progress “Planck-only run currently at sub-convergence sample count (R̂−1 ~ 0.05)” is mentioned in the body.
- Required fix: Remove this from the main text or move to an appendix with a clear statement that no results are drawn from it.

MINOR findings
P1B-m1 (MB–H0 offset statistic presentation) — Sec. III, “MB–H0 joint-posterior offset check” (p.7)
- Text: Reports a “3.2σ” figure for the offset along the SN degeneracy axis using σMB only, followed (correctly) by a disclaimer that this is not a conditioned tension statistic.
- Issue: The “σ” language invites misinterpretation; even with the caveat, readers may treat it as a proper tension.
- Required fix: Replace “3.2σ” with plain-language description (e.g., “0.156 mag offset relative to the MB marginal width”) and keep the caveat. Avoid any “σ” language for non-conditioned, single-axis normalizations.

P1B-m2 (Define symbols on first use) — Sec. IV (p.8–10)
- Issue: fsky, ℓmax, Nside, and “purify_b” appear before being explicitly defined in prose.
- Required fix: Briefly define each at first occurrence for standalone readability: fsky (sky fraction), Nside (HEALPix resolution), ℓmax (maximum multipole), purify_b (NaMaster B-mode purification flag).

P1B-m3 (AI tool acknowledgment — check journal policy) — Acknowledgments (p.18)
- Issue: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant...”
- Required fix: Confirm PRD policy on AI tool acknowledgments. If acceptable, retain; otherwise, move to a competing-interests or data/methods note per editorial guidance.

P1B-m4 (PACS numbers) — Header (p.1)
- Issue: PACS numbers are largely deprecated.
- Required fix: Remove PACS or replace with current keyword classification per PRD guidance.

P1B-m5 (Consistency of “headline” wording on β) — Abstract (p.1), Sec. IV (p.7–8), Fig. 3 caption (p.8)
- Issue: The paper does consistently caution that pipeline SNR is not a sky significance. However, the abstract’s phrasing “headline used throughout this paper” could be softened to avoid implying multiple independent detections.
- Required fix: Rephrase to: “We adopt the published WMAP+Planck summary β = 0.342° ± 0.094° (3.6σ) [5] as the primary external constraint and do not re-analyze sky maps.”

P1B-m6 (Bibliography format) — Refs. [3–5,19,28] (p.20–21)
- Issue: Mixed styles (“arXiv preprint (2025)”; missing journal info where available). PRD typically requires consistent citation formatting.
- Required fix: Standardize references to PRD style with journal, volume, page, year (or arXiv-only if unpublished), ensuring arXiv IDs and years match the cited versions.

NITs
P1B-n1 (Hyphenation and linebreak artifacts) — multiple pages
- Issue: Hyphenation artifacts like “decon￾volution” from PDF extraction are invisible in the PDF but watch for any spurious hyphens in the final production LaTeX.
- Fix: Production proofread.

P1B-n2 (Minor wording) — Sec. IV (p.9)
- Issue: “The production suite used non-negative injections; a dedicated rerun β = −0.27° ... recovers ... confirming sign-symmetric recovery...”
- Fix: Consider stating explicitly that the unweighted estimator bias is odd in β with equal magnitude.

Arithmetic and methodological audits (spot checks)
- H0 tension: |73.04 − 67.68| / sqrt(1.06^2 + 1.04^2) = 5.36 / 1.487 ≈ 3.60σ (matches “∼3.6σ”).
- One-sided ∆Neff bounds (truncated at ∆Neff ≥ 0): Full-tension mean −0.020, σ 0.169 yields ~0.31 at 95th percentile; Planck+BAO+SN mean +0.058, σ 0.179 yields ~0.40. Consistent with text (p.3–4).
- S8 recomputation: For σ8 = 0.812, Ωm = 0.312, S8 = 0.812 √(0.312/0.3) ≈ 0.828 (matches 0.827 ± 0.010).
- Pivot redshift and wpivot: Using the provided covariance and variances yields ap ≈ 0.790, zp ≈ 0.27, wpivot ≈ −0.952 ± 0.019 (matches text).
- ALP birefringence amplitude: α/(4π) ≈ 5.81×10^−4; with Caγ=8 and ∆φ/fa=1.06 gives β ≈ 0.00493 rad ≈ 0.282°, consistent with “≈ 0.28°” (p.13).
- Constant-product requirement: βobs (radians)/[α/(4π)] ≈ 5.97×10^−3 / 5.81×10^−4 ≈ 10.3, consistent (p.14).
- Inverse-variance combination of Planck/ACT β: β = 0.241° ± 0.061°, significance ~3.95σ; text correctly labels as an optimistic upper bound and not used as headline (p.13).

Stand-alone reader test
- The paper is self-contained for its three technical aims (ΛCDM+∆Neff proxy, NaMaster pipeline validation, ALP consistency check). Dependence on Paper I(a) is clearly limited to theoretical motivation/background. Symbols and assumptions are largely defined. Minor symbol-definitions fixes (P1B-m2) will help.

Effect-sizes and comparability
- The manuscript conscientiously distinguishes pipeline SNR vs. sky-detection σ and provides effect-size context for w0wa (e.g., ~1.7% change in H(z=0.5)). The MB–H0 “σ” point needs phrasing fix (P1B-m1).

Figure and table audit
- Captions match the body claims. Axes are labeled; units correct. Numeric values in Tables I–II align with calculations shown in text and cross-checks above.

## Summary recommendation
MAJOR REVISIONS

The core analyses are careful, the statistical procedures are appropriately caveated, and the arithmetic checks out. However, before publication in PRD, (1) the data/code artifacts must be archived with persistent DOIs and linked in the paper, and (2) the prominent w0–wa tail-distance claims should either be backed by a simple release-pairing robustness check or demoted to supplementary material. Additionally, operational repository minutiae should be moved out of the main text, and a few minor clarity/terminology fixes are needed. With these addressed, the paper would meet PRD methodological and presentation standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E2 (Convergence claim vs threshold; c15 rerun) — Sec. V.B (p.11)
- Issue: The c15 “verification” rerun is described as “converged … to R̂−1=0.0147.” Elsewhere the paper treats R̂−1<0.01 as a publication-quality threshold (Table II and multiple places). Calling R̂−1=0.0147 “converged” is inconsistent.
- Required fix: Rephrase to “near-converged” or report it as a spot-check not meeting the R̂−1<0.01 target. Alternatively, extend sampling to R̂−1<0.01 and then keep the 0.04σ comparison.

P1B-M5 (“χ2” nomenclature and missing covariance in EB fit) — Sec. IV, Eq. (1) and surrounding text (p.9–10)
- Issue: The cost function is called χ2(β) but is an unweighted sum of squared residuals without per-bin variances or the (known, non-negligible) bin–bin covariance after MASTER deconvolution. Dimensionally, this is not a χ2 statistic and the unaccounted covariance can bias minima and misstate uncertainties.
- Required fix: Rename to “unweighted least-squares cost” (not χ2). Add a covariance-weighted test using the MC-estimated bandpower covariance matrix to show the recovered β and bias remain within quoted tolerances, or clearly confine all quantitative bias statements to the unweighted-cost definition.

P1B-M6 (Units of β in estimator not specified) — Sec. IV, Eq. (1) (p.9)
- Issue: The trigonometric functions imply β must be in radians, but the paper otherwise reports β in degrees (and uses a degree-spaced fit grid). The unit used inside sin(4β) is not stated.
- Required fix: State explicitly that β is converted to radians inside Eq. (1) and code, while results are reported in degrees.

P1B-M7 (Anharmonic correction in Ωa estimate not treated) — Sec. VI, “Ωa definition and computation” (p.15)
- Issue: Eq. (9) uses ρa(zosc)≈m^2af^2a[1−cosθi] without the standard anharmonic correction factor that becomes significant as θi→π. The prior admits θi up to π, and the text mentions O(θ^2/12) corrections but does not incorporate or bound their impact on Ωa.
- Required fix: Include an anharmonic correction (or cite/apply a standard fitting function) and quantify the impact on the Ωa cuts, or restrict θi to the harmonic regime in the reported subsets and say so.

P1B-M8 (“Systematic floor” wording could mislead) — Sec. IV (p.8–10)
- Issue: The phrase “carry forward as the observed NaMaster pipeline bias floor” for |∆β̂|=0.040° risks being interpreted as a general systematic floor on sky analyses, despite the text later clarifying it is an MC-pipeline figure only.
- Required fix: Replace “bias floor” with “MC pipeline bias in this configuration” and reiterate it is not a sky-measurement systematic or a universal floor.

P1B-M9 (Ambiguity in σ-comparison for the 0.04σ agreement) — Sec. V.B (p.11)
- Issue: The “0.04σ agreement” between ∆Neff posteriors compares a mean shift (0.0066) to a single σ (0.179), not a combined uncertainty. Using the combined σ would yield ≈0.03σ.
- Required fix: Specify the normalization explicitly (vs. the frozen-chain σ), or report the combined-σ normalization to avoid ambiguity.

P1B-M10 (Use of ℓ bins above the band limit in the estimator) — Sec. IV (p.9–10)
- Issue: The estimator sums over 20 bins up to ℓ=1536 while the map band limit is 2Nside=1024. Although the template weight is zero above 1024 (making those terms β-independent constants), including noise-only bins in the cost is methodologically untidy and can complicate future changes if weighting is altered.
- Required fix: Restrict the sum in Eq. (1) to ℓ≤1024 in the baseline configuration or document that an equivalent masked-bin variant was used (and matches the reported numbers).

P1B-M11 (Neutrino-sector assumption not stress-tested) — Sec. III (p.3–5)
- Issue: The ∆Neff proxy run fixes Σmν=0.06 eV (one massive state). Since Neff–Σmν degeneracies can weakly interact with H0 and ns, a fixed Σmν may slightly bias ∆Neff bounds at current precision.
- Required fix: Add a short robustness note (or a quick control run) allowing Σmν to vary under a minimal prior to show that the headline ∆Neff/H0 posteriors are stable at the quoted precision.

P1B-M12 (Onset criterion 3H=ma used without justification) — Sec. VI (p.15)
- Issue: The onset-of-oscillation condition 3H(zosc)=ma is adopted without reference or justification (some literature uses H≈ma or includes anharmonic/temperature-dependent prefactors).
- Required fix: Cite the convention (e.g., Turner 1986; standard axion relic-abundance treatments) and comment that switching to H=ma (or a calibrated prefactor) does not change any Ωa subset classification at the quoted precision.

P1B-m7 (Rounding and inequality mismatch in convergence table) — Table I (p.5)
- Issue: The text states “all sampled parameters … satisfy R̂−1 < 3×10−3,” while the Planck+BAO+SN worst row reports 0.003. With rounding, this is “≈3×10−3,” not strictly <.
- Required fix: Change to “≤ 3×10−3” or report more digits.

P1B-m8 (Natural-units convention not stated) — Throughout (Eqs. 3, 4, 7, 9)
- Issue: Several equations implicitly adopt natural units (ħ=c=1), mixing “mass” and “rate” (ma and H) and angles; the convention is not declared.
- Required fix: Add a one-sentence statement that natural units are used unless otherwise noted.

P1B-m9 (Figure-caption/body unit clarity for β grid) — Fig. 3 caption (p.8) and Sec. IV (p.9)
- Issue: The caption and body mention a β grid but do not state if the grid step is in degrees or radians; the text later implies 10−3-degree resolution.
- Required fix: State the grid step and unit explicitly in the caption or main text.

P1B-m10 (Null-procedure comparability: tension metrics) — Table I note and Sec. III (p.5–7)
- Issue: The S8 “2.6σ” two-Gaussian tension and the overlap integral 0.05 are reported side-by-side without an explicit “not directly comparable” qualifier (they come from different null procedures). Elsewhere the manuscript is careful about σ comparability.
- Required fix: Add a short sentence that the σ and overlap integral are different tension metrics and not directly comparable.

P1B-m11 (Planck likelihood availability/licensing note) — Data and Code Availability (p.16–18)
- Issue: Reproducibility instructions omit that using PR4 CamSpec TTTEEE and Planck likelihoods requires obtaining the public likelihood packages (and, in some cases, registering or agreeing to license terms). This can block a cold-start reproduction.
- Required fix: Add a sentence with links to the Planck likelihood repository and a note on any required registration/license acceptance so readers can actually run the YAMLs.

P1B-m12 (Minor clarity in abstract on ALP prior vs posterior) — Abstract (p.1)
- Issue: The sentence “the scan-prior m ∼ H0 region brackets the published … but the posterior-supported fixed-coupling (Caγ=8) accommodation shifts to m ≫ H0” is correct but can be misread as implying both are comparably supported.
- Required fix: Clarify: “the prior box includes m∼H0, but the posterior at fixed Caγ=8 prefers m ≫ H0 (median ≃36 H0).”

P1B-N3 (Explicit “radians vs degrees” in Eq. 4 conversion) — Sec. VI (p.13)
- Issue: The rad→deg conversion is shown, but the final number is rounded; some readers may check with fewer digits and get 0.283°.
- Fix: Consider giving β=0.282°–0.283° (rounded consistently) or keep 0.282° and note rounding.

P1B-N4 (Tiny arithmetic normalization nit) — Sec. V.B (p.11)
- Issue: “0.04σ agreement in ∆Neff” uses one-sided σ normalization; using combined σ would give ≈0.03σ.
- Fix: Specify the normalization choice or use combined σ.

These issues are new relative to the initial review and focus on arithmetic/units rigor, estimator definition and covariance handling, convergence claims, and clarity about priors/units.