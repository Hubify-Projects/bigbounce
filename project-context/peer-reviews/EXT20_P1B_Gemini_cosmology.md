# P1B EXT20 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 173.9s

---

## Referee Report for Manuscript [P1B]

**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

**Journal:** Physical Review D

---

### General Comments

This manuscript presents three technical verification analyses intended as a companion to a separate theoretical work ("Paper I(a)"). The analyses cover: (1) a stock-CAMB MCMC analysis of the ΛCDM+∆Neff model as a proxy for spin-torsion effects, (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-executed, demonstrating a very high level of rigor, transparency, and commitment to reproducibility. The scope of each analysis is clearly and carefully delineated, with potential limitations and caveats stated upfront and discussed thoroughly. The authors take great care to distinguish between pipeline validation metrics and sky-measurement significance, and between posterior-based parameter constraints and model-selection statistics. The numerical results presented are internally consistent and appear to be robustly derived. The detailed appendices and references to public data/code repositories are commendable and set a high standard for computational papers in the field.

While the paper is dense and detailed, the length is justified by the thoroughness of the verification work. The findings, though largely null-results (i.e., consistency with standard cosmology and identification of required fine-tuning in the ALP model), are valuable contributions that properly contextualize the theoretical claims of the main companion paper. The manuscript is of high quality and is suitable for publication in Physical Review D after some minor revisions to improve structural clarity and address a few minor points.

---

### Findings

#### MAJOR

**ID: P1B-M1**
*   **Location:** Section III, Page 4
*   **Problem:** The structure of Section III, "STOCK-CAMB ΛCDM+∆Neff MCMC: GENERIC RADIATION-PROXY TEST", is confusing. While the section title and initial paragraphs focus on the ΛCDM+∆Neff proxy analysis (results in Table I), a significant portion of the section, starting with the "Physics interpretation (Table II)" paragraph on page 4, is dedicated to an entirely different analysis of a `w0wa` model (results in Table II). This second analysis uses a different dataset combination (including DESI DR2 BAO but not SHOES) and is methodologically distinct. Interleaving the discussion of this second chain within the section dedicated to the first makes the paper difficult to follow.
*   **Required Fix:** Restructure the paper to more clearly separate the discussion of these two distinct MCMC analyses. I recommend creating a new, dedicated section for the `w0wa` analysis. For example, the current Section V ("Cosmological Fits and Model Comparison") could be split. Part A could remain "Datasets and Configuration", Part B could be "Results: ΛCDM+∆Neff proxy", and a new Part C could be "Diagnostic Cross-Check: `w0wa` Model", containing the material currently on page 4 and in Section V.C. This would logically group the results with their respective models and tables, improving readability.

#### MINOR

**ID: P1B-m1**
*   **Location:** Page 1, Abstract
*   **Problem:** The abstract mentions the spectator-ALP scan-prior is `m ~ H0`, but the posterior-supported fixed-coupling accommodation shifts to `m >> H0` (median `m ≈ 36 H0`). While correct, the phrase "scan-prior `m ~ H0` region" could be misinterpreted as the full prior range. The actual prior is very broad (`m/H0 ≈ 7 × 10⁻³` to `7 × 10²`, per Appendix C). The `m ~ H0` region is better described as the "natural parameter range" or "benchmark region" as discussed in the main text.
*   **Required Fix:** To improve precision, rephrase slightly in the abstract. For example: "...the scan-prior covers the natural `m ~ H0` region...", or "...the benchmark `m ~ H0` region within the scan-prior...".

**ID: P1B-m2**
*   **Location:** Page 11, Section VI, Footnote 5
*   **Problem:** The footnote states that a quintom `w0wa` background would shift `H(z)` at `z < 1` by a "~few percent", which is a qualitative statement. The paper is otherwise excellent at quantifying such claims.
*   **Required Fix:** Provide a quantitative estimate for this effect, even if it is approximate. For example, using the posterior mean values from Table II, state the maximum percentage difference in `H(z)` compared to the ΛCDM background within the relevant redshift range. This would strengthen the claim that the effect on `Δφ/fa` is sub-dominant.

**ID: P1B-m3**
*   **Location:** Page 14, Figure 4 Caption
*   **Problem:** The caption states the mass prior is `log10(ma/eV) ∈ [-35, -30]` and gives the corresponding `m/H0` range. It would be helpful for the reader to also see the prior range for `θi` and `Cay` directly in the caption, as these are the other two dimensions plotted.
*   **Required Fix:** Add the flat prior ranges for `θi` (e.g., `θi ∈ [0.01, π]`) and `Cay` (e.g., `Cay ∈ [4, 60]`) to the caption of Figure 4 for completeness.

#### NIT (Nitpicks / Typos)

**ID: P1B-N1**
*   **Location:** Page 1, Abstract
*   **Problem:** The sentence "both are MC pipeline-recovery figures, not sky-measurement systematics, and are not directly comparable to each other's published sky significances" contains a minor grammatical ambiguity. "each other's" could be read as the two pipeline figures being compared to each other, rather than to the sky measurements.
*   **Required Fix:** Suggest rephrasing for clarity, e.g., "...and are not directly comparable to published sky-detection significances."

**ID: P1B-N2**
*   **Location:** Page 3, Footnote 1
*   **Problem:** The sentence "The correct both-chains post-burnin total is 216,432." is followed by "Burn-in reconciliation note:". This second part reads like a section heading rather than part of the prose.
*   **Required Fix:** Integrate the "Burn-in reconciliation note" text more smoothly into the footnote paragraph. For example: "The total post-burnin count across both chains is 216,432. This value is reconciled with the GetDist outputs as follows: ...".

**ID: P1B-N3**
*   **Location:** Page 8, last paragraph of left column
*   **Problem:** The text refers to the `β = 0.342°` injection and states "the pipeline recovers 0.302° at template-fit SNR = 25.71; for β = 0, the recovered angle is 0.000°...". The β symbol is used for both the injection value and the parameter itself.
*   **Required Fix:** For maximum clarity, use `β_inj` when referring to the injected value, e.g., "for `β_inj` = 0, the recovered angle is 0.000°...".

**ID: P1B-N4**
*   **Location:** Page 17, Appendix C, Likelihood stack
*   **Problem:** The text states "The c5_continuous ESS values (~800-2860) are adequate for posterior characterisation. The βfree run3_baseline chain...". The symbol `β_free` is used, but the parameter name in the table below is `βdeg`.
*   **Required Fix:** Harmonize the notation. Either change `β_free` in the text to `βdeg` or vice-versa to match the table.

---

### Summary recommendation

**MAJOR REVISIONS**

The manuscript is of excellent quality, demonstrating a standard of rigor and transparency that should be encouraged. The scientific content is sound, and the conclusions are well-supported by the detailed analyses. The primary reason for the "MAJOR REVISIONS" recommendation is the structural issue identified in **P1B-M1**, where the interleaved discussion of two separate MCMC analyses significantly hinders readability and logical flow. A restructuring to cleanly separate these analyses is essential for the paper to be accessible and clear. The remaining points are minor and straightforward to address. I am confident that the authors can revise the manuscript to an acceptable state, and I look forward to reviewing the revised version.