#!/usr/bin/env python3
"""POST-HOC DIAGNOSTIC 2 (not pre-registered) — the field-of-view mechanism.

The P4'/catalogue papers document the parent images correctly: Smith42/galaxies,
224x224 px in grz at 0.262"/pixel from DESI Legacy DR8 (chirality_catalog_paper
sec.data line 1019; p4prime paper line 171) = a 58.7" field fed to a 224 px
network at native resolution. The row 13/16 harness instead fetched the
convenience `image_url` column appended to catalog_production.parquet:
size=150 & layer=ls-dr9 = a 39.3" field upsampled 150 -> 224.

That is a 1.49x angular-scale mismatch plus a resampling difference, and it is
OUTSIDE the range the first zoom sweep could explore (a 150 px cutout cannot be
zoomed OUT). This script fetches matched 224 px cutouts (58.7", both layers) for
the same galaxies and measures the agreement with the released catalogue class.

Recorded deviation: ~600 new cutouts, ~12 MB, diagnostic only; feeds no
pre-registered statistic.

Output: posthoc_fov_test.json
"""
import io
import json
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "row16_pa_parity_transfer"))
from run_pa_transfer_inference import CACHE, SAMPLE, BATCH, REPO_ID, REV, TFM, load_model  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "posthoc_fov_test.json"
N = 300
SEED = 20260921
CW, CCW, NS = 0, 1, 2
VARIANTS = [("size224_ls-dr8", 224, "ls-dr8"), ("size224_ls-dr9", 224, "ls-dr9"),
            ("size150_ls-dr9_harness", 150, "ls-dr9")]


def infer(images, device, enc, head):
    buf = []
    for im in images:
        buf.append(TFM(im))
        buf.append(TFM(im.transpose(Image.FLIP_LEFT_RIGHT)))
    out = []
    for i in range(0, len(buf), BATCH):
        x = torch.stack(buf[i:i + BATCH]).to(device)
        with torch.no_grad():
            out.append(torch.softmax(head(enc(x)), dim=1).float().cpu().numpy())
    p = np.concatenate(out, 0)
    po, pf = p[0::2], p[1::2]
    return np.argmax(np.stack([(po[:, 0] + pf[:, 1]) / 2, (po[:, 1] + pf[:, 0]) / 2,
                               (po[:, 2] + pf[:, 2]) / 2], 1), 1)


def fetch(ra, dec, size, layer):
    url = (f"https://www.legacysurvey.org/viewer/jpeg-cutout?ra={ra}&dec={dec}"
           f"&size={size}&layer={layer}")
    with urllib.request.urlopen(url, timeout=60) as r:
        im = Image.open(io.BytesIO(r.read())).convert("RGB")
    return im if im.size == (size, size) else None


def main():
    t0 = time.time()
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    enc, head = load_model(device)
    sample = pd.read_parquet(SAMPLE)
    cached = [i for i in range(len(sample)) if (CACHE / f"{i}.jpg").exists()]
    ids = [cached[i] for i in np.random.default_rng(SEED).permutation(len(cached))[:N]]
    cat = sample["class_eq"].values[ids]
    catc = np.where(cat == "CW", CW, np.where(cat == "CCW", CCW, NS))

    res = {}
    keep = None
    for tag, size, layer in VARIANTS:
        imgs, ok = [], []
        for k, i in enumerate(ids):
            try:
                im = fetch(float(sample["ra"].values[i]), float(sample["dec"].values[i]),
                           size, layer)
            except Exception:
                im = None
            if im is not None:
                imgs.append(im)
                ok.append(k)
        cls = infer(imgs, device, enc, head)
        ok = np.array(ok)
        c = catc[ok]
        sp = cls != NS
        res[tag] = {"field_arcsec": round(size * 0.262, 1), "n": len(ok),
                    "agreement_with_released_catalogue": float((cls == c).mean()),
                    "fraction_NOT_SPIRAL": float((cls == NS).mean()),
                    "cw_ccw_agreement_among_our_spirals": float((cls[sp] == c[sp]).mean())}
        keep = {**(keep or {}), tag: (ok, cls)}
        print(f"[{time.time()-t0:.0f}s] {tag}: agree="
              f"{res[tag]['agreement_with_released_catalogue']:.4f} "
              f"NS={res[tag]['fraction_NOT_SPIRAL']:.3f}", flush=True)

    out = {"_label": "POST-HOC DIAGNOSTIC, NOT PRE-REGISTERED. Tests the field-of-view "
                     "mechanism behind the step-P control P2c failure.",
           "recorded_deviation": "~600-900 new cutouts (~12 MB) fetched; the pre-registration "
                                 "said no new cutout downloads. Diagnostic only.",
           "documented_parent_images": "Smith42/galaxies, 224x224 px, grz, 0.262 arcsec/px, "
                                       "DESI Legacy DR8 (chirality_catalog_paper.tex:1019; "
                                       "p4prime paper/main.tex:171) = 58.7 arcsec field at "
                                       "native 224 px",
           "harness_images": "image_url column appended by run_eq_fast.py:265-270 = "
                             "jpeg-cutout size=150 layer=ls-dr9 = 39.3 arcsec field upsampled "
                             "150 -> 224",
           "model": f"{REPO_ID}@{REV}", "n_requested": N, "seed": SEED, "variants": res}
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
