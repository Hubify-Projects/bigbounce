# EXT9 P5 — ChatGPT (in-thread delta round 9; recalibrated prompt)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064
**PDF**: p5_desi_chirality_v0.1.73.pdf · harvested 2026-06-13 13:29 PT
---
Referee report on Paper 5 v0.1.73

Updated recommendation: MINOR REVISIONS.
v0.1.73 has moved toward publishability and is now in the “minor revision / ship after final packaging” regime. I do not see a remaining load-bearing statistical flaw or missing control that requires substantial scientific rework. The remaining issues are mostly clarity, presentation, and submission-package dependencies.

1. Closure verification of prior BLOCKERS / MAJORS
Prior item	Status	Verification
DESIVAST primary non-void control not restricted to DESIVAST usable support.	PARTIAL, scientifically acceptable with caveat.	The paper now reports a footprint-restricted DESIVAST control and Table VIII includes a footprint-restricted non-void row; the text also states the footprint-restricted null remains clean. This closes the practical concern that the result was driven by out-of-support non-voids. The remaining caveat is that this is still a hole-support footprint constructed from the union of hole-sphere angular discs and radial span, not an independent published DESIVAST/BGS randoms mask. That caveat is disclosed and no longer publication-blocking.
DESIVAST ApJ void counts wrong.	CLOSED.	The final ApJ counts are now used: 1,489 VoidFinder, 389 V2-REVOLVER, and 297 V2-VIDE; the older 1,461/420/295 values are identified as preliminary. 

p5_desi_chirality_v0.1.73


VoidFinder k=20 membership approximation retained despite exact rerun.	CLOSED for publication standard.	The abstract now discloses that the hole-union definition is permissive, and §VIII.B gives the exact k-unbounded rerun: only 100 galaxies move into the void class, nvoid changes to 57,081, and ∆fCW changes from +0.0007 to +0.0006 with the same null verdict. The stricter maximal-sphere subset also gives a null at nvoid = 20,900. I still would prefer the exact row in the main table, but the approximation is now transparently bounded and not a load-bearing defect.
Paper IV chirality labels and monopole are load-bearing but external.	PARTIAL, submission-packaging condition.	The dependency is clear: Paper IV provides the per-galaxy CW/CCW labels and classifier-monopole reference, and this paper does not independently classify galaxies. The data appendix says a DOI-minted archival snapshot accompanies journal submission, but no DOI is printed in this draft. This is acceptable if the DOI and Paper IV/concurrent material are available to referees at submission.
V-Web/T-Web over-promoted despite selection-function domination.	PARTIAL, acceptable as framed.	DESIVAST is now clearly the primary path and V-Web/T-Web is secondary. The paper also states that the BGS-randoms-weighted low-z stress test substantially reshapes the V-Web field, with only 44% of common-mask cells and 26.6% of matched spirals retaining class labels. That keeps V-Web appropriately diagnostic, although it remains prominent in the title/abstract.
Use correct nomenclature: T-Web, not V-Web.	PARTIAL.	The title and footnote now identify the method as Hahn-style tidal tensor / T-Web rather than Hoffman velocity-shear V-Web. The body still uses “V-Web” for backward compatibility. This is now a nomenclature blemish, not a scientific problem. 

p5_desi_chirality_v0.1.73


Primary/secondary declaration and analysis tree incomplete.	CLOSED.	Table II and §V.B now define DESIVAST as the Bonferroni-5 primary family and V-Web/Tempel/ASTRA/T-Web as secondary or descriptive checks. The declared primary estimand is consistently the void–non-void ∆fCW contrast. 

p5_desi_chirality_v0.1.71


Target-program contingency needed effect size/log p/unique accounting.	PARTIAL.	Cramér’s V = 0.078 and log10 p ≈ −1069 are now quoted, the effect is described as small but sample-size amplified, and exact Appendix B contingency tables are supplied. The per-class bright/dark splits remain row-level/non-disjoint where objects appear in both programs, but the limitation is disclosed.
DESIVAST independence from target-program residuals not demonstrated.	CLOSED.	The DESIVAST bright/dark split now reports within-program void–non-void contrasts. Bright dominates and is null; the dark contrast is nominal ≈2σ and explicitly treated as small-n noise before multiplicity. 

p5_desi_chirality_v0.1.73


Phase 2 range statistic overstated.	CLOSED.	The text now distinguishes the descriptive range/floor comparison from the empirical max-statistic permutation null, which is the component controlling false positives. 

p5_desi_chirality_v0.1.69


DESIVAST RSD claim too strong.	CLOSED.	The manuscript now says void membership is not insensitive and that ∆fCW, not membership, is stable under the fixed-void-geometry perturbation. This resolves the earlier overclaim. 

p5_desi_chirality_v0.1.73


Use DESI primary redshifts / justify zall row-level usage.	PARTIAL.	The unique-TARGETID density-field rebuild is reassuring: volume fractions shift by at most 0.70 pp and 97.9% of matched-spiral assignments retain class. A ZCAT_PRIMARY rebuild is still not shown. DESI’s own documentation identifies ZCAT_PRIMARY as the recommended redshift selector and defines useful DR1 spectra with ZCAT_PRIMARY==True, OBJTYPE=='TGT', and ZWARN==0; since V-Web is secondary, this is not a blocker. 

p5_desi_chirality_v0.1.73

 
DESI Data
+1

Tempel and ASTRA over-described as robustness evidence.	CLOSED.	ASTRA is now explicitly framed as a supporting EDR-overlap diagnostic, with Noverlap = 25,186 and strong V-Web/ASTRA per-galaxy label disagreement disclosed. 

p5_desi_chirality_v0.1.73


Theoretical/bounce framing disproportionate.	CLOSED.	Appendix A now labels the EFT mapping as heuristic, non-covariant/slicing-dependent, and not a derived constraint. It no longer affects the empirical claim. 

p5_desi_chirality_v0.1.73

2. Closure verification of prior v0.1.72 fresh-pass items
Prior v0.1.72 item	Status	Verification
V-Web n=428 vs DESIVAST-overlap n=6 denominator ambiguity.	PARTIAL.	The body now clearly states that n=6 is the z≤0.24 overlap of the full n=428 V-Web void bin and that the denominators serve distinct roles. The abstract still says “the V-Web void class at z ≲ 0.24 is sample-size limited at n=428,” which remains imprecise because n=428 is the full secondary V-Web void bin, not the z≤0.24 DESIVAST-overlap count.
Footprint-restricted control present but not integrated into primary contrast table.	PARTIAL.	Table VIII now includes the footprint-restricted non-void row and §VIII.E gives the footprint-restricted contrast, but Table X—the main three-algorithm ∆fCW table—still lists only the three sphere-PIS rows. This is a presentation issue, not a missing analysis.
3. Fresh pass on v0.1.73 — new findings only
BLOCKERS

None.

MAJORS

None.

MINORS

The new abstract parenthetical on VoidFinder geometry is useful but overloaded.
Location: Abstract pp.1–2; §VIII.B–E pp.17–20.
The abstract now mentions three related but distinct things in one sentence: k=20 hole-union membership, exact k-unbounded any-hole membership nvoid = 57,081, and stricter maximal-sphere membership nvoid = 20,900. The scientific point is correct, but the wording is dense enough that readers may confuse “exact rerun” with “maximal-sphere rerun.”
Proposed fix: Split into two sentences: “The k-unbounded any-hole rerun gives nvoid = 57,081 and the same ∆fCW null. A stricter maximal-sphere subset gives nvoid = 20,900 and also remains null.”

One abstract phrase should be corrected before submission.
Location: Abstract p.1.
Replace “the V-Web void class at z ≲ 0.24 is sample-size limited at n = 428” with “the full V-Web secondary void bin is sample-size limited at n = 428; only n = 6 lie in the DESIVAST z≤0.24 overlap used for the per-galaxy disagreement check.” This is the cleanest way to prevent denominator confusion.

Final archive DOI remains a submission-day action.
Location: Appendix C p.31.
The appendix says a DOI-minted archival snapshot accompanies journal submission. That is acceptable in a pre-submission draft, but the submitted version should print the DOI or give the repository record explicitly. 

p5_desi_chirality_v0.1.73

4. Recommendation

MINOR REVISIONS.
The manuscript is now close to publishable: the remaining issues are wording/table-integration and submission-packaging items, not missing controls or statistical rework.
