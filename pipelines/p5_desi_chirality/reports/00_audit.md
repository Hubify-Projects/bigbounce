# P5 Repo Audit — 2026-05-15

## Scope

Establish what P5 ("Environmental Dependence of Spiral Chirality Across DESI Large-Scale Structure") can do today, what it needs to fetch, and what is permanently blocked on external data.

---

## 1. Available inputs

| Asset | Location | Rows | Notes |
|-------|----------|------|-------|
| P4 chirality catalog (canonical, post-TTA) | HuggingFace `bamfai/galaxy-chirality-catalog/catalog_production.parquet`, revision `paper4-v1.0.90` | 8,474,531 | Local fetch via `scripts/01_fetch_p4_catalog.py`. Currently **not on local disk** — only metadata sidecars at `pipelines/p2_chirality/outputs/canonical_provenance/` are present. |
| P4 high-confidence spiral subset | HF `catalog_c_hc_spiral_p_cw_gt_0p6.parquet` | 2,107,494 | Optional robustness rerun input. |
| Existing chirality × DESI-anomaly crossmatch | `pipelines/p1_highz_tracers/outputs/chirality_crossmatch/` | 5 (5″) / 136 (30″) | Different question; uses DESI **anomaly** sample (2,145 sources), not the full DR1 redshift catalog. Reference only — does not substitute for P5. |
| DESI DR1 anomaly metadata | `pipelines/p1_highz_tracers/outputs/desi_dr1/anomalies_for_xmatch.csv` | 195,829 | RA, Dec, anomaly score, target id; no redshift column. Subset of the 22.5M DR1 catalog. |
| DESI DR1 anomaly full JSON | `pipelines/p1_highz_tracers/outputs/desi_dr1/dr1_all_anomalies.json` | 195,829 | 36 MB; per-source band errors + reconstruction scores. |
| DESI taxonomy clusters | `pipelines/h200_results/pod_backup_20260408_full/outputs/desi-taxonomy/desi_taxonomy_clusters.csv` | 195,001 | UMAP + clustering on DESI anomalies. |
| DESI training shard metadata | `data/runpod_backups/ktds4mkmzb7ven_20260427/outputs/desi/training_shards/metadata.parquet` | ~47K | BigAE training sample; minimal columns. |

## 2. Missing inputs (blockers)

| Blocker | Severity | Mitigation |
|---------|----------|-----------|
| **P4 catalog not on local disk** | Low — fetch script ready | `python scripts/01_fetch_p4_catalog.py` (network + HF auth via `HF_TOKEN`). ~600 MB. |
| **DESI DR1 `zall-pix-iron.fits` not on local disk** | Low — fetch script ready | `python scripts/02_fetch_desi_dr1.py`. ~3 GB. Public, no auth required. |
| **"187 DESI-derived attributes" catalog NOT in repo** | Medium — used in original plan | Confirmed missing by exhaustive search (audit subagent, 2026-05-15). Two interpretations possible: (a) the file was never committed and lives on an old pod; (b) "187 attributes" referred to a count from a planned LSS VAC. Recommend: ask Houston where this file was originally produced; in parallel, P5 proceeds with DESI DR1 native columns (Z, ZWARN, SPECTYPE, TARGETID, PROGRAM, SURVEY, target bits, photometry, MORPHTYPE). |
| **Cosmic-web / environmental VAC** | High for analysis C | The DESI DR1 native catalog does **not** carry filament/void/cluster labels per source. Candidate sources: DESI DR1 LSS VAC (BGS/LRG/ELG/QSO catalogs with associated random catalogs — pending release), external void catalogs (Tempel+ 2018 SDSS DR12, Bisigello+ 2025, etc.) cross-matched on TARGETID via positional join. Until resolved, `08_analysis_cosmic_web.py` writes a schema contract instead of results — the pipeline does not silently produce nulls. |
| **3D density estimator** | Low (deferred) | Initial first-pass uses projected angular density. 3D density is a clear follow-up once the spectroscopic z column is in hand. |

## 3. Join keys + coordinate systems

- **Chirality side:** `ra`, `dec` (float64, ICRS J2000, degrees, 0–360 / –90 to +90). Object id: `objid` (int64, DESI Legacy DR8 Tractor brick+objid encoding).
- **DESI side:** `TARGET_RA`, `TARGET_DEC` (float64, J2000). Foreign key: `TARGETID` (int64). The matched table preserves both `objid` (P4) and `TARGETID` (DESI) as separate columns; no reliance on a derived id.
- Both catalogs reference the **same underlying imaging** (DESI Legacy DR8 / DR10), so position systematics should be sub-arcsecond. The 1″ primary radius is calibrated to this.

## 4. Catalog sizes

| Catalog | Rows | Spirals (CW + CCW) |
|---------|------|-------------------|
| P4 (post-TTA) | 8,474,531 | 3,201,160 |
| DESI DR1 (full, ZWARN==0, galaxies+QSOs, z ≤ 4) | ~13–18M (expected, after quality cuts) | n/a |
| Expected matched primary catalog at 1″ | rough order-of-magnitude estimate: **10⁵–10⁶ matched spirals**, dominated by the P4 catalogue's bright-end (r ≤ 17.8) galaxy population. Refine after first run. |

## 5. Version / provenance risks

| Risk | Notes |
|------|-------|
| HF revision drift | Mitigated: `paper4-v1.0.90` is pinned in `config/p5_config.yaml`; sidecars record observed vs expected row count. |
| DESI DR1 reduction churn | `zall-pix-iron.fits` is the iron-reduction canonical; should not change without a DR1.x version bump. Sidecar SHA-256 anchors the file. |
| P4 schema regression | The HF catalog dropped the `qc_flag` column carried by the intermediate Catalog C. We use `class_eq` + probability triplet (sufficient for QC). |
| Imaging-leg label inconsistency | P4 retains `imaging_leg` (BASS+MzLS / DECaLS / DES). DESI carries `PHOTSYS`/`SURVEY`; we cross-check, do not assume identical labelling. |

## 6. Reproducibility gaps

| Gap | Resolution |
|-----|-----------|
| First end-to-end run not yet executed | Requires network + disk; runnable on H200 pod or any host with ~5 GB free. |
| Environmental VAC missing | Documented contract in `scripts/08_analysis_cosmic_web.py`. |
| 187-attribute catalog provenance unknown | Open question — see §2 above. |

---

## Ranked TODO (scientific priority)

1. **Run the full fetch + cross-match end-to-end.** This is the load-bearing artefact: every downstream analysis depends on `results/p5_matched_chirality_desi.parquet`. Expected time: <1 hr on a pod with 16 GB RAM, including parquet round-trip.
2. **Validate the matched catalog's redshift distribution + sky footprint.** Does the matched sample inherit DESI's footprint as expected? Are there suspicious holes (e.g., DR8 Tractor coverage gaps that the chirality side trusted)?
3. **Run analyses A (redshift) and D (HEALPix coherence) first.** Both are fully self-contained on the matched catalog and produce the headline plots.
4. **Run analysis B (projected density).** Use this to set the bar for whether a sharper 3D density follow-up is worth the cost.
5. **Run the full systematics + null sweep (analysis E).** Without this, headline numbers are unverifiable. This is the gate before any draft sections are filled in.
6. **Resolve the environmental VAC question.**
   - 6a. Ask Houston whether the "187-attribute catalog" exists somewhere (old pod, external Zenodo, separate repo).
   - 6b. If it does, fetch + ingest + analyse C.
   - 6c. If it does not, plan a void/filament finder pass on the DESI DR1 LSS catalog (likely scikit-learn DBSCAN or DisPerSE-style filament tracing on the spectroscopic galaxy sample). Track as a separate sub-project under `pipelines/p5_desi_chirality/env_finder/`.
7. **Write the first draft of the abstract + §Results.** This requires the headline numbers from steps 3–5 in hand; do not draft prose against placeholder numbers.
8. **PDF compile pass.** First compile pass on the .tex skeleton to confirm `revtex4-2` formatting, `\artifact{}` link rendering, and that the bibliography stub builds clean.
9. **Houston Method completion gate.** Per `~/.claude/.../feedback_houston_method.md`: every experiment needs QC gate → scientific analysis → interpretation → cross-survey connection → site sync → queue expansion → backup. The first pass closes 4/7 (QC via systematics, analysis, interpretation, queue expansion); cross-survey connection (e.g., to P2 high-z tracers selection, to P3 anomaly engine) and site sync are explicit follow-up tasks.
10. **Decide on a Rubin/LSST follow-up window.** Note only — Rubin DP1 is commissioning, not survey data; revisit after first full LSST release.

---

## Operational notes

- All eight scripts pass `python -m py_compile` (syntactic). Runtime correctness is verifiable only after the two fetch scripts succeed.
- The codebase obeys the global rules: `\artifact{}` for repo paths, `revtex4-2` document class, deterministic seeds, provenance sidecars per output, no P4 modifications.
- Memory anchors honoured: (i) "Default to the hardest path" — chose the full DR1 join, not the anomaly-only subset; (ii) "No questions, full hard fix" — no clarification prompts; missing data blocked at the data layer, not the analysis layer; (iii) "Never defer path/dataset discovery" — DESI DR1 URL is hard-coded; HF revision is pinned; the only outstanding ambiguity is the 187-attribute file, flagged as TODO 6a.
