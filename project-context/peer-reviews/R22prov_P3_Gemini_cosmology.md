# P3 R22prov — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 167.6s

---

## Referee Report for "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The work is notable for its scale, its multi-survey approach enabling cross-validation, and its careful treatment of methodological artifacts such as training-set bias and cross-survey domain shift. The authors apply the resulting catalog to constrain primordial non-Gaussianity (PNG) and test the consistency of the matter-bounce scenario with pulsar timing array data.

The overall quality of the work is high, demonstrating methodological rigor, transparency about limitations, and a significant effort in validation. The resulting catalog and the methodological lessons learned are a valuable contribution to the community. However, there are several issues, particularly in the presentation and calculation of the cosmological forecasts, that must be addressed before the paper can be considered for publication in Physical Review D.

### Summary of Findings

**ESSENTIAL (1):** The primary cosmological forecast for σ(fNL) is presented with a non-standard and misleading error envelope.
**MAJOR (3):** A key percentage improvement claim cannot be reproduced; the use of two differently-normalized Fisher forecasts creates potential for confusion; the inclusion of a NANOGrav analysis feels disconnected from the main work.
**MINOR (4):** Several points of clarification are needed regarding anomaly thresholds, notation, and the logic for retaining catalogs that fail validation gates.
**NIT (1):** Typographical error in the date.

---

### Detailed Findings

#### ESSENTIAL

*   **P3-E1: Non-standard and misleading σ(fNL) error envelope.**
    *   **Location:** Abstract (p.1), §V.b (p.12), Table IV (p.15), Conclusion 5 (p.16).
    *   **Problem:** The paper reports a central forecast of σ(fNL) = 8.14 with a "1σ envelope [3.92, 8.98]". This interval is constructed from the minimum value of σ within the 1σ range of the bias parameter `a` (which is 3.92) and the value of σ at the null-hypothesis `a=0` (which is 8.98). This is not a standard 1σ confidence interval. The 1σ interval on `a` ([−0.46, 0.84]) correctly propagates to a 1σ interval on σ(fNL) of [3.92, 5.93]. Presenting the null value as the upper bound of the confidence interval is confusing and misrepresents the uncertainty.
    *   **Fix:** The authors must replace the non-standard envelope [3.92, 8.98] with the correctly propagated 1σ interval [3.92, 5.93] in all instances. Alternatively, they must provide a compelling justification for their non-standard choice and clearly define it in the text.

#### MAJOR

*   **P3-M1: Discrepancy in quoted σ(fNL) improvement.**
    *   **Location:** Abstract (p.1), Conclusion 5 (p.16).
    *   **Problem:** The paper claims a "7.9% improvement" when σ(fNL) is reduced from the single-tracer baseline of 8.98 to the multi-tracer value of 8.14. However, a direct calculation yields (8.98 - 8.14) / 8.98 = 9.35% improvement. The origin of the 7.9% figure is unclear.
    *   **Fix:** The authors must clarify the calculation of the 7.9% value or correct it to 9.4%.

*   **P3-M2: Potential for confusion between two different Fisher forecasts.**
    *   **Location:** §V (p.12) and Appendix C / Fig. 11 (p.18).
    *   **Problem:** The paper uses two distinct Fisher forecast calculations. The primary forecast in §V has a single-tracer baseline of σ(fNL)std = 8.98. A second, simplified forecast is used for the shot-noise analysis in Appendix C and Figure 11, which has a single-tracer baseline of σ(fNL) = 16.85 and a dense-tracer limit of σ(fNL) = 11.71. While the caption of Fig. 11 correctly notes the different normalization, the main text in §V does not warn the reader about this. This could lead to significant confusion, as the absolute σ values are not comparable.
    *   **Fix:** The main text in §V must explicitly state that a simplified, differently-normalized forecast is used for the shot-noise study in the appendix, and that its absolute σ(fNL) values should not be directly compared to those from the primary, redshift-binned forecast.

*   **P3-M3: Disconnected NANOGrav analysis.**
    *   **Location:** §VA (p.13).
    *   **Problem:** The analysis of NANOGrav 15-yr data to constrain the gravitational-wave background spectral index γ feels out of place. It uses a different dataset and methodology, and its only connection to the main paper is the shared "matter-bounce" model, which makes predictions for both fNL and γ. This section dilutes the paper's focus on optical/X-ray/CMB anomaly detection and its direct cosmological application.
    *   **Fix:** The authors should consider moving this section to an appendix to maintain the focus of the main text. Alternatively, they must better integrate it by, for example, discussing the joint constraints from both the anomaly-tracer fNL analysis and the NANOGrav γ analysis on the matter-bounce parameter space.

#### MINOR

*   **P3-m1: Ambiguity in DESI anomaly threshold.**
    *   **Location:** §IIIA (p.4).
    *   **Problem:** The text states the "headline 195,829 DESI anomaly count is the top-1% score-cut". However, the abstract and §IIB (p.3) state it derives from an absolute threshold of S > 5.0, which corresponds to a 0.87% rate. This is a minor contradiction.
    *   **Fix:** Please clarify that the S > 5.0 threshold is the definitive one and that "top-1%" is an approximation.

*   **P3-m2: Confusing notation for correlation coefficient.**
    *   **Location:** §IIIA (p.4).
    *   **Problem:** The text "The Spearman rank correlation ... is p = -0.03 (p = 0.12...)" uses the letter 'p' for both the correlation coefficient (ρ) and the p-value.
    *   **Fix:** Please use the standard notation ρ for the Spearman coefficient to avoid ambiguity.

*   **P3-m3: Unclear logic for retaining "FAIL" catalogs.**
    *   **Location:** Throughout §III, e.g., §IIIE (p.6) for eROSITA.
    *   **Problem:** Several surveys (LAMOST, Gaia, eROSITA) are noted as "FAIL" on the injection-recovery gate but are retained, sometimes with the label "exploratory". The logic is inconsistent, as ACT DR6 is "quarantined" for failing its gates. The criteria for when a "FAIL" leads to quarantine versus exploratory retention are not clearly articulated.
    *   **Fix:** Please provide a clear, upfront statement in the Methods section (§IID) defining the decision logic. For example, explain that if a survey fails the primary gate but shows high stability in a secondary metric (like cross-validation), it is retained as an exploratory catalog.

*   **P3-m4: Potentially confusing phrasing for NEOWISE mask.**
    *   **Location:** §IID.4 (p.3) and §H (p.7).
    *   **Problem:** The mask is described as an "ecliptic-pole mask" with the retained region being `|b_ecl| < 80°`. This is slightly confusing, as the name suggests a mask *of* the poles, which would be `|b_ecl| > 80°`.
    *   **Fix:** Consider rephrasing for clarity, for example, "a mask removing the ecliptic poles (|b_ecl| > 80°)" or similar.

#### NIT

*   **P3-N1: Date of submission.**
    *   **Location:** Abstract (p.1).
    *   **Problem:** The date is listed as "(Dated: June 2026)".
    *   **Fix:** Correct to the actual date of submission.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a strong, comprehensive, and methodologically sound paper that presents a significant data product and valuable scientific results. The authors' attention to detail in validating their methods and transparently reporting limitations is commendable. The work is well-suited for publication in Physical Review D. However, the identified issues, particularly the essential problem with the σ(fNL) error envelope and the major points regarding the reproducibility of the improvement claim and the clarity of the Fisher forecast normalizations, must be thoroughly resolved. Once these revisions are made, the paper will represent an excellent contribution to the field.