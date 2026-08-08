# D1 P4 — Visual / Packaging Audit (D-ROUND)

**Paper**: P4 — Survey-Scale Galaxy Chirality (chirality_catalog_paper)
**Version**: v1.0.188 (23 pp)
**PDF**: `pipelines/p2_chirality/chirality_catalog_paper.pdf` (md5 lineage c47abc18, 33 MB)
**Source**: `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Reviewer**: D-ROUND visual lead (rendered all 23 pages as images + grep .tex floats)
**Scope**: camera-ready VISUAL/packaging polish ONLY. Science is frozen/accepted.

---

## Method

Rendered every page (1–23) as image at print size. Grepped .tex for all
`figure/figure*/table/table*/includegraphics/align/equation`. Cross-checked the
4 D1 vendor reports (Gemini, Grok, OpenAI, Perplexity) for **visual-only** items.

**Float inventory (counts):**
- Figures: 9 total → 5 single-column (`figure`: pie Fig.3, density Fig.5, conf-dist Fig.6, multipoles Fig.8, harmonic-completeness Fig.9), 4 full-width (`figure*`: TTA gallery Fig.2, sky map Fig.4, raw-vs-eq sky Fig.7, equivariance demo). All `width` correctly matched to env.
- Tables: 11 total → Tables I, III, IV use `table*` (full-width, correct); II, V, VI, VII, VIII, IX, X, XI single-column. Every wide-content table is already full-width.
- Display equations: 4 numbered + 1 `aligned` + 1 `align` (loss). None overflow.

---

## Truth-audit of vendor "visual" findings

| Vendor item | Claim | Verdict |
|---|---|---|
| Grok P4-N2 | "color bars / axis labels legible but non-standard abbrevs (NS, CCW) without legend in every panel" | **PARTIALLY VALID (NIT)**. Figs 2/4/7/8 are legible at print size; CW/CCW/NS are defined in body + captions. A per-panel mini-key is a polish nicety, not a defect. Keep as optional NIT. |
| Grok P4-E2 | "dozens of internal file paths / artifact tags in rendered PDF" | **VISUAL-ADJACENT but SCIENCE/packaging-policy**, not a layout defect. `\artifact{}` paths render as wrapped blue hyperlinks INSIDE the column (pp. 9,10,12,17,18,20) — they wrap cleanly, no margin overflow. Removal is a content decision (out of D-ROUND visual remit); they do NOT break the layout. |
| Gemini P4-E1 / Grok P4-N1 | future date "June 13, 2026" + commit/version in Data Avail. | **VALID but NON-VISUAL** (metadata/content). Out of D-ROUND scope; flagged by science round already. |
| Gemini P4-N1 | title very long | **VALID (NIT)** — title is 6 typeset lines (p.1). Stylistic only. |

No vendor reported a genuine overflow, squished table, or cramped multi-panel.

---

## Independent visual findings (all 23 pages rendered)

**Overflow / margin escape:** NONE. No overfull-hbox content reaches the margin
on any page. No equation runs into the gutter or adjacent column.

**Tables:** all 11 fit their column cleanly. Wide tables (I leg/conf summary,
III multipole 7-col, IV monopole) are full-width `table*` and readable. The
dense multi-footnote captions (Tables III, IV, X) are long but set at normal
size and do not overrun. Table IX = GZ1 confusion (3-col, clean) — note the
"leg×conf Table IX" referenced in the brief does not exist as a table; leg×conf
interactions are described in text only (no missing/squished table).

**Figures:** all 9 legible at print size. Colorbars on the Mollweide sky map
(Fig.4) and density map (Fig.5) have readable tick labels and units. Fig.2 TTA
gallery (4×4 panels, full-width) is crisp. Fig.8 grouped-bar pseudo-C_ell has
readable per-ℓ σ annotations. Fig.9 completeness curve axes/legend readable.

**White-space / float placement / orphans:** clean. Floats land on or near their
reference page. No orphaned headings, no stranded single lines, no large white
gaps. Two-column balance is good throughout including the appendix.

**Title block / date:** `\date{\paperTimestamp}` renders centered, no overflow.

---

## Prioritized fix list

The paper is **camera-ready-clean on visual/packaging.** No SEV-MAJOR or
SEV-MINOR layout defects. Only optional polish remains:

- **[NIT]** p.1 / Title — 6 typeset lines. *Optional:* shorten for impact
  (e.g. drop the "(3.2 Million Spirals)" parenthetical line, fold spiral count
  into abstract). LaTeX: edit `\title{...}` line breaks at .tex:334.
- **[NIT]** Figs 2/4/7/8 (pp. 6, 8, 10) — multi-panel figures rely on body text
  for CW/CCW/NS color↔class mapping. *Optional:* add a one-line in-panel key or
  caption legend line "(blue=CW, red=CCW)" for at-a-glance reading. Pure polish;
  current state is legible and defined.
- **[FIGURE-ADD — optional, low value]** No visual gap demands a new figure.
  The systematics story (Appendix D, eight anchors) is currently all-prose/tables;
  *if* an addendum is ever wanted, a single small "systematics-budget" summary
  figure (the 8 anchor σ's as a labeled forest/bar panel) would aid skimming —
  but the existing Table-driven presentation is complete and not a deficiency.

**No DO-NOW visual fixes.** Date/commit (Gemini P4-E1) and artifact-path policy
(Grok P4-E2) are content/metadata items owned by the science round, not packaging.

**Verdict: VISUAL CAMERA-READY.** All floats correctly sized, zero overflow,
all figures/tables legible at print size.
