# EXT5 P4 — ChatGPT Pro Extended (in-thread delta round 5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37
**PDF**: chirality_catalog_paper_v177.pdf · harvested 2026-06-12 00:48 PT · state done
---
Referee report on Paper 4 v1.0.177

Updated recommendation: MAJOR REVISIONS

I re-read the full v1.0.177 PDF and spot-checked the live repository artifacts that the manuscript cites. The scientific core is now much closer to publishable than v1.0.171–v1.0.175: the HC dipole is correctly labelled, the post-MASTER monopole-only null is correctly described in the main text, and the flip-identity QC closure is scientifically much improved. However, the paper still fails an acceptance-grade reproducibility/provenance check: the v1.0.177 PDF’s Data Availability section still identifies the repository state as v1.0.175 / commit 53b41d12, and the new catalog-wide QC artifact is not present at that pinned commit. 

chirality_catalog_paper_v177

 

chirality_catalog_paper_v177

 
Invalid URL

1. Closure verification
Original v1.0.171 BLOCKERS
ID	Status	Verification
B1 — exact source/PDF/artifact release mismatch	REGRESSION / PARTIAL	The PDF header is v1.0.177, but Data Availability still says “Repository state for this version: commit 53b41d12 (v1.0.175, June 2026).” The live main source also still has that stale Data Availability line, while its header is v1.0.177. Worse, the new catalog-wide QC artifact exists on main but is absent at the pinned 53b41d12 commit. This is still not a reproducible immutable release. 

chirality_catalog_paper_v177

 
GitHub
+1

B2 — post-MASTER monopole-only null misinterpreted	PARTIAL	The main Sec. IV.D correction is now essentially right: the 99.32% statement is explicitly pre-MASTER only; post-MASTER monopole-only reproduces only ~12% and leaves +4.84/+5.14σ residuals requiring coherent systematics. But the Methods hierarchy bullet still says the N=500 monopole-only null demonstrates the +3.64σ canonical value is “consistent with monopole-mask leakage,” which is stale and too broad for the post-subtraction/post-MASTER residual. 
GitHub
 

chirality_catalog_paper_v177


B3 — +3.64σ vs +7.93σ taxonomy	PARTIAL	The abstract and notation subsection correctly say the values are diagnostics from different null sizes/conventions and are not independent detections. But Conclusions VII.c still says the +3.64σ and +7.93σ values describe the “same physical estimator and footprint under different null-run sizes,” which contradicts the “not mutually comparable” taxonomy and Table III’s “distinct estimator” warning. 

chirality_catalog_paper_v177

 
GitHub

B4 — training-set accounting inconsistency	CLOSED	The paper now reconciles the 25,790 source images with the 26,616 post-augmentation pool and the n
train
	​

=21,293, n
val
	​

=5,323 split. 

chirality_catalog_paper_v177


B5 — WLS/template-fit exact-mask reproducibility	PARTIAL	The NSIDE block-bootstrap sensitivity calculation is now present and reassuring: z=−16.9,−18.4,−19.4 at NSIDE 4/8/16. But the committed bootstrap artifact still says its mask is ((
Original v1.0.171 MAJORS
ID	Status	Verification
M1 — HC confidence-cut dependence	CLOSED	The full/unthresholded z≃4.2−4.4 sensitivity diagnostic and the HC p
eq
	​

>0.6, N=949,584, +0.41σ null are now clearly separated in the abstract, Sec. IV.C, Fig. 7/8 captions, and conclusions. 

chirality_catalog_paper_v177


M2 — “three-interpretation closure” overclaim	CLOSED	The language is now mostly “systematics-attributed,” “most likely,” and “supporting,” not a hard cosmological/systematics closure claim.
M3 — ℓ=2 cross-spectrum underpowered	PARTIAL	The result remains r
ℓ=2
	​

=−0.65, z=−2.89, with a 200-realization permutation null. The language has softened to “supporting,” which is better, but the diagnostic remains statistically thin if it is one of the named eight anchors. 

chirality_catalog_paper_v177


M4 — WLS z≃−18 interpretation	CLOSED, subject to B5	The naive z=−264.5 is now explicitly superseded by the block-bootstrap z≃−18.1, and the NSIDE sensitivity check makes the exclusion much less brittle. The remaining problem is exact-mask/provenance reproducibility, covered under B5. 

chirality_catalog_paper_v177

 
GitHub

M5 — classifier calibration caveat	CLOSED	The paper consistently describes p
eq
	​

 as a ranking score, not a calibrated probability, and warns against sub-threshold precision parity use without local re-normalization. 

chirality_catalog_paper_v177


M6 — D4-TTA low-confidence/spatial validation	PARTIAL / NOT FULLY ADDRESSED	The two ∼2000-object D4 hold-outs remain, with mean P
CW
	​

 stability but 21.4% argmax flips on borderline galaxies. I still do not see a spatially stratified Z2-vs-D4 comparison on the actual low-confidence-tail dipole estimator. 

chirality_catalog_paper_v177


M7 — Shamir comparison overreach	NOT ADDRESSED	The manuscript still says the monopole-mask leakage channel “can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples.” This remains broader than the demonstrated DESI/ViT-Small-mask mechanism, even though the text also correctly says a matched Ganalyzer reanalysis is needed. 
GitHub

M8 — “largest catalogue” precision	CLOSED	The abstract and conclusions now consistently pair 8.47M total classified galaxies with 3.20M CW/CCW spirals. 

chirality_catalog_paper_v177

Later blocker/major items from my v1.0.174–v1.0.175 reports
Prior item	Status	Verification
QC-artifact consistency charge	CLOSED scientifically; PARTIAL as released	The scientific fix is now correct on main: the new catalog-wide artifact evaluates all 8,474,531 rows and reports 2.93899% any-channel violators, max bound excursion 0.090094, and max normalization deviation 4.26×10
−7
, matching the PDF narrative. The old intersection-only artifact now explains why it has zero violators, and the HC rerun artifact gives z=+0.516 baseline vs +0.475 with flagged rows excluded. But the artifact is not present at the PDF’s pinned 53b41d12 commit, so the release bundle is still incomplete. 
+3
GitHub
+3
GitHub
+3

HC Fisher-floor comparison	CLOSED	Sec. VI.A now gives both the full-sample ideal floor ∼0.29% and the HC-sample ideal floor ∼0.53%, and decomposes the empirical A
50
	​

 gap. 

chirality_catalog_paper_v177


High-confidence cuts misdescribed as face-on proxies	CLOSED	Appendix E now calls them high-confidence morphology-selected subsamples and explicitly says they are not validated inclination proxies. 

chirality_catalog_paper_v177


Appendix E “post-MASTER null-consistent” contradiction	CLOSED	Appendix E now states that monopole-only leakage explains the bulk of the pre-MASTER power but not the post-MASTER residual, which remains systematics-attributed. 

chirality_catalog_paper_v177


“All 8 tests pass” overstatement	PARTIAL / ACCEPTABLE WITH POLISH	Table VII still begins “All 8 tests pass,” but the caption now adds “necessary-but-not-sufficient” and the Appendix text gives the T1/T5/T7 scope caveats. This no longer rises to a major issue, but the phrase remains quote-prone. 

chirality_catalog_paper_v177

2. Fresh pass on v1.0.177 — new findings only
BLOCKERS
ID	Section/page	Finding	Proposed fix
FB-177-1	Data Availability, pp.20–21; public source/artifacts	The v1.0.177 PDF is not self-consistently pinned. The title page says v1.0.177, but Data Availability says the repository state is 53b41d12 / v1.0.175. The live v1.0.177 source on main also still has this v1.0.175 Data Availability line, while the new catalog-wide QC artifact exists only on main and 404s at the pinned 53b41d12 commit. This is the only remaining acceptance-level blocker, but it is real: a referee cannot reconstruct v1.0.177 from the manuscript’s cited release state. 

chirality_catalog_paper_v177

 
GitHub
+2
GitHub
+2
	Mint a final v1.0.177 release/DOI or tag after all metadata and QC artifacts are committed. The PDF, .tex, artifact links, and Data Availability section must all point to the same immutable release. Do not rely on a “rendered PDF is authoritative” exception for journal submission.
MAJORS
ID	Section/page	Finding	Proposed fix
FM-177-1	Sec. III.B, p.4; Sec. IV.D, pp.9–11	The hierarchy bullet still says the monopole-only null demonstrates the +3.64σ canonical value is consistent with monopole-mask leakage, while Sec. IV.D correctly says post-MASTER monopole-only explains only ~12% and the residual requires coherent systematics beyond monopole-only leakage. This is now an isolated stale sentence, but it sits in the declared analysis hierarchy. 

chirality_catalog_paper_v177

 
GitHub
	Replace the hierarchy bullet with: “Generative monopole-only null: demonstrates that the raw pre-MASTER pseudo-C
1
	​

 is dominated by monopole-mask leakage; post-MASTER residuals require additional coherent systematics.”
FM-177-2	Conclusions VII.c, p.14; Table III, p.11	The conclusion still says +3.64σ and +7.93σ are the same physical estimator/footprint under different null-run sizes, but Table III says the Sec. IV.C single-mode estimator is distinct and should not be numerically equated with the full 39-band Table III row. The text cannot simultaneously claim “not comparable” and “same estimator.” 

chirality_catalog_paper_v177

 
GitHub
	Change VII.c to: “The 500-MC +3.64σ direct single-mode value is retained for continuity with the leakage analysis; the 10
4
-permutation Table III canonical row is the high-statistics diagnostic under its committed field convention.”
FM-177-3	Sec. IV.D, p.10; Sec. V.A, p.12	The Shamir comparison remains too broad. The DESI/ViT-Small analysis demonstrates a mechanism that can generate comparable pre-MASTER artifacts under this pipeline and mask; it does not demonstrate reproduction of SDSS/Ganalyzer signals as actually measured. 
GitHub
	Replace “can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples” with “can generate a comparable pre-MASTER dipole-class artifact under this DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required.”
FM-177-4	Sec. IV.D, p.10; Appendix D.g, p.19	The text says the two primary estimators “bypass the canonical-mask leakage channel,” but the WLS template fit is explicitly on the canonical-mask A
p
	​

 field. It does not bypass the mask channel; it marginalizes a clean-dipole template against nuisance templates and spatially coherent bootstrap errors. 

chirality_catalog_paper_v177

	Reword to: “the HC real-space estimator bypasses the harmonic leakage channel, and the WLS estimator tests a clean-dipole template after nuisance marginalization on the canonical-mask field.”
FM-177-5	Appendix D.g artifact provenance	The WLS artifact still uses a (	b_{\rm gal}
MINORS
ID	Section/page	Finding	Proposed fix
fm-177-1	Discussion, p.12	“The signal is rejected as isotropic noise at p
LEE
	​

≤10
−4
” is logically backwards. A small p
LEE
	​

 rejects the isotropic random-label null; the signal is then attributed to systematic structure.	Replace with: “the direct-MC max-statistic null rejects isotropic random-label noise at p
LEE
	​

≤10
−4
, so the excess is classified as a systematic-floor artifact.”
fm-177-2	Fig. 2, p.6	The caption says the figure illustrates the eight D4 transforms, but the rendered panel shows original/flipped examples and raw/equivariant probability bars, not an explicit eight-transform D4 grid.	Reword to “representative Z2 production TTA examples; D4 validation is described in Appendix B,” or render the eight D4 transforms explicitly.
fm-177-3	Data Availability, p.21	The Zenodo DOI is still not minted. This is acceptable for an internal draft but not for acceptance-stage review.	Mint the DOI or provide an immutable archival tag before journal submission.
3. Updated recommendation

Recommendation: MAJOR REVISIONS.

The paper moved toward scientific publishability since v1.0.175—the flip-identity QC closure is now technically credible—but it remains blocked by a release/provenance failure: v1.0.177 still points readers to a v1.0.175 commit that lacks the newly required QC artifact.
