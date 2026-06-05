# P1A 2026-06-04_R4fixed — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 127.2s

---

## Referee Report: P1A

### ESSENTIAL Findings

- **P1A-E1**: Abstract, p. 1  
  **Problem**: The claim "Ntot ≈ 92 post-bounce e-folds" is a load-bearing scalar with no traceable derivation in the main text or Appendix B. The abstract states this is a "fitted parameter," but the fitting procedure, data inputs, or error propagation (e.g., sensitivity to Treh/MGUT) are not provided.  
  **Required Fix**: Derive Ntot ≈ 92 explicitly in the main text (Sec. II or XII), showing the calculation from ρΛ ≈ (2.3 meV)⁴ and the ansatz Ξ ≡ (α/M) MPl × Dinf. Include error margins reflecting scheme dependence in γ and (Treh/MGUT)³/².

- **P1A-E2**: Section II.C.1, p. 6  
  **Problem**: The suppression factor Dinf = exp[−3Ntot] × (Treh/MGUT)³/² lacks provenance. The ansatz is admitted to be "order-of-magnitude matching" without a first-principles derivation (e.g., thermal partition function). The prefactor (Treh/MGUT)³/² ≈ 0.03 is critical for the fine-tuning hierarchy but is unjustified.  
  **Required Fix**: Provide a rigorous derivation of Dinf from thermal field theory or cite peer-reviewed sources for the ansatz. Quantify uncertainties from MGUT and Treh variations.

- **P1A-E3**: Section IV.B, p. 9  
  **Problem**: The Route 2 amplitude estimate Δθone-loop/Δθobs ∼ 10⁻⁵⁸–10⁻⁶⁰ relies on unstated dimensional reconciliation (e.g., implicit MPl factors). The derivation silently corrects a prior dimensional error ("eV·s as dimensionless"), but the final suppression lacks traceable steps.  
  **Required Fix**: Explicitly show dimensional analysis for Eq. (15), including unit conversions (eV to GeV) and justification for the H0/MPl ∼ 10⁻⁶¹ scaling. Provide a standalone equation for the dimensionless ratio.

### MAJOR Findings

- **P1A-M1**: Abstract and Section II.A.2, pp. 1, 5–6  
  **Problem**: The parity-odd operator (Eq. 6) is claimed to have off-shell mass dimension +1, but the mapping to ρΛ (via Ξ MPl⁴) is presented as an ansatz without operator-basis justification. Appendix B (dimensional analysis) is referenced but not provided in the submission.  
  **Required Fix**: Integrate Appendix B into the main text (Sec. II or new section) to show the operator’s dimensional status and the ad hoc nature of the ρΛ mapping. Clarify that this is not a controlled EFT result.

- **P1A-M2**: Section IX, pp. 12–14  
  **Problem**: The "13 logically-independent barriers" include Barrier 8 (parity-even interaction), which is subsumed by Barrier 14 (perturbation transparency). This double-counting inflates the constraint count. Table II admits they are "not logically independent" but retains both for "historical completeness."  
  **Required Fix**: Remove Barrier 8 from the catalog or demote it to a corollary of Barrier 14. Revise Table II and Sec. IX to list only 13 independent barriers.

- **P1A-M3**: Section III.A, p. 7  
  **Problem**: The CMB birefringence prediction β ≈ 0.27° is attributed to a spectator ALP, but the photon-torsion coupling "has not been derived" and is treated as a free parameter (α/M ∼ 10⁻²¹ GeV⁻¹). No ECH-specific derivation justifies this value.  
  **Required Fix**: Derive the photon-torsion coupling from the ECH action or cite foundational work. If phenomenological, state clearly that β ≈ 0.27° is a GR+ALP benchmark, not an ECH prediction.

### MINOR Findings

- **P1A-m1**: Section II.B, p. 6  
  **Problem**: The LQC critical density ρcrit ≃ 0.27–0.41 ρPl uses scheme-dependent values (γSU(2) ≈ 0.274 vs. γDLM ≈ 0.2375), but the uncertainty ("∼0.020") is not propagated in quantitative claims (e.g., ΩGW in Barrier 12).  
  **Required Fix**: Propagate γ-scheme uncertainties in all ρcrit-dependent calculations (e.g., Eq. 20) or cite a single consistent scheme.

- **P1A-m2**: Section XIV.D, p. 17  
  **Problem**: The tension between dark energy (Ntot ≈ 92) and fNL erasure (Ntot ≳ 60) claims SPHEREx scales are pushed to kbounceᵖʰʸˢ ∼ e³² kSPHERExᵖʰʸˢ, but the exponent 32 assumes Nexit = 60 without justification.  
  **Required Fix**: Justify Nexit ≈ 60 with a reference or calculation (e.g., from CMB horizon exit).

- **P1A-m3**: Abstract, p. 1  
  **Problem**: The phrase "perturbation-transparency" appears 3 times redundantly.  
  **Required Fix**: Consolidate to avoid repetition (e.g., "the central result is perturbation transparency: torsion vanishes...").

### NIT Findings

- **P1A-N1**: Section II.A.3, p. 6  
  **Problem**: "Parent black hole mass must exceed Mcrit ≈ 10⁻³ M⊙" has no citation or derivation.  
  **Required Fix**: Add a citation (e.g., Poplawski 2016) or derive in a footnote.

- **P1A-N2**: Section IV, p. 8  
  **Problem**: "Route 4 (parity-odd CMB coupling)" is inconsistently abbreviated as "R4" in closure summaries.  
  **Required Fix**: Use full route names (e.g., "Route 4") in all summaries for clarity.

---

## Summary recommendation  
**MAJOR REVISIONS**  
The paper presents a compelling channel-level closure of minimal ECH dark-energy routes but has critical gaps in provenance for load-bearing scalars (Ntot ≈ 92, Dinf suppression, Route 2 amplitude). The perturbation transparency result is robust, but the mass dimension ansatz (App. B) and spectator-ALP coupling lack derivation. The barrier catalog is inflated by double-counting, and key uncertainties (γ-scheme, Nexit) are unpropagated. Addressing ESSENTIAL fixes (explicit derivations for Ntot, Dinf, Route 2 amplitude) and MAJOR fixes (operator-basis clarity, barrier consolidation) is necessary for acceptance. The 21-page length is appropriate for the scope.