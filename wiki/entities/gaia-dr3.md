---
title: Gaia DR3 Anomaly Survey
type: entity
tags: [survey, anomaly, gaia, astrometric]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
---

# Gaia DR3

**Status:** COMPLETE | **QC:** PASS (needs expansion)

## Summary

Anomaly detection on a 50K-source subset of Gaia Data Release 3 variable star catalog. Reasonable results but sample is too small for statistical power.

## Numbers

| Metric | Value |
|--------|-------|
| Sources scored | 50,000 |
| Anomalies | 500 (1%) |
| Novelty fraction (not in SIMBAD) | 27% |
| Runtime | ~1 minute |

## QC Assessment

QC: PASS. No score explosions, no spatial concentration, reasonable anomaly distribution. The 27% novelty fraction is lower than [[erosita-dr1]] (73%) because Gaia sources are mostly Milky Way stars well-covered by existing catalogs.

## Limitations

- 50K is a tiny fraction of Gaia DR3 (~1.8 billion sources)
- Need to expand to 500K+ sources for meaningful coverage
- Focus on the most scientifically interesting subsets: variable stars, high proper motion objects, astrometric binaries

## Pending Follow-Up

- Expand to 500K+ sources
- Cross-match anomalies with AAVSO, GCVS variable star catalogs
- Cross-match with [[desi-dr1]] (spectroscopic x astrometric)
- Cross-match with [[sdss-dr18]]
- Look for anomalous proper motions or parallaxes

## Connections

- Included in [[paper-3-anomaly-catalog]]
- Comparison in [[survey-anomaly-rates]]
- Potential astrometric complement to spectroscopic anomalies from [[desi-dr1]]
