# R53 P5 — Truth Audit (verdict-first vs source)

**Paper:** P5 "Environmental Dependence of Spiral Chirality" (DESI chirality)
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.83, 3804 lines)
**Compiled PDF:** `/tmp/R53_P5/p5_desi_chirality.pdf` md5=e294df9b, 33 pp, 0 undef refs, 0 overfull \hbox >50pt
**Legs returned:** Grok_brutal (grok-4.3), Gemini_cosmology (gemini-2.5-pro), OpenAI_methodology (gpt-5, reasoning=high + pass-2). **Failed:** Perplexity_citations (401 quota). **Claude/Opus leg:** this audit (full read + independent arithmetic recompute).
**Auditor patterns:** 061 (verdict-first), 062 (primary/secondary inversion), 063 (already-self-stated caveat), 064 (text-extraction artifact misread) + calibration.

## Independent arithmetic recompute (Claude/Opus leg) — ALL PASS
- Contingency CW/CCW×class: χ²=3.55, 3 dof, p=0.315 ✓ (cells in App. Table XVI)
- Contingency class×program: χ²=4932.5≈4933, V=0.0780, **log10 p = −1069.33** (mpmath, dps=50) ✓ matches "≈−1069"
- Table III σ_from_half: void −0.68, wall +0.55, filament −2.61, cluster −4.66 ✓
- DESIVAST primary contrast: Δf=+0.00068, SE=0.00219, z=+0.31, p=0.76 ✓
- Three-algorithm table: max |z_Δ|=1.12 (V2-REVOLVER) ✓ matches "|z_Δ|≤1.12"
- bright/dark program splits (Table IX): all four σ recompute exactly ✓
- √(4p₀(1−p₀)) at p₀=0.4972 = 0.999984 → 0.99998 ✓ (paper correct)
- OpenAI pass-2 self-critique independently confirms: "Tables III–V, VII–XI, XIII–XV … all recompute within rounding."

## Verdict table

| ID | Finding | Verdict | Source evidence |
|----|---------|---------|-----------------|
| Grok REJECT | overall reject | **CALIBRATION-OVERHARSH** | Driven by length + Paper IV + primary/secondary inversion; no genuine arithmetic/logic defect. Same inversion false positive as prior Grok REJECT (R52). |
| Grok P5-E1 | "abstract does not qualify void n=428" | **FALSIFIED** | Abstract L516–523 explicitly: "full T-Web secondary void bin is sample-size limited at n=428 … controlling void constraint comes from DESIVAST re-projection (n=56,981)". |
| Grok P5-E2 | "null guaranteed by counting floor, no constraining power" | **FALSIFIED (pattern-062)** | Headline is the DESIVAST primary n=56,981 (§V.B, §VIII); T-Web void n=428 is explicitly demoted to secondary. Inversion of declared primary path. |
| Grok P5-E3 | monopole spatial uniformity unquantified | **OPINION** | Paper tests via HEALPix per-pixel scans + quality-quartile-flat; Δf contrast is monopole-invariant by construction (§III). |
| Grok P5-E4 | "n=6 check has zero power, presented as support" | **FALSIFIED (pattern-063)** | Abstract L546–547 already states "n=6 sample is too small for a formal purity constraint, but it illustrates the survey-shell systematic." Self-stated. |
| Grok M1 / Gemini M1 | 33 pp too long | **OPINION (editorial)** | Catalog/methodology paper; size not a defect. No false claim. |
| Gemini E1 / OpenAI E5 / Grok M2 | reliance on unpublished Paper IV | **STALE (already-reframed)** | Self-containedness reframe applied R52/EXT21: §"Relation to Paper IV" describes catalog generation (equivariant ViT-S, Z₂ TTA, public HF `class_eq`), paper independently measures own monopole f_P5=0.49719, headline Δf is monopole-invariant. Companion-paper public-release timing is submission-gated, not a text defect. |
| OpenAI E1 | post-hoc primary path | **OPINION (already-disclosed)** | §V.B "Primary vs secondary analysis paths" explicitly declares post-hoc choice, garden-of-forking-paths caveat, Bonferroni-5 family + analysis-tree Table IV. The transparency the reviewer requests is already present. |
| OpenAI E2 | mixed Paper IV (−0.0026) vs internal P5 (−0.00281) monopole | **OPINION/minor (disclosed)** | §"Relation to Paper IV" reconciles both ("consistent with the independent Paper IV estimate"); difference 0.0002 is negligible; Δf contrast monopole-invariant. No double-count error. |
| OpenAI E3 | reproducibility DOI missing | **SUBMISSION-GATED — SKIP** | §VII states DOI snapshot "accompanies journal submission" (minted at submission). Out of scope per round directive. |
| OpenAI E4 | "broken footnote insertion ('a on')" | **FALSE POSITIVE (pattern-064)** | revtex lettered abstract-footnote superscript `^a` after Cautun citation (L431 `\footnote{…}`); footnote renders correctly at p.1 bottom. pdftotext/Files-API flatten the superscript to inline "a". Not broken. NOT FIXED. |
| OpenAI m11 | "√(4p₀(1−p₀))=0.99998 should be 0.99997" | **FALSE POSITIVE (pattern-064)** | Reviewer dropped the square root. √(4·0.4972·0.5028)=√0.99996864=0.999984→0.99998. Paper correct. NOT FIXED. |
| Gemini T1 | "Dated June 18 2026 — typo year, correct it" | **FALSE POSITIVE** | 2026 is the current submission year (today 2026-06-26). Year is correct. (Cosmetic \date vs \paperVersion 1-day gap is out-of-scope: no bump this round.) |
| OpenAI M1 | selection-corrected T-Web should be displayed baseline | **OPINION** | §IX.A provides selection-corrected rebuild (χ²=0.11, p=0.99); abstract/conclusions already cite it. Framing preference. |
| OpenAI M2 / Gemini M2 / various NITs | add abstract SE/z, sharpen bright/dark text, parentheticals | **OPINION (gold-plating)** | bright/dark ~2σ already discussed §VI.D + flagged for DR2 follow-up; DESIVAST SE/z already in Table VIII. Clarifications, not defects. |

## NET VERDICT
**ACCEPT — polish-tier convergence confirmed at R53.** Zero BLOCKER, zero genuine MAJOR, zero new verified DO-NOW defects. Every ESSENTIAL/MAJOR across 3 returned legs resolves to: (a) the known, already-reframed Paper IV self-containedness preference (companion-paper public-release is a submission-timing prerequisite, not a P5 text defect), (b) submission-gated DOI (skip), or (c) falsified/false-positive (Grok primary/secondary inversions ×4 = same false positive as prior rounds; OpenAI "a on" footnote + m11 sqrt = text-extraction misreads; Gemini date-year = current year). OpenAI's own pass-2 + my independent recompute confirm full arithmetic/notational self-consistency.

**CLOSED THIS ROUND:** none (no verified DO-NOW item; no false-positive "fixed").
**Overflow audit:** 0 Overfull \hbox >50pt; deferred table* floats (Tables IV/VII/VIII/XII/XVI/XVIII) place cleanly (verified Table XVIII p.32 render, no column escape); \mbox{-} subscripts in `non\mbox{-}void` render as hyphen (pdftotext extracts "non-void", not "non−void"). No edits → recompile unchanged (the clean ×3 compile stands).
