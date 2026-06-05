# P1B 2026-06-04_R5clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 52.2s

---

**Referee Report: P1B**

This paper presents three technical verification analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program: (1) a `ΛCDM+∆Neff` MCMC analysis as a null test, (2) a `NaMaster` pipeline validation for birefringence measurements, and (3) a spectator-ALP model consistency check for the observed birefringence signal. The paper serves as a companion to a main theory paper (Paper I(a)).

The three core analyses are well-scoped and the author is commendably transparent about their limitations (e.g., clarifying that the MCMC is a proxy test, the NaMaster run is a pipeline validation not a sky detection, and the ALP model requires fine-tuning). However, the manuscript in its current form is not suitable for publication. It suffers from severe structural and presentational issues, including a confusing narrative that mixes in a fourth, un-abstracted analysis with strong claims, and contains numerous artifacts that appear to be internal notes or remnants of a review process.

## ESSENTIAL

*   **P1B-E1 (Abstract, p. 1; Table II, p. 4):** The paper is dated with a future year (2026). This must be corrected to the current date of submission/revision.
    *   **Problem:** The date is "Dated: 2026-06-03 PDT". The date "2026-05-18" also appears in the caption for Table II.
    *   **Fix:** Correct all dates to the present.

*   **P1B-E2 (Table III, p. 10):** The paper includes a "Claims classification" table (Table III) that appears to be an internal project management or tracking tool. This is highly unconventional and inappropriate for a scientific publication.
    *   **Problem:** Table III lists claims, their type, status, and notes. This is not a presentation of scientific results.
    *   **Fix:** Remove Table III entirely.

*   **P1B-E3 (Throughout, esp. Sec III, V):** The paper's structure is fundamentally confusing. The abstract and introduction frame the paper around three specific analyses. However, the main body (Sections III and V) is dominated by the results of a fourth analysis—a `w0wa` model fit (`iter2`)—which is not mentioned in the abstract or introduction. This analysis makes a strong claim about a >4σ departure from ΛCDM, which distracts from and obscures the paper's stated purpose as a verification companion.
    *   **Problem:** The narrative jumps from the `ΛCDM+∆Neff` proxy to the `w0wa` results without clear motivation or transition, making the paper's focus unclear. The abstract does not match the content of the main results sections.
    *   **Fix:** The paper must be completely restructured. The author must choose one of two paths: (1) Remove the `w0wa` analysis entirely and rewrite the paper to focus solely on the three analyses promised in the abstract. (2) Elevate the `w0wa` analysis to a primary result, introduce it in the abstract and introduction, and give it a dedicated section that clearly explains its motivation and context. The current hybrid approach is unacceptable.

*   **P1B-E4 (Throughout):** The manuscript is filled with internal versioning tags, file paths, and other artifacts that are not suitable for a final publication.
    *   **Problem:** Examples include "(Paper I(a) v1A.0.22)" (p. 2), "reproducibility/cosmology/iter2_converged_2026-05-18/" (p. 4), and the tag "paper1b-v1B.0.36" (p. 6).
    *   **Fix:** Scour the manuscript and remove all such internal-facing artifacts.

## MAJOR

*   **P1B-M1 (Sec III, p. 3):** The language used to present the `w0wa` result is too strong and potentially misleading, given the nature of the statistical evidence.
    *   **Problem:** The text states the posterior "disfavors... the LCDM point... at the joint level: w0 departs by +4.3σ and wa departs by -3.6σ". While footnotes clarify this is an "extrapolation distance" because the ΛCDM point is unsampled, the main text uses the language of a direct frequentist tension. For a methods-focused paper, this distinction is critical.
    *   **Fix:** Rephrase the main text to be more precise. For example: "The posterior for the `w0wa` model is centered far from the ΛCDM point, which is unsampled by the chain. The distance from the posterior mean to the ΛCDM point is 4.3σ in the `w0` marginal and 3.6σ in the `wa` marginal, indicating a strong preference for a phantom-crossing model over ΛCDM within this analysis, though a robust model comparison requires a dedicated nested sampling analysis."

*   **P1B-M2 (Throughout):** The text contains numerous phrases that read like responses to a previous review cycle, rather than as polished, standalone prose.
    *   **Problem:** Examples include: "Sample-count stratification (reconciliation)" (p. 2), "This addresses earlier reviewer concerns" (p. 4), "A concern was raised" (p. 4), "Direct arithmetic audit" (p. 4), "correcting the earlier Caγθi product" (p. 8).
    *   **Fix:** Rewrite these sections to present the information neutrally, without referring to an external review process. For example, instead of "A concern was raised...", simply state the potential issue and then present the audit that resolves it.

## MINOR

*   **P1B-m1 (Abstract, p. 1):** The abstract contains a footnote ('a') for a "disambiguation" of a reference. This level of detail is not appropriate for an abstract.
    *   **Problem:** The footnote clutters the abstract and breaks the flow.
    *   **Fix:** Move the content of this footnote into the main body of the text where the Eskilt & Komatsu result is first discussed in detail (e.g., Section VI).

*   **P1B-m2 (Contents, p. 1):** The Table of Contents has an oddly placed parenthetical line item.
    *   **Problem:** The line "(Not a Spin-Torsion Theory Module)" appears as a separate entry.
    *   **Fix:** Make this a subtitle for Section III, both in the Contents and in the section heading itself.

*   **P1B-m3 (Sec V.A, p. 4):** There is a likely typographical artifact in the text.
    *   **Problem:** The text reads "direct .input.yaml inspection". The leading space before the period is anomalous.
    *   **Fix:** Correct to "direct input.yaml inspection" or similar.

*   **P1B-m4 (Sec V.B, p. 6):** A subsection heading is a full sentence describing an action, not a title.
    *   **Problem:** The heading is "a. Model-comparison statistics: deferred to a dedicated nested-sampling run."
    *   **Fix:** Retitle the subsection to something like "Parameter Constraints and Model Selection".

*   **P1B-m5 (Acknowledgments, p. 8):** The acknowledgment of an AI research assistant is non-standard.
    *   **Problem:** "The author acknowledges the use of Claude (Anthropic) as an AI research assistant..."
    *   **Fix:** The author should consult PRD editorial policy on the proper way to disclose the use of AI tools in manuscript preparation. This may need to be rephrased or moved to a different section per journal guidelines.

## NIT

*   **P1B-N1 (Throughout):** Inconsistent notation is used for the Gelman-Rubin statistic.
    *   **Problem:** The text uses both `R-1` (Table I) and `R̂-1` (Table II, Conclusions).
    *   **Fix:** Use the standard notation `R̂-1` consistently.

*   **P1B-N2 (Throughout):** Inconsistent acronyms are used for ΛCDM and the SH0ES survey.
    *   **Problem:** The paper uses both `ACDM` and `ΛCDM`, and both `SHOES` and `SH0ES`.
    *   **Fix:** Choose one spelling for each and use it consistently (`ΛCDM` and `SH0ES` are standard).

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a set of well-scoped and carefully caveated technical analyses that could be a valuable companion to a theory paper. The author's transparency regarding the limitations of each analysis is a significant strength. However, the manuscript is not ready for publication. It is critically undermined by a confusing structure that fails to follow the outline promised in the abstract, instead giving significant weight to an unrelated `w0wa` analysis. Furthermore, the paper is littered with unprofessional artifacts, internal notes, and future dates that must be removed. A thorough rewrite is required to focus the narrative on the paper's stated goals and bring the presentation up to a publishable standard.