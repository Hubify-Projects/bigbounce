"""
publish_catalogs_hf.py
======================
Upload the multi-survey spectral anomaly catalogs to HuggingFace Hub as a
new dataset repository: bamfai/multi-survey-anomaly-catalogs

Usage (after installing deps):
    pip install huggingface_hub
    huggingface-cli login          # or set HF_TOKEN env var
    python3 scripts/publish_catalogs_hf.py

DO NOT run without Houston's explicit approval — this uploads ~2 GB of data
to a public HuggingFace repository.
"""

import os
import sys
import glob
import json
import textwrap
import tempfile
from pathlib import Path

# ── dependency check ──────────────────────────────────────────────────────────
try:
    from huggingface_hub import HfApi, RepoCard, RepoCardData
except ImportError:
    sys.exit(
        "huggingface_hub is not installed.\n"
        "Fix: pip install huggingface_hub"
    )

# ── configuration ─────────────────────────────────────────────────────────────
REPO_ID = "bamfai/multi-survey-anomaly-catalogs"
REPO_TYPE = "dataset"

REPO_ROOT = Path(__file__).resolve().parent.parent
H200_DIR = REPO_ROOT / "pipelines" / "h200_results"

SDSS_GLOB   = str(H200_DIR / "sdss_dr18" / "sdss_batch_*.parquet")
EROSITA_FILE = H200_DIR / "erosita" / "erosita_anomalies.parquet"
SUMMARY_MAIN = H200_DIR / "experiment_summary.json"
EROSITA_SUMMARY = H200_DIR / "erosita" / "erosita_summary.json"

# ── dataset card text ─────────────────────────────────────────────────────────
DATASET_CARD_CONTENT = textwrap.dedent("""\
    ---
    license: cc-by-4.0
    language:
      - en
    tags:
      - astronomy
      - spectroscopy
      - anomaly-detection
      - sdss
      - erosita
      - cosmology
      - bounce-cosmology
    pretty_name: Multi-Survey Spectral Anomaly Catalogs
    size_categories:
      - 10K<n<100K
    ---

    # Multi-Survey Spectral Anomaly Catalogs

    Anomaly catalogs produced by the **BigBounce** research program
    ([bigbounce.hubify.app](https://bigbounce.hubify.app)) as part of the
    multi-survey sweep to identify spectrally anomalous sources that may be
    candidate high-redshift tracers for primordial non-Gaussianity (PNG)
    constraints on bounce cosmology models.

    Anomaly scores are computed using a convolutional variational autoencoder
    trained on each survey's native feature space.  The encoder model is
    published separately at
    [bamfai/desi-spectral-anomaly-detector](https://huggingface.co/bamfai/desi-spectral-anomaly-detector).
    MCMC chains for the associated cosmological parameter fits are published at
    [bamfai/bigbounce-mcmc](https://huggingface.co/datasets/bamfai/bigbounce-mcmc).

    ---

    ## Surveys

    ### 1. SDSS DR18 — Optical Spectroscopy

    | Property | Value |
    |---|---|
    | Path in repo | `sdss_dr18/sdss_batch_XXXX.parquet` (46 files) |
    | Total spectra scanned | 2,285,580 |
    | Anomalies reported (top 1%) | **77,905** |
    | File size | ~1.8 GB total |
    | Anomaly threshold | 99th-percentile reconstruction error |

    **Column descriptions (SDSS)**

    | Column | Type | Description |
    |---|---|---|
    | `plate` | int64 | SDSS plate number |
    | `mjd` | int64 | Modified Julian Date of observation |
    | `fiberid` | int64 | Fiber ID on the plate (together with plate+mjd, uniquely identifies the spectrum in the SDSS CasJobs / SkyServer database) |
    | `anomaly_score` | float64 | Mean-squared reconstruction error from the variational autoencoder; higher = more anomalous |
    | `rB` | float64 | Residual (data – reconstruction) integrated over the blue arm (rest-frame ~3800–5500 Å) |
    | `rR` | float64 | Residual integrated over the red arm (rest-frame ~5500–7000 Å) |
    | `rZ` | float64 | Residual integrated over the z-band arm (rest-frame ~7000–9200 Å) |
    | `lat_000` … `lat_127` | float64 | 128-dimensional latent-space encoding from the encoder network (useful for clustering, nearest-neighbour retrieval, or secondary anomaly scoring) |

    **Cross-matching SDSS spectra**

    To retrieve the original spectra, redshifts, and classifications, join on
    `(plate, mjd, fiberid)` against the SDSS DR18 `SpecObj` view in CasJobs:
    ```sql
    SELECT s.plate, s.mjd, s.fiberid, s.z, s.zWarning, s.class, s.subClass
    FROM SpecObj AS s
    WHERE s.plate = <plate> AND s.mjd = <mjd> AND s.fiberid = <fiberid>
    ```

    ---

    ### 2. eROSITA DR1 — X-ray Point Source Catalog

    | Property | Value |
    |---|---|
    | Path in repo | `erosita/erosita_anomalies.parquet` |
    | Total sources scanned | 930,203 |
    | Anomalies reported (top 1%) | **9,303** |
    | File size | ~108 MB |
    | Anomaly threshold | 99th-percentile reconstruction error |

    **Column descriptions (eROSITA)**

    | Column | Type | Description |
    |---|---|---|
    | `iauname` | string | IAU-format source name from the eROSITA DR1 catalog (e.g. `1eRASS J053856.1-640457`) |
    | `ra` | float64 | Right Ascension (J2000, degrees) |
    | `dec` | float64 | Declination (J2000, degrees) |
    | `anomaly_score` | float64 | Mean-squared reconstruction error; higher = more anomalous |
    | `ml_flux_1` | float64 | Maximum-likelihood X-ray flux in band 1 (0.2–2.3 keV), erg/cm²/s |
    | `ml_rate_1` | float64 | Maximum-likelihood count rate in band 1, counts/s |
    | `det_like_1` | float64 | Detection likelihood in band 1 |
    | `ext` | float64 | Source extent (arcsec); 0 = point-like |
    | `ext_like` | float64 | Extension likelihood |
    | `pos_err` | float64 | 1σ positional uncertainty (arcsec) |
    | `lat_00` … `lat_15` | float64 | 16-dimensional latent-space encoding from the encoder network |

    **Cross-matching eROSITA sources**

    `iauname` is the primary key in the eROSITA DR1 main catalog
    (available from the eROSITA data release portal at
    https://erosita.mpe.mpg.de/dr1/).  You can also cross-match on
    `(ra, dec)` with a ≤ `pos_err` arcsec radius.

    ---

    ## Metadata files

    | File | Description |
    |---|---|
    | `metadata/experiment_summary.json` | Top-50 ranked anomalies from the SDSS recursive autoencoder experiment and multi-resolution ensemble |
    | `metadata/erosita_summary.json` | Top-20 ranked eROSITA anomalies with key catalog properties |

    ---

    ## Methods

    Anomaly detection uses a **variational autoencoder (VAE)** with a
    convolutional encoder trained end-to-end on each survey's native feature
    set (SDSS: continuum-normalised flux vectors binned to 3456 pixels reduced
    to 128-d latent space; eROSITA: 47 catalog features reduced to 16-d latent
    space).  Anomaly scores are the per-object mean-squared reconstruction
    error on a held-out validation split.  The top 1% by score are retained in
    these catalogs.

    The SDSS pipeline processed 46 shards of ~50,000 spectra each on an
    NVIDIA H200 GPU (RunPod). The eROSITA pipeline processed all 930,203 DR1
    point sources in a single pass.

    ---

    ## Citation

    If you use these catalogs, please cite:

    ```bibtex
    @misc{golden2026multisurveyanomaly,
      author       = {Golden, Houston},
      title        = {Multi-Survey Spectral Anomaly Catalogs},
      year         = {2026},
      publisher    = {HuggingFace},
      howpublished = {\\url{https://huggingface.co/datasets/bamfai/multi-survey-anomaly-catalogs}},
      note         = {Part of the BigBounce cosmology research program,
                      \\url{https://bigbounce.hubify.app}}
    }
    ```

    **Author:** Houston Golden (`houston@hubify.com`)
    **Project:** BigBounce — Bounce Cosmology vs ΛCDM + Inflation
    **Website:** https://bigbounce.hubify.app

    ---

    ## License

    [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) — Free to use
    with attribution.
""")


# ── main upload logic ─────────────────────────────────────────────────────────

def main():
    api = HfApi()

    # ── authenticate check ──────────────────────────────────────────────────
    token = os.environ.get("HF_TOKEN")
    try:
        whoami = api.whoami(token=token)
        print(f"Authenticated as: {whoami['name']}")
    except Exception as exc:
        sys.exit(
            f"Not authenticated with HuggingFace: {exc}\n"
            "Run: huggingface-cli login   (or set HF_TOKEN env var)"
        )

    # ── create repo if it doesn't exist ────────────────────────────────────
    print(f"\nCreating/verifying dataset repo: {REPO_ID}")
    api.create_repo(
        repo_id=REPO_ID,
        repo_type=REPO_TYPE,
        exist_ok=True,
        token=token,
        private=False,
    )
    print("  Repo ready.")

    # ── upload dataset card (README.md) ─────────────────────────────────────
    print("\nUploading dataset card (README.md) ...")
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as f:
        f.write(DATASET_CARD_CONTENT)
        card_path = f.name

    try:
        api.upload_file(
            path_or_fileobj=card_path,
            path_in_repo="README.md",
            repo_id=REPO_ID,
            repo_type=REPO_TYPE,
            token=token,
            commit_message="Add dataset card",
        )
        print("  README.md uploaded.")
    finally:
        os.unlink(card_path)

    # ── upload SDSS parquet files ────────────────────────────────────────────
    sdss_files = sorted(glob.glob(SDSS_GLOB))
    if not sdss_files:
        print(f"WARNING: No SDSS files found matching: {SDSS_GLOB}")
    else:
        print(f"\nUploading {len(sdss_files)} SDSS parquet files ...")
        for i, local_path in enumerate(sdss_files, 1):
            fname = Path(local_path).name
            remote_path = f"sdss_dr18/{fname}"
            size_mb = Path(local_path).stat().st_size / 1e6
            print(f"  [{i:02d}/{len(sdss_files)}] {fname}  ({size_mb:.1f} MB) ...", end=" ", flush=True)
            api.upload_file(
                path_or_fileobj=local_path,
                path_in_repo=remote_path,
                repo_id=REPO_ID,
                repo_type=REPO_TYPE,
                token=token,
                commit_message=f"Add SDSS batch file {fname}",
            )
            print("done")
        print("  All SDSS files uploaded.")

    # ── upload eROSITA parquet ───────────────────────────────────────────────
    if not EROSITA_FILE.exists():
        print(f"WARNING: eROSITA file not found: {EROSITA_FILE}")
    else:
        size_mb = EROSITA_FILE.stat().st_size / 1e6
        print(f"\nUploading eROSITA catalog ({size_mb:.1f} MB) ...")
        api.upload_file(
            path_or_fileobj=str(EROSITA_FILE),
            path_in_repo="erosita/erosita_anomalies.parquet",
            repo_id=REPO_ID,
            repo_type=REPO_TYPE,
            token=token,
            commit_message="Add eROSITA DR1 anomaly catalog",
        )
        print("  erosita_anomalies.parquet uploaded.")

    # ── upload summary JSONs ─────────────────────────────────────────────────
    print("\nUploading metadata JSON files ...")
    meta_files = [
        (SUMMARY_MAIN,    "metadata/experiment_summary.json",  "Add SDSS experiment summary"),
        (EROSITA_SUMMARY, "metadata/erosita_summary.json",     "Add eROSITA experiment summary"),
    ]
    for local_path, remote_path, commit_msg in meta_files:
        if not local_path.exists():
            print(f"  WARNING: {local_path} not found — skipping.")
            continue
        print(f"  {remote_path} ...", end=" ", flush=True)
        api.upload_file(
            path_or_fileobj=str(local_path),
            path_in_repo=remote_path,
            repo_id=REPO_ID,
            repo_type=REPO_TYPE,
            token=token,
            commit_message=commit_msg,
        )
        print("done")

    # ── done ─────────────────────────────────────────────────────────────────
    print(f"\nAll uploads complete.")
    print(f"Dataset live at: https://huggingface.co/datasets/{REPO_ID}")


if __name__ == "__main__":
    main()
