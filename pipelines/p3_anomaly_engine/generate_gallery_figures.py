#!/usr/bin/env python3
"""
generate_gallery_figures.py
----------------------------
Download DESI Legacy Survey sky cutouts for the top DESI DR1 anomalies
and compose publication-quality gallery figures in the style of the
Galaxy Chirality Catalog paper (black background, grz RGB thumbnails,
per-object labels).

Outputs (all in figures/):
  fig_gallery_top10.pdf / .png  -- main paper body: 2×5 grid, one per family
  fig_gallery_A1_highz_qso.pdf  -- appendix: high-z QSO family (3×4)
  fig_gallery_A2_qso.pdf        -- appendix: QSO / blue-excess family (4×4)
  fig_gallery_A3_agn.pdf        -- appendix: uncataloged AGN (4×4)
  fig_gallery_A4_bal_qso.pdf    -- appendix: BAL QSO candidates (4×4)
  fig_gallery_A5_elg.pdf        -- appendix: emission-line galaxies (4×4)
  fig_gallery_A6_lrg.pdf        -- appendix: unusual continuum (LRG) (4×4)
  fig_gallery_A7_post_sb.pdf    -- appendix: post-starburst galaxies (4×4)
  fig_gallery_A8_blue_compact.pdf -- appendix: blue compact galaxies (4×4)
  fig_gallery_A9_star.pdf       -- appendix: cool/unusual stars (4×4)
  fig_gallery_A10_unknown.pdf   -- appendix: multi-band unknowns (4×4)
"""

import csv
import os
import ssl
import sys
import time
import io
import urllib.request
import urllib.error
from collections import defaultdict
from pathlib import Path

# Bypass SSL verification for DESI Legacy Survey (trusted academic server)
_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
TAXONOMY_CSV = Path(
    "/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/"
    "h200_results/pod_backup_20260408_full/bigbounce/backups/"
    "20260406_231143/desi-taxonomy/desi_taxonomy_clusters.csv"
)
SPECTRA_DIR = Path(
    "/Users/houstongolden/Desktop/CODE_2025/bigbounce/"
    "pipelines/p1_highz_tracers/outputs/gold_anomalies/spectra"
)
FIGURES_DIR = SCRIPT_DIR / "figures"
CUTOUT_CACHE = SCRIPT_DIR / "figures" / "_cutout_cache"
FIGURES_DIR.mkdir(exist_ok=True)
CUTOUT_CACHE.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# DESI Legacy Survey cutout API
# ---------------------------------------------------------------------------
LEGACY_URL = (
    "https://www.legacysurvey.org/viewer/jpeg-cutout"
    "?ra={ra:.6f}&dec={dec:.6f}&size={size}&layer=ls-dr9"
)
FALLBACK_URL = (
    "https://www.legacysurvey.org/viewer/jpeg-cutout"
    "?ra={ra:.6f}&dec={dec:.6f}&size={size}&layer=sdss"
)
CUTOUT_SIZE = 128   # pixels — gives ~0.43" pix⁻¹ with ls-dr9


LAYER_FALLBACKS = [
    "ls-dr9", "ls-dr10", "sdss", "decals",
]


def _is_real_image(img: np.ndarray) -> bool:
    """Return True if image has actual sky content (not blank/error)."""
    return float(img.std()) > 3.0


def fetch_cutout(ra: float, dec: float, size: int = CUTOUT_SIZE) -> np.ndarray:
    """Return an (H, W, 3) uint8 RGB array from the Legacy Survey viewer.
    Tries ls-dr9 → ls-dr10 → sdss → decals. Uses curl to avoid macOS SSL.
    Validates image content via pixel std. Returns dark placeholder on fail."""
    import subprocess
    from PIL import Image

    cache_name = f"ra{ra:.5f}_dec{dec:.5f}_s{size}.jpg"
    cache_path = CUTOUT_CACHE / cache_name

    if cache_path.exists() and cache_path.stat().st_size > 500:
        try:
            img = np.array(Image.open(cache_path).convert("RGB"))
            if _is_real_image(img):
                return img
        except Exception:
            pass
        cache_path.unlink(missing_ok=True)

    base = "https://www.legacysurvey.org/viewer/jpeg-cutout"
    for layer in LAYER_FALLBACKS:
        url = f"{base}?ra={ra:.6f}&dec={dec:.6f}&size={size}&layer={layer}"
        try:
            result = subprocess.run(
                ["curl", "-s", "--max-time", "25", "-o", str(cache_path), url],
                capture_output=True, timeout=30,
            )
            if result.returncode == 0 and cache_path.exists() and cache_path.stat().st_size > 500:
                img = np.array(Image.open(cache_path).convert("RGB"))
                if _is_real_image(img):
                    print(f"  [ok:{layer}] {ra:.3f},{dec:.3f} → {cache_path.stat().st_size}B", flush=True)
                    return img
            if cache_path.exists():
                cache_path.unlink(missing_ok=True)
        except Exception as exc:
            print(f"  [warn] {layer} curl failed: {exc}", flush=True)
            if cache_path.exists():
                cache_path.unlink(missing_ok=True)

    print(f"  [miss] {ra:.3f},{dec:.3f} — no coverage in any layer", flush=True)
    # Dark placeholder with minimal marker
    img = np.zeros((size, size, 3), dtype=np.uint8)
    img[:, :] = [10, 12, 18]
    mid = size // 2
    img[mid - 1 : mid + 2, mid - size // 5 : mid + size // 5] = [35, 35, 55]
    img[mid - size // 5 : mid + size // 5, mid - 1 : mid + 2] = [35, 35, 55]
    return img


# ---------------------------------------------------------------------------
# Load taxonomy data
# ---------------------------------------------------------------------------
def load_taxonomy(max_dec_abs=62.0):
    """Return dict family -> list of dicts sorted descending by score."""
    families = defaultdict(list)
    with open(TAXONOMY_CSV) as f:
        reader = csv.DictReader(f)
        for row in reader:
            label = row["true_label"]
            if label == "Artifact":
                continue
            ra = float(row["ra"])
            dec = float(row["dec"])
            score = float(row["anomaly_score"])
            if abs(dec) > max_dec_abs:
                continue
            families[label].append({"ra": ra, "dec": dec, "score": score,
                                     "label": label})
    for fam in families:
        families[fam].sort(key=lambda x: -x["score"])
    return dict(families)


# ---------------------------------------------------------------------------
# High-z QSO gold objects (from confirmed z~6 spectra)
# ---------------------------------------------------------------------------
HIGHZ_QSO_OBJECTS = [
    {"targetid": "39633191367084936", "ra": 162.1878, "dec": 46.6218,
     "z": 6.1956, "score": 5.30, "label": "High-z QSO"},
    {"targetid": "39628507709444221", "ra": 245.8826, "dec": 31.2001,
     "z": 6.2161, "score": 5.18, "label": "High-z QSO"},
    {"targetid": "39633040179201450", "ra": 250.3406, "dec": 37.9222,
     "z": 6.016, "score": 4.32, "label": "High-z QSO"},
    {"targetid": "39628387379053918", "ra": 18.6205, "dec": 25.7785,
     "z": 6.0099, "score": 4.26, "label": "High-z QSO"},
    {"targetid": "39627689144878319", "ra": 60.8829, "dec": -3.9190,
     "z": 6.03, "score": 4.15, "label": "High-z QSO"},
    {"targetid": "39628353849789866", "ra": 339.6763, "dec": 23.9588,
     "z": 6.02, "score": 4.05, "label": "High-z QSO"},
    {"targetid": "39627905566769382", "ra": 7.0274, "dec": 4.9571,
     "z": 6.01, "score": 3.80, "label": "High-z QSO"},
    {"targetid": "39632995576973195", "ra": 174.3238, "dec": 35.8325,
     "z": 6.019, "score": 3.73, "label": "High-z QSO"},
    {"targetid": "39627789988529182", "ra": 313.5271, "dec": -0.0873,
     "z": 6.01, "score": 3.65, "label": "High-z QSO"},
    {"targetid": "39633152393611253", "ra": 107.7077, "dec": 44.1515,
     "z": 6.2297, "score": 3.62, "label": "High-z QSO"},
    {"targetid": "39628497290793707", "ra": 242.4053, "dec": 30.6965,
     "z": 6.1437, "score": 3.56, "label": "High-z QSO"},
    {"targetid": "39627944577993383", "ra": 181.9060, "dec": 6.5028,
     "z": 6.0135, "score": 3.31, "label": "High-z QSO"},
]


# ---------------------------------------------------------------------------
# Matplotlib style helpers
# ---------------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 7.5,
    "axes.labelsize": 7.5,
    "xtick.labelsize": 6.5,
    "ytick.labelsize": 6.5,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

BG_COLOR = "#000000"
LABEL_COLOR = "#ffffff"
SCORE_COLOR = "#f0c040"
BORDER_COLOR = "#333333"
FAMILY_COLORS = {
    "High-z QSO":     "#5bc8f5",
    "QSO":            "#7ec8e3",
    "AGN":            "#f07070",
    "BAL-QSO":        "#e89060",
    "ELG":            "#80d080",
    "LRG":            "#c090e0",
    "Post-starburst": "#f0b0d0",
    "Blue-compact":   "#60b8f0",
    "Star":           "#f8d060",
    "Unknown":        "#a0a0a0",
}
FAMILY_DISPLAY = {
    "High-z QSO":     "High-z QSO",
    "QSO":            "Blue-excess QSO",
    "AGN":            "Uncataloged AGN",
    "BAL-QSO":        "BAL QSO",
    "ELG":            "Emission-line",
    "LRG":            "Unusual Continuum",
    "Post-starburst": "Post-starburst",
    "Blue-compact":   "Blue Compact",
    "Star":           "Cool Dwarf",
    "Unknown":        "Multi-band",
}


def _sublabel(obj, short=True):
    """Build the per-thumbnail caption line."""
    fam = obj.get("label", "")
    if "targetid" in obj:
        # high-z QSO: show z and score
        return f"z={obj['z']:.2f} | AE={obj['score']:.2f}"
    elif short:
        return f"RA {obj['ra']:.1f}° | AE={obj['score']:.0f}"
    else:
        return f"RA={obj['ra']:.3f} Dec={obj['dec']:.3f}\nScore={obj['score']:.0f}"


def make_gallery_figure(
    objects,
    ncols: int,
    title: str,
    subtitle: str = "",
    outname: str = "gallery",
    show_family_label: bool = True,
    thumb_size: int = CUTOUT_SIZE,
):
    """Download cutouts and lay them out in a grid on a black background.

    Parameters
    ----------
    objects : list of dicts with 'ra', 'dec', 'score', 'label'
    ncols   : number of columns
    title   : figure title (suptitle)
    outname : output filename stem (no extension)
    """
    nrows = int(np.ceil(len(objects) / ncols))
    n_total = nrows * ncols

    # Figure sizing: each thumbnail ≈ 1.1" in the figure
    thumb_in = 1.05
    hpad_in = 0.05  # gap between thumbs
    side_in = ncols * (thumb_in + hpad_in) + 0.15
    top_in  = nrows * (thumb_in + hpad_in + 0.22) + 0.55
    fig = plt.figure(figsize=(side_in, top_in), facecolor=BG_COLOR)

    # Compute grid positions manually for pixel-perfect control
    margin_l = 0.06 / side_in
    margin_r = 1.0 - 0.06 / side_in
    margin_b = 0.04 / top_in
    margin_t = 1.0 - 0.40 / top_in

    cell_w = (margin_r - margin_l) / ncols
    cell_h = (margin_t - margin_b) / nrows

    print(f"  Generating {outname}: {len(objects)} objects, {nrows}×{ncols} grid", flush=True)

    for idx, obj in enumerate(objects):
        row = idx // ncols
        col = idx % ncols

        x0 = margin_l + col * cell_w + 0.008
        y0 = margin_t - (row + 1) * cell_h + 0.01
        w  = cell_w - 0.015
        h  = cell_h - 0.04

        ax = fig.add_axes([x0, y0 + 0.04 / top_in, w, h - 0.04 / top_in])
        ax.set_facecolor(BG_COLOR)

        # Download image
        img = fetch_cutout(obj["ra"], obj["dec"], size=thumb_size)
        ax.imshow(img, origin="upper", aspect="equal", interpolation="lanczos")
        ax.set_xlim(0, thumb_size)
        ax.set_ylim(thumb_size, 0)
        ax.set_xticks([])
        ax.set_yticks([])

        # Thin colored border by family
        fam = obj.get("label", "Unknown")
        fc = FAMILY_COLORS.get(fam, "#888888")
        for spine in ax.spines.values():
            spine.set_edgecolor(fc)
            spine.set_linewidth(0.8)

        # Caption line below the image
        cap = _sublabel(obj)
        if show_family_label:
            fdname = FAMILY_DISPLAY.get(fam, fam)
            cap = f"[{fdname}]\n{cap}"
        fig.text(
            x0 + w / 2, y0 + 0.012,
            cap,
            ha="center", va="bottom",
            fontsize=5.0,
            color=LABEL_COLOR,
            transform=fig.transFigure,
        )

    # Suptitle
    fig.text(
        0.5, 1.0 - 0.10 / top_in,
        title,
        ha="center", va="top",
        fontsize=8.5, fontweight="bold",
        color=LABEL_COLOR,
    )
    if subtitle:
        fig.text(
            0.5, 1.0 - 0.28 / top_in,
            subtitle,
            ha="center", va="top",
            fontsize=6.5, color="#aaaaaa",
            style="italic",
        )

    for ext in ("pdf", "png"):
        path = FIGURES_DIR / f"{outname}.{ext}"
        fig.savefig(path, facecolor=BG_COLOR, dpi=300)
        print(f"  Saved: {path}", flush=True)
    plt.close(fig)


# NEOWISE top anomaly — extreme W1-W2 color excess (paper §2.7)
NEOWISE_TOP = {
    "ra": 180.59, "dec": 0.56, "score": 11.5,
    "label": "NEOWISE",
    "note": "NEOWISE top anomaly: extreme W1-W2",
}


def predownload_all(all_objects: list):
    """Download all sky cutouts BEFORE generating figures.
    This lets us print a clean summary of coverage before committing to
    slow matplotlib rendering.
    """
    print(f"\nPre-downloading {len(all_objects)} unique sky positions...", flush=True)
    n_ok, n_miss = 0, 0
    for obj in all_objects:
        img = fetch_cutout(obj["ra"], obj["dec"])
        if _is_real_image(img):
            n_ok += 1
        else:
            n_miss += 1
    print(f"  Done: {n_ok} real images, {n_miss} placeholders\n", flush=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    from PIL import Image

    print("Loading DESI taxonomy catalog...", flush=True)
    families = load_taxonomy()
    print(f"  Loaded families: {sorted(families.keys())}", flush=True)

    # Collect all unique positions needed
    family_order = [
        "High-z QSO", "QSO", "AGN", "BAL-QSO", "ELG",
        "LRG", "Post-starburst", "Blue-compact", "Star", "Unknown",
    ]
    appendix_map = [
        ("QSO",            "A2", "Blue-excess QSO Candidates",
         "Top 16 of 16,602 QSO anomalies. Excess blue continuum relative to normal quasar template."),
        ("AGN",            "A3", "Uncataloged AGN",
         "Top 16 of 23,400 AGN-like anomalies. 73% lack prior catalog entries within 5\"."),
        ("BAL-QSO",        "A4", "Broad Absorption Line (BAL) QSO Candidates",
         "Top 16 of 13,650 BAL QSO anomalies. Deep UV absorption troughs indicate powerful outflows."),
        ("ELG",            "A5", "Extreme Emission-Line Galaxies",
         "Top 16 of 35,100 ELG anomalies. Anomalous line ratios classified BPT-AGN at 96.9%."),
        ("LRG",            "A6", "Unusual Continuum Objects",
         "Top 16 of 29,250 LRG-classified anomalies. Featureless or inverted continua."),
        ("Post-starburst", "A7", "Post-starburst Galaxies",
         "Top 16 of 11,700 post-starburst anomalies. Strong Balmer absorption, suppressed [O II]."),
        ("Blue-compact",   "A8", "Blue Compact Galaxies",
         "Top 16 of 7,800 blue compact anomalies. Compact morphology with UV-bright stellar populations."),
        ("Star",           "A9", "Cool/Unusual Stellar Objects",
         "Top 16 of 15,600 stellar anomalies. Candidate ultra-cool dwarfs and peculiar stellar types."),
        ("Unknown",        "A10", "Multi-band Anomalies (Uncataloged)",
         "Top 16 of 29,250 highest-uncertainty anomalies. No spectral template match."),
    ]

    # Build complete object list for pre-download (top 40 per family + top10 for top_per_family)
    all_positions = list(HIGHZ_QSO_OBJECTS)  # 12 high-z QSOs
    all_positions.append(NEOWISE_TOP)
    for fam_key, _, _, _ in appendix_map:
        for item in families.get(fam_key, [])[:40]:  # 40 candidates per appendix family
            all_positions.append(item)
    # Extra candidates for top10 figure (in case top-1 has no coverage)
    for fam in family_order:
        if fam == "High-z QSO":
            continue
        for item in families.get(fam, [])[:10]:
            all_positions.append(item)
    # Remove duplicates by (ra, dec) rounding
    seen = set()
    unique_positions = []
    for obj in all_positions:
        key = (round(obj["ra"], 4), round(obj["dec"], 4))
        if key not in seen:
            seen.add(key)
            unique_positions.append(obj)

    # PRE-DOWNLOAD PHASE — download all images before any figure rendering
    predownload_all(unique_positions)

    # ------------------------------------------------------------------
    # NEOWISE top anomaly — proper large single-panel figure
    # ------------------------------------------------------------------
    nw = NEOWISE_TOP
    nw_img = fetch_cutout(nw["ra"], nw["dec"], size=256)

    fig_nw, ax_nw = plt.subplots(1, 1, figsize=(3.5, 3.5))
    fig_nw.patch.set_facecolor(BG_COLOR)
    ax_nw.set_facecolor(BG_COLOR)
    ax_nw.imshow(nw_img, origin="upper", aspect="equal", interpolation="lanczos")
    ax_nw.set_xlim(0, 256)
    ax_nw.set_ylim(256, 0)
    ax_nw.set_xticks([])
    ax_nw.set_yticks([])
    for spine in ax_nw.spines.values():
        spine.set_edgecolor("#555555")
        spine.set_linewidth(0.5)

    fig_nw.suptitle(
        "NEOWISE Top Anomaly \u2014 Extreme W1\u2212W2 Color Excess",
        color=LABEL_COLOR,
        fontsize=8.5,
        fontweight="bold",
        y=0.98,
    )
    fig_nw.text(
        0.5, 0.015,
        r"Score = 11.5 | ($\alpha$, $\delta$) = (180.59°, 0.56°) | DESI Legacy Survey DR9 grz",
        ha="center", va="bottom",
        fontsize=6.5, color="#aaaaaa",
        style="italic",
    )

    plt.subplots_adjust(left=0.04, right=0.96, top=0.91, bottom=0.07)
    for ext in ("pdf", "png"):
        nw_path = FIGURES_DIR / f"fig_neowise_top_anomaly.{ext}"
        fig_nw.savefig(nw_path, facecolor=BG_COLOR, dpi=300, bbox_inches="tight")
        print(f"  Saved: {nw_path}", flush=True)
    plt.close(fig_nw)

    # ------------------------------------------------------------------
    # Figure top10: representative anomalies (main paper body)
    # ------------------------------------------------------------------
    top_per_family = []
    for fam in family_order:
        if fam == "High-z QSO":
            obj = dict(HIGHZ_QSO_OBJECTS[0])
            obj["label"] = "High-z QSO"
            top_per_family.append(obj)
        else:
            items = families.get(fam, [])[:10]
            picked = None
            for candidate in items:
                img = fetch_cutout(candidate["ra"], candidate["dec"])
                if _is_real_image(img):
                    picked = dict(candidate)
                    picked["label"] = fam
                    break
                print(f"  [top10 skip] {candidate['ra']:.1f},{candidate['dec']:.1f} — no coverage, trying next", flush=True)
            if picked is not None:
                top_per_family.append(picked)
            elif items:
                # fallback: use top-scored even if no coverage
                obj = dict(items[0])
                obj["label"] = fam
                top_per_family.append(obj)

    make_gallery_figure(
        objects=top_per_family,
        ncols=5,
        title="DESI DR1 Spectral Anomalies: Representative Objects by Taxonomy Family",
        subtitle=(
            "One highest-scoring anomaly per family. "
            "grz RGB composites from DESI Legacy Survey. "
            "Border color indicates taxonomy class."
        ),
        outname="fig_gallery_top10",
        show_family_label=True,
    )

    # ------------------------------------------------------------------
    # Appendix A1: High-z QSO family (all 12 confirmed z~6 sources)
    # ------------------------------------------------------------------
    highz_objs = [dict(o) for o in HIGHZ_QSO_OBJECTS]
    for o in highz_objs:
        o["label"] = "High-z QSO"
    make_gallery_figure(
        objects=highz_objs,
        ncols=4,
        title="Appendix A1 — High-z QSO Candidates (z ~ 6)",
        subtitle=(
            "All 12 DESI DR1 z>=6 anomalies surviving AE + Gunn-Peterson + SNR cuts. "
            "Scores are BigAE reconstruction MSE (lower SNR = more anomalous)."
        ),
        outname="fig_gallery_A1_highz_qso",
        show_family_label=False,
    )

    # ------------------------------------------------------------------
    # Appendix A2–A10: Top 16 per taxonomy family (4×4 grids)
    # Fetch from top 40 candidates, skipping positions with no coverage.
    # ------------------------------------------------------------------
    for fam_key, app_id, title_str, subtitle_str in appendix_map:
        items_all = families.get(fam_key, [])[:40]
        if not items_all:
            print(f"  [warn] no objects for family {fam_key}, skipping", flush=True)
            continue
        objs = []
        for item in items_all:
            if len(objs) >= 16:
                break
            img = fetch_cutout(item["ra"], item["dec"])
            if _is_real_image(img):
                o = dict(item)
                o["label"] = fam_key
                objs.append(o)
            else:
                print(f"  [skip] {item['ra']:.1f},{item['dec']:.1f} — no coverage, trying next", flush=True)
        if len(objs) < 16:
            print(f"  [warn] only {len(objs)}/16 real images for {fam_key}", flush=True)
        if not objs:
            print(f"  [warn] zero real images for {fam_key}, skipping", flush=True)
            continue
        make_gallery_figure(
            objects=objs,
            ncols=4,
            title=f"Appendix {app_id} — {title_str}",
            subtitle=subtitle_str,
            outname=f"fig_gallery_{app_id.lower()}_{fam_key.lower().replace('-','_').replace(' ','_')}",
            show_family_label=False,
        )

    print("\nAll gallery figures generated.", flush=True)


if __name__ == "__main__":
    try:
        from PIL import Image
    except ImportError:
        print("Installing Pillow...", flush=True)
        os.system("pip3 install Pillow --quiet")
        from PIL import Image

    main()
