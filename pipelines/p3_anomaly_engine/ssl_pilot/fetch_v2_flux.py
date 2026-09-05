#!/usr/bin/env python3
"""Fetch the 496-bin flux array for the 1,244 objects in the sealed v2
recovery-benchmark reference catalogue (`flagship_sample_v2.parquet`,
columns: targetid/anomaly_score/mean_mse/survey/program/healpix/...) so
the Row12 SSL model can be scored on the SAME known objects the v2
autoencoder catalogue was benchmarked against.

Re-downloads only the DISTINCT (survey, program, healpix) coadds these
1,244 objects live in (typically far fewer than 1,244, since anomalies
cluster in groups) -- reuses `stage_row12_flux.py`'s extraction function
unmodified.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("stage_row12_flux", HERE / "stage_row12_flux.py")
stage_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage_mod)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--v2-sample", type=Path, required=True, help="flagship_sample_v2.parquet")
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--audit-log", type=Path, required=True)
    args = ap.parse_args()

    v2 = pq.read_table(args.v2_sample).to_pylist()
    wanted_targetids = {int(r["targetid"]) for r in v2}
    groups: dict[tuple, list[dict]] = {}
    for r in v2:
        key = (r["survey"], r["program"], int(r["healpix"]))
        groups.setdefault(key, []).append(r)

    module = stage_mod.load_archived_inference_module()
    out_rows = []
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        for (survey, program, healpix), members in sorted(groups.items()):
            rel_path = f"healpix/{survey}/{program}/{healpix // 100}/{healpix}/coadd-{survey}-{program}-{healpix}.fits"
            record = {"survey": survey, "program": program, "healpix": healpix, "n_wanted": len(members)}
            try:
                coadd_path = stage_mod.download_coadd(rel_path, tmp)
            except stage_mod.StageError as exc:
                record.update({"status": "download_failed", "error": str(exc)})
                with open(args.audit_log, "a") as fh:
                    fh.write(json.dumps(record) + "\n")
                continue
            try:
                rows, fiberstatus_col = stage_mod.extract_group_flux(coadd_path, module)
            finally:
                coadd_path.unlink(missing_ok=True)

            by_tid = {r["targetid"]: r for r in rows}
            matched = 0
            for m in members:
                tid = int(m["targetid"])
                if tid in by_tid:
                    row = by_tid[tid]
                    out_rows.append(
                        {
                            "targetid": tid,
                            "target_ra": row["target_ra"],
                            "target_dec": row["target_dec"],
                            "flux": row["flux"],
                            "anomaly_score_v2": m["anomaly_score"],
                            "survey": survey,
                            "program": program,
                            "healpix": healpix,
                        }
                    )
                    matched += 1
            record.update({"status": "ok", "matched": matched})
            with open(args.audit_log, "a") as fh:
                fh.write(json.dumps(record) + "\n")
            print(f"{survey}/{program}/{healpix}: matched {matched}/{len(members)}", flush=True)

    missing = wanted_targetids - {r["targetid"] for r in out_rows}
    if missing:
        print(f"WARNING: {len(missing)}/{len(wanted_targetids)} v2 targetids not recovered", file=sys.stderr)

    table = pa.table(
        {
            "targetid": pa.array([r["targetid"] for r in out_rows], type=pa.int64()),
            "target_ra": pa.array([r["target_ra"] for r in out_rows], type=pa.float64()),
            "target_dec": pa.array([r["target_dec"] for r in out_rows], type=pa.float64()),
            "flux": pa.array([r["flux"] for r in out_rows], type=pa.list_(pa.float32())),
            "anomaly_score_v2": pa.array([r["anomaly_score_v2"] for r in out_rows], type=pa.float64()),
            "survey": pa.array([r["survey"] for r in out_rows], type=pa.string()),
            "program": pa.array([r["program"] for r in out_rows], type=pa.string()),
            "healpix": pa.array([r["healpix"] for r in out_rows], type=pa.int64()),
        }
    )
    pq.write_table(table, args.output)
    print(f"wrote {len(out_rows)}/{len(wanted_targetids)} v2 objects with flux -> {args.output}")


if __name__ == "__main__":
    main()
