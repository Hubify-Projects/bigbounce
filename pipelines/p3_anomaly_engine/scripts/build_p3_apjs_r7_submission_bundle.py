#!/usr/bin/env python3
"""Build the checksum-bound P3 r7 ApJS submission bundle.

The bundle does not relabel frozen component releases.  It binds the primary
catalog, secondary warned-row auxiliary product, AAS machine-readable table,
r6 science controls, and coordinate-lineage sources into one submission unit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ENGINE = Path(__file__).resolve().parents[1]
REPO = ENGINE.parents[1]
DEFAULT_OUTPUT = ENGINE / "apjs_submission_bundle_v3.2.0-r7"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def asset(source: Path, destination: str, role: str) -> tuple[Path, str, str]:
    return source, destination, role


PRIMARY = ENGINE / "desi_science_catalog_v3.2.0-r2"
WARNED = ENGINE / "desi_warned_primary_aux_v3.2.0-r5"
AAS = ENGINE / "aas_submission_v3.2.0-r4"
OUTPUTS = ENGINE / "outputs"
FIGURES = ENGINE / "figures"
SCRIPTS = ENGINE / "scripts"

ASSETS: list[tuple[Path, str, str]] = []
for path in sorted(PRIMARY.iterdir()):
    if path.is_file():
        ASSETS.append(asset(path, f"primary_release/{path.name}", "primary_release"))
for path in sorted(WARNED.iterdir()):
    if path.is_file():
        ASSETS.append(asset(path, f"warned_auxiliary/{path.name}", "secondary_warned_auxiliary"))
for path in sorted(AAS.iterdir()):
    if path.is_file():
        ASSETS.append(asset(path, f"aas_machine_readable_table/{path.name}", "aas_machine_readable_table"))
ASSETS.extend(
    [
        asset(SCRIPTS / "prepare_p3_v320_r4_aas_package.py", "aas_machine_readable_table/prepare_p3_v320_r4_aas_package.py", "aas_table_builder"),
        asset(SCRIPTS / "p3_apjs_r6_science_controls.py", "science_controls/p3_apjs_r6_science_controls.py", "science_control_code"),
        asset(SCRIPTS / "run_p3_apjs_r7_component_validators.py", "validation/run_p3_apjs_r7_component_validators.py", "non_mutating_component_validator_wrapper"),
        asset(OUTPUTS / "p3_apjs_r6_science_controls.json", "science_controls/p3_apjs_r6_science_controls.json", "science_control_result"),
        asset(OUTPUTS / "p3_apjs_r6_original_member_sensitivity.csv", "science_controls/p3_apjs_r6_original_member_sensitivity.csv", "original_member_sensitivity"),
        asset(OUTPUTS / "p3_apjs_r6_positional_tail.csv", "science_controls/p3_apjs_r6_positional_tail.csv", "positional_tail_rows"),
        asset(FIGURES / "p3_v320_r6_chance_control.pdf", "science_controls/p3_v320_r6_chance_control.pdf", "science_control_figure"),
        asset(REPO / "pipelines/p1_highz_tracers/outputs/desi_dr1/13_desi_dr1_gpu_inference.py", "coordinate_lineage/13_desi_dr1_gpu_inference.py", "upstream_coordinate_lineage"),
        asset(REPO / "pipelines/p1_highz_tracers/outputs/desi_dr1/run_dr1_parallel.py", "coordinate_lineage/run_dr1_parallel.py", "upstream_coordinate_lineage"),
        asset(REPO / "pipelines/p1_highz_tracers/scripts/enhanced_18M_inference.py", "coordinate_lineage/enhanced_18M_inference.py", "upstream_coordinate_lineage"),
        asset(ENGINE / "pathc_positional_dedup.py", "coordinate_lineage/pathc_positional_dedup.py", "cluster_coordinate_lineage"),
        asset(ENGINE / "apjs_submission_v3.1.161/desi_dr1_anomalies.parquet", "coordinate_lineage/desi_dr1_anomalies.parquet", "frozen_historical_anomaly_table"),
    ]
)


README = """# P3 ApJS submission bundle v3.2.0-r7

This directory is the definitive checksum-bound submission unit for the P3
catalog manuscript.  It binds, without relabeling, four frozen products:

1. `primary_release/`: the 181-row, 43-column primary Parquet release v3.2.0-r2.
   Its authoritative contract retains all 181 coordinate associations while
   distinguishing 170 `coordinate_consistent_le_0p1arcsec` core rows from 11
   `positional_match_gt_0p1_le_1arcsec` lower-confidence rows.  Neither tier is
   an object-identity proof or a purity estimate.
2. `warned_auxiliary/`: the 2,267-row warning-bearing global-primary auxiliary
   product v3.2.0-r5.  It is secondary and is not part of the primary catalog.
3. `aas_machine_readable_table/`: the AAS v3.2.0-r4 `tab3.tsv`, an exact typed
   serialization of the 181 x 43 primary Parquet table, plus its dictionary,
   manifest, and builder.  Its AAS digital-asset DOI is pending and is not
   claimed here.
4. `science_controls/` and `coordinate_lineage/`: the r6 association controls,
   original-member sensitivity, and SHA-bound code/data evidence showing that
   historical DESI anomaly `ra`/`dec` were copied from coadd FIBERMAP
   `TARGET_RA`/`TARGET_DEC` before cluster means were computed.  This recovers
   coordinate-field lineage, not the unavailable production object-to-spectrum
   mapping or anomaly-score preprocessing.

`BUNDLE_MANIFEST.json` records the role, source path, byte size, and SHA-256 of
every payload. `SHA256SUMS` additionally binds the manifest and this README.
Run `../scripts/validate_p3_apjs_r7_submission_bundle.py` from any directory to
validate the complete contract.
"""


def lineage_assertions() -> dict:
    gpu = REPO / "pipelines/p1_highz_tracers/outputs/desi_dr1/13_desi_dr1_gpu_inference.py"
    parallel = REPO / "pipelines/p1_highz_tracers/outputs/desi_dr1/run_dr1_parallel.py"
    enhanced = REPO / "pipelines/p1_highz_tracers/scripts/enhanced_18M_inference.py"
    dedup = ENGINE / "pathc_positional_dedup.py"
    checks = {
        str(gpu.relative_to(REPO)): ["'ra': float(fm['TARGET_RA'][i])", "'dec': float(fm['TARGET_DEC'][i])"],
        str(parallel.relative_to(REPO)): ["'ra':float(fm['TARGET_RA'][i])", "'dec':float(fm['TARGET_DEC'][i])"],
        str(enhanced.relative_to(REPO)): ["TARGET_RA", "TARGET_DEC", "MEAN_FIBER_RA", "MEAN_FIBER_DEC"],
        str(dedup.relative_to(REPO)): ["ra_mean", "dec_mean", "SkyCoord"],
    }
    for relative, needles in checks.items():
        text = (REPO / relative).read_text()
        missing = [needle for needle in needles if needle not in text]
        if missing:
            raise RuntimeError(f"coordinate-lineage assertion failed for {relative}: {missing}")
    return {
        "status": "PASS",
        "supported_claim": "Historical DESI anomaly ra/dec fields were copied from coadd FIBERMAP TARGET_RA/TARGET_DEC; frozen cluster coordinates were then computed from member-coordinate means.",
        "unsupported_claims_explicitly_excluded": [
            "secure object identity for any positional association",
            "a purity estimate for the 181-row catalog or 11-row tail",
            "recovery of the unavailable production object-to-spectrum mapping",
            "reproduction of historical score normalization or spectral preprocessing",
        ],
        "source_assertions": checks,
    }


def build(output: Path) -> None:
    missing = [str(source) for source, _, _ in ASSETS if not source.is_file()]
    if missing:
        raise FileNotFoundError("missing required assets:\n" + "\n".join(missing))
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    records = []
    for source, destination, role in ASSETS:
        target = output / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        records.append(
            {
                "path": destination,
                "role": role,
                "source_repo_path": str(source.relative_to(REPO)),
                "bytes": target.stat().st_size,
                "sha256": sha256(target),
            }
        )

    lineage = lineage_assertions()
    lineage_path = output / "coordinate_lineage/COORDINATE_LINEAGE_AUDIT.json"
    lineage_path.write_text(json.dumps(lineage, indent=2, sort_keys=True) + "\n")
    records.append(
        {
            "path": str(lineage_path.relative_to(output)),
            "role": "coordinate_lineage_audit",
            "source_repo_path": None,
            "bytes": lineage_path.stat().st_size,
            "sha256": sha256(lineage_path),
        }
    )

    (output / "BUNDLE_README.md").write_text(README)
    manifest = {
        "bundle": "p3-apjs-v3.2.0-r7",
        "status": "PASS",
        "created_utc": "2026-07-14T20:30:00Z",
        "component_versions": {
            "primary_release": "v3.2.0-r2",
            "warned_auxiliary": "v3.2.0-r5",
            "aas_machine_readable_table": "v3.2.0-r4",
            "science_controls": "r6",
        },
        "primary_contract": {
            "rows": 181,
            "columns": 43,
            "core_coordinate_consistent_le_0p1arcsec": 170,
            "lower_confidence_positional_gt_0p1_le_1arcsec": 11,
            "retain_all_181": True,
            "secure_identity_claim": False,
            "purity_claim": False,
        },
        "aas_relationship": {
            "tab3_tsv": "exact typed serialization of the primary 181-row, 43-column Parquet table",
            "digital_asset_doi": None,
            "digital_asset_doi_status": "pending AAS publication workflow; not claimed",
        },
        "coordinate_lineage": lineage,
        "payload_files": sorted(records, key=lambda row: row["path"]),
        "manifest_self_hash": "excluded (self-referential)",
    }
    manifest_path = output / "BUNDLE_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    checksum_paths = sorted(
        [path for path in output.rglob("*") if path.is_file() and path.name != "SHA256SUMS"],
        key=lambda path: str(path.relative_to(output)),
    )
    (output / "SHA256SUMS").write_text(
        "".join(f"{sha256(path)}  {path.relative_to(output)}\n" for path in checksum_paths)
    )
    print(f"built {output}")
    print(f"payload_files={len(records)} total_files={len(checksum_paths) + 1}")
    print(f"manifest_sha256={sha256(manifest_path)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()
