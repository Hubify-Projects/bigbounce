#!/usr/bin/env python3
"""P5 paper figure: HEALPix per-pixel chirality σ-residual sky map at NSIDE=32.

Two-panel figure (reader-label correction, v0.1.129):
  (a) TOP panel  — matched-spiral count per pixel (sequential
      YlOrRd colormap; integer colorbar ticks)
  (b) BOTTOM panel — per-pixel signed σ_from_half (diverging RdBu_r;
      labeled "Chirality σ_from_half per pixel")

Each panel is rendered with a fresh plt state (all figures closed between
calls) so the healpy "figure already exists" conflict never arises.
The two PNGs are composited vertically into the final output file.

Input:
    pipelines/p5_desi_chirality/results/analysis_healpix/nside32_cw_per_pixel.csv

Output:
    pipelines/p5_desi_chirality/paper/fig_p5_healpix_skymap_nside32.png
"""
from __future__ import annotations

import tempfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
import healpy as hp

P5 = Path(__file__).resolve().parents[1]
REPO = P5.parents[1]
SRC = P5 / "results/analysis_healpix/nside32_cw_per_pixel.csv"
OUT = P5 / "paper/fig_p5_healpix_skymap_nside32.png"

NSIDE = 32


def _render_panel(
    m: np.ndarray,
    title: str,
    cmap: str,
    vmin: float,
    vmax: float,
    cbar_label: str,
    tmp_path: Path,
) -> np.ndarray:
    """Close all figures, render one mollview, save to tmp_path, return RGBA."""
    plt.close("all")  # ensure no prior figures exist — healpy needs fig #1 free
    hp.mollview(
        m,
        title=title,
        cmap=cmap,
        min=vmin,
        max=vmax,
        unit=cbar_label,
        cbar=True,
        notext=False,
        coord=["C"],
    )
    hp.graticule(dpar=30, dmer=60, color="#888888", alpha=0.3, lw=0.4)
    plt.savefig(str(tmp_path), dpi=130, bbox_inches="tight", facecolor="white")
    plt.close("all")
    return mpimg.imread(str(tmp_path))


def main() -> int:
    df = pd.read_csv(SRC)
    npix = hp.nside2npix(NSIDE)

    sigma_map = np.full(npix, hp.UNSEEN, dtype=np.float64)
    n_map = np.full(npix, hp.UNSEEN, dtype=np.float64)
    for _, r in df.iterrows():
        pix = int(r["pix"])
        sigma_map[pix] = float(r["sigma_from_half"])
        n_map[pix] = float(r["n"])

    n_valid = n_map[n_map != hp.UNSEEN]
    n_min = float(n_valid.min())
    n_max = float(n_valid.max())
    vmax_sigma = 4.5

    with tempfile.TemporaryDirectory() as td:
        tmp1 = Path(td) / "top.png"
        tmp2 = Path(td) / "bot.png"

        img_top = _render_panel(
            n_map,
            title=(
                "(a)  Matched spirals per pixel  "
                "(NSIDE=32,  $n_{\\rm pix}=3{,}303$ occupied)"
            ),
            cmap="YlOrRd",
            vmin=n_min,
            vmax=n_max,
            cbar_label="Matched spirals per pixel",
            tmp_path=tmp1,
        )

        img_bot = _render_panel(
            sigma_map,
            title=(
                "(b)  Chirality $\\sigma_{\\rm from\\,half}$ per pixel  "
                "($p_{\\rm LEE}=0.135$;  "
                "$|\\sigma|^{\\rm obs}_{\\max}=4.13$  vs  "
                "null $|\\sigma|^{\\rm p99}_{\\max}=4.78$)"
            ),
            cmap="RdBu_r",
            vmin=-vmax_sigma,
            vmax=+vmax_sigma,
            cbar_label="Chirality $\\sigma_{\\rm from\\,half}$ per pixel",
            tmp_path=tmp2,
        )

    # Composite: stack vertically with a small white gap
    h_top, w_top = img_top.shape[:2]
    h_bot, w_bot = img_bot.shape[:2]
    w_out = max(w_top, w_bot)
    gap = 20  # pixels of white between panels

    # Pad narrower image to w_out with white
    def _pad_white(img: np.ndarray, target_w: int) -> np.ndarray:
        h, w = img.shape[:2]
        if w >= target_w:
            return img
        channels = img.shape[2] if img.ndim == 3 else 1
        pad = np.ones((h, target_w - w, channels), dtype=img.dtype)
        return np.concatenate([img, pad], axis=1)

    img_top = _pad_white(img_top, w_out)
    img_bot = _pad_white(img_bot, w_out)

    channels = img_top.shape[2]
    gap_row = np.ones((gap, w_out, channels), dtype=img_top.dtype)
    composite = np.concatenate([img_top, gap_row, img_bot], axis=0)

    plt.close("all")
    fig, ax = plt.subplots(1, 1, figsize=(w_out / 130, composite.shape[0] / 130))
    ax.imshow(composite)
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(OUT, dpi=130, bbox_inches="tight")
    plt.close("all")

    print(f"wrote {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
