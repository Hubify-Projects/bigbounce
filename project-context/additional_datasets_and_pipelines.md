# Additional Datasets & Pipeline Opportunities

**Created:** 2026-03-26
**Context:** Expanding beyond DESI DR1 to other large-scale astronomical datasets.
**Inspiration:** Paz 2024 (VARnet on 170B NEOWISE rows) — demonstrates feasibility of ML at 100B+ scale.

---

## Datasets Ranked by Discovery Potential × Feasibility

### TIER 1: Run Now (data public, infrastructure ready)

#### 1. NEOWISE / unTimely Time-Domain (Pipeline E)
- **Size:** 170B single-exposure rows (photometry), ~2B unique sources, 32 epochs in unTimely
- **What:** IR variability — find objects that changed brightness over 10.5 years
- **Our angle:** Cross-match NEOWISE variables with our 195K DESI anomalies. Objects that are BOTH spectrally anomalous AND time-variable are the most interesting.
- **Novel?** YES — nobody has cross-correlated DESI spectral anomalies with NEOWISE variability
- **Compute:** H200, ~2-4 days for unTimely (2B sources × 32 epochs)
- **Cost:** $100-200
- **Connection to bounce:** Variable high-z QSOs are the best f_NL tracers

#### 2. Planck CMB Maps (Pipeline A/C)
- **Size:** ~50GB (full-sky T/Q/U at 9 frequencies)
- **What:** AI anomaly detection on CMB patches — find unusual temperature/polarization patterns
- **Our angle:** Train autoencoder on simulated CMB patches, apply to real Planck data
- **Novel?** YES — nobody has done autoencoder anomaly detection on Planck maps at patch level
- **Compute:** H200, ~1-2 days
- **Cost:** $50-100
- **Connection to bounce:** Could find signatures of pre-bounce perturbations, anomalous cold/hot spots, or parity violations

#### 3. ACT DR6 CMB Polarization
- **Size:** ~20GB (high-resolution CMB, 19,000 deg²)
- **What:** AI-assisted birefringence measurement with improved systematic control
- **Our angle:** Use autoencoder to identify and mask contaminated polarization regions
- **Novel?** YES — AI-improved CMB polarization analysis
- **Compute:** H200, ~1 day
- **Cost:** $50
- **Connection to bounce:** Directly tests our β = 0.27° birefringence prediction

### TIER 2: Run Soon (data public, need model adaptation)

#### 4. SDSS DR18 Spectral Anomaly Scan
- **Size:** 5M spectra (different wavelength grid from DESI)
- **What:** Cross-survey validation — same autoencoder methodology, different survey
- **Novel?** YES — proves methodology is survey-independent
- **Compute:** Retrain autoencoder (~4h), inference (~2h)
- **Cost:** $30-50
- **Blocker:** SDSS API currently down, need to download bulk data

#### 5. LAMOST DR10 Spectral Anomaly Scan
- **Size:** 20M spectra (Chinese spectroscopic survey, largest in the world before DESI)
- **What:** Same methodology at even larger scale, different sky coverage
- **Novel?** YES — first autoencoder anomaly search on LAMOST at full scale
- **Compute:** H200, ~12 hours
- **Cost:** $50-100
- **Connection to bounce:** More tracers for f_NL measurement

#### 6. Gaia DR3 Spectral Anomalies
- **Size:** 220M low-resolution spectra (BP/RP), 1M RVS spectra
- **What:** Autoencoder on Gaia spectrophotometry — find unusual stellar spectra
- **Novel?** Partially — Gaia has its own outlier flags, but full autoencoder search not published
- **Compute:** H200, ~2 days for BP/RP
- **Cost:** $100-200
- **Connection to cosmology:** Unusual stars (white dwarf binaries, extreme metallicity) are interesting in their own right

#### 7. NANOGrav / IPTA PTA Data
- **Size:** ~1GB (15-year timing residuals for ~70 pulsars)
- **What:** Fit matter-bounce GW template to PTA free-spectrum data
- **Novel?** YES — first proper template fit (not just γ comparison)
- **Compute:** Local, ~2 hours
- **Cost:** Free
- **Connection to bounce:** Direct test of bounce-induced GW prediction

### TIER 3: Future (data not yet available or needs significant development)

#### 8. Euclid Spectroscopy (~30M galaxies, data release ~2027)
- **Size:** ~30M slitless spectra
- **What:** First anomaly detection on Euclid — next-generation survey after DESI
- **Novel?** YES — first of its kind
- **Connection to bounce:** More high-z tracers, f_NL improvement

#### 9. Roman Space Telescope Grism (~2028)
- **Size:** Millions of grism spectra from space
- **What:** Space-based spectral anomaly search — no atmospheric contamination
- **Novel?** YES
- **Connection to bounce:** Cleanest possible spectral data for anomaly detection

#### 10. LSST / Rubin Observatory (~2025-2035)
- **Size:** ~20B objects, 10-year time baseline, 6 filters
- **What:** Time-domain + photometric anomaly detection at unprecedented scale
- **Novel?** YES — LSST is the ultimate time-domain survey
- **Connection to bounce:** Galaxy chirality at z > 1, large-scale structure anomalies

#### 11. SPHEREx All-Sky Spectrophotometry (~2028)
- **Size:** ~300M objects with 96-band spectrophotometry
- **What:** Our flagship — this is the survey that measures f_NL
- **Our angle:** Pre-identify optimal tracers from DESI anomaly catalog
- **Connection to bounce:** DIRECT test of f_NL = -35/8

#### 12. CMB-S4 (~2030s)
- **Size:** Ground-based CMB at unprecedented sensitivity
- **What:** Definitive birefringence measurement
- **Connection to bounce:** Tests β = 0.27° at ~30σ (if real)

---

## The Hubify Lab Vision

Build a scalable, repeatable AI archival discovery platform:

```
Dataset (public archive)
  → Preprocessing pipeline (survey-specific)
    → AI model (autoencoder / classifier / time-series)
      → Anomaly catalog (scored, classified)
        → Cross-reference (SIMBAD, NED, Gaia, etc.)
          → Human review (anomaly explorer)
            → Paper + community data release
```

Each survey gets its own instance of this pipeline. Results cross-reference across surveys. Objects flagged by 2+ surveys are highest priority.

**Infrastructure needed:**
- H200 (or equivalent) for training + inference
- Convex for real-time data storage + explorer UI
- HuggingFace for model + dataset publishing
- GitHub for code + reproducibility
- Backblaze B2 for bulk data backup

**Cost per survey:** $50-200 (depending on data volume)
**Time per survey:** 1-4 weeks (including model training + inference + analysis)

---

## Comparison: Us vs Paz

| Aspect | Paz (VARnet) | Us (BigAE) |
|--------|-------------|-----------|
| Data type | Time-series photometry | Spectral flux |
| Dataset | NEOWISE (170B rows) | DESI DR1 (18M spectra) |
| Sources | ~2B unique | ~18M unique |
| Speed | ~53μs per source | ~1.1ms per source |
| Method | Wavelet + Fourier + CNN | Autoencoder (reconstruction error) |
| Training | Synthetic + real (supervised) | Real spectra (unsupervised) |
| Output | Classification (4 classes) | Anomaly score (continuous) |
| Cross-ref | SIMBAD, WiseView | SIMBAD, NED, AllWISE, Gaia, Milliquas |
| Publication | AJ (published 2024) | ApJS (draft, targeting 2026) |

**Key difference:** Paz does supervised classification (knows what he's looking for). We do unsupervised anomaly detection (finds things we DON'T know about). Both are valid but find different things.

**Synergy:** Run VARnet-style time-domain analysis on the unTimely light curves of our 195K anomalies. Objects that are spectrally unusual AND temporally unusual are the strongest discovery candidates.
