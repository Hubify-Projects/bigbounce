#!/usr/bin/env python3
"""Regenerate P5 Figure 8 without the accidental outer Cartesian axes.

The top Mollweide panel bins the 3,765 released VoidFinder MAXIMALS
centres at HEALPix NSIDE=32.  The bottom panel bins the exact frozen
z<=0.24 CW/CCW parent and displays sigma_from_half for pixels with at
least 200 spirals.  Each healpy panel is rendered independently and the
resulting raster panels are composited directly, so no 0--1 wrapper axes
or overlapping wrapper labels can be introduced.
"""
from __future__ import annotations

import tempfile
from pathlib import Path

import healpy as hp
import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.io import fits
from scipy import stats


P5 = Path(__file__).resolve().parents[1]
CACHE = P5 / "outputs/35_exact_primary_rows_cache.parquet"
DESIVAST = P5 / "data/desivast"
OUT = P5 / "paper/fig_p5_voids_vs_chirality_skymap.png"
NSIDE = 32


def render_panel(m: np.ndarray, title: str, cmap: str, vmin: float,
                 vmax: float, unit: str, path: Path) -> np.ndarray:
    plt.close("all")
    hp.mollview(
        m,
        title=title,
        cmap=cmap,
        min=vmin,
        max=vmax,
        unit=unit,
        cbar=True,
        coord=["C"],
        notext=False,
    )
    hp.graticule(dpar=30, dmer=60, color="#888888", alpha=0.3, lw=0.4)
    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close("all")
    return mpimg.imread(path)


def pad_white(image: np.ndarray, width: int) -> np.ndarray:
    if image.shape[1] >= width:
        return image
    pad = np.ones(
        (image.shape[0], width - image.shape[1], image.shape[2]),
        dtype=image.dtype,
    )
    return np.concatenate([image, pad], axis=1)


def main() -> int:
    rows = pd.read_parquet(
        CACHE,
        columns=["desi_ra", "desi_dec", "match_class_eq"],
    )
    pix = hp.ang2pix(
        NSIDE,
        rows["desi_ra"].to_numpy(float),
        rows["desi_dec"].to_numpy(float),
        lonlat=True,
    )
    grouped = pd.DataFrame({
        "pix": pix,
        "cw": rows["match_class_eq"].to_numpy() == "CW",
    }).groupby("pix")["cw"].agg(n="size", n_cw="sum")
    grouped = grouped[grouped["n"] >= 200].copy()
    grouped["sigma"] = (
        grouped["n_cw"] - 0.5 * grouped["n"]
    ) / (0.5 * np.sqrt(grouped["n"]))

    ra_parts: list[np.ndarray] = []
    dec_parts: list[np.ndarray] = []
    for cap in ["NGC", "SGC"]:
        path = DESIVAST / f"DESIVAST_BGS_VOLLIM_VoidFinder_{cap}.fits"
        with fits.open(path, memmap=True) as hdul:
            maximals = hdul["MAXIMALS"].data
            ra_parts.append(np.asarray(maximals["RA"], dtype=float))
            dec_parts.append(np.asarray(maximals["DEC"], dtype=float))
    void_pix = hp.ang2pix(
        NSIDE,
        np.concatenate(ra_parts),
        np.concatenate(dec_parts),
        lonlat=True,
    )
    void_counts = pd.Series(void_pix).value_counts().sort_index()

    npix = hp.nside2npix(NSIDE)
    top = np.full(npix, hp.UNSEEN, dtype=float)
    bottom = np.full(npix, hp.UNSEEN, dtype=float)
    top[void_counts.index.to_numpy(int)] = void_counts.to_numpy(float)
    bottom[grouped.index.to_numpy(int)] = grouped["sigma"].to_numpy(float)

    both = grouped.join(void_counts.rename("n_voids"), how="inner")
    r, p = stats.pearsonr(both["n_voids"], both["sigma"])
    if len(void_counts) != 885 or int(np.median(void_counts)) != 4:
        raise RuntimeError("unexpected maximal-void pixel distribution")
    if len(grouped) != 1496 or len(both) != 727:
        raise RuntimeError("unexpected chirality/both-pixel counts")
    if not (abs(r - 0.005678491865223675) < 1e-12 and
            abs(p - 0.8785192553228591) < 1e-12):
        raise RuntimeError("pixel correlation does not reproduce the frozen result")

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        image_top = render_panel(
            top,
            "(a) DESIVAST maximal voids per pixel "
            "(NSIDE=32; 885 occupied pixels)",
            "YlOrRd",
            1,
            float(void_counts.max()),
            "Maximal voids per pixel",
            root / "top.png",
        )
        image_bottom = render_panel(
            bottom,
            "(b) Chirality $\\sigma_{\\rm from\\,half}$ per pixel "
            "($n_{\\rm spiral} \\geq 200$; $z \\leq 0.24$)",
            "RdBu_r",
            -6,
            6,
            "$\\sigma_{\\rm from\\,half}$",
            root / "bottom.png",
        )

    width = max(image_top.shape[1], image_bottom.shape[1])
    image_top = pad_white(image_top, width)
    image_bottom = pad_white(image_bottom, width)
    gap = np.ones((18, width, image_top.shape[2]), dtype=image_top.dtype)
    composite = np.concatenate([image_top, gap, image_bottom], axis=0)
    mpimg.imsave(OUT, composite)
    print(
        f"wrote {OUT}; occupied_void_pixels={len(void_counts)}; "
        f"valid_sigma_pixels={len(grouped)}; both={len(both)}; "
        f"pearson_r={r:.12f}; p={p:.12f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
