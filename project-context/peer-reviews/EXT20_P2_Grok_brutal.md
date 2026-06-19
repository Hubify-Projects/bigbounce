# P2 EXT20 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 107.2s

---

**Referee Report: P2 (EXT20)**

**Paper:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook  
**Author:** Houston Golden  
**Journal:** Physical Review D

I have examined the full rendered manuscript, every equation, table, figure, caption, and the abstract. The following findings are listed without softening.

**ESSENTIAL findings (must be fixed or paper cannot be accepted)**

- **P2-E1 (Title page, p. 1)**: The manuscript contains pervasive internal-review and bookkeeping language that has no place in a PRD submission. Examples include repeated use of “headline 5.2–5.5σ”, “abstract headline”, “r → 1 bookkeeping endpoint”, “template-mismatch bookkeeping”, “bookkeeping endpoint”, and “the abstract headline reads BF ≈ 9–14”. These phrases appear in the abstract, introduction, and multiple sections. Required fix: complete excision of all such meta-language; the paper must read as a finished scientific document.
- **P2-E2 (Title page, p. 1)**: The submission carries the date “Dated: June 14, 2026”. A manuscript cannot be dated in the future. Required fix: remove or correct the date.
- **P2-E3 (Abstract, p. 1; cross-checked against §§III B, IV, VI, VII)**: Multiple headline numbers in the abstract (5.2–5.5σ, 2.6–5σ, BF ≈ 9, r = 0.84 ± 0.02, etc.) are presented without the explicit qualification that they are template-mismatch-corrected recast values, not independent Fisher forecasts. The abstract therefore overstates what the paper actually computes. Required fix: rewrite every abstract claim to match the body’s final calibrated language exactly, including all caveats.
- **P2-E4 (Throughout, e.g. pp. 4–5, 12–14)**: The paper repeatedly juxtaposes σ values obtained under different null-space weightings and different systematic budgets without the mandatory statement that they are “not directly comparable.” This violates the requirement that every side-by-side numerical comparison carry an explicit non-comparability qualifier.
- **P2-E5 (p. 1 and §II)**: The author’s own email is given as the placeholder “*houston@hubify.com”. Required fix: replace with a real institutional address.

**MAJOR findings**

- **P2-M1 (Entire manuscript)**: The paper is a sensitivity recast, not an independent forecast, yet is written at 29 pages. The claimed contribution does not justify this length. Recommended maximum: 12–14 pages after removal of internal language and consolidation of repeated robustness checks.
- **P2-M2 (§§VI–VII, Tables II–IV)**: All Bayes-factor and σ values rest on a single adopted prior width σ_theory = 1.0 whose justification is only “recommended.” The sensitivity of the quoted BF ≈ 9–14 range to this choice is shown only in a supplementary grid; the main text does not propagate the prior-width uncertainty into the headline numbers.
- **P2-M3 (Fig. 2, Table IV, §VII)**: The consolidated systematic budget adds GR marginalization, b_φ uncertainty, and photo-z degradation in quadrature after the template-overlap correction has already been applied. No justification is given for treating these contributions as independent of the shape-mismatch factor r.
- **P2-M4 (§III B and Appendix A)**: The factor-of-two discrepancy between Cai et al. and Li et al. is resolved by an operator-algebra argument, but the paper never shows the explicit four cubic integrals evaluated with both orderings on the same numerical grid. The claim that the physical value is unambiguously −35/8 therefore rests on an un-displayed calculation.

**MINOR findings**

- **P2-m1 (p. 2)**: The Wilson-Ewing dust contraction parameter is stated as w = −0.003 without a reference to the specific model implementation used for the mode functions.
- **P2-m2 (Figs. 4–5)**: Axis labels use mixed units (h Mpc^{-1} vs. Mpc^{-1}); the reader must infer the conversion.
- **P2-m3 (Table I)**: The folded configuration is evaluated at the degenerate boundary k_1 = 2k, k_2 = k_3 = k, but the caption does not state that this is a limiting case of the sequence k_1 = 2k, k_2 = k_3 = k.

**NIT findings**

- **P2-n1**: Several sentences begin with “We stress that…” or “We note that…”; these are editorial and can be removed.
- **P2-n2**: The phrase “robustness to the single- vs full-ordering Li/Cai factor of two” appears in a section heading; it is meta-commentary.

**Summary recommendation**

**MAJOR REVISIONS**

The manuscript contains multiple instances of internal-review language that must be removed before the paper can be considered a finished PRD submission. In addition, the abstract overstates the nature of the calculation (recast vs. independent forecast), the length is excessive for the actual contribution, and several headline numerical claims rest on un-displayed or insufficiently justified choices. Once the internal language is excised, the abstract is rewritten to match the body’s calibrated statements, and the length is reduced to ~12–14 pages, the technical content may be publishable as a concise sensitivity study. Until those changes are made, the paper does not meet PRD standards.