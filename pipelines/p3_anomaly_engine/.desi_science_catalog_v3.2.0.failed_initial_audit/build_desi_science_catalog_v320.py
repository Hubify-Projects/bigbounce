#!/usr/bin/env python3
"""Build the P3 v3.2.0 DESI DR1 science-target candidate catalog.

This is a memory-bounded positional rejoin of the committed P3 DESI anomaly
clusters to the public DESI DR1 ``zall-pix-iron.fits`` catalog.  It never
materializes the 28.4 million-row FITS table: explicit columns are read in row
chunks with fitsio, science-target rows are filtered in the chunk, and only
one-arcsecond matches are retained as checkpointed Parquet parts.

The released catalog is deliberately a *candidate* catalog.  Its QC cohort is
the existing DESI main-survey science-bit selection, restricted to the DESI
global primary redshift row (ZCAT_PRIMARY) and a warning-free Redrock fit
(ZWARN == 0).  No SPECTYPE or redshift-value cut is applied after matching.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import shutil
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import fitsio
import numpy as np
import pandas as pd
import pyarrow
import scipy
from scipy.spatial import cKDTree


VERSION = "3.2.0"
MATCH_RADIUS_ARCSEC = 1.0
SCIENCE_BITS = {
    "LRG": 0,
    "ELG": 1,
    "QSO": 2,
    "BGS_ANY": 60,
    "MWS_ANY": 61,
}
FITS_COLUMNS = [
    "TARGETID",
    "TARGET_RA",
    "TARGET_DEC",
    "SURVEY",
    "PROGRAM",
    "DESI_TARGET",
    "BGS_TARGET",
    "MWS_TARGET",
    "SCND_TARGET",
    "Z",
    "ZWARN",
    "SPECTYPE",
    "DELTACHI2",
    "COADD_FIBERSTATUS",
    "MAIN_NSPEC",
    "MAIN_PRIMARY",
    "ZCAT_NSPEC",
    "ZCAT_PRIMARY",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path, chunk_bytes: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(chunk_bytes)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, path)


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    with path.open("a") as handle:
        handle.write(json.dumps(payload, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def clean_text(values: np.ndarray) -> np.ndarray:
    return np.char.strip(np.asarray(values).astype("U"))


def native_array(values: np.ndarray) -> np.ndarray:
    """Return an array whose numeric dtype uses native byte order."""
    array = np.asarray(values)
    if array.dtype.byteorder not in ("=", "|"):
        array = array.astype(array.dtype.newbyteorder("="), copy=False)
    return array


def sky_unit_vectors(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    ra = np.deg2rad(np.asarray(ra_deg, dtype=np.float64))
    dec = np.deg2rad(np.asarray(dec_deg, dtype=np.float64))
    cos_dec = np.cos(dec)
    return np.column_stack((cos_dec * np.cos(ra), cos_dec * np.sin(ra), np.sin(dec)))


def chord_to_arcsec(chord: np.ndarray) -> np.ndarray:
    half = np.clip(np.asarray(chord, dtype=np.float64) / 2.0, 0.0, 1.0)
    return np.rad2deg(2.0 * np.arcsin(half)) * 3600.0


def science_bit_mask(desi_target: np.ndarray) -> np.ndarray:
    # FITS integers are big-endian; a numeric cast both normalizes byte order
    # and preserves high bits 60 and 61 without signed-shift ambiguity.
    bits = np.asarray(desi_target, dtype=np.uint64)
    selected = np.zeros(len(bits), dtype=bool)
    for bit in SCIENCE_BITS.values():
        selected |= (bits & (np.uint64(1) << np.uint64(bit))) != 0
    return selected


def decoded_science_class(desi_target: Iterable[int]) -> list[str]:
    result: list[str] = []
    for raw in desi_target:
        unsigned = int(raw) & ((1 << 64) - 1)
        labels = [name for name, bit in SCIENCE_BITS.items() if unsigned & (1 << bit)]
        result.append("|".join(labels))
    return result


def load_desi_clusters(clusters_path: Path, anomalies_path: Path) -> pd.DataFrame:
    clusters = pd.read_parquet(clusters_path)
    is_desi = clusters["survey_list"].astype(str).str.split(",").map(lambda xs: "desi_dr1" in xs)
    clusters = clusters.loc[is_desi].copy()
    if len(clusters) != 190_015:
        raise RuntimeError(f"expected 190,015 DESI-containing clusters, found {len(clusters):,}")

    anomalies = pd.read_parquet(anomalies_path).reset_index(names="desi_source_row")
    anomaly_scores = anomalies["score"].to_numpy(np.float64)
    chosen_rows: list[int] = []
    for member_ids in clusters["member_ids"].astype(str):
        indices = [
            int(token.removeprefix("desi_dr1_"))
            for token in member_ids.split("|")
            if token.startswith("desi_dr1_")
        ]
        if not indices:
            raise RuntimeError(f"DESI cluster lacks a DESI member: {member_ids}")
        # Canonical original anomaly member: greatest anomaly score, then
        # smallest original row index.  This rule is deterministic and is not
        # affected by FITS match multiplicity.
        chosen_rows.append(min(indices, key=lambda index: (-anomaly_scores[index], index)))

    original = anomalies.iloc[chosen_rows].reset_index(drop=True)
    clusters = clusters.reset_index(drop=True)
    out = clusters.rename(
        columns={
            "ra_mean": "cluster_ra_deg",
            "dec_mean": "cluster_dec_deg",
            "best_score": "cluster_best_score",
        }
    )
    out["desi_source_row"] = original["desi_source_row"].astype(np.int64)
    out["original_internal_tid"] = original["tid"].astype(np.int64)
    out["original_ra_deg"] = original["ra"].astype(np.float64)
    out["original_dec_deg"] = original["dec"].astype(np.float64)
    out["original_score"] = original["score"].astype(np.float64)
    out["original_worst_band"] = original["worst"].astype(str)
    out["original_residual_b"] = original["rB"].astype(np.float64)
    out["original_residual_r"] = original["rR"].astype(np.float64)
    out["original_residual_z"] = original["rZ"].astype(np.float64)
    return out


@dataclass(frozen=True)
class BuildPaths:
    output_dir: Path
    work_dir: Path
    parts_dir: Path
    checkpoint: Path
    progress_log: Path


def make_paths(output_dir: Path) -> BuildPaths:
    work = output_dir.parent / f".{output_dir.name}.build"
    return BuildPaths(
        output_dir=output_dir,
        work_dir=work,
        parts_dir=work / "match_parts",
        checkpoint=work / "checkpoint.json",
        progress_log=work / "progress.jsonl",
    )


def scan_fits(
    fits_path: Path,
    clusters: pd.DataFrame,
    paths: BuildPaths,
    chunk_rows: int,
) -> tuple[list[Path], dict[str, int]]:
    paths.parts_dir.mkdir(parents=True, exist_ok=True)
    tree = cKDTree(sky_unit_vectors(clusters["cluster_ra_deg"], clusters["cluster_dec_deg"]))
    max_chord = 2.0 * math.sin(math.radians(MATCH_RADIUS_ARCSEC / 3600.0) / 2.0)

    signature = {
        "version": VERSION,
        "fits_path": str(fits_path.resolve()),
        "fits_size_bytes": fits_path.stat().st_size,
        "clusters": len(clusters),
        "chunk_rows": chunk_rows,
        "columns": FITS_COLUMNS,
        "radius_arcsec": MATCH_RADIUS_ARCSEC,
    }
    previous: dict[str, Any] = {}
    if paths.checkpoint.exists():
        previous = json.loads(paths.checkpoint.read_text())
        if previous.get("signature") != signature:
            raise RuntimeError(
                "checkpoint signature differs from this run; remove the .build directory "
                "or restore the original arguments"
            )

    totals = dict(previous.get("totals", {})) or {
        "fits_rows_scanned": 0,
        "main_science_rows": 0,
        "one_arcsec_match_rows": 0,
    }
    completed = set(int(v) for v in previous.get("completed_chunk_starts", []))
    part_paths: list[Path] = []
    started = time.time()

    with fitsio.FITS(str(fits_path), "r") as hdus:
        table = hdus["ZCATALOG"]
        n_rows = int(table.get_nrows())
        for start in range(0, n_rows, chunk_rows):
            stop = min(start + chunk_rows, n_rows)
            part_path = paths.parts_dir / f"matches_{start:09d}_{stop:09d}.parquet"
            part_paths.append(part_path)
            if start in completed:
                if not part_path.exists():
                    raise RuntimeError(f"checkpoint lists missing part {part_path}")
                continue

            rows = np.arange(start, stop, dtype=np.int64)
            block = table.read(rows=rows, columns=FITS_COLUMNS)
            survey = clean_text(block["SURVEY"])
            keep = (survey == "main") & science_bit_mask(block["DESI_TARGET"])
            local = np.flatnonzero(keep)
            science_count = int(len(local))

            if science_count:
                coords = sky_unit_vectors(block["TARGET_RA"][local], block["TARGET_DEC"][local])
                distance, cluster_index = tree.query(coords, k=1, distance_upper_bound=max_chord)
                matched = np.isfinite(distance) & (cluster_index < len(clusters))
                selected = local[matched]
                matched_clusters = np.asarray(cluster_index[matched], dtype=np.int64)
                matched_distances = np.asarray(distance[matched], dtype=np.float64)
            else:
                selected = np.array([], dtype=np.int64)
                matched_clusters = np.array([], dtype=np.int64)
                matched_distances = np.array([], dtype=np.float64)

            part = pd.DataFrame(
                {
                    "fits_row": rows[selected],
                    "cluster_table_row": matched_clusters,
                    "match_separation_arcsec": chord_to_arcsec(matched_distances),
                }
            )
            for column in FITS_COLUMNS:
                values = block[column][selected]
                if values.dtype.kind in "SU":
                    values = clean_text(values)
                else:
                    values = native_array(values)
                part[column.lower()] = values
            tmp_part = part_path.with_suffix(".parquet.tmp")
            part.to_parquet(tmp_part, index=False)
            os.replace(tmp_part, part_path)

            chunk_matches = int(len(part))
            totals["fits_rows_scanned"] += stop - start
            totals["main_science_rows"] += science_count
            totals["one_arcsec_match_rows"] += chunk_matches
            completed.add(start)
            state = {
                "signature": signature,
                "fits_rows_total": n_rows,
                "completed_chunk_starts": sorted(completed),
                "last_completed_stop": stop,
                "totals": totals,
                "updated_utc": utc_now(),
                "complete": stop == n_rows,
            }
            atomic_json(paths.checkpoint, state)
            progress = {
                "event": "chunk_complete",
                "start": start,
                "stop": stop,
                "fits_rows_total": n_rows,
                "science_rows_chunk": science_count,
                "matches_chunk": chunk_matches,
                "totals": dict(totals),
                "elapsed_seconds": round(time.time() - started, 3),
                "utc": utc_now(),
            }
            append_jsonl(paths.progress_log, progress)
            print(json.dumps(progress, sort_keys=True), flush=True)
            del block, part, rows

    return part_paths, totals


def dedupe(frame: pd.DataFrame, predicate: pd.Series) -> pd.DataFrame:
    selected = frame.loc[predicate].copy()
    # One row per anomaly cluster.  Nearest angular match wins; ties prefer the
    # more strongly separated Redrock solution, then the smallest public
    # TARGETID and FITS row.  A final TARGETID uniqueness rule resolves the
    # unlikely case in which one DESI spectrum lies within 1 arcsec of two
    # anomaly clusters.
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


def cohort_frames(matches: pd.DataFrame) -> dict[str, pd.DataFrame]:
    yes = pd.Series(True, index=matches.index)
    return {
        "existing_bitmask_1arcsec": dedupe(matches, yes),
        "plus_main_primary": dedupe(matches, matches["main_primary"].astype(bool)),
        "plus_zcat_primary": dedupe(matches, matches["zcat_primary"].astype(bool)),
        "plus_main_primary_zwarn0": dedupe(
            matches, matches["main_primary"].astype(bool) & (matches["zwarn"] == 0)
        ),
        "plus_zcat_primary_zwarn0": dedupe(
            matches, matches["zcat_primary"].astype(bool) & (matches["zwarn"] == 0)
        ),
        "plus_both_primary_zwarn0": dedupe(
            matches,
            matches["main_primary"].astype(bool)
            & matches["zcat_primary"].astype(bool)
            & (matches["zwarn"] == 0),
        ),
        "plus_zcat_primary_zwarn0_fiberstatus0": dedupe(
            matches,
            matches["zcat_primary"].astype(bool)
            & (matches["zwarn"] == 0)
            & (matches["coadd_fiberstatus"] == 0),
        ),
    }


def dataframe_schema(frame: pd.DataFrame) -> list[dict[str, str]]:
    return [{"name": col, "dtype": str(dtype)} for col, dtype in frame.dtypes.items()]


def write_dictionary(path: Path, final: pd.DataFrame) -> None:
    descriptions = {
        "candidate_id": "Stable release-local identifier P3-DESI-000001, ordered by cluster_id.",
        "cluster_id": "Original Path-C positional cluster identifier.",
        "cluster_ra_deg": "Mean right ascension of the original anomaly cluster (ICRS degrees).",
        "cluster_dec_deg": "Mean declination of the original anomaly cluster (ICRS degrees).",
        "original_internal_tid": "Original internal anomaly-stream identifier; not a public DESI TARGETID.",
        "original_score": "Original robust multiband anomaly score.",
        "original_worst_band": "Band producing the largest original residual.",
        "original_residual_b": "Original B-band residual summary.",
        "original_residual_r": "Original R-band residual summary.",
        "original_residual_z": "Original Z-band residual summary.",
        "targetid": "Public DESI TARGETID from DR1 zall-pix-iron.",
        "target_ra": "Public DESI target right ascension (ICRS degrees).",
        "target_dec": "Public DESI target declination (ICRS degrees).",
        "match_separation_arcsec": "Great-circle separation between DESI target and anomaly-cluster mean.",
        "desi_target": "Raw DESI_TARGET bitmask from the public zcatalog.",
        "science_target_class": "Decoded selected DESI science bits: LRG, ELG, QSO, BGS_ANY, MWS_ANY.",
        "z": "Redrock redshift estimate; candidate metadata, not a validation label.",
        "zwarn": "Redrock warning bitmask; final cohort requires zero.",
        "spectype": "Redrock best-fit spectral type; not used to select the final cohort.",
        "zcat_primary": "DESI global primary redshift-row flag; final cohort requires true.",
    }
    lines = [
        "# P3 DESI DR1 candidate catalog data dictionary",
        "",
        "The final cohort requires main-survey science-target bits, a positional match within 1 arcsec,",
        "`ZCAT_PRIMARY == true`, and `ZWARN == 0`. No `SPECTYPE` or redshift cut is applied.",
        "",
        "| Column | Storage type | Meaning |",
        "|---|---|---|",
    ]
    for column, dtype in final.dtypes.items():
        description = descriptions.get(column, "Public DESI zcatalog field or preserved original cluster metadata.")
        lines.append(f"| `{column}` | `{dtype}` | {description} |")
    path.write_text("\n".join(lines) + "\n")


def build_release(
    args: argparse.Namespace,
    clusters: pd.DataFrame,
    parts: list[Path],
    scan_totals: dict[str, int],
    paths: BuildPaths,
) -> dict[str, Any]:
    raw = pd.concat([pd.read_parquet(path) for path in parts], ignore_index=True)
    cluster_fields = clusters[
        [
            "cluster_id",
            "n_detections",
            "n_surveys",
            "survey_list",
            "cluster_ra_deg",
            "cluster_dec_deg",
            "cluster_best_score",
            "member_ids",
            "best_survey",
            "desi_source_row",
            "original_internal_tid",
            "original_ra_deg",
            "original_dec_deg",
            "original_score",
            "original_worst_band",
            "original_residual_b",
            "original_residual_r",
            "original_residual_z",
        ]
    ].reset_index(names="cluster_table_row")
    raw = raw.merge(cluster_fields, on="cluster_table_row", validate="many_to_one")
    raw["science_target_class"] = decoded_science_class(raw["desi_target"])

    cohorts = cohort_frames(raw)
    selected_name = "plus_zcat_primary_zwarn0"
    final = cohorts[selected_name].copy()
    final.insert(0, "candidate_id", [f"P3-DESI-{i:06d}" for i in range(1, len(final) + 1)])
    if not final["cluster_id"].is_unique or not final["targetid"].is_unique:
        raise RuntimeError("final cohort violates cluster_id/TARGETID uniqueness")
    if not (final["match_separation_arcsec"] <= MATCH_RADIUS_ARCSEC + 1e-9).all():
        raise RuntimeError("final cohort contains a match outside 1 arcsec")
    if not final["zcat_primary"].astype(bool).all() or not (final["zwarn"] == 0).all():
        raise RuntimeError("final cohort violates ZCAT_PRIMARY/ZWARN QC gates")

    paths.output_dir.mkdir(parents=True, exist_ok=False)
    catalog_name = f"desi_dr1_science_anomaly_candidates_v{VERSION}.parquet"
    catalog_path = paths.output_dir / catalog_name
    final.to_parquet(catalog_path, index=False)

    counts = {
        "desi_containing_clusters": int(len(clusters)),
        **{name: int(len(frame)) for name, frame in cohorts.items()},
        "selected_release_cohort": selected_name,
        "selected_release_rows": int(len(final)),
        "raw_match_rows_before_deduplication": int(len(raw)),
        "scan_totals": {key: int(value) for key, value in scan_totals.items()},
    }
    atomic_json(paths.output_dir / "COHORT_COUNTS.json", counts)

    qc = {
        "version": VERSION,
        "created_utc": utc_now(),
        "status": "PASS",
        "catalog": catalog_name,
        "selection": {
            "positional_radius_arcsec": MATCH_RADIUS_ARCSEC,
            "survey": "main",
            "desi_target_any_bit": SCIENCE_BITS,
            "zcat_primary": True,
            "zwarn": 0,
            "spectype_cut": None,
            "redshift_cut": None,
        },
        "deduplication": (
            "Nearest angular row per cluster; ties prefer higher DELTACHI2, smaller TARGETID, "
            "then lower FITS row. A second pass enforces unique TARGETID using the same ordering."
        ),
        "assertions": {
            "candidate_id_unique": bool(final["candidate_id"].is_unique),
            "cluster_id_unique": bool(final["cluster_id"].is_unique),
            "targetid_unique": bool(final["targetid"].is_unique),
            "all_within_1arcsec": bool((final["match_separation_arcsec"] <= 1.0 + 1e-9).all()),
            "all_zcat_primary": bool(final["zcat_primary"].astype(bool).all()),
            "all_zwarn0": bool((final["zwarn"] == 0).all()),
            "all_main_survey": bool((final["survey"].astype(str) == "main").all()),
        },
        "spectype_counts_not_selection": {
            str(k): int(v) for k, v in final["spectype"].value_counts(dropna=False).items()
        },
        "program_counts": {str(k): int(v) for k, v in final["program"].value_counts().items()},
        "science_class_counts_nonexclusive": {
            label: int(final["science_target_class"].str.contains(label, regex=False).sum())
            for label in SCIENCE_BITS
        },
        "match_separation_arcsec": {
            "min": float(final["match_separation_arcsec"].min()),
            "median": float(final["match_separation_arcsec"].median()),
            "max": float(final["match_separation_arcsec"].max()),
        },
        "schema": dataframe_schema(final),
    }
    atomic_json(paths.output_dir / "QC_REPORT.json", qc)
    write_dictionary(paths.output_dir / "DATA_DICTIONARY.md", final)

    build_copy = paths.output_dir / "build_desi_science_catalog_v320.py"
    shutil.copy2(Path(__file__).resolve(), build_copy)
    provenance = {
        "version": VERSION,
        "created_utc": utc_now(),
        "command": " ".join(sys.argv),
        "inputs": {
            "clusters": {
                "path": str(args.clusters.resolve()),
                "size_bytes": args.clusters.stat().st_size,
                "sha256": sha256_file(args.clusters),
            },
            "anomalies": {
                "path": str(args.anomalies.resolve()),
                "size_bytes": args.anomalies.stat().st_size,
                "sha256": sha256_file(args.anomalies),
            },
            "desi_zall_fits": {
                "path": str(args.fits.resolve()),
                "size_bytes": args.fits.stat().st_size,
                "sha256": args.fits_sha256 or "not recomputed; use upstream DESI provenance",
                "public_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits",
            },
        },
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scipy": scipy.__version__,
            "fitsio": fitsio.__version__,
            "pyarrow": pyarrow.__version__,
            "chunk_rows": args.chunk_rows,
        },
        "selection_and_deduplication": qc["selection"] | {"deduplication": qc["deduplication"]},
        "counts": counts,
        "reproduction": (
            "Run the bundled build script with the three input paths and the same --chunk-rows. "
            "The checkpointed .build directory is outside this immutable release."
        ),
    }
    atomic_json(paths.output_dir / "PROVENANCE.json", provenance)

    readme = f"""# P3 DESI DR1 science-target anomaly candidates v{VERSION}

This clean release contains only the public-ID-rejoinable DESI DR1 candidate catalog and the
artifacts required to reproduce and audit it. It does not contain the historical Gaia,
eROSITA, LAMOST, SDSS, Planck, or mixed-survey tables.

The released cohort contains **{len(final):,} candidates** selected by a one-arcsecond
positional join to main-survey DESI science targets carrying at least one of the LRG, ELG,
QSO, BGS_ANY, or MWS_ANY `DESI_TARGET` bits, followed by `ZCAT_PRIMARY == true` and
`ZWARN == 0`. These are anomaly **candidates**, not validated astrophysical detections.

Files:

- `{catalog_name}` — released candidate table.
- `DATA_DICTIONARY.md` — field definitions and selection semantics.
- `COHORT_COUNTS.json` — existing-bitmask and stricter-cohort counts.
- `QC_REPORT.json` — machine-readable assertions and descriptive summaries.
- `PROVENANCE.json` — exact inputs, runtime, selection, and build command.
- `build_desi_science_catalog_v320.py` — exact build code.
- `RELEASE_MANIFEST.json` — SHA-256 and byte size for every payload file.

The manifest excludes itself to avoid a self-referential checksum. Historical P3 releases
remain historical and are not moved, deleted, or silently replaced by this release.
"""
    (paths.output_dir / "README.md").write_text(readme)

    payload_files = sorted(path for path in paths.output_dir.iterdir() if path.name != "RELEASE_MANIFEST.json")
    manifest = {
        "release": f"p3-v{VERSION}",
        "created_utc": utc_now(),
        "manifest_self_hash": "excluded (self-referential)",
        "files": [
            {"name": path.name, "size_bytes": path.stat().st_size, "sha256": sha256_file(path)}
            for path in payload_files
        ],
    }
    atomic_json(paths.output_dir / "RELEASE_MANIFEST.json", manifest)
    return {"counts": counts, "qc": qc, "manifest": manifest, "catalog_path": str(catalog_path)}


def parse_args() -> argparse.Namespace:
    repo = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--clusters",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/apjs_submission_v3.1.161/pathc_unique_objects.parquet",
    )
    parser.add_argument(
        "--anomalies",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/apjs_submission_v3.1.161/desi_dr1_anomalies.parquet",
    )
    parser.add_argument(
        "--fits",
        type=Path,
        default=repo / "pipelines/p5_desi_chirality/data/desi_zall.fits",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0",
    )
    parser.add_argument("--chunk-rows", type=int, default=200_000)
    parser.add_argument(
        "--fits-sha256",
        default="",
        help="Optional trusted upstream SHA-256; the 21 GB FITS is not rehashed by default.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.output_dir.exists():
        raise SystemExit(f"refusing to overwrite existing immutable release directory: {args.output_dir}")
    for path in (args.clusters, args.anomalies, args.fits):
        if not path.exists():
            raise SystemExit(f"missing input: {path}")
    if args.chunk_rows <= 0:
        raise SystemExit("--chunk-rows must be positive")

    paths = make_paths(args.output_dir)
    print(f"[{utc_now()}] loading DESI-containing anomaly clusters", flush=True)
    clusters = load_desi_clusters(args.clusters, args.anomalies)
    print(f"[{utc_now()}] loaded {len(clusters):,} clusters; streaming selected FITS columns", flush=True)
    parts, totals = scan_fits(args.fits, clusters, paths, args.chunk_rows)
    print(f"[{utc_now()}] scan complete; building cohort matrices and immutable release", flush=True)
    result = build_release(args, clusters, parts, totals, paths)
    append_jsonl(paths.progress_log, {"event": "release_complete", "utc": utc_now(), **result["counts"]})
    print(json.dumps(result["counts"], indent=2, sort_keys=True), flush=True)
    print(f"[{utc_now()}] release complete: {args.output_dir}", flush=True)


if __name__ == "__main__":
    main()
