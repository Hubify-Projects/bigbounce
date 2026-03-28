#!/usr/bin/env python3
"""
import_to_convex.py — Bulk import galaxy chirality catalog into Convex
======================================================================

Reads a merged Parquet catalog produced by Pipeline 2 and uploads it to
a Convex deployment in batches of 1000 rows via the HTTP mutation API.

Supports resume: on startup it queries the current row count in Convex
and skips that many rows from the Parquet file.

Required environment variables:
  CONVEX_URL        Deployment URL (e.g. https://impressive-quail-879.convex.cloud)
  CONVEX_DEPLOY_KEY Deploy key for authentication (starts with "prod:" or "dev:")

Usage:
  export CONVEX_URL="https://impressive-quail-879.convex.cloud"
  export CONVEX_DEPLOY_KEY="<your-deploy-key>"

  python import_to_convex.py /path/to/chirality_catalog.parquet

  # Dry-run (print stats, do not upload):
  python import_to_convex.py --dry-run /path/to/chirality_catalog.parquet

Prerequisites:
  pip install pandas pyarrow requests tqdm

Column mapping (Parquet -> Convex):
  dr8_id         -> dr8_id          (string)
  ra             -> ra              (float64)
  dec            -> dec             (float64)
  p_cw           -> p_cw            (float64)
  p_ccw          -> p_ccw           (float64)
  p_ns           -> p_ns            (float64)
  class          -> classification   (string: "CW" | "CCW" | "NOT_SPIRAL")
  confidence     -> confidence       (float64)

Note: The Parquet column "class" is renamed to "classification" because
"class" is a reserved keyword in TypeScript / Convex schema definitions.
"""

import argparse
import math
import os
import sys
import time

import pandas as pd
import requests
from tqdm import tqdm

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BATCH_SIZE = 1000  # Convex mutation limit per call
MAX_RETRIES = 5    # Retries per batch on transient failures
RETRY_BACKOFF = 2  # Exponential backoff base (seconds)

# Expected Parquet columns (input names) — ra/dec optional (added in Phase 2)
REQUIRED_COLUMNS = ["dr8_id", "p_cw", "p_ccw", "p_ns", "class", "confidence"]
OPTIONAL_COLUMNS = ["ra", "dec"]

# Convex function paths
IMPORT_MUTATION = "galaxies:importBatch"
COUNT_QUERY = "galaxies:count"


# ---------------------------------------------------------------------------
# Convex HTTP helpers
# ---------------------------------------------------------------------------

def convex_query(url: str, deploy_key: str, path: str, args: dict | None = None) -> any:
    """Execute a Convex query via the HTTP API."""
    resp = requests.post(
        f"{url}/api/query",
        json={"path": path, "args": args or {}},
        headers={
            "Authorization": f"Convex {deploy_key}",
            "Content-Type": "application/json",
        },
        timeout=30,
    )
    resp.raise_for_status()
    body = resp.json()
    if body.get("status") == "error":
        raise RuntimeError(f"Convex query error: {body.get('errorMessage', body)}")
    return body.get("value")


def convex_mutation(url: str, deploy_key: str, path: str, args: dict) -> any:
    """Execute a Convex mutation via the HTTP API with retries."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.post(
                f"{url}/api/mutation",
                json={"path": path, "args": args},
                headers={
                    "Authorization": f"Convex {deploy_key}",
                    "Content-Type": "application/json",
                },
                timeout=60,
            )
            resp.raise_for_status()
            body = resp.json()
            if body.get("status") == "error":
                raise RuntimeError(f"Convex mutation error: {body.get('errorMessage', body)}")
            return body.get("value")
        except (requests.RequestException, RuntimeError) as e:
            if attempt == MAX_RETRIES:
                raise
            wait = RETRY_BACKOFF ** attempt
            print(f"  Retry {attempt}/{MAX_RETRIES} after error: {e} (waiting {wait}s)")
            time.sleep(wait)


# ---------------------------------------------------------------------------
# Data preparation
# ---------------------------------------------------------------------------

def load_catalog(parquet_path: str) -> pd.DataFrame:
    """Load and validate the Parquet catalog."""
    print(f"Loading catalog: {parquet_path}")
    df = pd.read_parquet(parquet_path)
    print(f"  Rows: {len(df):,}")
    print(f"  Columns: {list(df.columns)}")

    # Check required columns
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Select and rename columns (only use what's available)
    cols_to_use = [c for c in REQUIRED_COLUMNS if c in df.columns]
    df = df[cols_to_use].copy()
    if "class" in df.columns:
        df = df.rename(columns={"class": "classification"})

    # Validate types — coerce to native Python types for JSON serialization
    df["dr8_id"] = df["dr8_id"].astype(str)
    if "ra" in df.columns:
        df["ra"] = df["ra"].astype(float)
    if "dec" in df.columns:
        df["dec"] = df["dec"].astype(float)
    df["p_cw"] = df["p_cw"].astype(float)
    df["p_ccw"] = df["p_ccw"].astype(float)
    df["p_ns"] = df["p_ns"].astype(float)
    df["classification"] = df["classification"].astype(str)
    df["confidence"] = df["confidence"].astype(float)

    # Sanity checks
    assert df["classification"].isin(["CW", "CCW", "NOT_SPIRAL"]).all(), \
        "Invalid classification values found"
    assert (df["confidence"] >= 0).all() and (df["confidence"] <= 1).all(), \
        "Confidence values out of [0,1] range"
    if "ra" in df.columns:
        assert (df["ra"] >= 0).all() and (df["ra"] < 360).all(), \
            "RA values out of [0,360) range"
    if "dec" in df.columns:
        assert (df["dec"] >= -90).all() and (df["dec"] <= 90).all(), \
            "Dec values out of [-90,90] range"

    # Drop any rows with NaN values (safety)
    n_before = len(df)
    df = df.dropna()
    n_dropped = n_before - len(df)
    if n_dropped > 0:
        print(f"  Dropped {n_dropped:,} rows with NaN values")

    print(f"  Classification distribution:")
    for cls, count in df["classification"].value_counts().items():
        print(f"    {cls}: {count:,} ({100*count/len(df):.1f}%)")
    print(f"  Confidence: mean={df['confidence'].mean():.3f}, "
          f"median={df['confidence'].median():.3f}, "
          f"min={df['confidence'].min():.3f}")

    return df


def df_to_batch(df_slice: pd.DataFrame) -> list[dict]:
    """Convert a DataFrame slice to a list of dicts for the Convex mutation."""
    records = df_slice.to_dict(orient="records")
    # Ensure all float values are JSON-safe (no NaN/Inf)
    for rec in records:
        for key, val in rec.items():
            if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
                raise ValueError(f"Non-finite float in record {rec['dr8_id']}: {key}={val}")
    return records


# ---------------------------------------------------------------------------
# Main import logic
# ---------------------------------------------------------------------------

def run_import(parquet_path: str, dry_run: bool = False):
    """Load catalog and bulk-import to Convex."""

    # Read environment
    convex_url = os.environ.get("CONVEX_URL")
    deploy_key = os.environ.get("CONVEX_DEPLOY_KEY")

    if not convex_url:
        print("ERROR: CONVEX_URL environment variable not set.")
        print("  Export it before running:")
        print('  export CONVEX_URL="https://impressive-quail-879.convex.cloud"')
        sys.exit(1)

    if not deploy_key:
        print("ERROR: CONVEX_DEPLOY_KEY environment variable not set.")
        print("  Export it before running:")
        print('  export CONVEX_DEPLOY_KEY="<your-deploy-key>"')
        sys.exit(1)

    # Load data
    df = load_catalog(parquet_path)
    total_rows = len(df)

    if dry_run:
        print(f"\n[DRY RUN] Would import {total_rows:,} galaxies to {convex_url}")
        print(f"[DRY RUN] Batches: {math.ceil(total_rows / BATCH_SIZE):,} x {BATCH_SIZE}")
        print("[DRY RUN] First batch sample:")
        sample = df_to_batch(df.head(3))
        for rec in sample:
            print(f"  {rec}")
        return

    # Resume support: check how many rows already exist
    print(f"\nConnecting to Convex: {convex_url}")
    existing_count = convex_query(convex_url, deploy_key, COUNT_QUERY)
    print(f"  Existing rows in Convex: {existing_count:,}")

    if existing_count >= total_rows:
        print(f"  All {total_rows:,} rows already imported. Nothing to do.")
        return

    if existing_count > 0:
        print(f"  Resuming from row {existing_count:,} (skipping already-imported rows)")
        df = df.iloc[existing_count:]
        print(f"  Remaining rows to import: {len(df):,}")

    # Import in batches
    n_batches = math.ceil(len(df) / BATCH_SIZE)
    imported = 0
    start_time = time.time()

    print(f"\nImporting {len(df):,} galaxies in {n_batches:,} batches of {BATCH_SIZE}...")
    print()

    with tqdm(total=len(df), unit="rows", desc="Importing") as pbar:
        for i in range(0, len(df), BATCH_SIZE):
            batch_df = df.iloc[i : i + BATCH_SIZE]
            batch = df_to_batch(batch_df)

            result = convex_mutation(
                convex_url,
                deploy_key,
                IMPORT_MUTATION,
                {"batch": batch},
            )

            imported += result
            pbar.update(len(batch))

    elapsed = time.time() - start_time
    rate = imported / elapsed if elapsed > 0 else 0

    print(f"\nImport complete.")
    print(f"  Rows imported this run: {imported:,}")
    print(f"  Total rows in Convex:   {existing_count + imported:,}")
    print(f"  Elapsed: {elapsed:.1f}s ({rate:.0f} rows/s)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Bulk import galaxy chirality catalog into Convex",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Import to dev deployment
  export CONVEX_URL="https://impressive-quail-879.convex.cloud"
  export CONVEX_DEPLOY_KEY="<key>"
  python import_to_convex.py outputs/chirality_catalog_merged.parquet

  # Dry run (no upload)
  python import_to_convex.py --dry-run outputs/chirality_catalog_merged.parquet

  # Import to production
  export CONVEX_URL="https://scintillating-cow-269.convex.cloud"
  export CONVEX_DEPLOY_KEY="<prod-key>"
  python import_to_convex.py outputs/chirality_catalog_merged.parquet
        """,
    )
    parser.add_argument(
        "parquet_path",
        help="Path to the merged Parquet chirality catalog",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print stats and sample data without uploading",
    )

    args = parser.parse_args()

    if not os.path.isfile(args.parquet_path):
        print(f"ERROR: File not found: {args.parquet_path}")
        sys.exit(1)

    run_import(args.parquet_path, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
