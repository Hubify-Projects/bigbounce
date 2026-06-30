# P1B INT-M2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=b3fe7527 pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4385 chars)
**Wall time**: 353.9s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall assessment
The manuscript presents three methodological verifications: (i) a stock-CAMB ΛCDM+ΔNeff MCMC proxy with carefully documented likelihood stacks and convergence; (ii) a NaMaster pseudo-Cl Monte Carlo validation for uniform-rotation recovery on synthetic polarized CMB skies; (iii) a spectator-ALP consistency check against a published Gaussian summary likelihood for cosmic birefringence. The authors are generally careful about scope, caveats, and separation of significances. Many numerical claims are internally recomputed and consistent when checked. The paper is primarily a methodology and verification companion; it avoids model-preference claims and is careful to label overlap- or prior-dependent results.

Below I list issues found, classified by severity, each with location, problem, and required fix.

ESSENTIAL

P1B-E1 (Appendix A, p.18–20; also Abstract/Conclusions via claims of “reproducibility manifest”)
Problem: Data/code availability relies on mutable GitHub/HuggingFace links; DOIs are “pending,” and the paper references a live commit hash (b22f8cc9) and a version tag (“v1B.0.82”), not an archival DOI or frozen release. PRD requires stable, permanent archival of key artifacts used for published results.
Required fix: Before acceptance, deposit all load-bearing artifacts (frozen MCMC chains used in Tables I–II/IV, NaMaster MC artifacts underlying Fig. 3 and the robustness battery, ALP chains used in Sec. VI/Fig. 4) in a permanent archive (e.g., Zenodo or similar) and provide DOIs in the paper. Create a frozen tagged release of the repository matching the paper and cite its DOI. Keep git SHAs if desired, but DOIs must be primary.

P1B-E2 (Sec. IV, p.10–12; Fig. 3 caption and body text)
Problem: The canonical estimator used for the NaMaster validation is explicitly unweighted in χ^2, and the authors show it induces a ≈12% multiplicative bias (−0.032° at 0.27°, −0.040° at 0.342°), with inverse-variance weighting removing ~80% of the bias (to −0.006°). Yet the paper retains the biased unweighted estimator as “canonical.”
Required fix: For a methods verification, either (a) adopt the inverse-variance-weighted estimator as the canonical baseline and update the reported pipeline-bias floor (repeat the 500-MC injections at β=0, 0.27°, 0.342° with the weighted fit; report biases and SEs), or (b) retain the unweighted estimator only as a legacy comparability check but clearly elevate the weighted estimator as the recommended method, present its full injection-recovery results (including worst-case bias), and move the unweighted results to an appendix. The current choice, while justified by “matching public scripts,” is not methodologically optimal and understates that a near-unbiased alternative is available and demonstrated by the authors.

MAJOR

P1B-M1 (Sec. IV, p.10–11)
Problem: The text states “Restricting the fit to bins with ℓ ≤ 1024 changes nothing (0.238°),” but the manuscript only asserts this in prose. Since the binning formally extends to ℓ=1536 while maps are band-limited at ℓ=1024, an explicit numeric readout should be included to avoid any ambiguity about the potential constant χ^2 offset from noise-only bins.
Required fix: Add the explicit recovered β̂ (mean ± SE) for a rerun that sums only bins with ℓ ≤ 1024 (N=500 MC) to the robustness-battery paragraph or to Fig. 3 caption/supplement. State which configurations (unweighted and weighted) were tested.

P1B-M2 (Sec. V C; Table II, p.12–13)
Problem: Table II prominently lists w0, wa, and wpivot with tight uncertainties even though the authors correctly warn (footnote a, bolded header note) that the DES-SN5YR × Pantheon+ product likelihood double-counts ~20% overlapping SNe and “artificially narrows the posterior,” making these widths not valid for model comparison or σ-distances. A casual reader could still misinterpret these as standard constraints.
Required fix: Add a conspicuous “overlap-uncorrected product likelihood—uncertainties not for significance/model selection” banner to the first column header or move Table II to an appendix. In the main text, immediately adjacent to the first presentation of those numbers, restate in-line that these are exploratory diagnostics only.

P1B-M3 (Sec. V B, p.12)
Problem: The “release-pairing note” for the Planck PR4 high-ℓ + Planck 2018 low-ℓ/lensing mixture is provided for ΔNeff (c15 rerun), but an analogous robustness check is not reported for the w0wa chain (Table II uses planck 2018 lensing.native rather than .clik; the text notes no dedicated swap test).
Required fix: Either perform and report a Planck low-ℓ/lensing pairing swap test for the w0wa chain (quantify shifts in w0, wa, and wpivot) or explicitly move the w0wa numbers to an appendix and further de-emphasize them as exploratory only.

MINOR

P1B-m1 (Sec. III, Table I caption, p.5)
Problem: The naive two-Gaussian combination of S8 values yields σ ≈ 0.0086, while the text reports 0.009. This is rounding-level but should be made precise since S8 tensions are quoted elsewhere to tenths of σ.
Required fix: State the combined σ to three significant figures (0.0086) or explain rounding choice.

P1B-m2 (Sec. III, p.6–7, “MB–H0 joint-posterior offset check”)
Problem: The 0.2σ agreement of MB with Riess+2020 is normalized to the chain σMB=0.049 (or to the combined uncertainty; both give ~0.18–0.20σ), but this could be misread.
Required fix: Add “relative to the combined uncertainty sqrt(σMB^2 + σRiess^2) = 0.056 mag, the offset is 0.18σ” for clarity.

P1B-m3 (Sec. IV, p.9–12)
Problem: The apodization and mask definitions are clear, but ACT-DR6-like footprint differs slightly between canonical and fsky-sweep runs. The text states this but does not quantify the exact fsky for each.
Required fix: Report the exact fsky values used in the fsky-sweep masks (numerical values already implied: 0.85, 0.65), and state the canonical mask’s fsky again (0.32) in the sweep paragraph for easy comparison.

P1B-m4 (Sec. VI, p.14–16)
Problem: The Ωa definition approximates ρa(zosc) ≈ V(ϕi) and applies a (1+zosc)−3 dilution once oscillations begin, with a special-case treatment if zosc ≤ 0. This is standard, but a short sentence clarifying the treatment near the transition (e.g., smooth interpolation or validation against the EOM) would aid reproducibility.
Required fix: Add one sentence noting that Eq. (9) was validated against direct EOM evolution for representative samples (cite the artifact listed) and that near-transition cases were handled by [brief rule], with negligible impact on the Ωa < 0.01 vs 0.1 classification.

P1B-m5 (Appendix A, p.18–20)
Problem: The paper includes process/internal-version language (e.g., “in-tex v1B.0.82 stamp,” commit SHA b22f8cc9, “Column-permutation warning,” “KNOWN_GAPS.md”) in the main text.
Required fix: Keep the commit/tag information and any artifact warnings, but move detailed process notes (e.g., column-permutation bug narrative) to a short “Code Notes” subsection or a brief footnote, and ensure the main text cites stable DOIs (see P1B-E1).

P1B-m6 (References, p.22)
Problem: Several references are arXiv-only (e.g., [4], arXiv:2509.13654) or indicate future-year arXiv identifiers. That is acceptable, but ensure accurate bibliographic format at proof stage and that arXiv identifiers are correct.
Required fix: Verify arXiv identifiers and metadata at proof stage; include journal info if available.

NITS

P1B-n1 (Typos/notation, several pages)
- Maintain uniform use of degree symbol “°” vs “deg” in text and figure axes; currently consistent in figures, mostly consistent in text.
- Ensure consistent capitalization of “lensed-ΛCDM” and uniform “Cℓ” typesetting.

P1B-n2 (Length; entire paper, 22 pages)
The length is acceptable for PRD Methods. If space is needed, moving Table II and some robustness details to an appendix would be a natural trim without loss to the main thrust.

Arithmetic/consistency spot-checks (all OK unless noted)
- ΔNeff posteriors and one-sided 95% limits are consistent with quoted σ values.
- H0 tension vs SH0ES: (73.04−67.68)/sqrt(1.06^2+1.04^2)=3.62σ (matches “~3.6σ”).
- S8 two-Gaussian tension: (0.827−0.776)/sqrt(0.010^2+0.017^2)=2.58σ (reported 2.6σ).
- wpivot construction: ap=0.790, zp≈0.27; wpivot=−0.952±0.019 (recomputed).
- CPL H(z=0.5) fractional shift ≈ +1.7% (recomputed given the chain means).
- NaMaster MC bias magnitudes and SEs: SE=0.046/√500=0.0021°; worst-case bias 0.040°±0.002° checks out.
- Inverse-variance combination of Planck+ACT β: 0.241°±0.061° → 3.9σ (recomputed).
- ALP birefringence normalization: β=(αEM/4π) Caγ Δϕ/fa = 0.28° for Caγ=8, Δϕ/fa=1.06 (recomputed).
- ρcrit,0 ≈ 3.7×10−11 eV^4 (recomputed).
- SN MB–H0 degeneracy constant and 0.156 mag offset (recomputed).
All above are internally consistent.

## Summary recommendation
MINOR REVISIONS

The manuscript is careful, numerically consistent, and methodologically scoped. The two required changes before acceptance are: (1) provide permanent DOIs for all load-bearing artifacts and a frozen software release; (2) resolve the estimator issue in Sec. IV by either elevating the inverse-variance-weighted estimator to canonical status with full injection-recovery numbers or, if retaining the unweighted estimator for legacy comparability, demote it clearly and present the weighted results as the recommended baseline. Additional minor clarifications (w0wa table labeling, explicit ℓ ≤ 1024 rerun numbers, small presentation/documentation edits) should also be addressed. With these changes, the paper will meet PRD’s methodological rigor standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

ESSENTIAL
(no new essential issues identified beyond P1B-E1 and P1B-E2 in the initial report)

MAJOR

P1B-M4 (Fig. 2; Sec. IV text around Fig. 2)
Problem: Axis/quantity mismatch in the ΔNeff plot. Panel (a) is described in the caption and body as “ΔNeff marginal posterior,” with a vertical marker at the Standard-Model value ΔNeff = 0. However, the panel’s x-axis label reads “Neff,” not “ΔNeff.” If the axis is Neff, the SM marker should be Neff = 3.046, not 0. This can confuse readers about what is actually plotted.
Required fix: Relabel the x-axis to “ΔNeff” (preferred), or, if the plotted variable is Neff, move the SM marker to 3.046 and consistently refer to Neff (not ΔNeff) in the caption/body text. Make the same correction for any other instances where ΔNeff vs Neff labeling could be ambiguous.

MINOR

P1B-m7 (Sec. V C; Table II discussion, “CPL H(z = 0.5) differs … by ≈ +1.7%”)
Problem: Recomputing with the quoted chain means (w0 = −0.812, wa = −0.667, Ωm = 0.314) gives a ≈ +2.1% increase in H(z = 0.5) relative to ΛCDM at fixed Ωm and H0, not 1.7%. Specifically, ρDE(a)/ρDE,0 = a−3(1+w0+wa) exp[3 wa (a−1)] at a = 2/3 yields ≈ 1.11; E^2(z=0.5) shifts by ≈ +4.3%, implying ΔH/H ≈ +2.1%.
Required fix: Recompute and correct the quoted percentage (or show the exact inputs/rounding used to obtain 1.7%). If radiation or slightly different rounded parameters were included, state that explicitly.

P1B-m8 (Sec. IV, Eq. (1) and surrounding text)
Problem: Two equivalent forms for the EB template are used interchangeably (“sin(2β) cos(2β) CEE” vs “½ sin(4β) CEE”). They are mathematically identical, but the narrative oscillates between them, which can be confusing when readers trace the estimator.
Required fix: Pick one form and keep it throughout (e.g., ½ sin(4β) CEE), noting once that it equals sin(2β) cos(2β) CEE in the small-angle expansion.

P1B-m9 (Sec. IV, binning/ℓ-range statements)
Problem: Early in Sec. IV the manuscript says “Only this single binning/ℓ-range configuration is exercised; an ℓ-range robustness sweep is not part of the present MC suite,” but later the robustness battery states “Restricting the fit to bins with ℓ ≤ 1024 changes nothing (0.238°).” This reads as a contradiction about whether an ℓ-range check was done.
Required fix: Harmonize the language: explicitly say that a targeted ℓ ≤ 1024 check was performed as part of the robustness battery (not a full sweep), and give the numeric mean ± SE (for both unweighted and weighted fits, if available).

P1B-m10 (Sec. IV, pixel window handling)
Problem: The text argues no pixel-window mismatch enters because the template is evaluated at Nside = 512 “so the pixel-window smoothing cancels.” This is likely correct, but it would help to state explicitly that the template includes the same HEALPix pixel window Wℓ (squared) as present in the decoupled spectra.
Required fix: Add one sentence confirming that the template bandpowers include the Nside = 512 HEALPix pixel window to match the decoupled spectra (or clarify exactly how the cancellation is ensured).

P1B-m11 (Fig. 3b; Sec. IV text)
Problem: The caption/body say the canonical fsky = 0.32 point is “plotted with the mean only” because σβ was not recorded, but Fig. 3b spans 0.3–0.9 in fsky and may visually suggest error bars on all points. This could be misread.
Required fix: In the caption, explicitly note whether the fsky = 0.32 point is shown in panel (b) and, if so, that it has no error bar (mean-only marker). Alternatively, add an open symbol for mean-only points and explain in the legend.

NITS

P1B-n3 (Terminology; Sec. IV)
- When comparing “template-fit SNR” (SNRtmpl) to “per-realization β/σβ,” the text correctly says they are different quantities. Consider adding a brief parenthetical reminding readers that SNRtmpl is a matched-filter significance of the injected template across bandpowers, not the sampling distribution significance of β̂, to prevent any possible conflation.

Explanation
These are new issues found on a fresh pass and do not duplicate items in the initial report. Most are presentation/clarity corrections (axis labeling, small arithmetic discrepancy, method-description harmonization) that can be addressed with light edits. The earlier essential items (archival DOIs and estimator baseline choice) remain the primary gatekeepers for acceptance.