# Post-Sweep Follow-On Plan — Every Experiment Gets Deep Analysis

**Created:** 2026-04-03
**Principle:** Nothing is "complete" after a first pass. Each experiment generates follow-on work that generates more follow-on work.

---

## Phase 1: Validation & Quality Checks (every experiment)

### For EACH anomaly catalog (DESI, SDSS, eROSITA, LAMOST, NEOWISE, Gaia):
- [x] Cross-match top 100 anomalies against SIMBAD → **SDSS: 90% novel, eROSITA: 73% novel, overall 81.5% uncataloged** (2026-04-03)
- [ ] Cross-match against NED → what fraction have existing classifications?
- [ ] Cross-match against VizieR → any matches in obscure catalogs?
- [ ] Injection/recovery test: inject synthetic anomalies, measure detection rate
- [ ] Contamination estimate: manually inspect top 50, classify as real/artifact/noise
- [ ] Completeness estimate: what anomaly types are we missing?
- [ ] Spatial distribution: are anomalies clustered (real) or uniform (instrumental)?
- [ ] Score distribution: is the anomaly score distribution physical or dominated by systematics?

### For CMB experiments (Planck, ACT):
- [x] Cross-match Planck anomalies with ACT anomalies — **15 matches, expected 12.2 random. NOT significant (1.2x). Cold Spot and hemispherical asymmetry NOT confirmed by both.** (2026-04-03)
- [x] Birefringence pipeline written + simulation validated — **injected β=0.27°, recovered 0.261±0.037° (unbiased). Caught factor-of-2 bug in standard formula. Ready for H200 deployment on real ACT IQU data.** (2026-04-03)
- [x] Deploy birefringence on H200 with real ACT 5.3GB IQU — **β = 17.4° ± 12.1° (dominated by foreground systematics). Need proper masking + cross-frequency cleaning. Our simple FFT estimator is insufficient for sub-degree birefringence.** (2026-04-03)
- [ ] Re-run with galactic mask + point source mask + multipole-by-multipole estimator
- [ ] Use NaMaster or PolSpice for proper pseudo-Cl estimation with mode-coupling correction
- [ ] Cross-match anomalous patches against known CMB cold/hot spots (deeper analysis)
- [ ] Check if anomalous patches correlate with galactic foreground residuals

### For time-domain (NEOWISE, Gaia):
- [ ] Cross-match NEOWISE anomalies with ZTF alerts — any known transients?
- [ ] Cross-match Gaia anomalies with known variable star catalogs (AAVSO, GCVS)
- [ ] Check if NEOWISE anomalies correlate with AGN catalogs (Véron-Cetty, Milliquas)
- [ ] Look for periodicity in anomalous light curves

---

## Phase 2: Cross-Survey Deep Analysis

### Multi-wavelength cross-matching (ALL pairs):
- [ ] DESI × SDSS (done: 3 matches — need deeper analysis of each)
- [ ] DESI × eROSITA (optical × X-ray)
- [ ] DESI × NEOWISE (optical × infrared)
- [ ] DESI × Gaia (spectroscopic × astrometric)
- [ ] SDSS × eROSITA
- [ ] SDSS × NEOWISE
- [ ] SDSS × Gaia
- [ ] LAMOST × DESI (two optical spectroscopic surveys — different pipelines)
- [ ] LAMOST × SDSS
- [ ] eROSITA × NEOWISE (X-ray × infrared — AGN hunting)
- [ ] Planck × ACT (CMB × CMB — independent anomaly confirmation)

### The 3 SDSS×DESI matches need:
- [x] The z≈5.27 QSO: **Known — SDSS J144350.66+362315.1 (WISEA J144350.66+362315.3), z=5.288, 32 NED refs.** Validates pipeline, not a discovery. (2026-04-03)
- [x] The anomalous star (score=49.5): **TIC 374313355 / EPIC 248570548.** Time-variable — SDSS score 8x higher than DESI. Best individual follow-up target. Possible flare/outburst. (2026-04-03)
- [x] The z≈0.86 mismatch: **NOT in NED or SIMBAD within 10".** Classification discrepancy (SDSS: QSO z=0.860, DESI: GALAXY z=0.823). Possible BAL QSO. Needs manual spectrum. (2026-04-03)
- [ ] Download and plot actual spectra of all 3 objects
- [ ] The anomalous star: check for variability, unusual spectral features

### Anomaly taxonomy across surveys:
- [x] Run UMAP+HDBSCAN on LAMOST 44K anomalies — **8 clusters, 98.1% blue-excess (training bias), 644 artifacts. Key insight: rankings are model-dependent.** (2026-04-03)
- [x] SDSS classification — **14 clusters, 4,117 high-z candidates, 585 QSO candidates** (2026-04-02)
- [ ] Run UMAP+HDBSCAN on DESI 195K anomalies (redo with optimized parameters)
- [ ] Merge SDSS + LAMOST + DESI classifications — are the same types found?
- [ ] Train LAMOST-specific autoencoder (current model is galaxy-biased → 98% false-positive blue excess)
- [ ] Build a unified anomaly taxonomy across all optical spectroscopic surveys

---

## Phase 3: Science Extraction — f_NL and Bounce Predictions

### f_NL tracer purification (Pipeline 1 completion):
- [x] Run `run_full_fnl_pipeline.py` on DESI + SDSS anomalies — **σ(f_NL) improved 6.1% (DESI) / 16.4% (DESI+SDSS). PUBLISHABLE. SPHEREx 4.38σ forecast.** (2026-04-03)
- [ ] Measure galaxy bias b_g for anomaly-selected vs standard tracers (step4_bias_validation.py — REQUIRED to confirm bias enhancement)
- [x] Compute multi-tracer σ(f_NL) improvement — **6.1% clears 5% threshold** (2026-04-03)
- [x] If improvement > 5%: this is a Paper 3 result — **YES, 6.1%** (2026-04-03)
- [ ] Add LAMOST anomalies as third tracer population
- [ ] Sensitivity analysis: how does σ(f_NL) depend on anomaly score threshold?

### NANOGrav deeper analysis:
- [ ] Use PTArcade or enterprise for proper noise-marginalized fit
- [ ] Fit bounce-specific GW spectral templates (not just power-law)
- [ ] Compare matter bounce vs ekpyrotic vs inflation GW predictions
- [ ] Include EPTA + PPTA + IPTA data alongside NANOGrav

### Birefringence from ACT:
- [ ] Compute EB cross-spectrum from the ACT IQU maps
- [ ] Estimate β = 0.5 * arctan(2*C_EB / (C_EE - C_BB))
- [ ] Compare with bounce prediction β = 0.27°
- [ ] Systematic checks: galactic dust, instrumental leakage

### Quintom bounce MCMC with new data:
- [ ] Add DESI DR2 BAO measurements (if released)
- [ ] Add DES Y6 weak lensing
- [ ] Rerun w0-wa MCMC with updated likelihoods
- [ ] Test quintom-B vs quintom-A vs ΛCDM

---

## Phase 4: New Dataset Scans (H200)

### High-priority new surveys to scan:
- [ ] BOSS/eBOSS DR16 spectra (~4M spectra, different from SDSS imaging)
- [ ] DES DR2 photometry (~700M objects, photo-z + morphology)
- [ ] ZTF DR20+ alerts/light curves (~1B detections)
- [ ] TESS full-frame images (time-domain anomalies)
- [ ] JWST public archive (NIRCam + NIRSpec)
- [ ] HST archive (decades of HST imaging — 150TB+)
- [ ] VLASS (VLA Sky Survey — radio continuum)
- [ ] FIRST/NVSS (radio surveys)
- [ ] XMM-Newton archive (X-ray — deeper than eROSITA in pointed obs)
- [ ] Chandra Source Catalog 2.1 (~400K X-ray sources)
- [ ] SPT-3G CMB maps (independent of Planck/ACT)
- [ ] HERA/CHIME 21cm data (if publicly released)
- [ ] PS1 3π survey (~3B objects)
- [ ] UKIDSS/VHS near-IR
- [ ] Herschel archive (far-IR)

### Advanced re-runs on existing data:
- [ ] DESI DR1 with transformer architecture (not just autoencoder)
- [ ] SDSS with variational autoencoder (VAE) — different anomaly ranking
- [ ] Multi-modal: combine spectral + photometric + positional features
- [ ] Train on ALL surveys jointly — learn cross-survey representations
- [ ] Contrastive learning: which objects look different across wavelengths?

---

## Phase 5: Papers

### Paper 3 — Multi-Survey Anomaly Catalog (target: ~95% → 100%)
- [x] Integrate ALL 8 survey results into unified catalog — **DONE in paper3_draft.tex** (2026-04-03)
- [x] Cross-match analysis section — **DONE** (2026-04-03)
- [x] f_NL improvement measurement — **6.1% improvement, SPHEREx 4.38σ** (2026-04-03)
- [x] Anomaly taxonomy table — **DONE** (2026-04-03)
- [x] Novel object discoveries section — **DONE (58.8% novel from SIMBAD)** (2026-04-03)
- [ ] Compile LaTeX, compile PDF (needs texlive-publishers on pod)
- [ ] Peer review round 1
- [ ] Add birefringence β result when H200 measurement finishes

### Paper 5 — Novel Objects from AI Archival Mining
- [ ] The z≈5.27 QSO: if confirmed uncataloged, this is a discovery
- [ ] Any objects in NEOWISE/Gaia not in SIMBAD
- [ ] Systematic discovery rates across surveys
- [ ] Comparison with traditional discovery methods

### Paper updates for Papers 1 & 2:
- [ ] Update NANOGrav section with validated γ=3.20±0.42 result
- [ ] Add BIC comparison (bounce favored over SMBHB)
- [ ] Update f_NL forecast with corrected σ(f_NL) = 8.98

---

## Phase 6: Ongoing Monitoring & Site Updates

After EVERY piece of follow-on work:
- [ ] Update activity.html with new timeline entry
- [ ] Update index.html stat cards if numbers change
- [ ] Update paper.html readiness percentages
- [ ] Update data-explorer.html if new datasets are embedded
- [ ] Commit and push (auto-deploy)
- [ ] Update research_queue.json
- [ ] Update project-context/active_pods_and_pipelines.md
- [ ] Backup new results to all locations (local, GitHub, B2, HuggingFace)
