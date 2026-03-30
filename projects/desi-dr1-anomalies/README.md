# DESI DR1 Spectral Anomaly Catalog

**Status:** Analysis Complete | **Paper:** 3 (~80% ready) | **Target:** ApJS

## Overview
22,504,897 DESI DR1 spectra scored by BigAE autoencoder with 173-column enhanced catalog including 128-dim latent vectors. 2,145 SNR-filtered anomalies, 1,127 completely uncataloged.

## Key Results
- 9.5% σ(f_NL) improvement via latent-space multi-tracer
- 1,127 uncataloged objects in 10 astrophysical families (76 AGN, 27 post-starburst)
- 16 IR-variable anomalies (NEOWISE 10yr), z=5.65 QSO with W2=5.5 mag
- σ_NMAD=0.028 photo-z from unsupervised latent vectors
- lat_067 spontaneous "redshift neuron"
- 0% false positive, 10-1,377x enrichment at matched SNR
- 12 z>6 reionization-era QSOs

## Files
- Paper: `arxiv/paper3_anomaly_catalog.tex` (1000 lines, compiled PDF)
- Pipeline: `pipelines/p1_highz_tracers/`
- Catalog: `pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped/` (46 Parquet, 16GB)
- Gold anomalies: `pipelines/p1_highz_tracers/outputs/gold_anomalies/`
- Taxonomy: `pipelines/p1_highz_tracers/outputs/uncataloged_taxonomy/`
- Sky maps: `pipelines/p1_highz_tracers/outputs/sky_maps/`
- Photo-z: `pipelines/p1_highz_tracers/outputs/photo_z/`
- NEOWISE: `pipelines/p1_highz_tracers/outputs/neowise_crossmatch/`
- Cross-match: `pipelines/p1_highz_tracers/outputs/silver_crossmatch/`
- Explorer: `anomaly-explorer.html`
- Model: [bamfai/desi-spectral-anomaly-detector](https://huggingface.co/bamfai/desi-spectral-anomaly-detector)

## Cost
~$200 (H200 inference + analysis)
