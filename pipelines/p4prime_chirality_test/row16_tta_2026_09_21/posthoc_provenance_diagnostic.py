#!/usr/bin/env python3
"""POST-HOC DIAGNOSTIC (not pre-registered) — why the pre-registered step-P
control P2c failed: the released P4' catalogue's labels are NOT reproducible
from the committed checkpoint applied to the cutouts rows 13/16 cached.

Recorded deviation (see the results document): this script fetches N_LAYER_TEST
= 300 NEW 150 px cutouts from the ls-dr8 layer (~3 MB) purely as a diagnostic.
It feeds no pre-registered statistic.

Two measurements:
  (a) zoom sweep  - agreement with the released catalogue class as a function of
      central crop (a proxy for angular scale), on the cached ls-dr9 cutouts;
  (b) layer test  - the same agreement on ls-dr8 vs ls-dr9 cutouts of the same
      galaxies, because the catalogue's inference ran on the HF dataset
      `Smith42/galaxies` (DR8-era, keyed by dr8_id) while rows 13/16 fetched the
      `image_url` column that run_eq_fast.py appended for display
      (`...jpeg-cutout?...&size=150&layer=ls-dr9`).

Output: posthoc_provenance_diagnostic.json
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
from run_pa_transfer_inference import (  # noqa: E402
    CACHE, SAMPLE, BATCH, REPO_ID, REV, TFM, load_model,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "posthoc_provenance_diagnostic.json"
CROPS = [150, 128, 106, 90, 75, 60]
N_ZOOM = 3000
N_LAYER_TEST = 300
SEED = 20260921
CW, CCW, NS = 0, 1, 2


def eq_from_pair(p_o, p_f):
    return np.stack([(p_o[:, 0] + p_f[:, 1]) / 2,
                     (p_o[:, 1] + p_f[:, 0]) / 2,
                     (p_o[:, 2] + p_f[:, 2]) / 2], axis=1)


def infer(images, device, enc, head, crop=None):
    """Released preprocessing (optionally a central crop first), original + flip."""
    po, pf = [], []
    buf = []
    for img in images:
        im = img
        if crop is not None and crop != im.size[0]:
            w, h = im.size
            l, t = (w - crop) // 2, (h - crop) // 2
            im = im.crop((l, t, l + crop, t + crop))
        buf.append(TFM(im))
        buf.append(TFM(im.transpose(Image.FLIP_LEFT_RIGHT)))
    out = []
    for i in range(0, len(buf), BATCH):
        x = torch.stack(buf[i:i + BATCH]).to(device)
        with torch.no_grad():
            out.append(torch.softmax(head(enc(x)), dim=1).float().cpu().numpy())
    p = np.concatenate(out, 0)
    return eq_from_pair(p[0::2], p[1::2])


def main():
    t0 = time.time()
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    enc, head = load_model(device)
    sample = pd.read_parquet(SAMPLE)
    cached = [i for i in range(len(sample)) if (CACHE / f"{i}.jpg").exists()]
    rng = np.random.default_rng(SEED)
    pick = rng.permutation(len(cached))[:N_ZOOM]
    ids = [cached[i] for i in pick]
    cat = sample["class_eq"].values[ids]
    catc = np.where(cat == "CW", CW, np.where(cat == "CCW", CCW, NS))
    imgs = [Image.open(CACHE / f"{i}.jpg").convert("RGB") for i in ids]

    zoom = {}
    for c in CROPS:
        eq = infer(imgs, device, enc, head, crop=c)
        cls = np.argmax(eq, 1)
        zoom[str(c)] = {
            "arcsec_field": round(c * 0.262, 2),
            "agreement_with_released_catalogue_class": float((cls == catc).mean()),
            "fraction_labelled_NOT_SPIRAL": float((cls == NS).mean()),
            "cw_ccw_agreement_among_our_spirals": float(
                (cls[(cls != NS)] == catc[(cls != NS)]).mean()),
        }
        print(f"[{time.time()-t0:.0f}s] crop {c}: agree="
              f"{zoom[str(c)]['agreement_with_released_catalogue_class']:.4f}", flush=True)

    # ---- (b) layer test: ls-dr8 vs ls-dr9 on the same galaxies ----
    ids8 = ids[:N_LAYER_TEST]
    cat8 = catc[:N_LAYER_TEST]
    imgs8, ok = [], []
    for k, i in enumerate(ids8):
        ra, dec = float(sample["ra"].values[i]), float(sample["dec"].values[i])
        url = (f"https://www.legacysurvey.org/viewer/jpeg-cutout?ra={ra}&dec={dec}"
               f"&size=150&layer=ls-dr8")
        try:
            with urllib.request.urlopen(url, timeout=45) as r:
                b = r.read()
            im = Image.open(io.BytesIO(b)).convert("RGB")
            if im.size != (150, 150):
                continue
            imgs8.append(im)
            ok.append(k)
        except Exception:
            continue
    layer = {"n_requested": N_LAYER_TEST, "n_fetched": len(imgs8),
             "bytes_note": "150 px JPEG cutouts, ~10 kB each; ~3 MB total, diagnostic only"}
    if imgs8:
        eq8 = infer(imgs8, device, enc, head)
        cls8 = np.argmax(eq8, 1)
        eq9 = infer([imgs[k] for k in ok], device, enc, head)
        cls9 = np.argmax(eq9, 1)
        c8 = cat8[np.array(ok)]
        layer.update({
            "agreement_ls_dr8_with_catalogue": float((cls8 == c8).mean()),
            "agreement_ls_dr9_with_catalogue_same_galaxies": float((cls9 == c8).mean()),
            "agreement_ls_dr8_vs_ls_dr9": float((cls8 == cls9).mean()),
            "fraction_NOT_SPIRAL_ls_dr8": float((cls8 == NS).mean()),
            "fraction_NOT_SPIRAL_ls_dr9": float((cls9 == NS).mean()),
        })

    out = {
        "_label": "POST-HOC DIAGNOSTIC, NOT PRE-REGISTERED. Explains the failure of the "
                  "pre-registered step-P control P2c. Feeds no pre-registered statistic.",
        "recorded_deviation": f"fetched {layer['n_fetched']} new ls-dr8 cutouts (~3 MB) "
                              "for the layer test; the pre-registration said no new cutout "
                              "downloads, so this is recorded as a deviation",
        "finding": "the released catalogue's inference ran on images from the HF dataset "
                   "Smith42/galaxies (pipelines/p2_chirality/run_eq_fast.py:37, keyed by "
                   "dr8_id); the `image_url` column (jpeg-cutout, size=150, layer=ls-dr9) "
                   "was APPENDED to catalog_production.parquet afterwards "
                   "(run_eq_fast.py:265-270) and is what the row 13/16 fetch scripts used. "
                   "They are not the same images.",
        "model": f"{REPO_ID}@{REV}",
        "n_zoom_sample": N_ZOOM, "seed": SEED,
        "zoom_sweep_central_crop": zoom,
        "layer_test": layer,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
