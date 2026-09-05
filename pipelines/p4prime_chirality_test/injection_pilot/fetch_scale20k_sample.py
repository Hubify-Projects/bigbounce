#!/usr/bin/env python3
"""Row 16 step (ii): sample N=20,000 galaxies (10,000 CW / 10,000 CCW,
sky-uniform via NSIDE=64 healpix) from the production catalog for the
20k-scale pixel-level parity injection test. Same method as the N=5000
Row 13 scale sample (fetch_scale_sample.py), NSIDE bumped 32->64 (49,152
bins) to reach 10,000/class without exhausting unique sky bins."""
import json
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download

OUT_DIR = Path(__file__).parent
N_PER_CLASS = 10000
SEED = 44  # distinct draw from N=500 pilot (seed=42) and N=5000 scale (seed=43)


def main():
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset"
    )
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    df = df.loc[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)

    nside = 64
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
        print(f"{cls}: reached {len(chosen)}/{n_target} from {i} unique bins scanned")

    sample = pd.concat(parts).reset_index(drop=True)
    sample["image_url"] = (
        "https://www.legacysurvey.org/viewer/jpeg-cutout?ra="
        + sample["ra"].astype(str) + "&dec=" + sample["dec"].astype(str)
        + "&size=150&layer=ls-dr9"
    )
    out_path = OUT_DIR / "scale20k_sample.parquet"
    sample.to_parquet(out_path)
    manifest = {
        "n_total": len(sample),
        "n_cw": int((sample["class_eq"] == "CW").sum()),
        "n_ccw": int((sample["class_eq"] == "CCW").sum()),
        "sampling": "sky-uniform via NSIDE=64 healpix bins, one galaxy per bin per class, seed=44",
        "source_catalog": "bamfai/galaxy-chirality-catalog:catalog_production.parquet",
        "supersedes": "N=5000 Row13 scale sample (scale_sample.parquet, seed=43); this is Row16 step (ii)",
    }
    (OUT_DIR / "scale20k_sample_manifest.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
