# P2 R35conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.56.pdf` md5=bd702ba5 pages=27
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 185.6s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

**Report ID:** P2-R35conf-Report-1

This paper presents a detailed sensitivity forecast for testing the matter-bounce scenario using primordial non-Gaussianity measurements from the upcoming SPHEREx survey and the proposed MegaMapper. The primary prediction under investigation is the local-type non-Gaussianity parameter `f_NL = -35/8`. The authors perform a comprehensive analysis, including a recast of existing SPHEREx forecasts, a detailed treatment of the template mismatch between the bounce bispectrum and the standard local shape, a thorough assessment of systematic uncertainties, and a Bayesian model comparison against inflationary alternatives. A significant contribution of this work is the clarification of a factor-of-two discrepancy in the predicted value of `f_NL` in the existing literature.

The paper is exceptionally well-researched, methodologically sound, and transparent about its assumptions and limitations. The analysis is rigorous and the conclusions are well-supported by the calculations presented. The work represents a valuable and timely contribution to the field. The following points should be addressed before publication.

---
### ESSENTIAL Revisions

None. The paper meets the essential criteria for publication in Physical Review D.

---
### MAJOR Revisions

None. The major components of the analysis are sound and well-presented.

---
### MINOR Revisions

**P2-M1: Clarification of the `b_φ` Universality Assumption in the Headline Forecast**
*   **Section/Page:** IV, p. 9; VII B, p. 16.
*   **Problem:** The headline significance range of `~2.6-5σ` is derived from a complex budget of systematics. A key component is the degradation due to uncertainty in the PNG bias parameter `b_φ`. The text on p. 16 explains that relaxing the `b_φ` universality relation (as recommended for Stage-IV surveys) widens `σ(f_NL)` by `O(20-50%)`. The text states the headline range "already incorporates the central 20-30% degradation." However, the baseline forecast from Heinrich et al. [6] (cited as the source for `σ(f_NL)=0.7`) *assumes* this universality. It is not fully clear to the reader whether the "20-30% degradation" is an estimate applied on top of the Heinrich et al. result or if it is a re-interpretation of the uncertainty within their forecast.
*   **Fix:** Please clarify precisely how the `b_φ` degradation is incorporated. For example, state explicitly: "We adopt the Heinrich et al. [6] baseline of `σ(f_NL) = 0.7`, which assumes `b_φ` universality. Following the recommendation of Barreira [27], we model the effect of relaxing this assumption by applying a 20-30% degradation to `σ(f_NL)`, resulting in an effective `σ(f_NL)` in the range [0.84, 0.91] for the bispectrum channel. This degradation is included in our final realistic significance range of 2.6-5σ." This would make the provenance of the systematic budget more transparent.

---
### NITs (Cosmetic)

**P2-N1: Author Contact Information**
*   **Section/Page:** I, p. 2 (footnote).
*   **Problem:** The provided email address `houston@hubify.com` appears to be associated with a commercial entity rather than a standard academic or research institution. While not a scientific error, it is unconventional for a publication in this journal.
*   **Fix:** The author may wish to consider providing an alternative, more conventional contact email (e.g., via a service like ORCID or a personal academic domain) if available. This is a suggestion, not a requirement.

**P2-N2: Table/Figure Floating**
*   **Section/Page:** VI, p. 14 and Appendix A.2, p. 25.
*   **Problem:** The text on page 14 refers to Table II, but the full table appears on page 15. Similarly, the text on page 25 refers to Table IV, which appears on page 26. This is a common consequence of LaTeX's float handling.
*   **Fix:** If possible, adjust the placement of the tables to appear closer to their first mention in the text to improve readability. This is a minor formatting suggestion.

**P2-N3: Consistency of `σ(f_NL)` for MegaMapper**
*   **Section/Page:** V, p. 10 and VII B, p. 16 (Fig. 5).
*   **Problem:** The text on page 10 states the ideal MegaMapper forecast is `σ(f_NL) ≈ 0.5`. The left panel of Figure 5 on page 16 includes a line labeled "MegaMapper ideal (σ=0.5)". However, the blue line for "MegaMapper SDB" starts at `σ(f_NL) ≈ 0.5` only at a `b_φ` prior uncertainty of 0%, and rises steeply. The text on p. 16 states that at the baseline 20% prior width, "MegaMapper SDB gives `σ(f_NL) ≈ 1.0`". This seems contradictory.
*   **Fix:** Please clarify that the "ideal `σ(f_NL) ≈ 0.5`" refers to the forecast *before* marginalization over `b_φ` (or assuming a perfect prior). The text should be harmonized to state something like: "The ideal, pre-marginalization forecast for MegaMapper is `σ(f_NL) ≈ 0.5`. However, as shown in Fig. 5, marginalizing over a realistic 20% prior on `b_φ` degrades this to `σ(f_NL) ≈ 1.0`."

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent and comprehensive paper that will be of significant interest to the cosmology community. The analysis is performed at a very high level of rigor, and the paper is written with admirable clarity and transparency. The authors have done a great service by not only providing a detailed forecast but also by carefully delineating the underlying assumptions, quantifying a key theoretical uncertainty (the polynomial null space), and resolving a confusing factor-of-two discrepancy in the literature. The systematic, observational, and theoretical aspects are handled with sophistication. The paper is a model of how a forecast study should be conducted and presented. After addressing the minor points listed above, the paper will be ready for publication in Physical Review D.