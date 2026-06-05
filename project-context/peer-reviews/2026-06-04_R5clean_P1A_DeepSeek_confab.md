# P1A 2026-06-04_R5clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 277.5s

---

## Referee Report: P1A

### ESSENTIAL Revisions

- **P1A-E1: Section I, page 1 (Abstract) & Section XV**  
  **Problem:** The value \( \beta \approx 0.27^\circ \) is presented as a "benchmark consistency point" for ALP birefringence but lacks provenance. It is not derived in the paper or traceable to a dataset/script. The text states it is "comparable" to observed values (0.342°±0.094° and 0.215°±0.074°), but 0.27° is not explicitly calculated from these measurements (e.g., midpoint, weighted average).  
  **Fix:** Justify how \( \beta \approx 0.27^\circ \) is obtained from cited observations ([3–5]) or provide a derivation. If it is an assumed midpoint, state this explicitly.

- **P1A-E2: Section I, page 1 (Abstract) & Table IV**  
  **Problem:** Cosmological parameters (\( H_0 = 67.68 \pm 1.06 \), \( \Delta N_{\text{eff}} \approx 0 \)) are sourced from "companion Paper I(b) [6]" (in preparation), which is unavailable. These values are critical to the structural argument (e.g., tension resolution) but lack traceable data/code.  
  **Fix:** Provide MCMC chains, Cobaya configurations, and dataset integration scripts as supplementary material. Pending public release of [6], include key derivations in an appendix.

- **P1A-E3: Section IV.D, page 10 (Route 4 closure)**  
  **Problem:** Route 4 (spectator ALP) is claimed closed due to naturalness (\( m_\theta \sim H_0 \) tuning), but the paper undercuts this by admitting that floating \( \alpha/M \) allows matching both \( \beta_{\text{obs}} \) and \( \rho_\Lambda \) without \( m_\theta \) tuning. This contradicts the closure claim.  
  **Fix:** Reconcile or revise the argument: Either (1) justify why \( \alpha/M \) cannot be floated (e.g., via ECH first-principles), or (2) clarify that Route 4 is not amplitude-closed but suffers from an explanatory deficit (no ECH derivation of \( \alpha/M \)).

---

### MAJOR Revisions

- **P1A-M1: Section II.B, page 6 (\( \rho_{\text{crit}} \)) & Appendix B**  
  **Problem:** The Barbero-Immirzi parameter \( \gamma_{\text{SU(2)}} \approx 0.274 \) has scheme-dependent uncertainty (\(\sim 0.020\)), but this is not propagated to \( \rho_{\text{crit}} \simeq 0.27–0.41 \rho_{\text{Pl}} \) or downstream calculations (e.g., \( N_{\text{tot}} \approx 92 \)).  
  **Fix:** Quantify uncertainty in \( \rho_{\text{crit}} \) and propagate it to all dependent quantities (e.g., \( N_{\text{tot}} \)). Discuss impact on constraints.

- **P1A-M2: Section II.C.1, page 7 (\( N_{\text{tot}} \approx 92 \))**  
  **Problem:** The derivation of \( N_{\text{tot}} \approx 92 \) (Eq. 11) depends on the ansatz \( D_{\text{inf}} \propto (T_{\text{reh}}/M_{\text{GUT}})^{3/2} \), but the exponent \( 3/2 \) is not derived (described as "dimensional-analysis aesthetic"). This weakens the fine-tuning argument.  
  **Fix:** Provide a first-principles phase-space integral or thermal partition function to justify the exponent. Acknowledge residual uncertainty in \( N_{\text{tot}} \).

- **P1A-M3: Section IX (Barrier Catalog), Table II**  
  **Problem:** Barrier 14 (perturbation transparency) subsumes Barrier 8 (observational consequence), but both are listed as "logically independent" in Sec. IX and Table II, inflating the constraint count.  
  **Fix:** Remove Barrier 8 from the catalog or label it explicitly as a corollary of Barrier 14. Revise Sec. IX to clarify: "13 logically independent barriers (Barrier 8 is subsumed by Barrier 14)."

- **P1A-M4: Section XIII, page 16 (Surviving Tests)**  
  **Problem:** The \( f_{\text{NL}} = -35/8 \) forecast (3–5σ with SPHEREx) is sourced from companion Paper II [2] (in preparation), making it untraceable.  
  **Fix:** Include key Fisher forecast details (e.g., \( \sigma(f_{\text{NL}}) \approx 0.7–1.0 \) degradation) in the main text or appendix. Provide code/script for reproducibility.

---

### MINOR Revisions

- **P1A-m1: Section I, page 1 (Header)**  
  **Problem:** Version-history artifacts ("ROUND: 2026-06-04_R5clean", "CHANGES SINCE LAST ROUND: R5: all known artifacts stripped") appear in the body.  
  **Fix:** Remove all version-tracking language.

- **P1A-m2: Section II.A.2, page 5 (Eq. 6)**  
  **Problem:** The parity-odd operator (Eq. 6) has mass dimension +1 but is treated as dimension +4 via ansatz (Appendix B). This switch is acknowledged but risks confusion.  
  **Fix:** Add a footnote to Eq. 6: "Off-shell dimension is +1; +4 is achieved on-shell via Eq. B2."

- **P1A-m3: Section III.A, page 7 (CMB EB)**  
  **Problem:** The statement "The parity-odd structure is qualitatively consistent" is vague. No quantitative link between Eq. 6 and \( \beta \) is derived.  
  **Fix:** Clarify that consistency is motivational, not derived, or add a phenomenological coupling derivation.

---

### NIT Revisions

- **P1A-n1: Section II.C.1, page 7**  
  **Problem:** Typo: "C/P-equilibrium" should be "CP-equilibrium".  
  **Fix:** Correct to "CP-equilibrium".

---

### Summary of Arithmetic/Provenance Checks
- **ρcrit ≃ 0.27–0.41 ρPl (Sec. II.B)**: Traceable via Eq. 9 and γ scheme-dependence.  
- **Ntot ≈ 92 (Sec. II.C.1)**: Internally consistent arithmetic (e.g., 92 - 60 = 32 e-folds → e32 scaling) but ansatz-dependent.  
- **fNL = -35/8 (Sec. I)**: Cited to [1]; no derivation needed.  
- **β ≈ 0.27° (Sec. I)**: Untraceable (see E1).  
- **H0, ΔNeff (Sec. I)**: Untraceable (see E2).  
- **Ξ ~ 10⁻¹²³ (Sec. XII.A)**: Consistent with Eq. 24 and Ntot ≈ 92.  
- **All σ values (e.g., H0, βobs)**: Sources cited; no conflation of scales.

---

### Page Count
The paper (21 pages) is within PRD limits (15–30 pp). No reduction needed.

---

## Summary Recommendation  
**MAJOR REVISIONS**  

The paper presents a significant theoretical contribution—the perturbation-transparency theorem and channel-level closure of four ECH dark-energy routes—but has critical flaws: (1) Key parameters (H0, ΔNeff, β≈0.27°) lack traceable provenance, relying on inaccessible companion works; (2) The closure of Route 4 is contradicted by the admission that α/M can float; (3) Uncertainties in γ and the Dinf ansatz are unpropagated. Addressing these is essential for verification and self-containment. The perturbation-transparency result and barrier catalog are robust but require clearer framing (e.g., Barrier 8/14 overlap). After revisions, this will be a high-impact methods paper.