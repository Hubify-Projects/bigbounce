#!/usr/bin/env python3
"""DAF-19 corrected re-clustering: spherical RA/Dec embedding, every
hyperparameter and seed stated, plus a (survey, programme) selection
baseline.

Fixes, relative to the published run
(`pipelines/p1_highz_tracers/clean_rerun/taxonomy_flagship.py`,
`flagship_taxonomy_v2.json`, manifest params below):

1. RA-wrap artifact: the published run fed raw (ra, dec) in degrees into
   Euclidean PCA/UMAP/HDBSCAN. RA is periodic at 360 deg, so objects near
   alpha=0 on either side were treated as maximally distant, and Table
   VIII's own RA spans (up to 350 deg) are the signature of exactly that.
   Fix: embed sky position as a unit vector on the sphere,
   (cos(ra)cos(dec), sin(ra)cos(dec), sin(dec)), so Euclidean distance in
   the embedded 3-space is a monotonic (chordal) function of the true
   great-circle separation and the wrap disappears by construction.
2. Missing hyperparameters: every UMAP/HDBSCAN setting and the random seed
   are recorded in the output manifest (this run intentionally reuses the
   published run's exact numeric hyperparameters -- same
   pca_components/umap_neighbors/umap_min_dist/min_cluster_size/
   min_samples/random_state -- so the *only* thing that changes between
   the published and corrected taxonomies is the RA-wrap fix, isolating
   its effect).
3. Near-vacuous PCA: unchanged in kind (4 input features after adding the
   spherical embedding is still <= pca_components, so PCA remains a
   rotation/rescale step, not a dimensionality reduction) -- reported
   honestly rather than silently carried forward.

Also runs the disposition-named (survey, programme) baseline: a trivial
partition by the object's own (survey, programme) pair, compared against
the corrected taxonomy's family labels via Adjusted Rand Index (ARI) and
Adjusted Mutual Information (AMI), the same comparison already reported in
the published paper's Sec. "What the families are" for the *published*
taxonomy (70.4% dominant-cell purity). Running it here lets the corrected
taxonomy be graded on the same axis.
"""

from __future__ import annotations

import hashlib
import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]
PHASE3_V2_DIR = (
    REPO_ROOT
    / "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2"
)
PUBLISHED_TAXONOMY_JSON = PHASE3_V2_DIR / "flagship_taxonomy_v2.json"
INPUT_UNMATCHED = PHASE3_V2_DIR / "flagship_crossmatch_v2_unmatched.parquet"
INPUT_UNMATCHED_EXPECTED_SHA256 = (
    "c0a6b57bd672f81b1424a65449f99d891810073ea59e600c1fc35cfec30eb7c3"
)

OUT_DIR = HERE / "outputs"

# Reused verbatim from the published run's manifest
# (flagship_taxonomy_v2_manifest.json) so the RA-wrap fix is the only
# variable changed between the published and corrected taxonomies.
PCA_COMPONENTS = 10
UMAP_NEIGHBORS = 15
UMAP_MIN_DIST = 0.05
MIN_CLUSTER_SIZE = 15
MIN_SAMPLES = 3
RANDOM_STATE = 42
SCORE_TIER_QUANTILES = (0.50, 0.80, 0.95)
SCORE_TIER_LABELS = ("low", "elevated", "high", "extreme")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True))


def load_unmatched(path: Path) -> dict[str, list[Any]]:
    import pyarrow.parquet as pq

    return pq.read_table(path).to_pydict()


def spherical_embedding(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)
    x = np.cos(ra) * np.cos(dec)
    y = np.sin(ra) * np.cos(dec)
    z = np.sin(dec)
    return np.stack([x, y, z], axis=1)


def cluster_features(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """PCA -> UMAP -> HDBSCAN(leaf) -> kNN noise reassignment.

    Identical algorithm/hyperparameters to the published
    `taxonomy_flagship.py::cluster_features`; only the input `matrix`
    differs (spherical embedding instead of raw ra/dec).
    """
    from sklearn.cluster import HDBSCAN
    from sklearn.decomposition import PCA
    from sklearn.neighbors import NearestNeighbors
    from sklearn.preprocessing import StandardScaler

    n_samples, n_features = matrix.shape
    scaled = StandardScaler().fit_transform(matrix)

    n_components = max(1, min(PCA_COMPONENTS, n_features, n_samples - 1))
    pca_reduced_dimension = n_features > n_components
    if pca_reduced_dimension:
        reduced = PCA(n_components=n_components, random_state=RANDOM_STATE).fit_transform(scaled)
    else:
        reduced = scaled

    import umap

    neighbors = max(2, min(UMAP_NEIGHBORS, n_samples - 1))
    embedding = umap.UMAP(
        n_components=2,
        n_neighbors=neighbors,
        min_dist=UMAP_MIN_DIST,
        random_state=RANDOM_STATE,
        n_jobs=1,
    ).fit_transform(reduced)

    clusterer = HDBSCAN(
        min_cluster_size=max(2, min(MIN_CLUSTER_SIZE, n_samples)),
        min_samples=MIN_SAMPLES,
        cluster_selection_method="leaf",
    )
    raw_labels = clusterer.fit_predict(embedding)

    labels = raw_labels.copy()
    is_core = np.ones(len(labels), dtype=bool)
    noise_mask = raw_labels == -1
    if noise_mask.any() and (~noise_mask).any():
        clustered_mask = ~noise_mask
        knn = NearestNeighbors(n_neighbors=1, metric="euclidean")
        knn.fit(embedding[clustered_mask])
        _, indices = knn.kneighbors(embedding[noise_mask])
        labels[noise_mask] = raw_labels[clustered_mask][indices.flatten()]
        is_core[noise_mask] = False
    elif noise_mask.all():
        labels = np.zeros(len(labels), dtype=int)

    return embedding, labels, is_core, pca_reduced_dimension


def score_tier_label(score: float, cutpoints: list[float]) -> str:
    for cutpoint, label in zip(cutpoints, SCORE_TIER_LABELS):
        if score < cutpoint:
            return label
    return SCORE_TIER_LABELS[-1]


def characterize_and_label(
    labels: np.ndarray,
    is_core: np.ndarray,
    scores: np.ndarray,
    surveys: list[str],
    programs: list[str],
    ra: np.ndarray,
    dec: np.ndarray,
) -> dict[int, dict[str, Any]]:
    cutpoints = [float(np.quantile(scores, q)) for q in SCORE_TIER_QUANTILES]
    clusters: dict[int, dict[str, Any]] = {}
    for cid in sorted(set(int(l) for l in labels)):
        mask = labels == cid
        idx = np.nonzero(mask)[0]
        cl_scores = scores[idx]
        cl_surveys = [surveys[i] for i in idx]
        cl_programs = [programs[i] for i in idx]
        dominant_survey = max(set(cl_surveys), key=cl_surveys.count)
        dominant_program = max(set(cl_programs), key=cl_programs.count)
        score_median = float(np.median(cl_scores))
        tier = score_tier_label(score_median, cutpoints)
        descriptor = f"{tier}-anomaly-score candidate family (survey={dominant_survey}, program={dominant_program})"
        clusters[cid] = {
            "cluster_id": cid,
            "n_objects": int(mask.sum()),
            "n_core": int(is_core[mask].sum()),
            "score_median": score_median,
            "score_tier": tier,
            "dominant_survey": dominant_survey,
            "dominant_program": dominant_program,
            "ra_range": [float(ra[idx].min()), float(ra[idx].max())],
            "ra_span_deg": float(ra_span(ra[idx])),
            "dec_range": [float(dec[idx].min()), float(dec[idx].max())],
            "family_descriptor": descriptor,
        }
    return clusters


def ra_span(ra_deg: np.ndarray) -> float:
    """Minimum-arc RA span (deg), correctly handling the 360 deg wrap.

    Used only for *reporting* the corrected taxonomy's own diagnostic
    table honestly (so the fix isn't undercut by a wrap bug in the
    diagnostic itself) -- unrelated to the clustering feature fix above.
    """
    if len(ra_deg) <= 1:
        return 0.0
    ang = np.sort(np.mod(ra_deg, 360.0))
    gaps = np.diff(np.concatenate([ang, [ang[0] + 360.0]]))
    largest_gap = gaps.max()
    return float(360.0 - largest_gap)


def merge_families(clusters: dict[int, dict[str, Any]]) -> tuple[dict[int, dict[str, Any]], dict[int, int]]:
    groups: dict[str, list[int]] = {}
    for cid, c in clusters.items():
        groups.setdefault(c["family_descriptor"], []).append(cid)
    family_info: dict[int, dict[str, Any]] = {}
    cluster_to_family: dict[int, int] = {}
    ordered = sorted(groups.items(), key=lambda kv: -sum(clusters[c]["n_objects"] for c in kv[1]))
    for family_id, (descriptor, cluster_ids) in enumerate(ordered):
        total_n = sum(clusters[c]["n_objects"] for c in cluster_ids)
        for cid in cluster_ids:
            cluster_to_family[cid] = family_id
        family_info[family_id] = {
            "family_id": family_id,
            "family_descriptor": descriptor,
            "n_objects": total_n,
            "source_clusters": cluster_ids,
        }
    return family_info, cluster_to_family


def survey_program_baseline(surveys: list[str], programs: list[str]) -> np.ndarray:
    """Trivial (survey, programme) partition -- the disposition-named
    selection baseline the corrected taxonomy is compared against."""
    pairs = list(zip(surveys, programs))
    unique = sorted(set(pairs))
    pair_to_id = {p: i for i, p in enumerate(unique)}
    return np.array([pair_to_id[p] for p in pairs], dtype=int)


def main() -> None:
    t_start = time.time()
    print("LAF4-af-reclustering START verifying input hash", flush=True)
    observed_sha = sha256_file(INPUT_UNMATCHED)
    if observed_sha != INPUT_UNMATCHED_EXPECTED_SHA256:
        raise SystemExit(
            f"input sha256 mismatch: expected {INPUT_UNMATCHED_EXPECTED_SHA256}, got {observed_sha}"
        )

    frame = load_unmatched(INPUT_UNMATCHED)
    n = len(frame["targetid"])
    assert n == 675, f"expected 675 unmatched objects, got {n}"
    targetids = [int(t) for t in frame["targetid"]]
    ra = np.array([float(v) for v in frame["ra"]])
    dec = np.array([float(v) for v in frame["dec"]])
    scores = np.array([float(v) for v in frame["anomaly_score"]])
    surveys = [str(v) for v in frame["survey"]]
    programs = [str(v) for v in frame["program"]]

    sky_xyz = spherical_embedding(ra, dec)
    matrix = np.concatenate([scores.reshape(-1, 1), sky_xyz], axis=1)  # (score, x, y, z)

    print("LAF4-af-reclustering MILESTONE running PCA->UMAP->HDBSCAN on spherical embedding", flush=True)
    embedding, labels, is_core, pca_reduced_dimension = cluster_features(matrix)
    clusters = characterize_and_label(labels, is_core, scores, surveys, programs, ra, dec)
    family_info, cluster_to_family = merge_families(clusters)

    objects = []
    for i, tid in enumerate(targetids):
        cid = int(labels[i])
        fid = cluster_to_family[cid]
        objects.append(
            {
                "targetid": tid,
                "cluster_id": cid,
                "family_id": fid,
                "family_descriptor": family_info[fid]["family_descriptor"],
                "is_core_member": bool(is_core[i]),
            }
        )

    results = {
        "metadata": {
            "total_objects": n,
            "n_clusters": len(clusters),
            "n_families": len(family_info),
            "method": "spherical-embedding PCA -> UMAP(2, n_neighbors, min_dist) -> "
                      "HDBSCAN(leaf, min_cluster_size, min_samples) -> kNN noise reassignment "
                      "-> descriptor-identity family merge",
            "feature_columns": ["anomaly_score", "sky_x", "sky_y", "sky_z"],
            "sky_embedding": "unit vector (cos(ra)cos(dec), sin(ra)cos(dec), sin(dec)), ra/dec in degrees converted to radians",
            "pca_reduced_dimension": pca_reduced_dimension,
            "source": "AUG-011 flagship candidate sample, crossmatch-unmatched subset (no SIMBAD/NED match) -- same 675-object input as the published taxonomy",
        },
        "families": {str(fid): info for fid, info in family_info.items()},
        "clusters": {str(cid): c for cid, c in clusters.items()},
        "objects": objects,
    }
    write_json(OUT_DIR / "flagship_taxonomy_corrected.json", results)

    # --- (survey, programme) baseline comparison ---
    from sklearn.metrics import adjusted_mutual_info_score, adjusted_rand_score

    baseline_labels = survey_program_baseline(surveys, programs)
    corrected_family_labels = np.array([cluster_to_family[int(l)] for l in labels])

    ari_vs_baseline = float(adjusted_rand_score(baseline_labels, corrected_family_labels))
    ami_vs_baseline = float(adjusted_mutual_info_score(baseline_labels, corrected_family_labels))

    # --- comparison against the published (defective) taxonomy, same 675 objects ---
    published = json.loads(PUBLISHED_TAXONOMY_JSON.read_text())
    published_family_by_tid = {
        int(o["targetid"]): int(o["family_id"]) for o in published["objects"]
    }
    published_labels_aligned = np.array([published_family_by_tid[tid] for tid in targetids])
    ari_vs_published = float(adjusted_rand_score(published_labels_aligned, corrected_family_labels))
    ami_vs_published = float(adjusted_mutual_info_score(published_labels_aligned, corrected_family_labels))

    n_unique_baseline_cells = int(len(set(zip(surveys, programs))))

    comparison = {
        "n_objects": n,
        "published_taxonomy": {
            "n_clusters": published["metadata"]["n_clusters"],
            "n_families": published["metadata"]["n_families"],
        },
        "corrected_taxonomy": {
            "n_clusters": len(clusters),
            "n_families": len(family_info),
        },
        "corrected_vs_published": {
            "adjusted_rand_index": ari_vs_published,
            "adjusted_mutual_info": ami_vs_published,
        },
        "corrected_vs_survey_programme_baseline": {
            "n_survey_programme_cells": n_unique_baseline_cells,
            "adjusted_rand_index": ari_vs_baseline,
            "adjusted_mutual_info": ami_vs_baseline,
        },
    }
    write_json(OUT_DIR / "comparison_metrics.json", comparison)

    wall_clock_s = time.time() - t_start

    import sklearn
    import umap as umap_module

    manifest = {
        "manifest_version": "daf19-corrected-taxonomy/v1",
        "created_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "lane": "LAF4-af-reclustering",
        "disposition": "DAF-19",
        "reproducibility_manifest_q2": {
            "external_data_sources": [],
            "apis_used": [],
            "input_files": [
                {
                    "path": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_crossmatch_v2_unmatched.parquet",
                    "sha256": INPUT_UNMATCHED_EXPECTED_SHA256,
                    "note": "identical file used for the published (defective) taxonomy -- verified byte-identical before this run",
                },
                {
                    "path": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_taxonomy_v2.json",
                    "sha256": sha256_file(PUBLISHED_TAXONOMY_JSON),
                    "note": "published taxonomy, used only as the comparison target",
                },
            ],
            "scripts": [
                "pipelines/p1_highz_tracers/anomaly_flagship_draft/reclustering_2026_09_22/recluster_spherical.py",
            ],
            "compute_venue": "local (Houston's machine), CPU only, no GPU required",
            "wall_clock_seconds": round(wall_clock_s, 2),
            "reproduction_cost_estimate": "free (local CPU, <1 minute, no external API calls)",
        },
        "versions": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "sklearn": sklearn.__version__,
            "umap_learn": getattr(umap_module, "__version__", "unknown"),
            "numpy": np.__version__,
        },
        "params": {
            "feature_columns": ["anomaly_score", "sky_x", "sky_y", "sky_z"],
            "sky_embedding": "unit-vector spherical embedding of (ra_deg, dec_deg)",
            "pca_components": PCA_COMPONENTS,
            "umap_neighbors": UMAP_NEIGHBORS,
            "umap_min_dist": UMAP_MIN_DIST,
            "min_cluster_size": MIN_CLUSTER_SIZE,
            "min_samples": MIN_SAMPLES,
            "random_state": RANDOM_STATE,
            "score_tier_quantiles": list(SCORE_TIER_QUANTILES),
            "score_tier_labels": list(SCORE_TIER_LABELS),
            "note": "numeric hyperparameters reused verbatim from the published run's manifest (flagship_taxonomy_v2_manifest.json) so the RA-wrap fix is isolated as the only changed variable",
        },
        "n_objects": n,
        "n_clusters": len(clusters),
        "n_families": len(family_info),
        "output_results": {
            "file_name": "flagship_taxonomy_corrected.json",
            "sha256": sha256_file(OUT_DIR / "flagship_taxonomy_corrected.json"),
        },
        "output_comparison": {
            "file_name": "comparison_metrics.json",
            "sha256": sha256_file(OUT_DIR / "comparison_metrics.json"),
        },
    }
    write_json(OUT_DIR / "reclustering_manifest.json", manifest)

    print("LAF4-af-reclustering MILESTONE corrected taxonomy written:", flush=True)
    print(json.dumps(comparison, indent=2), flush=True)
    print(f"LAF4-af-reclustering DONE wall_clock_s={wall_clock_s:.1f}", flush=True)


if __name__ == "__main__":
    main()
