---
title: Research Log
type: meta
last_updated: 2026-04-04
---

# Research Log

Chronological record of major events in the BigBounce research program.

---

## [2026-01] started | BigBounce Research Program

Houston Golden begins systematic investigation of spin-torsion (Einstein-Cartan-Hehl) cosmology as a bounce cosmology candidate. Goal: prove bounce cosmology fits observational data better than LCDM + inflation. Website launched at bigbounce.hubify.app.

## [2026-02] completed | Foundation Studies A-G

Seven foundation studies (A through G) systematically closed all ECH-specific routes from bounce to dark energy. 14 structural barriers identified. Key results: mass-coupling lock (A), topological-shift duality (B), scalar-tensor universality (C), Planck suppression (D), attractor-sensitivity dilemma (F), parameter immunity (G). ECH confirmed perturbation-transparent. See [[paper-1-spin-torsion]].

## [2026-03-17] completed | Bounce Evidence Audit

Full audit of all bounce evidence across ECH and alternative models. 14 barriers confirmed as ECH-specific. ALP birefringence prediction beta = 0.27 deg identified as matching the 3.6-sigma observed signal. Matter bounce f_NL = -35/8 confirmed as parameter-free and mechanism-independent. See [[fnl-prediction]], [[birefringence]].

## [2026-03-24] pivoted | Bounce Portfolio Strategy

Strategic reframe from "prove ECH Model B" to "prove bounce cosmology beats inflation across multiple models." Literature audit revealed three new tracks: quintom bounce-DE unification, PBH regulation by f_NL, NANOGrav consistency. See [[bounce-portfolio]].

## [2026-03-25] opened | Quintom, PBH, NANOGrav Tracks

Literature deep dive surfaced two major discoveries: (1) f_NL = -35/8 naturally regulates PBH production (Choudhury+ 2025), (2) matter bounce GW spectrum consistent with NANOGrav 15yr at 0.33-sigma (Papanikolaou 2025). f_NL triple role established. See [[fnl-prediction]], [[bounce-portfolio]].

## [2026-03-25] updated | Paper 1 to v2.2.0

Paper 1 updated with bounce model discrimination table, quintom references, portfolio framing. 24 pages, 63+ bibliography entries. See [[paper-1-spin-torsion]].

## [2026-03-28] completed | Galaxy Chirality Catalog

Pipeline 2 complete: 8.47M galaxies classified (CW/CCW/NOT_SPIRAL). 93.7% accuracy, 8/8 bias tests passed. CW/(CW+CCW) = 0.4974, dipole = 0.43-sigma (null). Published to HuggingFace, Convex, B2. See [[pipeline-2-chirality]], [[paper-4-chirality]].

## [2026-03-29] retracted | w0-wa MCMC Convergence — CONFABULATION

The earlier "Quintom-B favored at 2.3-sigma, P(quintom-B) = 98.6%, w0 = -0.871 +/- 0.060, wa = -0.542 +/- 0.245" log entry was fire-#21 confabulation — corrected fire #25 (2026-04-18). Paper 1 §VII.H is explicit: zero free w0-wa samples among the 309,789 frozen posterior samples in this program. The DESI DR2 2.8-4.2 sigma w-crossing signal is cited as observational context in the bounce portfolio, not as a BigBounce-group MCMC result. See [[bounce-portfolio]] + `project-context/SSOT/drive-to-100.md` fire #25.

## [2026-04-01] started | H200 Multi-Survey Queue

10-experiment research queue launched on H200 GPU pod. Surveys: Planck CMB, ACT DR6, NEOWISE, Gaia DR3, cross-match, plus existing DESI/SDSS/eROSITA/LAMOST results.

## [2026-04-02] completed | Multi-Survey Anomaly Sweep

All 10 experiments finished. Grand totals: ~33.5M sources/spectra scored, ~328K anomalies across 8 surveys + NANOGrav GW consistency check. See [[desi-dr1]], [[sdss-dr18]], [[lamost-dr10]], [[erosita-dr1]], [[planck-cmb]], [[act-dr6]], [[neowise]], [[gaia-dr3]].

## [2026-04-03] completed | Phase 2 Analysis

f_NL improvement measured at 6.1% (DESI) / 16.4% (DESI+SDSS). SPHEREx forecast: 4.38-sigma detection. ACT birefringence measurement: beta = 17.4 +/- 12.1 deg (systematic-dominated, needs NaMaster/PolSpice). Cross-match validation: SDSS x DESI found 3 matches including known z=5.27 QSO. See [[fnl-prediction]], [[birefringence]], [[pipeline-1-tracer-purification]].

## [2026-04-04] completed | Quality Audit & Houston Method v2

6 experiments flagged for re-run (Planck, ACT, NEOWISE QC failures; SDSS, LAMOST caution). Houston Method v2 written: 9-step completion loop (RUN -> QC -> ANALYZE -> INTERPRET -> CONNECT -> SYNC -> EXPAND -> BACKUP -> COMPLETE). See [[houston-method]], [[survey-anomaly-rates]].
