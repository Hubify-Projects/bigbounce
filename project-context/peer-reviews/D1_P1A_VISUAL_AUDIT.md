# D1 — P1A Visual / Camera-Ready Audit (consolidated)

**Paper:** P1A v1A.0.78 — Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes (29 pp)
**Rendered PDF:** `arxiv/paper1a_ech_nogo.pdf` (md5 198cb994, 29 pp)
**Source:** `arxiv/paper1a_ech_nogo.tex`
**Scope:** VISUAL / PACKAGING ONLY. Science findings (operator dimensions, companion-paper
self-containment, σ-comparability) belong to the science R-round, not here, and are excluded
below except where they manifest as a layout defect.
**Date:** 2026-06-19

## Inventory (cross-checked against .tex)
- **5 figures:** Fig 1 (`figure*`, p.5, theory map), Fig 2 (`figure`, p.6, energy hierarchy),
  Fig 3 (`figure`, p.8, RG running / Hubble), Fig 4 (`figure`, p.15, detection timeline),
  Fig 5 (`figure*`, p.18, naturalness), Fig 6 (`figure`, p.22, detection forecast).
  (Caption numbering in PDF: theory-map=Fig1, hierarchy=Fig2, RG=Fig3, timeline=Fig4,
  naturalness=Fig5, forecast=Fig6.)
- **4 tables:** Table I (`table*`, p.4, exec summary), Table II (`table*`, p.17, 14 barriers),
  Table III (`table*`, p.21, discrimination), Table IV (`table*`, p.26, parameter summary).
- **LaTeX log:** 3 overfull hboxes (lines 1012, 1760, 3006); 60 underfull (mostly
  two-column justification slack — cosmetic, not actionable).

## Truth-audited findings (real visual issues only)

### HIGH
- **Table II (p.17) — narrow tabular floating in a full-width `table*`.**
  `\begin{tabular}{clll}` of 4 short text columns is `\centering`ed inside a `table*`,
  so it occupies only ~55% of the page and reads as a lost island with large empty
  side-margins. **Fix:** either (a) demote to single-column `table` (it fits a column
  comfortably), or (b) keep `table*` and force full-width with
  `\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}clll}` so the columns spread to
  the page edge. Option (b) preserves the executive-table look matching Tables I/III/IV.

### MEDIUM
- **p.12, Eq.(15) region — overfull hbox 13.1pt (line 1760).** The inline parenthetical
  after `\alpha_{\rm em}/(4\pi)\approx 5\times10^{-4}` (the "(more precisely ≈5.8×10⁻⁴…)"
  clause) pushes a math run into the right margin of the single column.
  **Fix:** break the long inline parenthetical into a following sentence, or wrap the
  numeric aside in `\mbox{}`-free prose; ensure the `\sim 10^{-61}` math has a breakpoint.
- **Fig 4 (p.15) vs Fig 6 (p.22) — near-duplicate single-column line charts.** Both plot
  "detection significance vs year 2024–2034" with the same three curves; Gemini (m1) and
  OpenAI (M1) both flag the redundancy. Visually this is two small, low-density single-column
  figures doing one job. **Fix (packaging):** merge into ONE figure, OR if both are kept for
  narrative reasons, promote the survivor to `figure*` (full width) and enlarge the title +
  legend + axis fonts, which are small at print scale in the current single-column render.
- **Fig 4 (p.15) — small chart chrome.** Title "Observational Detection Timeline (2024–2034)"
  and legend text are noticeably small in a single column; axis-tick labels are borderline.
  **Fix:** regenerate at larger base font (≥12pt) or render as `figure*`.

### LOW
- **p.5/p.8, Eq.(1) and Appendix-B Eq.(B1) — overfull hboxes 3.2pt / 5.2pt (lines 1012, 3006).**
  Sub-points-worth of overrun; not visible to the eye but trivially closable. **Fix:** add a
  discretionary break / `\!` thin-space tuning, or let the `align` line wrap one term earlier.
- **Fig 3 (p.8) lower panel — zero line unmarked** (Grok n2). The `ΔH/H_ΛCDM [%]` panel has
  no drawn y=0 reference line. **Fix (figure regen):** add a light `axhline(0)`.
- **Title-page abstract equation — NOT a real defect.** Gemini N2 ("garbled
  k_phys…e32…") and OpenAI n1 ("e −N spacing") are pdftotext/OCR artifacts; the *typeset*
  page-1 render is clean (`k^{phys}_{bounce}\sim k^{phys}_{SPHEREx}e^{N_tot-N_exit}`,
  `a^{-1}\propto e^{-N}`). No LaTeX change needed. Discarded.

## Figure-ADD opportunities (theory paper is figure-adequate but two gaps)
- **§IX / Table II — a schematic of the 14-barrier / 7-foundation+6-branch structure** would
  convert a 14-row text table + 14 prose subsections into a single legible map (Foundations
  A–G across the top, Branches H–O, arrows to the closed routes R1–R4). HIGH-VALUE add: the
  barrier logic is the paper's core contribution and is currently all-text. Mark as **ADD**.
- **§IV route-closure logic** — a small 4-route × closure-mechanism grid/flow (NJL→Planck-supp,
  one-loop→parity+Planck, Immirzi→mass-lock, parity-CMB→naturalness) would visually anchor the
  "four-route no-go." Lower priority than the barrier map. Optional **ADD**.

## Confirmed CLEAN (no action)
- Table I (p.4), Table III (p.21), Table IV (p.26): full-width `table*`, fill the page, readable
  fonts, footnotes correctly placed below. Good.
- Fig 1 (p.5), Fig 5 (p.18): `figure*`, legible, well-placed. Good.
- Fig 2 (p.6): single-column, legible. Good.
- No margin overlap between columns, no orphaned headings, no figure floating far from its
  reference, no overlapping elements. Page breaks are clean.
