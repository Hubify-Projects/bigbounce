# EXT3 P4 — ChatGPT in-thread delta review (round 3)
**Provider**: chatgpt.com Big Bounce Book project · Pro Extended
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37
**PDF**: chirality_catalog_paper_v174.pdf · **Harvested**: 2026-06-11 ~02:50 PT

---

Show more
Thought for 9m 40s
Referee report on Paper 4 v1.0.174

Updated recommendation: MAJOR REVISIONS

The revision moved slightly toward publishability since v1.0.173: the A95 falsification boundary is now aligned with the paper’s own recovery criterion, and the main Fig. 8/Sec. IV.D HC-labeling fix is real. However, the paper is still not ready for acceptance because the advertised PDF/source provenance remains internally inconsistent, and several stale statements still undercut the main estimator hierarchy.

I read the full v1.0.174 PDF end-to-end and also spot-checked the public .tex and committed JSON artifacts at the PDF’s stated commit.

1. Closure verification

I treat the closure set as the full prior-review issue list: the fresh v1.0.173 findings plus the inherited v1.0.171 blocker/major items.

A. Closure of the fresh v1.0.173 blocker/major findings
ID	Status	Verification
FB1 — Data Availability / source-PDF provenance	REGRESSION / PARTIAL	The uploaded PDF now says Data Availability is commit 81c67790 for v1.0.174, with HC-broad N=949,584, p
eq
	​

>0.6, and +0.41σ. 

chirality_catalog_paper_v174

 But the public .tex at commit 81c67790 still says the Data Availability commit is 297aa805 / v1.0.173, while defining \paperVersion{v1.0.174}. The same source also defines artifact hyperlinks through mutable blob/main, not the pinned commit. 
GitHub
+1
 Fix: restamp once more so the PDF and the exact .tex at the cited commit agree, and change all artifact links to DOI or commit-pinned paths.
FM1 — +0.41σ mislabeled as full-catalog rather than HC	PARTIAL / REGRESSION	The two headline body sites you named are improved: Fig. 8/Sec. IV.D now explicitly call the +0.41σ result the HC p
eq
	​

>0.6, N=949,584 estimator. 

chirality_catalog_paper_v174

 However, Fig. 7 still says the Catalog C real-space dipole “collapses to 0.41σ” without the HC qualifier, Discussion repeats the same comparison, and Appendix E explicitly calls +0.41σ “equivariant, full sample.” 
GitHub
 Fix: every occurrence of +0.41σ must say “HC p
eq
	​

>0.6” unless it is immediately adjacent to the unthresholded z≃4.2−4.4 diagnostic.
FM2 — A50 used as falsification/disfavoring boundary	CLOSED	The abstract and Sec. VI.B now separate 50%-recovery sensitivity from the falsification boundary A
95
	​

∈(1.0%,1.5%]. The old “disfavors ≥0.75%” overstatement is gone from the parity-translation paragraph. 

chirality_catalog_paper_v174

 
GitHub

FM3 — Hemisphere look-elsewhere treatment	NOT ADDRESSED	The paper still says the direct max-statistic MC look-elsewhere test gives p
LEE
	​

≤10
−4
, then says Bonferroni/BH reduce the post-LEE significance to <1σ. These are not the same correction; the max-statistic MC is the correct LEE control if the statistic is the scanned maximum. 
GitHub
 Fix: make the direct max-statistic MC the primary hemisphere result and move Bonferroni/BH to a heuristic/non-primary note.
FM4 — “Mutual consistency” of +0.41σ and +7.28σ	NOT ADDRESSED	Sec. IV.C still says their “mutual consistency is established” by the harmonic-completeness check. That check shows a Shamir-class dipole would be much larger in the harmonic channel; it does not make the two measured estimators statistically consistent on a common axis. 
GitHub
 Fix: replace with “the harmonic-completeness check bounds what a clean Shamir-class dipole would have produced in the MASTER channel.”
FM5 — “All 8 tests pass” overstatement	PARTIAL	The text now says the tests are necessary but not sufficient, which is the right direction. However, Table VII still says simply “All 8 tests pass,” while T1 is an implementation check, T5 is not counted as a directional-coupling pass criterion, and T7 is only a confidence-mass proxy. 
GitHub
 Fix: change the table caption to “All implemented engineering checks meet their stated thresholds; these are not a complete sub-percent systematics null suite.”
B. Closure of inherited v1.0.171 blocker/major items
ID	Status	Verification
B1 — Exact source/PDF/artifact release mismatch	REGRESSION / PARTIAL	Same as FB1. The uploaded PDF’s Data Availability says 81c67790; the public .tex at 81c67790 says 297aa805 / v1.0.173. 

chirality_catalog_paper_v174

 
GitHub

B2 — Post-MASTER monopole-only null interpretation	PARTIAL	The central scientific correction is now in Sec. IV.D and Table IV: the 99.32% result is explicitly pre-MASTER only, while the post-MASTER monopole-only null is +4.84σ, ∼12% reproduction, with 10
4
 confirmation +5.14σ. 

chirality_catalog_paper_v174

 
GitHub
+1
 Remaining stale statements: the hierarchy bullet still says the +3.64σ canonical value is “consistent with monopole-mask leakage,” and Appendix E says subtraction/MASTER makes the residual “null-consistent.” 
GitHub
+1

B3 — +3.64σ vs +7.93σ taxonomy	PARTIAL	The notation subsection and Table III caption are much better: they distinguish null-run sizes, field conventions, and non-comparability. But the conclusion still says +3.64σ and +7.93σ are the “same physical estimator and footprint under different null-run sizes.” 
GitHub
+1
 Fix: call +3.64σ the legacy 500-MC continuity diagnostic, or call both separately named estimators; do not mix those two descriptions.
B4 — Training-set accounting	CLOSED	Sec. II.B now reconciles 25,790 source images with the 26,616 training pool after flip augmentation, with n
train
	​

=21,293, n
val
	​

=5,323. The committed training-semantics artifact supports this. 
GitHub
+1

B5 — WLS exact-mask reproducibility	PARTIAL	The NSIDE block-bootstrap sensitivity calculation is now present and strong: z=−16.9,−18.4,−19.4 at NSIDE 4,8,16. 
GitHub
 But the bootstrap artifact still says it uses ((
M1 — HC confidence cut dependence	PARTIAL / REGRESSION	The HC/full-sample distinction is much clearer in Sec. IV.C and Data Availability, but stale “full sample” language remains in Fig. 7/Discussion/Appendix E. 
GitHub

M2 — Three-interpretation closure overclaim	CLOSED	The paper now mainly says “systematics-attributed,” “most likely,” and “requires coherent depth/PSF/morphology systematics,” which is appropriate. 
GitHub
+1

M3 — ℓ=2 cross-spectrum underpowered	PARTIAL	The ℓ=2 result remains r=−0.65, z=−2.89, but still uses only 200 permutation realizations and still says “confirming” rather than “supporting.” 
GitHub
+1

M4 — WLS z=−18 interpretation	CLOSED, subject to B5	The naive z=−264.5 is clearly superseded by block bootstrap, and NSIDE sensitivity is now computed. The remaining problem is exact-mask reproducibility, covered by B5. 
GitHub
+1

M5 — Classifier calibration caveat	CLOSED	The paper clearly states that p
eq
	​

 values are ranking scores, not calibrated probabilities, and warns against using the catalog below the empirical threshold without local re-normalization.
M6 — D4-TTA spatial/low-confidence validation	PARTIAL / NOT FULLY ADDRESSED	The D4 hold-out is still only two ∼2000-object samples with 21.4% argmax flips on borderline galaxies; I do not see a spatially stratified Z2-vs-D4 low-confidence-tail comparison on the actual dipole estimator.
M7 — Shamir comparison overreach	NOT ADDRESSED	The paper still says the DESI/ViT-Small leakage channel “can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples.” That remains too broad without a matched Ganalyzer analysis. 
GitHub

M8 — “Largest catalogue” precision	CLOSED	The abstract and conclusions consistently state both 8.47M total galaxies and 3.20M spiral chirality sub-catalogue size. 

chirality_catalog_paper_v174

2. Fresh pass on v1.0.174 — new findings only
BLOCKERS

No new blocker beyond the still-open provenance/source mismatch above. That mismatch remains acceptance-blocking.

MAJORS
ID	Section/page	Finding	Proposed fix
NF-M1	Appendix B, p.16	The paper says the flip-pass probabilities are recovered “exactly” from stored raw and 2-fold-TTA columns, but then says 1.3% of rows violate the identity beyond 10
−3
 and attributes this to float32 storage. Float32 rounding is far below 10
−3
 for probabilities in [0,1]; a 1.3% tail above 10
−3
 is a real data/serialization/pipeline-consistency issue, not a normal float32 effect. 
GitHub
	Quantify the full residual distribution, identify the affected rows, add a QC flag, and rerun the HC dipole with those rows removed or downweighted. Do not call >10
−3
 discrepancies “consistent with float32” unless an explicit serialization/rounding analysis proves it.
NF-M2	Sec. VI.A, pp.12–13	The Fisher floor uses N
spiral
	​

=3,201,160, giving a 3σ ideal floor of ∼0.29%, while the empirical recovery curve is for the HC sample N=949,584. The text then attributes the gap mainly to classification noise. But the HC sample-size reduction alone raises the ideal 3σ floor to ∼3
3/949584
	​

≃0.53%. 
GitHub
+1
	Add an HC-sample Fisher floor row and decompose the 0.75% empirical A50 into sample-size loss, footprint/axis geometry, and classification/systematics degradation.
NF-M3	Appendix E, p.19	The paper uses p
eq
	​

>0.6 and p
eq
	​

>0.8 as “proxies for face-on (low-inclination) subsamples,” while the actual axis-ratio cross-match is explicitly deferred. Confidence is not a demonstrated inclination proxy, especially after the paper reports substantial edge-on contamination. 
GitHub
	Reword to “high-confidence morphology-selected subsamples” unless a b/a-based cross-match is performed. Do not use “face-on” or “low-inclination” without direct axis-ratio evidence.
NF-M4	Appendix E footnote, p.19	The footnote says that with subtraction or MASTER deconvolution “the leakage is removed and the residual is null-consistent.” This contradicts the paper’s corrected Sec. IV.D result that post-MASTER monopole-only nulls leave +4.84σ / +5.14σ residuals requiring coherent systematics beyond monopole-only leakage. 
GitHub
+1
	Replace with: “mean subtraction and MASTER deconvolution reduce the pure monopole leakage; the remaining post-MASTER residual is non-null and systematics-attributed.”
MINORS
ID	Section/page	Finding	Proposed fix
NF-m1	Fig. 7 caption, p.10	“The real-space dipole collapses to 0.41σ” is still visually tied to the full Catalog C sky map, not the HC p
eq
	​

>0.6 estimator. 

chirality_catalog_paper_v174

	Add “HC p
eq
	​

>0.6 estimator” in the caption or remove the numeric 0.41σ from the figure caption.
NF-m2	Sec. V.A, p.12	“Can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples” still reads as a cross-survey explanation rather than a mechanism demonstrated under this DESI/ViT-Small pipeline. 
GitHub
	Use “can generate a comparable pre-MASTER dipole-class artifact under this pipeline; a matched Ganalyzer test remains required.”
NF-m3	Table VII, p.17	The table caption still says “All 8 tests pass,” which is terser than the surrounding caveats and will be quoted out of context. 
GitHub
	Change the caption to “All implemented engineering checks meet their stated thresholds.”
NF-m4	Data Availability, p.20	The PDF still says the Zenodo DOI is not yet minted. This is acceptable for an internal draft, but not for acceptance-stage reproducibility. 

chirality_catalog_paper_v174

	Mint the DOI before submission or acceptance.
3. Updated recommendation

Recommendation: MAJOR REVISIONS. The paper moved toward publishability on the A95/falsification and main HC-labeling fixes, but it remains acceptance-blocked by the source/PDF provenance mismatch and several stale statements that still blur HC, full-sample, pre-MASTER, and post-MASTER results.

Sources

Pro Extended

