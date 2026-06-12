# EXT5 P5 — ChatGPT Pro Extended (in-thread delta round 5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064
**PDF**: p5_desi_chirality_v0.1.67.pdf · harvested 2026-06-12 00:49 PT · state done
---
Referee report on Paper 5 v0.1.67

Updated recommendation: MAJOR REVISIONS.
The manuscript moved toward publishability since v0.1.65: the Bonferroni-5 estimand-family problem is now substantially closed, and the new footprint-restricted DESIVAST null is scientifically reassuring. It is still not ready because the known-approximate k=20 VoidFinder membership remains the paper’s headline statistic, and v0.1.67 introduces a new reproducibility regression in Appendix B’s contingency tables.

1. Closure verification of original BLOCKERS
Original blocker	Status	Verification
B1. DESIVAST primary non-void control not restricted to DESIVAST usable angular/radial support.	PARTIAL	The new retabulation is a real closure attempt: using a hole-support footprint, all 57,081 exact-membership void spirals fall inside the constructed footprint, and the footprint-restricted control gives ∆fCW = +0.0018, SE = 0.0023, z = +0.78, p = 0.43. That confirms the original null is not driven by the obvious outside-footprint population. However, the footprint is still defined as the union of DESIVAST hole-sphere angular discs intersected with radial span, not as an independent DESIVAST/BGS randoms or published angular selection mask. The paper itself still notes that the maximal-void sky proxy is not a formal published DESIVAST angular mask. This is now a major caveat, not a fatal blocker, if labelled honestly as a hole-support footprint stress test. 

p5_desi_chirality_v0.1.67

 

p5_desi_chirality_v0.1.67


B2. DESIVAST published counts wrong.	CLOSED	The manuscript now quotes the final ApJ counts 1,489 / 389 / 297 and identifies the previous 1,461 / 420 / 295 values as preliminary. These match the published DESIVAST ApJ/OSTI record. 
OSTI.gov

B3. Known-insufficient k=20 VoidFinder membership retained after exact rerun.	NOT ADDRESSED	The paper still headlines 56,981 k=20 VoidFinder void spirals and states that k=20 statistics are retained “for continuity,” even though the exact k-unbounded rerun moves 100 galaxies into the void class, giving nvoid = 57,081 and ∆fCW ≈ +0.0006 instead of +0.0007. This remains the main publication blocker. 

p5_desi_chirality_v0.1.67


B4. Paper IV chirality labels and monopole remain load-bearing but external.	PARTIAL	The dependence is disclosed more clearly: Paper IV is still described as companion work and not yet peer-reviewed, while this paper consumes its per-galaxy labels and monopole as inputs. The data appendix still says a DOI-minted archival snapshot accompanies journal submission, but the PDF does not yet provide an actual DOI. 

p5_desi_chirality_v0.1.67

 

p5_desi_chirality_v0.1.67


B5. V-Web/T-Web classifier over-promoted despite selection-function domination.	PARTIAL	The hierarchy is much better: DESIVAST is primary and V-Web is secondary. But the paper still foregrounds V-Web/T-Web in the title and abstract while §IX.A states that the selection-corrected rebuild rewrites the environment field: class volumes shift up to 21 pp, only 44% of common-mask cells retain labels, and only 26.6% of matched spirals keep their class. This is acceptable only if V-Web remains explicitly diagnostic everywhere. 

p5_desi_chirality_v0.1.67

2. Closure verification of original MAJORS
Original major	Status	Verification
M1. Use correct nomenclature: T-Web, not V-Web.	PARTIAL	The title now says “T-Web (Hahn 2007)” and the footnote explains that the method is not the Hoffman velocity-shear V-Web. However, the paper still repeatedly names the implementation “V-Web” for backward compatibility. For journal clarity, “T-Web tidal-tensor classifier” should be the scientific name, with vweb reserved for code paths. 

p5_desi_chirality_v0.1.67


M2. Primary/secondary declaration and analysis tree incomplete.	CLOSED	The analysis tree now explicitly separates the DESIVAST Bonferroni-5 primary family, the Phase 2 secondary sweep, and descriptive diagnostics. It also now states that the declared primary estimand is the void-vs-non-void ∆fCW contrast. 

p5_desi_chirality_v0.1.67

 

p5_desi_chirality_v0.1.67


M3. Target-program contingency needs effect size, log p, and unique-target splits.	PARTIAL	Cramér’s V = 0.078 and log10 p ≈ −1069 are now present, and the effect is correctly framed as small but sample-size amplified. However, the per-class bright/dark splits remain row-level and non-disjoint in unique TARGETIDs; the manuscript states that the artifacts still do not carry a per-class unique-TARGETID program split. 

p5_desi_chirality_v0.1.67

 

p5_desi_chirality_v0.1.67


M4. DESIVAST independence from target-program residuals asserted, not demonstrated.	CLOSED	The DESIVAST program split is now shown and interpreted correctly. The bright subsample dominates and gives a null void/non-void contrast at ≈0.1σ; the dark split has a nominal ≈2σ contrast before multiplicity but is explicitly treated as small-n noise. 

p5_desi_chirality_v0.1.67


M5. Phase 2 range statistic overstated.	CLOSED	The paper now distinguishes the descriptive range/floor comparison from the inferential empirical max-statistic null, and Table VII reports both per-cell pLEE and a global max-stat correction. 

p5_desi_chirality_v0.1.67


M6. DESIVAST RSD claim too strong.	PARTIAL	The final interpretation is now largely correct: the manuscript says void membership is not insensitive and that ∆fCW, not membership, is stable under the fixed-void-geometry perturbation. However, some lead-in wording still says the FoG Monte Carlo “bounds the fractional membership shift to well below the statistical uncertainty,” while the same paragraph reports the hole-union count rising from 57,081 to 76,490 ± 161, a ∼34% membership change. That phrase should be removed. 

p5_desi_chirality_v0.1.67


M7. Use DESI primary redshifts/targets or justify zall row-level usage.	PARTIAL	The unique-TARGETID field rebuild remains useful, but the default V-Web density field still begins from zall survey-program coadd rows. I still do not see a ZCAT_PRIMARY rebuild or direct comparison. 

p5_desi_chirality_v0.1.67


M8. Tempel and ASTRA over-described as robustness evidence.	CLOSED	ASTRA is now explicitly framed as a supporting EDR-overlap diagnostic, with small overlap size and strong V-Web/ASTRA label disagreement stated clearly. 

p5_desi_chirality_v0.1.67


M9. Theoretical/bounce framing disproportionate.	CLOSED	The toy EFT appendix is now labelled as heuristic, slicing-dependent, non-covariant, and not a derived constraint. That is acceptable as an appendix-level phenomenological note. 

p5_desi_chirality_v0.1.64

3. Fresh pass on v0.1.67 — new findings only
New BLOCKERS

No wholly new blocker emerged. The carry-over blocker remains the same: the paper still publishes the k=20 approximate VoidFinder membership as the headline primary statistic despite having the exact rerun.

New MAJORS

Appendix B’s new 4×2 contingency tables do not reproduce the quoted statistics and are internally inconsistent.
Location: Appendix B, p.30–31.
Table XVI says the printed CW/CCW × V-Web class counts sum to n = 812,793 with CW = 404,075 and CCW = 408,718, but the printed row counts sum to CW = 404,115 and CCW = 408,678. The printed filament and cluster CW counts also disagree with Table III/body counts. Using the printed Table XVI cells gives a different Pearson χ² than the quoted χ² = 3.55. Table XVII has a larger problem: it is labelled as the bright/dark subset with nbright+dark = 811,609, but the printed class rows use the full V-Web class totals and sum to 812,793, not 811,609. This is not a “<1 row” rounding issue; it is a table-construction error of 1,184 rows. 

p5_desi_chirality_v0.1.67


Proposed fix: Replace Appendix B with exact integer contingency tables exported directly from the committed arrays used for the χ² calculations. Do not derive reproducibility tables from rounded abstract fractions. Add a checksum line: row totals, column totals, χ², d.o.f., p, and Cramér’s V computed from the printed cells.

The primary VoidFinder presentation now has three inconsistent parents: k=20, exact, and exact-footprint.
Location: Abstract p.1–2; §VIII.B p.17; §VIII.E p.20.
The abstract and Table VIII present k=20 nvoid = 56,981; §VIII.B says exact membership gives nvoid = 57,081; §VIII.E’s new footprint retabulation is explicitly based on the 57,081 exact-membership void spirals. Scientifically the difference is tiny, but a primary analysis should not have competing parent definitions. 

p5_desi_chirality_v0.1.67

 

p5_desi_chirality_v0.1.67


Proposed fix: Promote the exact-membership VoidFinder result to the main row everywhere. Then add the exact footprint-restricted row immediately below it. The k=20 value can remain only as a legacy artifact note.

The “largest controlled sample” and “|∆fCW| ≲ 0.002” wording is now stale after the GALZONE closure.
Location: §V.B p.7; Abstract p.2.
The paper now correctly reports that the two catalog-native GALZONE rows carry the same ∆fCW estimand, but V2-REVOLVER GALZONE has |∆fCW| = 0.0037, not ≤0.002. The abstract handles this with “all five ≤0.004,” but §V.B still says the headline rests on |∆fCW| ≲ 0.002 across all three algorithms, while treating five rows as the primary family. 

p5_desi_chirality_v0.1.67

 

p5_desi_chirality_v0.1.67


Proposed fix: Use one consistent statement: “three sphere-PIS definitions have |∆fCW| ≤ 0.002; all five Bonferroni-5 primary definitions, including catalog-native GALZONE complements, have |∆fCW| ≤ 0.0037.”

New MINORS

Appendix B should not say discrepancies are “<1 row.”
Location: Appendix B p.30–31.
The printed Table XVI and XVII discrepancies are larger than rounding.
Proposed fix: After regenerating exact tables, delete that sentence or replace it with an exact statement of whether printed cells are rounded or artifact-exact.

RSD wording still needs one final edit.
Location: §VIII opening, p.15–16.
Proposed fix: Replace “bounds the fractional membership shift to well below the statistical uncertainty” with “shows that the chirality contrast remains stable despite a large membership perturbation.”

The title still advertises the V-Web cross-check across 791,635 DR1 matched spirals.
Location: Title p.1.
The abstract correctly distinguishes 791,635 chirality-relevant matched spirals from 783,820 environment-matched spirals and 812,793 env-labeled rows.
Proposed fix: Use “across the DESI DR1 matched-spiral sample” or “across 783,820 environment-matched spirals” to avoid the parent-count ambiguity.

Data availability still promises a DOI rather than printing one.
Location: Appendix C p.31.
Proposed fix: Insert the archival DOI before submission, or state explicitly that the archive will be minted on acceptance. 

p5_desi_chirality_v0.1.67

4. Recommendation

MAJOR REVISIONS.
v0.1.67 is much stronger than v0.1.65 because the GALZONE estimand-family issue and footprint retabulation are real closures, but the paper remains short of publication standard until the exact VoidFinder membership replaces the k=20 headline and the new Appendix B contingency-table regression is fixed.
