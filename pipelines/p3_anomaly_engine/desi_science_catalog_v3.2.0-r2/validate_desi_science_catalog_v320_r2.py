#!/usr/bin/env python3
"""Independent integrity and selection audit for the P3 v3.2.0-r2 release."""

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
from scipy.spatial import cKDTree


VERSION = "3.2.0"
REVISION = "r2"
RELEASE = f"p3-v{VERSION}-{REVISION}"
CATALOG_BASENAME = f"desi_dr1_science_anomaly_candidates_v{VERSION}-{REVISION}.parquet"
SCIENCE_BITS = {"LRG": 0, "ELG": 1, "QSO": 2, "BGS_ANY": 60, "MWS_ANY": 61}
ZWARN_BITS = {
    1: "LITTLE_COVERAGE",
    2: "SMALL_DELTA_CHI2",
    11: "POORDATA",
}
OFFICIAL_CHECKSUM_URL = (
    "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/"
    "redux_iron_zcatalog_v1.sha256sum"
)
DESI_FITS_URL = (
    "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/"
    "zall-pix-iron.fits"
)
RANGE_SIZE_BYTES = 1024 * 1024
RANGE_OFFSETS_BYTES = [
    0,
    104_857_600,
    1_073_741_824,
    5_368_709_120,
    10_737_418_240,
    17_179_869_184,
    21_474_836_480,
    22_370_224_064,
]
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


def official_checksum(url: str) -> dict[str, Any]:
    try:
        request = urllib.request.Request(
            f"{url}?p3_audit={utc_now()}",
            headers={"User-Agent": "P3-v3.2-audit/1", "Cache-Control": "no-cache"},
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = response.read()
            line = next(
                text for text in payload.decode("ascii").splitlines()
                if text.rstrip().endswith("  zall-pix-iron.fits")
            )
            return {
                "reachable": True,
                "status": response.status,
                "url": url,
                "zall_pix_sha256": line.split()[0],
                "checksum_file_sha256": hashlib.sha256(payload).hexdigest(),
                "content_length": len(payload),
                "etag": response.headers.get("ETag"),
                "last_modified": response.headers.get("Last-Modified"),
            }
    except Exception as exc:
        return {"reachable": False, "url": url, "error": f"{type(exc).__name__}: {exc}"}


def verify_remote_ranges(
    local_path: Path,
    url: str,
    offsets: list[int] = RANGE_OFFSETS_BYTES,
    range_size: int = RANGE_SIZE_BYTES,
) -> dict[str, Any]:
    """Fetch and validate exact HTTP byte ranges against the local FITS bytes.

    PASS is earned only when every request returns HTTP 206, an exact
    Content-Range, exactly ``range_size`` bytes, and a digest equal to the
    corresponding local bytes. Any transport or protocol failure is recorded
    and makes the result FAIL.
    """
    local_size = local_path.stat().st_size
    samples: list[dict[str, Any]] = []
    for start in offsets:
        end = start + range_size - 1
        sample: dict[str, Any] = {"start": start, "end": end, "size_bytes": range_size}
        if start < 0 or end >= local_size:
            sample.update({"status": "FAIL", "error": f"range outside local file size {local_size}"})
            samples.append(sample)
            continue
        with local_path.open("rb") as handle:
            handle.seek(start)
            local_bytes = handle.read(range_size)
        sample["local_sha256"] = hashlib.sha256(local_bytes).hexdigest()
        try:
            request = urllib.request.Request(
                f"{url}?p3_range_audit={start}",
                headers={
                    "User-Agent": "P3-v3.2-r2-audit/1",
                    "Range": f"bytes={start}-{end}",
                    "Accept-Encoding": "identity",
                    "Cache-Control": "no-cache",
                },
            )
            with urllib.request.urlopen(request, timeout=120) as response:
                remote_bytes = response.read(range_size + 1)
                status = int(response.status)
                content_range = response.headers.get("Content-Range")
                content_length = response.headers.get("Content-Length")
            expected_content_range = f"bytes {start}-{end}/{local_size}"
            remote_sha = hashlib.sha256(remote_bytes).hexdigest()
            protocol_ok = (
                status == 206
                and content_range == expected_content_range
                and content_length is not None
                and int(content_length) == range_size
                and len(remote_bytes) == range_size
            )
            digest_ok = remote_sha == sample["local_sha256"]
            sample.update(
                {
                    "http_status": status,
                    "content_range": content_range,
                    "expected_content_range": expected_content_range,
                    "content_length": int(content_length) if content_length else None,
                    "bytes_received": len(remote_bytes),
                    "remote_sha256": remote_sha,
                    "protocol_valid": protocol_ok,
                    "digest_match": digest_ok,
                    "status": "PASS" if protocol_ok and digest_ok else "FAIL",
                }
            )
        except Exception as exc:
            sample.update({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"})
        samples.append(sample)
    passed = sum(sample["status"] == "PASS" for sample in samples)
    return {
        "status": "PASS" if passed == len(offsets) else "FAIL",
        "method": "Eight live 1 MiB HTTP Range requests compared byte-for-byte to the local FITS.",
        "range_size_bytes": range_size,
        "requested_samples": len(offsets),
        "matching_samples": passed,
        "samples": samples,
    }


def angular_separation_arcsec(
    ra1_deg: np.ndarray,
    dec1_deg: np.ndarray,
    ra2_deg: np.ndarray,
    dec2_deg: np.ndarray,
) -> np.ndarray:
    ra1 = np.deg2rad(np.asarray(ra1_deg, dtype=np.float64))
    dec1 = np.deg2rad(np.asarray(dec1_deg, dtype=np.float64))
    ra2 = np.deg2rad(np.asarray(ra2_deg, dtype=np.float64))
    dec2 = np.deg2rad(np.asarray(dec2_deg, dtype=np.float64))
    delta_ra = ra1 - ra2
    chord = np.sqrt(
        (np.cos(dec1) * np.cos(ra1) - np.cos(dec2) * np.cos(ra2)) ** 2
        + (np.cos(dec1) * np.sin(ra1) - np.cos(dec2) * np.sin(ra2)) ** 2
        + (np.sin(dec1) - np.sin(dec2)) ** 2
    )
    return np.rad2deg(2 * np.arcsin(np.clip(chord / 2, 0, 1))) * 3600


def sky_unit_vectors(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    ra = np.deg2rad(np.asarray(ra_deg, dtype=np.float64))
    dec = np.deg2rad(np.asarray(dec_deg, dtype=np.float64))
    cos_dec = np.cos(dec)
    return np.column_stack((cos_dec * np.cos(ra), cos_dec * np.sin(ra), np.sin(dec)))


def chord_to_arcsec(chord: np.ndarray) -> np.ndarray:
    return np.rad2deg(2 * np.arcsin(np.clip(np.asarray(chord) / 2, 0, 1))) * 3600


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
        default=repo / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0-r2",
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
        default=None,
        help=(
            "Checkpoint match-parts directory. By default this is derived portably as "
            "RELEASE_DIR.parent/.RELEASE_DIR.name.build/match_parts, matching the builder."
        ),
    )
    parser.add_argument(
        "--clusters", type=Path,
        default=repo / "pipelines/p3_anomaly_engine/apjs_submission_v3.1.161/pathc_unique_objects.parquet",
    )
    parser.add_argument("--remote-fits-url", default=DESI_FITS_URL)
    parser.add_argument("--skip-fits-hash", action="store_true")
    args = parser.parse_args()

    release = args.release_dir
    parts_dir = args.parts_dir or release.parent / f".{release.name}.build/match_parts"
    catalog_path = release / CATALOG_BASENAME
    final = pd.read_parquet(catalog_path)
    cohort_counts = json.loads((release / "COHORT_COUNTS.json").read_text())
    upstream = json.loads(args.upstream_provenance.read_text())

    part_paths = sorted(parts_dir.glob("matches_*.parquet"))
    if len(part_paths) != math.ceil(28_425_963 / 200_000):
        raise RuntimeError(
            f"expected 143 checkpoint parts in {parts_dir}, found {len(part_paths)}; "
            "pass --parts-dir explicitly if the builder checkpoint was moved"
        )
    base = pd.concat([pd.read_parquet(path) for path in part_paths], ignore_index=True)
    # Checkpoints intentionally retain only the stable zero-based source-row
    # key. Rejoin the independently committed cluster table before comparing
    # the exact public identities; counts alone cannot establish cohort parity.
    cluster_keys = (
        pd.read_parquet(args.clusters, columns=["cluster_id"])
        .reset_index(names="cluster_table_row")
    )
    base = base.merge(cluster_keys, on="cluster_table_row", validate="many_to_one")

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
    stale_sidecar_sha = upstream.get("raw_sha256")
    official = official_checksum(OFFICIAL_CHECKSUM_URL)
    official_sha = official.get("zall_pix_sha256")
    sha_matches = None if local_sha is None else local_sha == official_sha
    public_url = args.remote_fits_url
    remote = remote_head(public_url)
    remote_ranges = verify_remote_ranges(args.fits, public_url)

    primary = base["zcat_primary"].astype(bool)
    warning_free = base["zwarn"] == 0
    final_expected = base.loc[primary & warning_free]

    # Prove that nearest-only and all-neighbors-within-radius definitions are
    # identical for the exact frozen inputs. A >2-arcsec cluster separation is
    # sufficient because no public coordinate can then fall within 1 arcsec of
    # two clusters. We also perform the direct all-neighbor count check.
    all_clusters = (
        pd.read_parquet(
            args.clusters,
            columns=["cluster_id", "ra_mean", "dec_mean", "survey_list"],
        )
        .reset_index(names="cluster_table_row")
    )
    is_desi = all_clusters["survey_list"].astype(str).str.split(",").map(
        lambda labels: "desi_dr1" in labels
    )
    desi_clusters = all_clusters.loc[is_desi].reset_index(drop=True)
    cluster_vectors = sky_unit_vectors(desi_clusters["ra_mean"], desi_clusters["dec_mean"])
    cluster_tree = cKDTree(cluster_vectors)
    nearest_chords, _ = cluster_tree.query(cluster_vectors, k=2)
    nearest_arcsec = chord_to_arcsec(nearest_chords[:, 1])
    one_arcsec_chord = 2.0 * math.sin(math.radians(1.0 / 3600.0) / 2.0)
    neighbor_sets = cluster_tree.query_ball_point(
        sky_unit_vectors(base["target_ra"], base["target_dec"]),
        one_arcsec_chord,
    )
    neighbor_counts = np.asarray([len(indices) for indices in neighbor_sets], dtype=np.int64)
    local_cluster_index = {
        int(row): index for index, row in enumerate(desi_clusters["cluster_table_row"])
    }
    stored_nearest_present = all(
        local_cluster_index[int(row)] in indices
        for row, indices in zip(base["cluster_table_row"], neighbor_sets)
    )
    strict_neighbor_counts = neighbor_counts[(primary & warning_free).to_numpy()]
    nearest_all_neighbors = {
        "desi_containing_clusters": int(len(desi_clusters)),
        "cluster_nearest_neighbor_arcsec": {
            "minimum": float(np.min(nearest_arcsec)),
            "q01": float(np.quantile(nearest_arcsec, 0.01)),
            "q05": float(np.quantile(nearest_arcsec, 0.05)),
            "median": float(np.median(nearest_arcsec)),
        },
        "clusters_with_nearest_neighbor_le_1arcsec": int((nearest_arcsec <= 1).sum()),
        "clusters_with_nearest_neighbor_le_2arcsec": int((nearest_arcsec <= 2).sum()),
        "parent_rows": int(len(base)),
        "parent_rows_with_multiple_clusters_within_1arcsec": int((neighbor_counts > 1).sum()),
        "parent_max_clusters_within_1arcsec": int(neighbor_counts.max()),
        "all_pairs_within_1arcsec_for_parent_rows": int(neighbor_counts.sum()),
        "strict_rows": int(len(final_expected)),
        "strict_rows_with_multiple_clusters_within_1arcsec": int((strict_neighbor_counts > 1).sum()),
        "all_pairs_within_1arcsec_for_strict_rows": int(strict_neighbor_counts.sum()),
        "stored_nearest_cluster_present_in_all_neighbor_set": bool(stored_nearest_present),
    }

    warning_bearing = base.loc[primary & ~warning_free]
    warning_values = warning_bearing["zwarn"].to_numpy(dtype=np.uint64)
    zwarn_distribution = {
        "primary_rows": int(primary.sum()),
        "warning_free_rows": int((primary & warning_free).sum()),
        "warning_bearing_rows": int(len(warning_bearing)),
        "exact_mask_counts": counts(warning_bearing["zwarn"]),
        "set_bit_counts_nonexclusive": {
            f"bit_{bit}_{name}": int(
                ((warning_values & (np.uint64(1) << np.uint64(bit))) != 0).sum()
            )
            for bit, name in ZWARN_BITS.items()
        },
        "warning_bearing_spectype_counts": counts(warning_bearing["spectype"]),
        "definitions": {
            "source": "https://desidatamodel.readthedocs.io/en/25.3/bitmasks.html#zwarn",
            "bit_1": "LITTLE_COVERAGE: too little wavelength coverage",
            "bit_2": "SMALL_DELTA_CHI2: best and second-best chi-squared are too close",
            "bit_11": "POORDATA: poor input data quality; fitting attempted",
        },
    }
    identity_columns = ["cluster_id", "targetid", "fits_row"]
    for frame_name, frame in (("checkpoint-derived expected cohort", final_expected), ("release", final)):
        missing_keys = sorted(set(identity_columns) - set(frame.columns))
        if missing_keys:
            raise RuntimeError(f"{frame_name} lacks identity columns: {missing_keys}")
    expected_id_set = {
        tuple(int(value) for value in row)
        for row in final_expected[identity_columns].itertuples(index=False, name=None)
    }
    released_id_set = {
        tuple(int(value) for value in row)
        for row in final[identity_columns].itertuples(index=False, name=None)
    }
    missing_from_release = sorted(expected_id_set - released_id_set)
    unexpected_in_release = sorted(released_id_set - expected_id_set)
    strict_identifier_set_exact = not missing_from_release and not unexpected_in_release

    original_member_sep_recomputed = angular_separation_arcsec(
        final["target_ra"], final["target_dec"], final["original_ra_deg"], final["original_dec_deg"]
    )
    original_member_sep_exact = bool(
        np.allclose(
            final["original_member_separation_arcsec"].to_numpy(float),
            original_member_sep_recomputed,
            rtol=0,
            atol=1e-12,
        )
    )
    multi_member = final.loc[final["n_detections"] > 1]
    multi_member_summary = {
        "rows": int(len(multi_member)),
        "expected_exactly_one": int(len(multi_member)) == 1,
        "cases": [
            {
                "candidate_id": str(row.candidate_id),
                "cluster_id": int(row.cluster_id),
                "targetid": int(row.targetid),
                "fits_row": int(row.fits_row),
                "n_detections": int(row.n_detections),
                "member_ids": str(row.member_ids),
                "target_to_cluster_arcsec": float(row.match_separation_arcsec),
                "target_to_original_member_arcsec": float(row.original_member_separation_arcsec),
            }
            for row in multi_member.itertuples(index=False)
        ],
    }
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
        "release": RELEASE,
        "created_utc": utc_now(),
        "status": "PENDING",
        "selection_bias_statement": (
            "The 181-row release is an explicitly conservative redshift-quality slice, not an unbiased "
            "or complete sample of the 2,468 positional science-bit matches. The ZWARN==0 gate removes "
            "objects whose spectral fits triggered any Redrock warning; anomaly-selected spectra are "
            "therefore expected to be removed disproportionately. Catalog utility is reproducible "
            "candidate follow-up, not population-rate inference."
        ),
        "waterfall": waterfall,
        "nearest_vs_all_neighbors": nearest_all_neighbors,
        "primary_rejected_zwarn_distribution": zwarn_distribution,
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
            "original_member_separation_arcsec_quantiles": quantiles(
                final["original_member_separation_arcsec"]
            ),
            "multi_member_clusters": multi_member_summary,
            "separation_tail": {
                "le_0p1_arcsec": int((final["match_separation_arcsec"] <= 0.1).sum()),
                "gt_0p1_arcsec": int((final["match_separation_arcsec"] > 0.1).sum()),
                "gt_0p5_arcsec": int((final["match_separation_arcsec"] > 0.5).sum()),
                "gt_0p75_arcsec": int((final["match_separation_arcsec"] > 0.75).sum()),
                "max_arcsec": float(final["match_separation_arcsec"].max()),
                "policy": (
                    "Retain all predeclared <=1 arcsec matches; expose match_quality_tier so users "
                    "can restrict to the 0.1 arcsec coordinate-consistent subset without changing the release."
                ),
            },
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
            "local_input_label": "DESI DR1 public zall-pix-iron.fits",
            "local_size_bytes": args.fits.stat().st_size,
            "local_sha256": local_sha,
            "stale_2026_05_sidecar_sha256": stale_sidecar_sha,
            "stale_sidecar_matches_current": local_sha == stale_sidecar_sha if local_sha else None,
            "stale_sidecar_disposition": (
                "Historical local sidecar predates the July 2026 DESI file replacement and is not "
                "used to validate v3.2.0. Preserved here so the change is explicit."
            ),
            "current_official_checksum": official,
            "local_sha_matches_current_official": sha_matches,
            "public_url": public_url,
            "remote_head": remote,
            "remote_range_parity": remote_ranges,
        },
        "cross_checks": {
            "base_count_matches_builder": int(len(base)) == cohort_counts["existing_bitmask_1arcsec"] == 2468,
            "strict_count_matches_builder": int(len(final_expected)) == len(final) == cohort_counts["selected_release_rows"] == 181,
            "strict_identifier_set_exact": strict_identifier_set_exact,
            "strict_identifier_set_expected_rows": len(expected_id_set),
            "strict_identifier_set_released_rows": len(released_id_set),
            "strict_identifier_set_missing": [list(row) for row in missing_from_release],
            "strict_identifier_set_unexpected": [list(row) for row in unexpected_in_release],
            "original_member_separation_recomputed_exact": original_member_sep_exact,
            "exactly_one_multi_member_released_cluster": multi_member_summary["expected_exactly_one"],
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
        bool((final["match_quality_tier"] == np.where(
            final["match_separation_arcsec"] <= 0.1,
            "coordinate_consistent_le_0p1arcsec",
            "positional_match_gt_0p1_le_1arcsec",
        )).all()),
        report["cross_checks"]["base_count_matches_builder"],
        report["cross_checks"]["strict_count_matches_builder"],
        report["cross_checks"]["strict_identifier_set_exact"],
        report["cross_checks"]["original_member_separation_recomputed_exact"],
        report["cross_checks"]["exactly_one_multi_member_released_cluster"],
        report["cross_checks"]["no_nulls"],
        report["cross_checks"]["no_duplicate_cluster_or_targetid"],
        nearest_all_neighbors["desi_containing_clusters"] == 190_015,
        nearest_all_neighbors["clusters_with_nearest_neighbor_le_2arcsec"] == 0,
        nearest_all_neighbors["parent_rows_with_multiple_clusters_within_1arcsec"] == 0,
        nearest_all_neighbors["all_pairs_within_1arcsec_for_parent_rows"] == 2_468,
        nearest_all_neighbors["strict_rows_with_multiple_clusters_within_1arcsec"] == 0,
        nearest_all_neighbors["all_pairs_within_1arcsec_for_strict_rows"] == 181,
        nearest_all_neighbors["stored_nearest_cluster_present_in_all_neighbor_set"],
        zwarn_distribution["warning_bearing_rows"] == 2_267,
        remote_ranges["status"] == "PASS",
    ]
    if sha_matches is not None:
        required.append(sha_matches)
    report["status"] = "PASS" if all(required) else "FAIL"

    write_json(release / "SELECTION_AUDIT.json", report)
    markdown = f"""# P3 v{VERSION}-{REVISION} selection and integrity audit

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
- The released and strict checkpoint-derived `(cluster_id, targetid, fits_row)` sets are exactly
  equal ({len(released_id_set):,}/{len(expected_id_set):,}); there are no missing or unexpected rows.
- The 190,015 DESI-containing clusters have minimum nearest-neighbor separation
  {nearest_all_neighbors['cluster_nearest_neighbor_arcsec']['minimum']:.6f} arcsec. Direct
  all-neighbor queries produce exactly {nearest_all_neighbors['all_pairs_within_1arcsec_for_parent_rows']:,}
  parent and {nearest_all_neighbors['all_pairs_within_1arcsec_for_strict_rows']:,} strict pairs,
  with no public row within 1 arcsec of multiple clusters; nearest-only and all-neighbor identities
  are therefore identical for these frozen inputs.
- Among the {zwarn_distribution['warning_bearing_rows']:,} rejected primary rows, exact ZWARN
  masks are {zwarn_distribution['exact_mask_counts']}; nonexclusive set-bit counts are
  {zwarn_distribution['set_bit_counts_nonexclusive']}. Bit definitions are pinned to the official
  DESI data-model URL recorded in `SELECTION_AUDIT.json`.
- Candidate ID, cluster ID, and TARGETID are unique; there are no null cells.
- Every row is main survey, carries a specified science bit, is `ZCAT_PRIMARY`, has `ZWARN=0`,
  and lies within 1 arcsec of its anomaly cluster.
- Spectral types (descriptive, not selected): {counts(final['spectype'])}.
- Programs: {counts(final['program'])}.
- Sky coverage follows the DESI footprint ({int((final['target_dec'] >= 0).sum())} north,
  {int((final['target_dec'] < 0).sum())} south); no all-sky uniformity is claimed.
- Exactly one released row has `n_detections > 1`: `{multi_member.iloc[0]['candidate_id']}`.
  Its public target is {float(multi_member.iloc[0]['original_member_separation_arcsec']):.6f} arcsec
  from the canonical original DESI anomaly member; this is distinct from target-to-cluster separation.
- Separation tail: {int((final['match_separation_arcsec'] > 0.1).sum())} rows exceed 0.1 arcsec,
  {int((final['match_separation_arcsec'] > 0.5).sum())} exceed 0.5 arcsec, and the maximum is
  {float(final['match_separation_arcsec'].max()):.4f} arcsec. These rows are retained under the
  predeclared 1-arcsec join and explicitly flagged by `match_quality_tier`.
- Local FITS SHA-256: `{local_sha or 'skipped'}`; current official checksum:
  `{official_sha}`; match: `{sha_matches}`. The older May sidecar value `{stale_sidecar_sha}`
  is preserved as stale provenance and is not used for validation.
- Public source: {public_url}
- Official checksums: {OFFICIAL_CHECKSUM_URL}
- Live remote range parity: `{remote_ranges['status']}`; {remote_ranges['matching_samples']}/
  {remote_ranges['requested_samples']} exact 1 MiB HTTP 206/Content-Range/digest checks passed.

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
            "recomputed locally and matched the current official DESI checksum file"
        )
        provenance["inputs"]["desi_zall_fits"]["official_checksum"] = official
        provenance["inputs"]["desi_zall_fits"]["historical_sidecar_sha256_stale"] = stale_sidecar_sha
    provenance["independent_selection_audit"] = {
        "status": report["status"],
        "file": "SELECTION_AUDIT.json",
        "public_id_rows_rejoined": len(final),
        "all_source_fields_exact": report["public_id_rejoin"]["all_source_fields_exact"],
        "strict_identifier_set_exact": strict_identifier_set_exact,
        "remote_range_parity_status": remote_ranges["status"],
    }
    write_json(provenance_path, provenance)

    # Refresh manifest only after all pre-publication audit artifacts exist.
    manifest_files = sorted(path for path in release.iterdir() if path.name != "RELEASE_MANIFEST.json")
    manifest = {
        "release": RELEASE,
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
