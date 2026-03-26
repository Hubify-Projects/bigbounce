# Pipeline 1 Expanded Plan: Beyond Steps 1-6

**Created:** 2026-03-26
**Context:** 195,829 anomalies detected, 100/100 top objects NOT in SIMBAD, Steps 1-3 complete, Steps 4-5 in progress.

This document expands the original 6-step plan with additional workstreams for model improvement, robust classification, and bounce-relevant observational derivation.

---

## Phase A: Model Improvement (after initial catalog)

### A1. Fine-tune autoencoder on anomaly feedback loop

**Problem:** The current autoencoder was trained once on known spectral classes. It finds anomalies by reconstruction error — but it doesn't know WHAT KIND of anomaly each one is. A feedback loop can improve this.

**Method:**
1. Take the top 1,000 anomalies and visually inspect a random 100 (human + AI)
2. Label them: artifact / genuine-unusual / high-z-candidate / unknown
3. Fine-tune the autoencoder with these labels as a secondary classification head
4. Re-run inference on the full 18M spectra with the improved model
5. Compare: does the improved model find the same anomalies? New ones? Fewer artifacts?

**Compute:** GPU pod, ~4-6 hours for fine-tuning + re-inference

### A2. Train a dedicated anomaly classifier

**Problem:** The autoencoder flags 195K anomalies but can't distinguish artifact from genuine. We need a supervised classifier.

**Method:**
1. Build a labeled training set from the top anomalies:
   - Use Legacy Survey images to flag artifacts (no source at position, diffraction spike, satellite trail)
   - Use DESI pipeline flags (ZWARN, DELTACHI2) to identify pipeline failures
   - Use color cuts (W1-W2, g-r, r-z) to pre-classify QSOs vs stars vs galaxies
2. Train a simple classifier (random forest or small CNN on spectra) to separate:
   - ARTIFACT (bad data, pipeline failure, instrumental)
   - STAR (stellar contaminant)
   - GALAXY (known galaxy type but unusual features)
   - QSO_CANDIDATE (high-z or unusual AGN — useful for f_NL)
   - NOVEL (doesn't fit any category — genuinely unknown)
3. Apply to all 195K anomalies

**Key data needed:** DESI ZWARN flags, DELTACHI2 values, fiber status bits. These are in the DESI DR1 spectra files alongside the flux.

### A3. Ensemble anomaly scoring

**Problem:** Single autoencoder may have blind spots. Different architectures find different anomalies.

**Method:**
1. Train 3 different anomaly detectors:
   - Autoencoder (current) — reconstruction error
   - Variational Autoencoder (VAE) — latent space distance (like Nicolaou+ 2026)
   - Isolation Forest on spectral features — non-neural baseline
2. Objects flagged by 2+ methods are higher-confidence anomalies
3. Objects flagged by only 1 method may be architecture-specific artifacts

**This directly addresses the prior art:** Liang+2023 used AE + normalizing flow. Nicolaou+2026 used VAE + Astronomaly. We can show that our anomalies are robust across methods.

---

## Phase B: Robust Scientific Process

### B1. Artifact rejection pipeline

**Problem:** 99% of the top anomalies have worst_band = B (blue). This could indicate a systematic issue with blue-end calibration rather than genuine spectral anomalies.

**Investigation:**
1. Check if B-dominant anomalies correlate with:
   - Fiber number (instrumental)
   - Observation date (calibration epoch)
   - Airmass (atmospheric)
   - Moon phase (sky brightness)
   - Galactic latitude (foreground extinction)
2. If correlated → systematic artifact → remove from science catalog
3. If NOT correlated → genuine spectral features in the blue

**This is Gate 6 of the 12-gate publication standard.**

### B2. Injection/recovery test

**Problem:** We don't know our completeness — how many real anomalies did we MISS?

**Method:**
1. Take 1,000 known unusual spectra (BAL QSOs, double-peaked emitters, etc.) from SDSS
2. Inject them into the DESI spectral format
3. Run through our autoencoder
4. Measure: what fraction are recovered as anomalies?
5. This gives our completeness as a function of anomaly type

**This is Gate 3 of the 12-gate standard. Currently FAIL — must be done before publication.**

### B3. Spectral inspection of top 50

**Method:**
1. For the top 50 anomalies by score, download the actual DESI spectra from the DR1 archive
2. Plot each spectrum with the autoencoder reconstruction overlaid
3. Identify WHERE in the spectrum the anomaly occurs (which wavelength range)
4. Classify by spectral feature:
   - Unusual emission lines (double-peaked, offset, unusual ratios)
   - Unusual absorption (broad absorption lines, damped Lyman-alpha)
   - Unusual continuum (very blue, very red, broken power law)
   - Multiple redshift systems (gravitational lens candidate)
   - Featureless (possible artifact)

**This is the most scientifically valuable step — it tells us WHAT we found.**

---

## Phase C: Bounce-Relevant Observational Derivations

### C1. Scale-dependent bias measurement

**If Step 4 (bias validation) shows enhanced clustering:**

The f_NL scale-dependent bias formula is:
```
Δb(k) = (b₁ - 1) · f_NL · δ_c / (α(k) · k²)
```

With our anomaly-enhanced tracer catalog:
1. Compute the angular power spectrum C_ℓ for the enhanced sample
2. Fit for b₁ (linear bias) at small scales
3. Look for scale-dependent deviation at large scales (ℓ < 30)
4. Constrain f_NL from the deviation
5. Compare σ(f_NL) before and after adding anomaly tracers

**This is the publishable f_NL measurement** (if the improvement is real).

### C2. Cross-correlation with CMB lensing

**Novel angle:** Cross-correlate our anomaly catalog positions with the Planck CMB lensing convergence map (κ).

- High-z QSOs should correlate with CMB lensing (they sit behind the lensing mass)
- Artifacts should NOT correlate (random positions relative to mass)
- The cross-correlation amplitude gives an independent bias estimate

This is a clean, independent validation that doesn't require any spectral analysis.

### C3. Redshift distribution and tracer bias profile

**If we can recover redshifts for the anomaly objects (from DESI pipeline or re-fitting):**

1. Plot n(z) for anomalies vs standard DESI QSOs
2. If anomalies are preferentially at z > 2 → they're high-z tracers → higher bias → better for f_NL
3. Compute b(z) for anomalies using clustering in redshift slices
4. Feed b(z) profile into the multi-tracer f_NL forecast

### C4. Parity/isotropy tests on anomaly distribution

**Direct bounce connection (speculative but worth checking):**

1. Test whether anomaly positions show any preferred axis on the sky
2. Compare with the CMB anomaly axis (ℓ ≈ 230°, b ≈ 60°)
3. If anomalies are isotropic → null result (expected)
4. If anomalies show axis alignment → potential parity signal (extremely unlikely but would be headline-worthy)

This is a cheap test (just positions) and connects to the bounce cosmology parity predictions.

---

## Phase D: Enhanced Anomaly Explorer Features

### D1. Spectral viewer in the explorer

**Add an embedded spectral plot for each anomaly:**
- Fetch the actual DESI spectrum from the DR1 archive
- Plot flux vs wavelength with the autoencoder reconstruction overlaid
- Highlight the wavelength range where the anomaly occurs
- This lets reviewers see WHY each object is anomalous

### D2. Crowdsourced classification

**Add a simple classification interface:**
- For each anomaly, show the image + spectrum
- Buttons: "Genuine" / "Artifact" / "Unsure"
- Store votes in Convex
- After N votes, auto-classify by majority

### D3. Similar object finder

**For each anomaly, show the 5 most similar objects from the catalog:**
- Similarity by spectral residual pattern (cosine similarity in rB/rR/rZ space)
- Similarity by sky position (spatial clustering → same physical structure?)
- This helps identify GROUPS of anomalies that may be the same phenomenon

---

## Priority Order

1. **Step 4-5** (bias validation + f_NL measurement) — in progress
2. **B3** (spectral inspection of top 50) — highest scientific value
3. **B1** (artifact rejection) — required for publication credibility
4. **A2** (anomaly classifier) — needed to scale beyond manual inspection
5. **C2** (CMB lensing cross-correlation) — clean independent validation
6. **B2** (injection/recovery) — required for completeness claims
7. **A1** (autoencoder fine-tuning) — iterative improvement
8. **C1** (scale-dependent bias) — the ultimate f_NL measurement
9. **D1-D3** (explorer enhancements) — user experience

---

## What Would Be Truly Novel

| Item | Novelty level | Why |
|------|--------------|-----|
| 195K anomaly catalog from full DR1 | HIGH (scale) | ~90x prior EDR work |
| CMB lensing × anomaly cross-correlation | HIGH (method) | Never done with AI-detected anomalies |
| f_NL improvement from AI-purified tracers | VERY HIGH | Closed loop: AI → cosmology measurement |
| Spectral classification of top anomalies | MEDIUM | Similar to Liang/Nicolaou but on DR1 |
| Ensemble anomaly scoring (AE + VAE + IF) | MEDIUM | Methodological robustness |
| Parity test on anomaly distribution | LOW (likely null) | But cheap and connects to bounce |
