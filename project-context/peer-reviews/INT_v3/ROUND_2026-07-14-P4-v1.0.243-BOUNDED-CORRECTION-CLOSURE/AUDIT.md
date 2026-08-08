# P4 v1.0.243 bounded-correction closure audit

Date: 2026-07-14 PDT

Scope: canonical inclusive-mask regeneration, portable provenance, Fig. 7 regeneration, manuscript reconciliation, compile, and PDF QA.

Review status: no new review was dispatched in this lane; this bundle proves the closure artifact, not an external-review verdict.

## Exact frozen manuscript

- Source: `closure/P4_v1.0.243.tex`
- PDF: `closure/P4_v1.0.243.pdf`
- Bibliography output: `closure/P4_v1.0.243.bbl`
- Source SHA256: `6affe4205a49a7954716f09ef11f31e1c17da1cbd778c195f8966c25c0127ed0`
- PDF SHA256: `9e73fd888699058d421043b0dd2de5d37d2aeb36fe37e8dd1c0bf5409e947d19`
- BBL SHA256: `8958e589798442840738db51ade594dcba50650952ef83194921792065ccad28`
- PDF geometry: 27 letter-size pages; 25,158,104 bytes; unencrypted; no JavaScript.

## Canonical primary-result assertions

Values below were read from `proof/artifacts/catalog_c_summary.json` and checked against PDF text.

- High-confidence sample: `N = 949584`
- Inclusive mask: `N_spiral >= 10`; 23,682 valid NSIDE=64 pixels
- Dipole amplitude: `0.004597074287780104`
- Direction: RA `294.30537030397005 deg`, Dec `16.029115977736286 deg`
- Null mean: `0.0036928318780248184`
- Null population standard deviation (`ddof=0`): `0.0016467112675757516`
- Moment significance: `+0.549120193418297 sigma`
- Upper-tail rank: `k = 2651` of `10000`; `(k+1)/(N+1) = 0.26517348265173485`
- Monte Carlo seed: `20260418`
- Canonical null-array SHA256: `62bb1c019231974c2a7ed5d5e43ceb77a5596e4675c82d7ff1c899e029a36492`
- Fig. 7 SHA256: `7ca18de4109adb7334855c0e0255a8aa0a0ce600af40ce8df41024af839a6541`

The superseded strict `N_spiral > 10` execution is retained only as explicitly named historical sensitivity context.

## Portable provenance

The bundled generators and JSON artifacts contain no machine-specific macOS, Linux, or Windows home paths. They identify the immutable upstream dataset as:

- provider: Hugging Face
- repository: `bamfai/galaxy-chirality-catalog`
- repository type: `dataset`
- file: `catalog_production.parquet`
- immutable revision: `a21eb596fd10edb9af9e7a1bcefb04f87327a724`
- content SHA256: `e8525ba5c98576f6361580e4a0aa7a86929ccc9f79b1423808774cfaaf313563`
- byte count: `952115239`

## LaTeX and PDF audit

- Tectonic compile: pass.
- LaTeX errors: none.
- Undefined control sequences, citations, and references: none.
- Overfull hboxes/vboxes: none.
- Underfull warnings: present and non-clipping; retained in `proof/audit/tectonic-output.txt`.
- Raw `\\texttt{.../...}` filesystem-path scan: clean. The sole slash-bearing `\\texttt` value is the public Hugging Face dataset identifier, not a local path.
- Local absolute path scan of source and proof bundle: clean.
- Version/date extraction: `Version v1.0.243`, dated July 14, 2026.
- Visual audit: all 27 pages inspected from 100-dpi renders. No clipping, overlap, off-page equations, malformed tables, title/date overflow, or figure-caption collision was observed. Three 9-page contact sheets are in `proof/render/`.

## URL audit

- URI annotations: 107
- Unique URI targets: 34 (33 HTTP(S), one `mailto:`)
- HTTP(S) results at freeze time: 32 returned HTTP 200.
- One expected transient HTTP 404: the newly committed `fig7_raw_vs_eq_manifest.json` link. The artifact is present in provenance commit `e8a4d5ff` and in this proof bundle, but that commit had not yet reached remote `main` when the audit ran. This is a publication-order condition, not a missing local artifact; rerun after the orchestrator pushes the closure commits.
- The genuine broken directory link found on the first pass was corrected to a valid GitHub `tree/main` target and recompiled before this freeze.

Exact targets and response codes are recorded in `proof/audit/urls.tsv` and `proof/audit/http-status.tsv`.

## Deliberate scope exclusions

- No new P4 reviewer panel was launched.
- No site, SSOT, Convex, mirror, tag, push, or release mutation was performed in this lane.
- The existing dirty `version.json` belonged to another live lane and was intentionally not modified or staged.

`MANIFEST.sha256` is the integrity root for every other file in this bundle.
