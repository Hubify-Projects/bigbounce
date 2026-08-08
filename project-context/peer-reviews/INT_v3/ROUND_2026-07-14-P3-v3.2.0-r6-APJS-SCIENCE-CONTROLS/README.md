# P3 v3.2.0-r6 ApJS science-control closure

Frozen 2026-07-14 from the canonical `paper3_apjs.tex`. This directory is proof only; it does not update SSOT, site state, the revision tracker, or an external-review verdict.

## Truth-audited results

- Streamed all 28,425,963 DESI FITS rows; recovered the exact 20,299,155-row science-bit parent and 2,468 observed one-arcsecond associations.
- Sixteen deterministic local shifts (60/120 arcsec; eight position angles) over all 190,015 cluster positions gave 86.6875 +/- 14.4209 parent associations within one arcsecond (range 66--109), versus 2,468 observed.
- The warning-free global-primary control gave 76.1875 +/- 13.3027 within one arcsecond (range 61--103), versus 181 observed. Its 0.1--1 arcsec annulus gave 75.5625 +/- 13.0127 (range 61--101), versus 11 observed. The paper therefore does not claim secure candidate-level identity for the tail.
- Exact accepted/warning-bearing inputs were 181/2,267 rows. Median accepted versus warned values were: z 1.108423/0.886051; score 5.324423/5.841820; separation 0.001269/0.001350 arcsec; DELTACHI2 61.063386/4.919479.
- The explicit `original_member_separation_arcsec <= 1.0` counterfactual retains 180 rows and removes only P3-DESI-000030 (1.979009213974 arcsec).

These controls are descriptive. They are not a selection-bias correction, physical classification, candidate-level identity proof, or purity estimate.

## PDF audit

- Compile: PASS (`latexmk -pdf -interaction=nonstopmode -halt-on-error`)
- Pages: 15, US Letter
- PDF SHA-256: `a16c217930a31ba799b68a88b2477b020ad5e309ff79626e49b2b69a715fdd5a`
- TeX SHA-256: `723d25080fa0e192c225105d42cf7ead233d5ec5cc3956b30630e5601268fc89`
- Log scan: zero overfull/underfull boxes, undefined references, multiply-defined labels, or stuck floats; the sole warning is the known AASTeX/nameref label-hook warning.
- Visual audit: PASS, all 15 pages rendered and inspected; no column crossing, clipping, table overflow, broken figures, or date/version overflow.
- Artifact path audit: PASS, 6/6 manuscript `\artifact{}` targets exist locally.
- URL audit: 16 explicit URLs returned HTTP 200. The MNRAS DOI publisher returned HTTP 403 to the command-line user agent. Two GitHub directory routes for local r4/r5 artifacts returned 404 before this work is pushed to `main`; they remain delivery gates, not claimed archive DOI evidence.

The AAS contributed-asset DOI remains unassigned and is explicitly retained as a publication-workflow gate.

## Frozen hashes

| File | SHA-256 |
|---|---|
| `p3_apjs_r6_science_controls.py` | `9513ba5506381d381f43d21a73cf9553cb46c08ed93609bf4b62ec8eedb00ce3` |
| `p3_apjs_r6_science_controls.json` | `359240e5571be12a54e5600af732ab3fb6ffc28407bd67f83ce0d4f9b452c6f1` |
| `p3_apjs_r6_original_member_sensitivity.csv` | `8b3f9f4c0f24bb720f323fbf4568400a3648fa1d792683dc88832e2fdca4ebe2` |
| `p3_apjs_r6_positional_tail.csv` | `e8e214b2fb0876764e5747b5a0bef75028782b3cd24f54b855dd054755342739` |
| `p3_v320_r6_chance_control.pdf` | `06ccd371d9f22690dfdf1e188e9087dc691e0a3f037d07a5db17da70dad50e2a` |
| `paper3_apjs_v3.2.0-r6.log` | `294f5066b951c513cd3f4a532270d6d5d463c56c7605665f24d6cf39442ab2f4` |
