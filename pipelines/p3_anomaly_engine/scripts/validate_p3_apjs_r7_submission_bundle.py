#!/usr/bin/env python3
"""Validate the complete P3 r7 ApJS bundle and its scientific contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import pandas as pd


ENGINE = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ENGINE / "apjs_submission_bundle_v3.2.0-r7"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate(bundle: Path) -> dict:
    manifest_path = bundle / "BUNDLE_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text())
    require(manifest["bundle"] == "p3-apjs-v3.2.0-r7", "wrong bundle version")
    require(manifest["status"] == "PASS", "bundle status is not PASS")
    require(manifest["aas_relationship"]["digital_asset_doi"] is None, "unassigned DOI must remain null")

    listed = {row["path"] for row in manifest["payload_files"]}
    for row in manifest["payload_files"]:
        path = bundle / row["path"]
        require(path.is_file(), f"missing payload: {row['path']}")
        require(path.stat().st_size == row["bytes"], f"byte mismatch: {row['path']}")
        require(sha256(path) == row["sha256"], f"hash mismatch: {row['path']}")

    allowed_extras = {"BUNDLE_MANIFEST.json", "BUNDLE_README.md", "SHA256SUMS"}
    actual = {str(path.relative_to(bundle)) for path in bundle.rglob("*") if path.is_file()}
    require(actual == listed | allowed_extras, f"unmanifested or missing files: {sorted(actual ^ (listed | allowed_extras))}")

    expected_sums = {}
    for line in (bundle / "SHA256SUMS").read_text().splitlines():
        digest, relative = line.split("  ", 1)
        expected_sums[relative] = digest
    require(set(expected_sums) == actual - {"SHA256SUMS"}, "SHA256SUMS file set mismatch")
    for relative, digest in expected_sums.items():
        require(sha256(bundle / relative) == digest, f"SHA256SUMS mismatch: {relative}")

    primary_path = bundle / "primary_release/desi_dr1_science_anomaly_candidates_v3.2.0-r2.parquet"
    warned_path = bundle / "warned_auxiliary/desi_dr1_warned_global_primary_aux_v3.2.0-r5.parquet"
    primary = pd.read_parquet(primary_path)
    warned = pd.read_parquet(warned_path)
    require(primary.shape == (181, 43), f"primary shape {primary.shape}")
    require(warned.shape == (2267, 47), f"warned shape {warned.shape}")
    tiers = primary["match_quality_tier"].value_counts().to_dict()
    require(tiers == {"coordinate_consistent_le_0p1arcsec": 170, "positional_match_gt_0p1_le_1arcsec": 11}, f"tier counts {tiers}")
    require((primary["match_separation_arcsec"] <= 1.0).all(), "primary separation exceeds 1 arcsec")
    require((primary["zwarn"] == 0).all(), "primary contains ZWARN != 0")
    require((warned["zwarn"] != 0).all(), "warned auxiliary contains ZWARN == 0")
    require(not warned["primary_catalog_member"].any(), "warned auxiliary promoted to primary")
    original_member = primary["original_member_separation_arcsec"] <= 1.0
    require(int(original_member.sum()) == 180, "original-member counterfactual must retain 180")

    aas = pd.read_csv(bundle / "aas_machine_readable_table/tab3.tsv", sep="\t", dtype=str)
    require(aas.shape == (181, 43), f"AAS table shape {aas.shape}")
    aas_manifest = json.loads((bundle / "aas_machine_readable_table/AAS_DIGITAL_ASSET_MANIFEST.json").read_text())
    require(aas_manifest["validation"] == {"columns": 43, "null_cells": 0, "rows": 181, "tsv_roundtrip": "exact by column after typed parse"}, "AAS validation contract changed")
    require(aas_manifest["journal_asset_doi"] is None, "AAS DOI must remain null")

    controls = json.loads((bundle / "science_controls/p3_apjs_r6_science_controls.json").read_text())
    accepted = controls["accepted_vs_warning_bearing"]["accepted"]["fields"]["original_score"]["median"]
    warning = controls["accepted_vs_warning_bearing"]["warning_bearing"]["fields"]["original_score"]["median"]
    require(abs(accepted - 5.324423313140869) < 1e-12, f"accepted original_score median {accepted}")
    require(abs(warning - 5.841819763183594) < 1e-12, f"warned original_score median {warning}")
    require(controls["accepted_vs_warning_bearing"]["accepted"]["rows"] == 181, "controls accepted row count")
    require(controls["accepted_vs_warning_bearing"]["warning_bearing"]["rows"] == 2267, "controls warned row count")

    lineage = manifest["coordinate_lineage"]
    require(lineage["status"] == "PASS", "coordinate lineage audit failed")
    require("TARGET_RA/TARGET_DEC" in lineage["supported_claim"], "coordinate field lineage absent")
    for row in manifest["payload_files"]:
        if row["role"] == "upstream_coordinate_lineage":
            text = (bundle / row["path"]).read_text()
            require("TARGET_RA" in text and "TARGET_DEC" in text, f"coordinate fields absent: {row['path']}")

    result = {
        "status": "PASS",
        "bundle": manifest["bundle"],
        "manifest_sha256": sha256(manifest_path),
        "primary_rows": len(primary),
        "core_rows": tiers["coordinate_consistent_le_0p1arcsec"],
        "lower_confidence_rows": tiers["positional_match_gt_0p1_le_1arcsec"],
        "warned_auxiliary_rows": len(warned),
        "aas_rows": len(aas),
        "warned_original_score_median": warning,
        "coordinate_lineage": "PASS",
        "doi_status": "pending",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--component-replay", action="store_true", help="Also replay component validators through the non-mutating temporary wrapper.")
    args = parser.parse_args()
    validate(args.bundle.resolve())
    wrapper = ENGINE / "scripts/run_p3_apjs_r7_component_validators.py"
    subprocess.run(["python3", str(wrapper), "--self-check"], check=True)
    if args.component_replay:
        subprocess.run(["python3", str(wrapper)], check=True)


if __name__ == "__main__":
    main()
