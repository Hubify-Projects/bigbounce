# EXT1 P3 — ChatGPT Pro Extended referee report
**Provider**: chatgpt.com web app (Big Bounce Book project) · intelligence **Pro Extended** (GPT-5.5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a
**PDF**: paper3_anomaly_catalog_v3.1.87.pdf (md5 acde55ca) · **Harvested**: 2026-06-10T17:05 PDT

---

Show more
Thought for 11m 51s
Referee report

Paper: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Anomalies and Native-Trained Novelty Rates from 37.3 Million Sources
Recommendation: MAJOR REVISIONS — re-review required. For a primarily MNRAS-style catalogue/methods paper, the core idea is publishable after substantial restructuring and reproducibility fixes. For PRD/JCAP, the cosmology/NANOGrav sections are not yet sufficiently central or self-contained and should either be split out or heavily de-emphasised.

I reviewed the full 26-page PDF. The sandbox contained the uploaded PDF only; the referenced paper3_draft.tex and companion pipeline artifacts were not present, so the artifact-level claims below are judged from the rendered PDF plus a grep of the PDF text.

Specific audit of requested high-risk items

378,280 headline arithmetic: The arithmetic is internally consistent: native per-survey inputs sum to 388,493; subtracting 10,213 collapsed detections gives 378,280; subtracting the 200 Planck map patches gives 378,080 point-source-tier detections. The paper also correctly states that the catalog-grade subset is smaller and that LAMOST contributes an exploratory tier. The problem is not arithmetic; it is presentation. The title and conclusion still read like a homogeneous “catalog of anomalies,” while the headline mixes validated, exploratory, failed-gate, and map-patch strata. 

paper3_anomaly_catalog_v3.1.87

7-way 5″ FoF dedup arithmetic: The 10,213 = 637 + 9,576 reconciliation is convincing. The size-histogram accounting gives 10,213 collapsed detections, and the paper states that 637 clusters span two surveys, leaving 9,576 intra-survey duplicate collapses. I would not flag the arithmetic. 

paper3_anomaly_catalog_v3.1.87

Fisher-positivity caveats: The current paper uses the correct positivity-respecting form, 1/σ
2
(f
NL
	​

)=F
0
	​

+cα
2
, and the stated envelope [3.92,8.98] follows from clipping the negative side at α=0. This is not the retracted symmetric ±2.37 form. 

paper3_anomaly_catalog_v3.1.87

σ(f
NL
	​

)=8.14 at empirical α=0.19±0.65: The central value and the “<1σ from null” interpretation are internally consistent. The paper also correctly states that the de-biased point estimate gives no improvement over the single-tracer baseline. 

paper3_anomaly_catalog_v3.1.87

v3.1.71 cross-vendor R-round closure: I found no occurrence of v3.1.71, Grok, Perplexity, 13 findings, STALE, VERIFIED, or clean-round in the PDF text. If this is a required project QA deliverable, it is absent from the manuscript and from the accessible sandbox artifacts. This should be added as a frozen QA manifest or author-response artifact, not necessarily as main-text prose.

NANOGrav numbers: The reported γ=2.567±0.382, matter-bounce γ=3.0 at +1.13σ, SMBHB γ=4.33 at +4.61σ, and B
mb/SMBHB
	​

=7.14×10
3
 are numerically self-consistent. The interpretive problem is that “decisive” is too strong for the main abstract/conclusion unless prior sensitivity, the fixed-index nature of the SMBHB comparison, and the free-spectrum KDE approximation are foregrounded. The paper does disclose these caveats, but not enough to prevent over-reading. 

paper3_anomaly_catalog_v3.1.87

BLOCKERS — must fix before publication
B1. The 378,280 headline is not a single validated catalogue tier

Section/line anchor: Title; abstract first paragraph; Table I footnotes; §VII item 1.
Issue: The headline combines heterogeneous strata: DESI, SDSS, LAMOST, eROSITA, Gaia, NEOWISE point-source detections plus 200 Planck map patches. Within that, LAMOST is explicitly an exploratory FAIL, Gaia is exploratory/training-sample-conditioned, eROSITA has a failed injection gate and an irreproducible published score axis, and NEOWISE’s “PASS” is a mask-geometry QA test rather than a detector-sensitivity test. The paper discloses this, but the title and main conclusion still market the total as a “catalog of 378,280 anomalies.” 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Retitle and restructure as a multi-tier candidate catalogue. Put the catalog-grade point-source count and the full candidate headline side by side in the abstract and conclusion. A clean wording would be: “We release a 378,280-entry multi-tier candidate anomaly compilation, of which 269,117 point-source entries are catalog-grade under the current validation criteria.” LAMOST, Gaia, and eROSITA should be explicitly labelled in the catalogue schema as exploratory or membership-only where applicable.

B2. DESI “point-source object” count includes non-object spectra

Section/line anchor: §III.A, paragraph beginning “We processed all 22,504,897 coadded spectra…”
Issue: The DESI headline 195,829 anomalies is drawn from the full 22.5M-spectrum scan, while the paper states that only ~6.5M spectra carry validated science TARGETTYPE; the remaining ~16M include filler-tile, sky-fiber, and calibration-exposure spectra. Those cannot automatically be called “point-source object detections.” This directly contaminates the 378,080 point-source tier unless the 195,829 DESI anomalies are shown to be overwhelmingly from science targets. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Provide a mandatory table splitting the 195,829 DESI anomalies by TARGETTYPE, sky fiber, calibration exposure, filler target, duplicate TARGETID, and object-level unique ID. Either remove non-science spectra from the headline point-source count or rename the headline “spectral anomaly detections” rather than “object detections.”

B3. Planck denominator/rate/bookkeeping inconsistency

Section/line anchor: Table I; §III.F; Appendix A Table V.
Issue: Table I lists Planck as 20,000 patches and 200 anomalies, i.e. 1%. §III.F says the Path-C native pipeline extracts and re-scores an independent 200,000-patch bank, while keeping the Planck tier fixed at 200 top-ranked patches. If the science tier is top-200 from 200,000, the Planck rate is 0.1%, not 1%, and the title’s “37.3 million sources and map patches” undercounts the actual native-scored set by 180,000 patches. If the science tier is top-200 from 20,000, then the 200,000-patch native re-score is not the denominator of the published tier. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Decide which denominator defines the Planck catalogue. Update Table I, the abstract, the title count, and all rates accordingly. Suggested wording: “Planck contributes a fixed 200-patch native-ranked tier from a 200,000-patch bank; the 20,000-patch number is retained only for the historical cross-transfer baseline.”

B4. eROSITA score axis is not publication-grade as written

Section/line anchor: §III.E; Table III.
Issue: The paper states that the eROSITA threshold axis cannot be reconciled with canonical S, raw scores, standardized scores, or IsolationForest axes; the production Table III scores are non-monotone in the committed raw artifact; and downstream score-weighted analyses cannot use the published SBigAE values. That is too severe for a catalogue paper unless eROSITA is explicitly released as a membership-only subset. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Either rerun eROSITA from a recoverable pipeline and replace all eROSITA scores with a reproducible canonical axis, or remove SBigAE from the science catalogue and label eROSITA as “top-298 membership-only; raw-score artifact required for ranking.” The data release must include raw scores, hashes, scripts, and the exact membership list.

B5. Data/code/artifact availability is not reviewable

Section/line anchor: Data availability paragraph.
Issue: The most important claims rely on companion artifacts: dedup manifests, r23conf/r24conf audits, eROSITA raw scores, native-retrain logs, Planck patch scores, MCMC chains, and catalogue membership lists. The paper says these “will be made public with the arXiv posting.” For a catalogue paper, that is not enough at acceptance stage, especially when reproducibility claims are central. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Freeze a DOI-backed Zenodo/HuggingFace release before acceptance. Include SHA256 hashes for the catalogue, dedup manifest, raw scores, model weights, training logs, scripts, and MCMC chain. The paper should cite the DOI and give a minimal reproducibility command for the headline counts.

B6. Required v3.1.71 cross-vendor clean-round closure is absent

Section/line anchor: Global; absent from PDF.
Issue: The requested R-round closure deliverable — Grok+GPT+Perplexity, 13 findings, 0 VERIFIED, 13 STALE — is not present in the PDF text and was not available as an artifact in the sandbox.
Proposed fix: Add a short supplementary QA manifest with: finding ID, original claim, current status, evidence path, and final disposition. The main text can simply cite it in Data Availability; it does not need to become a journal-style section.

MAJORS — should fix
M1. Table I is still too confusing for readers

Section/line anchor: Table I and footnotes.
Issue: The N_anom column shows cross-transfer counts for some rows while the Path-C headline uses native counts. SDSS has three meaningful cuts: 77,905 continuity slice, 19,253 top-1% score-knee set, and 12 strict S>5 sources. LAMOST has 44,075 cross-transfer, 2,054 strict S>5, and 113,342 native top-1%. The footnotes explain this, but the table design fights the explanation. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Split Table I into explicit columns: cross-transfer count, native strict S>5 count, released tier count, validation status, catalog-grade?, included in headline?.

M2. The Planck 5″ positional-dedup framing is conceptually odd

Section/line anchor: §II.D step 6; Table I; §IV.C.
Issue: A 5″ FoF deduplication across point-source catalogues and 64×64 CMB map patches is not physically meaningful. The paper says Planck patches have zero overlaps with point-source surveys, so the count is arithmetically harmless, but the method description implies a unified object-level deduplication across incompatible entities.
Proposed fix: Run FoF only on point-source catalogues, then append Planck as a separate sky-region stratum. Report: “378,080 point-source unique detections after 6-way FoF, plus 200 Planck map patches.”

M3. Cosmology claims are over-prominent relative to evidence

Section/line anchor: Abstract; §V; §VII item 5; Appendix C.
Issue: The empirical bias measurement is 0.19±0.65, the de-biased multi-tracer gain is exactly zero, and the paper correctly says no detection is claimed. Yet the conclusion still advertises SPHEREx 3–5σ detection of f
NL
	​

=−35/8, and Appendix C retains a linear sensitivity table that can be misread as a positive forecast. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Move SPHEREx detectability to background/context unless this paper provides the full systematic-degradation forecast. In the conclusion, replace “SPHEREx 3–5σ detection is projected” with “the anomaly-selected tracer idea remains a possible input to future SPHEREx forecasts, but the present empirical bias measurement is consistent with no gain.”

M4. Appendix C should be reconciled with the adopted positivity form

Section/line anchor: Appendix C, Table VII.
Issue: Table VII is explicitly a linear scaling from the fixed-α=0.15 reference, while the main text now adopts 1/σ
2
=F
0
	​

+cα
2
. The table is not necessarily wrong as a labelled heuristic, but it is now a legacy/illustrative approximation and should not sit beside the canonical forecast without a warning. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Retitle it “legacy fixed-α linearized sensitivity” and add a column using the positivity formula, or remove the table.

M5. NANOGrav section should be split or sharply de-emphasised

Section/line anchor: §V.A; Appendix E; abstract and conclusion.
Issue: The NANOGrav analysis is interesting but not a natural consequence of the anomaly catalogue. It relies on a factorized free-spectrum KDE likelihood, not a full timing-data likelihood, and the Bayes-factor comparison is explicitly prior-sensitive and compares fixed spectral-index points. The “decisive” phrasing is too strong for the headline. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Move NANOGrav to a short appendix or a companion paper. In the main text: “As an illustrative external consistency exercise…” Avoid “decisive” in the abstract/conclusion unless a prior-sensitivity plot and alternative priors are shown.

M6. Injection-recovery summary should not headline “3 PASS” without the 2+1 split

Section/line anchor: §II.D step 5; Fig. 10; §VI.D(ii).
Issue: Only SDSS and Planck pass detector-sensitivity tests. NEOWISE passes a mask-geometry QA check by construction, not anomaly sensitivity. The paper does disclose this, but the “3 PASS / 3 FAIL” shorthand is still too easy to quote incorrectly. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Everywhere use “2 detector-sensitivity PASS + 1 mask-QA PASS; 3 FAIL-with-diagnostic.”

M7. Gaia should not be included as a validated catalogue component

Section/line anchor: §III.G; Table I footnote ⋆.
Issue: The paper says Gaia has 41% cross-validation stability and that more than half of the selection is training-sample-conditioned; the exact production preprocessing script for the 50k run was not recovered. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Either rerun Gaia from a recoverable production script with held-out validation or label Gaia as “exploratory, excluded from catalog-grade counts” in every headline table.

M8. LAMOST tier should remain a methodological appendix, not a headline contributor

Section/line anchor: §III.D; Table I footnote ♠; §VI.A.
Issue: The LAMOST detector is explicitly a FAIL for emission-line sensitivity, with 5.8% recovery at 5σ, and the blue-excess attribution has not been re-tabulated post-retrain. The methodological lesson is valuable; the catalogue-grade status is not. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Move LAMOST to an “exploratory/failure-mode catalogue” appendix and keep it out of the main validated headline. The full 378,280 number can remain as a multi-tier compilation, not the primary catalogue size.

M9. Spatial analysis is under-modelled

Section/line anchor: §IV.B; Fig. 7.
Issue: The paper correctly admits that χ
ν
2
	​

=15.7 is dominated by footprints, and that latitude/dust null tests are not sufficient because the input surveys avoid the Galactic plane. Therefore the statement that the signal is “not driven by Galactic foreground contamination” is too strong. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Replace with “we find no evidence for a first-order correlation with Galactic latitude or Planck dust within the surveyed footprints.” A real spatial-systematics section needs per-survey randoms, masks, completeness, and target-density maps.

M10. “Confirmed High-z QSO Candidates” is over-titled

Section/line anchor: §III.B.
Issue: The section title combines “confirmed” and “candidates.” The evidence is internal DESI spectral morphology and cutout appearance; the paper does not present independent follow-up spectroscopy. 

paper3_anomaly_catalog_v3.1.87


Proposed fix: Retitle “High-z QSO candidates” unless independent confirmation is shown. If DESI pipeline redshifts are considered confirmation, state the exact quality flags, redrock confidence, visual-inspection protocol, and failure cases.

M11. Reference [11] appears bibliographically wrong

Section/line anchor: References; §VI.E benchmark discussion.
Issue: The paper cites Liang et al. as “MNRAS 525, 1078 (2023), arXiv:2307.07664.” The bibliographic records I found for Outlier Detection in the DESI Bright Galaxy Survey give ApJ Letters 956, L6, not MNRAS 525, 1078. 
Princeton University
+1

Proposed fix: Correct the reference and re-check all benchmark ratios tied to [11]. The numerical 2,685-anomaly benchmark may still be fine, but the citation must be accurate.

MINORS — polish

Title: Use “candidate anomalies” or “multi-tier anomaly candidates,” not simply “anomalies.”

Abstract: Lead with 17.8% genuine novelty, not 58.8% SIMBAD-unmatched. The text does explain the distinction, but the conclusion still lists 58.8% first. 

paper3_anomaly_catalog_v3.1.87

Table I: Replace unexplained Nanom with N
anom
	​

 or plain “Anomalies.”

Table I footnotes: They are too long for a main table. Move detailed reconciliation to an appendix and keep Table I readable.

Figure 1: The UMAP is visually too dark; the claimed high-score lobe is hard to see in the rendered PDF.

Figure 2: The title says “all 319,443 anomalies across 8 archives,” but the caption says it is only the cross-transfer baseline. Put “cross-transfer baseline only” in the figure title itself.

Figure 8: Burned-in “display score” values are not catalogue scores. The caption explains this, but the labels invite confusion. Remove them or replace with catalogue IDs.

Artifact rate: “0% artifact rate in top 200” should be written as “0/200 visually flagged; binomial upper limit …” rather than a literal zero rate.

SNR test: The stratified p=0.12 should not be highlighted. Quote only ρ=−0.03, then provide the queued population-weighted test before publication.

NANOGrav wording: Replace “SMBHB strongly disfavoured” with “a fixed γ=4.33 population-mean reference is disfavoured under this free-spectrum/KDE/prior setup.”

Code provenance: Where a script is named, give a permanent path and hash. Current names like r24conf_pod_session_batch.json are not enough for archival reproducibility.

MNRAS style: The manuscript reads like a version-audit log in several footnotes. Retain transparency, but move correction-history prose to supplementary notes.

Strengths

Scale and ambition: The multi-survey sweep is genuinely large, and the 388,493 native survey-level detections → 378,280 unique-entry arithmetic is carefully reconciled.

Transparency: The manuscript is unusually explicit about failures, stale arithmetic, score-axis problems, and validation caveats.

Dedup audit: The FoF accounting, radius sensitivity, and chain-bridging checks are among the strongest parts of the paper.

Fisher correction: The current f
NL
	​

 section has repaired the main positivity issue and no longer claims a detected improvement.

Failure-mode science: The LAMOST blue-excess and ACT quarantine discussions are valuable methodological lessons.

Potential data product: A frozen, reproducible, tiered anomaly catalogue would be useful to the community, especially the DESI and SDSS validated tiers plus the cross-survey match list.

Bottom line

I would support publication after major revision if the authors make the catalogue tiering explicit, remove non-object spectra from object-level headlines, fix Planck/eROSITA reproducibility issues, freeze the data/code artifacts, and de-emphasise the cosmology/NANOGrav claims. The paper’s core catalogue/methods contribution is promising, but the current version still overstates the homogeneity and validation status of the 378,280-entry headline.

Sources

Pro Extended

