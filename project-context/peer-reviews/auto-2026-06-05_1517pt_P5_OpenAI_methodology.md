# P5 auto-2026-06-05_1517pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7580 chars)
**Wall time**: 282.9s

---

Referee report on: “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals” (P5)

Scope of review
I audited the methodology, statistical procedures, internal arithmetic, dimensional consistency, and the traceability of every load‑bearing scalar in the abstract and conclusions to values and derivations in the body. I recomputed every reported σ-from-half, range, ratio, and several p-values from the tabulated counts.

Findings

ESSENTIAL

P5-E1 (Sec. VI A; Table II; p. 5; Fig. 2 caption, p. 5)
Problem: Inconsistency between stated sample size and class counts. Table II is introduced as “on the 791,635 chirality-relevant matched spirals,” and Fig. 2 caption repeats “n = 791,635.” However, the class counts listed in Table II sum to 812,793 (428 + 6,673 + 408,187 + 397,505), not 791,635. Later (§VIII F, p. 12–13) the manuscript acknowledges an 812,793 “superset,” but Table II and Fig. 2 still label the 791,635 subset.
Required fix: Explicitly state in Table II and Fig. 2 captions which sample is used (791,635 vs 812,793), align the text around Table II with that choice, and ensure all class counts and derived σ values are recomputed for that exact sample. If the 812,793 superset is used, update the text that currently claims 791,635.

P5-E2 (Sec. VII; p. 9)
Problem: Impossible sample size in the Phase 2 sweep. The manuscript states: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152).” A chirality-based σ-from-half statistic requires CW/CCW labels. Nowhere is a chirality‑relevant matched sample larger than 812,793 reported. An n = 3,696,152 class cannot exist within this matched-labeled dataset.
Required fix: Clarify precisely what “n = 3,696,152” refers to. If this is not a chirality-labeled count (e.g., all DESI galaxies in that class), do not compute or quote a σ-from-half for it. Replace with the actual n for chirality-labeled galaxies in that sweep cell, and recompute the statistic. If a different dataset was used, document it and keep statistics strictly within like-for-like labeled samples.

P5-E3 (Sec. VI D.b vs Sec. XI; pp. 7 and 17–18)
Problem: Direct contradiction on bright vs dark target-program split. Section VI D.b reports a strong difference: bright fCW = 0.4970 (σ = −5.25) vs dark fCW = 0.5051 (σ = +1.25), a difference of ≈0.0081 in fraction. Section XI (Systematics and null tests) claims: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO,” which contradicts the earlier 0.0081 difference.
Required fix: Reconcile these sections. State explicitly the sample and cuts used in each, and correct whichever statement is wrong. If Section XI was intended to summarize post–monopole-subtracted residuals or a different subset, say so quantitatively. Provide a single, consistent set of numbers for the bright vs dark split used throughout.

P5-E4 (Sec. VI D.c; p. 7)
Problem: Implausible dark-subsample size within filament class. You report a filament-class “dark” subsample n = 21,203, but earlier in the same subsection the total dark sample across all classes is n = 14,782. A class-specific “dark” cannot exceed the catalog-wide dark count.
Required fix: Correct the filament “dark” n, or, if a different sample definition (e.g., the 812,793 superset) was used for this particular split, make that explicit and provide the corresponding catalog-wide dark count for that exact sample. All bright/dark class-level statistics must be computed on a single, consistently defined sample.

MAJOR

P5-M1 (Sec. V; Eq. (1); p. 4)
Problem: Ambiguous/mistyped σpred formula. You write “σpred = ΔfCW/0.5/√N = 2 · ΔfCW · √N.” As written, ΔfCW/0.5/√N equals 2ΔfCW/√N, not 2ΔfCW√N. The intended relation is σpred = ΔfCW / (0.5/√N) = 2ΔfCW√N.
Required fix: Add parentheses and correct the algebra to remove ambiguity: σpred = ΔfCW / (0.5/√N) = 2ΔfCW√N.

P5-M2 (Sec. VI A; p. 5)
Problem: Miscomputed σpred for the filament class. With ΔfCW = −0.0026 and n = 408,187, σpred = 2·(−0.0026)·√408,187 ≈ −3.33, not −3.16 as quoted. The cluster prediction −3.28 is consistent.
Required fix: Correct the filament σpred value and any downstream narrative (e.g., “within order unity of observation”) that uses −3.16.

P5-M3 (Sec. V A; p. 4; Sec. VI E; p. 8; Sec. VII A; p. 9)
Problem: Monte Carlo precision vs. claims. All empirical look-elsewhere corrections and permutation p-values use NMC = 1,000. Several reported p-values are near commonly used thresholds (e.g., 0.135, 0.413, 0.607), and null max-stat percentiles (e.g., “|σ|null,p99
max = 4.78”). With NMC=1,000, the resolution on p is ~0.001 and the sampling error on 0.01 or 0.05 quantiles is non-negligible; estimates of “p99” are particularly noisy at NMC=1,000.
Required fix: Increase NMC to at least 10,000 for all look-elsewhere and permutation-based max-statistics, recompute the corresponding p-values and quantiles, and update the text and tables. Alternatively, report uncertainty bands for empirical quantiles and p-values and avoid over-precise digits.

P5-M4 (Sec. VIII F; p. 13; Fig. 6 bottom caption p. 14)
Problem: Inconsistent pixel counts for NSIDE=32 and ≥200-spiral cut. The text claims “across the 1,821 valid pixels,” while Fig. 6 bottom caption reports “1,496 valid pixels.” These cannot both be correct for the same NSIDE and cut.
Required fix: Recompute and state a single consistent number of valid pixels. Update either the text or the figure caption accordingly.

P5-M5 (Sec. VII; Table VI caption; p. 8)
Problem: Mis-specified grid parameter. The caption says: “sweep over nine cells Rs ∈ {10, 25, 50} Mpc/h × Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}.” “Ngrid = 256 × λth” is meaningless; earlier text uses Ngrid = 256^3.
Required fix: Correct the caption to “Ngrid = 256^3; λth ∈ {0.0, 0.1, 0.3}.”

P5-M6 (Sec. VI A; p. 5)
Problem: Abstract/body coherence on σ magnitudes. The abstract claims the V-Web void result is “∼2σ on the binomial null,” while Table II shows σ = −0.68 for void with N=428. If the abstract refers to 2σ width for a ≈5 pp counting error, that needs to be clearly stated; presently it reads like a point estimate at ~2σ significance, which is not the case.
Required fix: Clarify in the abstract that “∼2σ” refers to the two-sided 95% binomial width (~±5 pp) at N=428, not to a detected offset. Or remove the “∼2σ” phrasing.

MINOR

P5-n1 (Sec. IV A, step list; p. 3–4)
Problem: Notation “2563” without superscript is ambiguous on first appearance. It appears elsewhere as 256^3.
Required fix: Use 256^3 consistently.

P5-n2 (Sec. VIII A; p. 10)
Problem: Units clarity. The DESIVAST hole radii are in h−1 Mpc; you state “units h−1 Mpc consistent with the DESIVAST hole catalog,” which is fine. For χ(z) you cite Planck 2018, but do not state whether h in the match is 0.6766 or 1; this matters for a point‑in‑sphere test at a few Mpc/h near boundaries.
Required fix: Explicitly state the value of h used in distance conversion and confirm it matches the DESIVAST unit conventions used in the FITS files.

P5-n3 (Sec. VIII B; p. 11)
Problem: KDTree k=20 nearest-neighbour justification. You state the max hole radius is 24 h−1 Mpc and use k=20 on hole centers for the search. While this is likely sufficient, a brief justification (e.g., nearest-neighbour density vs. typical hole separation) should be provided or, better, a deterministic radius query (ball tree) should be used to ensure no misses.
Required fix: Provide a short justification for k=20 or switch to a radius-based query for the point‑in‑sphere test.

P5-n4 (Sec. VIII A; p. 10)
Problem: Over-precise p-value claim. “p<10−1000” is not meaningful; most software will underflow far earlier, and the message is simply “p ≪ 10−10.”
Required fix: Replace with an interpretable bound (e.g., p < 10−50) or simply “p ≈ 0 to machine precision.”

P5-n5 (Sec. V B; p. 5)
Problem: Garden‑of‑forking‑paths discussion is good, but the text repeats “primary”/“secondary” frequently. Smaller, clearer bullets would improve readability.
Required fix: Condense and standardize wording; this is editorial.

P5-n6 (Throughout)
Problem: Typographical and stylistic issues: occasional extra hyphens (e.g., “re-projection,” “per-leg”), “σfrom half” without a space, inconsistent capitalization of class names.
Required fix: Copyedit for consistency.

NIT

P5-i1 (Sec. IV B; Fig. 1; p. 4)
Problem: The pie chart is minimally informative given exact fractions are elsewhere. A stacked bar with exact numbers and uncertainties (if any) would be clearer.
Required fix: Optional redesign.

P5-i2 (Sec. IX B; p. 15)
Problem: “Concurrent-literature” tone reads like a project status note. This is acceptable, but a briefer, more neutral summary would fit PRD style.

Audit of arithmetic and claims

- Table II σ-from-half values recompute correctly from the provided (n, nCW). Range 1.98 pp is correct. The filament σpred with Δf = −0.0026 should be −3.33 (not −3.16).
- Density quintiles: N = 158,327 per bin; |σ|max = 3.94; σpred = 2·0.0026·√158,327 ≈ 2.07; residual 1.87; Bonferroni-5 threshold |σ| ≈ 3.09; consistent.
- DESIVAST void vs non-void (Table VII): σvoid = −1.71; σnon-void = −4.59; both recompute correctly.
- DESIVAST algorithm cross-check (Table VIII): Signs and magnitudes are plausible. Without nCW, recomputation is limited, but σ magnitudes are consistent with the stated fCW differences and sample sizes.
- Tempel cross-validation (Table XI): All σ recompute from listed (n, nCW, fCW).
- HEALPix scans (Table V): With NMC = 1,000, the reported p-values are coarse but plausible; the need to increase NMC is noted above.

Other methodological points

- Pre-registration: The paper candidly declares a post hoc choice of “primary.” That is acceptable provided the DESIVAST path is clearly and exclusively used to anchor the headline claim. The current manuscript does this, but the sample-size inconsistencies (E1–E4) must be resolved.
- Mixing σ from different nulls: The manuscript generally compares “σ-from-half” across bins to the catalog monopole prediction and uses empirical LEE-corrected p-values separately; I did not find an instance where different σ (e.g., monopole-adjusted vs raw) are juxtaposed without context. After fixing the sample-size issues, maintain these distinctions explicitly wherever both appear on the same page/figure.

Length
At 20 pages for a primarily null result, the manuscript is long. After resolving the essential/major issues, consider reducing to ~12–14 pages by:
- Moving the HEALPix-by-pixel visualizations and some diagnostic decompositions (e.g., multiple quartile splits) to an appendix or data repository.
- Consolidating the concurrent-literature section to a concise paragraph with citations.

## Summary recommendation
MAJOR REVISIONS

The paper contains several critical internal inconsistencies (sample size mismatch in key tables/figures; impossible class size in the phase-2 sweep; contradictory statements on the bright vs dark split; an ambiguous equation; inconsistent pixel counts) that must be resolved for PRD standards. The core methodological framework is sound and many numbers check out, but the present manuscript’s internal arithmetic and sample bookkeeping are not yet publication-grade. After correcting these issues, clarifying the MC precision, and tightening presentation, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P5-E5 (Abstract; Phase-2 max-range value)
Problem: Decimal-place mismatch. Abstract states: “the per-cell range … never exceeds 0.22 percentage points (max 0.0022 at Rs = 25, λth = 0.3).” The parenthetical “0.0022” conflicts by a factor of 100 with “0.22 percentage points” and with Table VI (max = 0.220).
Required fix: Correct the parenthetical to 0.22 or clarify units if a different quantity was intended.

P5-E6 (Sec. VIII intro vs Sec. VIII C; DESIVAST void counts)
Problem: Inconsistent DESIVAST void counts across sections. Sec. VIII (intro) says “420 with V2-REVOLVER, and 295 with V2-VIDE,” while Sec. VIII C later quotes “V2-REVOLVER n_catalog_void = 1,992” and “V2-VIDE n_catalog_void = 1,478.” These cannot both describe the same catalog level without clear definitions (e.g., “maximal voids” vs “effective voids” vs “zones”).
Required fix: Define each reported count precisely (maximal voids, interior holes, effective voids, zones) and use consistent terminology. Provide a single reconciled set of numbers for REVOLVER/VIDE that matches the files used in analysis.

P5-E7 (Sec. VII/Table VI vs Sec. VI A/Table II; “range across classes”)
Problem: Canonical-cell inconsistency. Table VI reports the per-cell fCW range across classes for Rs=25, λth=0 as 0.165 pp, but Table II for the same canonical run shows a 1.98 pp range (0.5034 – 0.4836). If Table VI is a monopole-subtracted range, this is not stated; if it is raw fCW, it disagrees with Table II by an order of magnitude.
Required fix: State explicitly whether Table VI’s ranges are computed on raw fCW, on fCW − 0.5, or on fCW − fP5 (monopole-subtracted). Align all text (including the abstract’s 0.22 pp) and recompute/relabeled values so that the canonical cell agrees between Table II and Table VI if they purport to show the same statistic.

MAJOR

P5-M7 (Sec. VI B; logistic-regression specification)
Problem: Mis-specified angular regressors. The z-dependence test uses a logistic model with {z, |sin δ|, cos α, confidence}. Using only cos α (without sin α) and |sin δ| (rather than both sin and cos, or δ itself) can hide RA/Dec dependence due to phase choice. This under-specifies sky-position covariates.
Required fix: Use a rotation-complete basis for angle dependence (e.g., sin α and cos α; sin δ and cos δ, or spherical-harmonic Yℓm up to ℓ=1) and report coefficients/uncertainties. Otherwise, state clearly that the z test marginalizes only over a limited set of angular proxies and quantify any residual sensitivity.

P5-M8 (Abstract; Sec. VI D.b; methods gap)
Problem: Two-sample z-tests are quoted (e.g., “|z| ≈ 3.4σ” in filament bright vs dark), but no test definition or input counts are provided in Sec. V. Reproducibility is not possible from the text alone.
Required fix: Add the two-sample z-test formula to Sec. V, and provide the raw (nbright, nCW,bright) and (ndark, nCW,dark) for each class where a z is reported. If continuity-correction or pooled-variance assumptions are used, state them.

P5-M9 (Sec. VII; grid scale vs smoothing scale)
Problem: Phase-2 cells include Rs = 10 Mpc/h while the density field is sampled on a 256^3 grid with 6,634 Mpc/h box size, i.e., cell size ≈ 25.9 Mpc/h. A Gaussian smoothing scale smaller than the grid spacing is not resolved and renders the Rs=10 results effectively unsmoothed-at-grid-scale, undermining the intended hyperparameter test.
Required fix: Either (a) increase Ngrid to resolve Rs=10 (e.g., 512^3), or (b) drop Rs=10 from the sweep and state that the grid resolution limits the minimum meaningful Rs to ≥ cell size.

P5-M10 (Sec. VII A; RSD-to-eigenvalue mapping and boundary-crossing estimate)
Problem: Dimensional/methodological leap. The boundary-crossing estimate sets a criterion |λ − λth| ≤ σrsd/Rs and posits an “eigenvalue-shift magnitude ∼ 0.04 σλ” without derivation. λ is a dimensionless eigenvalue of the deformation tensor; mapping a spatial displacement ratio σrsd/Rs directly to an eigenvalue perturbation requires a quantitative model (e.g., perturbation of k-space tidal tensor under RSD). The 0.04 factor and “3–5% of cells near thresholds” are undocumented.
Required fix: Provide a derivation or a simulation-based calibration linking σrsd/Rs to Δλ statistics (or remove the quantitative claims). At minimum, specify what σλ denotes and how 0.04 was obtained.

MINOR

P5-n7 (Fig. 3 right caption; sign of σpred)
Problem: Caption states “σpred = −2∆fCW√N,” which, for ∆fCW < 0, flips the sign relative to Eq. (1) and to Table III values (which use σpred = 2∆fCW√N). This is a sign error in the captioned formula.
Required fix: Correct to σpred = 2∆fCW√N (or explicitly define the sign convention) to match the numbers plotted and Eq. (1).

P5-n8 (Sec. VIII C; provide raw counts for Table VIII)
Problem: Table VIII reports fCW and σ but not nCW for void/non-void per algorithm, preventing independent recomputation.
Required fix: Add nCW (or at least nCW,void) for each row so readers can verify σ.

P5-n9 (Sec. X; ASTRA “entropy-weighted” variance)
Problem: The stated sub-class variance “Pi^2/4 under the Bernoulli-0.5 null” is not derived and omits aggregation across galaxies. The correct variance of a weighted sum of Bernoulli-0.5 indicators is (1/4) Σi w_i^2; here w_i = Pi if weights are used. The text could mislead.
Required fix: Clarify the estimator and its variance: Var(Σi Pi Yi) = (1/4) Σi P_i^2 under independence and p=0.5. State whether class totals are normalized by Σi Pi and how uncertainties are propagated to fCW.

P5-n10 (Sec. VI B; “no significant intercept (0.000652)”)
Problem: Reporting a raw coefficient value as “no significant intercept” without an uncertainty or p-value is opaque.
Required fix: Provide standard error and p-value for the intercept and for the z coefficient, or remove the significance wording.

P5-n11 (Sec. IV A, step 1; consistency of SPECTYPE filter)
Problem: Step 1 lists SPECTYPE = GALAXY, but elsewhere the parent DR1 input includes SPECTYPE ∈ {GALAXY, QSO}. This is likely just a shorthand, but it reads inconsistently with Table I.
Required fix: Harmonize the wording (e.g., “SPECTYPE ∈ {GALAXY, QSO} for parent; GALAXY-only for V-Web density construction if that’s what was used”) or confirm QSOs were included in the V-Web field construction.

P5-n12 (Typographical precision)
Problem: Several places use gratuitous precision (e.g., “p = 0.607” from 1,000 shuffles). Given Monte Carlo resolution (see prior M3), 2–3 significant digits are sufficient.
Required fix: Round empirical p-values/quantiles to a precision commensurate with NMC, or provide uncertainty.

NITS

P5-i3 (Units/notation in Sec. IV; Poisson normalization)
Observation: The Poisson equation is written as Φ(k) = −δk/k^2 with k=0 zeroed; constants (4πG a^2 ρ̄) are dropped, which is fine for classification but worth a parenthetical note to avoid unit confusion.
Suggested edit: Add “up to a constant factor irrelevant for eigenvalue signs” to the step list.

P5-i4 (Figure/terminology consistency: “wall” vs “sheet”)
Observation: The manuscript uses “wall” (V-Web) and maps Tempel/T-Web “sheet” to “wall.” A one-line reminder in each cross-comparison figure/caption would help readers not to conflate the labels.
Suggested edit: Add “sheet ≡ wall” in captions where both appear.

Explanation
These are new findings uncovered by a second, line-by-line pass focused on cross-table arithmetic, caption/body coherence, method specification, and dimensional consistency. They do not repeat items already raised in the initial review.