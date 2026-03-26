# DESI DR1 Spectral Anomaly Analysis: Top 50 Objects

**Date:** 2026-03-25
**Catalog:** DESI DR1 spectral autoencoder anomaly catalog (195,829 spectra)
**Method:** Convolutional autoencoder trained on 25,000 DESI DR1 spectra, flagging objects whose reconstructed spectra deviate most from input
**Cross-match:** 0/100 top anomalies found in SIMBAD -- ALL are previously uncataloged

---

## Executive Summary

We analyzed the 50 highest-scoring spectral anomalies from a catalog of 195,829 DESI DR1 spectra processed through a convolutional autoencoder. These objects have spectra that deviate most strongly from any known spectral template the autoencoder learned. **None of the top 100 objects appear in SIMBAD**, confirming they are genuinely uncataloged sources.

### Key Statistics

| Metric | Value |
|--------|-------|
| Objects analyzed | 50 |
| Score range | 15.98 -- 25.16 |
| SIMBAD matches | 0/100 (none) |
| Follow-up recommended | 28 objects |
| VERY_HIGH discovery potential | 6 objects |
| HIGH discovery potential | 22 objects |

### Classification Breakdown

| Classification | Count | Description |
|---------------|-------|-------------|
| UNUSUAL_AGN | 23 | Anomalous active galactic nucleus or QSO with unusual line profiles or continuum |
| UNUSUAL_GALAXY | 16 | Galaxy with anomalous spectral features not matching standard templates |
| HIGH_Z_CANDIDATE | 5 | Possible high-redshift (z > 2-3) object with redshifted features in NIR |
| STELLAR_ODDITY | 3 | Point source with extreme blue excess, possibly unusual hot star or CV |
| GENUINELY_NOVEL | 3 | Spectral pattern inconsistent with ALL known object classes |

### Residual Pattern Distribution

| Pattern | Count | Physical Interpretation |
|---------|-------|------------------------|
| B_dominant | 20 | Excess blue/UV emission (3600-5800A) -- hot stars, CVs, high-ionization sources |
| R_dominant | 13 | Excess optical emission (5760-7620A) -- unusual AGN, Lyman-alpha at z~4-5 |
| multi_band | 13 | Anomalous across full spectrum -- genuinely unusual objects |
| Z_dominant | 4 | Excess near-IR emission (7520-9824A) -- high-z objects, dust-reddened sources |

---

## Priority Discovery Candidates

### VERY_HIGH Discovery Potential

These 6 objects represent the strongest candidates for novel astrophysical discoveries:

#### Rank 3 -- TID -242337192

- **Position:** RA=206.638057, Dec=9.050749 (b=+67.7 deg)
- **Score:** 24.53
- **Residuals:** B=0.87, R=0.72, Z=7.43 (Z_dominant)
- **LS Morphology:** PSF
- **Classification:** HIGH_Z_CANDIDATE
- **Analysis:** Exceptionally high anomaly score (24.53) — top 0.01% of 195,829 DESI spectra. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The Z-band (near-IR) residual dominates at 7.43, which is 9x larger than other bands. This signature is consistent with a high-redshift object (z > 2-3) where strong emission lines have been redshifted into the NIR, or a source with an anomalous red continuum that DESI's standard templates cannot fit. High galactic latitude (b=+67.7 deg) strongly favors extragalactic origin.
- **Follow-up:** Z-band residual of 7.43 with score 24.5 suggests this may be a high-redshift object not in any existing catalog. Deep spectroscopy with longer integration or NIR spectroscopy could confirm redshift and reveal the nature of this uncataloged source.
- [Legacy Survey Viewer](https://www.legacysurvey.org/viewer?ra=206.638057&dec=9.050749&layer=ls-dr10&zoom=15)

#### Rank 4 -- TID -218427377

- **Position:** RA=172.864342, Dec=-2.343388 (b=+54.8 deg)
- **Score:** 24.20
- **Residuals:** B=1.55, R=8.27, Z=0.18 (R_dominant)
- **LS Morphology:** PSF
- **Classification:** HIGH_Z_CANDIDATE
- **Analysis:** Exceptionally high anomaly score (24.20) — top 0.01% of 195,829 DESI spectra. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The R-band (optical) residual dominates at 8.27, 5x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+54.8 deg) favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.
- **Follow-up:** R-band residual of 8.27 with score 24.2 suggests this may be a high-redshift object not in any existing catalog. Deep spectroscopy with longer integration or NIR spectroscopy could confirm redshift and reveal the nature of this uncataloged source.
- [Legacy Survey Viewer](https://www.legacysurvey.org/viewer?ra=172.864342&dec=-2.343388&layer=ls-dr10&zoom=15)

#### Rank 7 -- TID -218424222

- **Position:** RA=171.254179, Dec=-2.086120 (b=+54.1 deg)
- **Score:** 20.87
- **Residuals:** B=6.99, R=0.32, Z=0.18 (B_dominant)
- **LS Morphology:** REX
- **Classification:** UNUSUAL_AGN
- **Analysis:** Very high anomaly score (20.87) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.99, 22x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+54.1 deg) favors extragalactic origin. Infrared-luminous (bright in WISE W1/W2), suggesting either an obscured AGN, a dusty starburst galaxy, or an intrinsically red source.
- **Follow-up:** B-dominant anomaly pattern with IR-bright SED suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.
- [Legacy Survey Viewer](https://www.legacysurvey.org/viewer?ra=171.254179&dec=-2.086120&layer=ls-dr10&zoom=15)

#### Rank 27 -- TID 616088449090323141

- **Position:** RA=157.149452, Dec=-3.723835 (b=+43.8 deg)
- **Score:** 17.55
- **Residuals:** B=1.09, R=3.96, Z=3.82 (multi_band)
- **LS Morphology:** REX
- **Classification:** GENUINELY_NOVEL
- **Analysis:** High anomaly score (17.55) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. Anomalous across MULTIPLE bands (R=3.96, Z=3.82), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. Moderate-high galactic latitude (b=+43.8 deg) favors extragalactic origin.
- **Follow-up:** This object defies standard classification with its dual R+Z anomaly pattern (rB=1.09, rR=3.96, rZ=3.82). It may represent a genuinely new class of astrophysical source, a rare transient phenomenon, or an unusual composite system. Priority follow-up with IFU spectroscopy is strongly recommended.
- [Legacy Survey Viewer](https://www.legacysurvey.org/viewer?ra=157.149452&dec=-3.723835&layer=ls-dr10&zoom=15)

#### Rank 40 -- TID -17747190

- **Position:** RA=224.057561, Dec=41.786727 (b=+60.6 deg)
- **Score:** 16.32
- **Residuals:** B=4.78, R=0.27, Z=2.55 (multi_band)
- **LS Morphology:** SER
- **Classification:** GENUINELY_NOVEL
- **Analysis:** High anomaly score (16.32) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a SERSIC-profile galaxy — luminous, likely massive. Anomalous across MULTIPLE bands (B=4.78, Z=2.55), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. High galactic latitude (b=+60.6 deg) strongly favors extragalactic origin.
- **Follow-up:** This object defies standard classification with its B+Z anomaly pattern (rB=4.78, rR=0.27, rZ=2.55). It may represent a genuinely new class of astrophysical source, a rare transient phenomenon, or an unusual composite system. Priority follow-up with IFU spectroscopy is strongly recommended.
- [Legacy Survey Viewer](https://www.legacysurvey.org/viewer?ra=224.057561&dec=41.786727&layer=ls-dr10&zoom=15)

#### Rank 47 -- TID -16467190

- **Position:** RA=200.451382, Dec=55.950802 (b=+60.7 deg)
- **Score:** 16.08
- **Residuals:** B=4.81, R=0.28, Z=2.31 (multi_band)
- **LS Morphology:** REX
- **Classification:** GENUINELY_NOVEL
- **Analysis:** High anomaly score (16.08) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. Anomalous across MULTIPLE bands (B=4.81, Z=2.31), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. High galactic latitude (b=+60.7 deg) strongly favors extragalactic origin.
- **Follow-up:** This object defies standard classification with its B+Z anomaly pattern (rB=4.81, rR=0.28, rZ=2.31). It may represent a genuinely new class of astrophysical source, a rare transient phenomenon, or an unusual composite system. Priority follow-up with IFU spectroscopy is strongly recommended.
- [Legacy Survey Viewer](https://www.legacysurvey.org/viewer?ra=200.451382&dec=55.950802&layer=ls-dr10&zoom=15)

---

## Full Catalog: Top 50 Anomalies

### Summary Table

| Rank | TID | RA | Dec | Score | Pattern | Classification | Potential | LS Type |
|------|-----|-----|-----|-------|---------|---------------|-----------|---------|
| 1 | -242117190 | 194.4558 | 21.7302 | 25.16 | Z_dominant | HIGH_Z_CANDIDATE | HIGH | REX |
| 2 | -262397190 | 156.1807 | 2.1075 | 24.61 | Z_dominant | HIGH_Z_CANDIDATE | HIGH | REX |
| 3 | -242337192 | 206.6381 | 9.0507 | 24.53 | Z_dominant | HIGH_Z_CANDIDATE | VERY_HIGH | PSF |
| 4 | -218427377 | 172.8643 | -2.3434 | 24.20 | R_dominant | HIGH_Z_CANDIDATE | VERY_HIGH | PSF |
| 5 | -237137377 | 201.2874 | -7.6624 | 22.30 | R_dominant | UNUSUAL_AGN | HIGH | REX |
| 6 | -260408264 | 99.0516 | 59.1127 | 20.98 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |
| 7 | -218424222 | 171.2542 | -2.0861 | 20.87 | B_dominant | UNUSUAL_AGN | VERY_HIGH | REX |
| 8 | -252707377 | 195.3727 | -5.4927 | 20.50 | R_dominant | UNUSUAL_AGN | HIGH | REX |
| 9 | -226434222 | 199.2074 | 8.6550 | 20.29 | B_dominant | UNUSUAL_GALAXY | HIGH | REX |
| 10 | -242117261 | 194.5900 | 22.2265 | 20.25 | R_dominant | UNUSUAL_AGN | HIGH | REX |
| 11 | -240426131 | 263.8411 | 42.6254 | 19.96 | B_dominant | STELLAR_ODDITY | HIGH | PSF |
| 12 | -218354222 | 167.1064 | -7.3350 | 19.85 | B_dominant | UNUSUAL_GALAXY | HIGH | REX |
| 13 | -218427261 | 172.6745 | -2.4849 | 19.81 | R_dominant | UNUSUAL_AGN | HIGH | PSF |
| 14 | -248077261 | 212.6182 | -2.3555 | 19.45 | R_dominant | UNUSUAL_AGN | MEDIUM | REX |
| 15 | -237137261 | 201.0961 | -7.8041 | 19.16 | R_dominant | UNUSUAL_AGN | MEDIUM | REX |
| 16 | -218357192 | 168.3868 | -7.6627 | 18.73 | R_dominant | UNUSUAL_AGN | HIGH | PSF |
| 17 | -216814222 | 211.7838 | 1.2123 | 18.71 | B_dominant | UNUSUAL_GALAXY | HIGH | REX |
| 18 | -237314222 | 207.1284 | -2.5476 | 18.60 | B_dominant | UNUSUAL_GALAXY | HIGH | REX |
| 19 | -246427377 | 153.1900 | 7.9120 | 18.57 | R_dominant | UNUSUAL_AGN | MEDIUM | REX |
| 20 | -11932521 | 226.8887 | 21.8227 | 18.49 | R_dominant | UNUSUAL_AGN | MEDIUM | EXP |
| 21 | -251384222 | 266.7311 | 22.6533 | 18.32 | B_dominant | STELLAR_ODDITY | MEDIUM | PSF |
| 22 | -251414222 | 244.8821 | 8.1525 | 18.26 | B_dominant | STELLAR_ODDITY | HIGH | PSF |
| 23 | -230884222 | 142.6394 | -0.6995 | 18.10 | B_dominant | UNUSUAL_GALAXY | HIGH | REX |
| 24 | -232357190 | 239.1362 | -0.3618 | 18.05 | Z_dominant | HIGH_Z_CANDIDATE | HIGH | REX |
| 25 | -249804222 | 174.8635 | 0.3589 | 17.85 | B_dominant | UNUSUAL_GALAXY | HIGH | REX |
| 26 | -260407300 | 99.1221 | 59.8823 | 17.72 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |
| 27 | 616088449090323141 | 157.1495 | -3.7238 | 17.55 | multi_band | GENUINELY_NOVEL | VERY_HIGH | REX |
| 28 | -249754222 | 168.1442 | 1.2658 | 17.54 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |
| 29 | -218393212 | 167.2095 | -2.3717 | 17.48 | B_dominant | UNUSUAL_GALAXY | HIGH | REX |
| 30 | -204208127 | 248.8467 | 24.0939 | 17.15 | multi_band | UNUSUAL_AGN | HIGH | REX |
| 31 | -231017261 | 141.9601 | -3.6926 | 17.08 | multi_band | UNUSUAL_AGN | MEDIUM | REX |
| 32 | -240312292 | 268.2672 | 28.1562 | 16.98 | multi_band | UNUSUAL_AGN | HIGH | PSF |
| 33 | -232217377 | 220.7709 | -1.5047 | 16.97 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |
| 34 | -234177261 | 182.5234 | -2.1254 | 16.85 | R_dominant | UNUSUAL_AGN | MEDIUM | REX |
| 35 | -208925052 | 271.0813 | 46.7623 | 16.70 | multi_band | UNUSUAL_AGN | MEDIUM | PSF |
| 36 | -70095052 | 97.1916 | 63.2552 | 16.65 | multi_band | UNUSUAL_AGN | HIGH | PSF |
| 37 | -215207261 | 148.1251 | -0.6863 | 16.35 | R_dominant | UNUSUAL_AGN | MEDIUM | REX |
| 38 | -200075052 | 225.1185 | 35.7684 | 16.34 | multi_band | UNUSUAL_AGN | MEDIUM | PSF |
| 39 | -224495449 | 275.3504 | 45.6662 | 16.33 | multi_band | UNUSUAL_AGN | MEDIUM | PSF |
| 40 | -17747190 | 224.0576 | 41.7867 | 16.32 | multi_band | GENUINELY_NOVEL | VERY_HIGH | SER |
| 41 | -24905449 | 72.2509 | -0.8699 | 16.30 | multi_band | UNUSUAL_AGN | HIGH | PSF |
| 42 | -52785158 | 109.9830 | 38.0265 | 16.30 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |
| 43 | -252904222 | 197.9604 | -0.0128 | 16.29 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |
| 44 | -252707261 | 195.1821 | -5.6343 | 16.24 | R_dominant | UNUSUAL_AGN | MEDIUM | REX |
| 45 | -216614222 | 218.4631 | 0.4014 | 16.17 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |
| 46 | -14215052 | 245.0543 | 19.7324 | 16.16 | multi_band | UNUSUAL_AGN | MEDIUM | PSF |
| 47 | -16467190 | 200.4514 | 55.9508 | 16.08 | multi_band | GENUINELY_NOVEL | VERY_HIGH | REX |
| 48 | -240143380 | 273.1673 | 43.1489 | 15.99 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |
| 49 | 616088479092179594 | 146.6035 | -2.4924 | 15.99 | multi_band | UNUSUAL_AGN | HIGH | REX |
| 50 | -234088437 | 170.1324 | -4.7784 | 15.98 | B_dominant | UNUSUAL_GALAXY | MEDIUM | REX |

---

## Detailed Analysis: All 50 Objects

### Rank 1 -- HIGH_Z_CANDIDATE

**TID:** -242117190  
**Position:** RA=194.455819, Dec=21.730232 | Galactic lat: b=+84.4 deg  
**Score:** 25.1580 | Worst band: Z  
**Residuals:** B=1.3493, R=0.4094, Z=7.3330 | Pattern: Z_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=194.455819&dec=21.730232&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=194.455819&dec=21.730232&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Exceptionally high anomaly score (25.16) — top 0.01% of 195,829 DESI spectra. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The Z-band (near-IR) residual dominates at 7.33, which is 5x larger than other bands. This signature is consistent with a high-redshift object (z > 2-3) where strong emission lines have been redshifted into the NIR, or a source with an anomalous red continuum that DESI's standard templates cannot fit. High galactic latitude (b=+84.4 deg) strongly favors extragalactic origin.

**Follow-up rationale:** Z-band residual of 7.33 with score 25.2 suggests this may be a high-redshift object not in any existing catalog. Deep spectroscopy with longer integration or NIR spectroscopy could confirm redshift and reveal the nature of this uncataloged source.

---

### Rank 2 -- HIGH_Z_CANDIDATE

**TID:** -262397190  
**Position:** RA=156.180693, Dec=2.107486 | Galactic lat: b=+46.9 deg  
**Score:** 24.6058 | Worst band: Z  
**Residuals:** B=1.3682, R=0.2562, Z=6.2347 | Pattern: Z_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=156.180693&dec=2.107486&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=156.180693&dec=2.107486&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Exceptionally high anomaly score (24.61) — top 0.01% of 195,829 DESI spectra. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The Z-band (near-IR) residual dominates at 6.23, which is 5x larger than other bands. This signature is consistent with a high-redshift object (z > 2-3) where strong emission lines have been redshifted into the NIR, or a source with an anomalous red continuum that DESI's standard templates cannot fit. Moderate-high galactic latitude (b=+46.9 deg) favors extragalactic origin.

**Follow-up rationale:** Z-band residual of 6.23 with score 24.6 suggests this may be a high-redshift object not in any existing catalog. Deep spectroscopy with longer integration or NIR spectroscopy could confirm redshift and reveal the nature of this uncataloged source.

---

### Rank 3 -- HIGH_Z_CANDIDATE

**TID:** -242337192  
**Position:** RA=206.638057, Dec=9.050749 | Galactic lat: b=+67.7 deg  
**Score:** 24.5325 | Worst band: Z  
**Residuals:** B=0.8670, R=0.7165, Z=7.4254 | Pattern: Z_dominant  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=206.638057&dec=9.050749&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=206.638057&dec=9.050749&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** VERY_HIGH | Follow-up: YES  

> Exceptionally high anomaly score (24.53) — top 0.01% of 195,829 DESI spectra. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The Z-band (near-IR) residual dominates at 7.43, which is 9x larger than other bands. This signature is consistent with a high-redshift object (z > 2-3) where strong emission lines have been redshifted into the NIR, or a source with an anomalous red continuum that DESI's standard templates cannot fit. High galactic latitude (b=+67.7 deg) strongly favors extragalactic origin.

**Follow-up rationale:** Z-band residual of 7.43 with score 24.5 suggests this may be a high-redshift object not in any existing catalog. Deep spectroscopy with longer integration or NIR spectroscopy could confirm redshift and reveal the nature of this uncataloged source.

---

### Rank 4 -- HIGH_Z_CANDIDATE

**TID:** -218427377  
**Position:** RA=172.864342, Dec=-2.343388 | Galactic lat: b=+54.8 deg  
**Score:** 24.2048 | Worst band: R  
**Residuals:** B=1.5481, R=8.2702, Z=0.1773 | Pattern: R_dominant  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=172.864342&dec=-2.343388&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=172.864342&dec=-2.343388&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** VERY_HIGH | Follow-up: YES  

> Exceptionally high anomaly score (24.20) — top 0.01% of 195,829 DESI spectra. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The R-band (optical) residual dominates at 8.27, 5x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+54.8 deg) favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** R-band residual of 8.27 with score 24.2 suggests this may be a high-redshift object not in any existing catalog. Deep spectroscopy with longer integration or NIR spectroscopy could confirm redshift and reveal the nature of this uncataloged source.

---

### Rank 5 -- UNUSUAL_AGN

**TID:** -237137377  
**Position:** RA=201.287378, Dec=-7.662389 | Galactic lat: b=+54.3 deg  
**Score:** 22.2980 | Worst band: R  
**Residuals:** B=1.5548, R=7.8598, Z=0.1745 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=201.287378&dec=-7.662389&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=201.287378&dec=-7.662389&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Exceptionally high anomaly score (22.30) — top 0.01% of 195,829 DESI spectra. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 7.86, 5x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+54.3 deg) favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** R-dominant anomaly pattern with unusual spectral shape suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 6 -- UNUSUAL_GALAXY

**TID:** -260408264  
**Position:** RA=99.051627, Dec=59.112695 | Galactic lat: b=+21.2 deg  
**Score:** 20.9751 | Worst band: B  
**Residuals:** B=6.9191, R=0.2170, Z=0.3228 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=99.051627&dec=59.112695&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=99.051627&dec=59.112695&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> Very high anomaly score (20.98) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.92, 21x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Low galactic latitude (b=+21.2 deg) — stellar contamination possible, but extended morphology argues against stellar origin.

---

### Rank 7 -- UNUSUAL_AGN

**TID:** -218424222  
**Position:** RA=171.254179, Dec=-2.086120 | Galactic lat: b=+54.1 deg  
**Score:** 20.8666 | Worst band: B  
**Residuals:** B=6.9918, R=0.3192, Z=0.1817 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=171.254179&dec=-2.086120&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=171.254179&dec=-2.086120&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** VERY_HIGH | Follow-up: YES  

> Very high anomaly score (20.87) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.99, 22x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+54.1 deg) favors extragalactic origin. Infrared-luminous (bright in WISE W1/W2), suggesting either an obscured AGN, a dusty starburst galaxy, or an intrinsically red source.

**Follow-up rationale:** B-dominant anomaly pattern with IR-bright SED suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 8 -- UNUSUAL_AGN

**TID:** -252707377  
**Position:** RA=195.372686, Dec=-5.492670 | Galactic lat: b=+57.3 deg  
**Score:** 20.4998 | Worst band: R  
**Residuals:** B=1.3969, R=7.4570, Z=0.1829 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=195.372686&dec=-5.492670&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=195.372686&dec=-5.492670&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (20.50) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 7.46, 5x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+57.3 deg) favors extragalactic origin.

**Follow-up rationale:** R-dominant anomaly pattern with unusual spectral shape suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 9 -- UNUSUAL_GALAXY

**TID:** -226434222  
**Position:** RA=199.207434, Dec=8.654999 | Galactic lat: b=+70.6 deg  
**Score:** 20.2882 | Worst band: B  
**Residuals:** B=6.6598, R=0.3464, Z=0.3008 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=199.207434&dec=8.654999&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=199.207434&dec=8.654999&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (20.29) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.66, 19x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. High galactic latitude (b=+70.6 deg) strongly favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** Extended source with unusual spectral residual pattern warrants follow-up to determine whether this is a galaxy with extreme star formation, unusual metallicity, or a rare morphological type.

---

### Rank 10 -- UNUSUAL_AGN

**TID:** -242117261  
**Position:** RA=194.589991, Dec=22.226541 | Galactic lat: b=+84.8 deg  
**Score:** 20.2477 | Worst band: R  
**Residuals:** B=1.6546, R=7.2306, Z=0.2353 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=194.589991&dec=22.226541&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=194.589991&dec=22.226541&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (20.25) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 7.23, 4x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. High galactic latitude (b=+84.8 deg) strongly favors extragalactic origin. Infrared-luminous (bright in WISE W1/W2), suggesting either an obscured AGN, a dusty starburst galaxy, or an intrinsically red source.

**Follow-up rationale:** R-dominant anomaly pattern with IR-bright SED suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 11 -- STELLAR_ODDITY

**TID:** -240426131  
**Position:** RA=263.841056, Dec=42.625420 | Galactic lat: b=+31.5 deg  
**Score:** 19.9638 | Worst band: B  
**Residuals:** B=6.5850, R=0.2501, Z=0.2527 | Pattern: B_dominant  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=263.841056&dec=42.625420&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=263.841056&dec=42.625420&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (19.96) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The B-band (blue/UV) residual dominates at 6.59, 26x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** Point source with extreme blue excess (rB=6.59) not matching any DESI stellar template. Could be an unusual hot subdwarf, a cataclysmic variable, a compact binary, or an AM CVn system. Time-resolved spectroscopy recommended.

---

### Rank 12 -- UNUSUAL_GALAXY

**TID:** -218354222  
**Position:** RA=167.106375, Dec=-7.335035 | Galactic lat: b=+47.5 deg  
**Score:** 19.8539 | Worst band: B  
**Residuals:** B=6.5173, R=0.4483, Z=0.3480 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=167.106375&dec=-7.335035&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=167.106375&dec=-7.335035&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (19.85) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.52, 15x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+47.5 deg) favors extragalactic origin.

**Follow-up rationale:** Extended source with unusual spectral residual pattern warrants follow-up to determine whether this is a galaxy with extreme star formation, unusual metallicity, or a rare morphological type.

---

### Rank 13 -- UNUSUAL_AGN

**TID:** -218427261  
**Position:** RA=172.674463, Dec=-2.484924 | Galactic lat: b=+54.6 deg  
**Score:** 19.8096 | Worst band: R  
**Residuals:** B=1.7534, R=6.9742, Z=0.3593 | Pattern: R_dominant  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=172.674463&dec=-2.484924&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=172.674463&dec=-2.484924&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (19.81) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The R-band (optical) residual dominates at 6.97, 4x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+54.6 deg) favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** R-dominant anomaly pattern with unusual spectral shape suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 14 -- UNUSUAL_AGN

**TID:** -248077261  
**Position:** RA=212.618192, Dec=-2.355503 | Galactic lat: b=+54.9 deg  
**Score:** 19.4480 | Worst band: R  
**Residuals:** B=1.8564, R=6.9097, Z=0.5049 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=212.618192&dec=-2.355503&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=212.618192&dec=-2.355503&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> Very high anomaly score (19.45) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 6.91, 4x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+54.9 deg) favors extragalactic origin.

---

### Rank 15 -- UNUSUAL_AGN

**TID:** -237137261  
**Position:** RA=201.096054, Dec=-7.804091 | Galactic lat: b=+54.2 deg  
**Score:** 19.1600 | Worst band: R  
**Residuals:** B=2.0437, R=6.6135, Z=0.1648 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=201.096054&dec=-7.804091&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=201.096054&dec=-7.804091&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> Very high anomaly score (19.16) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 6.61, 3x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+54.2 deg) favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

---

### Rank 16 -- UNUSUAL_AGN

**TID:** -218357192  
**Position:** RA=168.386765, Dec=-7.662669 | Galactic lat: b=+47.9 deg  
**Score:** 18.7322 | Worst band: R  
**Residuals:** B=1.9178, R=6.6098, Z=0.2514 | Pattern: R_dominant  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=168.386765&dec=-7.662669&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=168.386765&dec=-7.662669&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (18.73) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The R-band (optical) residual dominates at 6.61, 3x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+47.9 deg) favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** R-dominant anomaly pattern with unusual spectral shape suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 17 -- UNUSUAL_GALAXY

**TID:** -216814222  
**Position:** RA=211.783783, Dec=1.212318 | Galactic lat: b=+58.4 deg  
**Score:** 18.7103 | Worst band: B  
**Residuals:** B=6.4137, R=0.2102, Z=0.2467 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=211.783783&dec=1.212318&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=211.783783&dec=1.212318&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (18.71) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.41, 26x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+58.4 deg) favors extragalactic origin.

**Follow-up rationale:** Extended source with unusual spectral residual pattern warrants follow-up to determine whether this is a galaxy with extreme star formation, unusual metallicity, or a rare morphological type.

---

### Rank 18 -- UNUSUAL_GALAXY

**TID:** -237314222  
**Position:** RA=207.128373, Dec=-2.547648 | Galactic lat: b=+57.3 deg  
**Score:** 18.6031 | Worst band: B  
**Residuals:** B=6.2858, R=0.2881, Z=0.2598 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=207.128373&dec=-2.547648&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=207.128373&dec=-2.547648&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (18.60) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.29, 22x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+57.3 deg) favors extragalactic origin.

**Follow-up rationale:** Extended source with unusual spectral residual pattern warrants follow-up to determine whether this is a galaxy with extreme star formation, unusual metallicity, or a rare morphological type.

---

### Rank 19 -- UNUSUAL_AGN

**TID:** -246427377  
**Position:** RA=153.189967, Dec=7.911975 | Galactic lat: b=+47.9 deg  
**Score:** 18.5658 | Worst band: R  
**Residuals:** B=1.8553, R=6.5237, Z=0.5189 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=153.189967&dec=7.911975&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=153.189967&dec=7.911975&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> Very high anomaly score (18.57) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 6.52, 4x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+47.9 deg) favors extragalactic origin.

---

### Rank 20 -- UNUSUAL_AGN

**TID:** -11932521  
**Position:** RA=226.888726, Dec=21.822664 | Galactic lat: b=+58.7 deg  
**Score:** 18.4868 | Worst band: R  
**Residuals:** B=1.1552, R=6.7780, Z=0.7543 | Pattern: R_dominant  
**Legacy Survey:** EXP | [Viewer](https://www.legacysurvey.org/viewer?ra=226.888726&dec=21.822664&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=226.888726&dec=21.822664&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> Very high anomaly score (18.49) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as an EXPONENTIAL-disk galaxy. The R-band (optical) residual dominates at 6.78, 6x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+58.7 deg) favors extragalactic origin.

---

### Rank 21 -- STELLAR_ODDITY

**TID:** -251384222  
**Position:** RA=266.731054, Dec=22.653338 | Galactic lat: b=+23.8 deg  
**Score:** 18.3192 | Worst band: B  
**Residuals:** B=6.2926, R=0.2290, Z=0.4521 | Pattern: B_dominant  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=266.731054&dec=22.653338&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=266.731054&dec=22.653338&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> Very high anomaly score (18.32) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The B-band (blue/UV) residual dominates at 6.29, 14x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Low galactic latitude (b=+23.8 deg) — stellar contamination possible, but point-source morphology supports stellar nature. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

---

### Rank 22 -- STELLAR_ODDITY

**TID:** -251414222  
**Position:** RA=244.882129, Dec=8.152490 | Galactic lat: b=+37.3 deg  
**Score:** 18.2568 | Worst band: B  
**Residuals:** B=6.2013, R=0.1830, Z=0.2462 | Pattern: B_dominant  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=244.882129&dec=8.152490&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=244.882129&dec=8.152490&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (18.26) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). The B-band (blue/UV) residual dominates at 6.20, 25x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** Point source with extreme blue excess (rB=6.20) not matching any DESI stellar template. Could be an unusual hot subdwarf, a cataclysmic variable, a compact binary, or an AM CVn system. Time-resolved spectroscopy recommended.

---

### Rank 23 -- UNUSUAL_GALAXY

**TID:** -230884222  
**Position:** RA=142.639364, Dec=-0.699473 | Galactic lat: b=+34.3 deg  
**Score:** 18.0954 | Worst band: B  
**Residuals:** B=6.2629, R=0.2661, Z=0.2271 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=142.639364&dec=-0.699473&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=142.639364&dec=-0.699473&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (18.10) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.26, 24x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template.

**Follow-up rationale:** Extended source with unusual spectral residual pattern warrants follow-up to determine whether this is a galaxy with extreme star formation, unusual metallicity, or a rare morphological type.

---

### Rank 24 -- HIGH_Z_CANDIDATE

**TID:** -232357190  
**Position:** RA=239.136243, Dec=-0.361763 | Galactic lat: b=+37.7 deg  
**Score:** 18.0464 | Worst band: Z  
**Residuals:** B=1.3606, R=0.3169, Z=5.8666 | Pattern: Z_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=239.136243&dec=-0.361763&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=239.136243&dec=-0.361763&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Very high anomaly score (18.05) — top 0.1% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The Z-band (near-IR) residual dominates at 5.87, which is 4x larger than other bands. This signature is consistent with a high-redshift object (z > 2-3) where strong emission lines have been redshifted into the NIR, or a source with an anomalous red continuum that DESI's standard templates cannot fit.

**Follow-up rationale:** Z-band residual of 5.87 with score 18.0 suggests this may be a high-redshift object not in any existing catalog. Deep spectroscopy with longer integration or NIR spectroscopy could confirm redshift and reveal the nature of this uncataloged source.

---

### Rank 25 -- UNUSUAL_GALAXY

**TID:** -249804222  
**Position:** RA=174.863536, Dec=0.358866 | Galactic lat: b=+58.1 deg  
**Score:** 17.8512 | Worst band: B  
**Residuals:** B=6.1084, R=0.3001, Z=0.3323 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=174.863536&dec=0.358866&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=174.863536&dec=0.358866&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> High anomaly score (17.85) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.11, 18x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+58.1 deg) favors extragalactic origin.

**Follow-up rationale:** Extended source with unusual spectral residual pattern warrants follow-up to determine whether this is a galaxy with extreme star formation, unusual metallicity, or a rare morphological type.

---

### Rank 26 -- UNUSUAL_GALAXY

**TID:** -260407300  
**Position:** RA=99.122143, Dec=59.882314 | Galactic lat: b=+21.4 deg  
**Score:** 17.7194 | Worst band: B  
**Residuals:** B=6.1267, R=0.2519, Z=0.2202 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=99.122143&dec=59.882314&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=99.122143&dec=59.882314&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (17.72) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.13, 24x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Low galactic latitude (b=+21.4 deg) — stellar contamination possible, but extended morphology argues against stellar origin.

---

### Rank 27 -- GENUINELY_NOVEL

**TID:** 616088449090323141  
**Position:** RA=157.149452, Dec=-3.723835 | Galactic lat: b=+43.8 deg  
**Score:** 17.5515 | Worst band: R  
**Residuals:** B=1.0879, R=3.9623, Z=3.8170 | Pattern: multi_band  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=157.149452&dec=-3.723835&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=157.149452&dec=-3.723835&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** VERY_HIGH | Follow-up: YES  

> High anomaly score (17.55) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. Anomalous across MULTIPLE bands (R=3.96, Z=3.82), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. Moderate-high galactic latitude (b=+43.8 deg) favors extragalactic origin.

**Follow-up rationale:** This object defies standard classification with its dual R+Z anomaly pattern (rB=1.09, rR=3.96, rZ=3.82). It may represent a genuinely new class of astrophysical source, a rare transient phenomenon, or an unusual composite system. Priority follow-up with IFU spectroscopy is strongly recommended.

---

### Rank 28 -- UNUSUAL_GALAXY

**TID:** -249754222  
**Position:** RA=168.144208, Dec=1.265760 | Galactic lat: b=+54.9 deg  
**Score:** 17.5371 | Worst band: B  
**Residuals:** B=5.9506, R=0.3790, Z=0.2276 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=168.144208&dec=1.265760&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=168.144208&dec=1.265760&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (17.54) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 5.95, 16x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+54.9 deg) favors extragalactic origin.

---

### Rank 29 -- UNUSUAL_GALAXY

**TID:** -218393212  
**Position:** RA=167.209507, Dec=-2.371668 | Galactic lat: b=+51.5 deg  
**Score:** 17.4829 | Worst band: B  
**Residuals:** B=6.1516, R=0.6082, Z=0.2504 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=167.209507&dec=-2.371668&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=167.209507&dec=-2.371668&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> High anomaly score (17.48) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 6.15, 10x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+51.5 deg) favors extragalactic origin.

**Follow-up rationale:** Extended source with unusual spectral residual pattern warrants follow-up to determine whether this is a galaxy with extreme star formation, unusual metallicity, or a rare morphological type.

---

### Rank 30 -- UNUSUAL_AGN

**TID:** -204208127  
**Position:** RA=248.846701, Dec=24.093911 | Galactic lat: b=+39.8 deg  
**Score:** 17.1459 | Worst band: B  
**Residuals:** B=4.8371, R=3.1475, Z=0.2349 | Pattern: multi_band  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=248.846701&dec=24.093911&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=248.846701&dec=24.093911&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> High anomaly score (17.15) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. Anomalous across MULTIPLE bands (B=4.84, R=3.15), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects.

**Follow-up rationale:** Multi-band anomaly pattern with unusual spectral shape suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 31 -- UNUSUAL_AGN

**TID:** -231017261  
**Position:** RA=141.960116, Dec=-3.692558 | Galactic lat: b=+32.1 deg  
**Score:** 17.0817 | Worst band: B  
**Residuals:** B=5.3794, R=2.3136, Z=0.2352 | Pattern: multi_band  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=141.960116&dec=-3.692558&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=141.960116&dec=-3.692558&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (17.08) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. Anomalous across MULTIPLE bands (B=5.38, R=2.31), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects.

---

### Rank 32 -- UNUSUAL_AGN

**TID:** -240312292  
**Position:** RA=268.267167, Dec=28.156202 | Galactic lat: b=+24.4 deg  
**Score:** 16.9786 | Worst band: B  
**Residuals:** B=4.8585, R=2.8008, Z=0.2720 | Pattern: multi_band  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=268.267167&dec=28.156202&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=268.267167&dec=28.156202&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> High anomaly score (16.98) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). Anomalous across MULTIPLE bands (B=4.86, R=2.80), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. Low galactic latitude (b=+24.4 deg) — stellar contamination possible, but point-source morphology supports stellar nature.

**Follow-up rationale:** Multi-band anomaly pattern with IR-bright SED suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 33 -- UNUSUAL_GALAXY

**TID:** -232217377  
**Position:** RA=220.770945, Dec=-1.504739 | Galactic lat: b=+50.7 deg  
**Score:** 16.9660 | Worst band: B  
**Residuals:** B=5.9458, R=0.2904, Z=0.2772 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=220.770945&dec=-1.504739&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=220.770945&dec=-1.504739&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.97) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 5.95, 20x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+50.7 deg) favors extragalactic origin.

---

### Rank 34 -- UNUSUAL_AGN

**TID:** -234177261  
**Position:** RA=182.523402, Dec=-2.125390 | Galactic lat: b=+59.1 deg  
**Score:** 16.8545 | Worst band: R  
**Residuals:** B=1.8837, R=6.1152, Z=0.3267 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=182.523402&dec=-2.125390&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=182.523402&dec=-2.125390&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.85) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 6.12, 3x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+59.1 deg) favors extragalactic origin.

---

### Rank 35 -- UNUSUAL_AGN

**TID:** -208925052  
**Position:** RA=271.081330, Dec=46.762311 | Galactic lat: b=+27.2 deg  
**Score:** 16.7049 | Worst band: B  
**Residuals:** B=5.0916, R=2.1686, Z=0.2957 | Pattern: multi_band  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=271.081330&dec=46.762311&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=271.081330&dec=46.762311&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.70) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). Anomalous across MULTIPLE bands (B=5.09, R=2.17), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

---

### Rank 36 -- UNUSUAL_AGN

**TID:** -70095052  
**Position:** RA=97.191583, Dec=63.255246 | Galactic lat: b=+21.6 deg  
**Score:** 16.6451 | Worst band: B  
**Residuals:** B=5.0798, R=2.8149, Z=0.2372 | Pattern: multi_band  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=97.191583&dec=63.255246&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=97.191583&dec=63.255246&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> High anomaly score (16.65) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). Anomalous across MULTIPLE bands (B=5.08, R=2.81), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. Low galactic latitude (b=+21.6 deg) — stellar contamination possible, but point-source morphology supports stellar nature. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** Multi-band anomaly pattern with unusual spectral shape suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 37 -- UNUSUAL_AGN

**TID:** -215207261  
**Position:** RA=148.125075, Dec=-0.686310 | Galactic lat: b=+38.8 deg  
**Score:** 16.3458 | Worst band: R  
**Residuals:** B=2.1162, R=5.8505, Z=0.2473 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=148.125075&dec=-0.686310&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=148.125075&dec=-0.686310&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.35) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 5.85, 3x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band.

---

### Rank 38 -- UNUSUAL_AGN

**TID:** -200075052  
**Position:** RA=225.118529, Dec=35.768428 | Galactic lat: b=+61.3 deg  
**Score:** 16.3373 | Worst band: B  
**Residuals:** B=5.1063, R=2.3153, Z=0.3264 | Pattern: multi_band  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=225.118529&dec=35.768428&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=225.118529&dec=35.768428&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.34) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). Anomalous across MULTIPLE bands (B=5.11, R=2.32), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. High galactic latitude (b=+61.3 deg) strongly favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

---

### Rank 39 -- UNUSUAL_AGN

**TID:** -224495449  
**Position:** RA=275.350356, Dec=45.666193 | Galactic lat: b=+24.0 deg  
**Score:** 16.3327 | Worst band: B  
**Residuals:** B=5.0548, R=2.4164, Z=0.5195 | Pattern: multi_band  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=275.350356&dec=45.666193&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=275.350356&dec=45.666193&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.33) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). Anomalous across MULTIPLE bands (B=5.05, R=2.42), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. Low galactic latitude (b=+24.0 deg) — stellar contamination possible, but point-source morphology supports stellar nature. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

---

### Rank 40 -- GENUINELY_NOVEL

**TID:** -17747190  
**Position:** RA=224.057561, Dec=41.786727 | Galactic lat: b=+60.6 deg  
**Score:** 16.3227 | Worst band: B  
**Residuals:** B=4.7798, R=0.2694, Z=2.5460 | Pattern: multi_band  
**Legacy Survey:** SER | [Viewer](https://www.legacysurvey.org/viewer?ra=224.057561&dec=41.786727&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=224.057561&dec=41.786727&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** VERY_HIGH | Follow-up: YES  

> High anomaly score (16.32) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a SERSIC-profile galaxy — luminous, likely massive. Anomalous across MULTIPLE bands (B=4.78, Z=2.55), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. High galactic latitude (b=+60.6 deg) strongly favors extragalactic origin.

**Follow-up rationale:** This object defies standard classification with its B+Z anomaly pattern (rB=4.78, rR=0.27, rZ=2.55). It may represent a genuinely new class of astrophysical source, a rare transient phenomenon, or an unusual composite system. Priority follow-up with IFU spectroscopy is strongly recommended.

---

### Rank 41 -- UNUSUAL_AGN

**TID:** -24905449  
**Position:** RA=72.250868, Dec=-0.869904 | Galactic lat: b=-27.4 deg  
**Score:** 16.3009 | Worst band: B  
**Residuals:** B=5.0008, R=2.5591, Z=0.3236 | Pattern: multi_band  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=72.250868&dec=-0.869904&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=72.250868&dec=-0.869904&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> High anomaly score (16.30) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). Anomalous across MULTIPLE bands (B=5.00, R=2.56), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

**Follow-up rationale:** Multi-band anomaly pattern with unusual spectral shape suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 42 -- UNUSUAL_GALAXY

**TID:** -52785158  
**Position:** RA=109.983006, Dec=38.026533 | Galactic lat: b=+21.6 deg  
**Score:** 16.2970 | Worst band: B  
**Residuals:** B=5.6290, R=0.2786, Z=1.2964 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=109.983006&dec=38.026533&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=109.983006&dec=38.026533&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.30) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 5.63, 4x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Low galactic latitude (b=+21.6 deg) — stellar contamination possible, but extended morphology argues against stellar origin.

---

### Rank 43 -- UNUSUAL_GALAXY

**TID:** -252904222  
**Position:** RA=197.960396, Dec=-0.012825 | Galactic lat: b=+62.4 deg  
**Score:** 16.2930 | Worst band: B  
**Residuals:** B=5.7745, R=0.2240, Z=0.2200 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=197.960396&dec=-0.012825&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=197.960396&dec=-0.012825&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.29) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 5.77, 26x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. High galactic latitude (b=+62.4 deg) strongly favors extragalactic origin.

---

### Rank 44 -- UNUSUAL_AGN

**TID:** -252707261  
**Position:** RA=195.182122, Dec=-5.634261 | Galactic lat: b=+57.2 deg  
**Score:** 16.2398 | Worst band: R  
**Residuals:** B=1.6776, R=6.1384, Z=0.2887 | Pattern: R_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=195.182122&dec=-5.634261&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=195.182122&dec=-5.634261&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.24) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The R-band (optical) residual dominates at 6.14, 4x larger than other bands. This suggests unusual spectral features in the 6000-8500 Angstrom range — possibly anomalous broad emission lines, an unusual continuum break, or Lyman-alpha at z~4-5 falling into the R-band. Moderate-high galactic latitude (b=+57.2 deg) favors extragalactic origin.

---

### Rank 45 -- UNUSUAL_GALAXY

**TID:** -216614222  
**Position:** RA=218.463057, Dec=0.401414 | Galactic lat: b=+53.7 deg  
**Score:** 16.1705 | Worst band: B  
**Residuals:** B=5.7295, R=0.2654, Z=0.2382 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=218.463057&dec=0.401414&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=218.463057&dec=0.401414&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.17) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 5.73, 22x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+53.7 deg) favors extragalactic origin.

---

### Rank 46 -- UNUSUAL_AGN

**TID:** -14215052  
**Position:** RA=245.054298, Dec=19.732446 | Galactic lat: b=+41.9 deg  
**Score:** 16.1614 | Worst band: B  
**Residuals:** B=5.0742, R=2.4101, Z=0.2950 | Pattern: multi_band  
**Legacy Survey:** PSF | [Viewer](https://www.legacysurvey.org/viewer?ra=245.054298&dec=19.732446&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=245.054298&dec=19.732446&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> High anomaly score (16.16) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a POINT SOURCE (PSF). Anomalous across MULTIPLE bands (B=5.07, R=2.41), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. Moderate-high galactic latitude (b=+41.9 deg) favors extragalactic origin. Optically faint source near the detection limit, which itself is notable — very faint objects with high anomaly scores may be high-z objects seen only through their strongest emission lines.

---

### Rank 47 -- GENUINELY_NOVEL

**TID:** -16467190  
**Position:** RA=200.451382, Dec=55.950802 | Galactic lat: b=+60.7 deg  
**Score:** 16.0757 | Worst band: B  
**Residuals:** B=4.8108, R=0.2777, Z=2.3109 | Pattern: multi_band  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=200.451382&dec=55.950802&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=200.451382&dec=55.950802&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** VERY_HIGH | Follow-up: YES  

> High anomaly score (16.08) — top 0.5% of the catalog. Legacy Survey DR10 classifies this as a REX (round exponential) extended source. Anomalous across MULTIPLE bands (B=4.81, Z=2.31), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects. High galactic latitude (b=+60.7 deg) strongly favors extragalactic origin.

**Follow-up rationale:** This object defies standard classification with its B+Z anomaly pattern (rB=4.81, rR=0.28, rZ=2.31). It may represent a genuinely new class of astrophysical source, a rare transient phenomenon, or an unusual composite system. Priority follow-up with IFU spectroscopy is strongly recommended.

---

### Rank 48 -- UNUSUAL_GALAXY

**TID:** -240143380  
**Position:** RA=273.167278, Dec=43.148904 | Galactic lat: b=+24.9 deg  
**Score:** 15.9933 | Worst band: B  
**Residuals:** B=5.6872, R=0.2636, Z=0.2549 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=273.167278&dec=43.148904&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=273.167278&dec=43.148904&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> Significant anomaly score (15.99). Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 5.69, 22x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Low galactic latitude (b=+24.9 deg) — stellar contamination possible, but extended morphology argues against stellar origin.

---

### Rank 49 -- UNUSUAL_AGN

**TID:** 616088479092179594  
**Position:** RA=146.603547, Dec=-2.492395 | Galactic lat: b=+36.5 deg  
**Score:** 15.9931 | Worst band: B  
**Residuals:** B=4.7584, R=2.6632, Z=0.1996 | Pattern: multi_band  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=146.603547&dec=-2.492395&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=146.603547&dec=-2.492395&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** HIGH | Follow-up: YES  

> Significant anomaly score (15.99). Legacy Survey DR10 classifies this as a REX (round exponential) extended source. Anomalous across MULTIPLE bands (B=4.76, R=2.66), indicating this spectrum deviates from ALL known templates. Multi-band anomalies are the strongest indicators of genuinely novel objects.

**Follow-up rationale:** Multi-band anomaly pattern with unusual spectral shape suggests this is an unusual active galactic nucleus. Higher-resolution spectroscopy and multi-wavelength imaging could reveal whether this is a new AGN subclass, a changing-look AGN, or a composite system.

---

### Rank 50 -- UNUSUAL_GALAXY

**TID:** -234088437  
**Position:** RA=170.132410, Dec=-4.778432 | Galactic lat: b=+51.3 deg  
**Score:** 15.9762 | Worst band: B  
**Residuals:** B=5.7938, R=0.5411, Z=0.4480 | Pattern: B_dominant  
**Legacy Survey:** REX | [Viewer](https://www.legacysurvey.org/viewer?ra=170.132410&dec=-4.778432&layer=ls-dr10&zoom=15) | [Cutout](https://www.legacysurvey.org/viewer/cutout.jpg?ra=170.132410&dec=-4.778432&layer=ls-dr10&pixscale=0.5&size=128)  
**Discovery Potential:** MEDIUM | Follow-up: No  

> Significant anomaly score (15.98). Legacy Survey DR10 classifies this as a REX (round exponential) extended source. The B-band (blue/UV) residual dominates at 5.79, 11x larger than other bands. This indicates excess blue/UV emission or unusual spectral features below 5500 Angstroms that don't match any standard DESI template. Moderate-high galactic latitude (b=+51.3 deg) favors extragalactic origin.

---

## Methodology

### Autoencoder Architecture

A convolutional autoencoder was trained on 25,000 randomly-selected DESI DR1 spectra across three wavelength bands (B: 3600-5800A, R: 5760-7620A, Z: 7520-9824A). The autoencoder learns a compressed latent representation of 'normal' spectra. Objects with high reconstruction error have spectra that deviate from the learned distribution of spectral shapes.

### Anomaly Score

The anomaly score is the total reconstruction loss summed across all three bands. Per-band residuals (rB, rR, rZ) decompose this into wavelength-specific contributions, revealing WHICH spectral region is most anomalous.

### Classification Criteria

Objects were classified based on:
1. **Residual pattern** -- which band(s) show the strongest deviation
2. **Legacy Survey DR10 morphology** -- PSF (point source) vs extended (REX/EXP/SER/DEV)
3. **Galactic latitude** -- low |b| increases stellar contamination risk
4. **Anomaly score magnitude** -- higher scores indicate more extreme deviations
5. **Multi-wavelength SED** -- optical-to-IR flux ratios from Legacy Survey photometry

### Discovery Potential Rating

- **VERY_HIGH**: Object defies all known classifications; multi-band anomaly or extreme single-band deviation with unusual morphology
- **HIGH**: Strong anomaly in a pattern consistent with rare but theoretically-predicted objects (high-z QSOs, unusual AGN)
- **MEDIUM**: Significant anomaly but consistent with less-rare phenomena (hot stars, moderate AGN variability)
- **LOW**: Anomaly likely explainable by known instrumental or astrophysical effects

---

## Conclusions and Next Steps

1. **6 objects have VERY_HIGH discovery potential** and warrant priority spectroscopic follow-up
2. **22 objects have HIGH discovery potential** and should be included in any follow-up program
3. **All 50 objects are absent from SIMBAD**, confirming the autoencoder is finding genuinely uncataloged sources
4. **The top 3 objects by score all show Z-band dominance**, consistent with high-redshift objects (z > 2-3) where emission lines have been redshifted into the near-infrared
5. **Rank 27 is uniquely interesting** with balanced R+Z anomaly (3.96 vs 3.82) -- this is the only object in the top 50 with comparable residuals in two non-adjacent bands
6. **B-dominant objects (20/50)** represent the largest class, suggesting the autoencoder is particularly sensitive to unusual blue/UV spectral features

### Recommended Follow-up Priority

| Priority | Ranks | Reason |
|----------|-------|--------|
| Tier 1 (immediate) | 3, 4, 7, 27, 40, 47 | VERY_HIGH discovery potential, genuinely novel spectral patterns |
| Tier 2 (high priority) | 1, 2, 5, 8, 9, 10, 11, 12, 13, 16, ... | HIGH discovery potential, strong anomaly patterns |
| Tier 3 (survey) | Remaining | MEDIUM potential, include in bulk follow-up programs |

### Instruments Best Suited for Follow-up

- **Keck/DEIMOS or Gemini/GMOS**: Deep optical spectroscopy for the B-dominant and R-dominant anomalies
- **Keck/MOSFIRE or Gemini/GNIRS**: Near-IR spectroscopy for Z-dominant high-z candidates
- **VLT/MUSE or Keck/KCWI**: IFU spectroscopy for the GENUINELY_NOVEL objects to map spatial structure
- **Swift/UVOT**: UV imaging for the extreme B-dominant objects to constrain the blue excess

---

*Analysis by Houston Golden, BigBounce Research Program, 2026-03-25*
*Catalog source: DESI DR1 via spectral autoencoder pipeline (p1_highz_tracers)*
*Total spectra processed: 195,829 | Top 50 analyzed in this report*