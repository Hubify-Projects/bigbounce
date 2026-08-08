# P4 v1.0.241 frozen-PDF audit

The exact 35-page review PDF passed the post-compile visual gate.

| Check | Result |
|---|---|
| LaTeX errors (`^!`) | 0 |
| Undefined references/citations | 0 (the only `undefined` log hit is a non-structural Latin Modern bold-small-caps font-shape substitution) |
| Overfull hboxes | 0 |
| Long `\\date{}` risk | 0 |
| Raw path-like `\\texttt{}` | 0; the five regex hits are identifiers/model names rather than file paths |
| Visual render | PASS, all 35 pages inspected in `proof/render/contact.png`; no gutter crossing, clipping, overlap, missing float, or title-block overflow |
| URL check | Five manuscript `\\url{}` targets had already returned HTTP 200 in the frozen M44 closure proof; no URL changed between that proof and commit `4420453d` |

The rendered review proof is the committed pipeline PDF with SHA-256
`d6eded1df29da5d2ccf6acb1e04277876289ae1547a1b8a3d2fda819ae7097f2`.
The stale public mirror is a release-integration defect, not a PDF-layout defect.
