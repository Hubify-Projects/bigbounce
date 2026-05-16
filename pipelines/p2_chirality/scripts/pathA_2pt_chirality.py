#!/usr/bin/env python3
"""
Path A — two-point chirality correlation w_theta(theta).

For pairs of spirals at angular separation theta in bins, compute:
  w(theta) = (1 - 2*N_unlike / N_total_pairs)
where unlike = CW-CCW pairs, total = CW-CW + CCW-CCW + CW-CCW + CCW-CW.

Positive w(theta) at scale theta => CW spirals cluster with CW (spin alignment).
Pure null (random handedness) gives w(theta) = 0 at all scales.

To control n^2 cost, restrict to HC-spirals (p_eq > 0.6, ~950K) and use a
random subsample of 50K for the auto-pair counts. Compare against the
same statistic on N_MC=200 random-shuffle nulls.

If positive at any scale, that's a NOVEL signal not captured by the
mean dipole. If null, that's another confirmation.
"""
from __future__ import annotations
import json, time, sys
from pathlib import Path
import numpy as np
import pandas as pd
import healpy as hp
from huggingface_hub import hf_hub_download

OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/pathA_2pt_chirality.json")
N_SAMPLE = 50_000
N_MC = 200
SEED = 42
# Angular separation bins, log-spaced from 0.1 deg to 10 deg
THETA_EDGES_DEG = np.logspace(np.log10(0.1), np.log10(10.0), 11)

# K-D tree on unit sphere for fast neighbor queries.
from sklearn.neighbors import BallTree


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print(f"[{time.time()-t0:.1f}s] Loading catalog ...", flush=True)
    p = hf_hub_download("bamfai/galaxy-chirality-catalog", "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(p, columns=["ra", "dec", "class_eq", "p_cw_eq", "p_ccw_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    spirals["max_eq"] = spirals[["p_cw_eq", "p_ccw_eq"]].max(axis=1)
    hc = spirals[spirals["max_eq"] > 0.6].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] HC-spirals: {len(hc):,}", flush=True)

    idx = rng.choice(len(hc), size=min(N_SAMPLE, len(hc)), replace=False)
    sub = hc.iloc[idx].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] Sampled {len(sub):,} for pair counts", flush=True)

    ra_rad = np.radians(sub["ra"].values)
    dec_rad = np.radians(sub["dec"].values)
    coords = np.stack([dec_rad, ra_rad], axis=1)
    labels = (sub["class_eq"].values == "CW").astype(np.int8)  # 1=CW, 0=CCW
    n_cw = labels.sum()
    n_ccw = len(labels) - n_cw
    print(f"[{time.time()-t0:.1f}s] CW={n_cw:,} CCW={n_ccw:,} p_CW={n_cw/len(labels):.5f}", flush=True)

    tree = BallTree(coords, metric="haversine")
    radii = np.radians(THETA_EDGES_DEG)
    centers_deg = np.sqrt(THETA_EDGES_DEG[:-1] * THETA_EDGES_DEG[1:])

    def count_pairs(labels_in):
        """Returns (cw_cw + ccw_ccw pair counts, cw_ccw + ccw_cw pair counts) per bin."""
        same = np.zeros(len(THETA_EDGES_DEG) - 1, dtype=np.int64)
        diff = np.zeros(len(THETA_EDGES_DEG) - 1, dtype=np.int64)
        for r_lo, r_hi, i in zip(radii[:-1], radii[1:], range(len(centers_deg))):
            idxs_hi = tree.query_radius(coords, r=r_hi)
            idxs_lo = tree.query_radius(coords, r=r_lo) if r_lo > 0 else None
            for j, hi_nbrs in enumerate(idxs_hi):
                if idxs_lo is not None:
                    nbrs = np.setdiff1d(hi_nbrs, idxs_lo[j], assume_unique=True)
                else:
                    nbrs = hi_nbrs
                nbrs = nbrs[nbrs > j]  # avoid double-counting + self
                if len(nbrs) == 0:
                    continue
                same[i] += int((labels_in[nbrs] == labels_in[j]).sum())
                diff[i] += int((labels_in[nbrs] != labels_in[j]).sum())
        return same, diff

    print(f"[{time.time()-t0:.1f}s] Data pair counts ...", flush=True)
    same_obs, diff_obs = count_pairs(labels)
    total_obs = same_obs + diff_obs
    # w(theta) = (same - diff) / total = 2*same/total - 1; null = 0
    w_obs = np.where(total_obs > 0, (same_obs - diff_obs) / total_obs, 0.0)
    print(f"[{time.time()-t0:.1f}s] Bin centers (deg) + w_obs:", flush=True)
    for c, w, n in zip(centers_deg, w_obs, total_obs):
        print(f"  theta={c:6.3f} deg  w_obs={w:+.4f}  N_pairs={n:>9,}", flush=True)

    print(f"\n[{time.time()-t0:.1f}s] N_MC={N_MC} label-shuffle null ...", flush=True)
    w_null = np.zeros((N_MC, len(centers_deg)))
    for k in range(N_MC):
        labels_shuf = labels.copy()
        rng.shuffle(labels_shuf)
        s, d = count_pairs(labels_shuf)
        total = s + d
        w_null[k] = np.where(total > 0, (s - d) / total, 0.0)
        if (k + 1) % 20 == 0:
            print(f"  MC {k+1}/{N_MC}", flush=True)
    null_mean = w_null.mean(axis=0)
    null_std = w_null.std(axis=0, ddof=1)
    sigma = (w_obs - null_mean) / (null_std + 1e-30)
    print(f"\n[{time.time()-t0:.1f}s] === FINAL w(theta) ===", flush=True)
    for c, w, m, s, sig in zip(centers_deg, w_obs, null_mean, null_std, sigma):
        print(f"  theta={c:6.3f} deg  w_obs={w:+.5f}  null_mean={m:+.5f}  null_std={s:.5f}  sigma={sig:+.2f}", flush=True)

    out = {
        "config": {
            "n_sample": int(N_SAMPLE),
            "n_used": int(len(sub)),
            "n_mc": N_MC,
            "seed": SEED,
            "theta_edges_deg": THETA_EDGES_DEG.tolist(),
            "subsample": "HC-spiral (p_eq > 0.6)",
            "statistic": "w(theta) = (N_same - N_diff) / N_total per angular bin; null = label-shuffle preserving global p_CW",
        },
        "results": {
            "theta_centers_deg": centers_deg.tolist(),
            "w_observed": w_obs.tolist(),
            "w_null_mean": null_mean.tolist(),
            "w_null_std": null_std.tolist(),
            "sigma": sigma.tolist(),
            "n_pairs": total_obs.tolist(),
            "max_abs_sigma_across_bins": float(np.max(np.abs(sigma))),
        },
        "interpretation": (
            "w(theta) > 0 at any scale = primordial CW-CW (or CCW-CCW) clustering, "
            "an observable insensitive to mean-dipole systematics. "
            "max|sigma|<2 across all bins = no detection. "
            "Any bin >3 sigma is the kind of signal that would not be averaged out by "
            "the canonical-mask leakage channel and would constitute a real cosmological finding."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\nSaved -> {OUT}", flush=True)
    print(f"Total wall: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
