# EXT6 P4 — ChatGPT Pro Extended (in-thread delta round 6)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37
**PDF**: chirality_catalog_paper_v179.pdf (3ba688c1) · harvested 2026-06-12 19:53 PT

---

Referee report on Paper 4 v1.0.179

Updated recommendation: MAJOR REVISIONS

The paper has moved strongly toward scientific publishability since v1.0.177: the post-MASTER monopole-only interpretation is now correct in the main text, the +3.64σ / +7.93σ taxonomy is substantially repaired, the WLS language is more precise, and the flip-identity QC issue is now scientifically resolved. The remaining obstacle is mostly reproducibility/provenance: the v1.0.179 PDF still points to a v1.0.175 commit as “repository state for this version,” and one primary WLS artifact still relies on a mask-equivalence assertion rather than a paper-level canonical-mask audit. 

chirality_catalog_paper_v179

1. Closure verification of original BLOCKERS / MAJORS
Original BLOCKERS
ID	Status	Verification
B1 — exact source/PDF/artifact release mismatch	PARTIAL / still acceptance-blocking	The title page is v1.0.179, but Data Availability still says “Repository state for this version: commit 53b41d12 (v1.0.175, June 2026).” It then explains the two-step stamp/pin protocol and says the rendered PDF, not the in-repo source at the stamp hash, is authoritative. That is transparent, but not journal-grade reproducibility: a reader still cannot retrieve one immutable v1.0.179 source/PDF/artifact bundle from the stated commit. The live source also still hard-pins artifact links to 53b41d12, while its header is v1.0.179. 

chirality_catalog_paper_v179

 
GitHub
+1
 Fix: mint or stage a final v1.0.179 DOI/tag/commit after all metadata and artifacts are committed, and make the PDF, .tex, artifact links, and Data Availability section all point to that same immutable release.
B2 — post-MASTER monopole-only null misinterpreted	CLOSED	The main text and Table IV now correctly state that the 99.32% reproduction applies only to the raw pre-MASTER pseudo-C
ℓ
(ℓ=1)
	​

 power, while the post-MASTER monopole-only null reproduces only ∼12%, leaving +4.84σ / +5.14σ residuals requiring coherent depth/PSF/morphology systematics beyond monopole-only leakage. 

chirality_catalog_paper_v179


B3 — +3.64σ vs +7.93σ taxonomy	CLOSED	The conclusion now says the 500-MC +3.64σ direct single-mode value is retained for continuity with the leakage analysis, while the 10
4
-permutation Table III canonical row is the current high-statistics diagnostic under its committed field convention. That fixes the old “same physical estimator” contradiction. 
GitHub

B4 — training-set accounting inconsistency	CLOSED	The source-image count, augmentation accounting, and n
train
	​

=21,293, n
val
	​

=5,323 split are reconciled in the revised Data/Training Labels section. 

chirality_catalog_paper_v179


B5 — WLS exact-mask reproducibility	PARTIAL	The NSIDE block-bootstrap sensitivity is now computed and strong: z=−16.9,−18.4,−19.4 across NSIDE 4/8/16, so the exclusion is not single-block-scale brittle. The conditioning audit also shows the nuisance-template degeneracy does not contaminate the dipole posterior. However, the primary bootstrap artifact still says its mask is ((
Original MAJORS
ID	Status	Verification
M1 — HC confidence-cut dependence	CLOSED	The HC p
eq
	​

>0.6, N=949,584, +0.41σ result is now clearly separated from the unthresholded z≃4.2−4.4, 0.57% systematic-sensitivity excess. Fig. 7 and Sec. IV.C now correctly label the +0.41σ as HC. 

chirality_catalog_paper_v179


M2 — three-interpretation “closure” language too strong	CLOSED	The language is now mostly “systematics-attributed,” “supporting,” and “most likely,” rather than claiming definitive closure.
M3 — ℓ=2 cross-spectrum underpowered	PARTIAL / acceptable with caveat	The language has been softened to “supporting,” which is appropriate. The diagnostic still rests on a 200-realization permutation null and should not be treated as a stand-alone confirmation, but it is now one anchor in a broader eight-anchor battery rather than the sole discriminator. 

chirality_catalog_paper_v179


M4 — WLS z≃−18 interpretation	CLOSED, subject to B5	The naive z≃−264.5 is clearly superseded by the block-bootstrap z≃−18, and the NSIDE sensitivity demonstrates stability. The only remaining concern is exact-mask reproducibility under B5. 
GitHub

M5 — classifier calibration caveat too weak	CLOSED	The paper now clearly states that p
eq
	​

 values are ranking scores, not calibrated probabilities, and warns against precision parity use below the empirical threshold without local re-normalization. 

chirality_catalog_paper_v179


M6 — D4-TTA spatial/low-confidence validation	PARTIAL	The paper still uses two ∼2000-object D4 hold-outs, with mean P
CW
	​

 stable but 21.4% argmax flips on borderline galaxies. I still do not see a spatially stratified Z2-vs-D4 comparison on the low-confidence-tail dipole estimator. This no longer blocks the main result, because the HC estimator is clean and the low-confidence tail is explicitly systematics-attributed, but it remains a limitation.
M7 — Shamir comparison overreach	NOT ADDRESSED / still should fix	The paper still says the monopole-mask leakage channel “can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples.” That remains broader than what is demonstrated: the demonstrated mechanism is under this DESI/ViT-Small catalog, mask, and estimator, not under Shamir’s SDSS/Ganalyzer pipeline. 

chirality_catalog_paper_v179

 Fix: replace with “can generate a comparable pre-MASTER dipole-class artifact under this DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required.”
M8 — largest-catalogue precision	CLOSED	The abstract and conclusions consistently pair 8.47M total classified galaxies with 3.20M CW/CCW spirals. 

chirality_catalog_paper_v179

Later carryover issue: flip-identity QC

CLOSED scientifically; PARTIAL as released. The PDF now gives a coherent QC narrative: 2.9% any-channel out-of-range recovered flip probabilities, max excursion ≃0.09, max normalization deviation 4.3×10
−7
, 59,515 HC rows flagged, and a flagged-row-exclusion rerun that leaves the HC dipole null-consistent. The public catalog-wide artifact on main matches those numbers. 

chirality_catalog_paper_v179

 
GitHub
 The release problem remains B1: this new artifact is not pinned by the PDF’s stated v1.0.175 commit.

2. Fresh pass on v1.0.179 — new findings only
BLOCKERS
ID	Section/page	Finding	Proposed fix
F179-B1	Data Availability, p.21	No new scientific blocker beyond the still-open provenance/release blocker. The v1.0.179 PDF still declares a v1.0.175 repository state and makes the rendered PDF the authoritative carrier of the pin, which is not adequate for journal-stage reproducibility. 

chirality_catalog_paper_v179

	Finalize one immutable release: PDF, .tex, figures, scripts, JSON/NPY artifacts, catalog/model checksums, and DOI/tag all mutually consistent.
MAJORS
ID	Section/page	Finding	Proposed fix
F179-M1	Table I, p.5; Discussion, p.12; Appendix C, p.18	The hemisphere look-elsewhere treatment is mostly fixed in prose, but Table I still mixes two different ideas: the direct max-statistic MC gives p
LEE
	​

≤10
−4
, while Bonferroni/BH are described as bracketing the post-LEE significance below (	\sigma
F179-M2	Sec. V.A, p.12	The Shamir comparison remains overbroad, as noted under M7. The text still reads like the DESI/ViT-Small leakage mechanism explains SDSS-class samples directly. 

chirality_catalog_paper_v179

	Use the narrower language proposed above and keep the matched-footprint Ganalyzer caveat.
F179-M3	Appendix D.g artifacts / Table IX, p.19	The WLS result is now well described statistically, but the exact-mask equivalence is still not visible in the paper. Because this is one of the two primary estimators, the mask equivalence should not live only in JSON prose. 
GitHub
	Add a compact mask-equivalence audit table in Appendix D.g.
MINORS
ID	Section/page	Finding	Proposed fix
F179-m1	Fig. 2, p.6	The caption says the figure illustrates the eight D4 transforms, but the rendered figure shows original/flipped examples and raw/equivariant probability bars, not an explicit D4 grid.	Reword to “representative Z2 production TTA examples; D4 validation is described in Appendix B,” or replace the figure with an actual eight-transform D4 panel.
F179-m2	Table VII, p.17	“All 8 tests pass” is now surrounded by necessary-but-not-sufficient caveats and is no longer a major issue, but the headline phrase remains easy to quote out of context. 

chirality_catalog_paper_v179

	Change the caption opener to “All implemented engineering checks meet their stated thresholds.”
F179-m3	Data Availability, p.21	Zenodo DOI is still not minted. 

chirality_catalog_paper_v179

	Mint before journal submission or acceptance.
F179-m4	Conclusion VII.b, p.14	“Primary finding: a quantifiable monopole-mask leakage channel” can confuse readers because the abstract says the primary scientific result is the HC real-space null plus WLS exclusion.	Use “Primary methodological finding” for the leakage channel, and reserve “primary scientific result” for the null-dipole estimator hierarchy.
3. Updated recommendation

Recommendation: MAJOR REVISIONS.

The manuscript has moved toward publishability and is now scientifically close, but I would still require a clean immutable v1.0.179 release bundle and a paper-level WLS mask-equivalence audit before recommending acceptance.
