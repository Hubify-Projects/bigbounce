# R54 P5 — Truth Audit (verdict-first vs source) — CONVERGENCE TEST

**Paper:** P5 "Environmental Dependence of Spiral Chirality" (DESI chirality)
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.83, 3804 lines)
**Compiled PDF:** `/tmp/R54_P5/p5_desi_chirality.pdf` md5=b01bfece, 33 pp, 0 undef refs, 0 overfull \hbox (×3 pdflatex)
**Legs returned:** Gemini_cosmology (gemini-2.5-pro, +pass-2), Grok_brutal (grok-4.3, +pass-2), OpenAI_methodology (gpt-5, reasoning=high, +pass-2). **Failed:** Perplexity_citations (401 insufficient_quota). **Claude/Opus leg:** this audit (full read + independent recompute).
**Patterns:** 061 (verdict-first), 062 (primary/secondary inversion), 063 (already-self-stated caveat), 064 (text-extraction artifact) + calibration.
**Context:** Convergence test after R52 (2 MAJOR closed: V1 Paper IV reframe, V2 Table V log10 metric) + R53 (0 new) + EXT21/22 (0 new). Expected ZERO new items.

## R52/R53 closures — VERIFIED IN-TREE (not re-opened)
- **V1 Paper IV reframe:** internal matched-sample monopole $f_{\rm CW}^{\rm P5}=0.49719$ now leads (L455, L687, L982); §"Relation to Paper IV" (L671) demotes Paper IV to "consistent with the independent Paper IV estimate" corroboration. ✓
- **V2 Table V density metric:** caption (L1459-1467) now explicitly resolves log10-vs-linear — displayed 0.90–2.21 ARE $\log_{10}(1+\delta_{\rm smooth})$ values (Q4=2.21 → $1+\delta\approx162\times$), quartile membership invariant under monotone transform, verified by exact recompute [A5]. ✓

## Verdict table (R54 legs)
| ID | Finding | Verdict | Source evidence |
|----|---------|---------|-----------------|
| Grok REJECT→MAJOR-REV | overall | **CALIBRATION-OVERHARSH** | driven by primary/secondary inversion + length; no arithmetic/logic defect |
| Grok E1 | abstract drift vs n=428 void | **FALSIFIED (pattern-062)** | headline = DESIVAST primary n=56,981 (L444, Table X L2283); n=428 is T-Web secondary, explicitly demoted in abstract |
| Grok E2 / N2 | σ-comparability not at every juxtaposition | **FALSIFIED (pattern-063)** | qualifier in Tables III/V/VI/IX/XIII captions + §V (L995); 5th raise of same item |
| Grok E3 | n=428 null not competitive | **FALSIFIED (pattern-062)** | same inversion; primary is 56,981 |
| Grok M1 / Gemini M1 / OpenAI len | 33 pp too long | **OPINION (editorial)** | catalog/methodology paper; not a defect |
| Grok M2 | Paper IV unreproduced numbers | **STALE (already-reframed + submission-gated)** | internal monopole now load-bearing; arXiv ID minted at submission |
| Grok M3 | no effect-sizes (Cramér's V) | **FALSIFIED** | Cramér's $V=0.078$ reported + contextualized (L3546) |
| Grok N1 | Fig 3 void error bars large | **OPINION (already-flagged)** | non-comparability + Jeffreys CI shown honestly |
| Gemini E1 / OpenAI E2(DOI) | Paper IV non-public / arXiv ID / DOI | **STALE / SUBMISSION-GATED — SKIP** | self-containedness reframe applied R52; arXiv ID + DOI minted at submission (per round directive) |
| Gemini M2 | Table XII filament σ +0.99 should be +1.02 | **FALSE POSITIVE (pattern-064/calibration)** | reviewer divided rounded Δf=+0.0008; paper uses unrounded Δf=0.000775 → 0.99 (=0.99×0.5/√408187). Self-consistent. NOT FIXED |
| Gemini pass-2 M3 | Appendix A toy-EFT dimensionally inconsistent | **FALSIFIED / STALE (= EXT7 GEM-B1, already-caveated)** | App. A (L3476-3525) explicitly "schematic … order-of-magnitude estimate only, not a quantitative ALP exclusion"; bound in dimensionless $H_0$ units; dual rotational+gauge-invariance caveat states literal form "is a coordinate-aligned schematic, not a covariant operator." Disclosed by construction. NOT FIXED |
| Gemini N1 | Δf sign convention in body | **OPINION** | defined Table X caption + L2294/L2360 body; already stated |
| OpenAI E1 | Clopper-Pearson "1−0.05^{1/6}" mis-rendered | **FALSE POSITIVE (pattern-064)** | source L2117 = `$1 - 0.05^{1/6} = 39\%$` correct braces; documented R34 artifact (.tex L191-194). NOT FIXED |
| OpenAI M1/M2 | robustness per-class n/fCW in artifacts not main text | **OPINION (gold-plating)** | fCW values already quoted in body; full per-class in [A-IDs]; PRD-acceptable. R52 V5-V8 class already MINOR-closed |
| OpenAI M3 / units / NITs | h⁻¹Mpc phrasing, clarity | **OPINION** | low-severity presentation |

## Independent recompute (Claude/Opus leg) — ALL PASS
- Table XII filament: Δf=0.000775, SE=0.5/√408187=0.0007826, σ=+0.99 ✓ (Gemini's +1.02 = rounded-input artifact)
- Clopper-Pearson: 1−0.05^(1/6)=1−0.6070=0.393→39% ✓
- Contingency class×program χ²=4933, Cramér's V=0.078, log10 p≈−1069 ✓
- DESIVAST primary Δf=+0.0007, z=+0.31, p=0.76 ✓

## NET VERDICT
**ACCEPT — CONVERGED at R54.** Zero BLOCKER, zero genuine MAJOR, **ZERO new verified DO-NOW defects.** All ESSENTIAL/MAJOR across the 3 returned legs resolve to: (a) the known already-reframed Paper IV self-containedness + submission-gated arXiv ID/DOI (not a P5 text defect), (b) repeat FALSIFIED items (Grok primary/secondary inversion ×3 = same false positive as R52/R53; σ-comparability 5th raise; effect-sizes already present), (c) text-extraction artifacts (OpenAI Clopper-Pearson, Gemini Table XII rounding — both pattern-064, NOT fixed), or (d) the toy-EFT dimensional caveat already present verbatim (EXT7 GEM-B1). R52 V1/V2 closures verified in-tree, not re-opened.

**CLOSED THIS ROUND:** NONE (no verified DO-NOW; no false-positive "fixed").
**Overflow audit:** 0 overfull \hbox; deferred table* floats place cleanly; \mbox{-} subscripts (`non\mbox{-}void`, `T\mbox{-}Web`) render as hyphens, pdftotext extracts "non-void" (extraction-artifact watch clean). No edits → clean ×3 compile stands.

**CONVERGENCE STATEMENT:** P5 has now returned R52(closed)→R53(0 new)→EXT21/22(0 new)→**R54(0 new)**. Three consecutive zero-new-verified rounds. P5 is CONVERGED; final 1% is Houston sign-off (last in queue; needs P4 arXiv ID).
