# P5 auto-2026-06-08_1520pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (10361 chars)
**Wall time**: 542.3s

---

# Referee Report: Paper P5 — "Environmental Dependence of Spiral Chirality"

## Overall assessment

This is a 20-page paper reporting **a null result** with no theoretical motivation (the authors themselves write: "No published bounce or inflation model currently predicts a specific environment-conditional chirality signature at this scale"). The central claim—that spiral chirality is environment-independent in DESI DR1—is plausible, but the manuscript is bloated, internally inconsistent in several load-bearing places, anchored on an unpublished companion paper, and ridden with garden-of-forking-paths secondary analyses that the authors openly admit were not pre-registered. The arithmetic does not survive a basic audit.

---

## ESSENTIAL findings

### P5-E1. Table II / Fig. 2 sample size does not match the headline subsample
**Section VI A, p. 5–6.** Table II sums: n = 428 + 6,673 + 408,187 + 397,505 = **812,793**. Fig. 2 caption claims "n = 791,635 chirality-relevant matched spirals." The abstract states "Per-class CW fractions on the 791,635 chirality-relevant spirals are…"—and then quotes Table II values. The per-class CW counts also sum to 404,111 ≠ 393,592 (the headline CW count). The discrepancy is finally acknowledged in a parenthetical in §VIII F (p. 12) ("21,158-row excess … excluded from the headline by a stricter env-class-uncertainty filter"), which means the headline table is reported on a *different sample* than the abstract claims.
**Fix:** Either re-run Table II on the 791,635-row sample with the strict filter or relabel the headline table, Fig. 2, and the abstract honestly to identify the 812,793-row superset. As written, the abstract is wrong.

### P5-E2. Tracer-program decomposition arithmetic is impossible
**Section VI D ¶c (filament tracer-program) and abstract.** The abstract: total dark sample n = 14,782 (BGS-bright = 775,760, dark = 14,782, backup = 875, other = 218; sum = 791,635). But §VI D ¶c reports **filament dark alone n = 21,203**, and the abstract reports **cluster dark n = 4,234**. 21,203 + 4,234 = 25,437 ≫ 14,782 total. Similarly, filament bright alone n = 416,701 > filament total n = 408,187 (Table II). These numbers cannot all be true on any consistent definition of the matched-spiral sample.
**Fix:** Re-derive the per-V-Web-class × tracer-program table from a single declared sample and tabulate it; the 3.4σ bright-vs-dark filament sign-flip in the abstract is currently unsupported by arithmetically consistent counts.

### P5-E3. Paper IV (load-bearing input) is unpublished and not peer-reviewed
**Throughout (abstract; §II; ref. [3]).** The catalog monopole ∆f_CW = −0.0026, the global dipole bound, the per-leg systematics, and the classifier itself all come from Paper IV, cited as "in preparation; manuscript in preparation" (note the duplicate phrase in the ref). The present paper's "σ_pred" reference scale, monopole-subtracted residuals, and BGS-selection-function interpretation all depend on numbers from a non-existent reference. PRD cannot accept a paper whose principal calibration input is unpublished and unrefereeable.
**Fix:** Wait for Paper IV to be posted and refereed, or absorb its load-bearing content into this paper (re-deriving the monopole and dipole bounds here from first principles on the matched sample).

### P5-E4. σ_pred for the filament class is wrong
**Section VI A, p. 6.** The paper states σ_pred(filament) ≈ −3.16 using ∆f_CW = −0.0026 and N = 408,187. The correct value is 2·0.0026·√408,187 = **−3.32**. σ_pred(cluster) ≈ −3.28 is correct (2·0.0026·√397,505 = 3.28). The filament number is mis-computed by ~5% and the discrepancy is used to argue "within order-unity of observation."
**Fix:** Recompute and revise the interpretive text.

### P5-E5. DESIVAST void counts contradict between §VIII intro and §VIII C
**Section VIII, p. 10 vs. §VIII C, p. 11.** §VIII intro: "1,461 interior voids with VoidFinder, 420 with V2-REVOLVER, and 295 with V2-VIDE." §VIII C: "V2-REVOLVER (n_void^catalog = 1,992 effective voids, maximum effective radius 43.5 Mpc/h) and V2-VIDE (n_void^catalog = 1,478, max 55.9 Mpc/h)." 420 ≠ 1,992 and 295 ≠ 1,478. One of these pairs is wrong; both cannot be the official DESIVAST DR1 counts.
**Fix:** Reconcile against Rincón et al. 2025 Table 1; cite the authoritative number once.

### P5-E6. No pre-registration; multiplicity is enormous and only partially controlled
**Section V B, p. 5.** Authors openly state "a single a priori preregistered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc." The paper then reports five primary-path estimators, Phase 2 nine-cell sweep, three nulls (z, density, HEALPix), three NSIDE settings, four tracer-program splits, six robustness classes, plus ASTRA, Tempel, T-Web. The Bonferroni-5 over only the DESIVAST estimators is too narrow; the actual hypothesis space is in the hundreds. A pre-registered analysis was the right thing to do; doing this post-hoc and then selecting the cleanest cell as "primary" is exactly what PRD methods papers should not do.
**Fix:** Either declare the DESIVAST VoidFinder n=56,981 ∆f_CW=0.0007 result as the sole headline (drop everything else to an appendix) and propagate full multi-cell Bonferroni, or re-frame the paper as exploratory.

---

## MAJOR findings

### P5-M1. Abstract overstates "first/largest" without justification
The abstract describes the DESIVAST cross-check as the "largest matched-sample environmental-dependence test of spiral chirality in DESI DR1" (§VIII B). This is a tautological "largest of one" claim; no comparison sample exists because DESI DR1 chirality × environment is a new combination. Either give a benchmark or remove the superlative.

### P5-M2. Page length grossly excessive for a null result
20 pages, 11 figures/tables, 13 references, multiple appendices for a "no signal detected" paper. The body sells the absence of a phenomenon. PRD style demands compression: a null result with no theoretical predictor should be ≤ 8 pages including all secondary diagnostics, with the EFT toy mapping removed entirely (see P5-M4).
**Fix:** Recommend recasting as a Letter (~6 pp) or trimming the body to ≤ 10 pp with Tempel/ASTRA/T-Web overlays demoted to a supplement.

### P5-M3. Bright-vs-dark sign-flip is the most interesting result and is hidden
The 3.4σ filament bright-vs-dark sign-flip (abstract, §VI D ¶c) is a real residual—the authors say so—but it is dismissed as "BGS-selection-function-conditioned imaging-leg systematics" without quantitative model and without a clean reproduction in the cluster class (n too small). This is the only candidate signal in the data and it is not adequately tested.
**Fix:** Either test directly against an imaging-leg simulation/null, or honestly elevate to "tentative residual; null elsewhere; requires DR2 confirmation."

### P5-M4. Appendix A toy EFT mapping should be removed
**Appendix A, p. 19.** Authors admit (i) the operator is "not contained in either Alexander & Yunes [1] or Lue–Wang–Kamionkowski [2]", (ii) it breaks rotational invariance, (iii) it is not gauge-invariant, (iv) the bound is "order-of-magnitude only, not a quantitative ALP-coupling exclusion." This is a non-result presented as if it were a constraint. PRD will not benefit from publishing a self-admittedly invalid EFT toy.
**Fix:** Delete Appendix A; the paper is a measurement paper, not an EFT paper.

### P5-M5. RSD treatment is hand-waved
**Section XIII, p. 18.** Authors describe RSD as "sub-dominant" via a scalar σ_v/(aH) ≲ 5 Mpc/h argument, then admit (correctly) the dominant effect is anisotropic eigenvalue deformation, then defer the reconstructed-position rerun. For a V-Web tidal-tensor classification this is an unresolved systematic; the paper should either run reconstruction or quantify the boundary-flip fraction directly (estimated at "~3–5%") and propagate.
**Fix:** Either run the Zel'dovich reconstruction or quote a hard ∆f_CW per-class upper bound derived from the 3–5% boundary-flip estimate.

### P5-M6. ASTRA and V-Web disagree on per-galaxy labels but agreement is asserted
**Section X, p. 16.** ASTRA argmax classifies 25,186 EDR-overlap spirals as 11.9/31.7/35.2/21.3% void/sheet/filament/knot; V-Web on the same galaxies returns essentially 31.7%/68.3% filament/cluster with "only 3 spirals total in V-Web void + wall." The claim "both classifiers reach the same conclusion" is misleading: when one classifier's "void" class is empirically the *other classifier's* "filament/cluster" class, the null is not a real cross-validation, it is a tautological "no signal under any of three labelings of the same data."
**Fix:** Drop the ASTRA section, or honestly report it as confirming that the null is insensitive to label permutation, not as classifier cross-validation.

### P5-M7. Tempel cross-validation framed as confirming but secretly fails
**Section IX A, Table XI, p. 14.** Tempel "isolated" σ = −2.54, which the paper calls "formally just crossing the Bonferroni-4 |σ| = 2.498 threshold at α = 0.05 by 0.04σ but well below … |σ|^Bonf_0.01,4 = 3.02." The α=0.05 test fails. The paper then ignores this and concentrates on the 0.026-pp filament concordance. This is selective reporting.
**Fix:** Acknowledge that the Tempel scan formally exceeds α=0.05 Bonferroni in the isolated class.

### P5-M8. Figure 5 heat-map and Fig. 1 pie chart are filler
**Figs. 1, 5.** Fig. 1 is a 4-slice pie chart of volume fractions reported numerically in the same paragraph. Fig. 5 is a 3×3 heat-map of numbers already in Table VI. Neither figure conveys information beyond the tables. PRD discourages decorative figures.

### P5-M9. Figure 6 axis labels are non-standard
**Fig. 6, p. 14.** The Mollweide projection axes are labeled "0.0–1.0" rather than RA/Dec. The colorbar legend overlaps with the title in the top panel. Caption claims 885 occupied pixels in top, 1,496 valid in bottom, 727 in correlation — these three need a Venn-diagram reconciliation in the caption.

### P5-M10. Reference [3] (Paper IV) has duplicate phrase
**Ref. [3], p. 20.** "companion paper (Paper IV), in preparation; manuscript in preparation." Duplicate.

---

## MINOR findings

### P5-N1. "BAMfai/galaxy-chirality-catalog" is referenced but not formally cited as a data product
**§II, p. 2 and Appendix B.** A HuggingFace repository is not a publication. Either cite a Zenodo DOI with a fixed version, or label as "in preparation, see Paper IV."

### P5-N2. Inconsistent treatment of fCW digits
fCW values are sometimes 4-decimal (0.4980), sometimes 5-decimal (0.49718), sometimes 3-decimal (0.484). Standardize.

### P5-N3. "k= 0", "p= 0.372", "n= 428" formatting
Throughout: spaces around "=" are inconsistent (no-space then space). LaTeX formatting issue.

### P5-N4. "Filament + cluster" volume fraction claim
**Fig. 1 caption.** "wall+filament fraction (74.5%) dominates" — sum is 0.413 + 0.333 = 0.746 = 74.6% not 74.5%. Round consistently.

### P5-N5. "1.98 percentage points" range
**Table II "range" row.** 0.5034 − 0.4836 = 0.0198. The "range" row should explicitly show what is being differenced; currently the row reads "0.0198" without a column header that says "max − min."

### P5-N6. Reference [11] arXiv ID
arXiv:2604.02463 — if "2604" denotes 2026 April, this is consistent with the "Dated: June 2026" cover, but the date format follows the YYMM convention only ambiguously. Verify the arXiv identifier exists.

### P5-N7. "Hahn 2007 recipe, sometimes called the T-Web variant"
Footnote a (p. 2): authors use "T-Web recipe" then call it "V-Web" for "backward compatibility." This will confuse readers; standard nomenclature distinguishes T-Web (tidal) from V-Web (velocity-shear, Hoffman 2012) and they are not interchangeable. Pick one name and use it consistently. **Recommend "T-Web" since that is the actual algorithm used.**

### P5-N8. Per-quintile residual table III: arithmetic check
Quintile 1: f_CW = 0.4976, N = 158,327, σ_obs = (0.4976−0.5)·2·√158,327 = −0.0024·795.8 = −1.91 (paper says −1.94, ok rounding). Quintile 5: f_CW = 0.4985, σ_obs = −1.16 (computed: −0.0015·795.8 = −1.19). Mild rounding inconsistencies throughout. Tighten the table to consistent precision.

### P5-N9. P5 catalog monopole and Paper IV monopole inconsistency
**§VIII F.** Paper IV monopole = 0.4974; P5 catalog monopole = 0.4972. The authors attribute the 8% enhancement to BGS-bright selection. This is plausible but ad hoc; should be either tested or absorbed into the uncertainty budget.

### P5-N10. "21,158-row excess (2.7%)" defined twice
The same explanation appears as a parenthetical in §VIII F and again as a footnote-like aside; consolidate.

### P5-N11. Abstract sentence length
First sentence of the abstract is ~120 words. Compress.

### P5-N12. Number sometimes given as "n = " sometimes "N = "
Italicization and capitalization of sample sizes is inconsistent.

---

## Recompute audit (load-bearing scalars)

| Quantity | Quoted | Recomputed | Pass? |
|---|---|---|---|
| f_CW filament | 0.4980 | 203,261/408,187 = 0.49796 | ✓ |
| f_CW cluster | 0.4963 | 197,284/397,505 = 0.49631 | ✓ |
| σ filament | −2.61 | (203,261−204,093.5)/(0.5·638.9) = −2.61 | ✓ |
| σ cluster | −4.66 | (197,284−198,752.5)/(0.5·630.5) = −4.66 | ✓ |
| σ_pred filament | −3.16 | 2·0.0026·√408,187 = **−3.32** | **✗** (P5-E4) |
| Range across V-Web classes | 1.98 pp | 0.5034−0.4836 = 0.0198 | ✓ |
| Per-class CW sum | implied 393,592 | 207+3,359+203,261+197,284 = **404,111** | **✗** (P5-E1) |
| Per-class N sum | implied 791,635 | 428+6,673+408,187+397,505 = **812,793** | **✗** (P5-E1) |
| Filament bright + dark | should be ≤ 408,187 | 416,701 + 21,203 = **437,904** | **✗** (P5-E2) |
| Total dark | 14,782 (abstract) | filament dark 21,203 + cluster dark 4,234 alone = **25,437** | **✗** (P5-E2) |
| ∆f_CW VoidFinder | +0.0007 | 0.4971 − 0.4964 = 0.0007 | ✓ |
| Tempel filament concordance | 0.026 pp | |0.4982−0.4980| = 0.0002 = 0.02 pp | ≈ ✓ |
| DESIVAST V2-REVOLVER void count | 420 (§VIII) / 1,992 (§VIII C) | conflict | **✗** (P5-E5) |

---

## Summary recommendation

**REJECT**

This paper cannot be accepted in its present form. The arithmetic of its tracer-program decomposition is internally impossible (P5-E2: filament bright + dark exceeds filament total; cluster + filament dark exceeds total dark). The headline table and Figure 2 are reported on a 2.7%-larger sample than the abstract claims (P5-E1). The σ_pred reference value for the filament class is mis-computed (P5-E4). The DESIVAST void counts contradict between two sections (P5-E5). The entire interpretive scaffolding depends on an unpublished, non-peer-reviewed companion "Paper IV" whose ∆f_CW = −0.0026 monopole is treated as established truth (P5-E3). The paper acknowledges no pre-registration (P5-E6) yet declares a post-hoc "primary" path. The result itself is a null with no theoretical motivation, presented at 20 pages with a self-invalidating EFT toy in the appendix (P5-M4). Even after fixing the arithmetic, the appropriate venue is at best a ≤ 8-page focused null, after Paper IV is published and a pre-registered primary statistic is adopted; PRD's threshold for null results with no theoretical predictor is high, and this manuscript does not meet it.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional findings on fresh re-read

## ESSENTIAL findings

### P5-E7. Section VII reports n = 3,696,152 for a single Phase 2 cell, which exceeds the entire matched-spiral sample
**§VII, p. 8.** "The largest single-cell |σ_from half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152)." But σ_from_half requires CW/CCW labels, which exist only for the **791,635** chirality-relevant matched spirals (or 812,793 in the relaxed superset, per P5-E1). A filament class with n ≈ 3.7M is **4.5× larger than the entire matched chirality sample** and is physically impossible.

The paper then uses σ_pred = 2·∆f_CW·√N = 2·0.0026·√(3,696,152) ≈ -10 to argue "matches observed −11.3 within order unity." But the order-unity match is itself a downstream consequence of the wrong N: with N = 3,696,152 one expects σ_pred ≈ -10 from the monopole; with a physically possible N ≤ 812,793, one would expect σ_pred ≈ -4.7. The headline robustness statement of the entire Phase 2 sweep therefore rests on a number that cannot be true under the stated method.

**Fix:** Either (i) explicitly state which sample the n=3,696,152 is drawn from (the 14.6M V-Web parent, which has no chirality labels — making σ_from_half undefined), or (ii) recompute σ on the chirality-relevant matched sample at the (Rs=10, λth=0) cell and report the actual N consistent with the headline 791,635-spiral budget. As written, this is either a sample-mixing error or a typo and the Phase 2 sweep claim is unverifiable.

---

## MAJOR findings

### P5-M11. Bonferroni threshold values are numerically wrong in multiple places
**§V, §V B, §VII A.** Eq. (2), |σ|^Bonf_α,K = √2·erfc⁻¹(α/K), is correct for two-sided Bonferroni. But the numerical instantiations are inconsistent:

| Quoted location | Quoted threshold | Recomputed from Eq. (2) | Status |
|---|---|---|---|
| §V K=5 α=0.01 | 3.09 | 3.090 | ✓ |
| §V K=1054 α=0.05 | 4.05 | 4.077 | ✓ |
| §V B K=5 α=0.05 | **2.81** | **2.576** | ✗ |
| §VII A K=9 α=0.05 | **3.02** | **2.773** | ✗ |
| §IX A K=4 α=0.05 | 2.498 | 2.498 | ✓ |
| §IX A K=4 α=0.01 | 3.02 | 3.023 | ✓ |

The 2.81 value at K=5, α=0.05 corresponds instead to plugging α/(2K) into the formula (a one-sided/two-sided confusion that effectively halves the α budget); the 3.02 value at K=9, α=0.05 appears to be copy-pasted from the K=4, α=0.01 value used elsewhere in the paper. In neither case does the wrong threshold change the qualitative conclusion (no DESIVAST estimator crosses 2.576, and no Phase 2 cell crosses 2.77), but **the headline multiplicity-control claim of §V B is stated against an over-conservative threshold and the §VII A claim is stated against a non-existent one**.

**Fix:** Recompute and report 2.576 and 2.773 with consistent two-sided convention; verify all other Bonferroni numerics with a sanity-check script in the companion repository.

### P5-M12. NSIDE=32 valid-pixel counts disagree between Table V, §VIII F, and Fig. 6
**§VI E (Table V), §VIII F, Fig. 6 caption.** At NSIDE=32 on the matched-spiral catalog:

- Table V: n_pix = **3,303** (chirality-relevant matched-spiral sample)
- §VIII F: σ_vs_monopole distribution "across the **1,821** valid pixels"
- Fig. 6 (top): **885** occupied pixels (DESIVAST maximal voids)
- Fig. 6 (bottom): **1,496** valid pixels (z ≤ 0.24, ≥ 200 spirals/pix)
- Fig. 6 (Pearson): **727** pixels (both ≥ 200 spirals and ≥ 1 maximal void)

The 3,303 → 1,821 reduction between Table V and §VIII F is unexplained. The reader cannot tell whether the 1,821-pixel distribution moments (mean +0.020, std 1.184, skewness +0.044, kurtosis +0.825) used to argue "consistent with a pure shot-noise residual around the P4-monopole" are computed on the correct base sample. If 1,821 reflects a per-pixel spiral-count threshold, that threshold should be stated; if it reflects a footprint-mask, the mask should be cross-referenced to Fig. 4 (which is also NSIDE=32 and shows 3,303).

**Fix:** State the selection cut explicitly at each pixel count, or reconcile to a single canonical value.

### P5-M13. The σ_pred = −3.16 for filament is a stale number traceable to an older N or ∆f_CW
**§VI A, p. 6.** Beyond the simple arithmetic error noted in P5-E4: the value σ_pred = −3.16 corresponds either to N ≈ 369k (vs. the current 408,187) or to ∆f_CW ≈ −0.00247 (vs. the current −0.0026). Both are pre-update calibration values that would be present in an earlier draft. This is a load-bearing number used to argue "we interpret these as the global monopole leaking through the larger-sample bins, not as environment-dependent chirality" — a stale number underlying the entire physics interpretation of the headline result.

**Fix:** Recompute as −3.32 from the current sample, and verify no other σ_pred values in the paper (e.g., the Phase 2 sweep order-unity comparison, the density-quintile residual table) carry similar stale calibration.

### P5-M14. Abstract sentence "controlling void constraint comes from the DESIVAST-anchored re-projection (n = 56,981, ∆f_CW = 0.0007)" elides the asymmetry of sample sizes
**Abstract.** The DESIVAST void class (n=56,981) is compared to the non-void class (n=621,964), a 10.9:1 imbalance. The non-void class carries σ_non-void = −4.59 driven entirely by the P4 monopole at large N, and the void class carries σ_void = −1.71 which is also consistent with the same monopole at its N. The ∆f_CW = +0.0007 between the two is the residual after the catalog monopole subtracts identically from both classes. The abstract presents this as "statistically indistinguishable" without quantifying the **statistical power** of the test: with n_void = 56,981, the test can detect ∆f_CW differences down to ≈ 2/√56,981 ≈ 0.0084 at 2σ — so an environmental ∆f_CW signal of a few times 10⁻³ would not be excluded.

**Fix:** State the 2σ detection floor as the upper bound the test actually places, rather than asserting "statistically indistinguishable" as if no constraint were meaningful.

---

## MINOR findings

### P5-N13. Tracer-program σ values do not match the bright/dark joint-z formula
**§VI D ¶b and abstract.** Bright σ = −5.25 on n = 775,760, dark σ = +1.25 on n = 14,782 (per-class). The abstract claims a joint two-sample z-test gives |z| ≈ 3.4σ on the filament class. With independent two-sample-z, |z| = (σ_b/√(n_b/N_total) − σ_d/√(n_d/N_total))/√2 in some normalizations, but the precise value cannot be reconstructed from the displayed numbers because the filament-class n_bright (416,701) and n_dark (21,203) violate the conservation constraints (P5-E2). The 3.4σ value is therefore uncheckable from the paper's own arithmetic.

### P5-N14. Eq. (2) formula notation vs. instantiation inconsistency
**§V.** Eq. (2) uses erfc⁻¹(α/K) as the two-sided Bonferroni; the K=5 α=0.05 instantiation (P5-M11) effectively uses erfc⁻¹(α/(2K)). The reader cannot tell which convention is intended without recomputing. Add an explicit "two-sided" annotation and verify all instantiations agree.

### P5-N15. n_pix = 297 occupied DESIVAST voids per pixel vs. 885 in Fig. 6
**§VIII E, Fig. 6.** §VIII E: "Binning the maximal voids by HEALPix NSIDE = 16 pixel returns 297 occupied pixels." Fig. 6 top panel caption: "HEALPix NSIDE = 32 ... 885 occupied pixels (median 4 voids/pix)." Note: NSIDE=16 has 3,072 pixels; NSIDE=32 has 12,288. Going from NSIDE=16 (297 occupied) to NSIDE=32 (885 occupied) implies ~3× expansion. With 3,765 maximal voids: 3,765/297 = 12.7 at NSIDE=16 (paper says "median 14"); 3,765/885 = 4.25 at NSIDE=32 (Fig. 6 says "median 4"). Both internally consistent, but §VIII E uses NSIDE=16 for the stratification while §VIII F and Fig. 6 use NSIDE=32 for the Pearson correlation — the analysis uses different binning resolutions without flagging that the two stratifications cannot be cross-walked.

### P5-N16. Abstract "0.0022" vs body "0.22 pp"
**Abstract.** "max 0.0022 at Rs = 25, λth = 0.3" — written without explicit units. Reader must infer "fraction" not "pp." Table VI lists "0.220" in column header "fCW range (pp)." Standardize: either "max ∆f_CW = 0.0022" or "max 0.22 pp" — not both.

### P5-N17. ∆f_CW VoidFinder sign convention is ambiguous
**Table VIII.** ∆f_CW column gives +0.0007 for VoidFinder (where f_void = 0.4964 < f_non-void = 0.4971), −0.0019 for V2-REVOLVER (where f_void = 0.4986 > f_non-void = 0.4967), −0.0001 for V2-VIDE. The sign convention used appears to be ∆f_CW = f_non-void − f_void, which is non-obvious and not stated in the table caption.

### P5-N18. "Bonferroni-9 (α = 0.05) threshold |σ|^Bonf_0.05,9 ≈ 3.02" appears to be a copy-paste from §IX A
**§VII A vs §IX A.** The value 3.02 is the correct K=4, α=0.01 threshold used in §IX A (Tempel cross-validation). Its appearance verbatim in §VII A as the K=9, α=0.05 threshold suggests copy-paste error from the Tempel section. Recompute and replace with 2.77.

### P5-N19. Equation (1) σ_pred convention
**§V Eq. (1).** σ_pred = ∆f_CW / (0.5/√N) = 2·∆f_CW·√N. With ∆f_CW = −0.0026 (negative), σ_pred is negative — but the formula is presented as if it should yield a magnitude. State explicitly that σ_pred inherits the sign of ∆f_CW, so the comparison |σ_obs − σ_pred| properly accounts for sign agreement.

### P5-N20. §VIII E "297 occupied pixels with median 14 maximal voids per occupied pixel"
**§VIII E.** Mean = 3,765/297 = 12.68. Median "14" is plausible for a right-skewed distribution but the claim should be verified or labelled as such. (Minor; just unusual that median > mean for a count distribution).

---

## Summary of fresh-eyes additions

The most consequential new findings are **P5-E7** (the n=3,696,152 in §VII that cannot be a chirality-labeled sample) and **P5-M11** (Bonferroni thresholds wrong in §V B and §VII A by ~10–30%). The 3,696,152 issue in particular undermines the load-bearing "order-unity match" interpretation of the Phase 2 largest-σ cell, which is one of the paper's three pillars (alongside DESIVAST primary and Phase 2 max-range). The Bonferroni errors do not change qualitative conclusions but they reveal that the multiplicity-control numerics were not independently verified — which, combined with the absence of pre-registration (P5-E6) and the arithmetic-impossible tracer-program decomposition (P5-E2), substantially weakens the methodological credibility of the paper. **My reject recommendation strengthens.**