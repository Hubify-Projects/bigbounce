# EXT4 P5 — ChatGPT Pro Extended (in-thread delta round 4)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064
**PDF**: p5_desi_chirality_v0.1.65.pdf (f265c319) · harvested 2026-06-11 15:54 PT
---
Referee report on Paper 5 v0.1.65
1. Closure verification of original BLOCKERS
Original blocker	Status	Verification
B1. DESIVAST primary non-void control not restricted to DESIVAST usable angular/radial support.	PARTIAL	The new footprint-restricted retabulation is a major improvement and scientifically reassuring: the paper now reports a footprint-restricted null, ∆fCW = +0.0018, SE = 0.0023, z = +0.78, p = 0.43, with all 57,081 exact-membership void spirals inside the constructed footprint. However, the “usable footprint” is defined as the union of hole-sphere angular discs intersected with radial span, not as an independent DESIVAST/BGS/randoms angular selection mask. The original issue is therefore not fully closed as a formal survey-mask control. It should be promoted to a dedicated primary-control table and described as a hole-support footprint stress test unless a formal BGS/DESIVAST randoms mask is used. 

p5_desi_chirality_v0.1.65


B2. DESIVAST ApJ void counts were wrong.	CLOSED	v0.1.65 quotes the final published counts 1,489 / 389 / 297 and identifies 1,461 / 420 / 295 as preliminary. Those match the final DESIVAST ApJ/OSTI record. 

p5_desi_chirality_v0.1.65

 
OSTI.gov

B3. Known-insufficient k=20 VoidFinder membership retained after exact rerun.	NOT ADDRESSED	The paper still publishes 56,981 k=20 VoidFinder void spirals as the title/abstract/Table VIII primary statistic, while admitting the k-unbounded exact rerun gives nvoid = 57,081 and moves 100 galaxies. The text still says the k=20 statistics are retained “for continuity with the released artifacts.” This remains a publication-level blocker. 

p5_desi_chirality_v0.1.65


B4. Paper IV chirality labels and monopole remain load-bearing but external.	PARTIAL	The manuscript is clearer that Paper IV is companion work and propagates monopole uncertainty, but the per-galaxy chirality labels and classifier-monopole correction remain external inputs. The data appendix still says a DOI-minted snapshot accompanies journal submission rather than providing an actual DOI in this draft. 

p5_desi_chirality_v0.1.65

 

p5_desi_chirality_v0.1.65


B5. V-Web/T-Web classifier over-promoted despite selection-function domination.	PARTIAL	The primary/secondary hierarchy is much clearer, with DESIVAST now explicitly primary. But the title/abstract still carry the T-Web/V-Web cross-check prominently, and the manuscript itself shows that BGS-randoms weighting rewrites the environment field: only 44% of cells and 26.6% of matched spirals retain their class. This is acceptable only if every headline statement keeps DESIVAST primary and V-Web diagnostic. 

p5_desi_chirality_v0.1.65

 

p5_desi_chirality_v0.1.65

2. Closure verification of original MAJORS
Original major	Status	Verification
M1. Use correct nomenclature: T-Web, not V-Web.	PARTIAL	The title and footnote now clarify that the method is a Hahn 2007 tidal-tensor/T-Web recipe and not the Hoffman velocity-shear V-Web. But the text still repeatedly calls the implementation “V-Web.” For journal clarity, “T-Web tidal-tensor classifier” should be the paper-level name; vweb can remain only as a code-path name. 

p5_desi_chirality_v0.1.65


M2. Primary/secondary declaration and analysis tree incomplete.	PARTIAL	The analysis tree and primary/secondary declaration are much stronger, and the declared primary estimand is now ∆fCW. However, the Bonferroni-5 family still mixes three two-sample void/non-void ∆ contrasts with two catalog-native GALZONE one-sample void-fCW checks. The family-level language says the primary null is on the contrast itself, but two of five entries are not contrasts. 

p5_desi_chirality_v0.1.65

 

p5_desi_chirality_v0.1.65


M3. Target-program contingency needs effect size, log p, and unique-target splits.	PARTIAL	Cramér’s V = 0.078, log10 p ≈ −1069, and the “small effect driven by sample size” framing are now present. The per-class bright/dark split remains row-level and non-disjoint in unique TARGETIDs; the paper still treats the per-class z values as approximate. 

p5_desi_chirality_v0.1.65


M4. DESIVAST independence from target-program residuals was asserted, not demonstrated.	CLOSED	The DESIVAST bright/dark table and within-program contrasts are now reported. The dark split has a nominal ≈2σ void/non-void contrast before multiplicity, and the text correctly frames it as small-n noise; the bright split, which dominates the DESIVAST sample, is null at ≈0.1σ. This is the right closure. 

p5_desi_chirality_v0.1.65


M5. Phase 2 range statistic overstated.	CLOSED	The text now explicitly states that the empirical max-statistic permutation null controls the false-positive rate, while the range/floor comparison is descriptive. The global max-stat and resolved-cell bookkeeping are now adequate. 

p5_desi_chirality_v0.1.65

 

p5_desi_chirality_v0.1.65


M6. DESIVAST RSD sensitivity claim too strong.	PARTIAL	The conclusion is now correctly narrow: ∆fCW is stable under a fixed-void-geometry perturbation, while membership is not. However, the section still has tension between “RSD-bounded” language and the large membership change in the Monte Carlo: the hole-union count rises from 57,081 to 76,490 ± 161, about a 34% change. The manuscript should consistently say that the estimand, not membership, is stable. 

p5_desi_chirality_v0.1.65

 

p5_desi_chirality_v0.1.65


M7. Use DESI primary redshifts/targets or justify zall row-level usage.	PARTIAL	The unique-TARGETID density-field rebuild is a useful closure, but no ZCAT_PRIMARY rebuild/comparison is shown. The default field still begins from zall survey-program coadd rows. 

p5_desi_chirality_v0.1.65


M8. Tempel and ASTRA over-described as robustness evidence.	CLOSED	ASTRA is now framed as a supporting diagnostic consistency check on the EDR overlap, with the small overlap and strong per-galaxy V-Web/ASTRA label disagreement clearly stated. 

p5_desi_chirality_v0.1.64


M9. Theoretical/bounce framing disproportionate.	CLOSED	The toy mapping is now explicitly labelled heuristic, coordinate/slicing dependent, non-covariant, and not a derived EFT constraint. This is acceptable as an appendix-level phenomenological note. 

p5_desi_chirality_v0.1.65

3. Fresh pass on v0.1.65 — new findings only
New BLOCKERS

No wholly new blocker emerged beyond the unresolved carry-over blocker that the k=20 approximate VoidFinder membership is still the published primary statistic. The footprint issue is greatly improved but still not closed at the level of a formal independent survey mask.

New MAJORS

The new footprint retabulation mixes exact-membership bookkeeping with a k=20 primary presentation.
Location: Abstract p.1; §VIII.B p.17; §VIII.E p.19; Conclusions p.29.
The new footprint result is computed on exact-membership voids, all 57,081 of which fall inside the constructed footprint, but the title, abstract, Table VIII, and conclusion still headline the k=20 nvoid = 56,981 result. This creates two competing “primary” VoidFinder parents in the paper.
Proposed fix: Make the exact, footprint-restricted VoidFinder result the main VoidFinder row: nvoid = 57,081, nnonvoid,footprint = 253,276, fvoid, fnonvoid, ∆fCW, SE, z, p, and CI. Move the k=20 56,981 statistic to a legacy-artifact note. 

p5_desi_chirality_v0.1.65

 

p5_desi_chirality_v0.1.65

The Bonferroni-5 primary family still mixes unlike estimands.
Location: §V.B and Table II, pp.7–8; Table X, p.19.
The paper says the declared primary estimand is void-vs-non-void ∆fCW and that the family-level conclusion is a null on the contrast, but Table II’s five primary entries include two catalog-native GALZONE “void fCW” one-sample tests. That is not the same hypothesis family as the three void/non-void contrasts.
Proposed fix: Either compute non-void complements and full ∆/SE/z/p/CI statistics for V2-REVOLVER and V2-VIDE GALZONE memberships, or demote the GALZONE one-sample rows to supporting catalog-native checks and declare Bonferroni-3 for the actual primary ∆ family. 

p5_desi_chirality_v0.1.65

 

p5_desi_chirality_v0.1.65

The hole-support “usable footprint” should not be described as a DESIVAST survey mask.
Location: §VIII.E, p.19.
Defining the footprint as the union of hole-sphere angular discs intersected with the holes’ radial span is a useful support restriction, but it is not the same as a DESIVAST/BGS angular selection mask or random-catalog support. It could exclude valid survey regions containing no holes, which is acceptable for a conservative stress test but not equivalent to a formal mask.
Proposed fix: Rename it “hole-support-restricted control” or “DESIVAST hole-support footprint stress test.” If the intended claim is a formal footprint result, rebuild using BGS randoms or a published DESIVAST/DESI angular mask.

The RSD paragraph still contains an avoidable internal tension.
Location: §VIII opening, pp.15–16.
The final interpretation is correct: ∆fCW is stable, while membership is not. But the lead-in still reads too much like a membership-stability argument, even though the Monte Carlo changes the void count by about 34%.
Proposed fix: Replace all “membership shift bounded below statistical uncertainty” style wording with: “the membership perturbation is large, but the chirality contrast ∆fCW is empirically stable under this fixed-void-geometry perturbation.” 

p5_desi_chirality_v0.1.65

 

p5_desi_chirality_v0.1.65

New MINORS

Table VIII caption cross-reference should point to §VIII.B, not §VIII.A.
Location: Table VIII, p.17.
Proposed fix: The k-sufficiency/exact-rerun discussion is in §VIII.B; update the caption reference.

The abstract remains over-ledgered.
Location: Abstract, pp.1–2.
Proposed fix: Keep only the two parent populations and headline DESIVAST ∆ result in the abstract. Move detailed V-Web class counts, Phase 2 ranges, and sky/target residuals to a summary table.

Use “consistent with parity” carefully in selection-corrected V-Web discussion.
Location: §IX.A, p.21.
Because the paper’s own framing treats the Paper IV monopole as a classifier systematic, “consistent with the matched-sample monopole and with parity within uncertainties” is more precise than “individually consistent with parity” for large classes.

Data availability still lacks the actual archival DOI.
Location: Appendix B, p.30.
Proposed fix: Insert the DOI/Zenodo snapshot before journal submission, or explicitly mark it as “to be minted upon acceptance.” 

p5_desi_chirality_v0.1.65

4. Updated recommendation

Recommendation: MAJOR REVISIONS.

v0.1.65 moved substantially toward publishability: the ∆fCW contrast table and footprint-restricted null are real scientific closures, but the paper is still not ready until the exact/footprint-restricted VoidFinder result replaces the k=20 headline statistic and the primary Bonferroni family uses a single, consistent estimand.
