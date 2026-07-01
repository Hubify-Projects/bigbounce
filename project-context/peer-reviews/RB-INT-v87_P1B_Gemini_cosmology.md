# P1B RB-INT-v87 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=ce73d67c pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 169.6s

---

# Referee Report

**Paper ID:** [Assigned by Editor]
**Paper Title:** Technical Reproducibility and Consistency-Check Companion to the ECH Spin-Torsion Program: ACDM+ Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Author:** Houston Golden

This paper presents three numerical analyses that serve as technical cross-checks for a companion paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses consist of: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model to test for an extra radiation-like degree of freedom; (2) a Monte Carlo validation of a NaMaster-based pseudo-C_l pipeline for measuring cosmic birefringence; and (3) a consistency check accommodating the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper's primary strength is its exceptional rigor in both its methodology and its reporting. The authors are commendably transparent about the scope and limitations of their work. It is made explicitly clear from the abstract onwards that these analyses are null-consistency checks and reproducibility notes, not independent verifications or confirmations of the ECH theory itself. The distinction between pipeline validation figures and sky-detection significance is handled with exemplary care. The reproducibility materials are thorough and appear to be of high quality.

The analyses themselves are sound. The ΛCDM+ΔNeff MCMC analysis is standard and correctly finds no evidence for ΔNeff, concluding that this simple extension does not resolve the Hubble tension. The NaMaster pipeline validation is a valuable piece of work, systematically identifying and attributing the sources of bias in the recovery pipeline. The spectator-ALP analysis correctly frames the result not as a discovery, but as an "accommodation" that requires moving to a non-minimal and fine-tuned region of the model's parameter space, a crucial caveat that is clearly articulated.

Overall, the paper is a model of careful, rigorous, and honest scientific reporting. It provides a valuable and solid foundation for the claims made in its companion paper. The few required corrections are minor.

---
## Detailed Findings

### MAJOR

**P1B-M1: S8 Gaussian combination notation (Table I Caption)**
*   **Location:** Page 5, Table I Caption
*   **Problem:** The text describing the naive Gaussian combination of S8 values has a missing operator or symbol, making it syntactically incorrect. It reads: `(0.827±0.0100.776 ±0.017 = 0.814 ± 0.009; agreement at the 0.01σ level)`. The two distributions are simply concatenated.
*   **Fix:** Insert an appropriate symbol or word to denote the combination. For example, rephrase as "the inverse-variance-weighted combination of the Planck+BAO+SN marginal (0.827±0.010) and the DES-Y3 prior (0.776±0.017) yields 0.814±0.009...".

### MINOR

**P1B-M2: Ambiguous definition of "σ-agreement"**
*   **Location:** Page 10, Section V.B
*   **Problem:** The text states that the independent re-run result for ΔNeff is "in 0.04σ agreement with the frozen +0.058±0.179 quote above." This phrasing is slightly ambiguous. While it is a common shorthand for (value1 - value2) / error, it could also be interpreted as the significance of the difference, i.e., (value1 - value2) / sqrt(err1² + err2²), which would yield a different value (~0.03σ).
*   **Fix:** Clarify the definition for the reader to remove ambiguity. For example: "...in 0.04σ agreement (i.e., the difference between the central values is 0.04 times the quoted uncertainty of the frozen chain) with the...".

### NIT (Cosmetic)

**P1B-N1: Typographical errors and inconsistencies**
*   **Location:** Throughout the paper
*   **Problem:** Several minor typographical errors and formatting inconsistencies were found.
    1.  **Units of H₀:** The units for the Hubble constant are typeset inconsistently. For example, on page 1, the abstract has `kms-¹ Mpc¯¹` and `kms¯¹ Mpc¯¹`. The standard and correct form is `km s⁻¹ Mpc⁻¹`. Please check and correct all instances for consistency.
    2.  **Trailing Zeros in Sigma Values:** The paper uses "3.60 tension", "2.7-2.90", and "3.60 headline". The trailing zero is inconsistent and unnecessary. Suggest using "3.6σ", "2.7-2.9σ", etc., for clarity and consistency throughout the manuscript.
    3.  **Page 21, Appendix B:** "What is included us. regenerable." should be "What is included vs. regenerable."
    4.  **Page 21, Appendix B:** The URL `https: //huggingface.co/datasets/bamfai/ p1b-alp-chains.` contains a space before `p1b-alp-chains`. This should be removed to make the link functional.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

The paper is of very high quality and is suitable for publication in Physical Review D after the minor corrections listed above are addressed. The work is methodologically sound, the results are presented with exceptional clarity and intellectual honesty, and the paper serves as a strong example of reproducible research.