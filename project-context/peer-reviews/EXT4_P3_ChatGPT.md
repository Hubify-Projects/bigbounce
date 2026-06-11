# EXT4 P3 — ChatGPT Pro Extended (in-thread delta round 4)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a
**PDF**: paper3_anomaly_catalog_v3.1.95.pdf (799d13fc) · harvested 2026-06-11 15:55 PT
---
Referee report on Paper 3 v3.1.95

Recommendation: MAJOR REVISIONS

The paper moved strongly toward publishability since v3.1.91, especially because the DESI science-class recount is now computed and plainly reported, eROSITA scores are removed from the top-5 table, the Fisher mapping is numerically auditable, and the NANOGrav caveat is much cleaner. However, the new DESI recount creates a downstream-consistency problem that is now the central remaining blocker.

I reviewed the revised PDF end-to-end. I did not have the companion repository, parquet files, SHA manifest, MCMC chains, or scripts in the sandbox, so artifact-level claims remain checked only against the PDF text.

1. Closure verification
Original v3.1.87 BLOCKERS
ID	Original issue	Status	Verification
B1	378,280 headline not a single validated catalogue tier	PARTIAL	The abstract now correctly leads with the 269,317 recommended catalog-grade tier and subordinates the full 378,280 Path-C count. It also separates 378,080 point-source detections from 200 Planck patches. However, the “catalog-grade” tier still includes Gaia, explicitly labelled exploratory/training-sample-conditioned, and eROSITA, which is membership-list-only. The wording should be “recommended non-LAMOST tier” unless Gaia is removed or promoted by validation. 

paper3_anomaly_catalog_v3.1.95


B2	DESI 195,829 count includes non-object/non-science spectra	PARTIAL	The recount is a major improvement and is now plainly reported: of 190,015 deduplicated DESI anomaly clusters, only 2,468 match primary science-class spectra at 1″; ∼98.7% fall on non-science-target spectra, and 86% have DESI_TARGET=0. But the full-stream DESI count still feeds the “point-source object detections / sources” language. The fix is incomplete until the paper renames the full DESI tier as fiber-spectral anomaly detections or restricts object/source-count claims to the science-class subset.
B3	Planck denominator/rate inconsistency	PARTIAL	The paper now explains the 20,000 historical cross-transfer budget versus the 200,000 native bank and says the 200-patch tier is fixed. But Table I still shows Planck as 20,000 → 200 = 1.00%, while the released native tier is top-200 from 200,000, i.e. 0.10%. The caveat is now honest; the table remains structurally confusing. 

paper3_anomaly_catalog_v3.1.95


B4	eROSITA score axis not publication-grade	CLOSED	The top-5 table now omits SBigAE, uses membership-list rank order, and states that the production score axis is irreproducible; downstream analyses must use the raw-score artifact or the n=298 membership list.
B5	Data/code/artifact availability not reviewable	PARTIAL	The data-availability section now gives a HuggingFace staging location, GitHub code location, SHA-256 manifest path, and explicit score-axis schema. But the Zenodo DOI is still “to be minted,” and the actual artifacts were not supplied in the sandbox. This is not acceptance-grade for a catalogue paper until a referee-accessible frozen release exists. 

paper3_anomaly_catalog_v3.1.95


B6	v3.1.71 cross-vendor clean-round closure absent	NOT ADDRESSED / NOT VERIFIABLE	I still find no occurrence of v3.1.71, Grok, Perplexity, 13 findings, STALE, VERIFIED, or clean-round in the PDF text. If this is a project QA deliverable, it remains outside the manuscript and inaccessible to the referee.
Original v3.1.87 MAJORS
ID	Original issue	Status	Verification
M1	Table I too confusing	PARTIAL	The table is more honest but still mixes historical cross-transfer rows, native-retrained rows, fixed-count tiers, and membership-only tiers in one dense table. The footnotes rescue it, but the main table remains hard to parse.
M2	Planck 5″ FoF framing conceptually odd	PARTIAL	The paper now distinguishes 378,080 point-source entries from 200 Planck map patches. But the method still describes a “7-way positional deduplication” over mixed point-source and map-patch strata. This should be “6-way point-source FoF + appended Planck map-patch tier.”
M3	Cosmology claims over-prominent	PARTIAL	The f
NL
	​

 section is much safer: it states that the de-biased estimate gives no improvement and that the envelope, not the central convex value, is the relevant summary. Cosmology remains prominent for an MNRAS catalogue paper, but the caveats are now strong enough that this is no longer a blocker. 

paper3_anomaly_catalog_v3.1.95


M4	Appendix C not reconciled with Fisher positivity	CLOSED	The fixed-α appendix is now labelled reference-only and explicitly superseded by the empirical α
jk
	​

=0.19±0.65 result, which is consistent with no multi-tracer improvement. 

paper3_anomaly_catalog_v3.1.95


M5	NANOGrav should be split/de-emphasised	PARTIAL	The abstract and body now say the Bayes factor is decisive only against the idealized circular-orbit SMBHB reference and is not a cosmological detection. That is a substantial fix. The section still feels like a companion-paper result embedded in a catalogue paper, but the interpretation is no longer misleading. 

paper3_anomaly_catalog_v3.1.95


M6	Injection-recovery “3 PASS” needed 2+1 split	CLOSED	The 2 detector-sensitivity PASS + 1 geometry-QA PASS decomposition is now explicit. 

paper3_anomaly_catalog_v3.1.95


M7	Gaia should not be included as validated catalogue component	PARTIAL	Gaia is explicitly labelled exploratory and training-sample-conditioned, but it remains inside the 269,317 “catalog-grade” tier. This is still internally inconsistent.
M8	LAMOST should be methodological/exploratory	CLOSED	LAMOST is now clearly exploratory, excluded from the recommended tier, and retained as a methodological lesson. 

paper3_anomaly_catalog_v3.1.95


M9	Spatial analysis under-modelled	CLOSED	The χ
ν
2
	​

=15.7 result is now framed as a raw, selection-uncorrected footprint-dominated count distribution; the latitude/dust claim is scoped to surveyed footprints. 

paper3_anomaly_catalog_v3.1.95


M10	“Confirmed High-z QSO Candidates” over-titled	CLOSED	The section is now “High-z QSO Candidates,” and redshift provenance is Redrock template-fit spectroscopy requiring independent confirmation.
M11	Liang2023 reference wrong	CLOSED	Liang et al. is now ApJL 956 L6; the LAMOST DR10 data-release and Cui et al. 2012 survey references are also present.
v3.1.89 / v3.1.91 carry-over findings
ID	Prior issue	Status	Verification
NB1	Score schema internally inconsistent	CLOSED	Data availability now says DESI/SDSS/LAMOST/Gaia/NEOWISE carry canonical-S where applicable, Planck uses raw MSE, and eROSITA is membership-only. 

paper3_anomaly_catalog_v3.1.95


NB2	Title overclaimed novelty fractions	CLOSED	The title now uses singular “a Native-Trained Novelty Fraction,” matching the single DESI top-1,000 deep novelty estimate.
NM1	DESI 73× “like-for-like” wrong	CLOSED	The paper now states the full DESI 73× is not like-for-like and gives the restricted 2,468 vs. 2,685 result. 

paper3_anomaly_catalog_v3.1.95


NM2	SDSS native result mixed with cross-transfer diagnostic	CLOSED	SDSS physical categories are now explicitly labelled as cross-transfer diagnostic, not a physical census of the native-retrained tier. 

paper3_anomaly_catalog_v3.1.95


NM3	20-vs-18 catalog count inconsistency	CLOSED	The manuscript now uses 18 curated all-sky catalogs.
NM4	High-z QSO redshift provenance ambiguous	CLOSED	Redshift source is now Redrock REDSHIFTS HDU Z, with ZERR/ZWARN/SPECTYPE, and confirmation caveats.
NM5	“203 novel eROSITA X-ray sources” contradicted novelty definition	CLOSED	The text now says “203 SIMBAD-unmatched eROSITA membership-list sources,” and the top-5 table uses “No 5″ match,” not “Novel.”
NM6	TARGETTYPE/SPECTYPE conflated	CLOSED for terminology; new downstream issue below	The wording now distinguishes target-selection and Redrock spectral-template axes. But the DESI recount now conflicts with some downstream per-class rates; see fresh blocker.
NM7	Table IV “all closed” language	CLOSED	Table V is now “residual caveats and current handling” with documented active caveats. 

paper3_anomaly_catalog_v3.1.95


NM8	Appendix E mis-cited project MCMC artifacts	CLOSED	Appendix E now points to the project repository path for chain, posterior figure, and fitter script.
FM1	Full-sample feature scaling may affect tabular anomaly rankings	PARTIAL	The manuscript now admits the issue and says a train-split-only scaler refit with Jaccard/Spearman comparison is queued. That is honest, but the robustness check has not been done. 

paper3_anomaly_catalog_v3.1.95


FM2	Planck train/re-score independence unclear	CLOSED as disclosure, not as ideal validation	The paper now says the native Planck bank is scored in full, including training patches, so the released top-200 is not held out. It also gives the 152/48 train/validation split overlap. This is acceptable if framed as production autoencoder scoring rather than held-out discovery validation. 

paper3_anomaly_catalog_v3.1.95


FM3	eROSITA threshold description inconsistent	CLOSED	§II.B and §III.E now describe eROSITA as fixed top-298 membership-only rather than a recoverable score threshold.
FM4	DESI validation/rate-stability language overreached	PARTIAL	The language now says DESI passes the internal checks applied to it and acknowledges no independent architecture plus the science-class recount. But the downstream DESI class/rate/cosmology analyses still need propagation of the recount.
2. Fresh pass — new findings only
New BLOCKERS
FB1. The DESI science-class recount is not propagated into downstream DESI claims

Section/page: §III.A and Table II, pp. 5–8; §V, p. 17; §VII, pp. 20–21.
Issue: The new recount shows only 2,468/190,015 deduplicated DESI anomaly clusters match primary science-class spectra at 1″, with only 95 QSO by Redrock SPECTYPE, while ∼98.7% of DESI anomaly clusters are on non-primary-class spectra. Yet the next paragraph still quotes per-class rates such as “galaxies are flagged as anomalous at ∼20 times the rate of QSOs (0.75% vs. 0.037%)” over the ∼6.5M validated-TARGETTYPE subset. Those rates cannot be reconciled with only 2,468 primary-class anomaly clusters unless the denominators/definitions are different. The same issue affects the top-10,000 DESI novelty estimate, the top-200 artifact audit, the 12 high-z QSO candidates, and especially the 5,384 QSO-candidate sample used for the Landy–Szalay bias measurement.
Proposed fix: Add a DESI recount-propagation table with rows for: full spectra stream, deduplicated clusters, DESI_TARGET=0, sky fibers, secondary/ToO, calibration, primary-bit BGS/LRG/ELG/QSO/MWS, Redrock SPECTYPE, and the 12 high-z / 5,384 QSO-candidate subsets. Recompute all DESI class rates, novelty rates, artifact rates, and cosmology-input sample composition on those strata. If the 5,384 QSO-candidate sample is not drawn from a well-defined science/tracer selection function, de-scope the f
NL
	​

 result to an illustrative exercise only.

FB2. The “source/object” vocabulary is still wrong for the full DESI tier

Section/page: Title/abstract, p. 1; Table I, pp. 7–8; §VII, pp. 20–21.
Issue: The title and abstract still say “sources and map patches” and “point-source object detections,” but the DESI full-stream anomaly set is now shown to be dominated by sky-fiber, secondary/filler, or non-primary spectra. A sky fiber is not a source, and a non-primary/filler spectrum should not automatically be counted as an object-level astrophysical source.
Proposed fix: Rename the full DESI contribution “fiber-spectral anomaly detections” and reserve “source/object” for rows with an astrophysical target association. The title could become: “378,280 Path-C Unique Anomaly Detections across 37.3 Million Spectra, Sources, and Map Patches.”

New MAJORS
FM95-1. The “catalog-grade” tier remains semantically inconsistent

Section/page: Abstract, p. 1; Table I footnotes, pp. 7–8; Data availability, p. 22.
Issue: The recommended 269,317 tier includes Gaia despite the paper’s own warning that Gaia is exploratory and training-sample-conditioned, and includes eROSITA despite membership-only score provenance. eROSITA membership-only can be acceptable if flagged, but Gaia should not be called catalog-grade without a Gaia-optimized held-out validation.
Proposed fix: Define three explicit tiers: validated/source-grade, recommended non-LAMOST compilation, and exploratory/membership-only. Put Gaia in exploratory; put eROSITA in membership-only unless downstream users need score-weighted ranking.

FM95-2. Tabular-survey scaling robustness remains queued, not closed

Section/page: §II.B, p. 3.
Issue: The manuscript now openly admits that eROSITA, NEOWISE, and Gaia scalers were fit on the full sample, including validation/tail information, and that a train-split-only refit could reorder the extreme tail. The robustness check is still “queued.” 

paper3_anomaly_catalog_v3.1.95


Proposed fix: Run the stated train-split-only scaler refit before publication and report top-k Jaccard/Spearman for eROSITA, NEOWISE, and Gaia. If the released lists change materially, update the catalogue; if not, this becomes a strength.

FM95-3. The catalogue is still not independently reproducible at review time

Section/page: Data availability, p. 22.
Issue: The paper states that hashes are in DATA_RELEASE_MANIFEST.md and that a Zenodo DOI will be minted at submission, but those artifacts were not available to me. For a catalogue paper, the paper and frozen data product are inseparable. 

paper3_anomaly_catalog_v3.1.95


Proposed fix: Provide a referee-accessible frozen release before acceptance, including the catalogue parquet, dedup manifest, score schema, Planck/eROSITA raw artifacts, MCMC chains, and a one-command count-reproduction script.

FM95-4. The DESI “0.87% anomaly rate” should no longer be compared to science-target anomaly rates without a front-loaded warning

Section/page: §VI.E, p. 20; §VII item 1, pp. 20–21.
Issue: The comparison section now correctly says the 0.87% full-stream DESI rate and Liang et al.’s 1.07% science-target rate are different populations. However, the conclusion still leads with full-stream scale language, then gives the caveat parenthetically. Given the new recount, the warning should be in the first clause. 

paper3_anomaly_catalog_v3.1.95


Proposed fix: In the conclusion, replace “DESI-only is a ∼73× increase” with “DESI full-spectra-stream contains 195,829 anomaly detections, but the science-target-like subset is 2,468, ≈0.9× Liang et al.; the 73× number is not a source-catalog comparison.”

New MINORS

Table V, p. 20: Row (d) says B
mb/SMBHB
	​

=7.14×10
3
 is “decisive” without repeating “only versus the idealized circular-orbit SMBHB reference.” Add that phrase in the table row itself. 

paper3_anomaly_catalog_v3.1.95

Conclusion item 2, pp. 20–21: Lead with 17.8% genuine novelty, not 58.8% SIMBAD-unmatched. The paper correctly tells readers to quote 17.8%, but the conclusion still lists 58.8% first.

§III.A, p. 6: Replace “0% artifact rate” with “0/200 visually flagged; binomial upper limit …”.

Fig. 1 / §II.A, p. 3: The 83 display anomalies are force-included in the UMAP sample. The caption discloses this, but the main-text statement that high-score anomalies “concentrate” should say the force-included points are visual markers, not an unbiased density test. 

paper3_anomaly_catalog_v3.1.95

Table I, pp. 7–8: Still too footnote-heavy. Consider moving the long threshold/tiering explanation to a formal schema table.

§V.A / Table V: The NANOGrav caveat is now good, but the compact table row and conclusion should consistently say “not a cosmological detection.”

3. High-risk audit items

378,280 headline: Arithmetic remains internally consistent: native inputs sum to 388,493, 10,213 collapsed detections gives 378,280, stratified as 378,080 point-source-tier detections plus 200 Planck patches. The semantic issue is now sharper: the DESI component should be called full-stream fiber-spectral detections unless restricted to science targets.

7-way 5″ FoF arithmetic: The 10,213 = 637 + 9,576 reconciliation remains internally consistent, including the size-histogram and no chain-bridging audit. I do not flag the arithmetic.

Fisher positivity: The correct form 1/σ
2
(f
NL
	​

)=F
0
	​

+cα
2
 is retained and now made numerically auditable: F
0
	​

=1/8.98
2
=0.01239, 1/σ
2
=0.01509, σ=8.14, with envelope [3.92,8.98]. This is correct; the envelope, not the convex central value, is the right summary.

α=0.19±0.65: The central value remains <1σ from null and the de-biased estimate returns no improvement. That is now clearly stated. 

paper3_anomaly_catalog_v3.1.95

v3.1.71 cross-vendor R-round: Still not verifiable from the PDF or supplied sandbox artifacts.

NANOGrav: The γ=2.567±0.382, matter-bounce +1.13σ, idealized SMBHB +4.61σ, and B
mb/SMBHB
	​

=7.14×10
3
 numbers remain internally consistent. The environmental-SMBHB caveat is now strong enough; just repeat it in tables/conclusion. 

paper3_anomaly_catalog_v3.1.95

4. Updated recommendation

MAJOR REVISIONS. The paper moved toward publishability, but the DESI recount must be propagated through all downstream DESI rates, novelty claims, QSO-candidate/cosmology samples, and source/object vocabulary before this can be treated as a minor-revision catalogue paper.
