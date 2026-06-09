# P2 R22prov2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 158.6s

---

## Referee Report: Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook

This manuscript presents a comprehensive forecast for testing the matter-bounce cosmological scenario using upcoming data from the SPHEREx survey. The primary observable considered is the local-type non-Gaussianity parameter, `f_NL`, for which the matter bounce makes a sharp prediction of `f_NL = -35/8`. The authors perform a detailed analysis, recasting existing SPHEREx forecasts to account for theoretical and observational systematics. The main contributions are: (1) a thorough quantification of the template mismatch between the true matter-bounce bispectrum and the standard local template, including the impact of theoretical ambiguities in the polynomial representation of the shape function; (2) a full systematic budget analysis, leading to a realistic forecast for the detection significance; and (3) a Bayesian model comparison to quantify the discriminating power of SPHEREx against inflationary alternatives. The manuscript also provides a valuable clarification of a factor-of-two discrepancy in the literature regarding the predicted `f_NL` value.

The paper is exceptionally well-researched, methodologically sound, and transparent. The analysis is detailed and rigorous, and the authors are careful to state all assumptions and caveats. The handling of a retracted numerical result from a previous analysis stage (the joint SDB forecast) is a model of scientific integrity. The paper represents a significant and timely contribution to the field. However, several revisions are required to improve clarity and rigor on key points before the manuscript can be considered for publication in Physical Review D.

---
### Findings

#### MAJOR

*   **P2-M1: Lack of a quantitative systematic error budget.**
    *   **Section:** Abstract (p1), Sec. IV (p7), Sec. VII (p12-13).
    *   **Problem:** The paper's headline result is the post-systematic detection significance of `~3-5σ`. This is derived by degrading an optimistic, pre-systematic significance of `5.2-5.5σ`. While Section VII discusses the various systematic effects qualitatively (GR projections, `b_φ` uncertainty, photo-z degradation, etc.) and provides percentage-level estimates for some, the paper never explicitly shows how these effects are combined to arrive at the final `3-5σ` range. The link between the optimistic forecast and the final headline result is therefore opaque and not reproducible from the text.
    *   **Required Fix:** The authors must provide a quantitative breakdown of the systematic error budget. This could be in the form of a table or a clear, itemized paragraph. For a given baseline scenario (e.g., the `5.2σ` LSS-noise-weighted case), the authors should show how the significance is successively degraded by each systematic effect considered (e.g., template mismatch is already included, then add GR effects, then `b_φ` marginalization, etc.). This would make the paper's primary claim transparent and verifiable.

#### MINOR

*   **P2-m1: Confusing description of Bayes Factor variations in the abstract.**
    *   **Section:** Abstract (p1).
    *   **Problem:** The abstract states: "the GR-marginalization variation across the four scenarios of Table III (Sec. VII) introduces a separate BF ≈ 8-11 spread on the delta-prior row of Table II". This is potentially misleading. Table III shows the GR variation for a *narrow* multifield competitor prior, which results in BF ≈ 8-11. However, the main delta-prior result quoted for Table II is BF ≈ 17, which corresponds to a *broad* multifield competitor prior. The sentence structure makes it sound like the 8-11 spread applies to the same case that gives BF=17.
    *   **Required Fix:** Clarify the sentence to explicitly state that the 8-11 spread from GR variation corresponds to the *narrow* competitor prior case, distinct from the BF ≈ 17 result for the *broad* competitor prior. For example: "...and the GR-marginalization variation (see Table III) introduces a BF ≈ 8-11 spread for the delta-prior against a narrow competitor prior."

*   **P2-m2: Ambiguity in the `f_NL` convention terminology.**
    *   **Section:** Sec. IIC (p5), Abstract (p1), and throughout.
    *   **Problem:** The paper refers to the discrepancy between Cai et al. [7] (`f_NL=-35/8`) and Li & Brandenberger [17] (`f_NL=-35/16`) as a difference between the "Planck/Cai (c=2) convention" and the "Li & Brandenberger (c=1) normalization". As Appendix A excellently clarifies, the issue is twofold: a genuine normalization choice (`c`) and a physical factor of two from the in-in commutator (`-2 Im`). Lumping the physical commutator factor into the "convention" label is an oversimplification that slightly obscures the nature of the discrepancy in the main text.
    *   **Required Fix:** While the appendix is perfectly clear, the main text would benefit from more precise language. For instance, refer to the two cases as the "full in-in commutator result" (`-35/8`) versus the "single time-ordering result" (`-35/16`), while noting that both are presented here in the Planck (`c=2`) normalization. This is a minor wording change but improves precision.

*   **P2-m3: Inconsistent presentation of GR assumption in Table II.**
    *   **Section:** Table II and caption (p11).
    *   **Problem:** The caption for Table II states that the results are evaluated "at fixed baseline GR (σ_GR = 0.5)". However, one of the rows in the table ("Delta at f_NL = -35/8, narrow... (GR-variation only)") explicitly shows a result derived from varying GR effects. This makes the overall "fixed baseline" statement for the table inconsistent.
    *   **Required Fix:** Revise the table or caption for clarity. Either add a column to the table specifying the `σ_GR` assumption for each row, or amend the caption to state "All values are evaluated at a fixed baseline GR (σ_GR = 0.5) unless explicitly noted otherwise, as in the GR-variation row."

*   **P2-m4: Overstated significance of Planck PR4 update.**
    *   **Section:** Sec. VIII A (p13).
    *   **Problem:** The text states that "the PR4 NPIPE reanalysis tightens the error bar by ~2%". While numerically correct (`5.1` to `5.0`), a 2% change is marginal and within the rounding uncertainty of the quoted values. Phrasing it as a "tightening" might give a slight impression of a more significant improvement than was achieved.
    *   **Required Fix:** Soften the language slightly, for example: "...the PR4 NPIPE reanalysis reports a marginally smaller error bar (~2%) and shifts the central value toward zero...".

#### NIT-PICKING (Cosmetic)

*   **P2-N1: Overly complex sentence in the abstract.**
    *   **Section:** Abstract (p1).
    *   **Problem:** The sentence beginning "the headline envelope is therefore BF ~ 10-17 at the broad-multifield competitor..." is very long and contains multiple nested clauses and numerical values.
    *   **Required Fix:** Consider splitting this sentence into two for improved readability.

*   **P2-N2: Informal phrasing.**
    *   **Section:** Sec. IIC (p5).
    *   **Problem:** The phrase "the nearly order-of-magnitude range in K₁" is slightly informal for a PRD paper.
    *   **Required Fix:** Suggest rephrasing to something like "the wide range of K₁, which spans nearly an order of magnitude".

---
## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, thorough, and valuable paper that is very close to the standard for publication in Physical Review D. The authors have done an excellent job of forecasting the potential of SPHEREx to test a key prediction of the matter-bounce scenario, with careful attention to a wide range of systematics and theoretical nuances. The recommendation for Major Revisions is based on one key point: the lack of a quantitative, reproducible breakdown of the systematic error budget (P2-M1). The paper's headline significance of `3-5σ` is its most important result, and readers must be able to see exactly how this number is derived from the optimistic forecast. Addressing this point, along with the other minor revisions, will make the paper's conclusions significantly more robust and transparent, and would render the manuscript suitable for publication.