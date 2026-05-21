#!/usr/bin/env python3
"""P5 paper figure: HEALPix per-pixel chirality σ-residual sky map at NSIDE=32.

The healpix scan reported in §VI.D (Table~II) finds max|σ|^obs = 4.13 at
NSIDE=32 with label-shuffle null max|σ|^p99 = 4.78 (p = 0.135), consistent
with the look-elsewhere null distribution. This figure renders the
per-pixel signed σ_from_half as a Mollweide projection so reviewers can
see the spatial distribution directly: no coherent large-scale structure
should be visible if the chirality field is environment-independent.

Input:
    pipelines/p5_desi_chirality/results/analysis_healpix/nside32_cw_per_pixel.csv

Output:
    pipelines/p5_desi_chirality/figures/fig_p5_healpix_skymap_nside32.png
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import healpy as hp

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
P5 = REPO / "pipelines/p5_desi_chirality"
SRC = P5 / "results/analysis_healpix/nside32_cw_per_pixel.csv"
OUT = P5 / "figures/fig_p5_healpix_skymap_nside32.png"

NSIDE = 32


def main() -> int:
    df = pd.read_csv(SRC)
    npix = hp.nside2npix(NSIDE)
    sigma_map = np.full(npix, hp.UNSEEN, dtype=np.float64)
    n_map = np.zeros(npix, dtype=np.float64)
    for _, r in df.iterrows():
        sigma_map[int(r["pix"])] = float(r["sigma_from_half"])
        n_map[int(r["pix"])] = float(r["n"])

    # Use diverging colormap centered on 0
    vmax = 4.5  # caps near the observed max |σ|
    fig = plt.figure(figsize=(11.2, 5.6))
    hp.mollview(
        sigma_map,
        title="P5 HEALPix per-pixel $\\sigma_{\\rm from\\,half}$ (NSIDE=32, $n_{\\rm pix}=3{,}303$)\n"
              "label-shuffle null $p\\!=\\!0.135$; obs $|\\sigma|_{\\max}\\!=\\!4.13$ "
              "vs null $|\\sigma|_{\\max}^{\\rm p99}\\!=\\!4.78$",
        cmap="RdBu_r",
        min=-vmax,
        max=+vmax,
        unit="$\\sigma_{\\rm from\\,half}$",
        cbar=True,
        notext=False,
        coord=["C"],  # equatorial
        fig=fig.number,
    )
    hp.graticule(dpar=30, dmer=60, color="#888888", alpha=0.4, lw=0.4)
    fig.savefig(OUT, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
