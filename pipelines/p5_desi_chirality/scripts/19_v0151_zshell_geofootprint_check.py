#!/usr/bin/env python3
"""P5 v0.1.51 wave compute C6 / META-M4 — geometry-footprint shell-mean check.

The z-shell selection-corrected rebuild (scripts/16_*) computes each shell's
mean density over the OCCUPANCY-DERIVED footprint (dilated occupied cells in
that shell). META-M4 (R22prov) notes that an occupancy-conditioned denominator
can bias shell means relative to a survey-geometry (random/HEALPix-based)
denominator, especially in sparse high-z shells.

This script re-runs the z-shell rebuild with ONE change: the per-shell mean
is taken over a GEOMETRY-DEFINED footprint — cells whose angular direction
falls in the survey's redshift-independent HEALPix footprint (NSIDE=64 pixels
containing >= 1 filtered DR1 galaxy at any z) and whose cell-centre chi lies
in the shell. This denominator is the grid-cell equivalent of an unclustered
random catalog filling the survey geometry per shell. Grid, R_s, lambda_th,
shell scheme, smoothing, classification, interpolation, and the spiral join
are identical to scripts/16_*.

Output: pipelines/p5_desi_chirality/outputs/19_v0151_zshell_geofootprint_check.json
"""
from __future__ import annotations

import importlib.util
import json
import sys
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import yaml
from astropy.cosmology import Planck18
from scipy.ndimage import binary_dilation

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

# import shell scheme + helpers from script 16 (module name starts with digit)
_spec = importlib.util.spec_from_file_location(
    "zshell16", P5 / "scripts/16_cosmic_web_zshell_corrected.py")
_m16 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m16)

Z_EDGES = _m16.Z_EDGES
NSIDE_FOOT = 64
OUT = P5 / "outputs/19_v0151_zshell_geofootprint_check.json"


def main() -> int:
    t0 = time.time()
    cfg = yaml.safe_load(open(P5 / "env_finder/config.yaml"))
    N = int(cfg["grid"]["n"])
    pad = float(cfg["grid"]["bounding_box_pad_mpc_h"])
    R_s = float(cfg["smoothing"]["R_s_mpc_h"])
    lambda_th = float(cfg["classify"]["lambda_th"])

    df = _m16.load_filtered_zall(cfg, t0)
    pos = _m16.comoving_xyz_mpc_h(df["Z"].values, df["TARGET_RA"].values,
                                  df["TARGET_DEC"].values, t0)
    mins = pos.min(axis=0) - pad
    maxs = pos.max(axis=0) + pad
    box_side = float(np.max(maxs - mins))
    origin = mins.astype(np.float32)
    cell_size = box_side / N

    count = cic_deposit(pos, origin, cell_size, N, t0)

    # geometry footprint: NSIDE=64 pixels with >=1 galaxy at ANY redshift
    step(t0, "Building z-independent angular footprint (HEALPix NSIDE=64) ...")
    gal_pix = hp.ang2pix(NSIDE_FOOT, df["TARGET_RA"].values,
                         df["TARGET_DEC"].values, lonlat=True)
    foot_map = np.zeros(hp.nside2npix(NSIDE_FOOT), dtype=bool)
    foot_map[np.unique(gal_pix)] = True
    step(t0, f"  footprint pixels: {int(foot_map.sum()):,} "
             f"({100*foot_map.mean():.1f}% of sky)")

    # per-cell chi + angular pixel
    step(t0, "Cell-centre chi + HEALPix pixel for all cells ...")
    ax = (origin[:, None]
          + (np.arange(N, dtype=np.float32) + 0.0)[None, :] * np.float32(cell_size))
    X = np.broadcast_to(ax[0][:, None, None], (N, N, N))
    Y = np.broadcast_to(ax[1][None, :, None], (N, N, N))
    Z = np.broadcast_to(ax[2][None, None, :], (N, N, N))
    chi_cell = np.sqrt(X.astype(np.float64) ** 2 + Y.astype(np.float64) ** 2
                       + Z.astype(np.float64) ** 2)
    with np.errstate(invalid="ignore"):
        cell_pix = hp.vec2pix(NSIDE_FOOT,
                              X.ravel().astype(np.float64),
                              Y.ravel().astype(np.float64),
                              Z.ravel().astype(np.float64)).reshape(N, N, N)
    in_foot = foot_map[cell_pix]
    del X, Y, Z, cell_pix

    h = Planck18.H0.value / 100.0
    chi_edges = (Planck18.comoving_distance(Z_EDGES).value * h).astype(np.float64)
    n_shells = len(Z_EDGES) - 1
    shell_idx = np.clip(np.digitize(chi_cell, chi_edges) - 1, 0,
                        n_shells - 1).astype(np.int16)
    in_range = (chi_cell >= chi_edges[0]) & (chi_cell <= chi_edges[-1])
    del chi_cell
    mask_geo = in_foot & in_range

    # occupancy-dilated mask (canonical) — for comparison reporting only
    occupied = count > 0
    dil = int(np.ceil(R_s / cell_size)) + 1
    mask_occ = binary_dilation(occupied, iterations=dil)

    step(t0, "Per-shell means over GEOMETRY footprint cells ...")
    delta = np.zeros((N, N, N), dtype=np.float32)
    shells = []
    for s in range(n_shells):
        sel = mask_geo & (shell_idx == s)
        n_cells = int(sel.sum())
        if n_cells == 0:
            continue
        nbar_geo = float(count[sel].mean())
        sel_occ = mask_occ & (shell_idx == s)
        nbar_occ = float(count[sel_occ].mean()) if sel_occ.any() else None
        delta[sel] = (count[sel] / np.float32(nbar_geo) - 1.0).astype(np.float32)
        shells.append({"shell": s, "z_lo": float(Z_EDGES[s]),
                       "z_hi": float(Z_EDGES[s + 1]),
                       "n_cells_geo": n_cells,
                       "nbar_geo": nbar_geo,
                       "nbar_occupancy_mask": nbar_occ})
        step(t0, f"  shell {s:2d} cells={n_cells:>9,} nbar_geo={nbar_geo:9.4f} "
                 f"nbar_occ={nbar_occ if nbar_occ is None else round(nbar_occ,4)}")
    n_mask_geo = int(mask_geo.sum())
    del count, mask_occ, occupied, in_foot, in_range

    delta_smooth, KX, KY, KZ, k2 = gaussian_smooth_fft(delta, cell_size, R_s, t0)
    del delta
    l1, l2, l3 = tidal_eigenvalues(delta_smooth, KX, KY, KZ, k2, t0)
    del KX, KY, KZ, k2
    log1pd = np.log10(np.maximum(1.0 + delta_smooth, 1e-6)).astype(np.float32)
    del delta_smooth
    cell_class = classify_vweb(l1, l2, l3, lambda_th)
    vol_fracs = {ENV_CLASSES[i]:
                 float(((cell_class == i) & mask_geo).sum()) / max(n_mask_geo, 1)
                 for i in range(4)}
    step(t0, f"Geometry-footprint volume fractions: {vol_fracs}")

    interp = interpolate_to_galaxies(pos, origin, cell_size, N, cell_class,
                                     log1pd, (l1, l2, l3))
    del l1, l2, l3, log1pd
    env_df = pd.DataFrame({
        "TARGETID": df["TARGETID"].values,
        "env_class": pd.Categorical.from_codes(interp["env_class_idx"],
                                               categories=ENV_CLASSES),
    })

    step(t0, "Spiral join (08 contract) ...")
    matched = pq.read_table(str(P5 / "results/p5_matched_chirality_desi.parquet"),
                            columns=["desi_targetid", "match_class_eq",
                                     "matched_primary_deduped"]).to_pandas()
    matched = matched[matched["matched_primary_deduped"]]
    j = matched.merge(env_df, left_on="desi_targetid", right_on="TARGETID",
                      how="inner")
    j = j[j["match_class_eq"].isin(["CW", "CCW"])]
    tab = _m16.env_table(j, "env_class")

    art16 = json.loads((P5 / "outputs/16_cosmic_web_zshell_corrected.json")
                       .read_text())
    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/19_v0151_zshell_geofootprint_check.py",
        "closes": ["META-M4(C6)"],
        "method": {
            "footprint": f"HEALPix NSIDE={NSIDE_FOOT} pixels with >=1 filtered "
                         "DR1 galaxy at any z, intersected with shell chi range",
            "n_mask_cells_geo": n_mask_geo,
            "grid_n": N, "R_s_mpc_h": R_s, "lambda_th": lambda_th,
            "shell_scheme": "identical to scripts/16",
        },
        "shells": shells,
        "volume_fractions_geo": vol_fracs,
        "cw_fraction_by_env_geo_footprint": tab,
        "cw_fraction_by_env_occupancy_mask_reference":
            art16["cw_fraction_by_env"]["zshell_corrected"],
        "runtime_seconds": round(time.time() - t0, 1),
    }
    OUT.write_text(json.dumps(out, indent=2))
    step(t0, f"[done] wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
