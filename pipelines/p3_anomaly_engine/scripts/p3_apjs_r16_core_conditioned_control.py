#!/usr/bin/env python3
"""Recompute the r16 core-conditioned annular control.

The r6 aggregate control stores only the nearest strict target for each cluster.
This audit retains both nearest- and all-neighbor evidence for the 170 released
core clusters at their observed coordinates and at the same 16 fixed shifts.
It tests, without assigning a causal model, whether an inner seed target hides
an additional strict target in the 0.1--1 arcsec annulus.
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
SHIFT_RADII_ARCSEC = (60.0, 120.0)
SHIFT_POSITION_ANGLES_DEG = tuple(float(v) for v in range(0, 360, 45))
FITS_COLUMNS = ["TARGET_RA", "TARGET_DEC", "SURVEY", "DESI_TARGET", "ZCAT_PRIMARY", "ZWARN"]
EXPECTED_CLUSTERS_SHA256 = "b14deb02ddc374cc30a54e6013c0695d1c35cbf18cef9144245e338d6138c643"
EXPECTED_PRIMARY_SHA256 = "25f06752e0f1e9c0ddcde32e74fc0a82e8c2518a8fb24bf910c21e10ce988b03"
EXPECTED_FITS_SHA256 = "2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b"
EXPECTED_FITS_BYTES = 22_371_272_640


def sha256_file(path: Path, chunk_bytes: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(chunk_bytes), b""):
            digest.update(block)
    return digest.hexdigest()


def clean_text(values: np.ndarray) -> np.ndarray:
    return np.char.strip(np.asarray(values).astype("U"))


def science_bit_mask(values: np.ndarray) -> np.ndarray:
    bits = np.asarray(values, dtype=np.uint64)
    out = np.zeros(len(bits), dtype=bool)
    for bit in SCIENCE_BITS:
        out |= (bits & (np.uint64(1) << np.uint64(bit))) != 0
    return out


def sky_vectors(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    ra = np.deg2rad(np.asarray(ra_deg, dtype=np.float64))
    dec = np.deg2rad(np.asarray(dec_deg, dtype=np.float64))
    cos_dec = np.cos(dec)
    return np.column_stack((cos_dec * np.cos(ra), cos_dec * np.sin(ra), np.sin(dec)))


def chord_to_arcsec(chord: np.ndarray) -> np.ndarray:
    return np.rad2deg(2.0 * np.arcsin(np.clip(np.asarray(chord) / 2.0, 0.0, 1.0))) * 3600.0


def shifted_vectors(ra_deg: np.ndarray, dec_deg: np.ndarray, radius_arcsec: float, pa_deg: float) -> np.ndarray:
    ra = np.deg2rad(np.asarray(ra_deg, dtype=np.float64))
    dec = np.deg2rad(np.asarray(dec_deg, dtype=np.float64))
    u = sky_vectors(ra_deg, dec_deg)
    east = np.column_stack((-np.sin(ra), np.cos(ra), np.zeros(len(ra))))
    north = np.column_stack((-np.sin(dec) * np.cos(ra), -np.sin(dec) * np.sin(ra), np.cos(dec)))
    pa = math.radians(pa_deg)
    tangent = math.sin(pa) * east + math.cos(pa) * north
    delta = math.radians(radius_arcsec / 3600.0)
    return math.cos(delta) * u + math.sin(delta) * tangent


def load_core(clusters_path: Path, primary_path: Path) -> pd.DataFrame:
    clusters = pd.read_parquet(clusters_path)
    is_desi = clusters["survey_list"].astype(str).str.split(",").map(lambda xs: "desi_dr1" in xs)
    clusters = clusters.loc[is_desi, ["cluster_id", "ra_mean", "dec_mean"]].reset_index(drop=True)
    if len(clusters) != 190_015:
        raise RuntimeError(f"expected 190,015 DESI clusters, found {len(clusters):,}")
    primary = pd.read_parquet(primary_path, columns=["cluster_id", "match_separation_arcsec"])
    core_ids = set(primary.loc[primary.match_separation_arcsec <= 0.1, "cluster_id"].astype(int))
    core = clusters.loc[clusters.cluster_id.astype(int).isin(core_ids)].reset_index(drop=True)
    if len(core) != 170:
        raise RuntimeError(f"expected 170 core clusters, found {len(core):,}")
    return core


def control_vectors(core: pd.DataFrame) -> tuple[np.ndarray, list[dict[str, float | str]]]:
    vectors = [sky_vectors(core.ra_mean, core.dec_mean)]
    labels: list[dict[str, float | str]] = [
        {"label": "observed", "offset_arcsec": 0.0, "position_angle_deg": 0.0}
    ]
    for offset in SHIFT_RADII_ARCSEC:
        for pa in SHIFT_POSITION_ANGLES_DEG:
            vectors.append(shifted_vectors(core.ra_mean, core.dec_mean, offset, pa))
            labels.append({
                "label": f"shift_{int(offset)}arcsec_pa{int(pa):03d}",
                "offset_arcsec": offset,
                "position_angle_deg": pa,
            })
    return np.vstack(vectors), labels


def scan(fits_path: Path, vectors: np.ndarray, labels: list[dict[str, float | str]], chunk_rows: int) -> dict:
    n_core = 170
    n_realizations = len(labels)
    minima = np.full((n_realizations, n_core), np.inf, dtype=np.float64)
    has_core = np.zeros((n_realizations, n_core), dtype=bool)
    has_annulus = np.zeros_like(has_core)
    control_tree = cKDTree(vectors)
    max_chord = 2.0 * math.sin(math.radians(1.0 / 3600.0) / 2.0)
    fits_rows = 0
    strict_total = 0

    with fitsio.FITS(str(fits_path), "r") as hdus:
        table = hdus["ZCATALOG"]
        n_rows = int(table.get_nrows())
        for start in range(0, n_rows, chunk_rows):
            stop = min(start + chunk_rows, n_rows)
            block = table.read(rows=np.arange(start, stop, dtype=np.int64), columns=FITS_COLUMNS)
            strict = (
                (clean_text(block["SURVEY"]) == "main")
                & science_bit_mask(block["DESI_TARGET"])
                & np.asarray(block["ZCAT_PRIMARY"], dtype=bool)
                & (np.asarray(block["ZWARN"], dtype=np.int64) == 0)
            )
            fits_rows += stop - start
            strict_total += int(strict.sum())
            if strict.any():
                target_tree = cKDTree(sky_vectors(block["TARGET_RA"][strict], block["TARGET_DEC"][strict]))
                pairs = target_tree.sparse_distance_matrix(control_tree, max_chord, output_type="coo_matrix")
                if pairs.nnz:
                    realization = pairs.col // n_core
                    core_index = pairs.col % n_core
                    separation = chord_to_arcsec(pairs.data)
                    np.minimum.at(minima, (realization, core_index), separation)
                    inner = separation <= 0.1
                    annulus = (separation > 0.1) & (separation <= 1.0)
                    has_core[realization[inner], core_index[inner]] = True
                    has_annulus[realization[annulus], core_index[annulus]] = True
            print(json.dumps({"start": start, "stop": stop, "strict_total": strict_total}), flush=True)

    realizations = []
    for index, label in enumerate(labels):
        realizations.append({
            **label,
            "any_core_le_0p1": int(np.count_nonzero(has_core[index])),
            "any_annulus_gt_0p1_le_1": int(np.count_nonzero(has_annulus[index])),
            "hidden_annulus_due_to_core_slot": int(np.count_nonzero(has_core[index] & has_annulus[index])),
            "nearest_annulus_count": int(np.count_nonzero((minima[index] > 0.1) & (minima[index] <= 1.0))),
        })
    return {"fits_rows": fits_rows, "strict_total": strict_total, "realizations": realizations}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clusters", type=Path, required=True)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--fits", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--chunk-rows", type=int, default=1_000_000)
    args = parser.parse_args()

    clusters_sha = sha256_file(args.clusters)
    primary_sha = sha256_file(args.primary)
    if clusters_sha != EXPECTED_CLUSTERS_SHA256 or primary_sha != EXPECTED_PRIMARY_SHA256:
        raise RuntimeError("cluster or primary input hash does not match the frozen release")
    if args.fits.stat().st_size != EXPECTED_FITS_BYTES:
        raise RuntimeError("FITS byte size does not match the frozen DESI DR1 input")
    fits_sha = sha256_file(args.fits)
    if fits_sha != EXPECTED_FITS_SHA256:
        raise RuntimeError("FITS input hash does not match the frozen DESI DR1 input")

    core = load_core(args.clusters, args.primary)
    vectors, labels = control_vectors(core)
    result = scan(args.fits, vectors, labels, args.chunk_rows)
    payload = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "purpose": "core-conditioned all-neighbor audit; descriptive, not a conditional null",
        "inputs": {
            "clusters": {"path": str(args.clusters), "sha256": clusters_sha},
            "primary": {"path": str(args.primary), "sha256": primary_sha},
            "fits": {
                "path": str(args.fits),
                "size_bytes": args.fits.stat().st_size,
                "sha256": fits_sha,
            },
        },
        "cluster_population": 190_015,
        "core_clusters": 170,
        **result,
    }
    expected_zero_fields = ("any_annulus_gt_0p1_le_1", "hidden_annulus_due_to_core_slot", "nearest_annulus_count")
    if payload["fits_rows"] != 28_425_963 or payload["strict_total"] != 18_134_821:
        raise RuntimeError("FITS or strict-row count drifted")
    if payload["realizations"][0]["any_core_le_0p1"] != 170:
        raise RuntimeError("observed core recovery drifted")
    if any(row[field] != 0 for row in payload["realizations"] for field in expected_zero_fields):
        raise RuntimeError("core-conditioned annular result drifted from zero")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "status": "PASS"}))


if __name__ == "__main__":
    main()
