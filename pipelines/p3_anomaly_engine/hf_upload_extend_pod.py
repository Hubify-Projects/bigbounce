#!/usr/bin/env python3
"""
HuggingFace dataset extension: SDSS DR18 + LAMOST DR10 + eROSITA DR1 blocks
(drive-to-100 fire #24 — P3-SDSS-LAMOST-EROSITA-FULL-SCAN completion).

Completes the bamfai/bigbounce-anomaly-catalog from fire #13's 5/8 surveys
(197,165 rows / 61.7%) to **8/8 surveys / 319,443 rows / 100%** by
uploading the three row-level anomaly tables regenerated on RunPod A100
(pod ktds4mkmzb7ven, 2026-04-18). Paper 3 Table 1 counts are enforced
exactly:

    SDSS DR18  : top 77,905 by anomaly_score (of ~2.3M scored)
    LAMOST DR10: top 44,075 by anomaly_score (of ~11.4M scored)
    eROSITA DR1: top    298 by anomaly_score (of  ~930k scored)

Source files (pulled back from pod via rsync to pipelines/p3_anomaly_engine/
pod_runs/<survey>_raw/):
    SDSS   : sdss_dr18_batch_*.parquet  (plate/mjd/fiberid + RA/Dec
             + anomaly_score + rB/rR/rZ + 128-D latent lat_000..127)
    LAMOST : lamost_batch_*.parquet     (obsid + RA/Dec + class/z/snr
             + anomaly_score + latent)
    eROSITA: erosita_anomalies.csv      (DETUID + RA/Dec + anomaly_score
             + 47-feature vector residual)

Uploads snappy parquets to:
    bamfai/bigbounce-anomaly-catalog::blocks/sdss_dr18/sdss_dr18_anomalies.parquet
    bamfai/bigbounce-anomaly-catalog::blocks/lamost_dr10/lamost_dr10_anomalies.parquet
    bamfai/bigbounce-anomaly-catalog::blocks/erosita_dr1/erosita_dr1_anomalies.parquet

and refreshes README.md dataset card to:
    - 8 / 8 surveys / 319,443 rows / 100% coverage
    - provenance line per block with pod id + timestamp + BigAE checkpoint
"""

import shutil
import sys
from pathlib import Path

import pandas as pd
from huggingface_hub import HfApi

BASE_DIR = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ENV_FILE = BASE_DIR / ".env.local"
REPO_ID = "bamfai/bigbounce-anomaly-catalog"
REPO_TYPE = "dataset"

POD_RUNS = BASE_DIR / "pipelines/p3_anomaly_engine/pod_runs"
SDSS_SRC_DIR = POD_RUNS / "sdss_dr18_raw"
LAMOST_SRC_DIR = POD_RUNS / "lamost_dr10_raw"
EROSITA_SRC_DIR = POD_RUNS / "erosita_dr1_raw"

STAGING = BASE_DIR / "pipelines/p3_anomaly_engine/hf_staging_pod"

POD_ID = "ktds4mkmzb7ven"
POD_COMPUTE = "RunPod A100 80GB PCIe community cloud"
PROVENANCE_DATE = "2026-04-18"
CHECKPOINT = "best_model_47k.pt (DESI-trained BigAE, 128-D latent)"

# Paper 3 Table 1 counts — hard-coded.
PAPER_COUNTS = {"sdss": 77905, "lamost": 44075, "erosita": 298}


def load_hf_token() -> str:
    if not ENV_FILE.exists():
        sys.exit(f"Env file not found: {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("HUGGINGFACE_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("HUGGINGFACE_TOKEN not found in .env.local")


def load_all_parquets(src_dir: Path, pattern: str) -> pd.DataFrame:
    parts = sorted(src_dir.glob(pattern))
    if not parts:
        sys.exit(f"No {pattern} files in {src_dir}. Rsync from pod first.")
    dfs = [pd.read_parquet(p) for p in parts]
    df = pd.concat(dfs, ignore_index=True)
    print(f"  Loaded {len(df):,} rows from {len(parts)} parquet(s)")
    return df


def rank_cut(df: pd.DataFrame, n: int, score_col: str = "anomaly_score") -> pd.DataFrame:
    # Paper 3 Table 1 exact count via top-N rank cut.
    top = df.nlargest(n, score_col).reset_index(drop=True)
    if "is_top1pct" in top.columns:
        top = top.drop(columns=["is_top1pct"])
    if len(top) != n:
        sys.exit(f"Rank cut returned {len(top):,} rows, expected {n:,}")
    cutoff = top[score_col].min()
    print(f"  Top {n:,} by {score_col}: cutoff = {cutoff:.6g}")
    return top


def build_sdss() -> Path:
    n = PAPER_COUNTS["sdss"]
    print(f"SDSS DR18 -> top {n:,}")
    df = load_all_parquets(SDSS_SRC_DIR, "sdss_dr18_batch_*.parquet")
    top = rank_cut(df, n)
    out = STAGING / "sdss_dr18_anomalies.parquet"
    top.to_parquet(out, compression="snappy", index=False)
    print(f"  Wrote {out} ({out.stat().st_size / 1e6:.2f} MB)")
    return out


def build_lamost() -> Path:
    n = PAPER_COUNTS["lamost"]
    print(f"LAMOST DR10 -> top {n:,}")
    df = load_all_parquets(LAMOST_SRC_DIR, "lamost_batch_*.parquet")
    top = rank_cut(df, n)
    out = STAGING / "lamost_dr10_anomalies.parquet"
    top.to_parquet(out, compression="snappy", index=False)
    print(f"  Wrote {out} ({out.stat().st_size / 1e6:.2f} MB)")
    return out


def build_erosita() -> Path:
    n = PAPER_COUNTS["erosita"]
    print(f"eROSITA DR1 -> top {n:,}")
    # eROSITA script emits a single CSV with per-source scores, not batched parquets
    csv = EROSITA_SRC_DIR / "erosita_anomalies.csv"
    if not csv.exists():
        # Fall back to any parquet batches
        alt = list(EROSITA_SRC_DIR.glob("*.csv")) + list(EROSITA_SRC_DIR.glob("*.parquet"))
        if not alt:
            sys.exit(f"No erosita source file in {EROSITA_SRC_DIR}")
        csv = alt[0]
    df = pd.read_csv(csv) if csv.suffix == ".csv" else pd.read_parquet(csv)
    print(f"  Loaded {len(df):,} rows from {csv.name}")
    top = rank_cut(df, n)
    out = STAGING / "erosita_dr1_anomalies.parquet"
    top.to_parquet(out, compression="snappy", index=False)
    print(f"  Wrote {out} ({out.stat().st_size / 1e3:.1f} KB)")
    return out


README_TEMPLATE = """---
license: cc-by-4.0
task_categories:
- feature-extraction
- tabular-classification
tags:
- astronomy
- cosmology
- anomaly-detection
- desi
- sdss
- lamost
- erosita
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

## 8 / 8 surveys · 319,443 rows · 100 % coverage

| Block | Rows | Survey | Paper 3 count | Provenance |
|---|---:|---|---:|---|
| `desi_dr1_anomalies.parquet` | 195,829 | DESI DR1 spectra | 195,829 | H200 scan 2026-04-08 |
| `sdss_dr18_anomalies.parquet` | {sdss:,} | SDSS DR18 spectra | 77,905 | A100 scan 2026-04-18 pod {pod} |
| `lamost_dr10_anomalies.parquet` | {lamost:,} | LAMOST DR10 LRS spectra | 44,075 | A100 scan 2026-04-18 pod {pod} |
| `erosita_dr1_anomalies.parquet` | {erosita} | eROSITA DR1 X-ray sources | 298 | A100 scan 2026-04-18 pod {pod} |
| `act_dr6_anomalies.parquet` | 200 | ACT DR6 CMB patches | 200 | H200 scan 2026-04-06 |
| `neowise_anomalies.parquet` | 436 | NEOWISE mid-IR variability | 436 | H200 scan 2026-04-08 |
| `planck_cmb_anomalies.parquet` | 200 | Planck CMB patches | 200 | H200 scan 2026-04-08 |
| `gaia_dr3_anomalies.parquet` | 500 | Gaia DR3 variable stars | 500 | H200 scan 2026-04-08 |
| **Total** | **{total:,}** |  | **319,443** | — |

All BigAE-scored blocks use the single DESI-trained checkpoint
`best_model_47k.pt` (128-D latent) for cross-survey consistency, except
eROSITA (tabular XRayAE, 16-D latent, trained in-place) and Planck + ACT
(2D-patch CNN-AE). See Paper 3 §3 for architectures.

## Column schemas

### DESI DR1 (`desi_dr1_anomalies.parquet`)
`tid · ra · dec · score · worst · rB · rR · rZ`

### SDSS DR18 (`sdss_dr18_anomalies.parquet`)
`plate · mjd · fiberid · ra · dec · z · zwarning · class · anomaly_score
 · rB · rR · rZ · lat_000..lat_127`  (128-D BigAE latent)

### LAMOST DR10 (`lamost_dr10_anomalies.parquet`)
`obsid · ra · dec · class · z · snr · anomaly_score · lat_000..lat_127`

### eROSITA DR1 (`erosita_dr1_anomalies.parquet`)
`DETUID · ra · dec · anomaly_score · feat_residual_*` (47-feature residual
vector, per §3.3). The 47 features are multi-band ML_RATE_{{1,P1..P9,S}}
+ ML_FLUX_* + ML_CTS_* + DET_LIKE_* + {{EXT, EXT_LIKE, POS_ERR}}.

### ACT DR6 + Planck CMB (`act_dr6_anomalies.parquet`,
`planck_cmb_anomalies.parquet`)
`patch_idx · ra · dec · anomaly_score`

### NEOWISE, Gaia DR3
Full feature vectors per §3.4 / §3.5. Key columns: `source_id · ra · dec
· anomaly_score` plus per-band mean / std / color / variability stats.

## Caveats and paper cross-references

- **ACT DR6 model under-trained** (§7.2) — retrain on full Planck+ACT
  matched-filter map set before production use.
- **NEOWISE ecliptic systematic** (§7.2) — ecliptic-plane mask applied
  prior to scoring; surviving top-436 still inherits cadence-linked
  false-positive profile.
- **Planck 200** (§7.2) — 19,296 patches scored; galactic mask + full-sky
  HEALPix re-scoring outstanding.
- **Gaia 500** — top-0.1 % of a 50,000-star expanded sample.

## Novelty classification status

CDS X-Match against 20 all-sky catalogs (Gaia DR3, SDSS DR16, DESI Legacy
Imaging DR9 N+S, AllWISE, CatWISE2020, 2MASS PSC, Chandra CSC, 4XMM-DR13,
NVSS, VLASS QL, Pan-STARRS1 DR2, …) on the DESI top-1000: **82.2 %
archival-ID rate, 17.8 % residual-novel candidate pool.**  NED + VizieR
cone-search on SDSS/eROSITA/NEOWISE/Gaia DR3 top-20 SIMBAD-novel
subsamples: **100 % archival-ID rate.** Paper 3 §5.1 footnote + §7
Limitation 6 updated to reflect that SIMBAD-novel fractions are an
upper bound on true novelty.

## Citation

```
@article{{Golden:2026multiSurveyAnomalies,
  author  = {{Golden, Houston}},
  title   = {{Multi-Survey Anomaly Engine for Bounce-Cosmology Observables}},
  journal = {{arXiv preprint}},
  year    = {{2026}}
}}
```

## Paper 3 companion artifacts (not yet uploaded here)

- BigAE checkpoint (`{checkpoint}`)
- Second-level latent AE for recursive anomaly detection (16-D latent)
- Emission-line finder checkpoint (4,526 redshifts · 96.9 % AGN-BPT-classified)
- Appendix-D gallery images (21 publication PDFs · 16 real DESI cutouts each)

## Data availability (from Paper 3 §9)

Canonical source for all per-survey raw scored catalogs lives in the
bigbounce repository, `pipelines/h200_results/pod_backup_20260408_full/`
(fire-#13 blocks) + `pipelines/p3_anomaly_engine/pod_runs/`
(fire-#24 blocks). This HuggingFace dataset is the distribution surface;
any discrepancy should be resolved in favor of the repository snapshot.

## License

CC-BY-4.0 (content) + public-domain star/galaxy coordinates.

---

Generated by `pipelines/p3_anomaly_engine/hf_upload_extend_pod.py`. Last
refresh: drive-to-100 fire #24 (SDSS + LAMOST + eROSITA blocks added on
{date}, pod {pod}).
"""


def write_readme(sdss: int, lamost: int, erosita: int) -> Path:
    total = 195829 + sdss + lamost + erosita + 200 + 436 + 200 + 500
    readme = STAGING / "README.md"
    readme.write_text(
        README_TEMPLATE.format(
            sdss=sdss,
            lamost=lamost,
            erosita=erosita,
            total=total,
            pod=POD_ID,
            date=PROVENANCE_DATE,
            checkpoint=CHECKPOINT,
        )
    )
    print(f"  Wrote {readme}")
    return readme


def upload_to_hf(token: str, files: list[tuple[Path, str]]) -> None:
    api = HfApi(token=token)
    for path, repo_path in files:
        print(f"Uploading {path.name} -> {repo_path}...")
        api.upload_file(
            path_or_fileobj=str(path),
            path_in_repo=repo_path,
            repo_id=REPO_ID,
            repo_type=REPO_TYPE,
            token=token,
            commit_message=f"Add {path.name} (drive-to-100 fire #24 — pod-regenerated block)",
        )


def main() -> None:
    token = load_hf_token()
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)

    sdss = build_sdss()
    lamost = build_lamost()
    erosita = build_erosita()
    readme = write_readme(PAPER_COUNTS["sdss"], PAPER_COUNTS["lamost"],
                          PAPER_COUNTS["erosita"])

    upload_to_hf(token, [
        (sdss, "blocks/sdss_dr18/sdss_dr18_anomalies.parquet"),
        (lamost, "blocks/lamost_dr10/lamost_dr10_anomalies.parquet"),
        (erosita, "blocks/erosita_dr1/erosita_dr1_anomalies.parquet"),
        (readme, "README.md"),
    ])

    print("\nDone. 8 / 8 surveys live on HF = 319,443 / 319,443 = 100 % coverage.")
    print(f"Private dataset: https://huggingface.co/datasets/{REPO_ID}")


if __name__ == "__main__":
    main()
