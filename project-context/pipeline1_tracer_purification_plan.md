# Pipeline 1: High-z Tracer Purification for f_NL

**Last updated:** 2026-03-25
**Priority:** HIGHEST AI PIPELINE — directly improves the f_NL measurement
**Status:** Anomaly catalog 71% complete on H200. Cross-matching and purification NOT started.

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

### 1. DESI DR1 Anomaly Catalog (H200 pod — finishing now)
- **Script:** `/workspace/desi_dr1/run_dr1_parallel.py` on pod `rtv8cegaw1618r`
- **Model:** Spectral autoencoder trained on known DESI spectral classes
- **Progress:** 12.8M/~18M spectra processed (71%), 119,667 anomalies found (0.94%)
- **Output:** Anomaly scores + reconstructions for every DESI DR1 spectrum
- **ETA:** ~1-2 hours from 2026-03-25 22:30 UTC
- **Checkpoint:** `/workspace/desi_dr1/outputs/dr1_checkpoint.json`

### 2. Bispectrum Template Recast (P1a — complete)
- **Script:** `pipelines/p1a_bispectrum_recast/bispectrum_recast.py`
- **Result:** Planck f_NL = -0.9 ± 5.1 projected onto bounce template (α_L = 0.97) gives f_NL = -3.89 ± 4.76
- **Status:** RECAST ONLY — not a new measurement from maps

### 3. DESI f_NL Combination (P1b — complete)
- **Script:** `pipelines/p1b_desi_fnl/desi_fnl_forecast.py`
- **Result:** Combined Planck + all DESI gives σ(f_NL) = 2.94
- **Status:** RECAST ONLY — combines published numbers

### 4. Tracer Purification MVP Estimate (P1 — complete)
- **Output:** `pipelines/p1_highz_tracers/outputs/tracer_purification_mvp.json`
- **Result:** Purification could improve σ from 9.1 → 4.6 (1.97x), combined with Planck → 3.3
- **Status:** STATISTICAL ESTIMATE ONLY — no model trained, no cross-match done

### 5. High-z QSO Candidates from Earlier Anomaly Run
- **Output:** `research/current_data_extraction/F2_lss_png/outputs/highz_qso_tracer_candidates.json`
- **Result:** 500 candidate high-z QSOs with highest anomaly scores from an earlier smaller run
- **Status:** Candidates identified but not validated

---

## What's NOT Done (the novel work)

### Step 1: Pull and catalog the full H200 anomaly results
**When:** Immediately after H200 finishes (~1-2 hours)
**What:**
- Pull all anomaly scores and reconstructions from the pod
- Build a structured anomaly catalog with columns: TARGETID, RA, DEC, z, anomaly_score, reconstruction_error, DESI_class, spectrum_type
- Basic statistics: score distribution, spatial distribution, redshift distribution
- Save to `pipelines/p1_highz_tracers/outputs/desi_dr1_anomaly_catalog.parquet`

### Step 2: Cross-match anomalies with Legacy Survey + unWISE
**When:** After Step 1
**What:**
- Match 119K anomalies against Legacy Survey DR10 (g/r/z imaging) by position
- Match against unWISE (W1/W2 IR photometry)
- Extract: optical colors (g-r, r-z), IR colors (W1-W2), morphology flags, proper motions (from Gaia DR3 if available)
- This adds photometric information to the spectroscopic anomalies
- **Tools:** astropy coordinates + catalog cross-matching, or TOPCAT if interactive
- Save to `pipelines/p1_highz_tracers/outputs/anomaly_crossmatch.parquet`

### Step 3: Classify anomalies — which are high-z QSOs?
**When:** After Step 2
**What:**
- Use photometric colors + spectral features to separate:
  - **Recovered QSOs** (high-z, high-bias, useful for f_NL): W1-W2 > 0.8, point-source morphology, z > 1.5
  - **Unusual AGN** (potentially interesting but different science): broad lines, unusual continuum
  - **Stellar contaminants** (remove): proper motion > 0, stellar colors
  - **Pipeline artifacts** (remove): instrumental issues, bad sky subtraction
  - **Genuinely novel objects** (flag for follow-up): nothing matches any template
- Can use a simple decision tree first, then train a proper classifier if sample is large enough
- **Key metric:** How many genuine high-z QSOs did the standard DESI pipeline miss?
- Save classifications to `pipelines/p1_highz_tracers/outputs/anomaly_classifications.parquet`

### Step 4: Validate — do recovered QSOs have higher bias?
**When:** After Step 3
**What:**
- Compute the angular auto-correlation function w(θ) for the recovered QSOs
- Compare with the standard DESI QSO sample's w(θ)
- If recovered QSOs cluster more strongly → they have higher bias → they're MORE useful for f_NL
- Cross-correlate with known large-scale structure (DESI LRGs as reference)
- **This is the critical validation:** if recovered QSOs don't have enhanced bias, the improvement is marginal
- Save to `pipelines/p1_highz_tracers/outputs/bias_validation.json`

### Step 5: Re-compute σ(f_NL) with enhanced tracer sample
**When:** After Step 4 (only if validation passes)
**What:**
- Add recovered high-z QSOs to the DESI QSO sample
- Re-compute the scale-dependent bias signal using the multi-tracer technique
- Quantify the actual σ(f_NL) improvement
- Compare: standard pipeline σ vs our enhanced σ
- **This is the publishable measurement** (if the improvement is real)
- Save to `pipelines/p1_highz_tracers/outputs/enhanced_fnl_constraint.json`

### Step 6: Paper
**Title:** "AI-purified high-z tracer catalog from DESI DR1 anomaly mining for improved primordial non-Gaussianity constraints"
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
| DESI DR1 anomaly catalog | ~119K objects | H200 pod (finishing now) | In progress |
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

| Risk | Probability | Mitigation |
|------|------------|------------|
| Most anomalies are artifacts, not real objects | 30% | Visual inspection of top-scored anomalies; compare with known artifact patterns |
| Recovered QSOs don't have enhanced bias | 40% | Still publishable as anomaly catalog + null result on bias improvement |
| Sample too small for meaningful σ(f_NL) improvement | 50% | Focus on the catalog paper, defer the f_NL improvement to SPHEREx era |
| Standard DESI pipeline already finds these objects | 20% | Cross-check against DESI's internal QSO catalog; focus on objects they MISSED |

**Even in the worst case** (anomalies are mostly artifacts), the anomaly catalog itself is publishable as a methodology paper.
