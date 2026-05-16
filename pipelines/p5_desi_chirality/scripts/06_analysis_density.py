#!/usr/bin/env python3
"""Analysis B — chirality vs local density.

For each matched spiral, compute a k-nearest-neighbour projected surface
density on the unit sphere (angular distance to k-th nearest spiral), bin
into quantiles, and test for CW/CCW imbalance across quantiles. Controls
for redshift bin (so high-z dilution doesn't masquerade as a density
effect).

This is a *projected* density. A 3D density estimator requires reliable
redshifts and would be the natural follow-up; we leave that for analysis C
once the environmental VAC ingest lands.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_config, resolve_p5_path, ensure_dir, utc_now


def _knn_angular_density(ra_deg: np.ndarray, dec_deg: np.ndarray, k: int) -> np.ndarray:
    """Inverse k-th nearest-neighbour angular separation (a density proxy)."""
    from sklearn.neighbors import BallTree
    coords = np.column_stack([np.deg2rad(dec_deg), np.deg2rad(ra_deg)])
    tree = BallTree(coords, metric="haversine")
    dist, _ = tree.query(coords, k=k + 1)   # 0-th neighbor is self
    kth = dist[:, k]
    kth = np.where(kth <= 0, np.nan, kth)
    return 1.0 / (kth ** 2)


def _quantile_table(density: np.ndarray, labels: np.ndarray, qs: list[float]) -> pd.DataFrame:
    edges = np.quantile(density[np.isfinite(density)], qs)
    bin_idx = np.digitize(density, edges) - 1
    bin_idx = np.clip(bin_idx, 0, len(qs) - 2)
    rows = []
    for i in range(len(qs) - 1):
        m = bin_idx == i
        if not m.any():
            continue
        n = int(m.sum())
        n_cw = int((labels[m] == 1).sum())
        f = n_cw / n
        sigma = (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n > 0 else np.nan
        rows.append({
            "q_low": float(qs[i]), "q_high": float(qs[i + 1]),
            "density_low": float(edges[i]) if i < len(edges) else float("nan"),
            "density_high": float(edges[i + 1]) if (i + 1) < len(edges) else float("nan"),
            "n": n, "n_cw": n_cw, "n_ccw": n - n_cw,
            "cw_fraction": f, "sigma_from_half": sigma,
        })
    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    args = parser.parse_args()
    cfg = load_config(args.config)

    matched_path = resolve_p5_path(cfg["paths"]["out_matched"])
    if not matched_path.exists():
        print(f"ERROR: {matched_path} missing.")
        return 2
    out_dir = ensure_dir(resolve_p5_path("results/analysis_density"))

    df = pd.read_parquet(matched_path)
    df = df[df.get("matched_primary_deduped", df["matched_primary"])]
    sp = df[df["match_class_eq"].isin(["CW", "CCW"])].copy()
    if len(sp) < 100:
        (out_dir / "summary.json").write_text(json.dumps({
            "skipped": True, "reason": "fewer than 100 matched spirals", "n": int(len(sp)),
        }, indent=2))
        return 0

    k = int(cfg["analysis"]["density"]["knn_k"])
    qs = list(cfg["analysis"]["density"]["quantiles"])
    density = _knn_angular_density(sp["desi_ra"].to_numpy(), sp["desi_dec"].to_numpy(), k)
    labels = (sp["match_class_eq"] == "CW").astype(int).to_numpy()

    table = _quantile_table(density, labels, qs)
    table.to_csv(out_dir / "cw_fraction_by_density.csv", index=False)

    # Redshift-controlled: repeat in each redshift slab
    z_edges = list(cfg["analysis"]["redshift_bins"]["edges"])
    z = sp["desi_z"].to_numpy()
    z_bin = np.digitize(z, z_edges) - 1
    z_controlled_rows = []
    for i in range(len(z_edges) - 1):
        m = z_bin == i
        if m.sum() < 200:
            continue
        sub_table = _quantile_table(density[m], labels[m], qs)
        sub_table["z_low"] = z_edges[i]
        sub_table["z_high"] = z_edges[i + 1]
        z_controlled_rows.append(sub_table)
    if z_controlled_rows:
        z_ctrl = pd.concat(z_controlled_rows, ignore_index=True)
        z_ctrl.to_csv(out_dir / "cw_fraction_by_density_and_z.csv", index=False)

    summary = {
        "written_utc": utc_now(),
        "config_version": cfg["version"],
        "knn_k": k,
        "n_spirals": int(len(sp)),
        "max_abs_sigma_global": float(np.nanmax(np.abs(table["sigma_from_half"].to_numpy()))),
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    print(f"[done] wrote {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
