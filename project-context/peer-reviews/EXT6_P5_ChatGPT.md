# EXT6 P5 — ChatGPT Pro Extended (in-thread delta round 6)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064
**PDF**: p5_desi_chirality_v0.1.69.pdf (8a6e800f) · harvested 2026-06-12 19:54 PT

---

Referee report on Paper 5 v0.1.69

Updated recommendation: MAJOR REVISIONS.
The paper moved toward publishability since v0.1.67: the GALZONE estimand-family fix is real, Appendix B’s contingency-table regression is fixed, and the duplicate-row bookkeeping is now internally consistent. The remaining hard problem is still the same: the paper knowingly headlines the approximate k=20 VoidFinder membership instead of the exact membership rerun.

1. Closure verification of original BLOCKERS
Original blocker	Status	Verification
B1. DESIVAST primary non-void control not restricted to DESIVAST usable angular/radial support.	PARTIAL	The new footprint retabulation is a major improvement: all 57,081 exact-membership void spirals fall inside the constructed support, and the footprint-restricted control gives ∆fCW = +0.0018, z = +0.78, p = 0.43. However, the “DESIVAST usable footprint” is still constructed from the union of hole-sphere angular discs and radial span, not from an independent published DESIVAST/BGS randoms or angular selection mask. The paper itself still cautions that the maximal-void sky proxy is not a formal published DESIVAST angular mask. This is now a manageable caveat, but not a full closure of the original formal-mask request. 

p5_desi_chirality_v0.1.69


B2. DESIVAST published counts wrong.	CLOSED	The paper now quotes the final ApJ counts 1,489 / 389 / 297 and identifies 1,461 / 420 / 295 as preliminary. This matches the published DESIVAST record. 

p5_desi_chirality_v0.1.69

 
ADS Insights
+1

B3. Known-insufficient k=20 VoidFinder membership retained after exact rerun.	NOT ADDRESSED	The paper still headlines 56,981 k=20 VoidFinder void spirals and explicitly says it retains the k=20 catalog statistics “for continuity,” even though the exact k-unbounded rerun moves 100 galaxies into the void class and gives nvoid = 57,081. This remains the primary publication blocker. 

p5_desi_chirality_v0.1.69


B4. Paper IV chirality labels and monopole remain load-bearing but external.	PARTIAL	The dependency is clearly disclosed: Paper IV is still companion work and not peer-reviewed, and this paper uses its per-galaxy labels and monopole as inputs. The data appendix still says a DOI-minted archival snapshot accompanies journal submission, but no DOI is printed in this draft.
B5. V-Web/T-Web classifier over-promoted despite selection-function domination.	PARTIAL	The hierarchy is much improved: DESIVAST is declared primary and V-Web/T-Web is secondary. Still, the title and abstract give the secondary T-Web/V-Web cross-check substantial headline weight, while the selection-corrected rebuild shows large class-population migration and is explicitly framed as a stress test rather than independent confirmation.
2. Closure verification of original MAJORS
Original major	Status	Verification
M1. Use correct nomenclature: T-Web, not V-Web.	PARTIAL	The title and footnote correctly identify the method as Hahn-style T-Web/tidal tensor rather than Hoffman velocity-shear V-Web, but the text still repeatedly calls the implementation “V-Web.” This remains a nomenclature clarity issue. 

p5_desi_chirality_v0.1.69


M2. Primary/secondary declaration and analysis tree incomplete.	CLOSED	The analysis tree now separates the DESIVAST Bonferroni-5 primary family, Phase 2 secondary sweep, and descriptive diagnostics; it also states the declared primary estimand as void-vs-non-void ∆fCW. 

p5_desi_chirality_v0.1.69


M3. Target-program contingency needs effect size, log p, and unique-target splits.	PARTIAL	Cramér’s V = 0.078 and log10 p ≈ −1069 are now quoted, and the effect is correctly framed as small but sample-size driven. The per-class bright/dark split remains row-level and non-disjoint in TARGETID, with the paper correctly warning that the per-class z values are approximate. 

p5_desi_chirality_v0.1.69


M4. DESIVAST independence from target-program residuals asserted, not demonstrated.	CLOSED	The paper now reports DESIVAST bright/dark program splits and within-program contrasts. Bright dominates and is null; the dark contrast is low-n and treated as small-n noise. This is sufficient closure. 

p5_desi_chirality_v0.1.69


M5. Phase 2 range statistic overstated.	CLOSED	The paper now distinguishes descriptive range/floor bookkeeping from the empirical max-statistic permutation null, which is the component controlling false positives. 

p5_desi_chirality_v0.1.69


M6. DESIVAST RSD claim too strong.	PARTIAL	The final interpretation is now mostly correct: ∆fCW is stable, membership is not. But one lead-in sentence still says the FoG Monte Carlo “bounds the fractional membership shift to well below the statistical uncertainty,” while the same section reports the hole-union count rising from 57,081 to 76,490 ± 161, about a 34% membership change. The later correction is good; the earlier sentence should be removed.
M7. Use DESI primary redshifts/targets or justify zall row-level usage.	PARTIAL	The unique-TARGETID density-field rebuild is helpful, but I still do not see a ZCAT_PRIMARY rebuild/comparison. DESI documentation identifies ZCAT_PRIMARY as the recommended redshift selector in zall files and defines useful spectra using ZCAT_PRIMARY==True, OBJTYPE=='TGT', and ZWARN==0; the paper’s default V-Web field still begins from row-level zall survey-program coadds. 

p5_desi_chirality_v0.1.69

 
DESI Data
+1

M8. Tempel and ASTRA over-described as robustness evidence.	CLOSED	Tempel and ASTRA are now scoped as supporting diagnostics rather than load-bearing validation. The analysis tree also labels ASTRA as an EDR-overlap diagnostic with caveat. 

p5_desi_chirality_v0.1.69


M9. Theoretical/bounce framing disproportionate.	CLOSED	The toy EFT mapping is now clearly labelled heuristic, slicing-dependent, non-covariant, and not a derived constraint. This is acceptable as an appendix-level model-building guide. 

p5_desi_chirality_v0.1.69

3. Fresh pass on v0.1.69 — new findings only
New BLOCKERS

No wholly new blocker emerged. The remaining blocker is the carry-over B3: the k=20 VoidFinder statistic is still the paper’s published primary VoidFinder headline despite the exact rerun.

New MAJORS

The phrase “largest controlled sample (n = 56,981)” is now technically wrong or at least misleading.
Location: §V.B, p.7; §VIII.D, p.18.
The primary-path declaration says the DESIVAST path has “the largest controlled sample (nDESIVASTvoid = 56,981).” But the same paper now reports larger DESIVAST void samples in the same primary family: V2-REVOLVER sphere-PIS nvoid = 102,911 in Table X and V2-REVOLVER catalog-native GALZONE nvoid = 104,912. The paper even calls the V2-REVOLVER catalog-native nvoid > 10^5 result the cleanest single chirality-in-voids measurement.
Proposed fix: Replace “largest controlled sample (n = 56,981)” with “a properly powered DESIVAST VoidFinder sample, ∼130× the V-Web void bin; the largest DESIVAST void sample is the V2-REVOLVER catalog-native GALZONE row.” This is a wording/statistical-ledger fix, not a science change.

The footprint retabulation is scientifically important but still buried outside the main primary table.
Location: §VIII.E, p.20; Table X p.19.
The new footprint-restricted result is the direct closure of the most serious prior control-sample concern, but it is reported inside the sky-position stratification section rather than as a row in the main DESIVAST primary table. Table X still displays only the k=20 VoidFinder row and the two sphere-PIS watershed rows.
Proposed fix: Add a row to Table X or a new adjacent Table XI labelled “VoidFinder exact, hole-support-footprint-restricted control,” with nvoid = 57,081 and the footprint-restricted nnonvoid, fCW, ∆fCW, SE, z, p, and CI. This would make the formal response to the footprint critique visible in the declared-primary result block.

New MINORS

Figure 3’s plot title still uses the wrong parent count.
Location: Fig. 3, p.9.
The plotted/captioned parent is the 812,793 env-labeled row parent covering 783,820 unique spirals, but the figure title still says n = 791,635 chirality-relevant matched spirals.
Proposed fix: Retitle the panel “n = 812,793 env-labeled rows” or “783,820 unique env-matched spirals / 812,793 rows.”

The title still mixes the full chirality-relevant parent with the V-Web environment-labeled parent.
Location: Title, p.1.
“T-Web cross-check across 791,635 DR1 matched spirals” is not the actual V-Web env-labeled parent; the paper’s own ledger says 783,820 unique env-matched spirals carried on 812,793 rows. 

p5_desi_chirality_v0.1.69


Proposed fix: Use “across the DR1 matched-spiral sample” or “across 783,820 environment-matched spirals.”

The residual RSD sentence should be edited once more.
Location: §VIII opening, p.16.
Proposed fix: Delete “bounds the fractional membership shift to well below the statistical uncertainty” and keep the later, correct sentence: “void membership is not insensitive; ∆fCW is stable under the fixed-void-geometry perturbation.”

The data-availability DOI is still promised, not printed.
Location: Appendix C, p.31.
Proposed fix: Insert the archival DOI before journal submission or change the wording to “will be minted upon acceptance.” 

p5_desi_chirality_v0.1.69

4. Recommendation

MAJOR REVISIONS.
v0.1.69 is materially stronger than v0.1.67 and the Appendix B / GALZONE / duplicate-row fixes are real, but the paper remains below publication standard until the exact VoidFinder membership and footprint-restricted control replace the k=20 VoidFinder statistic as the visible primary result.
