# P5 auto-2026-06-08_1819pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (8959 chars)
**Wall time**: 455.9s

---

# Referee Report: P5 — Environmental Dependence of Spiral Chirality

## Overall Assessment

This is a 20-page null-result paper that reports no environment dependence of spiral chirality in DESI DR1. The arithmetic mostly checks out, but the paper has a severe foundational problem: it rests on labels from an unpublished, non-peer-reviewed "Paper IV" companion, cites two future-dated arXiv papers (2604.xxxxx), and contains a load-bearing internal inconsistency in the headline sample size. The "null" is also acknowledged to be systematics-dominated (BGS selection function), and the only non-null residual (filament bright/dark sign-flip at 3.4σ) is hand-waved away. The paper is far too long for a null with this much sensitivity ambiguity.

---

## ESSENTIAL findings

### P5-E1 — Headline sample-size inconsistency (Abstract, Table II, p.1, p.5)
The abstract states per-class CW fractions are computed "on the 791,635 chirality-relevant spirals." Table II rows sum to:
- void 428 + wall 6,673 + filament 408,187 + cluster 397,505 = **812,793**, not 791,635.
- CW counts sum to 207+3,359+203,261+197,284 = **404,111**, while Table I gives 393,592 CW (a 10,519 excess).

The mismatch is buried in §VIII F as a "21,158-row excess (2.7%)" but is never reconciled with the abstract or Table II caption. The headline σ values (notably the −4.66σ cluster and −2.61σ filament) are computed on a *different* sample than the one advertised. **Fix**: either restrict Table II to the 791,635 sample and recompute all σ values, or update the abstract and every caption to declare 812,793 explicitly. The current presentation is misleading.

### P5-E2 — Critical dependency on unpublished, non-peer-reviewed work
The entire CW/CCW labeling is taken from "Paper IV [3]" which is declared "in preparation; manuscript in preparation" and "not yet peer reviewed." The catalog-monopole offset ∆f_CW = −0.0026 — which the entire residual-significance framework relies on — is propagated as input from this unpublished work. PRD cannot accept a paper whose central numerical inputs are unverified preprints by the same author. **Fix**: either submit Paper IV first and let this paper be evaluated against the published version, or include a fully self-contained derivation of the classifier monopole in this manuscript.

### P5-E3 — Future-dated / unverifiable references
- [11] Ullah et al., arXiv:**2604.02463**, "preprint (2026)"
- [12] Zapata-Zuluaga et al., arXiv:**2604.01456**, "(2026)"

ArXiv identifiers 2604.xxxxx correspond to April 2026, which is in the future relative to a normal review cycle and cannot be checked. The "concurrent literature" cross-validation in §IX B and the ASTRA cross-match in §X depend on these. **Fix**: verify these IDs exist or replace with available citations.

### P5-E4 — Post-hoc primary/secondary designation
§V B explicitly states: *"a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc"*. The paper reports five environment classifiers (V-Web, Tempel FoF, three DESIVAST algorithms, ASTRA, T-Web overlay) with multiple stratifications each, then designates DESIVAST as primary *after seeing the results*. This is a textbook garden-of-forking-paths problem; the Bonferroni-5 family treatment within DESIVAST does not address the multi-classifier selection. **Fix**: report all classifiers on equal footing, or apply a Bonferroni correction across the full multi-classifier × multi-stratification family (which would erode whatever marginal "evidence" remains).

### P5-E5 — Filament 3.4σ sign-flip handwaved
The filament-class bright-vs-dark joint z-test of ≈3.4σ is real (I recompute 3.41σ from the quoted numbers, ✓), is presented as "the strongest single residual structure in the paper after the catalog-monopole subtraction," and is explicitly *not* cleanly attributable to BGS systematics ("the current data do not allow us to cleanly partition"). The paper then declares environment-independence anyway by anchoring on DESIVAST. A 3.4σ residual that "cannot be cleanly partitioned" between systematics and astrophysics is not a null result; it is an unresolved positive finding being papered over. **Fix**: either (a) demonstrate quantitatively that the DESIVAST analysis is statistically independent of this residual (it cannot be — the matched-spiral subsample is shared), or (b) reframe the headline as "consistent with environment-independence except for an unexplained 3.4σ filament target-class signature."

### P5-E6 — V-Web void class is not a measurement
The V-Web void class has n=428 spirals and 0/6 concordance with DESIVAST at the z≤0.24 BGS coverage. The paper concedes "the V-Web 'void' label at low z should be read as 'not in a DESIVAST-defined cosmic-web density minimum.'" Reporting this class in the headline Table II as a chirality-environment result is misleading. **Fix**: drop V-Web void from the headline or relabel it as a non-measurement.

---

## MAJOR findings

### P5-M1 — σ_pred arithmetic inconsistency
Page 6 states σ_pred(filament) ≈ −3.16 at n=408,187. Recomputing: 2 × 0.0026 × √408,187 = **−3.32**, not −3.16. This is a 5% error in a load-bearing number ("both within order-unity of observation"). σ_pred(cluster) = −3.28 checks out (✓ recomputed −3.28). **Fix**: correct the filament value.

### P5-M2 — Tempel cross-validation cherry-picks the concordant pair
The paper repeatedly emphasizes "filament_like vs filament: 0.026 pp" as the headline robustness check. The other three pairings (1.11, 0.62, 0.66 pp) fail the stated 0.2 pp spec but are explained away by "counting statistics" or "classifier-definition mismatch." Either the spec applies to all classes or to none. Also, the small_group↔wall and cluster_like↔cluster mappings are conceptually arbitrary (FoF richness vs. tidal-tensor eigenvalues), so the 0.026 pp filament agreement may itself be coincidence. **Fix**: drop the concordance-spec framing and report the comparison neutrally.

### P5-M3 — "Null is not positive evidence" admission used inconsistently
§VIII B says explicitly: *"a null is not positive evidence; we report it as a controlled-sample non-detection."* Yet the abstract, conclusions, and §XII C all advertise the result as if it were an upper limit constraining future bounce/inflation models. The Shamir 2022 comparison in §XII C ("leaving no room for a residual environment-dependent chirality of the Shamir 2022 amplitude") is exactly the kind of overclaim §VIII B disavows. **Fix**: pick one framing.

### P5-M4 — Length grossly disproportionate to content
20 pages + 7 figures + 11 tables for a null result driven by a systematic-dominated monopole, with the controlling analysis (DESIVAST n=56,981) producing ∆f_CW = 0.0007. The Phase 2 sweep, ASTRA cross-match, Tempel cross-validation, T-Web overlay, and toy EFT appendix are all redundant once the primary DESIVAST null is reported. **Recommended max**: 8 pages PRD Letter-style, or 12 pages with full Phase 2 + DESIVAST analysis only. Cut Tempel, ASTRA, T-Web, and Appendix A.

### P5-M5 — Toy EFT appendix admits it is not what it pretends to be
Appendix A introduces an operator L_parity ⊃ g_φ (∇^i φ)(∇^i ρ/ρ_bg)(L̂·ẑ), then admits in successive paragraphs that (i) the operator is not from cited literature, (ii) the ẑ factor breaks rotational invariance, and (iii) the construction is not gauge invariant. This is not a "guide for future model-building"; it is filler that retroactively justifies citing Alexander-Yunes and Lue-Wang-Kamionkowski. **Fix**: delete the appendix or replace with a properly motivated covariant operator.

### P5-M6 — Density-quintile residual buried under monopole
§VI C reports |σ|_max = 3.94 in density quintile 3, monopole-subtracted residual 1.87σ. But the test is presented as a "null" only after monopole subtraction, when the raw observed σ exceeds 3. The paper does not show the monopole subtraction is well-calibrated at the quintile level (the Paper IV monopole is a catalog-mean; per-quintile variation in selection function could shift it). **Fix**: demonstrate monopole stability per quintile or report the unsubtracted result honestly.

### P5-M7 — RSD treatment is hand-waved for the V-Web path
§XIII admits the V-Web tidal-tensor is computed in redshift space without reconstructed positions, that "anisotropic eigenvalue deformation is the dominant channel," and that the scalar σ_v/(aH) ≲ 5–8 Mpc/h bound is "necessary but not sufficient." The paper then proceeds as if the V-Web result were RSD-immune. The boundary-crossing estimate (3–5% of cells) gives 2–4 × 10^4 potentially misclassified galaxies — comparable in magnitude to the entire void and wall classes. **Fix**: either run the reconstructed-position re-classification or restrict claims to the DESIVAST primary path only.

### P5-M8 — Selection effects not actually controlled
§VI A.b ("Tracer-program stratification") demonstrates that the catalog-level −5σ "is entirely driven by the bright program." The contingency test in §VI A.d returns χ²=4932 with p<10^−1000 showing V-Web class is NOT independent of target program (max bright-fraction deviation 1.5 pp — note: I compute wall at 0.962 vs overall 0.978 = −1.6 pp, which is the actual max, so the "1.5 pp" claim is also slightly off). The paper acknowledges this but proceeds. A non-independent stratification means the V-Web tests are confounded by BGS selection. **Fix**: either marginalize over target program properly, or restrict to the dark sample (where n is too small as the paper concedes).

### P5-M9 — Sample size inconsistency in tracer decomposition
§VI A.c: "filament bright (n = 416,701)" and "filament dark (n = 21,203)" sum to 437,904, but the filament class in Table II has n=408,187. The tracer decomposition is on a different (larger) sample than the headline. **Fix**: reconcile.

### P5-M10 — Multiplicity treatment for HEALPix scans is inconsistent
§V A defines empirical max-stat p-values. §VI E quotes p=0.607, 0.135, 0.413 for NSIDE 16/32/64 (Table V). The abstract quotes 0.61/0.135/0.413. Why is NSIDE=16 rounded to 0.61 but the others kept at 3 digits? Trivial but symptomatic. More importantly, the three NSIDE choices are themselves a multiplicity that is not Bonferroni-corrected — three independent multi-bin scans means the effective family is larger than reported. **Fix**: apply consistent rounding; account for NSIDE multiplicity.

### P5-M11 — Catalog-native V2 cross-check inconsistent with three-algorithm table
Table VIII gives V2-REVOLVER n_void = 102,911. §VIII D gives V2-REVOLVER n_void = 86,276 (catalog-native). The two should be cross-referenced explicitly; the reader is left to figure out which is "primary." **Fix**: clarify which is the headline number and why both are reported.

---

## MINOR findings

### P5-m1 — Footnote `a` on page 1 splits the abstract
The Hahn-vs-Hoffman terminology disambiguation footnote is appended to the abstract and runs to the bottom of page 1. This should be in §IV.A, not the abstract.

### P5-m2 — Recurring phrase repetition
"BGS-selection-function-conditioned imaging-leg systematics tracked in Paper IV" appears nearly verbatim 4+ times (abstract, §VI A.b, §VI A.c, §VIII E). Compress.

### P5-m3 — Paper II [4] referenced but not used
The paper cites companion Paper II for "primordial f_NL discriminators" but Paper II is also "in preparation." Remove or defer.

### P5-m4 — Inconsistent use of "P4" vs "Paper IV"
Both notations appear (e.g. "P4 monopole" in §VIII F, "Paper IV monopole" elsewhere). Pick one.

### P5-m5 — Table II final row "range — — 0.0198 —" is poor table design
Range belongs in caption or a separate summary, not as a table row with em-dashes.

### P5-m6 — Figure 1 caption duplicates body text
The Phase 1 volume fractions are stated twice (caption and §IV B). Cut one.

### P5-m7 — Figure 6 caption references "885 occupied pixels, median 4 voids/pix" but body text §VIII E quotes "297 occupied pixels with median 14 maximal voids per occupied pixel"
The 297 number is for NSIDE=16; Figure 6 is NSIDE=32. The transition between NSIDE values is unclear; both should be tagged with NSIDE explicitly.

### P5-m8 — Reference [9] Shamir 2022 percentage claim
The paper states Shamir 2022 reports "∼ 2 − 4% large-scale asymmetry." Verify against the Shamir abstract; this kind of claim drives the §XII C comparison.

### P5-m9 — Bibliography format inconsistency
Refs [11] and [12] use "(2026)" while others use "Astron. Astrophys. 641, A6 (2020)" format. Standardize.

### P5-m10 — Sigma values from different nulls juxtaposed without explicit "not comparable" tag
Throughout, σ_from_half (binomial), σ_pred (monopole-based), and σ_vs_monopole (residual) are quoted side-by-side. While defined in §V, the juxtaposition in tables (e.g. Table III) without column headers distinguishing them invites misreading. **Fix**: rename column headers explicitly (σ_obs(binomial), σ_pred(monopole), residual).

### P5-m11 — "Survey-edge artifact dominated at z ≲ 0.24" in abstract
This is asserted without quantification in the abstract; the supporting evidence is the 0/6 cross-match in §VIII A which is far too small a sample to make this claim rigorously. **Fix**: soften or remove from abstract.

### P5-m12 — Mollweide Figure 6 (top panel) has axes labeled 0.0–1.0
Top panel of Figure 6 shows axis ticks "0.0, 0.2, 0.4, 0.6, 0.8, 1.0" on both axes — these are not standard celestial coordinates for a Mollweide projection. The plot framework is incorrectly configured.

### P5-m13 — Conclusion repeats abstract verbatim
§XV essentially restates the abstract. Compress.

---

## NIT findings

### P5-n1 — "Date: June 2026" on title page
For a manuscript citing 2604.xxxxx arXiv papers, the future date is consistent but should be normalized to the submission date.

### P5-n2 — "The Paper IV ¯fCW = 0.4974 horizontal reference"
Bar notation inconsistent (¯f vs f̄) throughout.

### P5-n3 — Page 4 Figure 1 caption: "(Rs = 25 Mpc/h, λth = 0, Ngrid = 256^3)" while body says 256³
Notation switch.

### P5-n4 — "DESIVAST" and "DESI-VAST" both appear
Standardize.

### P5-n5 — "−5σ" written without specifying which monopole-removed or raw
Several places, e.g. abstract "the −5σ catalog-level signal." Tag every instance.

---

## Summary recommendation

**REJECT**

The paper has three independently fatal issues: (1) the entire CW/CCW labeling depends on an unpublished, non-peer-reviewed companion paper by the same author whose monopole bias is the central calibration; (2) two of the key cross-validation references are arXiv IDs from April 2026 that cannot be verified, and the headline sample-size of 791,635 disagrees with the per-class sums in Table II (812,793) by 2.7% in a way that is buried 8 pages deep; (3) the paper is a 20-page null result whose strongest residual — a 3.4σ filament bright/dark sign-flip that the authors admit "cannot be cleanly partitioned" between systematics and astrophysics — is explicitly handwaved by anchoring on a post-hoc-designated "primary" analysis (DESIVAST) that the authors concede was not pre-registered. PRD requires that null results be definitive; this one is systematics-limited at every level, the calibration is propagated from unpublished work, and the framing oscillates between "controlled non-detection" (when convenient) and "upper bound on bounce models" (when advertising). Resubmit only after Paper IV is published, the headline sample is reconciled, the 3.4σ filament residual is either resolved or honestly elevated to a positive finding, and the manuscript is cut to ≤10 pages with the secondary cross-checks (Tempel, ASTRA, T-Web, toy EFT) removed.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings — Second Pass

I went back and checked arithmetic, cross-references, and sample-size cascades more carefully. Several new issues emerge.

---

## ESSENTIAL — Additional

### P5-E7 — Sample-size cascade across §VI A subsections is internally inconsistent in three independent ways
The bookkeeping problem flagged in P5-E1 (812,793 vs 791,635) is worse than first reported, because the *per-subsection* sample sizes also fail to reconcile:

**(a) §VI A.c filament stratification exceeds Table II filament total by 7.3%.**
"Filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203)" → 416,701 + 21,203 = **437,904**. Table II filament n = 408,187. Excess = 29,717 rows (7.3%).

**(b) Abstract cluster_dark = 4,234 implies cluster total ≠ Table II cluster total.**
Abstract: "cluster_dark = 4,234." §VI A.d: cluster bright/(bright+dark) = 0.989, so dark fraction = 0.011. If n_dark = 4,234 then total = 4,234/0.011 = **384,909**. Table II cluster n = 397,505. Discrepancy = 12,596 rows.

**(c) §VI A.d states n_bright+dark = 811,609.**
The 812,793 superset minus backup (875) minus other (218) = **811,700**. Paper says 811,609. Off by 91. Small, but symptomatic.

So the paper uses at least three internally inconsistent class totals (Table II superset, §VI A.b 791,635 program-totals sample, and §VI A.c/abstract per-class subset) without ever disclosing the differences. This is the actual source of the bookkeeping problem — not just a single off-by-21,158 reconciliation, but a cascade. **Fix**: produce a single sample-flow diagram with N at every cut and use those numbers consistently across all sections.

---

## MAJOR — Additional

### P5-M12 — Bonferroni-9 threshold value is wrong (§VII A)
The paper writes: "zero produces a per-class |σ_vs monopole| residual above the Bonferroni-9 (α = 0.05) threshold |σ|^Bonf_{0.05,9} ≈ 3.02".

Recomputing Eq. (2): √2 · erfc⁻¹(0.05/9) = √2 · erfc⁻¹(0.00556). The two-sided critical value at α/K = 0.00556 is z = Φ⁻¹(1 − 0.00278) ≈ **2.77**, not 3.02. The 3.02 value the paper quotes is actually the Bonferroni-4 threshold at α = 0.01 (which they correctly compute elsewhere). This is a stale-number import; the load-bearing statement "zero produces a residual above 3.02" should be "above 2.77" — still passes, but the framework value itself is wrong. **Fix**: recompute.

### P5-M13 — σ_pred(filament) computed inconsistently in two places
§VI A states: "predicting σ_pred from ∆f_CW = −0.0026 gives σ_pred(filament) ≈ −3.16 and σ_pred(cluster) ≈ −3.28."

§VIII F states: "the Paper IV monopole prediction σ^class_pred = 2 · 0.0026 · √n_class ranges from 0.10σ (void) through 0.42σ (wall) to 3.27σ (cluster) and **3.32σ (filament)**."

Recompute: 2 × 0.0026 × √408,187 = 3.32. The §VIII F value (3.32) is correct; the §VI A value (3.16) is wrong by 5%. This compounds P5-M1 — the *same quantity* is computed two different ways in the same paper. **Fix**: pick 3.32 and propagate consistently.

### P5-M14 — Table VIII column "∆f_CW" has implicit sign convention (non-void − void) that is not stated
Checking: VoidFinder f_void=0.4964, f_non-void=0.4971, table column ∆f_CW = +0.0007. So column = f_non-void − f_void. V2-REVOLVER: 0.4967 − 0.4986 = −0.0019 ✓. V2-VIDE: 0.4970 − 0.4971 = −0.0001 ✓. The convention is consistent within the table but is *opposite* to the natural reading "void minus non-void" (which would be the signed effect of being in a void). The abstract's "∆f_CW = 0.0007" is signless and avoids the issue, but the table caption should disclose the sign convention. **Fix**: state convention explicitly; consider flipping to void − non-void since that is what the paper is testing.

### P5-M15 — Figure 2 caption claim "all four classes bracket the Paper IV monopole" is barely true for cluster
Cluster has n = 397,505, f = 0.4963. The 95% Jeffreys CI is approximately [0.4948, 0.4979]. The Paper IV reference is 0.4974, which sits 0.0005 inside the upper edge. This is true but trivially so; the visual claim in the caption ("all four classes bracket") conveys "the data are consistent with the monopole" when in fact the largest-N class barely touches it. **Fix**: state numerically how close the upper edge of the cluster CI is to the monopole, or remove the descriptor.

---

## MINOR — Additional

### P5-m14 — Paper IV monopole predicts -3.32σ for filament; observed -2.61σ
The §VI A claim "we interpret these as the global monopole leaking through the larger-sample bins" requires σ_pred to roughly *match* σ_obs. With correct σ_pred(filament) = −3.32 and observed −2.61, the gap is 0.71σ (about 22% short of prediction). For cluster: σ_pred = −3.28, observed −4.66, gap 1.38σ (42% over). These are described as "within order-unity of observation" — which is technically true but not an especially clean monopole leak; the filament is *less* deviant than predicted and cluster is *more*, which is the opposite of what a uniform monopole would do. **Fix**: discuss the residual structure, or acknowledge that "monopole leak" is an approximation.

### P5-m15 — §VIII F "near-perfect null at this independent statistic" hedge
For V2-REVOLVER catalog-native σ = −0.24 at n = 86,276, this is correctly described as a clean null. But "near-perfect" is a hedge that does not appear in any other null. **Fix**: standardize.

### P5-m16 — Reproducibility seed "20260515" assumes future date
Seed = 20260515 (15 May 2026). This date is in the future relative to any normal review cycle and presumes the paper's nominal "June 2026" date. If the manuscript is reviewed before then, the seed value is not verifiable from any actual run output. **Fix**: change to a date-independent seed.

### P5-m17 — Stat description: per-pixel σ std = 1.184 described as "unit standard deviation (within ∼18%)"
Yes, 1.184/1.000 = 1.184, i.e. 18.4% above unity. The descriptor "within ∼18%" is asymmetric — for a shot-noise null the std should be 1.0 and 18% high is a notable excess (not "within"). This is the standard signature of mild residual structure in the field. **Fix**: state "18% above unit-variance null" instead of "within 18%."

### P5-m18 — Pearson r calculation independently verified
r = 0.006, n = 727, gives t = 0.162 and two-sided p ≈ 0.87. Paper quotes p = 0.88, consistent within rounding. ✓ no error here (recorded for completeness).

### P5-m19 — DESIVAST point-in-sphere with 24 Mpc/h max hole radius and k=20 KDTree query
§VIII B: "k = 20-nearest-neighbour scipy.spatial.KDTree query on the hole centres, sufficient given the 24 Mpc/h maximum hole radius." But the maximum VoidFinder hole radius is asserted without citation; if the actual DESIVAST max hole radius were larger, k=20 could miss hole memberships. **Fix**: either cite the catalog's max-hole-radius statistic or verify that the k=20 setting captures all overlaps.

---

## NIT — Additional

### P5-n6 — Numerical formatting inconsistency in σ values
Table II quotes σ to two decimals (-0.68, +0.55, -2.61, -4.66). §VI A.b quotes σ to two decimals. Table IV quotes σ to two decimals. But §X Table XII quotes max-|σ| to two decimals (2.68, 2.25, 2.00). §VI E Table V quotes max-|σ| to two decimals (3.32, 4.13, 3.92). Generally consistent, but in places the manuscript uses 3-digit precision (e.g., p-values "0.607" vs abstract "0.61"). Standardize.

### P5-n7 — "Galaxies in the same V-Web environment" is sometimes used to mean per-galaxy NN-interpolated label
§IV A step 12 says "NN-interpolate the per-cell label". For galaxies in 25.9 Mpc/h cells with 25 Mpc/h Gaussian smoothing, the per-galaxy class can flip if the galaxy sits near a cell boundary. The paper does not report the per-galaxy class-stability metric (how often does the assigned class match the modal class within Rs?). **Fix**: report as a robustness statistic.

### P5-n8 — Footnote `a` claim "for backward compatibility with prior analyses we retain the 'V-Web' label"
The Hahn 2007 T-Web vs Hoffman 2012 V-Web disambiguation is correct, but "backward compatibility with prior analyses" implies the same author has prior analyses using this nomenclature — yet no such prior analyses are cited. **Fix**: cite or remove the backward-compatibility justification.

---

## Summary of new findings

The most important additions are:

1. **P5-E7** — the sample-size cascade problem is *three* internally inconsistent totals, not just one.
2. **P5-M12** — Bonferroni-9 critical value is wrong (3.02 → 2.77); imported stale from a different family.
3. **P5-M13** — σ_pred(filament) computed differently in §VI A vs §VIII F (3.16 vs 3.32 for the same quantity).
4. **P5-M14** — Table VIII sign convention undocumented.
5. **P5-M15** — Figure 2 caption "all four classes bracket the monopole" is barely true for cluster.

None of these change the recommendation (REJECT), but they reinforce the impression that the manuscript was assembled from multiple analysis stages with insufficient cross-checking of derived quantities.