#!/usr/bin/env python3
"""
ChatGPT-M1 closure: Systematics-preserving canonical-mask null.

The standard binomial per-pixel-shuffle null does NOT preserve depth/PSF/
morphology/imaging-leg correlations. The cross-spectrum result
r_ell=2(A_p × n_total) = -0.65 / sigma = -2.89 shows the asymmetry map
A_p IS correlated with pixel-density structure. A null model that
preserves this correlation should absorb most of the +3.64sigma canonical-
mask residual.

Algorithm:
  1. Load catalog (cached locally from HF).
  2. Build A_p map + pixel-density map n_total on canonical mask (NSIDE=64).
  3. Stratify pixels into 10 pixel-density quintiles (10 strata for finer
     conditioning of the depth-systematic).
  4. For each null realization:
       a. WITHIN each stratum, randomly permute A_p values across pixels
          (preserving the within-stratum mean-zero, but breaking any
          residual spatial correlation that doesn't track the density
          stratification).
       b. Apply proper galaxy-weighted mask-mean subtraction.
       c. Compute pseudo-C_ell via nmt.NmtField + nmt.compute_coupled_cell.
       d. MASTER-decouple: C_decoupled = M^-1 pseudo_C.
       e. Record decoupled C_1.
  5. Compare data C_1 against the systematics-preserving null distribution.
     If data sigma vs this null is << +3.64 (binomial), then the
     density-stratification null absorbs the systematic — supporting
     interpretation (ii). If it's still high, depth-stratification is not
     the dominant systematic and ChatGPT-M2 full template regression is
     needed.

N_MC = 500 to match the original direct-MC. Time budget ~13 min on local
pymaster 2.6, same as the v1.0.131 N=10,000 MASTER-decoupled monopole null.

Output: outputs/canonical_provenance/systematics_preserving_null.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import healpy as hp
import pandas as pd
import pymaster as nmt
from huggingface_hub import hf_hub_download

NSIDE = 64
LMAX = 191
N_MC = 500
N_STRATA = 10  # decile-conditioning on pixel-density
SEED = 42
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/systematics_preserving_null.json")


def galactic_to_equatorial_mask(nside: int) -> np.ndarray:
    """Canonical mask: same as in canonical_l1_namaster_pod.py and master_decoupled_monopole_null.py."""
    npix = hp.nside2npix(nside)
    ipix = np.arange(npix)
    theta, phi = hp.pix2ang(nside, ipix)
    ra_deg = np.degrees(phi)
    dec_deg = 90.0 - np.degrees(theta)
    # Apply ~|b|>15 deg galactic cut (matches v1.0.107+ canonical mask)
    coords = hp.Rotator(coord=["C", "G"])
    theta_g, phi_g = coords(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    mask = (np.abs(b_deg) > 15.0).astype(float)
    return mask


def build_data_and_density_maps():
    """Load catalog + build A_p map and pixel-density map on canonical mask."""
    print(f"[{time.time()-t0:.1f}s] downloading catalog from HF cache ...", flush=True)
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset"
    )
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    print(f"[{time.time()-t0:.1f}s] catalog rows: {len(df):,}", flush=True)
    # Filter to spirals (CW + CCW); ignore NS/edge-on
    spi_mask = df["class_eq"].isin(["CW", "CCW"])
    df = df.loc[spi_mask].reset_index(drop=True)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)
    n_spi = len(df)
    print(f"[{time.time()-t0:.1f}s] spirals: {n_spi:,}", flush=True)

    # Compute per-pixel CW-fraction and total counts
    theta = np.radians(90.0 - df["dec"].values)
    phi = np.radians(df["ra"].values)
    pix = hp.ang2pix(NSIDE, theta, phi)
    npix = hp.nside2npix(NSIDE)
    n_cw = np.bincount(pix, weights=is_cw.astype(np.float64), minlength=npix)
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    A_p = np.zeros(npix, dtype=np.float64)
    valid = n_total > 0
    A_p[valid] = 2.0 * (n_cw[valid] / n_total[valid]) - 1.0
    return A_p, n_total, n_spi


def main():
    global t0
    t0 = time.time()
    print(f"[{t0:.1f}s] systematics-preserving canonical-mask null x {N_MC}", flush=True)
    rng = np.random.default_rng(SEED)

    A_p, n_total, n_spi = build_data_and_density_maps()

    mask = galactic_to_equatorial_mask(NSIDE)
    in_mask = mask > 0
    f_sky = float(in_mask.mean())
    print(f"[{time.time()-t0:.1f}s] f_sky = {f_sky:.5f}", flush=True)

    # Stratify pixels by pixel-density within the mask
    n_in = n_total[in_mask]
    strata_edges = np.quantile(n_in[n_in > 0], np.linspace(0, 1, N_STRATA + 1))
    strata_edges[0] = -1.0  # include zero-count pixels in stratum 0
    strata_edges[-1] = n_in.max() + 1.0
    # Map each in-mask pixel to its stratum
    pix_strata = np.full(hp.nside2npix(NSIDE), -1, dtype=np.int8)
    pix_strata[in_mask] = np.digitize(n_total[in_mask], strata_edges[1:-1])
    print(
        f"[{time.time()-t0:.1f}s] strata sizes:",
        [int((pix_strata == s).sum()) for s in range(N_STRATA)],
        flush=True,
    )

    # Galaxy-weighted mask-mean subtraction (matches v1.0.107+ proper-monopole convention)
    A_p_corr = A_p - np.average(A_p[in_mask], weights=n_total[in_mask])
    A_p_corr_in = A_p_corr * mask

    # Set up NaMaster
    print(f"[{time.time()-t0:.1f}s] computing MASTER coupling matrix ...", flush=True)
    nmtb = nmt.NmtBin.from_edges(np.arange(1, LMAX + 1), np.arange(2, LMAX + 2))
    wsp = nmt.NmtWorkspace()
    f0_mask = nmt.NmtField(mask, [np.zeros_like(mask)])
    wsp.compute_coupling_matrix(f0_mask, f0_mask, nmtb)
    print(f"[{time.time()-t0:.1f}s] coupling matrix done", flush=True)

    # Data side
    f0_data = nmt.NmtField(mask, [A_p_corr])
    coupled_data = nmt.compute_coupled_cell(f0_data, f0_data)
    decoupled_data = wsp.decouple_cell(coupled_data)[0]
    # bin index 0 corresponds to ell=1 (since we bin from ell=1)
    C1_data = float(decoupled_data[0])
    print(f"[{time.time()-t0:.1f}s] data C_1 (post-MASTER) = {C1_data:.4e}", flush=True)

    # Pre-extract per-stratum A_p values for shuffling
    stratum_to_pix = [np.where(pix_strata == s)[0] for s in range(N_STRATA)]
    stratum_to_values = [A_p_corr[stratum_to_pix[s]].copy() for s in range(N_STRATA)]

    # Null realizations: shuffle WITHIN strata
    C1_nulls = np.zeros(N_MC, dtype=np.float64)
    for k in range(N_MC):
        A_p_shuf = np.zeros_like(A_p_corr)
        for s in range(N_STRATA):
            pix = stratum_to_pix[s]
            vals = stratum_to_values[s].copy()
            rng.shuffle(vals)
            A_p_shuf[pix] = vals
        f0_shuf = nmt.NmtField(mask, [A_p_shuf])
        coupled = nmt.compute_coupled_cell(f0_shuf, f0_shuf)
        decoupled = wsp.decouple_cell(coupled)[0]
        C1_nulls[k] = float(decoupled[0])
        if (k + 1) % 25 == 0:
            elapsed = time.time() - t0
            rate = (k + 1) / elapsed
            eta = (N_MC - k - 1) / rate
            mean_so_far = C1_nulls[: k + 1].mean()
            std_so_far = C1_nulls[: k + 1].std()
            print(
                f"[{elapsed:.1f}s]   {k+1:5d}/{N_MC} ({rate:.2f}/s; ETA {eta:.0f}s); "
                f"current null mean={mean_so_far:.4e}, std={std_so_far:.4e}",
                flush=True,
            )

    null_mean = float(C1_nulls.mean())
    null_std = float(C1_nulls.std())
    sigma_data = (C1_data - null_mean) / null_std
    n_exceed = int((C1_nulls >= C1_data).sum())
    p_two_sided = 2.0 * min(n_exceed, N_MC - n_exceed) / N_MC

    results = {
        "version": "v1.0.133",
        "purpose": (
            "ChatGPT-M1 closure: systematics-preserving canonical-mask null on the "
            "post-MASTER decoupled C_1. Null model permutes A_p WITHIN pixel-density "
            "deciles (preserves density-stratified depth systematic structure)."
        ),
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "nside": NSIDE,
            "lmax": LMAX,
            "n_mc": N_MC,
            "n_strata": N_STRATA,
            "seed": SEED,
            "f_sky": f_sky,
            "n_spirals": n_spi,
        },
        "results": {
            "data_decoupled_C1": C1_data,
            "null_mean_C1": null_mean,
            "null_std_C1": null_std,
            "sigma_data_vs_null": sigma_data,
            "empirical_rank_p_two_sided": p_two_sided,
            "n_exceed_null": n_exceed,
        },
        "interpretation": (
            "If sigma_data_vs_null << +3.64 (the binomial null sigma), the density-"
            "stratified null absorbs the systematic, supporting interpretation (ii) "
            "depth-correlated systematic. If sigma still > +3, depth-stratification "
            "is not the dominant systematic and full template regression is needed."
        ),
    }
    print(
        f"\n[{time.time()-t0:.1f}s] FINAL: sigma_data_vs_null = {sigma_data:+.3f}, "
        f"p_MC = {n_exceed}/{N_MC} = {p_two_sided:.4f}",
        flush=True,
    )
    print(
        f"  Compare to binomial-null sigma = +3.64 ({C1_data:.3e} vs null mean 3.12e-6, std 3.31e-6)",
        flush=True,
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=2))
    print(f"[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
