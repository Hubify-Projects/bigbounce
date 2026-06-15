# P1B EXT19 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=135fdfb4 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (7799 chars)
**Wall time**: 173.6s

---

**Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program:..."**

**Report ID:** PRD-2026-06-HG-1B

This paper presents three technical analyses intended as a verification companion for a theoretical program described in a separate paper. The analyses cover: (1) a `ΛCDM+ΔNeff` MCMC parameter estimation to serve as a null-consistency test; (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-documented, with a laudable commitment to transparency and reproducibility. The authors are careful to properly scope their claims, distinguish between pipeline validation and sky detection, and disclose all relevant caveats and limitations. The three analyses are technically sound and provide valuable cross-checks.

However, the paper requires a significant structural revision to improve clarity and readability before it can be considered for publication. A few minor technical clarifications are also needed.

---
### ESSENTIAL Findings

None.

---
### MAJOR Findings

**ID: P1B-M1**
*   **Section:** III and V.C (pages 4, 5, 10)
*   **Problem:** The paper's structure is confusing due to the intermingling of results from two separate MCMC analyses. Section III is titled "STOCK-CAMB ΛCDM+ΔNeff MCMC", but a significant portion of the section (the "Physics interpretation (Table II)" and "Caveats" subsections on page 4, and points (d) and (e) on page 5) is dedicated to discussing a `w₀wₐ` analysis, whose primary results are presented later in Table II (page 20) and Section V.C (page 10). This makes the narrative difficult to follow, as the reader is presented with detailed results and caveats for a different model (`w₀wₐ`) in the middle of the discussion of the `ΔNeff` model.
*   **Required Fix:** Restructure the paper to cleanly separate the `ΛCDM+ΔNeff` and `w₀wₐ` analyses.
    1.  Section III should focus exclusively on the `ΛCDM+ΔNeff` proxy test, presenting the methods, results (Table I, Figs. 1-2), and conclusions for that analysis only.
    2.  Create a new, separate section (or a clearly delineated subsection within Section V) for the `w₀wₐ` analysis. This new section should contain the material currently on pages 4-5 ("Physics interpretation", "Caveats", etc.) and the material from Section V.C, presenting the motivation, methods, and results (Table II) for the `w₀wₐ` chain as a single, coherent analysis. This will greatly improve the logical flow of the paper.

---
### MINOR Findings

**ID: P1B-m1**
*   **Section:** IV (page 7)
*   **Problem:** The description of the template used for the birefringence angle `β` fit is potentially confusing or imprecise. The text states the fit is to `sin(2β)cos(2β) C_EE`, while Equation (1) uses `sin(4β) C_EE,tmpl`. Since `sin(4β) = 2sin(2β)cos(2β)`, there is a factor of 2 difference. Furthermore, the theoretically expected signal is `C_l^EB = 1/2 sin(4β) (C_l^EE - C_l^BB)`. The template used is an approximation that neglects the `C_BB` term and may have a different normalization. While the paper later correctly attributes the measured pipeline bias to this template mismatch, the initial description should be more explicit about the approximation being made.
*   **Required Fix:** Clarify the text on page 7 to explicitly state the form of the `C_l^EB` template being used. State that it is an approximation to the full signal (`1/2 sin(4β) (C_EE - C_BB)`) and briefly justify its use (e.g., `C_BB << C_EE` and matching the methodology of prior work [5]). This will make the source of the subsequently discussed bias clear from the outset.

---
### NITs (Cosmetic)

**ID: P1B-N1**
*   **Section:** V.A (page 9)
*   **Problem:** The text lists four dataset combinations, but the subsequent sentence lists five chains, with the "Planck-only" and "Planck+BAO" chains described as "accumulating" or "diagnostic". The phrasing is slightly ambiguous.
*   **Required Fix:** Reword for clarity. For example: "We analyze posteriors from two primary frozen MCMC chains (full-tension and Planck+BAO+SN), supported by several diagnostic and verification chains. The dataset combinations for the primary chains are..."

**ID: P1B-N2**
*   **Section:** VI (page 10)
*   **Problem:** The footnote for the `β = 0.342° ± 0.094° (3.6σ)` value is located in Section IV (footnote 3, page 6), but the value is used as the headline constraint for Section VI.
*   **Required Fix:** For reader convenience, either repeat the PR3/PR4 disambiguation footnote in Section VI or explicitly refer back to footnote 3 when the value is first introduced in Section VI.

---
## Summary recommendation

**MAJOR REVISIONS**

This paper provides a set of valuable and meticulously documented technical validations. The commitment to reproducibility is exemplary and sets a high standard. The scientific content is sound, and the conclusions are appropriately cautious and well-supported by the presented evidence. However, the paper's confusing structure, which mixes results from two distinct analyses, significantly hinders readability and must be addressed. Once the structural issue is resolved and the minor clarifications are made, the paper will be a strong candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the completed second-pass review.

================================================================
**Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program:..."**

**Report ID:** PRD-2026-06-HG-1B

This paper presents three technical analyses intended as a verification companion for a theoretical program described in a separate paper. The analyses cover: (1) a `ΛCDM+ΔNeff` MCMC parameter estimation to serve as a null-consistency test; (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-documented, with a laudable commitment to transparency and reproducibility. The authors are careful to properly scope their claims, distinguish between pipeline validation and sky detection, and disclose all relevant caveats and limitations. The three analyses are technically sound and provide valuable cross-checks.

However, the paper requires a significant structural revision to improve clarity and readability before it can be considered for publication. A few minor technical clarifications are also needed.

---
### ESSENTIAL Findings

None.

---
### MAJOR Findings

**ID: P1B-M1**
*   **Section:** III and V.C (pages 4, 5, 10)
*   **Problem:** The paper's structure is confusing due to the intermingling of results from two separate MCMC analyses. Section III is titled "STOCK-CAMB ΛCDM+ΔNeff MCMC", but a significant portion of the section (the "Physics interpretation (Table II)" and "Caveats" subsections on page 4, and points (d) and (e) on page 5) is dedicated to discussing a `w₀wₐ` analysis, whose primary results are presented later in Table II (page 20) and Section V.C (page 10). This makes the narrative difficult to follow, as the reader is presented with detailed results and caveats for a different model (`w₀wₐ`) in the middle of the discussion of the `ΔNeff` model.
*   **Required Fix:** Restructure the paper to cleanly separate the `ΛCDM+ΔNeff` and `w₀wₐ` analyses.
    1.  Section III should focus exclusively on the `ΛCDM+ΔNeff` proxy test, presenting the methods, results (Table I, Figs. 1-2), and conclusions for that analysis only.
    2.  Create a new, separate section (or a clearly delineated subsection within Section V) for the `w₀wₐ` analysis. This new section should contain the material currently on pages 4-5 ("Physics interpretation", "Caveats", etc.) and the material from Section V.C, presenting the motivation, methods, and results (Table II) for the `w₀wₐ` chain as a single, coherent analysis. This will greatly improve the logical flow of the paper.

---
### MINOR Findings

**ID: P1B-m1**
*   **Section:** IV (page 7)
*   **Problem:** The description of the template used for the birefringence angle `β` fit is potentially confusing or imprecise. The text states the fit is to `sin(2β)cos(2β) C_EE`, while Equation (1) uses `sin(4β) C_EE,tmpl`. Since `sin(4β) = 2sin(2β)cos(2β)`, there is a factor of 2 difference. Furthermore, the theoretically expected signal is `C_l^EB = 1/2 sin(4β) (C_l^EE - C_l^BB)`. The template used is an approximation that neglects the `C_BB` term and may have a different normalization. While the paper later correctly attributes the measured pipeline bias to this template mismatch, the initial description should be more explicit about the approximation being made.
*   **Required Fix:** Clarify the text on page 7 to explicitly state the form of the `C_l^EB` template being used. State that it is an approximation to the full signal (`1/2 sin(4β) (C_EE - C_BB)`) and briefly justify its use (e.g., `C_BB << C_EE` and matching the methodology of prior work [5]). This will make the source of the subsequently discussed bias clear from the outset.

**ID: P1B-m2**
*   **Section:** III (page 3, footnote 1)
*   **Problem:** The reconciliation of sample counts in footnote 1 is excellent but contains a minor ambiguity. It mentions a "third (Planck-only) dataset combination (114,992 raw samples; R-1 ~ 0.05) is still accumulating samples, is not reported in Table I... and is not aggregated into the 309,189-sample headline". However, Table III on page 20 *does* list a "Planck-only" chain and describes its status as "accumulating (not frozen)". This is a slight contradiction. The footnote says it's not reported in Table I (which is true), but the existence of the chain *is* reported elsewhere.
*   **Required Fix:** In footnote 1, rephrase slightly for full consistency. For example, change "...is not reported in Table I..." to "...is not used for any headline results in Table I...". Or, more simply, add a reference: "...is not reported in Table I (but is listed for completeness in Table III)...".

**ID: P1B-m3**
*   **Section:** IV (page 8, footnote 4)
*   **Problem:** Footnote 4 defines the pipeline-recovery SNR and gives a value of 20.32. It then cross-checks this against values from the `f_sky` sweep artifact, `32.98` and `28.81`, and states they are "consistent with 20.32fsky/0.32". This formula implies a linear scaling with sky fraction, whereas an SNR derived from a map is expected to scale with the square root of the sky fraction. A direct calculation confirms that the data are consistent with `20.32 * sqrt(f_sky/0.32)`, indicating a typo in the text.
*   **Required Fix:** In footnote 4, change the scaling relation from `20.32fsky/0.32` to `20.32 * sqrt(f_sky / 0.32)` to reflect the correct SNR scaling with sky area.

---
### NITs (Cosmetic)

**ID: P1B-N1**
*   **Section:** V.A (page 9)
*   **Problem:** The text lists four dataset combinations, but the subsequent sentence lists five chains, with the "Planck-only" and "Planck+BAO" chains described as "accumulating" or "diagnostic". The phrasing is slightly ambiguous.
*   **Required Fix:** Reword for clarity. For example: "We analyze posteriors from two primary frozen MCMC chains (full-tension and Planck+BAO+SN), supported by several diagnostic and verification chains. The dataset combinations for the primary chains are..."

**ID: P1B-N2**
*   **Section:** VI (page 10)
*   **Problem:** The footnote for the `β = 0.342° ± 0.094° (3.6σ)` value is located in Section IV (footnote 3, page 6), but the value is used as the headline constraint for Section VI.
*   **Required Fix:** For reader convenience, either repeat the PR3/PR4 disambiguation footnote in Section VI or explicitly refer back to footnote 3 when the value is first introduced in Section VI.

**ID: P1B-N3**
*   **Section:** Abstract and Page 1
*   **Problem:** The date is listed as "June 14, 2026". This is presumably a placeholder, but it is in the future.
*   **Required Fix:** Change the date to the submission date or remove it.

**ID: P1B-N4**
*   **Section:** Table I (page 19)
*   **Problem:** The caption states "S₈ = σ₈ (Ωm/0.3)¹/²". The exponent is `1/2`. In many places, this is written as `0.5`. Using the fraction `1/2` is less common in this context and could be misread.
*   **Required Fix:** For consistency and clarity, change the exponent from `1/2` to `0.5`, i.e., `S₈ = σ₈ (Ωm/0.3)^0.5`.

---
## Summary recommendation

**MAJOR REVISIONS**

This paper provides a set of valuable and meticulously documented technical validations. The commitment to reproducibility is exemplary and sets a high standard. The scientific content is sound, and the conclusions are appropriately cautious and well-supported by the presented evidence. However, the paper's confusing structure, which mixes results from two distinct analyses, significantly hinders readability and must be addressed. Once the structural issue is resolved and the minor clarifications are made, the paper will be a strong candidate for publication in Physical Review D.