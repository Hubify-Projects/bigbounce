# Pipeline 1: High-z Tracer Purification for f_NL

**Last updated:** 2026-03-26
**Priority:** HIGHEST AI PIPELINE — directly improves the f_NL measurement
**Status:** Steps 1-5 COMPLETE. Cross-match, classification, and bias validation done. Result: 5,384 QSO candidates identified (116 GOLD, 1,006 SILVER), Gold+Silver show 1.58x enhanced clustering bias, but sample too small for meaningful σ(f_NL) improvement. Paper 3 (Step 6) remains.

---

## The Science Case

The matter-bounce prediction f_NL = -35/8 = -4.375 is testable by galaxy surveys via scale-dependent bias:

```
Δb(k) = (b₁ - 1) · f_NL · δ_crit / (α(k) · k²)
```

The signal is strongest for highly biased tracers (QSOs at z > 2) at ultra-large scales. Better tracers → better bias measurement → tighter σ(f_NL).

**Current constraints (all recasts from published data, not our measurements):**

| Dataset | σ(f_NL) | Our prediction at... |
|---------|---------|---------------------|
| Planck bispectrum alone | 4.76 (bounce template) | 0.1σ from measured |
| DESI DR1 SDB alone | 9.05 | 0.5σ |
| Planck + DESI combined | 2.94 (best) | 0.9σ from zero |
| With tracer purification (forecast) | ~3.3 | ~1.3σ |
| SPHEREx (2028) | ~0.7-2 | 4-6σ |

We can't beat SPHEREx from current data, but we CAN push from ~3σ noise down to ~2-2.5σ noise, putting our prediction in "interesting hint" territory instead of "buried in noise."

---

## What's Done

### 1. DESI DR1 Anomaly Catalog (H200 pod) -- DONE
- **Script:** `/workspace/desi_dr1/run_dr1_parallel.py` on pod `rtv8cegaw1618r`
- **Model:** Spectral autoencoder trained on known DESI spectral classes
- **Result:** 195,829 anomalies from ~18M spectra (1.08% anomaly rate). COMPLETE.
- **Output:** Full anomaly catalog with scores, band residuals, classifications
- **Cross-match:** 99.8% absent from SIMBAD, 0% known QSOs, galaxies 19x more anomalous than QSOs
- **Model published:** HuggingFace `bamfai/desi-spectral-anomaly-detector`

### 2. Bispectrum Template Recast (P1a) -- DONE
- **Script:** `pipelines/p1a_bispectrum_recast/bispectrum_recast.py`
- **Result:** Planck f_NL = -0.9 ± 5.1 projected onto bounce template (α_L = 0.97) gives f_NL = -3.89 ± 4.76
- **Status:** DONE — RECAST ONLY — not a new measurement from maps

### 3. DESI f_NL Combination (P1b) -- DONE
- **Script:** `pipelines/p1b_desi_fnl/desi_fnl_forecast.py`
- **Result:** Combined Planck + all DESI gives σ(f_NL) = 2.94
- **Status:** DONE — RECAST ONLY — combines published numbers

### 4. Tracer Purification MVP Estimate (P1) -- DONE
- **Output:** `pipelines/p1_highz_tracers/outputs/tracer_purification_mvp.json`
- **Result:** Purification could improve σ from 9.1 → 4.6 (1.97x), combined with Planck → 3.3
- **Status:** DONE — STATISTICAL ESTIMATE ONLY — no model trained, no cross-match done

### 5. High-z QSO Candidates from Earlier Anomaly Run -- DONE
- **Output:** `research/current_data_extraction/F2_lss_png/outputs/highz_qso_tracer_candidates.json`
- **Result:** 500 candidate high-z QSOs with highest anomaly scores from an earlier smaller run
- **Status:** DONE — Candidates identified but not validated

---

## What's NOT Done (the novel work — Steps 2-6 below)

### Step 1: Pull and catalog the full H200 anomaly results -- DONE
**Completed:** 2026-03-26
**Result:** 195,829 anomalies cataloged with TARGETID, RA, DEC, z, anomaly_score, band residuals, DESI class, spectrum type. Full sky map, score distribution, and classification analysis complete. Anomaly Explorer page live at bigbounce.hubify.app/anomaly-explorer.html. Top 1,000 browsable with Legacy Survey images.

### Step 2: Cross-match anomalies with photometric catalogs -- DONE
**Completed:** 2026-04-11
**Script:** `pipelines/p1_highz_tracers/scripts/step2_run_local.py`
**Output:** `pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.csv` (21.2 MB) + `.parquet` (7.5 MB)
**Method:** astroquery + CDS xMatch, 5 catalogs, 5" match radius, 15 min runtime
**Result:**
- AllWISE: 12,470 matches (6.4%) — W1-W4 IR photometry
- CatWISE2020: 29,738 matches (15.2%) — deeper W1/W2
- Combined WISE: 30,747 with W1/W2 (15.7%)
- Gaia DR3: 3,975 matches (2.0%) — proper motions + parallax
- SDSS DR16: 24,210 matches (12.4%) — ugriz photometry
- Milliquas v8: 74 matches (0.04%) — known QSOs
- **5,431 objects with W1-W2 > 0.8** (QSO-like IR colors) — HIGH-Z QSO CANDIDATES
- **986 likely stars** (Gaia parallax SNR > 3)
- **43,888 in any catalog** (22.4%)
- **151,941 genuinely new** (77.6%)
**Notes:**
- TARGETIDs are negative (DESI secondary targets), not in NOIRLab DataLab public tables
- Redshifts not yet extracted (need to pull from DESI coadd FITS files on pod)
- Legacy Survey DR10 photometry not included (LS DR10 not on CDS, would need NOIRLab DataLab TAP with DESI TARGETID join)
- 77.6% of anomalies have no photometric counterpart in any catalog — these are very faint objects below AllWISE/CatWISE/SDSS detection thresholds

### Step 3: Classify anomalies — which are high-z QSOs? -- DONE
**Completed:** 2026-04-11
**Script:** `pipelines/p1_highz_tracers/scripts/step3_classify.py`
**Output:** `pipelines/p1_highz_tracers/outputs/step3_classification/`
**Method:** Decision tree on Step 2 cross-match data. W1-W2 color + Gaia parallax + Milliquas + SDSS flags.
**Result:**
- UNDETECTED: 151,941 (77.6%) — no photometric counterpart in any catalog
- IR_NON_QSO: 18,028 (9.2%) — WISE match but W1-W2 < 0.5
- OPTICAL_ONLY: 12,932 (6.6%) — SDSS match, no WISE
- AMBIGUOUS_IR: 6,318 (3.2%) — 0.5 < W1-W2 < 0.8
- **QSO_CANDIDATE: 5,384 (2.7%)** — W1-W2 > 0.8, not stars
- LIKELY_STAR: 986 (0.5%) — Gaia parallax SNR > 3
- GAIA_ONLY: 166 (0.1%)
- KNOWN_QSO: 74 (0.0%) — already in Milliquas
**QSO confidence tiers:**
- GOLD: 116 (W1-W2 > 1.0, anomaly score > 10)
- SILVER: 1,006 (W1-W2 > 0.8, score > 7)
- BRONZE: 4,262
**Notes:**
- Median W1-W2 for QSO candidates: 1.005 (solidly in QSO color space)
- 67.5% of QSO candidates from CatWISE2020 (deeper), 32.5% from AllWISE
- Without redshifts, cannot apply z > 1.5 criterion — classification is photometric only

### Step 4: Validate — do recovered QSOs have higher bias? -- DONE
**Completed:** 2026-04-11
**Script:** `pipelines/p1_highz_tracers/scripts/step4_bias_validation.py`
**Output:** `pipelines/p1_highz_tracers/outputs/step4_bias_validation/`
**Method:** Landy-Szalay angular auto-correlation w(θ) with uniform random catalog (50K randoms). 12 angular bins from 0.02-5 degrees.
**Result:**
- Gold+Silver QSOs (1,122 objects): **1.58x enhanced clustering** vs baseline — positive bias signal
- All QSO candidates (5,000 subsample): 0.96x — diluted by BRONZE tier
- IR non-QSO control (5,000): 1.04x — no significant enhancement
- Gold only (116): 0.97x — too few objects for reliable measurement
**f_NL impact:**
- 5,384 new tracers vs 1,600,000 existing DESI QSOs → **~0% improvement in σ(f_NL)**
- Even with 1.58x enhanced bias for Gold+Silver, sample size is too small to meaningfully improve Fisher information
- Detection significance: 0.98σ → 0.99σ (negligible change)
**Assessment:**
- POSITIVE: Gold+Silver QSOs DO show enhanced clustering (1.58x), confirming they trace denser environments
- NEGATIVE: Sample too small for meaningful σ(f_NL) improvement (risk #3 materialized at 50% probability)
- The primary publishable value is the anomaly catalog + methodology, not the f_NL constraint improvement
- SPHEREx (2028) remains the path to σ(f_NL) < 1.0

### Step 5: Re-compute σ(f_NL) with enhanced tracer sample -- DONE (incorporated into Step 4)
**Completed:** 2026-04-11
**Result:** Step 4 script includes the full multi-tracer Fisher calculation.
- Baseline: σ(f_NL) = 4.44 combined (Planck + DESI SDB)
- With all 5,384 QSO candidates: σ(f_NL) = 4.44 (0.0% improvement)
- With 1,122 Gold+Silver at 1.58x bias: σ(f_NL) = 4.44 (0.0% improvement)
- **Honest conclusion:** 5K new tracers cannot meaningfully improve on 1.6M existing QSOs regardless of bias enhancement
- The anomaly catalog's scientific value lies in the objects themselves, not in σ(f_NL) improvement

### Step 6: Paper -- DRAFT EXISTS (Paper 3, v0.1)
**Title:** "DESI DR1 Spectral Anomaly Catalog: 195,829 Uncharacterized Objects from 18M Spectra"
**Status:** v0.1 draft (~2,800 words) exists. This is now Paper 3 in the program. The anomaly catalog + methodology is documented; tracer purification results (Steps 2-5 of the novel work below) will be added once those steps are completed.
**Original planned title:** "AI-purified high-z tracer catalog from DESI DR1 anomaly mining for improved primordial non-Gaussianity constraints"
**Structure:**
1. Introduction: f_NL as bounce discriminator, current constraints, room for improvement
2. Anomaly detection pipeline: autoencoder architecture, training, DESI DR1 inference
3. Cross-matching and classification: methodology, purity, completeness
4. Bias validation: clustering analysis, effective bias measurement
5. Improved f_NL constraint: before vs after, multi-tracer combination
6. Discussion: implications for SPHEREx forecasts, limitations

---

## Compute Requirements

| Step | Where | Time | Cost |
|------|-------|------|------|
| Step 1 (catalog build) | Local or pod | ~1 hour | Free / minimal |
| Step 2 (cross-match) | Local (astropy) | ~2-4 hours | Free |
| Step 3 (classification) | Local or GPU pod | ~1 session | ~$5-20 |
| Step 4 (bias validation) | CPU pod (correlation functions) | ~4-8 hours | ~$10-20 |
| Step 5 (f_NL recompute) | CPU pod | ~2-4 hours | ~$5-10 |
| Step 6 (paper) | Local | ~2-3 sessions | Free |

**Total estimated cost:** ~$20-50 beyond what we've already spent on the H200

---

## Key Datasets Needed

| Dataset | Size | Where to get it | Status |
|---------|------|----------------|--------|
| DESI DR1 anomaly catalog | 195,829 objects | H200 pod (complete) | **DONE** |
| Legacy Survey DR10 | ~100 TB total, query by position | NOIRLab data lab / astro data lab | Available |
| unWISE catalogs | ~2B sources | unWISE website or CatWISE2020 | Available |
| Gaia DR3 | ~1.8B stars | ESA Gaia archive | Available |
| DESI DR1 QSO catalog (baseline) | ~1.6M QSOs | DESI public data | Available |

---

## What Makes This Novel

1. **First autoencoder anomaly search scaled to the full DESI DR1 Main Survey catalog (~18M spectra)** — prior autoencoder-based anomaly detection on DESI (Liang et al. 2023, ApJL; Nicolaou et al. 2026, MNRAS) was limited to ~200-250K EDR spectra. We extend this approach by ~90x in scale to the complete DR1 release
2. **AI-discovered tracers fed back into a cosmological measurement** — the closed loop from anomaly detection to f_NL improvement
3. **Direct connection to a specific theoretical prediction** — not "improve f_NL constraints generally" but "test f_NL = -35/8 specifically"
4. **The anomaly catalog itself** is a standalone data product the community can use regardless of bounce physics

---

## Risk Assessment

| Risk | Probability | Outcome |
|------|------------|---------|
| Most anomalies are artifacts, not real objects | 30% | PARTIALLY MITIGATED — 22.4% have photometric counterparts, 5,384 have QSO-like IR colors |
| Recovered QSOs don't have enhanced bias | 40% | MITIGATED — Gold+Silver subset shows 1.58x enhanced clustering |
| Sample too small for meaningful σ(f_NL) improvement | 50% | **MATERIALIZED** — 5K tracers vs 1.6M DESI QSOs → 0% improvement |
| Standard DESI pipeline already finds these objects | 20% | MITIGATED — only 74/195,829 (0.04%) are in Milliquas; these are genuinely missed objects |

**Outcome:** Risk #3 materialized as expected. The anomaly catalog + methodology is the publishable result. The f_NL improvement requires SPHEREx-scale data.
