# 05 — Cosmological Relevance Assessment

**Date:** 2026-03-13
**Purpose:** Evaluate whether any propagating torsion mode could realistically influence cosmology, and if so, how.
**Status:** Assessment document (combines derived results with physical arguments)

---

## 1. The Central Question

From the mass spectrum calculation (04_mass_spectrum_calculation.md), ghost-free PGT torsion modes have masses:
```
m = M_Pl / (4 sqrt(pi |t_I|))
```

The question is: can any of these modes play a cosmological role?

There are four distinct scenarios, ordered by increasing ambition:

---

## 2. Scenario Analysis

### Scenario A: Heavy torsion (m >> TeV)

**Parameter range:** |t_I| < 10^{10}
**Mass range:** m > 10^{12} GeV

In this regime, the torsion modes decouple at energies well below the GUT scale. Integrating them out reproduces the standard ECH four-fermion interaction (with small corrections from the finite torsion propagator). No cosmological relevance.

**Assessment:** This is the generic expectation. If PGT couplings are O(1) in Planck units, we recover the minimal model — which we already tested and closed.

### Scenario B: Intermediate torsion (eV–MeV scale)

**Parameter range:** 10^{40} < |t_I| < 10^{50}
**Mass range:** meV < m < MeV

The torsion mode is light enough to mediate a long-range force. Depending on the mode:

**Model A (0+ scalar):** Mediates a spin-independent Yukawa force between fermions. This is a "fifth force" of gravitational strength (coupling ~ kappa ~ 1/M_Pl). Existing fifth-force bounds from torsion pendulum experiments (Eotvash), lunar laser ranging, and solar system tests constrain the range/coupling to:
- For gravitational-strength coupling: m > 10^{-3} eV (range < 0.2 mm) from sub-millimeter force tests.
- Solar system constraints rule out gravitational-strength scalars with m < 10^{-20} eV.

**Model B (0- pseudoscalar):** Mediates a spin-dependent force (axial coupling). Fifth-force bounds on spin-dependent interactions are weaker than spin-independent ones. A pseudoscalar with m ~ meV-eV could be consistent with existing bounds if its coupling is suppressed relative to gravitational strength.

**Model C (2+ tensor):** Massive spin-2 with gravitational coupling. This is essentially a massive graviton from the torsion sector. Stringent bounds from gravitational wave observations (LIGO/Virgo constraint: m_graviton < 1.2 x 10^{-22} eV).

**Assessment for cosmology:**
An eV-scale torsion mode would not directly explain dark energy (too heavy to produce w = -1 dynamics) but could:
- Contribute to dark matter if stable and produced in the early universe
- Modify structure formation through fifth-force effects
- Produce distinctive signatures in gravitational-wave observations (spin-2 case)

These are interesting but do NOT address the original dark-energy question. Foundation A's cosmological goal is specifically about dark energy.

### Scenario C: Dark-energy-scale torsion (m ~ meV)

**Parameter range:** |t_I| ~ 10^{55}
**Mass range:** m ~ meV ~ rho_Lambda^{1/4}

A torsion mode at the dark energy scale could potentially:

1. **Act as a quintessence-like field** if it has a slow-roll potential. However, the quadratic PGT action gives a simple mass term, not a flat potential. For m ~ H_0, the field would oscillate, giving effective w = 0 (matter-like, not dark-energy-like). For m << H_0, the field is frozen and gives w = -1, but this requires m < H_0 ~ 10^{-33} eV, not m ~ meV.

2. **Contribute to the vacuum energy** through its zero-point energy. But this brings us back to the cosmological constant problem: the zero-point contribution is ~ m^4 ~ (meV)^4 ~ 10^{-12} eV^4 ~ rho_Lambda. This is numerically correct but is just restating the coincidence — the torsion mass would need to be fine-tuned to the dark energy scale.

3. **Modify gravitational dynamics at large scales** through a Yukawa modification of gravity. The Yukawa range for m ~ meV is ~ 0.2 mm. This does not affect cosmological scales (Mpc).

**Assessment:** m ~ meV does not produce dark energy dynamics. It produces a coincidence between scales that is no more explanatory than the CC problem itself.

### Scenario D: Ultra-light torsion (m ~ H_0)

**Parameter range:** |t_I| ~ 10^{122}
**Mass range:** m ~ H_0 ~ 10^{-33} eV

A torsion mode with Compton wavelength ~ Hubble radius. This is the "fuzzy dark matter" / "ultra-light dark energy" regime.

**Behavior:**
- If m < H_0: the field is frozen at its initial value and behaves as an effective cosmological constant (w = -1). The vacuum energy is V(chi_0) ~ m^2 chi_0^2 / 2, which can match rho_Lambda if m chi_0 ~ (meV)^2. With m ~ H_0 and chi_0 ~ M_Pl, this gives V ~ H_0^2 M_Pl^2 ~ rho_Lambda. This is numerically correct.

- If m ~ few x H_0: the field begins oscillating at late times, giving a dynamical dark energy with time-varying w(z). This could produce the w(z) behavior hinted at by DESI DR2.

**The fundamental problem remains:** |t_I| ~ 10^{122} is as fine-tuned as the CC itself. Without a symmetry or mechanism that selects this value, we have transferred the hierarchy problem from Lambda to t_I.

---

## 3. The Shift-Symmetry Argument for Model B

Among the ghost-free models, the pseudoscalar (0-) mode of Model B has one structural advantage: pseudoscalars can have approximate shift symmetries.

### How this could work:

1. Posit a classical shift symmetry chi -> chi + const for the axial torsion.
2. This symmetry forbids a mass term at tree level: m = 0.
3. The mass is generated by non-perturbative effects (instantons, condensates) that break the shift symmetry, analogous to the QCD axion.
4. The non-perturbative mass is exponentially suppressed: m ~ Lambda_strong^2 / f, where f is the "decay constant" (analogous to f_a) and Lambda_strong is the scale of the symmetry-breaking dynamics.
5. For appropriate choices (f ~ M_Pl, Lambda_strong ~ 10^{-3} eV), one can get m ~ H_0.

### Why this is NOT automatic:

The quadratic PGT action does not have a shift symmetry for the axial torsion. The mass term t_3 A_mu A^mu is explicitly present. A shift symmetry would require:

1. Setting t_3 = 0 at tree level (by fiat or by a symmetry).
2. Showing that the mass is generated radiatively or non-perturbatively at a controlled (small) scale.
3. Demonstrating that the resulting mass is radiatively stable.

None of these steps has been carried out for PGT axial torsion. The analogy with the QCD axion is suggestive but not demonstrated.

### What would need to be true:

For the shift-symmetry argument to work in PGT, we would need:

1. A UV completion of PGT in which the axial torsion coupling t_3 = 0 is natural (e.g., protected by a higher symmetry of the gravitational action).
2. A non-perturbative mechanism (gravitational instantons? torsion tunneling?) that generates m_chi ~ H_0.
3. Radiative stability of m_chi under quantum corrections from both gravity and matter loops.

**Assessment:** This is a research program, not a result. It is the most promising direction within Foundation A, but it requires substantial new work beyond the scope of this Phase 1 assessment.

---

## 4. Comparison with Existing Light-Field Programs

Several established programs involve light fields coupled to gravity. How does PGT torsion compare?

| Program | Field | Mass protection | Dark energy mechanism | Status |
|---------|-------|----------------|----------------------|--------|
| QCD axion | Pseudoscalar | PQ symmetry | No (m ~ 10^{-5} eV) | Well-established |
| Ultralight axion (fuzzy DM) | Pseudoscalar | String landscape | DM, not DE | Active |
| Quintessence | Scalar | Tracking potential | Yes (w ≠ -1) | Active, no UV completion |
| **PGT 0- torsion** | **Pseudoscalar** | **Hypothetical shift sym.** | **Possible if m ~ H_0** | **This work** |
| PGT 0+ torsion | Scalar | None known | Unlikely | This work |
| dRGT massive gravity | Spin-2 | Nonlinear structure | Yes (m ~ H_0) | Active, vDVZ issue |
| **PGT 2+ torsion** | **Spin-2** | **None (BD ghost risk)** | **Too risky** | **Flagged** |

**The PGT 0- torsion (Model B) occupies a unique niche:** it is a geometric pseudoscalar from the gravitational sector itself, not an ad-hoc scalar field added by hand. If a shift symmetry can be established, it would be a genuinely geometric realization of quintessence — directly addressing Foundation A's original motivation.

---

## 5. Observational Signatures of Light PGT Torsion

If a light torsion mode exists, what would it predict?

### 0- pseudoscalar (Model B, most promising):
1. **Spin-dependent fifth force:** A_mu couples to the axial current. The induced potential between polarized fermions is Yukawa with range 1/m. For m ~ H_0, the range is cosmological.
2. **Parity violation in gravitational waves:** The axial coupling breaks parity, potentially producing gravitational-wave birefringence (different propagation speeds for left/right GW circular polarizations). This is testable with LISA and third-generation GW detectors.
3. **Cosmic birefringence:** If the 0- mode couples to the electromagnetic Chern-Simons term (analogous to axion-photon coupling), it would produce cosmic birefringence. Unlike the minimal ECH model where this coupling is absent, the PGT 0- mode might have a derived photon coupling through its gravitational interactions — this needs explicit calculation.
4. **Modified growth rate:** The fifth force modifies structure formation, potentially affecting sigma_8/S_8.

### 0+ scalar (Model A):
1. **Spin-independent fifth force:** Universal Yukawa modification of gravity.
2. **No parity violation:** The scalar is parity-even, so no birefringence signature.
3. **Solar system bounds:** Stringent for gravitational-strength coupling.

### 2+ tensor (Model C):
1. **Modified gravitational wave dispersion:** Massive graviton gives frequency-dependent GW speed.
2. **Boulware-Deser ghost risk:** Makes predictions unreliable.

---

## 6. Assessment: Cosmological Relevance

| Question | Answer | Confidence |
|----------|--------|------------|
| Can PGT torsion modes exist? | Yes (ghost-free regions confirmed) | High |
| Are any naturally light? | **No — requires fine-tuning or symmetry protection** | High |
| Is a shift symmetry possible for 0-? | Conceivable but undemonstrated | Low |
| Could a light 0- produce dark energy? | In principle, if m < H_0 and initial conditions set V ~ rho_Lambda | Speculative |
| Would a light 0- produce distinctive signatures? | Yes: GW birefringence, spin-dependent force, possibly CMB birefringence | Moderate |
| Does this resolve the CC problem? | **No — it transfers the hierarchy to the torsion coupling** | High |

**Bottom line:** Propagating torsion in PGT can provide a cosmological degree of freedom, but it does not solve the cosmological constant problem by itself. It provides a geometric framework in which a light pseudoscalar (the axial torsion mode) could play the role of dark energy — but the smallness of its mass requires explanation. The structural advantage over generic quintessence is the geometric origin and the parity-odd coupling structure, which connects to the birefringence program. The structural disadvantage is the absence of a demonstrated mass-protection mechanism.

---

## 7. Verdict for Foundation A

Foundation A does NOT close at this stage. The PGT framework provides:
- Confirmed ghost-free propagating torsion modes
- A clear mass spectrum
- A candidate mode (0- pseudoscalar) with the right structural properties for cosmological relevance

But Foundation A does NOT deliver dark energy from first principles. The torsion mass hierarchy is a new version of the old problem. The path forward requires:
1. Investigate whether a shift symmetry for axial torsion is compatible with PGT
2. If yes, compute the non-perturbatively generated mass
3. Check radiative stability
4. Compute the photon coupling (if any) and predict birefringence
