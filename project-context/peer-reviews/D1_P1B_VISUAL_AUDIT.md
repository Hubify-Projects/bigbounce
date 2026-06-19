# D1 P1B — Visual / Packaging Audit (D-ROUND, camera-ready)

**Paper**: P1B v1B.0.74, 21 pp, letter, revtex4-2 two-column
**Rendered PDF**: `arxiv/paper1b_mcmc_companion.pdf` (md5 a29137f5)
**Source**: `arxiv/paper1b_mcmc_companion.tex`
**Scope**: VISUAL / layout / float-packaging only. Science, structure, and
numeric findings from the D1 vendor reviews are out of scope here (logged to the
science R-round, not this file).

## Float inventory (grep of .tex)

| # | Type | Line | Width | Lands | Content |
|---|------|------|-------|-------|---------|
| Fig 1 | `figure` | 1682 | `\columnwidth` | p.6 (L col) | 6-param ΛCDM+ΔNeff corner |
| Fig 2 | `figure` | 1693 | `\columnwidth` | p.6 (L col) | ΔNeff marginal posterior (a)+(b) |
| Fig 3 | `figure*` | 1713 | `0.85\textwidth` | p.7 (full) | NaMaster recovery (a)+(b) |
| Fig 4 | `figure` | 2569 | `\columnwidth` | p.14 (L col) | Spectator-ALP 3×3 triangle |
| Table I | `table` | 1384 | 1-col `[t]` | p.19 | ΛCDM+ΔNeff posterior means |
| Table II | `table*` | 1447 | full | p.19→20 | w0wa CPL posterior |
| (3 more `table*`) | — | 2080/2541/2830 | full | p.20–21 | dataset/relic/claims |

NaMaster recovery present (Fig 3), corner present (Fig 1), ALP triangle present
(Fig 4), convergence/scatter shown in Fig 3b error bars. Figure suite is
complete for an MCMC companion.

## Truth-audit of vendor VISUAL claims

| Vendor claim | Verdict | Evidence (rendered PDF) |
|---|---|---|
| OpenAI: Fig 2a–b axis labels truncated — "8"→σ8, "m"→Ωm; glyph clipping (p.6) | **FALSIFIED** | 300-dpi zoom of p.6: Fig 1 corner labels render `n_s, τ, Ω_m, S_8, σ_8, ΔN_eff, H_0` with correct subscripts; Fig 2 x-axis `ΔN_eff`, legend clean. The "8"/"m" was a reviewer-side pdftotext/raster artifact, not in the PDF. No fix needed. |
| OpenAI: Table I caption typography artifacts "0 . 1 σ", "132 ,949" (p.19) | **FALSIFIED** | 300-dpi zoom of p.19 caption: renders "within 0.1σ", "sub-0.1σ" cleanly, no broken spacing. Extraction artifact. No fix. |
| Grok/OpenAI: Fig 1 is "filler" / no new physics | **OUT OF SCOPE** (science, not visual) | — |

No vendor surfaced a real visual/packaging defect. The two genuinely
visual-sounding items are both reviewer-side rasterization artifacts.

## Self-found VISUAL findings (page-by-page render @ 80/150/220 dpi)

| SEV | Page/loc | Issue | Concrete LaTeX fix |
|-----|----------|-------|--------------------|
| MINOR | p.19, Table I (`table` `[t]`, L1384) | Single-column `table` containing a 3-column wide-content tabular sits in a `table*`-shaped region with a large empty band to the right; the caption + footnotes are very long for a 1-col float and crowd the column. | Acceptable as-is OR promote to `table*` so caption/footnotes use full width and reduce vertical crowding. Low priority. |
| MINOR | p.14, Fig 4 (`figure`, `\columnwidth`, L2569) | 3×3 ALP corner squeezed into one column; off-diagonal contour panels + tick labels are small/cramped relative to the same plot's information density. | Consider promoting to `figure*` at `width=0.85\textwidth` (mirror Fig 3) so the triangle is legible; right column on p.14 has room. ADD-quality upgrade, not a defect. |
| POLISH | p.6, Fig 2 title | Matplotlib title uses literal `---` (three hyphens) instead of an em-dash; baked into the PNG. | Regenerate PNG with `—` if the figure is re-rendered; not a `.tex` fix, do-not-block. |

## Figure-ADD opportunities (optional, not blocking camera-ready)

- **ADD (echo of OpenAI P1B-n*)**: a small Δϕ/fa-vs-(m/H0, θ_i) envelope contour
  panel would visualize the ALP parameter-space prose in §VI. Pairs naturally as
  a second panel beside Fig 4. Optional enhancement.
- **Fig 4 → `figure*`** (above) doubles as an ADD-quality legibility upgrade.

## Verdict

**Visually CAMERA-READY-CLEAN.** Zero overflow into margins or adjacent columns
across all 21 pages; no broken equations; no orphaned headings or bad page
breaks observed at render. Every axis label, legend, and table is legible at
print scale. The only actionable VISUAL items are two MINOR legibility/packaging
upgrades (Fig 4 width, Table I width) — both quality polish, neither a defect.
Both vendor-raised "visual" defects are reviewer-side extraction artifacts and
require no change.
