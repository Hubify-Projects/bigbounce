#!/usr/bin/env python3
"""Stage row12 pilot flux: stream the selected DESI DR1 iron healpix coadds
(from `row12_group_selection.json`), extract the 496-bin downsampled,
per-spectrum-normalized flux array (the exact same `downsample()` +
normalization the archived, NEVER-MODIFIED `enhanced_18M_inference.py`
uses, imported unmodified by file path -- no re-derivation) for every
science-target spectrum, and write one Parquet shard per group.

Science-target gate (applied BEFORE persisting any row, directly against
the downloaded coadd's own FIBERMAP HDU -- see
`select_row12_groups.py`'s docstring for why this is a valid narrower
provenance path than a separate zcatalog join):
    OBJTYPE == 'TGT' AND COADD_FIBERSTATUS == 0 AND TARGETID > 0
(falls back to FIBERSTATUS if COADD_FIBERSTATUS is absent from this coadd's
FIBERMAP schema -- both are logged in the audit line.)

Each group's row budget (from `select_row12_groups.py`'s PPS allocation)
is sampled, without replacement, from that group's SURVIVING science-target
rows using `numpy.random.Generator(numpy.random.PCG64(seed))` seeded
per-group as `seed_base + healpix` for full reproducibility; if fewer
science-target rows survive than the budget, ALL surviving rows are kept
(honest shortfall, logged -- never padded or fabricated).

Idempotent / resumable: skips any group whose shard file already exists.
Coadd FITS files are deleted immediately after extraction (matches the
RUNBOOK's download-bound, not-disk-bound design).

Usage:
  python3 stage_row12_flux.py --selection row12_group_selection.json \\
      --shard-dir /workspace/row12/shards --audit-log /workspace/row12/stage_audit.jsonl \\
      [--limit N] [--seed-base 20260904]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import tempfile
import time
import types
import urllib.request
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
ARCHIVED_INFERENCE_PATH = REPO_ROOT / "pipelines/p1_highz_tracers/outputs/enhanced_18M/enhanced_18M_inference.py"
DESI_HEALPIX_BASE_URL = "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/"


class StageError(RuntimeError):
    pass


def load_archived_inference_module(path: Path = ARCHIVED_INFERENCE_PATH) -> types.ModuleType:
    """Import `enhanced_18M_inference.py` unmodified, by exact file path --
    same sanctioned pattern `build_calibration.py` uses. We only use its
    pure-numpy `downsample()` helper here; the BigAE model/GPU is not
    needed for staging (raw flux is what we persist, not a score)."""
    spec = importlib.util.spec_from_file_location("enhanced_18M_inference_archived", path)
    if spec is None or spec.loader is None:
        raise StageError(f"cannot load archived inference module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def download_coadd(relative_path: str, dest_dir: Path, retries: int = 3) -> Path:
    url = DESI_HEALPIX_BASE_URL + relative_path
    dest = dest_dir / Path(relative_path).name
    last_exc: Exception | None = None
    for attempt in range(retries):
        try:
            urllib.request.urlretrieve(url, dest)
            return dest
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            time.sleep(2 * (attempt + 1))
    raise StageError(f"failed to download {url}: {last_exc}")


def extract_group_flux(coadd_path: Path, module: types.ModuleType) -> list[dict]:
    """Build the 496-bin normalized flux array for every FIBERMAP row in
    this coadd (identical math to `process_healpix`'s steps 1, lines
    291-305 of the archived module: downsample -> hstack -> nan_to_num ->
    per-spectrum median-abs normalize -> clip [-10, 10]), plus the
    science-target gate columns, WITHOUT running the BigAE model."""
    from astropy.io import fits

    with fits.open(coadd_path, memmap=True) as sp:
        fm = sp["FIBERMAP"].data
        n_obj = len(fm)
        b_flux = sp["B_FLUX"].data
        r_flux = sp["R_FLUX"].data
        z_flux = sp["Z_FLUX"].data

        b_ds = module.downsample(b_flux)
        r_ds = module.downsample(r_flux)
        z_ds = module.downsample(z_flux)
        flux = np.hstack([b_ds, r_ds, z_ds]).astype(np.float32)
        flux = np.nan_to_num(flux, nan=0, posinf=0, neginf=0)
        med = np.median(np.abs(flux), axis=1, keepdims=True)
        med = np.where(med > 0, med, 1.0)
        X = np.clip(flux / med, -10, 10).astype(np.float32)

        names = fm.dtype.names
        objtype = fm["OBJTYPE"] if "OBJTYPE" in names else np.full(n_obj, "", dtype="U8")
        if "COADD_FIBERSTATUS" in names:
            fiberstatus = fm["COADD_FIBERSTATUS"]
            fiberstatus_col = "COADD_FIBERSTATUS"
        elif "FIBERSTATUS" in names:
            fiberstatus = fm["FIBERSTATUS"]
            fiberstatus_col = "FIBERSTATUS"
        else:
            fiberstatus = np.full(n_obj, -1, dtype=np.int64)
            fiberstatus_col = "absent"
        targetid = fm["TARGETID"]
        ra = fm["TARGET_RA"] if "TARGET_RA" in names else np.full(n_obj, np.nan)
        dec = fm["TARGET_DEC"] if "TARGET_DEC" in names else np.full(n_obj, np.nan)

        rows = []
        for i in range(n_obj):
            ot_raw = objtype[i]
            ot = ot_raw.decode("utf-8").strip() if isinstance(ot_raw, bytes) else str(ot_raw).strip()
            tid = int(targetid[i])
            fs = int(fiberstatus[i])
            rows.append(
                {
                    "targetid": tid,
                    "objtype": ot,
                    "fiberstatus": fs,
                    "target_ra": float(ra[i]),
                    "target_dec": float(dec[i]),
                    "flux": X[i].tolist(),
                    "_is_science_target": (ot == "TGT" and fs == 0 and tid > 0),
                }
            )
        return rows, fiberstatus_col


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selection", type=Path, required=True)
    ap.add_argument("--shard-dir", type=Path, required=True)
    ap.add_argument("--audit-log", type=Path, required=True)
    ap.add_argument("--seed-base", type=int, default=20260904)
    ap.add_argument("--limit", type=int, default=None, help="only process the first N groups (smoke test)")
    args = ap.parse_args()

    args.shard_dir.mkdir(parents=True, exist_ok=True)
    args.audit_log.parent.mkdir(parents=True, exist_ok=True)

    selection = json.load(open(args.selection))
    groups = selection["groups"]
    if args.limit is not None:
        groups = groups[: args.limit]

    module = load_archived_inference_module()

    import pyarrow as pa
    import pyarrow.parquet as pq

    total_kept = 0
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        for g in groups:
            survey, program, healpix = g["survey"], g["program"], g["healpix"]
            shard_path = args.shard_dir / f"row12_{survey}_{program}_{healpix}.parquet"
            if shard_path.exists():
                continue

            record = {
                "survey": survey,
                "program": program,
                "healpix": healpix,
                "row_budget": g["row_budget"],
            }
            try:
                coadd_path = download_coadd(g["coadd_relative_path"], tmp)
            except StageError as exc:
                record.update({"status": "download_failed", "error": str(exc)})
                with open(args.audit_log, "a") as fh:
                    fh.write(json.dumps(record) + "\n")
                continue

            try:
                rows, fiberstatus_col = extract_group_flux(coadd_path, module)
            finally:
                coadd_path.unlink(missing_ok=True)

            sci_rows = [r for r in rows if r["_is_science_target"]]
            budget = g["row_budget"]
            if budget <= 0 or not sci_rows:
                kept = []
            elif len(sci_rows) <= budget:
                kept = sci_rows
            else:
                rng = np.random.Generator(np.random.PCG64(args.seed_base + int(healpix)))
                idx = rng.choice(len(sci_rows), size=budget, replace=False)
                kept = [sci_rows[i] for i in idx]

            for r in kept:
                r.pop("_is_science_target", None)

            record.update(
                {
                    "status": "ok",
                    "coadd_rows": len(rows),
                    "science_target_rows": len(sci_rows),
                    "kept": len(kept),
                    "shortfall": max(0, budget - len(sci_rows)),
                    "fiberstatus_column_used": fiberstatus_col,
                }
            )
            with open(args.audit_log, "a") as fh:
                fh.write(json.dumps(record) + "\n")

            if kept:
                table = pa.table(
                    {
                        "targetid": pa.array([r["targetid"] for r in kept], type=pa.int64()),
                        "objtype": pa.array([r["objtype"] for r in kept], type=pa.string()),
                        "fiberstatus": pa.array([r["fiberstatus"] for r in kept], type=pa.int64()),
                        "target_ra": pa.array([r["target_ra"] for r in kept], type=pa.float64()),
                        "target_dec": pa.array([r["target_dec"] for r in kept], type=pa.float64()),
                        "survey": pa.array([survey] * len(kept), type=pa.string()),
                        "program": pa.array([program] * len(kept), type=pa.string()),
                        "healpix": pa.array([healpix] * len(kept), type=pa.int64()),
                        "flux": pa.array([r["flux"] for r in kept], type=pa.list_(pa.float32())),
                    }
                )
                pq.write_table(table, shard_path)
                total_kept += len(kept)

            print(f"{survey}/{program}/{healpix}: kept {len(kept)}/{budget} (total {total_kept})", flush=True)

    print(f"DONE: {total_kept} rows staged across {len(groups)} groups")


if __name__ == "__main__":
    main()
