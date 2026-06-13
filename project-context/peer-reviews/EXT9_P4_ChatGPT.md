# EXT9 P4 — ChatGPT (in-thread delta round 9; recalibrated prompt)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37
**PDF**: chirality_catalog_paper_v183.pdf · harvested 2026-06-13 13:28 PT
---
Referee report on Paper 4 v1.0.183

Updated recommendation: MINOR REVISIONS

I read the full v1.0.183 PDF and spot-checked the live source/artifact paths for the remaining load-bearing concerns. The paper has now crossed the scientific threshold for publication: the main null result, post-MASTER interpretation, WLS exclusion framing, harmonic-completeness check, and QC disclosure are sufficiently supported. The remaining issues are release hygiene and a small WLS mask-audit arithmetic inconsistency; they should be fixed before final submission, but they do not require substantial scientific rework. 

chirality_catalog_paper_v183

1. Closure verification
A. Original BLOCKERS carried through my prior reports
ID	Status	Verification
B1 — exact source/PDF/artifact release mismatch	PARTIAL	Scientifically, the paper is now coherent, and the live main source is v1.0.183 with the harmonic-completeness figure in the text. However, Data Availability still pins 53b41d12 and describes it as v1.0.180, while the live source explains that the rendered PDF, not the in-repo source at the stamp hash, is authoritative. The source at 53b41d12 is actually v1.0.175 and points artifact links to an older hash. I also could not fetch the cited canonical_mask_nside64.npy from either main or 53b41d12 via the raw GitHub path. This is now a submission-packaging problem, not a scientific blocker, provided the final Zenodo/tagged release contains the PDF, .tex, figures, artifacts, catalog/model checksums, and scripts as one immutable bundle. 
+4
GitHub
+4
GitHub
+4

B2 — post-MASTER monopole-only null misinterpreted	CLOSED	The text now correctly states that the 99.32% monopole-only reproduction applies only to the raw pre-MASTER pseudo-C
ℓ
(ℓ=1)
	​

 power, while the post-MASTER monopole-only null reproduces only ∼12%, leaving +4.84σ/+5.14σ residuals requiring coherent depth/PSF/morphology systematics beyond monopole-only leakage. 

chirality_catalog_paper_v183


B3 — +3.64σ vs +7.93σ taxonomy	CLOSED	The conclusion now scopes +3.64σ as the 500-MC direct single-mode continuity diagnostic and +7.93σ as the current high-statistics canonical-table diagnostic under its committed field convention. The old “same physical estimator” ambiguity is gone. 

chirality_catalog_paper_v183


B4 — training-set accounting inconsistency	CLOSED	The 25,790 source images, 26,616 post-augmentation pool, and n
train
	​

=21,293, n
val
	​

=5,323 split are now reconciled; the 826-image delta is explicitly described as training-split-only flip augmentation. 

chirality_catalog_paper_v183


B5 — WLS exact-mask reproducibility	PARTIAL	The requested WLS mask-equivalence audit is now in the paper, and it states exact pixel-list identity between the NaMaster canonical mask and WLS artifact mask. However, the table still reports 24,061 pixels and f
sky
	​

=0.49005. At NSIDE=64, N
pix
	​

=49,152, so 24,061 pixels imply f
sky
	​

=0.48952, not 0.49005. This is a table/provenance correction, not a rerun-level scientific issue, but it should be corrected before final submission. 

chirality_catalog_paper_v183

B. Original MAJORS carried through my prior reports
ID	Status	Verification
M1 — HC confidence-cut dependence	CLOSED	The paper now cleanly separates the HC p
eq
	​

>0.6, N=949,584, +0.41σ null from the unthresholded z≃4.2−4.4, 0.57% low-confidence-tail systematic diagnostic.
M2 — “three-interpretation closure” overclaim	CLOSED	The canonical-mask residual is now consistently systematics-attributed rather than presented as a cosmological closure result.
M3 — ℓ=2 cross-spectrum underpowered	PARTIAL / acceptable	The ℓ=2 cross-spectrum remains a 200-realization diagnostic, but the language now treats it as one supporting anchor within a broader systematic battery, not as a stand-alone discriminator. That is acceptable for this paper.
M4 — WLS z≃−18 interpretation	CLOSED, subject to the table correction under B5	The naive z≃−264.5 is clearly superseded by the spatial block-bootstrap result, and the NSIDE 4/8/16 sensitivity remains stable at (
M5 — classifier calibration caveat too weak	CLOSED	The paper now states that p
eq
	​

 values are ranking scores, not calibrated probabilities, and repeatedly warns users against treating them as frequentist label probabilities.
M6 — D4-TTA spatial/low-confidence validation	PARTIAL / disclosed limitation	The D4 validation remains a two-∼2000-object hold-out, but the text now correctly says it is a classifier-stability check, not a survey-scale spatial-null or isotropy test. This limitation is adequately disclosed.
M7 — Shamir comparison overreach	CLOSED	The comparison is now properly scoped: the DESI/ViT-Small analysis can generate a comparable pre-MASTER artifact under this pipeline, while a matched Ganalyzer reanalysis remains required for a likelihood-level exclusion. 

chirality_catalog_paper_v183


M8 — “largest catalogue” precision	CLOSED	The abstract and conclusions consistently report both the 8,474,531 classified galaxies and N
spiral
	​

=3,201,160 CW/CCW spirals.
C. Fresh items from my v1.0.182 report
Prior item	Status	Verification
F182-B1 — release/provenance endpoint	PARTIAL	Same as B1. This should be closed by the final tagged/Zenodo release. I no longer view it as requiring major scientific revision, but I would not let the paper go to press without a single immutable archive.
F182-M1 — WLS mask-equivalence arithmetic	PARTIAL	The table is still arithmetically inconsistent: 24,061/49,152=0.48952, not 0.49005. Correct either the pixel count or the f
sky
	​

, and ensure the exact mask artifact is present in the archived release. 

chirality_catalog_paper_v183


F182-M2 — hemisphere look-elsewhere wording	PARTIAL / acceptable with polish	The prose now makes clear that the direct max-statistic MC is the principled look-elsewhere control, while Bonferroni/BH are conservative heuristics. Table I still says the two “bracket the significance,” which is conceptually untidy, but this is not load-bearing for the main null result.
Harmonic-completeness visibility	CLOSED	Fig. 9 is now in the paper, generated from the injection-recovery artifact. It shows the axis-averaged recovery curve, P(≥3σ)=0.92 at A
p
	​

=0.5%, saturation by A
p
	​

=0.75%, and separates the harmonic-channel convention from the real-space falsification boundary. The underlying artifact reports 1000 injections per amplitude per axis, seed 42, and values matching the figure/table narrative. 

chirality_catalog_paper_v183

 
GitHub
2. Fresh pass on v1.0.183 — new findings only
BLOCKERS

None. I found no new scientific blocker.

MAJORS

None. The remaining substantive issues are now bounded to release packaging and a WLS mask-audit table correction.

MINORS
ID	Location	Finding	Proposed fix
m183-1	Fig. 9, p.14	The figure title reports the observed harmonic-channel value as about 7.21σ, while the surrounding text and Table VI use +7.28σ. The artifact contains both sigma_data = 7.207... and c3_reference_sigma = 7.28, so this is traceable, but readers will see a mismatch. 

chirality_catalog_paper_v183

 
GitHub
	Add “artifact raw z=7.21; rounded/reference value +7.28σ” in the caption, or use one convention throughout Fig. 9/Table VI.
m183-2	Table XI, p.20	The WLS mask-equivalence table’s pixel count and f
sky
	​

 are internally inconsistent, as noted above. This is a minor correction only if the pixel-list identity and WLS result are unchanged.	Correct the table and archive the exact binary mask or pixel list in the final release.
m183-3	Data Availability, p.21	The final article should not rely on “rendered PDF is authoritative over the in-repo source at the stamp hash.” That is understandable for internal iteration, but awkward for journal reproducibility.	At submission, replace this with a single DOI/tag statement for the final immutable bundle.
3. Updated recommendation

Recommendation: MINOR REVISIONS.

The manuscript moved decisively toward publishability: the scientific case is now coherent and adequately controlled, and the remaining changes are final-release/provenance cleanup plus small table/figure consistency fixes rather than substantial scientific rework.
