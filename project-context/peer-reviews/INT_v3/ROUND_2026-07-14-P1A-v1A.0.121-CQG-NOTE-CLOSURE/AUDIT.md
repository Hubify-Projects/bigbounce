# P1A v1A.0.121 CQG Note closure audit

Date: 2026-07-14 PDT

Scope: surgical closure of the truth-audited v1A.0.120 CQG Note findings. No new reviewer panel was dispatched in this lane.

## Exact frozen manuscript

- Source: closure/P1A_v1A.0.121.tex
- PDF: closure/P1A_v1A.0.121.pdf
- Bibliography output: closure/P1A_v1A.0.121.bbl
- Source SHA256: 4bf3a979fa214a06c29c474fe7a49f3d032150769d505de16647b0854701a650
- PDF SHA256: adfaf5e9fec12dc89857ea947b06d2923d49a8a0b3e45880b278b79bd22dab77
- BBL SHA256: df9459aff03776469572c8fdfa784a815e0cba8254f5805bf2906fba6c584737
- PDF: 7 letter-size pages; 149,393 bytes; unencrypted; no JavaScript.
- Page-1 metadata: v1A.0.121, July 14, 2026, 11:32 PDT (verified with pypdf).

## Truth-audit closure map

1. The title, abstract, introduction, and conclusion now unify the Note around the spin-sourced and zero-spin branches of one algebraic Cartan equation. The text explicitly says the identities are standard and identifies the contribution as convention-audited consolidation and bounded consequence.
2. The sourced Holst-modified connection equation is displayed. An invertible-tetrad dual-frame contraction proves \(e^{[I}\wedge T^{J]}=0\Rightarrow T^I=0\).
3. The three above-Planck NJL rows and every dependent magnitude claim were removed. No cutoff above \(M_{\rm Pl}\) is evaluated.
4. Every all-orders statement is localized to the local classical reduced action after solving the Cartan equation, canonical scalar matter, an invertible tetrad, real nonsingular constant \(\gamma\), matched standard boundary/background data, and exclusion of nontrivial global/topological and quantum/anomaly sectors. Equality of helicity solutions is separately conditioned on parity-symmetric initial data. Off-shell equality of the original first-order actions is expressly disclaimed.
5. The finite-density illustration is parameterized as \(3.6\times10^{-69}(n_\psi/100\,{\rm cm}^{-3})^2\rho_\Lambda\), identifies \(100\,{\rm cm}^{-3}\) as deliberately elevated, and uses honest precision.
6. The Fierz appendix now displays the normalized axial-to-scalar matrix element, the Grassmann exchange sign, and the multiplication into \(G_s=-3\kappa/16\) in one three-line bridge.
7. The Freidel–Minic–Takeuchi contorsion solution and back-substitution coefficient are displayed and checked in PRIMARY_SOURCE_CHECK.md; zero current gives \(C=T=0\) without inventing a coefficient.
8. Undefined Route labels, companion pipeline prose, above-Planck rows, and the garbled inline Pontryagin shorthand were removed from the active manuscript. The running discussion and Nieh–Yan/Pontryagin distinction were shortened. Table I values are rounded to two or three significant figures.
9. The density illustration explicitly cross-references the separate canonical-scalar theorem domain.
10. Repeated scope caveats were consolidated, while the primary-source literature boundary remains explicit.

## Claims-consistency checks

- Active manuscript and extracted PDF contain no 3.5571, 7.84158, or above-Planck cutoff row.
- Abstract, body, and conclusion use the same 3.6e-69 normalized density scale.
- Body and Table I use the same retained maximum scalar ratio, 2.15.
- The removed values remain only in historical comments/review records or the separately retained reproducibility script output; they are not live paper claims.
- Shared site, SSOT, tracker, and version.json were intentionally not mutated. version.json was already stale/dirty in another live lane and was outside this scoped commit.

## LaTeX and visual audit

- Clean Tectonic compile from deleted intermediates: pass.
- LaTeX errors: 0.
- Undefined references/citations/control sequences: 0.
- Overfull hboxes/vboxes: 0.
- Raw path-like \texttt strings: 0.
- Machine-specific absolute paths: 0.
- Date overflow risk: 0; page 1 visually inspected.
- Visual audit: all 7 pages inspected at 110 dpi. No clipping, gutter crossing, overlap, malformed table, off-page equation, title/date overflow, or bad float placement was observed.
- The long-standing xdvipdfmx warning “Object @table.1 already defined” persists with one active REVTeX table. It produces no duplicate source table, bad reference, or visible PDF defect and was not introduced by this closure.

## URL audit

- PDF annotations: 100.
- Unique URI targets: 19 (18 HTTP(S), one mailto).
- HTTP results: 14 returned HTTP 200.
- Four DOI links reached their publisher targets but the final publisher response was HTTP 403 under command-line bot protection (APS/AIP); these are not missing repository artifacts.
- All three linked repository artifacts exist locally at the exact linked paths.
- Exact targets and results are in proof/audit/urls.tsv and proof/audit/http-status.tsv.

## Honest status

This bundle proves implementation and PDF quality of the v1A.0.121 closure. It does not prove ACCEPT/minor-only reviewer convergence. The v1A.0.120 panel contained surviving major findings, and no fresh exact-PDF panel was dispatched here by instruction.

MANIFEST.sha256 is the integrity root for every other file in this bundle.
