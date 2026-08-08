# P5 v0.1.131 bounded AJ closure proof

Status: **PASS for the bounded manuscript/PDF closure; no new analysis rerun and no publication/acceptance claim.**

This receipt closes the normalized AJ truth-audit findings against existing artifact A37. It does not claim submission, acceptance, a public release tag, a DOI, a released Paper IV final catalog, or a physical/cosmological exclusion.

## Reader-visible closure

- The released-parent DESIVAST estimate is presented first as a focal descriptive/exploratory estimate, not a confirmatory or preregistered primary analysis.
- The exact flow is explicit: 694,642 released GALZONE TARGETIDs to 145,789 joined rows to 145,766 `OUT=0` quality-parent rows to 31,937 VoidFinder hole-union members and 113,829 non-members.
- The membership contract distinguishes the GALZONE TARGET universe, the `OUT=0` parent, and exact membership in the union of released VoidFinder holes.
- The A37 model/covariance contract is explicit: unpenalized Newton-Cholesky logistic MLE, five/redshift and four-column continuous spline bases, constant missingness indicators dropped, 78 design columns/rank 78, 50 NSIDE=4 clusters, correction 1.020947, SE 0.00341274, and the 3,750-nearest-MAXIMALS scale sensitivity SE 0.003174 with p=0.692.
- Abstract and conclusion contain no editorial acceptance instructions. Limitations retain the Paper IV final-label/weight/provenance dependency and mandatory reverification.
- Post-hoc/exploratory status, unavailable selection function, underpowered label-bias check, archive/DOI limits, and the absence of physical/exclusion claims remain explicit.

## Exact evidence

- Manuscript: `P5_v0.1.131.tex`, SHA-256 `51a856531f06970938567e9ccd5e49719fc198c8484bc6b2a66cef538c5e38cb`.
- PDF: `P5_v0.1.131.pdf`, 39 pages, 1,510,954 bytes, SHA-256 `4f545606e290e0295b4284e8ba441f04155aa601100b213c1e3cfdb894d803a0`, MD5 `e29180555c90c0e60d56e8d6b7b82c81`.
- Frozen input A37: `pipelines/p5_desi_chirality/outputs/36_desivast_native_selection_control.json`, SHA-256 `64c3fad65c35c168caac60166399be9bd43d441a0a68963d17e3c1c9e00e91bd`.
- Analysis rerun: **none**. The bounded closure consumes A37 as frozen evidence.

## LaTeX and visual audit

- Compile command: `PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH" latexmk -pdf -interaction=nonstopmode -halt-on-error p5_desi_chirality.tex`.
- Compile exit: 0.
- Fatal errors, undefined references/citations, multiply-defined labels, and overfull boxes: 0.
- All 39 pages were rendered at 120 dpi and individually inspected. No margin, gutter, table, figure, equation, title, date, or path collision was found.
- The segmented rule above the references on page 39 is the intentional APS REVTeX bibliography device (`aps4-2.rtx` `\bib@device`), not an overflow or stray table rule.
- The PDF contains `v0.1.131-2026-07-14` in its release-candidate/data-availability material. The title page correctly shows July 14, 2026; the version is not printed on page 1, and this receipt does not claim otherwise.

## URI audit

Eight of nine static external URLs returned HTTP 200. The DOI resolver returned HTTP 403 to the automated client; this is recorded as bot denial, not treated as proof of a broken DOI. Repository-relative artifact links remain release-candidate links and become remotely meaningful only after the corresponding commit is pushed.

## Immutable retention

- Object: `project-context/pdf-archive/objects/sha256/4f/4f545606e290e0295b4284e8ba441f04155aa601100b213c1e3cfdb894d803a0.pdf`.
- Reference: `project-context/pdf-archive/refs/P5/P5__v0.1.131-2026-07-14__2026-07-14T161420-0700-PDT__4f545606e290.pdf`.
- Manifest: `project-context/pdf-archive/manifests/2026/07/20260714T231420Z-p5-v0.1.131-aj-bounded-closure-20260714T231420Z.json`.

## Scope guard

- New science computation: false
- Confirmatory/preregistered claim: false
- Physical or cosmological bound: false
- Immutable public tag or DOI claim: false
- Site, SSOT, Convex, global `version.json`, P1B, or P4 change: none
- Staging performed by this lane: none
