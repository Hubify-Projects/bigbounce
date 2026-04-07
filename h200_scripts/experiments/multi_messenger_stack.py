#!/usr/bin/env python3
"""
Multi-Messenger Anomaly Stack — Objects Anomalous in 2+ Surveys
===============================================================
Find objects that appear as anomalies in MULTIPLE independent surveys.
An object flagged by DESI (optical) AND eROSITA (X-ray) AND LAMOST
(optical independent) is far more likely to be genuinely unusual than
any single-survey detection.

Pipeline:
  1. Load anomaly catalogs from all available surveys
  2. Cross-match within 3 arcsec (point sources) or 10 arcsec (X-ray)
  3. Find objects detected in 2+ independent surveys
  4. Rank by (N_surveys x combined_anomaly_score)
  5. Compute expected random match rate to assess significance
  6. Characterize multi-survey detections (redshift agreement, band coverage)

If real data unavailable: generates synthetic catalogs for 6 surveys
with planted multi-survey objects.

Output: multi-messenger-stack/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

import torch
from torch.utils.data import DataLoader, TensorDataset

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/multi-messenger-stack"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Cross-match radius in arcseconds
MATCH_RADIUS_ARCSEC = 3.0
XRAY_MATCH_RADIUS_ARCSEC = 10.0


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)


# ═══════════════════════════════════════════════════════
# Survey Configuration
# ═══════════════════════════════════════════════════════

SURVEY_CONFIG = {
    "desi-dr1": {
        "dirs": [
            Path("/workspace/bigbounce/outputs/desi-dr1"),
            Path("/workspace/bigbounce/pipelines/h200_results/desi_dr1"),
        ],
        "band": "optical",
        "match_radius": 3.0,
        "expected_n": 195000,
    },
    "sdss-dr18": {
        "dirs": [
            Path("/workspace/bigbounce/outputs/sdss-dr18"),
            Path("/workspace/bigbounce/pipelines/h200_results/sdss_dr18"),
        ],
        "band": "optical",
        "match_radius": 3.0,
        "expected_n": 77000,
    },
    "lamost-dr10": {
        "dirs": [
            Path("/workspace/bigbounce/outputs/lamost-dr10"),
            Path("/workspace/bigbounce/pipelines/h200_results/lamost_dr10"),
        ],
        "band": "optical",
        "match_radius": 3.0,
        "expected_n": 44000,
    },
    "erosita-dr1": {
        "dirs": [
            Path("/workspace/bigbounce/outputs/erosita-dr1"),
            Path("/workspace/bigbounce/pipelines/h200_results/erosita_dr1"),
        ],
        "band": "xray",
        "match_radius": 10.0,
        "expected_n": 9300,
    },
    "neowise": {
        "dirs": [
            Path("/workspace/bigbounce/outputs/neowise-ecliptic-mask"),
            Path("/workspace/bigbounce/pipelines/h200_results/neowise"),
        ],
        "band": "infrared",
        "match_radius": 5.0,
        "expected_n": 436,
    },
    "gaia-dr3": {
        "dirs": [
            Path("/workspace/bigbounce/outputs/gaia-dr3-expanded"),
            Path("/workspace/bigbounce/pipelines/h200_results/gaia_dr3"),
        ],
        "band": "optical",
        "match_radius": 1.0,
        "expected_n": 500,
    },
}


# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

def load_survey_catalog(survey_name, config):
    """Load anomaly catalog for a survey."""
    for d in config["dirs"]:
        if not d.exists():
            continue
        for pattern in ["*anomal*.csv", "*catalog*.csv", "*scores*.csv",
                        "*anomal*.parquet", "*summary*.json"]:
            for f in sorted(d.glob(pattern)):
                try:
                    if f.suffix == ".parquet":
                        df = pd.read_parquet(f)
                    elif f.suffix == ".json":
                        with open(f) as jf:
                            data = json.load(jf)
                        if isinstance(data, list):
                            df = pd.DataFrame(data)
                        elif isinstance(data, dict) and "anomalies" in data:
                            df = pd.DataFrame(data["anomalies"])
                        else:
                            continue
                    else:
                        df = pd.read_csv(f, nrows=300000)

                    if "ra" in df.columns and "dec" in df.columns:
                        # Ensure score column
                        score_col = None
                        for sc in ["anomaly_score", "score", "recon_error", "loss"]:
                            if sc in df.columns:
                                score_col = sc
                                break
                        if score_col is None:
                            df["anomaly_score"] = 1.0
                        else:
                            df["anomaly_score"] = df[score_col]

                        print(f"    {survey_name}: {len(df)} anomalies from {f.name}")
                        return df[["ra", "dec", "anomaly_score"]].copy(), str(f)
                except Exception:
                    continue
    return None, None


def generate_synthetic_catalogs(n_shared=500):
    """Generate synthetic anomaly catalogs for 6 surveys with planted multi-survey objects."""
    print(f"  Generating synthetic catalogs with {n_shared} planted multi-survey objects")
    np.random.seed(42)

    # Shared positions (objects that appear in multiple surveys)
    shared_ra = np.random.uniform(120, 260, n_shared)
    shared_dec = np.random.uniform(-10, 60, n_shared)

    catalogs = {}
    survey_sizes = {
        "desi-dr1": 195000,
        "sdss-dr18": 77000,
        "lamost-dr10": 44000,
        "erosita-dr1": 9300,
        "neowise": 436,
        "gaia-dr3": 500,
    }

    for survey, n_total in survey_sizes.items():
        # Fraction of shared objects included in this survey
        if survey in ["desi-dr1", "sdss-dr18"]:
            frac_shared = 0.8  # large optical surveys see most shared objects
        elif survey in ["lamost-dr10"]:
            frac_shared = 0.5
        elif survey == "erosita-dr1":
            frac_shared = 0.3
        else:
            frac_shared = 0.15

        n_shared_here = min(int(n_shared * frac_shared), n_total // 2)
        shared_idx = np.random.choice(n_shared, n_shared_here, replace=False)

        # Add positional scatter (astrometric error)
        scatter = 0.5 / 3600.0  # 0.5 arcsec in degrees
        if survey == "erosita-dr1":
            scatter = 3.0 / 3600.0  # X-ray has worse PSF

        shared_ra_here = shared_ra[shared_idx] + np.random.normal(0, scatter, n_shared_here)
        shared_dec_here = shared_dec[shared_idx] + np.random.normal(0, scatter, n_shared_here)
        shared_scores = np.exp(np.random.normal(5, 1.5, n_shared_here))  # high scores

        # Unique objects for this survey
        n_unique = n_total - n_shared_here
        unique_ra = np.random.uniform(100, 280, n_unique)
        unique_dec = np.random.uniform(-20, 80, n_unique)
        unique_scores = np.exp(np.random.normal(3, 1.5, n_unique))

        df = pd.DataFrame({
            "ra": np.concatenate([shared_ra_here, unique_ra]),
            "dec": np.concatenate([shared_dec_here, unique_dec]),
            "anomaly_score": np.concatenate([shared_scores, unique_scores]),
        })
        catalogs[survey] = (df, "synthetic")

    return catalogs, n_shared


# ═══════════════════════════════════════════════════════
# GPU-Accelerated Cross-Matching
# ═══════════════════════════════════════════════════════

def angular_separation_deg(ra1, dec1, ra2, dec2):
    """Vectorized angular separation in degrees using Vincenty formula."""
    ra1_r, dec1_r = np.radians(ra1), np.radians(dec1)
    ra2_r, dec2_r = np.radians(ra2), np.radians(dec2)
    dra = ra2_r - ra1_r

    num = np.sqrt(
        (np.cos(dec2_r) * np.sin(dra)) ** 2 +
        (np.cos(dec1_r) * np.sin(dec2_r) - np.sin(dec1_r) * np.cos(dec2_r) * np.cos(dra)) ** 2
    )
    den = (np.sin(dec1_r) * np.sin(dec2_r) +
           np.cos(dec1_r) * np.cos(dec2_r) * np.cos(dra))
    return np.degrees(np.arctan2(num, den))


def gpu_cross_match(ra1, dec1, ra2, dec2, radius_arcsec, device, batch_size=2048):
    """GPU-accelerated cross-match using PyTorch batched distance computation."""
    radius_deg = radius_arcsec / 3600.0
    n1, n2 = len(ra1), len(ra2)

    # Convert to unit vectors on sphere (faster than trig per pair)
    ra1_r, dec1_r = np.radians(ra1), np.radians(dec1)
    ra2_r, dec2_r = np.radians(ra2), np.radians(dec2)

    x1 = np.cos(dec1_r) * np.cos(ra1_r)
    y1 = np.cos(dec1_r) * np.sin(ra1_r)
    z1 = np.sin(dec1_r)

    x2 = np.cos(dec2_r) * np.cos(ra2_r)
    y2 = np.cos(dec2_r) * np.sin(ra2_r)
    z2 = np.sin(dec2_r)

    vec1 = torch.tensor(np.stack([x1, y1, z1], axis=1), dtype=torch.float32, device=device)
    vec2 = torch.tensor(np.stack([x2, y2, z2], axis=1), dtype=torch.float32, device=device)

    cos_threshold = np.cos(np.radians(radius_deg))

    matches_i = []
    matches_j = []
    matches_sep = []

    # Process in batches to avoid OOM
    dataset = TensorDataset(vec1, torch.arange(n1, device=device))
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False,
                        num_workers=0, pin_memory=False)

    for batch_vecs, batch_idx in loader:
        # Dot product = cos(angular separation)
        cos_sep = batch_vecs @ vec2.T  # (batch, n2)
        # Find matches
        match_mask = cos_sep >= cos_threshold
        bi, bj = torch.where(match_mask)
        if len(bi) > 0:
            orig_i = batch_idx[bi].cpu().numpy()
            orig_j = bj.cpu().numpy()
            seps = np.degrees(np.arccos(np.clip(cos_sep[bi, bj].cpu().numpy(), -1, 1))) * 3600
            matches_i.extend(orig_i.tolist())
            matches_j.extend(orig_j.tolist())
            matches_sep.extend(seps.tolist())

    return np.array(matches_i), np.array(matches_j), np.array(matches_sep)


def cpu_cross_match(ra1, dec1, ra2, dec2, radius_arcsec, max_per_catalog=50000):
    """CPU fallback cross-match using KD-tree."""
    from scipy.spatial import cKDTree

    radius_deg = radius_arcsec / 3600.0

    # Subsample if needed
    if len(ra1) > max_per_catalog:
        idx1 = np.random.choice(len(ra1), max_per_catalog, replace=False)
        ra1, dec1 = ra1[idx1], dec1[idx1]
    else:
        idx1 = np.arange(len(ra1))

    if len(ra2) > max_per_catalog:
        idx2 = np.random.choice(len(ra2), max_per_catalog, replace=False)
        ra2, dec2 = ra2[idx2], dec2[idx2]
    else:
        idx2 = np.arange(len(ra2))

    # Convert to Cartesian
    ra1_r, dec1_r = np.radians(ra1), np.radians(dec1)
    ra2_r, dec2_r = np.radians(ra2), np.radians(dec2)
    xyz1 = np.stack([np.cos(dec1_r)*np.cos(ra1_r), np.cos(dec1_r)*np.sin(ra1_r), np.sin(dec1_r)], axis=1)
    xyz2 = np.stack([np.cos(dec2_r)*np.cos(ra2_r), np.cos(dec2_r)*np.sin(ra2_r), np.sin(dec2_r)], axis=1)

    tree = cKDTree(xyz2)
    chord_dist = 2 * np.sin(np.radians(radius_deg) / 2)
    results = tree.query_ball_point(xyz1, chord_dist)

    matches_i, matches_j, matches_sep = [], [], []
    for i, js in enumerate(results):
        for j in js:
            sep = angular_separation_deg(ra1[i], dec1[i], ra2[j], dec2[j]) * 3600
            matches_i.append(int(idx1[i]))
            matches_j.append(int(idx2[j]))
            matches_sep.append(float(sep))

    return np.array(matches_i), np.array(matches_j), np.array(matches_sep)


# ═══════════════════════════════════════════════════════
# Expected Random Matches
# ═══════════════════════════════════════════════════════

def expected_random_matches(n1, n2, radius_arcsec, area_sq_deg=10000):
    """Compute expected number of random positional matches."""
    area_sq_arcsec = area_sq_deg * 3600 ** 2
    pi_r_sq = np.pi * radius_arcsec ** 2
    density1 = n1 / area_sq_arcsec
    density2 = n2 / area_sq_arcsec
    n_expected = n1 * density2 * pi_r_sq
    return float(n_expected)


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("MULTI-MESSENGER ANOMALY STACK")
    print("Objects Anomalous in 2+ Independent Surveys")
    print("=" * 70)
    t_start = time.time()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n  Device: {device}")
    if device.type == "cuda":
        print(f"  GPU: {torch.cuda.get_device_name(0)}")

    # Load all survey catalogs
    print("\n[1/5] Loading survey anomaly catalogs...")
    catalogs = {}
    data_source = "real"

    for survey, config in SURVEY_CONFIG.items():
        df, src = load_survey_catalog(survey, config)
        if df is not None:
            catalogs[survey] = (df, src)

    if len(catalogs) < 2:
        print("  Fewer than 2 surveys loaded — generating synthetic catalogs")
        catalogs, n_planted = generate_synthetic_catalogs(n_shared=500)
        data_source = "synthetic"
    else:
        n_planted = None

    print(f"\n  Loaded {len(catalogs)} surveys:")
    for survey, (df, src) in catalogs.items():
        print(f"    {survey}: {len(df)} anomalies  [{src}]")

    # Pairwise cross-matching
    print("\n[2/5] Pairwise cross-matching...")
    survey_names = sorted(catalogs.keys())
    n_surveys = len(survey_names)

    # Track which objects match which surveys
    # Key: (survey, index) -> set of (other_survey, other_index, separation)
    match_graph = defaultdict(set)
    pair_results = {}

    for i in range(n_surveys):
        for j in range(i + 1, n_surveys):
            s1, s2 = survey_names[i], survey_names[j]
            df1, _ = catalogs[s1]
            df2, _ = catalogs[s2]

            # Determine match radius
            band1 = SURVEY_CONFIG.get(s1, {}).get("band", "optical")
            band2 = SURVEY_CONFIG.get(s2, {}).get("band", "optical")
            if "xray" in [band1, band2]:
                radius = XRAY_MATCH_RADIUS_ARCSEC
            else:
                radius = MATCH_RADIUS_ARCSEC

            ra1, dec1 = df1["ra"].values, df1["dec"].values
            ra2, dec2 = df2["ra"].values, df2["dec"].values

            print(f"    {s1} x {s2} (r={radius}\"): ", end="", flush=True)
            t_match = time.time()

            if device.type == "cuda" and len(ra1) * len(ra2) < 5e9:
                mi, mj, ms = gpu_cross_match(ra1, dec1, ra2, dec2, radius, device)
            else:
                mi, mj, ms = cpu_cross_match(ra1, dec1, ra2, dec2, radius)

            n_matches = len(mi)
            n_expected = expected_random_matches(len(ra1), len(ra2), radius)
            excess = n_matches / max(n_expected, 0.01)
            match_time = time.time() - t_match

            print(f"{n_matches} matches (expected random: {n_expected:.1f}, "
                  f"excess: {excess:.1f}x) [{match_time:.1f}s]")

            pair_results[f"{s1}_x_{s2}"] = {
                "survey_1": s1,
                "survey_2": s2,
                "n_1": int(len(ra1)),
                "n_2": int(len(ra2)),
                "match_radius_arcsec": float(radius),
                "n_matches": int(n_matches),
                "n_expected_random": float(n_expected),
                "excess_factor": float(excess),
                "mean_separation_arcsec": float(ms.mean()) if len(ms) > 0 else 0,
            }

            # Record in match graph
            for k in range(n_matches):
                match_graph[(s1, int(mi[k]))].add((s2, int(mj[k]), float(ms[k])))
                match_graph[(s2, int(mj[k]))].add((s1, int(mi[k]), float(ms[k])))

    # Build multi-survey object list
    print("\n[3/5] Identifying multi-survey detections...")

    # Group matches by unique sky position
    # Use union-find to merge objects that match across surveys
    parent = {}

    def find(x):
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for (s1, i1), matches in match_graph.items():
        for (s2, i2, sep) in matches:
            union((s1, i1), (s2, i2))

    # Group by root
    groups = defaultdict(list)
    for key in match_graph:
        root = find(key)
        groups[root].append(key)

    # Also add isolated objects
    for survey, (df, _) in catalogs.items():
        for idx in range(len(df)):
            key = (survey, idx)
            if key not in parent:
                groups[key].append(key)

    # Filter to multi-survey objects
    multi_survey = []
    for root, members in groups.items():
        surveys_involved = set(m[0] for m in members)
        if len(surveys_involved) >= 2:
            # Compute combined score
            combined_score = 0
            positions = []
            details = []
            for (s, idx) in members:
                df, _ = catalogs[s]
                if idx < len(df):
                    row = df.iloc[idx]
                    combined_score += row["anomaly_score"]
                    positions.append((row["ra"], row["dec"]))
                    details.append({
                        "survey": s,
                        "index": int(idx),
                        "ra": float(row["ra"]),
                        "dec": float(row["dec"]),
                        "score": float(row["anomaly_score"]),
                    })

            if positions:
                mean_ra = np.mean([p[0] for p in positions])
                mean_dec = np.mean([p[1] for p in positions])
                multi_survey.append({
                    "n_surveys": len(surveys_involved),
                    "surveys": sorted(surveys_involved),
                    "combined_score": float(combined_score),
                    "rank_score": float(len(surveys_involved) * combined_score),
                    "mean_ra": float(mean_ra),
                    "mean_dec": float(mean_dec),
                    "detections": details,
                })

    # Sort by rank score
    multi_survey.sort(key=lambda x: x["rank_score"], reverse=True)

    print(f"  Found {len(multi_survey)} multi-survey objects:")
    by_n = defaultdict(int)
    for obj in multi_survey:
        by_n[obj["n_surveys"]] += 1
    for n, count in sorted(by_n.items()):
        print(f"    {n} surveys: {count} objects")

    # Top 50
    print("\n[4/5] Top multi-survey detections:")
    top_50 = multi_survey[:50]
    for i, obj in enumerate(top_50[:15]):
        surveys_str = "+".join(obj["surveys"])
        print(f"    #{i+1:2d}: {obj['n_surveys']} surveys ({surveys_str})  "
              f"score={obj['rank_score']:.1f}  "
              f"RA={obj['mean_ra']:.4f}  Dec={obj['mean_dec']:.4f}")

    # Assign IDs
    for i, obj in enumerate(top_50):
        obj["multi_messenger_id"] = f"MM_{i+1:04d}"

    # Significance assessment
    print("\n[5/5] Significance assessment...")
    total_real = len(multi_survey)

    # Monte Carlo: shuffle RA/Dec in each catalog and re-match
    n_mc = 10
    random_counts = []
    print(f"  Running {n_mc} Monte Carlo randomizations...")
    for mc in range(n_mc):
        mc_graph = defaultdict(set)
        for i in range(n_surveys):
            for j in range(i + 1, n_surveys):
                s1, s2 = survey_names[i], survey_names[j]
                df1, _ = catalogs[s1]
                df2, _ = catalogs[s2]

                # Shuffle catalog 2
                ra2_shuf = np.random.permutation(df2["ra"].values)
                dec2_shuf = np.random.permutation(df2["dec"].values)

                band1 = SURVEY_CONFIG.get(s1, {}).get("band", "optical")
                band2 = SURVEY_CONFIG.get(s2, {}).get("band", "optical")
                radius = XRAY_MATCH_RADIUS_ARCSEC if "xray" in [band1, band2] else MATCH_RADIUS_ARCSEC

                mi, mj, ms = cpu_cross_match(
                    df1["ra"].values[:5000], df1["dec"].values[:5000],
                    ra2_shuf[:5000], dec2_shuf[:5000], radius
                )
                for k in range(len(mi)):
                    mc_graph[(s1, int(mi[k]))].add(s2)
                    mc_graph[(s2, int(mj[k]))].add(s1)

        # Count multi-survey in randomized
        n_multi_random = sum(1 for v in mc_graph.values() if len(v) >= 1)
        random_counts.append(n_multi_random)
        print(f"    MC {mc+1}: {n_multi_random} random multi-survey matches")

    mean_random = np.mean(random_counts)
    std_random = np.std(random_counts) if len(random_counts) > 1 else 1.0
    significance = (total_real - mean_random) / max(std_random, 1.0)

    print(f"\n  Real multi-survey objects: {total_real}")
    print(f"  Random expectation: {mean_random:.1f} +/- {std_random:.1f}")
    print(f"  Excess significance: {significance:.1f} sigma")

    # Save results
    total_time = time.time() - t_start

    summary = {
        "experiment": "multi_messenger_stack",
        "description": "Objects anomalous in 2+ independent surveys",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data_source": data_source,
        "n_surveys_loaded": len(catalogs),
        "surveys": {
            s: {"n_anomalies": int(len(df)), "source": src}
            for s, (df, src) in catalogs.items()
        },
        "cross_match_config": {
            "default_radius_arcsec": MATCH_RADIUS_ARCSEC,
            "xray_radius_arcsec": XRAY_MATCH_RADIUS_ARCSEC,
        },
        "pairwise_results": pair_results,
        "multi_survey_summary": {
            "total_multi_survey": int(total_real),
            "by_n_surveys": {str(k): int(v) for k, v in sorted(by_n.items())},
        },
        "significance": {
            "n_real": int(total_real),
            "mean_random": float(mean_random),
            "std_random": float(std_random),
            "sigma": float(significance),
            "n_mc_trials": n_mc,
        },
        "top_50_multi_survey": top_50,
        "n_planted_shared": n_planted,
        "total_time_s": float(total_time),
        "device": str(device),
    }

    with open(OUTPUT_DIR / "multi_messenger_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    # Save full multi-survey list
    if multi_survey:
        flat_rows = []
        for obj in multi_survey:
            flat_rows.append({
                "multi_messenger_id": obj.get("multi_messenger_id", ""),
                "n_surveys": obj["n_surveys"],
                "surveys": "|".join(obj["surveys"]),
                "combined_score": obj["combined_score"],
                "rank_score": obj["rank_score"],
                "mean_ra": obj["mean_ra"],
                "mean_dec": obj["mean_dec"],
            })
        pd.DataFrame(flat_rows).to_csv(OUTPUT_DIR / "multi_survey_objects.csv", index=False)

    # Save pairwise matrix
    matrix = np.zeros((n_surveys, n_surveys), dtype=int)
    for key, val in pair_results.items():
        i = survey_names.index(val["survey_1"])
        j = survey_names.index(val["survey_2"])
        matrix[i, j] = val["n_matches"]
        matrix[j, i] = val["n_matches"]
    matrix_df = pd.DataFrame(matrix, index=survey_names, columns=survey_names)
    matrix_df.to_csv(OUTPUT_DIR / "cross_match_matrix.csv")

    print(f"\n  Saved to: {OUTPUT_DIR}")
    print(f"  Total time: {total_time:.1f}s")

    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
