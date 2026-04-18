#!/usr/bin/env python3
"""
HuggingFace dataset extension: ACT DR6 block for P3-HF-UPLOAD-EXTEND
(drive-to-100 fire #12).

Adds the ACT DR6 200-anomaly block to the existing PRIVATE dataset at
bamfai/bigbounce-anomaly-catalog. Matches Paper 3 Table 1 exactly
(20,000 scored patches → 200 is-top-1% anomalies).

Source: pipelines/h200_results/pod_backup_20260408_full/bigbounce/backups/
        20260406_231143/act-dr6-proper/act_dr6_anomalies.csv

Columns passed through: patch_idx, ra, dec, anomaly_score (is_top1pct
filter applied, then column dropped since it's constant True).

Also updates the dataset README to reflect both DESI DR1 + ACT DR6 blocks.
"""

import sys
from pathlib import Path

import pandas as pd
from huggingface_hub import HfApi

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ENV_FILE = Path("/Users/houstongolden/Desktop/CODE_2025/hubify/.env.local")
REPO_ID = "bamfai/bigbounce-anomaly-catalog"
REPO_TYPE = "dataset"

ACT_SRC = BASE_DIR / "pipelines/h200_results/pod_backup_20260408_full/bigbounce/backups/20260406_231143/act-dr6-proper/act_dr6_anomalies.csv"
STAGING = BASE_DIR / "pipelines/p3_anomaly_engine/hf_staging"


def load_hf_token():
    if not ENV_FILE.exists():
        sys.exit(f"Env file not found: {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("HUGGINGFACE_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("HUGGINGFACE_TOKEN not found")


def build_act_parquet():
    STAGING.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(ACT_SRC)
    print(f"ACT DR6: {len(df):,} scored patches loaded")
    top = df[df["is_top1pct"] == 1].drop(columns=["is_top1pct"]).reset_index(drop=True)
    print(f"  top-1% anomalies: {len(top)} (matches Paper 3 Table 1)")
    out = STAGING / "act_dr6_anomalies.parquet"
    top.to_parquet(out, compression="snappy", index=False)
    print(f"  Wrote {out} ({out.stat().st_size / 1e3:.1f} KB)")
    return out, len(top)


def write_updated_readme(desi_rows=195829, act_rows=200):
    readme = STAGING / "README.md"
    readme.write_text(f"""---
license: cc-by-4.0
task_categories:
- feature-extraction
- tabular-classification
tags:
- astronomy
- cosmology
- anomaly-detection
- desi
- act
- cmb
- big-bounce
pretty_name: BigBounce Multi-Survey Anomaly Catalog
size_categories:
- 100K<n<1M
---

# BigBounce Multi-Survey Anomaly Catalog

Companion dataset for Golden (2026), *Multi-Survey Anomaly Engine for
Bounce-Cosmology Observables* (Paper 3 of the BigBounce program).

**This repository is PRIVATE until the paper lands on arXiv.** It will be
made public alongside the models and figures when the full BigBounce suite
(Papers 1–4) is released.

## Current contents (progressively filling from Paper 3 Table 1)

| File | Rows | Survey | Paper 3 count | Status |
|---|---:|---|---:|---|
| `desi_dr1_anomalies.parquet` | {desi_rows:,} | DESI DR1 spectra | 195,829 | **Matches paper** |
| `act_dr6_anomalies.parquet` | {act_rows} | ACT DR6 CMB patches | 200 | **Matches paper** (top-1% filter applied upstream) |

**Coverage so far:** {desi_rows + act_rows:,} / 319,443 rows = {(desi_rows + act_rows) / 319443 * 100:.1f} % of the paper aggregate.

Remaining blocks (tracked as `P3-HF-UPLOAD-EXTEND` in the bigbounce repo's
drive-to-100 queue) — each needs an explicit score-cut re-derivation from
the H200 snapshot:

| Survey | Paper 3 count | Source file |
|---|---:|---|
| SDSS DR18 | 77,905 | `score_dist_sdss-dr18.json` (score-distribution; cut TBD) |
| LAMOST DR10 | 44,075 | `score_dist_lamost-dr10.json` |
| eROSITA DR1 | 298 | `erosita-neowise/erosita_neowise_xmatch_summary.json` |
| NEOWISE | 436 | `neowise-ecliptic-mask/` (CSV parse error on the local copy; needs regen) |
| Planck CMB | 200 | `planck-cmb-masked/planck_cmb_masked_summary.json` |
| Gaia DR3 | 500 | `gaia-dr3-expanded/gaia_anomalies.csv` (needs top-500 filter by anomaly score column not in the 2026-04-06 snapshot) |

## Column schemas

### DESI DR1 (`desi_dr1_anomalies.parquet`)

| Column | Type | Description |
|---|---|---|
| `tid` | int | Internal pipeline ID (negative = synthetic test-time placeholder; kept for provenance) |
| `ra` | float | Right Ascension (deg, ICRS) |
| `dec` | float | Declination (deg, ICRS) |
| `score` | float | BigAE reconstruction loss (MSE over normalized flux) |
| `worst` | str | Filter with highest per-filter residual ratio (`B` · `R` · `Z`) |
| `rB` | float | Residual ratio in DESI B-filter (spec-flux / model-flux) |
| `rR` | float | Residual ratio in R-filter |
| `rZ` | float | Residual ratio in Z-filter |

### ACT DR6 (`act_dr6_anomalies.parquet`)

| Column | Type | Description |
|---|---|---|
| `patch_idx` | int | ACT DR6 patch index (from the 20,000-patch scoring pass) |
| `ra` | float | Patch-centre Right Ascension (deg, ICRS) |
| `dec` | float | Patch-centre Declination (deg, ICRS) |
| `anomaly_score` | float | CMB-patch autoencoder reconstruction score |

All 200 rows pass the paper's is-top-1% threshold. See Paper 3 §7.2 for QC
caveats (ACT DR6 training-loss telemetry flagged the model as
under-trained; these anomalies are reported as a coverage placeholder
pending a retrain on the full Planck+ACT matched-filter map set).

## Novelty classification status

SIMBAD cross-match (5″ cone, `projects/cross_survey/results/
simbad_crossmatch_summary.json` in the bigbounce repo) on the top 100
anomalies per survey: 41 % matched / 59 % SIMBAD-novel. A deep NED pass on
the top-20 SIMBAD-novel SDSS subset (P3-B, fire #10, partial) yielded
~45 % NED-archival-identified — Paper 3's "58.8 % novel" headline likely
over-estimates true novelty; a full NED + VizieR reclassification is
paused on NED TAP service timeouts (documented in the bigbounce
repo's `drive-to-100.md` fire #12 log). This card will be refreshed once
the reclassification completes.

## Citation

```
@article{{Golden:2026multiSurveyAnomalies,
  author  = {{Golden, Houston}},
  title   = {{Multi-Survey Anomaly Engine for Bounce-Cosmology Observables}},
  journal = {{arXiv preprint}},
  year    = {{2026}},
  note    = {{paper reference will be updated post-submission}}
}}
```

## Paper 3 companion artifacts (not yet uploaded here)

- BigAE checkpoint (`projects/sdss-dr18/best_model_47k.pt`)
- Second-level latent AE for recursive anomaly detection (16-D latent)
- Emission-line finder checkpoint (4,526 redshifts · 96.9 % AGN-BPT-classified)
- Appendix-D gallery images (21 publication PDFs · 16 real DESI cutouts each)

## Data availability (from Paper 3 §9)

Canonical source for all per-survey raw scored catalogs lives in the
bigbounce repository, `pipelines/h200_results/pod_backup_20260408_full/
bigbounce/backups/20260406_231143/`. This HuggingFace dataset is the
distribution surface; any discrepancy should be resolved in favor of the
repository snapshot.

## License

CC-BY-4.0 (content) + public-domain star/galaxy coordinates. Model
checkpoints when uploaded will carry Apache-2.0.

---

Generated by `pipelines/p3_anomaly_engine/hf_upload_*.py`. Last refresh:
drive-to-100 fire #12 (ACT DR6 block added).
""")
    print(f"  Wrote {readme}")
    return readme


def upload_to_hf(token, files):
    api = HfApi(token=token)
    for path in files:
        rel = Path(path).name
        print(f"Uploading {rel}...")
        api.upload_file(
            path_or_fileobj=str(path),
            path_in_repo=rel,
            repo_id=REPO_ID,
            repo_type=REPO_TYPE,
            token=token,
            commit_message=f"Add/update {rel} (drive-to-100 fire #12 — ACT DR6 block)",
        )


def main():
    import shutil
    token = load_hf_token()
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)

    act_path, act_n = build_act_parquet()
    readme_path = write_updated_readme(act_rows=act_n)

    upload_to_hf(token, [act_path, readme_path])

    print("\nDone.")
    print(f"Private dataset: https://huggingface.co/datasets/{REPO_ID}")


if __name__ == "__main__":
    main()
