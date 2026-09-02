# P4' status — current authoritative section

**Current candidate:** v4P.0.1 · `pipelines/p4prime_chirality_test/paper/main.tex`
**Directive-P readiness:** not yet scored (draft just created; no review board run)

## Lineage

P4' folds two already-reviewed sources into one ≤15-page ApJS-style paper,
per `project-context/PORTFOLIO_DECISION_2026-09-02.md` (Track C1 Addendum)
and `project-context/NEXT_SCIENCE_LEDGER.md` item 5:

- **P4** v1.0.274 · `pipelines/p2_chirality/chirality_catalog_paper.tex` —
  the 8,474,531-galaxy DESI Legacy DR8 catalog and its primary real-space
  chirality-dipole null (HC, $N_{\rm support}=887{,}472$;
  $z_{\rm mom}=+0.635$, $p=0.238$; $A_{95}^{\rm obs}\simeq0.98\%$).
- **P5** v0.1.147-2026-08-03 · `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` —
  the DESIVAST void/non-void environment contrast on 145,766 classifier-labelled
  galaxies ($\Delta f_{\rm CW}=+0.00145$, $p=0.66$), folded in as one
  condensed section rather than kept as a standalone 42-pp paper.

P4' adds one new section not present in either source: **"The black-hole-universe
prediction and its exclusion"** (Sec. 5 of `main.tex`), which reads Poplawski's
rotating-black-hole-universe papers (arXiv:1007.0587, 1111.4595, 1410.3881,
1910.10819) and finds they state only a qualitative preferred-axis alignment
tendency, not a computed dipole amplitude. Under the minimal closure needed
to make the claim testable ($A_{\rm pred}\approx\eta$, the alignment
fraction), the catalog's own $A_{95}^{\rm obs}\simeq0.98\%$ sensitivity floor
excludes $\eta>0.98\%$ at $\geq95\%$ coverage — a factor of $2$–$20\times$
below the $\sim7$–$33\%$ amplitudes reported by Longo (2011) and Shamir
(2012, 2020, 2022, 2025), the observational literature the model is invoked
to explain. This confirms the independent reanalyses of Iye, Yagi & Fukumoto
(2021, arXiv:2011.00662) and Patel & Desmond (2024, arXiv:2404.06617). No
bounce claim is made beyond this stated test (Sec. 6, Discussion, is
explicit that this bears on the black-hole-universe model's spin-axis claim
only, not on the separate matter-bounce cosmology this program otherwise
develops).

Computation for the exclusion is in the committed, deterministic script
`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py`
(numpy only; no fitting, no randomness — every output is a literal cited
input or a closed-form arithmetic function of inputs), output
`research/bh_universe_dipole/outputs/poplawski_dipole_exclusion_2026_09_02.json`.
Reproducibility manifest:
`reproducibility/manifests/experiments/p4prime-bh-universe-dipole-exclusion.json`.

No number in P4' is re-derived from raw data; every quantitative result is
quoted verbatim (with a section pointer) from the reviewed P4 v1.0.274 and P5
v0.1.147 sources, or is a deterministic output of the exclusion script above.
The catalog pipeline was NOT re-run.

## Current build

- **Version:** v4P.0.1, dated 2026-09-02.
- **Pages:** 6 (target ≤15; well under budget — no appendix/systematics cuts
  were needed to hit the page target, so full systematics diagnostics were
  simply not duplicated here and are pointed at the archived P4/P5 sources
  instead, per the fold-in mandate).
- **Compile:** 4-pass `pdflatex`, 0 undefined references/citations, 0
  overfull hboxes, 0 LaTeX warnings in the final pass log.
- **Visual audit:** every page rendered via `pdftoppm -r 60` and inspected;
  no column overflow, no figure/table escapes. Figure 1 (per-pixel HC
  CW-fraction sky map, from P4) and Figure 2 (T-Web secondary cosmic-web
  diagnostic bar chart, from P5) render cleanly; Table 1 (literature
  amplitude vs. $A_{95}^{\rm obs}$ comparison) is new to P4'.
- **PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf`
  — MD5 `d3e6f077ad5d772ed25d9f5d0b4c2140`,
  SHA-256 `a9cc26183c631ba88d021edc4b46f35a295832a9b1ceb7879aacf8d38253099f`.
  Mirrored byte-identically to
  `site/public/papers/paper4prime_chirality_test_v4P.0.1.pdf` and
  `public/papers/paper4prime_chirality_test_v4P.0.1.pdf`.
- **Registry:** `project-context/draft_paper_registry.json`, id `P4P`.
- **Bibliography:** manual `\begin{thebibliography}` in `main.tex` (matching
  the house style of both folded-in sources, neither of which uses
  bibtex/biber); a deduplicated `references.bib` documentation copy is
  co-located at `pipelines/p4prime_chirality_test/paper/references.bib`.

## Open gates (this draft has NOT been through review)

- No INT or EXT review board has been run on P4'. Directive-P readiness is
  unscored; this is a fresh draft, not yet in the R-round convergence loop.
- Site/Convex sync (`papers.ts`, `live-status.ts`, review timeline, Convex
  `paperVersions:bump`) has NOT been done — out of scope for the drafting
  worker that produced this version; site code was intentionally not
  touched per the drafting mandate.
- `PAPER_LINEAGE` (if/when it tracks P4'/P5-retirement formally per directive
  R3) has not been updated by this draft — P4 and P5 originals were left
  untouched, as instructed; the fold-in decision itself is already recorded
  in `PORTFOLIO_DECISION_2026-09-02.md` and `NEXT_SCIENCE_LEDGER.md` item 5.
- Whether/when P5's standalone 42-pp paper is formally retired (vs. kept as
  an archived companion with its own diagnostics) is a Houston-gated
  decision per the portfolio addendum ("retire the MCMC companion to
  Zenodo"-style disposition), not made by this draft.
- Houston sign-off (readiness 95→100) has not been sought.

## Historical status ledger

(none yet — this is the first entry for P4')
