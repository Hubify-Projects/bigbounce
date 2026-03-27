#!/usr/bin/env python3
"""
Pipeline A — CMB Anomaly Hunter: Patch Extraction
==================================================

Extracts 10 deg x 10 deg square patches from a Planck SMICA CMB temperature map
using gnomonic projection, normalizes them, and saves as numpy arrays.

Planck SMICA map: COM_CMB_IQU-smica_2048_R3.00_full.fits
  - NSIDE = 2048
  - Ordering: RING
  - Field 0 = temperature (I)
  - Field 1 = Q polarization
  - Field 2 = U polarization

Data source (Planck Legacy Archive / IRSA):
  https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb/COM_CMB_IQU-smica_2048_R3.00_full.fits

Usage:
  python extract_patches.py --map_file <path_to_fits> [--n_patches 1000] [--patch_deg 10] [--patch_pixels 64] [--output_dir outputs]
"""

import os
import sys
import argparse
import numpy as np
import healpy as hp
from pathlib import Path
import json
import time
from datetime import datetime

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
GALACTIC_PLANE_CUT_DEG = 20.0  # exclude |b| < this many degrees
DEFAULT_N_PATCHES = 1000
DEFAULT_PATCH_DEG = 10.0       # angular size of each patch (degrees)
DEFAULT_PATCH_PIXELS = 64      # output patch resolution (64x64)
CMB_FIELD = 0                  # field index for temperature in SMICA file

# ---------------------------------------------------------------------------
# Download helper (optional — tries to download if map not found)
# ---------------------------------------------------------------------------
PLANCK_SMICA_URL = (
    "https://irsa.ipac.caltech.edu/data/Planck/release_3/"
    "all-sky-maps/maps/component-maps/cmb/"
    "COM_CMB_IQU-smica_2048_R3.00_full.fits"
)

PLANCK_SMICA_PLA_URL = (
    "https://pla.esac.esa.int/pla/aio/product-action?"
    "MAP.MAP_ID=COM_CMB_IQU-smica_2048_R3.00_full.fits"
)


def download_map(output_path: str) -> bool:
    """Attempt to download the Planck SMICA map. Returns True on success."""
    import urllib.request
    import shutil

    urls = [PLANCK_SMICA_URL, PLANCK_SMICA_PLA_URL]

    for url in urls:
        print(f"\n[download] Trying: {url[:80]}...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                total = resp.headers.get("Content-Length")
                total = int(total) if total else None
                print(f"[download] Content-Length: {total or 'unknown'} bytes")

                with open(output_path, "wb") as f:
                    downloaded = 0
                    chunk_size = 1024 * 1024  # 1 MB
                    t0 = time.time()
                    while True:
                        chunk = resp.read(chunk_size)
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)
                        elapsed = time.time() - t0
                        speed = downloaded / (1024**2) / max(elapsed, 0.01)
                        if total:
                            pct = 100 * downloaded / total
                            print(
                                f"\r[download] {downloaded/(1024**2):.1f} MB / "
                                f"{total/(1024**2):.1f} MB  ({pct:.1f}%)  "
                                f"{speed:.1f} MB/s",
                                end="", flush=True,
                            )
                        else:
                            print(
                                f"\r[download] {downloaded/(1024**2):.1f} MB  "
                                f"{speed:.1f} MB/s",
                                end="", flush=True,
                            )
                    print()

                # Sanity check — FITS files are typically > 100 MB
                fsize = os.path.getsize(output_path)
                if fsize < 50 * 1024 * 1024:
                    print(f"[download] WARNING: file is only {fsize/(1024**2):.1f} MB — may be truncated or an error page")
                    os.remove(output_path)
                    continue

                print(f"[download] Saved to {output_path} ({fsize/(1024**2):.1f} MB)")
                return True

        except Exception as e:
            print(f"[download] Failed: {e}")
            if os.path.exists(output_path):
                os.remove(output_path)
            continue

    print("\n[download] Could not download automatically.")
    print("[download] Please download manually from:")
    print(f"  {PLANCK_SMICA_URL}")
    print(f"  or: {PLANCK_SMICA_PLA_URL}")
    return False


# ---------------------------------------------------------------------------
# Galactic coordinate filter
# ---------------------------------------------------------------------------
def galactic_latitude(theta_rad: float, phi_rad: float) -> float:
    """
    Convert HEALPix (co-latitude theta, longitude phi) in radians
    to Galactic latitude b in degrees.

    HEALPix convention: theta = co-latitude from North Pole (0..pi),
    phi = longitude (0..2pi). For Galactic coordinates these map directly
    to (90 - b, l).
    """
    b_deg = 90.0 - np.degrees(theta_rad)
    return b_deg


def generate_sky_positions(
    n_patches: int,
    gal_cut_deg: float = GALACTIC_PLANE_CUT_DEG,
    seed: int = 42,
) -> list[tuple[float, float]]:
    """
    Generate random sky positions (theta, phi) in radians,
    uniformly distributed on the sphere, avoiding the galactic plane.

    Returns list of (theta, phi) tuples.
    """
    rng = np.random.default_rng(seed)
    positions = []
    attempts = 0
    max_attempts = n_patches * 20  # generous budget

    while len(positions) < n_patches and attempts < max_attempts:
        # Uniform on sphere: cos(theta) uniform in [-1, 1]
        cos_theta = rng.uniform(-1, 1)
        theta = np.arccos(cos_theta)
        phi = rng.uniform(0, 2 * np.pi)
        attempts += 1

        b = galactic_latitude(theta, phi)
        if abs(b) >= gal_cut_deg:
            positions.append((theta, phi))

    if len(positions) < n_patches:
        print(
            f"WARNING: only generated {len(positions)}/{n_patches} positions "
            f"after {max_attempts} attempts"
        )

    return positions


# ---------------------------------------------------------------------------
# Patch extraction via gnomonic projection
# ---------------------------------------------------------------------------
def extract_patch(
    healpix_map: np.ndarray,
    theta: float,
    phi: float,
    patch_deg: float = DEFAULT_PATCH_DEG,
    patch_pixels: int = DEFAULT_PATCH_PIXELS,
) -> np.ndarray:
    """
    Extract a square patch from a HEALPix map using gnomonic (tangent-plane)
    projection centered on (theta, phi).

    Parameters
    ----------
    healpix_map : 1D HEALPix map array
    theta : co-latitude in radians (0 = North Pole)
    phi : longitude in radians
    patch_deg : angular size of the patch in degrees
    patch_pixels : number of pixels along each side of the output

    Returns
    -------
    2D numpy array of shape (patch_pixels, patch_pixels)
    """
    # healpy.gnomview can extract the projection data via return_projected_map
    # rot = (lon_deg, lat_deg) where lon = phi in deg, lat = 90 - theta in deg
    lon_deg = np.degrees(phi)
    lat_deg = 90.0 - np.degrees(theta)

    # Resolution in arcmin per pixel
    reso_arcmin = (patch_deg * 60.0) / patch_pixels

    patch = hp.gnomview(
        healpix_map,
        rot=(lon_deg, lat_deg),
        reso=reso_arcmin,
        xsize=patch_pixels,
        ysize=patch_pixels,
        return_projected_map=True,
        no_plot=True,
    )

    return np.array(patch)


def normalize_patch(patch: np.ndarray) -> np.ndarray:
    """
    Normalize a patch: subtract mean, divide by std.
    Handles NaN/masked pixels by replacing them with 0 after normalization.
    """
    # Convert masked array to regular array if needed
    if hasattr(patch, "filled"):
        mask = patch.mask if hasattr(patch, "mask") else np.zeros_like(patch, dtype=bool)
        patch = np.array(patch.filled(np.nan))
    else:
        mask = np.isnan(patch)

    valid = ~np.isnan(patch)
    if valid.sum() < 10:
        # Too few valid pixels — return zeros
        return np.zeros_like(patch, dtype=np.float32)

    mean = np.nanmean(patch)
    std = np.nanstd(patch)

    if std < 1e-30:
        return np.zeros_like(patch, dtype=np.float32)

    normed = (patch - mean) / std
    normed[~valid] = 0.0  # fill NaN pixels with 0

    return normed.astype(np.float32)


# ---------------------------------------------------------------------------
# Quality check
# ---------------------------------------------------------------------------
def patch_quality_ok(patch: np.ndarray, max_nan_frac: float = 0.1) -> bool:
    """Reject patches with too many NaN or zero pixels."""
    if patch is None:
        return False
    nan_frac = np.isnan(patch).sum() / patch.size
    if nan_frac > max_nan_frac:
        return False
    zero_frac = (patch == 0).sum() / patch.size
    if zero_frac > 0.5:
        return False
    return True


# ---------------------------------------------------------------------------
# Main extraction pipeline
# ---------------------------------------------------------------------------
def run_extraction(
    map_file: str,
    n_patches: int = DEFAULT_N_PATCHES,
    patch_deg: float = DEFAULT_PATCH_DEG,
    patch_pixels: int = DEFAULT_PATCH_PIXELS,
    output_dir: str = "outputs",
    seed: int = 42,
):
    """Full patch extraction pipeline."""

    print("=" * 70)
    print("PIPELINE A — CMB ANOMALY HUNTER: PATCH EXTRACTION")
    print("=" * 70)

    # ------------------------------------------------------------------
    # 1. Load map
    # ------------------------------------------------------------------
    print(f"\n[1/5] Loading HEALPix map: {map_file}")

    if not os.path.exists(map_file):
        print(f"  Map file not found: {map_file}")
        print(f"  Attempting download...")
        download_map(map_file)
        if not os.path.exists(map_file):
            print("  FATAL: Could not obtain map file. Exiting.")
            sys.exit(1)

    t0 = time.time()
    cmb_map = hp.read_map(map_file, field=CMB_FIELD, dtype=np.float64)
    nside = hp.get_nside(cmb_map)
    npix = hp.nside2npix(nside)
    elapsed = time.time() - t0
    print(f"  NSIDE = {nside}, npix = {npix:,}")
    print(f"  Map loaded in {elapsed:.1f}s")
    print(f"  Map range: [{cmb_map.min():.4e}, {cmb_map.max():.4e}] (K_CMB)")

    # Remove monopole and dipole
    print("  Removing monopole and dipole...")
    cmb_map = hp.remove_dipole(cmb_map, verbose=False)

    # ------------------------------------------------------------------
    # 2. Generate sky positions
    # ------------------------------------------------------------------
    print(f"\n[2/5] Generating {n_patches} sky positions (|b| >= {GALACTIC_PLANE_CUT_DEG} deg)...")
    positions = generate_sky_positions(n_patches, seed=seed)
    print(f"  Generated {len(positions)} valid positions")

    # ------------------------------------------------------------------
    # 3. Extract patches
    # ------------------------------------------------------------------
    print(f"\n[3/5] Extracting {patch_deg}deg x {patch_deg}deg patches at {patch_pixels}x{patch_pixels} pixels...")
    patches = []
    metadata = []
    n_rejected = 0
    t0 = time.time()

    for i, (theta, phi) in enumerate(positions):
        if (i + 1) % 100 == 0 or i == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / max(elapsed, 0.01)
            print(f"  Patch {i+1}/{len(positions)}  ({rate:.1f} patches/s)")

        try:
            raw_patch = extract_patch(cmb_map, theta, phi, patch_deg, patch_pixels)

            if not patch_quality_ok(raw_patch):
                n_rejected += 1
                continue

            normed_patch = normalize_patch(raw_patch)

            patches.append(normed_patch)

            lon_deg = np.degrees(phi)
            lat_deg = 90.0 - np.degrees(theta)
            b_deg = galactic_latitude(theta, phi)

            metadata.append({
                "index": len(patches) - 1,
                "theta_rad": float(theta),
                "phi_rad": float(phi),
                "glon_deg": float(lon_deg),
                "glat_deg": float(lat_deg),
                "b_deg": float(b_deg),
                "raw_mean": float(np.nanmean(raw_patch)),
                "raw_std": float(np.nanstd(raw_patch)),
                "raw_min": float(np.nanmin(raw_patch)),
                "raw_max": float(np.nanmax(raw_patch)),
            })

        except Exception as e:
            n_rejected += 1
            if n_rejected <= 5:
                print(f"  WARNING: Patch {i} failed: {e}")

    elapsed = time.time() - t0
    print(f"\n  Extracted {len(patches)} patches in {elapsed:.1f}s")
    print(f"  Rejected {n_rejected} patches (quality filter)")

    if len(patches) == 0:
        print("FATAL: No patches extracted. Check map file.")
        sys.exit(1)

    # ------------------------------------------------------------------
    # 4. Stack and save
    # ------------------------------------------------------------------
    print(f"\n[4/5] Saving patches to {output_dir}/...")
    os.makedirs(output_dir, exist_ok=True)

    patches_array = np.stack(patches, axis=0)  # shape: (N, patch_pixels, patch_pixels)
    print(f"  Patches array shape: {patches_array.shape}")
    print(f"  Patches dtype: {patches_array.dtype}")
    print(f"  Memory: {patches_array.nbytes / (1024**2):.1f} MB")

    patches_path = os.path.join(output_dir, "cmb_patches.npy")
    np.save(patches_path, patches_array)
    print(f"  Saved: {patches_path}")

    metadata_path = os.path.join(output_dir, "patch_metadata.json")
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"  Saved: {metadata_path}")

    # ------------------------------------------------------------------
    # 5. Summary statistics
    # ------------------------------------------------------------------
    print(f"\n[5/5] Summary statistics")
    print(f"  Total patches: {len(patches)}")
    print(f"  Patch size: {patch_pixels}x{patch_pixels} pixels ({patch_deg}deg x {patch_deg}deg)")
    print(f"  Angular resolution: {patch_deg * 60 / patch_pixels:.1f} arcmin/pixel")
    print(f"  Global mean of normalized patches: {patches_array.mean():.6f}")
    print(f"  Global std of normalized patches: {patches_array.std():.6f}")

    # Distribution of raw standard deviations (to catch any map issues)
    raw_stds = [m["raw_std"] for m in metadata]
    print(f"  Raw std range: [{min(raw_stds):.4e}, {max(raw_stds):.4e}]")
    print(f"  Raw std median: {np.median(raw_stds):.4e}")

    # Sky coverage
    lats = [m["glat_deg"] for m in metadata]
    print(f"  Latitude range: [{min(lats):.1f}, {max(lats):.1f}] deg")
    n_north = sum(1 for b in lats if b > 0)
    n_south = len(lats) - n_north
    print(f"  North/South: {n_north}/{n_south}")

    # Save a summary
    summary = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "map_file": map_file,
        "nside": int(nside),
        "n_patches": len(patches),
        "n_rejected": n_rejected,
        "patch_deg": patch_deg,
        "patch_pixels": patch_pixels,
        "reso_arcmin": patch_deg * 60 / patch_pixels,
        "gal_cut_deg": GALACTIC_PLANE_CUT_DEG,
        "seed": seed,
        "patches_file": patches_path,
        "metadata_file": metadata_path,
    }
    summary_path = os.path.join(output_dir, "extraction_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n  Summary saved: {summary_path}")
    print("=" * 70)
    print("PATCH EXTRACTION COMPLETE")
    print("=" * 70)

    return patches_array, metadata


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Pipeline A: Extract CMB patches from Planck SMICA map"
    )
    parser.add_argument(
        "--map_file",
        type=str,
        default="COM_CMB_IQU-smica_2048_R3.00_full.fits",
        help="Path to Planck SMICA FITS file (default: looks in current dir)",
    )
    parser.add_argument(
        "--n_patches",
        type=int,
        default=DEFAULT_N_PATCHES,
        help=f"Number of patches to extract (default: {DEFAULT_N_PATCHES})",
    )
    parser.add_argument(
        "--patch_deg",
        type=float,
        default=DEFAULT_PATCH_DEG,
        help=f"Patch angular size in degrees (default: {DEFAULT_PATCH_DEG})",
    )
    parser.add_argument(
        "--patch_pixels",
        type=int,
        default=DEFAULT_PATCH_PIXELS,
        help=f"Patch pixel resolution (default: {DEFAULT_PATCH_PIXELS})",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="outputs",
        help="Output directory (default: outputs/)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed (default: 42)",
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help="Download the Planck map if not found locally",
    )

    args = parser.parse_args()

    run_extraction(
        map_file=args.map_file,
        n_patches=args.n_patches,
        patch_deg=args.patch_deg,
        patch_pixels=args.patch_pixels,
        output_dir=args.output_dir,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()
