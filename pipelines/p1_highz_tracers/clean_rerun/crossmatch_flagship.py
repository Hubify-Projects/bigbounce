#!/usr/bin/env python3
"""Phase-3 SIMBAD/NED cone cross-match for the AUG-011 flagship candidate sample.

Port of `pipelines/p1_highz_tracers/scripts/silver_crossmatch.py` (the
historical silver-tier SIMBAD-script/NED-XML cross-match) onto the new
sealed-contract AUG-011 generation's selected sample
(`build_flagship_sample.py`'s output), using `astroquery` instead of the
historical raw-`requests`/hand-parsed-XML implementation.

Coordinate join (why this script exists, not just the historical one
verbatim): `build_flagship_sample.py`'s selected-sample rows carry
`targetid`/`anomaly_score`/`mean_mse`/`survey`/`program`/`healpix` only —
`run_scan.py`'s shard schema has no `target_ra`/`target_dec` columns, unlike
the historical `enhanced_18M_deduped` Parquet the original
`silver_crossmatch.py` read directly. This script recovers RA/Dec by
streaming the SAME sealed `zall-pix-iron.fits` zcatalog the run contract is
bound to (`--zcatalog`, SHA-256-verified against the sample manifest's
`parent.catalog_sha256`) in bounded row chunks, keeping only rows whose
TARGETID is in the sample (peak memory bounded by one chunk plus the sample
size, never the full ~23M-row zcatalog).

Fail-closed, in order:

  1. `--input-sample`'s SHA-256 must equal `--input-manifest`'s
     `output.sha256` (refuses a tampered or stale sample file).
  2. `--zcatalog`'s SHA-256 must equal `--input-manifest`'s
     `parent.catalog_sha256` (refuses cross-matching against a zcatalog that
     is not the one the sample's targetids were vouched against).
  3. Every sample targetid must resolve to a zcatalog coordinate; any that
     do not is a provenance break (the sample supposedly came from targetids
     the SAME sealed zcatalog vouches for) and aborts the run rather than
     silently dropping objects.

Resumable + rate-limit friendly: SIMBAD and NED results are checkpointed to
JSON (`--checkpoint-dir`) after every `--checkpoint-every` queries (default
50, matching the historical script), and a `--rate-limit-sleep` (default
1.0s) pause is inserted between queries per service. Re-running the exact
same command resumes from the checkpoint automatically.

Outputs: a matched table (Parquet), an unmatched table (Parquet, the input
to `taxonomy_flagship.py`), and a crossmatch manifest recording astroquery's
version, the exact query parameters (radius, timeout), start/end
timestamps, and the input sample's SHA-256.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derive_locator_inventory import (  # noqa: E402
    decode_fits_str,
    read_json,
    require_sha,
    sha256_file,
    write_json_atomic,
)

DEFAULT_RADIUS_ARCSEC = 3.0
DEFAULT_CHECKPOINT_EVERY = 50
DEFAULT_RATE_LIMIT_SLEEP = 1.0


class CrossmatchError(RuntimeError):
    """Raised when the crossmatch inputs cannot be trusted or joined."""


def verify_input_sample(sample_path: Path, manifest: dict[str, Any]) -> None:
    if not sample_path.is_file():
        raise CrossmatchError(f"input sample is absent: {sample_path}")
    expected = manifest.get("output", {}).get("sha256")
    require_sha(expected, "input manifest output.sha256")
    observed = sha256_file(sample_path)
    if observed != expected:
        raise CrossmatchError(
            f"input sample SHA-256 mismatch: expected {expected}, got {observed} for {sample_path}"
        )


def verify_zcatalog_for_sample(zcatalog_path: Path, manifest: dict[str, Any]) -> None:
    if not zcatalog_path.is_file():
        raise CrossmatchError(f"zcatalog FITS file is absent: {zcatalog_path}")
    expected = manifest.get("parent", {}).get("catalog_sha256")
    require_sha(expected, "input manifest parent.catalog_sha256")
    observed = sha256_file(zcatalog_path)
    if observed != expected:
        raise CrossmatchError(
            f"zcatalog SHA-256 mismatch: expected {expected}, got {observed} for {zcatalog_path} "
            "(this is not the zcatalog the sample's targetids were vouched against)"
        )


def find_zcat_coordinate_hdu(hdul: Any) -> Any:
    required = {"TARGETID", "TARGET_RA", "TARGET_DEC"}
    for hdu in hdul:
        columns = getattr(hdu, "columns", None)
        if columns is not None and required <= set(columns.names):
            return hdu
    raise CrossmatchError("no HDU in the zcatalog exposes TARGETID/TARGET_RA/TARGET_DEC columns")


def read_coordinates_for_targetids(
    zcatalog_path: Path, targetids: set[int], chunk_rows: int = 500_000
) -> dict[int, tuple[float, float]]:
    """Stream TARGETID/TARGET_RA/TARGET_DEC in bounded row chunks.

    Returns a mapping from targetid -> (ra, dec), containing ONLY the
    requested targetids. Peak memory is bounded by one chunk (`chunk_rows`
    rows) plus the size of the requested targetid set — never the full
    zcatalog row count.
    """
    try:
        from astropy.io import fits
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise CrossmatchError("astropy is required to read the zcatalog FITS file") from exc

    remaining = set(targetids)
    found: dict[int, tuple[float, float]] = {}
    with fits.open(zcatalog_path, memmap=True) as hdul:
        table_hdu = find_zcat_coordinate_hdu(hdul)
        data = table_hdu.data
        n_rows = len(data)
        for start in range(0, n_rows, chunk_rows):
            if not remaining:
                break
            stop = min(start + chunk_rows, n_rows)
            targetid_chunk = data["TARGETID"][start:stop]
            ra_chunk = data["TARGET_RA"][start:stop]
            dec_chunk = data["TARGET_DEC"][start:stop]
            if not (len(targetid_chunk) == len(ra_chunk) == len(dec_chunk)):
                raise CrossmatchError(f"column-length mismatch in zcatalog chunk [{start}:{stop}]")
            for targetid_raw, ra_raw, dec_raw in zip(targetid_chunk, ra_chunk, dec_chunk):
                targetid = int(targetid_raw)
                if targetid in remaining:
                    found[targetid] = (float(ra_raw), float(dec_raw))
                    remaining.discard(targetid)
    return found


def join_sample_with_coordinates(
    sample_rows: list[dict[str, Any]], coordinates: dict[int, tuple[float, float]]
) -> list[dict[str, Any]]:
    """Attach `ra`/`dec` to every sample row; fail closed on any missing join."""
    missing = [row["targetid"] for row in sample_rows if row["targetid"] not in coordinates]
    if missing:
        preview = ", ".join(str(t) for t in missing[:10])
        raise CrossmatchError(
            f"{len(missing)} sample targetid(s) have no zcatalog coordinate (e.g. {preview}); "
            "the sample and zcatalog are not provenance-consistent"
        )
    joined = []
    for row in sample_rows:
        ra, dec = coordinates[row["targetid"]]
        joined.append({**row, "ra": ra, "dec": dec})
    return joined


def decode_targetid_str(row: dict[str, Any]) -> str:
    return str(int(row["targetid"]))


def load_checkpoint(path: Path) -> dict[str, Any]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_checkpoint(path: Path, results: dict[str, Any]) -> None:
    write_json_atomic(path, results)


def query_simbad_cone(ra: float, dec: float, radius_arcsec: float, timeout: float) -> dict[str, Any]:
    """One SIMBAD cone search via astroquery. Network call; never used offline."""
    try:
        import astropy.units as u
        from astropy.coordinates import SkyCoord
        from astroquery.simbad import Simbad
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise CrossmatchError("astroquery/astropy are required for SIMBAD cross-match") from exc

    simbad = Simbad()
    simbad.TIMEOUT = timeout
    try:
        simbad.add_votable_fields("otype")
    except Exception:
        pass
    coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")
    try:
        table = simbad.query_region(coord, radius=radius_arcsec * u.arcsec)
    except Exception as exc:
        return {"found": False, "error": str(exc)}
    if table is None or len(table) == 0:
        return {"found": False}
    row = table[0]
    main_id = row["MAIN_ID"] if "MAIN_ID" in table.colnames else row.get("main_id", "")
    otype = row["OTYPE"] if "OTYPE" in table.colnames else row.get("otype", "")
    return {"found": True, "main_id": str(main_id), "otype": str(otype), "n_matches": len(table)}


def query_ned_cone(ra: float, dec: float, radius_arcsec: float, timeout: float) -> dict[str, Any]:
    """One NED cone search via astroquery. Network call; never used offline."""
    try:
        import astropy.units as u
        from astropy.coordinates import SkyCoord
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise CrossmatchError("astropy is required for NED cross-match") from exc
    try:
        from astroquery.ipac.ned import Ned
    except ImportError:
        from astroquery.ned import Ned  # type: ignore[no-redef]

    Ned.TIMEOUT = timeout
    coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")
    try:
        table = Ned.query_region(coord, radius=radius_arcsec * u.arcsec)
    except Exception as exc:
        message = str(exc)
        if "no object" in message.lower():
            return {"found": False}
        return {"found": False, "error": message}
    if table is None or len(table) == 0:
        return {"found": False}
    row = table[0]
    name = row["Object Name"] if "Object Name" in table.colnames else row.get("Object Name", "")
    otype = row["Type"] if "Type" in table.colnames else row.get("Type", "")
    return {"found": True, "ned_name": str(name), "ned_type": str(otype), "n_matches": len(table)}


def run_service_queries(
    service_name: str,
    query_fn: Any,
    joined_rows: list[dict[str, Any]],
    checkpoint_path: Path,
    radius_arcsec: float,
    timeout: float,
    rate_limit_sleep: float,
    checkpoint_every: int,
) -> dict[str, Any]:
    results = load_checkpoint(checkpoint_path)
    since_save = 0
    for row in joined_rows:
        key = decode_targetid_str(row)
        if key in results:
            continue
        results[key] = query_fn(row["ra"], row["dec"], radius_arcsec, timeout)
        since_save += 1
        if since_save >= checkpoint_every:
            save_checkpoint(checkpoint_path, results)
            since_save = 0
        time.sleep(rate_limit_sleep)
    save_checkpoint(checkpoint_path, results)
    return results


def run_crossmatch(
    input_sample: Path,
    input_manifest: Path,
    zcatalog: Path,
    checkpoint_dir: Path,
    output_matched: Path,
    output_unmatched: Path,
    output_manifest: Path,
    radius_arcsec: float = DEFAULT_RADIUS_ARCSEC,
    timeout: float = 30.0,
    rate_limit_sleep: float = DEFAULT_RATE_LIMIT_SLEEP,
    checkpoint_every: int = DEFAULT_CHECKPOINT_EVERY,
    limit: int | None = None,
) -> dict[str, Any]:
    import pyarrow as pa
    import pyarrow.parquet as pq

    manifest = read_json(input_manifest)
    verify_input_sample(input_sample, manifest)
    verify_zcatalog_for_sample(zcatalog, manifest)

    table = pq.read_table(input_sample)
    sample_rows = table.to_pylist()
    if limit is not None:
        sample_rows = sample_rows[:limit]
    if not sample_rows:
        raise CrossmatchError("input sample has zero rows")

    targetids = {int(row["targetid"]) for row in sample_rows}
    coordinates = read_coordinates_for_targetids(zcatalog, targetids)
    joined_rows = join_sample_with_coordinates(sample_rows, coordinates)

    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    started_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    simbad_results = run_service_queries(
        "simbad", query_simbad_cone, joined_rows, checkpoint_dir / "checkpoint_simbad.json",
        radius_arcsec, timeout, rate_limit_sleep, checkpoint_every,
    )
    ned_results = run_service_queries(
        "ned", query_ned_cone, joined_rows, checkpoint_dir / "checkpoint_ned.json",
        radius_arcsec, timeout, rate_limit_sleep, checkpoint_every,
    )
    finished_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    matched_rows, unmatched_rows = [], []
    for row in joined_rows:
        key = decode_targetid_str(row)
        simbad = simbad_results.get(key, {"found": False, "error": "not_queried"})
        ned = ned_results.get(key, {"found": False, "error": "not_queried"})
        record = {
            "targetid": row["targetid"],
            "ra": row["ra"],
            "dec": row["dec"],
            "anomaly_score": row["anomaly_score"],
            "survey": row["survey"],
            "program": row["program"],
            "healpix": row["healpix"],
            "simbad_found": bool(simbad.get("found")),
            "simbad_main_id": simbad.get("main_id", ""),
            "simbad_otype": simbad.get("otype", ""),
            "ned_found": bool(ned.get("found")),
            "ned_name": ned.get("ned_name", ""),
            "ned_type": ned.get("ned_type", ""),
        }
        if record["simbad_found"] or record["ned_found"]:
            matched_rows.append(record)
        else:
            unmatched_rows.append(record)

    def write_table(rows: list[dict[str, Any]], path: Path) -> str:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        if rows:
            pq.write_table(pa.Table.from_pylist(rows), tmp, compression="zstd")
        else:
            schema = pa.schema(
                [
                    ("targetid", pa.int64()), ("ra", pa.float64()), ("dec", pa.float64()),
                    ("anomaly_score", pa.float64()), ("survey", pa.string()), ("program", pa.string()),
                    ("healpix", pa.int64()), ("simbad_found", pa.bool_()), ("simbad_main_id", pa.string()),
                    ("simbad_otype", pa.string()), ("ned_found", pa.bool_()), ("ned_name", pa.string()),
                    ("ned_type", pa.string()),
                ]
            )
            pq.write_table(pa.Table.from_pylist([], schema=schema), tmp, compression="zstd")
        os.replace(tmp, path)
        return sha256_file(path)

    matched_sha = write_table(matched_rows, output_matched)
    unmatched_sha = write_table(unmatched_rows, output_unmatched)

    import astroquery

    crossmatch_manifest = {
        "manifest_version": "flagship-crossmatch/v1",
        "started_utc": started_utc,
        "finished_utc": finished_utc,
        "services": {
            "astroquery_version": astroquery.__version__,
            "simbad": "astroquery.simbad.Simbad",
            "ned": "astroquery.ipac.ned.Ned",
        },
        "query_params": {
            "radius_arcsec": radius_arcsec,
            "timeout_seconds": timeout,
            "rate_limit_sleep_seconds": rate_limit_sleep,
        },
        "input_sample_sha256": sha256_file(input_sample),
        "input_manifest_parent": manifest.get("parent", {}),
        "n_input": len(joined_rows),
        "n_matched": len(matched_rows),
        "n_unmatched": len(unmatched_rows),
        "n_simbad_found": sum(1 for r in matched_rows if r["simbad_found"]),
        "n_ned_found": sum(1 for r in matched_rows if r["ned_found"]),
        "matched_output": {"file_name": output_matched.name, "sha256": matched_sha},
        "unmatched_output": {"file_name": output_unmatched.name, "sha256": unmatched_sha},
    }
    write_json_atomic(output_manifest, crossmatch_manifest)
    return crossmatch_manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input-sample", type=Path, required=True)
    parser.add_argument("--input-manifest", type=Path, required=True)
    parser.add_argument("--zcatalog", type=Path, required=True)
    parser.add_argument("--checkpoint-dir", type=Path, required=True)
    parser.add_argument("--output-matched", type=Path, required=True)
    parser.add_argument("--output-unmatched", type=Path, required=True)
    parser.add_argument("--output-manifest", type=Path, required=True)
    parser.add_argument("--radius-arcsec", type=float, default=DEFAULT_RADIUS_ARCSEC)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--rate-limit-sleep", type=float, default=DEFAULT_RATE_LIMIT_SLEEP)
    parser.add_argument("--checkpoint-every", type=int, default=DEFAULT_CHECKPOINT_EVERY)
    parser.add_argument("--limit", type=int, default=None, help="cap the number of sample rows processed, for a smoke run")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    manifest = run_crossmatch(
        args.input_sample, args.input_manifest, args.zcatalog, args.checkpoint_dir,
        args.output_matched, args.output_unmatched, args.output_manifest,
        radius_arcsec=args.radius_arcsec, timeout=args.timeout,
        rate_limit_sleep=args.rate_limit_sleep, checkpoint_every=args.checkpoint_every,
        limit=args.limit,
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
