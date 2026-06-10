# P2 R25conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.47.pdf` md5=a6ea2ee9 pages=24
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 101.4s

---

**Referee Report**

**P2-E1 (ESSENTIAL)** — Abstract (p. 1) and Sec. IV (p. 8): The headline claim “template-corrected detection significance is ~5.2–5.5σ” is computed under the optimistic CMB-Fisher weighting (r = 0.876) before any GR or b_φ marginalization. The body (Sec. VII, p. 13–14 and Fig. 2) shows that once the full systematic budget is included the range collapses to 3–5σ. The abstract therefore reports a number that is not the final forecast result. Required fix: replace the 5.2–5.5σ figure in the abstract with the post-systematic range or explicitly qualify it as “pre-systematic.”

**P2-E2 (ESSENTIAL)** — Sec. II.C (p. 5) and Appendix A (p. 20): The paper adopts the Cai et al. convention (f_NL = −35/8) after an operator-algebra argument that the Li et al. value (−35/16) differs only by a missing commutator term. The explicit Wick-contraction derivation supplied in A.1 still leaves the two conventions numerically distinct by exactly a factor of two in the final bispectrum amplitude. Because the entire forecast chain (Fisher matrix, Bayes factors, detection significance) scales linearly with |f_NL|, the choice is not a harmless normalization convention; it halves every quoted σ. The paper never states this scaling in the abstract or in the main forecast sections. Required fix: propagate both conventions through the headline numbers or demonstrate that the physical observable is convention-independent.

**P2-M1 (MAJOR)** — Sec. VI and Table II (p. 11–12): All Bayes-factor results are shown only for three discrete prior widths. The text acknowledges that “wider bounce prior … reduces the Bayes factor monotonically,” yet no continuous marginalization over prior width is performed. The headline BF ~ 10–17 range is therefore prior-dependent at the level that changes the qualitative conclusion (BF > 10 vs. BF ~ 4). Required fix: either marginalize analytically over the prior hyper-parameter or demonstrate that the ranking is stable inside the physically motivated range.

**P2-M2 (MAJOR)** — Sec. III.B and Eq. (5) (p. 7): The amplitude-recovery factor r = 0.84 ± 0.02 is obtained from a 10 000-sample null-space scan that uses only the three benchmark triangles for validation. The scan itself shows a 1σ tail reaching r = 0.55. No figure shows the distribution of r across the full triangle space; only the median and inter-quartile range are quoted. The degradation from the naive 6.25σ to 5.2–5.5σ therefore rests on an incompletely characterized tail. Required fix: supply the full histogram of r or a worst-case envelope.

**P2-M3 (MAJOR)** — Length and scope (entire manuscript): The manuscript is 24 pages, contains 7 figures, 4 tables, an appendix, and an extensive systematics section. The core scientific claim is a set of Fisher forecasts and a Bayes-factor comparison under six strong assumptions. PRD articles presenting similar survey forecasts are routinely 8–12 pages. The present length is disproportionate to the incremental advance over Heinrich et al. (2024) and Doré et al. (2014). Required fix: condense to ≤ 14 pages or justify the length by adding a genuinely new methodological result.

**P2-N1 (MINOR)** — Fig. 1 caption (p. 5) and Table I (p. 5): The equilateral and folded B_NL values are listed to three decimal places while the squeezed-limit value is given to four. The underlying polynomial coefficients are quoted to only two significant figures; the extra digits are not justified. Required fix: round consistently or propagate coefficient uncertainties.

**P2-N2 (MINOR)** — Multiple instances of “we emphasize that …” and “note that …” (pp. 2, 4, 5, 6, 9, 13) create a defensive tone that is unnecessary in a PRD submission. Required fix: remove or shorten.

**P2-NIT1 (NIT)** — Several figure axes lack explicit units (e.g., Fig. 4 left panel, k_min in h Mpc^{-1} is implied but not labeled on the axis). Required fix: add units.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents an exhaustive forecast exercise whose headline numbers are sensitive to (i) an unresolved factor-of-two convention ambiguity that directly rescales every significance and Bayes factor, (ii) an incompletely characterized template-overlap distribution whose tails affect the final 3–5σ claim, and (iii) prior choices that are shown to move the Bayes factor across the conventional “strong evidence” threshold. In addition, the 24-page length far exceeds the scope of the incremental result. These issues must be resolved before the paper can be considered for Physical Review D.