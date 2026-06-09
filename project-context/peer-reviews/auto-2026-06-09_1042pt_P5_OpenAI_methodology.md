# P5 auto-2026-06-09_1042pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8381 chars)
**Wall time**: 342.9s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …”

Scope of this review
- Focus: statistical and methodological rigor; internal arithmetic consistency; derivation chains; correct handling of nulls and multiple testing; clarity and correctness of reported numbers in Abstract, tables, figures, and Conclusions.

Overall assessment
- The paper presents a broad null result: no detectable dependence of spiral chirality on large-scale environment in DESI DR1, with a primary DESIVAST-anchored void/non-void comparison and several secondary checks (V-Web classifier sweeps, Tempel FoF mapping, ASTRA EDR overlap).
- There are several strong aspects (large samples, multiple independent environment classifiers, and transparency about pre-registration). However, I found multiple essential methodological and arithmetic issues that must be fixed before the paper can be considered at PRD standards.

Findings

ESSENTIAL

P5-E1 (Section V, p. 4): Algebraic error in Eq. (1)
- Problem: The equation reads “σpred = ∆fCW/0.5/√N = 2 · ∆fCW · √N”. The left-hand side as written is (∆fCW)/(0.5√N) = 2∆fCW/√N, which is not equal to 2∆fCW√N.
- Required fix: Correct Eq. (1) to the intended form consistent with the definition σfrom half = 2(fCW − 0.5)√N. A correct expression is σpred = (∆fCW/0.5) × √N = 2∆fCW√N. Ensure the typesetting unambiguously shows multiplication by √N (not division).

P5-E2 (Section VII, p. 8–9): Inconsistent N and impossible sample size in Phase 2 sweep σ
- Problem: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ∆fCW = −0.0026 monopole … predicted … ≈ −10 matches the observed −11.3 within order unity.” The stated n=3,696,152 cannot be the chirality-relevant bin size (upper bounded by 791,635 total). The text appears to mix the DESI parent spectroscopic N (for environment classification) with the chirality-labeled N (for σfrom half). Using a parent-sample N to compute a chirality σ is methodologically invalid.
- Required fix: Recompute all σfrom half values in the sweep using the correct N = number of chirality-relevant matched spirals in that class and cell. Report the correct nclass, fCW, and σfrom half for that cell (or withdraw this claim). If you intended the statement as a heuristic “predicted magnitude,” label it clearly as such and remove any “observed” σ when N is not the chirality N. Provide a per-cell table (or public CSV with DOI) of nclass and σfrom half to support the significance framework claims.

P5-E3 (Section XI, p. 17 vs. Section VI.D.b, p. 7): Contradictory statements on target-program split
- Problem: Section VI.D.b reports large differences across DESI programs: bright fCW = 0.4970 (σ = −5.25) and dark fCW = 0.5051 (σ = +1.25), i.e., Δf ≈ 0.0081 (0.81 pp), and a 3.4σ bright-vs-dark z-test in the filament class. Section XI then states under “systematics” that the “target-class split (BGS vs. LRG-ELG-QSO) [has] BGS-only CW fraction within ±0.001 of LRG-ELG-QSO,” which flatly contradicts the earlier reported bright vs. dark difference in the full matched-spiral catalog.
- Required fix: Reconcile these statements. If Section XI refers to a different subset (e.g., after environment restriction, or after subtracting the catalog monopole within each program) state that explicitly and provide the corresponding numbers. Otherwise, correct or remove the ±0.001 claim. Present a consistent, single set of program-split results and clarify whether they are overall, environment-stratified, and/or monopole-subtracted.

P5-E4 (Sections V and VIII.F, multiple pages): Reliance on an unreviewed monopole estimate without uncertainty propagation
- Problem: Many core inferences rely on subtracting or comparing to the catalog-wide monopole ∆fCW = −0.0026 from Paper IV (unpublished). Although the text says “uncertainty is propagated explicitly below,” I do not find any uncertainty on ∆fCW propagated into the σvs monopole residuals or into the various look-elsewhere and Bonferroni assessments. Treating ∆fCW as a fixed constant overstates the certainty of “monopole-consistent” conclusions.
- Required fix: Propagate the uncertainty on ∆fCW into all σvs monopole residuals and any test that conditions on the monopole (e.g., show σvs monopole distributions with confidence bands). Better: fit ∆fCW as a nuisance parameter jointly with the per-class fCW and quote environment contrasts marginalized over the monopole uncertainty. At minimum, provide the Paper IV uncertainty on ∆fCW and carry it through all places where σpred = 2∆fCW√N is used.

P5-E5 (Section VII.A, p. 9–10): Unsupported “no cell crosses Bonferroni-9” claim without tabulated evidence
- Problem: You state that “zero of the nine sweep cells produces a per-class |σvs monopole| residual above the Bonferroni-9 (α = 0.05) threshold |σ| ≈ 3.02.” No per-cell σvs monopole tables are shown; the text says they are not reported.
- Required fix: Provide the per-cell, per-class σvs monopole values (either as a table in the paper or deposited in a public repository with a DOI and summarized concisely in the manuscript) to substantiate the claim. Include the underlying nclass for each cell.

MAJOR

P5-M1 (Section VI.A, p. 6): Inconsistent σpred numbers from the stated ∆fCW
- Problem: “Predicting σpred from ∆fCW = −0.0026 gives σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28.” Using Table II N, the correct values are ≈ −3.32 (filament, N=408,187) and ≈ −3.28 (cluster, N=397,505). The filament value appears miscomputed.
- Required fix: Correct σpred(filament) to approximately −3.32 (or provide the exact N used if different from Table II). Audit all similar σpred calculations for consistency.

P5-M2 (Sections IX.A and Fig. 7, p. 15–16): Tempel filament concordance rounding
- Problem: You report a 0.026 pp difference between V-Web filament and Tempel filament-like. From the given fCW (0.4980 vs. 0.4982), the absolute difference is 0.0002 = 0.02 pp, not 0.026 pp.
- Required fix: Correct the stated concordance to 0.02 pp (or provide the exact fCW used and how 0.026 pp was derived).

P5-M3 (Section VI.D, Table IV, p. 6–7): Ambiguous density variable used for within-class quartiles
- Problem: The quantity “¯ρ” is reported with values such as 1.55–2.21 but without units or a precise definition (e.g., smoothed overdensity δ, log-density, or normalized density).
- Required fix: Define the density variable used for stratification, its units (dimensionless?), smoothing scale, and normalization. Clarify if it is δ, 1+δ, log10(1+δ), or another quantity.

P5-M4 (Section VI.B, p. 6): Logistic regression result without uncertainties
- Problem: “A logistic regression … gives a z-coefficient of 0.0059 with no significant intercept (0.000652), consistent with no redshift dependence.” No standard errors, z-scores, or p-values are reported for the coefficient(s).
- Required fix: Report standard errors and p-values (or confidence intervals) for the logistic regression coefficients, and the number of objects used. If regularization was used, specify it.

P5-M5 (Section VIII.A, p. 10–11): Nearest-hole search adequacy for DESIVAST VoidFinder spheres
- Problem: The membership test uses a KDTree on hole centers with k=20 nearest neighbors, “sufficient given the 24 Mpc/h maximum hole radius.” There is no demonstration that k=20 is sufficient to capture all potentially containing spheres, given hole sizes and local densities.
- Required fix: Justify k=20 with a quantitative bound (e.g., show that the 21st nearest center is always beyond max(Reff) + safety margin for all tested points, or increase k to a conservative value and verify no changes). Alternatively, assert and show that an exact spatial index or bounding volume hierarchy was used.

P5-M6 (Section X, p. 16–17): Entropy-weighted variance formula is asserted without derivation
- Problem: For the ASTRA entropy-weighted classifier you state “sub-class variance Σi Pi^2/4 under the Bernoulli-0.5 null.” This expression needs justification because fractional weighting of Bernoulli indicators across probabilistic classes typically requires a specific estimator and variance derivation (and may include covariance between classes due to ΣPi = 1).
- Required fix: Provide a short derivation or a reference justifying the variance expression used for the entropy-weighted estimator. If it is an approximation, label it as such and quantify the potential bias or error.

P5-M7 (All sections depending on external “companion data repository”): Reproducibility artifact
- Problem: Many claims (permutation nulls, sweep-cell matrices, cross-matches) defer to a “companion data repository,” but the submission does not include a durable, citable archive.
- Required fix: Deposit the analysis code and all derived data products used for figures/tables in a permanent repository with a DOI (e.g., Zenodo). Cite the DOI in the manuscript. Include seeds and versions sufficient for bitwise reproducibility.

MINOR

P5-m1 (Section VII, first paragraph, p. 8): Notation typo for sweep definition
- Problem: “Rs ∈ {10, 25, 50} Mpc/h × Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}.” This reads as if Ngrid multiplies λth.
- Required fix: Rephrase as “Ngrid = 256^3; λth ∈ {0.0, 0.1, 0.3}.”

P5-m2 (Section VIII.E, Table IX, p. 12): Clarify that the “0 maximal voids per pixel” bin corresponds to out-of-coverage regions
- Problem: The text explains this in prose, but the table caption alone doesn’t.
- Required fix: Add a note in the table caption that the “0” bin corresponds to pixels outside DESIVAST BGS coverage (mask regions).

P5-m3 (Figures 4 and 6, p. 9 and p. 14): Axis/legend clarity
- Problem: Colorbars show σfrom half; axes on Mollweide plots do not include coordinate tick labels. This is minor but can hinder standalone interpretability.
- Required fix: Add minimal RA/Dec gridlines or tick labels, or specify “Equatorial coordinates” and orientation in caption.

P5-m4 (Section V.A, p. 4): LEE correction explanation
- Problem: You give both Bonferroni and empirical max-stat MC corrections. It would help to state explicitly that the empirical correction accounts for pixel-to-pixel correlations induced by the survey mask, whereas Bonferroni assumes independence.
- Required fix: Add one sentence clarifying this (you do hint at it, but being explicit will help readers).

NITS

P5-n1 (Throughout): 2563 used instead of 256^3
- Problem: Superscripting is sometimes omitted (e.g., “2563”).
- Required fix: Use 256^3 consistently.

P5-n2 (Section IX.B, p. 15): Extremely small p-values (e.g., p < 10^−1000)
- Problem: While mathematically possible, writing p < 10^−1000 reads hyperbolic.
- Required fix: Consider phrasing as “p ≪ 10^−10” or “effectively zero at double precision.”

P5-n3 (Formatting): Hyphenation and minor line breaks
- Problem: A few awkward breaks (e.g., “sensi- tivity”) occur.
- Required fix: Clean hyphenation.

Length and scope
- The manuscript is long (20 pages) for a null result of relatively narrow scope. Consider condensing by:
  - Moving the Phase 2 sweep details and some secondary cross-checks (ASTRA overlap nuances, T-Web fraction comparisons) to an Appendix or Supplementary Material.
  - Focusing the main text on the DESIVAST-anchored primary analysis and one canonical V-Web run, with compact summaries of secondary diagnostics.
- A target of 12–14 pages (plus appendices) seems appropriate.

Audit of key Abstract/Conclusion scalars
- DR1 spectro sample used for V-Web: 14,622,283 — matches body (p. 3–4).
- Matched unique galaxies: 2,232,212 — matches Table I (p. 3).
- Chirality-relevant: 791,635 — matches Table I (p. 3).
- Class fractions and σ (filament 0.4980/−2.61σ; cluster 0.4963/−4.66σ; wall 0.5034/+0.55σ; void 0.4836/−0.68σ) — consistent with Table II and recomputation (p. 5).
- Inter-class range 1.98 pp — 0.5034 − 0.4836 = 0.0198; correct (p. 5).
- Density-quintile max |σ| 3.94 and monopole-subtracted residual 1.87 — matches Table III (p. 6–7).
- HEALPix label-shuffle p-values 0.607/0.135/0.413 — Table V gives 0.607, 0.135, 0.413 (p. 8).
- Phase 2 sweep max inter-class range 0.22 pp — Table VI and Fig. 5 confirm (p. 8–10).
- DESIVAST void vs non-void: nvoid = 56,981; fvoid = 0.4964; fnon-void = 0.4971; Δf = 0.0007 — Table VII (p. 11).
- V2-REVOLVER catalog-native void σ = −0.24 at n = 86,276 — Section VIII.D (p. 11–12).
- Pearson r between maximal-void density and σpix = +0.006 (p = 0.88) across 727 pixels — Fig. 6 and text (p. 13–14).
- Tempel filament concordance cited as 0.026 pp — should be corrected to ~0.02 pp (see P5-M2).

These checks confirm most headline numbers, with the specific exceptions noted above (Eq. 1, the Phase 2 “n=3,696,152” σ, σpred(filament) misvalue, Tempel concordance rounding, and the program-split contradiction).

## Summary recommendation
MAJOR REVISIONS

The paper presents a useful and thorough null test with multiple cross-checks, but it contains essential methodological and arithmetic issues that must be corrected before acceptance. Specifically: fix the algebraic error in Eq. (1); correct the Phase 2 sweep σ computation and N misuse; reconcile contradictory statements about the program split; and propagate the Paper IV monopole uncertainty into all monopole-conditioned inferences. Additional major/minor fixes are listed above. Once these are resolved and the presentation is tightened, the manuscript could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

Note: I only list NEW issues not present in my initial report. IDs continue the same scheme (P5-E#, P5-M#, P5-m#, P5-n#). Citations like “§VI D” refer to sections in the manuscript you provided.

ESSENTIAL

P5-E6 (Abstract; §VIII B–C; Table VIII): Systematic sign errors in ΔfCW for DESIVAST results
- Problem: Multiple inconsistencies between text, table, and arithmetic:
  - Abstract: “DESIVAST … returns fvoid = 0.4964 vs fnon−void = 0.4971, ΔfCW = 0.0007.” Arithmetic gives ΔfCW = fvoid − fnon−void = −0.0007, not +0.0007.
  - Table VIII:
    • VoidFinder row: fvoid = 0.4964, fnon−void = 0.4971; table lists ΔfCW = +0.0007 (should be −0.0007).
    • V2-REVOLVER row: fvoid = 0.4986, fnon−void = 0.4967; table lists ΔfCW = −0.0019 (should be +0.0019).
    • V2-VIDE row: fvoid = 0.4971, fnon−void = 0.4970; table lists ΔfCW = −0.0001 (should be +0.0001).
  - Body (§VIII C) prose says REVOLVER has the “opposite sign of VoidFinder’s small difference,” which matches the corrected arithmetic, but contradicts the table.
- Required fix: Correct all ΔfCW signs (Abstract, Table VIII, and any dependent prose). Add a unit note (“pp”) wherever helpful.

P5-E7 (§VI D.a, cluster z-quartiles): Claim “none crosses Bonferroni-4” is false
- Problem: You report cluster σfrom half per redshift quartile as −2.33, −1.73, −3.14, −2.12, and then write “none individually crossing the Bonferroni-4 |σ| = 3.02 threshold at α = 0.01.” But |−3.14| > 3.02, so Z3 does cross the threshold.
- Required fix: Correct the statement and revisit any interpretation relying on it. If you intended a different α or a monopole-subtracted metric, state and compute that explicitly.

MAJOR

P5-M8 (§VI D.b vs §VIII F vs §VI D.d): Inconsistent denominators and program-split baselines
- Problem:
  - §VI D.b uses the chirality-relevant matched-spiral catalog (N = 791,635; bright = 775,760; dark = 14,782; backup/other = 1,093 total).
  - §VI D.d then analyzes a 4×2 contingency on “nbright+dark = 811,609 spirals,” which exceeds the 791,635 chirality-relevant total, implying a different denominator (likely the 812,793 env-labeled superset in §VIII F minus backup/other, but this is never stated).
  - The “overall matched-spiral ratio 0.978” for bright/(bright+dark) is incompatible with the visible counts in §VI D.b (775,760/(775,760+14,782) ≈ 0.9812). It may match the 811,609 denominator, but the numbers need to be shown.
- Required fix: Harmonize sample definitions and denominators across sections. For each reported program-split statistic, specify the exact population (e.g., “chirality-relevant,” “env-labeled superset,” “bright+dark only”). Recompute and present consistent bright-fraction baselines and p-values.

P5-M9 (§VIII A, §VIII E): Inconsistent DESIVAST void-radius bounds used in kNN search justification
- Problem: The VoidFinder-hole membership test asserts k = 20 nearest centers is “sufficient given the 24 Mpc/h maximum hole radius,” but elsewhere (§VIII E) you state DESIVAST maximal-void effective radii span 10–32 Mpc/h. If VoidFinder hole radii can exceed 24 Mpc/h (or if effective vs hole radii are not strictly comparable), k = 20 may be insufficient near dense void regions.
- Required fix: Provide a quantitative bound validating k = 20 for the actual distribution of VoidFinder hole radii in DR1 (e.g., show the 21st nearest center is always beyond max(Reff) + margin). If not guaranteed, increase k (or use an exact spatial index) and verify results are unchanged.

P5-M10 (§V, Figure captions): “Exact binomial credible interval” vs “Jeffreys credible interval”
- Problem: §V says “exact binomial 95% credible interval,” which colloquially refers to Clopper–Pearson. Figure captions and text elsewhere specify “95% Jeffreys binomial credible intervals.” These are not the same.
- Required fix: Use consistent terminology throughout. If you use Jeffreys intervals, state “95% Jeffreys Bayesian credible intervals” in §V and captions.

P5-M11 (§VIII D and Table VIII prose/table mismatch): REVOLVER “opposite sign” statement vs table
- Problem: §VIII C correctly notes that V2-REVOLVER’s sign is opposite to VoidFinder’s, but Table VIII’s ΔfCW entries carry the wrong signs (see P5-E6). The prose/table inconsistency can mislead readers.
- Required fix: Once ΔfCW signs are corrected in Table VIII, ensure the “opposite sign” statement remains accurate, and reconcile any text that references the incorrect table signs.

P5-M12 (§VIII F): Mixed pixel selections without explicit qualifiers
- Problem: You report per-pixel σvs monopole distributions “at NSIDE = 32 … across 1,821 valid pixels” (presumably all-z), while Figure 6’s bottom panel uses z ≤ 0.24 and “1,496 valid pixels.” The correlation calculation is on 727 pixels with both voids and ≥ 200 spirals. These are different selections, but the narrative flows without re-stating the selection changes.
- Required fix: Whenever switching the pixel selection (all-z vs z ≤ 0.24; ≥ 200 spirals; “both voids and ≥ 200 spirals”), make the filter explicit and keep the counts aligned in-text and in captions.

P5-M13 (§VI D.d): “Max class-to-overall bright-fraction deviation 1.5 pp” is inconsistent with stated numbers
- Problem: With the quoted class bright fractions {0.981, 0.962, 0.966, 0.989} and overall ≈ 0.978, the largest deviation is |0.962 − 0.978| = 1.6 pp (wall), not 1.5 pp.
- Required fix: Recompute and correct the deviation, or show the exact overall fraction used for this comparison and how 1.5 pp was obtained.

MINOR

P5-m5 (§IX A; Fig. 7 caption and text): “0.026 pp” filament concordance rounding
- Problem: The stated difference 0.026 pp between V-Web filament (0.4980) and Tempel filament-like (0.4982) is 0.0002 = 0.02 pp, not 0.026 pp.
- Required fix: Correct to 0.02 pp (or provide exact values if more precise fCW were used).

P5-m6 (§VII A, bullets): Range-vs-uncertainty comparison needs an explicit caveat
- Problem: You argue the per-cell inter-class fCW range (max 0.22 pp) is “below the per-class counting-statistics floor,” but a range statistic is not directly comparable to single-class 1σ uncertainties. You later mention an empirical max-stat null but provide no table (already flagged previously as P5-E5).
- Required fix: Add a sentence clarifying that the range-vs-1σ comparison is heuristic and that the formal assessment is via the empirical max-stat permutation test (and provide the per-cell table per P5-E5).

P5-m7 (§VIII F): Typo “NSIDE-= 32”
- Problem: Hyphen after NSIDE likely a typesetting artifact.
- Required fix: Remove.

P5-m8 (§V B, terminology): “Primary/secondary” labeling is clear, but the “V-Web secondary path (§XIII)” cross-reference is wrong
- Problem: §VIII A says “in contrast to the V-Web secondary path (§XIII),” but §XIII is Limitations, not the V-Web methods/results section.
- Required fix: Fix the cross-reference to the correct V-Web section (§IV/§VI/§VII as intended).

P5-m9 (§VIII E, Table IX caption): Clarify coverage in caption
- Problem: You note in prose that the “0 maximal voids/pixel” bin corresponds to out-of-coverage regions. The caption alone does not state this.
- Required fix: Add a note in the Table IX caption that 0-void pixels correspond to sky outside the DESIVAST BGS coverage.

P5-m10 (Units/notation consistency): 2563 vs 256^3
- Problem: Superscripts are sometimes omitted.
- Required fix: Use 256^3 consistently.

P5-m11 (Abstract phrasing): “max 0.0022 at Rs = 25, λth = 0.3”
- Problem: You mix “percentage points” and fractional units in the same parenthetical.
- Required fix: Use consistent units in the parenthetical, e.g., “max 0.22 pp (i.e., 0.0022 in fractional units).”

OBSERVATIONS THAT MAY REQUIRE AUTHOR CLARIFICATION (not formal findings)

- Inclusion of QSOs (SPECTYPE = QSO) in the parent sample for the tidal field is methodologically defendable, but a one-line justification (why including QSOs does not bias the density field at the chosen Rs) would help.
- The RSD order-of-magnitude argument is reasonable, but because you later emphasize anisotropic eigenvalue deformation, consider adding a short quantitative pointer (or reference) on expected eigenvalue perturbations at Rs = 25 Mpc/h to close the loop.

If these NEW issues are addressed alongside the items in my initial report, the manuscript’s statistical and arithmetic rigor will be much improved.