# P5 — Environmental Dependence of Spiral Chirality Across DESI Large-Scale Structure

> **CURRENT STATUS (2026-08-04):** selected standalone AJ companion,
> v0.1.147, technical package 95/100 pending Houston approval. The historical
> bootstrap plan below is preserved only as development provenance; it is not
> the current execution state. Use the
> [final portal kit](paper/AJ_PORTAL_KIT_v0.1.147-2026-08-03.md) and the
> [publication and release master map](../../project-context/PUBLICATION_AND_RELEASE_MASTER_MAP_2026-08-04.md)
> for publication work.

**Historical status recorded below:** Bootstrap (2026-05-15). Scaffolding complete; awaiting first data fetch.

**Working title:** *Environmental Dependence of Spiral Chirality Across DESI Large-Scale Structure*

**Scientific question (conservative framing):**
> Is galaxy chirality statistically independent of DESI-derived large-scale
> structure environment after controlling for sky position, redshift, imaging
> systematics, morphology confidence, and selection effects?

This pipeline is **separate from P4** (chirality catalog / null global parity).
P4 stays clean as the standalone catalog paper; P5 inherits P4's chirality
labels and asks an environment-dependent question that P4 is not designed to
answer.

## Inputs (canonical)

| Role | Source | Local cache |
|------|--------|-------------|
| Chirality (per-galaxy) | HF `bamfai/galaxy-chirality-catalog/catalog_production.parquet` (8,474,531 rows, post-TTA equivariant) | `data/p4_chirality.parquet` |
| Redshift / DESI spectra | DESI DR1 `zall-pix-iron.fits` (~22.5M rows) | `data/desi_zall.fits` |
| LSS / target context | DESI DR1 LSS VAC (BGS/LRG/ELG/QSO) | `data/desi_lss/` |
| Environment (filament/void/density) | **MISSING** — see `reports/00_audit.md` § "Environmental data blocker" | — |

**`187-attribute catalog` referenced in prior work:** confirmed not present in
the repository (audit, 2026-05-15). Treated as a future fetch target; P5 uses
DESI DR1 native columns for the first matched catalog and adds environmental
attributes as a separate join once the source is resolved.

## What this pipeline produces

1. `data/p4_chirality.parquet` — local mirror of the HF catalog (8.47M rows).
2. `data/desi_zall.parquet` — converted DESI DR1 redshift catalog.
3. `results/p5_matched_chirality_desi.parquet` — angular cross-match output
   (one row per matched galaxy, all join keys + provenance fields preserved).
4. `results/p5_matched_chirality_desi_summary.json` — counts before/after every
   filter, sky coverage, redshift distribution, target-class breakdown.
5. `results/p5_crossmatch_diagnostics.md` — human-readable schema dump +
   provenance trace.
6. Analysis modules (`results/analysis_*/`):
   - chirality vs redshift
   - chirality vs local density
   - chirality vs cosmic-web environment (placeholder until env data lands)
   - regional coherence (HEALPix)
   - systematics + null tests
7. Figures (`figures/`).
8. Paper draft (`paper/p5_desi_chirality.tex`).

## Operating rules

- Conservative language. The default claim is *"no evidence for environmental
  dependence beyond selection."* Every effect needs effect size + uncertainty
  + null comparison + multi-threshold robustness before it gets stronger
  language.
- Every run is reproducible from `config/p5_config.yaml`. No notebook-only
  state. No hand-edited intermediate files.
- Provenance: every output `.parquet` ships with a `*_provenance.json` sidecar
  recording inputs, config hash, git SHA, row counts pre/post each filter.
- Do not mutate P4 artifacts. P5 reads `catalog_production.parquet` and writes
  derived products only under `pipelines/p5_desi_chirality/`.

## Reproducibility

```bash
cd pipelines/p5_desi_chirality
python scripts/01_fetch_p4_catalog.py         # HF download (one-time, ~600 MB)
python scripts/02_fetch_desi_dr1.py           # DESI DR1 redshift catalog (~3 GB)
python scripts/03_crossmatch.py --config config/p5_config.yaml
python scripts/04_diagnostics.py
python scripts/05_analysis_redshift.py
python scripts/06_analysis_density.py
python scripts/07_analysis_healpix.py
python scripts/08_analysis_cosmic_web.py      # blocked on env data
python scripts/09_systematics.py
python scripts/10_make_figures.py
```

## Relation to existing work

- `pipelines/p1_highz_tracers/outputs/chirality_crossmatch/` already
  cross-matched the 2,145 DESI spectral *anomalies* with chirality and found
  near-zero overlap due to non-overlapping selection functions. P5 is the
  inverse join: full DESI DR1 redshift catalog (galaxies, not anomalies)
  against the canonical 8.47M chirality catalog. Expect ~hundreds of
  thousands of matches, not five.
- P4 paper (`pipelines/p2_chirality/chirality_catalog_paper.tex`) reports the
  global CW fraction is 0.4974 ± 0.000279 across 3.2M spirals — consistent
  with parity. P5 asks whether that null holds *bin-by-bin* in redshift,
  density, and cosmic-web environment.
