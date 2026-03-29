"""
HEALPix sky maps of DESI DR1 anomaly catalog.

Reads deduplicated parquet catalog, assigns objects to NSIDE=64 HEALPix pixels,
and produces three Mollweide projection maps:
  1. Survey depth (total objects per pixel)
  2. Anomaly count per pixel (anomaly_score > 5)
  3. Anomaly rate per pixel (anomaly_count / total_objects)

Also computes Pearson correlation between survey depth and anomaly rate
to check for systematic depth dependence.
"""

import glob
import json
import numpy as np
import healpy as hp
import pyarrow.parquet as pq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

# --- Configuration ---
NSIDE = 64
NPIX = hp.nside2npix(NSIDE)
ANOMALY_THRESHOLD = 5.0
DATA_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped"
OUT_DIR = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/sky_maps"

print(f"NSIDE={NSIDE}, NPIX={NPIX}")
print(f"Pixel area: {hp.nside2pixarea(NSIDE, degrees=True):.4f} deg^2")
print(f"Pixel side: {np.sqrt(hp.nside2pixarea(NSIDE, degrees=True))*60:.1f} arcmin")

# --- Step 1: Read all parquet files, extract RA/DEC/anomaly_score ---
parquet_files = sorted(glob.glob(f"{DATA_DIR}/desi_dr1_catalog_batch_*.parquet"))
print(f"\nFound {len(parquet_files)} parquet files")

# Accumulate per-pixel counts
total_map = np.zeros(NPIX, dtype=np.float64)
anomaly_map = np.zeros(NPIX, dtype=np.float64)

total_objects = 0
total_anomalies = 0

for i, fpath in enumerate(parquet_files):
    table = pq.read_table(fpath, columns=['target_ra', 'target_dec', 'anomaly_score'])
    ra = table.column('target_ra').to_numpy()
    dec = table.column('target_dec').to_numpy()
    score = table.column('anomaly_score').to_numpy()

    # Step 2: Assign to HEALPix pixels (lonlat=True: input is lon=RA, lat=DEC in degrees)
    pixels = hp.ang2pix(NSIDE, ra, dec, lonlat=True, nest=False)

    # Step 3: Count total and anomalies per pixel
    np.add.at(total_map, pixels, 1)

    is_anomaly = score > ANOMALY_THRESHOLD
    anomaly_pixels = pixels[is_anomaly]
    np.add.at(anomaly_map, anomaly_pixels, 1)

    n = len(ra)
    n_anom = is_anomaly.sum()
    total_objects += n
    total_anomalies += n_anom

    if (i + 1) % 10 == 0 or i == 0 or i == len(parquet_files) - 1:
        print(f"  File {i+1}/{len(parquet_files)}: {n:,} objects, {n_anom:,} anomalies | cumulative: {total_objects:,} objects, {total_anomalies:,} anomalies")

print(f"\nTotal: {total_objects:,} objects, {total_anomalies:,} anomalies ({100*total_anomalies/total_objects:.3f}%)")

# --- Step 3: Compute anomaly rate ---
# Only compute rate where we have objects (avoid division by zero)
observed_mask = total_map > 0
rate_map = np.full(NPIX, hp.UNSEEN)
rate_map[observed_mask] = anomaly_map[observed_mask] / total_map[observed_mask]

# For display: set unobserved pixels to UNSEEN
depth_display = np.copy(total_map)
depth_display[~observed_mask] = hp.UNSEEN

anomaly_display = np.copy(anomaly_map)
anomaly_display[~observed_mask] = hp.UNSEEN

# --- Stats on observed pixels ---
n_observed_pixels = observed_mask.sum()
print(f"\nObserved HEALPix pixels: {n_observed_pixels} / {NPIX} ({100*n_observed_pixels/NPIX:.1f}%)")
print(f"Sky coverage: {n_observed_pixels * hp.nside2pixarea(NSIDE, degrees=True):.0f} deg^2")

depth_values = total_map[observed_mask]
rate_values = rate_map[observed_mask]
anomaly_values = anomaly_map[observed_mask]

print(f"\nSurvey depth per pixel: median={np.median(depth_values):.0f}, mean={np.mean(depth_values):.0f}, max={np.max(depth_values):.0f}")
print(f"Anomaly count per pixel: median={np.median(anomaly_values):.0f}, mean={np.mean(anomaly_values):.1f}, max={np.max(anomaly_values):.0f}")
print(f"Anomaly rate per pixel: median={np.median(rate_values):.5f}, mean={np.mean(rate_values):.5f}, max={np.max(rate_values):.5f}")

# --- Step 5: Correlation test ---
# Only use pixels with sufficient objects for stable rate estimate
MIN_OBJECTS = 50
stable_mask = total_map >= MIN_OBJECTS
n_stable = stable_mask.sum()
depth_stable = total_map[stable_mask]
rate_stable = anomaly_map[stable_mask] / total_map[stable_mask]

pearson_r, pearson_p = stats.pearsonr(depth_stable, rate_stable)
spearman_r, spearman_p = stats.spearmanr(depth_stable, rate_stable)

print(f"\n--- Depth-Rate Correlation (pixels with >= {MIN_OBJECTS} objects, N={n_stable}) ---")
print(f"Pearson:  r = {pearson_r:.4f}, p = {pearson_p:.2e}")
print(f"Spearman: r = {spearman_r:.4f}, p = {spearman_p:.2e}")

if abs(pearson_r) < 0.1:
    interpretation = "UNCORRELATED: Anomaly rate does NOT depend on survey depth. Anomalies likely trace real astrophysical structure, not systematics."
elif abs(pearson_r) < 0.3:
    interpretation = "WEAKLY CORRELATED: Slight depth dependence detected. Some systematic contribution possible, but anomalies may still partially trace real structure."
else:
    interpretation = "CORRELATED: Anomaly rate depends on survey depth. Systematics (e.g., S/N, exposure time) likely contribute to anomaly detection."

print(f"Interpretation: {interpretation}")

# --- Step 4: Create Mollweide projection maps ---
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 12,
    'figure.facecolor': 'white',
})

# Map 1: Survey depth
fig1 = plt.figure(figsize=(16, 8))
hp.mollview(
    depth_display,
    title="DESI DR1 Survey Depth (objects per HEALPix pixel, NSIDE=64)",
    unit="N objects",
    cmap="viridis",
    norm="log",
    fig=fig1.number,
    hold=True,
)
hp.graticule(dpar=30, dmer=30, alpha=0.3)
fig1.savefig(f"{OUT_DIR}/survey_depth_map.png", dpi=200, bbox_inches='tight')
print(f"\nSaved: {OUT_DIR}/survey_depth_map.png")
plt.close(fig1)

# Map 2: Anomaly count
fig2 = plt.figure(figsize=(16, 8))
# Use log scale only if there are nonzero anomaly pixels
anomaly_display_log = np.copy(anomaly_display)
anomaly_display_log[(anomaly_display_log != hp.UNSEEN) & (anomaly_display_log == 0)] = hp.UNSEEN
hp.mollview(
    anomaly_display_log,
    title=f"DESI DR1 Anomaly Count (score > {ANOMALY_THRESHOLD}, NSIDE=64)",
    unit="N anomalies",
    cmap="hot",
    norm="log",
    fig=fig2.number,
    hold=True,
)
hp.graticule(dpar=30, dmer=30, alpha=0.3)
fig2.savefig(f"{OUT_DIR}/anomaly_count_map.png", dpi=200, bbox_inches='tight')
print(f"Saved: {OUT_DIR}/anomaly_count_map.png")
plt.close(fig2)

# Map 3: Anomaly rate (linear scale)
fig3 = plt.figure(figsize=(16, 8))
# Clip rate display to only pixels with enough objects for meaningful rate
rate_display = np.full(NPIX, hp.UNSEEN)
rate_display[stable_mask] = rate_stable
hp.mollview(
    rate_display,
    title=f"DESI DR1 Anomaly Rate (score > {ANOMALY_THRESHOLD}, pixels with N >= {MIN_OBJECTS})",
    unit="Anomaly rate",
    cmap="RdYlBu_r",
    fig=fig3.number,
    hold=True,
    min=0,
)
hp.graticule(dpar=30, dmer=30, alpha=0.3)
fig3.savefig(f"{OUT_DIR}/anomaly_rate_map.png", dpi=200, bbox_inches='tight')
print(f"Saved: {OUT_DIR}/anomaly_rate_map.png")
plt.close(fig3)

# --- Bonus: Scatter plot of depth vs rate ---
fig4, ax = plt.subplots(figsize=(10, 7))
ax.scatter(depth_stable, rate_stable * 100, s=2, alpha=0.3, c='steelblue')
ax.set_xlabel("Survey depth (objects per pixel)", fontsize=14)
ax.set_ylabel("Anomaly rate (%)", fontsize=14)
ax.set_title(f"Depth vs Anomaly Rate (Pearson r = {pearson_r:.4f}, p = {pearson_p:.2e})", fontsize=14)
ax.axhline(y=100 * total_anomalies / total_objects, color='red', ls='--', alpha=0.6, label=f'Global rate: {100*total_anomalies/total_objects:.3f}%')
ax.legend(fontsize=12)
ax.set_xscale('log')
fig4.savefig(f"{OUT_DIR}/depth_vs_rate_scatter.png", dpi=200, bbox_inches='tight')
print(f"Saved: {OUT_DIR}/depth_vs_rate_scatter.png")
plt.close(fig4)

# --- Step 7: Save statistics to JSON ---
stats_dict = {
    "nside": NSIDE,
    "npix": int(NPIX),
    "pixel_area_deg2": round(hp.nside2pixarea(NSIDE, degrees=True), 4),
    "total_objects": int(total_objects),
    "total_anomalies": int(total_anomalies),
    "anomaly_threshold": ANOMALY_THRESHOLD,
    "global_anomaly_rate": round(total_anomalies / total_objects, 6),
    "n_observed_pixels": int(n_observed_pixels),
    "sky_coverage_deg2": round(n_observed_pixels * hp.nside2pixarea(NSIDE, degrees=True), 1),
    "sky_coverage_fraction": round(n_observed_pixels / NPIX, 4),
    "depth_per_pixel": {
        "median": round(float(np.median(depth_values)), 1),
        "mean": round(float(np.mean(depth_values)), 1),
        "std": round(float(np.std(depth_values)), 1),
        "max": int(np.max(depth_values)),
    },
    "anomaly_rate_per_pixel": {
        "median": round(float(np.median(rate_values)), 6),
        "mean": round(float(np.mean(rate_values)), 6),
        "max": round(float(np.max(rate_values)), 6),
    },
    "depth_rate_correlation": {
        "min_objects_per_pixel": MIN_OBJECTS,
        "n_pixels_used": int(n_stable),
        "pearson_r": round(pearson_r, 6),
        "pearson_p": float(f"{pearson_p:.4e}"),
        "spearman_r": round(spearman_r, 6),
        "spearman_p": float(f"{spearman_p:.4e}"),
        "interpretation": interpretation,
    },
}

with open(f"{OUT_DIR}/sky_map_stats.json", 'w') as f:
    json.dump(stats_dict, f, indent=2)
print(f"\nSaved: {OUT_DIR}/sky_map_stats.json")

print("\nDone.")
