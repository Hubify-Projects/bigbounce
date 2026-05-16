#!/usr/bin/env python3
"""Fetch DESI DR1 redshift catalog (zall-pix-iron.fits) and convert to parquet.

Source: https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/

This is the canonical DR1 "all redshifts" healpix-coadded catalog. We keep
only the columns relevant to P5 cross-match and analysis (TARGETID,
TARGET_RA, TARGET_DEC, Z, ZWARN, ZERR, SPECTYPE, DESI_TARGET, BGS_TARGET,
MWS_TARGET, SCND_TARGET, TILEID, HEALPIX, COADD_NUMEXP) and drop large
per-pixel arrays.

Usage:
    python scripts/02_fetch_desi_dr1.py
    python scripts/02_fetch_desi_dr1.py --skip-fits-keep   # keep raw .fits

If you do not have network access on this machine, manually download
zall-pix-iron.fits to data/ and re-run; the script will skip the fetch
and convert the local file.
"""
from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_config, write_provenance, sha256_of_file, ensure_dir, resolve_p5_path

# Columns we keep. Anything not in this list is dropped to keep parquet small.
KEEP_COLUMNS = [
    "TARGETID", "TARGET_RA", "TARGET_DEC",
    "Z", "ZERR", "ZWARN",
    "SPECTYPE", "SUBTYPE",
    "DELTACHI2",
    "DESI_TARGET", "BGS_TARGET", "MWS_TARGET", "SCND_TARGET",
    "TILEID", "HEALPIX",
    "COADD_NUMEXP", "COADD_EXPTIME",
    "PROGRAM", "SURVEY",
    "FLUX_G", "FLUX_R", "FLUX_Z",
    "FLUX_W1", "FLUX_W2",
    "EBV",
    "MORPHTYPE",
    "MASKBITS",
    "FRACFLUX_R",
    "REF_CAT",
]


def _download(url: str, dest: Path) -> None:
    print(f"[fetch] {url} -> {dest}")
    with urllib.request.urlopen(url) as resp, open(dest, "wb") as fout:
        shutil.copyfileobj(resp, fout, length=8 * 1024 * 1024)
    print(f"[done] downloaded {dest.stat().st_size / 1e9:.2f} GB")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--skip-fits-keep", action="store_true",
                        help="Keep the raw .fits after parquet conversion (default: delete).")
    args = parser.parse_args()

    cfg = load_config(args.config)
    out_parquet = resolve_p5_path(cfg["paths"]["desi_zall"])
    ensure_dir(out_parquet.parent)
    raw_fits = out_parquet.with_suffix(".fits")

    if out_parquet.exists() and not args.force:
        print(f"[ok] {out_parquet} already present; --force to re-download.")
        return 0

    base = cfg["sources"]["desi_dr1"]["base_url"].rstrip("/") + "/"
    fname = cfg["sources"]["desi_dr1"]["file"]
    url = base + fname

    if not raw_fits.exists() or args.force:
        try:
            _download(url, raw_fits)
        except Exception as e:
            print(
                f"ERROR: download failed: {e}\n"
                f"Manually place the file at {raw_fits} and re-run."
            )
            return 2

    # Convert FITS -> parquet, keeping only relevant columns.
    try:
        from astropy.table import Table
    except ImportError:
        print("ERROR: astropy not installed. `pip install astropy pyarrow`.")
        return 2

    print(f"[convert] {raw_fits} -> {out_parquet}")
    t = Table.read(raw_fits, hdu=1)
    available = set(t.colnames)
    drop_cols = [c for c in t.colnames if c not in KEEP_COLUMNS]
    for c in drop_cols:
        t.remove_column(c)
    print(f"[convert] kept {len(t.colnames)} columns, dropped {len(drop_cols)}; rows={len(t):,}")
    df = t.to_pandas()
    # Decode bytes columns
    for c in df.columns:
        if df[c].dtype == object and len(df[c]) and isinstance(df[c].iloc[0], bytes):
            df[c] = df[c].str.decode("utf-8", errors="replace")
    df.to_parquet(out_parquet, index=False)
    n_rows = len(df)

    sha_fits = sha256_of_file(raw_fits)
    sha_parquet = sha256_of_file(out_parquet)

    if not args.skip_fits_keep:
        raw_fits.unlink()

    write_provenance(out_parquet, {
        "source": "desi-dr1",
        "url": url,
        "raw_sha256": sha_fits,
        "parquet_sha256": sha_parquet,
        "rows_observed": n_rows,
        "rows_expected_approx": int(cfg["sources"]["desi_dr1"]["expected_rows_approx"]),
        "columns_kept": list(df.columns),
        "columns_requested": KEEP_COLUMNS,
        "columns_missing_from_source": sorted(set(KEEP_COLUMNS) - available),
        "config_version": cfg["version"],
        "config_hash": cfg["_config_hash"],
    })
    print(f"[done] rows={n_rows:,} parquet_sha={sha_parquet[:16]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
