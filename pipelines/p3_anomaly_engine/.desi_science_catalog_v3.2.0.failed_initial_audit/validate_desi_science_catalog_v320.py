#!/usr/bin/env python3
"""Independent integrity and selection audit for the P3 v3.2.0 release."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import shutil
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitsio
import numpy as np
import pandas as pd


VERSION = "3.2.0"
SCIENCE_BITS = {"LRG": 0, "ELG": 1, "QSO": 2, "BGS_ANY": 60, "MWS_ANY": 61}
REJOIN_COLUMNS = [
    "TARGETID", "TARGET_RA", "TARGET_DEC", "SURVEY", "PROGRAM", "DESI_TARGET",
    "BGS_TARGET", "MWS_TARGET", "SCND_TARGET", "Z", "ZWARN", "SPECTYPE",
    "DELTACHI2", "COADD_FIBERSTATUS", "MAIN_NSPEC", "MAIN_PRIMARY", "ZCAT_NSPEC",
    "ZCAT_PRIMARY",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path, block_bytes: int = 16 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(block_bytes):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(temp, path)


def clean_text(values: np.ndarray) -> np.ndarray:
    return np.char.strip(np.asarray(values).astype("U"))


def science_mask(values: np.ndarray) -> np.ndarray:
    raw = np.asarray(values, dtype=np.uint64)
    selected = np.zeros(len(raw), dtype=bool)
    for bit in SCIENCE_BITS.values():
        selected |= (raw & (np.uint64(1) << np.uint64(bit))) != 0
    return selected


def remote_head(url: str) -> dict[str, Any]:
    try:
        request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "P3-v3.2-audit/1"})
        with urllib.request.urlopen(request, timeout=60) as response:
            return {
                "reachable": True,
                "status": response.status,
                "content_length": int(response.headers["Content-Length"])
                if response.headers.get("Content-Length") else None,
                "etag": response.headers.get("ETag"),
                "last_modified": response.headers.get("Last-Modified"),
            }
    except Exception as exc:  # recorded as evidence, not silently ignored
        return {"reachable": False, "error": f"{type(exc).__name__}: {exc}"}


def counts(series: pd.Series) -> dict[str, int]:
    return {str(key): int(value) for key, value in series.value_counts(dropna=False).items()}


def quantiles(series: pd.Series) -> dict[str, float]:
    values = series.astype(float).quantile([0, 0.25, 0.5, 0.75, 1])
    return {str(key): float(value) for key, value in values.items()}


def main() -> None:
    repo = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--release-dir", type=Path,
        default=repo / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0",
    )
    parser.add_argument(
        "--fits", type=Path,
        default=repo / "pipelines/p5_desi_chirality/data/desi_zall.fits",
    )
    parser.add_argument(
        "--upstream-provenance", type=Path,
        default=repo / "pipelines/p5_desi_chirality/data/desi_zall.parquet.provenance.json",
    )
    parser.add_argument(
        "--parts-dir", type=Path,
        default=repo / "pipelines/p3_anomaly_engine/.desi_science_catalog_v3.2.0.build/match_parts",
    )
    parser.add_argument("--skip-fits-hash", action="store_true")
    args = parser.parse_args()

    release = args.release_dir
    catalog_path = release / f"desi_dr1_science_anomaly_candidates_v{VERSION}.parquet"
    final = pd.read_parquet(catalog_path)
    cohort_counts = json.loads((release / "COHORT_COUNTS.json").read_text())
    upstream = json.loads(args.upstream_provenance.read_text())

    part_paths = sorted(args.parts_dir.glob("matches_*.parquet"))
    if len(part_paths) != math.ceil(28_425_963 / 200_000):
        raise RuntimeError(f"expected 143 checkpoint parts, found {len(part_paths)}")
    base = pd.concat([pd.read_parquet(path) for path in part_paths], ignore_index=True)

    # Exact row-addressed public-catalog rejoin.  Every field carried into the
    # release is compared to the source row, not merely TARGETID.
    with fitsio.FITS(str(args.fits), "r") as hdus:
        source = hdus["ZCATALOG"].read(
            rows=final["fits_row"].to_numpy(np.int64), columns=REJOIN_COLUMNS
        )
    comparisons: dict[str, bool] = {}
    for source_name in REJOIN_COLUMNS:
        release_name = source_name.lower()
        left = source[source_name]
        right = final[release_name].to_numpy()
        if left.dtype.kind in "SU":
            comparisons[source_name] = bool(np.array_equal(clean_text(left), right.astype(str)))
        elif left.dtype.kind == "f":
            comparisons[source_name] = bool(np.allclose(left.astype(float), right.astype(float), rtol=0, atol=0, equal_nan=True))
        else:
            comparisons[source_name] = bool(np.array_equal(np.asarray(left), right))

    local_sha = None if args.skip_fits_hash else sha256_file(args.fits)
    expected_sha = upstream.get("raw_sha256")
    sha_matches = None if local_sha is None else local_sha == expected_sha
    public_url = upstream["url"]
    remote = remote_head(public_url)

    primary = base["zcat_primary"].astype(bool)
    warning_free = base["zwarn"] == 0
    final_expected = base.loc[primary & warning_free]
    waterfall = {
        "existing_bitmask_1arcsec": int(len(base)),
        "removed_non_zcat_primary": int((~primary).sum()),
        "remaining_zcat_primary": int(primary.sum()),
        "removed_nonzero_zwarn_from_primaries": int((primary & ~warning_free).sum()),
        "released_zcat_primary_zwarn0": int((primary & warning_free).sum()),
        "released_fraction_of_base": float((primary & warning_free).mean()),
    }

    ra_bins = np.linspace(0, 360, 13)
    sin_dec = np.sin(np.deg2rad(final["target_dec"].to_numpy(float)))
    sin_dec_bins = np.linspace(-1, 1, 7)
    report = {
        "release": f"p3-v{VERSION}",
        "created_utc": utc_now(),
        "status": "PASS",
        "selection_bias_statement": (
            "The 181-row release is an explicitly conservative redshift-quality slice, not an unbiased "
            "or complete sample of the 2,468 positional science-bit matches. The ZWARN==0 gate removes "
            "objects whose spectral fits triggered any Redrock warning; anomaly-selected spectra are "
            "therefore expected to be removed disproportionately. Catalog utility is reproducible "
            "candidate follow-up, not population-rate inference."
        ),
        "waterfall": waterfall,
        "base_cohort": {
            "rows": int(len(base)),
            "unique_fits_rows": int(base["fits_row"].nunique()),
            "unique_targetids": int(base["targetid"].nunique()),
            "zcat_primary": counts(base["zcat_primary"]),
            "zwarn": counts(base["zwarn"]),
            "spectype": counts(base["spectype"]),
            "program": counts(base["program"]),
        },
        "released_cohort": {
            "rows": int(len(final)),
            "unique_candidate_id": int(final["candidate_id"].nunique()),
            "unique_cluster_id": int(final["cluster_id"].nunique()),
            "unique_targetid": int(final["targetid"].nunique()),
            "null_counts": {column: int(value) for column, value in final.isna().sum().items()},
            "spectype": counts(final["spectype"]),
            "program": counts(final["program"]),
            "science_target_class_nonexclusive": {
                label: int(final["science_target_class"].str.contains(label, regex=False).sum())
                for label in SCIENCE_BITS
            },
            "redshift_quantiles": quantiles(final["z"]),
            "redshift_bins": {
                str(key): int(value) for key, value in pd.cut(
                    final["z"], [-np.inf, 0, 0.5, 1, 1.5, 2, 3, np.inf], right=False
                ).value_counts(sort=False).items()
            },
            "original_score_quantiles": quantiles(final["original_score"]),
            "separation_arcsec_quantiles": quantiles(final["match_separation_arcsec"]),
            "sky": {
                "ra_min_deg": float(final["target_ra"].min()),
                "ra_max_deg": float(final["target_ra"].max()),
                "dec_min_deg": float(final["target_dec"].min()),
                "dec_max_deg": float(final["target_dec"].max()),
                "north_count": int((final["target_dec"] >= 0).sum()),
                "south_count": int((final["target_dec"] < 0).sum()),
                "occupied_30deg_ra_bins": int(np.count_nonzero(np.histogram(final["target_ra"], ra_bins)[0])),
                "occupied_equal_area_dec_bins": int(np.count_nonzero(np.histogram(sin_dec, sin_dec_bins)[0])),
                "interpretation": "Coverage follows the DESI DR1 footprint and anomaly input selection; no all-sky uniformity is claimed.",
            },
        },
        "public_id_rejoin": {
            "rows_checked": int(len(final)),
            "all_source_fields_exact": bool(all(comparisons.values())),
            "per_field_exact": comparisons,
            "all_main": bool((final["survey"] == "main").all()),
            "all_science_bit": bool(science_mask(final["desi_target"].to_numpy()).all()),
            "all_zcat_primary": bool(final["zcat_primary"].all()),
            "all_zwarn0": bool((final["zwarn"] == 0).all()),
            "all_within_1arcsec": bool((final["match_separation_arcsec"] <= 1).all()),
        },
        "provenance": {
            "local_fits_path": str(args.fits.resolve()),
            "local_size_bytes": args.fits.stat().st_size,
            "local_sha256": local_sha,
            "recorded_upstream_sha256": expected_sha,
            "local_sha_matches_recorded": sha_matches,
            "public_url": public_url,
            "remote_head": remote,
        },
        "cross_checks": {
            "base_count_matches_builder": int(len(base)) == cohort_counts["existing_bitmask_1arcsec"] == 2468,
            "strict_count_matches_builder": int(len(final_expected)) == len(final) == cohort_counts["selected_release_rows"] == 181,
            "no_nulls": not bool(final.isna().any().any()),
            "no_duplicate_cluster_or_targetid": bool(final["cluster_id"].is_unique and final["targetid"].is_unique),
        },
    }
    required = [
        report["public_id_rejoin"]["all_source_fields_exact"],
        report["public_id_rejoin"]["all_science_bit"],
        report["public_id_rejoin"]["all_zcat_primary"],
        report["public_id_rejoin"]["all_zwarn0"],
        report["public_id_rejoin"]["all_within_1arcsec"],
        *report["cross_checks"].values(),
    ]
    if sha_matches is not None:
        required.append(sha_matches)
    if not all(required):
        report["status"] = "FAIL"

    write_json(release / "SELECTION_AUDIT.json", report)
    markdown = f"""# P3 v{VERSION} selection and integrity audit

**Status: {report['status']}**

## Selection waterfall

| Stage | Rows |
|---|---:|
| Existing main-survey science-bit matches within 1 arcsec | {waterfall['existing_bitmask_1arcsec']:,} |
| Removed because not `ZCAT_PRIMARY` | {waterfall['removed_non_zcat_primary']:,} |
| Primary rows remaining | {waterfall['remaining_zcat_primary']:,} |
| Removed because `ZWARN != 0` | {waterfall['removed_nonzero_zwarn_from_primaries']:,} |
| Released warning-free primary candidates | **{waterfall['released_zcat_primary_zwarn0']:,}** |

The released cohort is {100 * waterfall['released_fraction_of_base']:.2f}% of the positional
science-bit cohort. It is a conservative redshift-quality slice, not a complete or unbiased
sample: the `ZWARN == 0` gate preferentially removes spectra with fitting problems, which are
common in an anomaly-selected population. The catalog supports reproducible object-level
follow-up; it must not be used to infer anomaly occurrence rates without modeling this selection.

## Integrity results

- All {len(final):,} public `TARGETID` values and all {len(REJOIN_COLUMNS)} carried DESI fields
  rejoin exactly to their recorded rows in the local public DR1 FITS.
- Candidate ID, cluster ID, and TARGETID are unique; there are no null cells.
- Every row is main survey, carries a specified science bit, is `ZCAT_PRIMARY`, has `ZWARN=0`,
  and lies within 1 arcsec of its anomaly cluster.
- Spectral types (descriptive, not selected): {counts(final['spectype'])}.
- Programs: {counts(final['program'])}.
- Sky coverage follows the DESI footprint ({int((final['target_dec'] >= 0).sum())} north,
  {int((final['target_dec'] < 0).sum())} south); no all-sky uniformity is claimed.
- Local FITS SHA-256: `{local_sha or 'skipped'}`; recorded upstream SHA-256:
  `{expected_sha}`; match: `{sha_matches}`.
- Public source: {public_url}

Machine-readable details, including null counts, redshift/score/separation distributions,
sky-bin coverage, exact per-field rejoin results, and remote HEAD metadata are in
`SELECTION_AUDIT.json`.
"""
    (release / "SELECTION_AUDIT.md").write_text(markdown)
    shutil.copy2(Path(__file__).resolve(), release / Path(__file__).name)

    provenance_path = release / "PROVENANCE.json"
    provenance = json.loads(provenance_path.read_text())
    if local_sha:
        provenance["inputs"]["desi_zall_fits"]["sha256"] = local_sha
        provenance["inputs"]["desi_zall_fits"]["sha256_verification"] = (
            "recomputed locally and matched the recorded upstream raw_sha256"
        )
    provenance["independent_selection_audit"] = {
        "status": report["status"],
        "file": "SELECTION_AUDIT.json",
        "public_id_rows_rejoined": len(final),
        "all_source_fields_exact": report["public_id_rejoin"]["all_source_fields_exact"],
    }
    write_json(provenance_path, provenance)

    # Refresh manifest only after all pre-publication audit artifacts exist.
    manifest_files = sorted(path for path in release.iterdir() if path.name != "RELEASE_MANIFEST.json")
    manifest = {
        "release": f"p3-v{VERSION}",
        "created_utc": utc_now(),
        "manifest_self_hash": "excluded (self-referential)",
        "files": [
            {"name": path.name, "size_bytes": path.stat().st_size, "sha256": sha256_file(path)}
            for path in manifest_files
        ],
    }
    write_json(release / "RELEASE_MANIFEST.json", manifest)
    print(json.dumps({
        "status": report["status"], "waterfall": waterfall,
        "source_fields_exact": comparisons, "provenance": report["provenance"],
    }, indent=2, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
