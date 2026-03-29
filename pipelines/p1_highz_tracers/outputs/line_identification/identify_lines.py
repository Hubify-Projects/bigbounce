#!/usr/bin/env python3
"""
Spectral Line Identification for Gold Anomalies
================================================
For each gold anomaly, compute rest-frame wavelength of the peak residual
and match against known emission/absorption lines.

Uses both the 83-object JSON catalog and the 120-object CSV catalog.
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path
import csv

# ── Known spectral lines (rest-frame wavelengths in Angstroms) ──────────────
KNOWN_LINES = {
    # UV / high-z emission lines
    "Ly-alpha":         1216,
    "Ly-beta":          1026,
    "NV":               1240,
    "SiIV":             1397,
    "CIV":              1549,
    "HeII":             1640,
    "CIII]":            1909,
    "MgII":             2798,
    # Optical emission lines
    "[OII]":            3727,
    "[NeIII]":          3869,
    "H-delta":          4102,
    "H-gamma":          4340,
    "H-beta":           4861,
    "[OIII] 4959":      4959,
    "[OIII] 5007":      5007,
    "[OI]":             6300,
    "H-alpha":          6563,
    "[NII]":            6584,
    "[SII] 6717":       6717,
    "[SII] 6731":       6731,
    # Absorption features
    "CaII K":           3934,
    "CaII H":           3969,
    "4000A break":      4000,
    "CaI":              4227,
    "G-band":           4304,
    "MgI b":            5175,
    "NaI D":            5893,
    "CaII triplet 8498": 8498,
    "CaII triplet 8542": 8542,
    "CaII triplet 8662": 8662,
    # Telluric / instrumental
    "O2 A-band (telluric)": 7600,
    "O2 B-band (telluric)": 6870,
    "H2O (telluric)":       7200,
    # Stellar
    "TiO 7100":         7100,
    "TiO 8430":         8430,
}

# Tolerance for matching (in Angstroms, rest-frame)
MATCH_TOLERANCE = 80  # generous for low-res DESI spectra

def compute_rest_wavelength(obs_wavelength, z):
    """Compute rest-frame wavelength from observed and redshift."""
    if z <= -1:
        return obs_wavelength  # unphysical, return as-is
    return obs_wavelength / (1 + z)

def find_best_line_match(rest_wavelength, tolerance=MATCH_TOLERANCE):
    """Find the closest known spectral line within tolerance."""
    best_name = None
    best_dist = float('inf')

    for name, lab_wave in KNOWN_LINES.items():
        dist = abs(rest_wavelength - lab_wave)
        if dist < best_dist:
            best_dist = dist
            best_name = name

    if best_dist <= tolerance:
        return best_name, KNOWN_LINES[best_name], best_dist
    else:
        return None, None, best_dist

def classify_anomaly_type(row, rest_wave, line_name):
    """Classify the nature of the anomaly based on all available info."""
    spectype = row.get('spectype', '')
    z = row.get('z', 0)
    anomaly_score = row.get('anomaly_score', 0)

    # Stars with near-zero redshift
    if spectype == 'STAR' or (abs(z) < 0.001):
        if line_name and 'CaII' in line_name:
            return "Unusual stellar CaII feature"
        elif line_name and 'TiO' in line_name:
            return "Unusual TiO band (cool star)"
        elif line_name and ('H-alpha' in line_name or 'H-beta' in line_name):
            return "Stellar Balmer anomaly (emission star?)"
        elif line_name and 'NaI' in line_name:
            return "Unusual NaI absorption (peculiar atmosphere)"
        elif line_name and 'MgI' in line_name:
            return "Unusual MgI feature"
        elif line_name:
            return f"Stellar anomaly near {line_name}"
        else:
            return "Unidentified stellar anomaly"

    # QSOs
    if spectype == 'QSO':
        if z > 4:
            if line_name == 'Ly-alpha':
                return "High-z QSO Ly-alpha anomaly (IGM absorption?)"
            elif line_name == 'Ly-beta':
                return "High-z QSO Ly-beta anomaly"
            elif line_name == 'NV':
                return "High-z QSO NV emission anomaly"
            elif line_name == 'CIV':
                return "High-z QSO CIV emission anomaly (BAL?)"
            elif line_name and 'telluric' in line_name:
                return "High-z QSO with telluric contamination"
            elif line_name:
                return f"High-z QSO anomaly near {line_name}"
            else:
                return "High-z QSO UNMATCHED anomaly -- INVESTIGATE"
        elif z > 1:
            if line_name == 'MgII':
                return "Intermediate-z QSO MgII anomaly (BAL/absorption?)"
            elif line_name == 'CIV':
                return "Intermediate-z QSO CIV anomaly (BAL?)"
            elif line_name == 'CIII]':
                return "Intermediate-z QSO CIII] anomaly"
            elif line_name == 'Ly-alpha':
                return "Intermediate-z QSO Ly-alpha anomaly"
            elif line_name:
                return f"Intermediate-z QSO anomaly near {line_name}"
            else:
                return "Intermediate-z QSO UNMATCHED anomaly -- INVESTIGATE"
        else:
            if line_name:
                return f"Low-z QSO anomaly near {line_name}"
            else:
                return "Low-z QSO UNMATCHED anomaly -- INVESTIGATE"

    # Galaxies
    if spectype == 'GALAXY':
        if line_name == '[OII]':
            return "Galaxy [OII] emission anomaly (strong emitter?)"
        elif line_name == '[OIII] 5007' or line_name == '[OIII] 4959':
            return "Galaxy [OIII] emission anomaly (AGN?)"
        elif line_name == 'H-alpha':
            return "Galaxy H-alpha anomaly (starburst?)"
        elif line_name == 'H-beta':
            return "Galaxy H-beta anomaly"
        elif line_name == 'MgII':
            return "Galaxy MgII anomaly (AGN outflow?)"
        elif line_name == 'CaII K' or line_name == 'CaII H':
            return "Galaxy CaII absorption anomaly (old population?)"
        elif line_name == '4000A break':
            return "Galaxy 4000A break anomaly"
        elif line_name:
            return f"Galaxy anomaly near {line_name}"
        else:
            return "Galaxy UNMATCHED anomaly -- INVESTIGATE"

    if line_name:
        return f"Anomaly near {line_name}"
    return "UNMATCHED anomaly -- INVESTIGATE"


def process_catalog(catalog, catalog_name):
    """Process a catalog of anomalies and return line identifications."""
    results = []

    for i, row in enumerate(catalog):
        obs_wave = row['peak_residual_wavelength']
        z = row['z']
        spectype = row.get('spectype', 'UNKNOWN')

        # Compute rest-frame wavelength
        rest_wave = compute_rest_wavelength(obs_wave, z)

        # Find best line match
        line_name, lab_wave, offset = find_best_line_match(rest_wave)

        # Classify the anomaly
        classification = classify_anomaly_type(row, rest_wave, line_name)

        results.append({
            'index': i,
            'targetid': row.get('targetid', ''),
            'ra': row.get('ra', row.get('target_ra', '')),
            'dec': row.get('dec', row.get('target_dec', '')),
            'z': z,
            'spectype': spectype,
            'anomaly_score': row.get('anomaly_score', ''),
            'obs_wavelength': obs_wave,
            'rest_wavelength': round(rest_wave, 2),
            'matched_line': line_name if line_name else 'UNMATCHED',
            'lab_wavelength': lab_wave if lab_wave else '',
            'offset_angstrom': round(offset, 2),
            'classification': classification,
            'is_unmatched': line_name is None,
            'worst_band': row.get('worst_band', ''),
        })

    return results


def aggregate_statistics(results):
    """Compute aggregate statistics over the line identifications."""
    stats = {}

    total = len(results)

    # Count by matched line
    line_counts = {}
    for r in results:
        ln = r['matched_line']
        line_counts[ln] = line_counts.get(ln, 0) + 1

    # Sort by count
    line_counts_sorted = dict(sorted(line_counts.items(), key=lambda x: -x[1]))

    # Count by spectype
    type_counts = {}
    for r in results:
        t = r['spectype']
        type_counts[t] = type_counts.get(t, 0) + 1

    # Unmatched fraction
    n_unmatched = sum(1 for r in results if r['is_unmatched'])

    # Classification counts
    class_counts = {}
    for r in results:
        c = r['classification']
        class_counts[c] = class_counts.get(c, 0) + 1
    class_counts_sorted = dict(sorted(class_counts.items(), key=lambda x: -x[1]))

    # Average anomaly score by line
    line_scores = {}
    for r in results:
        ln = r['matched_line']
        if ln not in line_scores:
            line_scores[ln] = []
        line_scores[ln].append(float(r['anomaly_score']) if r['anomaly_score'] != '' else 0)
    line_avg_scores = {k: round(np.mean(v), 3) for k, v in line_scores.items()}

    stats['total'] = total
    stats['n_unmatched'] = n_unmatched
    stats['unmatched_fraction'] = round(n_unmatched / total, 4) if total > 0 else 0
    stats['line_counts'] = line_counts_sorted
    stats['type_counts'] = type_counts
    stats['classification_counts'] = class_counts_sorted
    stats['line_avg_anomaly_scores'] = line_avg_scores

    return stats


def main():
    base = Path('/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs')
    outdir = base / 'line_identification'
    outdir.mkdir(exist_ok=True)

    # ── Load 83-object JSON catalog ─────────────────────────────────────
    with open(base / 'gold_anomalies' / 'gold_anomalies.json') as f:
        gold_83 = json.load(f)
    print(f"Loaded {len(gold_83)} objects from gold_anomalies.json")

    # ── Load 120-object CSV catalog ─────────────────────────────────────
    df_120 = pd.read_csv(base / 'gold_anomalies' / 'gold_120_snr05.csv')
    gold_120 = df_120.to_dict('records')
    print(f"Loaded {len(gold_120)} objects from gold_120_snr05.csv")

    # ── Process the 83-object catalog ───────────────────────────────────
    print("\n" + "="*80)
    print("PROCESSING 83 GOLD ANOMALIES (primary catalog)")
    print("="*80)

    results_83 = process_catalog(gold_83, "gold_83")
    stats_83 = aggregate_statistics(results_83)

    print(f"\nTotal objects: {stats_83['total']}")
    print(f"Unmatched: {stats_83['n_unmatched']} ({stats_83['unmatched_fraction']*100:.1f}%)")
    print(f"\nSpectral type distribution: {stats_83['type_counts']}")

    print(f"\n--- Line identification counts (83 objects) ---")
    for line, count in stats_83['line_counts'].items():
        pct = count / stats_83['total'] * 100
        avg_score = stats_83['line_avg_anomaly_scores'].get(line, 0)
        print(f"  {line:30s}: {count:3d} ({pct:5.1f}%)  avg_score={avg_score:.2f}")

    print(f"\n--- Classification breakdown ---")
    for cls, count in stats_83['classification_counts'].items():
        print(f"  {cls:55s}: {count:3d}")

    # ── Process the 120-object catalog ──────────────────────────────────
    print("\n" + "="*80)
    print("PROCESSING 120 GOLD ANOMALIES (extended catalog)")
    print("="*80)

    results_120 = process_catalog(gold_120, "gold_120")
    stats_120 = aggregate_statistics(results_120)

    print(f"\nTotal objects: {stats_120['total']}")
    print(f"Unmatched: {stats_120['n_unmatched']} ({stats_120['unmatched_fraction']*100:.1f}%)")
    print(f"\nSpectral type distribution: {stats_120['type_counts']}")

    print(f"\n--- Line identification counts (120 objects) ---")
    for line, count in stats_120['line_counts'].items():
        pct = count / stats_120['total'] * 100
        avg_score = stats_120['line_avg_anomaly_scores'].get(line, 0)
        print(f"  {line:30s}: {count:3d} ({pct:5.1f}%)  avg_score={avg_score:.2f}")

    # ── Identify the UNMATCHED objects (most interesting) ───────────────
    print("\n" + "="*80)
    print("UNMATCHED OBJECTS -- MOST SCIENTIFICALLY INTERESTING")
    print("="*80)

    unmatched_83 = [r for r in results_83 if r['is_unmatched']]
    print(f"\nFrom 83-object catalog: {len(unmatched_83)} unmatched")
    for u in sorted(unmatched_83, key=lambda x: -float(x['anomaly_score']) if x['anomaly_score'] != '' else 0):
        print(f"  targetid={u['targetid']}, z={u['z']:.4f}, spectype={u['spectype']}, "
              f"obs_wave={u['obs_wavelength']:.1f}, rest_wave={u['rest_wavelength']:.1f}, "
              f"score={u['anomaly_score']:.2f} -- {u['classification']}")

    unmatched_120 = [r for r in results_120 if r['is_unmatched']]
    print(f"\nFrom 120-object catalog: {len(unmatched_120)} unmatched")
    for u in sorted(unmatched_120, key=lambda x: -float(x['anomaly_score']) if x['anomaly_score'] != '' else 0):
        nearest_name, nearest_wave = None, None
        min_dist = float('inf')
        for name, wave in KNOWN_LINES.items():
            d = abs(u['rest_wavelength'] - wave)
            if d < min_dist:
                min_dist = d
                nearest_name = name
                nearest_wave = wave
        print(f"  targetid={u['targetid']}, z={u['z']:.4f}, spectype={u['spectype']}, "
              f"obs_wave={u['obs_wavelength']:.1f}, rest_wave={u['rest_wavelength']:.1f}, "
              f"score={float(u['anomaly_score']):.2f}, nearest={nearest_name}({nearest_wave}A, offset={min_dist:.0f}A)")

    # ── Ly-alpha deep dive (dominant feature) ───────────────────────────
    print("\n" + "="*80)
    print("LY-ALPHA ANOMALIES -- DEEP DIVE")
    print("="*80)

    lya_objects = [r for r in results_83 if r['matched_line'] == 'Ly-alpha']
    if lya_objects:
        zs = [r['z'] for r in lya_objects]
        scores = [float(r['anomaly_score']) for r in lya_objects]
        offsets = [r['offset_angstrom'] for r in lya_objects]
        print(f"  Count: {len(lya_objects)}")
        print(f"  Redshift range: {min(zs):.3f} - {max(zs):.3f}")
        print(f"  Mean anomaly score: {np.mean(scores):.3f}")
        print(f"  Mean offset from 1216A: {np.mean(offsets):.1f}A")
        print(f"  Median offset: {np.median(offsets):.1f}A")

        # Velocity offsets
        print(f"\n  Velocity offsets from Ly-alpha (negative = blueshift):")
        for r in sorted(lya_objects, key=lambda x: x['offset_angstrom']):
            v_offset = (r['rest_wavelength'] - 1216) / 1216 * 3e5  # km/s
            print(f"    targetid={r['targetid']}, z={r['z']:.3f}, "
                  f"rest_wave={r['rest_wavelength']:.1f}, "
                  f"v_offset={v_offset:+.0f} km/s, score={float(r['anomaly_score']):.2f}")

    # ── Save all results ────────────────────────────────────────────────

    # 1. Full results CSV (83 objects)
    df_results_83 = pd.DataFrame(results_83)
    df_results_83.to_csv(outdir / 'line_id_83_gold.csv', index=False)
    print(f"\nSaved: {outdir / 'line_id_83_gold.csv'}")

    # 2. Full results CSV (120 objects)
    df_results_120 = pd.DataFrame(results_120)
    df_results_120.to_csv(outdir / 'line_id_120_gold.csv', index=False)
    print(f"Saved: {outdir / 'line_id_120_gold.csv'}")

    # 3. Unmatched objects (most interesting)
    df_unmatched = pd.DataFrame(unmatched_120)
    df_unmatched.to_csv(outdir / 'unmatched_objects.csv', index=False)
    print(f"Saved: {outdir / 'unmatched_objects.csv'}")

    # 4. Statistics JSON
    # Combine stats
    full_stats = {
        'catalog_83': stats_83,
        'catalog_120': stats_120,
        'known_lines_used': KNOWN_LINES,
        'match_tolerance_angstrom': MATCH_TOLERANCE,
    }
    with open(outdir / 'line_id_statistics.json', 'w') as f:
        json.dump(full_stats, f, indent=2, default=str)
    print(f"Saved: {outdir / 'line_id_statistics.json'}")

    # 5. Summary report
    with open(outdir / 'line_id_summary.txt', 'w') as f:
        f.write("SPECTRAL LINE IDENTIFICATION -- GOLD ANOMALY CATALOG\n")
        f.write("=" * 70 + "\n\n")

        f.write("METHODOLOGY\n")
        f.write("-" * 40 + "\n")
        f.write(f"Match tolerance: {MATCH_TOLERANCE} Angstrom (rest-frame)\n")
        f.write(f"Number of reference lines: {len(KNOWN_LINES)}\n")
        f.write(f"Rest-frame wavelength: lambda_obs / (1 + z)\n\n")

        f.write("83-OBJECT PRIMARY CATALOG\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total: {stats_83['total']}\n")
        f.write(f"Matched: {stats_83['total'] - stats_83['n_unmatched']}\n")
        f.write(f"Unmatched: {stats_83['n_unmatched']} ({stats_83['unmatched_fraction']*100:.1f}%)\n")
        f.write(f"Types: {stats_83['type_counts']}\n\n")

        f.write("Line counts:\n")
        for line, count in stats_83['line_counts'].items():
            pct = count / stats_83['total'] * 100
            f.write(f"  {line:30s}: {count:3d} ({pct:5.1f}%)\n")

        f.write(f"\n120-OBJECT EXTENDED CATALOG\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total: {stats_120['total']}\n")
        f.write(f"Matched: {stats_120['total'] - stats_120['n_unmatched']}\n")
        f.write(f"Unmatched: {stats_120['n_unmatched']} ({stats_120['unmatched_fraction']*100:.1f}%)\n")
        f.write(f"Types: {stats_120['type_counts']}\n\n")

        f.write("Line counts:\n")
        for line, count in stats_120['line_counts'].items():
            pct = count / stats_120['total'] * 100
            f.write(f"  {line:30s}: {count:3d} ({pct:5.1f}%)\n")

        f.write(f"\nUNMATCHED OBJECTS (most scientifically interesting)\n")
        f.write("-" * 40 + "\n")
        for u in sorted(unmatched_120, key=lambda x: -float(x['anomaly_score']) if x['anomaly_score'] != '' else 0):
            f.write(f"  targetid={u['targetid']}, z={u['z']:.4f}, spectype={u['spectype']}, "
                    f"rest_wave={u['rest_wavelength']:.1f}A, score={float(u['anomaly_score']):.2f}\n")

        f.write(f"\nKEY FINDINGS\n")
        f.write("-" * 40 + "\n")

        # Determine dominant feature
        top_line = list(stats_83['line_counts'].keys())[0]
        top_count = list(stats_83['line_counts'].values())[0]
        top_pct = top_count / stats_83['total'] * 100

        f.write(f"1. Dominant feature: {top_line} ({top_count}/{stats_83['total']}, {top_pct:.0f}%)\n")
        f.write(f"2. Unmatched fraction: {stats_83['n_unmatched']}/{stats_83['total']} ({stats_83['unmatched_fraction']*100:.1f}%)\n")
        f.write(f"3. Most common spectype: QSO ({stats_83['type_counts'].get('QSO', 0)}/{stats_83['total']})\n")

        # High-z fraction
        n_highz = sum(1 for r in results_83 if r['z'] > 4)
        f.write(f"4. High-z (z>4) objects: {n_highz}/{stats_83['total']} ({n_highz/stats_83['total']*100:.0f}%)\n")

    print(f"Saved: {outdir / 'line_id_summary.txt'}")

    # ── Print final summary ─────────────────────────────────────────────
    print("\n" + "="*80)
    print("FINAL SUMMARY")
    print("="*80)
    print(f"\n83 gold anomalies analyzed:")
    print(f"  - {stats_83['total'] - stats_83['n_unmatched']} matched to known lines")
    print(f"  - {stats_83['n_unmatched']} UNMATCHED (rest-frame wavelength > {MATCH_TOLERANCE}A from any known line)")
    print(f"  - Top 3 lines: ", end="")
    for i, (line, count) in enumerate(list(stats_83['line_counts'].items())[:3]):
        if i > 0: print(", ", end="")
        print(f"{line} ({count})", end="")
    print()

    print(f"\n120 extended anomalies analyzed:")
    print(f"  - {stats_120['total'] - stats_120['n_unmatched']} matched to known lines")
    print(f"  - {stats_120['n_unmatched']} UNMATCHED")

    return results_83, results_120, stats_83, stats_120


if __name__ == '__main__':
    main()
