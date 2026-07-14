#!/usr/bin/env python3
"""Prepare and validate the P3 AAS machine-readable-table submission package.

The journal-facing table is derived byte-for-byte from the immutable public
v3.2.0-r2 Parquet release. No DOI is invented here: AAS assigns a digital-
asset DOI during its publication workflow.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import pandas as pd


RELEASE_TAG = "p3-v3.2.0-r2"
RELEASE_REVISION = "1a9e85ee004894956665444b4f110111f1090b79"
AAS_DATA_GUIDE = "https://journals.aas.org/data-guide/"
AAS_DOI_POLICY = "https://journals.aas.org/news/digital_asset_doi_landingpage/"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_dictionary(path: Path) -> list[dict[str, str]]:
    entries = []
    pattern = re.compile(r"^\| `([^`]+)` \| `([^`]+)` \| (.+) \|$")
    for line in path.read_text().splitlines():
        match = pattern.match(line)
        if match:
            entries.append({"name": match[1], "storage_type": match[2], "meaning": match[3]})
    return entries


def aas_unit(name: str) -> str:
    if name.endswith("_arcsec"):
        return "arcsec"
    if name.endswith("_ra") or name.endswith("_dec") or name.endswith("_ra_deg") or name.endswith("_dec_deg"):
        return "deg"
    return "---"


def write_readme(path: Path, entries: list[dict[str, str]]) -> None:
    lines = [
        "P3 DESI DR1 anomaly-candidate catalog: AAS digital-asset package",
        "================================================================",
        "",
        "File: tab3.tsv",
        "Rows: 181 data rows plus one header row",
        "Columns: 43 tab-separated columns",
        "Missing values: none",
        "License: CC BY 4.0",
        "",
        "Source release:",
        "  https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog",
        f"  tag: {RELEASE_TAG}",
        f"  immutable commit: {RELEASE_REVISION}",
        "  path: releases/p3-v3.2.0-r2/",
        "",
        "Journal DOI status:",
        "  No DOI is claimed before submission. This table is prepared for submission",
        "  as an AAS machine-readable digital asset; AAS assigns the asset DOI during",
        "  its publication workflow.",
        f"  AAS data guide: {AAS_DATA_GUIDE}",
        f"  AAS digital-asset DOI policy: {AAS_DOI_POLICY}",
        "",
        "Column descriptions:",
        "  No.  Name                                    Type       Unit    Description",
    ]
    for number, entry in enumerate(entries, 1):
        lines.append(
            f"  {number:>3}  {entry['name']:<39} {entry['storage_type']:<10} "
            f"{aas_unit(entry['name']):<7} {entry['meaning']}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="ascii", errors="strict")


def main() -> None:
    repo = Path(__file__).resolve().parents[3]
    release = repo / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0-r2"
    source = release / "desi_dr1_science_anomaly_candidates_v3.2.0-r2.parquet"
    dictionary_path = release / "DATA_DICTIONARY.md"
    output = repo / "pipelines/p3_anomaly_engine/aas_submission_v3.2.0-r3"
    output.mkdir(parents=True, exist_ok=True)

    frame = pd.read_parquet(source)
    entries = parse_dictionary(dictionary_path)
    expected_columns = [entry["name"] for entry in entries]
    if len(frame) != 181 or len(frame.columns) != 43:
        raise RuntimeError(f"expected 181x43 catalog, found {frame.shape}")
    if frame.columns.tolist() != expected_columns:
        raise RuntimeError("data-dictionary columns/order do not equal the released Parquet")
    if frame.isna().any().any():
        raise RuntimeError("released catalog contains missing values")

    table_path = output / "tab3.tsv"
    frame.to_csv(table_path, sep="\t", index=False, float_format="%.17g", lineterminator="\n")
    roundtrip = pd.read_csv(table_path, sep="\t", float_precision="round_trip")
    if roundtrip.columns.tolist() != frame.columns.tolist() or len(roundtrip) != len(frame):
        raise RuntimeError("TSV row/column round-trip mismatch")
    for column in frame.columns:
        left = frame[column]
        right = roundtrip[column]
        if pd.api.types.is_float_dtype(left):
            if not (left.to_numpy() == right.astype(float).to_numpy()).all():
                raise RuntimeError(f"TSV float round-trip mismatch: {column}")
        elif pd.api.types.is_bool_dtype(left):
            if not (left.to_numpy() == right.astype(bool).to_numpy()).all():
                raise RuntimeError(f"TSV Boolean round-trip mismatch: {column}")
        elif pd.api.types.is_integer_dtype(left):
            if not (left.to_numpy() == right.astype(left.dtype).to_numpy()).all():
                raise RuntimeError(f"TSV integer round-trip mismatch: {column}")
        elif not (left.astype(str).to_numpy() == right.astype(str).to_numpy()).all():
            raise RuntimeError(f"TSV string round-trip mismatch: {column}")

    readme_path = output / "ReadMe"
    write_readme(readme_path, entries)
    manifest = {
        "status": "PASS",
        "journal_asset_doi": None,
        "journal_asset_doi_status": "To be assigned by AAS during the publication workflow; not yet claimed.",
        "source_release": {
            "tag": RELEASE_TAG,
            "immutable_revision": RELEASE_REVISION,
            "path": "releases/p3-v3.2.0-r2/",
            "parquet_sha256": sha256_file(source),
        },
        "aas_policy": {
            "data_guide": AAS_DATA_GUIDE,
            "digital_asset_doi": AAS_DOI_POLICY,
        },
        "validation": {
            "rows": len(frame),
            "columns": len(frame.columns),
            "null_cells": int(frame.isna().sum().sum()),
            "tsv_roundtrip": "exact by column after typed parse",
        },
        "files": {},
    }
    for path in (readme_path, table_path):
        manifest["files"][path.name] = {"bytes": path.stat().st_size, "sha256": sha256_file(path)}
    manifest_path = output / "AAS_DIGITAL_ASSET_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
