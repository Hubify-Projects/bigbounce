"""
planck_act_cmb_crossmatch.py
-----------------------------
Cross-match Planck CMB and ACT DR6 anomalous patches to find sky regions
flagged as anomalous by BOTH independent instruments.

Steps:
  1. Load both anomaly catalogs
  2. Take top 200 Planck patches; cross-match against top 200 ACT patches
     within 2-degree angular radius
  3. Correlation analysis of matched anomaly scores
  4. Compare matched regions to known CMB anomalies
     (Cold Spot RA~209 DEC~-57; hemispherical power asymmetry axis)
  5. Angular power spectrum of anomaly positions
  6. Save full results to projects/cross_survey/results/planck_act_crossmatch.json
"""

import json
import os
import sys
import warnings
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from astropy.coordinates import SkyCoord, match_coordinates_sky
import astropy.units as u

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLANCK_PARQUET = os.path.join(REPO_ROOT, "pipelines/h200_results/planck_cmb/planck_cmb_anomalies.parquet")
PLANCK_SUMMARY = os.path.join(REPO_ROOT, "pipelines/h200_results/planck_cmb/planck_cmb_summary.json")
ACT_PARQUET    = os.path.join(REPO_ROOT, "pipelines/h200_results/act_dr6/act_anomalies.parquet")
ACT_SUMMARY    = os.path.join(REPO_ROOT, "pipelines/h200_results/act_dr6/act_summary.json")
OUT_JSON       = os.path.join(REPO_ROOT, "projects/cross_survey/results/planck_act_crossmatch.json")

# ---------------------------------------------------------------------------
# Known CMB anomalies for reference comparison
# ---------------------------------------------------------------------------
KNOWN_ANOMALIES = [
    {
        "name": "CMB Cold Spot",
        "ra": 209.0,
        "dec": -57.0,
        "radius_deg": 10.0,
        "description": "Supervoid candidate, Eridanus Supervoid; ~3-4 sigma below average temperature",
    },
    {
        "name": "Hemispherical Power Asymmetry Axis (preferred)",
        "ra": 221.0,
        "dec": -20.0,
        "radius_deg": 30.0,
        "description": "Low-multipole alignment dipole axis; WMAP/Planck confirmed",
    },
    {
        "name": "Axis of Evil / Quadrupole-Octupole Alignment",
        "ra": 240.0,
        "dec": -60.0,
        "radius_deg": 20.0,
        "description": "Quadrupole/octupole anomalous alignment axis",
    },
    {
        "name": "CMB Dipole Direction",
        "ra": 168.0,
        "dec": -7.0,
        "radius_deg": 10.0,
        "description": "Solar motion CMB dipole direction (kinematic); useful sanity check",
    },
]

# ---------------------------------------------------------------------------
# Helper: angular separation (haversine, vectorised)
# ---------------------------------------------------------------------------
def angular_sep_deg(ra1, dec1, ra2, dec2):
    """Return angular separation in degrees using haversine formula."""
    ra1, dec1 = np.radians(ra1), np.radians(dec1)
    ra2, dec2 = np.radians(ra2), np.radians(dec2)
    dra  = ra2 - ra1
    ddec = dec2 - dec1
    a = np.sin(ddec / 2)**2 + np.cos(dec1) * np.cos(dec2) * np.sin(dra / 2)**2
    return np.degrees(2 * np.arcsin(np.sqrt(np.clip(a, 0, 1))))


# ---------------------------------------------------------------------------
# Step 1: Load catalogs
# ---------------------------------------------------------------------------
print("Loading catalogs...")
planck_all = pd.read_parquet(PLANCK_PARQUET)
act_all    = pd.read_parquet(ACT_PARQUET)

with open(PLANCK_SUMMARY) as f:
    planck_meta = json.load(f)
with open(ACT_SUMMARY) as f:
    act_meta = json.load(f)

print(f"  Planck: {len(planck_all):,} total patches")
print(f"  ACT:    {len(act_all):,} total patches")

# ---------------------------------------------------------------------------
# Step 2: Select top 200 anomalies from each catalog
# ---------------------------------------------------------------------------
N_TOP = 200
planck_top = planck_all.nlargest(N_TOP, "anomaly_score").reset_index(drop=True)
act_top    = act_all.nlargest(N_TOP, "anomaly_score").reset_index(drop=True)

# Normalise scores to [0, 1] for fair comparison later
planck_top["score_norm"] = (
    (planck_top["anomaly_score"] - planck_all["anomaly_score"].min()) /
    (planck_all["anomaly_score"].max() - planck_all["anomaly_score"].min())
)
act_top["score_norm"] = (
    (act_top["anomaly_score"] - act_all["anomaly_score"].min()) /
    (act_all["anomaly_score"].max() - act_all["anomaly_score"].min())
)

print(f"\nTop {N_TOP} Planck score range: {planck_top['anomaly_score'].min():.4f} - {planck_top['anomaly_score'].max():.4f}")
print(f"Top {N_TOP} ACT   score range:  {act_top['anomaly_score'].min():.4e} - {act_top['anomaly_score'].max():.4e}")

# ---------------------------------------------------------------------------
# Step 3: Cross-match within 2 degrees using astropy SkyCoord
# ---------------------------------------------------------------------------
MATCH_RADIUS_DEG = 2.0
print(f"\nCross-matching within {MATCH_RADIUS_DEG} degrees...")

planck_coords = SkyCoord(ra=planck_top["ra"].values * u.deg,
                         dec=planck_top["dec"].values * u.deg)
act_coords    = SkyCoord(ra=act_top["ra"].values * u.deg,
                         dec=act_top["dec"].values * u.deg)

# For each Planck patch, find nearest ACT patch
idx_act, sep2d, _ = match_coordinates_sky(planck_coords, act_coords)
matched_mask = sep2d.deg <= MATCH_RADIUS_DEG

n_matches = matched_mask.sum()
print(f"  Matches found: {n_matches}")

# Build matched DataFrame
matched_rows = []
for i, (matched, act_idx, sep) in enumerate(zip(matched_mask, idx_act, sep2d.deg)):
    if matched:
        p_row = planck_top.iloc[i]
        a_row = act_top.iloc[act_idx]
        matched_rows.append({
            "planck_rank":        int(i + 1),
            "act_rank":           int(act_idx + 1),
            "ra_planck":          float(p_row["ra"]),
            "dec_planck":         float(p_row["dec"]),
            "ra_act":             float(a_row["ra"]),
            "dec_act":            float(a_row["dec"]),
            "sep_deg":            float(sep),
            "planck_score":       float(p_row["anomaly_score"]),
            "planck_score_norm":  float(p_row["score_norm"]),
            "act_score":          float(a_row["anomaly_score"]),
            "act_score_norm":     float(a_row["score_norm"]),
            # Mean sky position of the matched pair
            "ra_mean":            float(np.mean([p_row["ra"], a_row["ra"]])),
            "dec_mean":           float(np.mean([p_row["dec"], a_row["dec"]])),
        })

matched_df = pd.DataFrame(matched_rows)

# ---------------------------------------------------------------------------
# Step 4: Correlation analysis of anomaly scores in matched regions
# ---------------------------------------------------------------------------
print("\nComputing score correlations...")
correlation_results = {}
if n_matches >= 3:
    pscores = matched_df["planck_score_norm"].values
    ascores = matched_df["act_score_norm"].values

    pearson_r, pearson_p     = pearsonr(pscores, ascores)
    spearman_r, spearman_p   = spearmanr(pscores, ascores)

    correlation_results = {
        "n_matched": int(n_matches),
        "pearson_r": float(pearson_r),
        "pearson_p": float(pearson_p),
        "spearman_r": float(spearman_r),
        "spearman_p": float(spearman_p),
        "interpretation": (
            "Strong positive correlation" if pearson_r > 0.5 else
            "Weak positive correlation"  if pearson_r > 0.2 else
            "No clear correlation"       if pearson_r >= -0.2 else
            "Anti-correlation"
        ) + (
            " (statistically significant, p<0.05)"  if pearson_p < 0.05 else
            " (not statistically significant, p>0.05)"
        ),
    }
    print(f"  Pearson r={pearson_r:.3f} (p={pearson_p:.3f}), "
          f"Spearman r={spearman_r:.3f} (p={spearman_p:.3f})")
else:
    correlation_results = {
        "n_matched": int(n_matches),
        "note": "Too few matches for reliable correlation (<3)",
    }
    print("  Too few matches for correlation analysis.")

# ---------------------------------------------------------------------------
# Step 5: Compare matched regions to known CMB anomalies
# ---------------------------------------------------------------------------
print("\nChecking proximity to known CMB anomalies...")
known_anomaly_hits = []

for anom in KNOWN_ANOMALIES:
    # Check each matched patch against this known anomaly
    hits_in_matched = []
    for _, row in matched_df.iterrows():
        sep = angular_sep_deg(row["ra_mean"], row["dec_mean"],
                              anom["ra"], anom["dec"])
        if sep <= anom["radius_deg"]:
            hits_in_matched.append({
                "planck_rank":  int(row["planck_rank"]),
                "act_rank":     int(row["act_rank"]),
                "sep_deg":      float(sep),
                "ra_mean":      float(row["ra_mean"]),
                "dec_mean":     float(row["dec_mean"]),
                "planck_score": float(row["planck_score"]),
                "act_score":    float(row["act_score"]),
            })

    # Also check all top-200 Planck patches individually for Cold Spot coverage
    planck_seps = angular_sep_deg(
        planck_top["ra"].values, planck_top["dec"].values,
        anom["ra"], anom["dec"]
    )
    act_seps = angular_sep_deg(
        act_top["ra"].values, act_top["dec"].values,
        anom["ra"], anom["dec"]
    )
    n_planck_near = int((planck_seps <= anom["radius_deg"]).sum())
    n_act_near    = int((act_seps    <= anom["radius_deg"]).sum())

    known_anomaly_hits.append({
        "known_anomaly":         anom["name"],
        "description":           anom["description"],
        "reference_ra":          anom["ra"],
        "reference_dec":         anom["dec"],
        "search_radius_deg":     anom["radius_deg"],
        "n_planck_top200_nearby": n_planck_near,
        "n_act_top200_nearby":    n_act_near,
        "n_crossmatched_hits":   len(hits_in_matched),
        "crossmatched_hits":     hits_in_matched,
        "both_instruments_flag": len(hits_in_matched) > 0,
    })

    print(f"  {anom['name']}: Planck={n_planck_near}, ACT={n_act_near}, "
          f"cross-match hits={len(hits_in_matched)}")

# ---------------------------------------------------------------------------
# Step 6: Angular clustering / power spectrum of anomaly positions
# ---------------------------------------------------------------------------
# We compute the two-point angular correlation function for matched anomalies
# and compare to what random positions would give.  We also check whether the
# spatial distribution is structured vs uniform by computing the variance
# in HEALPix-pixel occupation (quick proxy for C_l power).

print("\nAnalysing spatial distribution of anomalies...")

def _all_pair_seps_deg(ras, decs):
    """
    Vectorised all-pairs angular separation using numpy broadcasting (haversine).
    Returns upper-triangle separations as a flat array.
    """
    ra  = np.radians(ras)
    dec = np.radians(decs)
    # Broadcast: shape (n, 1) vs (1, n)
    dra  = ra[:, None]  - ra[None, :]
    ddec = dec[:, None] - dec[None, :]
    a = (np.sin(ddec / 2)**2
         + np.cos(dec[:, None]) * np.cos(dec[None, :]) * np.sin(dra / 2)**2)
    seps = np.degrees(2 * np.arcsin(np.sqrt(np.clip(a, 0, 1))))
    # Upper triangle only (no self-pairs)
    n = len(ras)
    idx = np.triu_indices(n, k=1)
    return seps[idx]


def two_point_angular_corr(ras, decs, bins_deg, n_random=500, seed=42):
    """
    Simple DD/RR two-point angular correlation function (vectorised).
    Returns bin centres and w(theta) = DD/RR - 1 per bin.
    n_random=500 is sufficient for 200-point catalogs.
    """
    rng = np.random.default_rng(seed)
    n_data = len(ras)

    seps_dd = _all_pair_seps_deg(np.array(ras), np.array(decs))

    ra_r  = rng.uniform(0, 360, n_random)
    dec_r = np.degrees(np.arcsin(rng.uniform(-1, 1, n_random)))
    seps_rr = _all_pair_seps_deg(ra_r, dec_r)

    edges = np.array([0] + list(bins_deg))
    dd_counts, _ = np.histogram(seps_dd, bins=edges)
    rr_counts, _ = np.histogram(seps_rr, bins=edges)

    norm = (n_random * (n_random - 1)) / (n_data * (n_data - 1))
    with np.errstate(divide="ignore", invalid="ignore"):
        w = np.where(rr_counts > 0, norm * dd_counts / rr_counts - 1, np.nan)

    centres = 0.5 * (edges[:-1] + edges[1:])
    return centres.tolist(), w.tolist(), int(len(seps_dd)), int(len(seps_rr))


# Bins: 0-5, 5-15, 15-30, 30-60, 60-90, 90-120, 120-180 degrees
bins_deg = [5, 15, 30, 60, 90, 120, 180]

spatial_results = {}

# Distribution of all top-200 Planck
p_centres, p_w, p_npairs, _ = two_point_angular_corr(
    planck_top["ra"].values, planck_top["dec"].values, bins_deg, n_random=2000)
# Distribution of all top-200 ACT
a_centres, a_w, a_npairs, _ = two_point_angular_corr(
    act_top["ra"].values, act_top["dec"].values, bins_deg, n_random=2000)

spatial_results["planck_top200"] = {
    "n_patches": int(len(planck_top)),
    "n_pairs": p_npairs,
    "theta_bins_deg": p_centres,
    "w_theta": [round(v, 4) if not np.isnan(v) else None for v in p_w],
    "interpretation": (
        "Clustered at small angles (w>0 at <5 deg)"
        if (len(p_w) > 0 and p_w[0] is not None and not np.isnan(p_w[0]) and p_w[0] > 0.5)
        else "Consistent with random or anti-clustered distribution"
    ),
}
spatial_results["act_top200"] = {
    "n_patches": int(len(act_top)),
    "n_pairs": a_npairs,
    "theta_bins_deg": a_centres,
    "w_theta": [round(v, 4) if not np.isnan(v) else None for v in a_w],
    "interpretation": (
        "Clustered at small angles (w>0 at <5 deg)"
        if (len(a_w) > 0 and a_w[0] is not None and not np.isnan(a_w[0]) and a_w[0] > 0.5)
        else "Consistent with random or anti-clustered distribution"
    ),
}

# For matched patches (if enough)
if n_matches >= 5:
    m_centres, m_w, m_npairs, _ = two_point_angular_corr(
        matched_df["ra_mean"].values, matched_df["dec_mean"].values,
        bins_deg, n_random=2000)
    spatial_results["matched_pairs"] = {
        "n_patches": int(n_matches),
        "n_pairs": m_npairs,
        "theta_bins_deg": m_centres,
        "w_theta": [round(v, 4) if not np.isnan(v) else None for v in m_w],
        "interpretation": (
            "Matched anomalies cluster at small angles — spatially coherent"
            if (len(m_w) > 0 and m_w[0] is not None and not np.isnan(m_w[0]) and m_w[0] > 0.5)
            else "Matched anomalies consistent with random angular distribution"
        ),
    }
else:
    spatial_results["matched_pairs"] = {
        "n_patches": int(n_matches),
        "note": "Too few matched pairs (<5) for two-point correlation",
    }

print(f"  Planck top-200 w(theta) at <5 deg: {p_w[0]:.4f}" if p_w and p_w[0] is not None else "  Planck: no data in bin")
print(f"  ACT top-200   w(theta) at <5 deg: {a_w[0]:.4f}"  if a_w and a_w[0] is not None else "  ACT:    no data in bin")

# ---------------------------------------------------------------------------
# Step 7: Assess cosmological significance
# ---------------------------------------------------------------------------
print("\nAssessing cosmological significance...")

# Expected number of chance coincidences between two random uniform catalogs
# of N points each on the full sphere, within radius r:
# E[matches] = N^2 * (1 - cos(r)) / 2  (fraction of sphere covered by cap)
FULL_SPHERE_STER = 4 * np.pi
cap_fraction = (1 - np.cos(np.radians(MATCH_RADIUS_DEG))) / 2
expected_random = N_TOP * N_TOP * cap_fraction
significance_note = (
    f"Expected random coincidences (N={N_TOP}x{N_TOP}, r={MATCH_RADIUS_DEG} deg): "
    f"{expected_random:.2f}. "
    f"Observed: {n_matches}. "
)
if n_matches > expected_random * 2:
    significance_note += (
        f"Observed excess: {n_matches / max(expected_random, 0.01):.1f}x expected — "
        "suggests genuine spatial overlap beyond chance."
    )
elif n_matches > expected_random:
    significance_note += (
        f"Modest excess: {n_matches / max(expected_random, 0.01):.1f}x expected."
    )
else:
    significance_note += "Not significantly above chance overlap."

print(f"  {significance_note}")

# Cold Spot specific check
cold_spot_matched = [h for anom_hit in known_anomaly_hits
                     if "Cold Spot" in anom_hit["known_anomaly"]
                     for h in anom_hit["crossmatched_hits"]]
cold_spot_flag = len(cold_spot_matched) > 0

# Hemispherical asymmetry check
asym_matched = [h for anom_hit in known_anomaly_hits
                if "Hemispherical" in anom_hit["known_anomaly"]
                for h in anom_hit["crossmatched_hits"]]

# ---------------------------------------------------------------------------
# Step 8: Compile full results
# ---------------------------------------------------------------------------
print("\nCompiling results...")

# Score distribution statistics
def score_stats(series):
    return {
        "min":    float(series.min()),
        "max":    float(series.max()),
        "mean":   float(series.mean()),
        "median": float(series.median()),
        "std":    float(series.std()),
    }

results = {
    "metadata": {
        "script":        "planck_act_cmb_crossmatch.py",
        "date":          "2026-04-02",
        "planck_n_total": int(len(planck_all)),
        "act_n_total":    int(len(act_all)),
        "n_top_selected": N_TOP,
        "match_radius_deg": MATCH_RADIUS_DEG,
        "planck_summary_timestamp": planck_meta.get("timestamp", ""),
        "act_summary_timestamp":    act_meta.get("timestamp", ""),
    },
    "catalog_stats": {
        "planck_top200_scores": score_stats(planck_top["anomaly_score"]),
        "act_top200_scores":    score_stats(act_top["anomaly_score"]),
        "planck_top200_score_threshold": float(planck_top["anomaly_score"].min()),
        "act_top200_score_threshold":    float(act_top["anomaly_score"].min()),
    },
    "crossmatch": {
        "n_matches":          int(n_matches),
        "match_radius_deg":   MATCH_RADIUS_DEG,
        "expected_random":    float(expected_random),
        "significance_note":  significance_note,
        "matches": [
            {k: (round(v, 6) if isinstance(v, float) else v)
             for k, v in row.items()}
            for row in matched_rows
        ],
    },
    "score_correlation": correlation_results,
    "known_anomaly_comparison": known_anomaly_hits,
    "cold_spot_flagged_by_both": cold_spot_flag,
    "cold_spot_matched_patches": cold_spot_matched,
    "hemispherical_asymmetry_flagged_by_both": len(asym_matched) > 0,
    "hemispherical_asymmetry_matched_patches": asym_matched,
    "spatial_distribution": spatial_results,
    "cosmological_interpretation": {
        "genuine_overlap_likely": (
            n_matches > expected_random * 1.5 or
            correlation_results.get("pearson_r", 0) > 0.3
        ),
        "cold_spot_confirmed_both_instruments": cold_spot_flag,
        "hemispherical_asymmetry_confirmed": len(asym_matched) > 0,
        "summary": (
            f"{n_matches} regions flagged as anomalous by both Planck and ACT "
            f"(within {MATCH_RADIUS_DEG} deg). "
            + significance_note +
            (f" Pearson r={correlation_results.get('pearson_r', float('nan')):.3f} "
             f"between normalised scores in matched regions."
             if "pearson_r" in correlation_results else "") +
            (" Cold Spot region confirmed by both instruments."
             if cold_spot_flag else " Cold Spot NOT confirmed by dual cross-match.") +
            (" Hemispherical asymmetry axis region confirmed."
             if len(asym_matched) > 0 else " Hemispherical asymmetry axis NOT in dual cross-match.")
        ),
    },
}

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
with open(OUT_JSON, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to: {OUT_JSON}")
print("\n=== SUMMARY ===")
print(f"  Cross-matched patches:   {n_matches} / {N_TOP}")
print(f"  Expected by chance:      {expected_random:.2f}")
print(f"  Score correlation (r):   {correlation_results.get('pearson_r', 'N/A')}")
print(f"  Cold Spot hit both:      {cold_spot_flag}")
print(f"  Hemi. asymmetry hit both:{len(asym_matched) > 0}")
if n_matches > 0:
    print("\n  Top matched regions (by Planck rank):")
    for r in sorted(matched_rows, key=lambda x: x["planck_rank"])[:10]:
        print(f"    Planck#{r['planck_rank']:3d}  RA={r['ra_planck']:.2f}  DEC={r['dec_planck']:.2f}  "
              f"sep={r['sep_deg']:.2f}deg  P_score={r['planck_score']:.4f}  A_score={r['act_score']:.2e}")
