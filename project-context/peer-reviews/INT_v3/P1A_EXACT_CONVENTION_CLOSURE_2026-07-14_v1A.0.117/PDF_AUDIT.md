# P1A v1A.0.117 PDF audit

## Build

- Engine: Tectonic 0.15.0, local cached bundle
- Result: successful seven-page PDF
- PDF SHA-256: `a5dcf033306c3b949a4a16d834a6fa39875d3da8af8d3c69cabba48ca4876fee`
- PDF MD5: `1a34a9d378d0877a20e764caefdfb867`
- Size: `149500 bytes`
- Page geometry: US Letter, `612 x 792 pt`
- Encryption, JavaScript, forms: none

## Log and reference audit

- Fatal TeX errors: `0`
- Undefined references: `0`
- Undefined citations: `0`
- Overfull boxes: `0`
- Underfull boxes: `12`, cosmetic; no rendered clipping or collision
- Bibliography warning: one pre-existing REVTeX ordering warning,
  `jnrlst (dependency: not reversed) set 1`
- REVTeX warnings: default 10-point size selected; `float` package repaired;
  keywords hidden without the `showkeys` class option
- Engine/package warnings: `inputenc` ignored by the Unicode engine; hyperref
  removed one line-break token from a PDF bookmark string
- Engine console warning: xdvipdfmx reports `Object @table.1 already defined`;
  the table renders once, all references resolve, and no duplicate content or
  visual defect is present

The frozen `.log` and `.blg` are included under `audit/`.

## Visual audit

Every page was rendered to PNG and inspected at original detail:

| Page | Result | SHA-256 |
|---:|---|---|
| 1 | pass | `ecc55c00e5e5c0380ae96b709e8081627f644925eee8014f98a9d1c4f0f937bb` |
| 2 | pass | `52cf135f4cd2825a38e0e36bce3f5d0f4333c527fc13f0e4a611d7c539219aee` |
| 3 | pass | `d7e1f18de82fbf06612ab49df07ff52a790d8db9808ff8e30878eb823fc29e52` |
| 4 | pass | `80e2121085e3a331011e24d8c9e621084385aeba13a1cb23616b855700d2644e` |
| 5 | pass | `39da2733efb0550b8666dcca07dceaccd29e7650b9365d03618b18de386eaad0` |
| 6 | pass | `1d9c3797908ec1b2adf29799c0930142666090cb716d58bcb47e67c70a458c6b` |
| 7 | pass | `048a0197567d8a36417b155d4c0d0007a0aa3824a869fecd8d66f216eb463b03` |

No page has text outside the media box, clipped equations, gutter collisions,
table overflow, malformed glyphs, or overlapping objects.

## Date, paths, and URLs

- Page 1 visibly reports `July 14, 2026`.
- The source internal version is `v1A.0.117`.
- Raw `texttt` filesystem paths in the source: `0`.
- Rendered raw filesystem paths: `0`.
- The artifact links display the actual script and JSON filenames.
- All `35` embedded URL annotations were extracted and inventoried. The repository
  artifact targets correspond to files present in this checkout; DOI/arXiv
  identifiers are syntactically valid and match the bibliography entries.
- Direct live HTTP response checking was unavailable in the restricted build
  environment (`curl` returned no network connection). External reachability is
  therefore recorded as an environment-limited remaining gate, not guessed.

## Verdict

**Pass for compilation, references, typography, overflow, page-by-page visual
inspection, date, and rendered-path checks.** External live URL reachability is
the only environment-limited audit item.
