#!/usr/bin/env python3
"""Row 16 (iv-b): fetch DESI DR1 BGS_BRIGHT-21.5 clustering data + randoms.

Streams each FITS, records sha256 + byte size, converts to a compact parquet
(RA, DEC, Z, WEIGHT[, WEIGHT_FKP]) and DELETES the FITS so peak disk stays
small. Manifest rows are appended to bgs_download_manifest.json.
"""
import hashlib, json, os, subprocess, sys
from pathlib import Path
import numpy as np, pandas as pd
from astropy.table import Table

BASE = "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5"
OUT = Path.home() / "Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/bgs"
OUT.mkdir(parents=True, exist_ok=True)
MAN = OUT / "bgs_download_manifest.json"
TRACER = "BGS_BRIGHT-21.5"
NRAN = int(sys.argv[1]) if len(sys.argv) > 1 else 4
KEEP = ["RA", "DEC", "Z", "WEIGHT", "WEIGHT_FKP", "NZ"]


def sha256(p, buf=1 << 22):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(buf), b""):
            h.update(c)
    return h.hexdigest()


def grab(name):
    pq = OUT / (name.replace(".fits", "") + ".parquet")
    man = json.loads(MAN.read_text()) if MAN.exists() else {}
    if pq.exists() and name in man:
        print("skip", name, flush=True)
        return
    fits = OUT / name
    print("get", name, flush=True)
    subprocess.run(["curl", "-sSfL", "-o", str(fits), f"{BASE}/{name}"], check=True)
    size, dig = fits.stat().st_size, sha256(fits)
    t = Table.read(fits)
    cols = [c for c in KEEP if c in t.colnames]
    df = t[cols].to_pandas().astype({c: np.float64 for c in cols})
    df.to_parquet(pq, index=False)
    fits.unlink()
    man[name] = {"url": f"{BASE}/{name}", "bytes": size, "sha256": dig,
                 "rows": int(len(df)), "columns": cols, "parquet": pq.name,
                 "parquet_bytes": pq.stat().st_size}
    MAN.write_text(json.dumps(man, indent=2))
    print("ok", name, len(df), flush=True)


if __name__ == "__main__":
    for cap in ("NGC", "SGC"):
        grab(f"{TRACER}_{cap}_clustering.dat.fits")
        for i in range(NRAN):
            grab(f"{TRACER}_{cap}_{i}_clustering.ran.fits")
    print("FETCH_DONE", flush=True)
