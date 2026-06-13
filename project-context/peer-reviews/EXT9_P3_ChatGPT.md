# EXT9 P3 — ChatGPT (in-thread delta round 9; recalibrated prompt)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a
**PDF**: paper3_anomaly_catalog_v3.1.104.pdf · harvested 2026-06-13 13:28 PT
---
Referee report on Paper 3 v3.1.104

Recommendation: MAJOR REVISIONS

The paper is close in concept, but the PDF supplied as v3.1.104 does not close the load-bearing issues from my v3.1.103 report. The remaining problems are not merely prose preferences: the DESI denominator reconciliation is still internally unresolved, and two central summary tables remain visibly broken in the rendered PDF.

I reviewed the full v3.1.104 PDF. I did not have the companion repository, parquet files, SHA manifest, R36/R37 artifacts, or scripts, so artifact-level closure remains verifiable only from the PDF.

1. Closure verification of my prior BLOCKER/MAJORS
Prior ID	Issue from v3.1.103 report	Status	Verification
FB103-1	DESI Table II explicitly states an unresolved inconsistency between the 2,468 science-class recount and the per-class GALAXY/QSO rates	PARTIAL	The table now clearly states that the DESI full-stream count is 195,829, the science-bit positional recount is 2,468, and the like-for-like Liang comparison is ≈0.9×, not 73×. However, the table still says the per-class GALAXY/QSO rates are “inconsistent with the 2,468 science-class match count” because of denominator definitions, without giving explicit per-row numerators or a shared-ID mapping. This remains a load-bearing unresolved ambiguity, not just a wording issue. 

paper3_anomaly_catalog_v3.1.104


FM103-1	Table II visibly broken in rendered PDF	NOT ADDRESSED	On rendered p.8, the rightmost entries of Table II overlap the adjacent body text. This is visibly broken in the supplied PDF. The textual content is also still too compressed to resolve the denominator issue. 

paper3_anomaly_catalog_v3.1.104


FM103-2	Table V clipped/overfull in rendered PDF	NOT ADDRESSED	On rendered p.21, Table V still extends beyond the right margin; row (h) is cut off at the eROSITA threshold material, and row (j) still uses internal shorthand. This table is meant to summarize residual caveats, so it must be readable. 

paper3_anomaly_catalog_v3.1.104


FM103-3	“Catalog-grade” remains too strong for the 269,317 tier	PARTIAL	The caveats are present, but the label remains problematic. The recommended 269,317 tier still includes Gaia even though the paper says Gaia should be treated as exploratory and not as a validated catalog component, and includes eROSITA as membership-list-only. 

paper3_anomaly_catalog_v3.1.104


FM103-4	Full-stream DESI band-dominance language remains too astrophysical	PARTIAL	Appendix B now labels the taxonomy as “fiber-spectral reconstruction taxonomy” and says the 2,468 science-class subset has not been re-tabulated by arm dominance. But it still states that the full-stream multi-band anomalies are “consistent with genuine spectral anomalies,” and §III.A still says the multi-band majority is consistent with “genuinely unusual spectral energy distributions.” Given that the full DESI anomaly stream is dominated by non-primary science-target spectra, this is still too astrophysical. 

paper3_anomaly_catalog_v3.1.104

2. Fresh pass — new findings only
New BLOCKERS

No wholly new blocker beyond the unresolved prior blocker FB103-1. The DESI denominator problem remains the central reason I cannot recommend minor revision.

New MAJORS

No genuinely new major scientific issue beyond the non-closure of the prior majors above. The main problem is that the PDF still contains the same unresolved DESI recount/per-class-rate ambiguity and the same broken rendered tables.

New MINORS

No new minor items beyond prior polish issues. I would not spend review capital on additional polish while Table II and Table V remain unresolved.

3. Updated high-risk audit

The 378,280 arithmetic remains internally consistent: the Path-C per-survey native counts sum to 388,493, the 5″ FoF removes 10,213 detections, and the headline stratifies as 378,080 point-source-tier detections plus 200 Planck CMB map patches. The problem is still semantic/tiered interpretation, not arithmetic. 

paper3_anomaly_catalog_v3.1.104

The DESI recount is correctly front-loaded in the text: only 2,468 of 190,015 DESI anomaly clusters match a primary science-class spectrum at 1″, and the Liang-like comparison is ≈0.9× rather than 73×. But the per-class GALAXY/QSO rates still imply a much larger science-class anomaly population unless the manuscript provides explicit shared-ID bookkeeping. 

paper3_anomaly_catalog_v3.1.104

The eROSITA de-scoping remains correct: the tier is membership-list-only, with no reproducible per-object score column for SBigAE; users must use the raw-score artifact or the n=298 membership list. 

paper3_anomaly_catalog_v3.1.104

The Fisher positivity treatment remains correct: the paper uses 1/σ
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

=0.19±0.65, and treats the [3.92,8.98] envelope as the relevant summary rather than a symmetric error bar. 

paper3_anomaly_catalog_v3.1.104

The NANOGrav caveat remains adequate in the main text and conclusion: the Bayes factor is framed as decisive only against the idealized circular-orbit SMBHB reference, not as a cosmological detection. 

paper3_anomaly_catalog_v3.1.104

The data release is still future-tense in the PDF: the HuggingFace staging, GitHub code, manifest, and planned Zenodo DOI are described, but the DOI is still to be minted at submission. I treat this as an acceptance-stage verification item, not the primary scientific blocker. 

paper3_anomaly_catalog_v3.1.104

4. Recommendation

MAJOR REVISIONS. The supplied v3.1.104 PDF did not materially move toward publishability relative to my v3.1.103 report because the DESI denominator reconciliation remains unresolved and the two central rendered tables remain broken; once those are fixed, the paper could plausibly move to minor revision quickly.
