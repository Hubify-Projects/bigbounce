# P3 v3.2.0-r8 closure proof

This directory freezes the exact P3 r8 manuscript and PDF after the bounded Codex-finding closure. It is a validation/proof artifact, not a new referee wave and not an acceptance or readiness claim.

## Closure scope

- One reader-visible sentence labels the 0.1-arcsec boundary post hoc and descriptive rather than predeclared.
- The predeclared 1-arcsec membership and scientific contract remain 181 = 170 + 11.
- The r7 bundle manifest and all component bytes remain unchanged; exactly three already-manifested Parquet copies complete its Git representation.
- A fresh `git archive`-based tree plus exactly those three payloads passes the bundle validator with 41/41 files.
- No SSOT, readiness tracker, site, Convex, or public-state mutation is part of this closure.

## LaTeX audit

```text
LATEX AUDIT — P3_v3.2.0-r8.pdf
────────────────────────────────
Compile errors:        0
Undefined references:  0
Overfull hboxes:       0
Underfull hboxes:      0
Overfull vboxes:       2 at 4.23666 pt (visually contained)
Table-row overflows:   0
Broken URLs:           0 / 26 unique annotations
Raw \texttt paths:     0
\date overflow risk:   0
Page-1 metadata:       PASS (2026-07-14 14:18 PT — v3.2.0-r8)
Visual review:         PASS (all 16 pages rendered at 110 DPI)

Verdict: PASS
```

All 16 pages were inspected for gutter crossing, margin escape, clipping, overlap, title/date overflow, table/figure bounds, and illegibility. The new provenance sentence is legible and contained on page 4. Table 2 remains fully legible on page 5. Pages 13--15 retain substantial whitespace but no content or layout defect. The two small overfull-vbox messages are not visible boundary violations.

The final PDF has the same set of 26 URI annotations as the fully audited r7 PDF, so the prior 0/26 broken-link result remains applicable; no link was added, removed, or changed by r8.

## Frozen hashes

```text
2b9a5fd356e49ae7a9939cbf8e9197379bef71b1f66a0e364e0de41ae416d10b  P3_v3.2.0-r8.tex
b5f254f92b10bda43b687f07c5f58b828a6f7dc70d98c08f9e9b609edbba08b0  P3_v3.2.0-r8.pdf
e59710a1c4f88fc816257d1441ae3eb69d954828c180a8541a1aa8f1c855007a  BUNDLE_MANIFEST.json
bb37501f1912cc9199903ba39844a19f7ff0da0272ba5448986eac496e2d4a4f  bundle SHA256SUMS
```
