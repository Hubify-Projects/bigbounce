#!/usr/bin/env python3
"""Row 13 pilot: sample N galaxies (balanced CW/CCW, sky-uniform via healpix)
from the production catalog for the image-level injection pilot."""
import json
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download

OUT_DIR = Path(__file__).parent
N_PER_CLASS = 250  # reduced from declared 5k/class — session time budget
SEED = 42


def main():
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset"
    )
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    df = df.loc[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)

    # sky-uniform stratified sample via NSIDE=16 healpix bins
    nside = 16
    theta = np.radians(90.0 - df["dec"].values)
    phi = np.radians(df["ra"].values)
    df["hpix"] = hp.ang2pix(nside, theta, phi)

    rng = np.random.default_rng(SEED)
    parts = []
    for cls, n_target in [("CW", N_PER_CLASS), ("CCW", N_PER_CLASS)]:
        sub = df.loc[df["class_eq"] == cls]
        bins = sub["hpix"].unique()
        rng.shuffle(bins)
        picked = []
        i = 0
        while sum(len(p) for p in picked) < n_target and i < len(bins):
            b = bins[i]
            rows = sub.loc[sub["hpix"] == b]
            picked.append(rows.sample(n=1, random_state=SEED + i))
            i += 1
        chosen = pd.concat(picked).head(n_target)
        parts.append(chosen)

    sample = pd.concat(parts).reset_index(drop=True)
    sample["image_url"] = (
        "https://www.legacysurvey.org/viewer/jpeg-cutout?ra="
        + sample["ra"].astype(str) + "&dec=" + sample["dec"].astype(str)
        + "&size=150&layer=ls-dr9"
    )
    out_path = OUT_DIR / "pilot_sample.parquet"
    sample.to_parquet(out_path)
    manifest = {
        "n_total": len(sample),
        "n_cw": int((sample["class_eq"] == "CW").sum()),
        "n_ccw": int((sample["class_eq"] == "CCW").sum()),
        "sampling": "sky-uniform via NSIDE=16 healpix bins, one galaxy per bin per class, seed=42",
        "source_catalog": "bamfai/galaxy-chirality-catalog:catalog_production.parquet",
    }
    (OUT_DIR / "pilot_sample_manifest.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
