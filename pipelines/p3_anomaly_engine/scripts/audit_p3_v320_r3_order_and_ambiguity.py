#!/usr/bin/env python3
"""Audit P3 gate ordering and positional ambiguity against public DESI DR1.

This script is independent of manuscript prose. It consumes the immutable
v3.2.0-r2 catalog, the full-scan checkpoint parts produced by the released
builder, and the public DESI DR1 ZCATALOG FITS file. It proves the selection
order counterfactually and enumerates every eligible public row within 1 and
2 arcsec of both the released cluster coordinate and canonical historical
DESI-member coordinate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import fitsio
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree


SCIENCE_BITS = (0, 1, 2, 60, 61)
FITS_ROWS = 28_425_963
FITS_SHA256 = "2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b"
SCAN_COLUMNS = [
    "TARGETID",
    "TARGET_RA",
    "TARGET_DEC",
    "SURVEY",
    "DESI_TARGET",
    "ZCAT_PRIMARY",
    "ZWARN",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path, block_bytes: int = 16 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(block_bytes):
            digest.update(block)
    return digest.hexdigest()


def clean_text(values: np.ndarray) -> np.ndarray:
    return np.char.strip(np.asarray(values).astype("U"))


def science_mask(values: np.ndarray) -> np.ndarray:
    raw = np.asarray(values, dtype=np.uint64)
    selected = np.zeros(len(raw), dtype=bool)
    for bit in SCIENCE_BITS:
        selected |= (raw & (np.uint64(1) << np.uint64(bit))) != 0
    return selected


def sky_unit_vectors(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    ra = np.deg2rad(np.asarray(ra_deg, dtype=np.float64))
    dec = np.deg2rad(np.asarray(dec_deg, dtype=np.float64))
    cos_dec = np.cos(dec)
    return np.column_stack((cos_dec * np.cos(ra), cos_dec * np.sin(ra), np.sin(dec)))


def chord_radius(arcsec: float) -> float:
    return 2.0 * math.sin(math.radians(arcsec / 3600.0) / 2.0)


def chord_to_arcsec(chord: np.ndarray) -> np.ndarray:
    return np.rad2deg(2.0 * np.arcsin(np.clip(np.asarray(chord) / 2.0, 0.0, 1.0))) * 3600.0


def dedupe(frame: pd.DataFrame, predicate: pd.Series) -> pd.DataFrame:
    selected = frame.loc[predicate].copy()
    selected = selected.sort_values(
        ["match_separation_arcsec", "deltachi2", "targetid", "fits_row"],
        ascending=[True, False, True, True],
        kind="mergesort",
    ).drop_duplicates("cluster_id", keep="first")
    selected = selected.sort_values(
        ["match_separation_arcsec", "deltachi2", "cluster_id", "fits_row"],
        ascending=[True, False, True, True],
        kind="mergesort",
    ).drop_duplicates("targetid", keep="first")
    return selected.sort_values("cluster_id", kind="mergesort").reset_index(drop=True)


def identity_set(frame: pd.DataFrame) -> set[tuple[int, int, int]]:
    return {
        tuple(int(value) for value in row)
        for row in frame[["cluster_id", "targetid", "fits_row"]].itertuples(index=False, name=None)
    }


def order_audit(parts_dir: Path, clusters_path: Path, released: pd.DataFrame) -> dict:
    parts = sorted(parts_dir.glob("matches_*.parquet"))
    expected_parts = math.ceil(FITS_ROWS / 200_000)
    if len(parts) != expected_parts:
        raise RuntimeError(f"expected {expected_parts} checkpoint parts, found {len(parts)}")
    base = pd.concat([pd.read_parquet(path) for path in parts], ignore_index=True)
    cluster_keys = pd.read_parquet(clusters_path, columns=["cluster_id"]).reset_index(
        names="cluster_table_row"
    )
    base = base.merge(cluster_keys, on="cluster_table_row", validate="many_to_one")

    primary = base["zcat_primary"].astype(bool)
    warning_free = base["zwarn"] == 0
    strict_predicate = primary & warning_free

    # Released algorithm: apply each cohort predicate first, then run the same
    # deterministic cluster/TARGETID tie-break within that cohort.
    parent_deduped = dedupe(base, pd.Series(True, index=base.index))
    primary_deduped = dedupe(base, primary)
    safe_strict = dedupe(base, strict_predicate)

    # Deliberately unsafe counterfactual: dedupe the broad parent first, then
    # filter. Comparing it with safe_strict proves whether order could matter
    # for these exact checkpoint rows.
    unsafe_counterfactual = parent_deduped.loc[
        parent_deduped["zcat_primary"].astype(bool) & (parent_deduped["zwarn"] == 0)
    ].copy()

    safe_ids = identity_set(safe_strict)
    unsafe_ids = identity_set(unsafe_counterfactual)
    released_ids = identity_set(released)
    cluster_multiplicity = base.groupby("cluster_id").size()
    target_multiplicity = base.groupby("targetid").size()

    return {
        "checkpoint_parts": len(parts),
        "raw_checkpoint_match_rows": int(len(base)),
        "raw_unique_clusters": int(base["cluster_id"].nunique()),
        "raw_unique_targetids": int(base["targetid"].nunique()),
        "clusters_with_multiple_parent_rows": int((cluster_multiplicity > 1).sum()),
        "targetids_assigned_to_multiple_clusters": int((target_multiplicity > 1).sum()),
        "predicate_before_dedupe": {
            "zcat_primary_rows": int(primary.sum()),
            "zcat_primary_zwarn0_rows": int(strict_predicate.sum()),
        },
        "deduped_cohorts": {
            "parent": int(len(parent_deduped)),
            "zcat_primary": int(len(primary_deduped)),
            "zcat_primary_zwarn0_safe": int(len(safe_strict)),
            "broad_dedupe_then_strict_filter_unsafe_counterfactual": int(len(unsafe_counterfactual)),
        },
        "safe_equals_released": safe_ids == released_ids,
        "safe_missing_from_release": sorted(safe_ids - released_ids),
        "unexpected_in_release": sorted(released_ids - safe_ids),
        "unsafe_counterfactual_equals_safe_for_these_rows": unsafe_ids == safe_ids,
        "valid_rows_lost_by_unsafe_counterfactual": sorted(safe_ids - unsafe_ids),
        "unsafe_counterfactual_extra_rows": sorted(unsafe_ids - safe_ids),
        "interpretation": (
            "The executable rule applies ZCAT_PRIMARY/ZWARN predicates before deterministic "
            "deduplication within the strict cohort. For these exact checkpoint rows, every "
            "parent match already has a unique cluster_id and TARGETID, so even the deliberately "
            "unsafe order loses zero valid rows; this empirical equality does not redefine the "
            "declared safe order."
        ),
    }


def positional_scan(fits_path: Path, released: pd.DataFrame, chunk_rows: int) -> dict:
    centers = {
        "cluster": sky_unit_vectors(released["cluster_ra_deg"], released["cluster_dec_deg"]),
        "original_member": sky_unit_vectors(released["original_ra_deg"], released["original_dec_deg"]),
    }
    radius_2 = chord_radius(2.0)
    found: dict[str, list[list[dict]]] = {
        kind: [[] for _ in range(len(released))] for kind in centers
    }
    scanned_parent_rows = 0

    with fitsio.FITS(str(fits_path), "r") as hdus:
        table = hdus["ZCATALOG"]
        if table.get_nrows() != FITS_ROWS:
            raise RuntimeError(f"unexpected ZCATALOG row count: {table.get_nrows()}")
        for start in range(0, FITS_ROWS, chunk_rows):
            stop = min(start + chunk_rows, FITS_ROWS)
            block = table[start:stop][SCAN_COLUMNS]
            eligible = (clean_text(block["SURVEY"]) == "main") & science_mask(block["DESI_TARGET"])
            rows = np.flatnonzero(eligible)
            scanned_parent_rows += int(len(rows))
            if not len(rows):
                continue
            vectors = sky_unit_vectors(block["TARGET_RA"][rows], block["TARGET_DEC"][rows])
            tree = cKDTree(vectors)
            for kind, query_vectors in centers.items():
                neighbors = tree.query_ball_point(query_vectors, radius_2)
                for candidate_index, local_indices in enumerate(neighbors):
                    if not local_indices:
                        continue
                    local = np.asarray(local_indices, dtype=np.int64)
                    selected_rows = rows[local]
                    separations = chord_to_arcsec(
                        np.linalg.norm(vectors[local] - query_vectors[candidate_index], axis=1)
                    )
                    for row_index, separation in zip(selected_rows, separations):
                        found[kind][candidate_index].append(
                            {
                                "fits_row": int(start + row_index),
                                "targetid": int(block["TARGETID"][row_index]),
                                "target_ra": float(block["TARGET_RA"][row_index]),
                                "target_dec": float(block["TARGET_DEC"][row_index]),
                                "separation_arcsec": float(separation),
                                "zcat_primary": bool(block["ZCAT_PRIMARY"][row_index]),
                                "zwarn": int(block["ZWARN"][row_index]),
                                "strict_primary_zwarn0": bool(
                                    block["ZCAT_PRIMARY"][row_index] and block["ZWARN"][row_index] == 0
                                ),
                            }
                        )

    if scanned_parent_rows != 20_299_155:
        raise RuntimeError(f"parent-row scan mismatch: {scanned_parent_rows}")

    cases = []
    for candidate_index, released_row in released.reset_index(drop=True).iterrows():
        case = {
            "candidate_id": str(released_row.candidate_id),
            "cluster_id": int(released_row.cluster_id),
            "released_targetid": int(released_row.targetid),
            "released_fits_row": int(released_row.fits_row),
            "released_match_separation_arcsec": float(released_row.match_separation_arcsec),
            "released_original_member_separation_arcsec": float(
                released_row.original_member_separation_arcsec
            ),
            "centers": {},
        }
        for kind in centers:
            rows = sorted(found[kind][candidate_index], key=lambda item: (item["separation_arcsec"], item["fits_row"]))
            radius_summary = {}
            for radius in (1.0, 2.0):
                within = [item for item in rows if item["separation_arcsec"] <= radius + 1e-9]
                competing = [item for item in within if item["fits_row"] != int(released_row.fits_row)]
                radius_summary[f"within_{int(radius)}arcsec"] = {
                    "eligible_rows": len(within),
                    "strict_primary_zwarn0_rows": sum(item["strict_primary_zwarn0"] for item in within),
                    "competing_eligible_rows": len(competing),
                    "competing_strict_primary_zwarn0_rows": sum(
                        item["strict_primary_zwarn0"] for item in competing
                    ),
                }
            case["centers"][kind] = {"counts": radius_summary, "rows_within_2arcsec": rows}
        cases.append(case)

    distribution = released["original_member_separation_arcsec"].astype(float)
    ambiguous = [
        case for case in cases
        if any(
            center["counts"][radius]["competing_eligible_rows"] > 0
            for center in case["centers"].values()
            for radius in ("within_1arcsec", "within_2arcsec")
        )
    ]
    return {
        "public_parent_rows_scanned": scanned_parent_rows,
        "radii_arcsec": [1.0, 2.0],
        "center_definitions": {
            "cluster": "Historical positional-cluster mean used by the declared public-ID recovery cut.",
            "original_member": "Canonical highest-score historical DESI anomaly-member coordinate.",
        },
        "target_to_original_member_separation_arcsec": {
            "minimum": float(distribution.min()),
            "q25": float(distribution.quantile(0.25)),
            "median": float(distribution.median()),
            "q75": float(distribution.quantile(0.75)),
            "q90": float(distribution.quantile(0.90)),
            "q95": float(distribution.quantile(0.95)),
            "q99": float(distribution.quantile(0.99)),
            "maximum": float(distribution.max()),
            "count_gt_0p1": int((distribution > 0.1).sum()),
            "count_gt_0p5": int((distribution > 0.5).sum()),
            "count_gt_0p75": int((distribution > 0.75).sum()),
            "count_gt_1": int((distribution > 1.0).sum()),
            "count_gt_2": int((distribution > 2.0).sum()),
        },
        "candidates_with_any_competing_eligible_row": len(ambiguous),
        "ambiguous_candidate_ids": [case["candidate_id"] for case in ambiguous],
        "cases": cases,
    }


def parse_args() -> argparse.Namespace:
    repo = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0-r2/desi_dr1_science_anomaly_candidates_v3.2.0-r2.parquet",
    )
    parser.add_argument(
        "--fits", type=Path, default=repo / "pipelines/p5_desi_chirality/data/desi_zall.fits"
    )
    parser.add_argument(
        "--clusters",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/apjs_submission_v3.1.161/pathc_unique_objects.parquet",
    )
    parser.add_argument(
        "--parts-dir",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/.desi_science_catalog_v3.2.0-r2.build/match_parts",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/audits/p3_v320_r3_order_and_ambiguity.json",
    )
    parser.add_argument("--chunk-rows", type=int, default=200_000)
    parser.add_argument("--skip-fits-hash", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    released = pd.read_parquet(args.catalog)
    if len(released) != 181:
        raise RuntimeError(f"expected 181 released rows, found {len(released)}")
    fits_sha = None if args.skip_fits_hash else sha256_file(args.fits)
    if fits_sha is not None and fits_sha != FITS_SHA256:
        raise RuntimeError(f"FITS SHA mismatch: {fits_sha}")
    payload = {
        "created_utc": utc_now(),
        "status": "PENDING",
        "inputs": {
            "catalog": str(args.catalog),
            "catalog_sha256": sha256_file(args.catalog),
            "fits": str(args.fits),
            "fits_sha256": fits_sha,
            "expected_fits_sha256": FITS_SHA256,
            "clusters": str(args.clusters),
            "clusters_sha256": sha256_file(args.clusters),
            "parts_dir": str(args.parts_dir),
        },
        "selection_order": order_audit(args.parts_dir, args.clusters, released),
        "positional_ambiguity": positional_scan(args.fits, released, args.chunk_rows),
    }
    required = [
        payload["selection_order"]["safe_equals_released"],
        not payload["selection_order"]["safe_missing_from_release"],
        not payload["selection_order"]["unexpected_in_release"],
        not payload["selection_order"]["valid_rows_lost_by_unsafe_counterfactual"],
        payload["positional_ambiguity"]["public_parent_rows_scanned"] == 20_299_155,
    ]
    payload["status"] = "PASS" if all(required) else "FAIL"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "output": str(args.output),
        "selection_order": payload["selection_order"],
        "positional_summary": {
            key: value for key, value in payload["positional_ambiguity"].items() if key != "cases"
        },
    }, indent=2, sort_keys=True))
    if payload["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
