# P1B_v1B018_R14 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1500pt
**Wall time**: 131.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=18794, completion=15996, reasoning=15356, total=34790

---

This is an adversarial peer review of Paper 1B (v1B.0.18). I have verified the R14 closures, including the removal of the AIC/BIC/lnB block, the Table 3 status updates, the new iter2 posterior regressions, and the NaMaster bias arithmetic. 

Below are the findings, focusing strictly on new load-bearing math/physics errors and critical inconsistencies.

## PAPER-GEM-B1: SH0ES Prior / Pantheon+ Parameter Decoupling Contradiction
**Classification:** BLOCKER
**Location:** Section 3, Caveats paragraph (SH0ES audit text)
**Issue:** The text claims the chain successfully pulls $M_B$ to the Riess value ($-19.263 \pm 0.049$) while simultaneously finding $H_0 = 67.69 \pm 1.06$ because "Pantheon+ determines $H_0$". This is physically and mathematically impossible in a properly configured joint fit. In the SNIa distance modulus equation, $M_B$ and $H_0$ are perfectly degenerate: the SN likelihood strictly constrains the intercept $M_B - 5 \log_{10}(H_0)$. If $H_0 = 67.69$, Pantheon+ *forces* the absolute magnitude to be $M_B \approx -19.42$. If the chain sample mean reports $M_B = -19.263$ alongside $H_0 = 67.69$, it proves that the `M_B` parameter constrained by the `H0.riess2020Mb` likelihood is completely decoupled from the absolute magnitude parameter actually being used by Pantheon+ (a classic Cobaya YAML alias failure). The audit text inadvertently proves the YAML is broken.
**Fix:** Acknowledge the parameter decoupling in the YAML audit. If the run is kept as a demonstration of the tension, clarify that forcing $M_B$ to the SH0ES value while $H_0$ remains at 67.69 incurs a massive $\Delta\chi^2$ penalty in Pantheon+ unless the parameters are aliased incorrectly. 

## PAPER-GEM-M1: Inconsistent ALP Birefringence Bounds (Survived Deferral)
**Classification:** MAJOR
**Location:** Section 6, "Birefringence value" paragraph
**Issue:** The text claims the prediction spans $\beta \approx 0.17^\circ$--$0.43^\circ$ over the ranges $C_{a\gamma} \in [4,12]$ and $\Delta\phi/f_a \in [0.2, 1.1]$. This arithmetic is false. The minimum is $4 \times 0.2 \times 0.0333^\circ = 0.027^\circ$. The maximum is $12 \times 1.1 \times 0.03
