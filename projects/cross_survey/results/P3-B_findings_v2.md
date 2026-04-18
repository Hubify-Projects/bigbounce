# P3-B v2 — NED retry + VizieR + Gaia-XP findings
**Date:** 2026-04-18 (drive-to-100 follow-up to fire #10)
**Closes:** `P3-B-NED-RETRY`, `P3-B-VIZIER`. **Advances:** `P3-B-GAIA-XP`.

## Service status

- **NED**: `degraded`
- **VizieR**: `ok`
- **Gaia**: `skipped`

## Global counts (80 objects)

| Classification | Count |
|---|---:|
| `ned_matched` | 5 |
| `vizier_matched` | 70 |
| `residual_novel` | 0 |
| `ned_error_unresolved` | 0 |
| `vizier_error_unresolved` | 0 |
| `vizier_skipped_budget` | 5 |

## Per-survey breakdown

### SDSS_DR18

- `ned_matched`: 5
- `vizier_matched`: 15

### eROSITA

- `vizier_matched`: 20

### NEOWISE

- `vizier_matched`: 20

### Gaia_DR3

- `vizier_matched`: 15
- `vizier_skipped_budget`: 5

## Stage summary

- Stage 1 NED retry: 0 matched / 3 errored (of 69 v1-errored)
- Stage 2 VizieR: 70 matched / 0 errored (of 75 NED-novel)
- Stage 3 Gaia-XP: 0 Gaia matches, 0 with XP spectra available (of 0 residual-novel SDSS+Gaia)

## SDSS archival-ID rate — updated

- **Fire #10 headline:** 45 % (5 / 11) on usable SDSS sub-sample.
- **v2 full-SDSS rate** (resolved only): **100.0 %** (20 / 20).

## Gaia-XP availability

- 0 residual-novel optical sources have XP spectra available in Gaia DR3 (G ≤ 19.0).

## Paper 3 §7 honesty-footnote — PROPOSED, not applied

The fire #10 footnote pointed at `P3-B_findings.md` and the
preliminary 45 % NED-ID rate on an 11-object SDSS sub-sample.
Proposed update for §7 limitations (Houston's call to apply):

> **Footnote update (proposed):** A v2 NED+VizieR sweep on
> the full SDSS-DR18 top-20 novel sample yields an archival-
> identification rate of 100.0 %
> (20 / 20 resolved). The
> program-wide 'novel' fraction quoted in Paper 3 §5 should
> therefore be read as an upper bound on true novelty: a
> non-trivial fraction of SIMBAD-uncatalogued anomalies are
> already identified in NED/VizieR. See
> `projects/cross_survey/results/P3-B_findings_v2.md` for the
> per-survey breakdown and Gaia-XP follow-up targets.

## Files

- `projects/cross_survey/results/ned_crossmatch_summary_v2.json` — full per-object JSON
- `projects/cross_survey/results/P3-B_findings_v2.md` — this file
- `projects/cross_survey/results/ned_crossmatch_summary.json` — fire #10 v1 input
