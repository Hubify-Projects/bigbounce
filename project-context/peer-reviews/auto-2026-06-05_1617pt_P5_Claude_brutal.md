# P5 auto-2026-06-05_1617pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11595 chars)
**Wall time**: 385.0s

---

# Referee Report: P5 — Environmental Dependence of Spiral Chirality

**Manuscript:** "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"
**Target journal:** Physical Review D
**Reviewer stance:** Brutal honesty, hard PRD bar.

---

## Overview assessment

This is a 20-page manuscript reporting a null detection of environment-dependent spiral chirality, anchored on a chirality catalog from an unpublished companion paper ("Paper IV"). The central claim — that CW fraction is statistically independent of environment — is bounded by ∼0.2 pp at high-n classes and by counting noise at low-n. The methodology (V-Web on DESI DR1, DESIVAST cross-check, Tempel and ASTRA cross-validations) is competently executed. However, the paper has serious structural problems for a PRD submission: (i) the load-bearing input (Paper IV) is unpublished and not peer-reviewed, (ii) the paper is dramatically over-length for a null result, (iii) the abstract makes statements not supported in the body, (iv) several σ values do not survive arithmetic recomputation, (v) the "primary vs secondary" distinction is admittedly post-hoc, and (vi) the Appendix A toy EFT mapping is so heavily caveated as to be substanceless.

---

## ESSENTIAL findings

### P5-E1 — Load-bearing dependence on unpublished, non-peer-reviewed companion work
**Section II, p. 2; Refs [3], [4]:** The entire chirality catalog, the monopole offset ΔfCW = −0.0026 used as the primary subtraction throughout, the dipole nulls, and the systematics characterization are all imported from "Paper IV [3]", which is described as "in preparation; manuscript in preparation" and "not yet peer-reviewed". Paper II [4] is in the same state. Every headline σ in this manuscript depends on the catalog being correct and the monopole being characterized as quoted. **This is not acceptable for PRD.** PRD does not accept papers whose central data product and central systematic-correction value come from an unpublished, unrefereed, in-preparation companion. The manuscript must either (a) wait until Paper IV is submitted, posted on arXiv, and made publicly auditable (minimum), or (b) re-derive the catalog-monopole offset internally to this paper with full documentation. Currently the manuscript is unreviewable as a standalone document.

### P5-E2 — Abstract σ values inconsistent with body
**Abstract, p. 1, vs Table II, p. 5.** The abstract reports:
- filament σ = −2.61 at n = 408,187
- cluster σ = −4.66 at n = 397,505

Recomputing from Table II: filament fCW = 0.4980, n = 408,187 → σ = (203,261 − 204,093.5)/√(0.25·408,187) = −832.5/319.6 = **−2.61** ✓
Cluster fCW = 0.4963, n = 397,505 → σ = (197,284 − 198,752.5)/√(99,376.25) = −1468.5/315.24 = **−4.66** ✓
OK on those two. But:
- Abstract says wall σ = +0.55 at n = 6,673 with fCW = 0.5034. Recompute: nCW = 3359, n/2 = 3336.5, σ = 22.5/40.84 = **+0.551** ✓
- Void σ = −0.68 at n = 428, fCW = 0.4836. Recompute: nCW = 207, n/2 = 214, σ = −7/10.34 = **−0.677** ✓

So the headline table is internally arithmetically consistent. However:

**Abstract claims** "filament-class concordance 0.026 pp" for Tempel. Body (§IX A, p. 14) gives V-Web filament 0.4980 vs Tempel filament_like 0.4982 → difference = 0.0002 = 0.02 pp, which rounds to 0.02 pp, not 0.026 pp. The "0.026 pp" figure is also quoted in Fig. 7 caption. This is a self-consistent claim across body/caption but the displayed decimals only support 0.02 pp. Either provide more decimal places or correct to 0.02 pp.

### P5-E3 — Abstract "−0.24 near-perfect null on n = 86,276" vs body n = 86,276 in §VIII D but Table VIII reports V2-REVOLVER n = 102,911
**Abstract, p. 1 vs Table VIII, p. 12 vs §VIII D, p. 11.** The abstract says V2-REVOLVER catalog-native returns σ = −0.24 on n = 86,276. §VIII D says the same: "V2-REVOLVER nvoid = 86,276, fCW^void = 0.4996, σ^void = −0.24". Table VIII, however, lists V2-REVOLVER nvoid = 102,911 with fCW = 0.4986 and σ = −0.88. These are described as two different definitions (sphere-approximation vs catalog-native GALZONE) but the abstract conflates them with a phrase that reads as if 86,276 is the only V2-REVOLVER number. Recompute σ for n = 86,276, fCW = 0.4996: σ = (0.4996 − 0.5) · 2 · √86,276 = −0.0004 · 587.5 = **−0.235** ✓. OK. But the abstract phrasing must be disambiguated, and the apparent jump between sphere (n = 102,911) and catalog-native (n = 86,276) needs unambiguous accounting: ∼16,635 galaxies have moved between categories with no explanation of the OUT/EDGE flag accounting.

### P5-E4 — "Joint two-sample z-test |z| ≈ 3.4σ" not derived or shown
**Abstract, p. 2 and §VI D, p. 8.** The abstract states "The joint two-sample z-test on the bright-vs-dark fCW difference is |z| ≈ 3.4σ on the filament class". Body (§VI D) gives bright n=416,701 σ=−2.80 and dark n=21,203 σ=+2.85. A two-sample z-test for the difference of two binomial proportions under H0: p1=p2 gives z = (p̂1 − p̂2)/√(p̂(1−p̂)(1/n1+1/n2)). The body never displays the underlying fCW values for filament-bright and filament-dark (only the σ-from-half values, which constrain (p − 0.5) but not (p1 − p2) directly without a sign+magnitude reconstruction). Recompute: p1 ≈ 0.5 − 2.80/(2√416,701) = 0.5 − 0.002168 = 0.497832; p2 ≈ 0.5 + 2.85/(2√21,203) = 0.5 + 0.009787 = 0.509787. Δp = −0.011955. SE ≈ √(0.25·(1/416,701 + 1/21,203)) = √(2.40e-6 + 1.18e-5) = √(1.42e-5) = 3.77e-3. z = −0.01196/3.77e-3 = **−3.17σ**, not 3.4σ. Close but not matching; the discrepancy may come from pooled-variance vs unpooled. Either show the calculation or correct the value. Given the importance of the bright-vs-dark sign-flip discussion (the largest single residual structure flagged in the paper), this must be made auditable.

### P5-E5 — "max class-to-overall bright-fraction deviation 1.5 pp" inconsistent with displayed ratios
**Abstract, p. 2 and §VI D, p. 8.** Body gives bright/(bright+dark) ratios {0.981, 0.962, 0.966, 0.989} vs overall 0.978. Max deviations: |0.989 − 0.978| = 0.011 = 1.1 pp; |0.962 − 0.978| = 0.016 = 1.6 pp. The "1.5 pp" abstract figure is approximately correct but neither matches the 1.1 nor the 1.6 pp computed from displayed numbers. Either give the actual max (1.6 pp) or display more precise ratios.

### P5-E6 — Density-quintile σpred computation error
**§VI C, p. 6.** Text says "at N = 158,327 per quintile the predicted |σpred| = 2 · |−0.0026| · √158,327 ≈ 2.07". Recompute: 2·0.0026·√158,327 = 0.0052 · 397.9 = **2.069 ✓**. OK that's correct. But §V Eq. (1) defines σpred = ΔfCW/(0.5/√N) = 2·ΔfCW·√N, so for negative ΔfCW the sign is negative. The body uses σpred = −2.07 in Table III (correct), but the inline text drops the sign. Minor inconsistency. **However:** the Bonferroni-5 threshold is given as |σ|Bonf_0.01,5 ≈ 3.09. Recompute: √2 · erfc⁻¹(0.01/5) = √2 · erfc⁻¹(0.002). erfc⁻¹(0.002) corresponds to z such that 2Φ(−z) = 0.002 → Φ(−z) = 0.001 → z ≈ 3.090. **OK ✓**. Note: this is the two-tailed per-test threshold for K=5 at family α=0.01. Correct.

The Bonferroni for NSIDE-16 HEALPix (K=1054) at α=0.05: √2 · erfc⁻¹(0.05/1054) = √2·erfc⁻¹(4.74e-5). z ≈ 4.07. Paper says **4.05**. Close enough but verify.

### P5-E7 — Mixing of σ scales for "not directly comparable" tests
Per review instruction 7. The paper repeatedly juxtaposes σfrom_half (binomial deviation from 0.5), σpred (catalog-monopole prediction), σvs_monopole (residual after monopole subtraction), and σ from look-elsewhere max-stat null distributions, **without consistent labeling at each juxtaposition**. Examples:
- Table II reports σfrom_half, but the abstract reads "filament: −2.61σ" without specifying that this is σfrom_half not σvs_monopole.
- §VI A says the filament σ "tracks the catalog-wide classifier-monopole offset" and gives σpred values, then in the next paragraph quotes σ = −0.68 for void without specifying that this is σfrom_half not σvs_monopole.
- §VIII E reports σ = −4.75 in the "0 maximal voids" bin and then says "the Paper IV monopole prediction at N = 378,511 is σpred = −3.20; the observed −4.75σ leaves a residual of −1.55σ". This is the correct labeling, but earlier tables (II, III, V, VIII) lack it.

This is a PRD-essential clarity issue. Every σ in the paper must be labeled with its scale, and any juxtaposition of σ values from different scales must carry "not directly comparable" at the point of juxtaposition.

### P5-E8 — Length vs content
The paper is 20 pages for a **null result** with one primary measurement (DESIVAST ΔfCW = 0.0007, n = 56,981) and one secondary supporting measurement (V-Web). The Phase 2 sensitivity sweep, the multiple sub-stratifications (z-quartile × density-quartile × tracer-program), the ASTRA EDR cross-check, the Tempel cross-check, and the Appendix A toy EFT mapping are all extended diagnostic checks, none of which independently change the headline. A PRD Letter (4 pages) or a focused PRD article (≤ 10 pages) would be appropriate. **Recommended max for a PRD article: 8 pages including refs.** Cut the Appendix A, the ASTRA EDR section, the maximal-void HEALPix stratification, the within-class density-stratified follow-up, and most of the Phase 2 prose. Move to companion data release.

### P5-E9 — Primary/secondary distinction is post-hoc by author admission
**§V B, p. 4–5.** The text explicitly states: "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc". For a paper anchored on a **null detection**, the post-hoc selection of which classifier defines "primary" is a serious garden-of-forking-paths problem that the disclosure does not resolve — it only documents. With ≥5 environment classifiers × multiple stratifications, the look-elsewhere correction across the full analysis tree is not done. The DESIVAST primary path itself involves ≥5 estimators, only crudely Bonferroni-corrected. The paper should either (a) report the headline as "consistent with monopole-only across all classifiers tested" without any primary/secondary designation, or (b) actually pre-register a follow-up with DR2.

---

## MAJOR findings

### P5-M1 — Appendix A toy EFT mapping should be removed
**Appendix A, p. 19.** The author admits the operator is "not contained in either" of the two cited references, that the operator is not rotationally invariant as written, not gauge invariant, and that "a real exclusion would require (i) a full transfer-function calculation… and (ii) propagation of the per-class ΔfCW measurement uncertainties through that transfer function. We do not claim either calculation here." This appendix has no scientific content beyond the disclaimers. It does not constrain any model. It should be deleted; the bound is already adequately stated as |ΔfCW| < 0.01 per class.

### P5-M2 — Headline statistical floor numerically incoherent in abstract
**Abstract, p. 1.** Abstract states "the sensitivity floor set by the Paper IV catalog-monopole offset of ∼0.2 pp (systematic-dominated for V-Web filament/cluster at n ≳ 4 × 10⁵) and by counting statistics of ∼5 pp (statistical-dominated for V-Web void at n = 428, ∼2σ on the binomial null)". The 5 pp counting-floor at n=428 corresponds to 1σ ≈ 1/(2√428) = 0.024 = 2.4 pp, so the "5 pp" is roughly 2σ. The text then says "∼2σ on the binomial null", which is consistent. But the abstract claim that the void floor is 5 pp is in tension with the fact that the actual void deviation is fCW = 0.4836 − 0.5 = −1.64 pp, well inside that floor. The "5 pp" framing oversells the constraining power. State the 1σ floor (2.4 pp) for honesty.

### P5-M3 — RSD treatment for V-Web is hand-waved
**§XIII (Limitations), p. 18 and §VIII intro, p. 10.** The author acknowledges that V-Web positions are in redshift space, and that "the anisotropic eigenvalue deformation above is the dominant channel and is not separable from the sweep-induced shift without a reconstructed-position rerun". The paper then "explicitly do[es] not quantify the propagated uncertainty in the present paper". For a methods paper claiming 0.22 pp sensitivity at the Phase 2 sweep level, an unquantified anisotropic RSD systematic of order the sensitivity is a serious limitation. The DESIVAST path is RSD-immune as the author argues, but then the V-Web result becomes mere supplementary check — which contradicts the manuscript title's prominent display of "V-Web Cross-Check Across 791,635 DR1 Matched Spirals". Either run the reconstructed-position re-classification or downgrade V-Web in the title and abstract.

### P5-M4 — Tempel cross-validation has known sample mismatch
**§IX A, p. 13–14.** Tempel covers SDSS DR10, z ≤ 0.20; multiplicity classes are richness-based, not tidal-tensor. The "concordance" comparison maps multiplicity ≥ 20 to V-Web cluster (λ-threshold > 0 in three dimensions). These are not the same physical object. The 0.026 pp filament/filament_like agreement is the comparison of two CW fractions that both sit near the global classifier monopole and that the author already acknowledges are independently constrained to be close to 0.4974 by the catalog-monopole offset. The Tempel "cross-validation" is therefore tautological at the precision the paper claims: both classifiers necessarily return ≈ 0.4974 because both samples inherit the same per-galaxy chirality labels. This is not independent confirmation of the environment-independence statement; it is a re-projection of the same data. State this honestly.

### P5-M5 — ASTRA EDR cross-check is null because of small overlap, but presented as validation
**§X, p. 16–17.** The author admits: "the EDR-overlap subsample falls disproportionately on cells where the edge-density mask suppresses the V-Web void class" and "V-Web and ASTRA argmax disagree strongly on per-galaxy environment labels on this overlap". The two classifiers return the same null on the same galaxies — but because n = 25,186 and the per-class fCW is constrained near 0.4974 by the catalog monopole, the agreement is forced by the chirality-side bias, not by environment classifier agreement. The author partially acknowledges this in the final paragraph of §X. But the headline framing "a strong robustness result" overclaims. Soften.

### P5-M6 — Self-grading language: "strongest single residual structure", "cleanest single chirality-in-voids measurement"
Multiple instances of author self-grading the relative importance of his own findings ("strongest", "cleanest", "load-bearing"). PRD style is neutral. Remove or replace with quantitative statements.

### P5-M7 — Reference [11] and [12] arXiv IDs are future-dated
**Refs [11], [12], p. 20.** Listed as arXiv:2604.02463 and arXiv:2604.01456 with year 2026. arXiv IDs of the form YYMM.NNNNN with YY=26 imply 2026, and MM=04 implies April 2026. The manuscript is dated June 4, 2026. These references are plausibly real but the reviewer cannot verify them; the cited paper for Ref [11] is described as "currently in submission to MNRAS" — non-peer-reviewed. Treating an in-submission MNRAS preprint as "concurrent literature overlay" load-bearing for the V-Web vs T-Web comparison is borderline. Verify these refs and clearly mark them as preprints.

### P5-M8 — "Most rigorous, largest" framing not supported
**§VIII B, p. 11.** "This DESIVAST-anchored re-analysis is the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date". This is a claim about literature — what is the comparison baseline? Shamir 2022 (cited) used 1.3M galaxies but with Ganalyzer, not on DESI DR1 specifically. Without an actual literature audit, "largest" is unsupported. Remove or document.

### P5-M9 — Table VIII σ values not arithmetically reproducible
**Table VIII, p. 12.** V2-VIDE row: nvoid = 81,354, fCW = 0.4971. Recompute σ = (0.4971 − 0.5)·2·√81,354 = −0.0058 · 285.23 = **−1.65**. Table says −1.67. Close, but text mismatch — see also §VIII D which says "V2-VIDE catalog-native −1.06 vs sphere −1.67". The −1.67 appears in Table VIII for sphere, which is correct (close to −1.65 within rounding). VoidFinder row: n=56,981, fCW=0.4964, σ should be (0.4964−0.5)·2·√56,981 = −0.0072·477.4 = **−1.72**. Table says −1.71. Within rounding. OK.

V2-REVOLVER sphere: n=102,911, fCW=0.4986, σ = (0.4986−0.5)·2·√102,911 = −0.0028·641.6 = **−0.898**. Table says −0.88. OK within rounding.

Non-void rows: VoidFinder non-void n=621,964, fCW=0.4971, σ = (−0.0029)·2·√621,964 = −0.0058·788.6 = **−4.57**. Table says −4.59. OK within rounding.

These match. Note however that ΔfCW for VoidFinder row is +0.0007, but the sign convention is ambiguous: f_void − f_nonvoid = 0.4964 − 0.4971 = **−0.0007**, not +0.0007. The table is inconsistent on sign convention. Fix.

### P5-M10 — Equation (1) presentation is non-standard
**Eq. (1), p. 4.** σpred = ΔfCW/(0.5/√N) = 2·ΔfCW·√N. For ΔfCW = −0.0026 this gives a negative σpred, as the body sometimes uses. But the abstract and many tables drop the sign and write |σpred|. Standardize.

### P5-M11 — HEALPix permutation p-values (Table V) ordering
**Table V, p. 8.** NSIDE = 16 p = 0.607; NSIDE = 32 p = 0.135; NSIDE = 64 p = 0.413. The abstract lists "p = 0.61/0.135/0.413" — order matches. But the abstract also gives the first as p=0.61, which is "0.607" rounded — fine. No issue here, but verify Table V matches the abstract.

### P5-M12 — Within-class density quartile σ values in Table IV not consistent with quoted body text
**§VI D, Table IV, p. 6.** Cluster Q1 σ = −3.07 at n = 99,398, fCW unstated. Recompute the implied fCW: fCW = 0.5 + (−3.07)/(2√99,398) = 0.5 − 0.00487 = **0.49513**. The text says "the most-typical-cluster-density quartile Q3 (ρ̄ = 2.01, n = 99,526) returns σ = −0.37, statistically null after Bonferroni-4 correction." Recompute Q3: fCW = 0.5 − 0.37/(2√99,526) = 0.5 − 0.000587 = 0.499413. Both look fine. Recompute filament Q1: σ = −0.69 at n = 102,050 → fCW = 0.5 − 0.69/(2√102,050) = 0.5 − 0.00108 = 0.49892. OK.

The Bonferroni-4 threshold quoted as "|σ| = 2.50 at α = 0.05" — recompute: √2 · erfc⁻¹(0.05/4) = √2 · erfc⁻¹(0.0125) = √2 · 1.7665 = **2.498** ✓. OK.

The Bonferroni-4 threshold quoted as "|σ| = 3.02 at α = 0.01" — recompute: √2 · erfc⁻¹(0.01/4) = √2 · erfc⁻¹(0.0025) = √2 · 2.135 = **3.02** ✓. OK.

Numerically fine.

### P5-M13 — "Headline cosmic-web result" inconsistent with the post-hoc primary anchor
The Conclusions (§XV) and abstract repeatedly call the V-Web cosmic-web run "headline" and "the headline cosmic-web result". §V B explicitly designates DESIVAST as primary and V-Web as secondary. Within the same manuscript, two different sections claim "headline". Resolve.

---

## MINOR findings

### P5-m1 — Figure 4 caption gives p=0.135 from a label-shuffle null with NMC=1000
**Fig. 4 caption, p. 9.** p = 0.135 at NSIDE=32. The footprint mask shape is clearly visible (DESI N+S+DES patches). The Mollweide projection is acceptable. But the caption claims "high-|σ| pixels are isolated rather than clustered" — this is a visual assertion that should be quantified with a spatial-correlation statistic (e.g. Moran's I) or removed.

### P5-m2 — Figure 1 pie chart redundant with body text
The volume fractions {0.244, 0.413, 0.333, 0.010} are quoted verbatim in §IV B and again in Fig. 1. The pie chart adds nothing. Cut.

### P5-m3 — Figure 5 heat-map: max-range cell label collision
Fig. 5 shows "0.220" in the (Rs=25, λth=0.3) cell with text label apparently overlapping the colorbar tick. Layout issue.

### P5-m4 — Table I "Matched primary" before and after dedup
2,349,908 → 2,232,212 implies 117,696 duplicates (5.0%). Comment on what fraction of duplicates were genuine sky-coincidences vs. tractor reprocessing. Not critical.

### P5-m5 — Repeated phrasing "load-bearing"
"Load-bearing" appears ≥6 times in the body. The word is becoming a verbal tic. Trim.

### P5-m6 — Abstract repeats "consistent with parity at ∼1σ" indirectly
Abstract first paragraph and §I duplicate the framing. Tighten.

### P5-m7 — Repeated "supporting rather than load-bearing" phrasing
Abstract and §IX A use nearly identical phrasing. Consolidate.

### P5-m8 — Inconsistent decimals
fCW values quoted variously to 3 vs 4 vs 5 decimals (0.4974, 0.49719, 0.4970, 0.498). Standardize to 4.

### P5-m9 — "Pearson r = +0.006, p = 0.88" — n=727 pixel test
**Fig. 6 caption, p. 14.** A null correlation at n=727 with the catalog-monopole already accounted for is mildly informative but the figure caption framing as a "direct single-statistic confirmation" is over-strong. Soften.

### P5-m10 — Equation references missing in some places
"per Eq. (1), §V" appears but Eq. (3) is referenced without parenthesizing in §V A. Standardize.

### P5-m11 — Reference formatting
Ref [9] (Shamir 2022) cited as showing 2-4% asymmetry: actually Shamir's paper claims asymmetry at smaller amplitude in subsamples; check the quoted 2-4% against the cited paper's abstract.

### P5-m12 — Reproducibility checklist is sparse
"Single config file (available in companion data repository)" — the repository URL is never given. Provide DOI.

### P5-N1 — Title length
The title is 23 words. PRD prefers ≤ 15. Shorten.

### P5-N2 — Affiliation
"Independent Researcher, Los Angeles, California, USA" — fine but lacking an institutional ORCID or affiliation. PRD requires ORCID.

### P5-N3 — Date "(Dated: June 4, 2026)" on a 2026 manuscript: ensure the date is the submission date.

### P5-N4 — Reference [3] gives no arXiv ID — needed since this is the load-bearing companion.

---

## Items I checked and could NOT find problems with

- Table I row totals: CW + CCW + NS = 393,592 + 398,043 + 1,440,577 = 2,232,212 ✓
- Chirality-relevant = CW + CCW = 791,635 ✓
- Phase 2 sweep ranges in Table VI all ≤ 0.22 pp as claimed ✓
- Eq. (2) Bonferroni formula is dimensionally and numerically correct ✓
- The DESIVAST point-in-sphere test methodology is sound
- Volume fractions sum to 1.000 ✓
- V-Web computational steps (1)-(12) are standard

---

## Summary recommendation

**REJECT** (with option for major revision and resubmission after Paper IV is publicly posted/refereed)

The manuscript reports a competently executed null measurement of environment-dependent spiral chirality, but it is not acceptable for PRD in its current form for three independent reasons, any one of which is sufficient grounds for rejection: (1) the load-bearing chirality catalog and the central systematic-correction monopole ΔfCW = −0.0026 are imported from an unpublished, in-preparation companion paper that the reviewer cannot audit, making the present manuscript non-self-contained and unreviewable as a standalone document; (2) the paper is roughly 2-3× over-length for the actual content (one primary null at n=56,981 plus monopole-projection re-statements in N secondary classifiers), with an Appendix A toy EFT mapping that the author admits is neither rotationally nor gauge invariant and constrains nothing; and (3) the primary/secondary classifier designation is admittedly post-hoc, σ values from incompatible scales (σfrom_half, σpred, σvs_monopole, max-stat LEE) are juxtaposed throughout the abstract and tables without consistent labeling, the "joint z = 3.4σ" filament bright-vs-dark sign-flip does not reproduce from displayed numbers (I get 3.17σ), and the abstract overstates the constraining power of the void floor. Recommended path: (a) wait until Paper IV is on arXiv and accepted somewhere, (b) cut to ≤ 8 pages with DESIVAST as the only reported analysis path, (c) drop Appendix A, (d) fix all σ-scale labeling, and (e) re-derive the disputed joint z-test.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report (Second Pass): Additional Findings

After re-examining with fresh eyes, I find several significant issues the initial review missed. The most serious is a fundamental sample-size inconsistency that propagates throughout the paper.

---

## ESSENTIAL findings (new)

### P5-E10 — Headline sample size 791,635 is internally inconsistent with Table II (sums to 812,793)
**Abstract, §VI A, Table II, §VI D, Fig. 2 caption — pervasive.** The abstract states: "Per-class CW fractions on the 791,635 chirality-relevant spirals are... filament n=408,187... cluster n=397,505... wall n=6,673... void n=428". Sum: 408,187 + 397,505 + 6,673 + 428 = **812,793**, not 791,635. §VI A also claims "Table II reports CW fraction by cosmic-web class on the 791,635 chirality-relevant matched spirals" while the displayed n's sum to 812,793. Verifying via nCW: 207 + 3,359 + 203,261 + 197,284 = 404,111, which divided by 812,793 gives fCW = 0.49719 — consistent with the stated f^P5_CW = 0.4972. So **Table II is actually on 812,793, not on 791,635**. §VIII F obliquely acknowledges this with a buried footnote ("the 21,158-row excess (2.7%) over the 791,635-spiral headline subsample is the population of CW/CCW-labelled spirals whose V-Web env-class assignment passes the relaxed env-label confidence used by the cosmic-web pipeline but is excluded from the headline by a stricter env-class-uncertainty filter"). This is a **load-bearing labeling error**: the headline subsample changes between the chirality-relevant (791,635) and env-class-relaxed (812,793) definitions, and the paper conflates them throughout. Every σfrom_half in Table II is computed on the 812,793 superset but presented under the 791,635 headline. The 791,635 vs 812,793 distinction must be made explicit at every occurrence, and the abstract sentence must be rewritten.

### P5-E11 — Arithmetic error: σpred(filament) quoted as −3.16, true value is −3.32
**§VI A, p. 5.** Paper states "predicting σpred from ΔfCW = −0.0026 gives σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28". Recompute filament with the displayed n=408,187: σpred = 2·(−0.0026)·√408,187 = −0.0052·638.90 = **−3.32**, not −3.16. Cluster recompute: 2·(−0.0026)·√397,505 = −0.0052·630.48 = **−3.28** ✓. So **the filament σpred is arithmetically wrong by ~5%**. This matters because the body uses σpred(filament) = −3.16 to argue the observed −2.61σ is "within order-unity of observation" — with the correct −3.32, the observed −2.61 actually leaves a +0.71σ residual (a slight under-shoot of the monopole prediction), which is the opposite of what the body implies. The qualitative conclusion (monopole-consistent) holds, but the specific number is wrong.

### P5-E12 — Sign convention on Table VIII ΔfCW column is inverted for all three rows
**Table VIII, p. 12.** All three rows have ΔfCW with the wrong sign if the natural reading is f_void − f_non-void:
- VoidFinder: 0.4964 − 0.4971 = **−0.0007**, table says **+0.0007**
- V2-REVOLVER: 0.4986 − 0.4967 = **+0.0019**, table says **−0.0019**
- V2-VIDE: 0.4971 − 0.4970 = **+0.0001**, table says **−0.0001**

The table is internally consistent under the convention ΔfCW = f_non-void − f_void, but this is the unusual direction (the column header just reads "ΔfCW" without specifying which way). The abstract amplifies the error: "f^void_CW = 0.4964 vs f^non−void_CW = 0.4971, ΔfCW = 0.0007" — this is consistent with the table convention but inconsistent with the natural subscript convention. Initial review flagged VoidFinder; on second pass I confirm **all three rows are inverted relative to natural reading**. State the convention or fix the signs.

---

## MAJOR findings (new)

### P5-M14 — σvs_monopole pixel distribution std = 1.184 rejects unit variance at >10σ; paper waves it away
**§VIII F, p. 13.** "At the HEALPix-NSIDE-= 32 per-pixel level… the distribution of σvs_monopole across the 1,821 valid pixels has mean +0.020, std 1.184, skewness +0.044, and excess kurtosis +0.825. The unit standard deviation (within ∼18%, consistent with finite-pixel sample-size fluctuation)…". This dismissal is wrong. The sampling distribution of an empirical σ-distribution standard deviation under H0 (each σ ∼ N(0,1)) is approximately σ_std ≈ 1/√(2·N_pix) = 1/√3642 = 0.0166 for N=1821 pixels. Observed std = 1.184; deviation from 1.0 is 0.184, which is **0.184/0.0166 = 11.1σ**. Equivalently, χ² = 1820·1.184² = 2552 vs expected 1820 (std≈60), a **12σ excess**. This is a real over-dispersion that the analysis does not address. Possible sources: residual large-scale systematic the monopole subtraction doesn't remove, heteroscedasticity from per-pixel sample-size variation that should have been pre-whitened, or a real but spatially incoherent (no preferred sky direction) environment effect. The author cannot truthfully claim "consistent with a pure shot-noise residual around the P4-monopole" — the variance test rejects shot noise.

### P5-M15 — Body and abstract use two different monopole values (−0.0026 vs −0.0028) without consistent attribution
**§V Eq. (1) and §VIII F.** Eq. (1) and the density-quintile / Phase-2-sweep predictions use ΔfCW = −0.0026 (the Paper IV catalog value). §VIII F notes "the observed −5.00σ corresponds to ΔfCW^P5 ≈ −0.0028, ∼8% larger than the P4 catalog-mean", attributing the inflation to BGS-leg weighting. But the σpred values quoted throughout (§VI A: −3.16/−3.28; §VIII E: −3.20/−2.64; §VI C: −2.07) all use −0.0026. If the spectro-confirmed subsample has its own monopole of −0.0028, then all σpred predictions should be scaled up by ~8%. The corrected filament σpred at the correct ΔfCW^P5 = −0.0028 is 2·(−0.0028)·√408,187 = **−3.58**, compared to observed −2.61. The residual is +0.97σ, not within order-unity (as the body claims with −3.16). The choice of monopole value matters for the residual interpretation and is not consistently applied.

### P5-M16 — Phase 2 sweep "largest single-cell |σfrom_half| = 11.32" cell uses n=3,696,152 spirals but headline says ~800k
**§VII, p. 8.** "The largest single-cell |σfrom_half| across the entire sweep is 11.32 (filament at Rs=10, λth=0, n=3,696,152)". This n is ~4.7× the headline 791,635/812,793 sample. Where does the additional sample come from? The Phase 2 sweep should be applied to the same chirality-relevant matched-spiral catalog (where the per-galaxy CW/CCW labels exist), which is fixed at 791,635. The n=3,696,152 figure is unexplained — possibly the V-Web-relabeled full 14.6M parent catalog, but those galaxies have no chirality labels. If the sweep is reporting n_classified rather than n_chirality-labeled, the σ comparison to a chirality null is malformed. Document.

### P5-M17 — ASTRA distribution "31.7% sheet" coincidentally matches "V-Web filament 31.7%" — possible transcription error
**§X, p. 16–17.** "ASTRA argmax distributes the 25,186 spirals as 11.9% void / 31.7% sheet / 35.2% filament / 21.3% knot, while V-Web puts essentially the entire sample into filament (**31.7%**) and cluster (68.3%)". Two unrelated classifier classes reported as exactly 31.7%. With 4 significant figures, the probability of coincidence is ~10⁻³. Possibly real, possibly a copy-paste error where the ASTRA sheet fraction got written into the V-Web filament slot. Verify and recompute.

### P5-M18 — Fig. 1 caption "74.5%" vs "0.413 + 0.333 = 0.746 = 74.6%"
**Fig. 1 caption, p. 4.** "the wall+filament fraction (74.5%)" — sum from displayed Phase 1 volume fractions is 0.413 + 0.333 = 0.746 = 74.6%. Off by 0.1 pp; minor rounding error.

### P5-M19 — §VIII F "1,821 valid pixels" vs §VI E "3,303 NSIDE=32 pixels"
Two different pixel counts for NSIDE=32 quoted in adjacent sections. §VI E Table V says n_pix=3,303 for the full chirality-relevant sample. §VIII F says n=1,821 valid pixels for the σvs_monopole distribution. The distinction (likely a per-pixel minimum-N cut for stable fCW) is never spelled out. Explicit definition required.

---

## MINOR findings (new)

### P5-m7 — §VIII A claim "minimum spiral-to-nearest-hole separations span 28.7–158.1 Mpc/h" is presented as evidence of 0/6 disagreement
**§VIII A, p. 10.** Author writes that minimum distances span 28.7–158.1 Mpc/h "consistent with… 0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes". The point-in-sphere test is the binding statement (0/6); the 28.7 Mpc/h minimum is shown to be larger than the maximum hole radius 24 Mpc/h (mentioned earlier). Fine, but write the bound explicitly: "28.7 Mpc/h minimum spiral-to-center distance exceeds the 24 Mpc/h maximum hole radius, confirming the point-in-sphere result is not sensitive to spatial-precision tolerance."

### P5-m8 — "−0.135 null verdict" — Fig. 4 caption claims this null comes from the label-shuffle, but p=0.135 is just the empirical max-stat
**Fig. 4 caption, p. 9.** Caption says "label-shuffle null p=0.135". §VI E Table V states this is the empirical max-stat null p-value from 1000 shuffles. Two procedures conflated.

### P5-m9 — Conclusions repeat "headline cosmic-web result" twice for V-Web after §V B designated DESIVAST as primary
**§XV, p. 18.** Conclusion says: "The headline cosmic-web result, the Phase 2 sensitivity sweep, the redshift and density tests, and the HEALPix regional-coherence scan all return null". This designates V-Web as headline, contradicting §V B which moves headline to DESIVAST. Already in P5-M13 but worth re-flagging because Conclusions is where readers focus.

### P5-m10 — "1.98 percentage points" range is across 4 classes including a n=428 void; reporting the range across classes of vastly different n is potentially misleading
**Abstract, §VI A, §XV.** The 1.98 pp range across the four V-Web classes is dominated by the noisy n=428 void bin (binomial 1σ ≈ 2.4 pp at this sample size). A more honest range statistic would restrict to high-n classes (filament/cluster: 0.17 pp range) or report the range with per-class uncertainty propagated. The 1.98 pp number cited repeatedly is a counting-noise artifact of the smallest bin, not a class-uniformity test.

### P5-m11 — DESIVAST z≤0.24 subsample n_lz = 678,945; verify against headline
Recompute: total matched-spiral chirality-relevant = 791,635. If n_lz = 678,945 at z ≤ 0.24, then the >0.24 tail has 112,690 spirals (14.2%). This is consistent with z_median = 0.168 from Table I (more than half below 0.24). ✓

---

## Summary

The second-pass found one additional **essential** issue (the 791,635 vs 812,793 sample-size inconsistency, which propagates through abstract + Table II + §VI A + Fig. 2), two arithmetic errors (σpred filament = −3.16 should be −3.32; Table VIII signs all inverted), and one significant statistical issue the paper waves away (the 12σ rejection of unit variance in the per-pixel σvs_monopole distribution). Combined with the first-pass essentials (Paper IV dependence, abstract overclaims, length, post-hoc primary selection), the manuscript is not ready for PRD. Required revisions before re-review:

1. **Wait for Paper IV to be at minimum on arXiv with a stable DOI** (P5-E1).
2. **Reconcile the 791,635 vs 812,793 labeling** across abstract, §VI A, Table II, Fig. 2, §VIII F (P5-E10).
3. **Fix σpred(filament) and the Table VIII sign convention** (P5-E11, P5-E12).
4. **Properly address the 12σ over-dispersion in the σvs_monopole pixel distribution** (P5-M14).
5. **Standardize the monopole value (−0.0026 vs −0.0028) across all σpred predictions** (P5-M15).
6. **Cut by ~50%** — the paper is twice as long as the science warrants.
7. **Remove Appendix A** — substanceless after the disclaimers.