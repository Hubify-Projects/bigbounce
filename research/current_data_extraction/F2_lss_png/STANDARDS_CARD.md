# Pipeline B Standards Card — DESI Spectral Anomaly Miner

| Field | Specification |
|-------|---------------|
| **Scientific object** | Spectral residual object — a DESI spectrum whose reconstruction error exceeds a calibrated threshold after artifact control |
| **Benchmark to reproduce** | Recover known QSO, galaxy, star classifications from DESI pipeline; recover known BAL QSOs and known lens candidates |
| **Injection plan** | Inject synthetic unusual emission lines, redshift-shifted templates, blended spectra, artificial noise patterns |
| **Null test plan** | Wavelength-shuffled spectra, noise-only spectra, known-good spectra scored as anomalous at <1% rate |
| **Holdout plan** | Sky-region split (N vs S galactic cap), redshift bins, SNR regimes, target-type holdouts |
| **Nuisance audit** | Test correlation with: fiber ID, plate, exposure time, sky brightness, airmass, seeing, E(B-V) |
| **External comparison** | Compare anomaly recovery against SDSS known-weird catalog, literature BAL catalogs, known lens catalogs |
| **Catalog schema** | targetid, ra, dec, z, anomaly_score, anomaly_family, tracer_utility, snr, qc_flags, model_version |
| **Fail conditions** | >20% of top anomalies are artifacts; anomaly score correlates with fiber/plate; baseline PCA beats autoencoder |
| **Claim language** | OK: "catalog of spectroscopically unusual DESI objects." NOT OK: "discovered new physics in DESI spectra" |
