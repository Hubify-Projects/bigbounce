# DESI anomaly-science claim inventory

**Truth audit · 2026-08-03 · governs the anomaly-paper rebuild**

## Executive result

The original anomaly program contains real and potentially publishable science,
but no surviving manuscript may be submitted as written.

The strongest bounded scientific object currently preserved in the repository
is a **2,145-object filtered DESI candidate slice** and its **1,127-object
SIMBAD/NED-unmatched candidate taxonomy**. The 10 family groupings, IR
variability follow-up, and latent-space photo-z experiment are potentially
useful secondary results.

The full-scale lineage is not yet publication-ready. The 22,504,897-row,
173-column enhanced parent catalog and its 46 Parquet files are absent locally;
the exact enhanced-model asset is not present; `S>5` counts conflict; and
several memorable summary claims overstate or contradict their underlying
artifacts. The public 195,829-row frozen catalog remains real and downloadable,
but its absolute score normalization is not reproducible and most legacy IDs
cannot be rejoined to spectra.

Therefore:

- do not revive the deprecated multi-survey manuscript;
- do not treat current P3's 181 public IDs as the anomaly science;
- do not call the 1,127 objects discoveries or confirmed classes;
- restore or rebuild the selection lineage before drafting the new flagship.

## Data generations that were being conflated

| Generation | What it contains | Preserved state | Proper role |
|---|---|---|---|
| Original DESI scan | Frozen 195,829-row `S>5` candidate table with coordinates, legacy IDs, total score, and B/R/Z residuals | Public immutable HF artifact and local 10 MB Parquet; 195,790 unique legacy IDs | Legacy parent candidate catalog; usable only with explicit provenance limits |
| Enhanced full catalog | 22,504,897 rows, 173 columns, including 128 latent dimensions and DESI metadata | Only summary and downstream results remain locally; claimed 46 Parquets/~16 GB are absent | Must be restored or regenerated before it can support selection-level reproducibility |
| Filtered “silver” slice | 2,145 rows selected by `anomaly_score > 3.0` and `max_snr > 0.5` | Full cross-match result JSON and summary preserved | Best current bounded candidate sample, subject to parent-lineage restoration |
| Unmatched taxonomy | 1,127 of the 2,145 with no SIMBAD or NED match at 3 arcsec; 29 clusters merged into 10 descriptive families | Result JSON, summary, code, and figures preserved | Strongest candidate-science centerpiece; labels remain interpretations, not confirmations |
| Current P3 | 181 warning-free public TARGETID associations recovered from historical coordinates | Exact r17 technical package preserved | Technical recovery/data product; supporting output, not flagship science |

The numbers are not supposed to be forced into one denominator. They describe
different data generations and cuts. The problem was that project summaries
presented them as one continuously reproducible catalog.

## Claim-by-claim audit

| Claim | Direct evidence | Verdict | Allowed wording now |
|---|---|---|---|
| 22,504,897 spectra; 173 columns; 128 latent dimensions | `pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped/catalog_summary.json`; `scripts/enhanced_18M_inference.py` | **Result-only, not currently reproducible.** The 46 Parquets and exact enhanced-model asset are absent. | “A completed historical enhanced run reports 22,504,897 rows and 128 latent features; restoration/reproduction is pending.” |
| 195,829 `S>5` DESI anomalies | Public `desi_dr1_anomalies.parquet`; local frozen copy | **Frozen catalog verified, generation conflicted.** Public table has 195,829 rows and 195,790 unique legacy IDs. A later enhanced summary says 249,905 `S>5`. | “The frozen original release contains 195,829 reconstruction-outlier candidates.” Do not merge it with the later enhanced count. |
| 249,905 `S>5` enhanced anomalies | Enhanced summary JSON | **Unreconciled.** Cannot be regenerated from surviving local parent files. | Do not headline or compare until the parent run is restored and the score definition is reconciled. |
| 2,145 SNR-filtered candidates | `outputs/silver_crossmatch/silver_crossmatch_summary.json`; 2,145-row results JSON | **Recountable.** It is a distinct `score > 3`, `max_snr > 0.5` slice—not the same as the summary's `median_coadd_snr_r > 2` counts. | “A historical filtered candidate slice contains 2,145 rows under the recorded score/SNR rule.” |
| 1,127 uncataloged objects | Same cross-match summary/results | **Recountable but bounded.** Means no SIMBAD/NED match within 3 arcsec, not absent from every catalog. | “1,127 candidates are unmatched in the stated SIMBAD/NED cone searches.” |
| 10 astrophysical families; 76 AGN; 27 post-starburst | `outputs/uncataloged_taxonomy/taxonomy_results.json` and `taxonomy_summary.md` | **Descriptive candidate taxonomy.** Counts reproduce; physical labels do not constitute confirmation. | “The pipeline groups the 1,127 candidates into 10 interpretable candidate families, including 76 IR-bright AGN candidates and 27 post-starburst candidates.” |
| 0% false-positive rate and 10–1,377x enrichment | `outputs/injection_recovery/false_positive_analysis.json`, `injection_recovery_results.json`, and DESI proxy injection report | **Contradicted/overstated.** One star false positive exists at `S>5`; detailed tables peak below the 1,377x summary; a separate DESI NNLS-proxy study reports only 33.4% overall completeness. | Retire. Report per-class recovery and false-positive definitions directly, with the exact model and substrate named. |
| 9.5% `sigma(f_NL)` improvement | `outputs/fnl_tracer_selection/fnl_forecast.json`; `step6_alpha_empirical/alpha_empirical_results.json`; `step4_bias_validation/bias_validation.json` | **Not a result.** The large number is assumption-driven. Empirical `alpha = 0.19 +/- 0.65` is consistent with zero; the direct scenario in an earlier committed calculation improves the combined number by only about 0.04%. | “No defensible `f_NL` improvement is demonstrated.” Remove from the anomaly headline. |
| `sigma_NMAD = 0.028` photo-z from latents | `outputs/photo_z/metrics.json` | **Result-only, useful demonstration.** It is a supervised MLP trained on 800k rows and tested on 200k rows, using latent features from the absent enhanced parent. | “A supervised regressor on the historical latent vectors achieved `sigma_NMAD = 0.0279` on its recorded split.” Do not call it unsupervised photo-z. |
| `lat_067` is a spontaneous “redshift neuron” | Photo-z feature-importance output | **Overinterpretation.** `lat_067` is the most important feature in one fitted regressor, not a demonstrated neuron with an isolated causal encoding. | “`lat_067` had the largest feature importance in the recorded regressor.” |
| 16 IR-variable anomalies | `outputs/neowise_crossmatch/crossmatch_summary.json` | **Recountable, sample-limited.** 16 of 283 processed candidates meet the recorded variability rule; this is not the full 2,145. | “Sixteen of 283 examined candidates met the recorded NEOWISE variability criterion.” |
| `z=5.65` QSO with `W2=5.5 mag` | README only; detailed NEOWISE artifacts | **False conflation.** `5.522` is a W2 amplitude in a result, not a W2 magnitude; the exact headline object is not supported. | Retire until a named TARGETID and independently checked photometry/redshift support it. |
| 12 `z>6` QSO discoveries | `outputs/gold_anomalies/spectra/z6_qsos_detailed.json` | **Candidate list verified, discovery claim unsupported.** Twelve rows carry DESI Redrock QSO labels and `z>6`; independent redshift validation and novelty review are absent. | “Twelve anomaly-selected spectra are DESI-pipeline `z>6` QSO candidates.” |
| Exact released per-object scores are reproducible | `project-context/P3_REINFERENCE_PLAN.md`; `outputs/dp3_15_heldout_reinference.json` | **No.** Model behavior and injection recovery reproduce on a 20k held-out substrate, but the production absolute normalization and most `tid -> spectrum` joins are lost. | State the successful bounded pipeline validation and the exact per-object reproduction failure together. |

## What is genuinely notable

1. **Survey-scale candidate generation happened.** The frozen public artifact
   contains 195,829 DESI reconstruction-outlier rows; the enhanced run reports
   22.5 million processed spectra.
2. **A scientifically interpretable filtered sample survives.** The 2,145-row
   slice and 1,127 unmatched candidates are preserved row by row, not merely as
   prose.
3. **The taxonomy is more interesting than the raw count.** Ten candidate
   families create concrete follow-up targets and falsifiable class hypotheses.
4. **There are named follow-up demonstrations.** NEOWISE variability, latent
   photo-z, spectral line analysis, and 12 DESI-pipeline `z>6` candidates can be
   reported with appropriate labels.
5. **The failure history is scientifically useful.** Injection-recovery is
   strongly class-dependent, absolute score reproduction failed, and public-ID
   recovery exposed a real provenance limitation. A good paper can treat these
   as method boundaries rather than hiding them.

## Recommended flagship scope

### Preferred route: restore, then publish the filtered-candidate science

Build a DESI-only paper around this question:

> What astrophysical candidate populations survive a reproducible,
> SNR-aware filtering and external-catalog follow-up of a survey-scale DESI
> autoencoder scan?

Proposed central deliverable:

- a manifest-bound 2,145-row candidate table;
- the 1,127 SIMBAD/NED-unmatched subset;
- the 10 candidate-family taxonomy;
- per-class injection-recovery limitations;
- a bounded set of named, auditable spectral/IR follow-up examples;
- current P3's public-ID machinery integrated as provenance support.

This route is allowed only after the 22.5M enhanced parent artifacts and exact
model/selection lineage are restored or the sample is regenerated from public
inputs.

### Fallback route: rerun a clean DESI survey

If the enhanced parent cannot be recovered, run a new end-to-end DESI DR1 scan
with public TARGETIDs from ingestion, an immutable input manifest, a locked
model and normalization, held-out/injection validation, checkpointed outputs,
and row-level public release. The old 195,829 and 2,145 products become
historical comparison sets rather than the new paper's primary sample.

This is slower but scientifically cleaner than trying to prove that lost
production state still exists.

## Required closure gates before manuscript drafting

1. Locate the 46 enhanced Parquets and exact enhanced-model weights in local,
   HF, Backblaze, RunPod backup, or You.md source catalogs; verify hashes before
   trusting them.
2. Reconcile 195,829 versus 249,905 and document whether the change is input
   population, deduplication, normalization, threshold, or model generation.
3. Create an immutable manifest for the 2,145 and 1,127 tables with exact schema,
   selection code, row counts, hashes, and source-parent binding.
4. Re-run the selection and taxonomy from the restored parent; require exact or
   explained agreement.
5. Replace summary-level injection claims with per-class, exact-model results.
6. Independently validate any named high-redshift or physical-class candidate
   before using “discovery,” “confirmed,” or population language.
7. Keep `f_NL` out of the anomaly paper unless a proper selection-function and
   survey-window analysis produces a nonzero, defensible result.

## Current strategic status

**Promising science, not submission-ready.** The anomaly program belongs among
the three core research stories, but its flagship manuscript is now a rebuild
project. Current P3 remains a technically complete supporting package on
editorial hold.
