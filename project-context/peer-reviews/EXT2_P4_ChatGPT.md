# EXT2 P4 — ChatGPT in-thread delta review
**Provider**: chatgpt.com Big Bounce Book project · Pro Extended (GPT-5.5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37
**PDF**: chirality_catalog_paper_v173.pdf · **Harvested**: 2026-06-10 ~21:30 PDT
**Mode**: same-thread re-review (closure verification + fresh pass + updated verdict)

---

Show more
Thought for 7m 0s
Referee report on Paper 4 v1.0.173

Updated recommendation: MAJOR REVISIONS

The paper moved substantially toward publishability since v1.0.171: the monopole/post-MASTER distinction is now mostly correct, the significance conventions are far clearer, the Shamir reference split is fixed, and the NSIDE block-bootstrap sensitivity calculation materially strengthens the WLS exclusion. However, I still would not accept it in the present form because the exact PDF/source/artifact provenance is still not closed, and several load-bearing labels remain internally inconsistent.

I reviewed the full revised 22-page PDF and spot-checked the public source/artifacts at the paper’s stated commit where accessible. I did not rerun the full 8.47M-object pipeline.

1. Closure verification of original BLOCKERS and MAJORS
Original BLOCKERS
ID	Status	Verification
B1 — Data Availability/source-PDF version mismatch	REGRESSION / PARTIAL	The uploaded PDF now says “Repository state for this version: commit 297aa805 (v1.0.173)” and gives the HC sample and +0.41σ result, which is the intended fix. 

chirality_catalog_paper_v173

 However, the public .tex opened at commit 297aa805 contains \paperVersion{v1.0.173} in the header but its Data Availability line still says commit 7c03bb64 / v1.0.172, not 297aa805. 
GitHub
+1
 This means the uploaded PDF and the stated source commit are still not a clean reproducible pair. Fix: restamp after the source itself contains the exact PDF Data Availability text, pin artifact links to the immutable commit or DOI, and include a build/manifest hash.
B2 — Post-MASTER monopole-only null was misinterpreted	PARTIAL	The core scientific correction is now present: Sec. IV.D/Table IV explicitly says the 99.32% result is pre-MASTER only, and that the post-MASTER monopole-only null gives +4.84σ, ∼12% reproduction, with a 10
4
-run confirmation at +5.14σ. The public artifacts confirm the same +4.84 and +5.14 results. 
GitHub
+1
 Remaining problem: the analysis-hierarchy bullet still says the monopole-only null “demonstrat[es] the +3.64σ canonical value is consistent with monopole-mask leakage,” which is no longer correct for the post-MASTER residual. 
GitHub
 Fix: change that bullet to “demonstrates pre-MASTER monopole-mask leakage; post-MASTER residual requires additional coherent systematics.”
B3 — +3.64σ vs +7.93σ canonical harmonic significance inconsistency	PARTIAL	The new notation subsection and abstract now acknowledge the three significance conventions and explicitly state that +3.64σ, +7.93σ, and +7.28σ are not mutually comparable. But the conclusion still says the +3.64σ and +7.93σ values “describe the same physical estimator and footprint under different null-run sizes,” which muddies the earlier “not mutually comparable” convention. 

chirality_catalog_paper_v173

 Fix: choose one taxonomy: either present +3.64σ as a historical 500-MC direct diagnostic retained for continuity, or present both as explicitly separate estimators. Do not call them the same physical estimator if their field convention/decoupling/null implementation differs.
B4 — Training-set accounting inconsistency	CLOSED	Sec. II.B now reconciles the 25,790 source images with the 26,616 training pool after flip augmentation and gives the 80/20 split n
train
	​

=21,293, n
val
	​

=5,323. 

chirality_catalog_paper_v173

 The supporting artifact states the best-epoch validation semantics and confirms n
train
	​

, n
val
	​

. 
GitHub

B5 — WLS/template-fit mask/artifact mismatch	PARTIAL	The requested NSIDE block sensitivity was computed and is useful: z=−16.9,−18.4,−19.4 at NSIDE 4,8,16, with similar bootstrap inflation factors. 

chirality_catalog_paper_v173

 The committed artifact confirms this. 
GitHub
 But the core exact-mask concern remains: joint_nuisance_bootstrap_sigma.json still says the bootstrap uses a galactic-latitude/n_total mask that differs from the paper’s stated canonical N
spiral
	​

≥10 mask. 
GitHub
 Fix: either rerun the WLS and bootstrap on the exact canonical pixel set used in the paper, or relabel the primary WLS result as a closely related (
Original MAJORS
ID	Status	Verification
M1 — HC null depends on confidence cut; unthresholded sample is non-null	PARTIAL	The paper now gives the unthresholded result, the full-sample injection floor, and a confidence-cut sweep showing the transition collapses at p
eq
	​

>0.6. This is a real improvement. Remaining problem: some text still calls the +0.41σ result the “full-catalog real-space dipole,” even though it is the HC p
eq
	​

>0.6, N=949,584 result.
M2 — Three-interpretation “closure” language too strong	CLOSED	The language is now mostly “systematics-attributed,” “most likely,” and “requires coherent depth/PSF/morphology systematics,” rather than overclaiming cosmological closure.
M3 — ℓ=2 cross-spectrum underpowered as formal discriminator	PARTIAL	The diagnostic remains valuable, but still uses a 200-realization permutation null and is still described as “confirming” a depth-correlated systematic. 

chirality_catalog_paper_v173

 Fix remains: increase the null ensemble and/or soften “confirming” to “supporting.”
M4 — WLS z=−18 interpretation needed tightening	CLOSED, subject to B5	The paper now explicitly supersedes naive z≃−264.5 with the block-bootstrap z≃−18.1, and the NSIDE sensitivity strengthens the interpretation. 

chirality_catalog_paper_v173

 It also continues to avoid a formal Ganalyzer-pipeline exclusion. Remaining exact-mask reproducibility is covered under B5.
M5 — Classifier calibration caveat too weak	CLOSED	Sec. IV.A and Data Availability now clearly state that p
eq
	​

 values are ranking scores, not calibrated probabilities, and that the mean confidence far exceeds independent GZ1 accuracy.
M6 — D4-TTA validation not enough to dismiss rotation-related systematics	PARTIAL / NOT FULLY ADDRESSED	The paper still reports only the two ∼2000-object D4 hold-outs, mean P
CW
	​

 stability, and a 21.4% argmax-label flip rate on borderline galaxies. 

chirality_catalog_paper_v173

 I do not see the requested spatially stratified Z2-vs-D4 comparison in the low-confidence tail.
M7 — Previous-work comparison overreaches	NOT ADDRESSED	Sec. V.A still says the monopole-mask leakage channel “can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples.” 

chirality_catalog_paper_v173

 That remains too broad for a DESI/ViT-Small demonstration.
M8 — “Largest chirality-labelled catalogue” claim should be precise	CLOSED	The abstract now pairs the 8.47M catalogue claim with N
spiral
	​

=3,201,160, making the scope clear enough. 

chirality_catalog_paper_v173

2. Fresh pass on v1.0.173 — new or still-unresolved findings
BLOCKERS
ID	Section/page	Finding	Proposed fix
FB1	Data Availability, p.20; source at stated commit	The uploaded PDF says the repository state is 297aa805, but the public .tex at 297aa805 still has Data Availability text saying 7c03bb64 / v1.0.172. Worse, the source defines the \artifact{} macro to link artifacts through the mutable main branch rather than the pinned commit. This still fails an external referee’s “can I rebuild exactly what I am reviewing?” test. 

chirality_catalog_paper_v173

 
GitHub
+1
	Mint or stage a release where the .tex, PDF, figures, JSON artifacts, scripts, and catalog/model checksums are all pinned together. Change artifact hyperlinks from blob/main/... to blob/<release-commit>/... or DOI-backed paths. The PDF’s stated commit should contain the exact same Data Availability text as the PDF.
MAJORS
ID	Section/page	Finding	Proposed fix
FM1	Sec. IV.D, p.10; Fig. 8 caption, p.10; Appendix E, p.20	The paper still refers to the “full-catalog real-space dipole at +0.41σ.” That is wrong: the +0.41σ headline is the HC p
eq
	​

>0.6, N=949,584 estimator, while the unthresholded full sample has a 0.57%, z≃4.2−4.4 systematic-sensitivity excess.	Replace every “full-catalog real-space dipole at +0.41σ” phrase with “HC real-space dipole at +0.41σ” or “Catalog-C HC dipole.” Reserve “full-sample/unthresholded” for the 0.57% diagnostic.
FM2	Sec. VI.B, p.13	The statement “The present null disfavors ... any model predicting ... dipole ≥0.75%” overuses A
50
	​

. The paper itself defines A
50
	​

≈0.75% as a 50%-recovery threshold and A
95
	​

∈(1.0,1.5]% as the falsification boundary.	Change this to “is sensitive at the 50%-recovery level to ∼0.75%” and reserve “disfavors/falsifies” for amplitudes ≳A
95
	​

, or explicitly state a likelihood/coverage convention if the authors intend a stronger claim.
FM3	Table I, p.5; Discussion, p.12; Appendix C, p.17	The hemisphere look-elsewhere treatment is internally confused. A direct max-statistic MC null with p
LEE
	​

≤10
−4
 already incorporates the 648-direction scan and is a strong rejection of the random-label null. The text then says Bonferroni/BH “reduce the post-LEE significance to <1σ,” which is not the same correction and contradicts the stated “principled” max-statistic result. 

chirality_catalog_paper_v171

	Present one primary hemisphere statistic: the direct max-statistic p
LEE
	​

, systematics-attributed. Move Bonferroni/BH to a clearly labelled heuristic on per-direction p-values, and do not describe it as the post-LEE correction if the max-statistic MC is the LEE correction.
FM4	Sec. IV.C, p.9	The paper says the +0.41σ real-space result and +7.28σ harmonic diagnostic are “mutually consistent” because a Shamir-class injected dipole would give z∼68−218 in the harmonic channel. This is not a consistency test between the two measured estimators; it is an amplitude/completeness argument in the harmonic channel. 

chirality_catalog_paper_v173

	Rephrase: “The harmonic-completeness check shows that a Shamir-class clean dipole would be far larger than the observed harmonic residual in this channel; it does not make the HC real-space and systematics-attributed harmonic residuals statistically interchangeable.”
FM5	Appendix B, p.17; Table VII	The “all 8 tests pass” statement is too strong after the text admits T5 is not an independent directional-coupling pass criterion and T7 is only a confidence-mass/flip-error proxy, not a calibration or truth-reliability test. 

chirality_catalog_paper_v173

	Change “all 8 tests pass” to “all implemented engineering checks pass at their stated thresholds; T5/T7 are necessary but not sufficient for sub-percent isotropy control.” This will prevent readers from treating the bias-hardening table as a formal systematics null suite.
MINORS
ID	Section/page	Finding	Proposed fix
m1	Title, p.1	The title remains more like an abstract than a journal title.	Shorten to something like: “Survey-scale galaxy chirality with equivariant TTA: a DESI Legacy null dipole and low-ℓ mask-systematics diagnostic.”
m2	Data Availability, p.20	Zenodo DOI is still “not yet minted.” This is acceptable for an internal draft but not ideal for acceptance-stage review. 

chirality_catalog_paper_v173

	Mint before journal submission or change the text to a fully citable archived release.
m3	Sec. III.A / Conclusion VII.c	The text alternates between “not mutually comparable” and “same physical estimator” for +3.64σ vs +7.93σ.	Add a one-row estimator dictionary: name, mask, field convention, decoupling, null size, and whether it supersedes/diagnoses another value.
m4	Sec. V.A, p.12	The Shamir comparison is now better referenced, but the phrase “pre-MASTER dipole-class signal observed in SDSS-class samples” still reads as broader than what was actually demonstrated. 

chirality_catalog_paper_v173

	Use “can generate a comparable pre-MASTER dipole-class artifact under this DESI/ViT-Small pipeline; a matched Ganalyzer test remains required.”
m5	Appendix D.h, p.19	The ℓ=2 cross-spectrum remains a useful but low-N diagnostic.	Either raise the permutation count above 200 or soften “confirming” to “supporting.”
3. Updated recommendation

MAJOR REVISIONS. The revision moved toward publishability and closed several scientific interpretation problems, but the paper still needs an immutable, source-consistent release and several wording/statistical-consistency fixes before I would recommend acceptance.

Sources

Pro Extended

