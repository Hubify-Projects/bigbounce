# EXT3 P3 — ChatGPT in-thread delta review (round 3)
**Provider**: chatgpt.com Big Bounce Book project · Pro Extended
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a
**PDF**: paper3_anomaly_catalog_v3.1.91.pdf · **Harvested**: 2026-06-11 ~02:50 PT

---

Show more
Thought for 10m 28s
Referee report on Paper 3 v3.1.91

Recommendation: MAJOR REVISIONS

The manuscript has moved substantially toward publishability since v3.1.89, especially on eROSITA de-scoping, NANOGrav caveating, Table IV language, fixed-α demotion, and DESI benchmark wording. It is still not at minor-revision stage because several core catalogue-definition and reproducibility issues remain unresolved.

I reviewed the full revised PDF. I did not have the companion repository, parquet files, SHA manifest, MCMC chains, or scripts in the sandbox, so artifact-level claims remain checked only against the PDF text.

1. Closure verification
Original v3.1.87 BLOCKERS
ID	Original issue	Status	Verification
B1	378,280 headline not a single validated catalogue tier	PARTIAL	The abstract now leads with the 269,317 recommended catalog-grade tier and subordinates the full 378,280 Path-C count. It also separates 378,080 point-source detections from 200 Planck map patches and excludes LAMOST from the recommended tier. However, the “catalog-grade” tier still includes Gaia, explicitly marked exploratory/training-sample-conditioned, and eROSITA, now membership-only with no reproducible per-object score. The title still foregrounds 378,280. 

paper3_anomaly_catalog_v3.1.91


B2	DESI 195,829 count includes non-object/non-science spectra	PARTIAL	The abstract now correctly says the DESI 73× comparison is not like-for-like and that a TARGETTYPE-restricted recount is queued. But the headline DESI count remains the top-1% of the full 22.5M-spectrum scan, not a validated science-target/object subset. 

paper3_anomaly_catalog_v3.1.91


B3	Planck denominator/rate inconsistency	PARTIAL	The paper now explains the historical 20,000-patch cross-transfer budget versus the 200,000-patch native bank. But Table I still reports Planck as 20,000 → 200 = 1%, while the Path-C native tier is top-200 from the 200,000-patch re-score. The rate remains bookkeeping, not a native anomaly frequency. 

paper3_anomaly_catalog_v3.1.91


B4	eROSITA score axis not publication-grade	CLOSED	eROSITA is now membership-only. The PDF states that no committed score axis reproduces the production threshold, that SBigAE must not be used as a continuous science score, and that the reproducible product is the n=298 membership list / raw-score artifact. 

paper3_anomaly_catalog_v3.1.91


B5	Data/code/artifact availability not reviewable	PARTIAL	The data-availability section now adds a score-schema flag table, SHA-256 manifest, HuggingFace staging, GitHub code location, and future Zenodo DOI. But the DOI is not minted in the paper, and the actual artifacts were not available in the sandbox for independent verification. 

paper3_anomaly_catalog_v3.1.91


B6	v3.1.71 cross-vendor clean-round closure absent	NOT ADDRESSED / NOT VERIFIABLE	I still found no PDF occurrence of v3.1.71, Grok, Perplexity, 13 findings, STALE, VERIFIED, or clean-round. If this is a project QA deliverable, it remains outside the manuscript and inaccessible to the referee.
Original v3.1.87 MAJORS
ID	Original issue	Status	Verification
M1	Table I too confusing	PARTIAL	The footnotes are more honest and much more complete, but Table I still mixes cross-transfer N_anom rows with Path-C native counts and relies on dense footnotes to explain which number is science-grade. The table is improved but still structurally confusing. 

paper3_anomaly_catalog_v3.1.91


M2	Planck 5″ FoF framing conceptually odd	PARTIAL	The paper now clearly distinguishes 378,080 point-source entries from 200 Planck map patches. However, the method still describes a “7-way positional deduplication” that includes physically different objects and sky regions. A “6-way point-source FoF + appended Planck map-patch tier” framing would be cleaner. 

paper3_anomaly_catalog_v3.1.91


M3	Cosmology claims over-prominent	PARTIAL	The f
NL
	​

 section now clearly states that the de-biased estimate returns no improvement and that the central 9.4% gain is not a detection. Still, cosmology remains one of the two motivating goals and remains prominent in abstract/conclusion. 

paper3_anomaly_catalog_v3.1.91


M4	Appendix C not reconciled with Fisher positivity	CLOSED	Appendix C is now explicitly labelled “Legacy Fixed-α=0.15 Sensitivity Reference (Superseded)” and says the fixed-α grid should not be read as a forecast for the current data. 

paper3_anomaly_catalog_v3.1.91


M5	NANOGrav should be split/de-emphasised	PARTIAL	The environmental-SMBHB caveat is now strong and explicit, and the result is framed as illustrative. But NANOGrav still appears in the abstract, body, conclusion, and appendix of a catalogue paper. 

paper3_anomaly_catalog_v3.1.91


M6	Injection-recovery “3 PASS” needs 2+1 split	CLOSED	The paper now consistently states “2 detector-sensitivity PASS + 1 geometry-QA PASS,” with NEOWISE explicitly described as passing by construction. 

paper3_anomaly_catalog_v3.1.91


M7	Gaia should not be validated catalogue component	PARTIAL	Gaia is now explicitly labelled exploratory and unsuitable for downstream science without a Gaia-optimized detector. But Gaia remains inside the 269,317 “catalog-grade” tier. 

paper3_anomaly_catalog_v3.1.91


M8	LAMOST should be methodological/exploratory	CLOSED	LAMOST is now clearly labelled a transparent FAIL/exploratory tier, excluded from the recommended catalog-grade tier, and retained as a methodological lesson. 

paper3_anomaly_catalog_v3.1.91


M9	Spatial analysis under-modelled	CLOSED	The foreground claim is now scoped to “within surveyed footprints,” and the χ
ν
2
	​

=15.7 result is explicitly said to be footprint-dominated and not astrophysical-clustering evidence.
M10	“Confirmed High-z QSO Candidates” over-titled	CLOSED	The section is now “High-z QSO Candidates,” and the redshifts are described as Redrock template-fit spectroscopic pipeline estimates requiring independent confirmation.
M11	Liang2023 reference wrong	CLOSED	Liang et al. is now given as ApJ Letters 956, L6; LAMOST DR10 is also now cited with the data release plus Cui et al. 2012 survey paper.
v3.1.89 fresh findings
ID	v3.1.89 issue	Status	Verification
NB1	Data-release score schema internally inconsistent	CLOSED	Data Availability now explicitly says DESI/SDSS/LAMOST/Gaia/NEOWISE have canonical-S scores where applicable, Planck uses raw per-patch MSE, and eROSITA is membership-only with no reproducible per-object score column. 

paper3_anomaly_catalog_v3.1.91


NB2	Title overclaims “Native-Trained Novelty Fractions”	PARTIAL	The text now says the 17.8% novelty fraction is a single DESI top-1,000 estimate and not a survey-wide native-retrained rate. But the title still says “Native-Trained Novelty Fractions,” plural. 

paper3_anomaly_catalog_v3.1.91


NM1	DESI 73× “like-for-like” wrong	CLOSED	The abstract and conclusion now state that DESI-only 73× is not like-for-like, because the paper’s DESI count is full-scan while the benchmark is science-target-only. 

paper3_anomaly_catalog_v3.1.91


NM2	SDSS native result mixed with cross-transfer diagnostic	PARTIAL	The text better frames the SDSS UMAP/HDBSCAN material as cross-transfer diagnostic, but the physical category discussion still rests substantially on the cross-transfer set.
NM3	20-vs-18 catalog count inconsistency	CLOSED	The paper now states 18 curated all-sky catalogs, matching the enumerated list. 

paper3_anomaly_catalog_v3.1.91


NM4	High-z QSO redshift provenance ambiguous	CLOSED	The redshift source is now specified as DR1 Redrock REDSHIFTS HDU Z, with ZERR/ZWARN/SPECTYPE, and independent confirmation is required.
NM5	“203 novel eROSITA X-ray sources” contradicted novelty definition	PARTIAL	Main text now says “203 SIMBAD-unmatched eROSITA membership-list sources,” which is correct. However, Table III still uses a SIMBAD column value “Novel” to mean “no SIMBAD counterpart,” which perpetuates the ambiguity. 

paper3_anomaly_catalog_v3.1.91


NM6	TARGETTYPE/SPECTYPE conflated	CLOSED	The text now distinguishes DESI target-selection classes from Redrock spectral-template classifications.
NM7	Table IV “all closed” language	CLOSED	Table IV is now “Path-C residual caveats and current handling,” with documented/open caveats distinguished from resolved items. 

paper3_anomaly_catalog_v3.1.91


NM8	Appendix E mis-cited project MCMC artifacts	CLOSED	Appendix E now points the chain/figure/script to the project repository path rather than to the NANOGrav reference.
2. Fresh pass — new findings only
New BLOCKERS

No wholly new blockers beyond the carry-over partial blockers above. The remaining acceptance-blocking items are still the same core issues: catalogue tier semantics, DESI object-vs-spectrum bookkeeping, Planck denominator/independence, referee-accessible artifact release, and missing QA clean-round manifest.

New MAJORS
FM1. Full-sample feature scaling leaks information and may affect anomaly rankings

Section/page: §II.B, p.3.
Issue: The paper states that eROSITA and NEOWISE feature scalers are fit on the full sample, not the training split, and Gaia’s preprocessing is lineage-inferred. It then asserts that this affects validation MSE scale but not within-survey anomaly ranking. That assertion is not guaranteed: anomaly detection is tail-sensitive, and full-sample normalization can be influenced by outliers that later appear in the top-ranked tail.
Proposed fix: Re-run the tabular surveys with scalers fit on the training split only, or with a robust background-only scaling pass excluding the top tail. Report top-298/top-1% Jaccard overlap, count changes, and rank correlation relative to the published products. If unchanged, this becomes a strength; if changed, update the catalogue.

FM2. Planck training/re-score independence is not demonstrated

Section/page: §III.F, p.10–11; Table V, p.22.
Issue: The text says the Path-C Planck native pipeline extracts a 200,000-patch bank for training and re-scoring, and the top-200 of the native re-score form the released Planck tier. It is not clear whether the released top-200 can include patches used in training or validation. For a CMB map-patch anomaly product, releasing training-set patches as top anomalies would weaken the validation interpretation.
Proposed fix: Provide disjoint train/validation/science-patch identifiers and explicitly state whether released top-200 patches were excluded from training and validation. If not excluded, re-score a held-out science-only patch bank and update the Planck tier.

FM3. eROSITA threshold description remains inconsistent across sections

Section/page: §II.B, p.4; §III.E/Table III, p.10.
Issue: §II.B still says eROSITA uses a “data-driven IsolationForest score-knee threshold.” But §III.E says the production threshold is unreconciled with canonical S, raw scores, or IsolationForest axes, and that eROSITA should be treated as a fixed top-298 membership list. These statements are not equivalent.
Proposed fix: Replace the §II.B threshold-family sentence with: “eROSITA is released as a fixed top-298 production membership list; its score axis is non-reproducible and IsolationForest is used only as a dependent cross-validation diagnostic.”

FM4. DESI validation and rate-stability language still overreach

Section/page: §VI.A–E, p.17–19.
Issue: The paper says DESI anomalies pass “every validation test” and that the 0.87% DESI rate’s agreement with Liang et al. suggests a stable DESI spectroscopic anomaly rate. But the limitations section says no independent architecture was applied to DESI/SDSS/LAMOST, the DESI full-scan count is not science-target restricted, and the paper still queues the TARGETTYPE-restricted recount. The k-fold/OOD Jaccards are valuable, but not “every validation test.”
Proposed fix: Replace with: “DESI passes the internal k-fold, OOD-Jaccard, and top-200 visual artifact checks performed here.” Defer claims of a stable DESI anomaly rate until a science-target-only recount and an independent-architecture validation are provided.

New MINORS

Table III, p.10: Replace Novel in the SIMBAD column with No SIMBAD 5″ match or SIMBAD-unmatched. The caption defines “Novel” as no SIMBAD counterpart, but the paper elsewhere correctly says SIMBAD absence is not discovery. 

paper3_anomaly_catalog_v3.1.91

Title, p.1: “Native-Trained Novelty Fractions” should be changed to “Native-Trained Anomaly Fractions” or “DESI Top-1,000 Novelty Estimate,” unless the same deep novelty analysis is done for all native tiers. 

paper3_anomaly_catalog_v3.1.91

Figure 2, p.6: The title still says “all 319,443 anomalies across 8 archives.” The caption clarifies cross-transfer baseline, but the plot title itself should say “cross-transfer baseline.”

Appendix C / Fig. 11, p.21–23: The shot-noise sensitivity paragraph mixes signs when comparing σ(f
NL
	​

) values to the “baseline multi” number. Rewrite as “σ decreases by X%” or “σ increases by Y%,” not “+X% over” and “−Y% vs” with ambiguous sign conventions. 

paper3_anomaly_catalog_v3.1.91

NANOGrav environmental caveat, §V.A: The caveat is now scientifically necessary and useful, but the cited references should include a targeted environmental-coupling/spectral-turnover SMBHB reference in addition to the broad review/selection-bias citations.

3. Requested high-risk audit items

378,280 headline: Arithmetic remains internally consistent: 388,493 survey-level detections minus 10,213 collapsed detections yields 378,280; the paper now correctly foregrounds 269,317 recommended entries and 269,117 point-source recommended entries after dropping Planck. The semantic problem remains that “catalog-grade” still includes Gaia exploratory and eROSITA membership-only material. 

paper3_anomaly_catalog_v3.1.91

7-way 5″ FoF arithmetic: The 10,213 = 637 + 9,576 reconciliation remains internally consistent. I do not flag the arithmetic.

Fisher positivity: The positivity-respecting form 1/σ
2
(f
NL
	​

)=F
0
	​

+cα
2
, σ(f
NL
	​

)=8.14 central at α=0.19, and envelope [3.92,8.98] are retained; the paper now correctly states that the de-biased estimate gives no improvement.

NANOGrav: The γ=2.567±0.382, matter-bounce +1.13σ, idealized SMBHB +4.61σ, and B
mb/SMBHB
	​

=7.14×10
3
 numbers remain self-consistent. The environmental-SMBHB caveat is now strong enough that I no longer treat the interpretation as a blocker. 

paper3_anomaly_catalog_v3.1.91

v3.1.71 cross-vendor R-round: Still not verifiable from the manuscript or supplied sandbox artifacts.

4. Updated recommendation

MAJOR REVISIONS. The paper has moved markedly toward publishability, but the catalogue still needs a clean tier definition, DESI science-target/object-level recounting or relabelling, Planck held-out-denominator clarification, final artifact/DOI availability, and a small number of consistency edits before I would recommend minor revision.

Sources

Pro Extended

