#!/usr/bin/env python3
"""Ingest Tempel+2014 SDSS DR10 FoF galaxy catalog into parquet.

Source:
    https://cdsarc.cds.unistra.fr/ftp/J/A+A/566/A1/galaxies.dat.gz
    Tempel et al. 2014, A&A 566 A1, arXiv:1402.1350.

Schema (per ReadMe):
    GalID    (bytes  1-  6) int
    specID   (bytes  8- 26) int (SDSS DR10 spectroscopic objectID; 0 if missing)
    objID    (bytes 28- 46) int (SDSS DR10 photometric objectID)
    GroupID  (bytes 49- 53) int (0 = isolated)
    Ngal     (bytes 57- 59) int (richness = multiplicity)
    zobs     (bytes 78- 89) float
    RAdeg    (bytes 139-152) float
    DEdeg    (bytes 154-167) float

Output (parquet):
    pipelines/p5_desi_chirality/data/desi_env/tempel/tempel_2014_fof.parquet
    Columns: GalID, specID, objID, GroupID, Ngal (==multiplicity), zobs, ra, dec

We use ra/dec rather than RAdeg/DEdeg to match the downstream
03_tempel_cross_validation.py schema contract.

For galaxies with GroupID == 0 (isolated, no FoF group), Ngal is set to 1 so
the multiplicity-to-class mapping works correctly.
"""
from __future__ import annotations

import gzip
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
TEMPEL_DIR = REPO / "pipelines/p5_desi_chirality/data/desi_env/tempel"
SRC_GZ = TEMPEL_DIR / "galaxies.dat.gz"
OUT_PARQUET = TEMPEL_DIR / "tempel_2014_fof.parquet"


# Byte ranges are 1-based inclusive in the ReadMe; we convert to
# Python 0-based [start, end) slices.
COLSPECS = [
    ("GalID",   0,   6, int),
    ("specID",  7,  26, int),
    ("objID",  27,  46, int),
    ("GroupID",48,  53, int),
    ("Ngal",   56,  59, int),
    ("zobs",   77,  89, float),
    ("ra",    138, 152, float),
    ("dec",   153, 167, float),
]


def _utc() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def parse(path: Path) -> pd.DataFrame:
    t0 = time.time()
    rows = []
    with gzip.open(path, "rt") as fh:
        for i, line in enumerate(fh):
            if not line.strip():
                continue
            row = {}
            for name, lo, hi, cast in COLSPECS:
                tok = line[lo:hi].strip()
                if tok == "":
                    row[name] = 0 if cast is int else float("nan")
                else:
                    try:
                        row[name] = cast(tok)
                    except ValueError:
                        row[name] = 0 if cast is int else float("nan")
            rows.append(row)
            if (i + 1) % 100_000 == 0:
                print(f"  parsed {i+1:,} rows ({time.time()-t0:.1f}s)")
    df = pd.DataFrame(rows)
    # multiplicity convention: GroupID == 0 (no group) -> Ngal := 1
    isolated_mask = df["GroupID"] == 0
    df.loc[isolated_mask, "Ngal"] = 1
    df = df.rename(columns={"Ngal": "multiplicity"})
    print(f"  parsed {len(df):,} total rows in {time.time()-t0:.1f}s")
    return df


def main() -> int:
    if not SRC_GZ.exists():
        print(f"[FATAL] source not found: {SRC_GZ}")
        return 1
    print(f"[{_utc()}] Parsing {SRC_GZ.name} ({SRC_GZ.stat().st_size/1e6:.1f} MB) ...")
    df = parse(SRC_GZ)
    print(f"\nMultiplicity distribution:")
    print(df["multiplicity"].value_counts().sort_index().head(20))
    print(f"\nIsolated (GroupID==0) -> Ngal=1: {(df['GroupID']==0).sum():,} galaxies")
    print(f"Distinct GroupID values: {df['GroupID'].nunique():,}")
    print(f"RA range: [{df['ra'].min():.3f}, {df['ra'].max():.3f}]")
    print(f"Dec range: [{df['dec'].min():.3f}, {df['dec'].max():.3f}]")
    print(f"z range: [{df['zobs'].min():.4f}, {df['zobs'].max():.4f}]")
    t = pa.Table.from_pandas(df, preserve_index=False)
    pq.write_table(t, OUT_PARQUET, compression="zstd")
    print(f"\nWrote {OUT_PARQUET.relative_to(REPO)} ({OUT_PARQUET.stat().st_size/1e6:.1f} MB)")
    # provenance sidecar
    sidecar = OUT_PARQUET.with_suffix(".parquet.provenance.json")
    import json
    sidecar.write_text(json.dumps({
        "source_url": "https://cdsarc.cds.unistra.fr/ftp/J/A+A/566/A1/galaxies.dat.gz",
        "source_paper": "Tempel et al. 2014, A&A 566 A1, arXiv:1402.1350",
        "ingest_utc": _utc(),
        "n_rows": int(len(df)),
        "n_isolated": int((df["GroupID"] == 0).sum()),
        "n_groups": int(df["GroupID"].nunique()),
        "ra_range": [float(df["ra"].min()), float(df["ra"].max())],
        "dec_range": [float(df["dec"].min()), float(df["dec"].max())],
        "z_range": [float(df["zobs"].min()), float(df["zobs"].max())],
    }, indent=2))
    print(f"Wrote provenance sidecar to {sidecar.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
