# P1B R52 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/public/papers/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7196 chars)
**Wall time**: 303.3s

---

Referee report on “Technical Verification Companion to the ECH Spin‑Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator‑ALP Model”

General assessment
- Scope and positioning are clear: this is a methods/verification companion, not an ECH theory paper. Many caveats are explicit and the authors generally separate pipeline recovery, proxy MCMC, and model consistency from sky-detection claims.
- The paper is long for the stated contribution and contains extensive repository/process prose that could be trimmed for PRD formatting.
- Most numerical claims are internally consistent; I verified the headline σ and ratio computations. However, several methodological items require tightening to meet PRD standards, and a few presentation issues could mislead non‑specialists if not sharpened.

Findings

ESSENTIAL

P1B-E1 (Appendix A, p. 15–16): “DOI assignment is pending … identifiers will be inserted at submission … current snapshot commit: b22f8cc9”
- Problem: PRD requires stable, citable archival links at acceptance. “Pending” DOIs and a moving-head commit hash are not acceptable in the published record.
- Required fix: Before acceptance, (i) mint DOIs for all referenced datasets (chains, NaMaster artifacts, ALP chains) and insert the final DOIs; (ii) tag the exact code release used for the paper and cite the immutable tag/Zenodo DOI instead of an ephemeral commit; (iii) remove “pending” language.

P1B-E2 (Sec. V.C/Table II, p. 10, 20): σ-distances for w0 and wa presented as “+4.3σ” and “−3.6σ” in the table body
- Problem: Although the text and footnote (a) state these are marginal-tail posterior distances and not Bayes/evidence or frequentist significances, the σ annotations appear in the main table cells and can be misread as detection significances.
- Required fix: Move the σ-distances into the footnote only, or mark every σ in the table with an inline “marginal-tail distance (not a detection)” label. Add “Illustrative only; SN-overlap systematic active” to the table title. Alternatively, relocate Table II to an appendix labeled “diagnostic cross-check” if the main text must remain clean of overlap-uncorrected results.

P1B-E3 (Sec. IV, p. 7–9; Fig. 3): NaMaster “observed pipeline bias floor” quoted as a single number (0.040°) with no uncertainty
- Problem: A bias used as a carried-forward systematic floor must be quoted with its uncertainty (standard error on the 500‑MC mean) and a stability check vs. NMC; otherwise the precision is overstated.
- Required fix: Quote the standard error of the 500‑MC mean at the worst‑bias point (using the explicitly measured σβ and N=500), and add a brief NMC-stability note (e.g., N=1000 rerun at the worst‑case point shows the mean within ±X×10−3°). If you intend the number purely as a descriptive MC-recovery bias, say so next to the value and give the ±.

P1B-E4 (Sec. VI, Eq. 9, p. 13): Ωa calculation neglects standard anharmonic corrections near θi ≳ O(1)
- Problem: You compute posterior fractions for Ωa < X using V(ϕ) at onset without the well-known anharmonic enhancement factor f(θi) (Turner‑type correction). Because your θi prior extends to π, the Ωa boundary can be biased in the large‑angle region.
- Required fix: Either (a) include the standard anharmonic correction factor in Eq. (9) and the per-step Ωa evaluation, or (b) restrict all Ωa‑based subset statements to a small-angle prior (θi ≲ 0.3) where the quadratic approximation is accurate, and explicitly state that the reported Ωa fractions apply only in that regime. In either case, report the size of the correction to the 44% / 13% fractions.

MAJOR

P1B-M1 (Sec. IV, p. 7–9): Unweighted χ² template fit adopted as the “canonical estimator”
- Problem: The equal-weight fit is statistically inefficient and is shown to be the dominant source of the ≈12% multiplicative bias; the weighted estimator removes ≈80% of this bias. The justification (“matches published driver scripts”) is not documented with a citation, and readers may mistake your baseline for best practice.
- Required fix: (i) Add an explicit literature citation that the referenced public drivers indeed used an unweighted estimator; otherwise adopt inverse‑variance weighting as the primary baseline and retain the unweighted result as a historical cross‑check. (ii) In either case, report both results clearly in Fig. 3 or the text, and emphasize that the weighted estimator is the statistically efficient choice.

P1B-M2 (Sec. V, p. 10): Release pairing consistency
- Problem: You demonstrate 0.04σ stability in ΔNeff when swapping low‑ℓ EE/lensing likelihoods to PR4‑consistent counterparts. You also state H0, σ8, S8, Ωm stability <0.1σ—this is good—but this statement is not backed in text for all derived quantities in Table I.
- Required fix: Add a one‑sentence numerical line listing the four auxiliary parameters (H0, σ8, S8, Ωm) with their deltas and combined-σ comparisons for the c15 rerun vs. the frozen chain (you already report the numbers; group them in one place). This will make the “provides an empirical bound on pairing-induced bias” fully documented.

P1B-M3 (Sec. IV, Fig. 3 caption p. 7–8): Missing error bars at the canonical fsky = 0.32 point
- Problem: The figure shows no per‑realization error bar at fsky = 0.32 (later measured as σβ = 0.046°). PRD expects uncertainties on plotted points when they underpin a bias claim.
- Required fix: Update Fig. 3(b) to include the σβ and standard-error-of-the-mean bars for fsky = 0.32 using the dedicated 500‑MC rerun. State these uncertainties in the caption.

P1B-M4 (Sec. IV, p. 7): ACT-like footprint parameters inconsistent across text
- Problem: Canonical mask uses dec ∈ [−65°, +25°] (fsky = 0.32), while the fsky = 0.65 mask later uses dec ∈ [−60°, +25°]. The change may be intentional but is unexplained.
- Required fix: Clarify that the two declination cuts differ by design (and why), or harmonize the definitions. Provide the exact fsky values to three decimals for each mask.

P1B-M5 (Sec. V.C, p. 10, Table II): Overlap-uncorrected SN product likelihood in a headline table
- Problem: Despite explicit caveats, placing an overlap‑uncorrected w0wa result in a main‑text table invites over‑interpretation.
- Required fix: Either (i) move Table II to an appendix, or (ii) retain it in main text but add a boldface line to the caption: “Overlap‑uncorrected DES‑SN5YR × Pantheon+ product likelihood; results are diagnostic only and not suitable for model selection,” and remove “phantom‑crossing indicated” from the body of the table (keep it in the caption with the same caveat).

MINOR

P1B-m1 (Sec. III, p. 3–5): ΔNeff one‑sided bound computation
- Comment: Method explained clearly. For transparency, add the closed‑form Gaussian‑truncation check as you did in prose (e.g., show the 0.977 CDF computation) or provide the exact weighted‑sample 95th‑percentile value in an appendix table.

P1B-m2 (Sec. IV, p. 7): SNRtmpl definition
- Problem: SNRtmpl is described verbally; σb is not defined symbolically.
- Required fix: Add the explicit expression SNRtmpl^2 = Σb [C^th_EB(b)/σb]^2 and define σb as the per‑bin standard deviation across the 500 MC realizations.

P1B-m3 (Sec. VI, Eq. 4, p. 11): Conventions for β normalization
- Comment: You note competing αEM/(2π) vs αEM/(4π) conventions. Add a one‑line pointer to the precise Lagrangian normalization used to avoid ambiguity (you already mention it; italicize or typeset the equation to be unmissable).

P1B-m4 (Sec. VI, p. 12–14): θi prior choice and spectator‑sliver mass
- Problem: You do a good job quantifying prior dependence. For completeness, add a single sentence quantifying how the Ωa < 0.01 fraction changes under the cosθ prior (you provided θi ≤ 0.1 changes; report Ωa sliver change too if available).

P1B-m5 (Sec. III, p. 5): MB–H0 degeneracy constant
- Comment: The consistency check is useful. Consider adding the numerical 3.6σ tension in H0 terms right there to tie the two views together.

P1B-m6 (Appendix A, p. 15–16): Internal process/log language
- Problem: Detailed internal filenames, “parameter_summary_CORRECTED.json”, and column‑permutation bug discussion need not be in the main paper.
- Required fix: Compress to a single sentence: “Some auxiliary JSON exports in early internal builds had a column‑indexing bug; all results here are recomputed from the raw chains. See repository release notes for details.”

P1B-m7 (Sec. V, p. 9–10): “planck 2018 lensing.native” versus “.clik”
- Problem: Different lensing likelihood backends are mentioned for different chains. While probably negligible, the reader benefits from clarity.
- Required fix: Add one sentence stating that the .native vs .clik backend choice produces negligible shifts at your precision, with a citation to Planck likelihood documentation or a brief numerical check.

P1B-m8 (Sec. IV, p. 8–9): β grid search details
- Problem: You mention 10−3 degree β-grid resolution in passing.
- Required fix: State the β‑grid range explicitly and confirm that tightening the grid does not shift the mean at the 10−3° level.

NITS

P1B-n1 (Global): Length
- Comment: For a methods companion, 21 pages is long. Consider trimming repository/process narration and moving the DESI w0wa diagnostic table to an appendix to target ≲15 pages.

P1B-n2 (Global): Micro-typography
- Examples: “σ ˆβ” (footnote 4) should be σ(β̂); stray soft hyphenation artifacts like “load￾bearing” in the PDF; standardize “deg” vs “◦” spacing. Correct at proof stage.

P1B-n3 (Sec. IV, p. 7): Mask fsky values
- Suggest reporting fsky with three decimals in each case for easier independent replication.

Numerical checks audited (spot‑checks)
- Hubble tension: (73.04 − 67.68)/√(1.06^2 + 1.04^2) = 3.61σ (abstract claim “∼3.6σ” is correct).
- ΔNeff one‑sided bound (full‑tension): Gaussian‑truncation estimate 0.318; reported 0.31 (consistent within sampling).
- Planck+ACT naive combination: 0.241 ± 0.061° → 3.94σ (text: 3.9σ “upper bound” with caveat; correct).
- wpivot: ap = 0.790 ⇒ zp = 0.27, σwpivot = 0.019, wpivot = −0.952 (all consistent with Table II and footnote).
- CPL H(z=0.5) effect size: ≈ +1.76% (text: ≈ +1.7%; consistent).
- αEM/(4π) × Caγ × Δϕ/fa = 5.81×10−4 × 8 × 1.06 = 4.93×10−3 rad = 0.282° (Eq. 4; consistent).
- ρcrit,0 = 3H0^2 MPl^2: using H0 = 1.444×10−33 eV and MPl = 2.435×10^27 eV gives 3.7×10−11 eV^4 (text: 3.7×10−11 eV^4; correct).
- σβ at fsky=0.32 rerun: 0.046°, |β̂|/σβ ≈ 0.238/0.046 = 5.17 (text: “≈5.2”; consistent).

## Summary recommendation
MAJOR REVISIONS

The core numerical content is largely consistent and appropriately caveated, and the paper’s aim as a technical companion is reasonable. However, before PRD publication the authors must (i) replace all “pending” archival references with stable DOIs/tags; (ii) prevent misinterpretation of the w0wa σ‑distances by relocating or prominently re‑labeling Table II; (iii) provide a quantitative uncertainty on the quoted NaMaster bias “floor”; and (iv) incorporate anharmonic corrections (or clearly restrict the regime) for the Ωa subset accounting. Several additional methodological clarifications and figure updates are requested. With these addressed and some editorial trimming, the paper should meet PRD methodology standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P1B-E5 (Sec. VI, multiple places): Understated “∼25×” misalignment tuning relative to stated priors
- Problem: The paper repeatedly characterizes the spectator-status tuning as “∼25×” based on θi from 0.5 → 0.1 (Ωa ∝ θi^2). But the actual sampling prior used in the ALP MCMC is θi ∈ [0.01, π] (flat in θi, Appendix C), and you also present a flat-in-cosθi rerun. Under either of these “natural” priors, the typical θi is O(1), so the energy-density tuning to reach θi≈0.1 is ≳100× (not 25×). You partly quantify this by reporting the tiny posterior mass for θi ≤ 0.1 under the cosθi prior (0.068%), but the headline “25×” is inconsistent with that prior.
- Required fix: Define “natural” explicitly (flat θi vs flat cosθi) and report the tuning factor consistently for that choice. At minimum, replace “∼25×” with “≳100× under a cosθi prior (∼25× relative to the ad‑hoc θi≈0.5 envelope midpoint)” and quote both posterior sliver fractions (you already give 0.33% flat‑θi and 0.068% flat‑cosθi for θi ≤ 0.1). This materially changes the stated fine‑tuning burden.

MAJOR

P1B-M6 (Sec. IV, Eq. 1 and rotation text): β units are ambiguous in the estimator/rotation
- Problem: The estimator uses sin(4β) and the map rotation applies e^{2iβ}(Q+iU), but the text never states whether β is in radians or degrees inside the trigonometric functions and the exponential. You also describe a “β grid” in degrees elsewhere. This is a reproducibility hazard.
- Required fix: State explicitly that β is in radians in Eq. (1) and in the e^{2iβ} rotation, and that the degree grid is converted to radians inside the code. Add the actual grid range/resolution and confirm that tightening the grid does not shift β̂ at the 10^{-3}° level (see also P1B-m11 below).

P1B-M7 (Sec. IV, “bins above the band limit”): χ² contribution from ℓ > 2Nside is misstated
- Problem: The text says bins above ℓmax = 1024 “carry zero template weight … so the 20‑bin sum is effectively restricted to ℓ ≤ 1024.” In fact, those bins add a β‑independent constant χ² term; they do not vanish from the sum.
- Required fix: Rephrase to “bins above 2Nside contribute a β‑independent constant to χ² (since C^EE_tmpl=0 there) and hence do not affect the β minimizer.” Optionally, drop those bins in the code for clarity and state that doing so leaves β̂ unchanged.

P1B-M8 (Sec. V.B, “Independent re‑run cross‑check”): Nonstandard “effective weight” exceeds raw samples
- Problem: You report 28,245 post‑burn‑in samples but “107,853 effective weight.” An “effective” size larger than the raw MCMC count is nonstandard and confusing (ESS should be ≤ Npost).
- Required fix: Report the conventional integrated‑autocorrelation‑time ESS (per parameter) in addition to raw/post‑burn‑in counts. If “effective weight” is a GetDist‑specific metric, label it as such and add the standard ESS for comparability.

P1B-M9 (Sec. IV, fn. 4): Inconsistent SNR conventions for per‑realization angle recovery
- Problem: You quote “per‑realization angle‑recovery ratio” values 8.1 (fsky=0.85) and 7.2 (0.65), which are inconsistent with βinj/σβ = 0.27/0.029 ≈ 9.3 and 0.27/0.033 ≈ 8.2. It appears you used |β̂|/σβ (0.237/σβ), not βinj/σβ.
- Required fix: State explicitly which convention you use (βinj or |β̂| in the numerator) and use one convention consistently throughout. If both are useful, report both to avoid confusion.

P1B-M10 (Sec. IV, “well below σobs” language): Bias floor vs ACT DR6 uncertainty
- Problem: The text says the 0.040° pipeline bias is “well below the published observational uncertainty σobsβ = 0.094°.” While true for the WMAP+Planck summary, ACT DR6 quotes σ=0.074°, for which 0.040° is ~0.54σ and not “well below.” You do elsewhere caution non‑comparability, but this sentence can mislead.
- Required fix: Qualify the statement to the specific σ used (WMAP+Planck 0.094°), and add that relative to ACT DR6’s 0.074° the 0.040° MC bias is ~0.5σ and remains a pipeline‑validation quantity not directly comparable to sky‑measurement systematics.

MINOR

P1B-m9 (Sec. III, “MB–H0 constant” arithmetic): Small rounding mismatch
- Problem: Recomputing MB − 5 log10 h gives −18.569 (Riess anchor) and −18.415 (chain mean), Δ≈0.154 mag, whereas the text quotes −18.571, −18.415 (Δ=0.156). The difference is tiny but avoidable.
- Required fix: Carry one more significant figure or show the exact calculator values you used so Δ is reproducible to 0.001 mag.

P1B-m10 (Sec. IV, SNRtmpl definition): Make the definition fully explicit
- Problem: SNRtmpl is described verbally without a displayed formula or explicit σb definition in symbols.
- Required fix: Add SNRtmpl^2 = Σ_b [C^th_EB(b)/σ_b]^2 with σ_b defined as the per‑bin standard deviation across the N_MC realizations.

P1B-m11 (Sec. IV, β‑grid details): Explicit grid range and unit conversion
- Problem: You note a 10^{-3}° grid but don’t give the range, nor confirm degree→radian conversion.
- Required fix: State the β grid range, resolution, and unit conversion used in both the χ² scan and the Q/U rotation, and confirm that tightening the grid does not change β̂ at the 10^{-3}° level.

P1B-m12 (Sec. IV, NaMaster purification defaults): Clarify n_iter with purify_b
- Problem: You report purify_b=True “with all other defaults,” but the efficacy of purification depends on n_iter. Readers may not know the NaMaster default (typically 3).
- Required fix: State the actual default n_iter value used and confirm that varying n_iter (e.g., 0, 3, 10) leaves β̂ unchanged within the quoted ±.

P1B-m13 (Sec. IV, mask/footprint): ℓ‑range statement precision
- Problem: “Restricting the fit to bins with ℓ ≤ 1024 changes nothing (0.238°).” To avoid implying those bins were weighted out, clarify they were dropped from the χ² sum and the minimizer was identical within 10^{-3}°.
- Required fix: Minor wording change as above (ties to P1B‑M7 precision).

P1B-m14 (Table IV): Column content clarity
- Problem: The first row mixes “median ≃ 36” (m/H0), “broad” for θi, and Caγ statistics; the presentation is hard to parse and differs from subsequent rows with percentile triplets.
- Required fix: Standardize the reporting per column (median and 16–84% range for all three quantities in every row), or move “broad” remarks to the caption.

NITS

P1B-n4 (Global, radians vs degrees): Standardize β notation
- Comment: Use a consistent convention: by default β is in radians inside equations and code, while all reported values are in degrees. State this once prominently (ties to P1B‑M6), and avoid mixing symbols without unit reminders.

P1B-n5 (Sec. IV, “effectively restricted” phrasing): Tighten language
- Comment: Replace with “contribute a β‑independent constant to χ²” (see P1B‑M7), to avoid implying those bins are excluded.

Reason for new findings
These issues emerged from a second‑pass audit focused on arithmetic recomputation, estimator/unit rigor, and consistency between narrative, equations, and figures. Several items (misalignment‑tuning quantification, β‑unit ambiguity, χ² bin treatment, ESS reporting, SNR conventions) materially improve clarity and reproducibility and were not covered in the initial review.