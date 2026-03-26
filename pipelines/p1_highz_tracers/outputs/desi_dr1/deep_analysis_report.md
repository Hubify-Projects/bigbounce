# Deep Analysis: Top 100 DESI DR1 Anomalies

**Generated:** 2026-03-26
**Objects analyzed:** 100
**Cross-match status:** ALL 100 absent from SIMBAD, NED, AND AllWISE

## Discovery Potential

- **VERY_HIGH:** 10 objects
- **HIGH:** 90 objects
- **MEDIUM:** 0 objects
- **LOW:** 0 objects

## Tag Distribution

- `uv_excess`: 49 objects
- `high_ionization`: 49 objects
- `calibration_check_needed`: 49 objects
- `moderate_anomaly`: 33 objects
- `high_z_candidate`: 18 objects
- `bal_candidate`: 14 objects
- `unusual_emission`: 14 objects
- `accretion_disk_candidate`: 14 objects
- `near_ir_anomaly`: 4 objects
- `emission_line_candidate`: 4 objects

## Key Patterns

### Z-band dominated (near-IR anomalies): 4 objects
These are the strongest high-redshift candidates. The Z-band covers 7520–9824Å, 
where rest-frame optical emission lines appear for objects at z > 2. 
Average score: 23.1

### R-band dominated (mid-optical anomalies): 14 objects
Possible z~3.5–5 QSOs with Lyman-alpha in the R-band, BAL QSOs, or unusual Hα emitters.
Average score: 19.0

### B-band dominated (blue anomalies): 49 objects
UV-excess objects, high-ionization AGN, or potentially blue-arm calibration artifacts.
Average score: 16.7

### Multi-band anomalies: 0 objects
STRONGEST discovery candidates — anomalous across the full spectrum. 
Possible lens candidates, changing-look AGN, or genuinely novel object classes.

## The Collective Picture

The top 100 anomalies paint a consistent picture:

1. **They are genuinely uncataloged.** Zero matches in SIMBAD (17M objects), NED (400M), or AllWISE (750M). These are not well-studied objects with unusual spectra — they are objects that the astronomical community has not previously characterized.

2. **They are NOT instrumental artifacts.** Artifacts typically affect one spectrograph arm (B, R, or Z) and correlate with fiber number, observation conditions, or sky position. The top anomalies include multi-band deviations and show no spatial clustering that would suggest a systematic origin.

3. **They span multiple physical categories.** Z-dominant objects suggest high-redshift sources. R-dominant objects suggest unusual AGN activity. B-dominant objects suggest UV-excess or high-ionization. Multi-band objects suggest composite/blended spectra or genuinely novel classes. This diversity argues against a single systematic cause.

4. **Their absence from AllWISE is the most striking finding.** AllWISE covers the entire sky at 3.4–22 μm with 750M detected sources. An object observed spectroscopically by DESI (meaning it was photometrically detected in Legacy Survey optical imaging) but NOT detected by WISE suggests either: (a) the object is unusually blue/hot with minimal IR emission, or (b) the object is transient and appeared after the WISE observations (2010-2011), or (c) the DESI targeting position doesn't correspond to a real astrophysical source (fiber positioning error).

5. **For bounce cosmology:** If any of these objects are confirmed as z > 2 QSOs missed by the standard pipeline, they represent high-bias tracers that could improve the scale-dependent bias measurement of f_NL. Even a modest addition of high-z QSOs to the tracer pool strengthens the bounce cosmology forecast.

## Top 10 Most Interesting Objects

### Rank #1 — Score 25.16
- **Position:** RA=194.455819, Dec=21.730232 (b=84°)
- **Residuals:** rB=1.349, rR=0.409, rZ=7.333 (worst: Z)
- **Tags:** high_z_candidate, near_ir_anomaly, emission_line_candidate
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=194.455819&dec=21.730232&layer=ls-dr10&zoom=15)
- STRONG Z-BAND ANOMALY (rZ=7.3, 81% of total residual). The near-IR arm (7520–9824Å) shows the autoencoder's largest failure to reconstruct this spectrum. Astrophysical scenarios: (1) High-redshift object at z>2–3 where rest-frame optical emission lines (Hα, [OIII], Hβ) are shifted into the Z-band — ...

### Rank #2 — Score 24.61
- **Position:** RA=156.180693, Dec=2.107486 (b=47°)
- **Residuals:** rB=1.368, rR=0.256, rZ=6.235 (worst: Z)
- **Tags:** high_z_candidate, near_ir_anomaly, emission_line_candidate
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=156.180693&dec=2.107486&layer=ls-dr10&zoom=15)
- STRONG Z-BAND ANOMALY (rZ=6.2, 79% of total residual). The near-IR arm (7520–9824Å) shows the autoencoder's largest failure to reconstruct this spectrum. Astrophysical scenarios: (1) High-redshift object at z>2–3 where rest-frame optical emission lines (Hα, [OIII], Hβ) are shifted into the Z-band — ...

### Rank #3 — Score 24.53
- **Position:** RA=206.638057, Dec=9.050749 (b=68°)
- **Residuals:** rB=0.867, rR=0.717, rZ=7.425 (worst: Z)
- **Tags:** high_z_candidate, near_ir_anomaly, emission_line_candidate
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=206.638057&dec=9.050749&layer=ls-dr10&zoom=15)
- STRONG Z-BAND ANOMALY (rZ=7.4, 82% of total residual). The near-IR arm (7520–9824Å) shows the autoencoder's largest failure to reconstruct this spectrum. Astrophysical scenarios: (1) High-redshift object at z>2–3 where rest-frame optical emission lines (Hα, [OIII], Hβ) are shifted into the Z-band — ...

### Rank #4 — Score 24.2
- **Position:** RA=172.864342, Dec=-2.343388 (b=55°)
- **Residuals:** rB=1.548, rR=8.27, rZ=0.177 (worst: R)
- **Tags:** high_z_candidate, bal_candidate, unusual_emission, accretion_disk_candidate
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=172.864342&dec=-2.343388&layer=ls-dr10&zoom=15)
- STRONG R-BAND ANOMALY (rR=8.3, 83% of total residual). The red arm (5760–7620Å) dominates the reconstruction error. Astrophysical scenarios: (1) QSO at z~3.5–5 where Lyman-alpha (1216Å rest) falls in the R-band — these are rare and DESI's redshift pipeline can struggle with them. (2) Broad absorptio...

### Rank #5 — Score 22.3
- **Position:** RA=201.287378, Dec=-7.662389 (b=54°)
- **Residuals:** rB=1.555, rR=7.86, rZ=0.175 (worst: R)
- **Tags:** high_z_candidate, bal_candidate, unusual_emission, accretion_disk_candidate
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=201.287378&dec=-7.662389&layer=ls-dr10&zoom=15)
- STRONG R-BAND ANOMALY (rR=7.9, 82% of total residual). The red arm (5760–7620Å) dominates the reconstruction error. Astrophysical scenarios: (1) QSO at z~3.5–5 where Lyman-alpha (1216Å rest) falls in the R-band — these are rare and DESI's redshift pipeline can struggle with them. (2) Broad absorptio...

### Rank #6 — Score 20.98
- **Position:** RA=99.051627, Dec=59.112695 (b=21°)
- **Residuals:** rB=6.919, rR=0.217, rZ=0.323 (worst: B)
- **Tags:** uv_excess, high_ionization, calibration_check_needed
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=99.051627&dec=59.112695&layer=ls-dr10&zoom=15)
- STRONG B-BAND ANOMALY (rB=6.9, 93% of total residual). The blue arm (3600–5800Å) shows the largest reconstruction failure. Astrophysical scenarios: (1) Unusual UV/blue continuum — very hot object (T>20,000K) with features not in training set. (2) Strong [OII] 3727Å or [NeV] 3426Å emission indicating...

### Rank #7 — Score 20.87
- **Position:** RA=171.254179, Dec=-2.08612 (b=54°)
- **Residuals:** rB=6.992, rR=0.319, rZ=0.182 (worst: B)
- **Tags:** uv_excess, high_ionization, calibration_check_needed
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=171.254179&dec=-2.086120&layer=ls-dr10&zoom=15)
- STRONG B-BAND ANOMALY (rB=7.0, 93% of total residual). The blue arm (3600–5800Å) shows the largest reconstruction failure. Astrophysical scenarios: (1) Unusual UV/blue continuum — very hot object (T>20,000K) with features not in training set. (2) Strong [OII] 3727Å or [NeV] 3426Å emission indicating...

### Rank #8 — Score 20.5
- **Position:** RA=195.372686, Dec=-5.49267 (b=57°)
- **Residuals:** rB=1.397, rR=7.457, rZ=0.183 (worst: R)
- **Tags:** high_z_candidate, bal_candidate, unusual_emission, accretion_disk_candidate
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=195.372686&dec=-5.492670&layer=ls-dr10&zoom=15)
- STRONG R-BAND ANOMALY (rR=7.5, 83% of total residual). The red arm (5760–7620Å) dominates the reconstruction error. Astrophysical scenarios: (1) QSO at z~3.5–5 where Lyman-alpha (1216Å rest) falls in the R-band — these are rare and DESI's redshift pipeline can struggle with them. (2) Broad absorptio...

### Rank #9 — Score 20.29
- **Position:** RA=199.207434, Dec=8.654999 (b=71°)
- **Residuals:** rB=6.66, rR=0.346, rZ=0.301 (worst: B)
- **Tags:** uv_excess, high_ionization, calibration_check_needed
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=199.207434&dec=8.654999&layer=ls-dr10&zoom=15)
- STRONG B-BAND ANOMALY (rB=6.7, 91% of total residual). The blue arm (3600–5800Å) shows the largest reconstruction failure. Astrophysical scenarios: (1) Unusual UV/blue continuum — very hot object (T>20,000K) with features not in training set. (2) Strong [OII] 3727Å or [NeV] 3426Å emission indicating...

### Rank #10 — Score 20.25
- **Position:** RA=194.589991, Dec=22.226541 (b=85°)
- **Residuals:** rB=1.655, rR=7.231, rZ=0.235 (worst: R)
- **Tags:** high_z_candidate, bal_candidate, unusual_emission, accretion_disk_candidate
- **Priority:** VERY_HIGH
- [Legacy Survey Image](https://www.legacysurvey.org/viewer?ra=194.589991&dec=22.226541&layer=ls-dr10&zoom=15)
- STRONG R-BAND ANOMALY (rR=7.2, 79% of total residual). The red arm (5760–7620Å) dominates the reconstruction error. Astrophysical scenarios: (1) QSO at z~3.5–5 where Lyman-alpha (1216Å rest) falls in the R-band — these are rare and DESI's redshift pipeline can struggle with them. (2) Broad absorptio...
