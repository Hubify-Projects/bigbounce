# P1B R56 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R56_P1B/paper1b_mcmc_companion.pdf` md5=f5f3c8ad pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 154.2s

---

## Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..."

This paper presents three technical analyses intended as a verification companion for a separate work on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a proxy for extra radiation, (2) a validation of a NaMaster pseudo-C_ell pipeline for cosmic birefringence on synthetic skies, and (3) a consistency check of a spectator axion-like particle (ALP) model with observed birefringence signals.

The paper is exceptionally transparent, with detailed explanations of methods, careful scoping of claims, and exemplary documentation for reproducibility. The three core analyses are, for the most part, well-executed and their conclusions are appropriately cautious. However, the manuscript contains a significant analysis with a known, uncorrected systematic that undermines its conclusions, and there are several other points that require revision.

### ESSENTIAL

*   **P1B-E1:** Section III (page 4), Section V.C (page 12), Table II (page 6) — **Analysis with Uncorrected Systematics.**
    *   **Problem:** The paper presents a detailed analysis of a `w0-wa` dark energy model, reporting high-precision results such as `wo = -0.8122 ± 0.0436` and a `+4.3σ` tail-distance from ΛCDM. However, as acknowledged in "Caveat (e)" on page 5, the supernova likelihood used is a simple product of the DES-SN5YR and Pantheon+ likelihoods, which share ~20% of their supernovae. This introduces an unquantified systematic from the double-counting of events and the use of different Malmquist-bias corrections. Presenting high-significance results based on a likelihood with a known, uncorrected, and potentially large systematic is not acceptable for publication in PRD. The caveat, while present, is insufficient to justify the inclusion of these results in the main body of the paper.
    *   **Required Fix:** The entire `w0-wa` analysis, including the "Physics interpretation" paragraph on page 4, the `wowa cross-check` section on page 12, and Table II on page 6, must be removed from the manuscript. Alternatively, it could be moved to an appendix with the title "Exploratory Analysis with Uncorrected Supernova Overlap," with all high-sigma claims (`+4.3σ`, `-3.6σ`) removed and the text reframed to focus solely on the methodological limitation. The primary option of removal is strongly preferred to improve the paper's focus and rigor.

### MAJOR

*   **P1B-M1:** Section II (page 2) and throughout — **Reliance on Companion Paper.**
    *   **Problem:** The paper is explicitly a "companion" to "Paper I(a) [1]". While the three main analyses are largely self-contained, the motivation and context are heavily dependent on this other work. For example, the specific prediction `fNL = -35/8` is quoted on page 2 but its derivation and significance are entirely in Paper I(a). A PRD paper must be readable and its arguments assessable on a standalone basis.
    *   **Required Fix:** The authors must ensure that no load-bearing claims in this manuscript depend on results derived only in Paper I(a). For imported results used for context (like the `fNL` value), the text should be modified to make it clear that these are for motivation only and do not form part of the evidence presented in this work. For example, rephrase "the surviving matter-bounce-specific test predictions (fNL = -35/8...)" to something like "For context, the ECH framework discussed in Paper I(a) motivates tests of specific predictions such as fNL = -35/8, which we do not test here."

### MINOR

*   **P1B-m1:** Page 1, Abstract — **Futuristic Date.**
    *   **Problem:** The paper is dated "June 26, 2026".
    *   **Required Fix:** Replace the placeholder date with the current submission date.

*   **P1B-m2:** Page 17, Section "wowa cross-check" — **Redundant Section.**
    *   **Problem:** The section titled "wowa cross-check" on page 17 is largely a repetition of the discussion and caveats already presented in Section III on page 4 and Section V.C on page 12.
    *   **Required Fix:** This section should be removed. If the `w0-wa` analysis is retained in an appendix per P1B-E1, this content should be merged into that appendix.

*   **P1B-m3:** Page 13, Footnote 5 — **Clarity of Background Model.**
    *   **Problem:** Footnote 5 states that the ALP ODE is integrated on a ΛCDM background, which is distinct from the "quintom-bounce dynamics" of the ECH cosmology. It then estimates a "few-percent systematic on Δφ/fa". This is a key detail for the consistency claim.
    *   **Required Fix:** The main text should briefly mention that the ALP evolution is computed in a standard ΛCDM background for this consistency check, and that the potential systematic from using a different background cosmology is estimated to be sub-dominant (as argued in the footnote). This makes the assumption clear without requiring the reader to parse the footnote.

*   **P1B-m4:** Page 20, Table V — **Clarity of "Model-comparison" Claim.**
    *   **Problem:** The fifth row of Table V lists the claim "Model-comparison ΔAIC/BIC/ln B" with the reference value "Not reported" and the note "Nested-sampling follow-up". This is confusing as it lists a non-claim.
    *   **Required Fix:** Rephrase the "Claim" to "Bayesian evidence for model extensions" or similar, to make it clear what is being deferred. The current phrasing reads like a missing result.

### NIT

*   **P1B-N1:** Page 10, "Robustness battery and bias attribution" — **Duplicate Phrase.**
    *   **Problem:** The text reads "...reproduces the pod anchor exactly (p = 0.238°, bias -0.032°). The bias is then unchanged under an apodization-scale sweep (0.5° and 3° FWHM vs. the canonical 2°: β = 0.239° and 0.238°), under a larger Galactic cut (|b| > 30°, fsky = 0.20: 0.238°), and under B-mode purification (purify_b=True: 0.238°) so the earlier attribution...". The value `β=0.238°` appears three times in a row for different tests.
    *   **Required Fix:** While numerically correct, this could be rephrased for better readability, e.g., "...The bias remains at -0.032° (β_rec = 0.238°) under an apodization-scale sweep..., a larger Galactic cut..., and B-mode purification...".

*   **P1B-N2:** Page 11, "Independent re-run cross-check" — **Sigma-value comparison.**
    *   **Problem:** The text states that the re-run `ΔNeff` value is in `0.04σ` agreement with the frozen chain. As noted in the text, this is `(mean1 - mean2) / sigma1`. While not incorrect, a more standard comparison would use the combined uncertainty in the denominator.
    *   **Required Fix:** No change is strictly required as the text is self-consistent, but for clarity, the authors might consider stating the comparison as `|μ1 - μ2| / sqrt(σ1^2 + σ2^2) ≈ 0.03σ` or explicitly justifying their choice of normalization.

## Summary recommendation

**MAJOR REVISIONS**

The manuscript presents three distinct technical analyses. Two of these—the ΛCDM+ΔNeff MCMC proxy and the NaMaster pipeline validation—are executed to a very high standard of rigor and transparency. The third, a spectator ALP consistency check, is also well-argued, with its significant limitations (fine-tuning) stated upfront. The paper's commitment to reproducibility is commendable.

However, the paper is significantly flawed by the inclusion of a fourth analysis on the `w0-wa` model. This analysis suffers from a known and uncorrected systematic due to supernova sample overlap, yet its results are presented with high-precision statistics that imply a level of confidence the methodology cannot support. This section does not meet the standards of the journal and its inclusion detracts from the high quality of the other work.

I recommend that the paper be accepted for publication after major revisions, the most critical of which is the removal or complete reframing of the problematic `w0-wa` analysis. Once this is addressed, the remaining paper will represent a solid and useful contribution to the literature on cosmological verification methods.