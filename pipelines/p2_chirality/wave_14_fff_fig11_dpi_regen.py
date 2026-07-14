#!/usr/bin/env python3
"""Regenerate P4 Fig. 7 from the full-coverage raw/equivariant catalog fields.

The raw map is defined by ``class_raw_y``.  ``class_raw_x`` is used only when
the y-pass label is missing.  The 8,474,531-row Parquet is read in projected
batches, so no full catalog DataFrame is materialized.  Both displayed panels
use the same support: the intersection of pixels having at least five raw and
five equivariant spirals.

Outputs:
  figs/fig_raw_vs_eq.png
  outputs/canonical_provenance/fig7_raw_vs_eq_manifest.json
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

import healpy as hp
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np
import pyarrow.parquet as pq


ROOT = Path(__file__).resolve().parent
DATASET_REPO_ID = "bamfai/galaxy-chirality-catalog"
DATASET_REPO_TYPE = "dataset"
DATASET_FILENAME = "catalog_production.parquet"
DATASET_REVISION = "a21eb596fd10edb9af9e7a1bcefb04f87327a724"
DATASET_SHA256 = "e8525ba5c98576f6361580e4a0aa7a86929ccc9f79b1423808774cfaaf313563"
DATASET_BYTES = 952_115_239
FIGURE_ARTIFACT = "pipelines/p2_chirality/figs/fig_raw_vs_eq.png"
OUT_PATH = Path(os.environ.get("FIG7_OUT", ROOT / "figs" / "fig_raw_vs_eq.png"))
MANIFEST_PATH = Path(
    os.environ.get(
        "FIG7_MANIFEST",
        ROOT / "outputs" / "canonical_provenance" / "fig7_raw_vs_eq_manifest.json",
    )
)
NSIDE = 64
NPIX = hp.nside2npix(NSIDE)
MIN_SPIRALS = 5
BATCH_SIZE = 262_144
SPIRAL_LABELS = {"CW", "CCW"}


def default_catalog_path() -> str:
    explicit = os.environ.get("CAT_C_PATH")
    if explicit:
        return explicit
    from huggingface_hub import hf_hub_download

    return hf_hub_download(
        DATASET_REPO_ID,
        DATASET_FILENAME,
        repo_type=DATASET_REPO_TYPE,
        revision=DATASET_REVISION,
    )


def sha256_file(path: str | Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        while chunk := fh.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def projected_image(m: np.ndarray) -> np.ndarray:
    """Project a HEALPix map onto a regular equatorial RA/Dec image."""
    ra = np.linspace(-180.0, 180.0, 720)
    dec = np.linspace(-90.0, 90.0, 360)
    ra_grid, dec_grid = np.meshgrid(ra, dec)
    pix = hp.ang2pix(
        NSIDE,
        np.radians(90.0 - dec_grid),
        np.radians(ra_grid % 360.0),
    )
    return m[pix]


def main() -> int:
    started = time.time()
    catalog = Path(default_catalog_path())
    if not catalog.exists():
        raise FileNotFoundError(catalog)
    catalog_sha256 = sha256_file(catalog)
    if catalog_sha256 != DATASET_SHA256:
        raise ValueError(
            "Catalog content hash mismatch: "
            f"expected {DATASET_SHA256}, got {catalog_sha256}"
        )
    if catalog.stat().st_size != DATASET_BYTES:
        raise ValueError(
            "Catalog byte-count mismatch: "
            f"expected {DATASET_BYTES}, got {catalog.stat().st_size}"
        )

    columns = ["ra", "dec", "class_raw_y", "class_raw_x", "class_eq"]
    parquet = pq.ParquetFile(catalog)
    raw_cw = np.zeros(NPIX, dtype=np.int64)
    raw_total = np.zeros(NPIX, dtype=np.int64)
    eq_cw = np.zeros(NPIX, dtype=np.int64)
    eq_total = np.zeros(NPIX, dtype=np.int64)
    n_rows = 0
    n_raw_y_used = 0
    n_raw_x_fallback = 0

    for batch in parquet.iter_batches(columns=columns, batch_size=BATCH_SIZE):
        frame = batch.to_pandas()
        n_rows += len(frame)
        ra = frame["ra"].to_numpy(dtype=float)
        dec = frame["dec"].to_numpy(dtype=float)
        finite = np.isfinite(ra) & np.isfinite(dec)
        pix = np.full(len(frame), -1, dtype=np.int64)
        pix[finite] = hp.ang2pix(
            NSIDE,
            np.radians(90.0 - dec[finite]),
            np.radians(ra[finite] % 360.0),
        )

        raw_y = frame["class_raw_y"]
        raw_x = frame["class_raw_x"]
        y_present = raw_y.notna() & raw_y.astype(str).ne("")
        raw = raw_y.where(y_present, raw_x)
        raw_spiral = finite & raw.isin(SPIRAL_LABELS).to_numpy()
        eq = frame["class_eq"]
        eq_spiral = finite & eq.isin(SPIRAL_LABELS).to_numpy()

        n_raw_y_used += int((raw_spiral & y_present.to_numpy()).sum())
        n_raw_x_fallback += int((raw_spiral & ~y_present.to_numpy()).sum())
        np.add.at(raw_total, pix[raw_spiral], 1)
        np.add.at(raw_cw, pix[raw_spiral], (raw[raw_spiral] == "CW").to_numpy())
        np.add.at(eq_total, pix[eq_spiral], 1)
        np.add.at(eq_cw, pix[eq_spiral], (eq[eq_spiral] == "CW").to_numpy())

    raw_native = raw_total >= MIN_SPIRALS
    eq_native = eq_total >= MIN_SPIRALS
    common = raw_native & eq_native

    raw_fraction = np.full(NPIX, np.nan, dtype=float)
    eq_fraction = np.full(NPIX, np.nan, dtype=float)
    raw_fraction[common] = raw_cw[common] / raw_total[common]
    eq_fraction[common] = eq_cw[common] / eq_total[common]

    image_raw = projected_image(raw_fraction)
    image_eq = projected_image(eq_fraction)
    norm = Normalize(vmin=0.47, vmax=0.53)
    cmap = plt.colormaps["RdBu_r"]
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), constrained_layout=True)
    panels = [
        (axes[0], image_raw, "Raw ViT-Small (Catalog A)"),
        (axes[1], image_eq, "Equivariant TTA (Catalog C)"),
    ]
    image_artist = None
    for ax, image, title in panels:
        image_artist = ax.imshow(
            image,
            extent=[-180, 180, -90, 90],
            origin="lower",
            cmap=cmap,
            norm=norm,
            aspect="auto",
            interpolation="nearest",
        )
        ax.set_xlabel("RA (deg)")
        ax.set_ylabel("Dec (deg)")
        ax.set_title(title, fontweight="bold")
        ax.set_xlim(-180, 180)
        ax.set_ylim(-90, 90)
    assert image_artist is not None
    colorbar = fig.colorbar(image_artist, ax=axes, orientation="vertical", shrink=0.92)
    colorbar.set_label("CW fraction")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    manifest = {
        "figure": "P4 Figure 7: raw versus equivariant CW-fraction sky maps",
        "generator": "pipelines/p2_chirality/wave_14_fff_fig11_dpi_regen.py",
        "catalog": {
            "provider": "huggingface",
            "repo_id": DATASET_REPO_ID,
            "repo_type": DATASET_REPO_TYPE,
            "filename": DATASET_FILENAME,
            "revision": DATASET_REVISION,
            "sha256": catalog_sha256,
            "bytes": DATASET_BYTES,
            "rows": int(n_rows),
        },
        "read_mode": {
            "format": "pyarrow.parquet.ParquetFile.iter_batches",
            "projected_columns": columns,
            "batch_size": BATCH_SIZE,
        },
        "raw_definition": {
            "primary_column": "class_raw_y",
            "fallback_column": "class_raw_x only when class_raw_y is missing",
            "raw_spirals": int(raw_total.sum()),
            "raw_spirals_from_class_raw_y": int(n_raw_y_used),
            "raw_spirals_from_class_raw_x_fallback": int(n_raw_x_fallback),
            "raw_cw": int(raw_cw.sum()),
            "raw_cw_fraction_galaxy_weighted": float(raw_cw.sum() / raw_total.sum()),
        },
        "equivariant_definition": {
            "column": "class_eq",
            "equivariant_spirals": int(eq_total.sum()),
            "equivariant_cw": int(eq_cw.sum()),
            "equivariant_cw_fraction_galaxy_weighted": float(eq_cw.sum() / eq_total.sum()),
        },
        "pixel_support": {
            "nside": NSIDE,
            "minimum_spirals_per_pixel": MIN_SPIRALS,
            "operator": ">=",
            "raw_native_valid_pixels": int(raw_native.sum()),
            "equivariant_native_valid_pixels": int(eq_native.sum()),
            "displayed_common_support_pixels": int(common.sum()),
            "common_support_definition": "raw_total>=5 AND equivariant_total>=5; identical in both panels",
        },
        "render": {
            "coordinate_frame": "equatorial RA/Dec",
            "shared_color_scale": [0.47, 0.53],
            "dpi": 300,
            "output": FIGURE_ARTIFACT,
            "output_sha256": sha256_file(OUT_PATH),
            "output_bytes": OUT_PATH.stat().st_size,
        },
        "wall_seconds": time.time() - started,
    }
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w") as fh:
        json.dump(manifest, fh, indent=2)
        fh.write("\n")

    print(json.dumps(manifest, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
