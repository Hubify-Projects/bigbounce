# Uncataloged Anomaly Taxonomy

**Total uncataloged objects:** 1127
**Clusters found:** 3
**Unclustered (noise):** 1 (0.1%)
**Method:** PCA(128->20) + UMAP(n_neighbors=15, min_dist=0.05) + HDBSCAN(min_cluster_size=20)

---

## Taxonomy Summary

| Family | N | z (median) | Score (median) | Dominant Type | Label |
|--------|---|-----------|---------------|---------------|-------|
| C0 | 696 | 1.106 | 3.4 | GALAXY | UV-excess galaxies (possible starbursts) |
| C1 | 29 | 0.500 | 4.6 | GALAXY | UV-excess galaxies (AGN candidates) |
| C2 | 401 | 0.506 | 3.3 | GALAXY | UV-excess galaxies (possible starbursts) |
| noise | 1 | 0.234 | 3.9 | GALAXY | Unclustered anomalies (diverse) |

---

## Detailed Cluster Profiles

### Noise (unclustered): Unclustered anomalies (diverse)

**N = 1** objects

**Classification rationale:** Objects not assigned to any cluster by HDBSCAN

**Redshift:** median z = 0.234 (range 0.234 -- 0.234, std = nan)
**Anomaly score:** median = 3.9, mean = 3.9
**Spectype distribution:** GALAXY: 1
**Morphology:** : 1
**Point source fraction:** 0.0%
**Anomaly dominant band:** B: 1
**Dominant spectral feature:** unmatched (3132A) (100% of cluster)
**Top 3 lines:** unmatched (3132A): 1
**Peak residual wavelength:** 3864 A (std = nan A)
**rB residual (median):** 2.289
**rR residual (median):** 0.750
**rZ residual (median):** 0.626
**deltachi2 (median):** 3.8

---

### Cluster 0: UV-excess galaxies (possible starbursts)

**N = 696** objects

**Classification rationale:** blue g-r=0.30; blue colors without IR AGN signature; anomaly dominant in B band

**Redshift:** median z = 1.106 (range -0.002 -- 6.105, std = 0.990)
**Anomaly score:** median = 3.4, mean = 3.7
**Colors:** g-r = 0.30, r-z = 0.73, W1-W2 = -0.10
**Spectype distribution:** GALAXY: 589, QSO: 77, STAR: 30
**Morphology:** : 312, REX: 209, PSF: 117, EXP: 30, DEV: 26, SER: 2
**Point source fraction:** 16.8%
**Anomaly dominant band:** B: 519, Z: 101, R: 76
**Dominant spectral feature:** C IV (10% of cluster)
**Top 3 lines:** C IV: 68, C III]: 49, [O II]: 39
**Peak residual wavelength:** 5834 A (std = 2148 A)
**rB residual (median):** 1.832
**rR residual (median):** 0.744
**rZ residual (median):** 1.047
**deltachi2 (median):** 22.1

---

### Cluster 1: UV-excess galaxies (AGN candidates)

**N = 29** objects

**Classification rationale:** blue g-r=0.20; IR-bright w1-w2=1.24; anomaly dominant in B band

**Redshift:** median z = 0.500 (range -0.000 -- 5.173, std = 0.949)
**Anomaly score:** median = 4.6, mean = 4.6
**Colors:** g-r = 0.20, r-z = 0.47, W1-W2 = 1.24
**Spectype distribution:** GALAXY: 24, QSO: 3, STAR: 2
**Morphology:** : 28, REX: 1
**Point source fraction:** 0.0%
**Anomaly dominant band:** B: 29
**Dominant spectral feature:** Mg II (10% of cluster)
**Top 3 lines:** Mg II: 3, H-delta: 2, Ca II K: 2
**Peak residual wavelength:** 4482 A (std = 1025 A)
**rB residual (median):** 2.874
**rR residual (median):** 0.487
**rZ residual (median):** 0.402
**deltachi2 (median):** 4.1

---

### Cluster 2: UV-excess galaxies (possible starbursts)

**N = 401** objects

**Classification rationale:** blue g-r=0.04; blue colors without IR AGN signature; anomaly dominant in B band

**Redshift:** median z = 0.506 (range -0.001 -- 2.834, std = 0.499)
**Anomaly score:** median = 3.3, mean = 3.4
**Colors:** g-r = 0.04, r-z = 0.50, W1-W2 = 0.04
**Spectype distribution:** GALAXY: 380, QSO: 19, STAR: 2
**Morphology:** : 357, PSF: 21, REX: 16, EXP: 6, DEV: 1
**Point source fraction:** 5.2%
**Anomaly dominant band:** B: 401
**Dominant spectral feature:** Mg II (20% of cluster)
**Top 3 lines:** Mg II: 79, [O II]: 39, C IV: 12
**Peak residual wavelength:** 5038 A (std = 1662 A)
**rB residual (median):** 2.036
**rR residual (median):** 0.918
**rZ residual (median):** 0.667
**deltachi2 (median):** 5.8

---

## Astrophysical Interpretation

These 1,127 objects are spectral anomalies detected by a 128-dimensional 
autoencoder trained on ~25K DESI DR1 spectra that have NO match in SIMBAD 
or NED within 3 arcsec. The clustering reveals natural groupings based on 
latent-space similarity, which we interpret using physical properties 
(redshift, colors, spectral type, morphology, and the spectral feature 
driving the anomaly).

Key findings:

- **C0 (UV-excess galaxies (possible starbursts)):** 696 objects at median z=1.106. blue g-r=0.30; blue colors without IR AGN signature; anomaly dominant in B band
- **C1 (UV-excess galaxies (AGN candidates)):** 29 objects at median z=0.500. blue g-r=0.20; IR-bright w1-w2=1.24; anomaly dominant in B band
- **C2 (UV-excess galaxies (possible starbursts)):** 401 objects at median z=0.506. blue g-r=0.04; blue colors without IR AGN signature; anomaly dominant in B band
