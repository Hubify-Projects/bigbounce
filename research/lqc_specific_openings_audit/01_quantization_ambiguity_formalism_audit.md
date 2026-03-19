# LQC Quantization-Ambiguity / Perturbation-Formalism Audit

**Created:** 2026-03-18
**Status:** ACTIVE
**Priority:** #1 among all LQC-specific openings

---

## The Four LQC Perturbation Formalisms

### 1. Dressed-Metric Approach (Agullo, Ashtekar, Nelson)

**Core idea:** Perturbations propagate on a quantum-corrected background geometry. The effective metric incorporates quantum fluctuations of the background via a "dressed" metric that the perturbation modes see.

**Technical implementation:**
- Background evolves via the effective LQC Friedmann equation: H^2 = (8piG/3) rho (1 - rho/rho_c)
- The Mukhanov-Sasaki equation receives corrections through an effective mass term z''/z that differs from the classical expression near the bounce
- The quantum-corrected z''/z suppresses tensor modes relative to scalar modes

**Key predictions:**
- r ~ 10^-4 for the Wilson-Ewing model (tensor suppression)
- n_s receives negligible corrections at observable k (quantum corrections confined to k ~ k_LQC)
- Power spectrum at intermediate k shows distinctive LQC oscillations

**Literature:** Agullo, Ashtekar, Nelson, PRL 109 (2012) 251301; CQG 30 (2013) 085014; Wilson-Ewing, CQG 29 (2012) 215013; CQG 30 (2013) 035011

**Status in our program:** This is what we use. The r ~ 10^-4 prediction and the n_s robustness come from this formalism.

### 2. Hybrid Approach (Fernandez-Mendez, Mena Marugan, Olmedo)

**Core idea:** Quantize the homogeneous background with LQC (polymer quantization), but quantize perturbations with standard Fock space quantum field theory. The two sectors interact through a Born-Oppenheimer-like separation.

**Technical implementation:**
- Same background evolution (same effective Friedmann equation)
- Perturbation Hamiltonian derived from the full Hamiltonian constraint after the homogeneous-inhomogeneous split
- The perturbation equation differs from the dressed-metric one in the effective mass term, particularly in the regularization of the terms containing 1/a^n (inverse-volume corrections)

**Key predictions:**
- Agrees with dressed-metric in the UV (short wavelengths, k >> k_LQC)
- Agrees with dressed-metric in the deep IR (very long wavelengths, k << k_LQC) for the power spectrum
- Can differ at intermediate k (near the bounce scale)
- The vacuum prescription at the bounce can differ

**Literature:** Fernandez-Mendez, Mena Marugan, Olmedo, PRD 86 (2012) 024003; PRD 89 (2014) 044041; Castelló Gomar, Mena Marugan, Martin de Blas, PRD 93 (2016) 104025

**Status in our program:** NOT used. The question is whether it would give a different f_NL.

### 3. Deformed Algebra Approach (Bojowald, Paily)

**Core idea:** Instead of fixing the quantization of the Hamiltonian constraint and deriving effective equations, modify the classical constraint algebra to include quantum corrections. The modified algebra generates effective equations that differ from the dressed-metric and hybrid approaches.

**Technical implementation:**
- The Dirac algebra of constraints receives quantum corrections: {H[N], H[M]} = D[...] with modified structure functions
- The resulting effective equations have different correction terms
- Known compatibility issue: the modified algebra may not close consistently in some regimes

**Key issues:**
- The modified algebra approach has been criticized for potential violations of general covariance (Bojowald, Paily, PRD 86 (2012) 104018, but see Cailleteau et al. PRD 86 (2012) 087301 for defense)
- Less used for phenomenology due to these technical controversies
- Some results appear incompatible with dressed-metric and hybrid in the UV

**Status in our program:** DEPRIORITIZED. Technical controversies make it less reliable for predictions. Do not invest time unless forced by results from #1 and #2.

### 4. Separate Universe Approach

**Core idea:** For superhorizon modes (k << aH), each Hubble patch evolves as a separate FRW universe. Perturbations are encoded as differences in the local expansion history. The delta-N formalism relates perturbations to differences in the number of e-folds.

**Technical implementation:**
- Valid only when spatial gradients are negligible (superhorizon limit)
- Each patch evolves with the same LQC effective Friedmann equation but different initial conditions
- f_NL computed from the nonlinear delta-N formula: f_NL = (5/6) N_phiphi / (N_phi)^2

**Key limitation for bouncing cosmologies:**
- The standard delta-N formalism assumes zeta is conserved on superhorizon scales. In matter contraction, zeta GROWS on superhorizon scales (the growing mode).
- The growing mode invalidates the standard delta-N and requires the extended Salopek-Bond gradient expansion.
- For the BISPECTRUM, mode-coupling effects at the bounce may not be captured by the separate universe approach.

**Status in our program:** Useful as a cross-check. Our modes ARE deeply superhorizon (k/k_bounce ~ 10^-56), so the separate-universe picture applies for the power spectrum. For the bispectrum, it needs careful treatment of the growing mode.

---

## What the 2024 Comparison Paper Shows (arXiv:2405.12296)

**Paper:** Agullo, Ashtekar, Gupt (2024), comparison of dressed-metric and hybrid perturbation formalisms in LQC.

### Agreements:
- Both formalisms give the same background evolution (same effective Friedmann equation, same bounce).
- Both agree in the UV (k >> k_LQC): quantum corrections vanish at short wavelengths.
- Both agree in the deep IR (k << k_LQC) for the power spectrum: superhorizon modes are unaffected by the quantum bounce.
- Both give the same qualitative picture: tensor suppression, scalar near-invariance for the matter bounce.

### Differences:
- **Initial-state prescriptions:** The two formalisms motivate different vacuum prescriptions at the bounce. The dressed-metric approach defines a natural vacuum via the quantum-corrected geometry. The hybrid approach defines a vacuum via the Fock space for perturbations on the quantum background. These can differ.
- **Infrared behavior of quantum corrections:** The intermediate-k regime (modes that are near-horizon at the bounce) receives different corrections in the two formalisms. The effective mass terms z''/z differ in their bounce-era behavior.
- **Regularization near the bounce:** The dressed-metric uses quantum-geometry-corrected expressions for the background quantities. The hybrid uses the standard expressions evaluated on the effective trajectory. Near the bounce (where rho ~ rho_c), these differ.

### Implications for observable modes:
- For modes relevant to CMB (k ~ 0.002 - 0.2 Mpc^-1), these modes are superhorizon during the bounce by many orders of magnitude (k/k_bounce ~ 10^-56 for k ~ 0.01 Mpc^-1 with standard LQC parameters).
- The differences between formalisms are confined to k ~ k_LQC.
- Observable modes are far from the difference region.

### Critical gap: The paper compares POWER SPECTRUM only. No bispectrum comparison exists.

---

## Analysis: Does Ambiguity Affect Our Observables?

### Power spectrum (n_s, r):

For k << k_LQC: both formalisms agree. Quantum corrections are negligible at these scales. The mode evolution is determined by the classical contraction dynamics, which are the same in both approaches.

This is well-established. The differences documented in arXiv:2405.12296 occur at k ~ k_LQC, which is ~10^56 above observable k.

**Our n_s = 0.964 and r ~ 10^-4 are ROBUST to formalism choice.**

**Verdict: SETTLED -- no ambiguity at observable k.**

### Bispectrum (f_NL):

The situation is more subtle:

1. **Pre-bounce generation:** f_NL = -35/8 comes from matter contraction dynamics. This is purely classical (no quantum corrections during the contraction phase far from the bounce). Both formalisms agree here.

2. **Bounce transmission:** The pre-bounce bispectrum must be transmitted through the quantum bounce to the expanding phase. This is where formalism differences COULD matter.

3. **Leading-order argument:** For superhorizon modes (k << k_LQC), the bounce is effectively instantaneous. The zeta modes evolve continuously through the bounce (no discontinuity in the effective equations). At leading order, the bispectrum transfer coefficient should be 1.

4. **Next-order corrections:** At next order in k/k_LQC, quantum corrections during the bounce could modify the transfer. These corrections:
   - Scale as (k/k_LQC)^2 ~ 10^-112 for CMB-relevant modes
   - Are completely negligible by any measure
   - BUT: the dressed-metric and hybrid approaches regularize the bounce-era equations differently
   - The question is whether these different regularizations produce different O(1) corrections at third order

5. **The real question:** Is there a third-order interaction during the bounce that is NOT suppressed by k/k_LQC? This could happen if the nonlinear coupling involves the background curvature (which IS large at the bounce) rather than the mode wavenumber. If such a term exists, it would couple to ALL modes regardless of k, and could be formalism-dependent.

**Nobody has computed this.** Not in dressed-metric, not in hybrid, not in any formalism.

**Verdict: OPEN -- but likely negligible for superhorizon modes. The key unknown is whether any unsuppressed third-order interaction exists at the bounce.**

### The honest assessment:

- **Most likely (85%):** Dressed-metric and hybrid give the SAME f_NL for observable modes. The quantum corrections are negligible at k << k_LQC, and the pre-bounce bispectrum passes through unchanged. Both formalisms agree because they agree on the classical dynamics that generate f_NL.

- **Less likely but important (15%):** A formalism-dependent third-order interaction exists at the bounce that is NOT k-suppressed. This would produce different f_NL values in the two formalisms and would constitute a genuinely testable quantum-gravity statement.

- **Even the 85% outcome is valuable:** It closes the ambiguity, raises prediction confidence from 75% to ~90%+, and constitutes a publishable robustness result ("LQC matter-bounce f_NL is formalism-independent").

---

## Does Our Live Model Depend on a Particular Formalism?

### Wilson-Ewing quasi-dust model:

| Observable | Formalism dependence | Notes |
|-----------|---------------------|-------|
| n_s = 0.964 | NONE (classical contraction) | Both formalisms give same classical dynamics |
| r ~ 10^-4 | WEAK (dressed-metric specific) | Hybrid may give different r, but r is untestable at 10^-4 anyway |
| f_NL = -35/8 | UNKNOWN (pre-bounce is same, transfer untested) | This is the key question |
| BKL resolution | NONE (ekpyrotic pre-phase) | Classical, no quantum corrections |

**Conclusion:** The model is weakly formalism-dependent. The main risk is NOT to f_NL itself (which is generated pre-bounce) but to the theoretical consistency argument that the pre-bounce prediction survives the bounce.

If the two formalisms give different transfer coefficients at third order, the prediction becomes: "f_NL = -35/8 in the dressed-metric formalism, f_NL = X in the hybrid formalism." This would reduce the prediction from "parameter-free" to "formalism-conditional" -- still testable, but weaker.

---

## Is This the Strongest Remaining LQC-Specific Opening?

**Yes, but with an important caveat.**

**Why it is the strongest:**
- Cleanest question: Does formalism choice matter for f_NL?
- Every outcome is informative and publishable.
- Bounded effort: literature audit + separate-universe calculation.
- Directly impacts the flagship prediction.

**The caveat:** The most likely answer is "no difference at observable scales." This is valuable (robustness confirmation) but not exciting. The 15% chance of a genuine difference is what makes it worth doing -- that 15% is where the LQC-specific content lives.

**Comparison with alternatives:**
- PBH channel (Opening 9): potentially more exciting but harder and may be dead for smooth LQC bounce.
- Third-order transfer (Opening 10): more technically demanding, expected null result at leading order.
- Ekpyrotic two-field (Opening 7): interesting but adds complexity, may weaken rather than strengthen the prediction.

---

## Concrete Next Steps

### Step 1: Literature audit (immediate)
- Search for ANY paper that computes f_NL through an LQC bounce in EITHER formalism.
- If found: extract the comparison. Check whether it applies at k << k_LQC.
- If not found: confirm this is a genuine gap. The gap itself is the finding.

### Step 2: Separate-universe estimate (1-2 sessions)
- Use the effective Friedmann equation H^2 = (8piG/3) rho (1 - rho/rho_c) in the gradient expansion.
- Compute the transfer of the bispectrum through the bounce for superhorizon modes.
- Do this once with dressed-metric effective mass, once with hybrid effective mass.
- Compare the two values of the post-bounce f_NL.

### Step 3: Document and decide (1 session)
- If agree: write up as robustness result. Move to Opening 10.
- If disagree: quantify the difference. This IS the paper's strongest LQC-specific result.

---

## Expected Timeline

| Step | Effort | Output |
|------|--------|--------|
| Literature audit | 1 session | Confirmed gap or existing result |
| Separate-universe calculation | 1-2 sessions | f_NL transfer in both formalisms |
| Documentation | 1 session | Publishable result either way |
| **Total** | **3-4 sessions** | **Formalism question resolved** |
