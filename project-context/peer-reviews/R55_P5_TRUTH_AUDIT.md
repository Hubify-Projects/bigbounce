# R55 P5 — Truth Audit (verdict-first vs source) — CONVERGENCE CONFIRMATION

**Paper:** P5 "Environmental Dependence of Spiral Chirality" (DESI chirality)
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.83-2026-06-19, 3805 lines)
**Compiled PDF:** `/tmp/R55_P5/p5_desi_chirality.pdf` 33 pp, 0 undef refs/citations (only a harmless `OMS/cmtt/m/n` font-shape warning), 0 overfull \hbox (×3 pdflatex; 14 `\bibitem`, no bibtex).
**Legs returned:** Gemini_cosmology (gemini-2.5-pro), Grok_brutal (grok-4), OpenAI_methodology (gpt-5, reasoning=high). **Failed:** Perplexity_citations (401 insufficient_quota — same as R54). **Claude/Opus leg:** this audit (full read + independent recompute).
**Patterns:** 061 (verdict-first), 062 (primary/secondary inversion), 063 (already-self-stated caveat), 064 (text-extraction artifact) + calibration.
**Context:** Convergence-confirmation after R52 (2 MAJOR closed: V1 Paper IV reframe, V2 Table V log10) → R53 (0 new) → EXT21/22 (0 new) → R54 (0 new). Strongly expect ZERO new items.

## R52 closures — VERIFIED IN-TREE (not re-opened)
- **V1 Paper IV reframe:** internal matched-sample monopole `f_CW^P5 = 0.49719` leads (L456, L686-688, L982); §"Relation to Paper IV" (L671) demotes Paper IV to "consistent with the independent Paper IV estimate" corroboration; Δf_CW contrast stated invariant under any catalog-wide monopole shift (L462, L695). ✓
- **V2 Table V density metric:** caption (L1455-1467) explicitly resolves log10-vs-linear — displayed 0.90–2.21 ARE `log10(1+δ_smooth)`; "Q4 ρ̄=2.21 → 1+δ≈162×"; quartile membership invariant under monotone transform; verified by exact recompute [A5]. ✓

## Verdict table (R55 legs)
| ID | Finding | Verdict | Source evidence |
|----|---------|---------|-----------------|
| Grok REJECT (overall) | central claim on n=428 void bin | **CALIBRATION-OVERHARSH (pattern-062)** | headline = DESIVAST primary n=56,981, Δf=+0.0007 (L426, L444, L3426-3431, Table X); n=428 is T-Web SECONDARY, explicitly demoted (abstract L517-523). 4th consecutive Grok inversion (R52/R53/R54). |
| Grok E1/E2/E3 | n=428 underpowered / χ²=3.55 effect-size / not informative | **FALSIFIED (pattern-062/063)** | same inversion; σ-comparability + range-in-pp effect size already in abstract L481-483 + Table III/V/VI captions; 6th raise. Test is null (p=0.31) regardless. |
| Grok E4 | n=6 DESIVAST overlap too small | **FALSIFIED (pattern-063)** | already disclosed verbatim "six-object illustrative check … too small for a formal purity constraint" (L543-547); not the primary (n=56,981 is). |
| Grok M1/M2/M3 | Phase-2 reconfirms floor / Fig 3 power annotation / σ-comparability | **OPINION + FALSIFIED** | M3 comparability stated verbatim L481-483 (6th raise); M1/M2 editorial. |
| Grok N3 | "the the" duplication p.2 | **FALSE POSITIVE (pattern-064)** | grep `\bthe the\b` (and all doubled words) over source = ZERO hits. Text-extraction artifact. NOT FIXED. |
| Gemini MAJOR-REV (overall) | sign errors + Paper IV unpublished | **CALIBRATION + STALE** | see below; no arithmetic/logic defect. |
| Gemini M1 | V2-REVOLVER Δ=−0.0037 is a "sign error" (should be +0.0037) | **FALSIFIED (pattern-062/064)** | paper DEFINES Δf_CW ≡ f_nonvoid − f_void (L2359-2361); f_nonvoid=0.4955, f_void=0.4992 → Δ=−0.0037 CORRECT. Paper even warns "artifact stores opposite-signed f_void − f_nonvoid" (L2414-2415). Gemini used the opposite convention. |
| Gemini M2 / N1 / T1 | jargon/length / effect-size for χ²=3.55 / date "2026"→"2024" | **OPINION / FALSE POSITIVE** | length=editorial; χ²=3.55 is NULL (Cramér's V already given for the significant χ²=4933 test); date 2026 is correct (vendor-cutoff artifact). |
| Gemini N2 | design-effect "≤1.9%" should be "1.8%" | **FALSE POSITIVE** | √(812793/783820)=1.0183 → 1.83% ≤ 1.9% is TRUE; "≤1.9%" upper-bound phrasing is factually correct. Precision preference only. |
| OpenAI MINOR-REV (overall) | DOI + tabulate χ²=0.11 counts | **gentlest verdict; 0 DO-NOW** | OpenAI's own arithmetic audit confirms EVERY abstract scalar traceable, all σ/χ²/Δf/Cramér's V recompute within rounding, "No over-claim detected." |
| OpenAI E2 | DOI missing | **SUBMISSION-GATED — SKIP** | DOI minted at journal submission per round directive. |
| OpenAI E1 | per-class n/nCW for z-shell χ²=0.11 not in PDF | **OPINION (gold-plating)** | supporting (not headline) result; four n totals already parenthetical; artifact-cited [A...]; OpenAI itself: "artifact pointer acceptable / move to Supplemental." |
| OpenAI M1 | Bonferroni |σ| threshold 4.05 vs ~4.01-4.03 | **OPINION (convention-dependent; no verdict flips)** | my recompute z_{1-0.05/2108}≈4.07 (ABOVE printed 4.05); 2.77 & 2.58 exact. All HEALPix max-|σ| are null (p=0.607/0.135/0.413) — far below 4.0; no comparison flips at any value. |
| OpenAI M2/M3/M4 | dedup-TARGETID shuffle / ASTRA variance wording / 33pp length | **OPINION (gold-plating + editorial)** | artifact pointer acceptable; ASTRA σ already MC-validated; length = same editorial as Grok/Gemini. |
| OpenAI m3 | "dangling 'a' before 'on'" in abstract | **FALSE POSITIVE (pattern-064)** | source L430-440: `\cite{Cautun2014})` then `\footnote{…} on the full`. Abstract footnote letter-marker "a" extracts inline. Same as R53 adjudication. NOT FIXED. |
| OpenAI m1/m2/m4/m5/m6/nits | units, version-history phrasing, σ rounding, sign-convention clarity, p_global, fig labels | **OPINION (polish)** | none falsify a claim; σ "within rounding from exact counts" per OpenAI's own audit. |

## Independent recompute (Claude/Opus leg) — ALL PASS
- Appendix B Table CW/CCW×class: cells sum to per-class n; f_CW ratios → printed 4-dec; row marginals CW=404,111 / CCW=408,682; total 812,793 ✓
- Appendix B Table class×program: cells sum to per-class n; f_bright → printed; total n=811,609; Cramér's V=√(4933/811609)=0.078 ✓
- V2-REVOLVER catalog-native Δ = 0.4955 − 0.4992 = −0.0037 under stated convention (Gemini M1 falsified) ✓
- Bonferroni: z_{1-0.05/18}=2.773→2.77 ✓; z_{1-0.05/10}=2.576→2.58 ✓; NSIDE=16 ~4.05-4.07 (no comparison flips) ✓
- Conclusions per-class {0.484,0.503,0.498,0.496} + range 1.98pp match abstract ✓
- `\mbox{-}` (13 sites: `non\mbox{-}void`, `T\mbox{-}Web`) all correct math-mode hyphens; render "non-void"/"T-Web"; pdftotext extracts hyphen cleanly. Extraction-artifact watch CLEAN.
- 0 residual `_{V-Web}` / `_{\rm V` in math context (changelog comments only).

## NET VERDICT
**ACCEPT — CONVERGED at R55.** Zero BLOCKER, zero genuine MAJOR, **ZERO new verified DO-NOW defects.** All ESSENTIAL/MAJOR across the 3 returned legs resolve to: (a) submission-gated DOI/arXiv (skip), (b) repeat FALSIFIED items (Grok primary/secondary inversion ×4; Gemini sign-convention misread; σ-comparability 6th raise; effect-size already present), (c) text-extraction artifacts (Grok "the the", OpenAI/Gemini abstract footnote "a on" — both pattern-064, NOT in source), or (d) gold-plating/editorial opinion (tabulate supporting z-shell counts, 33pp length, units harmonization). OpenAI's own full arithmetic audit independently confirms "No over-claim detected; every abstract scalar traceable." R52 V1/V2 closures verified in-tree, not re-opened.

**CLOSED THIS ROUND:** NONE (no verified DO-NOW; no false-positive "fixed").
**Overflow audit:** 0 overfull \hbox; deferred table*/figure* floats place cleanly across 33 pp (visual render pp.1,2,10,18,28 — no column escape); `\mbox{-}` subscripts render as hyphens. No edits → clean ×3 compile stands.

**CONVERGENCE STATEMENT:** P5 has now returned R52(closed 2)→R53(0 new)→EXT21/22(0 new)→R54(0 new)→**R55(0 new)**. **Four consecutive zero-new-verified rounds.** P5 is CONVERGED; the residual 1% is Houston sign-off (gated on P4 arXiv ID + DOI mint at submission), not any text defect.
