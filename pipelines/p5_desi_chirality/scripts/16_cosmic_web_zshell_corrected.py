#!/usr/bin/env python3
"""P5 fire-21 P5-META-E1 + E2 — selection-function-corrected V-Web classifier.

Addresses two ESSENTIAL review findings against the canonical run
(env_finder/01_compute_vweb.py, provenance env_finder-vweb-v0.1-8e6f138179b6):

  E1  The canonical run used a SINGLE GLOBAL mean density over the whole
      0.01 <= z <= 2 volume (rho_mean ~ 4.64 gal/cell in the dilated
      footprint mask), so delta = rho/rho_mean - 1 tracks the radial
      selection function n(z) rather than true large-scale structure:
      distant shells look like "voids" because DESI detects fewer
      galaxies there, not because they are underdense.
      FIX: compute the mean in THIN REDSHIFT SHELLS over occupied-footprint
      cells in that shell only; delta_shell = n_cell / nbar_shell - 1.

  E2  Masked/empty regions enter the periodic FFT; the canonical run set
      them to delta = 0 (mean density), which still leaks into the
      smoothed field near the footprint edge.
      FIX: interior buffer — flag galaxies within R_s of the survey
      footprint boundary (accounting for the mask-dilation distance) and
      report results BOTH with and without the buffer cut.

Everything else (grid N=256, R_s=25 Mpc/h, lambda_th=0.0, CIC, Gaussian
k-space smoothing, Poisson inversion, tidal eigenvalues, 4-class V-Web,
NN interpolation, join contract with script 08) is kept IDENTICAL to the
canonical run so the comparison is apples-to-apples.

Shell scheme (chosen from the actual filtered n(z), see report):
  dz = 0.05 for 0.01 <= z < 0.50   (10 shells, min count 216k at 0.01-0.05)
  dz = 0.10 for 0.50 <= z < 1.50   (10 shells)
  one merged shell 1.50 <= z <= 1.70 (323k; the raw 1.60-1.70 bin alone has
      only 82k < 200k, so it is merged with 1.50-1.60)
  All 21 shells contain >= 216k galaxies (>= 200k criterion satisfied).
  No galaxies beyond z = 1.6964 in the filtered sample.

Outputs (no .tex edits, no git):
  data/desi_env/desi_env_vweb_zshell.parquet           per-galaxy labels
  outputs/16_cosmic_web_zshell_corrected.json           full numeric results
  outputs/16_cosmic_web_zshell_corrected.md             summary table
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import yaml
from astropy.cosmology import Planck18
from scipy.ndimage import binary_dilation, distance_transform_edt

REPO_ROOT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
P5 = REPO_ROOT / "pipelines/p5_desi_chirality"
sys.path.insert(0, str(P5 / "env_finder"))
from _compute_vweb_lib import (  # noqa: E402
    ENV_CLASSES,
    cic_deposit,
    classify_vweb,
    gaussian_smooth_fft,
    interpolate_to_galaxies,
    step,
    tidal_eigenvalues,
)

CONFIG_PATH = P5 / "env_finder/config.yaml"
CANONICAL_ENV = P5 / "data/desi_env/desi_env_vweb.parquet"
MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
OUT_DIR = P5 / "outputs"
OUT_ENV_PARQUET = P5 / "data/desi_env/desi_env_vweb_zshell.parquet"

# --- shell scheme (see module docstring) ---
Z_EDGES = np.concatenate([
    np.array([0.01]),
    np.arange(0.05, 0.50 + 1e-9, 0.05),   # 0.05 .. 0.50
    np.arange(0.60, 1.50 + 1e-9, 0.10),   # 0.60 .. 1.50
    np.array([1.70]),
])  # 22 edges -> 21 shells


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_filtered_zall(cfg, t0):
    p = REPO_ROOT / cfg["input"]["zall_path"]
    step(t0, f"Loading {p.name} ...")
    cols = ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z", "ZWARN", "SPECTYPE"]
    df = pq.read_table(str(p), columns=cols).to_pandas()
    f = cfg["input"]["filter"]
    mask = (
        (df["ZWARN"] == f["zwarn_max"])
        & (df["SPECTYPE"].astype(str).str.strip() == f["spectype"])
        & (df["Z"] > f["z_min"])
        & (df["Z"] < f["z_max"])
    )
    df = df.loc[mask, ["TARGETID", "TARGET_RA", "TARGET_DEC", "Z"]].reset_index(drop=True)
    step(t0, f"  filtered rows: {len(df):,}")
    return df


def comoving_xyz_mpc_h(z, ra_deg, dec_deg, t0):
    step(t0, "Comoving Cartesian positions (Planck18, Mpc/h) ...")
    chi = (Planck18.comoving_distance(z).value * (Planck18.H0.value / 100.0)).astype(np.float32)
    ra = np.deg2rad(ra_deg).astype(np.float32)
    dec = np.deg2rad(dec_deg).astype(np.float32)
    cd = np.cos(dec)
    pos = np.empty((len(z), 3), dtype=np.float32)
    pos[:, 0] = chi * cd * np.cos(ra)
    pos[:, 1] = chi * cd * np.sin(ra)
    pos[:, 2] = chi * np.sin(dec)
    return pos


def env_table(joined_spirals: pd.DataFrame, label_col: str) -> list[dict]:
    """Per-environment CW-fraction table, identical statistic to script 08."""
    n_tot = len(joined_spirals)
    ncw_tot = int((joined_spirals["match_class_eq"] == "CW").sum())
    fbar = ncw_tot / n_tot
    rows = []
    for cls in ENV_CLASSES:
        sub = joined_spirals[joined_spirals[label_col] == cls]
        n = len(sub)
        n_cw = int((sub["match_class_eq"] == "CW").sum())
        f = n_cw / n if n else float("nan")
        sigma_half = (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n else float("nan")
        # sigma relative to the sample's own monopole (P4 monopole carried over)
        sigma_mono = ((n_cw - fbar * n) / np.sqrt(n * fbar * (1 - fbar))) if n else float("nan")
        rows.append({
            "env_class": cls, "n": int(n), "n_cw": n_cw, "n_ccw": int(n - n_cw),
            "cw_fraction": float(f),
            "sigma_from_half": float(sigma_half),
            "sigma_from_sample_monopole": float(sigma_mono),
        })
    rows.append({
        "env_class": "ALL", "n": int(n_tot), "n_cw": ncw_tot, "n_ccw": int(n_tot - ncw_tot),
        "cw_fraction": float(fbar),
        "sigma_from_half": float((ncw_tot - 0.5 * n_tot) / (0.5 * np.sqrt(n_tot))),
        "sigma_from_sample_monopole": 0.0,
    })
    return rows


def main() -> int:
    t0 = time.time()
    cfg = yaml.safe_load(open(CONFIG_PATH))
    N = int(cfg["grid"]["n"])
    pad = float(cfg["grid"]["bounding_box_pad_mpc_h"])
    R_s = float(cfg["smoothing"]["R_s_mpc_h"])
    lambda_th = float(cfg["classify"]["lambda_th"])
    step(t0, f"Config: N={N} pad={pad} R_s={R_s} lambda_th={lambda_th} (IDENTICAL to canonical)")

    # 1. Load + positions + box (identical to canonical).
    df = load_filtered_zall(cfg, t0)
    pos = comoving_xyz_mpc_h(df["Z"].values, df["TARGET_RA"].values, df["TARGET_DEC"].values, t0)
    mins = pos.min(axis=0) - pad
    maxs = pos.max(axis=0) + pad
    box_side = float(np.max(maxs - mins))
    origin = mins.astype(np.float32)
    cell_size = box_side / N
    step(t0, f"Box side {box_side:.1f} Mpc/h; cell {cell_size:.3f} Mpc/h")

    # 2. CIC + footprint mask (identical to canonical).
    count = cic_deposit(pos, origin, cell_size, N, t0)
    occupied = count > 0
    dilate_radius_cells = int(np.ceil(R_s / cell_size)) + 1
    mask = binary_dilation(occupied, iterations=dilate_radius_cells)
    n_mask = int(mask.sum())
    rho_mean_global = float(count[mask].mean())
    step(t0, f"Mask: {n_mask:,} cells ({100*n_mask/mask.size:.1f}%); "
             f"global rho_mean (canonical) = {rho_mean_global:.3f} gal/cell")

    # 3. Per-cell comoving distance -> redshift shell index.
    step(t0, "Assigning cells to redshift shells via cell-center chi ...")
    ax = (origin[:, None] + np.arange(N, dtype=np.float32)[None, :] * np.float32(cell_size))
    x2 = (ax[0] ** 2)[:, None, None]
    y2 = (ax[1] ** 2)[None, :, None]
    z2 = (ax[2] ** 2)[None, None, :]
    chi_cell = np.sqrt(x2 + y2 + z2).astype(np.float32)
    h = Planck18.H0.value / 100.0
    chi_edges = (Planck18.comoving_distance(Z_EDGES).value * h).astype(np.float64)
    n_shells = len(Z_EDGES) - 1
    # digitize: shell s covers [chi_edges[s], chi_edges[s+1]); clamp outside cells
    shell_idx = np.clip(np.digitize(chi_cell, chi_edges) - 1, 0, n_shells - 1).astype(np.int16)
    del x2, y2, z2, chi_cell

    # 4. Per-shell footprint-aware mean + shell-normalised delta.
    step(t0, "Computing per-shell means over in-mask cells ...")
    delta = np.zeros((N, N, N), dtype=np.float32)
    shell_report = []
    # galaxy shell counts for the report
    gal_shell = np.clip(np.digitize(df["Z"].values, Z_EDGES) - 1, 0, n_shells - 1)
    for s in range(n_shells):
        sel = mask & (shell_idx == s)
        n_cells = int(sel.sum())
        if n_cells == 0:
            shell_report.append({"shell": s, "z_lo": float(Z_EDGES[s]), "z_hi": float(Z_EDGES[s + 1]),
                                 "n_mask_cells": 0, "nbar_shell": None, "n_galaxies": 0})
            continue
        nbar = float(count[sel].mean())
        delta[sel] = (count[sel] / np.float32(nbar) - 1.0).astype(np.float32)
        n_gal = int((gal_shell == s).sum())
        shell_report.append({
            "shell": s, "z_lo": float(Z_EDGES[s]), "z_hi": float(Z_EDGES[s + 1]),
            "n_mask_cells": n_cells, "nbar_shell": nbar, "n_galaxies": n_gal,
        })
        step(t0, f"  shell {s:2d} z=[{Z_EDGES[s]:.2f},{Z_EDGES[s+1]:.2f}) "
                 f"cells={n_cells:>9,} nbar={nbar:9.4f} gal={n_gal:>9,}")
    del count

    # 5. Smooth -> tidal eigenvalues -> classify (library code, identical params).
    delta_smooth, KX, KY, KZ, k2 = gaussian_smooth_fft(delta, cell_size, R_s, t0)
    del delta
    l1, l2, l3 = tidal_eigenvalues(delta_smooth, KX, KY, KZ, k2, t0)
    del KX, KY, KZ, k2
    log1pd_cell = np.log10(np.maximum(1.0 + delta_smooth, 1e-6)).astype(np.float32)
    del delta_smooth
    cell_class = classify_vweb(l1, l2, l3, lambda_th)

    vol_fracs = {ENV_CLASSES[i]: float(((cell_class == i) & mask).sum()) / max(n_mask, 1)
                 for i in range(4)}
    step(t0, f"In-footprint volume fractions (corrected): {vol_fracs}")

    # 6. Interior buffer (E2): distance of each in-mask cell to the mask
    # exterior. The mask was dilated dilate_radius_cells beyond the occupied
    # footprint, so a galaxy within R_s of the TRUE footprint boundary sits
    # within (dilation + R_s) of the mask exterior.
    step(t0, "Distance transform for interior buffer ...")
    edt_cells = distance_transform_edt(mask).astype(np.float32)
    buffer_thresh_mpc_h = dilate_radius_cells * cell_size + R_s
    cell_buffer = (edt_cells * np.float32(cell_size)) <= np.float32(buffer_thresh_mpc_h)
    step(t0, f"  buffer threshold = {buffer_thresh_mpc_h:.1f} Mpc/h "
             f"({buffer_thresh_mpc_h/cell_size:.2f} cells); "
             f"{int((cell_buffer & mask).sum()):,} in-mask cells flagged")

    # 7. NN interpolation to galaxies (identical to canonical).
    step(t0, "Interpolating to galaxies ...")
    interp = interpolate_to_galaxies(pos, origin, cell_size, N, cell_class,
                                     log1pd_cell, (l1, l2, l3))
    u = (pos - origin) / cell_size
    idx = np.clip(np.floor(u + 0.5).astype(np.int64), 0, N - 1)
    gal_buffer = cell_buffer[idx[:, 0], idx[:, 1], idx[:, 2]]
    del u, idx, l1, l2, l3, cell_buffer, edt_cells, log1pd_cell

    env_class_str = pd.Categorical.from_codes(interp["env_class_idx"], categories=ENV_CLASSES)
    out_df = pd.DataFrame({
        "TARGETID": df["TARGETID"].values,
        "env_class": env_class_str,
        "env_density": interp["env_density"].astype(np.float64),
        "near_boundary_Rs": gal_buffer.astype(bool),
        "vac_provenance": np.full(len(df), "env_finder-vweb-zshell-v0.1", dtype=object),
    })
    OUT_ENV_PARQUET.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_parquet(OUT_ENV_PARQUET, index=False)
    step(t0, f"Wrote {OUT_ENV_PARQUET.name} ({len(out_df):,} rows)")

    # 8. Migration matrix vs canonical labels (row-aligned; verify TARGETIDs).
    step(t0, "Loading canonical env labels for migration matrix ...")
    canon = pq.read_table(str(CANONICAL_ENV), columns=["TARGETID", "env_class"]).to_pandas()
    assert len(canon) == len(out_df), "canonical/corrected row count mismatch"
    assert np.array_equal(canon["TARGETID"].values, out_df["TARGETID"].values), \
        "canonical/corrected TARGETID order mismatch — cannot align"
    mig = pd.crosstab(canon["env_class"].astype(str), out_df["env_class"].astype(str))
    mig = mig.reindex(index=ENV_CLASSES, columns=ENV_CLASSES, fill_value=0)
    step(t0, f"Migration matrix (rows=canonical, cols=corrected):\n{mig}")

    # 9. Chirality-by-environment join, EXACTLY as script 08 does it.
    step(t0, "Joining matched spiral catalog (08 join contract) ...")
    matched = pq.read_table(str(MATCHED), columns=[
        "desi_targetid", "match_class_eq", "matched_primary", "matched_primary_deduped",
    ]).to_pandas()
    matched = matched[matched["matched_primary_deduped"]]

    def join_table(env_df: pd.DataFrame, label_col: str = "env_class"):
        j = matched.merge(env_df, left_on="desi_targetid", right_on="TARGETID", how="inner")
        return j[j["match_class_eq"].isin(["CW", "CCW"])]

    sp_canon = join_table(canon)
    sp_corr = join_table(out_df[["TARGETID", "env_class", "near_boundary_Rs"]])
    sp_corr_buf = sp_corr[~sp_corr["near_boundary_Rs"]]
    step(t0, f"Spirals joined: canonical={len(sp_canon):,} corrected={len(sp_corr):,} "
             f"corrected+buffer={len(sp_corr_buf):,}")

    tab_canon = env_table(sp_canon, "env_class")
    tab_corr = env_table(sp_corr, "env_class")
    tab_buf = env_table(sp_corr_buf, "env_class")

    runtime_s = time.time() - t0
    result = {
        "written_utc": utc_now(),
        "script": "scripts/16_cosmic_web_zshell_corrected.py",
        "closes_findings": ["P5-META-E1 (radial selection in global mean)",
                            "P5-META-E2 (mask leakage / FFT boundary)"],
        "method": {
            "grid_n": N, "cell_size_mpc_h": cell_size, "box_side_mpc_h": box_side,
            "R_s_mpc_h": R_s, "lambda_th": lambda_th,
            "dilate_radius_cells": dilate_radius_cells,
            "global_rho_mean_canonical_ref": rho_mean_global,
            "shell_scheme": "dz=0.05 for z<0.5; dz=0.10 for 0.5<=z<1.5; merged 1.5-1.7",
            "n_shells": n_shells,
            "buffer_threshold_mpc_h": buffer_thresh_mpc_h,
            "buffer_definition": "galaxy cell within (dilation + R_s) of mask exterior "
                                 "== within R_s of true occupancy-footprint boundary",
        },
        "shells": shell_report,
        "volume_fractions_in_footprint_corrected": vol_fracs,
        "migration_matrix_all_galaxies": {
            "rows_canonical_cols_corrected": ENV_CLASSES,
            "counts": mig.values.tolist(),
        },
        "spiral_counts": {"canonical": len(sp_canon), "corrected": len(sp_corr),
                          "corrected_buffer": len(sp_corr_buf)},
        "cw_fraction_by_env": {
            "canonical_recomputed": tab_canon,
            "zshell_corrected": tab_corr,
            "zshell_corrected_buffer_cut": tab_buf,
        },
        "runtime_seconds": runtime_s,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_json = OUT_DIR / "16_cosmic_web_zshell_corrected.json"
    out_json.write_text(json.dumps(result, indent=2))
    step(t0, f"Wrote {out_json}")

    # Markdown summary.
    def md_table(rows):
        lines = ["| env | n | f_CW | sigma(0.5) | sigma(monopole) |",
                 "|---|---|---|---|---|"]
        for r in rows:
            lines.append(f"| {r['env_class']} | {r['n']:,} | {r['cw_fraction']:.4f} "
                         f"| {r['sigma_from_half']:+.2f} | {r['sigma_from_sample_monopole']:+.2f} |")
        return "\n".join(lines)

    md = [
        "# 16 — z-shell selection-corrected cosmic-web chirality test",
        f"_Generated {utc_now()} · runtime {runtime_s:.0f}s · closes P5-META-E1/E2_",
        "",
        f"Shell scheme: {result['method']['shell_scheme']} ({n_shells} shells, all >=216k galaxies).",
        f"Grid/smoothing/threshold identical to canonical: N={N}, R_s={R_s} Mpc/h, lambda_th={lambda_th}.",
        f"Buffer cut: galaxies within {buffer_thresh_mpc_h:.0f} Mpc/h of mask exterior "
        f"(= R_s of occupancy boundary).",
        "",
        "## Migration matrix (all 14.6M galaxies; rows=canonical, cols=corrected)",
        "",
        "| canonical \\ corrected | " + " | ".join(ENV_CLASSES) + " |",
        "|---|" + "---|" * len(ENV_CLASSES),
        *(f"| {c} | " + " | ".join(f"{mig.values[i, j]:,}" for j in range(4)) + " |"
          for i, c in enumerate(ENV_CLASSES)),
        "",
        "## Canonical (recomputed)",
        md_table(tab_canon),
        "",
        "## z-shell corrected",
        md_table(tab_corr),
        "",
        "## z-shell corrected + interior buffer cut",
        md_table(tab_buf),
        "",
    ]
    (OUT_DIR / "16_cosmic_web_zshell_corrected.md").write_text("\n".join(md))
    step(t0, "DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
