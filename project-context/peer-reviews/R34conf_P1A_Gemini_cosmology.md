# P1A R34conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.62.pdf` md5=9a1a725b pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 138.6s

---

**Referee Report for "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

**Manuscript ID:** [Assigned by editor]
**Journal:** Physical Review D

This paper presents a systematic assessment of four potential channels through which minimal Einstein-Cartan-Holst (ECH) theory could source late-time dark energy. The authors conclude that all four enumerated routes are closed, either by amplitude suppression or by a naturalness objection that recasts the cosmological constant problem. The central theoretical result is a "perturbation-transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbation equations of motion at all orders. The paper argues that the surviving, testable predictions often associated with such frameworks, namely a non-Gaussianity signature (`f_NL = -35/8`) and cosmic birefringence (`β`), are not distinctive predictions of the minimal ECH model but rather of the broader matter-bounce and spectator-ALP classes of models, respectively.

The analysis is comprehensive, rigorous, and intellectually honest. The authors are commendably transparent about the assumptions and limitations of their framework, particularly the phenomenological nature of the scaling ansatz required to connect the Planck-scale physics to the dark energy scale. The perturbation-transparency result is elegant and significant, clarifying which observables are and are not affected by the Holst term in this context. The systematic "no-go" arguments for the four dark-energy routes are well-reasoned and provide a valuable map of the phenomenological landscape.

Despite these strengths, the manuscript has several issues that preclude its publication in the current form. The most critical is its reliance on multiple companion papers that are cited as "in preparation" or "posted concurrently," which makes the present work not self-contained and its supporting evidence unverifiable.

## Detailed Findings

### ESSENTIAL

*   **P1A-E1: Reliance on Unpublished Companion Papers**
    *   **Location:** Throughout the paper, but specifically noted on Page 4 ("Companion paper" section), Table I (footnote b), Table IV, and in discussions of galaxy spin (Sec. V) and `f_NL` forecasts (Sec. VII).
    *   **Problem:** The paper bases several of its quantitative claims and contextual arguments on results from companion papers [2, 6, 23] which are not yet published or publicly archived. A manuscript submitted to PRD must be self-contained. Key inputs, such as the MCMC-derived cosmological parameters (`H_0`, `ΔN_eff`), the details of the SPHEREx `f_NL` Fisher forecast, and the full analysis of the galaxy spin null result, are located in these external, un-reviewed documents. While the authors correctly state that their core theoretical closure arguments do not depend on the MCMC posteriors, these values are used to "anchor the discussion" and are presented in summary tables, giving them an air of established fact.
    *   **Required Fix:** The manuscript must be made self-contained. The authors should either (a) incorporate the essential methods and results from the companion papers into appendices of the current manuscript, or (b) wait to submit this paper until the companion works are accepted for publication or are publicly available on a permanent archive (like arXiv) and can be properly cited. Citing work as "in preparation" is not acceptable for load-bearing claims.

*   **P1A-E2: Placeholder Dates and Versioning**
    *   **Location:** Page 1, Abstract: "(Dated: June 11, 2026 PDT)"; Page 24, Data and Code Availability section: "resynced 2026-06-10".
    *   **Problem:** The manuscript contains future dates, which is unprofessional and indicates that the submission is not in its final form.
    *   **Required Fix:** All dates must be corrected to reflect the actual date of submission. The versioning information in the Data Availability section must be finalized to correspond to the exact state of the code and data at the time of submission.

### MAJOR

*   **P1A-M1: Disconnection in the CMB Birefringence Analysis**
    *   **Location:** Page 9, Sec. III A; Page 12, Sec. IV D.
    *   **Problem:** The paper's analysis of cosmic birefringence (`β`) is not a direct test of the minimal ECH model. The authors honestly state that a direct coupling between the ECH torsion sector and photons "has not been derived here." The analysis then pivots to constraining a generic spectator-ALP field. Consequently, the closure of "Route 4" is a naturalness argument against this spectator field, not a direct constraint on the fundamental ECH theory. While this is a valid argument for the spectator-ALP scenario, the connection to the core ECH framework is tenuous.
    *   **Required Fix:** The abstract and introduction must more clearly and prominently state this limitation. It should be made explicit from the outset that the CMB birefringence discussion serves as a test of a hypothetical ECH-plus-photon-sector extension, for which a spectator-ALP model is used as a proxy, rather than a direct test of the minimal ECH model itself.

### MINOR

*   **P1A-m1: Unclear Provenance in Table Footnote**
    *   **Location:** Page 4, Table I, footnote `b`.
    *   **Problem:** The footnote `b` concerning the `f_NL` forecast significance (`2.6-5σ`) is dense and relies entirely on a companion paper.
    *   **Required Fix:** Pending the resolution of P1A-E1, this footnote should be made more descriptive. For example: "The 2.6-5σ range reflects pessimistic and optimistic forecasts, respectively, after accounting for systematic effects such as GR projection and photo-z uncertainties, with full details provided in [2]." This would improve readability and context for the reader.

### NIT

*   **P1A-N1: Redundant Phrasing**
    *   **Location:** Page 23, Sec. XV Conclusions.
    *   **Problem:** The text reads "...distinct from - and not equal to - the Pontryagin density...".
    *   **Required Fix:** The phrase "and not equal to" is redundant. Simplify to "distinct from the Pontryagin density".

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, rigorous, and well-written theoretical paper with significant potential. The core claims regarding the perturbation-transparency of the Holst term and the closure of the enumerated dark-energy channels are well-supported and represent a valuable contribution to the cosmology literature. However, the manuscript is not ready for publication in its current state. The essential issue of relying on unpublished companion papers for key results and context must be fully resolved. Once the manuscript is made self-contained and the placeholder information is corrected, it will be a strong candidate for publication in Physical Review D.