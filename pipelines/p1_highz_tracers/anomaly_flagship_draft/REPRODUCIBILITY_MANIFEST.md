# Reproducibility manifest — anomaly flagship manuscript (vAF.0.2)

Directive Q2. Everything needed to reproduce every number in `main.tex`:
external data sources with links, APIs, exact scripts, compute venue,
reproduction cost, and wall-clock. Two stages: the **scan and
characterisation** (GPU, already run and landed) and the **assembly** (CPU,
local, re-runnable in under a minute).

## 1. External data sources

| Source | What is used | Link | Access |
|---|---|---|---|
| DESI DR1 (`iron`) zcatalog | `zall-pix-iron.fits`; 27,547,223 unique science `TARGETID`s; redshift, `ZWARN`, `SPECTYPE`, `DELTACHI2`, `OBJTYPE`, `COADD_FIBERSTATUS` | https://data.desi.lbl.gov/public/dr1/ | public, no account |
| DESI DR1 coadd spectra | per-`(survey, program, healpix)` coadd FITS, streamed and scored in place (never bulk-downloaded) | https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/ | public, no account |
| DESI Legacy Imaging Surveys DR9/DR10 photometry | `FLUX_G/R/Z/W1/W2`, `MORPHTYPE`, `SHAPE_R`, `SERSIC`, `EBV`, Gaia columns (carried in the DESI target catalogue) | https://www.legacysurvey.org/ | public |
| SIMBAD | object cross-identification, 3.0″ cone | via `astroquery.simbad` (v0.4.11), https://simbad.cds.unistra.fr/ | public API, rate-limited |
| NED | object cross-identification, 3.0″ cone | via `astroquery.ipac.ned`, https://ned.ipac.caltech.edu/ | public API, rate-limited |
| AllWISE (VizieR `II/328/allwise`) | `W1`, `W2`, `W1−W2`, 3.0″ cone | via `astroquery.vizier`, https://vizier.cds.unistra.fr/ | public API |
| VizieR reference classes (benchmark only) | BAL quasars, Roma-BZCAT (5th ed.), CV/WD binaries, LAEs, SLSN hosts | VizieR, cached locally at `~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02/` | public API |

APIs used: `astroquery` 0.4.11 (SIMBAD, NED, VizieR) and the DESI public HTTPS
data service. No authenticated or proprietary service is required to reproduce
any result.

## 2. Frozen model and contract

| Item | SHA-256 |
|---|---|
| Run contract (`clean-rerun-6699d09ff886`) | `6699d09ff886f74dab6608bd70a70b73b7a34afabc436d365c69f16a95ac5edf` |
| Archived autoencoder `best_model_47k.pt` | `f5266ba48f476bca2f1b12610e0e81322caaa955af70ab83f0b05bf763885f07` |
| Inference code | `3e7efb243fa5cc4e7e06c5ce8e13f011e1173d2cc44aecd8df47e0c67c0ab996` |
| DESI zcatalog | `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b` |
| `flagship_sample_v2.parquet` | `d6d43dfa04d6a8b2b4d014f5f4899b5e5b844144a50b6c88e01a9a771a6baa5f` |
| `flagship_sample_v2_enriched.parquet` | `c3b176ff2d355a421ac48d00c5b6565fdfce8956fe6298eb85596bfb94f09fff` |
| `flagship_crossmatch_v2_matched.parquet` | `4a718d1a7ad253d2f91c69841d81e3b8015650fc0ca1f4a711fa0ee9da17f135` |
| `flagship_crossmatch_v2_unmatched.parquet` | `c0a6b57bd672f81b1424a65449f99d891810073ea59e600c1fc35cfec30eb7c3` |
| `flagship_wise_v2.parquet` | `1b42125d5e62830cf44806a842b7253e787ec218c77b3a19e690eed4fedb40f3` |
| `flagship_taxonomy_v2.json` | `1420388b59f3727814dda63c90c8e4cd0d2226c1e6ad2907c3301ed844edbf60` |

All ten are re-verified by validation checks V2 and V3.

## 3. Stage A — scan and characterisation (already run)

| Property | Value |
|---|---|
| Scripts | `pipelines/p1_highz_tracers/clean_rerun_contract.py`, `outputs/enhanced_18M/enhanced_18M_inference.py`, `pod_phase3_v2.sh` stages 01–08, `pipelines/p1_highz_tracers/clean_rerun/gates/check_sample_provenance.py` |
| Compute venue | RunPod GPU pod `8ofv5d4ynu7hku` ($0.17/hr) |
| Wall-clock | 7 h 42 m 53 s end to end (2026-09-03 16:12:36Z → 23:55:29Z); per-stage breakdown in `project-context/PHASE3_V2_LANDING_2026-09-03.md` |
| Cost | ≈ **$1.31** (pod compute only) |
| Dominant stages | enrichment 2 h 43 m, SIMBAD/NED cross-match 3 h 24 m (rate-limited, not compute-bound), AllWISE 41 m |
| Reproduction note | the cross-match stage is dominated by public-service rate limits, so it reproduces at similar wall-clock on any machine; the scoring stage needs a GPU |
| Backups (checksum-verified) | local `~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/phase3_v2/2026-09-03/`; HuggingFace `bamfai/bigbounce-aug-011-clean-rerun` path `phase3_v2/2026-09-03/`; Backblaze B2 bucket `bigbounce` prefix `aug-011-clean-rerun/phase3_v2/2026-09-03/` |

## 4. Stage B — assembly of this manuscript's numbers (local, re-runnable)

| Property | Value |
|---|---|
| Scripts | `pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/assemble_flagship_evidence.py`, then `.../make_tables.py`, then `.../make_draft_figures.py` (vAF.0.2; reuses the first script's loaders and joins by import, so the two cannot diverge) |
| Inputs | only the ten hashed artifacts above (no network access) |
| Outputs | `flagship_assembly_2026-09-18/outputs/*` (validation contract, family evidence, follow-up set, provenance re-check, zcatalog re-join table, **`draft_numbers.json`** — every derived quantity quoted in `main.tex`) and this directory's `tables/*.tex` (11 tables), `figures/*.pdf` (9 figures) |
| Compute venue | local CPU (Apple silicon laptop); no GPU, no network |
| Wall-clock | < 60 s total for both scripts |
| Cost | ≈ **$0** |
| Environment | Python 3, `pandas` 3.0.5, `pyarrow` 25.0.0, `numpy` 2.5.1, `scipy` 1.18.0, `scikit-learn` 1.9.0, `matplotlib` 3.11.1 |
| Determinism | fully deterministic except the V12 permutation null, which is seeded (`numpy` default_rng(42), 50 draws) |

Reproduce:

```sh
cd <repo root>
python3 pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/assemble_flagship_evidence.py
python3 pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/make_tables.py
python3 pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/make_draft_figures.py
cd pipelines/p1_highz_tracers/anomaly_flagship_draft
for i in 1 2 3 4; do pdflatex -interaction=nonstopmode main.tex; done
```

Expected: validation contract V1–V12 as recorded (13 PASS, V11 and DEFECT-3
REPORTED, DEFECT-1 and DEFECT-2 FAIL by design — they are the known defects
the release carries openly), then a 15-page PDF with 0 undefined references
and 0 overfull hboxes.

## 5. Manuscript build

| Property | Value |
|---|---|
| Source | `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.tex` (`\paperVersion` = vAF.0.2) |
| Class | `revtex4-2` (`aps,prd,twocolumn`), the lab compile standard; the target venue is ApJS, so conversion to AASTeX is a packaging step, not a rewrite |
| Tables | 11 tables, machine-generated into `tables/` by `make_tables.py` and `make_draft_figures.py`; never hand-edited |
| Figures | 9 figures, all generated by committed scripts from the landed artifacts (no manual composites): `fig_sky_fraction`, `fig_score_distribution`, `fig_sky_distribution`, `fig_score_vs_quality`, `fig_band_residuals`, `fig_redshift_distribution`, `fig_latent_silhouette`, `fig_family_evidence`, `fig_fta_photometry`. The landed run's own `sky_fraction_by_score.png` is retained in the directory as the source artifact but is not used in the manuscript — its 0–1 y-axis makes the effect invisible, so `fig_sky_fraction.pdf` redraws the same released JSON on a readable scale. |
| Bibliography | inline `thebibliography`; no BibTeX pass required |
| Build | 4 × `pdflatex`; last verified 2026-09-19: 15 pages, 0 undefined references, 0 overfull hboxes, `/latex-audit` visual pass over all 15 rendered pages |

## 6. Not reproducible from public data alone

- The **archived autoencoder weights** (`best_model_47k.pt`) are a lab
  artifact, mirrored on HuggingFace and hash-bound here. Re-training from
  scratch is not part of this manuscript's reproduction path; scoring is
  reproducible given the frozen weights.
- The **per-object photometric significance** of any Legacy Survey flux in
  the released tables: the published schema carries `FLUX_*` but no
  `FLUX_IVAR_*`, so the Lyman-break check of §VII B can refute a candidate
  whose $g$ flux is far above the sample distribution but cannot confirm a
  dropout. DR10 forced photometry with inverse variances closes this at zero
  observing cost; the deposit must also carry the missing columns.
- The **selection function** (completeness/purity) does not exist yet for
  this model–substrate pair. It is open test OT-1 and requires GPU compute;
  nothing in this manuscript depends on it, and no population-level claim is
  made that would.
