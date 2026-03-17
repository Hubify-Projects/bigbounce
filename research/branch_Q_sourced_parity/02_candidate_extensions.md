# Branch Q: Candidate Parity-Violating Extensions

**Date:** 2026-03-16

---

## Candidate A: Gravitational Chern-Simons (dynamical CS gravity)

### Action term

```
S_CS = (1/16 pi G) integral theta(x) * R^{ab} wedge R_{ab}
     = (1/16 pi G) integral theta * (1/4) epsilon^{mu nu rho sigma} R^{alpha beta}_{mu nu} R_{alpha beta rho sigma} * sqrt(-g) d^4x
```

where theta(x) is a pseudoscalar field (possibly the promoted Barbero-Immirzi
parameter) and R^{ab} wedge R_{ab} is the Pontryagin density.

### New parameters

- f_CS: decay constant for theta (1 parameter)
- Optionally: V(theta) potential (adds more parameters)

### Observable channel

- **Chiral gravitational waves:** Different propagation speeds for left-
  and right-circular GW polarizations. Delta v / v ~ theta-dot / M_Pl.
- **TB/EB CMB correlations from tensor modes** (not from photon birefringence).
- **Modified GW dispersion** in LIGO/Virgo band for strong-field sources.

### Geometric motivation: MODERATE

This is well-studied theory (Jackiw-Pi 2003, Alexander-Yunes 2009). The
Pontryagin density is a natural geometric invariant. If theta is the promoted
Barbero-Immirzi parameter gamma(x), the coupling is geometrically natural.
However, this is NOT specific to ECH: dynamical CS gravity exists independently
of torsion and the Holst term.

### Known issues

1. **R-tilde R = 0 on exact FRW** (established in Branch H). The Pontryagin
   density vanishes on any conformally flat spacetime. This means:
   - No background evolution for theta from gravity alone on FRW
   - Chiral effects only arise at the PERTURBATION level (tensor modes)
   - Need theta-dot from a separate source (potential V(theta) or initial conditions)

2. **Strong-field constraints:** Binary pulsar observations constrain
   the CS coupling at xi^{1/4} < 8.5 km (Ali-Haimoud-Chen 2011).
   LIGO constraints: xi^{1/4} < O(10) km (Yunes et al. 2016).

3. **Not a complete theory:** The field equations are third-order (C-tensor).
   Only the non-dynamical limit (theta = linear in time) is ghost-free in
   the standard formulation.

### Assessment: VIABLE BUT NOT ECH-SPECIFIC

The theory works and produces chiral GWs, but it is standard dynamical CS
gravity. The ECH origin adds nothing beyond a motivational story for why
theta exists. Any pseudoscalar coupled to the Pontryagin density gives the
same physics.

---

## Candidate B: Standard ALP with phi F F-tilde, bounce-sourced

### Action term

```
S_ALP = integral [ (1/2)(partial phi)^2 - V(phi) - (1/4 f_a) phi F_{mu nu} F-tilde^{mu nu} ] sqrt(-g) d^4x
```

### New parameters

- f_a: axion decay constant (1 parameter)
- m_a: axion mass (from V(phi), 1 parameter)
- theta_0: initial misalignment angle (1 initial condition)

### Observable channel

- **Cosmic birefringence:** beta = (Delta phi) / (2 f_a) over the photon
  propagation path. Observed: beta ~ 0.35 +/- 0.09 degrees.
- **Frequency-independent** (isotropic) birefringence for uniform phi roll.
- **Anisotropic birefringence** for phi fluctuations.

### Geometric motivation: NONE

This is standard ALP phenomenology. The bounce could in principle set the
initial misalignment angle theta_0, but Branch N showed that the bounce
modifies the axion angle by Delta theta ~ 10^{-96} radians. The ALP does
not know the bounce happened.

### Known constraints

The birefringence observation beta ~ 0.35 deg requires:
```
Delta phi / f_a ~ 0.012 radians
```
For an ultralight ALP with m_a ~ 10^{-33} eV (dark energy scale), this is
natural. For heavier ALPs, phi must be slowly rolling at late times.

The coupling f_a ~ 10^{8} - 10^{12} GeV is the standard ALP window.

### Assessment: WORKS BUT GENERIC

This explains birefringence perfectly. It has no ECH content whatsoever.
If the project pivots here, it becomes a standard ALP constraints paper
using the existing MCMC infrastructure.

---

## Candidate C: Dynamical Barbero-Immirzi Field (Torsion-Axion Mixing)

### Action term

Promote the Barbero-Immirzi parameter to a pseudoscalar field:
gamma -> gamma_0 + phi(x) / f_phi

The Holst term becomes:

```
S_Holst = (1/2 kappa) integral (1/gamma(x)) * e^I wedge e^J wedge F_{IJ}
```

where F_{IJ} is the curvature 2-form. In the Palatini formulation, integrating
out the connection yields:

```
S_eff = S_{GR}[g] + S_{matter}
      + integral [ (1/2)(partial phi)^2 - V(phi) ] sqrt(-g) d^4x
      + integral (phi / f_phi) * N_4      [Nieh-Yan coupling]
      - (kappa/4) integral C(gamma, phi) * (J^5)^2 sqrt(-g) d^4x
```

where N_4 = T^I wedge T_I - R_{IJ} wedge e^I wedge e^J is the Nieh-Yan
4-form, and C(gamma, phi) is a phi-dependent version of the torsion
elimination coefficient.

### New parameters

- f_phi: decay constant for the Immirzi field (1 parameter)
- V(phi): potential for the Immirzi field (instanton-generated, adds m_phi)
- Total: 2 new parameters (f_phi, m_phi)

### Observable channel

The key question: does phi couple to F F-tilde (photon birefringence)?

**Direct coupling:** NO. The Nieh-Yan term couples phi to T^I wedge T_I
and R_{IJ} wedge e^I wedge e^J, not to the EM field strength.

**Induced coupling through fermion loops:** The phi-(J^5)^2 vertex,
combined with the ABJ anomaly triangle (Branch S), generates an effective
phi-F-F-tilde coupling at two loops. The question is the STRENGTH.

**Derivative coupling:** After torsion elimination, phi acquires a
derivative coupling to the fermion axial current:
```
L_deriv ~ (1/f_phi) partial_mu phi * J^{5,mu}
```
This is the standard ALP-fermion coupling. Through the ABJ anomaly, it
generates:
```
L_eff ~ (alpha / 4 pi f_phi) * phi * F F-tilde
```
This is the STANDARD ALP birefringence mechanism with the identification
f_a = 4 pi f_phi / alpha.

### Geometric motivation: HIGH

This is the most geometrically natural extension:
- gamma is already in the ECH action (Holst term)
- Promoting gamma to a field is the minimal dynamical extension
- The Nieh-Yan coupling is geometrically determined (not ad hoc)
- The approach has precedent: Taveras-Yunes (2011), Calcagni-Mercuri (2009)
- LQG: gamma determines the area gap; a dynamical gamma has implications
  for quantum geometry

### Known issues

1. **Foundation B result:** The Nieh-Yan coupling in metric-affine gravity
   IS non-topological, but the Topological-Shift Duality means mass protection
   and geometric content are mutually exclusive for linear couplings.

2. **After torsion elimination:** phi couples to fermions as a standard
   ALP with derivative coupling (1/f_phi) partial phi * J^5. The geometric
   origin is invisible at low energies.

3. **The induced phi F F-tilde coupling is the STANDARD ALP coupling.**
   The ABJ anomaly does not know where the axial coupling came from.
   The operator alpha/(4 pi f_phi) * phi F F-tilde is the same whether
   phi is a QCD axion, a string axion, or the Immirzi field.

4. **The phi-dependent four-fermion term** C(gamma, phi) * (J^5)^2 is
   formally new, but it is Planck-suppressed (kappa ~ 1/M_Pl^2) and
   parity-EVEN (it modifies the strength of the existing parity-even
   interaction, not its symmetry).

### Assessment: GEOMETRICALLY MOTIVATED BUT PHENOMENOLOGICALLY GENERIC

The Immirzi field is the most natural pseudoscalar in the ECH framework.
It does produce birefringence -- but through the STANDARD ALP mechanism
(derivative coupling to J^5 -> ABJ anomaly -> phi F F-tilde). The coupling
strength is 1/f_phi, which is a FREE PARAMETER not determined by ECH
geometry.

The distinctive ECH content is:
- The ORIGIN of phi (promoted Immirzi parameter)
- The Nieh-Yan coupling structure (specific to torsional geometry)
- The phi-dependent (J^5)^2 modification (new but Planck-suppressed)

None of these produce a DISTINCTIVE OBSERVABLE PREDICTION different from
a generic ALP with the same (f_phi, m_phi).

---

## Candidate D: Explicit phi F F-tilde (Standard ALP Photon Coupling)

### Action term

```
S = integral [ (1/2)(partial phi)^2 - V(phi) - (g_{phi gamma} / 4) phi F_{mu nu} F-tilde^{mu nu} ] sqrt(-g) d^4x
```

### New parameters

- g_{phi gamma}: dimensionful coupling (1/f_a) (1 parameter)
- m_phi: mass from V(phi) (1 parameter)

### Observable channel

- Cosmic birefringence: beta = g_{phi gamma} Delta phi / 2
- Spectral distortions, photon-ALP oscillations

### Geometric motivation: NONE

This is the standard ALP-photon coupling with no ECH content. It is listed
for completeness as it is what the birefringence observation most directly
points to.

### Assessment: WORKS, COMPLETELY GENERIC

This is the baseline. Any extension that reduces to this after field
elimination is phenomenologically equivalent to it.

---

## Candidate E: Explicit Parity-Breaking Torsion Mass Term

### Action term

Add to the PGT Lagrangian:

```
S_PV = integral [ lambda * S_mu * V^mu ] sqrt(-g) d^4x
```

where V^mu is either:
- A fixed cosmological vector (breaks Lorentz invariance)
- The 4-velocity u^mu of the cosmological frame (preserves spatial isotropy)
- The gradient of a background field partial^mu Phi

Or alternatively, a linear torsion-matter coupling:

```
S_linear = integral [ lambda * S_mu * J^{5,mu} ] sqrt(-g) d^4x
```

that explicitly breaks the Z_2 symmetry phi -> -phi protecting the
pseudoscalar vacuum.

### New parameters

- lambda: parity-violating coupling (1 parameter)
- Possibly: V^mu specification (additional structure)

### Observable channel

- Populates the pseudoscalar torsion mode S_0 != 0 (defeats Barrier 14)
- If S_0 oscillates with m_T ~ eV scale, could produce dark radiation
- If S_0 is ultralight, could produce birefringence through phi-matter coupling

### Geometric motivation: LOW

This is explicitly ad hoc. A fixed vector V^mu breaks Lorentz invariance
(or requires additional structure). A linear S*J^5 coupling is technically
natural (dimension-4 operator) but has no geometric origin within ECH.

### Known issues

- Lorentz violation is tightly constrained (SME bounds)
- The linear coupling lambda S_mu J^5_mu modifies the torsion elimination:
  S_mu = -(kappa/4) C(gamma) J^5_mu + (lambda/m_T^2) J^5_mu, which just
  rescales the four-fermion coupling. Not qualitatively new.
- Without propagating torsion (m_T -> infinity), the S_0 field does not
  exist and the population question is moot.

### Assessment: AD HOC, DOES NOT SOLVE THE PROBLEM

Breaking parity by hand does not provide geometric insight. If you must
add an explicit parity-breaking term, you might as well add phi F F-tilde
directly (Candidate D) and skip the geometric pretense.

---

## Candidate F: Nieh-Yan Coupled Pseudoscalar with Instanton Potential

### Action term

This is a refinement of Candidate C, using the Foundation B result that
the Nieh-Yan form is non-topological in metric-affine gravity:

```
S = S_{MAG} + integral [ (1/2)(partial phi)^2
    + (phi / f_phi) * (N_4 + Q_{AB} wedge e^B wedge T^A)
    - Lambda_inst^4 cos(phi / f_phi) ] sqrt(-g) d^4x
```

where the instanton potential provides a technically natural mass:
m_phi^2 = Lambda_inst^4 / f_phi^2.

### New parameters

- f_phi: decay constant (1 parameter)
- Lambda_inst: instanton scale (1 parameter)
- Total: 2 new parameters

### Observable channel

Same as Candidate C: birefringence through the induced ALP-photon coupling.

### Geometric motivation: MODERATE-HIGH

Uses the non-topological Nieh-Yan correction (Foundation B positive result).
But the Topological-Shift Duality (also Foundation B) applies: the
non-topological part of N_4 breaks the shift symmetry of phi, so the
instanton mass is not the only source of mass. The geometric coupling
itself contributes a mass term, potentially spoiling naturalness.

### Assessment: REFINEMENT OF C, SAME PHENOMENOLOGICAL OUTCOME

After field elimination, this reduces to a standard ALP with coupling
~ alpha/(4 pi f_phi) to photons. The non-topological Nieh-Yan correction
vanishes on FRW (T = 0 in the cosmological background, established in
Foundation B Phase 2). No distinctive prediction beyond generic ALP.

---

## Candidate G: Parity-Odd Torsion Bilinear in PGT

### Action term

In the Poincare gauge theory with 10 independent torsion parameters,
there exist parity-odd invariants:

```
L_PO = beta_4 * T^{[abc]} * T_{abc} (totally antisymmetric part, but this is parity-EVEN)
```

Actually, the parity-odd torsion bilinears are:

```
L_PO = sum_I c_I * epsilon^{abcd} T_{ab}^e T_{cde}
```

These contract a torsion tensor with its dual. The only independent
parity-odd bilinear is:

```
L_PO = c_PO * epsilon^{mu nu rho sigma} T^alpha_{mu nu} T_{alpha rho sigma}
```

### New parameters

- c_PO: parity-odd torsion coupling (1 parameter, dimensionless)

### Observable channel

- Modifies torsion propagator to split left/right modes
- Could produce chiral GW background if torsion is propagating
- Could modify tensor perturbation spectrum

### Geometric motivation: HIGH within PGT

This is a legitimate term in the PGT Lagrangian, often included in complete
analyses (Hayashi-Shirafuji, Yo-Nester). It is geometrically natural as a
parity-odd invariant of the torsion tensor.

### Known issues

- Requires propagating torsion (PGT, not minimal EC)
- Ghost-free conditions in PGT with parity-odd terms are restrictive
  (Nester-Yo 1999, Karananas 2014)
- The parity-odd torsion bilinear epsilon T T is actually proportional
  to the Nieh-Yan density dN_4 in certain decompositions
- Does not directly produce PHOTON birefringence (couples to gravity sector)
- Chiral GW signature requires propagating torsion with m_T accessible to
  GW detectors

### Assessment: INTERESTING BUT DIFFERENT PROGRAM

This is a legitimate PGT extension but opens a different research program
(chiral GW from torsion, not photon birefringence). It does not directly
address the birefringence observation and requires the full PGT machinery
with its own ghost/stability constraints.

---

## Summary Table

| Candidate | New params | Geometric? | Observable | ECH-specific? | Viable? |
|-----------|-----------|------------|------------|--------------|---------|
| A: Grav CS | 1 (f_CS) | Moderate | Chiral GWs | NO (standard dCS) | YES but not ECH |
| B: Standard ALP | 2 (f_a, m_a) | None | Birefringence | NO | YES but generic |
| C: Dynamical Immirzi | 2 (f_phi, m_phi) | HIGH | Birefringence | Origin only | YES but reduces to ALP |
| D: Explicit phi FF-tilde | 2 (g, m) | None | Birefringence | NO | YES but generic |
| E: Explicit PV mass | 1 (lambda) | Low | Populations S_0 | NO | MARGINAL |
| F: Nieh-Yan + instanton | 2 (f_phi, Lambda) | Moderate-High | Birefringence | Vanishes on FRW | Reduces to C |
| G: PGT parity-odd | 1 (c_PO) | High (in PGT) | Chiral GWs | Possibly | Different program |
