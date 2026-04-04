---
title: Wiki Index
type: meta
last_updated: 2026-04-04
---

# BigBounce Wiki Index

Categorized catalog of all wiki pages.

---

## Entities: Surveys

- [[desi-dr1]] -- 22.5M spectra, 195K anomalies (0.87%), flagship anomaly catalog. QC: PASS.
- [[sdss-dr18]] -- 2.3M spectra, 78K anomalies (3.4%), transfer-learning from DESI. QC: CAUTION.
- [[lamost-dr10]] -- 11.4M spectra, 44K anomalies (0.39%), 98% blue-excess training bias. QC: CAUTION.
- [[erosita-dr1]] -- 930K X-ray sources, 9.3K anomalies (1%), 73% novel. QC: PASS.
- [[planck-cmb]] -- 20K patches, 200 anomalies, all at Dec<-84 (galactic contamination). QC: FAIL.
- [[act-dr6]] -- 20K patches, 200 anomalies, val_loss=22,420 (undertrained). QC: FAIL.
- [[neowise]] -- 43.5K sources, 436 anomalies, all at RA~180 (survey systematic). QC: FAIL.
- [[gaia-dr3]] -- 50K sources, 500 anomalies, 27% novel. QC: PASS (needs expansion).

## Entities: Papers

- [[paper-1-spin-torsion]] -- v2.2.0, 24pp. 14 barriers, ALP birefringence, bounce discrimination. ~80% submission-ready.
- [[paper-2-fnl-forecast]] -- v1.3.0, 12pp. f_NL = -35/8 prediction + Fisher forecast. SUBMISSION-READY.
- [[paper-3-anomaly-catalog]] -- 735 lines LaTeX. 8 surveys, 328K anomalies. ~95% ready.
- [[paper-4-chirality]] -- 1,099 lines LaTeX. 8.47M galaxies, dipole null. ~85% ready.

## Entities: Pipelines

- [[pipeline-b-desi-anomaly]] -- BigAE autoencoder on full DESI DR1. COMPLETE.
- [[pipeline-1-tracer-purification]] -- Anomaly-to-f_NL improvement. Steps 2-6 NOT STARTED.
- [[pipeline-2-chirality]] -- 8.47M galaxy chirality catalog. COMPLETE.

## Concepts

- [[fnl-prediction]] -- f_NL = -35/8, parameter-free, triple role, decisive discriminator.
- [[birefringence]] -- ALP beta = 0.27 deg prediction, ACT measurement systematic-dominated.
- [[bounce-portfolio]] -- Model-agnostic strategy across 6 observational channels.
- [[houston-method]] -- 9-step completion protocol: RUN through COMPLETE.
- [[anomaly-detection-methodology]] -- Autoencoder-based anomaly detection with QC gates.

## Comparisons

- [[survey-anomaly-rates]] -- All 8 surveys side-by-side with QC status.
- [[bounce-vs-inflation]] -- Observational discriminators and current status.

## Meta

- [SCHEMA](SCHEMA.md) -- Wiki conventions, workflows, lint rules.
- [log](log.md) -- Chronological research event log.
- [index](index.md) -- This file.
