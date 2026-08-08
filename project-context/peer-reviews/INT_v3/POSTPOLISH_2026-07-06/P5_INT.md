# P5 v0.1.103 — POST-POLISH INT (Claude leg, full-source, read-only)

**Paper:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
**Scope:** verify the D-round polish (7df2e305) — title tail-drop, parity-null-first abstract, 3 restyled figures, paperIVarxiv/SUBMISSION_NOTE, new acknowledgments — under ZERO-numbers-changed.
**Verdict: MINOR-REVISIONS (content faithful, zero-numbers CONFIRMED; one figure-path regression to fix).**

## Zero-numbers guarantee — CONFIRMED
Diff numeric-token extraction, each checked against full current + parent `.tex`:
- Abstract "additions" `0.0007`, `0.31`, `0.76` are the headline null values pulled UP into the new lead paragraph (counts 7→8, 17→18, 3→4 — purely additive; already in body at :693+). ✓
- `20260515` (seed) count rose only because the new acknowledgments discloses it — a provenance disclosure, not a science number. ✓
- Title-footnote `2007`/`2012` (Hahn/Hoffman) dropped from the footnote but retained 12×/7× in body incl. the `sec:vweb` note the condensed footnote now points to. ✓
- **0 distinct numeric values added or deleted vs v0.1.102.**

## Title tail-drop — no meaning lost
Dropped "with a Secondary Tidal-Tensor Cross-Check"; footnote condensed to `see \S\ref{sec:vweb}`. The full T-Web/V-Web nomenclature note (Hahn2007 φ_k=−δ_k/k², not Hoffman2012 V-Web) survives at :673–681. Served PDF page-1 title verified (pdftotext): "…Void Null Test on 56,981 DESI DR1 Spirals". ✓

## Parity-null-first abstract — caveats kept
New `\textbf{Headline result:}` lead states Δf_CW=+0.0007, z=+0.31, p=0.76, parity across all 5 void-finders. Monopole-invariance caveat consolidated 3+→ STATED ONCE (":Independence from Paper~IV internals" para, :625+: "algebraically invariant under any catalog-wide monopole shift"). GZ1 model-independent cross-check (z=−0.54σ, N=46,017), a-priori primary-path designation, and post-hoc flag all retained. ✓

## paperIVarxiv / SUBMISSION_NOTE — coherent
`\paperIVarxiv = arXiv:XXXX.XXXXX` placeholder (:24) used consistently (:626,:897,:939,:1064); `submissions/P5/SUBMISSION_NOTE.txt` present + coordinated-submission framing coherent. ✓

## Acknowledgments — accurate
New block (:3977): DESI facility ack ("DESI is supported by the U.S. DOE and the U.S. NSF") accurate; DESIVAST VAC credited; AI-methodology disclosure + seed 20260515 correct. ✓ (Standard DESI ack is normally longer, but the abbreviated form is factually correct.)

## Regression
[MINOR] **Restyled 300-dpi figures are NOT the ones embedded in the compiled PDF.** Script-11 was updated to `savefig.dpi=300` and regenerated `pipelines/p5_desi_chirality/figures/*.png` (300 dpi, 1710×1230 etc.). But the paper has NO `\graphicspath`; `\includegraphics{fig_p5_cw_by_env_bar.png}` (:1672, :1309, :2293) resolves relative to `paper/`, where STALE 150-dpi copies (852×613, last touched EXT11 commit f056b496) still sit and were NOT updated by the D-round. So the served PDF embeds the OLD 150-dpi figures. **Values identical** (same committed JSON/CSV generator) — presentation-only, not a numbers issue. Fix: copy the 3 regenerated `figures/*.png` into `paper/` (or add `\graphicspath{{../figures/}}`) and recompile.
