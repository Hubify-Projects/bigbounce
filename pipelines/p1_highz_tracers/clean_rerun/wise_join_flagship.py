#!/usr/bin/env python3
"""Phase-3c WISE photometry cross-match join for the AUG-011 flagship
enriched sample, adding IR colors (`w1`/`w2`/`w1_w2`) as an extra feature
`taxonomy_flagship.py`'s `--extra-features` can pull in — the new-generation
analog of how the historical taxonomy pipeline's "IR-bright AGN candidate"
family was built on `w1w2_color` (Stern+2012 criterion, W1-W2 > 0.8).

**Same service as the historical NEOWISE/AllWISE pipeline (still viable, no
fallback needed).** `neowise_crossmatch.py`/`neowise_crossmatch_silver.py`
queried TWO VizieR/IRSA services: (1) the AllWISE catalog (`II/328/allwise`)
via the VizieR TAP sync endpoint (`https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync`)
for `W1mag`/`W2mag`, and (2) the IRSA Gator `neowiser_p1bs_psd` catalog for
per-epoch NEOWISE-R lightcurve variability. This script only needs the W1/W2
COLOR, not the multi-epoch variability statistics, so it targets only the
first of those two — the AllWISE `II/328/allwise` catalog, i.e. exactly the
service the historical `w1w2_color`/`agn_ir_color` fields came from. VizieR
is a live, actively-maintained CDS service (unlike some IRSA legacy
endpoints), so no service fallback (e.g. `astroquery.ipac.irsa`) is used.

The ONLY change from the historical scripts is the client library: they
issued raw `requests.get()` calls against the VizieR TAP endpoint by hand;
this script uses `astroquery.vizier.Vizier` against the SAME catalog ID
(`II/328/allwise`), matching the precedent `crossmatch_flagship.py` already
set when it ported the historical raw-`requests`/hand-parsed-XML SIMBAD/NED
scripts onto `astroquery.simbad`/`astroquery.ipac.ned` for this generation.

**Coordinate source.** Unlike `crossmatch_flagship.py`'s input (`run_scan.py`'s
narrow shard schema, `targetid`/`anomaly_score`/`mean_mse`/`survey`/`program`/
`healpix` only — no ra/dec), this script's input is `enrich_flagship_sample.py`'s
phase-3b OUTPUT, which carries `target_ra`/`target_dec` straight through from
the archived `process_healpix()`'s FIBERMAP columns (see that script's
`EXCLUDED_ARCHIVED_ROW_FIELDS` — only `targetid`/`anomaly_score` are excluded,
so `target_ra`/`target_dec` survive verbatim). No zcatalog re-join is needed;
the sample-vs-zcatalog coordinate-join fallback `crossmatch_flagship.py` uses
is unnecessary here.

**Batching/checkpoint/resume**, reused rather than reimplemented: this module
imports `run_service_queries` (generic per-row query-with-checkpoint loop),
`load_checkpoint`, `save_checkpoint`, and `decode_targetid_str` directly from
`crossmatch_flagship.py`. Fault barrier per row (network/service error) is
handled the same way SIMBAD/NED are: the network-calling `query_wise_cone()`
catches its own exceptions and returns `{"found": False, "error": ...}`
rather than raising, so one bad query never aborts the run — the row is
recorded as unmatched and checkpointed exactly like a genuine no-match, so
resuming after a transient outage recomputes those rows without redownloading
anything already resolved (re-running with a genuinely fixed service would
require clearing that row's checkpoint entry, exactly like SIMBAD/NED).

Cone-search radius defaults to 3 arcsec (crossmatch_flagship.py's default);
when a cone search returns multiple AllWISE candidates, `select_nearest_match`
(a pure, network-free function, unit-tested directly) picks the smallest
angular separation.

Output: a Parquet keyed by `targetid` with `w1`/`w2`/`w1_w2`/
`match_separation_arcsec`/`match_flag` — directly usable as
`taxonomy_flagship.py --extra-features` (its contract: a Parquet keyed by
`targetid` with extra numeric feature columns; `match_flag` is boolean but
still numeric-coercible if ever passed as a feature column). Manifest records
service/catalog/query params, input/output SHA-256, matched/unmatched counts,
and timestamps, matching `crossmatch_flagship.py`'s manifest conventions.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derive_locator_inventory import read_json, require_sha, sha256_file, write_json_atomic  # noqa: E402
from crossmatch_flagship import (  # noqa: E402
    decode_targetid_str,
    load_checkpoint,
    run_service_queries,
    save_checkpoint,
)

DEFAULT_RADIUS_ARCSEC = 3.0
DEFAULT_CHECKPOINT_EVERY = 50
DEFAULT_RATE_LIMIT_SLEEP = 1.0
ALLWISE_CATALOG_ID = "II/328/allwise"
ALLWISE_VIZIER_COLUMNS = ["AllWISE", "RAJ2000", "DEJ2000", "W1mag", "W2mag"]


class WiseJoinError(RuntimeError):
    """Raised when the WISE-join inputs cannot be trusted or joined safely."""


def verify_input_enriched(enriched_path: Path, enriched_manifest: dict[str, Any]) -> None:
    if not enriched_path.is_file():
        raise WiseJoinError(f"input enriched sample is absent: {enriched_path}")
    expected = enriched_manifest.get("output", {}).get("sha256")
    require_sha(expected, "enriched-sample manifest output.sha256")
    observed = sha256_file(enriched_path)
    if observed != expected:
        raise WiseJoinError(
            f"input enriched sample SHA-256 mismatch: expected {expected}, got {observed} for {enriched_path}"
        )


def load_enriched_rows(enriched_path: Path) -> list[dict[str, Any]]:
    import pyarrow.parquet as pq

    table = pq.read_table(enriched_path, columns=["targetid", "target_ra", "target_dec"])
    rows = table.to_pylist()
    if not rows:
        raise WiseJoinError(f"enriched sample has zero rows: {enriched_path}")
    return rows


def select_nearest_match(
    candidates: list[dict[str, Any]], ra: float, dec: float
) -> dict[str, Any] | None:
    """Pure, network-free nearest-match selection among cone-search candidates.

    Each candidate must carry numeric `ra`/`dec` (degrees); `w1`/`w2`/
    `allwise_id` are passed through unchanged. Separation is the small-angle
    planar approximation (`dra * cos(dec)`, `ddec`), which is accurate to
    well under a milli-arcsec at the few-arcsec search radii this pipeline
    uses. Returns the candidate with the smallest separation, augmented with
    `separation_arcsec`, or `None` if `candidates` is empty.
    """
    if not candidates:
        return None
    best: dict[str, Any] | None = None
    best_sep: float | None = None
    for candidate in candidates:
        dra = (candidate["ra"] - ra) * math.cos(math.radians(dec))
        ddec = candidate["dec"] - dec
        separation_arcsec = math.hypot(dra, ddec) * 3600.0
        if best_sep is None or separation_arcsec < best_sep:
            best_sep = separation_arcsec
            best = dict(candidate)
            best["separation_arcsec"] = separation_arcsec
    return best


def _masked_to_optional_float(value: Any) -> float | None:
    """Convert an astropy Table cell (possibly numpy-masked) to a plain float
    or None. Isolated as its own function so tests can exercise it without
    a real astropy Table."""
    if value is None:
        return None
    try:
        import numpy as np

        if np.ma.is_masked(value):
            return None
    except ImportError:  # pragma: no cover - numpy always present in this repo
        pass
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def query_wise_cone(ra: float, dec: float, radius_arcsec: float, timeout: float) -> dict[str, Any]:
    """One AllWISE (`II/328/allwise`) cone search via `astroquery.vizier.Vizier`.

    Network call; never used offline — tests mock this function directly
    (per SIMBAD/NED's pattern in `crossmatch_flagship.py`), never the
    astroquery internals. Catches its own exceptions and returns
    `{"found": False, "error": ...}` rather than raising, so a single bad
    query never aborts the run (fault barrier, matching `query_simbad_cone`/
    `query_ned_cone`).
    """
    try:
        import astropy.units as u
        from astropy.coordinates import SkyCoord
        from astroquery.vizier import Vizier
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise WiseJoinError("astroquery/astropy are required for the AllWISE cross-match") from exc

    vizier = Vizier(columns=ALLWISE_VIZIER_COLUMNS, catalog=ALLWISE_CATALOG_ID)
    vizier.ROW_LIMIT = 20
    vizier.TIMEOUT = timeout
    coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")
    try:
        result = vizier.query_region(coord, radius=radius_arcsec * u.arcsec)
    except Exception as exc:  # noqa: BLE001 — deliberate per-query fault barrier
        return {"found": False, "error": str(exc)}

    if result is None or len(result) == 0:
        return {"found": False}
    table = result[0]
    if len(table) == 0:
        return {"found": False}

    candidates = []
    for row in table:
        candidates.append(
            {
                "ra": float(row["RAJ2000"]),
                "dec": float(row["DEJ2000"]),
                "w1": _masked_to_optional_float(row["W1mag"]) if "W1mag" in table.colnames else None,
                "w2": _masked_to_optional_float(row["W2mag"]) if "W2mag" in table.colnames else None,
                "allwise_id": str(row["AllWISE"]) if "AllWISE" in table.colnames else None,
            }
        )
    nearest = select_nearest_match(candidates, ra, dec)
    if nearest is None:
        return {"found": False}
    return {"found": True, **nearest}


def build_result_row(targetid: int, query_result: dict[str, Any]) -> dict[str, Any]:
    """Turn one `query_wise_cone`-shaped result into an output row.

    Unmatched (no AllWISE candidate within radius, or a query error) yields
    `match_flag=False` with `w1`/`w2`/`w1_w2`/`match_separation_arcsec` all
    null — never a fabricated color. A match with only one of W1/W2 present
    (rare, but AllWISE can carry a null magnitude for one band) yields a null
    `w1_w2` rather than a color computed against a missing band.
    """
    if not query_result.get("found"):
        return {
            "targetid": targetid,
            "w1": None,
            "w2": None,
            "w1_w2": None,
            "match_separation_arcsec": None,
            "match_flag": False,
        }
    w1 = query_result.get("w1")
    w2 = query_result.get("w2")
    w1_w2 = (w1 - w2) if (w1 is not None and w2 is not None) else None
    return {
        "targetid": targetid,
        "w1": w1,
        "w2": w2,
        "w1_w2": w1_w2,
        "match_separation_arcsec": query_result.get("separation_arcsec"),
        "match_flag": True,
    }


def run_wise_join(
    input_enriched: Path,
    input_enriched_manifest: Path,
    checkpoint_path: Path,
    output: Path,
    output_manifest: Path,
    radius_arcsec: float = DEFAULT_RADIUS_ARCSEC,
    timeout: float = 30.0,
    rate_limit_sleep: float = DEFAULT_RATE_LIMIT_SLEEP,
    checkpoint_every: int = DEFAULT_CHECKPOINT_EVERY,
    limit: int | None = None,
    query_fn: Any = query_wise_cone,
) -> dict[str, Any]:
    import pyarrow as pa
    import pyarrow.parquet as pq

    enriched_manifest = read_json(input_enriched_manifest)
    verify_input_enriched(input_enriched, enriched_manifest)

    sample_rows = load_enriched_rows(input_enriched)
    if limit is not None:
        sample_rows = sample_rows[:limit]

    joined_rows = [
        {"targetid": int(row["targetid"]), "ra": float(row["target_ra"]), "dec": float(row["target_dec"])}
        for row in sample_rows
    ]

    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    started_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    query_results = run_service_queries(
        "allwise", query_fn, joined_rows, checkpoint_path, radius_arcsec, timeout, rate_limit_sleep, checkpoint_every,
    )
    finished_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    output_rows = []
    for row in joined_rows:
        key = decode_targetid_str(row)
        result = query_results.get(key, {"found": False, "error": "not_queried"})
        output_rows.append(build_result_row(row["targetid"], result))

    n_matched = sum(1 for r in output_rows if r["match_flag"])
    n_unmatched = len(output_rows) - n_matched

    output.parent.mkdir(parents=True, exist_ok=True)
    tmp_output = output.with_suffix(output.suffix + ".tmp")
    schema = pa.schema(
        [
            ("targetid", pa.int64()),
            ("w1", pa.float64()),
            ("w2", pa.float64()),
            ("w1_w2", pa.float64()),
            ("match_separation_arcsec", pa.float64()),
            ("match_flag", pa.bool_()),
        ]
    )
    pq.write_table(pa.Table.from_pylist(output_rows, schema=schema), tmp_output, compression="zstd")
    import os

    os.replace(tmp_output, output)
    output_sha256 = sha256_file(output)

    import astroquery

    manifest = {
        "manifest_version": "flagship-wise-join/v1",
        "started_utc": started_utc,
        "finished_utc": finished_utc,
        "service": {
            "name": "AllWISE (VizieR)",
            "astroquery_version": astroquery.__version__,
            "client": "astroquery.vizier.Vizier",
            "catalog": ALLWISE_CATALOG_ID,
            "endpoint": "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync",
            "historical_precedent": (
                "same catalog neowise_crossmatch.py/neowise_crossmatch_silver.py queried via raw "
                "requests.get() for w1w2_color; only the client library changed, matching the "
                "raw-requests -> astroquery precedent crossmatch_flagship.py set for SIMBAD/NED"
            ),
        },
        "query_params": {
            "radius_arcsec": radius_arcsec,
            "timeout_seconds": timeout,
            "rate_limit_sleep_seconds": rate_limit_sleep,
            "checkpoint_every": checkpoint_every,
        },
        "input_enriched_sha256": sha256_file(input_enriched),
        "input_enriched_manifest": input_enriched_manifest.name,
        "n_input": len(joined_rows),
        "n_matched": n_matched,
        "n_unmatched": n_unmatched,
        "output": {"file_name": output.name, "sha256": output_sha256},
    }
    write_json_atomic(output_manifest, manifest)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input-enriched", type=Path, required=True, help="enrich_flagship_sample.py's --output Parquet")
    parser.add_argument("--input-enriched-manifest", type=Path, required=True, help="enrich_flagship_sample.py's --manifest-output JSON")
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--output-manifest", type=Path, required=True)
    parser.add_argument("--radius-arcsec", type=float, default=DEFAULT_RADIUS_ARCSEC)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--rate-limit-sleep", type=float, default=DEFAULT_RATE_LIMIT_SLEEP)
    parser.add_argument("--checkpoint-every", type=int, default=DEFAULT_CHECKPOINT_EVERY)
    parser.add_argument("--limit", type=int, default=None, help="cap the number of sample rows processed, for a smoke run")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    manifest = run_wise_join(
        args.input_enriched, args.input_enriched_manifest, args.checkpoint,
        args.output, args.output_manifest,
        radius_arcsec=args.radius_arcsec, timeout=args.timeout,
        rate_limit_sleep=args.rate_limit_sleep, checkpoint_every=args.checkpoint_every,
        limit=args.limit,
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
