#!/usr/bin/env python3
"""
Additional scientific analyses on the chirality catalog.
Runs on the H200 pod with catalog_production.parquet and gz_desi_friendly.parquet.

Analyses:
1. Spiral fraction sky map (healpix NSIDE=32)
2. Morphology-chirality cross-analysis (winding, bars, edge-on)
3. Magnitude/size dependence (brightness/size bias test)
4. Catalog purity check (sample URLs for visual inspection)
5. Statistical power analysis (minimum detectable dipole/hemisphere asymmetry)

Houston Golden, 2026-03-28
"""

import json
import time
import numpy as np
import pandas as pd
import healpy as hp
from scipy import stats

t0 = time.time()

OUT_PATH = "/workspace/chirality/additional_analysis.json"
results = {}

# ─────────────────────────────────────────────────────────────────────────────
# Load catalogs
# ─────────────────────────────────────────────────────────────────────────────
print("Loading catalogs...")
cat = pd.read_parquet("/workspace/chirality/catalog_production.parquet")
gz = pd.read_parquet("/workspace/chirality/gz_desi_friendly.parquet")
print(f"  catalog_production: {len(cat):,} rows, {cat.shape[1]} cols")
print(f"  gz_desi_friendly:   {len(gz):,} rows, {gz.shape[1]} cols")

# Use equalized labels for all analyses (mitigates reflection bias)
cat["label"] = cat["class_eq"]

N_total = len(cat)
n_cw = (cat["label"] == "CW").sum()
n_ccw = (cat["label"] == "CCW").sum()
n_ns = (cat["label"] == "NOT_SPIRAL").sum()
n_spiral = n_cw + n_ccw

print(f"\n  CW: {n_cw:,}  CCW: {n_ccw:,}  NOT_SPIRAL: {n_ns:,}")
print(f"  Spiral fraction: {n_spiral/N_total:.4f}")

# ═════════════════════════════════════════════════════════════════════════════
# 1. SPIRAL FRACTION SKY MAP
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*72)
print("1. SPIRAL FRACTION SKY MAP (NSIDE=32)")
print("="*72)

NSIDE = 32
NPIX = hp.nside2npix(NSIDE)

# Convert RA/Dec to healpix pixels
theta = np.radians(90.0 - cat["dec"].values)  # co-latitude
phi = np.radians(cat["ra"].values)
pix = hp.ang2pix(NSIDE, theta, phi)

cat["healpix"] = pix
is_spiral = (cat["label"] == "CW") | (cat["label"] == "CCW")

# Count spirals and total per pixel
spiral_counts = np.zeros(NPIX)
total_counts = np.zeros(NPIX)

for p, s in zip(pix, is_spiral):
    total_counts[p] += 1
    if s:
        spiral_counts[p] += 1

# Mask empty pixels
occupied = total_counts > 0
spiral_frac_map = np.full(NPIX, np.nan)
spiral_frac_map[occupied] = spiral_counts[occupied] / total_counts[occupied]

# Statistics over occupied pixels
fracs = spiral_frac_map[occupied]
mean_frac = float(np.mean(fracs))
std_frac = float(np.std(fracs))
median_frac = float(np.median(fracs))
min_frac = float(np.min(fracs))
max_frac = float(np.max(fracs))
n_occupied = int(occupied.sum())

# Check for spatial structure: compute angular power spectrum of spiral fraction
# Fill unoccupied pixels with mean for power spectrum estimation
frac_filled = np.where(occupied, spiral_frac_map, mean_frac)
# Subtract mean to get fluctuation map
delta_frac = frac_filled - mean_frac
cl = hp.anafast(delta_frac, lmax=3*NSIDE - 1)
ell = np.arange(len(cl))

# Dipole (l=1) and quadrupole (l=2) power
dipole_power = cl[1] if len(cl) > 1 else 0.0
quadrupole_power = cl[2] if len(cl) > 2 else 0.0

# Compare to shot noise expectation
# Shot noise for fraction = p(1-p)/N_per_pixel
mean_n_per_pix = total_counts[occupied].mean()
shot_noise_var = mean_frac * (1 - mean_frac) / mean_n_per_pix
# Shot noise Cl ~ 4*pi * shot_noise_var / Npix (white noise)
shot_cl = 4 * np.pi * shot_noise_var / n_occupied

# Top/bottom 10 pixels by spiral fraction (with enough galaxies)
well_sampled = total_counts > 100
if well_sampled.sum() > 0:
    ws_fracs = spiral_frac_map[well_sampled]
    ws_pix = np.where(well_sampled)[0]
    ws_counts = total_counts[well_sampled]
    # Sort by fraction
    sorted_idx = np.argsort(ws_fracs)
    top10_pix = ws_pix[sorted_idx[-10:]]
    bot10_pix = ws_pix[sorted_idx[:10]]
    top10_info = [{"pixel": int(p), "frac": float(spiral_frac_map[p]),
                   "n_gal": int(total_counts[p]),
                   "lon_lat": list(hp.pix2ang(NSIDE, p, lonlat=True))}
                  for p in top10_pix]
    bot10_info = [{"pixel": int(p), "frac": float(spiral_frac_map[p]),
                   "n_gal": int(total_counts[p]),
                   "lon_lat": list(hp.pix2ang(NSIDE, p, lonlat=True))}
                  for p in bot10_pix]
else:
    top10_info = []
    bot10_info = []

# Chi-squared test for uniformity
# Use pixels with > 50 galaxies
good = total_counts > 50
if good.sum() > 10:
    good_idx = np.where(good)[0]
    expected_spiral = mean_frac * total_counts[good_idx]
    observed_spiral = spiral_counts[good_idx]
    chi2_stat = np.sum((observed_spiral - expected_spiral)**2 / expected_spiral)
    chi2_dof = len(good_idx) - 1
    chi2_pval = float(stats.chi2.sf(chi2_stat, chi2_dof))
else:
    chi2_stat = 0
    chi2_dof = 0
    chi2_pval = 1.0

results["spiral_fraction_map"] = {
    "nside": NSIDE,
    "n_occupied_pixels": n_occupied,
    "n_total_pixels": NPIX,
    "mean_spiral_fraction": mean_frac,
    "std_spiral_fraction": std_frac,
    "median_spiral_fraction": median_frac,
    "min_spiral_fraction": min_frac,
    "max_spiral_fraction": max_frac,
    "mean_galaxies_per_pixel": float(mean_n_per_pix),
    "dipole_power_cl1": float(dipole_power),
    "quadrupole_power_cl2": float(quadrupole_power),
    "shot_noise_cl": float(shot_cl),
    "dipole_over_shot_noise": float(dipole_power / shot_cl) if shot_cl > 0 else None,
    "quadrupole_over_shot_noise": float(quadrupole_power / shot_cl) if shot_cl > 0 else None,
    "chi2_uniformity_stat": float(chi2_stat),
    "chi2_uniformity_dof": int(chi2_dof),
    "chi2_uniformity_pval": chi2_pval,
    "top10_highest_spiral_frac": top10_info,
    "top10_lowest_spiral_frac": bot10_info,
}

print(f"  Occupied pixels: {n_occupied}/{NPIX}")
print(f"  Mean spiral fraction: {mean_frac:.4f} +/- {std_frac:.4f}")
print(f"  Range: [{min_frac:.4f}, {max_frac:.4f}]")
print(f"  Mean galaxies/pixel: {mean_n_per_pix:.0f}")
print(f"  Dipole power / shot noise: {dipole_power/shot_cl:.2f}" if shot_cl > 0 else "  Shot noise = 0")
print(f"  Quadrupole power / shot noise: {quadrupole_power/shot_cl:.2f}" if shot_cl > 0 else "")
print(f"  Chi-squared uniformity: chi2={chi2_stat:.1f}, dof={chi2_dof}, p={chi2_pval:.4e}")

# ═════════════════════════════════════════════════════════════════════════════
# 2. MORPHOLOGY-CHIRALITY CROSS-ANALYSIS
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*72)
print("2. MORPHOLOGY-CHIRALITY CROSS-ANALYSIS")
print("="*72)

# Cross-match on dr8_id
print("  Cross-matching catalogs on dr8_id...")
merged = cat.merge(gz, on="dr8_id", how="inner", suffixes=("", "_gz"))
print(f"  Matched: {len(merged):,} / {len(cat):,} ({100*len(merged)/len(cat):.1f}%)")

# Filter to spirals only for winding/bar analyses
spirals = merged[(merged["label"] == "CW") | (merged["label"] == "CCW")].copy()
print(f"  Spirals in cross-match: {len(spirals):,}")

# --- 2a. Winding tightness vs chirality ---
print("\n  --- 2a. Winding tightness vs chirality ---")
# Determine dominant winding class
winding_cols = ["spiral-winding_tight_fraction", "spiral-winding_medium_fraction",
                "spiral-winding_loose_fraction"]
has_winding = spirals[winding_cols].notna().all(axis=1)
sp_w = spirals[has_winding].copy()
print(f"  Spirals with winding data: {len(sp_w):,}")

if len(sp_w) > 0:
    sp_w["winding_class"] = sp_w[winding_cols].idxmax(axis=1).str.replace("spiral-winding_", "").str.replace("_fraction", "")

    winding_results = {}
    for wclass in ["tight", "medium", "loose"]:
        sub = sp_w[sp_w["winding_class"] == wclass]
        n_sub = len(sub)
        n_cw_sub = (sub["label"] == "CW").sum()
        n_ccw_sub = (sub["label"] == "CCW").sum()
        cw_frac = n_cw_sub / n_sub if n_sub > 0 else 0
        # Binomial test for CW/CCW balance
        if n_sub > 0:
            binom_p = float(stats.binom_test(n_cw_sub, n_sub, 0.5)) if hasattr(stats, 'binom_test') else float(stats.binomtest(n_cw_sub, n_sub, 0.5).pvalue)
        else:
            binom_p = 1.0
        winding_results[wclass] = {
            "n_total": int(n_sub),
            "n_cw": int(n_cw_sub),
            "n_ccw": int(n_ccw_sub),
            "cw_fraction": float(cw_frac),
            "cw_excess_sigma": float((n_cw_sub - n_sub/2) / np.sqrt(n_sub/4)) if n_sub > 0 else 0,
            "binomial_pval": binom_p,
        }
        print(f"    {wclass:8s}: N={n_sub:,}  CW={n_cw_sub:,}  CCW={n_ccw_sub:,}  "
              f"CW_frac={cw_frac:.5f}  excess={winding_results[wclass]['cw_excess_sigma']:.2f}σ  p={binom_p:.4e}")

    # Chi-squared test: is CW fraction different across winding classes?
    contingency_wind = np.array([
        [winding_results[w]["n_cw"] for w in ["tight", "medium", "loose"]],
        [winding_results[w]["n_ccw"] for w in ["tight", "medium", "loose"]]
    ])
    chi2_wind, p_wind, dof_wind, _ = stats.chi2_contingency(contingency_wind)
    winding_results["chi2_test"] = {
        "chi2": float(chi2_wind),
        "pval": float(p_wind),
        "dof": int(dof_wind),
    }
    print(f"    Chi-squared (winding vs chirality): chi2={chi2_wind:.2f}, p={p_wind:.4e}, dof={dof_wind}")
else:
    winding_results = {"error": "No winding data available"}

results["morphology_chirality"] = {"winding_vs_chirality": winding_results}

# --- 2b. Bar presence vs chirality ---
print("\n  --- 2b. Bar presence vs chirality ---")
bar_cols = ["bar_strong_fraction", "bar_weak_fraction", "bar_no_fraction"]
has_bar_data = spirals[bar_cols].notna().all(axis=1)
sp_b = spirals[has_bar_data].copy()
print(f"  Spirals with bar data: {len(sp_b):,}")

if len(sp_b) > 0:
    # Classify: barred (strong or weak dominant) vs unbarred
    sp_b["has_bar"] = (sp_b["bar_strong_fraction"] + sp_b["bar_weak_fraction"]) > sp_b["bar_no_fraction"]

    bar_results = {}
    for bar_label, bar_val in [("barred", True), ("unbarred", False)]:
        sub = sp_b[sp_b["has_bar"] == bar_val]
        n_sub = len(sub)
        n_cw_sub = (sub["label"] == "CW").sum()
        n_ccw_sub = (sub["label"] == "CCW").sum()
        cw_frac = n_cw_sub / n_sub if n_sub > 0 else 0
        if n_sub > 0:
            binom_p = float(stats.binomtest(n_cw_sub, n_sub, 0.5).pvalue)
        else:
            binom_p = 1.0
        bar_results[bar_label] = {
            "n_total": int(n_sub),
            "n_cw": int(n_cw_sub),
            "n_ccw": int(n_ccw_sub),
            "cw_fraction": float(cw_frac),
            "cw_excess_sigma": float((n_cw_sub - n_sub/2) / np.sqrt(n_sub/4)) if n_sub > 0 else 0,
            "binomial_pval": binom_p,
        }
        print(f"    {bar_label:10s}: N={n_sub:,}  CW={n_cw_sub:,}  CCW={n_ccw_sub:,}  "
              f"CW_frac={cw_frac:.5f}  excess={bar_results[bar_label]['cw_excess_sigma']:.2f}σ  p={binom_p:.4e}")

    # Chi-squared
    contingency_bar = np.array([
        [bar_results["barred"]["n_cw"], bar_results["unbarred"]["n_cw"]],
        [bar_results["barred"]["n_ccw"], bar_results["unbarred"]["n_ccw"]]
    ])
    chi2_bar, p_bar, dof_bar, _ = stats.chi2_contingency(contingency_bar)
    bar_results["chi2_test"] = {"chi2": float(chi2_bar), "pval": float(p_bar), "dof": int(dof_bar)}
    print(f"    Chi-squared (bar vs chirality): chi2={chi2_bar:.2f}, p={p_bar:.4e}, dof={dof_bar}")
else:
    bar_results = {"error": "No bar data available"}

results["morphology_chirality"]["bar_vs_chirality"] = bar_results

# --- 2c. Edge-on galaxies ---
print("\n  --- 2c. Edge-on galaxy classifier predictions ---")
edgeon_col = "disk-edge-on_yes_fraction"
has_edgeon = merged[edgeon_col].notna()
m_eo = merged[has_edgeon].copy()

if len(m_eo) > 0:
    # Strongly edge-on: yes_fraction > 0.5
    edgeon_strong = m_eo[m_eo[edgeon_col] > 0.5]
    edgeon_moderate = m_eo[(m_eo[edgeon_col] > 0.3) & (m_eo[edgeon_col] <= 0.5)]
    face_on = m_eo[m_eo[edgeon_col] <= 0.1]

    edgeon_results = {}
    for label, sub in [("edge_on_gt05", edgeon_strong),
                       ("edge_on_03_05", edgeon_moderate),
                       ("face_on_lt01", face_on)]:
        n_sub = len(sub)
        n_cw_sub = (sub["label"] == "CW").sum()
        n_ccw_sub = (sub["label"] == "CCW").sum()
        n_ns_sub = (sub["label"] == "NOT_SPIRAL").sum()
        edgeon_results[label] = {
            "n_total": int(n_sub),
            "n_cw": int(n_cw_sub),
            "n_ccw": int(n_ccw_sub),
            "n_not_spiral": int(n_ns_sub),
            "not_spiral_fraction": float(n_ns_sub / n_sub) if n_sub > 0 else 0,
            "cw_fraction_of_spirals": float(n_cw_sub / (n_cw_sub + n_ccw_sub)) if (n_cw_sub + n_ccw_sub) > 0 else 0,
        }
        spiral_n = n_cw_sub + n_ccw_sub
        print(f"    {label:20s}: N={n_sub:,}  CW={n_cw_sub:,}  CCW={n_ccw_sub:,}  "
              f"NS={n_ns_sub:,}  NS_frac={n_ns_sub/n_sub:.4f}" + (f"  CW/(CW+CCW)={n_cw_sub/spiral_n:.5f}" if spiral_n > 0 else ""))

    results["morphology_chirality"]["edge_on_analysis"] = edgeon_results
else:
    results["morphology_chirality"]["edge_on_analysis"] = {"error": "No edge-on data"}

# ═════════════════════════════════════════════════════════════════════════════
# 3. MAGNITUDE/SIZE DEPENDENCE (BIAS TEST)
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*72)
print("3. MAGNITUDE/SIZE DEPENDENCE (BIAS TESTS)")
print("="*72)

# GZ DESI doesn't have magnitude/size columns directly in the friendly catalog.
# Use morphological proxies: smooth fraction as a proxy for apparent brightness
# (brighter galaxies have more detail visible), and bulge-size as a structural proxy.
# Also: the how-rounded fractions correlate with apparent size/axis ratio.

# Actually, let's use the catalog's own confidence and probability values as proxies,
# and also split by declination bands (which correlate with different survey depth).

# --- 3a. Confidence-based analysis (proxy for S/N ~ brightness) ---
print("\n  --- 3a. Confidence vs chirality (proxy for brightness/S/N) ---")
spirals_only = cat[(cat["label"] == "CW") | (cat["label"] == "CCW")].copy()
conf_quartiles = spirals_only["confidence_eq"].quantile([0.25, 0.5, 0.75]).values

conf_results = {}
bins = [("Q1_low_conf", 0, conf_quartiles[0]),
        ("Q2", conf_quartiles[0], conf_quartiles[1]),
        ("Q3", conf_quartiles[1], conf_quartiles[2]),
        ("Q4_high_conf", conf_quartiles[2], 1.01)]

for label, lo, hi in bins:
    sub = spirals_only[(spirals_only["confidence_eq"] >= lo) & (spirals_only["confidence_eq"] < hi)]
    n_sub = len(sub)
    n_cw_sub = (sub["label"] == "CW").sum()
    cw_frac = n_cw_sub / n_sub if n_sub > 0 else 0
    excess_sigma = float((n_cw_sub - n_sub/2) / np.sqrt(n_sub/4)) if n_sub > 0 else 0
    conf_results[label] = {
        "conf_range": [float(lo), float(hi)],
        "n_total": int(n_sub),
        "n_cw": int(n_cw_sub),
        "cw_fraction": float(cw_frac),
        "cw_excess_sigma": excess_sigma,
    }
    print(f"    {label:15s} [{lo:.4f},{hi:.4f}): N={n_sub:,}  CW_frac={cw_frac:.6f}  excess={excess_sigma:.2f}σ")

# Chi-squared across quartiles
contingency_conf = np.array([
    [conf_results[b[0]]["n_cw"] for b in bins],
    [conf_results[b[0]]["n_total"] - conf_results[b[0]]["n_cw"] for b in bins]
])
chi2_conf, p_conf, dof_conf, _ = stats.chi2_contingency(contingency_conf)
conf_results["chi2_test"] = {"chi2": float(chi2_conf), "pval": float(p_conf), "dof": int(dof_conf)}
print(f"    Chi-squared (confidence vs chirality): chi2={chi2_conf:.2f}, p={p_conf:.4e}")

results["magnitude_size_dependence"] = {"confidence_vs_chirality": conf_results}

# --- 3b. Declination bands (proxy for survey depth/conditions) ---
print("\n  --- 3b. Declination bands vs chirality ---")
dec_bins = [(-90, -30), (-30, -10), (-10, 10), (10, 30), (30, 60), (60, 90)]
dec_results = {}
for dec_lo, dec_hi in dec_bins:
    label = f"dec_{dec_lo:+d}_to_{dec_hi:+d}"
    sub = spirals_only[(spirals_only["dec"] >= dec_lo) & (spirals_only["dec"] < dec_hi)]
    n_sub = len(sub)
    n_cw_sub = (sub["label"] == "CW").sum()
    cw_frac = n_cw_sub / n_sub if n_sub > 0 else 0
    excess_sigma = float((n_cw_sub - n_sub/2) / np.sqrt(n_sub/4)) if n_sub > 0 else 0
    dec_results[label] = {
        "dec_range": [dec_lo, dec_hi],
        "n_total": int(n_sub),
        "n_cw": int(n_cw_sub),
        "cw_fraction": float(cw_frac),
        "cw_excess_sigma": excess_sigma,
    }
    print(f"    {label:20s}: N={n_sub:,}  CW_frac={cw_frac:.6f}  excess={excess_sigma:.2f}σ")

# Chi-squared
filled_bins = [b for b in dec_results.values() if b["n_total"] > 0]
if len(filled_bins) > 1:
    cont_dec = np.array([
        [b["n_cw"] for b in filled_bins],
        [b["n_total"] - b["n_cw"] for b in filled_bins]
    ])
    chi2_dec, p_dec, dof_dec, _ = stats.chi2_contingency(cont_dec)
    dec_results["chi2_test"] = {"chi2": float(chi2_dec), "pval": float(p_dec), "dof": int(dof_dec)}
    print(f"    Chi-squared (dec band vs chirality): chi2={chi2_dec:.2f}, p={p_dec:.4e}")

results["magnitude_size_dependence"]["declination_vs_chirality"] = dec_results

# --- 3c. Morphological size proxy: bulge-size from GZ DESI ---
print("\n  --- 3c. Bulge size vs chirality (morphological proxy) ---")
bulge_cols = ["bulge-size_dominant_fraction", "bulge-size_large_fraction",
              "bulge-size_moderate_fraction", "bulge-size_small_fraction",
              "bulge-size_none_fraction"]
has_bulge = spirals[bulge_cols].notna().all(axis=1)
sp_bulge = spirals[has_bulge].copy()
print(f"  Spirals with bulge data: {len(sp_bulge):,}")

if len(sp_bulge) > 0:
    sp_bulge["bulge_class"] = sp_bulge[bulge_cols].idxmax(axis=1).str.replace("bulge-size_", "").str.replace("_fraction", "")
    bulge_results = {}
    for bclass in ["dominant", "large", "moderate", "small", "none"]:
        sub = sp_bulge[sp_bulge["bulge_class"] == bclass]
        n_sub = len(sub)
        n_cw_sub = (sub["label"] == "CW").sum()
        cw_frac = n_cw_sub / n_sub if n_sub > 0 else 0
        excess_sigma = float((n_cw_sub - n_sub/2) / np.sqrt(n_sub/4)) if n_sub > 0 else 0
        bulge_results[bclass] = {
            "n_total": int(n_sub),
            "n_cw": int(n_cw_sub),
            "cw_fraction": float(cw_frac),
            "cw_excess_sigma": excess_sigma,
        }
        print(f"    {bclass:10s}: N={n_sub:,}  CW_frac={cw_frac:.6f}  excess={excess_sigma:.2f}σ")

    filled_bulge = [v for v in bulge_results.values() if isinstance(v, dict) and v.get("n_total", 0) > 0]
    if len(filled_bulge) > 1:
        cont_bulge = np.array([
            [b["n_cw"] for b in filled_bulge],
            [b["n_total"] - b["n_cw"] for b in filled_bulge]
        ])
        chi2_bulge, p_bulge, dof_bulge, _ = stats.chi2_contingency(cont_bulge)
        bulge_results["chi2_test"] = {"chi2": float(chi2_bulge), "pval": float(p_bulge), "dof": int(dof_bulge)}
        print(f"    Chi-squared (bulge vs chirality): chi2={chi2_bulge:.2f}, p={p_bulge:.4e}")

    results["magnitude_size_dependence"]["bulge_size_vs_chirality"] = bulge_results

# --- 3d. Smooth vs featured (proxy for resolution/brightness) ---
print("\n  --- 3d. Featured fraction vs chirality ---")
feat_col = "smooth-or-featured_featured-or-disk_fraction"
has_feat = merged[feat_col].notna()
m_feat = merged[has_feat].copy()
m_spirals = m_feat[(m_feat["label"] == "CW") | (m_feat["label"] == "CCW")]

if len(m_spirals) > 0:
    feat_quartiles = m_spirals[feat_col].quantile([0.25, 0.5, 0.75]).values
    feat_results = {}
    fbins = [("Q1_low_featured", 0, feat_quartiles[0]),
             ("Q2", feat_quartiles[0], feat_quartiles[1]),
             ("Q3", feat_quartiles[1], feat_quartiles[2]),
             ("Q4_high_featured", feat_quartiles[2], 1.01)]
    for label, lo, hi in fbins:
        sub = m_spirals[(m_spirals[feat_col] >= lo) & (m_spirals[feat_col] < hi)]
        n_sub = len(sub)
        n_cw_sub = (sub["label"] == "CW").sum()
        cw_frac = n_cw_sub / n_sub if n_sub > 0 else 0
        excess_sigma = float((n_cw_sub - n_sub/2) / np.sqrt(n_sub/4)) if n_sub > 0 else 0
        feat_results[label] = {
            "feat_range": [float(lo), float(hi)],
            "n_total": int(n_sub),
            "n_cw": int(n_cw_sub),
            "cw_fraction": float(cw_frac),
            "cw_excess_sigma": excess_sigma,
        }
        print(f"    {label:20s}: N={n_sub:,}  CW_frac={cw_frac:.6f}  excess={excess_sigma:.2f}σ")

    cont_feat = np.array([
        [feat_results[b[0]]["n_cw"] for b in fbins],
        [feat_results[b[0]]["n_total"] - feat_results[b[0]]["n_cw"] for b in fbins]
    ])
    chi2_feat, p_feat, dof_feat, _ = stats.chi2_contingency(cont_feat)
    feat_results["chi2_test"] = {"chi2": float(chi2_feat), "pval": float(p_feat), "dof": int(dof_feat)}
    print(f"    Chi-squared (featured fraction vs chirality): chi2={chi2_feat:.2f}, p={p_feat:.4e}")
    results["magnitude_size_dependence"]["featured_fraction_vs_chirality"] = feat_results

# ═════════════════════════════════════════════════════════════════════════════
# 4. CATALOG PURITY CHECK — SAMPLE URLS FOR VISUAL INSPECTION
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*72)
print("4. CATALOG PURITY CHECK (SAMPLE URLS)")
print("="*72)

np.random.seed(42)

def sample_galaxies(df, label, n=100, min_confidence=0.8):
    """Sample n high-confidence galaxies of given label."""
    sub = df[(df["label"] == label) & (df["confidence_eq"] >= min_confidence)]
    if len(sub) < n:
        # Fall back to lower confidence threshold
        sub = df[df["label"] == label].nlargest(n, "confidence_eq")
    if len(sub) > n:
        sub = sub.sample(n, random_state=42)
    return sub[["dr8_id", "confidence_eq", "ra", "dec", "image_url"]].to_dict(orient="records")

purity_cw = sample_galaxies(cat, "CW", 100, 0.8)
purity_ccw = sample_galaxies(cat, "CCW", 100, 0.8)
purity_ns = sample_galaxies(cat, "NOT_SPIRAL", 100, 0.8)

results["purity_check"] = {
    "description": "100 high-confidence samples per class for visual inspection",
    "cw_sample": purity_cw,
    "ccw_sample": purity_ccw,
    "not_spiral_sample": purity_ns,
    "cw_mean_confidence": float(np.mean([g["confidence_eq"] for g in purity_cw])),
    "ccw_mean_confidence": float(np.mean([g["confidence_eq"] for g in purity_ccw])),
    "ns_mean_confidence": float(np.mean([g["confidence_eq"] for g in purity_ns])),
}

print(f"  CW sample: {len(purity_cw)} galaxies, mean conf={results['purity_check']['cw_mean_confidence']:.4f}")
print(f"  CCW sample: {len(purity_ccw)} galaxies, mean conf={results['purity_check']['ccw_mean_confidence']:.4f}")
print(f"  NOT_SPIRAL sample: {len(purity_ns)} galaxies, mean conf={results['purity_check']['ns_mean_confidence']:.4f}")

# Print a few example URLs
print("\n  Example CW URLs:")
for g in purity_cw[:3]:
    print(f"    {g['dr8_id']}: {g['image_url']}")
print("  Example CCW URLs:")
for g in purity_ccw[:3]:
    print(f"    {g['dr8_id']}: {g['image_url']}")
print("  Example NOT_SPIRAL URLs:")
for g in purity_ns[:3]:
    print(f"    {g['dr8_id']}: {g['image_url']}")

# ═════════════════════════════════════════════════════════════════════════════
# 5. STATISTICAL POWER ANALYSIS
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*72)
print("5. STATISTICAL POWER ANALYSIS")
print("="*72)

# Total spirals
N_spirals = int(n_spiral)
global_cw_frac = n_cw / n_spiral

print(f"  Total spirals: {N_spirals:,}")
print(f"  Global CW fraction: {global_cw_frac:.6f}")

# --- 5a. Minimum detectable dipole ---
# A dipole signal means CW fraction varies as f(theta) = f0 + A*cos(theta)
# where theta is angle from the dipole axis.
# For N galaxies uniformly distributed, the estimator variance for A is:
# Var(A) ~ 3 * f0*(1-f0) / N  (from Fisher information on sphere)
# At 3-sigma: A_min = 3 * sqrt(Var(A))
sigma_A = np.sqrt(3 * global_cw_frac * (1 - global_cw_frac) / N_spirals)
A_min_3sigma = 3 * sigma_A
A_min_5sigma = 5 * sigma_A

# Account for non-uniform sky coverage
# Effective fraction of sky covered
sky_frac = n_occupied / NPIX
sigma_A_corrected = sigma_A / np.sqrt(sky_frac)
A_min_3sigma_corrected = 3 * sigma_A_corrected
A_min_5sigma_corrected = 5 * sigma_A_corrected

print(f"\n  --- Dipole sensitivity ---")
print(f"  Sky coverage: {sky_frac:.3f} ({100*sky_frac:.1f}%)")
print(f"  Dipole amplitude uncertainty (full sky): sigma_A = {sigma_A:.6f}")
print(f"  Dipole amplitude uncertainty (corrected): sigma_A = {sigma_A_corrected:.6f}")
print(f"  Minimum detectable dipole (3σ, full sky): A = {A_min_3sigma:.6f}")
print(f"  Minimum detectable dipole (3σ, corrected): A = {A_min_3sigma_corrected:.6f}")
print(f"  Minimum detectable dipole (5σ, corrected): A = {A_min_5sigma_corrected:.6f}")

# For context: Longo (2011) claimed A ~ 0.01-0.02 with ~15k galaxies
# Shamir claims A ~ 0.001-0.01 with various samples
print(f"\n  Context: Longo (2011) claimed A ~ 0.01-0.02 with ~15K galaxies")
print(f"           Our 3σ sensitivity is {A_min_3sigma_corrected:.6f} — {'sufficient' if A_min_3sigma_corrected < 0.01 else 'marginal'} for Longo-scale signals")

# --- 5b. Minimum detectable hemisphere asymmetry ---
# Split sky into two hemispheres. Each has ~N/2 spirals.
# CW_N - CW_S has variance ~ f0*(1-f0) * (1/N_N + 1/N_S)
# For equal split: var = 2*f0*(1-f0)/N * 2 = 4*f0*(1-f0)/N
# Detectable asymmetry delta_f at 3-sigma:
N_hemi = N_spirals / 2
sigma_delta = np.sqrt(global_cw_frac * (1 - global_cw_frac) * (1/N_hemi + 1/N_hemi))
delta_3sigma = 3 * sigma_delta
delta_5sigma = 5 * sigma_delta

# Also expressed as fractional asymmetry
frac_asym_3sigma = delta_3sigma / global_cw_frac

print(f"\n  --- Hemisphere asymmetry sensitivity ---")
print(f"  N per hemisphere (approx): {N_hemi:,.0f}")
print(f"  Sigma(delta_f): {sigma_delta:.6f}")
print(f"  Min detectable delta_f (3σ): {delta_3sigma:.6f}")
print(f"  Min detectable delta_f (5σ): {delta_5sigma:.6f}")
print(f"  Min detectable fractional asymmetry (3σ): {frac_asym_3sigma:.6f} ({100*frac_asym_3sigma:.4f}%)")

# --- 5c. Pixel-level sensitivity ---
# Per-pixel sensitivity for NSIDE=32
N_per_pix = N_spirals / n_occupied
sigma_pix = np.sqrt(global_cw_frac * (1 - global_cw_frac) / N_per_pix)
print(f"\n  --- Pixel-level sensitivity (NSIDE=32) ---")
print(f"  Mean spirals per pixel: {N_per_pix:.0f}")
print(f"  Per-pixel sigma(CW_frac): {sigma_pix:.5f}")
print(f"  Per-pixel 3σ: {3*sigma_pix:.5f}")

# --- 5d. Comparison with literature ---
# Shamir 2022 (MNRAS): ~1.2M galaxies, reported 2σ-3σ dipole signals
# Our catalog: 8.5M total, ~X spirals
literature_comparison = {
    "longo_2011": {"n_galaxies": 15158, "claimed_signal": "~7σ dipole, A≈0.02"},
    "shamir_2020": {"n_galaxies": 208478, "claimed_signal": "~2.5σ dipole"},
    "shamir_2022": {"n_galaxies": 1200000, "claimed_signal": "~2-3σ dipole, dataset dependent"},
    "this_work": {"n_spirals": N_spirals, "n_total": N_total,
                  "sensitivity_3sigma_dipole": float(A_min_3sigma_corrected),
                  "sensitivity_5sigma_dipole": float(A_min_5sigma_corrected)},
}

improvement_over_shamir = np.sqrt(1200000 / N_spirals)
print(f"\n  --- Literature comparison ---")
print(f"  Improvement in sigma over Shamir (2022, 1.2M): {1/improvement_over_shamir:.1f}x")
print(f"  Our sample is {N_spirals/1200000:.1f}x larger than Shamir (2022)")

results["statistical_power"] = {
    "n_spirals": N_spirals,
    "n_total": N_total,
    "global_cw_fraction": float(global_cw_frac),
    "sky_fraction_covered": float(sky_frac),
    "dipole": {
        "sigma_A_full_sky": float(sigma_A),
        "sigma_A_coverage_corrected": float(sigma_A_corrected),
        "min_detectable_3sigma": float(A_min_3sigma_corrected),
        "min_detectable_5sigma": float(A_min_5sigma_corrected),
    },
    "hemisphere_asymmetry": {
        "sigma_delta_f": float(sigma_delta),
        "min_detectable_3sigma": float(delta_3sigma),
        "min_detectable_5sigma": float(delta_5sigma),
        "fractional_asymmetry_3sigma": float(frac_asym_3sigma),
    },
    "pixel_level": {
        "nside": NSIDE,
        "mean_spirals_per_pixel": float(N_per_pix),
        "sigma_cw_frac_per_pixel": float(sigma_pix),
    },
    "literature_comparison": literature_comparison,
}

# ═════════════════════════════════════════════════════════════════════════════
# SAVE RESULTS
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*72)
print("SAVING RESULTS")
print("="*72)

# Convert any numpy types for JSON serialization
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

with open(OUT_PATH, "w") as f:
    json.dump(results, f, indent=2, cls=NumpyEncoder)

elapsed = time.time() - t0
print(f"\nResults saved to {OUT_PATH}")
print(f"Total runtime: {elapsed:.1f}s")

# ═════════════════════════════════════════════════════════════════════════════
# COMPREHENSIVE SUMMARY
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*72)
print("COMPREHENSIVE SUMMARY")
print("="*72)

print(f"""
CATALOG: {N_total:,} galaxies | {N_spirals:,} spirals ({100*n_spiral/N_total:.1f}%)
         CW: {n_cw:,} | CCW: {n_ccw:,} | NOT_SPIRAL: {n_ns:,}

1. SPIRAL FRACTION MAP (NSIDE=32)
   Mean spiral fraction: {mean_frac:.4f} ± {std_frac:.4f}
   Range: [{min_frac:.4f}, {max_frac:.4f}]
   Occupied pixels: {n_occupied}/{NPIX} ({100*n_occupied/NPIX:.1f}%)
   Chi² uniformity: χ²={chi2_stat:.1f}, dof={chi2_dof}, p={chi2_pval:.2e}
   Dipole/shot noise: {dipole_power/shot_cl:.2f}x
   Quadrupole/shot noise: {quadrupole_power/shot_cl:.2f}x
   → {"SPATIAL STRUCTURE DETECTED" if chi2_pval < 0.01 else "Consistent with uniform + shot noise"}

2. MORPHOLOGY-CHIRALITY CROSS-ANALYSIS
   Cross-match: {len(merged):,} galaxies ({100*len(merged)/len(cat):.1f}%)
   Winding: tight/medium/loose CW fractions span varies
   Bar: barred vs unbarred chirality comparison
   Edge-on: classifier behavior on edge-on galaxies

3. MAGNITUDE/SIZE BIAS TESTS
   Confidence quartile chi²: χ²={chi2_conf:.2f}, p={p_conf:.2e}
   → {"BIAS DETECTED — CW fraction depends on confidence" if p_conf < 0.01 else "No significant confidence bias"}

4. PURITY CHECK
   300 sample URLs saved (100 per class) for visual inspection

5. STATISTICAL POWER
   Dipole sensitivity (3σ): A_min = {A_min_3sigma_corrected:.6f}
   Dipole sensitivity (5σ): A_min = {A_min_5sigma_corrected:.6f}
   Hemisphere asymmetry (3σ): Δf = {delta_3sigma:.6f}
   Sample is {N_spirals/1200000:.1f}x larger than Shamir (2022)
   Improvement in sigma: {1/improvement_over_shamir:.1f}x over Shamir (2022)
""")
