# EXT7 P4 — ChatGPT Pro Extended (in-thread delta round 7; Gemini = fresh thread)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37
**PDF**: chirality_catalog_paper_v181.pdf (f5867e653f02488a) · harvested 2026-06-13 ~03:19 PT
---

Recommendation: MAJOR REVISIONS

The paper has moved toward publishability since v1.0.179: most of the scientific/statistical issues I previously raised are now closed in the manuscript text. The remaining acceptance blocker is still the release/provenance layer: the v1.0.181 PDF does not yet point to a single immutable source/PDF/artifact bundle that reconstructs the paper being reviewed.

I read the full v1.0.181 PDF and spot-checked the public source/artifacts where the manuscript’s claims are load-bearing. I did not rerun the full 8.47M-object pipeline. 

chirality_catalog_paper_v181

1. Closure verification of original BLOCKERS / MAJORS
Original BLOCKERS
ID	Status	Verification
B1 — exact source/PDF/artifact release mismatch	PARTIAL — still acceptance-blocking	The PDF is v1.0.181, but Data Availability says “Repository state for this version” is commit 53b41d12 / v1.0.180 and explicitly makes the rendered PDF, not the .tex at the stamp hash, authoritative. That is transparent, but still not a journal-grade immutable release. The public main source is v1.0.181 and links artifacts through blob/53b41d12, while the .tex at 53b41d12 still has Data Availability pointing to 81c67790 / v1.0.174; the catalog-wide QC artifact exists on main but 404s at 53b41d12. 

chirality_catalog_paper_v181

 
GitHub
+2
GitHub
+2

B2 — post-MASTER monopole-only null misinterpreted	CLOSED	The main text now clearly distinguishes the pre-MASTER 99.32% monopole-mask leakage reproduction from the post-MASTER behavior: the post-MASTER monopole-only null reproduces only ∼12% and leaves +4.84σ / +5.14σ residuals requiring coherent depth/PSF/morphology systematics beyond monopole-only leakage.
B3 — +3.64σ vs +7.93σ taxonomy	CLOSED	The abstract, notation subsection, Table III caption, and conclusions now consistently treat +3.64σ as a 500-MC direct single-mode continuity diagnostic and +7.93σ as the current high-statistics canonical-table diagnostic, not as two independent detections or the same number under trivial null-size variation. 

chirality_catalog_paper_v181


B4 — training-set accounting inconsistency	CLOSED	The paper now reconciles the 25,790 source images with the 26,616 post-augmentation pool, explicitly saying the 826-image delta comes from horizontal-flip augmentation of the training split only, while the validation split is never augmented. 

chirality_catalog_paper_v181


B5 — WLS/template-fit exact-mask reproducibility	PARTIAL	The NSIDE block-bootstrap sensitivity is computed and reassuring: z=−16.9,−18.4,−19.4 across NSIDE 4/8/16, so the exclusion is not single-block-scale brittle. However, the primary bootstrap artifact still says its mask is ((
Original MAJORS
ID	Status	Verification
M1 — HC confidence-cut dependence	CLOSED	The paper now clearly separates the HC p
eq
	​

>0.6, N=949,584, +0.41σ null from the unthresholded z≃4.2−4.4, 0.57% systematics-sensitivity excess. The confidence-cut sweep is now central rather than hidden.
M2 — “three-interpretation closure” overclaim	CLOSED	The wording is now “systematics-attributed,” “supporting,” and “most likely,” rather than a hard closure claim.
M3 — ℓ=2 cross-spectrum underpowered	PARTIAL / acceptable with caveat	The ℓ=2 result remains based on a 200-realization permutation null, but the paper now presents it as supporting evidence within a broader eight-anchor systematics battery. That is acceptable if the authors keep it framed as a diagnostic, not a standalone confirmation. 

chirality_catalog_paper_v181


M4 — WLS z≃−18 interpretation	CLOSED, subject to B5	The naive WLS z≃−264.5 is now clearly superseded by the block-bootstrap z≃−18, and the NSIDE sensitivity computation supports robustness. The remaining concern is exact-mask reproducibility, already covered by B5. 

chirality_catalog_paper_v181


M5 — classifier calibration caveat too weak	CLOSED	The paper now repeatedly states that p
eq
	​

 values are ranking scores, not calibrated probabilities, and quotes the large gap between mean confidence and independent GZ1 accuracy. 

chirality_catalog_paper_v181


M6 — D4-TTA spatial/low-confidence validation	PARTIAL / limitation remains	The paper still uses two ∼2000-object D4 hold-outs, with mean P
CW
	​

 stable but 21.4% argmax flips on borderline galaxies. I still do not see a spatially stratified Z2-vs-D4 comparison on the low-confidence-tail dipole estimator. This is no longer a blocker because the low-confidence tail is explicitly systematics-attributed, but it remains a limitation. 

chirality_catalog_paper_v181


M7 — Shamir comparison overreach	CLOSED in Sec. V.A; minor residue noted below	The previous overbroad phrasing in the comparison section is fixed: it now says the mechanism can generate a comparable pre-MASTER artifact under this DESI/ViT-Small pipeline, with matched Ganalyzer reanalysis still required. 

chirality_catalog_paper_v181


M8 — “largest catalogue” precision	CLOSED	The abstract and conclusions consistently pair the 8.47M classified-galaxy release with the 3.20M CW/CCW spiral sub-catalogue. 

chirality_catalog_paper_v181

Later carryover items from my v1.0.175–v1.0.179 reviews
Item	Status	Verification
Flip-identity QC artifact inconsistency	CLOSED scientifically; PARTIAL as release-pinned	The catalog-wide QC artifact on main now evaluates all 8,474,531 rows and matches the manuscript’s anchors: 2.94% any-channel violators, 1.57% CW-channel violators, max bound excursion 0.0901, and max normalization deviation 4.26×10
−7
. The HC dipole remains null-consistent after excluding flagged rows. However, this artifact is still absent at the PDF’s pinned 53b41d12 commit. 

chirality_catalog_paper_v181

 
GitHub
+1

Fig. 2 D4-caption mismatch	CLOSED	The v1.0.181 PDF caption now correctly describes the figure as representative Z2 production TTA examples and sends D4 validation to Appendix B. 

chirality_catalog_paper_v181


Shamir wording in Sec. V.A	CLOSED	The revised phrase is appropriately scoped to “this DESI/ViT-Small pipeline,” with matched Ganalyzer reanalysis still required. 

chirality_catalog_paper_v181


Table IV erroneous “sr” unit	CLOSED in source; PDF search did not show the old “sr” string in v1.0.181	The public main source now says “A
p
	​

-map ×10
−6
 units,” not “sr scale.” 
GitHub

A
95
UL
	​

 naming	PARTIAL / polish	The symbol is now A
95,nq
	​

 in the real-space section, with the null-quantile/no-coverage caveat. But the prose still introduces it under “formal upper limit,” which invites exactly the confusion the rename was meant to avoid.
2. Fresh pass on v1.0.181 — new or still-open findings only
BLOCKERS
ID	Section/page	Finding	Proposed fix
B-181-1	Data Availability, p.21; public source/artifacts	The release remains non-immutable. The PDF is v1.0.181 but pins 53b41d12 / v1.0.180; the source at that pinned hash does not contain the v1.0.181 Data Availability text and still cites an older commit; the current source’s artifact macro points to 53b41d12; the catalog-wide QC artifact required by the paper is present on main but absent at the pinned hash. This is now the only true acceptance blocker. 

chirality_catalog_paper_v181

 
GitHub
+2
GitHub
+2
	Create one final immutable release/tag/DOI after all metadata and artifacts are committed. The PDF, .tex, figures, scripts, JSON/NPY artifacts, catalog/model checksums, and all artifact hyperlinks must point to the same release. Remove the “rendered PDF is authoritative over the in-repo source at the stamp hash” exception before journal submission.
MAJORS
ID	Section/page	Finding	Proposed fix
M-181-1	Appendix D.g / Table IX, p.19; WLS bootstrap artifact	The WLS exclusion is now statistically well framed, but the exact-mask equivalence is still not visible in the paper. The artifact states that the bootstrap used a (	b_{\rm gal}
M-181-2	Table I, p.5; Appendix C.c, p.18	The hemisphere look-elsewhere treatment remains conceptually cluttered. The direct max-statistic MC null already incorporates the 648-direction scan and gives p
LEE
	​

≤10
−4
; Bonferroni/BH over per-direction p-values are a different heuristic, not a second estimate of the same “post-LEE significance.” The prose is much better than before, but Table I still says row (v) reports “post-look-elsewhere-corrected significance” while mixing the direct-MC and Bonferroni/BH interpretations.	Split the table/caption into two diagnostics: “direct max-statistic MC: rejects random-label isotropic null, p
LEE
	​

≤10
−4
, systematics-attributed” and “per-direction Bonferroni/BH heuristic: <1σ.” Do not call both together one post-LEE significance.
M-181-3	Sec. IV.D, p.10	One sentence still says the prior literature’s pre-MASTER dipole-detection claims are “explained at the percent level” by this leakage channel under the DESI/ViT-Small pipeline. Sec. V.A now uses the correct narrower language, but this earlier sentence can still be read as explaining Shamir/Ganalyzer directly.	Reword to match Sec. V.A: “This demonstrates a mechanism that can generate a comparable pre-MASTER dipole-class artifact under this DESI/ViT-Small pipeline; it does not constitute a matched Ganalyzer/SDSS explanation.”
M-181-4	Sec. IV.C, p.9; Conclusions VII.c, p.14	The harmonic-completeness statement is load-bearing enough to deserve an in-paper mini-table. The text says a clean Shamir-class real-space dipole would register at z≃68−218 in the MASTER channel and the abstract quotes P(≥3σ)≥0.999 at A
p
	​

=0.75%, but the supporting information is still only an artifact reference. 

chirality_catalog_paper_v181

	Add a small table or figure with injected amplitude, recovery probability, null convention, and expected MASTER z range. This does not need to be a major new computation; it just needs to make the argument visible to readers.
MINORS
ID	Section/page	Finding	Proposed fix
m-181-1	Sec. IV.C, p.7	A
95,nq
	​

 is now renamed correctly, but the sentence still begins “formal upper limit.” That phrase is too strong for a null-quantile with no coverage guarantee.	Replace “formal upper limit” with “formal null-quantile benchmark” or “descriptive null-quantile bound.”
m-181-2	Table VII, p.17	“All 8 tests pass” remains quote-prone, even with the caveat that the tests are necessary but not sufficient.	Change the caption opener to “All implemented engineering checks meet their stated thresholds.”
m-181-3	Data Availability, p.21	Zenodo DOI remains unminted. This is acceptable for an internal draft but not for acceptance-stage publication. 

chirality_catalog_paper_v181

	Mint DOI or provide a permanent archival release before submission/acceptance.
m-181-4	Appendix B.c, p.16–17	D4 validation remains small-sample and borderline-argmax-focused. The limitation is disclosed, but a reader may overinterpret it as a survey-scale rotation systematic null. 

chirality_catalog_paper_v181

	Add one sentence: “This D4 hold-out is not a survey-scale spatial systematic null; the low-confidence-tail spatial systematics are instead assessed by the confidence-cut and harmonic diagnostics.”
3. Updated recommendation

Recommendation: MAJOR REVISIONS.

The manuscript moved toward publishability and is now scientifically close, but I would not recommend acceptance until the authors produce a single immutable v1.0.181 release bundle and add a paper-level WLS mask-equivalence audit.
