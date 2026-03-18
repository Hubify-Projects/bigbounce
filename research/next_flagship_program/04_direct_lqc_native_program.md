# 04: Direct LQC-Native Perturbation and Observable Program

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Why LQC Is Now the Active Framework

Our ECH program established that:
1. The ECH modified Friedmann equation H^2 = (rho/3M^2)(1 - rho/rho_c) is IDENTICAL to LQC at background level
2. ECH is perturbation-transparent — no corrections to the Mukhanov-Sasaki equation
3. LQC provides perturbation-level corrections via the dressed-metric approach
4. The only viable distinctive model (Wilson-Ewing quasi-dust) requires LQC corrections for r suppression

**We need to build an LQC-native program, not just reference LQC literature.**

---

## Program Design

### A. Background Equations

**LQC Effective Friedmann Equation:**
$$
H^2 = \frac{\rho}{3M_{\rm Pl}^2}\left(1 - \frac{\rho}{\rho_c}\right)
$$

with rho_c = 0.41 * rho_Pl (from numerical LQC simulations; Ashtekar, Pawlowski, Singh 2006).

Note: Our ECH derivation gives rho_c = 0.21 M_Pl^4 from gamma = 0.274. The LQC value is rho_c = 0.41 * rho_Pl = 0.41 * M_Pl^4. These differ by a factor ~2. **This difference affects r and f_NL quantitatively but not qualitatively.**

**Raychaudhuri Equation:**
$$
\dot{H} = -\frac{\rho + P}{2M_{\rm Pl}^2}\left(1 - \frac{2\rho}{\rho_c}\right)
$$

**Matter content for the quasi-dust model:**
$$
P = -\epsilon \rho, \quad w = -\epsilon, \quad \epsilon = 0.003
$$

Physical realization: dust + Lambda (LCDM), where the effective EOS is slightly negative due to Lambda contribution during contraction.

### B. Perturbation Variables and Formalism

**Two LQC perturbation schemes exist:**

| Scheme | Developers | Key Feature |
|--------|-----------|-------------|
| Dressed-metric | Agullo, Ashtekar, Nelson (2012-2013) | Perturbations on quantum-corrected background |
| Hybrid | Fernandez-Mendez, Mena Marugan, Olmedo (2012) | Different time-dependent mass term |

**We use the dressed-metric approach** because:
1. It is more widely used in the matter bounce literature
2. Wilson-Ewing's predictions use it
3. It gives explicit perturbation equations we can compute with

**Dressed-metric Mukhanov-Sasaki equation (scalar):**
$$
v_k'' + \left(c_s^2 k^2 - \frac{z''}{z}\right) v_k = 0
$$

where the prime is conformal time derivative, and the pump field z is modified from the classical expression by LQC corrections:

$$
z = \frac{a \sqrt{\rho + P}}{\tilde{c}_s H} \times f_{\rm LQC}(\rho/\rho_c)
$$

The correction factor f_LQC depends on the specific quantization scheme and modifies the effective mass z''/z near the bounce. Far from the bounce (rho << rho_c), f_LQC -> 1 and the equation reduces to classical GR.

**Tensor perturbation equation:**
$$
\mu_k'' + \left(k^2 - \frac{a''}{a}\right) \mu_k = 0
$$

The tensor equation has a DIFFERENT effective mass (a''/a) from the scalar (z''/z). This difference is what allows differential suppression of tensors relative to scalars, giving r << 1.

### C. Assumptions Required

1. **LQC effective equations are valid.** The effective equations are derived from the full loop quantum dynamics in the homogeneous sector. Inhomogeneous corrections are treated perturbatively. This is believed reliable for modes with k << k_Pl.

2. **Dressed-metric quantization scheme.** Results differ between dressed-metric and hybrid approaches. We commit to dressed-metric following Wilson-Ewing.

3. **Bounce-Davies initial conditions.** In the asymptotic contracting past (a -> infinity), modes are in the standard Minkowski vacuum. This is the analog of Bunch-Davies in inflation.

4. **Matter content: quasi-dust (w = -epsilon).** The effective EOS comes from CDM + Lambda. During deep contraction, matter dominates (w -> 0). Near turnaround (before contraction begins), Lambda dominates.

5. **Single-field adiabatic perturbations.** No spectator fields, no isocurvature modes. The f_NL prediction requires this.

### D. Calculable Observables

| Observable | Formula/Method | Literature Status |
|-----------|---------------|------------------|
| n_s | 1 - 12*epsilon | Known (Wilson-Ewing 2013) |
| r | Numerical: ratio of tensor to scalar power at CMB scales after bounce | Known numerically (~10^-4), not analytically |
| f_NL^local | In-in formalism at third order, evaluated through bounce | **NOT COMPUTED in LQC** |
| f_NL^local (pre-bounce) | Cai et al. 2009: -35/8 | Known but with discrepancies (see file 05) |
| alpha_s | d(n_s)/d(ln k) | Known to be positive (Lehners & Wilson-Ewing 2015) |
| n_T | Tensor spectral index | Known to be blue (>0) |

**THE KEY GAP: f_NL through the LQC bounce has not been computed.** This is where our program can make a genuine contribution.

### E. What Can Be Imported vs What We Must Derive

**Import from literature:**
- n_s formula: directly from Wilson-Ewing (well-established)
- r ~ 10^-4 estimate: from Wilson-Ewing numerical work
- Pre-bounce f_NL = -35/8: from Cai et al. (but with caveats — see file 05)
- BKL resolution via ekpyrotic pre-phase: from Ijjas & Steinhardt

**Must derive ourselves:**
1. **Resolution of the f_NL = -35/8 discrepancies** (Li-Brandenberger gives -2.2 at c_s = 1; Quintin quotes -35/16)
2. **f_NL transfer through the LQC bounce** (does the dressed-metric amplification enhance or preserve f_NL?)
3. **Combined f_NL: pre-bounce + bounce contribution** (the observable quantity)
4. **Whether the Quintin no-go applies to the LQC dressed-metric bounce** (does r suppression force f_NL enhancement?)

### F. How This Differs from Generic Matter-Bounce EFT

| Feature | Generic EFT | LQC Dressed-Metric |
|---------|-------------|-------------------|
| Bounce mechanism | Parametrized (rho_c free) | Derived from loop quantum gravity (rho_c fixed by Immirzi) |
| Perturbation corrections | None assumed or arbitrary | Specific z''/z modification from quantum geometry |
| r suppression | Must be imposed or hoped for | Follows from scalar-tensor differential amplification |
| f_NL bounce transfer | Unknown / assumed transparent | Calculable from the dressed-metric equations |
| Parameter freedom | rho_c, possibly bounce shape | gamma (Immirzi parameter, fixed by black hole entropy) |

**LQC is more constrained than generic EFT** because both the background (rho_c) and perturbations (z''/z) are derived from the quantization, not freely parametrized. This is a theoretical advantage: fewer free choices means more predictive power.

### G. Does LQC Offer Stronger Predictive Control Than ECH?

**YES, definitively.**

| | ECH | LQC |
|-|-----|-----|
| Background | H^2 = (rho/3M^2)(1-rho/rho_c) | Same |
| Perturbations | Classical Mukhanov-Sasaki (no corrections) | Modified z''/z from dressed metric |
| r prediction | Same as classical GR (~O(10) for dust) | ~10^-4 (suppressed by quantum corrections) |
| f_NL prediction | -35/8 from contraction (no bounce modification) | -35/8 from contraction + possible bounce modification |
| Testable difference from inflation | NONE (r too large to be viable, f_NL unchanged) | f_NL = -4.375 (testable by MegaMapper) |
| Overall | Perturbation-transparent, observationally silent | Perturbation-active, potentially observable |

---

## The Research Roadmap

### Phase 1: Foundation Verification (CURRENT)
- Resolve f_NL = -35/8 discrepancies (independent derivation)
- Verify convention alignment with Planck
- Establish whether the pre-bounce value is -35/8, -35/16, or -2.2

### Phase 2: Bounce Transfer Calculation
- Compute the scalar and tensor transfer functions through the LQC dressed-metric bounce
- Determine whether scalar amplification (which gives r ~ 10^-4) also enhances f_NL
- Test whether the Quintin no-go theorem applies to the dressed-metric bounce

### Phase 3: Observable Prediction Set
- Compile the complete {n_s, r, f_NL, alpha_s, n_T} prediction set
- Compute detection forecasts for MegaMapper, SPHEREx, CMB-S4
- Compare directly with Starobinsky R^2 predictions

### Phase 4: Robustness Tests
- Sensitivity to epsilon (w = -0.003 +/- ?)
- Sensitivity to rho_c (Immirzi parameter uncertainty)
- Sensitivity to initial conditions (Bounce-Davies vs alternatives)
- Effect of the ekpyrotic pre-phase on observable-scale perturbations
