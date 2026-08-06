#!/usr/bin/env python3
"""Phase-3 candidate-family taxonomy for the AUG-011 flagship unmatched subset.

Port of the historical clustering method behind
`pipelines/p1_highz_tracers/outputs/uncataloged_taxonomy/classify_uncataloged.py`
(PCA -> UMAP -> HDBSCAN[leaf] -> kNN noise reassignment -> rule-based
labeling -> family merge) onto `crossmatch_flagship.py`'s unmatched output,
i.e. the new-generation analog of the historical 1,127-object "uncataloged"
slice (`ANOMALY_FLAGSHIP_MANUSCRIPT_ARCHITECTURE_2026-08-05.md` Sec.2c).

**Historical-tooling gap (read before trusting the labels this emits).** The
historical script clustered on 128-dim autoencoder LATENT vectors and then
labeled clusters using an astrophysics-specific decision tree keyed on WISE
colors (`gr_color`, `rz_color`, `w1w2_color`), DESI pipeline `spectype`/
`morphtype`, `peak_residual_wavelength` (rest-frame line ID), `deltachi2`,
and `zwarn` — ALL of those columns lived in the historical
`enhanced_18M_deduped` Parquet schema. The AUG-011 `run_scan.py` shard
schema does not carry any of them (`targetid`, `anomaly_score`, `mean_mse`,
`healpix`, `survey`, `program` only — see `build_flagship_sample.py`'s
docstring for the same gap noted at the sample-selection stage), so
`crossmatch_flagship.py`'s output only adds `ra`/`dec` on top of that. There
is currently no companion export of latent vectors, colors, spectype, or
line IDs for the new generation.

Consequently this script ports the clustering METHOD faithfully (PCA -> UMAP
-> HDBSCAN[leaf] -> kNN reassignment -> rule-merge) but runs it over
whatever numeric feature columns are actually present
(`anomaly_score`/`ra`/`dec` by default, plus anything joined in via
`--extra-features`), and labels clusters with GENERIC, DATA-SUPPORTED
descriptors only: an anomaly-score tier (from configurable quantile
cutpoints over the WHOLE unmatched sample, never hardcoded) and the
cluster's dominant `survey`/`program` provenance. Per directive Q1 (no
discovery language) this also means: no astrophysical family names
(AGN/QSO/post-starburst/etc.) are assigned, because assigning them would
require color/spectral-type data this generation does not yet have —
inventing such a label from `anomaly_score`/`ra`/`dec` alone would be
fabrication, not classification. Producing astrophysically-labeled families
comparable to the historical 10-family/76-AGN/27-post-starburst breakdown
requires a companion feature-extraction step (colors, spectype, latents) for
the new generation that does not exist yet; that is out of scope here and
is a real, open gap for whoever picks up Sec.5's "Taxonomy" dependency gate.
If `--extra-features` supplies richer per-targetid columns in the future,
this script's labeling can be extended additively without touching the
clustering pipeline.

Uses `sklearn.cluster.HDBSCAN` (built into scikit-learn >= 1.3) rather than
the historical standalone `hdbscan` package, and `umap-learn` for the 2D
embedding (imported lazily; installs required on the runtime host, not
bundled with this repo's offline test environment — see RUNBOOK Phase 3).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derive_locator_inventory import read_json, require_sha, sha256_file, write_json_atomic  # noqa: E402

DEFAULT_FEATURE_COLUMNS = ("anomaly_score", "ra", "dec")
DEFAULT_SCORE_TIER_QUANTILES = (0.50, 0.80, 0.95)
DEFAULT_SCORE_TIER_LABELS = ("low", "elevated", "high", "extreme")


class TaxonomyError(RuntimeError):
    """Raised when the taxonomy inputs cannot be trusted or clustered safely."""


def verify_input_unmatched(unmatched_path: Path, crossmatch_manifest: dict[str, Any]) -> None:
    if not unmatched_path.is_file():
        raise TaxonomyError(f"input unmatched table is absent: {unmatched_path}")
    expected = crossmatch_manifest.get("unmatched_output", {}).get("sha256")
    require_sha(expected, "crossmatch manifest unmatched_output.sha256")
    observed = sha256_file(unmatched_path)
    if observed != expected:
        raise TaxonomyError(
            f"unmatched table SHA-256 mismatch: expected {expected}, got {observed} for {unmatched_path}"
        )


def load_feature_table(
    unmatched_path: Path,
    extra_features_path: Path | None,
    feature_columns: tuple[str, ...],
) -> tuple[list[int], np.ndarray, dict[str, list[Any]]]:
    """Load the unmatched table and (optionally) join extra numeric features.

    Returns (targetids, feature_matrix, metadata_columns) where
    metadata_columns carries `survey`/`program`/`anomaly_score` for
    descriptive labeling, kept separate from the numeric feature matrix fed
    to PCA/UMAP/HDBSCAN.
    """
    import pyarrow.parquet as pq

    table = pq.read_table(unmatched_path)
    frame = table.to_pydict()
    n = len(frame["targetid"])
    if n == 0:
        raise TaxonomyError("unmatched table has zero rows; nothing to cluster")
    targetids = [int(t) for t in frame["targetid"]]

    extra: dict[int, dict[str, float]] = {}
    if extra_features_path is not None:
        extra_table = pq.read_table(extra_features_path).to_pydict()
        if "targetid" not in extra_table:
            raise TaxonomyError("--extra-features must have a targetid column")
        extra_columns = [c for c in extra_table if c != "targetid"]
        for i, tid in enumerate(extra_table["targetid"]):
            extra[int(tid)] = {c: extra_table[c][i] for c in extra_columns}

    resolved_columns = list(feature_columns)
    if extra:
        any_row = next(iter(extra.values()))
        resolved_columns = resolved_columns + [c for c in any_row if c not in resolved_columns]

    matrix = np.zeros((n, len(resolved_columns)), dtype=np.float64)
    for j, column in enumerate(resolved_columns):
        if column in frame:
            matrix[:, j] = np.array([np.nan if v is None else float(v) for v in frame[column]])
        else:
            for i, tid in enumerate(targetids):
                value = extra.get(tid, {}).get(column)
                matrix[i, j] = np.nan if value is None else float(value)
    matrix = np.nan_to_num(matrix, nan=0.0, posinf=0.0, neginf=0.0)

    metadata = {
        "anomaly_score": [float(v) for v in frame.get("anomaly_score", [0.0] * n)],
        "survey": [str(v) for v in frame.get("survey", ["unknown"] * n)],
        "program": [str(v) for v in frame.get("program", ["unknown"] * n)],
        "ra": [float(v) for v in frame.get("ra", [0.0] * n)],
        "dec": [float(v) for v in frame.get("dec", [0.0] * n)],
    }
    return targetids, matrix, metadata


def cluster_features(
    matrix: np.ndarray,
    pca_components: int,
    umap_neighbors: int,
    umap_min_dist: float,
    min_cluster_size: int,
    min_samples: int,
    random_state: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """PCA -> UMAP -> HDBSCAN(leaf) -> kNN noise reassignment.

    Returns (embedding_2d, cluster_labels, is_core_member).
    """
    from sklearn.cluster import HDBSCAN
    from sklearn.neighbors import NearestNeighbors
    from sklearn.preprocessing import StandardScaler

    n_samples, n_features = matrix.shape
    if n_samples < 2:
        raise TaxonomyError("need at least 2 objects to cluster")

    scaled = StandardScaler().fit_transform(matrix)

    n_components = max(1, min(pca_components, n_features, n_samples - 1))
    if n_features > n_components:
        from sklearn.decomposition import PCA

        reduced = PCA(n_components=n_components, random_state=random_state).fit_transform(scaled)
    else:
        reduced = scaled

    try:
        import umap
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise TaxonomyError(
            "umap-learn is required for taxonomy clustering (pip install umap-learn)"
        ) from exc

    neighbors = max(2, min(umap_neighbors, n_samples - 1))
    embedding = umap.UMAP(
        n_components=2, n_neighbors=neighbors, min_dist=umap_min_dist,
        random_state=random_state, n_jobs=1,
    ).fit_transform(reduced)

    clusterer = HDBSCAN(
        min_cluster_size=max(2, min(min_cluster_size, n_samples)),
        min_samples=min_samples,
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
        # Degenerate case (e.g. tiny synthetic input): treat everything as
        # one candidate family rather than raising, so a small honest sample
        # still yields a usable (if trivial) taxonomy.
        labels = np.zeros(len(labels), dtype=int)

    return embedding, labels, is_core


def score_tier_label(score: float, cutpoints: list[float], tier_labels: tuple[str, ...]) -> str:
    for cutpoint, label in zip(cutpoints, tier_labels):
        if score < cutpoint:
            return label
    return tier_labels[-1]


def characterize_and_label(
    targetids: list[int],
    labels: np.ndarray,
    is_core: np.ndarray,
    metadata: dict[str, list[Any]],
    score_tier_quantiles: tuple[float, ...],
    score_tier_labels: tuple[str, ...],
) -> dict[int, dict[str, Any]]:
    """Rule-based, GENERIC candidate-family labeling (directive Q1: descriptive only)."""
    scores = np.array(metadata["anomaly_score"], dtype=np.float64)
    cutpoints = [float(np.quantile(scores, q)) for q in score_tier_quantiles]

    clusters: dict[int, dict[str, Any]] = {}
    for cluster_id in sorted(set(int(l) for l in labels)):
        mask = labels == cluster_id
        indices = np.nonzero(mask)[0]
        cluster_scores = scores[indices]
        surveys = [metadata["survey"][i] for i in indices]
        programs = [metadata["program"][i] for i in indices]
        ra_vals = [metadata["ra"][i] for i in indices]
        dec_vals = [metadata["dec"][i] for i in indices]

        dominant_survey = max(set(surveys), key=surveys.count)
        dominant_program = max(set(programs), key=programs.count)
        score_median = float(np.median(cluster_scores))
        tier = score_tier_label(score_median, cutpoints, score_tier_labels)

        descriptor = f"{tier}-anomaly-score candidate family (survey={dominant_survey}, program={dominant_program})"

        clusters[cluster_id] = {
            "cluster_id": cluster_id,
            "n_objects": int(mask.sum()),
            "n_core": int(is_core[mask].sum()),
            "score_median": score_median,
            "score_mean": float(np.mean(cluster_scores)),
            "score_min": float(np.min(cluster_scores)),
            "score_max": float(np.max(cluster_scores)),
            "score_tier": tier,
            "dominant_survey": dominant_survey,
            "dominant_program": dominant_program,
            "ra_range": [float(min(ra_vals)), float(max(ra_vals))],
            "dec_range": [float(min(dec_vals)), float(max(dec_vals))],
            "family_descriptor": descriptor,
            "rationale": (
                f"score_tier={tier} (median={score_median:.2f}, cutpoints={cutpoints}); "
                f"dominant survey/program={dominant_survey}/{dominant_program}"
            ),
        }
    return clusters


def merge_families(clusters: dict[int, dict[str, Any]]) -> tuple[dict[int, dict[str, Any]], dict[int, int]]:
    """Merge clusters that produced an identical descriptor into one family."""
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
            "score_tier": clusters[cluster_ids[0]]["score_tier"],
            "dominant_survey": clusters[cluster_ids[0]]["dominant_survey"],
            "dominant_program": clusters[cluster_ids[0]]["dominant_program"],
        }
    return family_info, cluster_to_family


def build_taxonomy(
    unmatched_path: Path,
    crossmatch_manifest_path: Path,
    output_results: Path,
    output_manifest: Path,
    extra_features_path: Path | None = None,
    feature_columns: tuple[str, ...] = DEFAULT_FEATURE_COLUMNS,
    pca_components: int = 10,
    umap_neighbors: int = 15,
    umap_min_dist: float = 0.05,
    min_cluster_size: int = 15,
    min_samples: int = 3,
    random_state: int = 42,
    score_tier_quantiles: tuple[float, ...] = DEFAULT_SCORE_TIER_QUANTILES,
    score_tier_labels: tuple[str, ...] = DEFAULT_SCORE_TIER_LABELS,
) -> dict[str, Any]:
    crossmatch_manifest = read_json(crossmatch_manifest_path)
    verify_input_unmatched(unmatched_path, crossmatch_manifest)

    targetids, matrix, metadata = load_feature_table(unmatched_path, extra_features_path, feature_columns)
    embedding, labels, is_core = cluster_features(
        matrix, pca_components, umap_neighbors, umap_min_dist, min_cluster_size, min_samples, random_state
    )
    clusters = characterize_and_label(targetids, labels, is_core, metadata, score_tier_quantiles, score_tier_labels)
    family_info, cluster_to_family = merge_families(clusters)

    objects = []
    for i, targetid in enumerate(targetids):
        cid = int(labels[i])
        fid = cluster_to_family[cid]
        objects.append(
            {
                "targetid": targetid,
                "ra": metadata["ra"][i],
                "dec": metadata["dec"][i],
                "anomaly_score": metadata["anomaly_score"][i],
                "survey": metadata["survey"][i],
                "program": metadata["program"][i],
                "cluster_id": cid,
                "family_id": fid,
                "family_descriptor": family_info[fid]["family_descriptor"],
                "is_core_member": bool(is_core[i]),
                "umap_x": float(embedding[i, 0]),
                "umap_y": float(embedding[i, 1]),
            }
        )

    results = {
        "metadata": {
            "total_objects": len(targetids),
            "n_clusters": len(clusters),
            "n_families": len(family_info),
            "method": "PCA -> UMAP(2, n_neighbors, min_dist) -> HDBSCAN(leaf, min_cluster_size, min_samples) "
                      "-> kNN noise reassignment -> descriptor-identity family merge",
            "feature_columns": list(feature_columns),
            "source": "AUG-011 flagship candidate sample, crossmatch-unmatched subset (no SIMBAD/NED match)",
            "labeling_policy": "candidate-family descriptors only (directive Q1); no astrophysical class names",
        },
        "families": {str(fid): info for fid, info in family_info.items()},
        "clusters": {str(cid): c for cid, c in clusters.items()},
        "objects": objects,
    }
    write_json_atomic(output_results, results)
    results_sha256 = sha256_file(output_results)

    import sklearn

    try:
        import umap

        umap_version = getattr(umap, "__version__", "unknown")
    except ImportError:
        umap_version = "unavailable"

    manifest = {
        "manifest_version": "flagship-taxonomy/v1",
        "created_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "versions": {"sklearn": sklearn.__version__, "umap_learn": umap_version, "numpy": np.__version__},
        "params": {
            "feature_columns": list(feature_columns),
            "pca_components": pca_components,
            "umap_neighbors": umap_neighbors,
            "umap_min_dist": umap_min_dist,
            "min_cluster_size": min_cluster_size,
            "min_samples": min_samples,
            "random_state": random_state,
            "score_tier_quantiles": list(score_tier_quantiles),
            "score_tier_labels": list(score_tier_labels),
        },
        "input_unmatched_sha256": sha256_file(unmatched_path),
        "input_crossmatch_manifest": crossmatch_manifest_path.name,
        "n_objects": len(targetids),
        "n_clusters": len(clusters),
        "n_families": len(family_info),
        "output_results": {"file_name": output_results.name, "sha256": results_sha256},
    }
    write_json_atomic(output_manifest, manifest)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input-unmatched", type=Path, required=True, help="crossmatch_flagship.py's unmatched Parquet output")
    parser.add_argument("--input-crossmatch-manifest", type=Path, required=True)
    parser.add_argument("--extra-features", type=Path, default=None, help="optional Parquet keyed by targetid with extra numeric feature columns")
    parser.add_argument("--feature-columns", type=str, default=",".join(DEFAULT_FEATURE_COLUMNS))
    parser.add_argument("--pca-components", type=int, default=10)
    parser.add_argument("--umap-neighbors", type=int, default=15)
    parser.add_argument("--umap-min-dist", type=float, default=0.05)
    parser.add_argument("--min-cluster-size", type=int, default=15)
    parser.add_argument("--min-samples", type=int, default=3)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument("--score-tier-quantiles", type=str, default=",".join(str(q) for q in DEFAULT_SCORE_TIER_QUANTILES))
    parser.add_argument("--score-tier-labels", type=str, default=",".join(DEFAULT_SCORE_TIER_LABELS))
    parser.add_argument("--output-results", type=Path, required=True)
    parser.add_argument("--output-manifest", type=Path, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    feature_columns = tuple(c.strip() for c in args.feature_columns.split(",") if c.strip())
    score_tier_quantiles = tuple(float(q) for q in args.score_tier_quantiles.split(","))
    score_tier_labels = tuple(l.strip() for l in args.score_tier_labels.split(","))
    manifest = build_taxonomy(
        args.input_unmatched, args.input_crossmatch_manifest, args.output_results, args.output_manifest,
        extra_features_path=args.extra_features, feature_columns=feature_columns,
        pca_components=args.pca_components, umap_neighbors=args.umap_neighbors, umap_min_dist=args.umap_min_dist,
        min_cluster_size=args.min_cluster_size, min_samples=args.min_samples, random_state=args.random_state,
        score_tier_quantiles=score_tier_quantiles, score_tier_labels=score_tier_labels,
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
