# P1A v1A.0.122 CQG Note bounded-clarity closure audit

Date: 2026-07-14 PDT

Scope: exact implementation of the truth-audited v1A.0.121 minor-only board. No new reviewer panel, regulator calculation, numerical result, readiness change, SSOT change, or site change is claimed in this lane.

## Exact frozen manuscript

- Canonical source: `arxiv/paper1a_ech_nogo.tex`
- Canonical PDF: `arxiv/paper1a_ech_nogo.pdf`
- Closure source: `closure/P1A_v1A.0.122.tex`
- Closure PDF: `closure/P1A_v1A.0.122.pdf`
- Closure bibliography: `closure/P1A_v1A.0.122.bbl`
- Source SHA-256: `9f83351baa7a47dc11771927a12e05259c70a0d74040b46d43e56390cbfc9adc`
- PDF SHA-256: `e2607d1a8476aa8df9e5e89b04595655b81048be34cabb4bec273e59c4c87e04`
- BBL SHA-256: `df9459aff03776469572c8fdfa784a815e0cba8254f5805bf2906fba6c584737`
- PDF: 7 letter-size pages; 149,503 bytes; unencrypted; no JavaScript.
- Page-1 metadata: `v1A.0.122`, `July 14, 2026`, `1:11 PDT` (verified with pypdf).

## Exact finding closures

1. **P1A-121-01 — dimensional benchmark wording: CLOSED.** Abstract and discussion now call the density illustration a dimensional coefficient benchmark, not an observational consequence; the conclusion retains explicit non-constraint language.
2. **P1A-121-02 — density anchor: CLOSED WITHOUT NEW PHENOMENOLOGY.** The existing deliberately elevated `100 cm^-3` normalization remains explicitly illustrative, neither a cosmological-density estimate nor a preferred state. No relic-neutrino or ensemble calculation was invented.
3. **P1A-121-03 — Cartan source/coefficient bridge: CLOSED.** A convention-pinned intermediate line displays `4 pi G=kappa/2` and `-(3/2) pi G=-3 kappa/16`, cross-referenced to the sourced equation, contorsion solution, and Freidel--Minic--Takeuchi Eqs. 17/23.
4. **P1A-121-04 — coefficient-one/contact/Holst/state separation: CLOSED.** The abstract now explicitly separates `kappa n^2`, the `3/16` contact factor, the finite-Holst factor, and the state-dependent renormalized composite.
5. **P1A-121-05 — cutoff and axial diagnostic scope: CLOSED.** Table I repeats that `Lambda=M_Pl` is only a bookkeeping ceiling and that `R_A` is a coefficient-magnitude benchmark, not an axial condensation threshold.
6. **P1A-121-06 — standard boundary data: CLOSED.** The theorem now names matched background, initial, and boundary data and defines standard boundary data as usual falloff with the first-order variational surface contribution set to zero.
7. **P1A-121-07 — Fierz ordering cross-reference: CLOSED.** The first main-text scalar-channel check now points directly to Appendix A's exchange ordering and Grassmann sign.
8. **P1A-121-08 — Euclidean-to-Lorentzian barrier: CLOSED NARROWLY.** The text states only the evidenced missing bridge: a matched physical Lorentzian cosmological stress tensor and observable derived from the Euclidean running results. It invents no Wick-rotation failure mechanism.
9. **P1A-121-09 — TB/EB expansion: CLOSED.** The active theorem text expands them as temperature--B-mode and E-mode--B-mode CMB cross-power spectra.
10. **P1A-121-10 — alternate regulators: CLOSED AS OPEN SCOPE.** The appendix states that no alternate regulator was evaluated and therefore claims no outcome for the stability condition.
11. **P1A-121-11 — PACS and immutable provenance: CLOSED.** `showpacs` and the active PACS line were removed. The three reproducibility artifacts now link directly to reviewed commit `b587cb7bb8e075aa9d0245ba8257fcef7ff196b8`.

## Derivation-fabrication gate

`NEVER_FABRICATE_DERIVATION.md` records the strict added-line scan. The only two triggered mathematical lines are arithmetic normalization identities supported in the same paragraph by source equations and `Freidel2005`. Verdict: **CLEAN**.

## Compile and LaTeX audit

- The preferred four-pass `pdflatex` route was unavailable on this host (`pdflatex: command not found`) before source ingestion.
- Tectonic 0.16.9 was run with retained logs/intermediates and two forced reruns; it ran BibTeX and produced the final PDF.
- LaTeX errors: **0**.
- Undefined references/citations/control sequences: **0**.
- Overfull hboxes/vboxes: **0**.
- Raw path-like `texttt` strings: **0**.
- Long `date` overflow candidates: **0**.
- Mid-paragraph ad-hoc table candidates: **0**.
- Known non-blocking warnings: underfull prose boxes only; REVTeX/xdvipdfmx repeats the pre-existing `Object @table.1 already defined` warning with one visible source table and no rendered duplication.

## All-page visual proof

All seven pages were rendered at 140 dpi under `proof/render/` and inspected individually. Page 1 title/date/abstract, the new normalization bridge on page 2, boundary and running language on page 4, cross-power expansion and discussion on page 5, immutable code links/Fierz appendix on page 6, and the cutoff table/regulator scope on page 7 are legible. No clipping, margin loss, gutter crossing, overlap, malformed equation, table overflow, duplicate rendered table, title/date overflow, or bad float placement was found.

**Visual verdict: PASS.**

## URL and path proof

- PDF annotations: 21 unique URI targets (20 HTTP(S), one mailto).
- Five repository file URLs map to existing local paths; the three immutable links additionally pass `git cat-file` at commit `b587cb7b`.
- All five arXiv links return 200.
- Five publisher DOI routes return 200; four resolve to valid AIP/APS publisher targets and then return 403 bot protection.
- The three newly pinned file URLs plus the commit-tree URL are typed **PRE-PUSH**, not missing content: commit `b587cb7b` is in the local main ancestry but `origin/main` is stale and does not contain it yet. The serialized parent push will publish that ancestor; recheck these four URLs after push.
- Full targets and evidence are recorded in `proof/audit/urls.tsv`.

## Honest status

The bounded source closure, exact PDF, derivation gate, and local path/all-page audit pass. Readiness is unchanged. Automated minor-only review is not human journal acceptance. The only incomplete publication check is the remote HTTP resolution of the immutable commit URLs, which cannot pass until the already-existing local ancestor is pushed by the serialized parent workflow.
