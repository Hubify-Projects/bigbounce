# DESI DR1 spectral anomaly research program

**Status:** Publication architecture and provenance rebuild in progress

This directory previously compressed several different data generations into
one “Paper 3” summary. That framing is superseded. Read:

- `project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`
- `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`

The active `pipelines/p3_anomaly_engine/paper3_apjs.tex` is a 181-row
public-ID recovery technical note. It does **not** replace the original DESI
anomaly-discovery science.

## Overview
The historical enhanced run reports 22,504,897 DESI DR1 rows and 128 latent
features. Its claimed 46 Parquet parent files and exact enhanced-model asset
are not currently present locally. A preserved 2,145-row filtered candidate
slice contains 1,127 rows unmatched in the recorded SIMBAD/NED 3-arcsec
searches. Those are candidates—not confirmed discoveries or objects proven
absent from every catalog.

## Supported results worth rebuilding around

- 1,127 SIMBAD/NED-unmatched candidates grouped into 10 descriptive candidate
  families, including 76 IR-bright AGN candidates and 27 post-starburst
  candidates.
- 16 of 283 examined candidates meet the recorded NEOWISE variability rule.
- A supervised MLP using historical latent features records
  `sigma_NMAD=0.0279` on its stored train/test split.
- 12 anomaly-selected spectra carry DESI Redrock QSO labels with `z>6`; they
  remain candidates pending independent redshift and novelty validation.

Retired claims: 9.5% `f_NL` improvement, 0% false positives, 1,377x enrichment,
“redshift neuron,” confirmed `z>6` discoveries, and the `z=5.65` / `W2=5.5
mag` headline. Their underlying artifacts either contradict the summary or do
not support the stronger wording.

## Files
- Deprecated manuscript stub: `arxiv/paper3_anomaly_catalog.tex`
- Pipeline: `pipelines/p1_highz_tracers/`
- Enhanced parent summary: `pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped/catalog_summary.json` (the historical 46 Parquets/~16 GB are not present locally)
- Gold anomalies: `pipelines/p1_highz_tracers/outputs/gold_anomalies/`
- Taxonomy: `pipelines/p1_highz_tracers/outputs/uncataloged_taxonomy/`
- Sky maps: `pipelines/p1_highz_tracers/outputs/sky_maps/`
- Photo-z: `pipelines/p1_highz_tracers/outputs/photo_z/`
- NEOWISE: `pipelines/p1_highz_tracers/outputs/neowise_crossmatch/`
- Cross-match: `pipelines/p1_highz_tracers/outputs/silver_crossmatch/`
- Explorer: `anomaly-explorer.html`
- Model: [bamfai/desi-spectral-anomaly-detector](https://huggingface.co/bamfai/desi-spectral-anomaly-detector)

## Next gate

Restore the enhanced parent/model and reproduce the 2,145/1,127 selection, or
rerun a clean public-ID-first DESI scan. Do not draft the flagship manuscript
until that choice is closed.
