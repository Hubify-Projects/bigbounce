# P3 final package receipt — v3.2.0-r14

Audited 2026-08-03 against the current source, canonical PDF, arXiv-style source
bundle, and the existing ApJS digital-asset bundle. This receipt records package
evidence only; it does not change scientific claims or readiness.

| Item | Binding |
|---|---|
| Source | `paper3_apjs.tex` · SHA-256 `5000b09d55191aaf858956e297dd2304ec1a20642ffd6b93c688f562b5b90a4e` |
| Canonical PDF | `paper3_apjs.pdf` · SHA-256 `4b5a51949a9f91264e4ae4bf97fcd946997053d68d6a7343ab008156c094313b` · MD5 `e9c947e2c56d15851242e74330da93de` · 17 pages |
| Submission venue | *The Astrophysical Journal Supplement Series* |
| Source bundle | `project-context/SSOT/arxiv_tarballs/paper3_apjs_arxiv_v3.2.0-r14.tar.gz` · SHA-256 `6ef3a614add20eba1f588d625a8555ad2f7d4ec78745b7005c1ecdfdd4cd9c3d` |

## Package check

The source bundle contains the exact current `.tex`, `aastex701.cls`, and all three
referenced vector figures. The bibliography is inline, so no `.bbl` is required.
Fresh extraction and Tectonic compilation passed with 17 pages, zero fatal errors,
and zero undefined references/citations. The only overfull hbox is 1.82327 pt in
the long identifier paragraph at source lines 285--296, below the 10 pt visual-risk
threshold; it is retained for Houston's visual look rather than silently reflowed.

The local `apjs_submission_bundle_v3.2.0-r7` validator passed: 181-row / 43-column
AAS table, 170 core plus 11 lower-confidence rows, 2,267 warned-auxiliary rows,
all manifest and SHA-256 checks, and coordinate-lineage status PASS. The journal
digital-asset DOI is correctly still `pending`, not claimed as minted.

## Submission decision

The P3 source PDF and data assets are ready for Houston's visual approval. Before an
ApJS portal submission, confirm the portal metadata and digital-asset upload choices;
the manuscript already has AASTeX 7, author email, keywords, and an approximately
244-word abstract (under the AAS 250-word checklist cap). The separate bounded
final-hash active-leg confirmation and Houston's explicit sign-off remain outstanding;
this receipt alone does not create a new readiness gate.
