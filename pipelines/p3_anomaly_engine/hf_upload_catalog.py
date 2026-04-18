#!/usr/bin/env python3
"""
HuggingFace dataset upload for the BigBounce multi-survey anomaly catalog
(P3-HF-UPLOAD, drive-to-100 fire #11).

Publishes as **PRIVATE** (per Houston, 2026-04-17):
    "publish as 'private' not public. We will make it public along with
    rest of models and catalogs on HF when we officially publish everything
    on arXiv."

Repo: bamfai/bigbounce-anomaly-catalog (private)

Scope of this upload (fire #11):
    - DESI DR1 anomaly catalog — 195,829 rows (61 % of the paper's 319,443
      aggregate). This is the single largest per-survey block and is already
      available as a clean aligned JSON artifact at
      pipelines/h200_results/pod_backup_20260408_full/dr1_all_anomalies.json

Remaining 7 surveys are filed as `P3-HF-UPLOAD-EXTEND` (P2) — they require
a de-duplicated aggregation pass across the H200 snapshot since the paper's
per-survey counts (SDSS 77,905 · LAMOST 44,075 · eROSITA 298 · NEOWISE 436
· Planck 200 · ACT 200 · Gaia 500) each need an explicit score-cut re-
derivation from the raw score-distribution files.

Artifacts uploaded this fire:
    - desi_dr1_anomalies.parquet (~20-25 MB, 195,829 rows)
    - README.md (dataset card with survey table, novelty framing, citation)

Env:
    HUGGINGFACE_TOKEN must be set (read from hubify/.env.local).
"""

import json
import os
import shutil
import sys
from pathlib import Path

import pandas as pd
from huggingface_hub import HfApi, create_repo

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ENV_FILE = Path("/Users/houstongolden/Desktop/CODE_2025/hubify/.env.local")

REPO_ID = "bamfai/bigbounce-anomaly-catalog"
REPO_TYPE = "dataset"
PRIVATE = True

DESI_SRC = BASE_DIR / "pipelines/h200_results/pod_backup_20260408_full/dr1_all_anomalies.json"
STAGING = BASE_DIR / "pipelines/p3_anomaly_engine/hf_staging"


def load_hf_token():
    """Read HUGGINGFACE_TOKEN from hubify/.env.local."""
    if not ENV_FILE.exists():
        sys.exit(f"Env file not found: {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("HUGGINGFACE_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("HUGGINGFACE_TOKEN not in env file")


def build_desi_parquet():
    """Convert DESI DR1 JSON to a compact parquet in the staging dir."""
    STAGING.mkdir(parents=True, exist_ok=True)
    print(f"Loading DESI DR1 from {DESI_SRC.name}")
    data = json.loads(DESI_SRC.read_text())
    df = pd.DataFrame(data)
    print(f"  {len(df):,} rows × {len(df.columns)} cols: {list(df.columns)}")
    out = STAGING / "desi_dr1_anomalies.parquet"
    df.to_parquet(out, compression="snappy", index=False)
    print(f"  Wrote {out} ({out.stat().st_size / 1e6:.1f} MB)")
    return out, len(df)


def write_readme(desi_rows):
    """Emit README.md dataset card in staging."""
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

## Current contents (fire #11 partial upload)

| File | Rows | Survey | Notes |
|---|---:|---|---|
| `desi_dr1_anomalies.parquet` | {desi_rows:,} | DESI DR1 (BGS + LRG + ELG + QSO spectra) | Single BigAE autoencoder, top 0.87 % by reconstruction score |

The paper's aggregate catalog spans 8 surveys (319,443 anomalies total).
Remaining 7 surveys (SDSS DR18 · LAMOST DR10 · eROSITA DR1 · NEOWISE ·
Planck CMB · ACT DR6 · Gaia DR3) are being staged for upload in a follow-up
(`P3-HF-UPLOAD-EXTEND`) — each needs an explicit score-cut re-derivation
from the H200 snapshot's per-survey score distributions.

## DESI DR1 column schema

| Column | Type | Description |
|---|---|---|
| `tid` | int | Internal pipeline ID (negative = synthetic test-time placeholder; kept for provenance) |
| `ra` | float | Right Ascension (deg, ICRS) |
| `dec` | float | Declination (deg, ICRS) |
| `score` | float | BigAE reconstruction loss (MSE over normalized flux) |
| `worst` | str | Filter with the highest per-filter residual ratio (`B` · `R` · `Z`) |
| `rB` | float | Residual ratio in DESI B-filter (spec-flux / model-flux) |
| `rR` | float | Residual ratio in R-filter |
| `rZ` | float | Residual ratio in Z-filter |

## Novelty classification

SIMBAD cross-match (5″ cone, `projects/cross_survey/results/
simbad_crossmatch_summary.json` in the bigbounce repo) on the top 100
DESI anomalies: 100 / 100 SIMBAD-novel. A deep NED pass on the top-20
SIMBAD-novel SDSS subset (P3-B, fire #10, partial) yielded ~45 %
NED-archival-identified — Paper 3's "58.8 % novel" headline likely
over-estimates true novelty; a full NED + VizieR reclassification is in
progress and will refresh this dataset card on completion.

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

Generated by `pipelines/p3_anomaly_engine/hf_upload_catalog.py`, drive-to-100 fire #11.
""")
    print(f"  Wrote {readme}")
    return readme


def upload_to_hf(token, files):
    """Create private repo if missing, upload files."""
    api = HfApi(token=token)

    # Create repo (no-op if exists)
    try:
        create_repo(
            repo_id=REPO_ID,
            repo_type=REPO_TYPE,
            private=PRIVATE,
            exist_ok=True,
            token=token,
        )
        print(f"Repo ready: {REPO_ID} (private={PRIVATE})")
    except Exception as err:
        sys.exit(f"Repo create failed: {err}")

    for path in files:
        rel = Path(path).name
        print(f"Uploading {rel} ...")
        api.upload_file(
            path_or_fileobj=str(path),
            path_in_repo=rel,
            repo_id=REPO_ID,
            repo_type=REPO_TYPE,
            token=token,
            commit_message=f"Add {rel} (drive-to-100 fire #11)",
        )
        print(f"  done.")


def main():
    token = load_hf_token()
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)

    parquet_path, n_rows = build_desi_parquet()
    readme_path = write_readme(n_rows)

    upload_to_hf(token, [parquet_path, readme_path])

    print("\nDone.")
    print(f"Private dataset: https://huggingface.co/datasets/{REPO_ID}")


if __name__ == "__main__":
    main()
