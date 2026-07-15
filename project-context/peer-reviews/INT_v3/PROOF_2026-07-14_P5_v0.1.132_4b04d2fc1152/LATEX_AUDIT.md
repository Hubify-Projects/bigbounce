# P5 v0.1.132 LaTeX audit

## Exact artifact

- PDF: `P5_v0.1.132.pdf`.
- SHA-256: `4b04d2fc1152b911d85c9db8fa315f9c135af2f7cd6c4f54c932d22d5eff1c18`.
- MD5: `fbdb7e6a37665fa3110a0c5561e74ccf`.
- Size: 1,510,730 bytes.
- Pages: 39.
- Build: four TinyTeX `pdflatex` passes with `-halt-on-error`.

## Seven-step audit

| Gate | Result |
|---|---|
| Compile errors | 0 |
| Undefined references | 0 |
| Undefined citations | 0 |
| Overfull hboxes | 0 total; 0 above 50 pt |
| Table-row overflows | 0 |
| URI annotations | 128 annotations / 49 unique; 0 missing local GitHub targets |
| Raw path/date risk | No new unbreakable path or long-date defect; all active long artifact paths use the existing hyperlink/allowbreak treatment |
| Visual review | PASS: every page 1--39 inspected at 120 dpi using five contact sheets and the underlying page renders |

The title-page date is July 14, 2026. The release-candidate material contains
`v0.1.132-2026-07-14`. Page 37 now begins with the complete reproducibility
checklist; the prior orphaned word `release.` is no longer present.

## Verdict

**PASS.** No overflow, overlap, clipping, blank-page, orphan, stale-version, or
broken-local-artifact-link defect was observed.
