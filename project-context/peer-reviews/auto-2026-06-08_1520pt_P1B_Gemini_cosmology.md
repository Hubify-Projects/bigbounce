# P1B auto-2026-06-08_1520pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3137 chars)
**Wall time**: 132.7s

---

## Referee Report for Manuscript P1B

**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Author:** Houston Golden

This paper presents three technical verification analyses intended as a companion to a primary paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses cover: (1) a stock-CAMB MCMC analysis of the ACDM+ΔNeff model, (2) a validation of a NaMaster pseudo-Cℓ pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model. A fourth analysis of a w₀-wₐ dark energy model is also presented.

The paper is generally transparent about the scope and limitations of its analyses, which is commendable. However, it suffers from several critical issues, including a severe structural problem, a demonstrably incorrect calculation in a key table, and the inclusion of material inappropriate for a peer-reviewed publication. These issues must be fully addressed before the paper can be considered for publication in Physical Review D.

### Summary recommendation
**MAJOR REVISIONS**

The paper contains valuable verification work and is laudably transparent about its limitations. However, the presence of an incorrect statistical calculation, a highly confusing paper structure, and a table that appears to be an internal author checklist are all critical flaws. The paper requires significant restructuring and correction before it can meet the standards of Physical Review D. If the authors can satisfactorily address the essential and major points below, the revised manuscript may be suitable for publication.

---
### Detailed Findings

#### ESSENTIAL Revisions (Paper cannot be accepted without these fixes)

**P1B-E1**
*   **Location:** Page 10, Table III
*   **Problem:** Table III, "Claims classification for this companion paper," is not appropriate for a scientific publication. It appears to be an internal author checklist or project management tool, listing claims and their verification status. This content is unprofessional and has no place in a peer-reviewed article.
*   **Required Fix:** Remove Table III entirely.

**P1B-E2**
*   **Location:** Page 4, Table II, footnote b
*   **Problem:** The calculation of the uncertainty on the pivot equation of state, σ(w_pivot), is incorrect. The provided formula, `σ²_pivot = σ²_w₀ + (1-a_p)²σ²_wₐ`, is wrong as it omits the covariance term. Using the author's own numbers (`a_p = 0.6680`, `σ_w₀ = 0.0436`, `σ_wₐ = 0.1864`) and the definition `a_p = 1 - Cov(w₀,wₐ)/Var(wₐ)`, one can derive the correlation coefficient `ρ`. This derivation leads to a non-physical value `ρ > 1` and a negative variance for `w_pivot`. The entire statistical basis for the quoted `w_pivot = -1.0344 ± 0.0301` is therefore unsound as presented.
*   **Required Fix:** Re-derive and correct the formula, calculation, and all associated numbers in footnote b of Table II. The correct formula for the variance of `w(a_p)` at the pivot scale `a_p` should be used, and all input numbers must be consistent.

**P1B-E3**
*   **Location:** Throughout the paper (Abstract, Introduction, Sec. III, Sec. V)
*   **Problem:** The paper's structure is deeply confusing. The abstract and introduction frame the paper around three specific analyses. However, a fourth, distinct analysis of a `w₀-wₐ` model using DESI DR2 data is presented in detail (Table II, and surrounding text on pages 3, 4, and 6) without any formal introduction. This `w₀-wₐ` analysis yields one of the paper's strongest claimed results (a >4σ departure from ΛCDM), yet its relationship to the other three "verification" tasks is never explained. This makes the paper's narrative disjointed and difficult to follow.
*   **Required Fix:** The paper must be restructured. The `w₀-wₐ` analysis must be either: (a) formally introduced in the abstract and introduction as a fourth, distinct analysis, with its motivation and context clearly explained, or (b) removed if it is not central to the paper's purpose as a "technical verification companion." The current presentation is unacceptable.

**P1B-E4**
*   **Location:** Page 8, Section VII. Conclusions
*   **Problem:** The units for the Hubble constant are written incorrectly. The text reads: "recovers H₀ = 67.68 ± 1.06 km s⁻¹ Mpc⁻¹". The unit `s⁻¹` should apply to `km`, not be a separate term.
*   **Required Fix:** Correct the units to the standard `km s⁻¹ Mpc⁻¹`. Note that the abstract correctly uses `kms⁻¹ Mpc⁻¹`. Ensure consistency.

#### MAJOR Revisions (Significant revision required)

**P1B-M1**
*   **Location:** Page 7 (Sec. VI and footnote 4) and Page 9 (Appendix C and footnote 5)
*   **Problem:** The paper performs a consistency check for a "spectator" ALP, but footnotes 4 and 5 reveal that for the chosen MCMC priors (specifically `θᵢ ∈ [0.5, 2]`), the ALP is generally *not* a spectator. Instead, it is in a regime where its energy density is comparable to the critical density (`Ωₐ ~ 1`), meaning it acts as dark energy. The true spectator regime (`θᵢ << 1`) is shown to require `~25x` fine-tuning. This is a critical physical caveat that significantly weakens the "consistency check" interpretation, yet it is relegated to footnotes.
*   **Required Fix:** This point must be brought into the main body of Section VI. The text should clearly state that the MCMC analysis primarily explores a dark-energy ALP parameter space and that accommodating the observed birefringence with a true spectator ALP requires significant fine-tuning. The current presentation buries a crucial weakness of the model interpretation.

**P1B-M2**
*   **Location:** Page 5, Figure 1 and caption
*   **Problem:** The caption for Figure 1 states it shows "119,617 post-burnin samples, getdist-thinned from 176,240 raw". However, footnote 1 on page 2 calculates the post-burn-in sample count for this chain as `176,240 * 0.7 ≈ 123,368`. The discrepancy is attributed in the text to "additional getdist effective-sample weight-based thinning," which is opaque jargon to a general reader. A figure caption should be clear and self-contained.
*   **Required Fix:** Clarify the caption of Figure 1. State the full post-burn-in sample count (`~123k`) and then explain that the plot shows a thinned subset of `119,617` samples for visual clarity. Avoid unexplained jargon.

#### MINOR Revisions (Address but paper can proceed)

**P1B-m1**
*   **Location:** Page 8, Acknowledgments
*   **Problem:** The paper acknowledges "Claude (Anthropic) as an AI research assistant". While transparency is good, the use and acknowledgment of AI tools in scientific papers is a developing area with varying journal policies.
*   **Required Fix:** The author should confirm that this form of acknowledgment is compliant with the current editorial policies of Physical Review D. This is a note for the author and editor to consider.

**P1B-m2**
*   **Location:** Page 10, Reference [20]
*   **Problem:** The citation for the Cobaya paper is formatted redundantly: "Journal of Cosmology and Astroparticle Physics 05 (057), 057".
*   **Required Fix:** Correct the citation to the standard format, e.g., "J. Cosmol. Astropart. Phys. 05 (2021) 057".

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second, more rigorous review of the paper.

================================================================
## Referee Report for Manuscript P1B (Second Pass)

This second review re-examines the manuscript with a focus on numerical, logical, and structural consistency, following up on the initial report. Several new critical issues have been identified, reinforcing the initial recommendation for **MAJOR REVISIONS**.

---
### NEW Findings from Second Review

#### ESSENTIAL Revisions (Paper cannot be accepted without these fixes)

**P1B-E5**
*   **Location:** Page 3 (text) and Page 4 (Table II)
*   **Problem:** The uncertainty reported for the sum of the dark energy equation of state parameters, `w₀ + wₐ = -1.4788 ± 0.1485`, is arithmetically inconsistent with the other reported parameter constraints and covariance information. Using the provided values for `σ(w₀)`, `σ(wₐ)`, and the pivot scale `a_p` (which implies the covariance), standard error propagation yields a much larger uncertainty of `σ(w₀+wₐ) ≈ 0.24`. Furthermore, deriving the correlation coefficient `ρ` from the given numbers results in a non-physical value `ρ > 1`. This indicates a fundamental inconsistency in the MCMC posterior analysis or its reporting, invalidating the claimed statistical significance of the `w₀+wₐ` result. This issue compounds the error identified in the initial review (P1B-E2) regarding `σ(w_pivot)`.
*   **Required Fix:** The author must find and correct the source of this numerical inconsistency. This likely requires re-analyzing the MCMC chain's covariance matrix for the `(w₀, wₐ)` parameters and correcting all derived quantities, including `σ(w₀+wₐ)`, `σ(w_pivot)`, and the associated marginal tail departures.

#### MAJOR Revisions (Significant revision required)

**P1B-M3**
*   **Location:** Abstract vs. Page 7 (Section VI)
*   **Problem:** The abstract is significantly more transparent about the fine-tuning required for the spectator-ALP model than the main body of the paper. The abstract contains a clear and prominent "Spectator-status caveat," correctly noting that the spectator interpretation requires `θᵢ << 1`, which constitutes significant fine-tuning. However, the main analysis in Section VI proceeds with MCMC priors that violate this condition and relegates this critical weakness to a footnote (fn. 4). The main text should not be less transparent than the abstract.
*   **Required Fix:** Elevate the discussion of the spectator-status caveat and the associated `~25x` fine-tuning from footnote 4 into the main body of Section VI. The analysis should be framed with this important context up front, making it clear to the reader that the "consistency" comes at the cost of significant fine-tuning if the ALP is to be a true spectator.

#### Notes (Minor points for author's attention)

**P1B-N1**
*   **Location:** Page 1, under the author's name.
*   **Problem:** The date of the manuscript is listed as "(Dated: 2026-06-08 PDT)", which is a future date.
*   **Required Fix:** Correct the date to the actual submission date.
================================================================