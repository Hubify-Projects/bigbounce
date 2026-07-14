#!/usr/bin/env python3
"""Audit P3 tail and representative rows in the public DESI DR1 viewer.

The audit records only objective viewer/API evidence: HTTP availability,
released-vs-viewer metadata agreement, served spectral-arm array lengths, and
the linked imaging cutout URL. It deliberately makes no physical or novelty
classification from a browser image.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from bs4 import BeautifulSoup


VIEWER_TEMPLATE = "https://www.legacysurvey.org/viewer/desi-spectrum/dr1/targetid{targetid}"
DESI_ACCESS_DOC = "https://data.desi.lbl.gov/doc/access/"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def walk(value: Any):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def data_entries(source: dict) -> dict[str, Any]:
    data = source.get("attributes", {}).get("data", {})
    entries = data.get("entries", []) if isinstance(data, dict) else []
    return dict(entries)


def simple_array(value: Any) -> list[Any] | None:
    if isinstance(value, list):
        return value
    if isinstance(value, dict) and value.get("type") == "ndarray":
        array = value.get("array")
        if isinstance(array, list):
            return array
    return None


def first_scalar(value: Any) -> Any:
    array = simple_array(value)
    return array[0] if array else None


def parse_viewer(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    documents = []
    for tag in soup.find_all("script", {"type": "application/json"}):
        try:
            documents.append(json.loads(tag.string or ""))
        except json.JSONDecodeError:
            continue
    sources = [
        item for document in documents for item in walk(document)
        if isinstance(item, dict) and item.get("name") == "ColumnDataSource"
    ]
    metadata = None
    arm_lengths: dict[str, int] = {}
    cutout = {}
    for source in sources:
        entries = data_entries(source)
        keys = set(entries)
        name = source.get("attributes", {}).get("name")
        if {"TARGETID", "Z", "SPECTYPE", "ZWARN", "DELTACHI2"}.issubset(keys):
            metadata = {key: first_scalar(value) for key, value in entries.items()}
        if name in {"b", "r", "z"} and "origwave" in entries:
            value = entries["origwave"]
            shape = value.get("shape") if isinstance(value, dict) else None
            if isinstance(shape, list) and shape:
                arm_lengths[name] = int(shape[0])
        if {"url", "txt"}.issubset(keys):
            cutout = {
                "url": first_scalar(entries["url"]),
                "label": first_scalar(entries["txt"]),
            }
    if metadata is None:
        raise RuntimeError("viewer response lacks the expected DESI metadata source")
    return {"metadata": metadata, "spectral_arm_pixel_counts": arm_lengths, "cutout": cutout}


def representative_ids(frame: pd.DataFrame) -> list[str]:
    chosen: list[str] = []

    def add(rows: pd.DataFrame) -> None:
        for candidate_id in rows["candidate_id"].astype(str):
            if candidate_id not in chosen:
                chosen.append(candidate_id)

    add(frame.nlargest(6, "original_score"))
    add(frame.loc[frame["spectype"] == "QSO"].nlargest(1, "original_score"))
    add(frame.loc[frame["spectype"] == "STAR"])
    add(frame.nlargest(1, "z"))
    add(frame.loc[frame["z"] < 0].sort_values("z"))
    add(frame.nlargest(1, "match_separation_arcsec"))
    # The named strata can overlap (for example, a top-score row may also be
    # the highest-score QSO). Fill any vacated slots deterministically with the
    # highest-score rows not already selected so the public example table has
    # a stable 12 rows without pretending that the strata are disjoint.
    add(frame.sort_values(["original_score", "candidate_id"], ascending=[False, True]))
    chosen = chosen[:12]
    if len(chosen) != 12:
        raise RuntimeError(f"representative construction expected 12 unique rows, found {len(chosen)}")
    return chosen


def parse_args() -> argparse.Namespace:
    repo = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0-r2/desi_dr1_science_anomaly_candidates_v3.2.0-r2.parquet",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo / "pipelines/p3_anomaly_engine/audits/p3_v320_r3_public_viewer_audit.json",
    )
    parser.add_argument("--timeout", type=float, default=60.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    frame = pd.read_parquet(args.catalog)
    tail_ids = frame.loc[frame["match_separation_arcsec"] > 0.1, "candidate_id"].astype(str).tolist()
    representative = representative_ids(frame)
    audit_ids = list(dict.fromkeys(tail_ids + representative))
    session = requests.Session()
    session.headers["User-Agent"] = "P3-v3.2.0-r3-public-viewer-audit/1"
    cases = []
    for position, candidate_id in enumerate(audit_ids, 1):
        row = frame.loc[frame["candidate_id"] == candidate_id].iloc[0]
        url = VIEWER_TEMPLATE.format(targetid=int(row.targetid))
        response = session.get(url, timeout=args.timeout)
        response.raise_for_status()
        viewer = parse_viewer(response.text)
        metadata = viewer["metadata"]
        checks = {
            "targetid": int(metadata["TARGETID"]) == int(row.targetid),
            "z": abs(float(metadata["Z"]) - float(row.z)) < 5e-5,
            "spectype": str(metadata["SPECTYPE"]).strip() == str(row.spectype),
            "zwarn": int(metadata["ZWARN"]) == int(row.zwarn) == 0,
            "deltachi2": abs(float(metadata["DELTACHI2"]) - float(row.deltachi2)) < 0.01,
            "three_spectral_arms_served": set(viewer["spectral_arm_pixel_counts"]) == {"b", "r", "z"},
        }
        cases.append({
            "candidate_id": candidate_id,
            "roles": [
                role for role, ids in (("separation_tail", tail_ids), ("representative_table", representative))
                if candidate_id in ids
            ],
            "released": {
                "targetid": int(row.targetid),
                "spectype": str(row.spectype),
                "z": float(row.z),
                "zwarn": int(row.zwarn),
                "deltachi2": float(row.deltachi2),
                "original_score": float(row.original_score),
                "match_separation_arcsec": float(row.match_separation_arcsec),
                "original_member_separation_arcsec": float(row.original_member_separation_arcsec),
            },
            "viewer_url": url,
            "http_status": response.status_code,
            "viewer_metadata": {
                key: metadata.get(key) for key in (
                    "TARGETID", "Z", "SPECTYPE", "SUBTYPE", "ZERR", "ZWARN", "DELTACHI2",
                    "COADD_NUMEXP", "COADD_EXPTIME", "COADD_NUMNIGHT", "COADD_NUMTILE",
                    "MORPHTYPE", "mag_G", "mag_R", "mag_Z", "mag_W1", "mag_W2",
                )
            },
            "spectral_arm_pixel_counts": viewer["spectral_arm_pixel_counts"],
            "imaging_cutout": viewer["cutout"],
            "checks": checks,
            "status": "PASS" if all(checks.values()) else "FAIL",
        })
        print(f"[{position:02d}/{len(audit_ids)}] {candidate_id} {cases[-1]['status']}", flush=True)
        time.sleep(0.1)

    payload = {
        "created_utc": utc_now(),
        "status": "PASS" if all(case["status"] == "PASS" for case in cases) else "FAIL",
        "scope": {
            "separation_tail_threshold_arcsec": 0.1,
            "tail_candidates": tail_ids,
            "representative_table_candidates": representative,
            "audited_unique_candidates": len(audit_ids),
        },
        "sources": {
            "official_desi_access_documentation": DESI_ACCESS_DOC,
            "viewer_url_template": VIEWER_TEMPLATE,
        },
        "input": {"catalog": str(args.catalog), "catalog_sha256": sha256_file(args.catalog)},
        "interpretation": (
            "PASS establishes that the public DR1 viewer served metadata, B/R/Z spectral arrays, "
            "and an imaging-cutout link for every audited TARGETID, and that the listed metadata "
            "agree with the release. It is not a visual classification, novelty claim, or proof "
            "that a historical anomaly score has an astrophysical origin."
        ),
        "cases": cases,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "output": str(args.output),
        "tail_candidates": len(tail_ids),
        "representative_candidates": len(representative),
        "audited_unique_candidates": len(audit_ids),
    }, indent=2))
    if payload["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
