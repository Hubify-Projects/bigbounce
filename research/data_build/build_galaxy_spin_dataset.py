#!/usr/bin/env python3
"""
build_galaxy_spin_dataset.py — Build reproducible galaxy spin dataset from Galaxy Zoo DECaLS

Downloads the Galaxy Zoo DECaLS volunteer classification catalog from Zenodo
(DOI: 10.5281/zenodo.4573248, Walmsley et al. 2022, MNRAS 509:3966) and
extracts an object-level spiral galaxy catalog.

IMPORTANT LIMITATION:
    Galaxy Zoo DECaLS does NOT include a clockwise/anticlockwise (CW/CCW)
    winding direction question. The decision tree classifies spiral TIGHTNESS
    (tight/medium/loose) but not CHIRALITY. This means:

    - This catalog provides a verified set of spiral galaxies with redshifts
    - CW/CCW counts CANNOT be derived from Galaxy Zoo DECaLS alone
    - For the hierarchical Bayesian A(z) fit, we use published aggregate
      CW/CCW counts from Shamir (2012, 2022, 2024) as documented in
      research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv

    Galaxy Zoo 2 (Willett et al. 2013) DOES include a CW/ACW question for
    SDSS galaxies, but covers a smaller sample and lower redshift range.

Output:
    data/public_mirror/galaxy_zoo_decals_spins.csv
    - Object-level catalog of spiral galaxies from GZ DECaLS
    - Columns: galaxy_id, ra, dec, redshift, spiral_vote_fraction,
               winding_tight, winding_medium, winding_loose, survey_source
    - NOT a CW/CCW catalog (see limitation above)

Usage:
    python build_galaxy_spin_dataset.py [--min-spiral-vote 0.6] [--output OUTPUT_PATH]
    python build_galaxy_spin_dataset.py --skip-download  # use cached parquet

Requirements:
    pip install pandas pyarrow requests tqdm

Citation:
    Walmsley et al. (2022), MNRAS 509:3966
    DOI: 10.5281/zenodo.4573248
    License: CC-BY-4.0
"""

import argparse
import hashlib
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]

# Zenodo record for Galaxy Zoo DECaLS (Walmsley et al. 2022)
ZENODO_DOI = "10.5281/zenodo.4573248"
ZENODO_RECORD_ID = "4573248"

# We use the volunteers_1_and_2 parquet file (18.7 MB) — much smaller than
# the auto_posteriors (1.6 GB) and sufficient for spiral identification.
PARQUET_URL = (
    f"https://zenodo.org/api/records/{ZENODO_RECORD_ID}"
    "/files/gz_decals_volunteers_1_and_2.parquet/content"
)
PARQUET_FILENAME = "gz_decals_volunteers_1_and_2.parquet"

# Expected columns for spiral morphology (GZ DECaLS campaigns 1+2 decision tree)
# Question: "has-spiral-arms" -> yes / no
# Question: "spiral-winding" -> tight / medium / loose
# Columns use the pattern: {question}_{answer}_fraction
SPIRAL_COL = "has-spiral-arms_yes_fraction"
SPIRAL_COLS_WINDING = {
    "tight": "spiral-winding_tight_fraction",
    "medium": "spiral-winding_medium_fraction",
    "loose": "spiral-winding_loose_fraction",
}

# Fallback column patterns (campaigns may vary naming)
SPIRAL_COL_ALTS = [
    "has-spiral-arms_yes_fraction",
    "spiral-arms_yes_fraction",
    "has_spiral_arms_yes_fraction",
]

DEFAULT_OUTPUT = REPO_ROOT / "data" / "public_mirror" / "galaxy_zoo_decals_spins.csv"
CACHE_DIR = REPO_ROOT / "data" / "public_mirror" / "galaxy_zoo_decals"


def download_parquet(dest_dir: Path, force: bool = False) -> Path:
    """Download the GZ DECaLS parquet file from Zenodo."""
    import requests
    from tqdm import tqdm

    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / PARQUET_FILENAME

    if dest_path.exists() and not force:
        print(f"Using cached file: {dest_path}")
        return dest_path

    print(f"Downloading {PARQUET_FILENAME} from Zenodo ({ZENODO_DOI})...")
    print(f"URL: {PARQUET_URL}")

    resp = requests.get(PARQUET_URL, stream=True, timeout=120)
    resp.raise_for_status()

    total = int(resp.headers.get("content-length", 0))
    with open(dest_path, "wb") as f, tqdm(
        total=total, unit="B", unit_scale=True, desc=PARQUET_FILENAME
    ) as pbar:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
            pbar.update(len(chunk))

    size_mb = dest_path.stat().st_size / 1e6
    print(f"Downloaded: {dest_path} ({size_mb:.1f} MB)")
    return dest_path


def compute_sha256(path: Path) -> str:
    """Compute SHA-256 checksum of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def find_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    """Find the first matching column from a list of candidates."""
    for col in candidates:
        if col in df.columns:
            return col
    # Try case-insensitive and underscore/hyphen-insensitive match
    norm = {c.lower().replace("-", "_").replace(" ", "_"): c for c in df.columns}
    for candidate in candidates:
        key = candidate.lower().replace("-", "_").replace(" ", "_")
        if key in norm:
            return norm[key]
    return None


def build_spiral_catalog(
    parquet_path: Path, min_spiral_vote: float = 0.6
) -> pd.DataFrame:
    """Extract spiral galaxies from GZ DECaLS volunteer classifications."""
    print(f"Reading {parquet_path}...")
    df = pd.read_parquet(parquet_path)
    print(f"Total galaxies in catalog: {len(df):,}")
    print(f"Columns available: {len(df.columns)}")

    # Identify the spiral arms column
    spiral_col = find_column(df, SPIRAL_COL_ALTS)
    if spiral_col is None:
        # Print available columns for debugging
        morph_cols = [c for c in df.columns if "spiral" in c.lower() or "arm" in c.lower()]
        print(f"\nWARNING: Could not find spiral arms column.")
        print(f"Spiral/arm-related columns found: {morph_cols}")
        print(f"All columns: {list(df.columns)}")
        sys.exit(1)

    print(f"Using spiral column: {spiral_col}")

    # Identify winding columns
    winding_cols = {}
    for tightness, col_name in SPIRAL_COLS_WINDING.items():
        found = find_column(df, [col_name])
        if found:
            winding_cols[tightness] = found

    # Identify coordinate and redshift columns
    id_col = find_column(df, ["iauname", "objid", "dr8_id", "id"])
    ra_col = find_column(df, ["ra"])
    dec_col = find_column(df, ["dec"])
    z_col = find_column(df, ["redshift", "z", "z_phot", "photoz"])

    print(f"ID column: {id_col}")
    print(f"RA column: {ra_col}")
    print(f"Dec column: {dec_col}")
    print(f"Redshift column: {z_col}")
    print(f"Winding columns: {winding_cols}")

    # Filter to spirals
    spirals = df[df[spiral_col] >= min_spiral_vote].copy()
    print(f"\nSpirals with vote_fraction >= {min_spiral_vote}: {len(spirals):,}")

    # Filter to galaxies with valid redshifts
    if z_col and z_col in spirals.columns:
        has_z = spirals[z_col].notna() & (spirals[z_col] > 0)
        spirals = spirals[has_z].copy()
        print(f"With valid redshift (z > 0): {len(spirals):,}")

    # Build output dataframe
    out = pd.DataFrame()
    out["galaxy_id"] = spirals[id_col].values if id_col else spirals.index
    if ra_col:
        out["ra"] = spirals[ra_col].values
    if dec_col:
        out["dec"] = spirals[dec_col].values
    if z_col:
        out["redshift"] = spirals[z_col].values
    out["spiral_vote_fraction"] = spirals[spiral_col].values

    for tightness, col in winding_cols.items():
        out[f"winding_{tightness}"] = spirals[col].values

    out["survey_source"] = "Galaxy_Zoo_DECaLS"

    # Sort by redshift
    if "redshift" in out.columns:
        out = out.sort_values("redshift").reset_index(drop=True)

    return out


def write_catalog(catalog: pd.DataFrame, output_path: Path) -> None:
    """Write the spiral catalog with provenance header."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    header_lines = [
        "# Galaxy Zoo DECaLS Spiral Galaxy Catalog",
        "# Source: Walmsley et al. (2022), MNRAS 509:3966",
        "# DOI: 10.5281/zenodo.4573248",
        "# License: CC-BY-4.0",
        f"# Generated by: research/data_build/build_galaxy_spin_dataset.py",
        f"# Total spirals: {len(catalog)}",
        "#",
        "# LIMITATION: This catalog identifies spiral galaxies but does NOT",
        "# include CW/CCW winding direction. Galaxy Zoo DECaLS classifies",
        "# winding TIGHTNESS (tight/medium/loose), not CHIRALITY.",
        "# For CW/CCW counts, see galaxy_spin_counts.csv (Shamir 2024).",
        "#",
    ]

    with open(output_path, "w") as f:
        for line in header_lines:
            f.write(line + "\n")
        catalog.to_csv(f, index=False)

    print(f"\nWrote {len(catalog):,} spirals to {output_path}")
    print(f"File size: {output_path.stat().st_size / 1024:.1f} KB")


def print_summary(catalog: pd.DataFrame) -> None:
    """Print summary statistics."""
    print("\n" + "=" * 60)
    print("CATALOG SUMMARY")
    print("=" * 60)
    print(f"Total spiral galaxies: {len(catalog):,}")

    if "redshift" in catalog.columns:
        z = catalog["redshift"]
        print(f"Redshift range: {z.min():.4f} - {z.max():.4f}")
        print(f"Median redshift: {z.median():.4f}")

        # Redshift bins
        bins = [0, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0]
        for i in range(len(bins) - 1):
            n = ((z >= bins[i]) & (z < bins[i + 1])).sum()
            if n > 0:
                print(f"  z = {bins[i]:.2f} - {bins[i+1]:.2f}: {n:,} galaxies")

    if "spiral_vote_fraction" in catalog.columns:
        svf = catalog["spiral_vote_fraction"]
        print(f"\nSpiral vote fraction: mean={svf.mean():.3f}, "
              f"median={svf.median():.3f}")

    print("\n" + "=" * 60)
    print("NOTE: CW/CCW classification is NOT available in GZ DECaLS.")
    print("The hierarchical Bayesian A(z) fit uses published aggregate")
    print("counts from Shamir (2012, 2022, 2024) — see:")
    print("  research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Build spiral galaxy catalog from Galaxy Zoo DECaLS"
    )
    parser.add_argument(
        "--min-spiral-vote", type=float, default=0.6,
        help="Minimum spiral arms vote fraction (default: 0.6)"
    )
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT,
        help=f"Output CSV path (default: {DEFAULT_OUTPUT})"
    )
    parser.add_argument(
        "--skip-download", action="store_true",
        help="Use cached parquet file (skip download)"
    )
    parser.add_argument(
        "--force-download", action="store_true",
        help="Re-download even if cached file exists"
    )
    args = parser.parse_args()

    # Step 1: Download
    if args.skip_download:
        parquet_path = CACHE_DIR / PARQUET_FILENAME
        if not parquet_path.exists():
            print(f"ERROR: --skip-download but no cached file at {parquet_path}")
            sys.exit(1)
    else:
        parquet_path = download_parquet(CACHE_DIR, force=args.force_download)

    # Checksum
    sha = compute_sha256(parquet_path)
    print(f"SHA-256: {sha}")

    # Write checksum file
    checksum_path = CACHE_DIR / "CHECKSUMS.txt"
    with open(checksum_path, "w") as f:
        f.write(f"{sha}  {PARQUET_FILENAME}\n")

    # Step 2: Build catalog
    catalog = build_spiral_catalog(parquet_path, args.min_spiral_vote)

    # Step 3: Write output
    write_catalog(catalog, args.output)

    # Step 4: Summary
    print_summary(catalog)

    # Step 5: Compute output checksum
    out_sha = compute_sha256(args.output)
    print(f"\nOutput SHA-256: {out_sha}")


if __name__ == "__main__":
    main()
