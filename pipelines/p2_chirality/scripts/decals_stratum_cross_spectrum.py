#!/usr/bin/env python3
"""
Cross-spectrum C^{An}_ell on the DECaLS [0.5, 0.6) confidence stratum
— Gemini external review v1.0.122 MAJOR M2 closure.

Gemini M2 asked us to apply the same depth-proxy cross-spectrum
diagnostic used to evaluate the canonical-mask +3.64σ residual directly
to the DECaLS [0.5, 0.6) stratum, which carries the largest per-cell
sigma in the 15-cell leg×confidence grid (max|σ|=4.724, family-corrected
to ~2.4σ per the v1.0.119 closure). If the stratum-specific cross-spectrum
with pixel-density is non-trivial at low ell, the DECaLS [0.5, 0.6) excess
is tied to the same depth/sampling systematic that drives interpretation~(ii)
on the canonical mask.

Algorithm:
    1. Load catalog; filter to spirals.
    2. Filter to imaging-leg == DECaLS and confidence_eq ∈ [0.5, 0.6).
    3. Build pixel-density map n_total(p) on this stratum (NSIDE=64).
    4. Build galaxy-weighted-monopole-subtracted A_p map on this stratum.
    5. Compute cross-power C^{An}_ell via NaMaster mode-coupling
       deconvolution on the stratum's own footprint mask.
    6. Run per-pixel-shuffle null × 200 (shuffles CW/CCW labels across
       the stratum spirals; rebuilds A_p but holds n_total fixed).
    7. Report sigma and correlation r at ell=1, 2.

Cost: ~2-3 min wall on Apple Silicon via the v1.0.121 pymaster source build.

Output: outputs/canonical_provenance/decals_stratum_cross_spectrum.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import healpy as hp
import pymaster as nmt
from huggingface_hub import hf_hub_download

NSIDE = 64
LMAX = 3 * NSIDE - 1
N_MC = 200
SEED = 42
CONF_LO = 0.5
CONF_HI = 0.6

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
OUT = REPO / "pipelines/p2_chirality/outputs/canonical_provenance/decals_stratum_cross_spectrum.json"


def assign_leg(ra: np.ndarray, dec: np.ndarray) -> np.ndarray:
    """Same DESI Legacy DR8 imaging-leg cuts as per_leg_confidence_familywise_maxstat.py."""
    leg = np.full(len(ra), "DECaLS", dtype=object)
    leg[dec > 32.375] = "BASS+MzLS"
    des_mask = (dec < -10) & (
        ((ra >= 0) & (ra <= 60)) | ((ra >= 300) & (ra <= 360))
    )
    leg[des_mask] = "DES"
    return leg


def build_master_workspace(mask: np.ndarray) -> nmt.NmtWorkspace:
    """Build NmtWorkspace with single-ell bandpowers including ell=1."""
    bpws = np.full(LMAX + 1, -1, dtype=np.int32)
    for ell in range(1, LMAX + 1):
        bpws[ell] = ell - 1
    ells_arr = np.arange(LMAX + 1, dtype=np.int32)
    weights_arr = np.ones(LMAX + 1, dtype=np.float64)
    b_custom = nmt.NmtBin(bpws=bpws, ells=ells_arr, weights=weights_arr, lmax=LMAX)
    dummy_map = np.zeros(len(mask), dtype=np.float64)
    f0_dummy = nmt.NmtField(mask, [dummy_map], lite=True)
    w = nmt.NmtWorkspace()
    w.compute_coupling_matrix(f0_dummy, f0_dummy, b_custom)
    return w


def cross_decoupled(mask: np.ndarray, A_field: np.ndarray, n_field: np.ndarray,
                     workspace: nmt.NmtWorkspace) -> np.ndarray:
    f_A = nmt.NmtField(mask, [A_field], lite=True)
    f_n = nmt.NmtField(mask, [n_field], lite=True)
    cl_coupled = nmt.compute_coupled_cell(f_A, f_n)
    cl_decoupled = workspace.decouple_cell(cl_coupled)
    return cl_decoupled[0]  # 1D over ell-bins


def auto_decoupled(mask: np.ndarray, field: np.ndarray,
                     workspace: nmt.NmtWorkspace) -> np.ndarray:
    f = nmt.NmtField(mask, [field], lite=True)
    cl_coupled = nmt.compute_coupled_cell(f, f)
    cl_decoupled = workspace.decouple_cell(cl_coupled)
    return cl_decoupled[0]


def main() -> int:
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] DECaLS [0.5,0.6) stratum cross-spectrum", flush=True)

    cat_path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                                "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat_path)
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] spirals: {len(spirals):,}", flush=True)

    ra = spirals["ra"].values.astype(np.float64)
    dec = spirals["dec"].values.astype(np.float64)
    leg = assign_leg(ra, dec)
    p_cw_eq = spirals["p_cw_eq"].values.astype(np.float32)
    p_ccw_eq = spirals["p_ccw_eq"].values.astype(np.float32)
    confidence_eq = np.maximum(p_cw_eq, p_ccw_eq)
    iscw = (spirals["class_eq"].values == "CW").astype(np.int8)

    sel = (leg == "DECaLS") & (confidence_eq >= CONF_LO) & (confidence_eq < CONF_HI)
    print(f"[{time.time()-t0:.1f}s] DECaLS [{CONF_LO}, {CONF_HI}) stratum: {int(sel.sum()):,} spirals",
          flush=True)
    if sel.sum() < 1000:
        print("[FATAL] stratum too small for cross-spectrum")
        return 1

    ra_s = ra[sel]
    dec_s = dec[sel]
    iscw_s = iscw[sel].astype(bool)
    p_cw_local = float(iscw_s.sum() / len(iscw_s))
    print(f"[{time.time()-t0:.1f}s] stratum p_CW_local = {p_cw_local:.6f}", flush=True)

    # Build maps on stratum sample, on canonical NSIDE=64 grid
    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec_s), np.radians(ra_s)).astype(np.int64)
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    n_cw_obs = np.bincount(pix[iscw_s], minlength=npix).astype(np.float64)

    # Stratum footprint mask (nonzero pixels in this stratum only)
    mask = (n_total > 0).astype(np.float64)
    f_sky = float(mask.mean())
    n_pix = int(mask.sum())
    print(f"[{time.time()-t0:.1f}s] stratum footprint mask f_sky={f_sky:.5f}, "
          f"in-mask pixels={n_pix:,}", flush=True)

    # CW-fraction map A_p with proper galaxy-weighted-mean subtraction
    nz = mask.astype(bool)
    A_obs = np.zeros(npix, dtype=np.float64)
    A_obs[nz] = (n_cw_obs[nz] / np.maximum(n_total[nz], 1.0)) - 0.5
    A_gw = float((A_obs[nz] * n_total[nz]).sum() / n_total[nz].sum())
    A_obs_sub = A_obs.copy()
    A_obs_sub[nz] -= A_gw
    print(f"[{time.time()-t0:.1f}s] A_gw (galaxy-weighted mean) = {A_gw:+.6f}", flush=True)

    # Pixel-density field: log10(1+n_total) is a smoother proxy than raw n_total,
    # but for parity with p4_cross_spectrum_A_n.json we use raw n_total minus its
    # mask-mean (centred to zero so the cross power has the same convention).
    n_field = n_total.copy().astype(np.float64)
    n_mean = float(n_field[nz].mean())
    n_field[nz] -= n_mean
    n_field[~nz] = 0.0
    print(f"[{time.time()-t0:.1f}s] n_total mean (in-mask) = {n_mean:.2f}", flush=True)

    # MASTER workspace for cross-decoupling on this stratum's footprint
    print(f"[{time.time()-t0:.1f}s] computing MASTER coupling matrix on stratum mask ...",
          flush=True)
    w = build_master_workspace(mask)
    print(f"[{time.time()-t0:.1f}s] coupling matrix done", flush=True)

    # Auto and cross spectra (data)
    C_AA_data = auto_decoupled(mask, A_obs_sub, w)
    C_NN_data = auto_decoupled(mask, n_field, w)
    C_AN_data = cross_decoupled(mask, A_obs_sub, n_field, w)

    # Correlation r_ell = C_AN / sqrt(C_AA * C_NN)
    def r_at(ell_idx: int) -> float:
        denom = np.sqrt(max(C_AA_data[ell_idx] * C_NN_data[ell_idx], 0.0))
        return float(C_AN_data[ell_idx] / denom) if denom > 0 else float("nan")

    print(f"[{time.time()-t0:.1f}s] data C_AN(ell=1..5) = "
          f"{[f'{v:+.3e}' for v in C_AN_data[:5]]}", flush=True)
    print(f"[{time.time()-t0:.1f}s] data r(ell=1..5) = "
          f"{[f'{r_at(i):+.3f}' for i in range(5)]}", flush=True)

    # Per-pixel-shuffle null × N_MC: shuffle CW/CCW labels within the stratum,
    # rebuild A_p, recompute cross spectrum; n_total field stays fixed.
    rng = np.random.default_rng(SEED)
    C_AN_null = np.zeros((N_MC, LMAX), dtype=np.float64)
    for k in range(N_MC):
        iscw_shuf = rng.binomial(1, p_cw_local, size=len(iscw_s)).astype(np.bool_)
        n_cw_shuf = np.bincount(pix[iscw_shuf], minlength=npix).astype(np.float64)
        A_shuf = np.zeros(npix, dtype=np.float64)
        A_shuf[nz] = (n_cw_shuf[nz] / np.maximum(n_total[nz], 1.0)) - 0.5
        A_gw_shuf = float((A_shuf[nz] * n_total[nz]).sum() / n_total[nz].sum())
        A_shuf_sub = A_shuf.copy()
        A_shuf_sub[nz] -= A_gw_shuf
        C_AN_shuf = cross_decoupled(mask, A_shuf_sub, n_field, w)
        C_AN_null[k] = C_AN_shuf
        if (k + 1) % 50 == 0:
            print(f"[{time.time()-t0:.1f}s]   null {k+1}/{N_MC}", flush=True)

    # Sigma at ell=1, 2
    def sigma_at(ell_idx: int) -> float:
        data = C_AN_data[ell_idx]
        null_mean = float(C_AN_null[:, ell_idx].mean())
        null_std = float(C_AN_null[:, ell_idx].std(ddof=1))
        return (data - null_mean) / null_std if null_std > 0 else float("nan")

    sigma_l1 = sigma_at(0)
    sigma_l2 = sigma_at(1)
    r_l1 = r_at(0)
    r_l2 = r_at(1)
    null_mean_l1 = float(C_AN_null[:, 0].mean())
    null_mean_l2 = float(C_AN_null[:, 1].mean())
    null_std_l1 = float(C_AN_null[:, 0].std(ddof=1))
    null_std_l2 = float(C_AN_null[:, 1].std(ddof=1))

    summary = {
        "purpose": ("DECaLS [0.5, 0.6) confidence stratum cross-spectrum C^{An}_ell — "
                    "Gemini v1.0.122 external review MAJOR M2 closure. Tests whether the "
                    "stratum's max|σ|=4.724 dipole signature shares the same depth-correlated "
                    "systematic origin as the canonical-mask +3.64σ residual."),
        "version": "v1.0.125-decals-stratum-cross-spectrum",
        "config": {"nside": NSIDE, "lmax": LMAX, "n_mc": N_MC, "seed": SEED,
                   "stratum_leg": "DECaLS", "stratum_conf_range": [CONF_LO, CONF_HI]},
        "stratum": {"n_spirals": int(sel.sum()), "p_cw_local": p_cw_local,
                    "f_sky": f_sky, "n_pix_in_mask": n_pix, "A_gw": A_gw,
                    "n_total_mean_in_mask": n_mean},
        "data_C_AA_l1_to_5": [float(v) for v in C_AA_data[:5]],
        "data_C_NN_l1_to_5": [float(v) for v in C_NN_data[:5]],
        "data_C_AN_l1_to_5": [float(v) for v in C_AN_data[:5]],
        "data_correlation_r_l1_to_5": [r_at(i) for i in range(5)],
        "null_mean_C_AN_l1_to_5": [float(C_AN_null[:, i].mean()) for i in range(5)],
        "null_std_C_AN_l1_to_5": [float(C_AN_null[:, i].std(ddof=1)) for i in range(5)],
        "sigma_C_AN_l1_to_5": [sigma_at(i) for i in range(5)],
        "headline": {
            "ell_1": {
                "C_AN": float(C_AN_data[0]),
                "r": r_l1, "sigma": sigma_l1,
                "null_mean": null_mean_l1, "null_std": null_std_l1,
            },
            "ell_2": {
                "C_AN": float(C_AN_data[1]),
                "r": r_l2, "sigma": sigma_l2,
                "null_mean": null_mean_l2, "null_std": null_std_l2,
            },
        },
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    OUT.write_text(json.dumps(summary, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] wrote {OUT.relative_to(REPO)}", flush=True)
    print(f"\nHEADLINE: DECaLS [{CONF_LO}, {CONF_HI}) cross-spectrum")
    print(f"  ell=1: C_AN={C_AN_data[0]:+.3e}  r={r_l1:+.3f}  sigma={sigma_l1:+.2f}")
    print(f"  ell=2: C_AN={C_AN_data[1]:+.3e}  r={r_l2:+.3f}  sigma={sigma_l2:+.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
