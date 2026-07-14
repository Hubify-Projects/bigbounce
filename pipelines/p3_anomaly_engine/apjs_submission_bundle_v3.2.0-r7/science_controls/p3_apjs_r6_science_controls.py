#!/usr/bin/env python3
"""Deterministic P3 ApJS r6 association, warning, and member controls.

The positional control evaluates the exact 190,015 historical cluster centers
at their observed coordinates and after 16 fixed local tangent-plane shifts
(60 and 120 arcsec; eight position angles).  The 28.4-million-row public DESI
zcatalog is streamed once.  Counts are reported separately for the declared
20,299,155-row science-bit parent and for the warning-free global-primary
cohort, so a quality-conditioned release is never compared with the wrong
background population.

This is a descriptive association control, not a selection-bias correction or
physical validation of any candidate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import fitsio
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree


SCIENCE_BITS = (0, 1, 2, 60, 61)
RADII_ARCSEC = np.array([0.05, 0.1, 0.2, 0.5, 0.75, 1.0], dtype=np.float64)
SHIFT_RADII_ARCSEC = (60.0, 120.0)
SHIFT_POSITION_ANGLES_DEG = tuple(float(v) for v in range(0, 360, 45))
FITS_COLUMNS = ["TARGET_RA", "TARGET_DEC", "SURVEY", "DESI_TARGET", "ZCAT_PRIMARY", "ZWARN"]


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
    """Move each coordinate on a great circle along a local position angle."""
    ra = np.deg2rad(np.asarray(ra_deg, dtype=np.float64))
    dec = np.deg2rad(np.asarray(dec_deg, dtype=np.float64))
    u = sky_vectors(ra_deg, dec_deg)
    east = np.column_stack((-np.sin(ra), np.cos(ra), np.zeros(len(ra))))
    north = np.column_stack((-np.sin(dec) * np.cos(ra), -np.sin(dec) * np.sin(ra), np.cos(dec)))
    pa = math.radians(pa_deg)
    tangent = math.sin(pa) * east + math.cos(pa) * north
    delta = math.radians(radius_arcsec / 3600.0)
    return math.cos(delta) * u + math.sin(delta) * tangent


def load_cluster_centers(clusters_path: Path) -> pd.DataFrame:
    clusters = pd.read_parquet(clusters_path)
    is_desi = clusters["survey_list"].astype(str).str.split(",").map(lambda xs: "desi_dr1" in xs)
    out = clusters.loc[is_desi, ["cluster_id", "ra_mean", "dec_mean"]].reset_index(drop=True)
    if len(out) != 190_015:
        raise RuntimeError(f"expected 190,015 DESI clusters, found {len(out):,}")
    return out


def build_control_tree(clusters: pd.DataFrame) -> tuple[cKDTree, list[dict[str, float | int | str]]]:
    vectors = [sky_vectors(clusters.ra_mean, clusters.dec_mean)]
    labels: list[dict[str, float | int | str]] = [
        {"index": 0, "label": "observed", "offset_arcsec": 0.0, "position_angle_deg": 0.0}
    ]
    for offset in SHIFT_RADII_ARCSEC:
        for pa in SHIFT_POSITION_ANGLES_DEG:
            labels.append(
                {"index": len(labels), "label": f"shift_{int(offset)}arcsec_pa{int(pa):03d}",
                 "offset_arcsec": offset, "position_angle_deg": pa}
            )
            vectors.append(shifted_vectors(clusters.ra_mean, clusters.dec_mean, offset, pa))
    return cKDTree(np.vstack(vectors)), labels


def scan_associations(
    fits_path: Path,
    tree: cKDTree,
    n_clusters: int,
    n_realizations: int,
    chunk_rows: int,
) -> tuple[np.ndarray, np.ndarray, dict[str, int]]:
    parent_min = np.full((n_realizations, n_clusters), np.inf, dtype=np.float64)
    strict_min = np.full_like(parent_min, np.inf)
    max_chord = 2.0 * math.sin(math.radians(1.0 / 3600.0) / 2.0)
    totals = {"fits_rows": 0, "parent_rows": 0, "strict_rows": 0, "pairs_within_1arcsec": 0}

    with fitsio.FITS(str(fits_path), "r") as hdus:
        table = hdus["ZCATALOG"]
        n_rows = int(table.get_nrows())
        for start in range(0, n_rows, chunk_rows):
            stop = min(start + chunk_rows, n_rows)
            rows = np.arange(start, stop, dtype=np.int64)
            block = table.read(rows=rows, columns=FITS_COLUMNS)
            parent = (clean_text(block["SURVEY"]) == "main") & science_bit_mask(block["DESI_TARGET"])
            local = np.flatnonzero(parent)
            totals["fits_rows"] += stop - start
            totals["parent_rows"] += len(local)
            if len(local):
                strict_local = np.asarray(block["ZCAT_PRIMARY"][local], dtype=bool) & (
                    np.asarray(block["ZWARN"][local], dtype=np.int64) == 0
                )
                totals["strict_rows"] += int(strict_local.sum())
                target_tree = cKDTree(sky_vectors(block["TARGET_RA"][local], block["TARGET_DEC"][local]))
                pairs = target_tree.sparse_distance_matrix(tree, max_chord, output_type="coo_matrix")
                if pairs.nnz:
                    shift_index = pairs.col // n_clusters
                    cluster_index = pairs.col % n_clusters
                    sep = chord_to_arcsec(pairs.data)
                    np.minimum.at(parent_min, (shift_index, cluster_index), sep)
                    strict_pair = strict_local[pairs.row]
                    np.minimum.at(
                        strict_min,
                        (shift_index[strict_pair], cluster_index[strict_pair]),
                        sep[strict_pair],
                    )
                    totals["pairs_within_1arcsec"] += int(pairs.nnz)
            print(
                json.dumps({"start": start, "stop": stop, "parent_rows": totals["parent_rows"],
                            "strict_rows": totals["strict_rows"], "pairs": totals["pairs_within_1arcsec"]}),
                flush=True,
            )
    return parent_min, strict_min, totals


def radius_summary(minima: np.ndarray, labels: list[dict[str, object]]) -> dict[str, object]:
    counts = np.array([[int(np.count_nonzero(row <= radius)) for radius in RADII_ARCSEC] for row in minima])
    shifted = counts[1:]
    curve = []
    for j, radius in enumerate(RADII_ARCSEC):
        curve.append(
            {
                "radius_arcsec": float(radius),
                "observed": int(counts[0, j]),
                "shift_mean": float(shifted[:, j].mean()),
                "shift_sample_std": float(shifted[:, j].std(ddof=1)),
                "shift_min": int(shifted[:, j].min()),
                "shift_max": int(shifted[:, j].max()),
            }
        )
    annulus = np.count_nonzero((minima > 0.1) & (minima <= 1.0), axis=1)
    return {
        "radius_curve": curve,
        "annulus_gt_0p1_le_1arcsec": {
            "observed": int(annulus[0]),
            "shift_mean": float(annulus[1:].mean()),
            "shift_sample_std": float(annulus[1:].std(ddof=1)),
            "shift_min": int(annulus[1:].min()),
            "shift_max": int(annulus[1:].max()),
        },
        "realizations": [
            {**label, "counts_by_radius": {f"{r:g}": int(v) for r, v in zip(RADII_ARCSEC, row)},
             "annulus_gt_0p1_le_1arcsec": int(a)}
            for label, row, a in zip(labels, counts, annulus)
        ],
    }


def describe(frame: pd.DataFrame) -> dict[str, object]:
    fields = {}
    for column in ("z", "original_score", "match_separation_arcsec", "deltachi2"):
        values = pd.to_numeric(frame[column], errors="coerce").dropna().to_numpy(np.float64)
        q25, median, q75 = np.quantile(values, [0.25, 0.5, 0.75])
        fields[column] = {
            "n": int(len(values)), "q25": float(q25), "median": float(median), "q75": float(q75),
            "min": float(values.min()), "max": float(values.max()),
        }
    return {
        "rows": int(len(frame)),
        "spectype_counts": {str(k): int(v) for k, v in frame.spectype.value_counts().sort_index().items()},
        "fields": fields,
    }


def write_figure(path: Path, parent: dict[str, object], strict: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.7), constrained_layout=True)
    for ax, title, summary in zip(axes, ["Science-bit parent", "Warning-free global primary"], [parent, strict]):
        curve = summary["radius_curve"]
        x = np.array([row["radius_arcsec"] for row in curve])
        observed = np.array([row["observed"] for row in curve])
        mean = np.array([row["shift_mean"] for row in curve])
        low = np.array([row["shift_min"] for row in curve])
        high = np.array([row["shift_max"] for row in curve])
        ax.fill_between(x, low, high, color="#9ca3af", alpha=0.35, label="16-shift range")
        ax.plot(x, mean, "o--", color="#4b5563", label="shift mean")
        ax.plot(x, observed, "o-", color="#b42318", label="observed")
        ax.set(xlabel="Match radius (arcsec)", ylabel="Associated cluster positions", title=title)
        ax.set_yscale("log")
        ax.grid(alpha=0.2)
    axes[0].legend(frameon=False, fontsize=8)
    fig.savefig(path)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clusters", type=Path, required=True)
    parser.add_argument("--fits", type=Path, required=True)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--warned", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--sensitivity-csv", type=Path, required=True)
    parser.add_argument("--tail-csv", type=Path, required=True)
    parser.add_argument("--figure", type=Path, required=True)
    parser.add_argument("--chunk-rows", type=int, default=200_000)
    args = parser.parse_args()

    clusters = load_cluster_centers(args.clusters)
    primary = pd.read_parquet(args.primary)
    warned = pd.read_parquet(args.warned)
    tree, labels = build_control_tree(clusters)
    parent_min, strict_min, totals = scan_associations(
        args.fits, tree, len(clusters), len(labels), args.chunk_rows
    )
    if totals["fits_rows"] != 28_425_963 or totals["parent_rows"] != 20_299_155:
        raise RuntimeError(f"unexpected streamed totals: {totals}")

    sensitivity = primary[["candidate_id", "cluster_id", "targetid", "match_separation_arcsec",
                           "original_member_separation_arcsec"]].copy()
    sensitivity["original_member_match_le_1arcsec"] = (
        sensitivity["original_member_separation_arcsec"] <= 1.0
    )
    sensitivity["original_member_sensitivity_status"] = np.where(
        sensitivity["original_member_match_le_1arcsec"], "retained", "removed"
    )
    if int((~sensitivity.original_member_match_le_1arcsec).sum()) != 1:
        raise RuntimeError("expected exactly one released row to fail the original-member 1-arcsec rule")
    tail = sensitivity.loc[primary.match_separation_arcsec > 0.1].copy()
    if len(tail) != 11:
        raise RuntimeError(f"expected 11 positional-tail rows, found {len(tail)}")

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    sensitivity.to_csv(args.sensitivity_csv, index=False, float_format="%.12g")
    tail.to_csv(args.tail_csv, index=False, float_format="%.12g")
    parent_summary = radius_summary(parent_min, labels)
    strict_summary = radius_summary(strict_min, labels)
    payload = {
        "schema": "p3-apjs-r6-science-controls-v1",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "interpretation_boundary": (
            "Deterministic local-shift association and descriptive cohort controls only; "
            "not a selection-bias correction, physical classification, or candidate-level identity proof."
        ),
        "inputs": {
            "clusters": {"path": str(args.clusters), "sha256": sha256_file(args.clusters), "rows": len(clusters)},
            "fits": {"path": str(args.fits), "sha256": sha256_file(args.fits), "bytes": args.fits.stat().st_size},
            "primary": {"path": str(args.primary), "sha256": sha256_file(args.primary), "rows": len(primary)},
            "warned": {"path": str(args.warned), "sha256": sha256_file(args.warned), "rows": len(warned)},
        },
        "shift_design": {
            "offsets_arcsec": list(SHIFT_RADII_ARCSEC),
            "position_angles_deg": list(SHIFT_POSITION_ANGLES_DEG),
            "realizations": 16,
            "method": "fixed great-circle local tangent shifts; nearest eligible target per shifted cluster position",
        },
        "stream_totals": totals,
        "association_control": {"parent": parent_summary, "strict": strict_summary},
        "accepted_vs_warning_bearing": {"accepted": describe(primary), "warning_bearing": describe(warned)},
        "original_member_1arcsec_sensitivity": {
            "expression": "original_member_separation_arcsec <= 1.0",
            "retained": int(sensitivity.original_member_match_le_1arcsec.sum()),
            "removed": int((~sensitivity.original_member_match_le_1arcsec).sum()),
            "removed_candidate_ids": sensitivity.loc[
                ~sensitivity.original_member_match_le_1arcsec, "candidate_id"
            ].tolist(),
            "removed_separations_arcsec": sensitivity.loc[
                ~sensitivity.original_member_match_le_1arcsec, "original_member_separation_arcsec"
            ].tolist(),
        },
    }
    args.output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    write_figure(args.figure, parent_summary, strict_summary)
    print(json.dumps({"output": str(args.output_json), "parent": parent_summary["radius_curve"][-1],
                      "strict": strict_summary["radius_curve"][-1],
                      "tail": strict_summary["annulus_gt_0p1_le_1arcsec"]}, sort_keys=True))


if __name__ == "__main__":
    main()
