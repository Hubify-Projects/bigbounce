# Final Gate Results: Exact Torsion Elimination with Dynamical Immirzi Field

**Date:** 2026-03-16
**Calculation:** All-orders torsion elimination, gamma(x) = gamma_0 + phi(x)/f_phi
**Status:** COMPLETE

---

## VERDICT: DYNAMICAL_IMMIRZI_GENERIC_ALP

The dynamical Barbero-Immirzi field, after exact torsion elimination to all
orders in phi/f_phi, produces an effective action that is EXACTLY within the
operator basis of a generic axion-like particle (ALP) EFT. No new operator
appears. No observationally testable ECH-specific signature exists.

---

## What Exact Elimination Produces

### Operators generated:

1. **Non-canonical kinetic term:** [1/2 + Z_T(gamma_0 + phi/f_phi)](partial phi)^2
   - Z_T is a known rational function of its argument
   - Can be canonically normalized by field redefinition phi -> chi
   - Result: standard kinetic term with modified effective couplings

2. **Derivative coupling:** C_1(gamma_0 + phi/f_phi) * (1/f_phi) * partial_mu phi J^{5,mu}
   - C_1 is a known rational function
   - Leading term: standard ALP-fermion coupling with effective f_eff
   - Subleading terms: phi^n (partial phi) J^5, suppressed by (phi/f_phi)^n

3. **Four-fermion coupling:** C_2(gamma_0 + phi/f_phi) * (kappa/4) * (J^5)^2
   - C_2 is a known rational function
   - Constant piece: standard Einstein-Cartan four-fermion (Planck-suppressed)
   - phi-dependent pieces: corrections to a Planck-suppressed operator

4. **Anomaly-induced photon coupling:** [alpha N_eff / (4 pi f_eff)] phi F Ftilde
   - From 1-loop ABJ triangle (universal, not from torsion elimination)
   - Identical to any ALP with derivative fermion coupling

### Operators NOT generated:

- No tree-level phi F Ftilde (photons do not see torsion)
- No tree-level phi F F (same reason)
- No higher-derivative operators (torsion elimination is algebraic)
- No non-local operators
- No operators outside the standard ALP basis

---

## Whether Any New Operator Appears

**NO.** Every operator in the torsion-eliminated action belongs to the standard
ALP EFT operator basis. The ECH derivation predicts specific Wilson coefficients
as functions of gamma_0, but does not extend the operator basis.

This result is a THEOREM, not an approximation. It follows from the fact that
torsion in ECH is non-propagating (algebraic equation of motion), so its
elimination cannot generate new dynamical structures. The available operators
are fixed by the field content (phi, psi, A_mu), the symmetries (Lorentz,
U(1) gauge, approximate shift), and dimensional analysis.

---

## Whether Birefringence Is ECH-Specific

**NO.** The birefringence prediction:

```
beta = [alpha N_eff / (8 pi)] * (Delta phi / f_eff) * (180/pi) ~ 0.13 deg
```

is numerically identical to the prediction of ANY ALP with:
- Derivative coupling to fermions at scale f_a ~ f_eff ~ M_Pl
- O(1) field excursion since recombination
- Ultralight mass m ~ 10^{-33} eV (for cosmological dynamics)

The ECH framework provides a MOTIVATION for f_a ~ M_Pl (from the geometric
identification gamma = gamma_0 + phi/f_phi with gamma ~ O(1)), but this
is a theoretical prior, not an observable distinction.

---

## What the ECH Framework Actually Contributes

### Positive contributions (theoretical):
1. A geometric motivation for the existence of an ultralight pseudoscalar
2. A natural scale f_phi ~ M_Pl from the Immirzi parameter identification
3. A restriction to anomaly-mediated photon coupling (no tree-level phi F Ftilde)
4. Specific (but unmeasurable) relations among Wilson coefficients

### What it does NOT contribute (observational):
1. No new operator in the low-energy EFT
2. No distinctive spectral or angular signature in birefringence
3. No measurable correction to the standard ALP predictions
4. No way to distinguish "Immirzi ALP" from "generic ALP with f_a ~ M_Pl"

### The structural reason:
The Immirzi parameter enters ONLY through the Holst term in the gravitational
action. After torsion elimination, the Holst term's contribution is absorbed
into the four-fermion coupling coefficient, which is Planck-suppressed. The
dynamical phi inherits this property: all ECH-specific corrections to the
standard ALP Lagrangian involve kappa ~ 1/M_Pl^2 and are unmeasurable.

The only non-Planck-suppressed effect is the derivative coupling itself,
which IS the standard ALP coupling. Its coefficient depends on gamma_0, but
gamma_0 is unknown, so this is just a free parameter.

---

## Recommended Next Move

### For the spin-torsion cosmology program:

**The program is COMPREHENSIVELY CLOSED.**

The complete barrier inventory:
- Foundations A-G: Seven structural barriers closing the DE program
- Branch Q Phase 1: Parity-violating observables reduce to generic ALP
- Branch Q Final Gate (this calculation): Exact elimination confirms no new operators

There is no remaining avenue within the ECH framework that could produce
distinctive low-energy observables. The mathematical structure is clear:
ECH-specific content lives at the Planck scale and is invisible in the
low-energy effective theory.

### For publication:

**Option A (recommended): Comprehensive closure paper.**
Add this result to Paper 1.2. The dynamical Immirzi field is the final
negative result. The paper establishes that the ECH framework, in all its
minimal extensions, reduces to known physics at low energies. This is a
clean, publishable no-go result.

**Option B: Generic ALP birefringence constraints.**
Use the existing MCMC infrastructure to constrain ALP parameters from
birefringence data. Publishable but not novel -- many groups are doing this.
The ECH motivation adds a paragraph of introduction but does not change the
analysis.

**Option C: Bounce-only pivot.**
The ECH framework may still be relevant at the Planck scale (bounce cosmology,
singularity avoidance). This requires different observables (tensor spectrum,
initial conditions for inflation). Completely separate from the DE and
birefringence programs.

---

## The Bottom Line

The dynamical Barbero-Immirzi field is a perfectly valid ultralight pseudoscalar.
It may well exist and may well produce the observed cosmic birefringence. But
there is nothing in its phenomenology that identifies it as coming from the
ECH framework rather than from any other UV completion that produces an ALP
with f_a ~ M_Pl.

The ECH framework provides a MOTIVATION for the field. It does not provide a
SIGNATURE.

This is the honest conclusion of the calculation. The final gate is closed.

---

## Verdict Summary

| Question | Answer |
|----------|--------|
| Does exact elimination produce new operators? | **NO** |
| Is birefringence ECH-specific? | **NO** (generic ALP prediction) |
| Are Wilson coefficient relations testable? | **NO** (Planck-suppressed or degenerate) |
| Is there ANY observable ECH signature? | **NO** |
| Is the dynamical Immirzi field ruled out? | **NO** (consistent with data, just not distinctive) |
| Final verdict | **DYNAMICAL_IMMIRZI_GENERIC_ALP** |
| Program status | **COMPREHENSIVELY CLOSED** |
| Recommended action | Add to Paper 1.2 as final closure result |
