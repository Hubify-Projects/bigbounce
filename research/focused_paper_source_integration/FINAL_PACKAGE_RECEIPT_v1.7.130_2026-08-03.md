# P2 final package receipt — v1.7.130

Audited 2026-08-03 against the current source, canonical PDF, and local arXiv-style source bundle. This receipt records package evidence only; it does not change scientific claims or readiness.

| Item | Binding |
|---|---|
| Source | `02_full_draft.tex` · SHA-256 `4a780eb8666ad536f25fc5cf75e9d2331e0fa8c384d0e89f4a50aabdf3d14943` |
| Canonical PDF | `02_full_draft.pdf` · SHA-256 `d3afe79fe70ce13cee5ec8149e84c4b42c78224ca6a90569058ec501222f5c2f` · MD5 `f7116fe3e2541d6f649876f2ec7789ee` · 12 pages |
| Submission venue | *Physical Review D* — Research Article |
| Source bundle | `paper2_arxiv_v1.7.130.tar.gz` · SHA-256 `74124142a3bc92bcc69cbfd73dfe9dd49c731421e69148414e1bfd58dc8e9a69` |

## Package check

The bundle contains the exact current `.tex`, both rendered figures, the committed
`.bbl`, `02_full_draftNotes.bib`, and `focused_paper_refs.bib`. The last file was
added in this package-only refresh: the prior tarball declared it through
`\bibliography{focused_paper_refs}` but omitted it, causing a clean-room engine
that invokes BibTeX to rebuild an empty bibliography. Source and figure hashes
match the paper directory exactly.

Fresh extraction and Tectonic compilation passed with 12 pages, zero fatal errors,
zero undefined references/citations, and zero overfull hboxes. The visual audit of
the canonical title page and a table/figure page found no clipping, gutter crossing,
or broken title block. Non-blocking underfull boxes and one output-routine vbox
warning are retained as compiler diagnostics, not paper changes.

## Submission decision

The P2 PDF and source package are ready for Houston's visual approval and PRD portal
upload. The separate bounded final-hash active-leg confirmation and Houston's explicit
sign-off remain outstanding; this receipt alone does not create a new readiness gate.
