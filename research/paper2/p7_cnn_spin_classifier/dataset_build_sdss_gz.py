#!/usr/bin/env python
"""
BigBounce P7 — Build galaxy spin classification dataset from Galaxy Zoo + SDSS.

Loads Galaxy Zoo DECaLS catalog, filters for confident CW/CCW spiral labels,
downloads SDSS DR17 cutout images, and creates train/val/test splits.

Fallback: generates synthetic spiral images if SDSS downloads fail.

Usage:
    python dataset_build_sdss_gz.py --max_galaxies 10000 --output_dir data/ --seed 42
"""

from __future__ import print_function, division

import argparse
import csv
import hashlib
import json
import logging
import os
import sys
import time
import warnings

import numpy as np
import pandas as pd
import requests
from PIL import Image, ImageDraw

warnings.filterwarnings("ignore")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("dataset_build")

# ---------------------------------------------------------------------------
# Galaxy Zoo DECaLS catalog URL (Zenodo)
# ---------------------------------------------------------------------------
GZ_DECALS_URL = (
    "https://zenodo.org/records/4573248/files/"
    "gz_decals_volunteers_1_and_2.csv?download=1"
)

# SDSS DR17 SkyServer image cutout endpoint
SDSS_CUTOUT_URL = (
    "https://skyserver.sdss.org/dr17/SkyServerWS/ImgCutout/getjpeg"
    "?ra={ra}&dec={dec}&scale=0.4&width={size}&height={size}"
)

# Rate limit between SDSS requests (seconds)
SDSS_RATE_LIMIT = 0.5


def parse_args():
    parser = argparse.ArgumentParser(
        description="Build galaxy spin dataset from Galaxy Zoo DECaLS + SDSS DR17"
    )
    parser.add_argument(
        "--max_galaxies", type=int, default=10000,
        help="Maximum total galaxies (CW+CCW combined). Default 10000."
    )
    parser.add_argument(
        "--output_dir", type=str, default="data/",
        help="Output directory for images and catalog. Default: data/"
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="Random seed for reproducibility. Default: 42"
    )
    parser.add_argument(
        "--cutout_size", type=int, default=128,
        help="Cutout image size in pixels. Default: 128"
    )
    parser.add_argument(
        "--use_synthetic", action="store_true",
        help="Force use of synthetic images (skip SDSS download)"
    )
    parser.add_argument(
        "--gz_catalog_path", type=str, default=None,
        help="Path to local GZ DECaLS catalog CSV. If not provided, downloads from Zenodo."
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Galaxy Zoo catalog loading and filtering
# ---------------------------------------------------------------------------

def download_gz_catalog(output_dir):
    """Download Galaxy Zoo DECaLS catalog from Zenodo."""
    catalog_path = os.path.join(output_dir, "gz_decals_catalog.csv")
    if os.path.exists(catalog_path):
        logger.info("GZ catalog already exists at %s", catalog_path)
        return catalog_path

    logger.info("Downloading Galaxy Zoo DECaLS catalog from Zenodo...")
    logger.info("URL: %s", GZ_DECALS_URL)
    logger.info("This may take several minutes for the full catalog (~200 MB).")

    try:
        response = requests.get(GZ_DECALS_URL, stream=True, timeout=600)
        response.raise_for_status()
        total = int(response.headers.get("content-length", 0))
        downloaded = 0
        with open(catalog_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                f.write(chunk)
                downloaded += len(chunk)
                if total > 0:
                    pct = 100.0 * downloaded / total
                    sys.stdout.write(
                        "\r  Downloaded %.1f MB / %.1f MB (%.0f%%)"
                        % (downloaded / 1e6, total / 1e6, pct)
                    )
                    sys.stdout.flush()
        print("")
        logger.info("Catalog saved to %s", catalog_path)
        return catalog_path
    except Exception as e:
        logger.error("Failed to download GZ catalog: %s", str(e))
        if os.path.exists(catalog_path):
            os.remove(catalog_path)
        return None


def load_and_filter_gz_catalog(catalog_path, max_per_class, rng):
    """
    Load GZ DECaLS catalog and filter for high-confidence CW/CCW spirals.

    Selection criteria:
    - Featured/disk galaxy: smooth-or-featured_featured-or-disk_fraction > 0.5
    - Has spiral arms: has-spiral-arms_yes_fraction > 0.5
    - CW: spiral-winding_clockwise_fraction > 0.6
    - CCW: spiral-winding_anticlockwise_fraction > 0.6
    """
    logger.info("Loading GZ catalog from %s", catalog_path)
    df = pd.read_csv(catalog_path, low_memory=False)
    logger.info("Loaded %d rows, %d columns", len(df), len(df.columns))

    # Identify relevant columns — GZ DECaLS uses various naming conventions
    # Try to find the right column names
    cols = list(df.columns)

    # Map expected column patterns to actual columns
    col_map = {}

    # RA/Dec
    for c in cols:
        cl = c.lower()
        if cl in ("ra", "ra_1", "ra_gz"):
            col_map["ra"] = c
        elif cl in ("dec", "dec_1", "dec_gz"):
            col_map["dec"] = c
        elif cl in ("iauname", "dr8_id", "objid", "id_str"):
            col_map["objid"] = c

    # GZ DECaLS vote fraction columns
    featured_candidates = [
        c for c in cols
        if "featured" in c.lower() and "fraction" in c.lower()
        and "featured-or-disk" in c.lower()
    ]
    spiral_candidates = [
        c for c in cols
        if "spiral" in c.lower() and "yes" in c.lower()
        and "fraction" in c.lower()
    ]
    cw_candidates = [
        c for c in cols
        if "clockwise" in c.lower() and "fraction" in c.lower()
        and "anti" not in c.lower() and "counter" not in c.lower()
    ]
    ccw_candidates = [
        c for c in cols
        if ("anticlockwise" in c.lower() or "counter" in c.lower())
        and "fraction" in c.lower()
    ]
    smooth_candidates = [
        c for c in cols
        if "smooth" in c.lower() and "fraction" in c.lower()
        and "featured" not in c.lower()
    ]

    if featured_candidates:
        col_map["featured_frac"] = featured_candidates[0]
    if spiral_candidates:
        col_map["spiral_frac"] = spiral_candidates[0]
    if cw_candidates:
        col_map["cw_frac"] = cw_candidates[0]
    if ccw_candidates:
        col_map["ccw_frac"] = ccw_candidates[0]
    if smooth_candidates:
        col_map["smooth_frac"] = smooth_candidates[0]

    logger.info("Column mapping: %s", json.dumps(col_map, indent=2))

    required = ["ra", "dec", "featured_frac", "cw_frac", "ccw_frac"]
    missing = [k for k in required if k not in col_map]
    if missing:
        logger.error(
            "Missing required columns in catalog: %s", ", ".join(missing)
        )
        logger.info("Available columns (first 50): %s", ", ".join(cols[:50]))
        return None, None

    # Use objid or create one from index
    if "objid" not in col_map:
        df["_objid"] = ["gz_{:08d}".format(i) for i in range(len(df))]
        col_map["objid"] = "_objid"

    # Filter for featured/disk galaxies
    featured_mask = df[col_map["featured_frac"]] > 0.5
    logger.info("Featured/disk galaxies (>0.5): %d", featured_mask.sum())

    # Filter for spiral arms if column exists
    if "spiral_frac" in col_map:
        spiral_mask = df[col_map["spiral_frac"]] > 0.5
        logger.info("Has spiral arms (>0.5): %d", spiral_mask.sum())
        base_mask = featured_mask & spiral_mask
    else:
        logger.warning("No spiral arms column found, using featured mask only")
        base_mask = featured_mask

    # CW and CCW selections
    cw_mask = base_mask & (df[col_map["cw_frac"]] > 0.6)
    ccw_mask = base_mask & (df[col_map["ccw_frac"]] > 0.6)

    logger.info("High-confidence CW spirals (>0.6): %d", cw_mask.sum())
    logger.info("High-confidence CCW spirals (>0.6): %d", ccw_mask.sum())

    cw_df = df[cw_mask].copy()
    ccw_df = df[ccw_mask].copy()

    if len(cw_df) == 0 or len(ccw_df) == 0:
        logger.error("No galaxies found matching criteria. Check column names.")
        return None, None

    # Balance classes
    n_per_class = min(max_per_class, len(cw_df), len(ccw_df))
    logger.info("Balancing to %d per class (%d total)", n_per_class, 2 * n_per_class)

    cw_sample = cw_df.sample(n=n_per_class, random_state=rng)
    ccw_sample = ccw_df.sample(n=n_per_class, random_state=rng)

    # Build catalog dataframe
    records = []
    for _, row in cw_sample.iterrows():
        records.append({
            "objid": str(row[col_map["objid"]]),
            "ra": float(row[col_map["ra"]]),
            "dec": float(row[col_map["dec"]]),
            "label": "cw",
            "gz_cw_frac": float(row[col_map["cw_frac"]]),
            "gz_ccw_frac": float(row[col_map["ccw_frac"]]),
        })
    for _, row in ccw_sample.iterrows():
        records.append({
            "objid": str(row[col_map["objid"]]),
            "ra": float(row[col_map["ra"]]),
            "dec": float(row[col_map["dec"]]),
            "label": "ccw",
            "gz_cw_frac": float(row[col_map["cw_frac"]]),
            "gz_ccw_frac": float(row[col_map["ccw_frac"]]),
        })

    catalog = pd.DataFrame(records)

    # Also extract smooth/elliptical galaxies for null test
    null_df = None
    if "smooth_frac" in col_map:
        smooth_mask = df[col_map["smooth_frac"]] > 0.8
        null_candidates = df[smooth_mask].copy()
        logger.info("Smooth/elliptical galaxies for null test: %d", len(null_candidates))
        if len(null_candidates) > 0:
            n_null = min(500, len(null_candidates))
            null_sample = null_candidates.sample(n=n_null, random_state=rng)
            null_records = []
            for _, row in null_sample.iterrows():
                null_records.append({
                    "objid": str(row[col_map["objid"]]),
                    "ra": float(row[col_map["ra"]]),
                    "dec": float(row[col_map["dec"]]),
                    "label": "null",
                    "gz_cw_frac": float(row[col_map["cw_frac"]]) if col_map["cw_frac"] in row.index else 0.0,
                    "gz_ccw_frac": float(row[col_map["ccw_frac"]]) if col_map["ccw_frac"] in row.index else 0.0,
                })
            null_df = pd.DataFrame(null_records)

    return catalog, null_df


# ---------------------------------------------------------------------------
# SDSS image download
# ---------------------------------------------------------------------------

def download_sdss_cutout(ra, dec, size, output_path, timeout=30):
    """Download a single SDSS DR17 cutout image."""
    url = SDSS_CUTOUT_URL.format(ra=ra, dec=dec, size=size)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        # Check it is actually a JPEG
        if len(response.content) < 500:
            return False, "Response too small (likely error page)"
        with open(output_path, "wb") as f:
            f.write(response.content)
        # Verify image can be opened
        img = Image.open(output_path)
        if img.size[0] < 10 or img.size[1] < 10:
            os.remove(output_path)
            return False, "Image too small"
        return True, "ok"
    except Exception as e:
        if os.path.exists(output_path):
            os.remove(output_path)
        return False, str(e)


def download_all_cutouts(catalog, output_dir, cutout_size, null_df=None):
    """Download SDSS cutouts for all galaxies in catalog."""
    img_dir_cw = os.path.join(output_dir, "images", "cw")
    img_dir_ccw = os.path.join(output_dir, "images", "ccw")
    img_dir_null = os.path.join(output_dir, "images", "null")
    os.makedirs(img_dir_cw, exist_ok=True)
    os.makedirs(img_dir_ccw, exist_ok=True)
    os.makedirs(img_dir_null, exist_ok=True)

    failures = []
    success_count = 0
    total = len(catalog)

    # Combine catalog and null_df for downloading
    all_items = list(catalog.iterrows())
    if null_df is not None:
        all_items.extend(list(null_df.iterrows()))
        total += len(null_df)

    logger.info("Downloading %d SDSS cutouts (%.1f sec rate limit)...", total, SDSS_RATE_LIMIT)

    for idx, (_, row) in enumerate(all_items):
        label = row["label"]
        objid = row["objid"]
        ra = row["ra"]
        dec = row["dec"]

        if label == "cw":
            img_path = os.path.join(img_dir_cw, "{}.jpg".format(objid))
        elif label == "ccw":
            img_path = os.path.join(img_dir_ccw, "{}.jpg".format(objid))
        else:
            img_path = os.path.join(img_dir_null, "{}.jpg".format(objid))

        if os.path.exists(img_path):
            success_count += 1
            continue

        ok, msg = download_sdss_cutout(ra, dec, cutout_size, img_path)
        if ok:
            success_count += 1
        else:
            failures.append({
                "objid": objid,
                "ra": ra,
                "dec": dec,
                "label": label,
                "error": msg,
            })

        if (idx + 1) % 100 == 0 or (idx + 1) == total:
            logger.info(
                "  Progress: %d/%d downloaded, %d failures",
                success_count, idx + 1, len(failures)
            )

        time.sleep(SDSS_RATE_LIMIT)

    # Early abort check: if too many failures, switch to synthetic
    failure_rate = len(failures) / max(total, 1)
    if failure_rate > 0.5 and success_count < 100:
        logger.warning(
            "High failure rate (%.0f%%) — SDSS may be unavailable. "
            "Falling back to synthetic images.",
            failure_rate * 100,
        )
        return failures, True  # signal to use synthetic

    return failures, False


# ---------------------------------------------------------------------------
# Synthetic image generation (fallback)
# ---------------------------------------------------------------------------

def generate_synthetic_spiral(size, handedness, rng_local):
    """
    Generate a synthetic spiral galaxy image.
    SYNTHETIC - NOT FOR SCIENCE. For pipeline testing only.

    Args:
        size: image size in pixels
        handedness: 'cw' or 'ccw'
        rng_local: numpy random state

    Returns:
        PIL Image
    """
    img = Image.new("RGB", (size, size), (5, 5, 15))
    draw = ImageDraw.Draw(img)

    cx, cy = size / 2.0, size / 2.0

    # Draw spiral arms
    n_arms = rng_local.choice([2, 3])
    arm_offsets = np.linspace(0, 2 * np.pi, n_arms, endpoint=False)

    # Spiral parameters
    a = rng_local.uniform(0.1, 0.3)  # tightness
    brightness_base = rng_local.randint(150, 220)

    # Direction: CW spirals wind clockwise, CCW wind counter-clockwise
    direction = 1.0 if handedness == "cw" else -1.0

    # Draw galactic bulge
    bulge_r = int(size * rng_local.uniform(0.06, 0.12))
    bulge_color = (
        brightness_base + rng_local.randint(-20, 20),
        brightness_base - 20 + rng_local.randint(-10, 10),
        brightness_base - 60 + rng_local.randint(-10, 10),
    )
    bulge_color = tuple(max(0, min(255, c)) for c in bulge_color)
    draw.ellipse(
        [cx - bulge_r, cy - bulge_r, cx + bulge_r, cy + bulge_r],
        fill=bulge_color,
    )

    # Draw spiral arms as series of dots
    for arm_offset in arm_offsets:
        n_points = rng_local.randint(200, 400)
        for t in np.linspace(0, 4 * np.pi, n_points):
            r = a * t * size / (4 * np.pi) * 0.45
            theta = direction * t + arm_offset

            # Add some scatter
            scatter = rng_local.normal(0, max(1, r * 0.08))
            x = cx + (r + scatter) * np.cos(theta)
            y = cy + (r + scatter) * np.sin(theta)

            if 0 <= x < size and 0 <= y < size:
                # Brightness decreases with radius
                fade = max(0.2, 1.0 - t / (4 * np.pi))
                b = int(brightness_base * fade * rng_local.uniform(0.6, 1.0))
                color = (
                    max(0, min(255, b + rng_local.randint(-15, 15))),
                    max(0, min(255, b - 10 + rng_local.randint(-10, 10))),
                    max(0, min(255, b - 40 + rng_local.randint(-10, 10))),
                )
                dot_size = max(1, int(rng_local.uniform(0.5, 2.0)))
                draw.ellipse(
                    [x - dot_size, y - dot_size, x + dot_size, y + dot_size],
                    fill=color,
                )

    # Add some background stars
    n_stars = rng_local.randint(5, 20)
    for _ in range(n_stars):
        sx = rng_local.randint(0, size - 1)
        sy = rng_local.randint(0, size - 1)
        sb = rng_local.randint(80, 200)
        draw.point((sx, sy), fill=(sb, sb, sb))

    # Add slight Gaussian noise via numpy
    arr = np.array(img, dtype=np.float32)
    noise = rng_local.normal(0, 3, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    img = Image.fromarray(arr)

    return img


def generate_synthetic_elliptical(size, rng_local):
    """
    Generate a synthetic elliptical galaxy (no spiral arms).
    SYNTHETIC - NOT FOR SCIENCE. For balanced null test.
    """
    img = Image.new("RGB", (size, size), (5, 5, 15))
    draw = ImageDraw.Draw(img)

    cx, cy = size / 2.0, size / 2.0
    rx = int(size * rng_local.uniform(0.15, 0.35))
    ry = int(size * rng_local.uniform(0.10, 0.30))
    brightness = rng_local.randint(120, 200)
    color = (
        brightness + rng_local.randint(-10, 10),
        brightness - 15 + rng_local.randint(-10, 10),
        brightness - 40 + rng_local.randint(-10, 10),
    )
    color = tuple(max(0, min(255, c)) for c in color)
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=color)

    arr = np.array(img, dtype=np.float32)
    noise = rng_local.normal(0, 3, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)


def generate_synthetic_dataset(catalog, output_dir, cutout_size, rng, null_df=None):
    """Generate synthetic images for all galaxies in catalog."""
    logger.warning("=" * 60)
    logger.warning("SYNTHETIC IMAGES — NOT FOR SCIENCE")
    logger.warning("Using synthetic spiral images for pipeline testing.")
    logger.warning("Replace with real SDSS images for any scientific analysis.")
    logger.warning("=" * 60)

    img_dir_cw = os.path.join(output_dir, "images", "cw")
    img_dir_ccw = os.path.join(output_dir, "images", "ccw")
    img_dir_null = os.path.join(output_dir, "images", "null")
    os.makedirs(img_dir_cw, exist_ok=True)
    os.makedirs(img_dir_ccw, exist_ok=True)
    os.makedirs(img_dir_null, exist_ok=True)

    for idx, row in catalog.iterrows():
        objid = row["objid"]
        label = row["label"]
        rng_local = np.random.RandomState(hash(objid) % (2**31))

        if label == "cw":
            img_path = os.path.join(img_dir_cw, "{}.jpg".format(objid))
        else:
            img_path = os.path.join(img_dir_ccw, "{}.jpg".format(objid))

        if not os.path.exists(img_path):
            img = generate_synthetic_spiral(cutout_size, label, rng_local)
            img.save(img_path, "JPEG", quality=95)

    if null_df is not None:
        for idx, row in null_df.iterrows():
            objid = row["objid"]
            rng_local = np.random.RandomState(hash(objid) % (2**31))
            img_path = os.path.join(img_dir_null, "{}.jpg".format(objid))
            if not os.path.exists(img_path):
                img = generate_synthetic_elliptical(cutout_size, rng_local)
                img.save(img_path, "JPEG", quality=95)

    logger.info("Synthetic images generated.")

    # Write synthetic flag
    flag_path = os.path.join(output_dir, "SYNTHETIC_DATA_FLAG.txt")
    with open(flag_path, "w") as f:
        f.write("WARNING: This dataset uses SYNTHETIC images.\n")
        f.write("NOT FOR SCIENCE. Pipeline testing only.\n")
        f.write("Replace with real SDSS images before any scientific analysis.\n")


# ---------------------------------------------------------------------------
# Train/val/test split
# ---------------------------------------------------------------------------

def assign_splits(catalog, seed):
    """Assign train/val/test splits (70/15/15), stratified by label."""
    rng = np.random.RandomState(seed)
    splits = []

    for label in ["cw", "ccw"]:
        mask = catalog["label"] == label
        indices = catalog.index[mask].tolist()
        rng.shuffle(indices)

        n = len(indices)
        n_train = int(0.70 * n)
        n_val = int(0.15 * n)

        for i, idx in enumerate(indices):
            if i < n_train:
                splits.append("train")
            elif i < n_train + n_val:
                splits.append("val")
            else:
                splits.append("test")

    # This approach won't work directly because we need to match order
    # Redo properly
    split_col = pd.Series("", index=catalog.index)
    for label in ["cw", "ccw"]:
        mask = catalog["label"] == label
        indices = catalog.index[mask].tolist()
        rng.shuffle(indices)
        n = len(indices)
        n_train = int(0.70 * n)
        n_val = int(0.15 * n)
        for i, idx in enumerate(indices):
            if i < n_train:
                split_col[idx] = "train"
            elif i < n_train + n_val:
                split_col[idx] = "val"
            else:
                split_col[idx] = "test"

    catalog = catalog.copy()
    catalog["split"] = split_col
    return catalog


# ---------------------------------------------------------------------------
# Manifest and checksums
# ---------------------------------------------------------------------------

def compute_catalog_hash(catalog_path):
    """Compute SHA256 of the catalog CSV."""
    sha256 = hashlib.sha256()
    with open(catalog_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


# ---------------------------------------------------------------------------
# Synthetic-only catalog generation (no GZ catalog needed)
# ---------------------------------------------------------------------------

def generate_synthetic_catalog(max_galaxies, seed):
    """
    Generate a fully synthetic catalog when GZ catalog is unavailable.
    Random sky positions with balanced CW/CCW labels.
    """
    rng = np.random.RandomState(seed)
    n_per_class = max_galaxies // 2

    records = []
    for i in range(n_per_class):
        records.append({
            "objid": "syn_cw_{:06d}".format(i),
            "ra": rng.uniform(0, 360),
            "dec": rng.uniform(-60, 60),
            "label": "cw",
            "gz_cw_frac": 0.8 + rng.uniform(0, 0.15),
            "gz_ccw_frac": rng.uniform(0, 0.1),
        })
    for i in range(n_per_class):
        records.append({
            "objid": "syn_ccw_{:06d}".format(i),
            "ra": rng.uniform(0, 360),
            "dec": rng.uniform(-60, 60),
            "label": "ccw",
            "gz_cw_frac": rng.uniform(0, 0.1),
            "gz_ccw_frac": 0.8 + rng.uniform(0, 0.15),
        })

    catalog = pd.DataFrame(records)

    # Null test galaxies
    null_records = []
    for i in range(min(500, n_per_class // 5)):
        null_records.append({
            "objid": "syn_null_{:06d}".format(i),
            "ra": rng.uniform(0, 360),
            "dec": rng.uniform(-60, 60),
            "label": "null",
            "gz_cw_frac": rng.uniform(0.1, 0.3),
            "gz_ccw_frac": rng.uniform(0.1, 0.3),
        })
    null_df = pd.DataFrame(null_records) if null_records else None

    return catalog, null_df


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    rng = np.random.RandomState(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    logger.info("=" * 60)
    logger.info("BigBounce P7 — Galaxy Spin Dataset Builder")
    logger.info("Max galaxies: %d", args.max_galaxies)
    logger.info("Output dir: %s", args.output_dir)
    logger.info("Seed: %d", args.seed)
    logger.info("Cutout size: %d px", args.cutout_size)
    logger.info("=" * 60)

    max_per_class = args.max_galaxies // 2
    use_synthetic = args.use_synthetic
    catalog = None
    null_df = None

    # Step 1: Load Galaxy Zoo catalog
    if not use_synthetic:
        if args.gz_catalog_path and os.path.exists(args.gz_catalog_path):
            gz_path = args.gz_catalog_path
        else:
            gz_path = download_gz_catalog(args.output_dir)

        if gz_path is not None:
            catalog, null_df = load_and_filter_gz_catalog(gz_path, max_per_class, rng)

        if catalog is None:
            logger.warning(
                "Could not load/filter GZ catalog. Falling back to synthetic."
            )
            use_synthetic = True

    if use_synthetic or catalog is None:
        logger.info("Generating synthetic catalog...")
        catalog, null_df = generate_synthetic_catalog(args.max_galaxies, args.seed)
        use_synthetic = True

    logger.info(
        "Catalog: %d galaxies (%d CW, %d CCW)",
        len(catalog),
        (catalog["label"] == "cw").sum(),
        (catalog["label"] == "ccw").sum(),
    )
    if null_df is not None:
        logger.info("Null test galaxies: %d", len(null_df))

    # Step 2: Download images or generate synthetic
    if use_synthetic:
        generate_synthetic_dataset(
            catalog, args.output_dir, args.cutout_size, rng, null_df
        )
    else:
        failures, fallback_needed = download_all_cutouts(
            catalog, args.output_dir, args.cutout_size, null_df
        )
        if fallback_needed:
            logger.info("Switching to synthetic fallback due to download failures.")
            generate_synthetic_dataset(
                catalog, args.output_dir, args.cutout_size, rng, null_df
            )
            use_synthetic = True
        else:
            # Remove galaxies whose images failed to download
            if failures:
                fail_path = os.path.join(args.output_dir, "download_failures.csv")
                fail_df = pd.DataFrame(failures)
                fail_df.to_csv(fail_path, index=False)
                logger.info("Download failures logged to %s", fail_path)

                failed_ids = set(f["objid"] for f in failures)
                before = len(catalog)
                catalog = catalog[~catalog["objid"].isin(failed_ids)].reset_index(drop=True)
                logger.info(
                    "Removed %d failed downloads, %d galaxies remain",
                    before - len(catalog), len(catalog),
                )

                # Re-balance if needed
                n_cw = (catalog["label"] == "cw").sum()
                n_ccw = (catalog["label"] == "ccw").sum()
                if n_cw != n_ccw:
                    n_min = min(n_cw, n_ccw)
                    cw_idx = catalog[catalog["label"] == "cw"].sample(
                        n=n_min, random_state=rng
                    ).index
                    ccw_idx = catalog[catalog["label"] == "ccw"].sample(
                        n=n_min, random_state=rng
                    ).index
                    catalog = catalog.loc[
                        cw_idx.tolist() + ccw_idx.tolist()
                    ].reset_index(drop=True)
                    logger.info("Re-balanced to %d per class", n_min)

    # Step 3: Assign train/val/test splits
    catalog = assign_splits(catalog, args.seed)

    split_counts = catalog.groupby(["split", "label"]).size()
    logger.info("Split distribution:\n%s", str(split_counts))

    # Step 4: Save catalog
    catalog_path = os.path.join(args.output_dir, "catalog.csv")
    catalog.to_csv(catalog_path, index=False)
    logger.info("Catalog saved to %s", catalog_path)

    # Save null catalog separately if exists
    if null_df is not None:
        null_path = os.path.join(args.output_dir, "null_catalog.csv")
        null_df.to_csv(null_path, index=False)
        logger.info("Null catalog saved to %s", null_path)

    # Step 5: Manifest
    catalog_hash = compute_catalog_hash(catalog_path)
    manifest = {
        "total_galaxies": len(catalog),
        "n_cw": int((catalog["label"] == "cw").sum()),
        "n_ccw": int((catalog["label"] == "ccw").sum()),
        "n_null": int(len(null_df)) if null_df is not None else 0,
        "n_train": int((catalog["split"] == "train").sum()),
        "n_val": int((catalog["split"] == "val").sum()),
        "n_test": int((catalog["split"] == "test").sum()),
        "cutout_size": args.cutout_size,
        "seed": args.seed,
        "synthetic": use_synthetic,
        "catalog_sha256": catalog_hash,
    }
    manifest_path = os.path.join(args.output_dir, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    logger.info("Manifest saved to %s", manifest_path)
    logger.info("Catalog SHA256: %s", catalog_hash)

    logger.info("=" * 60)
    logger.info("Dataset build complete.")
    if use_synthetic:
        logger.warning("SYNTHETIC DATA — NOT FOR SCIENCE. Pipeline testing only.")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
