#!/usr/bin/env python3
"""Build the P3 v3.2.0-r5 warned-primary *secondary* DESI data product.

This product is deliberately not the 181-row primary catalog.  It exposes the
2,267 global-primary positional matches rejected solely because ``ZWARN != 0``
so follow-up users can inspect warning-bearing spectra without weakening the
primary catalog's conservative quality gate.  It performs no physical anomaly
classification and supplies no purity or selection-efficiency estimate.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import platform
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pyarrow


VERSION = "3.2.0-r5"
CATALOG = "desi_dr1_warned_global_primary_aux_v3.2.0-r5.parquet"
EXPECTED_PARTS = 143
EXPECTED_RAW_MATCHES = 2_468
EXPECTED_GLOBAL_PRIMARY = 2_448
EXPECTED_WARNED_PRIMARY = 2_267
EXPECTED_INPUTS = {
    "clusters": "b14deb02ddc374cc30a54e6013c0695d1c35cbf18cef9144245e338d6138c643",
    "anomalies": "0a36b8d6dfb8086c2c417885c99689d7a75b416dad1b030db56477baf103ec65",
}
HISTORICAL_COMMIT = "cdaaa03a72c69d86f011be128d93f261dc5b39a8"
DESI_FITS_SHA256 = "2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b"
STATUS = "SECONDARY_WARNING_BEARING_NOT_PRIMARY_NOT_PHYSICALLY_VALIDATED"
ZWARN_BITS = {
    1: "LITTLE_COVERAGE",
    2: "SMALL_DELTA_CHI2",
    11: "POORDATA",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path, block_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(block_size), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, payload: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, path)


def load_primary_builder(path: Path):
    spec = importlib.util.spec_from_file_location("p3_primary_builder_r2", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import primary builder: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def decode_zwarn(mask: int) -> str:
    labels = [name for bit, name in ZWARN_BITS.items() if int(mask) & (1 << bit)]
    unknown = int(mask) & ~sum(1 << bit for bit in ZWARN_BITS)
    if unknown:
        labels.append(f"UNKNOWN_MASK_0x{unknown:016x}")
    return "|".join(labels)


def exact_set_sha256(frame: pd.DataFrame) -> str:
    rows = [
        [int(row.cluster_id), int(row.targetid), int(row.fits_row), int(row.zwarn)]
        for row in frame.sort_values(["cluster_id", "targetid", "fits_row"]).itertuples()
    ]
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


CLUSTER_COLUMNS = [
    "cluster_id", "n_detections", "n_surveys", "survey_list", "cluster_ra_deg",
    "cluster_dec_deg", "cluster_best_score", "member_ids", "best_survey",
    "desi_source_row", "original_internal_tid", "original_ra_deg", "original_dec_deg",
    "original_score", "original_worst_band", "original_residual_b", "original_residual_r",
    "original_residual_z",
]


def construct_auxiliary(primary, parts_dir: Path, clusters_path: Path, anomalies_path: Path):
    parts = sorted(parts_dir.glob("matches_*.parquet"))
    if len(parts) != EXPECTED_PARTS:
        raise RuntimeError(f"expected {EXPECTED_PARTS} checkpoint parts, found {len(parts)}")
    raw = pd.concat([pd.read_parquet(path) for path in parts], ignore_index=True)
    if len(raw) != EXPECTED_RAW_MATCHES:
        raise RuntimeError(f"expected {EXPECTED_RAW_MATCHES} raw matches, found {len(raw)}")

    clusters = primary.load_desi_clusters(clusters_path, anomalies_path)
    cluster_fields = clusters[CLUSTER_COLUMNS].reset_index(names="cluster_table_row")
    raw = raw.merge(cluster_fields, on="cluster_table_row", validate="many_to_one")
    raw["science_target_class"] = primary.decoded_science_class(raw["desi_target"])

    global_primary = raw.loc[raw["zcat_primary"].astype(bool)].copy()
    warned_pre_dedup = global_primary.loc[global_primary["zwarn"] != 0].copy()
    warned = primary.dedupe(raw, raw["zcat_primary"].astype(bool) & (raw["zwarn"] != 0))
    if len(global_primary) != EXPECTED_GLOBAL_PRIMARY:
        raise RuntimeError(f"expected {EXPECTED_GLOBAL_PRIMARY} global-primary rows")
    if len(warned_pre_dedup) != EXPECTED_WARNED_PRIMARY or len(warned) != EXPECTED_WARNED_PRIMARY:
        raise RuntimeError("warned-primary count or pre/post-dedup exactness failed")
    if not warned["cluster_id"].is_unique or not warned["targetid"].is_unique:
        raise RuntimeError("warned-primary keys are not unique")

    warned = warned.sort_values("cluster_id", kind="mergesort").reset_index(drop=True)
    warned.insert(0, "candidate_id", [f"P3-DESI-WARNED-{i:06d}" for i in range(1, len(warned) + 1)])
    warned.insert(1, "auxiliary_status", STATUS)
    warned.insert(2, "primary_catalog_member", False)
    warned.insert(
        6,
        "match_quality_tier",
        np.where(
            warned["match_separation_arcsec"] <= 0.1,
            "coordinate_consistent_le_0p1arcsec",
            "positional_match_gt_0p1_le_1arcsec",
        ),
    )
    warned.insert(
        7,
        "original_member_separation_arcsec",
        primary.angular_separation_arcsec(
            warned["target_ra"].to_numpy(np.float64),
            warned["target_dec"].to_numpy(np.float64),
            warned["original_ra_deg"].to_numpy(np.float64),
            warned["original_dec_deg"].to_numpy(np.float64),
        ),
    )
    zwarn_position = warned.columns.get_loc("zwarn") + 1
    warned.insert(zwarn_position, "zwarn_hex", [f"0x{int(value):016x}" for value in warned["zwarn"]])
    warned.insert(zwarn_position + 1, "zwarn_decoded_bits", [decode_zwarn(value) for value in warned["zwarn"]])
    if len(warned.columns) != 47:
        raise RuntimeError(f"expected 47 columns, found {len(warned.columns)}")
    return warned, raw, parts


FIELD_DESCRIPTIONS = {
    "candidate_id": "Stable auxiliary-only ID ordered by cluster_id; prefix P3-DESI-WARNED prevents confusion with the primary catalog.",
    "auxiliary_status": "Constant label declaring this row secondary, warning-bearing, non-primary, and not physically validated.",
    "primary_catalog_member": "Always false; the 181-row ZWARN=0 catalog is the primary product.",
    "fits_row": "Zero-based row in the exact DESI DR1 zall-pix-iron ZCATALOG extension.",
    "cluster_table_row": "Zero-based row in the immutable Path-C cluster table.",
    "match_separation_arcsec": "Great-circle target-to-cluster separation in arcseconds; required <=1.",
    "match_quality_tier": "Coordinate-consistent <=0.1 arcsec or positional >0.1 and <=1 arcsec.",
    "original_member_separation_arcsec": "Target-to-canonical-original-member separation; not a selection cut.",
    "targetid": "Public DESI DR1 TARGETID.",
    "target_ra": "Public target ICRS right ascension in degrees.",
    "target_dec": "Public target ICRS declination in degrees.",
    "survey": "DESI survey label; main for this cohort.",
    "program": "DESI observing program.",
    "desi_target": "Raw DESI_TARGET mask.",
    "bgs_target": "Raw BGS_TARGET mask.",
    "mws_target": "Raw MWS_TARGET mask.",
    "scnd_target": "Raw SCND_TARGET mask.",
    "z": "Redrock redshift metadata; not a validation label.",
    "zwarn": "Nonzero Redrock warning mask that caused exclusion from the primary catalog.",
    "zwarn_hex": "ZWARN rendered as an unsigned 64-bit hexadecimal string.",
    "zwarn_decoded_bits": "Pipe-separated exact set bits: LITTLE_COVERAGE, SMALL_DELTA_CHI2, and/or POORDATA.",
    "spectype": "Redrock best-fit spectral type; descriptive only.",
    "deltachi2": "Redrock best-versus-next-best chi-square separation.",
    "coadd_fiberstatus": "Bitwise OR of contributing DESI fiber-status flags.",
    "main_nspec": "Number of main-survey spectra for the target.",
    "main_primary": "Primary-within-main-survey flag.",
    "zcat_nspec": "Number of spectra in the global zcatalog grouping.",
    "zcat_primary": "Global primary redshift-row flag; required true.",
    "cluster_id": "Stable historical positional-cluster identifier.",
    "n_detections": "Number of historical members in the cluster.",
    "n_surveys": "Number of historical surveys in the cluster.",
    "survey_list": "Comma-separated historical survey membership.",
    "cluster_ra_deg": "Historical cluster ICRS mean right ascension.",
    "cluster_dec_deg": "Historical cluster ICRS mean declination.",
    "cluster_best_score": "Maximum historical score in the cluster.",
    "member_ids": "Pipe-separated legacy member row identifiers; not public archive IDs.",
    "best_survey": "Historical survey supplying cluster_best_score.",
    "desi_source_row": "Row of the canonical DESI member in the immutable anomaly table.",
    "original_internal_tid": "Legacy mixed/hash identifier; never use as a public key.",
    "original_ra_deg": "Canonical historical DESI member ICRS right ascension.",
    "original_dec_deg": "Canonical historical DESI member ICRS declination.",
    "original_score": "Frozen historical canonical-S score; uncalibrated ranking metadata only.",
    "original_worst_band": "Historical band with the largest residual summary.",
    "original_residual_b": "Historical B-band residual summary.",
    "original_residual_r": "Historical R-band residual summary.",
    "original_residual_z": "Historical Z-band residual summary.",
    "science_target_class": "Decoded selected DESI science bits.",
}


def write_dictionary(path: Path, frame: pd.DataFrame) -> None:
    missing = set(frame.columns) - set(FIELD_DESCRIPTIONS)
    if missing:
        raise RuntimeError(f"dictionary missing columns: {sorted(missing)}")
    lines = [
        "# P3 warned-primary auxiliary data dictionary",
        "",
        "**Secondary/non-primary/not physically validated.** Every row is a global-primary",
        "DESI positional match with nonzero `ZWARN`; none belongs to the 181-row primary catalog.",
        "",
        "| Column | Storage type | Meaning |", "|---|---|---|",
    ]
    for column, dtype in frame.dtypes.items():
        lines.append(f"| `{column}` | `{dtype}` | {FIELD_DESCRIPTIONS[column]} |")
    path.write_text("\n".join(lines) + "\n")


def payload_manifest(directory: Path) -> dict[str, Any]:
    files = []
    for path in sorted(directory.iterdir()):
        if path.is_file() and path.name != "RELEASE_MANIFEST.json":
            files.append({"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    return {
        "release": f"p3-v{VERSION}",
        "product_role": "SECONDARY_WARNING_BEARING_NOT_PRIMARY_NOT_PHYSICALLY_VALIDATED",
        "files": files,
    }


def repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("cannot locate repository root from script path")


def parse_args() -> argparse.Namespace:
    root = repo_root()
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts-dir", type=Path, required=True)
    parser.add_argument("--clusters", type=Path, required=True)
    parser.add_argument("--anomalies", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--primary-builder", type=Path,
        default=root / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0-r2/build_desi_science_catalog_v320_r2.py",
    )
    parser.add_argument(
        "--primary-provenance", type=Path,
        default=root / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0-r2/PROVENANCE.json",
    )
    parser.add_argument(
        "--clean-replay", type=Path,
        default=root / "project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P3-v3.2.0-r4-CLOSURE/evidence/clean_replay.json",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.output_dir.exists():
        raise RuntimeError(f"output directory already exists: {args.output_dir}")
    for label, path in (("clusters", args.clusters), ("anomalies", args.anomalies)):
        actual = sha256_file(path)
        if actual != EXPECTED_INPUTS[label]:
            raise RuntimeError(f"{label} SHA mismatch: {actual}")
    replay = json.loads(args.clean_replay.read_text())
    if replay.get("status") != "PASS" or replay["replay"]["raw_match_rows_before_deduplication"] != EXPECTED_RAW_MATCHES:
        raise RuntimeError("clean replay evidence is absent or inconsistent")

    primary = load_primary_builder(args.primary_builder)
    frame, raw, parts = construct_auxiliary(primary, args.parts_dir, args.clusters, args.anomalies)
    args.output_dir.mkdir(parents=True)
    frame.to_parquet(args.output_dir / CATALOG, index=False, compression="zstd")
    shutil.copy2(Path(__file__).resolve(), args.output_dir / Path(__file__).name)
    validator = Path(__file__).with_name("validate_desi_warned_primary_aux_v320_r5.py")
    shutil.copy2(validator, args.output_dir / validator.name)

    exact_masks = {str(int(k)): int(v) for k, v in frame["zwarn"].value_counts().sort_index().items()}
    bit_counts = {
        name: int(((frame["zwarn"].astype(np.int64) & (1 << bit)) != 0).sum())
        for bit, name in ZWARN_BITS.items()
    }
    part_manifest = {
        "parts": [
            {"path": path.name, "rows": int(len(pd.read_parquet(path, columns=["fits_row"]))), "sha256": sha256_file(path)}
            for path in parts
        ]
    }
    write_json(args.output_dir / "CHECKPOINT_MANIFEST.json", part_manifest)
    qc = {
        "status": "PASS",
        "rows": len(frame), "columns": len(frame.columns),
        "selection": "ZCAT_PRIMARY == true and ZWARN != 0 after the declared positional/main-science join; predicate before dedupe",
        "product_role": STATUS,
        "counts": {"raw_matches": len(raw), "global_primary": EXPECTED_GLOBAL_PRIMARY, "warned_primary": len(frame)},
        "exact_zwarn_mask_counts": exact_masks,
        "zwarn_set_bit_counts_nonexclusive": bit_counts,
        "exact_set_sha256_cluster_target_fits_zwarn": exact_set_sha256(frame),
        "assertions": {
            "candidate_ids_unique": bool(frame["candidate_id"].is_unique),
            "cluster_ids_unique": bool(frame["cluster_id"].is_unique),
            "targetids_unique": bool(frame["targetid"].is_unique),
            "all_global_primary": bool(frame["zcat_primary"].all()),
            "all_zwarn_nonzero": bool((frame["zwarn"] != 0).all()),
            "all_primary_catalog_member_false": bool((~frame["primary_catalog_member"]).all()),
            "all_status_labels_exact": bool((frame["auxiliary_status"] == STATUS).all()),
            "pre_post_dedup_rows_equal": True,
        },
    }
    write_json(args.output_dir / "QC_REPORT.json", qc)
    write_dictionary(args.output_dir / "DATA_DICTIONARY.md", frame)

    provenance = {
        "created_utc": utc_now(), "release": f"p3-v{VERSION}", "product_role": STATUS,
        "command_contract": (
            "python3 build_desi_warned_primary_aux_v320_r5.py "
            "--parts-dir .desi_science_catalog_v3.2.0-r2.build/match_parts "
            "--clusters pathc_unique_objects.parquet --anomalies desi_dr1_anomalies.parquet "
            "--output-dir desi_warned_primary_aux_v3.2.0-r5"
        ),
        "inputs": {
            "historical_dataset_commit": HISTORICAL_COMMIT,
            "clusters": {"sha256": EXPECTED_INPUTS["clusters"], "url": f"https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog/resolve/{HISTORICAL_COMMIT}/pathc_unique_objects.parquet"},
            "anomalies": {"sha256": EXPECTED_INPUTS["anomalies"], "url": f"https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog/resolve/{HISTORICAL_COMMIT}/desi_dr1_anomalies.parquet"},
            "desi_zall_fits_sha256": DESI_FITS_SHA256,
            "primary_provenance_sha256": sha256_file(args.primary_provenance),
            "clean_replay_sha256": sha256_file(args.clean_replay),
            "checkpoint_parts": EXPECTED_PARTS,
        },
        "exact_set_sha256_cluster_target_fits_zwarn": exact_set_sha256(frame),
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "pandas": pd.__version__, "pyarrow": pyarrow.__version__},
        "boundary": "This is a warning-bearing secondary follow-up list, not the primary catalog, not physically validated, and not an anomaly-rate or selection-efficiency measurement.",
    }
    write_json(args.output_dir / "PROVENANCE.json", provenance)

    (args.output_dir / "LICENSE.md").write_text(
        "# License\n\nThe derived data table and accompanying documentation are released under "
        "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Upstream DESI DR1 "
        "metadata retains its source attribution and terms. Bundled Python scripts retain the "
        "repository's code terms; this file grants no broader patent or trademark rights.\n"
    )
    (args.output_dir / "README.md").write_text(f"""# P3 v{VERSION} warned-primary auxiliary product

> **SECONDARY / WARNING-BEARING / NOT THE PRIMARY CATALOG / NOT PHYSICALLY VALIDATED**

This product contains exactly **2,267** public DESI DR1 global-primary rows that pass the
declared main-survey science-bit and one-arcsecond positional join but have nonzero `ZWARN`.
They are excluded from the 181-row warning-free primary catalog. Publishing this list does
not weaken that gate, establish that any spectrum is physically anomalous, measure purity,
or quantify model/selection efficiency.

The table `{CATALOG}` carries stable `P3-DESI-WARNED-*` IDs, all primary-product DESI and
historical-lineage fields, the exact integer/hex warning mask, and decoded set bits. The only
observed masks are 2, 4, 6, 2048, 2050, 2052, and 2054, composed of DESI Redrock bits 1
(`LITTLE_COVERAGE`), 2 (`SMALL_DELTA_CHI2`), and 11 (`POORDATA`).

Reproduction uses the 143 exact checkpoint parts created by the clean 28,425,963-row DESI
DR1 replay, plus immutable historical inputs at Hugging Face commit `{HISTORICAL_COMMIT}`.
Run the bundled validator with the same checkpoint and historical inputs; it independently
reselects the rows and requires exact key and carried-source-field equality.

The upstream BigAE production normalization/resampling and physical-feature sensitivity are
not recoverable from these rows. `original_score` is frozen canonical-S ranking metadata only.
""")
    write_json(args.output_dir / "RELEASE_MANIFEST.json", payload_manifest(args.output_dir))
    print(json.dumps(qc, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
