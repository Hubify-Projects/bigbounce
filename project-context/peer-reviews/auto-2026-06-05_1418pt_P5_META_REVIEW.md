# P5 auto-2026-06-05_1418pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 373.1s

---

META-REFEREE REPORT — New issues not caught by any of the 5 prior reviewers

P5-META-E1 — Missing selection-function correction in the 3D density field (ESSENTIAL)
- Where: §IV A.5–A.7 (p. 3–4), “Build mask… Convert counts to overdensity δ = ρ/ρ̄ − 1… Gaussian-smooth δ…”
- Why others missed it: Prior reviews focused on sample arithmetic and σ accounting but did not audit how the 3D field handles DESI’s highly non-uniform angular/radial selection.
- Problem: The pipeline deposits raw galaxy counts into a 256^3 grid, computes a single global mean density “ρ̄cell = 4.64 galaxies/cell” inside the dilated mask, and defines δ = ρ/ρ̄ − 1. There is no correction for the DESI spectroscopic selection function (radial n(z) and angular completeness), no use of a random catalog, and no FKP/weighting. Over 0.01 ≤ z ≤ 2, the mean number density varies strongly; with a single ρ̄ the “overdensity” δ is biased negative at high z and positive at low z, and the tidal eigenvalue classification becomes a proxy for n(z) and footprint geometry rather than LSS. This undermines every V-Web environment assignment and any within-class density stratification derived from this field.
- Required fix: Rebuild the density field using a random/catalog-based selection-function correction: δ(x) = [n(x) − α n_rand(x)]/[α n_rand(x)], with angular completeness weights and radial n(z) built from the DESI randoms; apply standard FKP weighting if used. Demonstrate that V-Web class fractions and per-galaxy labels are stable with/without this correction. If randoms are not available for the exact parent selection, restrict to a volume-limited subsample (as DESIVAST does) and state the completeness model explicitly.

P5-META-E2 — FFT/Poisson on a masked, non-periodic survey volume without window treatment (ESSENTIAL)
- Where: §IV A.4–A.10 (p. 3–4): CIC deposit in a thin spherical-shell footprint; FFT smoothing; k-space Poisson solve “with k=0 mode zeroed.”
- Why others missed it: Reviewers noted “survey-shell systematics” qualitatively but did not examine the numerical implication of using FFTs on a highly non-periodic, masked geometry.
- Problem: The FFT-based smoothing and Poisson solve implicitly assume periodic boundary conditions. Here, most of the cube is empty (in-mask only 18.8% after a dilation), and out-of-mask cells are effectively zero-filled. Convolution with the survey window and wrap-around in Fourier space create ringing and leakage that bias the tidal tensor near boundaries and across large scales; no window deconvolution, padding/inpainting, or constrained realization is applied. Simply dilating the mask before selecting “in-footprint” cells does not cure spectral leakage induced by the hard mask in the FFT pipeline.
- Required fix: Adopt a window-aware approach: either (i) embed the footprint with sufficient zero-padding and demonstrate that wrap-around leakage is negligible (quantify via injection tests), and/or (ii) solve Poisson in real space on the masked domain with appropriate boundary conditions, or (iii) deconvolve the mask/window in Fourier space using a random catalog to estimate the window power. Provide quantitative tests showing stability of eigenvalue spectra and class labels to the chosen window treatment.

P5-META-M1 — Smoothing below grid resolution in Phase-2 sweep (MAJOR)
- Where: §IV A.4 (cell = 25.9 Mpc/h), §VII/Table VI (p. 8–10): sweep includes Rs = 10 Mpc/h.
- Why others missed it: Phase-2 robustness was criticized conceptually, but not for resolution feasibility.
- Problem: The grid voxel is 25.9 Mpc/h. A Gaussian smoothing with Rs = 10 Mpc/h is sub-voxel and cannot be meaningfully represented on this grid; in practice it reduces to a near-identity filter dominated by voxel-scale aliasing. Claims of robustness at Rs = 10 on a 256^3 grid are therefore not physically informative.
- Required fix: Either (a) increase Ngrid (≥ 512^3) so that Rs = 10 Mpc/h is ≥ 1–2 voxels, or (b) drop the Rs = 10 cells from Phase-2 and limit the sweep to Rs values ≥ voxel size. Recompute Table VI and any related conclusions accordingly.

P5-META-M2 — Incomplete and internally inconsistent angular basis in the “redshift dependence” logistic regression (MAJOR)
- Where: §VI B (p. 6): “logistic regression of the CW indicator on {z, |sin δ|, cos α, confidence}…”
- Why others missed it: Prior comments questioned documentation but not the regressors themselves.
- Problem: The angular terms {cos α, |sin δ|} do not span the ℓ = 1 spherical-harmonic basis; they also asymmetrically treat declination (absolute value) and omit sin α. This can leave residual dipole-like systematics undetected and mixes notation (δ here is declination, while δ elsewhere is overdensity). The regression cannot cleanly control for sky-position effects as claimed.
- Required fix: Use a complete ℓ = 1 basis for sky-position controls, e.g. {cos α cos δ, sin α cos δ, sin δ}, plus “confidence.” Report coefficients with standard errors and p-values. Also disambiguate symbols: use Dec for declination and reserve δ for overdensity.

P5-META-M3 — Invalid “range vs counting-noise floor” argument in Phase-2 (MAJOR)
- Where: §VII A (p. 9–10): “the per-cell range… is below the wall- and void-class counting-statistics floors… so no (Rs, λth) cell shows an inter-class range that exceeds the dominant per-class measurement uncertainty.”
- Why others missed it: Others noted that Phase-2 does not probe the right residual, but not this specific statistical fallacy.
- Problem: Comparing an inter-class range (a between-class statistic) to the maximum of per-class SEs (within-class uncertainty) is not a valid significance test. Even if the range is below the largest single-class SE, the between-class variance could still be inconsistent with the null once the joint covariance is considered.
- Required fix: Replace the “range < SE” heuristic with: (i) an ANOVA-style test (or permutation) of between-class variance vs within-class variance per cell, or (ii) pairwise two-sample tests with multiplicity control across the four classes, and (iii) an explicit max-statistic permutation (labels shuffled) on the between-class range. Report per-cell p-values.

P5-META-M4 — Shot-noise treatment absent in the tidal-field construction (MAJOR)
- Where: §IV A.6–A.10 (p. 3–4).
- Why others missed it: Focus remained on mask/systematics; the impact of discrete sampling was not discussed.
- Problem: The power spectrum of a CIC-deposited discrete field includes a Poisson shot-noise term. The text proceeds to smooth δ and solve for Φ(k) without subtracting shot noise or demonstrating that Gaussian smoothing sufficiently suppresses it. The resulting tidal tensor will be contaminated by grid-scale noise, especially at Rs near voxel size, which affects eigenvalue distributions and class assignments.
- Required fix: Quantify and subtract shot noise (Pshot ≈ 1/ n̄, with the CIC window correction) before Poisson; or demonstrate via simulations that chosen Rs values render shot-noise contributions negligible for eigenvalues/classification. Provide eigenvalue histograms with/without shot-noise subtraction.

P5-META-M5 — Primary DESIVAST void-membership test uses non-maximal “hole spheres” as ground truth (MAJOR)
- Where: §VIII B (p. 11): “point-in-sphere test against 101,863 DESIVAST VoidFinder hole spheres,” headline nvoid = 56,981 used throughout (title/abstract).
- Why others missed it: Reviewers noted catalog-native GALZONE later, but not that the headline 56,981 is based on an approximate sphere union rather than catalog-native membership.
- Problem: The VoidFinder “hole sphere” set contains many overlapping spheres per void; classifying “void galaxy = inside any hole” double-counts overlapping volumes and extends void interiors toward walls. DESIVAST ships catalog-native per-galaxy zone/void assignments (GALZONE/ZONEVOID); those return materially different counts (e.g., V2-REVOLVER catalog-native nvoid = 86,276 vs 102,911 with spheres). Using the sphere-union as the primary membership overstates both coverage and purity.
- Required fix: Make the catalog-native GALZONE/VOID0 membership the primary DESIVAST void definition throughout (title/abstract), with the sphere-union only as a sensitivity cross-check. Recompute the headline ΔfCW and σ with the catalog-native membership.

P5-META-M6 — Unweighted pixel-level correlation ignores heteroskedasticity (MAJOR)
- Where: §VIII F (p. 12–13), Fig. 6: Pearson r between per-pixel “maximal-void density” and σ from half.
- Why others missed it: Others accepted the near-zero r at face value and did not examine estimator optimality.
- Problem: Pixel counts vary widely; σpix has different standard errors per pixel. An unweighted Pearson on σpix vs. void-count treats noisy, low-N pixels on par with well-measured pixels, diluting power and potentially biasing the result.
- Required fix: Use a weighted correlation/regression with weights proportional to pixel N (or 1/Var[σpix]) and/or a permutation test preserving per-pixel occupancy. Report both weighted and unweighted results, and confirm robustness.

P5-META-m1 — Ambiguous and inconsistent terminology for samples (“matched-spiral,” “matched primary,” “chirality-relevant”) (MINOR)
- Where: §III D/Table I (p. 3), §VI B (p. 6), §VIII B/Table VII (p. 11–12), Conclusions (p. 18).
- Why others missed it: Reviewers flagged a specific 812,793 vs 791,635 misattribution but not the pervasive terminological ambiguity causing it.
- Problem: “Matched primary,” “matched-spiral,” and “chirality-relevant” are used interchangeably in places; e.g., §VIII B: “Restricting the matched-spiral catalog to z ≤ 0.24 leaves nlz = 678,945 spirals…” without re-stating that “matched-spiral” here means CW/CCW-only. Elsewhere “matched primary” (2,232,212) includes NS. This inconsistency makes it hard to trace which N underlies which σ or fCW.
- Required fix: Define the three sets once (matched primary; chirality-relevant; env-labeled subset/superset), assign fixed symbols (e.g., N_all, N_chi, N_env), and use them consistently in text, tables, and captions.

P5-META-m2 — Symbol overloading for δ (Declination vs overdensity) (MINOR)
- Where: §IV (δ as overdensity), §VI B (|sin δ| as declination), passim.
- Why others missed it: Focus on larger issues; the symbol clash is easy to overlook.
- Problem: δ denotes both the overdensity field and declination, which are used in adjacent sections. This can confuse derivations (especially when “smoothed δ” is followed by “|sin δ|” in a regression).
- Required fix: Use “Dec” (declination) in regressions and reserve δ for overdensity throughout.

P5-META-m3 — Lack of a formal two-sample test for DESIVAST void vs non-void (MINOR)
- Where: §VIII B/Table VII (p. 12): “The two classes return fCW values differing by only 0.0007… statistically indistinguishable.”
- Why others missed it: Reviewers accepted the narrative; no z-test is shown.
- Problem: The statement is correct by eye, but no two-sample difference-in-proportions test (with pooled SE) is reported to quantify “statistically indistinguishable.”
- Required fix: Report the two-sample z-test (or exact test) for fvoid − fnonvoid with its p-value; this will be small (non-significant) but should be shown for completeness.

Meta-review recommendation
REJECT

Given the union of issues across all six reviews, there are multiple essential blockers:
- foundational dependence on an unpublished chirality catalog and its monopole (others),
- irreconcilable internal arithmetic/program-split contradictions (others),
- an impossible sample size in Phase-2 (others),
- and, newly identified here, fundamental methodological flaws in the construction of the V-Web density/tidal field (no selection-function correction; FFT/window leakage) and an invalid smoothing scale relative to grid resolution.

Even if the arithmetic inconsistencies were fixed, the V-Web classifier as implemented cannot be trusted without rebuilding the density field with proper randoms/selection-function modeling and a window-aware Poisson/smoothing pipeline. My confidence that the paper, as presently designed, would survive external cosmology-methods peer review is low. A substantially redesigned and shortened manuscript—anchored on DESIVAST catalog-native membership and an independently validated environment classifier built with proper selection-function treatment—could be reconsidered, but that is closer to a new submission than a revision.