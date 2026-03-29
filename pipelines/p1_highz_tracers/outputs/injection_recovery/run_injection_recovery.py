#!/usr/bin/env python3
"""
BigAE Empirical Injection/Recovery Test
========================================
Measures autoencoder completeness for detecting genuine spectral anomalies
using the existing 22.5M-object deduplicated DESI DR1 catalog.

Method: empirical injection/recovery on KNOWN unusual objects.
We select objects that should be anomalous based on astrophysical reasoning
and measure what fraction the autoencoder actually flags.

Categories of "known anomalous" objects:
  1. High-z QSOs (z > 3): rare, extreme spectra
  2. Very-high-z QSOs (z > 5): exceptionally rare
  3. Pipeline-flagged but well-detected (ZWARN != 0, SNR > 2)
  4. Spectral mismatches: STAR with z > 0.01 (impossible for real stars)
  5. White dwarfs: spectrally distinct from normal stars
  6. Low deltachi2 QSOs: ambiguous pipeline classification

False positive controls:
  A. Normal low-z galaxies (GALAXY, z < 0.5, ZWARN=0, SNR > 5)
  B. Normal stars (STAR, ZWARN=0, SNR > 5, z ~ 0)
  C. Normal QSOs (QSO, 0.5 < z < 2, ZWARN=0, SNR > 3)

Also analyzes the gold anomaly catalog for known rare types recovered.

Houston Golden, 2026-03-29
"""

import os
import json
import glob
import numpy as np
import pandas as pd
from datetime import datetime

BASE = "/Users/houstongolden/Desktop/CODE_2026/bigbounce"
CATALOG_DIR = os.path.join(BASE, "pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped")
GOLD_FILE = os.path.join(BASE, "pipelines/p1_highz_tracers/outputs/gold_anomalies/gold_anomalies_83.parquet")
BROAD_FILE = os.path.join(BASE, "pipelines/p1_highz_tracers/outputs/gold_anomalies/broad_anomalies_115.parquet")
OUTPUT_DIR = os.path.join(BASE, "pipelines/p1_highz_tracers/outputs/injection_recovery")

# Anomaly score thresholds to test
THRESHOLDS = [3, 5, 7]

def load_full_catalog():
    """Load all 46 parquet batches into a single DataFrame with key columns only."""
    files = sorted(glob.glob(os.path.join(CATALOG_DIR, "desi_dr1_catalog_batch_*.parquet")))
    print(f"Loading {len(files)} catalog files...")

    cols = [
        'anomaly_score', 'z', 'zwarn', 'spectype', 'subtype',
        'deltachi2', 'targetid',
        'median_coadd_snr_b', 'median_coadd_snr_r', 'median_coadd_snr_z',
        'classification', 'discovery_potential'
    ]

    dfs = []
    for i, f in enumerate(files):
        df = pd.read_parquet(f, columns=cols)
        dfs.append(df)
        if (i + 1) % 10 == 0:
            print(f"  Loaded {i+1}/{len(files)} files ({sum(len(d) for d in dfs):,} rows)")

    catalog = pd.concat(dfs, ignore_index=True)
    print(f"Total catalog: {len(catalog):,} objects")
    return catalog


def compute_snr_max(df):
    """Compute max SNR across b, r, z bands."""
    snr_cols = ['median_coadd_snr_b', 'median_coadd_snr_r', 'median_coadd_snr_z']
    available = [c for c in snr_cols if c in df.columns]
    if available:
        return df[available].max(axis=1)
    return pd.Series(0, index=df.index)


def recovery_rates(subset, thresholds=THRESHOLDS):
    """Compute fraction of subset above each anomaly score threshold."""
    n = len(subset)
    if n == 0:
        return {f"score_gt{t}": {"count": 0, "fraction": 0.0, "N": 0} for t in thresholds}
    result = {}
    for t in thresholds:
        above = (subset['anomaly_score'] > t).sum()
        result[f"score_gt{t}"] = {
            "count": int(above),
            "fraction": round(float(above / n), 6),
            "N": int(n)
        }
    return result


def score_statistics(subset):
    """Compute anomaly score statistics for a subset."""
    if len(subset) == 0:
        return {}
    scores = subset['anomaly_score']
    return {
        "mean": round(float(scores.mean()), 4),
        "median": round(float(scores.median()), 4),
        "std": round(float(scores.std()), 4),
        "min": round(float(scores.min()), 4),
        "max": round(float(scores.max()), 4),
        "p90": round(float(scores.quantile(0.9)), 4),
        "p95": round(float(scores.quantile(0.95)), 4),
        "p99": round(float(scores.quantile(0.99)), 4),
    }


def main():
    print("=" * 70)
    print("BigAE Empirical Injection/Recovery Test")
    print("=" * 70)
    print()

    # Load catalog
    catalog = load_full_catalog()
    catalog['snr_max'] = compute_snr_max(catalog)
    print()

    # =========================================================================
    # INJECTION CATEGORIES (objects we EXPECT to be anomalous)
    # =========================================================================
    print("=" * 70)
    print("INJECTION CATEGORIES — known unusual objects")
    print("=" * 70)
    print()

    injection_results = {}

    # Category 1: High-z QSOs (z > 3)
    cat1 = catalog[(catalog['spectype'] == 'QSO') & (catalog['z'] > 3)]
    injection_results['highz_qso_z_gt3'] = {
        "description": "QSOs with z > 3 (high-redshift, rare spectra)",
        "N": int(len(cat1)),
        "recovery": recovery_rates(cat1),
        "score_stats": score_statistics(cat1),
    }
    print(f"Category 1: High-z QSOs (z > 3)")
    print(f"  N = {len(cat1):,}")
    for t in THRESHOLDS:
        r = injection_results['highz_qso_z_gt3']['recovery'][f'score_gt{t}']
        print(f"  score > {t}: {r['count']:,} / {r['N']:,} = {r['fraction']*100:.2f}%")
    print()

    # Category 2: Very-high-z QSOs (z > 5)
    cat2 = catalog[(catalog['spectype'] == 'QSO') & (catalog['z'] > 5)]
    injection_results['vhighz_qso_z_gt5'] = {
        "description": "QSOs with z > 5 (very rare, extreme Lyman-alpha forest)",
        "N": int(len(cat2)),
        "recovery": recovery_rates(cat2),
        "score_stats": score_statistics(cat2),
    }
    print(f"Category 2: Very-high-z QSOs (z > 5)")
    print(f"  N = {len(cat2):,}")
    for t in THRESHOLDS:
        r = injection_results['vhighz_qso_z_gt5']['recovery'][f'score_gt{t}']
        print(f"  score > {t}: {r['count']:,} / {r['N']:,} = {r['fraction']*100:.2f}%")
    print()

    # Category 3: Pipeline-flagged but well-detected (ZWARN != 0, SNR > 2)
    cat3 = catalog[(catalog['zwarn'] != 0) & (catalog['snr_max'] > 2)]
    injection_results['zwarn_snr_gt2'] = {
        "description": "Pipeline-flagged objects (ZWARN != 0) with SNR > 2",
        "N": int(len(cat3)),
        "recovery": recovery_rates(cat3),
        "score_stats": score_statistics(cat3),
    }
    print(f"Category 3: Pipeline-flagged + well-detected (ZWARN!=0, SNR>2)")
    print(f"  N = {len(cat3):,}")
    for t in THRESHOLDS:
        r = injection_results['zwarn_snr_gt2']['recovery'][f'score_gt{t}']
        print(f"  score > {t}: {r['count']:,} / {r['N']:,} = {r['fraction']*100:.2f}%")
    print()

    # Category 4: Spectral mismatches — STAR with z > 0.01
    cat4 = catalog[(catalog['spectype'] == 'STAR') & (catalog['z'].abs() > 0.01)]
    injection_results['star_z_mismatch'] = {
        "description": "Objects classified STAR but |z| > 0.01 (spectral mismatch)",
        "N": int(len(cat4)),
        "recovery": recovery_rates(cat4),
        "score_stats": score_statistics(cat4),
    }
    print(f"Category 4: Spectral mismatches (STAR, |z| > 0.01)")
    print(f"  N = {len(cat4):,}")
    for t in THRESHOLDS:
        r = injection_results['star_z_mismatch']['recovery'][f'score_gt{t}']
        print(f"  score > {t}: {r['count']:,} / {r['N']:,} = {r['fraction']*100:.2f}%")
    print()

    # Category 5: White dwarfs (STAR, subtype WD)
    cat5 = catalog[(catalog['spectype'] == 'STAR') & (catalog['subtype'] == 'WD')]
    injection_results['white_dwarfs'] = {
        "description": "White dwarfs (STAR subtype WD — spectrally distinct)",
        "N": int(len(cat5)),
        "recovery": recovery_rates(cat5),
        "score_stats": score_statistics(cat5),
    }
    print(f"Category 5: White dwarfs (STAR, subtype WD)")
    print(f"  N = {len(cat5):,}")
    for t in THRESHOLDS:
        r = injection_results['white_dwarfs']['recovery'][f'score_gt{t}']
        print(f"  score > {t}: {r['count']:,} / {r['N']:,} = {r['fraction']*100:.2f}%")
    print()

    # Category 6: Low deltachi2 QSOs (ambiguous classification, deltachi2 < 10)
    cat6 = catalog[(catalog['spectype'] == 'QSO') & (catalog['deltachi2'] < 10)]
    injection_results['low_deltachi2_qso'] = {
        "description": "QSOs with deltachi2 < 10 (ambiguous pipeline classification)",
        "N": int(len(cat6)),
        "recovery": recovery_rates(cat6),
        "score_stats": score_statistics(cat6),
    }
    print(f"Category 6: Low deltachi2 QSOs (deltachi2 < 10)")
    print(f"  N = {len(cat6):,}")
    for t in THRESHOLDS:
        r = injection_results['low_deltachi2_qso']['recovery'][f'score_gt{t}']
        print(f"  score > {t}: {r['count']:,} / {r['N']:,} = {r['fraction']*100:.2f}%")
    print()

    # Category 7: High-z QSOs with good SNR (z > 3, SNR > 2) — stricter
    cat7 = catalog[(catalog['spectype'] == 'QSO') & (catalog['z'] > 3) & (catalog['snr_max'] > 2)]
    injection_results['highz_qso_good_snr'] = {
        "description": "High-z QSOs (z > 3) with SNR > 2 (real detections)",
        "N": int(len(cat7)),
        "recovery": recovery_rates(cat7),
        "score_stats": score_statistics(cat7),
    }
    print(f"Category 7: High-z QSOs + good SNR (z > 3, SNR > 2)")
    print(f"  N = {len(cat7):,}")
    for t in THRESHOLDS:
        r = injection_results['highz_qso_good_snr']['recovery'][f'score_gt{t}']
        print(f"  score > {t}: {r['count']:,} / {r['N']:,} = {r['fraction']*100:.2f}%")
    print()

    # Category 8: Emission-line galaxies at moderate z
    cat8 = catalog[
        (catalog['spectype'] == 'GALAXY') &
        (catalog['z'] > 1.0) & (catalog['z'] < 2.0) &
        (catalog['snr_max'] > 2)
    ]
    injection_results['highz_elg'] = {
        "description": "Galaxies at 1 < z < 2 with SNR > 2 (high-z ELGs)",
        "N": int(len(cat8)),
        "recovery": recovery_rates(cat8),
        "score_stats": score_statistics(cat8),
    }
    print(f"Category 8: High-z emission-line galaxies (1 < z < 2, SNR > 2)")
    print(f"  N = {len(cat8):,}")
    for t in THRESHOLDS:
        r = injection_results['highz_elg']['recovery'][f'score_gt{t}']
        print(f"  score > {t}: {r['count']:,} / {r['N']:,} = {r['fraction']*100:.2f}%")
    print()

    # =========================================================================
    # FALSE POSITIVE CONTROLS (objects that should NOT be anomalous)
    # =========================================================================
    print("=" * 70)
    print("FALSE POSITIVE CONTROLS — known normal objects")
    print("=" * 70)
    print()

    fp_results = {}

    # Control A: Normal low-z galaxies
    ctrlA = catalog[
        (catalog['spectype'] == 'GALAXY') &
        (catalog['z'] > 0.05) & (catalog['z'] < 0.5) &
        (catalog['zwarn'] == 0) &
        (catalog['snr_max'] > 5)
    ]
    fp_results['normal_lowz_galaxy'] = {
        "description": "Normal galaxies (0.05 < z < 0.5, ZWARN=0, SNR > 5)",
        "N": int(len(ctrlA)),
        "false_positive_rates": recovery_rates(ctrlA),  # "recovery" here = false positives
        "score_stats": score_statistics(ctrlA),
    }
    print(f"Control A: Normal low-z galaxies (0.05 < z < 0.5, ZWARN=0, SNR > 5)")
    print(f"  N = {len(ctrlA):,}")
    for t in THRESHOLDS:
        r = fp_results['normal_lowz_galaxy']['false_positive_rates'][f'score_gt{t}']
        print(f"  FALSE POSITIVE (score > {t}): {r['count']:,} / {r['N']:,} = {r['fraction']*100:.4f}%")
    print()

    # Control B: Normal stars
    ctrlB = catalog[
        (catalog['spectype'] == 'STAR') &
        (catalog['zwarn'] == 0) &
        (catalog['snr_max'] > 5) &
        (catalog['z'].abs() < 0.005)
    ]
    fp_results['normal_star'] = {
        "description": "Normal stars (ZWARN=0, SNR > 5, |z| < 0.005)",
        "N": int(len(ctrlB)),
        "false_positive_rates": recovery_rates(ctrlB),
        "score_stats": score_statistics(ctrlB),
    }
    print(f"Control B: Normal stars (ZWARN=0, SNR > 5, |z| < 0.005)")
    print(f"  N = {len(ctrlB):,}")
    for t in THRESHOLDS:
        r = fp_results['normal_star']['false_positive_rates'][f'score_gt{t}']
        print(f"  FALSE POSITIVE (score > {t}): {r['count']:,} / {r['N']:,} = {r['fraction']*100:.4f}%")
    print()

    # Control C: Normal mid-z QSOs
    ctrlC = catalog[
        (catalog['spectype'] == 'QSO') &
        (catalog['z'] > 0.5) & (catalog['z'] < 2.0) &
        (catalog['zwarn'] == 0) &
        (catalog['snr_max'] > 3)
    ]
    fp_results['normal_midz_qso'] = {
        "description": "Normal QSOs (0.5 < z < 2, ZWARN=0, SNR > 3)",
        "N": int(len(ctrlC)),
        "false_positive_rates": recovery_rates(ctrlC),
        "score_stats": score_statistics(ctrlC),
    }
    print(f"Control C: Normal mid-z QSOs (0.5 < z < 2, ZWARN=0, SNR > 3)")
    print(f"  N = {len(ctrlC):,}")
    for t in THRESHOLDS:
        r = fp_results['normal_midz_qso']['false_positive_rates'][f'score_gt{t}']
        print(f"  FALSE POSITIVE (score > {t}): {r['count']:,} / {r['N']:,} = {r['fraction']*100:.4f}%")
    print()

    # Control D: Full "normal" population (ZWARN=0, SNR > 3, any type)
    ctrlD = catalog[
        (catalog['zwarn'] == 0) &
        (catalog['snr_max'] > 3)
    ]
    fp_results['all_normal_snr3'] = {
        "description": "All objects with ZWARN=0, SNR > 3 (general population)",
        "N": int(len(ctrlD)),
        "false_positive_rates": recovery_rates(ctrlD),
        "score_stats": score_statistics(ctrlD),
    }
    print(f"Control D: General clean population (ZWARN=0, SNR > 3)")
    print(f"  N = {len(ctrlD):,}")
    for t in THRESHOLDS:
        r = fp_results['all_normal_snr3']['false_positive_rates'][f'score_gt{t}']
        print(f"  FALSE POSITIVE (score > {t}): {r['count']:,} / {r['N']:,} = {r['fraction']*100:.4f}%")
    print()

    # =========================================================================
    # GOLD ANOMALY CHARACTERIZATION
    # =========================================================================
    print("=" * 70)
    print("GOLD ANOMALY CATALOG ANALYSIS")
    print("=" * 70)
    print()

    gold = pd.read_parquet(GOLD_FILE)
    broad = pd.read_parquet(BROAD_FILE)

    gold_analysis = {
        "total_gold": int(len(gold)),
        "total_broad": int(len(broad)),
        "gold_by_spectype": gold['spectype'].value_counts().to_dict(),
        "gold_by_subtype": gold['subtype'].value_counts().to_dict(),
        "gold_score_stats": score_statistics(gold),
        "broad_score_stats": score_statistics(broad),
        "gold_z_stats": {
            "mean": round(float(gold['z'].mean()), 4),
            "median": round(float(gold['z'].median()), 4),
            "min": round(float(gold['z'].min()), 4),
            "max": round(float(gold['z'].max()), 4),
        },
        "known_rare_types_recovered": {},
    }

    # Check for known rare types in gold catalog
    rare_categories = {
        "high_z_qso_z_gt5": gold[(gold['spectype'] == 'QSO') & (gold['z'] > 5)],
        "high_z_qso_z_gt3": gold[(gold['spectype'] == 'QSO') & (gold['z'] > 3)],
        "white_dwarf": gold[(gold['spectype'] == 'STAR') & (gold['subtype'] == 'WD')],
        "M_star": gold[(gold['spectype'] == 'STAR') & (gold['subtype'] == 'M')],
        "anomalous_galaxy": gold[gold['spectype'] == 'GALAXY'],
        "zwarn_nonzero": gold[gold['zwarn'] != 0],
    }

    print(f"Gold anomalies: {len(gold)}")
    print(f"Broad anomalies: {len(broad)}")
    print(f"Gold by type: {gold['spectype'].value_counts().to_dict()}")
    print(f"Gold by subtype: {gold['subtype'].value_counts().to_dict()}")
    print()
    print("Known rare types recovered in gold catalog:")
    for name, subset in rare_categories.items():
        count = len(subset)
        gold_analysis['known_rare_types_recovered'][name] = int(count)
        print(f"  {name}: {count}")
    print()

    # =========================================================================
    # OVERALL ANOMALY SCORE DISTRIBUTION
    # =========================================================================
    print("=" * 70)
    print("OVERALL CATALOG SCORE DISTRIBUTION")
    print("=" * 70)
    print()

    total = len(catalog)
    overall_stats = {
        "total_objects": int(total),
        "score_stats": score_statistics(catalog),
        "above_thresholds": {},
    }

    for t in THRESHOLDS:
        n_above = (catalog['anomaly_score'] > t).sum()
        overall_stats['above_thresholds'][f'score_gt{t}'] = {
            "count": int(n_above),
            "fraction": round(float(n_above / total), 8),
        }
        print(f"  score > {t}: {n_above:,} / {total:,} = {n_above/total*100:.4f}%")

    print()

    # =========================================================================
    # DISCRIMINATION POWER: enrichment factor
    # =========================================================================
    print("=" * 70)
    print("DISCRIMINATION POWER (enrichment factors)")
    print("=" * 70)
    print()

    # How much more likely is each injection category to be flagged vs general population?
    baseline_gt3 = overall_stats['above_thresholds']['score_gt3']['fraction']
    baseline_gt5 = overall_stats['above_thresholds']['score_gt5']['fraction']

    enrichment = {}
    print(f"{'Category':<45} {'Recovery>3':>12} {'Enrichment':>12} {'Recovery>5':>12} {'Enrichment':>12}")
    print("-" * 95)

    for name, data in injection_results.items():
        r3 = data['recovery']['score_gt3']['fraction']
        r5 = data['recovery']['score_gt5']['fraction']
        e3 = r3 / baseline_gt3 if baseline_gt3 > 0 else 0
        e5 = r5 / baseline_gt5 if baseline_gt5 > 0 else 0
        enrichment[name] = {
            "recovery_gt3": round(r3, 6),
            "enrichment_gt3": round(e3, 2),
            "recovery_gt5": round(r5, 6),
            "enrichment_gt5": round(e5, 2),
        }
        print(f"  {name:<43} {r3*100:>10.2f}% {e3:>10.1f}x {r5*100:>10.2f}% {e5:>10.1f}x")

    print()
    print("  (Enrichment = category recovery rate / baseline catalog rate)")
    print()

    # =========================================================================
    # COMPLETENESS vs PURITY CURVE
    # =========================================================================
    print("=" * 70)
    print("COMPLETENESS vs PURITY AT VARIOUS THRESHOLDS")
    print("=" * 70)
    print()

    # Define "true anomalies" as high-z QSOs (z > 3) for this analysis
    is_known_anomalous = (
        ((catalog['spectype'] == 'QSO') & (catalog['z'] > 3)) |
        ((catalog['spectype'] == 'STAR') & (catalog['z'].abs() > 0.01)) |
        ((catalog['spectype'] == 'STAR') & (catalog['subtype'] == 'WD')) |
        ((catalog['zwarn'] != 0) & (catalog['snr_max'] > 2))
    )
    n_true_anomalous = is_known_anomalous.sum()
    print(f"Total 'known anomalous' objects: {n_true_anomalous:,}")
    print()

    completeness_purity = {}
    fine_thresholds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"{'Threshold':>10} {'Flagged':>12} {'True Pos':>12} {'Completeness':>14} {'Purity':>10}")
    print("-" * 60)

    for t in fine_thresholds:
        flagged = catalog['anomaly_score'] > t
        n_flagged = flagged.sum()
        true_pos = (flagged & is_known_anomalous).sum()
        completeness = true_pos / n_true_anomalous if n_true_anomalous > 0 else 0
        purity = true_pos / n_flagged if n_flagged > 0 else 0

        completeness_purity[f'threshold_{t}'] = {
            "threshold": t,
            "n_flagged": int(n_flagged),
            "true_positives": int(true_pos),
            "completeness": round(float(completeness), 6),
            "purity": round(float(purity), 6),
        }
        print(f"  {t:>8} {n_flagged:>12,} {true_pos:>12,} {completeness*100:>12.2f}% {purity*100:>8.2f}%")

    print()

    # =========================================================================
    # SAVE RESULTS
    # =========================================================================

    # Injection/recovery results
    ir_output = {
        "test_name": "BigAE Empirical Injection/Recovery Test",
        "date": datetime.now().isoformat(),
        "method": "Empirical completeness using known unusual objects in DESI DR1 catalog",
        "catalog_size": int(total),
        "injection_categories": injection_results,
        "enrichment_factors": enrichment,
        "completeness_vs_purity": completeness_purity,
        "overall_distribution": overall_stats,
        "gold_anomaly_analysis": gold_analysis,
    }

    ir_path = os.path.join(OUTPUT_DIR, "injection_recovery_results.json")
    with open(ir_path, 'w') as f:
        json.dump(ir_output, f, indent=2, default=str)
    print(f"Saved: {ir_path}")

    # False positive analysis
    fp_output = {
        "test_name": "BigAE False Positive Analysis",
        "date": datetime.now().isoformat(),
        "method": "False positive rates measured on known normal objects",
        "control_categories": fp_results,
        "baseline_catalog_rate": {
            "score_gt3": round(baseline_gt3, 8),
            "score_gt5": round(baseline_gt5, 8),
        }
    }

    fp_path = os.path.join(OUTPUT_DIR, "false_positive_analysis.json")
    with open(fp_path, 'w') as f:
        json.dump(fp_output, f, indent=2, default=str)
    print(f"Saved: {fp_path}")

    # =========================================================================
    # FINAL SUMMARY TABLE
    # =========================================================================
    print()
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    print()

    print("RECOVERY RATES (true positive rate for known anomalous objects):")
    print(f"{'Category':<45} {'N':>10} {'R(>3)':>10} {'R(>5)':>10} {'R(>7)':>10}")
    print("-" * 87)
    for name, data in injection_results.items():
        n = data['N']
        r3 = data['recovery']['score_gt3']['fraction'] * 100
        r5 = data['recovery']['score_gt5']['fraction'] * 100
        r7 = data['recovery']['score_gt7']['fraction'] * 100
        print(f"  {name:<43} {n:>10,} {r3:>9.2f}% {r5:>9.2f}% {r7:>9.2f}%")

    print()
    print("FALSE POSITIVE RATES (fraction of normal objects falsely flagged):")
    print(f"{'Category':<45} {'N':>10} {'FP(>3)':>10} {'FP(>5)':>10} {'FP(>7)':>10}")
    print("-" * 87)
    for name, data in fp_results.items():
        n = data['N']
        fp3 = data['false_positive_rates']['score_gt3']['fraction'] * 100
        fp5 = data['false_positive_rates']['score_gt5']['fraction'] * 100
        fp7 = data['false_positive_rates']['score_gt7']['fraction'] * 100
        print(f"  {name:<43} {n:>10,} {fp3:>9.4f}% {fp5:>9.4f}% {fp7:>9.4f}%")

    print()
    print("KEY METRICS:")
    # Best enrichment
    best_cat = max(enrichment.items(), key=lambda x: x[1]['enrichment_gt5'])
    print(f"  Highest enrichment (>5): {best_cat[0]} at {best_cat[1]['enrichment_gt5']}x")
    # Completeness at score > 3
    cp3 = completeness_purity['threshold_3']
    print(f"  Completeness at score > 3: {cp3['completeness']*100:.2f}%")
    print(f"  Purity at score > 3: {cp3['purity']*100:.2f}%")
    cp5 = completeness_purity['threshold_5']
    print(f"  Completeness at score > 5: {cp5['completeness']*100:.2f}%")
    print(f"  Purity at score > 5: {cp5['purity']*100:.2f}%")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
