# Paper 1 Companion Technical Note — arXiv Submission Staging

**Closes:** R42 finding `P1-OA-B6` (GPT-5 cross-model peer review,
2026-05-01) — Ref [28] (`Golden2026supplement`) was annotated "available
upon request from the author" in `arxiv/references.bib`. PRD reviewers
cannot evaluate non-public calculations. This directory stages the
companion note for arXiv deposit so the citation can change to a public
arXiv identifier.

## What this is

`Systematic Closure of Minimal First-Principles Routes to Dark Energy in
Einstein-Cartan-Holst Gravity` — a 41-page standalone technical note
documenting the four negative-result calculations referenced in
`arxiv/main.tex` §IV and §XVI:

1. NJL-condensate channel (scalar/pseudoscalar repulsive, subcritical by
   ~175× even when attractive).
2. One-loop fermion effective action after exact torsion elimination
   (no Barbero-Immirzi dependence at one loop).
3. Dynamical Barbero-Immirzi parameter γ → θ(x) (reduces to ALP, no novel
   gravitational content; cosmology yields stiff matter w = +1).
4. Parity-odd photon coupling (no minimal-model coupling; assumed coupling
   produces constant-β indistinguishable from generic ALP birefringence).

## Files

```
arxiv_companion_note/
├── README.md                            # this file
├── supplement_negative_results.tex      # canonical .tex (55 KB, ~41 pp)
└── supplement_negative_results.pdf      # locally compiled PDF (284 KB)
```

The .tex compiles standalone (article documentclass, inline
`thebibliography` — no external `.bib` file needed).

## Provenance

The canonical home of this note is
`research/paper2/ir_vacuum_program/supplement_negative_results.tex` (and
its compiled `.pdf`); both files in this staging directory are byte-copies
of those originals. The split out into `arxiv_companion_note/` is
**only** to make arXiv deposit a one-step `arxiv-tarball`-ready bundle:
the source compiles cleanly with `pdflatex` (no makeindex / no
bibliography pass) on a machine with `texlive-latex-extra` and
`texlive-fonts-recommended`.

## What Houston needs to do (arXiv-pending)

1. Log in to arXiv (`houston@hubify.com` account).
2. Submit `supplement_negative_results.tex` to `gr-qc` (cross-list:
   `hep-th`).
3. Once accepted (typically same-day), edit
   `arxiv/references.bib` and replace the `Golden2026supplement` entry
   with the assigned arXiv identifier:

   ```bibtex
   @misc{Golden2026supplement,
     author = {Golden, Houston},
     title  = {Systematic Closure of Minimal First-Principles Routes to Dark Energy in {Einstein-Cartan-Holst} Gravity},
     year   = {2026},
     eprint = {YYMM.NNNNN},
     archivePrefix = {arXiv},
     primaryClass  = {gr-qc}
   }
   ```

4. Recompile `arxiv/main.pdf` so the citation resolves to the public arXiv
   identifier instead of "available upon request from the author."

## Alternative path (rejected for this round)

GPT-5's review suggested an option to "Move the relevant derivations into
an appendix of this manuscript." We chose arXiv-deposit instead because:

- The note is 41 pages with its own theorem/proof structure; folding it
  into Paper 1 would push the main paper from ~31 pp to ~70 pp.
- The four negative results have independent value as a standalone
  technical reference.
- arXiv-deposit is a one-time Houston action; the appendix path requires
  re-architecting Paper 1 §IV and §XVI cross-references.

If arXiv submission is delayed past the next planned Paper 1 recompile,
the appendix path remains a viable fallback — but it is not staged here.

## Status

- `supplement_negative_results.tex`: ready for arXiv-deposit.
- `supplement_negative_results.pdf`: 284 KB, locally compiled
  (timestamps in canonical-source dir 2026-04-06).
- arXiv submission: **Houston-pending** (requires Houston's arXiv login).
- Post-submission `references.bib` update: blocked on arXiv ID assignment.
