# DESI DR1 Anomaly-Score Candidate Catalogue (v2, science-only)

*A machine-flagged catalogue of 1,244 spectroscopically unusual DESI DR1
objects, released as reproducible data infrastructure for follow-up
characterization.*

**Release date:** 2026-09-03
**Sample:** `flagship_sample_v2_enriched.parquet` (science-target-only,
anomaly_score > 3, n = 1,244)

---

## Purpose

An unsupervised autoencoder trained on DESI DR1 optical spectra assigns a
reconstruction-error anomaly score to every science-target spectrum in the
public `iron` release. This release publishes the resulting high-score
candidate catalogue — 1,244 objects — together with cross-match enrichment
against SIMBAD, NED, and AllWISE, and an unsupervised descriptive taxonomy
over the objects that current databases do not already identify. The
catalogue is offered as a starting point for targeted spectroscopic or
imaging follow-up, not as a claim of new astrophysical classes.

## Data

- **DESI DR1 (`iron`) zcatalog** — `zall-pix-iron.fits`, the public
  spectroscopic redshift catalogue for DESI Data Release 1. 27,547,223
  unique science-target `TARGETID`s scanned; source: DESI public data
  release (https://data.desi.lbl.gov/public/dr1/).
- **DESI DR1 coadd spectra** — per-`(survey, program, healpix)` coadd FITS
  files streamed and scored pixel-by-pixel, never bulk-downloaded (see
  `pipelines/p1_highz_tracers/clean_rerun/RUNBOOK.md` §0).
- **SIMBAD / NED** — queried via `astroquery` (v0.4.11) at a 3.0-arcsec
  match radius for object cross-identification.
- **AllWISE (VizieR `II/328/allwise`)** — queried via `astroquery.vizier`
  at a 3.0-arcsec match radius for infrared colours.
- **VizieR reference classes** (recovery benchmark only) — BAL quasars,
  Roma-BZCAT blazars (5th ed.), cataclysmic variables/white-dwarf binaries,
  Lyman-alpha emitters, superluminous-supernova host galaxies; fetched and
  cached under `~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02/`.

## Method

### Anomaly score

Every science-target spectrum is scored by the archived BigAE autoencoder
(`best_model_47k.pt`, a 496→128 reconstruction network) via
`outputs/enhanced_18M/enhanced_18M_inference.py` — both artifacts frozen and
never modified for this run, per the clean-rerun contract in
`pipelines/p1_highz_tracers/clean_rerun_contract.py`. The anomaly score is
the model's reconstruction-error statistic; higher scores indicate spectra
the model reconstructs less well, i.e. spectra less like the training
distribution's typical shapes. Architecture, training provenance, and the
full inference contract are documented in the clean-rerun runbook
(`pipelines/p1_highz_tracers/clean_rerun/RUNBOOK.md`) and are not
re-derived here.

### Science-target selection

Earlier characterization passes over this scan (see "Known limitations of
the prior sample" below) selected candidates by anomaly score alone. This
release instead applies an explicit provenance gate before any score
threshold: a row qualifies as a science target only if `OBJTYPE == 'TGT'`
**and** `COADD_FIBERSTATUS == 0` **and** `TARGETID > 0` (asserted, not just
filtered). This excludes sky fibers, standard-star fibers, and any row
without a positive, sanity-checked `TARGETID`. `03_CHOOSE_THRESHOLD_AND_BUILD`'s
output passed `gates/check_sample_provenance.py` clean (0 rows flagged).

### Sky-fraction-by-score validation

Before choosing a score threshold, every candidate row across the full
scanned score range was classified science-target vs. sky-or-nonscience and
binned by anomaly score. The resulting curve (Figure 1) is the validation
evidence that a naive top-score cut without the provenance gate would be
dominated by non-astrophysical fibers: in every score bin above 3, more
than 99.5% of rows are sky-or-nonscience, and the sky-or-nonscience
fraction *rises* with score (99.53% in `[3,4)` to 99.97% in `[8,10)`) —
i.e. the model's highest-confidence anomalies, in raw fiber counts, are
overwhelmingly instrumental artifacts, not astrophysically unusual sources.
Only after this gate is applied do the reported science-target counts and
the released catalogue reflect real objects.

| Score bin | Total fibers | Science targets | Sky-or-nonscience fraction |
|---|---|---|---|
| [3, 4) | 234,365 | 1,092 | 99.53% |
| [4, 5) | 33,865 | 108 | 99.68% |
| [5, 6) | 25,008 | 24 | 99.90% |
| [6, 8) | 23,370 | 18 | 99.92% |
| [8, 10) | 3,473 | 1 | 99.97% |
| [10, 24.42] | 337 | 1 | 99.70% |

Figure: `figures/sky_fraction_by_score.png`.

### Threshold selection (pre-declared rule)

The release threshold was chosen by a rule fixed before inspecting the
science-only counts: from the grid {3, 4, 5, 6, 8, 10}, take the largest
threshold whose science-only count is ≥ 300; if that count exceeds 1,500,
step to the next-larger grid point unless doing so would drop the count
below 300.

| Threshold (σ) | Science-only count |
|---|---|
| 3 | 1,244 |
| 4 | 152 |
| 5 | 44 |
| 6 | 20 |
| 8 | 2 |
| 10 | 1 |

Applying the rule selects **threshold = 3** (count 1,244, the largest grid
value clearing 300 and not exceeding 1,500). This is the released sample.

## Contents of the release

- **1,244 objects** (`flagship_sample_v2_enriched.parquet`), each carrying
  `TARGETID`, sky position (`target_ra`, `target_dec`), DESI `survey` /
  `program`, redshift and spectral-classification fields from the zcatalog,
  and `anomaly_score`.
- **Enrichment**: SIMBAD/NED cross-match flag and matched name/type where
  available (`flagship_crossmatch_v2_matched.parquet` /
  `..._unmatched.parquet`); AllWISE colours for 74/1,244 matched objects
  (`flagship_wise_v2.parquet`).
- **Cross-match outcome**: 569/1,244 (45.7%) matched an existing SIMBAD or
  NED entry (562 via NED, 38 via SIMBAD — some rows match both); 675/1,244
  (54.3%) are unmatched, i.e. not already carrying a catalogued
  identification in either database.
- **VizieR reference-class enrichment**: one object positionally coincides
  with a cataloged BAL quasar (4.2× base-rate enrichment over the 5,285
  in-footprint BAL-quasar references); see the recovery benchmark below.
- **Descriptive taxonomy** (`flagship_taxonomy_v2.json`): the 675
  SIMBAD/NED-unmatched objects are grouped by PCA→UMAP→HDBSCAN clustering
  on `(anomaly_score, ra, dec)` into 25 clusters, which roll up by
  descriptor identity into 8 candidate families. These are unsupervised
  groupings — descriptive labels only, not confirmed astrophysical
  classes, per the release's labeling policy (no invented class names).

| Family | Score tier | Dominant survey/program | N objects | Descriptor |
|---|---|---|---|---|
| 0 | low | main / dark | 302 | low-anomaly-score candidate family |
| 1 | elevated | main / dark | 87 | elevated-anomaly-score candidate family |
| 2 | elevated | sv3 / bright | 71 | elevated-anomaly-score candidate family |
| 3 | extreme | sv3 / bright | 61 | extreme-anomaly-score candidate family |
| 4 | low | sv3 / bright | 44 | low-anomaly-score candidate family |
| 5 | low | sv1 / other | 38 | low-anomaly-score candidate family |
| 6 | high | main / dark | 36 | high-anomaly-score candidate family |
| 7 | high | sv3 / bright | 36 | high-anomaly-score candidate family |

(Family sizes sum to 675, exactly the SIMBAD/NED-unmatched count.)

## Known-object recovery benchmark

To test whether the catalogue's highest-score objects recover published
classes of spectroscopically unusual objects, five reference classes with
identifiable positions were positionally cross-matched (1.5-arcsec radius)
against the released sample.

| Reference class | N in footprint | N matched | Enrichment | Recovery |
|---|---|---|---|---|
| Broad absorption line (BAL) quasars | 5,285 | 1 | 4.2× | 0.019% |
| Roma-BZCAT blazars (5th ed.) | 2,060 | 0 | 0.0× | 0.000% |
| Cataclysmic variables / white-dwarf binaries | 580 | 0 | 0.0× | 0.000% |
| Lyman-alpha emitters (LAEs) | 84 | 0 | 0.0× | 0.000% |
| Superluminous supernova (SLSN) host galaxies | 27 | 0 | 0.0× | 0.000% |

Stated honestly: **no reference class is confirmed recovered** by this
catalogue at the pre-declared bar (≥1 class, >10× enrichment, ≥5 positional
matches). The single BAL-quasar match is the only nonzero cell and clears
neither the enrichment nor the match-count criterion. This benchmark result
is the basis for releasing the catalogue as data infrastructure rather than
as a discovery paper — see `project-context/NEXT_SCIENCE_LEDGER.md` row 8
and `project-context/PAPER_LINEAGE_2026-08-05.md`.

## Reproducibility

- **Provenance manifests** (sha256-bound, in this repo at
  `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/`):
  `flagship_sample_v2_manifest.json`, `flagship_enriched_v2_manifest.json`,
  `flagship_crossmatch_v2_manifest.json`, `flagship_wise_v2_manifest.json`,
  `flagship_taxonomy_v2_manifest.json`, `threshold_choice.json`,
  `science_target_summary.json`, `sky_fraction_by_score.json`.
- **Compute venue**: RunPod pod `8ofv5d4ynu7hku` (A4000-class GPU/
  CPU-strong instance, $0.17/hr).
- **Wall-clock**: 7h42m53s end to end (16:12:36Z–23:55:29Z, 2026-09-03),
  per-stage breakdown in `project-context/PHASE3_V2_LANDING_2026-09-03.md`.
- **Cost estimate**: ≈$1.31 (pod compute only, at $0.17/hr).
- **Mirrors** (backup-3plus, checksum-verified):
  - Local: `~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/phase3_v2/2026-09-03/`
  - HuggingFace: `bamfai/bigbounce-aug-011-clean-rerun`, path
    `phase3_v2/2026-09-03/`
  - Backblaze B2: bucket `bigbounce`, key prefix
    `aug-011-clean-rerun/phase3_v2/2026-09-03/`
- **Full landing receipt** (21 files, sha256 diff pod==local, 3-location
  checksum verification): `project-context/PHASE3_V2_LANDING_2026-09-03.md`.

## Limitations

- The autoencoder was trained on a fixed spectral template; anomaly score
  reflects reconstruction distance from that template, not a
  physically-motivated significance.
- The catalogue's SIMBAD/NED unmatched fraction (54.3%) includes objects
  simply outside existing survey footprints or below other surveys'
  detection thresholds, not only genuinely novel sources.
- The 8-family taxonomy is descriptive (unsupervised clustering on score
  and sky position only); it is not a claim of physically distinct object
  classes and should not be cited as such.
- The known-object recovery benchmark used only 5 of 11 candidate reference
  classes (the other 6 lacked identifiable RA/Dec columns or catalogue
  IDs); a wider reference-class sweep could change the recovery picture.
- This is a science-only re-run superseding an earlier characterization
  pass over the same score-tail candidates; users should reference this v2
  release, not any prior draft.

## How to cite

A Zenodo DOI for this release will be minted by Houston Golden prior to
public distribution (Houston-only action, not automatable). Cite as:

> Golden, H. (2026). *DESI DR1 Anomaly-Score Candidate Catalogue (v2)*.
> Zenodo. DOI: `[PLACEHOLDER — pending Houston-authorized minting]`.

Until the DOI is minted, cite the pinned repository commit and this
document's path:
`pipelines/p3_anomaly_engine/release/ANOMALY_CATALOGUE_RELEASE_v2_2026-09-03.md`,
https://github.com/Hubify-Projects/bigbounce.
