#!/usr/bin/env python3
"""
Brick-boundary control test for the w_CW(theta) -2.41σ excursion at θ≈0.5°
(GRO-B4 + GPT-B4 MAJOR from the v1.0.77 external review round).

DESI Legacy DR8 bricks are ~0.25° square, encoded in the dr8_id column
as "<brick_id>_<source_idx>". We compute the two-point chirality
correlation w_CW(theta) twice on the same 50K-HC-spiral sample:

  (A) baseline: as in v1.0.77 §sec:wtheta (no brick masking)
  (B) brick-boundary-cut: drop sources within 0.05° of any brick edge

If the -2.41σ at θ≈0.5° is driven by brick-boundary classifier
artifacts, the (B) result should null out that bin. If it persists,
the brick-boundary attribution in the paper is unsupported.

Output: brick_boundary_control_wtheta.json
"""
import json, time, sys
from pathlib import Path
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download
from sklearn.neighbors import BallTree

N_SAMPLE = 50_000
N_MC = 100
SEED = 42
THETA_EDGES_DEG = np.logspace(np.log10(0.1), np.log10(10.0), 11)
BRICK_EDGE_BUFFER_DEG = 0.05  # exclude sources within 0.05° of brick edge
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/brick_boundary_control_wtheta.json")


def parse_brick_id(dr8_id):
    """Extract brick_id from dr8_id of form 'BBBBBB_NNN'."""
    return int(dr8_id.split("_")[0])


def brick_pixel_position_within_brick(ra, dec, brick_id):
    """Approximate per-brick position within its 0.25° square.
    DESI Legacy DR8 bricks are tiled in (dec, ra) at 0.25° pitch with
    declination-dependent ra-spacing. We approximate as:
      ra_within_brick = (ra mod 0.25) / 0.25 (range [0,1])
      dec_within_brick = (dec mod 0.25) / 0.25
    A source is near a brick edge if either coordinate is within
    BRICK_EDGE_BUFFER_DEG/0.25 = 0.2 of {0, 1}.
    """
    ra_frac = (ra % 0.25) / 0.25
    dec_frac = (dec % 0.25) / 0.25
    edge_buffer_frac = BRICK_EDGE_BUFFER_DEG / 0.25  # = 0.2
    near_edge = (
        (ra_frac < edge_buffer_frac) | (ra_frac > 1 - edge_buffer_frac) |
        (dec_frac < edge_buffer_frac) | (dec_frac > 1 - edge_buffer_frac)
    )
    return near_edge


def count_pairs_via_tree(coords, labels, radii):
    """Same-vs-different label pair counts in concentric angular shells."""
    tree = BallTree(coords, metric="haversine")
    same = np.zeros(len(radii) - 1, dtype=np.int64)
    diff = np.zeros(len(radii) - 1, dtype=np.int64)
    for k, (r_lo, r_hi) in enumerate(zip(radii[:-1], radii[1:])):
        idxs_hi = tree.query_radius(coords, r=r_hi)
        idxs_lo = tree.query_radius(coords, r=r_lo) if r_lo > 0 else None
        for j, hi_nbrs in enumerate(idxs_hi):
            if idxs_lo is not None:
                nbrs = np.setdiff1d(hi_nbrs, idxs_lo[j], assume_unique=True)
            else:
                nbrs = hi_nbrs
            nbrs = nbrs[nbrs > j]
            if len(nbrs) == 0:
                continue
            same[k] += int((labels[nbrs] == labels[j]).sum())
            diff[k] += int((labels[nbrs] != labels[j]).sum())
    return same, diff


def compute_wtheta(sub, seed, label, n_mc=N_MC):
    rng = np.random.default_rng(seed)
    ra_rad = np.radians(sub["ra"].values)
    dec_rad = np.radians(sub["dec"].values)
    coords = np.stack([dec_rad, ra_rad], axis=1)
    labels = (sub["class_eq"].values == "CW").astype(np.int8)
    radii = np.radians(THETA_EDGES_DEG)
    centers = np.sqrt(THETA_EDGES_DEG[:-1] * THETA_EDGES_DEG[1:])

    print(f"  data pair counts on {len(sub):,} sources ...", flush=True)
    t = time.time()
    same_obs, diff_obs = count_pairs_via_tree(coords, labels, radii)
    total_obs = same_obs + diff_obs
    w_obs = np.where(total_obs > 0, (same_obs - diff_obs) / total_obs, 0.0)
    print(f"  data pairs in {time.time()-t:.1f}s", flush=True)

    print(f"  N_MC={n_mc} label-shuffle null ...", flush=True)
    w_null = np.zeros((n_mc, len(centers)))
    for k in range(n_mc):
        labels_shuf = labels.copy()
        rng.shuffle(labels_shuf)
        s, d = count_pairs_via_tree(coords, labels_shuf, radii)
        tot = s + d
        w_null[k] = np.where(tot > 0, (s - d) / tot, 0.0)
        if (k + 1) % 20 == 0:
            print(f"    MC {k+1}/{n_mc}", flush=True)

    null_mean = w_null.mean(axis=0)
    null_std = w_null.std(axis=0, ddof=1)
    sigma = (w_obs - null_mean) / (null_std + 1e-30)
    return {
        "label": label,
        "n_used": int(len(sub)),
        "theta_centers_deg": centers.tolist(),
        "w_obs": w_obs.tolist(),
        "null_mean": null_mean.tolist(),
        "null_std": null_std.tolist(),
        "sigma": sigma.tolist(),
        "n_pairs": total_obs.tolist(),
        "max_abs_sigma": float(np.max(np.abs(sigma))),
    }


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print(f"[{time.time()-t0:.1f}s] Loading catalog ...", flush=True)
    p = hf_hub_download("bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(p, columns=["dr8_id", "ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    spirals["max_eq"] = spirals[["p_cw_eq", "p_ccw_eq"]].max(axis=1)
    hc = spirals[spirals["max_eq"] > 0.6].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] HC-spirals: {len(hc):,}", flush=True)

    idx = rng.choice(len(hc), size=min(N_SAMPLE, len(hc)), replace=False)
    sub_all = hc.iloc[idx].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] Sampled {len(sub_all):,} for pair counts", flush=True)

    # Identify brick-boundary sources
    near_edge = brick_pixel_position_within_brick(sub_all["ra"].values, sub_all["dec"].values, sub_all["dr8_id"].values)
    n_near = int(near_edge.sum())
    print(f"[{time.time()-t0:.1f}s] sources near brick edge (buffer {BRICK_EDGE_BUFFER_DEG}°): {n_near:,} ({100*n_near/len(sub_all):.1f}%)", flush=True)

    sub_interior = sub_all[~near_edge].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] sources interior (away from brick edge): {len(sub_interior):,}", flush=True)

    print(f"\n[{time.time()-t0:.1f}s] === BASELINE: no brick masking ===", flush=True)
    res_baseline = compute_wtheta(sub_all, seed=SEED, label="baseline_no_brick_mask")

    print(f"\n[{time.time()-t0:.1f}s] === BRICK-INTERIOR ONLY ===", flush=True)
    res_interior = compute_wtheta(sub_interior, seed=SEED + 1, label="brick_interior_only")

    print(f"\n=== SUMMARY ===", flush=True)
    print(f"{'θ (deg)':>8s} {'baseline σ':>12s} {'interior σ':>12s} {'Δσ':>8s}", flush=True)
    for i, c in enumerate(res_baseline["theta_centers_deg"]):
        b = res_baseline["sigma"][i]
        x = res_interior["sigma"][i]
        print(f"{c:8.3f} {b:+12.3f} {x:+12.3f} {(x-b):+8.3f}", flush=True)

    out = {
        "version": "v1.0.83-brick-boundary-control",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "n_sample": N_SAMPLE,
            "n_mc": N_MC,
            "seed": SEED,
            "theta_edges_deg": THETA_EDGES_DEG.tolist(),
            "brick_edge_buffer_deg": BRICK_EDGE_BUFFER_DEG,
            "brick_size_deg": 0.25,
            "subsample": "HC-spiral (p_eq > 0.6)",
            "rationale": "Test whether the -2.41σ excursion at θ≈0.5° in baseline w_CW(θ) (v1.0.77 §sec:wtheta) is driven by brick-boundary classifier artifacts. If interior-only sample shows the same excursion, brick-boundary is NOT the mechanism. If excursion vanishes/attenuates, brick-boundary is confirmed as the source.",
        },
        "results": {
            "baseline": res_baseline,
            "brick_interior": res_interior,
            "n_near_brick_edge": n_near,
            "fraction_near_brick_edge": float(n_near / len(sub_all)),
        },
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\nSaved -> {OUT}", flush=True)
    print(f"Total wall: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
