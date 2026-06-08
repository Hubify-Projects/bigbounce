# P1B auto-2026-06-08_1354pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2803 chars)
**Wall time**: 115.6s

---

## Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..."

This paper presents three technical analyses intended as a companion to a larger program on Einstein-Cartan-Holst (ECH) cosmology. The analyses cover: (1) a ΛCDM+ΔNeff MCMC analysis as a null test, (2) a validation of a NaMaster pseudo-Cℓ pipeline for birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The scientific content of the analyses is generally sound. The authors are commendably careful in scoping their claims, providing clear caveats, and distinguishing between pipeline validation and on-sky detection. The statistical interpretations, particularly regarding model comparison and the limitations of MCMC posteriors, are rigorous and correct. The provision of a public repository with code and configuration files is excellent and meets modern standards for reproducibility.

However, the paper suffers from a significant structural problem that severely impacts its readability and logical flow. The results of different, independent analyses are intermingled in a confusing manner. This structural issue is the primary obstacle to publication and must be addressed.

---

### Detailed Findings

#### ESSENTIAL

*   **P1B-E1: Paper Structure and Readability (Sections III and V, Pages 2-4, 6)**
    *   **Problem:** The paper's structure is highly confusing. Section III is titled "Stock-CAMB ΛCDM+ΔNeff MCMC", but halfway through (p. 3), it abruptly pivots to a detailed "Physics interpretation" of a completely different analysis, a w0-wa model, whose results are presented in Table II. The ΔNeff results are in Table I. Then, Section V, "Cosmological Fits and Model Comparison," re-summarizes the results from both the ΔNeff and w0-wa analyses, making it largely redundant with Section III. This organization makes the paper very difficult to follow. The w0-wa analysis, which yields a >4σ departure from ΛCDM, is a significant result in its own right and should not be buried as a subsection of the ΔNeff analysis.
    *   **Required Fix:** The paper must be restructured for clarity. I recommend the following structure:
        1.  Introduction (largely as is).
        2.  A new, dedicated section for the "ΛCDM+ΔNeff MCMC Proxy Test". This section should contain the setup, Table I, the corner plot (Fig. 1), and the discussion currently on pages 2-3 and the top of p. 4 related to this analysis.
        3.  A new, dedicated section for the "w0-wa Quintom-B Test". This section should introduce this separate analysis, present its setup, Table II, and the associated discussion currently mixed into Section III.
        4.  The "CMB E-B Analysis" (current Sec. IV) and "Spectator ALP Consistency Check" (current Sec. VI) can remain as they are.
        5.  The current Section V should be eliminated, and its unique content (e.g., the list of datasets) should be integrated into the newly structured sections. The conclusion (Sec. VII) already provides an adequate summary.

#### MAJOR

(No findings classified as MAJOR. The structural issue in P1B-E1 is deemed ESSENTIAL.)

#### MINOR

*   **P1B-M1: Incorrect Section Reference (Section VII, Page 8)**
    *   **Problem:** In the "Spectator-ALP consistency" summary paragraph of the Conclusions, the text refers to the NaMaster pipeline bias calculation. The text reads: "...amplitude-dependent bias 0.032-0.040° (worst-case 0.040° at injection β = 0.342°; see §VI body text)...".
    *   **Required Fix:** The NaMaster pipeline validation is described in Section IV, not Section VI. The reference should be changed to "§IV".

*   **P1B-M2: Typo in Equation (3) (Section VI, Page 7)**
    *   **Problem:** Equation (3) for the birefringence angle β contains a typo. It is written as "β ≈ (OEM × 8 / 4π) × 1.07 ≈ 0.29°". The fine-structure constant α_EM is incorrectly written as "OEM".
    *   **Required Fix:** Replace "OEM" with the standard notation "α_EM".

*   **P1B-M3: Unclear Sample Count in Figure Caption (Figure 1, Page 5)**
    *   **Problem:** The caption for Figure 1 states it shows "119,617 post-burnin samples, getdist-thinned from 176,240 raw". Footnote 1 (p. 2) calculates the post-burnin count as ~123,368. Footnote 2 (p. 3) clarifies that the 119,617 number is due to "additional getdist effective-sample weight-based thinning". While this is documented, it is confusing.
    *   **Required Fix:** For maximum clarity, the caption of Figure 1 should be self-contained. I suggest adding a brief parenthetical explanation directly in the caption, e.g., "(119,617 post-burnin samples, thinned from 176,240 raw samples for plotting via getdist's effective-sample weighting; see fn. 1 and 2 for details)".

#### NIT (Nitpicks)

*   **P1B-N1: Dated Reference in Abstract (Abstract, Page 1)**
    *   **Problem:** The abstract gives the date as "(Dated: 2026-06-03 PDT)". This is presumably a placeholder and is set in the future.
    *   **Required Fix:** Update the date to the current submission date.

*   **P1B-N2: Redundant Phrase (Section III, Page 3)**
    *   **Problem:** In the "Caveats" subsection for the w0-wa analysis, the text says: "...robust In B recompute therefore requires dedicated nested sampling (e.g., PolyChord or Multi-Nest) or thermodynamic integration on the same likelihood stack rather than a KDE readout from the converged Metropolis-Hastings chain; robust In B computation is left to a follow-up nested-sampling analysis." The phrase "robust ln B" is used twice in close succession.
    *   **Required Fix:** Consider rephrasing to avoid the repetition, for example: "...robust ln B recompute therefore requires dedicated nested sampling... This computation is left to a follow-up nested-sampling analysis."

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a set of well-executed and carefully documented technical analyses. The authors demonstrate a high level of rigor in their methods and interpretation, particularly in their handling of statistical caveats and scope limitations. However, the paper is critically undermined by a confusing structure that mixes results from independent analyses, making it unnecessarily difficult for the reader to follow the paper's logic. The required revisions, centered on reorganizing the content into a more logical flow, are substantial but should be straightforward to implement as they primarily involve rearranging existing text. Once these structural issues are addressed, the paper will be a valuable and clear contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

An excellent and rigorous second pass. Here are the new findings to add to the report.

================================================================
### Additional Findings from Second Review

My second, more detailed review confirms the soundness of the paper's calculations and the authors' careful approach to scoping their claims. The arithmetic is robust, and the internal consistency is high. The initial review's primary finding—the essential need for structural reorganization—remains the most critical issue. The following new points are mostly minor but will further improve the paper's precision.

#### MINOR

*   **P1B-m4: Confusing Phrasing in Pipeline Bias Calculation (Section IV, Page 5)**
    *   **Problem:** The sentence describing the pipeline bias recovery is slightly ambiguous. It reads: "The pipeline-recovery bias is Δβ = 0.032° at injection β = 0.27° (β = 0.238°) and Δβ = 0.040° at injection β = 0.342°". The parenthetical `(β = 0.238°)` could be misinterpreted.
    *   **Required Fix:** Clarify that this is the recovered value. A simple fix would be to change the parenthetical to `(recovering β = 0.238°)`.

*   **P1B-m5: Overly Strong Claim in Hubble Tension Calculation (Section III, Page 4)**
    *   **Problem:** In the "MB-H0 joint-posterior offset check," the text calculates the tension in the MB direction as ~3.2σ and states this "corresponds exactly to the canonical 3.6σ Hubble tension". While the physical point is correct (the tension manifests across correlated parameters), the word "exactly" is too strong given the numerical difference (3.2σ vs. 3.6σ), which likely arises from ignoring parameter covariances in the simple check.
    *   **Required Fix:** Soften the language to be more precise. Replace "corresponds exactly to" with a phrase like "is the manifestation of" or "corresponds to".

#### NIT (Nitpicks)

*   **P1B-N3: Minor Typo in H0 Value (Section III, Page 4)**
    *   **Problem:** In the paragraph discussing the full-tension chain, the text quotes `H0 = 67.69 ± 1.06 km/s/Mpc`. Table I, the authoritative source for this result, lists it as `67.68 ± 1.06`.
    *   **Required Fix:** Change `67.69` to `67.68` to maintain consistency with Table I.

*   **P1B-N4: Unquantified Expectation for Pipeline Bias (Section IV, Page 5)**
    *   **Problem:** The text states the recovered bias of `0.032°` is "consistent with the apodized-mask bias expected from a 2º apodization scale". This claim, while plausible, is unquantified and unsupported by a citation or estimate.
    *   **Required Fix (Optional but Recommended):** To strengthen the claim, add a citation to a relevant work on pseudo-Cℓ methods or provide a brief estimation of the expected bias. For example: "(as expected for E→B leakage from a C2 mask of this scale [cite])".