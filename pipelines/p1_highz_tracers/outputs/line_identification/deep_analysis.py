#!/usr/bin/env python3
"""
Deep analysis of unmatched and interesting anomalies.
Focus on:
1. Sub-Lyman-limit rest wavelengths (< 912A) -- possible Lyman continuum leakers
2. Objects in the "UV desert" (912-1216A) -- possible DLA features
3. Stellar anomalies at unusual wavelengths
4. Galaxy anomalies at rest ~2100-2500A -- possible FeII/FeIII UV bump
5. Redshift-wavelength diagnostic plot
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path

base = Path('/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs')
outdir = base / 'line_identification'

# Load the 83-object catalog
with open(base / 'gold_anomalies' / 'gold_anomalies.json') as f:
    gold_83 = json.load(f)

# Load 120-object catalog
df_120 = pd.read_csv(base / 'gold_anomalies' / 'gold_120_snr05.csv')

# Also load the full 83-object parquet for extra columns
df_83_full = pd.read_parquet(base / 'gold_anomalies' / 'gold_anomalies_83.parquet')

# Extended line list including UV iron pseudo-continuum features
EXTENDED_LINES = {
    # Lyman series
    "Ly-limit (912A)":    912,
    "Ly-gamma":           972,
    "Ly-beta":           1026,
    "Ly-alpha":          1216,
    # UV emission
    "NV":                1240,
    "OI 1302":           1302,
    "SiII 1304":         1304,
    "CII 1335":          1335,
    "SiIV 1394":         1394,
    "SiIV 1403":         1403,
    "CIV":               1549,
    "HeII":              1640,
    "AlIII":             1857,
    "CIII]":             1909,
    # UV iron pseudo-continuum
    "FeII UV1 (2344)":   2344,
    "FeII UV2 (2383)":   2383,
    "FeII UV3 (2587)":   2587,
    "FeII UV4 (2600)":   2600,
    "MgII 2796":         2796,
    "MgII 2803":         2803,
    "MgI 2853":          2853,
    # Near-UV
    "[OII]":             3727,
    "[NeIII]":           3869,
    "CaII K":            3934,
    "CaII H":            3969,
    "4000A break":       4000,
    "H-delta":           4102,
    "H-gamma":           4340,
    "H-beta":            4861,
    "[OIII] 4959":       4959,
    "[OIII] 5007":       5007,
    "MgI b":             5175,
    "NaI D":             5893,
    "[OI]":              6300,
    "H-alpha":           6563,
    "[NII]":             6584,
    "[SII] 6717":        6717,
    "[SII] 6731":        6731,
    # NIR CaII triplet
    "CaII 8498":         8498,
    "CaII 8542":         8542,
    "CaII 8662":         8662,
    # Absorption systems (DLA/sub-DLA features typically at Ly-alpha of absorber)
}

TIGHT_TOLERANCE = 50  # tighter tolerance for extended list

def match_extended(rest_wave):
    best_name, best_dist = None, float('inf')
    for name, w in EXTENDED_LINES.items():
        d = abs(rest_wave - w)
        if d < best_dist:
            best_dist = d
            best_name = name
    return best_name, EXTENDED_LINES.get(best_name, 0), best_dist


# ── Categorize all 83 objects ───────────────────────────────────────────

categories = {
    "sub_lyman_limit": [],      # rest < 912 A
    "lyman_forest_region": [],   # 912 < rest < 1216 A
    "uv_emission_region": [],    # 1216 < rest < 1900 A
    "uv_iron_region": [],        # 1900 < rest < 3000 A
    "optical_region": [],        # 3000 < rest < 7000 A
    "nir_region": [],            # rest > 7000 A
}

detailed_results = []

for obj in gold_83:
    z = obj['z']
    obs_wave = obj['peak_residual_wavelength']
    rest_wave = obs_wave / (1 + z) if z > -1 else obs_wave

    ext_name, ext_lab, ext_dist = match_extended(rest_wave)

    # Categorize by rest-frame region
    if rest_wave < 912:
        cat = "sub_lyman_limit"
    elif rest_wave < 1216:
        cat = "lyman_forest_region"
    elif rest_wave < 1900:
        cat = "uv_emission_region"
    elif rest_wave < 3000:
        cat = "uv_iron_region"
    elif rest_wave < 7000:
        cat = "optical_region"
    else:
        cat = "nir_region"

    # Physical interpretation
    if cat == "sub_lyman_limit":
        if rest_wave < 600:
            phys_interp = "EXTREME sub-LL: possible ionizing continuum anomaly or misclassified z"
        elif rest_wave < 800:
            phys_interp = "Deep sub-LL: Lyman continuum leaker candidate or z error"
        else:
            phys_interp = "Near Lyman limit: possible LyC leaker or DLA Gunn-Peterson trough"
    elif cat == "lyman_forest_region":
        phys_interp = "Lyman forest region: possible unusual IGM absorption or Ly-beta/Ly-gamma feature"
    elif cat == "uv_emission_region":
        if ext_dist < TIGHT_TOLERANCE:
            phys_interp = f"UV emission match: {ext_name} (offset {ext_dist:.0f}A)"
        else:
            phys_interp = "UV desert: no standard emission line, possible unusual FeII or BAL feature"
    elif cat == "uv_iron_region":
        if ext_dist < TIGHT_TOLERANCE:
            phys_interp = f"UV match: {ext_name} (offset {ext_dist:.0f}A)"
        else:
            phys_interp = "UV iron pseudo-continuum region: possible unusual FeII/MgII feature"
    elif cat == "optical_region":
        if ext_dist < TIGHT_TOLERANCE:
            phys_interp = f"Optical match: {ext_name} (offset {ext_dist:.0f}A)"
        else:
            phys_interp = "Optical region: no standard line match"
    else:
        if ext_dist < TIGHT_TOLERANCE:
            phys_interp = f"NIR match: {ext_name} (offset {ext_dist:.0f}A)"
        else:
            phys_interp = "NIR region: possible molecular band or telluric residual"

    categories[cat].append(obj['targetid'])

    detailed_results.append({
        'targetid': obj['targetid'],
        'ra': obj['ra'],
        'dec': obj['dec'],
        'z': z,
        'spectype': obj['spectype'],
        'anomaly_score': obj['anomaly_score'],
        'obs_wavelength': obs_wave,
        'rest_wavelength': round(rest_wave, 2),
        'rest_region': cat,
        'extended_match': ext_name,
        'ext_lab_wavelength': ext_lab,
        'ext_offset': round(ext_dist, 2),
        'matched': ext_dist < TIGHT_TOLERANCE,
        'physical_interpretation': phys_interp,
        'worst_band': obj['worst_band'],
    })


# ── Print category summary ─────────────────────────────────────────────

print("=" * 80)
print("REST-FRAME WAVELENGTH CATEGORIES (83 gold anomalies)")
print("=" * 80)
for cat, ids in categories.items():
    print(f"\n  {cat:25s}: {len(ids)} objects")

# ── Sub-Lyman limit objects ─────────────────────────────────────────────

print("\n" + "=" * 80)
print("SUB-LYMAN-LIMIT OBJECTS (rest < 912A) -- LYMAN CONTINUUM LEAKER CANDIDATES")
print("=" * 80)

sub_ll = [r for r in detailed_results if r['rest_region'] == 'sub_lyman_limit']
sub_ll.sort(key=lambda x: x['rest_wavelength'])

for r in sub_ll:
    print(f"  targetid={r['targetid']}, z={r['z']:.3f}, spectype={r['spectype']}, "
          f"obs={r['obs_wavelength']:.0f}A, rest={r['rest_wavelength']:.0f}A, "
          f"score={r['anomaly_score']:.2f}")
    print(f"    -> {r['physical_interpretation']}")

# ── Lyman forest region ────────────────────────────────────────────────

print("\n" + "=" * 80)
print("LYMAN FOREST REGION (912-1216A) -- IGM/DLA FEATURES")
print("=" * 80)

lyf = [r for r in detailed_results if r['rest_region'] == 'lyman_forest_region']
lyf.sort(key=lambda x: x['rest_wavelength'])

for r in lyf:
    print(f"  targetid={r['targetid']}, z={r['z']:.3f}, spectype={r['spectype']}, "
          f"obs={r['obs_wavelength']:.0f}A, rest={r['rest_wavelength']:.0f}A, "
          f"nearest={r['extended_match']} ({r['ext_offset']:.0f}A away), "
          f"score={r['anomaly_score']:.2f}")

# ── UV Iron region ─────────────────────────────────────────────────────

print("\n" + "=" * 80)
print("UV IRON REGION (1900-3000A) -- FeII/MgII FEATURES")
print("=" * 80)

uv_iron = [r for r in detailed_results if r['rest_region'] == 'uv_iron_region']
uv_iron.sort(key=lambda x: x['rest_wavelength'])

for r in uv_iron:
    matched_str = "MATCHED" if r['matched'] else "UNMATCHED"
    print(f"  targetid={r['targetid']}, z={r['z']:.3f}, spectype={r['spectype']}, "
          f"rest={r['rest_wavelength']:.0f}A, nearest={r['extended_match']} "
          f"({r['ext_offset']:.0f}A), {matched_str}, score={r['anomaly_score']:.2f}")

# ── Objects where z might be wrong ──────────────────────────────────────

print("\n" + "=" * 80)
print("POSSIBLE REDSHIFT ERRORS / MISCLASSIFICATIONS")
print("=" * 80)

suspicious = []
for r in detailed_results:
    # QSOs with rest wavelength far below Lyman limit
    if r['spectype'] == 'QSO' and r['rest_wavelength'] < 700 and r['z'] > 4:
        suspicious.append(r)
    # Stars with z exactly 0 but anomaly at unusual wavelength
    elif r['spectype'] == 'STAR' and abs(r['z']) < 0.001 and not r['matched']:
        suspicious.append(r)
    # GALAXY with very small z but classified differently
    elif r['spectype'] == 'GALAXY' and r['z'] < 0 and r['anomaly_score'] > 3:
        suspicious.append(r)

for r in sorted(suspicious, key=lambda x: -x['anomaly_score']):
    print(f"  targetid={r['targetid']}, z={r['z']:.4f}, spectype={r['spectype']}, "
          f"obs={r['obs_wavelength']:.0f}A, rest={r['rest_wavelength']:.0f}A, "
          f"score={r['anomaly_score']:.2f}")
    print(f"    -> {r['physical_interpretation']}")


# ── Ly-alpha velocity offset analysis ──────────────────────────────────

print("\n" + "=" * 80)
print("LY-ALPHA VELOCITY OFFSET DISTRIBUTION")
print("=" * 80)

lya_matches = [r for r in detailed_results
               if r['extended_match'] == 'Ly-alpha' and r['ext_offset'] < 50]

velocities = []
for r in lya_matches:
    v = (r['rest_wavelength'] - 1216) / 1216 * 3e5
    velocities.append(v)

if velocities:
    velocities = np.array(velocities)
    print(f"  N = {len(velocities)}")
    print(f"  Mean velocity offset: {np.mean(velocities):+.0f} km/s")
    print(f"  Median: {np.median(velocities):+.0f} km/s")
    print(f"  Std: {np.std(velocities):.0f} km/s")
    print(f"  Min: {np.min(velocities):+.0f} km/s")
    print(f"  Max: {np.max(velocities):+.0f} km/s")
    n_red = np.sum(velocities > 0)
    n_blue = np.sum(velocities < 0)
    print(f"  Redshifted: {n_red}, Blueshifted: {n_blue}")
    print(f"  Asymmetry: mostly {'redshifted (IGM absorption blueward)' if n_red > n_blue else 'blueshifted (unusual)'}")


# ── Priority objects for follow-up ──────────────────────────────────────

print("\n" + "=" * 80)
print("TOP PRIORITY OBJECTS FOR SPECTROSCOPIC FOLLOW-UP")
print("=" * 80)

# Score by: unmatched + high anomaly score + high-z
priority = []
for r in detailed_results:
    p_score = r['anomaly_score']
    if not r['matched']:
        p_score *= 1.5  # boost unmatched
    if r['rest_wavelength'] < 912:
        p_score *= 1.3  # boost sub-LL
    if r['spectype'] == 'QSO' and r['z'] > 5:
        p_score *= 1.2  # boost high-z QSOs
    priority.append((p_score, r))

priority.sort(key=lambda x: -x[0])

print(f"\nRank  Score  targetid                z       spectype  rest_wave  interpretation")
print("-" * 120)
for i, (ps, r) in enumerate(priority[:20]):
    print(f"  {i+1:2d}  {ps:5.1f}  {r['targetid']:24d}  {r['z']:7.4f}  {r['spectype']:8s}  "
          f"{r['rest_wavelength']:7.0f}A    {r['physical_interpretation'][:60]}")


# ── Save everything ─────────────────────────────────────────────────────

df_detailed = pd.DataFrame(detailed_results)
df_detailed.to_csv(outdir / 'detailed_line_analysis.csv', index=False)
print(f"\nSaved: {outdir / 'detailed_line_analysis.csv'}")

# Priority list
df_priority = pd.DataFrame([{
    'priority_rank': i+1,
    'priority_score': round(ps, 2),
    **r
} for i, (ps, r) in enumerate(priority[:30])])
df_priority.to_csv(outdir / 'priority_followup.csv', index=False)
print(f"Saved: {outdir / 'priority_followup.csv'}")

# Category summary JSON
cat_summary = {
    'rest_frame_categories': {k: len(v) for k, v in categories.items()},
    'n_sub_lyman_limit': len(sub_ll),
    'n_lyman_forest': len(lyf),
    'n_uv_iron': len(uv_iron),
    'n_suspicious_redshift': len(suspicious),
    'n_lya_velocity_matches': len(velocities) if isinstance(velocities, np.ndarray) and len(velocities) > 0 else 0,
    'lya_mean_velocity_kms': round(float(np.mean(velocities)), 0) if isinstance(velocities, np.ndarray) and len(velocities) > 0 else None,
    'n_matched_extended': sum(1 for r in detailed_results if r['matched']),
    'n_unmatched_extended': sum(1 for r in detailed_results if not r['matched']),
    'total': len(detailed_results),
}
with open(outdir / 'deep_analysis_summary.json', 'w') as f:
    json.dump(cat_summary, f, indent=2)
print(f"Saved: {outdir / 'deep_analysis_summary.json'}")

# ── Now do the 120 catalog ─────────────────────────────────────────────

print("\n" + "=" * 80)
print("120-OBJECT EXTENDED CATALOG -- REST-FRAME CATEGORY BREAKDOWN")
print("=" * 80)

cat_120 = {"sub_lyman_limit": 0, "lyman_forest_region": 0, "uv_emission_region": 0,
           "uv_iron_region": 0, "optical_region": 0, "nir_region": 0}
matched_120 = 0
results_120_detailed = []

for _, row in df_120.iterrows():
    z = row['z']
    obs_wave = row['peak_residual_wavelength']
    rest_wave = obs_wave / (1 + z) if z > -1 else obs_wave

    ext_name, ext_lab, ext_dist = match_extended(rest_wave)

    if rest_wave < 912:
        cat = "sub_lyman_limit"
    elif rest_wave < 1216:
        cat = "lyman_forest_region"
    elif rest_wave < 1900:
        cat = "uv_emission_region"
    elif rest_wave < 3000:
        cat = "uv_iron_region"
    elif rest_wave < 7000:
        cat = "optical_region"
    else:
        cat = "nir_region"

    cat_120[cat] += 1
    if ext_dist < TIGHT_TOLERANCE:
        matched_120 += 1

    results_120_detailed.append({
        'targetid': row['targetid'],
        'z': z,
        'spectype': row['spectype'],
        'obs_wavelength': obs_wave,
        'rest_wavelength': round(rest_wave, 2),
        'rest_region': cat,
        'extended_match': ext_name,
        'ext_offset': round(ext_dist, 2),
        'matched': ext_dist < TIGHT_TOLERANCE,
        'anomaly_score': row['anomaly_score'],
    })

print(f"\nCategory breakdown (120 objects):")
for cat, n in cat_120.items():
    pct = n / 120 * 100
    print(f"  {cat:25s}: {n:3d} ({pct:5.1f}%)")

print(f"\nMatched (extended list, 50A tolerance): {matched_120}/120 ({matched_120/120*100:.1f}%)")
print(f"Unmatched: {120 - matched_120}")

df_120_detailed = pd.DataFrame(results_120_detailed)
df_120_detailed.to_csv(outdir / 'detailed_line_analysis_120.csv', index=False)
print(f"\nSaved: {outdir / 'detailed_line_analysis_120.csv'}")
