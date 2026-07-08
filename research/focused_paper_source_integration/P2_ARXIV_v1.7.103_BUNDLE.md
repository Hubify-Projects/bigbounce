# P2 arXiv bundle — v1.7.103 (RSD-Fisher closure)

**Date:** July 8, 2026
**Paper:** `research/focused_paper_source_integration/02_full_draft.tex`
**Round:** c14 redshift-space (RSD) tree bispectrum Fisher applied — retires the
"independent Fisher is real-space monopole only (~18% offset per Heinrich)"
limitation with real computation.

## What changed (v1.7.102 → v1.7.103)
- **para:reconcile limitation retired.** The single "real-space monopole (no RSD
  multipoles ℓ=0,2,4, ~18% one-directional/conservative offset)" limitation
  sentence is replaced by the completed redshift-space extension.
- **RSD result stated (VERIFIED, from committed `c14_rsd_multipole_fisher.json`):**
  - σ(f_NL^local)_RSD = 0.415 (bias-fixed) / 0.449 (bias-marginalized) vs c13
    real-space 0.687 → +34.7% tighter (RSD/Heinrich ratio 0.64).
  - σ(f_NL^bounce)_RSD = 0.417 / 0.449; r_eff ≈ 0.99 persists in redshift space.
  - f→0 limit reproduces c13 to six significant figures.
- **Headline discipline:** unmarginalized −35/16 significance updated
  3.2–3.5σ (real-space, labeled the conservative floor) → 4.9–5.2σ (RSD,
  labeled unmarginalized, before the systematic + GR-projection budget). The c12
  GR-projection marginalization bracket (ρ≈0.95; marginalized ~0.8–1.3σ edge) is
  retained EXACTLY.
- **Honest reconciliation** of +34.7% vs Heinrich ~18% included as computed
  (full real-space→redshift-space gain vs the narrower monopole→multipole gain).
- **Approximations stated:** tree-level, linear k_max, b2=bs2=0, no
  fingers-of-God (noted conservative at high-k).
- **New bib entries:** `Kaiser:1987`, `Scoccimarro:1999`.
- **No headline f_NL value changed** (−35/16 unchanged). Nothing fabricated.

## Provenance (VERIFIED artifacts)
- Script: `scripts/c14_rsd_multipole_fisher.py`
- Output: `outputs/c14_rsd_multipole_fisher.json`
- Extends: committed, validated `scripts/c13_independent_bounce_fisher.py`

## Directive-G hygiene (all in this bundle)
- [x] `\date` → July 8, 2026; v1.7.103 changelog block added in `.tex`.
- [x] Recompiled with bibtex, 0 undefined references/citations.
- [x] `/latex-audit`: 0 overfull hboxes; visual render of para:reconcile pages
      (25–26) confirmed clean two-column layout, no column overflow, `\path{}`
      filenames break cleanly.
- [x] PDF mirrored byte-identical (md5 `cca2e95f45507d02bb3c76951f83d090`, 36 pp)
      to all served paths:
      - `public/papers/02_full_draft_v1.7.103.pdf`
      - `public/papers/02_full_draft.pdf`
      - `site/public/papers/02_full_draft_v1.7.103.pdf`
      - `site/public/papers/02_full_draft.pdf`
- [x] Convex `paperVersions:bump` (paper-2, v1.7.103, md5 cca2e95f, 36 pp).
- [x] Convex `activityFeed:add` closure entry.
- [x] `site/src/data/papers.ts` + `live-status.ts` updated (version, date, pages,
      hrefs, keyResults, tldr, pendingWork).
- [x] `site/src/data/reviewTimeline.ts` closure-wave entry added.

## arXiv tarball
- File: `paper2_arxiv_v1.7.103.tar.gz` (md5 `53e56934c5e7c55d25d9ce891fb3aee6`)
- Alias refreshed: `paper2_arxiv_submission.tar.gz`
- Contents: `02_full_draft.tex`, `02_full_draft.bbl`, `focused_paper_refs.bib`,
  `bphi_sensitivity.pdf`, `fig1..fig5.png` (6 figures).
- **Standalone-verified:** clean re-extract into /tmp + 2-pass pdflatex (bbl
  present, no bibtex needed) → 36 pages, 0 undef-refs, 0 fatal errors.

## arXiv submission kit (unchanged from prior version)
- Title/authors/abstract/categories: as in `abstract_for_webform.txt`.
- Primary category: astro-ph.CO.
- Author: Houston Golden — houston@hubify.com.
