# Track B -- PBH-like Relic / Compact-Seed Channel

## Model-to-Observable Map

**Date**: 2026-03-12
**Status**: FUTURE WORK ONLY
**Author**: Houston Golden (with Claude Code assistance)

---

## 1. Executive Summary

**Verdict: FUTURE WORK ONLY**

The spin-torsion bounce cosmology framework has **no direct mechanism** for producing primordial black holes (PBHs) in our universe. The bounce mechanism creates baby universes *inside* existing black holes; it does not generate compact objects in the observable cosmos. No legitimate likelihood connecting this framework to PBH observables can be constructed at present. This document explains why, surveys what would be needed, and catalogs the public constraint datasets that would become relevant if a production mechanism were ever derived.

---

## 2. Does the Framework Have Any Direct Connection to PBH Formation?

### 2.1 What the Framework Actually Does

The core equations are:

- **Modified Friedmann equation**: H^2 = (8piG/3) rho [1 - rho/rho_crit], with rho_crit ~ 0.41 rho_Pl
- **Four-fermion contact interaction**: L_int = -(3piG/2) [gamma^2/(gamma^2+1)] J^mu_A J_{A mu}
- **Effective dark energy**: Lambda_obs = (alpha/M) D_inf ~ (2.3 meV)^4

The modification to the Friedmann equation is a quantum gravity correction that activates **only** at densities approaching rho_Pl ~ 5.16 x 10^93 g/cm^3. At all astrophysical and cosmological densities relevant to PBH formation (rho << rho_Pl), the equation reduces identically to standard GR.

### 2.2 Why There Is No PBH Channel

PBH formation requires one or more of the following:

1. **Enhanced curvature perturbations** on specific comoving scales during inflation (the standard mechanism). Requires P_R(k) ~ 10^{-2} on small scales, seven orders of magnitude above the CMB-constrained amplitude P_R ~ 2 x 10^{-9}.
2. **First-order phase transitions** producing bubbles that collapse to black holes.
3. **Cosmic string loops** or other topological defects.
4. **Domain wall collapse** from symmetry-breaking potentials.

The spin-torsion framework provides **none** of these:

- **No modified inflationary perturbation spectrum.** The paper explicitly states "we assume standard slow-roll inflation unmodified by parity violation" (Section 28, Limitations). The scalar power spectrum P_R(k) is unmodified.
- **No phase transitions.** The framework does not introduce new scalar fields with first-order transition potentials.
- **No topological defects.** There are no cosmic strings, domain walls, or monopoles in the model.
- **The bounce creates baby universes, not PBHs.** When matter collapses to Planck density inside a black hole, torsion repulsion triggers a bounce that creates a new expanding spacetime region *inside* the horizon. This child universe is causally disconnected from the parent. No compact remnant is deposited in the parent universe's matter content.

### 2.3 The Baby-Universe Distinction

This point deserves emphasis because it is the most common source of confusion:

| Process | What Happens | PBHs in Our Universe? |
|---------|-------------|----------------------|
| Stellar collapse in our universe | Star forms BH; baby universe may form inside | No -- the BH already exists as a standard astrophysical object |
| Quantum bounce at Planck density | New FRW-like expansion begins inside the BH interior | No -- the new spacetime is causally disconnected |
| Perturbation collapse in early universe | Standard GR process if P_R(k) is large enough | Requires enhanced perturbation spectrum, which the framework does not provide |

The framework says every black hole spawns an interior cosmos. This is a statement about black hole interiors, not about black hole production rates or mass functions.

---

## 3. What Would Be Needed to Establish a Connection?

To honestly connect this framework to PBH observables, the following theoretical work would be required (in order of logical priority):

### 3.1 Required Calculation: Modified Inflationary Perturbation Spectrum

**The critical missing piece.** One would need to:

1. Compute the scalar and tensor perturbation equations through the bounce, accounting for the modified Friedmann equation at near-Planck densities.
2. Show that the bounce-to-inflation transition imprints features on the primordial power spectrum P_R(k) -- specifically, an enhancement on small scales.
3. Derive the scale dependence: which comoving wavenumbers k are enhanced, and by how much?
4. Show that the enhancement reaches P_R(k) ~ O(10^{-2}) on at least some scale, which is the threshold for gravitational collapse to PBHs during radiation domination.

**Current status:** The paper acknowledges "the tensor perturbation spectrum through the bounce is not computed -- only quoted from Agullo et al." (peer review). No scalar perturbation calculation through the bounce exists in this work.

**Difficulty level:** Very high. This requires full numerical evolution of cosmological perturbations through a quantum bounce, which is an active research frontier in LQC (see Agullo, Ashtekar, Nelson 2012-2013; Agullo & Morris 2015; Zhu, Cleaver, Ashtekar 2017). Existing LQC calculations generally find that the bounce *suppresses* power on large scales rather than enhancing it on small scales, which would work *against* PBH formation.

### 3.2 Required Calculation: PBH Mass Function from Bounce Perturbations

Even if a modified P_R(k) were derived, one would then need:

1. The Press-Schechter or peaks-theory mass function: beta(M) = integral of P(delta > delta_c) over the appropriate smoothing scale.
2. The threshold delta_c for PBH formation, which depends on the equation of state at formation (delta_c ~ 0.45 for radiation domination in standard GR).
3. Whether the torsion four-fermion interaction modifies delta_c at any relevant density. (Almost certainly not -- the interaction is negligible at sub-Planck densities.)

### 3.3 Required Calculation: Torsion Effects on Collapse Threshold

A speculative but honest question: does the four-fermion repulsive interaction from torsion modify the PBH formation threshold? The interaction strength is:

L_int ~ G_N * n_fermion^2

At radiation-domination densities (rho ~ 10^{15} g/cm^3 for solar-mass PBH formation), this is suppressed by a factor of ~10^{-78} relative to the gravitational term. **The answer is no** -- torsion effects are utterly negligible at these densities.

### 3.4 Required Calculation: Could Bounce Dynamics Source Specific Defects?

A more creative (but highly speculative) route: could the bounce-to-inflation transition create topological defects that later collapse to PBH-like objects? This would require:

1. A symmetry-breaking pattern during or after the bounce.
2. A new scalar sector not present in the current framework.
3. Demonstration that the resulting defects have the right properties (mass, abundance, stability).

**This is entirely outside the current framework** and would constitute a major new model.

---

## 4. Survey of PBH Constraint Datasets

The following datasets constrain PBH abundance as a function of mass. They are real, public, and well-established -- but they are **useless for this framework** without a production mechanism (Sections 2-3 above).

### 4.1 Microlensing Constraints

| Dataset | Mass Range | Constraint (f_PBH upper limit) | Reference |
|---------|-----------|-------------------------------|-----------|
| EROS-2 (LMC/SMC) | 10^{-7} -- 15 M_sun | f < 0.04 (1 M_sun) | Tisserand+ 2007 |
| OGLE (Galactic bulge) | 10^{-6} -- 10^{-3} M_sun | f < 0.1 | Niikura+ 2019 |
| Subaru/HSC (M31) | 10^{-11} -- 10^{-6} M_sun | f < 0.01 (10^{-10} M_sun) | Croon+ 2020, Smyth+ 2020 |
| Kepler/K2 | 10^{-10} -- 10^{-7} M_sun | f < 0.3 | Griest+ 2014 |
| MACHO (LMC) | 0.1 -- 30 M_sun | f < 0.2 | Alcock+ 2001 |

### 4.2 CMB Accretion Constraints

| Dataset | Mass Range | Constraint | Reference |
|---------|-----------|-----------|-----------|
| Planck (CMB anisotropies) | 1 -- 10^4 M_sun | f < 10^{-3} (30 M_sun) | Ali-Haimoud & Kamionkowski 2017 |
| FIRAS (spectral distortions) | 10^4 -- 10^{13} M_sun | f < 10^{-5} (10^8 M_sun) | Nakama+ 2018 |

### 4.3 Gravitational Wave Constraints

| Dataset | Mass Range | Constraint | Reference |
|---------|-----------|-----------|-----------|
| LIGO/Virgo O3 merger rates | 1 -- 100 M_sun | f < 10^{-3} (dependent on mass function) | Abbott+ 2021 (GWTC-3) |
| LIGO/Virgo stochastic background | 0.1 -- 100 M_sun | f < 10^{-2} | Abbott+ 2022 |
| NANOGrav 15-yr | 0.1 -- 10 M_sun (induced GW from enhanced P_R) | Model-dependent | Afzal+ 2023 |
| LISA projections | 10^3 -- 10^7 M_sun | f < 10^{-5} (projected) | Bartolo+ 2019 |

### 4.4 Dynamical / Astrophysical Constraints

| Dataset | Mass Range | Constraint | Reference |
|---------|-----------|-----------|-----------|
| Wide binary disruption | 1 -- 10^3 M_sun | f < 0.1 | Monroy-Rodriguez & Allen 2014; but see recent debates |
| Ultra-faint dwarf heating | 10 -- 10^5 M_sun | f < 0.01 | Brandt 2016, Koushiappas & Loeb 2017 |
| Neutron star capture | 10^{-16} -- 10^{-10} M_sun | f < 0.1 | Capela+ 2013 |
| Lyman-alpha forest (Poisson) | > 10^3 M_sun | f < 0.01 | Murgia+ 2019 |

### 4.5 Evaporation Constraints (Hawking Radiation)

| Dataset | Mass Range | Constraint | Reference |
|---------|-----------|-----------|-----------|
| Extragalactic gamma-ray background | 10^{15} -- 10^{17} g | f < 10^{-8} | Carr+ 2010, Arbey+ 2020 |
| Galactic 511 keV line | ~10^{16} g | f < 10^{-4} | DeRocco & Graham 2019 |
| BBN (photodissociation) | 10^{9} -- 10^{13} g | f < 10^{-20} -- 10^{-10} | Carr+ 2021 |
| CMB spectral distortions (evaporation) | 10^{11} -- 10^{14} g | f < 10^{-8} | Acharya & Khatri 2020 |

### 4.6 Asteroid-Mass Window

The mass range 10^{17} -- 10^{22} g (roughly 10^{-16} -- 10^{-11} M_sun) remains the least constrained "open window" where PBHs could constitute all of dark matter. However, this window is narrowing with HSC/Subaru microlensing and femtolensing constraints.

---

## 5. Can Any Legitimate Likelihood Be Constructed?

### 5.1 Assessment

**No.** A likelihood requires:

1. A forward model: framework parameters --> PBH mass function f(M).
2. A data model: f(M) --> observable predictions (event rates, flux limits, etc.).
3. Noise/systematic model for each dataset.

Item (1) does not exist. The framework has no map from its parameters {gamma, alpha/M, D_inf, a_*, M_BH} to a PBH abundance or mass spectrum. Without a forward model, there is no predicted observable, and therefore no likelihood to evaluate.

Writing down a likelihood anyway -- for example, by parameterizing an arbitrary f(M) and fitting it to microlensing data -- would have **zero connection** to the spin-torsion framework. It would be generic PBH phenomenology unrelated to bounce cosmology.

### 5.2 What About Indirect Constraints?

One might ask: "Can PBH non-detection constrain the framework?" Only if the framework *predicted* PBHs. Since it does not, PBH constraints place no constraint on any framework parameter. The data and the model live in non-overlapping spaces.

### 5.3 Could Delta-N_eff Provide a Bridge?

The paper mentions Delta-N_eff ~ 0.2-0.5 from particle production at the bounce. If PBHs existed and evaporated, they would also contribute to N_eff. But:

- The MCMC best-fit gives Delta-N_eff ~ 0 (consistent with standard model).
- PBH evaporation contributions to N_eff require PBHs with mass < 10^9 g, which evaporate before BBN.
- Even if one forced this connection, the N_eff constraint would be on PBH abundance, not on the bounce parameters that are already constrained by CMB and BAO.

This is a dead end.

---

## 6. Recommendation

### FUTURE WORK ONLY

This track cannot proceed to forward modeling or MCMC. The theoretical prerequisites are absent.

### Required Before Any Progress

| Step | Description | Difficulty | Estimated Effort |
|------|------------|-----------|-----------------|
| 1 | Full scalar perturbation evolution through the quantum bounce | Very High | 1-2 years, requires numerical LQC expertise |
| 2 | Determine whether bounce imprints enhancement or suppression on P_R(k) at small scales | Very High | Depends on Step 1 |
| 3 | If enhancement exists: compute PBH mass function beta(M) | Moderate | Months, once P_R(k) is known |
| 4 | If beta(M) > 0: construct forward model and likelihoods | Moderate | Months |
| 5 | Fit to constraint datasets cataloged in Section 4 | Standard | Weeks-months |

### Honest Assessment of Prospects

Existing LQC perturbation calculations (Agullo, Ashtekar, Nelson; Wilson-Ewing; Zhu, Cleaver, Ashtekar) generally find that the bounce **suppresses** infrared power and does not produce the small-scale enhancement needed for PBH formation. If this result carries over to the spin-torsion variant, then Step 2 would yield a negative answer and the entire PBH channel would be closed permanently.

The most speculative possibility: the parity-odd operator (alpha/M) epsilon^{abcd} K_{ab} R_{cd} could, in principle, source an asymmetry between left- and right-helicity gravitational perturbations during the bounce-to-inflation transition. If this asymmetry were scale-dependent and coupled back to scalar modes at second order, it *might* modify P_R(k) on some scales. But this is three levels of speculation deep, with no calculation to support it.

### What This Track Should NOT Do

- Do not parameterize an arbitrary PBH mass function and claim it connects to the framework.
- Do not cite PBH constraint datasets as "constraints on the model" -- the model makes no PBH predictions.
- Do not conflate "every BH spawns a baby universe" with "the framework produces PBHs." These are categorically different statements.
- Do not claim that the torsion four-fermion interaction modifies PBH formation thresholds -- it is negligible at all relevant densities.

---

## 7. Summary Table

| Question | Answer |
|----------|--------|
| Direct connection to PBH formation? | **No** |
| Mechanism for enhanced P_R(k)? | **Not derived** |
| Modified collapse threshold from torsion? | **Negligible (suppressed by ~10^{-78})** |
| Legitimate likelihood constructible? | **No** |
| PBH constraints informative for framework? | **No** |
| Recommendation | **FUTURE WORK ONLY** |
| Prerequisite for progress | Full perturbation evolution through quantum bounce |
| Likely outcome if perturbations are computed | Suppression, not enhancement (based on existing LQC literature) |
