#!/usr/bin/env python3
"""R23conf closure P4-META-M4: quantitative per-slab monopole-uniformity stats.

(1) Splits the full Catalog C spiral sample into 7 equatorial slabs two ways:
    (a) 7 equal-spiral-count declination slabs (equal-weight partition),
    (b) 7 equal-spiral-count RA slabs,
    and reports per-slab f_CW +/- binomial sigma and N_spiral.
(2) Direct demonstration that a constant monopole does not bias the
    uniform-weight real-space dipole estimator on the canonical mask:
    per-pixel binomial draws at p = p_CW_global (monopole present) vs
    p = 0.5 (no monopole); the dipole-amplitude null distributions are
    compared. The constant template is in the span of the fit regressors
    (monopole + dipole), so the offset is absorbed by the monopole
    coefficient; this test verifies that empirically.

Output: outputs/canonical_provenance/c11_meta_m4_slab_stats.json
"""
import json
import time

import healpy as hp
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download

NSIDE = 64
MIN_SPIRALS = 10
N_MC = 500
SEED = 42
OUT = "outputs/canonical_provenance/c11_meta_m4_slab_stats.json"

t0 = time.time()


def log(m):
    print(f"[{time.time()-t0:7.1f}s] {m}", flush=True)


def slab_stats(values_is_cw, key, n_slabs=7):
    """Equal-count slabs along sorted `key`; returns per-slab stats."""
    order = np.argsort(key)
    is_cw_sorted = values_is_cw[order]
    key_sorted = key[order]
    edges_idx = np.linspace(0, len(key), n_slabs + 1).astype(int)
    rows = []
    for i in range(n_slabs):
        sl = slice(edges_idx[i], edges_idx[i + 1])
        n = edges_idx[i + 1] - edges_idx[i]
        ncw = int(is_cw_sorted[sl].sum())
        f = ncw / n
        sig = float(np.sqrt(f * (1 - f) / n))
        rows.append({
            "slab": i + 1,
            "range": [float(key_sorted[sl][0]), float(key_sorted[sl][-1])],
            "n_spiral": int(n),
            "n_cw": ncw,
            "f_cw": float(f),
            "sigma_binomial": sig,
            "dev_from_half_pct": float((f - 0.5) * 100),
            "z_vs_global": float((f - values_is_cw.mean()) / sig),
        })
    return rows


def main():
    path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                           "catalog_production.parquet",
                           repo_type="dataset", local_files_only=True)
    df = pd.read_parquet(path, columns=["ra", "dec", "class_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    is_cw = (spirals["class_eq"].values == "CW").astype(float)
    f_global = is_cw.mean()
    log(f"spirals: {len(spirals):,}, global f_CW = {f_global:.6f}")

    dec_slabs = slab_stats(is_cw, spirals["dec"].values)
    ra_slabs = slab_stats(is_cw, spirals["ra"].values % 360)

    # ---- monopole-no-dipole-bias demonstration ----
    npix = hp.nside2npix(NSIDE)
    theta = np.radians(90.0 - spirals["dec"].values)
    phi = np.radians(spirals["ra"].values % 360)
    pix = hp.ang2pix(NSIDE, theta, phi)
    n_sp_map = np.bincount(pix, minlength=npix)
    mask = n_sp_map >= MIN_SPIRALS
    mask_idx = np.where(mask)[0]
    n_sp_in = n_sp_map[mask]
    log(f"canonical mask n_pix={mask.sum()}, f_sky={mask.sum()/npix:.5f}")

    rng = np.random.default_rng(SEED)

    def amp_of(p_cw):
        ncw = rng.binomial(n_sp_in, p_cw)
        a = (2.0 * ncw - n_sp_in) / n_sp_in
        m = np.full(npix, hp.UNSEEN)
        m[mask_idx] = a
        _, dip = hp.fit_dipole(m, gal_cut=0)
        return float(np.sqrt(np.sum(dip ** 2)))

    amps_mono = np.array([amp_of(f_global) for _ in range(N_MC)])
    amps_half = np.array([amp_of(0.5) for _ in range(N_MC)])
    log(f"monopole-present null amp: {amps_mono.mean():.6e} +/- {amps_mono.std(ddof=1):.6e}")
    log(f"no-monopole       null amp: {amps_half.mean():.6e} +/- {amps_half.std(ddof=1):.6e}")
    shift_sigma = (amps_mono.mean() - amps_half.mean()) / np.sqrt(
        amps_mono.var(ddof=1) / N_MC + amps_half.var(ddof=1) / N_MC)

    out = {
        "job": "C11-P4-R23conf-META-M4-slab-stats",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "closes": ["P4-META-M4"],
        "config": {"n_slabs": 7, "partition": "equal-spiral-count slabs",
                    "nside": NSIDE, "min_spirals_per_pix": MIN_SPIRALS,
                    "n_mc": N_MC, "seed": SEED, "catalog_parquet": path},
        "global_f_cw": float(f_global),
        "dec_slabs_equal_count": dec_slabs,
        "ra_slabs_equal_count": ra_slabs,
        "max_abs_dev_from_half_pct_dec": float(max(abs(r["dev_from_half_pct"]) for r in dec_slabs)),
        "max_abs_dev_from_half_pct_ra": float(max(abs(r["dev_from_half_pct"]) for r in ra_slabs)),
        "monopole_dipole_bias_test": {
            "description": "binomial per-pixel draws on the canonical mask at p=f_CW_global (monopole present) vs p=0.5 (none); uniform-weight hp.fit_dipole amplitude distributions",
            "amp_mean_monopole_present": float(amps_mono.mean()),
            "amp_std_monopole_present": float(amps_mono.std(ddof=1)),
            "amp_mean_no_monopole": float(amps_half.mean()),
            "amp_std_no_monopole": float(amps_half.std(ddof=1)),
            "mean_shift_significance_sigma": float(shift_sigma),
        },
    }
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    log(f"saved {OUT}")


if __name__ == "__main__":
    main()
