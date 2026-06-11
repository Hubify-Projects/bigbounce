# EXT4 P4 — ChatGPT Pro Extended (in-thread delta round 4)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37
**PDF**: chirality_catalog_paper_v175.pdf (8ad2cdfb) · harvested 2026-06-11 15:54 PT
---
Referee report on Paper 4 v1.0.175

Updated recommendation: MAJOR REVISIONS

The paper moved toward publishability in scientific interpretation, especially on the HC-sample labeling, A95 falsification boundary, Appendix E morphology wording, and the explicit QC treatment. However, v1.0.175 introduces or exposes a new acceptance-blocking reproducibility inconsistency: the PDF’s flip-identity QC narrative is not consistent with the committed QC artifact it cites. The paper is now scientifically close, but the release/provenance layer still fails the standard I would require before recommending acceptance. 

chirality_catalog_paper_v175

1. Closure verification
A. Immediate v1.0.174 findings
Prior item	Status	Verification
FB1 — Data Availability / source-PDF provenance	PARTIAL	The PDF now states commit 53b41d12 for v1.0.175 and explains the two-step stamp-then-pin protocol, with the rendered PDF treated as authoritative. That is transparent. But the .tex stored at 53b41d12 still cites 81c67790 in Data Availability and has artifact links hard-coded to blob/81c67790; the current main source has the expected 53b41d12 pin. This is an improvement, but still not a clean immutable source/PDF pair. 

chirality_catalog_paper_v175

 
GitHub
+2
GitHub
+2

FM1 — +0.41σ mislabeled as full-catalog rather than HC	CLOSED	The major stale “full-catalog” mislabel is gone from the body and figure-caption load-bearing sites. The headline is now consistently the HC p
eq
	​

>0.6, N=949,584 estimator in the key places. 
GitHub

FM2 — A50 used as falsification/disfavoring boundary	CLOSED	Sec. VI.B and the conclusions now separate A
50
	​

≈0.75% from A
95
	​

∈(1.0%,1.5%]. This fixes the previous overstatement. 

chirality_catalog_paper_v175


FM3 — Hemisphere look-elsewhere treatment	PARTIAL	Discussion now says the direct-MC max-statistic null is the principled directional LEE control, while Bonferroni/BH are conservative heuristics. That is better. Table I and Appendix C still conflate “post-look-elsewhere” with two incompatible correction philosophies: direct max-stat MC gives p
LEE
	​

≤10
−4
, while Bonferroni/BH are said to bracket below <1σ. 
GitHub

FM4 — “Mutual consistency” of +0.41σ and +7.28σ	CLOSED	The problematic “mutual consistency is established” wording is gone. The text now correctly says the harmonic-completeness check bounds what a clean Shamir-class dipole would produce and does not establish statistical consistency of the two measured estimators on a common axis. 
GitHub

FM5 — “All 8 tests pass” overstatement	PARTIAL	The caveat “necessary but not sufficient” is now present, but Table VII still leads with “All 8 tests pass.” This is less dangerous than before, but still quote-bait.
NF-M1 — Flip-identity QC / float32 issue	REGRESSION / PARTIAL	The PDF now correctly stops attributing >10
−3
 excursions to float32 and says 2.9% of rows have any-channel out-of-range recovered flip probabilities, with 59,515 HC rows excluded in a robustness rerun. But the committed artifact ext3_nfm1_flip_identity_qc.json says zero rows violate beyond 10
−3
, only 88,278 rows were evaluated, and no QC flag or row exclusion is required; the companion rerun artifact says 59,515 HC rows were flagged and exclusion changes z=0.516→0.475. These artifacts contradict both each other and the PDF. 

chirality_catalog_paper_v175

 
GitHub
+1

NF-M2 — HC Fisher floor missing	CLOSED	Sec. VI.A now gives the full-sample ideal 3σ floor ≈0.29%, the HC-sample ideal floor ≈0.53%, and decomposes the empirical A
50
	​

 gap into sample-size, footprint, and classification-noise terms. 
GitHub

NF-M3 — p
eq
	​

 cuts described as face-on/low-inclination proxies	CLOSED	Appendix E now calls the p
eq
	​

>0.6 and p
eq
	​

>0.8 cuts “high-confidence morphology-selected subsamples” and explicitly says they are not validated inclination proxies. 

chirality_catalog_paper_v175


NF-M4 — Appendix E claimed subtraction/MASTER made the residual null-consistent	CLOSED	Appendix E now says monopole subtraction leaves +3.64σ, MASTER monopole-only reproduces only ∼12%, and the residual remains +4.84σ, systematics-attributed. That fixes the previous contradiction. 
GitHub
B. Inherited v1.0.171 blocker/major items still tracked
Prior item	Status	Verification
B1 — Exact source/PDF/artifact release mismatch	PARTIAL	The two-step protocol is disclosed, and current main has the desired 53b41d12 artifact pin. But the actual 53b41d12 source cannot reproduce the uploaded PDF’s Data Availability section because it still cites 81c67790. A DOI/tag snapshot can close this; the PDF alone should not be the only authoritative carrier. 
GitHub
+1

B2 — Post-MASTER monopole-only null interpretation	PARTIAL	The main scientific correction is now right: 99.32% is pre-MASTER only, post-MASTER monopole-only leaves a non-null residual. But the analysis-hierarchy bullet still says the +3.64σ canonical value is “consistent with monopole-mask leakage,” which remains too strong for the post-subtraction/post-MASTER residual. 
GitHub
+1

B3 — +3.64σ vs +7.93σ taxonomy	PARTIAL	The notation section and Table III caveats are good, but the conclusion still says the two values describe the “same physical estimator and footprint under different null-run sizes,” while earlier text says they are not mutually comparable. This remains internally muddy. 
GitHub

B4 — Training-set accounting	CLOSED	The 25,790 source images, 26,616 augmented pool, and n
train
	​

=21,293, n
val
	​

=5,323 accounting are now reconciled. 

chirality_catalog_paper_v175


B5 — WLS exact-mask reproducibility	PARTIAL	NSIDE block sensitivity is computed and reassuring: z=−16.9,−18.4,−19.4 for NSIDE 4,8,16. But joint_nuisance_bootstrap_sigma.json still says the bootstrap mask is ((
M1 — HC confidence-cut dependence	CLOSED	The full-sample/unthresholded z≃4.2−4.4 diagnostic and the HC +0.41σ null are now clearly separated. 
GitHub

M2 — Three-interpretation closure overclaim	CLOSED	The paper now mostly uses “systematics-attributed,” “most likely,” and “supporting,” rather than claiming hard closure.
M3 — ℓ=2 cross-spectrum underpowered	PARTIAL	The language is softened to “supporting,” but the cross-spectrum still rests on a 200-realization permutation null and remains one of the named anchors. 
GitHub

M4 — WLS z=−18 interpretation	CLOSED, subject to B5	The naive z≃−264 is clearly superseded by block bootstrap, and NSIDE sensitivity was computed. Exact-mask reproducibility remains under B5.
M5 — Classifier calibration caveat	CLOSED	The paper now clearly states p
eq
	​

 values are ranking scores, not calibrated probabilities. 

chirality_catalog_paper_v175


M6 — D4-TTA spatial/low-confidence validation	PARTIAL / NOT FULLY ADDRESSED	The same two ∼2000-object D4 hold-outs remain. I still do not see a spatially stratified Z2-vs-D4 comparison on the actual low-confidence-tail dipole estimator.
M7 — Shamir comparison overreach	NOT ADDRESSED	The text still says the DESI/ViT-Small monopole-mask leakage channel “can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples.” That remains broader than demonstrated without a matched Ganalyzer run. 
GitHub

M8 — “Largest catalogue” precision	CLOSED	The abstract and conclusions consistently pair 8.47M total galaxies with the 3.20M spiral chirality sub-catalogue. 

chirality_catalog_paper_v175

2. Fresh pass on v1.0.175 — new findings only
BLOCKERS
ID	Section/page	Finding	Proposed fix
FB-175-1	Appendix B, p.16–17; cited artifacts	The new flip-identity QC closure is not reproducible from the committed artifacts. The PDF says: 2.9% of rows have any-channel recovered flip probability outside [0,1], the excursions are not float32 rounding, a QC flag identifies affected rows, and excluding 59,515 HC rows leaves the dipole null-consistent. But ext3_nfm1_flip_identity_qc.json says only 88,278 rows were evaluated, zero rows violate beyond 10
−3
, and no QC flag or row exclusion is required. The companion rerun artifact then uses 59,515 flagged HC rows. This is internally inconsistent. 

chirality_catalog_paper_v175

 
GitHub
+1
	Publish one canonical QC artifact and one canonical rerun artifact generated by the same flag definition on the same released catalog columns. The artifact must state: columns used, missing-column policy, total rows, evaluated rows, flagged rows, HC-flagged rows, max excursions, and the exact rerun sample sizes. Until then, the Appendix B QC disclosure should not be treated as closed.
MAJORS
ID	Section/page	Finding	Proposed fix
FM-175-1	Data Availability, p.21; source at pinned commit	The paper now explicitly makes the rendered PDF, not the .tex at the pinned commit, the authoritative carrier of the pin. That is transparent, but it is not a journal-grade reproducibility endpoint: an external reader should be able to retrieve one immutable source/PDF/artifact bundle, not infer a two-step stamp/pin workflow. This is related to the earlier provenance issue but sharpened by the new Data Availability wording. 

chirality_catalog_paper_v175

 
GitHub
+1
	Mint the Zenodo release before submission, or cite the post-pin commit/tag that contains the correct .tex, PDF, and artifact links. The PDF should not say the source at the cited commit is expected to disagree with the PDF.
FM-175-2	Conclusion VII.c, p.14	The conclusion still says +3.64σ and +7.93σ are the “same physical estimator and footprint under different null-run sizes.” This undermines the improved notation section, which says the values are from different null-run sizes and mask/weight conventions and are not mutually comparable. 
GitHub
	Replace with: “The 500-MC +3.64σ direct single-mode value is retained for continuity with the leakage analysis; the 10
4
-permutation Table III canonical row is the current high-statistics diagnostic under its committed field convention.”
FM-175-3	Sec. V.A, p.12	The Shamir comparison remains overbroad: “can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples” reads as a cross-survey explanation, while the demonstrated mechanism is under this DESI/ViT-Small pipeline and mask. 
GitHub
	Use: “can generate a comparable pre-MASTER dipole-class artifact under this DESI/ViT-Small pipeline; a matched Ganalyzer test remains required.”
MINORS
ID	Section/page	Finding	Proposed fix
fm-175-1	Fig. 2, p.6	The caption says the figure illustrates the eight D4 transforms, but the rendered figure shows original/flipped examples and probability bars, not an explicit eight-transform D4 grid.	Reword the caption to say the figure illustrates the 2-fold production TTA and representative D4-validation context, or change the figure to show all eight D4 transforms explicitly.
fm-175-2	Table VII, p.17	The caption still begins “All 8 tests pass,” even though the text correctly says T1 is an implementation check, T5 is not a directional-coupling pass criterion, and T7 is only a confidence-mass proxy.	Change to “All implemented engineering checks meet their stated thresholds; these are necessary but not sufficient for sub-percent isotropy control.”
fm-175-3	Data Availability, p.21	The Zenodo DOI is still not minted. This is acceptable for an internal draft but not for acceptance-stage review.	Mint DOI or provide an immutable archival tag before journal submission.
3. Updated recommendation

Recommendation: MAJOR REVISIONS.

The paper moved toward publishability in the scientific narrative, but the v1.0.175 QC-artifact contradiction and the still-non-immutable source/PDF/artifact release prevent a minor-revision recommendation.
