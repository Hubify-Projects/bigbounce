# P1B auto-2026-06-09_1042pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (5102 chars)
**Wall time**: 153.9s

---

# Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

## Summary of the Paper
This manuscript presents three technical verification analyses intended to support a separate, primary paper on Einstein-Cartan-Holst (ECH) cosmology. The three documented analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model, serving as a null test for an extra radiation component; (2) a Monte Carlo validation of a NaMaster-based pseudo-Cℓ pipeline for measuring cosmic birefringence, confirming the pipeline's ability to recover an injected signal; and (3) a consistency check showing that a standard spectator axion-like particle (ALP) model can accommodate the currently observed birefringence signal. The paper is commendably transparent about the scope and limitations of each analysis, emphasizing what is *not* being claimed (e.g., no direct test of ECH theory, no new sky measurement of birefringence).

## General Assessment
The manuscript provides a useful set of technical validations. The authors have made a laudable effort to ensure reproducibility by providing code and clearly delineating the scope of their work. The disclosures regarding pipeline limitations, model fine-tuning, and the distinction between different types of signal-to-noise ratios are excellent examples of good scientific practice.

However, the paper suffers from several significant structural and technical issues that must be addressed before it can be considered for publication in Physical Review D. These include the introduction of a major, un-scaffolded analysis, a non-standard and inappropriate table, and errors in the presentation of key equations and statistical derivations.

## Detailed Findings

### ESSENTIAL Revisions

**P1B-E1: Un-scaffolded `w0wa` Analysis**
- **Location:** Section III (p. 3) and Table II (p. 4).
- **Problem:** The abstract, title, and introduction frame the paper around three specific analyses: a ΛCDM+ΔNeff proxy, a NaMaster pipeline validation, and a spectator-ALP consistency check. However, the paper presents a fourth, major analysis of a `w0wa` dark energy model, which finds a >4σ departure from ΛCDM for `w0`. This is a significant cosmological result in its own right, but it is not introduced or contextualized within the paper's stated structure. It appears abruptly in the "Physics interpretation" subsection of the ΔNeff analysis, creating significant structural confusion.
- **Required Fix:** The `w0wa` analysis and its discussion (including Table II) must be removed from this manuscript. It is sufficiently distinct and significant to warrant its own publication where it can be properly introduced, analyzed, and discussed. This companion paper should remain focused on the three technical verifications outlined in the abstract.

**P1B-E2: Inappropriate "Claims Classification" Table**
- **Location:** Table III, Page 10.
- **Problem:** This table, which classifies the paper's own claims as "Verified," "Omitted," "Cited," etc., is highly unconventional for a formal scientific publication. It reads like an internal author checklist or a project management tool. It does not add scientific value for the reader and undermines the professional tone of the manuscript.
- **Required Fix:** Table III must be removed entirely. The status of each result should be clear from the main text.

### MAJOR Revisions

**P1B-M1: Incorrect Birefringence Formula Presentation**
- **Location:** Section VI, Equation (3), Page 7.
- **Problem:** The equation for the birefringence value `β` contains a likely typo, `O_EM`, where `α_EM` (the fine-structure constant) is presumably intended. More importantly, the equation as written, `β ≈ O_EM x 8 / 4π × 1.07`, is dimensionally and physically ambiguous. The standard formula is `β = (C_aγγ * α_EM / (4π)) * (Δφ/fa)`. The text seems to use this formula in its numerical calculation, but the equation itself is not written correctly.
- **Required Fix:** Correct the typo to `α_EM`. Write the equation in its full, unambiguous form, clearly defining all terms (e.g., `C_αγ`, `Δφ/fa`). For example: `β = (C_αγ * α_EM / (4π)) * (Δφ/fa)`.

**P1B-M2: Confused Statistical Explanation in Table II Footnote**
- **Location:** Table II, footnote `b`, Page 4.
- **Problem:** The explanation for the pivot equation of state `w_pivot` and its variance is incorrect. The formula provided for the variance, `σ^2_{pivot} = σ^2_{w0} + (1-ap)^2 σ^2_{wa}`, is wrong as it omits the crucial covariance term. The definition of `a_p` and its relation to the decorrelation of parameters is also non-standard and confusingly explained. The subsequent calculation appears to be an attempt to justify the quoted error on `w_pivot` but fails. This demonstrates a lack of care in presenting statistical results.
- **Required Fix:** This finding is tied to P1B-E1. If the `w0wa` analysis is removed as required, this issue becomes moot. If the authors were to retain it against advice, this entire footnote would need to be rewritten with a correct and standard derivation for `w_pivot` and its uncertainty, or the derivation should be removed, simply stating the result from the MCMC analysis.

### MINOR Revisions

**P1B-m1: Redundant Citation Formatting**
- **Location:** Bibliography, e.g., Reference [20], Page 11.
- **Problem:** The citation for the Cobaya paper reads "Journal of Cosmology and Astroparticle Physics 05 (057), 057". The issue number and article number are repeated.
- **Required Fix:** Correct the formatting to the standard JCAP style, e.g., "JCAP 05 (2021) 057". Review other citations for similar formatting issues.

**P1B-m2: Redundancy in Backreaction Disclosure**
- **Location:** Footnote 5 (p. 7) and Footnote 6 (p. 10).
- **Problem:** The important disclosure about the fine-tuning required for the ALP to remain a spectator is made in detail in footnote 5 and then repeated in footnote 6. While the point is important, the repetition is unnecessary.
- **Required Fix:** Consolidate the disclosure into a single, comprehensive footnote (preferably footnote 5, where the topic is first introduced) and remove the other to improve readability.

### NIT (Cosmetic)

**P1B-N1: Awkward Phrasing in Abstract**
- **Location:** Abstract, Page 1.
- **Problem:** The phrase "pipeline-recovery bias 0.032°" is slightly awkward.
- **Required Fix:** Suggest rephrasing to "with a pipeline-recovery bias of 0.032°" or similar.

---

## Summary recommendation

**MAJOR REVISIONS**

This manuscript has the foundation of a solid technical note that would be a valuable companion to the authors' main work. The commitment to transparency and reproducibility is commendable. However, the paper in its current form is not acceptable for publication. The inclusion of a major, un-contextualized `w0wa` analysis fundamentally breaks the paper's structure and focus. This, along with the inappropriate "claims" table and technical errors in key equations and statistical descriptions, requires a significant overhaul.

If the authors remove the `w0wa` analysis and Table III, and correct the other identified issues, the resulting focused manuscript would be a much stronger and more appropriate contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report with new findings from a more rigorous, second-pass review.

================================================================
# Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..." (Second Pass)

This report supplements my initial review. After a more detailed re-examination of the manuscript, several additional issues have been identified. The initial recommendations, particularly the essential revisions **P1B-E1** (removal of the `w0wa` analysis) and **P1B-E2** (removal of Table III), remain the highest priority. The new findings below further underscore the need for careful revision.

### NEW FINDINGS (Second Pass)

### MAJOR Revisions

**P1B-M3: Ambiguous Role and Impact of the DES Y3 S8 Prior**
- **Location:** Section V.A (p. 6) and Table I (p. 3).
- **Problem:** The text states that the "full-tension" dataset combination includes a DES Y3 `S8` prior (`S8 = 0.776 ± 0.017`). However, the resulting posterior in Table I is `S8 = 0.814 ± 0.008`. This posterior is significantly shifted away from the DES prior and has a much smaller uncertainty, indicating it is overwhelmingly dominated by the Planck data. While this is a known tension between the datasets, the manuscript fails to comment on it. Including a dataset in the analysis which is in significant tension with the result, without any discussion, is potentially misleading.
- **Required Fix:** The authors must add a brief discussion clarifying the inclusion of the DES Y3 `S8` data. They should explicitly state that the final posterior is dominated by Planck's constraining power and note the tension with the DES Y3 value. This provides necessary context for the "full-tension" results.

**P1B-M4: Misleading Phrasing of the `w0wa` Result**
- **Location:** Section III, "Physics interpretation" (p. 3).
- **Problem:** The main text claims the `w0wa` posterior "disfavors" the ΛCDM point, which implies a statistically significant exclusion. However, footnote `a` of Table II correctly and carefully clarifies that the quoted >4σ value is merely a "posterior-tail extrapolation distance" and "not a frequentist tension." The strong language in the main body of the text is not supported by the author's own more rigorous explanation in the footnote.
- **Required Fix:** This is contingent on addressing **P1B-E1**. If the `w0wa` analysis is removed, this point is moot. If it is retained against advice, the language in the main text must be softened to match the careful, qualified explanation provided in the footnote. For example, instead of "disfavors," use language like "is centered at a >4σ extrapolation distance from the ΛCDM point."

### MINOR Revisions

**P1B-m3: Inconsistent Terminology for Planck Data Releases**
- **Location:** Throughout the manuscript (e.g., footnote `a` on p. 1, Table II caption on p. 4).
- **Problem:** The manuscript uses inconsistent and sometimes ambiguous terms for the Planck data, mixing "Planck 2018" (which refers to the PR3 data release), "NPIPE" (the PR4 data release), and "Planck PR4". For maximum clarity and reproducibility, the exact data source and likelihood version should be specified consistently.
- **Required Fix:** Choose a single, precise descriptor for the Planck data and likelihoods used (e.g., "Planck 2018 likelihoods with NPIPE maps") and apply it consistently throughout the paper.

**P1B-m4: Potentially Misleading SNR Comparison**
- **Location:** Footnote 3, Page 6.
- **Problem:** The footnote compares the per-realization signal-to-noise ratio (`SNR_real`) from the Monte Carlo simulations to the measured SNR from the actual Planck NPIPE sky measurement. While the arithmetic is correct, the comparison is not strictly apples-to-apples. The simulated `SNR_real` is derived from an idealized case where the only error source is the injected instrumental noise, whereas the real-sky measurement's error budget includes complex systematics and foreground residuals.
- **Required Fix:** Add a clarifying clause to the footnote to explicitly state that the `SNR_real` represents an idealized case and that the real-sky SNR is subject to additional uncertainties not modeled in the simulation. This prevents any potential misinterpretation of the comparison.

### NIT (Cosmetic)

**P1B-N2: Future Date on Manuscript**
- **Location:** Page 1.
- **Problem:** The manuscript is dated "2026-06-08 PDT," which is in the future.
- **Required Fix:** Correct the date to the actual date of submission.

---
## Summary Recommendation (Unchanged)

**MAJOR REVISIONS**

The new findings reinforce the initial assessment. The manuscript contains valuable technical work and demonstrates a high degree of transparency. However, it requires significant structural and technical revisions to meet the standards of PRD. The removal of the out-of-scope `w0wa` analysis and the inappropriate "claims" table remains paramount. Addressing the additional major and minor points detailed in both reports will be necessary to produce a focused, clear, and technically sound manuscript suitable for publication.