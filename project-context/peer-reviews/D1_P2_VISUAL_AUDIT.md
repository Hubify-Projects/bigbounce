# D1 P2 — VISUAL / CAMERA-READY AUDIT (design lead)

**Paper**: P2 "Testing the Matter Bounce with Primordial Non-Gaussianity" v1.7.70 (29 pp)
**PDF audited**: `research/focused_paper_source_integration/02_full_draft.pdf` (all 29 pp read as images)
**Source**: `research/focused_paper_source_integration/02_full_draft.tex`
**Scope**: visual/packaging ONLY (layout, floats, overflow, figure sufficiency). No science.

---

## Inventory (from .tex grep)

- **Figures (6, all single-column `\columnwidth`)**: Fig1 shape function (p5, L643), Fig2 survey-significance bars (p11, L736), Fig3 fNL landscape (p11, L761), Fig4 σ vs k_min two-panel (p16, L885), bphi_sensitivity (Fig5, two-panel, p17, L896), Fig6 decision thresholds (p22, L1019).
- **Tables (6)**: Table I single-col `table` (p5, L650); Tables II/III/IV/V full-width `table*` (L827, L850, L909, L949); plus `table*[!htbp]` at L1151.
- **Compile log**: only **2 overfull hboxes** (2.95pt Table I L652–661; trivial). Large cluster of `badness 10000` **underfull** hboxes at L955–961 = Table IV narrow `p{}` columns forcing ragged wraps.

---

## Truth-audit of vendor D1 visual findings

| Vendor finding | Verdict | Note |
|---|---|---|
| Gemini N1: Table IV caption `x` → `\times` | **STALE** | Committed caption L969 already uses `$|\fnl| \times r/\sigma_{\rm eff}$`. No literal `x`. Drop. |
| Grok E1: future "(Dated: June 18, 2026)" on title page | **VERIFIED (non-visual / production)** | Real placeholder-date artifact, but a metadata/date item, not a layout defect. Flag to science/packaging lead, not D-round. |
| Grok N2: orphaned internal heading "Robustness to the single- vs full-ordering…" p2 | **VERIFIED (prose)** | Reads as a stray heading in body. Borderline visual; italic run-in. Minor. |
| All other Gemini/Grok/OpenAI items | **OUT-OF-SCOPE (science/prose)** | Abstract–body consistency, systematic-combination method, etc. Not visual packaging. |

---

## Visual findings (PAGE NUMBERS, prioritized)

| SEV | Page / loc | Issue | Concrete LaTeX fix |
|---|---|---|---|
| MAJOR | p20, Table IV (`tab:systematics`, L949–971) | Over-dense: `p{3.4cm}` "Value/range" + `p{2.5cm}` σ column force heavy ragged wrapping; row 1's σ cell wraps a long parenthetical ("…not directly comparable to the template-corrected…distinct null procedures") over ~6 lines. Confirmed by badness-10000 underfull hboxes L955–961. Looks broken. | Move row-1's long parenthetical OUT of the cell into the caption (caption already long but is the right home for the "naive uncorrected not comparable" caveat). Rebalance column widths e.g. `p{3.2cm}p{3.0cm}p{1.6cm}p{2.6cm}p{2.2cm}`; or use `\small`/`\footnotesize` on the tabular and `\raggedright` the wide text columns to kill the badness. Keep the row, trim the cell. |
| MAJOR | p16 Fig4 (L885) + p17 Fig5 (L896) | Two-panel side-by-side plots crammed into `\columnwidth`; axis labels, tick numbers, and legends render small/tight at column width — legibility risk for a forecast paper whose core deliverable is sensitivity curves. | Promote both to **full-width** `figure*` with `\includegraphics[width=\textwidth]{...}` (panels then get ~2× linear size). Fig4 (σ vs k_min, both surveys) and Fig5 (σ(fNL) vs b_phi prior + significance) are the paper's two key sensitivity figures — they deserve the full text width. |
| MINOR | p15 (Table II) & p18 (Table III) | `table*[h]` floats land at top of otherwise near-empty pages → large orphaned white-space below (p18 is Table III essentially alone on the page). Awkward float placement. | Change `[h]` → `[t]` or `[!t]` (or `[tp]`) on `table*` at L827 (II) and L909 (III) so they pack with text and stop pushing a half-page of whitespace. `table*[h]` is the usual cause of this. Apply same to L850, L949 for consistency. |
| MINOR | p2, L… "Robustness to the single- vs full-ordering Li/Cai factor of two." | Stray italic run-in reads as an orphaned section heading left in body text (Grok N2). | Either demote to a real `\paragraph{}`/`\textit{…}.` lead-in merged with the following sentence, or delete the standalone fragment so it doesn't look like a leftover header. |
| NIT | §VI.C Bayesian, p12–15 | Reviewer-flagged over-qualified prose reads as a dense wall (many nested parentheticals + worked-example bullet lists). Visually heavy but not a layout break; the four-corner grid IS already extracted to Table II. | No hard layout fix required. Optional: the "worked example: reproducing the abstract BF≈9" three-step block (p14) could be set as a `description`/numbered list or a small boxed callout to break the wall — presentation polish only. |

---

## Figure-ADD opportunities (marked)

- **ADD candidate — none strictly required.** The paper is already figure-rich for a forecast (sensitivity curves Fig2/Fig4/Fig5 present; fNL landscape Fig3; decision thresholds Fig6; shape function Fig1). Reviewers' "needs sensitivity / b_phi vs σ / contrast figures" boxes are all **already satisfied** (Fig5 IS the b_phi-vs-σ plot; Fig4 IS σ vs k_min). No missing-figure gap.
- **Optional polish ADD**: a single small **contrast-ratio / Bayes-factor-vs-prior-width** schematic could replace some of the §VI.C prose wall, but this is optional and overlaps Table II. Not required for camera-ready.

---

## Bottom line

**Not camera-ready-clean — 2 MAJOR + 3 lower visual items.** Headline visual fixes:
1. Table IV (p20) over-dense column wrapping — move row-1 caveat to caption + rebalance widths.
2. Promote Fig4 (p16) and Fig5 (p17) two-panel sensitivity plots to full-width `figure*`.
3. Float-placement whitespace on Table II/III pages — `[h]`→`[t]`.

No figure is missing; reviewers' figure-sufficiency boxes are already met. Gemini's `\times` nit is stale. The future-date is real but belongs to the science/packaging lead, not D-round.
