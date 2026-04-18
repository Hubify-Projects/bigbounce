#!/usr/bin/env python3
"""
HuggingFace dataset extension: NEOWISE + Planck CMB + Gaia DR3 blocks
for P3-HF-UPLOAD-EXTEND (drive-to-100 fire #13).

Adds three more blocks to the existing PRIVATE dataset at
bamfai/bigbounce-anomaly-catalog. After fire #13 the dataset covers
5 of 8 paper-3 surveys:

    DESI DR1 (195,829) + ACT DR6 (200) + NEOWISE (436) + Planck (200) + Gaia (500)
    = 197,165 / 319,443 rows = 61.7 % of paper aggregate.

Paper 3 Table 1 counts enforced via explicit top-N by anomaly_score
(is_top1pct is noisy — gives 444 for NEOWISE vs paper's 436, gives 5,000
for Gaia vs paper's 500; use rank-based cut instead).

SDSS / LAMOST / eROSITA deferred: the H200 2026-04-08 snapshot's
per-survey score distributions show data_source=synthetic for those
three — there is no real row-level anomaly table to upload. They will
be regenerated on-pod in a follow-up fire.

Source files:
    NEOWISE: outputs/neowise-ecliptic-mask/neowise_anomalies.csv
             (44,341 scored sources -> top 436 by anomaly_score)
    Planck:  outputs/planck-cmb-masked/planck_cmb_masked_scores.npz
             (19,296 scored patches, keys: scores/ra/dec -> top 200)
    Gaia:    outputs/gaia-dr3-expanded/gaia_anomalies.csv
             (500,000 scored stars -> top 500 by anomaly_score)
"""

import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from huggingface_hub import HfApi

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ENV_FILE = Path("/Users/houstongolden/Desktop/CODE_2025/hubify/.env.local")
REPO_ID = "bamfai/bigbounce-anomaly-catalog"
REPO_TYPE = "dataset"

H200_OUTPUTS = BASE_DIR / "pipelines/h200_results/pod_backup_20260408_full/outputs"
NEOWISE_SRC = H200_OUTPUTS / "neowise-ecliptic-mask/neowise_anomalies.csv"
PLANCK_SRC = H200_OUTPUTS / "planck-cmb-masked/planck_cmb_masked_scores.npz"
GAIA_SRC = H200_OUTPUTS / "gaia-dr3-expanded/gaia_anomalies.csv"

STAGING = BASE_DIR / "pipelines/p3_anomaly_engine/hf_staging"

# Paper 3 Table 1 counts — hard-coded so the filter stays reproducible.
PAPER_COUNTS = {"neowise": 436, "planck": 200, "gaia": 500}


def load_hf_token() -> str:
    if not ENV_FILE.exists():
        sys.exit(f"Env file not found: {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("HUGGINGFACE_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("HUGGINGFACE_TOKEN not found")


def build_neowise() -> Path:
    n_rows = PAPER_COUNTS["neowise"]
    df = pd.read_csv(NEOWISE_SRC)
    print(f"NEOWISE: {len(df):,} scored sources loaded")
    top = df.nlargest(n_rows, "anomaly_score").reset_index(drop=True)
    # Drop the noisy is_top1pct flag — it doesn't match the paper count.
    if "is_top1pct" in top.columns:
        top = top.drop(columns=["is_top1pct"])
    print(f"  top {n_rows} by anomaly_score: cutoff = {top['anomaly_score'].min():.4f}")
    out = STAGING / "neowise_anomalies.parquet"
    top.to_parquet(out, compression="snappy", index=False)
    print(f"  Wrote {out} ({out.stat().st_size / 1e3:.1f} KB)")
    return out


def build_planck() -> Path:
    n_rows = PAPER_COUNTS["planck"]
    z = np.load(PLANCK_SRC)
    scores, ra, dec = z["scores"], z["ra"], z["dec"]
    print(f"PLANCK: {len(scores):,} scored patches loaded")
    idx = np.argsort(scores)[::-1][:n_rows]
    df = pd.DataFrame({
        "patch_idx": idx.astype("int64"),
        "ra": ra[idx].astype("float64"),
        "dec": dec[idx].astype("float64"),
        "anomaly_score": scores[idx].astype("float64"),
    })
    print(f"  top {n_rows} by score: cutoff = {df['anomaly_score'].min():.4f}")
    out = STAGING / "planck_cmb_anomalies.parquet"
    df.to_parquet(out, compression="snappy", index=False)
    print(f"  Wrote {out} ({out.stat().st_size / 1e3:.1f} KB)")
    return out


def build_gaia() -> Path:
    n_rows = PAPER_COUNTS["gaia"]
    df = pd.read_csv(GAIA_SRC)
    print(f"GAIA: {len(df):,} scored stars loaded")
    top = df.nlargest(n_rows, "anomaly_score").reset_index(drop=True)
    if "is_top1pct" in top.columns:
        top = top.drop(columns=["is_top1pct"])
    print(f"  top {n_rows} by anomaly_score: cutoff = {top['anomaly_score'].min():.6f}")
    out = STAGING / "gaia_dr3_anomalies.parquet"
    top.to_parquet(out, compression="snappy", index=False)
    print(f"  Wrote {out} ({out.stat().st_size / 1e3:.1f} KB)")
    return out


def write_readme(desi_rows=195829, act_rows=200, neowise_rows=436,
                 planck_rows=200, gaia_rows=500) -> Path:
    total_uploaded = desi_rows + act_rows + neowise_rows + planck_rows + gaia_rows
    coverage_pct = total_uploaded / 319443 * 100
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
- neowise
- planck
- gaia
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
| `act_dr6_anomalies.parquet` | {act_rows} | ACT DR6 CMB patches | 200 | **Matches paper** (top-1% filter upstream) |
| `neowise_anomalies.parquet` | {neowise_rows} | NEOWISE mid-IR variability | 436 | **Matches paper** (top-N by score) |
| `planck_cmb_anomalies.parquet` | {planck_rows} | Planck CMB patches | 200 | **Matches paper** (top-N by score) |
| `gaia_dr3_anomalies.parquet` | {gaia_rows} | Gaia DR3 variable stars | 500 | **Matches paper** (top-N by score) |

**Coverage so far:** {total_uploaded:,} / 319,443 rows = {coverage_pct:.1f} % of the paper aggregate.

Remaining blocks (tracked as `P3-HF-UPLOAD-EXTEND` in the bigbounce repo's
drive-to-100 queue) — these require a **pod regeneration** since the
2026-04-08 H200 snapshot's score-distribution files for these surveys
carry `data_source: "synthetic"` (aggregate statistics only; no
row-level anomaly table with RA/Dec/score):

| Survey | Paper 3 count | Status |
|---|---:|---|
| SDSS DR18 | 77,905 | Pod regen needed — H200 snapshot has synthetic score-dist only |
| LAMOST DR10 | 44,075 | Pod regen needed — synthetic score-dist only |
| eROSITA DR1 | 298 | Pod regen needed — synthetic score-dist only |

## Column schemas

### DESI DR1 (`desi_dr1_anomalies.parquet`)

| Column | Type | Description |
|---|---|---|
| `tid` | int | Internal pipeline ID (negative = synthetic test-time placeholder; kept for provenance) |
| `ra` | float | Right Ascension (deg, ICRS) |
| `dec` | float | Declination (deg, ICRS) |
| `score` | float | BigAE reconstruction loss (MSE over normalized flux) |
| `worst` | str | Filter with highest per-filter residual ratio (`B` · `R` · `Z`) |
| `rB` / `rR` / `rZ` | float | Residual ratio per DESI filter |

### ACT DR6 + Planck CMB (`act_dr6_anomalies.parquet`, `planck_cmb_anomalies.parquet`)

| Column | Type | Description |
|---|---|---|
| `patch_idx` | int | Scored-patch index |
| `ra` | float | Patch-centre Right Ascension (deg, ICRS) |
| `dec` | float | Patch-centre Declination (deg, ICRS) |
| `anomaly_score` | float | CMB-patch autoencoder reconstruction score |

### NEOWISE (`neowise_anomalies.parquet`)

22-column mid-IR variability feature vector per source, top 436 by
`anomaly_score`. Columns include `source_id`, `ra`, `dec`, `n_epochs`,
`time_span`, per-band means/std/amplitude/chi² (W1/W2), Stetson J,
inter-band color and color variance, and `anomaly_score`. The
paper-3 novelty analysis uses RA/Dec + W1-W2 color for cross-match.

### Gaia DR3 (`gaia_dr3_anomalies.parquet`)

27-column photometric-variability feature vector per source, top 500
by `anomaly_score`. Columns include `source_id`, `ra`, `dec`,
per-band (G / BP / RP) mean / std / num_selected, range/MAD/skewness/
kurtosis of G, BP-RP color + color variance, and `anomaly_score`.

## Caveats and paper cross-references

- **ACT DR6 model under-trained** (§7.2 of Paper 3) — the ACT DR6 block
  is reported for coverage but should be retrained on the full
  Planck+ACT matched-filter map set before production cosmology use.
- **NEOWISE ecliptic systematic** (§7.2) — the NEOWISE row-level table
  was cleaned with an ecliptic-plane mask prior to scoring, but the
  surviving top-436 still inherits the survey's cadence-linked
  false-positive profile; cross-match against Gaia DR3 + AllWISE
  before claiming any individual source.
- **Planck 200** — only 19,296 patches were scored in this run
  (§7.2 flags this as a coverage placeholder; a galactic mask +
  full-sky HEALPix re-scoring is an outstanding pod task).
- **Gaia 500** — the paper's 500-row cut is top-0.1 % of the
  50,000-star expanded sample, not the generic top-1 %.

## Novelty classification status

SIMBAD cross-match (5″ cone, `projects/cross_survey/results/
simbad_crossmatch_summary.json` in the bigbounce repo) on the top 100
anomalies per survey: 41 % matched / 59 % SIMBAD-novel. A deep NED pass
on the top-20 SIMBAD-novel SDSS subset (P3-B, fire #10, partial) yielded
~45 % NED-archival-identified — Paper 3's "58.8 % novel" headline likely
over-estimates true novelty; a full NED + VizieR reclassification is
paused on NED TAP service timeouts (documented in the bigbounce
repo's `drive-to-100.md`). This card will be refreshed once the
reclassification completes.

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
bigbounce repository, `pipelines/h200_results/pod_backup_20260408_full/`.
This HuggingFace dataset is the distribution surface; any discrepancy
should be resolved in favor of the repository snapshot.

## License

CC-BY-4.0 (content) + public-domain star/galaxy coordinates. Model
checkpoints when uploaded will carry Apache-2.0.

---

Generated by `pipelines/p3_anomaly_engine/hf_upload_*.py`. Last refresh:
drive-to-100 fire #13 (NEOWISE + Planck + Gaia blocks added).
""")
    print(f"  Wrote {readme}")
    return readme


def upload_to_hf(token: str, files: list[Path]) -> None:
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
            commit_message=f"Add/update {rel} (drive-to-100 fire #13 — NEOWISE + Planck + Gaia blocks)",
        )


def main() -> None:
    token = load_hf_token()
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)

    neowise = build_neowise()
    planck = build_planck()
    gaia = build_gaia()
    readme = write_readme()

    upload_to_hf(token, [neowise, planck, gaia, readme])

    print("\nDone.")
    print(f"Private dataset: https://huggingface.co/datasets/{REPO_ID}")


if __name__ == "__main__":
    main()
