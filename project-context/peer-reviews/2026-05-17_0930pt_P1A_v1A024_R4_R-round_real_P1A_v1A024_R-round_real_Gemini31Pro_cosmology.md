# P1A_v1A024 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0930pt_P1A_v1A024_R4_R-round_real
**Wall time**: 170.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=27037, completion=12293, reasoning=10559, total=39330

---

## PAPER-GEM-B1: Incomplete Propagation of Kinematics Closure (BLOCKER)
**Location:** Abstract, Sec 1.1, Sec 13, Sec 14.4
**Issue:** The R3 closure mandating the shift from $N_{tot}=92$ to the relative differential $N_{tot}-N_{exit}=32$ was only partially applied and introduced a new dimensional error. The Abstract, Sec 1.1, and Sec 14.4 still contain the garbled $k e^{N_{tot}} \sim e^{30}$ (which implies $N_{tot}=30$, contradicting the $N_{tot}=92$ fit). Furthermore, the updated Sec 13 incorrectly equates physical and comoving wavenumbers: $k^{phys}_{bounce} \sim k_{SPHEREx} e^{N_{tot}-N_{exit}}$ is dimensionally invalid because $k_{SPHEREx}$ is a comoving scale, requiring an $a_0$ normalization factor to map to a physical scale at the bounce.
**Fix:** Globally replace all instances of $e^{N_{tot}} \sim e^{30}$ with the relative differential $e^{N_{tot}-N_{exit}} \sim e^{32}$. Correct the Sec 13 formula to properly relate comoving to physical scales: $k_{phys}(bounce) = k_{comoving} / a_{bounce}$.

## PAPER-GEM-B2: Direct Contradiction of Route 2 Deferral Closure (BLOCKER)
**Location:** Sec 4.0
**Issue:** The R4 mandate explicitly states that the Route 2 dimensionless reduction is now executed and no longer deferred. However, Sec 4.0 retains the exact R3 deferral text: "remains **on-record deferred** pending a dedicated photon-Chern-Simons coupling derivation". This is a direct failure to apply the mandated closure, creating a glaring contradiction between the section intro and the executed derivation in Sec 4.2.
**Fix:** Delete the deferral sentence in Sec 4.0 and explicitly state that the dimensionless reduction has been successfully executed in Sec 4.2.

## PAPER-GEM-M1: Invalid Statistical Tension Calculation (MAJOR)
**Location:** Sec 15 (Conclusions), Item 2
**Issue:** The text claims LiteBIRD will distinguish a future $0.27^\circ$ measurement from the current $0.342^\circ$ prior at $2.4\sigma$ by calculating $|0.342-0.27|/0.03$. This is a fundamental statistical error; it completely ignores the prior measurement's own uncertainty ($\pm 0.094^\circ$). The actual tension between the two independent measurements must be calculated in quadrature: $\Delta / \sqrt{\sigma_{new}^2 + \sigma_{old}^2} = 0.072 / \sqrt{0.03^2 + 0.094^2} \approx 0.73\sigma$.
**Fix:** Recalculate the tension using the quadrature sum of both uncertainties, and correct the text to state that LiteBIRD will *not* statistically distinguish the spectator-ALP value from the current central value.

## PAPER-GEM-M2: Dimensional Inconsistency in Route 2 Effective Action (MAJOR)
**Location:** Sec 4.2 (Route 2)
**Issue:** The dimensionless reduction in Route 2 is built on a dimensionally flawed operator assignment. Eq 13 defines the action as $\Gamma \propto \frac{1}{M_{Pl}} \int d^4x \partial_\mu \theta J^{5\mu}$. Since $J^{5\mu}$ has mass dimension 3 and $d^4x$ is dimension -4, $\partial_\mu \theta$ *must* have mass dimension 2 for the action to be dimensionless. However, the text immediately substitutes $\partial_\mu \theta \sim H \sim 10^{-33}$ eV (dimension 1). 
**Fix:** Correct the operator dimension (e.g., the prefactor must be $1/M_{Pl}^2$ if $\theta$ is a standard dimension-1 axion field) and re-evaluate the dimensionless suppression ratio accordingly.

## PAPER-GEM-m1: Thermal Reset Renders $N_{tot}=92$ Tension Fictitious (minor)
**Location:** Sec 2.3.1 vs Sec 14.4
**Issue:** Sec 2.3.1 correctly proves that reheating populates a thermal fermion bath that completely overwrites any bounce-era torsion memory. However, the text fails to acknowledge the logical consequence: this renders the entire $N_{tot}=92$ calculation (Eq 11) dynamically fictitious, not just "fine-tuned". Consequently, the "structural tension" highlighted in Sec 14.4 is a ghost tension, as the mechanism cannot carry the $N_{tot}$ dependence through reheating anyway.
**Fix:** Add a sentence in Sec 2.3.1 explicitly stating that the thermal reset renders the $N_{tot}=92$ structural tension dynamically moot, and adjust the framing in Sec 14.4 to reflect this.

## PAPER-GEM-n1: Misaligned Barrier Count in Table 2 (nit)
**Location:** Table 2
**Issue:** The text has been updated to repeatedly emphasize "13 logically-independent barriers" (with B8 subsumed by B14). However, Table 2 still lists Barrier 8 as a distinct, equally-weighted row (1 through 14), which visually contradicts the 13-barrier structural claim.
**Fix:** Merge the B8 row into B14 in Table 2, or visually gray it out with a table note indicating it is subsumed, to align the table with the text's 13-barrier count.

---

### Per-Finding Truth-Audit Table

| ID | Claim | Verification in Text | Status |
| :--- | :--- | :--- | :--- |
| **B1** | Kinematics closure not fully propagated; dimensional error in Sec 13. | Abstract, Sec 1.1, Sec 14.4 still say $e^{N_{tot}} \sim e^{30}$. Sec 13 says $k^{phys}_{bounce} \sim k_{SPHEREx} e^{N_{tot}-N_{exit}}$, mixing physical and comoving units. | Confirmed |
| **B2** | Sec 4.0 retains deferral note despite R4 closure. | Sec 4.0 explicitly states: "remains **on-record deferred** pending a dedicated photon-Chern-Simons coupling derivation". | Confirmed |
| **M1** | LiteBIRD tension calculation ignores prior uncertainty. | Sec 15 calculates tension as $\|0.342-0.27\|/0.03 \approx 2.4\sigma$, ignoring the $\pm 0.094^\circ$ prior error. | Confirmed |
| **M2** | Route 2 operator dimensions are inconsistent. | Sec 4.2 defines $\Gamma \propto M_{Pl}^{-1} \int d^4x \partial_\mu \theta J^{5\mu}$ but sets $\partial_\mu \theta \sim H$ (dim 1), yielding an action of dimension -1. | Confirmed |
| **m1** | Thermal reset logic invalidates $N_{tot}=92$ tension. | Sec 2.3.1 states torsion memory is "overwritten by the reheating thermal reset", but Sec 14.4 still treats the $N_{tot}=92$ tension as a physical robustness check. | Confirmed |
| **n1** | Table 2 lists 14 distinct rows despite 13-barrier text. | Table 2 contains 14 numbered rows, treating B8 identically to the others. | Confirmed |
