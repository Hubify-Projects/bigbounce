# P4_v1093 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0030pt_P4_v1093_R12_R-round_real
**Wall time**: 44.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=81734, completion=5228, reasoning=4302, total=86962

---

Here is the adversarial peer review of the cosmology paper (v1.0.93), focusing on theoretical physics rigor, adversarial prompt constraints, and cross-vendor convergence.

## PAPER-GEM-MAJOR-1
**Section:** Sec. VI.H (Future Directions)
**Concrete Issue:** A severe regression of the TTA overclaim sweep survived in the Future Directions section: "...applying the equivariant Catalog C classifications, which eliminate handedness-dependent systematic biases by construction". This directly contradicts the paper's load-bearing empirical findings (the 9.5σ residual monopole, the 1.35% D4 argmax shift, and the 21% argmax-flip rate) which explicitly prove that hard-label systematic biases are *not* eliminated by construction.
**Fix:** Soften to: "...applying the equivariant Catalog C classifications, which suppress the horizontal-flip component of orientation bias..."

## PAPER-GEM-minor-2
**Section:** Sec. VI.D (Sensitivity Floor)
**Concrete Issue:** The text states "The generator... sweeps five injection amplitudes $A \in \{0.05\%, 0.10\%, 0.20\%, 0.30\%, 0.50\%\}$", but Table VIII and the abstract correctly reflect the new extended 9-amplitude sweep up to 2.00%. The inline text was not updated during the R11 extension.
**Fix:** Update the inline text to read "sweeps nine injection amplitudes $A \in \{0.05\%, \dots, 2.00\%\}$" to match Table VIII.

## PAPER-GEM-minor-3
**Section:** Abstract / Table III / Footnote 5
**Concrete Issue:** The abstract quotes $+6.48\sigma$ for the "lowest pseudo-$C_\ell$ bandpower ($\ell_{\rm eff}=4$)". However, Table III reports $+6.097\sigma$ for this exact bandpower. Footnote 5 explains that $+6.48\sigma$ is the raw asymmetry map value while $+6.097\sigma$ is the NaMaster-coupled pseudo-$C_\ell$ before inversion, but using $+6.48\sigma$ in the abstract while calling it a "pseudo-$C_\ell$ bandpower" creates a numerical mismatch with the primary multipole table.
**Fix:** In the abstract, either change $+6.48\sigma$ to $+6.097\sigma$ to match Table III exactly, or clarify the noun phrase to "raw asymmetry map bandpower" to distinguish it from the NaMaster pseudo-$C_\ell$ stage.

## PAPER-GEM-nit-4
**Section:** Abstract
**Concrete Issue:** The capitalized "AND" in "...in monopole-subtraction treatment, AND in MASTER mode-coupling inversion..." is too colloquial/conversational for a PRD/MNRAS abstract.
**Fix:** Change to lowercase "and".

***

### Convergence Audit & Physics Sign-off
*   **Fisher-floor reframe:** Verified. The abstract and text cleanly separate the 0.29% ideal-statistical floor from the 0.75% empirical threshold on the HC-spiral subsample.
*   **TTA softening:** Verified complete in the main text, with the single exception of the regression caught in Finding 1.
*   **AUDIT-1 7th iteration:** Verified. The Conclusions cleanly separate the single-mode $\ell=1$ collapse ($-0.12\sigma$) from the bandpower diagnostics.
*   **Hemisphere LEE:** Verified. Direct-MC is correctly framed as the primary rejection, with Bonferroni demoted to a conservative parametric upper bound.
*   **Table V gap:** Verified. The 4,758-galaxy boundary-edge explanation is mathematically acceptable and transparent.
*   **Physics/EFT framing:** Excellent. Section VI.G correctly identifies that a dipole is an axial vector projection testing *isotropy*, not an isotropic parity-odd scalar correlator (like the 4PCF), and correctly refrains from forcing a mapping to the scalar EFT parameter $g_*$.

**Status:** Pending the fix to the MAJOR regression in Sec VI.H and the minor text-sync issues, the manuscript has reached convergence and is ready for external journal submission.
