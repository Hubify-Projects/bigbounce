# EXT6 P3 — ChatGPT Pro Extended (in-thread delta round 6)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a
**PDF**: paper3_anomaly_catalog_v3.1.100.pdf (39c00ff6) · harvested 2026-06-12 19:53 PT

---

According to the v3.1.100 PDF uploaded on 2026-06-12, the manuscript has moved further toward publishability, but I still recommend MAJOR REVISIONS. The largest remaining issues are no longer the headline arithmetic; they are catalogue-tier semantics, DESI denominator propagation, and acceptance-stage reproducibility.

I reviewed the rendered PDF and extracted text. I did not have the companion repository, parquet files, SHA manifest, R35conf audit artifact, or scripts, so artifact-level closure claims remain unverified beyond what is stated in the PDF.

1. Closure verification
Original v3.1.87 BLOCKERS
ID	Original issue	Status	Verification
B1	378,280 headline not a single validated catalogue tier	PARTIAL	The abstract now correctly foregrounds 269,317 recommended catalog-grade entries and subordinates the full 378,280 Path-C count. However, “catalog-grade” still includes Gaia, which the paper itself says is exploratory/not validated, and eROSITA, which is membership-list-only. The abstract and Table I also still use “point-source object detections” for the full DESI-heavy tier. 

paper3_anomaly_catalog_v3.1.100


B2	DESI 195,829 count includes non-object/non-science spectra	PARTIAL	The recount is now computed and clearly reported: 2,468/190,015 deduplicated DESI anomaly clusters match primary science-class spectra at 1″, and ≈98.7% fall on non-science-target spectra. This closes the arithmetic. The remaining gap is propagation: the full DESI stream still appears in source/object language, and the per-class rate paragraph still sits uneasily beside the recount.
B3	Planck denominator/rate inconsistency	PARTIAL	The Planck footnote now explicitly says the 1.00% rate is bookkeeping against the historical 20,000-patch bank, while the released tier is top-200 from the 200,000-patch native bank, i.e. 0.10%; neither is a data-driven rate. The disclosure is honest, but Table I still displays 20,000 → 200 = 1.00% in the main row. 

paper3_anomaly_catalog_v3.1.100


B4	eROSITA score axis not publication-grade	CLOSED	eROSITA is now correctly membership-list-only; the top-5 table no longer prints the irreproducible SBigAE catalogue scores, and the score-axis caveat is explicit.
B5	Data/code/artifact availability not reviewable	PARTIAL	The paper now gives a staged HuggingFace location, GitHub code location, score-axis schema language, and SHA-256 manifest path. However, the Zenodo DOI remains future-tense and the review sandbox did not include the release artifacts, so this is still not acceptance-grade for a catalogue paper. 

paper3_anomaly_catalog_v3.1.100


B6	v3.1.71 cross-vendor clean-round closure absent	NOT ADDRESSED / NOT VERIFIABLE	I still find no PDF-visible v3.1.71, Grok, Perplexity, 13 findings, STALE, VERIFIED, R35conf, or clean-round manifest. If this is a project QA deliverable, it remains outside the reviewable manuscript.
Original v3.1.87 MAJORS
ID	Original issue	Status	Verification
M1	Table I too confusing	PARTIAL	Better caveated, but still structurally overloaded: cross-transfer rows, native rows, fixed-count tiers, membership-only tiers, exploratory tiers, and incompatible rate meanings are all in one table.
M2	Planck 5″ FoF framing conceptually odd	PARTIAL	The paper now separates 378,080 point-source-tier detections from 200 Planck map patches, but the method still calls the operation “7-way positional deduplication.” Cleaner framing remains “6-way point-source FoF + appended Planck map-patch tier.”
M3	Cosmology claims over-prominent	PARTIAL	The f
NL
	​

 discussion is much safer: de-biased result is no improvement, the [3.92,8.98] envelope is emphasized, and the central 8.14 value is labelled noise-driven. Cosmology remains very prominent for an MNRAS catalogue paper. 

paper3_anomaly_catalog_v3.1.100


M4	Appendix C not reconciled with Fisher positivity	CLOSED	Appendix C/Table VIII is now clearly reference-only in substance; it states that the empirical α
jk
	​

=0.19±0.65 result supersedes the fixed-α grid.
M5	NANOGrav should be split/de-emphasised	PARTIAL	The Bayes-factor arithmetic is now auditable, and the environmental-SMBHB caveat is strong. But NANOGrav still occupies abstract/body/conclusion space in a catalogue paper. 

paper3_anomaly_catalog_v3.1.100


M6	Injection-recovery “3 PASS” needed 2+1 split	CLOSED	The 2 detector-sensitivity PASS + 1 geometry-QA PASS decomposition is explicit.
M7	Gaia should not be included as validated catalogue component	PARTIAL	Gaia remains explicitly exploratory/training-sample-conditioned, yet it remains in the “catalog-grade” 269,317 tier.
M8	LAMOST should be methodological/exploratory	CLOSED	LAMOST is explicitly excluded from the recommended tier and retained as a methodological failure-mode lesson.
M9	Spatial analysis under-modelled	CLOSED	The χ
ν
2
	​

=15.7 result is now framed as raw, selection-uncorrected, and footprint-dominated.
M10	“Confirmed High-z QSO Candidates” over-titled	CLOSED	The section is now “High-z QSO Candidates,” with Redrock template-fit provenance and independent confirmation required.
M11	Liang2023 reference wrong	CLOSED	Liang et al. is corrected to ApJL 956 L6; LAMOST DR10 citation handling is also corrected.
Carry-over blockers/majors from later rounds
ID	Later issue	Status	Verification
FB1	DESI recount not propagated downstream	PARTIAL	The recount is now front-loaded and the Liang comparison correctly opens with the 2,468 vs. 2,685 result. However, the per-class rates still need an explicit numerical reconciliation with the 2,468 science-class match count, and the 5,384-QSO cosmology sample remains a parent-population ratio rather than a selection-function-controlled tracer sample.
FB2	“Source/object” vocabulary wrong for full DESI tier	PARTIAL	The body says the full DESI tier is “everything DESI pointed a fiber at,” dominated by non-science-target spectra. The abstract/Table I still say “point-source object detections.”
FM95-2 / FM98-2	Tabular scaler-refit robustness	PARTIAL	eROSITA is now checked: top-298 overlap 257/298, top-1% Jaccard 0.64, Spearman 0.94. But NEOWISE and Gaia remain queued because their feature tables existed only pod-side. This is not fully closed. 

paper3_anomaly_catalog_v3.1.100


FM95-3	Frozen release not referee-accessible	PARTIAL	Still no minted DOI or review-accessible artifact bundle.
FM98-1	Hardware provenance contradiction	CLOSED	v3.1.100 consistently states A100 provenance in §II.C, acknowledgements, and Table VI. 

paper3_anomaly_catalog_v3.1.100


FM98-3	Conclusion ordered novelty result backwards	CLOSED	The conclusion now leads with the 17.8% genuine novelty figure and demotes 58.8% to database coverage.
2. Fresh pass — new findings only
New BLOCKERS

No wholly new blockers beyond the unresolved partial blockers above. The remaining acceptance-blocking items are carry-overs: catalogue-tier semantics, DESI denominator propagation, source/object vocabulary, and frozen data-release availability.

New MAJORS
FM100-1. Table V threshold summary is incorrect for SDSS

Section/page: Table V, p.21.
Issue: Table V row (h) says “Thresholds: DESI S>5.0; SDSS/LAMOST top-1%; eROSITA top-298.” This is wrong for the published SDSS headline tier: Table I and §III.C state that SDSS uses a 77,905-object continuity slice, equal to 4.05% of the 1,925,279 native-rescored spectra, while the true SDSS native top-1% is 19,253 and the strict S>5 set is 12. 

paper3_anomaly_catalog_v3.1.100


Proposed fix: Change Table V row (h) to: “DESI S>5; SDSS continuity slice 77,905 / native top-1% 19,253 / strict S>5 12; LAMOST native top-1%; eROSITA top-298 membership list.”

New MINORS
fM100-1. Figure 1’s embedded legend still says “Gold Anomalies (83)”

Section/page: Fig. 1, p.3.
Issue: The caption text now correctly says “Exemplar Set,” but the rendered plot legend still reads “Gold Anomalies (83).”
Proposed fix: Regenerate the plot so the embedded legend says “Exemplar Set (83).”

fM100-2. Table V row (j) uses internal shorthand

Section/page: Table V, p.21.
Issue: “GS corrected: σ(f
NL
	​

)
GS
	​

∈[0.94,8.98] central 1.95; prior ±7.43 dropped” is too audit-log-like for the main text and does not define GS in the table. 

paper3_anomaly_catalog_v3.1.100


Proposed fix: Replace with “Gold+Silver QSO-candidate subset: central σ(f
NL
	​

)=1.95, envelope [0.94,8.98]; no positive improvement at <1σ.” Move “prior ±7.43 dropped” to a supplementary change log.

fM100-3. Appendix C title should say “reference-only”

Section/page: Appendix C, p.22–23.
Issue: The title “Fisher Forecast with a Fixed Bias Prior” is less safe than the surrounding text, which correctly says the fixed-α grid is retained only for comparison and should not be read as the current forecast.
Proposed fix: Retitle as “Reference-only fixed-α=0.15 Fisher grid.”

3. Updated high-risk audit

378,280 arithmetic: Still internally consistent: native inputs sum to 388,493; 10,213 collapsed detections give 378,280; stratification remains 378,080 point-source-tier detections + 200 Planck patches. The unresolved issue is semantic, not arithmetic.

7-way 5″ FoF arithmetic: Still correct: 637 multi-survey clusters + 9,576 intra-survey duplicate collapses = 10,213 total collapsed detections.

DESI recount: The 2,468 science-class count is now plainly reported and the Liang comparison is corrected. The remaining problem is propagation into all “source/object” and per-class-rate language.

Fisher positivity: Correct. The paper uses 1/σ
2
(f
NL
	​

)=F
0
	​

+cα
2
, reports α
jk
	​

=0.19±0.65, gives central σ=8.14, and treats [3.92,8.98] as the appropriate envelope rather than a symmetric error bar. 

paper3_anomaly_catalog_v3.1.100

NANOGrav: The γ=2.567±0.382, matter-bounce +1.13σ, idealized SMBHB +4.61σ, and 3.23/(4.52×10
−4
)=7.14×10
3
 arithmetic are internally consistent. The caveat “decisive only against the idealized circular-orbit SMBHB reference” is now strong in the main text. 

paper3_anomaly_catalog_v3.1.100

R35conf / clean-round: Still not verifiable from the PDF or supplied sandbox artifacts.

4. Recommendation

MAJOR REVISIONS. The paper moved toward publishability, but it still needs clean tier nomenclature, DESI denominator/source-language reconciliation, a corrected Table V threshold row, completed or explicitly de-scoped Gaia/NEOWISE scaler robustness, and a referee-accessible frozen data release before I would recommend minor revision.
