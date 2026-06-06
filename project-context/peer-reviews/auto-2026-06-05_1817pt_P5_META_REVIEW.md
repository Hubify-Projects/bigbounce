# P5 auto-2026-06-05_1817pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 463.3s

---

META-REVIEW (focus: blind spots none of the 5 referees flagged)

P5-META-E1
- Severity: ESSENTIAL
- Location: Sec. VII (Phase 2 sensitivity sweep), pp. 8–10; Sec. IV.A step 4, p. 3–4
- Why missed: Reviewers critiqued statistics and notation but did not examine numerical resolution vs smoothing scale.
- Problem (quote): “Cloud-in-Cell deposit onto a 2563 comoving grid (full DR1 bounding box 6,634 Mpc/h at 2563 → cell 25.9 Mpc/h). … Phase 2 sweep over {Rs, λth} ∈ {10, 25, 50} Mpc/h × {0.0, 0.1, 0.3}.” The Rs = 10 Mpc/h runs are grossly under-resolved on a grid with 25.9 Mpc/h cells (kernel FWHM well below a single voxel). Any V-Web eigenvalue classification at Rs < cell size is not physically resolved and can be dominated by pixelization noise; yet these cells are treated on equal footing in the sweep and cited in the text (e.g., the “largest single-cell |σ|” example).
- Required fix: Either (i) re-run the Rs = 10 Mpc/h cells on a finer grid (e.g., ≥5123 so that cell size ≲13 Mpc/h) and show stability, or (ii) drop the Rs = 10 Mpc/h cells from the sweep and revise the Phase 2 claims accordingly. Explicitly state the resolution criterion (e.g., Rs ≥ ~1.5× cell size) used to accept sweep cells.

P5-META-E2
- Severity: ESSENTIAL
- Location: Sec. VI.B (Redshift dependence), p. 6
- Why missed: Others checked the existence of the regression but not the basis functions.
- Problem (quote): “A logistic regression of the CW indicator on {z, |sin δ|, cos α, confidence} …” This basis cannot represent a general dipole or low-order spherical pattern: only cos α (no sin α term) fixes an arbitrary phase, and |sin δ| (absolute value) removes north–south sign information. Consequently, the regression is structurally blind to many anisotropies and could return a false null.
- Required fix: Refit using a complete dipole basis (e.g., spherical harmonics Y1m: {sin δ, cos δ cos α, cos δ sin α}) and, ideally, augment with Y2m terms to test robustness. Report coefficients, uncertainties, and a nested-model comparison. If the test is intended only as a redshift trend check, remove RA/Dec from the model and state so explicitly.

P5-META-E3
- Severity: ESSENTIAL
- Location: Sec. VI.C (Projected density dependence), p. 6–7; Fig. 3
- Why missed: Prior reviews checked arithmetic but not the construct validity of the density proxy.
- Problem (quote): “The angular separation to the k = 5 NN spiral on the sphere serves as a projected-density proxy.” With the sample spanning 0.01 ≤ z ≤ 3.83, a 2D angular kNN is strongly confounded with redshift (higher-z galaxies have denser projections for the same 3D density). No control for z (or distance weighting) is applied when forming quintiles, so the “density” bins are in part redshift bins, undermining the interpretation as an environment test.
- Required fix: Repeat the analysis in narrow redshift slices (or with a 3D comoving-kNN using spectroscopic z), and/or regress fCW on both projected density and z jointly. Alternatively, show that within narrow-z slices the quintile results remain monopole-consistent.

P5-META-M1
- Severity: MAJOR
- Location: Sec. VI.D(c) (Filament class tracer-program split), p. 7
- Why missed: Other reviews flagged sample-size mismatches elsewhere but not this specific inconsistency.
- Problem (quote): “filament bright (n = 416,701) … filament dark (n = 21,203).” These two counts sum to 437,904, exceeding the filament total n = 408,187 reported in Table II for the headline sample. The section does not state that a different superset (812,793) is being used here, creating an internal inconsistency in counts at the point of interpretation.
- Required fix: State explicitly at first use that this subsection uses the env-labeled superset (give exact N per class and per program), not the 791,635 headline subset. Provide a reconciliation table mapping each decomposition to its parent sample.

P5-META-M2
- Severity: MAJOR
- Location: Sec. VI.E (HEALPix per-pixel scans), p. 8; Table V; Fig. 4 caption
- Why missed: Others checked per-NSIDE p-values, but not multi-scale correction across NSIDEs.
- Problem (quote): “HEALPix per-pixel CW-deviation scans at NSIDE ∈ {16, 32, 64}… p = 0.61/0.135/0.413.” Running three independent NSIDEs is itself a multiple-comparison scan. Family-wise error is not controlled across NSIDE choices; only within each NSIDE. This weakens the claim “none reach 3σ after look-elsewhere correction” at the map scale.
- Required fix: Either pre-register a single NSIDE or apply a second-level multiplicity correction across the three NSIDE scans (e.g., Bonferroni ×3 or an empirical max-over-NSIDE permutation). Report the corrected p-values.

P5-META-M3
- Severity: MAJOR
- Location: Abstract p. 1; Sec. VIII.C–D, pp. 11–12
- Why missed: Reviewers noted catalog-native checks later, but not the abstract-level conflation.
- Problem (quote): “three-algorithm DESIVAST robustness (VoidFinder + V2-REVOLVER + V2-VIDE) returns |ΔfCW| < 0.002 at all three independent void definitions…” In the body, V2-REVOLVER/VIDE results are obtained twice: (i) via “effective-radius spheres” (an approximation to watershed cells), and (ii) via catalog-native GALZONE membership. The abstract does not disclose that the V2 tests summarized there are based on the spherical approximation for V2 (not the native zone membership), which is a nontrivial methodological change.
- Required fix: Amend the abstract and main text to clearly separate “sphere-approximation” results from “catalog-native membership” results for V2, and make the latter the primary statistic for V2 (the abstract should cite the catalog-native numbers or explicitly label the approximation).

P5-META-M4
- Severity: MAJOR
- Location: Sec. III.C–D (Cross-match method and sensitivity), p. 3–4; XI (Systematics), p. 17
- Why missed: Others questioned the median separation but not stability of environment results to match radius.
- Problem (quote): “Sensitivity to acceptance radius is mild: {0.5, 1.0, 2.0, 3.0, 5.0}′′ produces {2.34, 2.35, 2.37, 2.39, 2.44}×106 matched-primary rows, a ≤ 4% band.” The paper never shows that the chirality-by-environment results (e.g., Table II) are numerically stable under these match radii, only that matched-primary counts shift ≤4%. Given known small but nonzero rates of mis-association at larger radii, fCW by class could drift without visible effect on total counts.
- Required fix: Provide per-environment fCW and σfrom half at 0.5", 1", and 2" on the 791,635 sample (or as close as possible under each radius), or demonstrate that differences are within the quoted “0.2 pp” systematics floor.

P5-META-M5
- Severity: MAJOR
- Location: Sec. VI.A (Headline V-Web table), p. 5–6; Sec. XIII (Limitations), p. 18
- Why missed: Others flagged selection-function issues for V-Web globally, but not this specific conditioning.
- Problem: The title and early headline messaging emphasize a four-class environment test, yet the only class that is underpowered (void) is acknowledged to be dominated by “survey-edge artifacts” at low z and n = 428. The paper leans on the DESIVAST void re-projection to fix this, but the main V-Web class table (Table II) is still used rhetorically in multiple places to support claims about “all four classes” bracketing the monopole. This commingles an underpowered, contaminated class with better-sampled ones.
- Required fix: Add a clear disclaimer directly under Table II stating that the void row is not used for any inference due to n and survey-edge contamination, and that all void-specific statements come from the DESIVAST analysis.

P5-META-m1
- Severity: MINOR
- Location: Sec. VIII.B (DESIVAST-anchored classifier), p. 11
- Why missed: Others focused on k=20’s sufficiency; not on unit cosmology.
- Problem (quote): “Converting each spiral to flat-ΛCDM comoving Cartesian coordinates (H0 = 67.66, Ωm = 0.315, units h−1 Mpc consistent with the DESIVAST hole catalog)…” DESIVAST’s published cosmology should be explicitly cited, and any mismatch in h or Ωm quantified. A small mismatch changes distances and could move marginal cases across hole boundaries.
- Required fix: State the exact DESIVAST fiducial cosmology used to define void centers/radii and confirm it matches the one used for spiral positions. If not identical, quantify the induced boundary uncertainty (e.g., Δχ/RS) and argue it is subdominant.

P5-META-m2
- Severity: MINOR
- Location: Sec. V.A (Bonferroni), p. 4; Fig. 3 caption
- Why missed: Others corrected formula semantics but not visualization.
- Problem: While Bonferroni thresholds are quoted, there is no depiction of the empirical max-stat null envelope in Fig. 3 right panel; only the point predictions from the monopole are shown. Given correlations across quintiles, a shaded MC envelope would prevent over-interpretation.
- Required fix: Add a shaded 95% band from the label-shuffle max-stat MC for |σ| across quintiles, or include it as supplemental, and reference it in the caption.

P5-META-m3
- Severity: MINOR
- Location: Sec. VIII.E (Maximal-void stratification), p. 12; Table IX
- Why missed: Others asked for a footprint overlay but not the binning asymmetry.
- Problem: The “0 maximal voids per pixel” bin (NSIDE=16) contains ~56% of the z ≤ 0.24 sample (378,511/678,945), while the 1–2 and 3–5 bins are an order of magnitude smaller. The text interprets σ differences largely as mask geometry effects, but the extreme imbalance alone makes the σ comparison hard to interpret as “per-void-density.” This deserves explicit caution.
- Required fix: Add a sentence noting the strong class-imbalance across bins and that this stratification is primarily a mask/coverage diagnostic rather than a quantitative void-density trend test.

P5-META-N1
- Severity: NIT
- Location: Title and Abstract
- Why missed: Others focused on sign/precision errors, not phrasing.
- Problem: Title: “V-Web Cross-Check Across 791,635 DR1 Matched Spirals” could be read as if all analyses uniformly used that exact N, while parts of the paper (e.g., χ2 contingency, monopole baseline) use a slightly larger env-labeled superset (812,793). This can confuse readers.
- Required fix: Consider “V-Web cross-check on ~0.79M spectro-matched spirals” or add a brief footnote early in the text clarifying the two closely related Ns and where each is used.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews (the five prior plus this meta-review), there are multiple essential and major blockers: resolution invalidation of part of the Phase 2 sweep (Rs = 10 on a 2563 grid), mis-specified anisotropy regression (cos α and |sin δ| only), confounding in the projected-density analysis, lack of multi-scale LEE correction across NSIDEs, an internal sample-size inconsistency at the point of interpretation, and abstract-level opacity about sphere approximations for V2 voids. My assessment is that, once these are addressed alongside the already extensive list from the other referees (propagation of Paper IV uncertainty, sigma-definition hygiene, selection-function correction for V-Web, HEALPix pixel accounting, repository/DOI, etc.), the paper can likely survive external peer review; however, the current blocker count is high (≈10–15 substantive items), and I estimate only moderate confidence of acceptance without a careful, methodical revision that tightens methodology, clarifies sampling, and corrects statistical framing.