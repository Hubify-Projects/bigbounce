#!/usr/bin/env python3
"""POST-HOC DIAGNOSTIC (not pre-registered; feeds no pre-registered statistic).

What angular field do the in-domain Smith42/galaxies images actually cover?
main.tex:171 describes the parent as "224x224 px grz cutouts at 0.262 arcsec/
pixel"; the v1.0 files the catalogue was built from are 512x512 px (verified),
so the paper's px figure is the network input, not the cutout. This measures the
pixel scale directly instead of assuming it, by fetching Legacy Survey viewer
cutouts of the SAME galaxies at a grid of pixel scales and taking the scale that
maximises the pixel correlation with the in-domain image.

Recorded deviation: fetches ~N_GAL x len(SCALES) 256 px JPEG cutouts (~10 MB) of
galaxies that are already in this lane's sample. Diagnostic only.

Output: posthoc_pixel_scale.json
"""
import io
import json
import os
import time
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from PIL import Image
from huggingface_hub import HfFileSystem

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parents[1] / "p2_chirality" / "apjs_release_v1.0.244" / "p4_catalog_primary_safe_v1.0.244.parquet"
OUT = HERE / "posthoc_pixel_scale.json"
REPO, REV = "Smith42/galaxies", "bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2"
SCALES = [0.131, 0.20, 0.262, 0.35, 0.45, 0.524]   # arcsec/px for a 512 px cutout
N_GAL = 30
SIDE = 128          # both images reduced to this before correlating


def grab(ra, dec, pixscale, layer="ls-dr8", size=256):
    url = (f"https://www.legacysurvey.org/viewer/jpeg-cutout?ra={ra}&dec={dec}"
           f"&size={size}&pixscale={pixscale}&layer={layer}")
    with urllib.request.urlopen(url, timeout=60) as r:
        return Image.open(io.BytesIO(r.read())).convert("L"), len(r.read() or b"")


def corr(a, b):
    x = np.asarray(a.resize((SIDE, SIDE), Image.BILINEAR), dtype=np.float64).ravel()
    y = np.asarray(b.resize((SIDE, SIDE), Image.BILINEAR), dtype=np.float64).ravel()
    if x.std() == 0 or y.std() == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def main():
    t0 = time.time()
    fs = HfFileSystem(token=os.environ.get("HF_TOKEN"))
    pf = pq.ParquetFile(fs.open(f"datasets/{REPO}@{REV}/data/train-00000-of-00192.parquet", "rb"))
    tbl = pf.read_row_group(0)
    ids = tbl.column("dr8_id").to_pylist()[:N_GAL]
    imgs = {i: Image.open(io.BytesIO(x["bytes"])).convert("L")
            for i, x in zip(ids, tbl.column("image").to_pylist()[:N_GAL])}
    native = Image.open(io.BytesIO(tbl.column("image")[0].as_py()["bytes"]))
    rel = pq.read_table(CATALOG, columns=["object_id", "ra_deg", "dec_deg"]).to_pandas().set_index("object_id")

    per_scale = {str(s): [] for s in SCALES}
    n_ok = 0
    for gid in ids:
        if gid not in rel.index:
            continue
        ra, dec = float(rel.loc[gid, "ra_deg"]), float(rel.loc[gid, "dec_deg"])
        row = {}
        try:
            for s in SCALES:
                # the viewer cutout at scale s covers 256*s arcsec; the in-domain
                # image covers 512*p arcsec, so compare like fields by requesting
                # 256 px at 2*p and correlating whole frames
                im, _ = grab(ra, dec, 2 * s)
                row[s] = corr(imgs[gid], im)
        except Exception:
            continue
        if any(np.isnan(v) for v in row.values()):
            continue
        for s in SCALES:
            per_scale[str(s)].append(row[s])
        n_ok += 1

    med = {k: (float(np.median(v)) if v else float("nan")) for k, v in per_scale.items()}
    best = max((k for k in med if not np.isnan(med[k])), key=lambda k: med[k])
    res = {
        "_label": "POST-HOC DIAGNOSTIC, NOT PRE-REGISTERED. Feeds no pre-registered statistic.",
        "recorded_deviation": f"fetched {n_ok * len(SCALES)} 256 px Legacy Survey viewer cutouts "
                              f"(~10 MB) as a diagnostic; the pre-registration's sample is untouched",
        "question": "what angular field does a Smith42/galaxies v1.0 image cover?",
        "native_image_size_px": list(native.size),
        "native_image_format": native.format,
        "paper_claim_main_tex_171": "224x224 px grz cutouts at 0.262 arcsec/pixel",
        "n_galaxies_compared": n_ok,
        "median_pixel_correlation_by_assumed_pixscale_arcsec_per_px": med,
        "best_fit_pixscale_arcsec_per_px": float(best),
        "implied_field_arcsec": float(best) * native.size[0],
        "viewer_cutout_field_arcsec_rows_13_16": 150 * 0.262,
        "field_ratio_indomain_over_viewer": float(best) * native.size[0] / (150 * 0.262),
        "wall_clock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
