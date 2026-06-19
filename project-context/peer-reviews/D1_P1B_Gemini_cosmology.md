# P1B D1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3376 chars)
**Wall time**: 168.9s

---

**Referee Report for Manuscript [P1B]**

**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

This manuscript presents a technical companion paper detailing three verification analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program of a companion paper (Paper I(a)). The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model, serving as a null-consistency test; (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally thorough in its methodology, documentation, and reproducibility. The authors have gone to great lengths to clearly state the scope of each analysis, provide detailed validation and robustness checks, and make all materials publicly available. The level of transparency, particularly in the footnotes, appendices, and the claims classification table (Table V), is commendable and sets a high standard for technical papers in the field.

However, the manuscript requires significant revision to address several issues related to structure, scientific context, and the presentation of key results before it can be considered for publication in Physical Review D.

---
### **Detailed Findings**

#### **ESSENTIAL REVISIONS**

**P1B-E1: Abstract Understates Key Model-Building Obstacle (Fine-Tuning)**
-   **Section:** Abstract (Page 1)
-   **Problem:** The abstract states that for the spectator-ALP model, "the spectator-safe (Ωα < 0.01) subset is tuned". This phrasing significantly obscures the severity of the tuning required. The main text (Sec. VI, p. 10, and especially fn. 6) reveals this corresponds to a "~25x fine-tuning" of the initial misalignment angle (θᵢ ~ 0.1 vs. the natural midpoint of the prior). For a reader assessing the viability of the model, the quantitative degree of fine-tuning is a critical piece of information that is effectively hidden in the abstract.
-   **Required Fix:** The abstract must be revised to include the quantitative measure of the fine-tuning. Replace "is tuned" with language that reflects the ~25x tuning, for example: "...and the spectator-safe (Ωα < 0.01) subset requires a ~25× fine-tuning of the initial misalignment angle..."

#### **MAJOR REVISIONS**

**P1B-M1: Illogical Manuscript Structure Obscures Narrative**
-   **Section:** III (Page 3) and V (Page 9)
-   **Problem:** The structure of the paper is confusing and illogical. Section III is titled "STOCK-CAMB ΛCDM+ΔNeff MCMC...", but the "Physics interpretation" subsection on page 4 immediately launches into a detailed discussion of a `w₀wₐ` CPL model, referencing Table II. This `w₀wₐ` analysis is formally part of a different dataset combination and model extension, which is only properly contextualized in Section V.C. This conflation of two separate analyses under a single, misleading section heading makes the paper very difficult to follow.
-   **Required Fix:** The manuscript must be restructured to logically separate the different analyses.
    1.  Section III should be strictly limited to the ΛCDM+ΔNeff proxy test.
    2.  The `w₀wₐ` analysis (currently scattered between Sec. III and Sec. V.C) should be consolidated into its own distinct, top-level section. This new section should contain the physics interpretation, the extensive caveats, and the presentation of the Table II results. This will provide a clear, self-contained narrative for each of the paper's main analyses.

**P1B-M2: Paper Fails Standalone-Reader Test due to Lack of Scientific Context**
-   **Section:** I. Introduction (Page 2)
-   **Problem:** The manuscript is presented as a "technical verification companion" to Paper I(a) [1]. While this framing is acceptable, the paper completely outsources the scientific motivation for its analyses to the companion paper. It is not self-contained. A reader of Physical Review D should not need to read a separate manuscript to understand the fundamental purpose of the calculations presented. Key questions are left unanswered: Why is ΔNeff a relevant proxy for a spin-torsion theory? What is the connection between the ECH framework and the spectator-ALP model that motivates the consistency check?
-   **Required Fix:** The Introduction must be expanded to provide the minimal necessary scientific context from Paper I(a). Add one to two paragraphs concisely summarizing: (a) the core idea of the ECH framework being tested, (b) the theoretical reason that a search for an effective radiation component (ΔNeff) serves as a meaningful (even if null) test, and (c) the motivation for investigating the ALP-birefringence signal in this context, even if it is not a unique prediction.

**P1B-M3: Missing Effect Size for a High-Significance Statistical Claim**
-   **Section:** V.C (Page 10) and related text in Sec. III (Page 4)
-   **Problem:** The paper reports a >4σ statistical preference for a phantom-crossing dark energy model over ΛCDM, based on a "posterior-tail extrapolation distance" for `w₀`. This is the most statistically significant result in the manuscript. While the authors correctly provide numerous caveats that this is not a formal model selection result, they fail to report the corresponding physical effect size in the same section. A >4σ tension demands immediate physical contextualization. The text on page 4 calculates this effect size—a mere ~1.7% change in the Hubble rate at z=0.5—but this crucial context is divorced from the headline sigma value reported on page 10.
-   **Required Fix:** The physical effect size must be reported immediately alongside the statistical significance. In Section V.C, where the +4.3σ and -3.6σ values are quoted, the text must also state that this corresponds to a small (≈1.7% at z=0.5) deviation in the expansion history. This immediately grounds the statistical result and provides the reader with the necessary context to interpret its practical importance.

#### **MINOR REVISIONS**

**P1B-m1: Ambiguous Language Regarding Model Parameter Space**
-   **Section:** VI (Page 12)
-   **Problem:** The text refers to a "natural envelope box" for the ALP parameters (θᵢ, m/H₀). It is not immediately clear from the main text whether this "natural" region defines the MCMC priors or is simply a benchmark region for theoretical comparison. Appendix C clarifies that the actual priors are much wider, but the main-text phrasing could be misleading.
-   **Required Fix:** Clarify the status of the "natural envelope box" in the main text of Section VI. Explicitly state that it is a theoretically-motivated benchmark for assessing naturalness and that the MCMC analysis employs the wider priors detailed in Appendix C.

**P1B-m2: Awkward Phrasing in Abstract**
-   **Section:** Abstract (Page 1)
-   **Problem:** The phrase "...and are not directly comparable to each other's published sky significances)" is grammatically awkward.
-   **Required Fix:** Rephrase for clarity, for example: "...and are not directly comparable to published sky-detection significances."

---
### **Summary Recommendation**

**MAJOR REVISIONS**

This manuscript represents a high-quality, transparent, and rigorous body of technical work. The commitment to reproducibility is exemplary. However, the paper in its current form is not suitable for publication. The structural flaws severely impede readability, and the lack of self-contained scientific motivation makes it difficult to assess the importance of the presented calculations. Furthermore, the presentation of the `w₀wₐ` result and the ALP fine-tuning must be improved to provide immediate and clear context.

If the authors can successfully restructure the manuscript to present a clear narrative for each analysis, provide the necessary scientific context in the introduction, and properly contextualize their key results as specified above, the paper will be a valuable contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second-pass review, incorporating new findings.

================================================================
**Referee Report for Manuscript [P1B] (Second Pass)**

This second review pass re-examines the manuscript with a focus on detailed numerical, logical, and cross-referential consistency, following the initial review which identified several major structural and contextual issues. The new findings below are to be considered in addition to those in the first report.

---
### **NEW FINDINGS**

#### **NEW (MINOR) REVISIONS**

**P1B-N1: Arithmetic Error in a Key Physical Effect Size**
-   **Section:** III (Page 4, "Physics interpretation" paragraph)
-   **Problem:** The manuscript states that for the best-fit CPL model (`w₀=-0.812`, `wₐ=-0.667`), the Hubble rate at z=0.5 differs from the ΛCDM rate by "≈ +1.7%". A direct recalculation using the standard formula for `H(z)` in a `w₀wₐ` cosmology with the paper's stated parameters (`Ω_m=0.314`) yields a deviation of **≈ +1.1%**. This discrepancy, while not large, is significant because this number is the primary measure of the physical effect size corresponding to the >4σ statistical result discussed in the manuscript (and highlighted in my initial review point P1B-M3). An incorrect effect size misrepresents the physical implications of the statistical finding.
-   **Required Fix:** The authors must re-verify this calculation and correct the value in the text. It is possible this is a stale number from an earlier, slightly different MCMC posterior that was not updated.

**P1B-N2: Typo in Technical Footnote**
-   **Section:** IV (Footnote 4, Page 8)
-   **Problem:** The text in footnote 4 describes the scaling of the template-fit SNR with sky fraction, stating it is consistent with the relation `20.32 * f_sky / 0.32`. This is incorrect; the SNR for a measurement limited by sample variance on the sky should scale as `sqrt(f_sky)`. The numerical values provided in the same footnote (`32.98` at `f_sky=0.85`) are indeed consistent with the correct `sqrt(f_sky)` scaling, not the linear scaling written in the text.
-   **Required Fix:** Correct the typo in the text of footnote 4 to reflect the correct square-root dependence, changing `...f_sky/0.32` to `...sqrt(f_sky/0.32)`.

---
### **Confirmation of Initial Assessment**

This detailed second pass confirms that the manuscript is, on a micro level, exceptionally rigorous. The vast majority of numerical claims, cross-references, and technical explanations hold up to scrutiny. The authors have demonstrated a laudable commitment to internal consistency and careful qualification of their results (e.g., explicitly noting when different σ-values are not comparable).

The discovery of the arithmetic error in P1B-N1 reinforces the importance of the major revision P1B-M3 from the initial report. The most statistically significant finding in the paper (the >4σ preference for phantom crossing) must be accompanied by an accurate and prominent statement of its relatively small physical effect size on the expansion history.

The overall recommendation of **MAJOR REVISIONS** stands. The structural and contextual issues identified in the first report remain the primary barriers to publication. Addressing those issues, along with the new minor corrections identified here, will make this a strong and valuable technical paper.