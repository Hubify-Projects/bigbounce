---
model: gpt-5
paper: p4 — Galaxy Chirality Catalog — 8.47M galaxies, CW/CCW classification
pdf: /Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf
date: 2026-05-01
input_tokens: 28760
output_tokens: 12395
total_tokens: 41155
reviewer: openai (cross-model adversarial)
retry: true (reasoning=medium, max_output=32000)
---
## BLOCKERs
1) Catastrophic inconsistency in “not spiral” counts used to validate TTA stability
- Problem: Section III.D (a. not spiral stability) claims only 53,862 objects are “not spiral” in the single-pass raw head, yet Section IV.A reports 5,152,736 “not spiral” classifications in the catalog. This is a two-orders-of-magnitude mismatch that invalidates the TTA-leakage sanity check and any rates quoted there.
- Evidence: §III.D, subsec. “a. not spiral stability under TTA averaging (R42 R3 BLOCKER B21)” vs. §IV.A (“not spiral: 5,152,736 (60.8%)”).
- Fix: State precisely what subset the 53,862 refers to (if any), and recompute the TTA leakage on the full 8.47M sample (or on the full 5.15M not-spirals). Report the correct N, the exact leakage fractions, and their uncertainties.

2) Broken cross-references and a missing analysis promised in the abstract
- Problem: The abstract claims an “edge-on-enriched stress-test of 2,000 GZ DESI galaxies (Sec. IV B), four of eight tests pass...” but §IV.B is “Global CW Fraction” and contains no such stress test; the analysis is absent. There is also a dangling reference “Section ??” in §III.D.
- Evidence: Abstract line “edge-on-enriched stress-test ... (Sec. IV B)”; §III.D: “production ViT-Small-Small chirality v2 checkpoint (Section ??)”.
- Fix: Add the actual 2,000-object stress-test analysis with full metrics into §IV (and fix the section pointer), or remove the claim from the abstract. Replace “Section ??” with the correct section number.

3) Confidence calibration numbers contradict each other by a wide margin
- Problem: Table II T7 says only 37.9% of predictions have confidence >0.9, but Fig. 6 claims 62.1% of the full 8.47M have confidence >0.99 (which implies >0.9 ≥ 62.1%). These cannot both be true without very explicit dataset scoping, which is not provided.
- Evidence: Table II (T7: “Frac. at > 0.9 conf. 37.9%”), Fig. 6 caption (“62.1% ... confidence > 0.99”).
- Fix: Specify exactly which dataset each number refers to (validation-only vs full catalog vs spirals-only) and recompute so the thresholds and samples are consistent. If T7 is on the held-out validation split, say so and add the full-catalog value for the same threshold.

4) Spiral-count mismatch between Figure 1 and the catalog totals
- Problem: Figure 1’s panel title (in the figure itself) shows “3,201,160 spirals,” but §IV.A and Table V use Nspiral = 3,321,795. A ~120,000-object discrepancy undermines map-derived inferences.
- Evidence: Fig. 1 (embedded title text: “3,201,160 spirals”); §IV.A spiral count; Table V (“All sky 3,321,795”).
- Fix: Regenerate Fig. 1 with the exact Nspiral used in the analysis mask, or add a figure note explaining the mask difference and list the precise masked N. Ensure all sky maps and all summary tables use the same sample.

5) “Most sensitive measurement” and 0.2% minimum-detectable-dipole claim lacks a validated noise model and Neff
- Problem: §VI.C derives 0.2% using an idealized binomial/Poisson model at NSIDE=8 with an ad hoc fsky fudge, while §IV.B explicitly warns that Neff < N due to spatial correlations. No empirical Neff, no injection/recovery test on the real mask/depth pattern, and the derivation uses a different pixelization than the reported analyses (which mostly use NSIDE=64).
- Evidence: §VI.C (Eqs. 5–6 and fsky rounding), §IV.B (“spatial correlations ... reduce Neff ... a rigorous Neff estimate is needed”).
- Fix: Compute Neff from the pixel-to-pixel variance of A or via block bootstrap; and run end-to-end MC injections of a 0.2% dipole on the real mask/depth map to demonstrate ≥3σ recovery with the actual estimator. If not, retract/soften the “0.2% at 3σ” and “most sensitive” claims.

6) Platt calibration is mischaracterized; the table contradicts the text
- Problem: §III.F claims the sigmoid calibration “removes the residual CW excess,” but Table III shows the calibrated catalog still has a 0.4% CW excess (0.504 ± 0.0003).
- Evidence: §III.F, Catalog B description; Table III “B (calibrated) 0.504 ± 0.0003”.
- Fix: Change the text to “reduces” (not “removes”) and document the calibration objective, dataset, and residual offset explicitly. Alternatively, re-fit the calibration so that cw/(cw+ccw)=0.5 on the stated validation set and update Table III.

7) Training/validation circularity undermines sub-percent cosmological claims
- Problem: 67.6% of training labels come from CE-ResNet predictions; the headline 93.7% accuracy is on a CE-ResNet-augmented validation, while the only independent check gives just 58.71% (3-class) and 69.91% (spiral-only) on GZ1. There is no demonstration that CW↔CCW error rates are symmetric to <0.1% across magnitude/size/PSF—yet sub-percent null claims are made.
- Evidence: §II.B (label sources and 67.6% derived from CE-ResNet; independent GZ1 accuracies), §IV.B and §VI.C sensitivity/exclusion claims.
- Fix: Provide bin-by-bin CW fraction flatness tests at the 0.1% level across r magnitude, surface brightness, size, and PSF FWHM (and edge-on proxy) to demonstrate symmetry; or restrict to a high-purity, high-confidence, face-on subsample and re-run the cosmology analyses and sensitivity floor on that set.

## MAJOR
1) Missing first-order systematics regressions (dust, seeing, depth, scan angle, instrument)
- Evidence: No plots/tables regressing cw/(cw+ccw) vs E(B−V), PSF FWHM, sky brightness, airmass, scan/CCD orientation, or instrument/telescope (DECaLS/BASS/MzLS). §VI.E notes spiral fraction tracks depth, but there is no chirality-vs-systematic null test.
- Fix: Add per-pixel or per-object regressions and/or binned null tests of cw fraction versus these systematics, with <0.1% flatness demonstrated in each bin. Include instrument-by-instrument breakdown.

2) p-value reporting inconsistency for the simple-dipole fit
- Evidence: §IV.C(a) states “0.43σ (p = 0.33)”. For a two-sided Gaussian, 0.43σ corresponds to p ≈ 0.67; p=0.33 is one-sided. The paper elsewhere uses two-sided significances.
- Fix: State explicitly whether p-values are one- or two-sided and use a consistent convention throughout. Provide both when helpful.

3) Rotation augmentation description is conceptually wrong; rotation-systematic left untreated
- Evidence: §III.B says “random rotation (0–360°), without chirality-label remapping—the rotation … does not preserve the CW/CCW label under large rotations” (incorrect; chirality is invariant under in-plane rotation). §III.D concedes rotational orientation dependence remains and may source the residual 0.26%.
- Fix: Correct the text: CW/CCW labels are preserved under rotation. Quantify rotation sensitivity by reporting class-stability at 90°/180°/270° specifically for the full catalog and assess its coupling to survey scan orientations. Either add D4 TTA or show that rotation non-equivariance cannot alias into a sky dipole (e.g., via regression vs. scan-angle distributions).

4) Key results are only accessible in external logs, not in the paper/SI
- Evidence: §II.B and §III.D cite “r42 results/*.json” for confusion matrices, counts, and throughput; these are not part of the manuscript or a formal SI.
- Fix: Move essential numerical results (full confusion matrices, matched counts, and any numbers the text relies on) into the paper or Supplementary Material with persistent DOIs.

5) Edge-on contamination claims are contradictory and unquantified
- Evidence: §VI.D first uses DESI axis ratios to conclude 65.7% of b/a<0.3 are given CW/CCW; later in the same section it says axis ratios are “not included in Catalog C” and a cross-match is required. No sample sizes, no b/a-binned cw fractions, and an implausibly tiny global raw→eq not-spiral flip count (3,445 objects) are reported, which conflicts with the 4.03% leakage on 53,862 objects in §III.D(a).
- Fix: Provide a cross-match table (counts and cw fraction with errors) for b/a bins {>0.5, 0.3–0.5, <0.3}, and reconcile the 3,445 vs 53,862 numbers. If you did not cross-match, remove claims that depend on b/a and add the cross-match.

6) Artifact-rejection test may be trivial if evaluated on training negatives
- Evidence: §II.B.3 includes 2,000 synthetic hard negatives in training; §III.E (T3) reports 100% blank→not-spiral without stating that the test set is disjoint from training negatives.
- Fix: Explicitly state that T3 is evaluated on a held-out set and provide N and the exact pass rate with uncertainty.

7) Angular power spectrum noise term uses the wrong N; conclusions about “residual signal power” are not robust
- Evidence: §IV.C(b), footnote 5: Cnoise_1 computed from Ngal that includes not-spiral objects, although the asymmetry field uses only spirals. The authors note sign flips when substituting Nspiral but retain narrative language about “residual power.”
- Fix: Recompute Cnoise_ℓ using per-pixel Nspiral (and proper weighting), propagate through the MASTER deconvolution, and update the text and Fig. 8 bars accordingly.

8) Hemisphere look-elsewhere correction handled with crude Bonferroni/BH; no max-statistic null
- Evidence: §IV.D uses Bonferroni and BH-FDR over ~650 directions. Neighboring hemispheres are highly correlated; the correct correction is the null distribution of the maximum-over-directions statistic on the real mask.
- Fix: Monte Carlo the maximum asymmetry over all tested hemispheres under label shuffling on the actual footprint and report the corrected significance.

9) Quantify depth/asymmetry coupling before/after TTA rather than rely on maps
- Evidence: §VI.A and Fig. 11 qualitatively compare maps but no quantitative correlation between asymmetry Ap and per-pixel spiral density or depth is shown.
- Fix: Report corr(Ap, Nspiral) and corr(Ap, depth/seeing) with uncertainties before and after TTA to substantiate the “systematic eliminated” claim.

## MINOR
- Remove all internal-reviewer and repo shorthand (e.g., “R42,” “Reviewer R1,” “BLOCKER B21,” “Section ??”). Evidence: §III.D, §III.E footnotes; multiple places. Fix: Clean manuscript to PRD standards.
- Typo/wording: Abstract “equivarianta post-processing” → “equivariant post-processing.” Evidence: Abstract. Fix: Correct.
- Consistency: Use CCW uniformly (avoid ACW in §V.B). Fix: Standardize terminology.
- Clarify Platt-scaling parameters: report standard A, B (or “temperature, bias”) with equation used; currently ambiguous. Evidence: §III.F. Fix: Add equation and mapping.
- Justify T2 rotation-stability choice of 60° increments (why not the cardinal 90° set relevant to CCD orientation?), or add that set. Evidence: Table II, T2. Fix: Add justification or additional test.

## Strengths
- Largest spiral-chirality catalog to date with public data, models, and code; strong reproducibility posture overall.
- Clear demonstration that a small classifier bias, coupled with non-uniform survey coverage, can generate an enormous spurious dipole (94.6σ), and that flip-TTA collapses it—an important cautionary result for the field.
- Multiple complementary null tests (simple dipole, pseudo-Cℓ with MASTER, hemisphere scans, confidence stratification), with an honest discussion of residuals and limitations.
- Inclusion of an explicit not-spiral class to reduce contamination, and an attempt at a bias-hardening suite—both steps forward relative to prior work.
