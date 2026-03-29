#!/usr/bin/env python3
"""
Deduplicate the enhanced 18M DESI DR1 catalog.

Due to a crash and restart during processing, ~5M rows are duplicated
(same TARGETID processed twice). This script:
  1. Reads all 46 parquet files
  2. Deduplicates by 'targetid' (keeps LAST occurrence = more recent run)
  3. Reports stats: total before, unique IDs, duplicates removed
  4. Writes deduplicated catalog as 500K-row batches
  5. Verifies final count is close to 17.65M unique DESI DR1 spectra
"""

import os
import sys
import time
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

INPUT_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M"
OUTPUT_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped"
BATCH_SIZE = 500_000
EXPECTED_UNIQUE = 17_650_000  # approximate unique DESI DR1 spectra


def main():
    t0 = time.time()

    # --- Step 1: Discover parquet files ---
    parquet_files = sorted([
        os.path.join(INPUT_DIR, f)
        for f in os.listdir(INPUT_DIR)
        if f.endswith(".parquet")
    ])
    print(f"Found {len(parquet_files)} parquet files in input directory")

    # --- Step 2: Read all files into a single DataFrame ---
    print("Reading all parquet files...")
    dfs = []
    total_read = 0
    for i, fpath in enumerate(parquet_files):
        df = pd.read_parquet(fpath)
        total_read += len(df)
        dfs.append(df)
        if (i + 1) % 10 == 0 or i == len(parquet_files) - 1:
            print(f"  Read {i + 1}/{len(parquet_files)} files ({total_read:,} rows so far)")

    t1 = time.time()
    print(f"Read complete in {t1 - t0:.1f}s")

    print("Concatenating DataFrames...")
    combined = pd.concat(dfs, ignore_index=True)
    del dfs  # free memory
    total_rows_before = len(combined)
    print(f"\nTotal rows before dedup: {total_rows_before:,}")

    t2 = time.time()
    print(f"Concat complete in {t2 - t1:.1f}s")

    # --- Step 3: Deduplicate by targetid, keeping LAST occurrence ---
    print("\nDeduplicating by 'targetid' (keeping last occurrence)...")
    deduped = combined.drop_duplicates(subset="targetid", keep="last")
    del combined  # free memory

    unique_count = len(deduped)
    duplicates_removed = total_rows_before - unique_count

    print(f"Unique TARGETIDs: {unique_count:,}")
    print(f"Duplicates removed: {duplicates_removed:,}")
    print(f"Duplicate fraction: {duplicates_removed / total_rows_before * 100:.2f}%")

    t3 = time.time()
    print(f"Dedup complete in {t3 - t2:.1f}s")

    # --- Step 4: Write output in 500K-row batches ---
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\nWriting deduplicated catalog to: {OUTPUT_DIR}")
    print(f"Batch size: {BATCH_SIZE:,} rows per file")

    # Reset index for clean slicing
    deduped = deduped.reset_index(drop=True)

    num_batches = (unique_count + BATCH_SIZE - 1) // BATCH_SIZE
    for batch_idx in range(num_batches):
        start = batch_idx * BATCH_SIZE
        end = min(start + BATCH_SIZE, unique_count)
        batch_df = deduped.iloc[start:end]

        out_path = os.path.join(
            OUTPUT_DIR,
            f"desi_dr1_catalog_batch_{batch_idx:04d}.parquet"
        )
        batch_table = pa.Table.from_pandas(batch_df, preserve_index=False)
        pq.write_table(batch_table, out_path)

        if (batch_idx + 1) % 10 == 0 or batch_idx == num_batches - 1:
            print(f"  Wrote batch {batch_idx + 1}/{num_batches} ({len(batch_df):,} rows)")

    t4 = time.time()
    print(f"Write complete in {t4 - t3:.1f}s")

    # --- Step 5: Verification ---
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)

    # Re-read and verify
    output_files = sorted([
        os.path.join(OUTPUT_DIR, f)
        for f in os.listdir(OUTPUT_DIR)
        if f.endswith(".parquet")
    ])

    verify_count = 0
    verify_ids = set()
    for fpath in output_files:
        df = pd.read_parquet(fpath, columns=["targetid"])
        verify_count += len(df)
        verify_ids.update(df["targetid"].tolist())

    verify_unique = len(verify_ids)

    print(f"Output files written: {len(output_files)}")
    print(f"Final row count: {verify_count:,}")
    print(f"Unique TARGETIDs in output: {verify_unique:,}")
    print(f"Remaining duplicates: {verify_count - verify_unique:,}")

    deviation = abs(verify_count - EXPECTED_UNIQUE) / EXPECTED_UNIQUE * 100
    print(f"\nExpected unique spectra: ~{EXPECTED_UNIQUE:,}")
    print(f"Actual unique spectra:   {verify_count:,}")
    print(f"Deviation from expected: {deviation:.2f}%")

    if deviation < 5:
        print("PASS: Final count is within 5% of expected 17.65M")
    else:
        print(f"NOTE: Deviation is {deviation:.2f}% from expected (may indicate "
              "the input had more/fewer unique spectra than anticipated)")

    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.1f}s")

    # Summary block
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Input:  {total_rows_before:,} rows across {len(parquet_files)} files")
    print(f"  Output: {verify_count:,} rows across {len(output_files)} files")
    print(f"  Deduped: {duplicates_removed:,} duplicate rows removed")
    print(f"  Verified: {verify_count - verify_unique} remaining duplicates")
    print("=" * 60)


if __name__ == "__main__":
    main()
