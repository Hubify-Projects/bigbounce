# P5 D1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=401a73f9 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4896 chars)
**Wall time**: 300.5s

---

Referee report (Round D1: Design/Presentation QA only — visual/packaging issues; no science)

I reviewed the rendered 32-page PDF. Below are only visual/layout/packaging findings (figures, tables, layout, footnotes, typography, overflow, and presentational clarity). No scientific assessment is included in this D-round.

ESSENTIAL

- P5-E1 (Abstract, p.1): “2563 comoving grid” is used repeatedly (also elsewhere) as plain “2563” instead of 256^3 with a superscript. Required fix: typeset all grid sizes as 128^3, 256^3, 384^3, etc., throughout the paper, figures, and captions.

- P5-E2 (Title block/Abstract → Footnote placement, pp.1–3): The superscript “a” footnote marker for the T-Web definition appears awkwardly attached to a parenthesis in the title block/abstract and the actual footnote text appears much later on p.3. Required fix: anchor the footnote marker at its first T-Web mention and place the footnote text on the same page; alternatively convert it into a numbered footnote/endnote and move the long explanatory material into the main text or Appendix for cleaner layout.

- P5-E3 (Figure 8, p.22): Top panel is “DESIVAST maximal voids per HEALPix pixel,” but the colorbar is mislabeled “Chirality σfrom half per pixel” and shows a 0.2–1.0 scale inappropriate for a count map. Required fix: relabel the top-panel colorbar to “Maximal voids per pixel” with an integer scale covering the actual min–max. Ensure the bottom panel alone carries the “σfrom half” colorbar.

- P5-E4 (Unit notation consistency, multiple pages incl. Abstract, pp.1, 5–7, 15–17, 23): Mixed use of “Mpc/h” and “h−1 Mpc.” Required fix: standardize to Physical Review D style (h−1 Mpc) everywhere, including in figure axes and captions.

MAJOR

- P5-M1 (Figure style, p.6, Fig. 2): Pie chart for volume fractions is nonideal for PRD; slice labels can be hard to read and areas are poor for precise comparison. Required fix: replace Fig. 2 with a bar chart (with error bars if applicable) to improve legibility and quantitative readability.

- P5-M2 (Long filesystem paths in running text, many instances pp.1–2, 5–8, 9–13, 15–21): Numerous inline file paths and filenames (e.g., pipelines/p5_desi_chirality/outputs/…) appear in the main narrative and captions. These are visually disruptive and risk line overflow in two-column layout. Required fix: move all path-level details to Appendix C or a data-availability footnote; in the main text/captions, reference a short artifact ID or appendix table.

- P5-M3 (Internal cross-reference artifact in text, p.5): “the sec:vweb cross-reference label are retained for backward compatibility…” — this is build-system prose leaking into the scientific narrative. Required fix: remove internal cross-reference labels and build-log prose from the main text; if necessary, mention briefly in Appendix C.

- P5-M4 (Footnote formatting, p.5, step 5): The “1 Dimensional derivation: …” note is set as a run-in paragraph rather than an actual footnote/endnote, interrupting the numbered list. Required fix: convert to a real footnote or relocate into a short parenthetical after the equation; preserve the list structure.

- P5-M5 (Figure 5 caption and panel labeling, p.11): Two-panel figure relies on “Left/Right” in caption without panel labels in the figure. Required fix: add (a) and (b) panel labels in the figure and mirror them in the caption.

- P5-M6 (Terminology typesetting, many pages): The bespoke statistic “σfrom half” is inconsistently formatted (sometimes in math, sometimes plain text) and visually clumsy. Required fix: define a concise symbol (e.g., z1/2) once, use it consistently in math font, and avoid mixed text/math styling in captions and axes. Where the phrase must appear, use a consistent small-caps or roman style.

- P5-M7 (Table VII notation, p.15): Dagger markers “10†” appear in the first column, but the dagger is only implicitly explained in a section-header row. Required fix: explicitly define † in the caption (e.g., “† grid-unresolved (Rs below grid scale)”) and ensure the symbol is typeset consistently.

- P5-M8 (Figure/colorbar legibility, multi-figures pp.14, 16, 22): Colorbars have small tick labels relative to the map text; on print these may be hard to read. Required fix: increase colorbar font sizes and ensure adequate contrast for colorblind-safe palettes.

- P5-M9 (Abstract density and packaging, p.1–2): The abstract packs extensive procedural details, file paths, and parenthetical caveats that belong in Methods or Appendix. Required fix: trim the abstract to scientific headline claims and key numbers only; move pipeline and configuration enumerations to the body/appendix.

MINOR

- P5-m1 (Arcsecond symbol, multiple pages): Use proper unicode/TeX double-prime ″ rather than two ASCII primes where possible, and ensure consistent spacing (e.g., 1″ acceptance). Current “1′′” may render inconsistently across fonts. Required fix: unify on ″.

- P5-m2 (Equation typography, p.6 Eq. (1), p.7 Eq. (2), p.7 Eq. (3)): Ensure all functions (erfc−1, etc.) are upright roman; variables italic; and spacing around fractions is adequate. Align multi-part equations to avoid overfull lines in two columns.

- P5-m3 (Table width management, pp.8, 15, 31): Wider tables (Table II, VII, XVI–XVII) may overflow in a two-column layout. Required fix: set as table* (full-width) and ensure line-breaking within cells is balanced; consider smaller but legible font.

- P5-m4 (Figure 9, p.26): Add panel labels (a)/(b) and consider aligning y-axis ticks to the same fixed interval on both panels for easier visual comparison; presently the shared y-limits are fine, but panel labels would aid reference.

- P5-m5 (Caption verbosity, many figures): Several captions include long parenthetical artifact pointers. Required fix: keep captions self-contained and brief; move artifact pointers to Appendix C.

- P5-m6 (Unit spacing and hyphenation, multiple pages): Normalize to “25 h−1 Mpc Gaussian smoothing” (no slash, thin space between number and unit) and avoid inconsistent hyphenations like “25 Mpc/h Gaussian-smoothing.” Required fix: global style pass.

- P5-m7 (Typo/stray characters, p.13): Text shows “NSIDE 16 p /32/64” in one place (likely a stray “p”). Required fix: correct to “NSIDE = 16/32/64”.

- P5-m8 (Figure 1 axis labeling, p.4): Y-axis reads “count” in lowercase; PRD style often capitalizes axis labels. Required fix: change to “Count” and “Redshift z”.

- P5-m9 (Table XI range formatting, p.20): Use en dashes and consistent spacing for ranges, e.g., “1–2”, “3–5”, “6+”. Some ranges appear with mixed typography. Required fix: unify.

- P5-m10 (Appendix C data availability, p.31): Text promises a DOI-minted archival snapshot but does not list the DOI. Required fix: insert the DOI or Zenodo record number in the final.

- P5-m11 (Figure references, multiple pages): Ensure all “Fig.” vs “FIG.” usage matches PRD style consistently in text and captions.

- P5-m12 (Hyphen artifacts from PDF extraction, multiple pages): Hyphenation artifacts (e.g., “Re￾lease,” “spectro”) in the provided render may indicate copy/paste layer issues; while likely harmless in print, ensure the final PDF text layer is clean to support accessibility and search. Required fix: reflow to remove soft hyphen artifacts in the text layer.

NIT

- P5-n1 (Consistent capitalization in headings, e.g., §VIII): Prefer sentence case or consistent Title Case per PRD style; current subsection titles mix capitalization styles.

- P5-n2 (Overuse of em-dashes and nested parentheses): Several sentences stack em-dashes and parentheses; consider light edits to reduce visual clutter.

- P5-n3 (“pp” vs “percentage points”): Define “pp” once in the abstract and then use the abbreviation consistently; a few places spell out the phrase again.

- P5-n4 (Color palette): Consider colorblind-safe palettes for heatmaps and maps (e.g., Viridis); the blue–red diverging map is acceptable but could be improved.

- P5-n5 (Small in-figure text): Counts printed over bars in Fig. 3 appear small; consider slightly larger font.

Length assessment

- The manuscript is long (32 pages) for a presentation of a null result with multiple robustness checks. From a packaging standpoint, it would benefit from trimming path-level details from the main text and captions and consolidating them in Appendix C. Recommended maximum main-text length after trimming: ~24–26 pages (excluding appendices), with unchanged scientific content.

Summary recommendation

MAJOR REVISIONS

Justification: There are several essential and major presentation issues that must be corrected for publication quality: the superscript formatting of grid sizes (256^3 etc.), the mislabelled colorbar in Figure 8 (top panel), inconsistent unit notation (Mpc/h vs h−1 Mpc), intrusive build/path artifacts in the main text, and footnote placement/formatting problems. Addressing these, along with the recommended figure/table adjustments, will bring the manuscript into conformance with PRD visual and packaging standards. The science is not evaluated in this D-round.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (Round D1: Design/Presentation QA — new items only)

Arithmetic and consistency checks uncovered several new issues that were not noted in my initial pass. I list only new items below, using the same tagging convention.

ESSENTIAL

- P5-E5 (Density-covariate label/scale mismatch, Table V and §IV.A.12/§VI.D): Table V states “ρ̄ is the quartile mean of log10(1 + δsmooth),” but the reported values (e.g., ρ̄ = 1.55, 1.80, 2.01, 2.21 for cluster quartiles; 0.90–1.86 for filament quartiles) are incompatible with a base-10 log of (1 + δ). Those numbers are consistent with linear 1 + δ (dimensionless density contrast) rather than log10(1 + δ). The surrounding text in §VI.D uses the numeric values to argue boundary overlap (e.g., 1.55 vs 1.86), which likewise implies a linear scale. Required fix: correct the descriptor in Table V and in §IV.A.12 to match the actual stored/used variable (either report linear 1 + δ and keep the numbers, or keep the log10 definition and adjust the reported values accordingly). Also ensure any figure axes and later references use the same scale consistently.

MAJOR

- P5-M10 (Mis-typed one-sided Clopper–Pearson expression, §VIII.A): The text shows “1 − 0.051/6 = 39%” for the 0-of-6 upper bound. This looks like a typesetting artifact for 1 − 0.05^(1/6). Please re-typeset the exponent explicitly. Also consider printing the numeric value (≈39.3%) once to avoid ambiguity.

- P5-M11 (Interval nomenclature, multiple figures vs. §V): The paper states use of “Jeffreys 95% binomial credible intervals,” but several captions refer to “95% binomial confidence intervals.” This credible vs. confidence wording is easy to confuse for readers. Required fix: standardize captions and text to “Jeffreys 95% binomial intervals” (or explicitly “Jeffreys Bayesian credible intervals”) throughout.

- P5-M12 (Class terminology consistency, §IX.C and elsewhere): The paper’s own taxonomy is {void, wall, filament, cluster}, while external comparisons use {void, sheet, filament, knot}. Although §IX.C notes sheet ≡ wall and knot ≡ cluster, there are other places where the terms appear without the mapping. Required fix: add an early, single explicit mapping table (e.g., in §IV.A) and refer back to it where needed, to avoid reader confusion.

MINOR

- P5-m13 (Figure 5, caption vs. statistic label): The caption references “Bonferroni-5 thresholds at α = 0.01,” and the right-hand panel plots σ deviations. For absolute clarity, please annotate the panel with (a)/(b) labels (already requested in P5-M5) and explicitly note that the dotted threshold corresponds to |σ|Bonf,0.01,5 ≈ 3.09 derived from Eq. (2), to connect caption, axis, and equation.

- P5-m14 (Table VII caption clarity on σpred basis): Table VII lists max |σobs − σpred| per cell, where σpred is based on Eq. (1) using the Paper IV monopole (∆fCW = −0.0026). Elsewhere (Table XII) residuals are vs. the matched-sample monopole fP5. To prevent reader confusion, please add a short parenthetical in the Table VII caption: “σpred uses the Paper IV catalog-wide monopole (Eq. (1)), not the matched-sample fP5.”

- P5-m15 (Figure 8 bottom, colorbar range vs. stated data range): The caption states the per-pixel σ range is −3.45 to +3.48, but the colorbar appears to extend beyond ±3.5. To improve quantitative readability, set the colorbar limits to tightly bracket the actual data range (or state the deliberate padding).

- P5-m16 (Numeric precision, §V small-factor statement): The text states “4 p0(1 − p0) = 0.99998 at p0 = 0.4972.” The exact value is ≈0.99997. It’s a negligible difference but may as well be printed with consistent rounding (e.g., 0.99997).

- P5-m17 (Figure/table cross-linking on NSIDE counts): The Fig. 6 caption reports NSIDE = 32, npix = 3,303; Table VI reports the same. In §VIII.F the bottom panel reports 1,496 valid pixels (z ≤ 0.24 subset) and n_both_pix = 727. This is all consistent but scattered. Consider a brief parenthetical in §VIII.F explicitly tying the figure’s 1,496 to the Table VI framework to aid readers.

ARITHMETIC SPOT-CHECKS (no change requested; listed here for transparency)

- Table III σfrom half recompute matches all four rows to two decimals.
- Table VIII void/non-void σfrom half, ∆fCW, SE(∆), z, and 95% CI all recompute exactly.
- Table X three-algorithm DESIVAST contrasts: SE(∆) values recompute from class sizes; z and CIs match.
- Table IV density-quintile σobs and σpred values recompute; residuals within rounding.
- Table XII σvs monopole recompute within rounding (±0.03 in σ).
- Table XI χ bin labels and σ values are internally consistent with the footprint caveat in §VIII.E.

If the authors address the new Essential/Major items above (particularly the density-covariate scale/label mismatch and the mis-typed Clopper–Pearson expression), the presentation will be considerably clearer and internally consistent.