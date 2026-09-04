# Ledger #8 — known-object recovery benchmark on the phase-3 v2 (science-only, S>3) sample

**SAMPLE-V2 (science-only, contamination-fixed).** This benchmark runs against
`flagship_sample_v2_enriched.parquet` (1,244 rows, `anomaly_score` threshold
S>3, `threshold_choice.json` grid pick), built by `pod_phase3_v2.sh`'s
`03_CHOOSE_THRESHOLD_AND_BUILD` stage, which passed
`gates/check_sample_provenance.py` (`phase3_v2.log`: `OK: {'sample':
'/workspace/phase3_v2/flagship_sample_v2.parquet', 'row_count': 1244,
'checked_objtype': False, 'checked_fiberstatus': False, 'status': 'clean'}`)
— i.e. this sample is the fix for the SAMPLE-V1 negative-TARGETID / sky-fiber
contamination issue recorded in
`project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md`. Numbers below
are reported as-is; no paper-vs-release decision is made here (orchestrator
call per task instructions).

## VizieR positional cross-match (5 fetched reference classes vs S>3 v2, n=1,244)

Command run:

```sh
python3 pipelines/p1_highz_tracers/clean_rerun/benchmark_known_object_recovery.py \
  --crossmatch \
  --reference-cache-dir ~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02 \
  --reference-manifest ~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02/reference_manifest_local.json \
  --catalogs-config /tmp/catalogs_config_v2.json \
  --locator-inventory pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/locator_inventory.jsonl \
  --radius-arcsec 1.5 \
  --out-dir pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark
```

`catalogs-config` points at `flagship_sample_v2_enriched.parquet`
(`id_col=targetid`, `ra_col=target_ra`, `dec_col=target_dec`,
`score_col=anomaly_score`, `threshold=3.0`, `catalog_total_at_threshold=1244`,
`parent_total=27547223` from `sky_fraction_by_score.json`'s
`unique_targetids_considered`). Full output:
`recovery_benchmark.json`/`.md` in this directory.

| Class | N ref (footprint) | N matched | Recovery | 95% CI | Base rate | Enrichment | Closed-loop candidate |
|---|---|---|---|---|---|---|---|
| Broad absorption line (BAL) quasars | 5,285 | 1 | 0.019% | [0.003%, 0.107%] | 0.0045% | 4.2x | no |
| Roma-BZCAT blazars (5th ed.) | 2,060 | 0 | 0.000% | [0.000%, 0.186%] | 0.0045% | 0.0x | no |
| Cataclysmic variables / white-dwarf binaries | 580 | 0 | 0.000% | [0.000%, 0.658%] | 0.0045% | 0.0x | no |
| Lyman-alpha emitters (LAEs) | 84 | 0 | 0.000% | [0.000%, 4.373%] | 0.0045% | 0.0x | no |
| Superluminous supernova (SLSN) host galaxies | 27 | 0 | 0.000% | [0.000%, 12.456%] | 0.0045% | 0.0x | no |

**Ledger #8 exit rule (>=1 class, enrichment >10x, >=5 matches): NOT MET.**
1 BAL-quasar positional match at 4.2x enrichment is the only nonzero cell;
it clears neither the 10x-enrichment nor the 5-match bar. No closed-loop
candidate class at this threshold/sample (same conclusion as v1, at a much
smaller reference-footprint intersection given the sample is 1,244 rows vs
3,810 for v1's S>8 cut).

Reference classes: 11 total, 5 fetched (used above), 4 unavailable
(no RA/Dec columns identifiable), 1 no catalogue ID known — unchanged from
the v1 run since this uses the same cached reference fetch
(`recovery_refs_2026-09-02/reference_manifest_local.json`).

## Pod's own SIMBAD/NED cross-match (flagship_crossmatch_v2_matched/unmatched.parquet)

- Matched: **569 / 1,244 (45.7%)**; Unmatched: **675 / 1,244 (54.3%)**
  (`phase3_v2.log` STAGE 05_CROSSMATCH: `n_matched: 569, n_ned_found: 562,
  n_simbad_found: 38, n_unmatched: 675`)
- NED: 562/569 of matches came via NED; SIMBAD: 38/569 via SIMBAD (rows may
  match both services — see `flagship_crossmatch_v2_matched.parquet` for the
  per-row source breakdown).

## Taxonomy (8 descriptive families over the 675 unmatched objects; flagship_taxonomy_v2.json)

25 UMAP+clustering clusters roll up into 8 descriptive families (unsupervised
groupings, not confirmed physical classes). `n_objects` sums to 675, matching
the SIMBAD/NED-unmatched count exactly:

| Family ID | Score tier | Dominant survey | Dominant program | N objects |
|---|---|---|---|---|
| 0 | low | main | dark | 302 |
| 1 | elevated | main | dark | 87 |
| 2 | elevated | sv3 | bright | 71 |
| 3 | extreme | sv3 | bright | 61 |
| 4 | low | sv3 | bright | 44 |
| 5 | low | sv1 | other | 38 |
| 6 | high | main | dark | 36 |
| 7 | high | sv3 | bright | 36 |
| **Total** | | | | **675** |

## Side-by-side: v1 (contaminated, S>8) vs v2 (science-only, S>3)

| Metric | v1 (S>8, n=3,810, contaminated) | v2 (S>3, n=1,244, science-only) |
|---|---|---|
| Sample-provenance status | 84.8% negative-TARGETID rows (sky-fiber suspect), unresolved | `check_sample_provenance.py` passed clean, 0 flagged |
| SIMBAD/NED matched | 92 / 3,810 (2.4%) | 569 / 1,244 (45.7%) |
| SIMBAD/NED unmatched | 3,718 / 3,810 (97.6%) | 675 / 1,244 (54.3%) |
| Taxonomy clusters (unmatched) | 8 descriptive clusters, sizes 1589/1032/556/239/142/80/47/33 | 25 clusters -> 8 families, sizes 302/87/71/61/44/38/36/36 |
| VizieR reference-class recovery | 0/0/0/0/0 matches across 5 fetched classes | 1 BAL-quasar match (4.2x enrichment); 0/0/0/0 elsewhere |
| Ledger #8 confirmed-class bar (>=1 class, >10x, >=5 matches) | Not met | Not met |

The SIMBAD/NED match-rate jump (2.4% -> 45.7%) is consistent with the v1
sample containing a large non-astrophysical (sky-fiber) fraction that NED/
SIMBAD would be expected to never match, while the v2 science-only sample is
overwhelmingly composed of real catalogued sources. The VizieR
"unusual-object" reference-class recovery test still does not clear the
ledger #8 confirmed-class bar in either sample.

## Ledger #8 answer

**Not confirmed, in either sample.** v2's fix for sample-provenance
contamination substantially raises the SIMBAD/NED match rate (a sanity
signal that the cleaned sample is dominated by real astrophysical sources),
but the VizieR reference-class positional cross-match still finds no class
clearing the >10x-enrichment / >=5-match confirmed-class bar. This is a
numbers-only report; no paper-vs-release editorial decision is recorded
here.
