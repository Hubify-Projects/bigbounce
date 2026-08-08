# P3 v3.2.0-r7 closure proof

This directory freezes the exact P3 r7 manuscript and PDF after the catalog-contract closure. It is a validation/proof artifact, not a new referee wave and not an acceptance claim.

## Scientific contract

- Primary list: 181 positional associations retained.
- High-coordinate-consistency core: 170 rows at or below 0.1 arcsec.
- Lower-confidence tail: 11 rows between 0.1 and 1 arcsec.
- Neither tier is a secure identity or purity claim.
- Historical coordinate lineage is recovered at the field/code level: DESI anomaly `ra`/`dec` came from FIBERMAP `TARGET_RA`/`TARGET_DEC`, then cluster coordinates were member-coordinate means.
- The production object-to-spectrum mapping and score preprocessing/normalization remain explicitly unavailable.
- The exact warned-row `original_score` median is 5.841819763183594 (displayed 5.84182); the earlier non-reproducible value is rejected.

## Validator results

- Bundle contract: PASS — 181 = 170 + 11; warned auxiliary 2,267; AAS table 181 x 43; DOI null/pending.
- Non-mutating component wrapper self-check: PASS — four unsafe in-place destinations rejected and two temporary destinations accepted.
- Primary replay: PASS — exact 18-field source-row equality, 143 checkpoint parts, strict 181 identity set, and 8/8 live remote byte ranges.
- Warned replay: PASS — exact 2,267 key set/order, carried fields, masks, and ZWARN bit counts.
- Process defect closed: the legacy primary validator reaches a final `SameFileError` if invoked inside its frozen release because it copies itself onto itself. The r7 wrapper validates temporary copies and preserves frozen component bytes. The first invocation had already recomputed the full 22.37 GB FITS SHA-256 and completed the scientific checks before that packaging-only error; the guarded replay then passed with the redundant full hash skipped.

## LaTeX audit

```text
LATEX AUDIT — P3_v3.2.0-r7.pdf
────────────────────────────────
Compile errors:        0
Undefined references:  0
Overfull hboxes:       0
Table-row overflows:   0
Broken URLs:           0 / 26 unique annotations
Raw \texttt paths:     0
\date overflow risk:   0
Visual review:         PASS (all 16 pages rendered at 110 DPI)

Verdict: PASS
```

AASTeX emits a deferred-float placement warning for the 11-row positional-tail table. This is not a hidden layout failure: all eight tables and three figures appear in the final PDF, and all 16 pages were inspected for gutter crossing, margin escape, overlap, title/date overflow, and illegibility.

The URL audit mapped every repository link to an existing local file/directory. Fourteen external URLs returned HTTP 200. The MNRAS DOI returned the correct HTTP 302 resolution; the final publisher page blocks automated clients with HTTP 403. One directory link initially used `/blob/`; it was corrected to `/tree/` before this freeze.

## Frozen hashes

```text
01cb68b1d52d411c1f4b181d6504f2f1344bc45d1f0ad3793d74b58a5d7e75d8  P3_v3.2.0-r7.tex
761e35ec840e93599163d68c6b4db9b8d75293545e49c45c978dc0be0f38cb2b  P3_v3.2.0-r7.pdf
e59710a1c4f88fc816257d1441ae3eb69d954828c180a8541a1aa8f1c855007a  BUNDLE_MANIFEST.json
bb37501f1912cc9199903ba39844a19f7ff0da0272ba5448986eac496e2d4a4f  bundle SHA256SUMS
```
