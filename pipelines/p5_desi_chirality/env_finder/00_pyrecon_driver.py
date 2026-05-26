#!/usr/bin/env python3
"""DESI DR1 BAO Zel'dovich reconstruction driver for P5 env_finder.

For each LSS tracer (BGS_BRIGHT, LRG, ELG_LOPnotqso, QSO):
  1. Download clustering data + first N random files from DESI DR1 LSS v1.5.
  2. Load galaxies and randoms, convert to comoving Mpc/h Cartesian using
     Planck18 cosmology.
  3. Apply pyrecon IterativeFFTReconstruction (Zel'dovich + iterative
     bias correction).
  4. Write reconstructed positions per tracer as parquet.

After all tracers complete, concatenate into a single combined parquet
that 02_compute_vweb_recon.py reads.

Designed to run on a CPU-heavy pod (>=96 GB RAM). The compute is
FFT-bound and memory-bound, not GPU-bound.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

DESI_BASE = "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5"
TRACERS = ["BGS_BRIGHT", "LRG", "ELG_LOPnotqso", "QSO"]
N_RANDOM_FILES_PER_REGION = 4  # 4 random files per region; 4 tracers x 2 regions x 4 = 32 total
RECON_BIAS = {
    # Tracer-specific large-scale bias (DESI DR1 BAO paper Adame+ 2024).
    "BGS_BRIGHT": 1.5,
    "LRG": 2.0,
    "ELG_LOPnotqso": 1.2,
    "QSO": 2.1,
}
RECON_FNL = 0.8  # Linear-growth rate at the effective z; OK approximation.


def step(t0, msg):
    print(f"[{time.time()-t0:8.1f}s] {msg}", flush=True)


def sh(cmd, t0, check=True):
    step(t0, f"  $ {cmd}")
    rc = subprocess.run(cmd, shell=True, check=check)
    return rc.returncode


def download_tracer(t0: float, out_dir: Path, tracer: str, n_rand_files: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for region in ["NGC", "SGC"]:
        data = out_dir / f"{tracer}_{region}_clustering.dat.fits"
        if not data.exists():
            sh(f"curl -L -s -o {data} '{DESI_BASE}/{data.name}'", t0)
        else:
            step(t0, f"  exists {data.name}")
        for i in range(n_rand_files):
            ran = out_dir / f"{tracer}_{region}_{i}_clustering.ran.fits"
            if not ran.exists():
                sh(f"curl -L -s -o {ran} '{DESI_BASE}/{ran.name}'", t0)
            else:
                step(t0, f"  exists {ran.name}")


def load_catalog(path: Path) -> pd.DataFrame:
    from astropy.io import fits
    with fits.open(path) as h:
        d = h[1].data
        cols = {c.name: c.name for c in h[1].columns}
        # Required: RA, DEC, Z, TARGETID (data only). Randoms have no TARGETID.
        out = {
            "RA": np.asarray(d["RA"], dtype=np.float64),
            "DEC": np.asarray(d["DEC"], dtype=np.float64),
            "Z": np.asarray(d["Z"], dtype=np.float64),
        }
        if "TARGETID" in cols:
            out["TARGETID"] = np.asarray(d["TARGETID"], dtype=np.int64)
        if "WEIGHT" in cols:
            out["WEIGHT"] = np.asarray(d["WEIGHT"], dtype=np.float64)
        else:
            out["WEIGHT"] = np.ones(len(d), dtype=np.float64)
    return pd.DataFrame(out)


def to_cartesian(df: pd.DataFrame) -> np.ndarray:
    from astropy.cosmology import Planck18
    chi_mpc = Planck18.comoving_distance(df["Z"].values).value
    h = Planck18.H0.value / 100.0
    chi = (chi_mpc * h).astype(np.float64)
    ra = np.deg2rad(df["RA"].values)
    dec = np.deg2rad(df["DEC"].values)
    cd = np.cos(dec)
    pos = np.empty((len(df), 3), dtype=np.float64)
    pos[:, 0] = chi * cd * np.cos(ra)
    pos[:, 1] = chi * cd * np.sin(ra)
    pos[:, 2] = chi * np.sin(dec)
    return pos


def run_pyrecon_tracer(t0: float, tracer: str, lss_dir: Path, out_dir: Path, n_rand_files: int) -> Path:
    out_path = out_dir / f"desi_recon_{tracer}.parquet"
    if out_path.exists():
        step(t0, f"  exists {out_path.name} — skipping pyrecon for {tracer}")
        return out_path

    step(t0, f"=== pyrecon for {tracer} ===")
    # Load galaxies (NGC + SGC concatenated).
    dfs = []
    for region in ["NGC", "SGC"]:
        df = load_catalog(lss_dir / f"{tracer}_{region}_clustering.dat.fits")
        df["REGION"] = region
        dfs.append(df)
    galaxies = pd.concat(dfs, ignore_index=True)
    step(t0, f"  galaxies: {len(galaxies):,} (NGC + SGC combined)")

    # Load randoms (concatenate all files across regions).
    r_dfs = []
    for region in ["NGC", "SGC"]:
        for i in range(n_rand_files):
            rp = lss_dir / f"{tracer}_{region}_{i}_clustering.ran.fits"
            r = load_catalog(rp)
            r_dfs.append(r)
    randoms = pd.concat(r_dfs, ignore_index=True)
    step(t0, f"  randoms: {len(randoms):,} ({n_rand_files * 2} files)")

    gal_pos = to_cartesian(galaxies)
    ran_pos = to_cartesian(randoms)

    from pyrecon import IterativeFFTReconstruction
    bias = RECON_BIAS[tracer]
    f_growth = RECON_FNL
    # Tracer-specific: use a 1024 grid covering both regions.
    all_pos = np.vstack([gal_pos, ran_pos])
    mins = all_pos.min(axis=0) - 50.0
    maxs = all_pos.max(axis=0) + 50.0
    boxsize = float((maxs - mins).max())
    boxcenter = (mins + maxs) / 2.0
    step(t0, f"  pyrecon: bias={bias} f={f_growth} boxsize={boxsize:.1f} Mpc/h boxcenter={boxcenter}")
    recon = IterativeFFTReconstruction(
        f=f_growth,
        bias=bias,
        boxsize=boxsize,
        boxcenter=tuple(boxcenter),
        nmesh=1024,
        los="local",
        positions=ran_pos,
        dtype="f8",
    )
    recon.assign_data(gal_pos, weights=galaxies["WEIGHT"].values)
    recon.assign_randoms(ran_pos, weights=randoms["WEIGHT"].values)
    recon.set_density_contrast(smoothing_radius=15.0)  # 15 Mpc/h standard for DESI BAO
    recon.run()
    gal_recon = recon.read_shifted_positions(gal_pos)
    step(t0, f"  pyrecon done; displacement RMS = {np.linalg.norm(gal_recon - gal_pos, axis=1).mean():.2f} Mpc/h")

    out_df = pd.DataFrame({
        "TARGETID": galaxies["TARGETID"].values,
        "TRACER": tracer,
        "RECON_X": gal_recon[:, 0].astype(np.float32),
        "RECON_Y": gal_recon[:, 1].astype(np.float32),
        "RECON_Z": gal_recon[:, 2].astype(np.float32),
        "RSD_X": gal_pos[:, 0].astype(np.float32),
        "RSD_Y": gal_pos[:, 1].astype(np.float32),
        "RSD_Z": gal_pos[:, 2].astype(np.float32),
        "REGION": galaxies["REGION"].values,
        "Z_orig": galaxies["Z"].astype(np.float32).values,
        "WEIGHT": galaxies["WEIGHT"].astype(np.float32).values,
    })
    out_df.to_parquet(out_path, index=False)
    step(t0, f"  wrote {out_path}")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lss-dir", default="/workspace/desi_lss_v1p5", help="DESI LSS catalog dir")
    parser.add_argument("--out-dir", default="/workspace/desi_recon", help="output dir for per-tracer + combined parquets")
    parser.add_argument("--n-rand-files", type=int, default=N_RANDOM_FILES_PER_REGION)
    parser.add_argument("--tracers", nargs="+", default=TRACERS)
    args = parser.parse_args()
    t0 = time.time()

    lss_dir = Path(args.lss_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    step(t0, f"DESI DR1 BAO Zel'dovich reconstruction driver")
    step(t0, f"  LSS catalogs dir: {lss_dir}")
    step(t0, f"  output dir: {out_dir}")
    step(t0, f"  tracers: {args.tracers}")
    step(t0, f"  random files per region: {args.n_rand_files}")

    # Phase 1: download.
    step(t0, "Phase 1: download")
    for tracer in args.tracers:
        download_tracer(t0, lss_dir, tracer, args.n_rand_files)

    # Phase 2: pyrecon per tracer.
    step(t0, "Phase 2: pyrecon per tracer")
    tracer_parquets = []
    for tracer in args.tracers:
        p = run_pyrecon_tracer(t0, tracer, lss_dir, out_dir, args.n_rand_files)
        tracer_parquets.append(p)

    # Phase 3: concatenate.
    step(t0, "Phase 3: concatenate tracers")
    dfs = [pd.read_parquet(p) for p in tracer_parquets]
    combined = pd.concat(dfs, ignore_index=True)
    combined_path = out_dir / "desi_recon_combined.parquet"
    combined.to_parquet(combined_path, index=False)
    step(t0, f"  wrote {combined_path}: {len(combined):,} rows across {len(args.tracers)} tracers")

    # Summary
    summary = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "wall_seconds": time.time() - t0,
        "tracers": args.tracers,
        "n_rand_files_per_region": args.n_rand_files,
        "combined_rows": int(len(combined)),
        "per_tracer_rows": {t: int((combined["TRACER"] == t).sum()) for t in args.tracers},
        "recon_bias_per_tracer": {t: RECON_BIAS[t] for t in args.tracers},
        "recon_f_growth": RECON_FNL,
    }
    summary_path = out_dir / "pyrecon_summary.json"
    with summary_path.open("w") as fh:
        json.dump(summary, fh, indent=2)
    step(t0, f"  wrote {summary_path}")
    step(t0, "DONE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
