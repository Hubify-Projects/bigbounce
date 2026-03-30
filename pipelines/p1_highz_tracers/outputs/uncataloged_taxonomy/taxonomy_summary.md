# Uncataloged Anomaly Taxonomy

**Total objects classified:** 1127
**Spectral clusters found:** 29
**Astrophysical families:** 10
**Method:** PCA(128->20) + UMAP(20->2) + HDBSCAN(leaf) + kNN reassignment + family merge
**Source:** DESI DR1 spectral autoencoder anomalies with NO match in SIMBAD or NED (3")

---

## Family Summary

| ID | N | z (med) | Score | g-r | W1-W2 | Spectype | Family |
|----|---|---------|-------|-----|-------|----------|--------|
| F0 | 363 | 1.213 | 3.3 | 0.24 | 0.12 | GALAXY | Blue intermediate-z galaxy anomalies |
| F1 | 148 | 0.517 | 3.4 | 0.26 | 0.12 | GALAXY | Blue emission-line galaxies (star-forming) |
| F2 | 126 | 0.536 | 3.2 | 0.16 | 0.22 | GALAXY | Blue star-forming galaxy anomalies |
| F3 | 103 | 0.827 | 3.5 | 1.45 | -0.35 | GALAXY | Red anomalous galaxies (dusty/evolved/quenched) |
| F4 | 93 | 0.513 | 3.3 | 0.03 | -0.10 | GALAXY | Blue UV-excess galaxies (strong B-band anomaly) |
| F5 | 78 | 0.504 | 3.2 | -0.31 | 0.40 | GALAXY | Extreme UV-excess galaxies (strong starbursts or AGN) |
| F6 | 76 | 0.498 | 3.4 | 0.20 | 1.28 | GALAXY | IR-bright AGN candidates (WISE color selection) |
| F7 | 71 | 1.191 | 3.6 | 0.26 | -0.25 | GALAXY | NIR-excess galaxies (dusty starbursts or evolved populations) |
| F8 | 42 | 0.811 | 4.1 | 1.29 | -0.42 | GALAXY | Optical-band spectral anomalies |
| F9 | 27 | 0.468 | 4.5 | 1.47 | -0.62 | GALAXY | Post-starburst (E+A) galaxy candidates |

---

## Detailed Family Profiles

### Family 0: Blue intermediate-z galaxy anomalies

**N = 363** objects (from clusters 1, 6, 12, 16, 21, 23, 24, 25, 26, 27, 28)

**Classification rationale:** g-r=0.17, z=1.33; worst band: B; spectral feature: [O II]

- **Redshift:** median z = 1.213, IQR [0.922, 1.498], range [0.000, 6.097]
- **Anomaly score:** median = 3.3, mean = 3.5, max = 6.2
- **Colors:** g-r = 0.24, r-z = 0.69, W1-W2 = 0.12
- **Spectype:** {'GALAXY': 325, 'QSO': 36, 'STAR': 2}
- **Morphology:** {'': 136, 'REX': 131, 'PSF': 68, 'EXP': 18, 'DEV': 9, 'SER': 1}
- **Point source fraction:** 18.7%
- **Worst band:** {'B': 324, 'Z': 34, 'R': 5}
- **Band residuals (med):** rB = 1.839, rR = 0.444, rZ = 1.154
- **Dominant spectral feature:** He II
- **Top lines:** {'He II': 37, 'C IV': 31, '[O II]': 24, 'C III]': 22, 'Fe II UV': 14}
- **deltachi2 (med):** 21.2
- **Good redshift (zwarn=0):** 10.5%

---

### Family 1: Blue emission-line galaxies (star-forming)

**N = 148** objects (from clusters 3, 4, 20)

**Classification rationale:** g-r=0.00, emission: [O II]; worst band: B; spectral feature: [O II]

- **Redshift:** median z = 0.517, IQR [0.267, 1.385], range [-0.002, 4.033]
- **Anomaly score:** median = 3.4, mean = 3.7, max = 15.2
- **Colors:** g-r = 0.26, r-z = 0.63, W1-W2 = 0.12
- **Spectype:** {'GALAXY': 120, 'QSO': 26, 'STAR': 2}
- **Morphology:** {'': 106, 'PSF': 20, 'REX': 17, 'EXP': 4, 'DEV': 1}
- **Point source fraction:** 13.5%
- **Worst band:** {'B': 128, 'Z': 13, 'R': 7}
- **Band residuals (med):** rB = 2.060, rR = 0.935, rZ = 0.678
- **Dominant spectral feature:** [O II]
- **Top lines:** {'[O II]': 16, 'Mg II': 10, 'Ca II K': 8, 'C IV': 8, 'Fe II UV': 6}
- **deltachi2 (med):** 11.1
- **Good redshift (zwarn=0):** 14.9%

---

### Family 2: Blue star-forming galaxy anomalies

**N = 126** objects (from clusters 5, 11, 17)

**Classification rationale:** g-r=0.24, z=0.99; worst band: B; spectral feature: C IV

- **Redshift:** median z = 0.536, IQR [0.346, 1.013], range [0.057, 2.800]
- **Anomaly score:** median = 3.2, mean = 3.4, max = 5.3
- **Colors:** g-r = 0.16, r-z = 0.68, W1-W2 = 0.22
- **Spectype:** {'GALAXY': 122, 'QSO': 4}
- **Morphology:** {'': 90, 'REX': 19, 'PSF': 14, 'EXP': 3}
- **Point source fraction:** 11.1%
- **Worst band:** {'B': 125, 'Z': 1}
- **Band residuals (med):** rB = 1.973, rR = 0.894, rZ = 0.700
- **Dominant spectral feature:** Mg II
- **Top lines:** {'Mg II': 15, '[O II]': 10, 'He II': 8, 'C IV': 5, '[Ne V]': 5}
- **deltachi2 (med):** 6.7
- **Good redshift (zwarn=0):** 10.3%

---

### Family 3: Red anomalous galaxies (dusty/evolved/quenched)

**N = 103** objects (from cluster 9)

**Classification rationale:** red g-r=1.45; worst band: B; spectral feature: C III]

- **Redshift:** median z = 0.827, IQR [0.602, 1.199], range [-0.001, 5.114]
- **Anomaly score:** median = 3.5, mean = 3.7, max = 6.3
- **Colors:** g-r = 1.45, r-z = 1.77, W1-W2 = -0.35
- **Spectype:** {'GALAXY': 84, 'QSO': 14, 'STAR': 5}
- **Morphology:** {'': 44, 'REX': 27, 'PSF': 17, 'DEV': 10, 'EXP': 5}
- **Point source fraction:** 16.5%
- **Worst band:** {'B': 75, 'R': 27, 'Z': 1}
- **Band residuals (med):** rB = 1.997, rR = 1.408, rZ = 0.334
- **Dominant spectral feature:** C III]
- **Top lines:** {'C III]': 9, 'He II': 5, 'Fe II UV': 5, 'C IV': 4, 'H-gamma': 4}
- **deltachi2 (med):** 13.4
- **Good redshift (zwarn=0):** 6.8%

---

### Family 4: Blue UV-excess galaxies (strong B-band anomaly)

**N = 93** objects (from clusters 2, 15)

**Classification rationale:** g-r=0.03, rB=2.01; worst band: B; spectral feature: Mg II

- **Redshift:** median z = 0.513, IQR [0.263, 0.575], range [-0.001, 2.834]
- **Anomaly score:** median = 3.3, mean = 3.3, max = 5.8
- **Colors:** g-r = 0.03, r-z = 0.49, W1-W2 = -0.10
- **Spectype:** {'GALAXY': 85, 'QSO': 7, 'STAR': 1}
- **Morphology:** {'': 74, 'PSF': 8, 'REX': 7, 'EXP': 3, 'DEV': 1}
- **Point source fraction:** 8.6%
- **Worst band:** {'B': 93}
- **Band residuals (med):** rB = 2.047, rR = 0.884, rZ = 0.693
- **Dominant spectral feature:** Mg II
- **Top lines:** {'Mg II': 14, '[O II]': 8, 'C III]': 3, 'Ca II H': 3, 'unmatched (3131A)': 2}
- **deltachi2 (med):** 6.5
- **Good redshift (zwarn=0):** 3.2%

---

### Family 5: Extreme UV-excess galaxies (strong starbursts or AGN)

**N = 78** objects (from clusters 13, 19)

**Classification rationale:** very blue g-r=-0.57, z=0.37; worst band: B; spectral feature: Mg II

- **Redshift:** median z = 0.504, IQR [0.241, 0.540], range [0.000, 1.639]
- **Anomaly score:** median = 3.2, mean = 3.3, max = 5.1
- **Colors:** g-r = -0.31, r-z = -0.03, W1-W2 = 0.40
- **Spectype:** {'GALAXY': 75, 'QSO': 2, 'STAR': 1}
- **Morphology:** {'': 75, 'REX': 1, 'PSF': 1, 'EXP': 1}
- **Point source fraction:** 1.3%
- **Worst band:** {'B': 78}
- **Band residuals (med):** rB = 2.004, rR = 0.938, rZ = 0.648
- **Dominant spectral feature:** Mg II
- **Top lines:** {'Mg II': 17, 'He II': 3, 'H-gamma': 2, '[Ne V]': 2, 'C IV': 2}
- **deltachi2 (med):** 7.4
- **Good redshift (zwarn=0):** 0.0%

---

### Family 6: IR-bright AGN candidates (WISE color selection)

**N = 76** objects (from clusters 0, 18)

**Classification rationale:** W1-W2=1.24 (AGN wedge), z=0.50; worst band: B; spectral feature: Mg II

- **Redshift:** median z = 0.498, IQR [0.232, 0.536], range [-0.000, 5.173]
- **Anomaly score:** median = 3.4, mean = 3.8, max = 7.8
- **Colors:** g-r = 0.20, r-z = 0.47, W1-W2 = 1.28
- **Spectype:** {'GALAXY': 71, 'QSO': 3, 'STAR': 2}
- **Morphology:** {'': 73, 'PSF': 2, 'REX': 1}
- **Point source fraction:** 2.6%
- **Worst band:** {'B': 76}
- **Band residuals (med):** rB = 2.141, rR = 0.902, rZ = 0.624
- **Dominant spectral feature:** Mg II
- **Top lines:** {'Mg II': 13, '[O II]': 4, 'Ca II K': 4, 'He II': 4, '[Ne V]': 3}
- **deltachi2 (med):** 3.8
- **Good redshift (zwarn=0):** 1.3%

---

### Family 7: NIR-excess galaxies (dusty starbursts or evolved populations)

**N = 71** objects (from clusters 14, 22)

**Classification rationale:** Z-band dominated rZ=1.82, z=0.98; worst band: Z; spectral feature: H-delta

- **Redshift:** median z = 1.191, IQR [1.022, 1.193], range [-0.000, 6.105]
- **Anomaly score:** median = 3.6, mean = 3.7, max = 6.6
- **Colors:** g-r = 0.26, r-z = 0.73, W1-W2 = -0.25
- **Spectype:** {'GALAXY': 63, 'QSO': 4, 'STAR': 4}
- **Morphology:** {'': 59, 'REX': 9, 'PSF': 2, 'EXP': 1}
- **Point source fraction:** 2.8%
- **Worst band:** {'Z': 51, 'B': 19, 'R': 1}
- **Band residuals (med):** rB = 1.465, rR = 0.814, rZ = 1.824
- **Dominant spectral feature:** [Ne V]
- **Top lines:** {'[Ne V]': 9, 'H-beta': 5, 'unmatched (1780A)': 2, 'H-delta': 2, 'unmatched (4468A)': 2}
- **deltachi2 (med):** 45.3
- **Good redshift (zwarn=0):** 4.2%

---

### Family 8: Optical-band spectral anomalies

**N = 42** objects (from clusters 7, 8)

**Classification rationale:** R-band dominated rR=1.96; worst band: R; spectral feature: Mg II

- **Redshift:** median z = 0.811, IQR [0.251, 1.419], range [-0.000, 4.080]
- **Anomaly score:** median = 4.1, mean = 4.4, max = 6.5
- **Colors:** g-r = 1.29, r-z = 1.46, W1-W2 = -0.42
- **Spectype:** {'GALAXY': 34, 'STAR': 5, 'QSO': 3}
- **Morphology:** {'': 29, 'REX': 5, 'DEV': 3, 'PSF': 3, 'EXP': 1, 'SER': 1}
- **Point source fraction:** 7.1%
- **Worst band:** {'R': 32, 'B': 9, 'Z': 1}
- **Band residuals (med):** rB = 1.247, rR = 2.205, rZ = 0.886
- **Top lines:** {'unmatched (5587A)': 2, 'Ca II K': 2, 'H-gamma': 2, 'Fe II UV': 2, 'Mg II': 2}
- **deltachi2 (med):** 12.6
- **Good redshift (zwarn=0):** 14.3%

---

### Family 9: Post-starburst (E+A) galaxy candidates

**N = 27** objects (from cluster 10)

**Classification rationale:** red g-r=1.47, absorption: Ca II K; worst band: B; spectral feature: Ca II K

- **Redshift:** median z = 0.468, IQR [-0.000, 0.834], range [-0.001, 1.286]
- **Anomaly score:** median = 4.5, mean = 4.7, max = 7.8
- **Colors:** g-r = 1.47, r-z = 1.84, W1-W2 = -0.62
- **Spectype:** {'GALAXY': 15, 'STAR': 12}
- **Morphology:** {'': 12, 'REX': 9, 'PSF': 3, 'DEV': 3}
- **Point source fraction:** 11.1%
- **Worst band:** {'B': 23, 'R': 4}
- **Band residuals (med):** rB = 2.292, rR = 1.719, rZ = 0.251
- **Dominant spectral feature:** Ca II K
- **Top lines:** {'Ca II K': 3, 'Fe II UV': 2, 'unmatched (5587A)': 2, 'H-delta': 2, '[O II]': 2}
- **deltachi2 (med):** 21.0
- **Good redshift (zwarn=0):** 0.0%

---

## Astrophysical Interpretation

These 1,127 objects are spectral anomalies found by a 128-dimensional autoencoder 
trained on ~25K DESI DR1 spectra. They have NO counterpart in SIMBAD or NED within 
3 arcseconds -- genuinely uncataloged in major astronomical databases.

The taxonomy uses a three-stage approach:
1. **Spectral clustering** via PCA + UMAP + HDBSCAN on autoencoder latent vectors
2. **Noise reassignment** via k-nearest-neighbor to the closest cluster
3. **Astrophysical labeling** using physical properties (z, colors, line IDs, morphology)
4. **Family merging** to combine clusters with identical physical interpretations

### Key Findings

- **F0 -- Blue intermediate-z galaxy anomalies** (363 objects): g-r=0.17, z=1.33; worst band: B; spectral feature: [O II]
- **F1 -- Blue emission-line galaxies (star-forming)** (148 objects): g-r=0.00, emission: [O II]; worst band: B; spectral feature: [O II]
- **F2 -- Blue star-forming galaxy anomalies** (126 objects): g-r=0.24, z=0.99; worst band: B; spectral feature: C IV
- **F3 -- Red anomalous galaxies (dusty/evolved/quenched)** (103 objects): red g-r=1.45; worst band: B; spectral feature: C III]
- **F4 -- Blue UV-excess galaxies (strong B-band anomaly)** (93 objects): g-r=0.03, rB=2.01; worst band: B; spectral feature: Mg II
- **F5 -- Extreme UV-excess galaxies (strong starbursts or AGN)** (78 objects): very blue g-r=-0.57, z=0.37; worst band: B; spectral feature: Mg II
- **F6 -- IR-bright AGN candidates (WISE color selection)** (76 objects): W1-W2=1.24 (AGN wedge), z=0.50; worst band: B; spectral feature: Mg II
- **F7 -- NIR-excess galaxies (dusty starbursts or evolved populations)** (71 objects): Z-band dominated rZ=1.82, z=0.98; worst band: Z; spectral feature: H-delta
- **F8 -- Optical-band spectral anomalies** (42 objects): R-band dominated rR=1.96; worst band: R; spectral feature: Mg II
- **F9 -- Post-starburst (E+A) galaxy candidates** (27 objects): red g-r=1.47, absorption: Ca II K; worst band: B; spectral feature: Ca II K

### Relevance to Bounce Cosmology

The classified families feed into Pipeline 1 (tracer purification for f_NL):

- High-z QSO and galaxy families provide potential tracers with distinctive 
  bias properties for primordial non-Gaussianity measurement
- UV-excess and emission-line families may include objects with unusual formation 
  histories sensitive to primordial conditions
- Family labels enable computing per-family halo bias b(z), the critical input 
  for improving sigma(f_NL) constraints
