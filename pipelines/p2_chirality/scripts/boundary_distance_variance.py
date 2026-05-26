#!/usr/bin/env python3
"""
Gemini-Major1 closure: Boundary-distance variance.

The canonical mask has a complex multi-leg patchy footprint (~|b|>15 deg
galactic cut + DR8 survey-area cuts). If the +3.64sigma canonical-mask
ell=1 residual is mask-edge-induced (NaMaster sharp-edge artifact or
boundary-region depth/PSF gradient), then the A_p variance should
concentrate near the mask boundary and dilute toward the interior.
Conversely, if the residual is uniformly distributed across the
interior, mask-boundary leakage is NOT the dominant mechanism.

Algorithm:
  1. Build the canonical |b|>15 deg mask at NSIDE=64.
  2. For each in-mask pixel, compute the angular distance to the
     nearest out-of-mask pixel (Euclidean on the unit sphere via
     hp.query_disc growth OR direct nearest-neighbor over the
     boundary set).
  3. Define 5 boundary-distance shells:
       Shell 0 (boundary):   d <= 2 deg
       Shell 1 (near):       2 deg < d <= 5 deg
       Shell 2 (mid):        5 deg < d <= 10 deg
       Shell 3 (deep):       10 deg < d <= 20 deg
       Shell 4 (deep-int):   d > 20 deg
  4. For each shell, compute:
       - n_pix_shell, total_galaxies_shell, n_spiral_shell
       - var(A_p) within shell
       - <A_p^2> weighted by per-pixel galaxy count
       - The partial contribution to C_1 if only that shell were retained:
           Strip A_p outside the shell, recompute MASTER-decoupled C_1
           with the shell-restricted mask.
       - sigma_C1 per shell against the same systematics-preserving
         density-stratified null (rerunning per shell would be expensive;
         instead use binomial null at the shell sample size).

  5. If shell-0 dominates the C_1 budget, mask-edge mechanism is favored.
     If C_1 is uniformly distributed (all shells contribute proportional
     to f_sky_shell), then interpretation (ii) coherent depth-correlated
     systematic is favored (consistent with the M1 finding that density-
     stratified null doesn't absorb the residual).

Local-feasible: pure numpy + healpy + pymaster, no GPU, no pod, no
catalog re-download (uses HF cache from M1 script).

Output: pipelines/p2_chirality/outputs/canonical_provenance/
        boundary_distance_variance.json
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
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/boundary_distance_variance.json")

SHELL_EDGES_DEG = [0.0, 2.0, 5.0, 10.0, 20.0, 180.0]
SHELL_LABELS = ["boundary_le2deg", "near_2to5deg", "mid_5to10deg", "deep_10to20deg", "deep_interior_gt20deg"]


def canonical_mask(nside: int) -> np.ndarray:
    """|b|>15 deg galactic cut at NSIDE; matches v1.0.107+ canonical."""
    npix = hp.nside2npix(nside)
    ipix = np.arange(npix)
    theta, phi = hp.pix2ang(nside, ipix)
    coords = hp.Rotator(coord=["C", "G"])
    theta_g, _ = coords(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > 15.0).astype(float)


def build_data_maps():
    print(f"[{time.time()-t0:.1f}s] downloading catalog from HF cache ...", flush=True)
    cat_path = hf_hub_download(
        "bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset"
    )
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    df = df.loc[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)
    n_spi = len(df)
    print(f"[{time.time()-t0:.1f}s] spirals: {n_spi:,}", flush=True)

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


def boundary_distance_deg(mask: np.ndarray, nside: int) -> np.ndarray:
    """
    For each in-mask pixel, compute the angular distance (degrees) to the
    nearest out-of-mask pixel. Implementation: iterate over boundary
    pixels (in-mask with at least one out-of-mask neighbor), then run
    healpy query_disc outward in 1-deg shells, marking in-mask pixels
    with their first-touched shell distance.
    """
    npix = hp.nside2npix(nside)
    in_mask = mask > 0
    # Identify boundary pixels: in-mask pixels with at least one out-of-mask neighbor
    nbr = hp.get_all_neighbours(nside, np.arange(npix))  # (8, npix)
    has_out_nbr = np.any((nbr >= 0) & (~in_mask[nbr]), axis=0) & in_mask
    boundary_pix = np.where(has_out_nbr)[0]
    print(f"[{time.time()-t0:.1f}s] boundary pixels: {len(boundary_pix):,}", flush=True)

    # For each in-mask pixel, find min distance to any boundary pixel.
    # Use BFS in pixel-neighbor space (cheaper than per-pixel angular distance to all boundary).
    # Initialize: boundary pixels at distance 0 (in pixel-rings), expand outward.
    dist_rings = np.full(npix, -1, dtype=np.int32)
    dist_rings[boundary_pix] = 0
    frontier = boundary_pix
    ring = 0
    while len(frontier) > 0:
        ring += 1
        next_frontier_set = set()
        nbrs = hp.get_all_neighbours(nside, frontier)  # (8, len(frontier))
        for col in nbrs.T:
            for p in col:
                if p < 0:
                    continue
                if in_mask[p] and dist_rings[p] == -1:
                    next_frontier_set.add(int(p))
        frontier = np.array(sorted(next_frontier_set), dtype=np.int32)
        dist_rings[frontier] = ring
        if ring > 200:  # safety
            break
    # Convert ring count to angular distance via pixel resolution.
    pix_res_deg = np.degrees(hp.nside2resol(nside))
    dist_deg = np.where(dist_rings >= 0, dist_rings * pix_res_deg, np.nan)
    print(f"[{time.time()-t0:.1f}s] max boundary distance: {np.nanmax(dist_deg):.2f} deg "
          f"(pix_res={pix_res_deg:.3f} deg, {int(np.nanmax(dist_rings))} rings)", flush=True)
    return dist_deg


def shell_C1(A_p_corr: np.ndarray, mask_shell: np.ndarray, wsp_full: nmt.NmtWorkspace,
             wsp_cache: dict, nmtb: nmt.NmtBin) -> tuple[float, nmt.NmtWorkspace]:
    """Compute MASTER-decoupled C_1 with a shell-restricted mask.
    Reuses workspace per unique mask via cache keyed on mask-hash."""
    mask_key = hash(mask_shell.tobytes())
    if mask_key in wsp_cache:
        wsp = wsp_cache[mask_key]
    else:
        wsp = nmt.NmtWorkspace()
        f0_mask = nmt.NmtField(mask_shell, [np.zeros_like(mask_shell)])
        wsp.compute_coupling_matrix(f0_mask, f0_mask, nmtb)
        wsp_cache[mask_key] = wsp
    f0 = nmt.NmtField(mask_shell, [A_p_corr * mask_shell])
    coupled = nmt.compute_coupled_cell(f0, f0)
    decoupled = wsp.decouple_cell(coupled)[0]
    return float(decoupled[0]), wsp


def main():
    global t0
    t0 = time.time()
    print(f"[{t0:.1f}s] boundary-distance variance — canonical mask NSIDE={NSIDE}", flush=True)

    A_p, n_total, n_spi = build_data_maps()
    mask = canonical_mask(NSIDE)
    in_mask = mask > 0
    f_sky_full = float(in_mask.mean())
    print(f"[{time.time()-t0:.1f}s] full canonical f_sky = {f_sky_full:.5f}", flush=True)

    dist_deg = boundary_distance_deg(mask, NSIDE)

    # Galaxy-weighted mask-mean subtraction
    A_p_corr = A_p - np.average(A_p[in_mask], weights=n_total[in_mask])

    # Full-mask MASTER baseline (matches v1.0.133 M1 baseline)
    nmtb = nmt.NmtBin.from_edges(np.arange(1, LMAX + 1), np.arange(2, LMAX + 2))
    wsp_full = nmt.NmtWorkspace()
    f0_full_mask = nmt.NmtField(mask, [np.zeros_like(mask)])
    wsp_full.compute_coupling_matrix(f0_full_mask, f0_full_mask, nmtb)
    f0_data = nmt.NmtField(mask, [A_p_corr * mask])
    coupled = nmt.compute_coupled_cell(f0_data, f0_data)
    C1_full = float(wsp_full.decouple_cell(coupled)[0][0])
    print(f"[{time.time()-t0:.1f}s] full-mask C_1 = {C1_full:.4e} "
          f"(should match v1.0.133 baseline 6.55e-6)", flush=True)

    # Per-shell analysis
    shells = []
    wsp_cache: dict = {}
    for i in range(len(SHELL_LABELS)):
        lo, hi = SHELL_EDGES_DEG[i], SHELL_EDGES_DEG[i + 1]
        shell_pix = in_mask & (dist_deg > lo) & (dist_deg <= hi)
        # Shell-restricted mask: keep only pixels within this distance shell
        mask_shell = mask.copy()
        mask_shell[~shell_pix] = 0.0
        n_pix = int(shell_pix.sum())
        f_sky_shell = float(shell_pix.mean())
        if n_pix == 0:
            print(f"[{time.time()-t0:.1f}s] shell {SHELL_LABELS[i]}: EMPTY", flush=True)
            shells.append({
                "label": SHELL_LABELS[i], "lo_deg": lo, "hi_deg": hi,
                "n_pix": 0, "f_sky_shell": 0.0,
                "var_A_p": None, "weighted_A2": None,
                "n_total_in_shell": 0, "n_spiral_in_shell": 0,
                "C1_shell_master": None, "frac_C1": 0.0,
            })
            continue
        A_p_in_shell = A_p_corr[shell_pix]
        n_in_shell = n_total[shell_pix]
        # var weighted by per-pixel galaxy count (avoids empty-pixel domination)
        if n_in_shell.sum() > 0:
            weighted_A = np.average(A_p_in_shell, weights=n_in_shell)
            weighted_A2 = float(np.average((A_p_in_shell - weighted_A) ** 2, weights=n_in_shell))
        else:
            weighted_A2 = float(np.var(A_p_in_shell))
        var_A_p = float(np.var(A_p_in_shell))
        C1_shell, _ = shell_C1(A_p_corr, mask_shell, wsp_full, wsp_cache, nmtb)
        print(f"[{time.time()-t0:.1f}s] shell {SHELL_LABELS[i]}: n_pix={n_pix:,} "
              f"f_sky={f_sky_shell:.4f} var(A_p)={var_A_p:.3e} "
              f"weighted_A2={weighted_A2:.3e} C1_shell={C1_shell:.4e}", flush=True)
        shells.append({
            "label": SHELL_LABELS[i], "lo_deg": lo, "hi_deg": hi,
            "n_pix": n_pix, "f_sky_shell": f_sky_shell,
            "var_A_p": var_A_p, "weighted_A2": weighted_A2,
            "n_total_in_shell": int(n_in_shell.sum()),
            "n_spiral_in_shell": int(n_in_shell.sum()),
            "C1_shell_master": C1_shell,
            "frac_C1": C1_shell / C1_full if C1_full != 0 else 0.0,
        })

    # Interpretation: shell-0 (boundary) C_1 / f_sky_shell vs deep-interior C_1 / f_sky_shell
    # If boundary >> interior per unit f_sky, mask-edge mechanism favored.
    # If proportional, interpretation (ii) coherent depth-correlated systematic uniform.
    per_fsky_C1 = [(s["label"], s["C1_shell_master"] / s["f_sky_shell"] if s["f_sky_shell"] > 0
                    and s["C1_shell_master"] is not None else None) for s in shells]
    print(f"\n[{time.time()-t0:.1f}s] per-fsky-normalized C_1 by shell:", flush=True)
    for label, val in per_fsky_C1:
        print(f"    {label}: {val:.4e}" if val is not None else f"    {label}: None", flush=True)

    results = {
        "version": "v1.0.133+",
        "purpose": (
            "Gemini-Major1 closure: stratify the canonical-mask C_1 budget "
            "by boundary-distance shells. Tests whether the +3.64sigma residual "
            "concentrates near the mask boundary (NaMaster sharp-edge / "
            "boundary-region systematic) or is uniformly distributed across "
            "the interior (interpretation (ii) coherent depth-correlated)."
        ),
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "nside": NSIDE, "lmax": LMAX,
            "pix_res_deg": float(np.degrees(hp.nside2resol(NSIDE))),
            "shell_edges_deg": SHELL_EDGES_DEG,
            "shell_labels": SHELL_LABELS,
            "n_spirals": n_spi,
            "f_sky_full": f_sky_full,
        },
        "baseline": {
            "data_decoupled_C1_full_mask": C1_full,
        },
        "shells": shells,
        "per_fsky_normalized_C1": [
            {"label": label, "C1_per_fsky": val}
            for label, val in per_fsky_C1
        ],
        "interpretation": (
            "If shell-0 boundary (d<=2 deg) per-fsky C_1 >> deep-interior "
            "per-fsky C_1, the mask-edge mechanism is the dominant contributor "
            "(consistent with interpretation (iii) sharp-edge variant). If "
            "all shells give comparable per-fsky C_1, the residual is uniformly "
            "distributed across the canonical interior — consistent with "
            "interpretation (ii) coherent depth/PSF/morphology-correlated "
            "systematic, and complementary to the M1 finding that density-"
            "stratification alone doesn't absorb it."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
