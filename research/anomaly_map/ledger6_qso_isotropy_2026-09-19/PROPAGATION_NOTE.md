# PROPAGATION NOTE → lane L5 / paper-af (anomaly flagship), and to ledger row 12

**From:** lane `bb-LS2-ledger6`, 2026-09-19 · **Source result:**
`LEDGER6_QSO_ISOTROPY_RESULT_2026-09-19.md`, JSON `outputs/ledger6_qso_isotropy.json`.

**Bearing on the flagship: LIMITED AND INDIRECT. Nothing in paper-af changes because of this
run, and nothing here answers OT-1.** This note exists so that the overlap is recorded
explicitly rather than discovered later and over-read.

## What genuinely transfers

1. **A validated angular-isotropy estimator for DESI DR1 maps, with its own nulls.** The
   estimator (weighted data/random pixel ratio, per-pixel Σw² shot term, per-cap monopole
   marginalisation, look-elsewhere axis scan, Poisson/selection null, injection–recovery) is in
   `analyze_isotropy.py` and is unbiased to < 0.007 in recovering an injected modulation. If the
   flagship ever needs a large-angle-structure check on an anomaly-selected sample (e.g. "is the
   S > 5 catalogue's sky distribution consistent with the parent selection function?"), this is
   the tool, and it runs in seconds on CPU.
2. **A quantified statement that DR1 imaging-systematics weights matter at the ~2% level in
   number counts.** With `WEIGHT_SYS` removed, the QSO count dipole grows 5× to 0.0221; with it
   applied, |d| = 0.0045 ± 0.0047 (null-consistent). Any flagship claim about the *sky
   distribution* of anomaly-selected objects that does not carry an equivalent weight treatment
   should be read as uncontrolled at that level.
3. **An edge-pixel warning for HEALPix work on DR1 footprints.** At nside 128 the measured
   dipole is 0.0296 and falls to 0.0131 when the mask threshold tightens from 0.5× to 0.95× the
   median random density — it is a partial-coverage artifact. Any nside ≥ 128 map made from
   these catalogues needs the stricter mask.

## What explicitly does NOT transfer — do not use this as OT-1

- The sample here is the **QSO clustering catalogue** (0.8 < z < 2.1, DESI's LSS target class,
  with the LSS pipeline's completeness/systematics/redshift-failure weights). The flagship's
  sample is **anomaly-selected science spectra across all target classes**. The selection
  functions are different objects. An isotropy result for the former says nothing quantitative
  about the latter.
- OT-1 (the flagship's selection function, GPU-gated) remains **open and untouched**. This run
  must not be cited as progress on it.
- No number in paper-af, its SSOT row, its readiness, or its Convex state is affected. **No
  writes were made to any of them by this lane.**

## Related open ledger item

Row 12 (self-supervised model on the full DR1 science-target population) inherits point 1: if a
v3 catalogue is ever produced, a large-angle isotropy check of the anomaly *score* field against
the parent selection function is a cheap sanity gate that this lane has now made turnkey.
