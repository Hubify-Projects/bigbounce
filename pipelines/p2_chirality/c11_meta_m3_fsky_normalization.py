#!/usr/bin/env python3
"""R23conf closure P4-META-M3: f_eff,sky normalization conventions.

For each weight map used in the paper (binary, Wp=N_all, Wp=N_spiral on the
N_all>=1 footprint; unapodized and C2 2-deg apodized), computes:
  (a) the paper's convention  f_eff = <W>^2/<W^2>  (means over ALL pixels),
      which equals (Sum w)^2 / (Npix_tot * Sum w^2) and is invariant under
      W -> c*W (so unnormalized integer counts and [0,1]-normalized weights
      give identical values);
  (b) the mask-restricted weight-uniformity factor
      (Sum_in w)^2 / (N_in * Sum_in w^2), which is NOT a sky fraction but the
      in-mask effective-pixel fraction; (a) = (b) x (N_in/Npix_tot).
Cross-checks (a) against the published c3_wp_invariance_fsky.json values.

Output: outputs/canonical_provenance/c11_meta_m3_fsky_normalization.json
"""
import json
import time

import healpy as hp
import numpy as np
import pandas as pd
import pymaster as nmt
from huggingface_hub import hf_hub_download

NSIDE = 64
OUT = "outputs/canonical_provenance/c11_meta_m3_fsky_normalization.json"
t0 = time.time()


def log(m):
    print(f"[{time.time()-t0:7.1f}s] {m}", flush=True)


def conventions(w, support):
    npix = len(w)
    n_in = int(support.sum())
    s1, s2 = float(w.sum()), float((w ** 2).sum())
    full_sky = s1 ** 2 / (npix * s2)          # = <W>^2/<W^2>, paper convention
    mask_restricted = s1 ** 2 / (n_in * s2)   # in-mask uniformity factor
    return {"fsky_eff_fullsky_mean": full_sky,
            "mask_restricted_uniformity": mask_restricted,
            "n_in_support": n_in,
            "identity_check_fullsky_eq_restricted_x_pixfrac":
                abs(full_sky - mask_restricted * n_in / npix) < 1e-12}


def main():
    path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                           "catalog_production.parquet",
                           repo_type="dataset", local_files_only=True)
    df = pd.read_parquet(path, columns=["ra", "dec", "class_eq"])
    npix = hp.nside2npix(NSIDE)
    theta = np.radians(90.0 - df["dec"].values)
    phi = np.radians(df["ra"].values % 360)
    pix = hp.ang2pix(NSIDE, theta, phi)
    n_all = np.bincount(pix, minlength=npix).astype(float)
    sp = df["class_eq"].isin(["CW", "CCW"]).values
    n_spiral = np.bincount(pix[sp], minlength=npix).astype(float)
    log(f"galaxies {len(df):,}; spirals {int(sp.sum()):,}")

    footprint = (n_all >= 1).astype(float)
    apod = nmt.mask_apodization(footprint, 2.0, "C2")
    log("apodization done")

    weight_maps = {
        "binary_unapodized": footprint,
        "binary_apodized": apod,
        "Wp_Nall_unapodized": n_all * footprint,
        "Wp_Nall_apodized": n_all * apod,
        "Wp_Nspiral_unapodized": n_spiral * footprint,
        "Wp_Nspiral_apodized": n_spiral * apod,
    }
    support = footprint > 0
    results = {k: conventions(v, support) for k, v in weight_maps.items()}

    # scale-invariance demonstration: W -> W/max(W) changes nothing
    wn = weight_maps["Wp_Nall_apodized"]
    scaled = conventions(wn / wn.max(), support)
    results["Wp_Nall_apodized_rescaled_to_unit_max"] = scaled

    # cross-check against published c3 artifact
    c3 = json.load(open("outputs/canonical_provenance/c3_wp_invariance_fsky.json"))
    pub = c3["fsky_numbers"]
    xchk = {
        "fsky_eff_Wp_Nall_apodized": [pub["fsky_eff_Wp_Nall_apodized"],
                                       results["Wp_Nall_apodized"]["fsky_eff_fullsky_mean"]],
        "fsky_eff_Wp_Nspiral_apodized": [pub["fsky_eff_Wp_Nspiral_apodized"],
                                          results["Wp_Nspiral_apodized"]["fsky_eff_fullsky_mean"]],
        "fsky_eff_Wp_Nall_unapodized": [pub["fsky_eff_Wp_Nall_unapodized"],
                                         results["Wp_Nall_unapodized"]["fsky_eff_fullsky_mean"]],
        "fsky_eff_binary_apodized": [pub["fsky_eff_binary_apodized"],
                                      results["binary_apodized"]["fsky_eff_fullsky_mean"]],
    }
    for k, (a, b) in xchk.items():
        log(f"cross-check {k}: published={a:.6f} recomputed={b:.6f} "
            f"({'OK' if abs(a-b) < 5e-3 else 'MISMATCH'})")

    out = {
        "job": "C11-P4-R23conf-META-M3-fsky-normalization",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "closes": ["P4-META-M3"],
        "config": {"nside": NSIDE, "apodization": "C2 2.0 deg",
                    "footprint": "N_all >= 1", "catalog_parquet": path},
        "definitions": {
            "fsky_eff_fullsky_mean": "<W>^2/<W^2>, means over all Npix pixels == (Sum w)^2/(Npix*Sum w^2); scale-invariant under W->cW",
            "mask_restricted_uniformity": "(Sum_in w)^2/(N_in*Sum_in w^2); in-mask weight-uniformity factor, NOT a sky fraction",
        },
        "results": results,
        "cross_check_vs_c3": xchk,
    }
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    log(f"saved {OUT}")


if __name__ == "__main__":
    main()
