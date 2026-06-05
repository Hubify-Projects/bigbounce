# P1A 2026-06-04_R3clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 70.0s

---

# Referee Report: P1A

**To:** The Editor, Physical Review D
**From:** Referee
**Subject:** Review of manuscript P1A, "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

## Summary of the Manuscript

This manuscript investigates the possibility that late-time dark energy can be sourced by mechanisms within the minimal Einstein-Cartan-Holst (ECH) framework, in the context of a bouncing cosmology motivated by Loop Quantum Cosmology (LQC). The author assesses four specific "channels" for generating dark energy or other distinctive cosmological signatures. The main claims are: (1) a "channel-level closure" of these four routes, arguing that none can successfully produce the observed dark energy at the required amplitude without fine-tuning or violating other constraints; (2) a "perturbation-transparency theorem" showing that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbations, leaving them identical to standard GR; and (3) a "structural tension" between the number of e-folds required for the dark-energy mechanism and the survival of a matter-bounce signature in the non-Gaussianity parameter `f_NL`.

The paper's positive result is the perturbation-transparency theorem, which is a clear and useful finding. However, the primary claim of "closure" is built on a foundation that is not derived from first principles, a fact the author is commendably transparent about. Several other key arguments rely on incorrect physics or unpublished work, which must be addressed before the paper can be considered for publication.

## General Comments

The paper is ambitious and tackles an interesting and important problem. The author's transparency regarding the limitations of the framework, particularly the "ansatz" nature of the dark-energy mapping, is a significant strength. The perturbation-transparency theorem (Sec. X) is elegant and appears to be a solid, novel contribution. The systematic cataloging of constraints ("barriers") is also a useful organizational effort.

However, the manuscript suffers from several critical flaws that prevent its acceptance in its current form. The most severe issues are a physically incorrect scaling argument that underpins the "structural tension" claim, a heavy reliance on unpublished companion papers for essential numerical results and forecasts, and the overstatement of claims based on analyses that have not yet been completed. Furthermore, the central "closure" argument is weakened by the fact that the dark-energy generation mechanism itself is based on a phenomenological ansatz for a dimensionally-incomplete operator, a point that should be more prominently framed as the main conclusion.

## Specific Findings

### ESSENTIAL

**P1A-E1: Incorrect Physical Wavenumber Scaling**
*   **Location:** Abstract (p. 1), Sec. III A (p. 3), and Sec. XIV D (p. 17)
*   **Problem:** The paper claims a structural tension based on the erasure of the `f_NL = -35/8` signature. The argument relies on calculating the physical wavenumber of a mode at the bounce. The formula used is `k_phys^bounce ~ k_SPHEREx * e^(N_tot - N_exit)`. This scaling is physically incorrect. A comoving wavenumber `k` corresponds to a physical wavenumber `k_phys = k/a`. A mode with comoving scale `k` exits the horizon when `k = a_exit H_exit`. Its physical wavenumber at the bounce is `k_phys^bounce = k/a_bounce = (a_exit H_exit) / a_bounce = H_exit * e^N_exit`, where `N_exit` is the number of e-folds from the bounce to horizon exit. The paper's formula uses `N_tot - N_exit`, the number of e-folds from horizon exit to the end of inflation, which does not correctly scale the mode back to the bounce.
*   **Fix:** The author must re-derive this scaling relation from first principles. The entire "structural tension" argument in Sec. XIV D must be re-evaluated based on the correct scaling. If the argument no longer holds, this key conclusion of the paper must be removed from the abstract, introduction, and conclusion.

**P1A-E2: Over-reliance on Unpublished Companion Papers**
*   **Location:** Throughout the paper, specifically references [2] and [6]. E.g., Abstract (p. 1), Table I (p. 4), Sec. V (p. 5), Sec. XIII (p. 16).
*   **Problem:** The paper is not self-contained. All MCMC-derived cosmological parameter values (`H_0`, `ΔN_eff`, etc.) are cited from a companion paper "in preparation" [6]. The entire SPHEREx forecast for `f_NL`, which is presented as a key surviving test, is cited from another paper "in preparation" [2]. A reader cannot verify the claims or understand the methodology (e.g., priors, datasets, systematic error budget) for these crucial inputs.
*   **Fix:** The manuscript must be made self-contained. The author must add appendices summarizing the methodology, datasets, and key results from the MCMC analysis and the Fisher forecast for `f_NL`. This summary should be sufficient for a referee to understand the logic and assess the robustness of the numbers used in this paper's arguments.

**P1A-E3: Claims Based on Incomplete Analysis**
*   **Location:** Table III (p. 16) and its footnote `‡`.
*   **Problem:** The table reports that the Quintom-B bounce model is "consistent" with DESI `w0-wa` evidence. However, the footnote explicitly states that the MCMC chain required to test this is still running and has not converged. Making a scientific claim based on an incomplete analysis is unacceptable.
*   **Fix:** The "consistent" entry must be changed to "not tested" to match the other rows. The accompanying text in footnote `†` must be rephrased to state that Quintom-B is a *theoretical candidate* for explaining the evidence, but that no analysis has been performed in this work to verify this.

### MAJOR

**P1A-M1: Framing of the "Closure" Claim**
*   **Location:** Abstract, Introduction, and Conclusions (Sec. I, IV, XV).
*   **Problem:** The paper's main claim is the "closure" of four dark-energy routes. However, as the author honestly details in Appendix B, the link between the ECH parity-odd operator and a late-time vacuum energy is not derived from theory. It relies on a "phenomenological on-shell scaling ansatz" to fix the dimensionality of an operator that is not a valid dimension-4 Lagrangian density term. Therefore, the paper is not closing well-established theoretical routes to dark energy; it is demonstrating that these routes are not open from first principles and that ad-hoc attempts to open them via an ansatz are subsequently constrained. This is a subtle but crucial distinction.
*   **Fix:** The framing should be revised throughout the paper. The primary conclusion should be presented not as a "closure of routes," but as a demonstration that the minimal ECH framework lacks a first-principles mechanism to generate late-time dark energy, and that phenomenological attempts to construct one are highly constrained and require fine-tuning. This reframing would more accurately reflect the paper's core contribution.

**P1A-M2: Paper Length and Structure**
*   **Location:** Entire manuscript.
*   **Problem:** At 21 pages, the paper is long for its primary, defensible contributions (the perturbation-transparency theorem and the catalog of issues with ECH-as-DE). Section IX, in particular, lists 14 "barriers" that are a mix of novel calculations, known results, and philosophical arguments. This section dilutes the impact of the more rigorous constraints.
*   **Fix:** The author should significantly condense the manuscript. I recommend restructuring to a main text of ~15 pages focusing on the core logical thread: (1) Introduction to the ECH bounce framework, (2) The phenomenological nature of the DE link (bringing the key points of Appendix B forward), (3) The four-route analysis (Sec. IV), (4) The robust perturbation-transparency theorem (Sec. X), and (5) Conclusions. The detailed catalog of all 14 barriers (Sec. IX) should be moved to an appendix for completeness.

### MINOR

**P1A-m1: Future Dating**
*   **Location:** Page 1, Header.
*   **Problem:** The paper is dated "June 2, 2026 PDT". This is inappropriate for a journal submission.
*   **Fix:** Replace the date with a placeholder like "(Dated: ...)" or remove it.

**P1A-m2: Internal Version History Language**
*   **Location:** Sec. IV E, p. 11.
*   **Problem:** The text mentions the "...original Golden 2025/2026 internal note that motivated the project." This is internal project history and is not suitable for a formal publication.
*   **Fix:** Remove this phrase.

**P1A-m3: Internal Repository Artifacts**
*   **Location:** Sec. XV, "Data and Code Availability", p. 18.
*   **Problem:** The text refers to the repository's `CHANGELOG.md` file. This is an internal-facing detail.
*   **Fix:** Rephrase to be more general, for example: "The exact commit hash corresponding to this manuscript version is tagged in the repository for reproducibility."

**P1A-m4: Justification for a Key Claim**
*   **Location:** Sec. IX C, "Barrier 3", p. 12.
*   **Problem:** The statement "Torsion decouples from the FRW background precisely at the bounce density, yielding no distinctive perturbation signal" is a strong claim presented without immediate justification or a specific citation.
*   **Fix:** Please add a brief physical explanation or a precise reference that supports this statement.

### NIT

**P1A-N1: Author Contact Information**
*   **Location:** Page 1, footnote.
*   **Problem:** The email address `houston@hubify.com` appears to be from a commercial entity rather than a research institution, which is unconventional.
*   **Fix:** If possible, the author should consider using a standard academic or persistent identifier-linked email address. This is a stylistic suggestion at the editor's discretion.

## Summary recommendation

**MAJOR REVISIONS**

The manuscript presents a valuable and interesting positive result in the perturbation-transparency theorem and performs a useful, systematic investigation of potential dark-energy mechanisms in ECH cosmology. The author's intellectual honesty about the ansatz-based nature of the dark-energy model is commendable. However, the paper cannot be published in its current form. The essential flaws in the "structural tension" argument's derivation and the reliance on unpublished work for key numerical inputs must be rectified. Furthermore, the overall framing of the "closure" claim needs to be significantly revised to more accurately reflect what has been demonstrated. After these substantial revisions, the paper could represent a solid contribution to the theoretical cosmology literature.