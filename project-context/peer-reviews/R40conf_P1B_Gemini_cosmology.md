# P1B R40conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1b_mcmc_companion.pdf` md5=62374add pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (13437 chars)
**Wall time**: 160.7s

---

**Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program**

This paper presents three technical analyses intended to support a larger program on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ACDM+Neff model as a null test; (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

While the analyses are detailed and the authors demonstrate a high degree of transparency regarding their methods and data, the paper in its current form has several issues that prevent it from being acceptable for publication in Physical Review D. The most critical issues are its failure to function as a self-contained scientific article and a potential sign error in the core formula for the birefringence analysis. Significant restructuring and revision are required.

---
### ESSENTIAL

**P1B-E1**
*   **Section:** Entire paper, especially Sec. I (p. 2)
*   **Problem:** The paper is explicitly framed as a "technical verification companion" to another paper, "Paper I(a)" [1], which is cited as an un-refereed, concurrent arXiv submission. The entire motivation and context for the work presented (e.g., the "ECH structural-closure no-go result") are imported from this external, un-refereed source. A paper published in PRD must be a self-contained contribution to the scientific literature. It cannot be structured as an appendix to a preprint. This violates the core principle of a standalone scientific paper.
*   **Required Fix:** The paper must be rewritten to be self-contained. The authors must provide sufficient background and motivation from the ECH framework to allow a reader to understand the purpose and significance of the three analyses without referring to Paper I(a). This will likely require adding a concise but complete theory background section and reframing the introduction and conclusions. Alternatively, the content should be merged as an appendix into Paper I(a) if that paper is submitted for publication.

**P1B-E2**
*   **Section:** IV (p. 7)
*   **Problem:** The estimator for the cosmic birefringence angle β is based on a template fit to the `CEB` spectrum. The paper states the template is proportional to `sin(2β)cos(2β)CEE`, which is `(1/2)sin(4β)CEE`. However, the standard theoretical prediction for birefringence from a primordial E-mode only sky is `C_l^{EB} = -(1/2)sin(4β)C_l^{EE}`. The formula and implementation used in the paper appear to have a sign error relative to the standard convention in the literature.
*   **Required Fix:** The authors must rigorously verify the sign in their formula (Eq. 1 and its implementation) against first-principles derivation and standard literature (e.g., Lue, Wang, Kamionkowski 1999; Komatsu et al. 2009). If their convention differs, it must be explicitly derived, justified, and its impact on the recovered β must be stated. A simple sign flip in β would result from this, but for a methods paper, the correctness of the core formula is paramount.

---
### MAJOR

**P1B-M1**
*   **Section:** Entire paper
*   **Problem:** At 21 pages, the paper is excessively long for its stated contribution of documenting three verification analyses. The structure combines three distinct, loosely connected topics, making the paper unfocused. The level of detail, while commendable for its transparency, is often overwhelming for the main text (e.g., the extended discussion of the NaMaster robustness battery in Sec. IV, the MCMC sample-count reconciliation in footnote 1).
*   **Required Fix:** The paper must be significantly condensed and restructured. The three analyses could be presented more concisely, with lengthy technical verifications (like the robustness battery details) moved to an appendix within this paper. The authors should aim for a total length of 10-12 pages, which is more appropriate for the scope of the work. The paper should be reframed as a standalone methods paper, not a "companion".

**P1B-M2**
*   **Section:** Multiple (e.g., Sec. VI, p. 10, p. 12)
*   **Problem:** The paper contains several uncomputed quantitative claims, relying on qualitative descriptors where precise numbers are required for a rigorous physics paper.
    *   p. 10, fn. 5: "a quintom late-time wowa background ... shifts H(z) at z≤1 by ~few percent". This must be quantified. What is the maximum percentage shift for the posterior-mean `wowa` parameters?
    *   p. 12: "pushes the required enhancement well above standard KSVZ/DFSZ O(1) benchmarks". The text later implies factors of ~9-160. This should be stated clearly upfront when the claim is first made.
    *   p. 12: The terms "modest photon-coupling enhancement" and "substantial UV-completion enhancement" are subjective. Provide quantitative ranges for what the authors consider "modest" and "substantial" in this context.
*   **Required Fix:** Replace all qualitative descriptors of quantitative effects with precise numbers, ranges, or order-of-magnitude estimates. Every claim of "small," "large," "negligible," or "substantial" must be backed by a calculation or a specific numerical threshold.

**P1B-M3**
*   **Section:** References (p. 2, p. 17)
*   **Problem:** Citations [1], [6], [7], and [8] are to "companion paper, posted concurrently on arXiv". For a manuscript under review for publication, load-bearing citations must point to peer-reviewed articles or stable, public preprints with fixed identifiers (e.g., arXiv IDs). Relying on placeholder citations for core context is not acceptable.
*   **Required Fix:** Before publication, all citations must be updated to point to either published articles or permanent, citable preprint records. This is directly related to P1B-E1; the paper cannot be properly reviewed or understood with these unresolved dependencies.

---
### MINOR

**P1B-m1**
*   **Section:** IV (p. 8)
*   **Problem:** The text states: "The estimator is not unbiased in the standard statistical sense; the 0.040° is the observed pipeline bias on the multiplicative bias, not a bound on random scatter." This phrasing is confusing. A bias is typically an additive or multiplicative offset of the mean of an estimator. The term "bias on the multiplicative bias" is unclear.
*   **Required Fix:** Rephrase for clarity. For example: "The estimator exhibits a multiplicative bias, under-recovering the injected angle by ~12%. The reported pipeline bias, `Δβ = β_rec - β_inj`, reaches a worst-case value of -0.040°, which represents a systematic offset of the estimator, not a statistical uncertainty."

**P1B-m2**
*   **Section:** Multiple
*   **Problem:** The text contains internal project jargon and versioning information not suitable for a formal publication.
    *   p. 8: "mirroring the executed pod run". "Pod run" is internal jargon.
    *   p. 15: "in-tex v1B.0.69 stamp". This is an internal version tag.
*   **Required Fix:** Replace jargon with standard scientific terminology (e.g., "computational run"). Remove internal versioning stamps from the manuscript body. The commit hash provided in the reproducibility section is the correct way to version-stamp the work.

**P1B-m3**
*   **Section:** IV (p. 7, Fig. 3)
*   **Problem:** In Figure 3b, the data point for the canonical `fsky = 0.32` is plotted without an error bar for `σβ`, with the caption explaining it was not recorded and a rerun was necessary to measure it. While the transparency is good, plotting a point without its associated uncertainty in a plot that otherwise shows uncertainties is poor practice.
*   **Required Fix:** Update the plot to show the `fsky = 0.32` point with the error bar (`σβ = 0.046°`) measured in the dedicated rerun mentioned in the caption. This will make the figure consistent and easier to interpret.

**P1B-m4**
*   **Section:** References (p. 17-18)
*   **Problem:** Several references list future publication years (e.g., 2025).
    *   Ref [4]: `arXiv preprint (2025)`
    *   Ref [14]: `Astrophys. J. Lett. 973, L14 (2024)` (The date is June 2026, so this is in the past, but many others are future)
    *   Ref [16]: `Mon. Not. Roy. Astron. Soc. 541, 2585 (2025)`
    *   Ref [18]: `European Physical Journal C (2025)`
    *   Ref [19]: `Physical Review D 112, 083515 (2025)`
*   **Required Fix:** All publication dates must be corrected to their actual values. If a paper is not yet published, it should be cited as a preprint with the correct submission year.

---
### NIT

**P1B-N1**
*   **Section:** I (p. 1)
*   **Problem:** The date of the paper is given as a future date: "June 13, 2026".
*   **Required Fix:** Replace with the actual date of submission.

**P1B-N2**
*   **Section:** V (p. 9)
*   **Problem:** The text states that the `wowa` chain uses `planck_2020_lollipop.lowlE`. This seems to be a typo or a non-standard likelihood name. The standard Planck 2018 low-E likelihood is `planck_2018_lowl.EE`.
*   **Required Fix:** Please verify and correct the name of the Planck likelihood used. If it is a non-standard or modified likelihood, this should be explicitly stated and justified.

**P1B-N3**
*   **Section:** VI (p. 11)
*   **Problem:** The text states: "the direct-sample priors are on the underlying ALP parameters (θi, ma), not on Δφ/fa, which is a derived quantity along each ALP trajectory." This sentence is slightly confusing.
*   **Required Fix:** Suggest rephrasing for clarity: "The MCMC samples the fundamental ALP parameters (θi, ma) from their prior distributions. The field displacement Δφ/fa is a derived quantity, calculated for each sample along its corresponding trajectory, and does not have a prior directly imposed on it."

**P1B-N4**
*   **Section:** Table I (p. 19)
*   **Problem:** The S8 tension is described in the table caption. The calculation `0.827±0.010 ⊕ 0.776±0.017 = 0.814±0.009` is a combination, not a tension. The tension is the difference divided by the combined error.
*   **Required Fix:** Rephrase for clarity. State the difference between the central values, the combined uncertainty, and the resulting significance in σ. For example: "The Planck+BAO+SN marginal (0.827±0.010) is in 2.6σ tension with the DES-Y3 prior (0.776±0.017)."

---
## Summary recommendation
**MAJOR REVISIONS**

This paper presents a set of detailed and transparently documented technical analyses. The authors have clearly put significant effort into validating their pipelines and exploring model parameter spaces. However, the manuscript is not acceptable for publication in its current form. The critical flaw is its structure as a "companion paper," which renders it not self-contained and reliant on an un-refereed preprint for its entire motivation. Furthermore, a potential sign error in the core birefringence formula must be addressed. If the authors can successfully restructure the paper to be a standalone contribution, condense its length, and rigorously verify their theoretical formulas, it may become a valuable contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating findings from the second, more rigorous review.

================================================================
**Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program**

This paper presents three technical analyses intended to support a larger program on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ACDM+Neff model as a null test; (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

While the analyses are detailed and the authors demonstrate a high degree of transparency regarding their methods and data, the paper in its current form has several critical issues that prevent it from being acceptable for publication in Physical Review D. The most critical issues are its failure to function as a self-contained scientific article, a potential sign error and an ambiguous parameter definition in the core birefringence analysis, and the use of a mixed-release likelihood stack with unquantified systematic effects. Significant restructuring and revision are required.

---
### ESSENTIAL

**P1B-E1**
*   **Section:** Entire paper, especially Sec. I (p. 2)
*   **Problem:** The paper is explicitly framed as a "technical verification companion" to another paper, "Paper I(a)" [1], which is cited as an un-refereed, concurrent arXiv submission. The entire motivation and context for the work presented (e.g., the "ECH structural-closure no-go result") are imported from this external, un-refereed source. A paper published in PRD must be a self-contained contribution to the scientific literature. It cannot be structured as an appendix to a preprint. This violates the core principle of a standalone scientific paper.
*   **Required Fix:** The paper must be rewritten to be self-contained. The authors must provide sufficient background and motivation from the ECH framework to allow a reader to understand the purpose and significance of the three analyses without referring to Paper I(a). This will likely require adding a concise but complete theory background section and reframing the introduction and conclusions. Alternatively, the content should be merged as an appendix into Paper I(a) if that paper is submitted for publication.

**P1B-E2**
*   **Section:** IV (p. 7, Eq. 1)
*   **Problem:** The estimator for the cosmic birefringence angle β is based on a template fit to the `CEB` spectrum. The paper states the template is proportional to `sin(2β)cos(2β)CEE`, which is `(1/2)sin(4β)CEE`. However, the standard theoretical prediction for birefringence from a primordial E-mode only sky is `C_l^{EB} = -(1/2)sin(4β)C_l^{EE}`. The formula and implementation used in the paper appear to have a sign error relative to the standard convention in the literature.
*   **Required Fix:** The authors must rigorously verify the sign in their formula (Eq. 1 and its implementation) against first-principles derivation and standard literature (e.g., Lue, Wang, Kamionkowski 1999; Komatsu et al. 2009). If their convention differs, it must be explicitly derived, justified, and its impact on the recovered β must be stated. A simple sign flip in β would result from this, but for a methods paper, the correctness of the core formula is paramount.

**P1B-E3**
*   **Section:** VI (p. 11, Eq. 4 and surrounding text)
*   **Problem:** The birefringence angle `β` is calculated using `β = (g_aγ / 2) Δφ`, where `g_aγ` is the photon-axion coupling. The standard normalization is `g_aγ = C_aγ α_EM / (π f_a)`, leading to `β = (C_aγ α_EM / (2π f_a)) Δφ`. The paper's formula is `β ≈ (α_EM / 4π) * Cay * (Δφ/fa)`. This implies the paper's `Cay` is equivalent to `2 * C_aγ`, where `C_aγ` is the coefficient used in standard benchmarks (e.g., KSVZ/DFSZ). This non-standard definition of the coupling constant `Cay` is confusing and not explicitly stated. The subsequent comparison of the required `Cay` to `O(1)` benchmarks is therefore ambiguous.
*   **Required Fix:** The authors must provide the explicit Lagrangian they are using and clearly define their parameter `Cay` in terms of the standard photon-axion coupling constant `g_aγ` or `C_aγ`. They must then re-evaluate their comparison to standard model benchmarks (KSVZ/DFSZ) using a consistent definition.

---
### MAJOR

**P1B-M1**
*   **Section:** Entire paper
*   **Problem:** At 21 pages, the paper is excessively long for its stated contribution of documenting three verification analyses. The structure combines three distinct, loosely connected topics, making the paper unfocused. The level of detail, while commendable for its transparency, is often overwhelming for the main text (e.g., the extended discussion of the NaMaster robustness battery in Sec. IV, the MCMC sample-count reconciliation in footnote 1).
*   **Required Fix:** The paper must be significantly condensed and restructured. The three analyses could be presented more concisely, with lengthy technical verifications (like the robustness battery details) moved to an appendix within this paper. The authors should aim for a total length of 10-12 pages, which is more appropriate for the scope of the work. The paper should be reframed as a standalone methods paper, not a "companion".

**P1B-M2**
*   **Section:** Multiple (e.g., Sec. VI, p. 10, p. 12)
*   **Problem:** The paper contains several uncomputed quantitative claims, relying on qualitative descriptors where precise numbers are required for a rigorous physics paper.
    *   p. 10, fn. 5: "a quintom late-time wowa background ... shifts H(z) at z≤1 by ~few percent". This must be quantified. What is the maximum percentage shift for the posterior-mean `wowa` parameters?
    *   p. 12: "pushes the required enhancement well above standard KSVZ/DFSZ O(1) benchmarks". The text later implies factors of ~9-160. This should be stated clearly upfront when the claim is first made.
    *   p. 12: The terms "modest photon-coupling enhancement" and "substantial UV-completion enhancement" are subjective. Provide quantitative ranges for what the authors consider "modest" and "substantial" in this context.
*   **Required Fix:** Replace all qualitative descriptors of quantitative effects with precise numbers, ranges, or order-of-magnitude estimates. Every claim of "small," "large," "negligible," or "substantial" must be backed by a calculation or a specific numerical threshold.

**P1B-M3**
*   **Section:** References (p. 2, p. 17)
*   **Problem:** Citations [1], [6], [7], and [8] are to "companion paper, posted concurrently on arXiv". For a manuscript under review for publication, load-bearing citations must point to peer-reviewed articles or stable, public preprints with fixed identifiers (e.g., arXiv IDs). Relying on placeholder citations for core context is not acceptable.
*   **Required Fix:** Before publication, all citations must be updated to point to either published articles or permanent, citable preprint records. This is directly related to P1B-E1; the paper cannot be properly reviewed or understood with these unresolved dependencies.

**P1B-M4**
*   **Section:** III (p. 3, footnote 1) and V.A (p. 9)
*   **Problem:** The paper uses a mixed-release likelihood stack: Planck NPIPE (PR4) for high-l TTTEEE, but Planck 2018 (PR3) for low-l and lensing. The paper acknowledges this limitation: "any pairing-induced bias on the headline ΔNeff/H0/S8 at the quoted precision is therefore unquantified here". This is a significant systematic uncertainty that is left unquantified for a precision cosmology analysis. Stating this in a footnote and parenthetically is insufficient for a potential systematic that could be comparable to the statistical uncertainty on `ΔNeff`.
*   **Required Fix:** The authors must either run a control chain with a consistent likelihood stack (e.g., all PR3 or all PR4, if available) to quantify the bias, or they must add a systematic error budget to their final parameter constraints. The limitation must be made prominent in the abstract and conclusions, not just in footnotes.

---
### MINOR

**P1B-m1**
*   **Section:** IV (p. 8)
*   **Problem:** The text states: "The estimator is not unbiased in the standard statistical sense; the 0.040° is the observed pipeline bias on the multiplicative bias, not a bound on random scatter." This phrasing is confusing.
*   **Required Fix:** Rephrase for clarity. For example: "The estimator exhibits a multiplicative bias, under-recovering the injected angle by ~12%. The reported pipeline bias, `Δβ = β_rec - β_inj`, reaches a worst-case value of -0.040°, which represents a systematic offset of the estimator, not a statistical uncertainty."

**P1B-m2**
*   **Section:** Multiple
*   **Problem:** The text contains internal project jargon and versioning information not suitable for a formal publication (e.g., "pod run", "in-tex v1B.0.69 stamp").
*   **Required Fix:** Replace jargon with standard scientific terminology (e.g., "computational run"). Remove internal versioning stamps from the manuscript body. The commit hash provided in the reproducibility section is the correct way to version-stamp the work.

**P1B-m3**
*   **Section:** IV (p. 7, Fig. 3)
*   **Problem:** In Figure 3b, the data point for the canonical `fsky = 0.32` is plotted without an error bar for `σβ`, with the caption explaining it was not recorded. This is poor practice.
*   **Required Fix:** Update the plot to show the `fsky = 0.32` point with the error bar (`σβ = 0.046°`) measured in the dedicated rerun mentioned in the caption.

**P1B-m4**
*   **Section:** References (p. 17-18)
*   **Problem:** Several references list future publication years (e.g., 2025).
*   **Required Fix:** All publication dates must be corrected to their actual values. If a paper is not yet published, it should be cited as a preprint with the correct submission year.

**P1B-m5**
*   **Section:** IV (p. 7)
*   **Problem:** The noise model for the NaMaster validation uses "10 μK arcmin white noise" and is described as "ACT-like". This is a significant simplification, as real experimental noise is non-uniform and non-white.
*   **Required Fix:** The authors should briefly acknowledge this simplification and its potential impact on the validation results (e.g., regarding E-B mixing from non-uniform noise).

---
### NIT

**P1B-N1**
*   **Section:** I (p. 1)
*   **Problem:** The date of the paper is given as a future date: "June 13, 2026".
*   **Required Fix:** Replace with the actual date of submission.

**P1B-N2**
*   **Section:** V.C (p. 10) and IX (p. 9)
*   **Problem:** The text on p. 9 mentions `planck_2020_lollipop.lowlE`. This appears to be a non-standard likelihood name.
*   **Required Fix:** Please verify and correct the name of the Planck likelihood used. If it is a non-standard or modified likelihood, this should be explicitly stated and justified.

**P1B-N3**
*   **Section:** VI (p. 11)
*   **Problem:** The sentence "the direct-sample priors are on the underlying ALP parameters (θi, ma), not on Δφ/fa, which is a derived quantity along each ALP trajectory" is slightly confusing.
*   **Required Fix:** Suggest rephrasing for clarity: "The MCMC samples the fundamental ALP parameters (θi, ma) from their prior distributions. The field displacement Δφ/fa is a derived quantity, calculated for each sample, and does not have a prior directly imposed on it."

**P1B-N4**
*   **Section:** Table I (p. 19)
*   **Problem:** The S8 tension is described in the table caption. The calculation `0.827±0.010 ⊕ 0.776±0.017 = 0.814±0.009` is a combination, not a tension.
*   **Required Fix:** Rephrase for clarity. State the difference between the central values, the combined uncertainty, and the resulting significance in σ. For example: "The Planck+BAO+SN marginal (0.827±0.010) is in 2.6σ tension with the DES-Y3 prior (0.776±0.017)."

**P1B-N5**
*   **Section:** Table I (p. 19, caption)
*   **Problem:** The caption states: "S8 = σε (Ωm/0.3)^1/2". The parameter is `σ8`, not `σε`. This is a typo.
*   **Required Fix:** Change `σε` to `σ8` in the caption of Table I.

**P1B-N6**
*   **Section:** IV (p. 4, Caveat (b))
*   **Problem:** The text states "the chain has 7 free with the standard low-l data constraint". It is unclear which 7 parameters are free in the `wowa` analysis.
*   **Required Fix:** Clarify which parameters are being sampled. For a `w0waCDM` model, one would expect 8 cosmological parameters. Please list them.

---
## Summary recommendation
**MAJOR REVISIONS**

This paper presents a set of detailed and transparently documented technical analyses. The authors have clearly put significant effort into validating their pipelines and exploring model parameter spaces. However, the manuscript is not acceptable for publication in its current form. The critical flaws are its structure as a "companion paper," which renders it not self-contained; a potential sign error and ambiguous parameter definition in the birefringence analysis; and the use of a mixed-release likelihood stack with unquantified systematics. If the authors can successfully restructure the paper to be a standalone contribution, condense its length, and rigorously verify their theoretical formulas and analysis choices, it may become a valuable contribution to the literature.