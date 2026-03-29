# Spectral Line Identification Report -- Gold Anomaly Catalog

## Overview

Analysis of 83 primary gold anomalies (from JSON catalog) and 120 extended gold anomalies (from CSV catalog), identifying the rest-frame spectral features driving each object's anomaly score.

**Method:** For each object, compute rest-frame wavelength as `lambda_rest = lambda_obs / (1 + z)`, then match against a library of 40+ known emission/absorption lines with tolerances of 50-80 Angstroms.

---

## 83-Object Primary Catalog Results

### Spectral Type Distribution
| Type | Count | Fraction |
|------|-------|----------|
| QSO | 69 | 83% |
| GALAXY | 11 | 13% |
| STAR | 3 | 4% |

### Rest-Frame Wavelength Categories
| Region | Lambda Range | Count | Fraction | Interpretation |
|--------|-------------|-------|----------|----------------|
| Sub-Lyman limit | < 912 A | 6 | 7.2% | Ionizing continuum / possible z errors |
| Lyman forest | 912-1216 A | 33 | 39.8% | Ly-beta/gamma, IGM absorption features |
| UV emission | 1216-1900 A | 30 | 36.1% | Ly-alpha, NV, SiIV, CIV |
| UV iron | 1900-3000 A | 4 | 4.8% | FeII pseudo-continuum, MgII |
| Optical | 3000-7000 A | 6 | 7.2% | Balmer, [OIII], CaII |
| NIR | > 7000 A | 4 | 4.8% | CaII triplet, molecular bands |

### Line Identification (80A tolerance)
| Line | Count | Fraction | Avg Score |
|------|-------|----------|-----------|
| Ly-beta (1026 A) | 26 | 31.3% | 4.14 |
| Ly-alpha (1216 A) | 16 | 19.3% | 3.58 |
| **UNMATCHED** | **15** | **18.1%** | **4.41** |
| NV (1240 A) | 12 | 14.5% | 3.69 |
| SiIV (1397 A) | 7 | 8.4% | 3.67 |
| CIV (1549 A) | 2 | 2.4% | 5.47 |
| H-gamma (4340 A) | 2 | 2.4% | 4.20 |
| H-alpha (6563 A) | 2 | 2.4% | 4.24 |
| CaI (4227 A) | 1 | 1.2% | 3.18 |

### Key Finding: Ly-alpha Velocity Offsets
16 objects match Ly-alpha within 50A. Velocity offset distribution:
- Mean: -1 km/s (centered on systemic)
- Median: +136 km/s (slight redshift)
- Std dev: 1925 km/s
- Range: -4399 to +2924 km/s
- 9 redshifted, 7 blueshifted
- The slight redshift bias is consistent with IGM absorption preferentially removing blue-side Ly-alpha flux

---

## 6 Sub-Lyman-Limit Objects (Lyman Continuum Leaker Candidates)

These are the most physically interesting: the autoencoder residual peaks at a rest-frame wavelength BELOW 912A, where essentially no flux should escape in a normal high-z QSO due to hydrogen opacity.

| targetid | z | rest_wave | Score | Interpretation |
|----------|---|-----------|-------|----------------|
| 39628080880291871 | 5.990 | 520 A | 3.94 | EXTREME: ionizing continuum anomaly or z error |
| 39628203496572448 | 5.955 | 524 A | 3.77 | EXTREME: ionizing continuum anomaly or z error |
| 39627789988529182 | 6.009 | 625 A | 3.65 | Deep sub-LL: LyC leaker candidate |
| 39627663148586278 | 5.776 | 640 A | 3.31 | Deep sub-LL: LyC leaker candidate |
| 39633152393611253 | 6.230 | 800 A | 3.62 | Near Lyman limit: LyC leaker or GP trough |
| 39633191367084936 | 6.196 | 807 A | 5.30 | Near Lyman limit: LyC leaker or GP trough |

**Possible explanations:**
1. **Lyman continuum leakers** -- genuinely ionizing radiation escaping, extremely rare at z > 5
2. **Redshift errors** -- DESI pipeline assigned wrong z; true z may be lower
3. **Unusual IGM transmission** -- line-of-sight with anomalously low neutral hydrogen
4. **Reconstruction artifact** -- autoencoder has anomalous residual in a region with no signal (low SNR = high residual)

---

## 4 UV Iron Region Galaxies (z ~ 1.6)

A cluster of 4 galaxies at z ~ 1.63 with rest-frame anomalies near 2100-2200 A:

| targetid | z | rest_wave | Score |
|----------|---|-----------|-------|
| 39633127475250050 | 1.636 | 2197 A | 5.30 |
| 39633169590258797 | 1.637 | 2197 A | 5.21 |
| 39633441347600823 | 1.628 | 2126 A | 4.59 |
| 39627696593961086 | 1.670 | 2174 A | 4.55 |

This wavelength range (2100-2200 A) falls in the UV iron pseudo-continuum between the AlIII (1857 A) and FeII UV1 (2344 A) lines. These could be:
- Unusual FeII emission strength
- BAL features in misclassified AGN
- Rare UV spectral breaks

---

## 120-Object Extended Catalog

The extended catalog has a very different composition (70 galaxies, 31 QSOs, 19 stars vs. the QSO-dominated 83 catalog).

### Match Rate (50A extended tolerance)
- Matched: 68/120 (56.7%)
- Unmatched: 52/120 (43.3%)

The higher unmatched fraction reflects the galaxy-dominated sample where many anomalies fall in the UV iron continuum region without a clean line match.

### Rest-Frame Category Breakdown
| Region | Count | Fraction |
|--------|-------|----------|
| Optical (3000-7000 A) | 44 | 36.7% |
| UV iron (1900-3000 A) | 35 | 29.2% |
| UV emission (1216-1900 A) | 16 | 13.3% |
| Lyman forest (912-1216 A) | 16 | 13.3% |
| Sub-Lyman limit (< 912 A) | 6 | 5.0% |
| NIR (> 7000 A) | 3 | 2.5% |

---

## Top 10 Priority Objects for Follow-up

Ranked by composite priority score (anomaly score, boosted for unmatched, sub-Lyman, and high-z).

| Rank | targetid | z | Type | rest_wave | Interpretation |
|------|----------|---|------|-----------|----------------|
| 1 | 39633010877796273 | 5.267 | QSO | 1489 A | UV desert -- no standard line |
| 2 | 39633191367084936 | 6.196 | QSO | 807 A | Near Lyman limit -- LyC leaker? |
| 3 | 39637210621808589 | ~0 | STAR | 8820 A | Unidentified NIR feature |
| 4 | 39628080880291871 | 5.990 | QSO | 520 A | EXTREME sub-LL |
| 5 | 39628203496572448 | 5.955 | QSO | 524 A | EXTREME sub-LL |
| 6 | 39627789988529182 | 6.009 | QSO | 625 A | Deep sub-LL |
| 7 | 39633152393611253 | 6.230 | QSO | 800 A | Deep sub-LL |
| 8 | 39633127475250050 | 1.636 | GALAXY | 2197 A | UV FeII anomaly |
| 9 | 39633169590258797 | 1.637 | GALAXY | 2197 A | UV FeII anomaly |
| 10 | 39627663148586278 | 5.776 | QSO | 640 A | Deep sub-LL |

---

## Summary Statistics

| Metric | 83 Catalog | 120 Catalog |
|--------|-----------|-------------|
| Total objects | 83 | 120 |
| Matched to known line | 68 (82%) | 68 (57%) |
| Unmatched | 15 (18%) | 52 (43%) |
| Sub-Lyman limit | 6 | 6 |
| Dominant feature | Ly-beta (31%) | (diverse) |
| Mean anomaly score (unmatched) | 4.41 | 5.85 |
| Mean anomaly score (matched) | 3.70 | (varies) |

**Key insight:** Unmatched objects have systematically HIGHER anomaly scores (4.41 vs 3.70 for the 83 catalog), confirming the autoencoder is flagging genuinely unusual spectral features, not just known emission lines at unusual strength.

---

## Output Files

| File | Description |
|------|-------------|
| `line_id_83_gold.csv` | Full line identification for 83 primary anomalies |
| `line_id_120_gold.csv` | Full line identification for 120 extended anomalies |
| `detailed_line_analysis.csv` | Extended analysis with categories and interpretations (83) |
| `detailed_line_analysis_120.csv` | Extended analysis for 120 catalog |
| `unmatched_objects.csv` | All unmatched objects from 120 catalog |
| `priority_followup.csv` | Top 30 priority objects for spectroscopic follow-up |
| `line_id_statistics.json` | Aggregate statistics |
| `deep_analysis_summary.json` | Category-level summary |
| `identify_lines.py` | Primary analysis script |
| `deep_analysis.py` | Deep analysis script |
