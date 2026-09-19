# Defended selected sample — DESI DR1 anomaly flagship (2026-09-18)

**Internal assembly record.** This document defends the sample the anomaly
flagship manuscript is written on. Per directive Q1 it is process evidence:
the manuscript presents the science-target selection as its method, in its own
right, and does not narrate this file.

## The sample

| Property | Value |
|---|---|
| Sample | `flagship_sample_v2_enriched.parquet` (phase-3 v2, science-target-only) |
| Selection | DESI DR1 `iron` science targets with autoencoder anomaly score $S>3$ |
| Size | **1,244 objects** |
| Parent universe | 27,547,223 unique science `TARGETID`s scanned (generation `clean-rerun-6699d09ff886`) |
| Selected fraction | $4.5\times10^{-5}$ of the parent |
| SHA-256 (sample) | `d6d43dfa04d6a8b2b4d014f5f4899b5e5b844144a50b6c88e01a9a771a6baa5f` |
| SHA-256 (enriched) | `c3b176ff2d355a421ac48d00c5b6565fdfce8956fe6298eb85596bfb94f09fff` |
| Location | `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/` |

## Why this sample and not another

1. **Science-target provenance is enforced before any score cut.** A row is
   eligible only if `OBJTYPE == 'TGT'` **and** `COADD_FIBERSTATUS == 0`
   **and** `TARGETID > 0` (asserted, not merely filtered). Sky fibres,
   standard-star fibres and rows without a positive `TARGETID` are excluded
   by construction, and the gate is re-runnable
   (`clean_rerun/gates/check_sample_provenance.py`).
2. **The gate is load-bearing, and the released curve proves it.** Across
   every score bin above 3, more than 99.5% of raw fibres are
   sky-or-non-science, and the fraction *rises* with score (99.53% in
   $[3,4)$ to 99.97% in $[8,10)$). Without the provenance gate, a naive
   top-score cut selects instrument artefacts, not objects. This is the
   sample's single most important defence and it is a published figure of
   the release, not an assertion.
3. **The threshold follows a pre-declared rule, replayed here.** From the
   fixed grid $\{3,4,5,6,8,10\}$: take the largest threshold whose
   science-only count is $\ge 300$; if that count exceeds 1,500, step to the
   next grid point unless doing so drops below 300. Replaying the rule on
   the science-target counts selects $S>3$, $n=1{,}244$ — check **V4** in
   `VALIDATION_CONTRACT.md`, which reproduces the released choice
   independently of `threshold_choice.json`.
4. **It supersedes the earlier $S\ge 8$, 3,810-row characterisation cohort**
   (`project-context/ANOMALY_FLAGSHIP_SELECTION_DECISION_2026-08-26.md`).
   That cohort was selected by score alone and therefore inherits the
   sky-fibre population described above; it is retained for provenance only
   and is not the manuscript's sample. The science-only count at $S>8$ is 2
   objects, which is why the ladder rule lands at $S>3$ rather than at the
   earlier cut.

## Provenance re-run (2026-09-18)

`gates/check_sample_provenance.py` was re-run today against both released
tables; raw output in `outputs/provenance_recheck_2026-09-18.txt`:

```
OK: {'sample': '.../flagship_sample_v2.parquet', 'row_count': 1244,
     'checked_objtype': False, 'checked_fiberstatus': False, 'status': 'clean'}
OK: {'sample': '.../flagship_sample_v2_enriched.parquet', 'row_count': 1244,
     'checked_objtype': False, 'checked_fiberstatus': False, 'status': 'clean'}
```

Both files re-hash to the SHA-256 values recorded in
`project-context/PHASE3_V2_LANDING_2026-09-03.md` (9/9 released artifacts
match — check V2). `checked_objtype`/`checked_fiberstatus` are `False`
because the built sample does not carry those two columns; the rule was
applied upstream at build time and the gate's always-valid `TARGETID > 0`
invariant is what it re-checks here. **That is a gap worth closing:** the
re-runnable gate cannot, from the released file alone, re-verify the
`OBJTYPE`/`FIBERSTATUS` conditions. Recommended fix for the data release —
carry `objtype` and `coadd_fiberstatus` as columns in the published table so
the gate is self-contained for downstream users. Recorded as an open item;
it does not affect the sample, which was built under the rule.

## What the sample is and is not

- It **is** a machine-flagged candidate list: the objects a fixed,
  SHA-256-bound autoencoder reconstructs worst among DESI DR1 science
  spectra, with their provenance chain published.
- It is **not** a list of discoveries, a list of confirmed unusual objects,
  or a statistically complete sample of any physical class. 40.4% of rows
  (502/1,244) carry a DESI-reliable redshift (`ZWARN == 0`); the remaining
  742 carry `ZWARN == 4` (`SMALL_DELTA_CHI2`) and their redshifts must not be
  used as measurements.
- Its selection function is not characterised: no injection-recovery
  completeness has been measured for this model on this substrate, so no
  population-level inference (rate, abundance, cosmology) may be drawn from
  it. That is a named open test, not a limitation to be argued away.
