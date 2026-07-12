# P3 — ApJS variant (AASTeX conversion)

**Bundle:** `arxiv_p3_apjs_v3.1.155.tar.gz`
**Class:** AASTeX v7.0.1 (`\documentclass[twocolumn]{aastex701}`)
**Source of record:** `pipelines/p3_anomaly_engine/paper3_apjs.tex` (v3.1.155)
**Derived from:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (revtex4-2, v3.1.155) — the PRD version, which is UNCHANGED.

---

## What this is

A **format-only** conversion of the P3 multi-survey autoencoder anomaly catalog
from Physical Review D (revtex4-2) to **The Astrophysical Journal Supplement
Series** (AASTeX). Every number, claim, table value, figure, citation, and the
AI-disclosure / data-availability text is **byte-identical** to the revtex
source — a `diff` of the two files from `\begin{abstract}` to `\end{document}`
shows only the four mechanical format edits listed below. Zero content change.

## Venue rationale

See `submissions/P3_VENUE_DECISION.md`. Three independent referees (Gemini INT,
ChatGPT EXT, OpenAI INT) converged on the same structural point: P3 is a
**catalog / data-release paper**, and PRD is the wrong venue — the natural home
is a catalog journal, with **ApJS named first** by the Gemini referee. The
science is unanimously agreed to be supported; the disagreement was purely venue
fit. This variant retires that objection before the human round by matching the
manuscript to the venue the referees pointed to. The arXiv posture is unchanged
either way: `astro-ph.IM` primary, `astro-ph.CO` + `astro-ph.GA` cross-list.

## What differs from the revtex (PRD) version — format only

1. **Document class.** `\documentclass[...]{revtex4-2}` →
   `\documentclass[twocolumn]{aastex701}`. AASTeX v7 loads amsmath, amssymb,
   graphicx, hyperref, xcolor, and natbib itself; the redundant `\usepackage`
   lines were dropped and `\setcitestyle{numbers,square,comma}` forces AASTeX's
   natbib into the numeric citation style the paper's inline numbered
   `\thebibliography` uses.
2. **Frontmatter.** revtex `\author`/`\email`/`\affiliation` reordered to the
   AASTeX v7 required order (`\author` → `\affiliation` → `\email`); `\maketitle`
   removed (AASTeX v7 typesets the frontmatter automatically — calling
   `\maketitle` after the abstract creates a phantom second author in v7).
3. **Table notes.** The three numbered `\footnotemark[1..3]` /
   `\footnotetext[1..3]` pairs inside the wide `tab:provenance` table (a
   revtex-only optional-argument form AASTeX v7 disables) → AASTeX
   `\tablenotemark{a..c}` / `\tablenotetext{a..c}{...}`. Note text unchanged.
4. **One in-title cross-reference.** The `\ref{tab:survey_summary}` inside a
   run-in `\paragraph*` title is pre-stored in a macro so AASTeX v7's run-in
   uppercasing does not mangle the label; rendered text is identical.

The `ruledtabular` environment is provided natively by AASTeX v7, so all ten
source tables convert verbatim.

## Compile

```
pdflatex paper3_apjs && pdflatex paper3_apjs && pdflatex paper3_apjs
```

No bibtex pass (bibliography is an inline numbered `\thebibliography`).
Requires the TeX Live `aastex` package (ships `aastex701.cls`) and `epsf`.
Standalone-verified from a clean directory: **40 pages, 0 undefined references,
0 undefined citations, 0 errors** (the only console notice is natbib's
auto-recovery into numeric style, which is the intended style).

## Not touched

The PRD version (`paper3_draft.tex`) and its bundles under `submissions/P3/`
and `pipelines/p3_anomaly_engine/paper3_arxiv_*.tar.gz` are unchanged. This ApJS
variant is additive; choosing a lane (ApJS vs PRD vs MNRAS) remains Houston-gated
per the venue decision packet.
