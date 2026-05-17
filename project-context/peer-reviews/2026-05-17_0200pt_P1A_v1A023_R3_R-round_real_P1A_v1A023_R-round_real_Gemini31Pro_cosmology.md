# P1A_v1A023 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P1A_v1A023_R3_R-round_real
**Wall time**: 99.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=27035, completion=14123, reasoning=12239, total=41158

---

Here is the adversarial peer review of P1A v1A.0.23, focusing on theoretical physics, dimensional consistency, and structural claims.

## Finding 1: Appendix B Dimensional Math Error (BLOCKER)
**ID:** PAPER-GEM-B1
**Location:** Appendix B, paragraph 2
**Issue:** The text claims to resolve the dimensional shortfall of the parity-odd operator by adding "three additional powers of $M_{\rm Pl}$", but the formula written adds only two ($M_{\rm Pl}^2$). Because $[\alpha/M] = -1$ and $[\mathcal{F}] = +2$, the operator $\alpha M_{\rm Pl}^2 \varepsilon e e \mathcal{F} / M$ has mass dimension $+3$, failing the "dim+4 by construction" claim. 
**Fix:** Change "$\alpha M_{\rm Pl}^2 / M$" to "$\alpha M_{\rm Pl}^3 / M$" to correctly implement the three powers of mass required to reach dimension $+4$.

| Truth-Audit | Content |
| :--- | :--- |
| **Citation** | Appendix B |
| **Paper Says** | "the coupling must carry three additional powers of $M_{\rm Pl}$ in its coefficient ($\alpha/M \to \alpha M_{\rm Pl}^2 / M$)" |
| **Fact Says** | $M_{\rm Pl}^2$ provides two powers of mass. $-1 (\text{from } \alpha/M) + 2 (\text{from } M_{\rm Pl}^2) + 2 (\text{from } \mathcal{F}) = +3 \neq +4$. |
| **Verdict** | STILL-UNRESOLVED |
| **Fix** | Write $\alpha M_{\rm Pl}^3 / M$. |

## Finding 2: Route 2 Dimensionless Reduction is Mathematically Invalid (BLOCKER)
**ID:** PAPER-GEM-B2
**Location:** Section 4.2, paragraph 1
**Issue:** The text attempts a "dimensionless reduction" for Route 2 but writes a formula with units of Energy: $\frac{H_0}{M_{\rm Pl} (\alpha/M) \beta_{\rm obs}}$. Since $M_{\rm Pl} (\alpha/M)$ is dimensionless, the denominator is dimensionless, leaving the numerator $H_0$ (dimension $+1$). The text then silently fakes the numerical evaluation by substituting the dimensionless value $10^{-61}$ (which is $H_0/M_{\rm Pl}$) in place of $H_0$. You cannot fix a dimensional error by plugging a dimensionless ratio into a dimensionful variable.
**Fix:** Explicitly include the missing $1/M_{\rm Pl}$ factor in the numerator of the formula: $\frac{H_0/M_{\rm Pl}}{M_{\rm Pl} (\alpha/M) \beta_{\rm obs}}$.

| Truth-Audit | Content |
| :--- | :--- |
| **Citation** | Section 4.2 |
| **Paper Says** | "in the dimensionless ratio $\Delta\theta_{\rm one-loop}/\Delta\theta_{\rm obs} \sim \frac{\alpha_{\rm em}}{4\pi} \frac{H_0}{M_{\rm Pl} (\alpha/M) \beta_{\rm obs}}$" |
| **Fact Says** | The formula evaluates to units of GeV. The text forces it to be dimensionless by substituting $H_0/M_{\rm Pl} \sim 10^{-61}$ into the $H_0$ slot. |
| **Verdict** | STILL-UNRESOLVED |
| **Fix** | Correct the formula to $\frac{H_0/M_{\rm Pl}}{M_{\rm Pl} (\alpha/M) \beta_{\rm obs}}$. |

## Finding 3: Contradiction on Route 2 Deferral Status (MAJOR)
**ID:** PAPER-GEM-M1
**Location:** Section 4.0 vs Section 4.2
**Issue:** Section 4.0 explicitly states that the Route 2 dimensionless re-derivation "remains on-record deferred". However, Section 4.2 contains a new paragraph claiming to perform exactly this re-derivation ("the dimensionless reduction above corrects that"). This is a direct structural contradiction, made worse by the fact that the attempted correction in 4.2 contains the mathematical error flagged in Finding 2.
**Fix:** Delete the attempted dimensionless reduction in Sec 4.2 to align with the deferral note in Sec 4.0, or remove the deferral note and provide a mathematically valid derivation in Sec 4.2.

| Truth-Audit | Content |
| :--- | :--- |
| **Citation** | Sec 4.0 vs Sec 4.2 |
| **Paper Says** | (4.0): "dimensionless-form re-derivation---remains on-record deferred" vs (4.2): "the dimensionless reduction above corrects that" |
| **Fact Says** | A paper cannot simultaneously claim a derivation is deferred to future work while claiming to execute the corrected derivation in the next subsection. |
| **Verdict** | REGRESSION |
| **Fix** | Remove the contradictory text in 4.2. |

## Finding 4: Garbled Kinematics in Structural Tension Argument (MAJOR)
**ID:** PAPER-GEM-M2
**Location:** Section 13 and Section 14.4
**Issue:** The text states "bounce-era comoving scales $k e^{N_{\rm tot}} \sim e^{30} \times k_{\rm SPHEREx}$". First, comoving scales ($k$) are constant by definition; it is *physical* scales that scale as $a^{-1}$. Second, if $N_{\rm tot} \approx 92$, then $e^{N_{\rm tot}} = e^{92}$, not $e^{30}$. The $e^{30}$ likely refers to the relative expansion difference between the bounce and CMB horizon exit ($e^{92-60}$), but the formula $k e^{N_{\rm tot}}$ evaluates to $e^{92}$, making the equation mathematically inconsistent with its own output.
**Fix:** Correct the terminology to "physical scales" and fix the math to reflect the relative e-fold difference: $k_{\rm phys}^{\rm bounce} \sim k_{\rm phys}^{\rm SPHEREx} e^{N_{\rm tot} - N_{\rm exit}} \sim k_{\rm phys}^{\rm SPHEREx} e^{32}$.

| Truth-Audit | Content |
| :--- | :--- |
| **Citation** | Sec 13 and Sec 14.4 |
| **Paper Says** | "bounce-era comoving scales $k e^{N_{\rm tot}} \sim e^{30} \times k_{\rm SPHEREx}$" |
| **Fact Says** | Comoving scales do not scale with $e^N$. If $N_{\rm tot}=92$, $e^{N_{\rm tot}} \neq e^{30}$. |
| **Verdict** | NOVEL |
| **Fix** | Rewrite as relative physical scale scaling: $k_{\rm phys}^{\rm bounce} \sim k_{\rm phys}^{\rm SPHEREx} e^{N_{\rm tot} - 60}$. |

## Finding 5: Category Error in Barrier 14 Classification (minor)
**ID:** PAPER-GEM-m1
**Location:** Section 2.3.1
**Issue:** The text introduces a "Reheating thermal-reset barrier" (a thermodynamic overwrite of background torsion by a thermal fermion bath) and claims it "strengthens Barrier 14 (perturbation transparency)". These are entirely different physical mechanisms. Barrier 14 is a kinematic decoupling theorem regarding scalar perturbations; it has nothing to do with thermodynamic background resets.
**Fix:** Separate the thermal-reset argument into its own distinct barrier, or group it with Barrier 5 (Scale Separation), rather than conflating it with perturbation transparency.

| Truth-Audit | Content |
| :--- | :--- |
| **Citation** | Section 2.3.1 |
| **Paper Says** | "This strengthens Barrier 14 (perturbation transparency) by adding a parallel thermodynamic erasure channel" |
| **Fact Says** | Perturbation transparency ($\delta T = 0$ for scalars) and thermodynamic background reset ($T_{\rm bg} \sim T_{\rm reh}^3$) are physically unrelated phenomena. |
| **Verdict** | NOVEL |
| **Fix** | Decouple the thermal-reset argument from Barrier 14. |
