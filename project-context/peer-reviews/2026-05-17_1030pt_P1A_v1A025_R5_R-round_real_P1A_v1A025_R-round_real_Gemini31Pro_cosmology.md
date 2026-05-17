# P1A_v1A025 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_1030pt_P1A_v1A025_R5_R-round_real
**Wall time**: 71.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=27275, completion=9609, reasoning=8567, total=36884

---

Here is the adversarial peer review of Paper 1A (v1A.0.25), focusing on theoretical physics, EFT consistency, and the verification of R4/R5 closures.

## PAPER-GEM-B1 [BLOCKER]: Kinematics propagation-tail regression in Sec 14.4
**Location:** Sec 14.4, "($k_{\rm bounce}\sim k\,e^{N_{\rm tot}}\sim e^{30}\times k_{\rm SPHEREx}$)"
**Issue:** The v1A.0.25 kinematics closure was successfully applied to the Abstract and Sec 1.1, but missed in Sec 14.4. The text here still uses the erroneous absolute $e^{N_{tot}}$ scaling and mixes comoving/physical wavenumbers, directly contradicting the corrected $e^{N_{tot}-N_{exit}}$ differential formula established earlier in the paper.
**Fix:** Update Sec 14.4 to match the corrected kinematics in the Abstract: "$k_{\rm bounce}^{\rm phys} \sim k_{\rm SPHEREx}^{\rm phys}\,e^{N_{\rm tot}-N_{\rm exit}} \sim e^{32}\,k_{\rm SPHEREx}^{\rm phys}$".

## PAPER-GEM-M1 [MAJOR]: Illegitimate dimensional "fix" in Route 2
**Location:** Sec 4.2, Eq 14 and preceding text ("$H_0 \to H_0/M_{Pl}$ factor restored").
**Issue:** The text attempts to fix the dimensional inconsistency of the $\Delta\theta_{\rm one-loop}/\Delta\theta_{\rm obs}$ ratio by manually dividing the numerator by $M_{Pl}$. This is mathematically illegitimate. A physical rotation angle $\Delta\theta$ must be dimensionless by definition. If the one-loop effective action yields a dimensionful $\Delta\theta$, the derivation mapping the action to the observable is fundamentally botched; ad-hoc division by $M_{Pl}$ merely masks the underlying physics error.
**Fix:** Re-derive the induced rotation angle $\Delta\theta_{\rm one-loop}$ from the effective action (Eq 13) properly to yield a naturally dimensionless quantity, rather than patching a dimensionful result with an arbitrary mass scale.

## PAPER-GEM-M2 [MAJOR]: Category error in Barrier 14 / Thermal Reset grouping
**Location:** Sec 2.3.1, "Reheating thermal-reset barrier (R2 finding, supporting B14)"
**Issue:** Grouping the thermodynamic thermal-reset of background torsion under Barrier 14 is a severe category error. B14 is a kinematic theorem proving torsion vanishes identically for *scalar perturbations* ($T=0$). Thermal reset is a thermodynamic argument about *homogeneous background* torsion tracking a fermion bath. They are physically orthogonal mechanisms and cannot be conflated.
**Fix:** Decouple the thermal-reset argument from B14 entirely. Reclassify it as an independent thermodynamic barrier or group it under Barrier 5 (Scale Separation).

## PAPER-GEM-M3 [MAJOR]: Route 4 overshoot logic artificially freezes $\alpha/M$
**Location:** Sec 4.4, "For any $m_\theta$ in the natural ALP range... the produced $\rho_\theta \propto m_\theta^2$ overshoots $\rho_\Lambda$"
**Issue:** The claim that natural ALP masses overshoot $\rho_\Lambda$ by 22-36 orders of magnitude assumes $\alpha/M$ is rigidly fixed to $10^{-21}$ GeV$^{-1}$. If $\alpha/M$ is treated as a free phenomenological parameter, one can perfectly match both $\beta_{\rm obs}$ and $\rho_\Lambda$ for *any* $m_\theta$ simply by scaling $\alpha/M \propto m_\theta$ (e.g., requiring $\alpha/M \sim 10^{-10}$ GeV$^{-1}$ for $m_\theta \sim 10^{-22}$ eV). 
**Fix:** Explicitly state that the overshoot assumes $\alpha/M$ is bounded near $10^{-21}$ GeV$^{-1}$ by the one-loop estimate. Acknowledge that if $\alpha/M$ is completely free, the observables can be matched by tuning the coupling.

## PAPER-GEM-N1 [nit]: Directional reference error in Sec 4.0
**Location:** Sec 4.0, "executed in-line in Sec. \ref{sec:route2} above"
**Issue:** Section 4.0 is the introduction to Section 4. The Route 2 derivation is in Section 4.2, which is *below* this text, not above it. 
**Fix:** Change "above" to "below" and verify the LaTeX label points to Section 4.2 (`sec:r2_oneloop`).
