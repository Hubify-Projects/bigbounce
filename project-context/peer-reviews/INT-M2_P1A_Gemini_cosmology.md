# P1A INT-M2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=a80102d5 pages=32
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2509 chars)
**Wall time**: 172.8s

---

**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

**P1A-Report-v1**

This paper presents a systematic investigation into the possibility of generating late-time dark energy from four minimal channels within Einstein-Cartan-Holst (ECH) gravity. The authors conclude that, under stated assumptions, all four channels are closed. The primary mechanisms for closure are amplitude suppression, thermal washout, and a fine-tuning objection. The paper's central theoretical result is a "perturbation-transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector of ECH gravity decouples from all scalar and tensor perturbation equations, leaving them identical to those of standard General Relativity. The paper also identifies two "surviving" observational tests, `f_NL = -35/8` from the matter-bounce scenario and cosmic birefringence from a spectator axion-like particle (ALP), clarifying that these are tests of broader model classes, not specific predictions of the minimal ECH framework.

The paper is exceptionally well-structured, thorough, and intellectually honest. The authors are commendably transparent about their assumptions, particularly the phenomenological on-shell scaling ansatz that underpins the entire dark-energy connection. The perturbation-transparency result is clean, rigorously proven, and has significant implications for constraining ECH-type theories with cosmological perturbations. The systematic catalog of 13 distinct "barriers" is a valuable contribution that maps out the failure modes of this class of models.

However, the manuscript in its current form has several issues that must be addressed before it can be considered for publication in Physical Review D. The most critical issue is the extensive reliance on quantitative results, particularly observational forecasts, cited from companion papers that are "in preparation." A published paper must be self-contained in its primary, load-bearing claims.

## Summary recommendation
**MAJOR REVISIONS**

The paper contains a solid and valuable core, namely the perturbation-transparency theorem and the systematic barrier analysis. These results are worthy of publication. However, the manuscript requires significant revision to meet the standards of Physical Review D. The essential revisions involve removing all quantitative claims not derived within the paper. Major revisions are also needed to improve self-containment and reduce the paper's length. If the authors can successfully address these points, the revised manuscript would be a strong candidate for acceptance.

---
### Detailed Findings

#### ESSENTIAL

**P1A-E1: Removal of Quantitative Claims from "In Preparation" Companion Papers**
-   **Location:** Abstract (p. 1), Table I (p. 5), Table II (p. 7), Sec. VII (p. 16), Sec. X G (p. 20), Sec. XIII (p. 22), Sec. XV (p. 24), Fig. 4 (p. 30), Fig. 7 (p. 32), and throughout the text.
-   **Problem:** The paper repeatedly quotes specific quantitative forecasts, primarily the `2.6-5σ` realistic significance for detecting `f_NL = -35/8` with SPHEREx. These values are cited from a companion paper [2] which is "in preparation." Similarly, details of the spectator-ALP MCMC fit and benchmark value are cited to another "in preparation" paper [6]. A published work cannot be based on results from unpublished, non-peer-reviewed manuscripts. While the paper claims these numbers are "illustrative," they appear in the abstract and conclusions, and are presented as key testable consequences.
-   **Fix:** All specific sigma values, forecast ranges, and quantitative MCMC results derived in companion papers must be removed. The text should be rephrased to state the qualitative prediction (e.g., "the matter-bounce scenario predicts `f_NL = -35/8`, which is a testable signature for upcoming surveys like SPHEREx") and can cite the companion paper for the detailed forecasting methodology, but without quoting the final numerical significance. Figures 4 and 7, which are entirely based on these external forecasts, must be removed or completely redrawn to be schematic illustrations without specific significance values on the y-axis.

**P1A-E2: Abstract-Body Mismatch on Key Claims (Abstract-Last Drift Sweep)**
-   **Location:** Abstract (p. 1).
-   **Problem:** The abstract presents the `f_NL` forecast and the `β ≈ 0.27°` benchmark with specific numerical significance values. As per finding P1A-E1, these numbers are not derived in the paper. Their prominent placement in the abstract gives a misleading impression of what this manuscript actually proves. The abstract must be a summary of the work contained *within this paper*.
-   **Fix:** The abstract must be rewritten to remove all quantitative forecasts and MCMC fitting results from companion papers. The focus should be on the two main results derived herein: the channel-level closure arguments and the perturbation-transparency theorem. The "surviving tests" should be mentioned qualitatively as consequences for the broader model class.

#### MAJOR

**P1A-M1: Lack of Self-Containment for Key Arguments**
-   **Location:** Sec. II C 2 (p. 10), Sec. IV D (p. 15).
-   **Problem:** The paper makes strong quantitative claims that are not substantiated with even a back-of-the-envelope calculation. For example, in Sec. II C 2, it is stated that the ECH coupling "underpredicts any plausible spin asymmetry by > 100 orders of magnitude." This is a crucial part of closing the galaxy spin channel, but no calculation is shown. Similarly, the one-loop estimate for `α/M ~ 10⁻²¹ GeV⁻¹` in Sec. IV D is central to the Route 4 argument, but its derivation is not sketched, relying on a complex chain of identifications mentioned only in a footnote (footnote 5, p. 15).
-   **Fix:** For each major physical argument, at least an order-of-magnitude derivation must be provided within the paper (possibly in an appendix). For the galaxy spin asymmetry, show the calculation that leads to the >100 OOM suppression. For the `α/M` value, the derivation should be more transparently explained in the main text or an appendix, rather than being buried in a footnote.

**P1A-M2: Excessive Length and Structure**
-   **Location:** Entire manuscript.
-   **Problem:** At 32 pages, the paper is excessively long for its core contributions. The narrative is spread across a large number of sections, subsections, and a 14-entry catalog. While thorough, this structure makes it difficult for the reader to follow the main logical thread. Much of the detailed discussion, especially for the individual barriers in Sec. IX, could be streamlined.
-   **Fix:** The paper should be significantly restructured and shortened. I recommend a target length of 15-18 pages for the main body.
    -   The main text should focus on the core logic: (1) The setup of the ECH model. (2) The perturbation-transparency theorem (Sec. X). (3) The summary of the four-route closure (a condensed version of Sec. IV). (4) The structural tension between DE and `f_NL` (Sec. XIV D). (5) Conclusions.
    -   The detailed discussions of each of the 13 barriers (Sec. IX), the derivation of the birefringence formula (Appendix C), and the dimensional analysis (Appendix B) should be moved to appendices or supplementary material. The main text can then summarize the barriers with a table (like Table III) and refer to the appendix for details.

**P1A-M3: Weakness of the Foundational "On-Shell Scaling Ansatz"**
-   **Location:** Abstract (p. 1), Sec. IIC (p. 8), Appendix B (p. 25).
-   **Problem:** The entire connection between the ECH parity-odd sector and late-time dark energy hinges on the phenomenological ansatz in Appendix B, `ρ_bounce ~ (α/M) M_Pl⁴`. This ansatz essentially assumes that a dimension +1 operator `L_odd` can source a dimension +4 energy density at the bounce, with a coefficient that makes it work. The paper is commendably honest that this is an ansatz and not a derivation. However, its physical basis is extremely weak, which undermines the premise of the dark energy investigation.
-   **Fix:** While the authors are already transparent, they should further emphasize in the introduction and conclusion that the dark energy part of their analysis is a "no-go" investigation of a phenomenological possibility, and that this possibility itself lacks a firm theoretical foundation. This reframing would place more appropriate weight on the paper's truly solid result, the perturbation-transparency theorem.

#### MINOR

**P1A-m1: Future Date on Manuscript**
-   **Location:** Page 1.
-   **Problem:** The paper is dated "June 28, 2026." This is presumably a placeholder or typo.
-   **Fix:** The date should be corrected to the date of submission or revision.

**P1A-m2: Inconsistent `N_tot` Value**
-   **Location:** Throughout the text.
-   **Problem:** The paper uses `N_tot ≈ 92` throughout the main text (e.g., abstract, Sec. XIV D), but the derivation in Appendix B yields `N_tot ≈ 94`. The appendix explains the `~2%` difference, but for consistency, the authors should choose one value and use it consistently, or present it as a range (e.g., `N_tot = 92-94`).
-   **Fix:** Use a single, consistently derived value for `N_tot` or explicitly state the range and its origin each time. The abstract and conclusions should reflect the value derived in the appendix.

**P1A-m3: Unclear Justification for Matching Factor**
-   **Location:** Sec. II C 1 (p. 9).
-   **Problem:** The justification for the `(T_reh / M_GUT)^(3/2)` factor in the dilution formula (Eq. 11) is described as being based on "dimensional / phase-space grounds" and is admitted to be "dimensional-analysis aesthetic at this level rather than calculated." This is a weak point in the quantitative bookkeeping of the `N_tot` value.
-   **Fix:** The authors should either provide a more solid, albeit schematic, derivation for this factor or explicitly state that the `N_tot` value has an inherent `O(few)` uncertainty due to this and other matching factors. This is a minor point because the paper's main conclusions are robust to this level of uncertainty, but it would improve rigor.

#### NIT

**P1A-N1: Footnote Placement**
-   **Location:** Page 13, footnote 3.
-   **Problem:** Footnote 3, which clarifies the parity of the operator in Eq. (14), is attached to the main text paragraph rather than the equation or operator itself, making it easy to miss.
-   **Fix:** Consider moving the footnote anchor to be directly adjacent to the term `∂_μ D_NY J⁵μ` in the text, or to the equation number (14), for better clarity.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the new findings from the second-pass review.

---
### Additional Findings from Second-Pass Review

**P1A-m4: Unclear Derivation of Forecast Significance Range**
-   **Location:** Footnote 6 (p. 16).
-   **Problem:** The footnote attempts to justify the `2.6-5σ` realistic significance range for the SPHEREx `f_NL` forecast. While the upper end (`~5σ`) is roughly derivable from the numbers given (`f_NL = -35/8 ≈ -4.375`, `σ(f_NL) ≈ 1.0` post-degradation), the origin of the lower end (`2.6σ`) is not explained. The text states that the full multi-tracer forecast is computed in Paper II [2] and that the footnote merely "summarizes that result." This is insufficient for a self-contained argument. The logic connecting the inputs provided in the paper to the full quoted range is opaque.
-   **Fix:** This reinforces the essential finding P1A-E1. The specific numerical range must be removed. The paper should state qualitatively that SPHEREx can test the prediction, and cite the companion paper for the detailed forecast, without quoting the un-derived final numbers.

**P1A-m5: Typo in Cosmological Constant Parameterization**
-   **Location:** Eq (10), page 8.
-   **Problem:** The equation `Λ_eff = Ξ M_Pl⁴ + c_ω ω²` is dimensionally inconsistent. As defined in the surrounding text, `Λ_eff` has units of `[mass]²` (a curvature), while the term `Ξ M_Pl⁴` has units of `[mass]⁴` (an energy density). Based on the text which states `ρ_Λ = Ξ M_Pl⁴` and the standard relation `ρ_Λ ∝ Λ_eff M_Pl²`, the equation should contain `M_Pl²`.
-   **Fix:** Correct the power of `M_Pl` in the first term of Eq (10) from 4 to 2, to read `Λ_eff = Ξ M_Pl² + c_ω ω²`.

**P1A-N2: Inconsistent Terminology for Torsion-Induced Interaction**
-   **Location:** Abstract (p. 1), Sec. IV (p. 11), Sec. IV A (p. 12).
-   **Problem:** The abstract and Sec. IV refer to Route 1 as "NJL contact." Section IV A correctly derives the four-fermion contact term `(ψγ^αγ⁵ψ)²`, which is the Hehl-Datta interaction. While this interaction is structurally similar to the one in the Nambu-Jona-Lasinio (NJL) model, they are not identical and arise in different contexts. Using "NJL" may be confusing to readers familiar with the original NJL model of chiral symmetry breaking in QCD. "Four-fermion contact interaction" or "Hehl-Datta interaction" would be more precise.
-   **Fix:** For clarity and precision, consider replacing "NJL contact" with "Hehl-Datta four-fermion contact" or a similar descriptor throughout the manuscript.