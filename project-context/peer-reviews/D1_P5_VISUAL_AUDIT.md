# D1 P5 — D-Round Visual / Packaging Audit (camera-ready)

**Paper**: P5 v0.1.82 (32pp) — `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=401a73f9
**Scope**: VISUAL / packaging only (figures, tables, equations, layout, typography, float placement). NOT science.
**Method**: Read rendered PDF pages 1-2, 6-8, 11-12, 15-16, 22-23, 26-27, 31-32 as images; cross-checked D1 vendor reviews (Gemini, OpenAI-methodology, Grok, Perplexity[failed]); grepped .tex for floats / `\artifact` macros / grid notation / units / log overfull.

## Float inventory (.tex grep, verified)
- **Figures**: 9 total. Single-column (`figure`): Fig 1 (z-hist p4), Fig 2 (volume-fraction PIE p6), Fig 3 (cw-by-env bar p8), Fig 4 (cw_vs_z), Fig 6 (sensitivity heatmap), Fig 7 (Phase-2 heatmap p16). Full-width (`figure*`): Fig 5 (density-quintile 2-panel p11), Fig 8 (HEALPix skymap 2-panel p22), Fig 9 (T-Web vs Tempel 2-panel p26).
- **Tables**: ~20. Full-width (`table*`): Table VII (p15), the skymap/contrast tables, Table at p2260, p3092 (Appendix). All others single-column.
- **Log**: ZERO overfull/underfull hboxes — no hard margin overflow. Issues below are density/legibility/labeling, not column escape.

## Truth-audit of vendor findings
- Grok P5-E2 (pipeline paths in running text) — **VERIFIED**, root cause = 60× `\artifact{...}` macros rendering full repo paths via `\nolinkurl`. Dominant visual problem.
- OpenAI P5-E3 (Fig 8 top colorbar mislabeled) — **VERIFIED**, two colorbar labels physically overlap ("voids/pixel" collides with "Chirality σ_from half per pixel"). Serious.
- OpenAI P5-M1 (Fig 2 pie chart) — **VERIFIED**, pie present p6; bar chart is PRD-appropriate.
- OpenAI P5-M5 / P5-m4 (Fig 5 & Fig 9 lack (a)/(b) panel labels, caption says Left/Right) — **VERIFIED** both.
- OpenAI P5-M7 (Table VII `10†` dagger explained only in section-header row, not caption) — **VERIFIED**, minor.
- OpenAI P5-E1 (`2563` not superscripted) — **FALSIFIED in source**: `256^3` is correctly typeset (10× in .tex). The "256 3" the reviewer saw is a PDF text-layer extraction artifact in the dense abstract, not a rendering defect. NO FIX NEEDED (verify abstract render shows superscript — it does).
- OpenAI P5-E4 / P5-m6 (Mpc/h vs h⁻¹ Mpc) — **MOSTLY FALSIFIED**: .tex uses `Mpc/h` only 1×; h⁻¹ Mpc form dominates. Near-consistent already; one stray `Mpc/h` to normalize. Borderline NIT, not ESSENTIAL.
- OpenAI P5-m3 (Tables overflow → table*) — **FALSIFIED for the cited tables**: Table II, VII already fit; Appendix Tables XVI/XVII are narrow 5-col and fit single-column. No overflow.
- Gemini P5-M3 / Grok P5-M1 / OpenAI summary (abstract too dense, 32pp long) — **VERIFIED as packaging**: abstract env = 212 source lines, spills p1→p2; visually heavy. Real but science-adjacent (trimming = science-lead call).

## Prioritized fix list — [SEV] page/loc | issue | LaTeX fix

- **[ESSENTIAL] p22 Fig 8 top colorbar** | "voids/pixel" label overlaps the bottom-panel "Chirality σ_from half per pixel" label — two strings physically collide under the top map. | In `12_make_p5_*` figure script: give the top (count) panel its own colorbar with integer ticks labeled "Maximal voids per pixel"; reserve the diverging σ colorbar for the bottom panel only; increase vertical spacing between panels. Regenerate `fig_p5_healpix_skymap_nside32.png`.
- **[ESSENTIAL] throughout (60 sites)** | `\artifact{pipelines/p5_desi_chirality/outputs/…json}` macros render full repo paths inline in body text, figure/table captions (Table III p8, Table V p11, Table VII p15, p23, p26, Appendix C p31). Visually disruptive; reads as build-system leakage. | Redefine `\artifact{}` to emit a short hyperlinked artifact ID (e.g. `\href{\repoBase/#1}{[A12]}`) and collect the full path→ID map in one Appendix C table; OR strip captions/body to a one-line "see data repository" and keep paths only in Appendix C. Do NOT leave 60 inline `\nolinkurl` paths.
- **[MAJOR] p6 Fig 2** | volume-fraction PIE chart — poor for precise comparison, slice labels (Cluster 1.0%) cramped. | Replace with horizontal bar chart, fractions on x-axis, value labels at bar ends; regenerate `fig_p5_volume_fractions_pie.png` → `..._bar.png` and update `\includegraphics` + caption.
- **[MAJOR] p11 Fig 5 & p26 Fig 9** | caption says "Left/Right" but panels carry no (a)/(b) labels. | Add `(a)`/`(b)` text annotations top-left of each panel in the figure scripts; change captions to "(a) … (b) …". Files: `fig_p5_cw_vs_density.png`, `fig_p5_vweb_vs_tempel_overlay.png`.
- **[MINOR] p15 Table VII** | `10†` dagger defined only in an italic section-header row, not the caption. | Add to caption: "† R_s=10 Mpc/h is below the 25.9 Mpc/h grid scale (grid-unresolved; excluded from the robustness claim)."
- **[MINOR] p1–2 Abstract** | 212-line abstract spills p1→p2, very dense; runs straight into a 2nd abstract-like "Robustness" paragraph (Gemini P5-m1). | Packaging-only: trim to headline + top-level numbers; defer per-bin σ/n enumerations to body. (Coordinate with science-lead — content move.)
- **[NIT] multi-page** | one stray `Mpc/h` vs dominant `h⁻¹ Mpc`; `σ_from half` mixed math/text styling. | Global s/Mpc\/h/h^{-1} Mpc/; define one macro `\sigmahalf` and use in math mode in all captions/axes.

## Figure-ADD opportunities
- **[ADD-1]** No single "money figure" summarizing the headline null across ALL classifiers (DESIVAST 3-algo + T-Web + Tempel + ASTRA) on one panel with the ±Bonferroni band. A forest/whisker plot of Δf_CW ± CI per classifier, all overlapping zero, would let a reader grasp the null in one glance. Strong camera-ready add for a null-result paper.
- **[ADD-2 / optional]** Appendix schematic of the analysis tree (Table II) as a small dendrogram (primary Bonferroni-5 vs secondary-9 vs descriptive) — would replace the wall-of-rows table with an at-a-glance figure.

## Bottom line
NOT camera-ready-clean visually. Two ESSENTIAL items (Fig 8 overlapping colorbar labels; 60 inline `\artifact` repo-path leaks) must close before submission. Pie→bar, panel labels, dagger caption are quick MAJOR/MINOR fixes. The `256³` and table-overflow vendor flags are FALSIFIED (source already correct / tables fit). Recommend ADD-1 forest plot.
