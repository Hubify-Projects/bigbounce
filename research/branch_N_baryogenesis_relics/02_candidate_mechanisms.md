# Branch N: Candidate Mechanisms

**Date:** 2026-03-16

---

## Candidate A: Torsion-Induced Axial Chemical Potential for Baryogenesis

### Basic Interaction

In Einstein-Cartan theory with fermions, integrating out
non-propagating torsion yields the effective Lagrangian:

```
L_eff = L_GR + L_Dirac - (3kappa/16) * 1/(1 - 3gamma^2 kappa xi^2) * (J^5_mu)^2
```

where J^5_mu = psi-bar gamma_mu gamma_5 psi is the axial current.

In a thermal/dense fermion medium with net chirality n_5 = n_R - n_L,
the temporal component J^5_0 = n_5 acts as an effective axial chemical
potential:

```
mu_5^eff = (3kappa/8) * n_5 / (1 - 3gamma^2 kappa xi^2)
```

This mu_5^eff is a CPT-odd background if n_5 != 0, and can bias
baryon-number-violating processes (sphalerons) to produce a net
baryon asymmetry.

### Bounce/Torsion Ingredient

The (J^5)^2 interaction is the UNIQUE non-standard term from
spin-torsion gravity. At bounce densities (rho ~ M_Pl^4), the spin
density xi and fermion number density n_5 are both at their maximum
values, so the torsion-induced mu_5 is at its strongest.

### Why It Might Work

1. mu_5 couples to the chiral anomaly: partial_mu J^5_mu contains
   the SU(2) instanton density, which IS the sphaleron rate.
2. At T ~ M_Pl, the sphaleron rate Gamma_sph ~ alpha_W^5 T^4 is
   enormous.
3. The bounce provides both out-of-equilibrium conditions AND the
   maximal axial chemical potential simultaneously.

### Biggest Theoretical Risk

**The (J^5)^2 interaction is parity-EVEN.** The product of two
pseudovectors is a scalar. mu_5^eff by itself does not violate CP --
it only BIASES existing CP-violating processes. If the CP violation
comes entirely from CKM/PMNS phases (standard model), then torsion
is merely enhancing a pre-existing mechanism, and the question is
whether the enhancement is quantitatively significant.

More critically: n_5 = 0 in thermal equilibrium at temperatures
below the chiral symmetry restoration scale (~150 MeV for QCD).
At T ~ M_Pl, ALL fermions are effectively massless and chirality
IS conserved (to leading order), so n_5 is set by initial conditions
or by the chiral anomaly -- NOT by torsion.

**Risk: mu_5 at the bounce depends on the initial n_5, which torsion
does not generate. Torsion modifies the dynamics of existing n_5 but
does not CREATE it.**

### Likely Observable/Constraint

eta_B = n_B/n_gamma ~ 6 x 10^{-10}. If the mechanism works, it
constrains the Barbero-Immirzi parameter gamma through the
(1 - 3gamma^2 kappa xi^2) denominator. If it fails, it constrains
the maximum n_5 at the bounce.

---

## Candidate B: Torsion-Modified Out-of-Equilibrium Decay

### Basic Interaction

Heavy fermions (e.g., right-handed neutrinos N_R with mass M_N)
decay near the bounce. The (J^5)^2 interaction modifies their
effective mass and decay kinematics:

```
M_N^eff = M_N + delta_M(rho)
delta_M ~ G_torsion * n_5 ~ (kappa/M_Pl^2) * M_Pl^3 ~ M_Pl
```

During the bounce, the effective mass shift is O(M_Pl), drastically
altering decay rates and CP asymmetries for any heavy particle with
M_N < M_Pl.

### Bounce/Torsion Ingredient

The four-fermion (J^5)^2 term acts as a density-dependent mass
correction for chiral fermions. At bounce densities, this correction
is O(M_Pl) -- comparable to or larger than any particle mass.

### Why It Might Work

1. Modified decay kinematics can change the CP asymmetry parameter
   epsilon in leptogenesis.
2. The bounce provides a natural "freeze-out" epoch: the rapid
   transition from contraction to expansion takes particles out of
   equilibrium.
3. The modification IS torsion-specific: the (J^5)^2 interaction
   distinguishes left- from right-handed fermions.

### Biggest Theoretical Risk

**The mass shift is O(M_Pl) for ALL fermions simultaneously.** This
means it cannot preferentially affect heavy neutrinos vs other
species. Every fermion gets the same O(M_Pl) mass shift, so the
RELATIVE mass splittings and decay asymmetries are unchanged.

More precisely: delta_M/M_N ~ M_Pl/M_N >> 1 for any M_N < M_Pl.
In this regime, the "original" mass M_N is irrelevant -- all fermions
are effectively degenerate at mass ~M_Pl. This ERASES the mass
hierarchy that standard leptogenesis relies on for CP asymmetry.

**Risk: universal O(M_Pl) mass shift destroys rather than enhances
the mechanism.**

### Likely Observable/Constraint

If viable: eta_B constrains G_torsion * n_5 at the bounce.
More likely: mechanism is killed by universality of the mass shift.

---

## Candidate C: Gravitational/Nonadiabatic Production of Heavy DM

### Basic Interaction

The bounce background a(t) = a_b(1+4alpha^2 t^2)^{1/4} produces
particles via nonadiabatic vacuum amplification. For a scalar field
chi of mass m_chi:

```
chi_k'' + (k^2/a^2 + m_chi^2 - xi_R R) chi_k = 0
```

The Bogoliubov coefficient |beta_k|^2 gives the particle number
density produced. The Ricci scalar at the bounce:

```
R(t=0) = 6(a-ddot/a + (a-dot/a)^2) ~ alpha^2 ~ M_Pl^2 (ECH)
```

### Bounce/Torsion Ingredient

The bounce profile a(t) determines the nonadiabaticity and hence
|beta_k|^2. In minimal ECH, alpha ~ M_Pl. In PGT, alpha ~ m_T.
The specific bounce profile (1+4alpha^2 t^2)^{1/4} gives a specific
|beta_k|^2 that differs from, e.g., a cosh-bounce or a linear bounce.

### Why It Might Work

1. Gravitational production is unavoidable -- any massive particle
   coupled to gravity is produced.
2. Superheavy DM (m_chi ~ 10^{13} GeV for "wimpzillas") is a known
   viable candidate from gravitational production.
3. The specific bounce profile might predict a specific m_chi
   dependence.

### Biggest Theoretical Risk

**This is EXACTLY standard gravitational particle production. The
bounce profile enters only through the specific shape of |beta_k|^2,
which is a modest quantitative correction to generic bounce
production.**

The result for ANY radiation bounce at scale H_b is:

```
n_chi ~ H_b^3 * |beta|^2
Omega_chi h^2 ~ (m_chi / M_Pl) * (H_b / M_Pl)^{3/2} * |beta|^2
```

For ECH (H_b ~ M_Pl): Omega ~ (m_chi/M_Pl) * |beta|^2.
The specific |beta|^2 for the spin-torsion bounce is O(1) for
m_chi < H_b, same as any other bounce.

**Risk: gravitational production is bounce-model-independent at
leading order. Torsion is decorative.**

### Likely Observable/Constraint

Omega_DM h^2 = 0.12 constrains m_chi. But the constraint is the
same as for any Planck-scale bounce, so it constrains m_chi, not
the torsion model.

---

## Candidate D: Bounce-Modified Axion/pNGB Relic Abundance

### Basic Interaction

An axion or pseudo-Nambu-Goldstone boson (pNGB) phi with potential
V(phi) = Lambda^4(1 - cos(phi/f)) evolves through the bounce. The
equation of motion:

```
phi-ddot + 3H phi-dot + (Lambda^4/f) sin(phi/f) = 0
```

The bounce modifies H(t) through the modified Friedmann equation
H^2 = (8piG/3) rho (1 - rho/rho_crit). At the bounce, H = 0 and
H-dot > 0 (expansion begins).

### Bounce/Torsion Ingredient

Two possible effects:
1. The modified Friedmann equation H^2 propto rho(1-rho/rho_crit)
   causes H to vanish at the bounce and reverse sign, trapping phi
   at a specific field value.
2. If phi couples to the Pontryagin density through
   (phi/f) R-tilde R, then... R-tilde R = 0 on FRW. Dead end.
3. If phi couples to the torsion Nieh-Yan density... this requires
   dynamical torsion (PGT), and Foundation B showed this is a
   generic ALP (topological-shift duality).

### Why It Might Work

1. The misalignment mechanism depends on H(t) history, which the
   bounce modifies.
2. If the bounce traps phi at a specific initial angle theta_i,
   the relic abundance becomes a PREDICTION rather than an input.

### Biggest Theoretical Risk

**The axion starts oscillating when m_a ~ H. For QCD axion,
m_a ~ Lambda_QCD^2/f ~ 10^{-5} eV (for f ~ 10^{12} GeV). This is
56 orders of magnitude below M_Pl. The axion is frozen from the
bounce until T ~ Lambda_QCD, and the bounce-era H(t) is completely
irrelevant to the misalignment dynamics.**

The bounce modifies H(t) only for t ~ t_Pl. The axion oscillation
onset occurs at t ~ 10^{-7} s (QCD epoch). The bounce is a
sub-Planck-time blip in the axion's cosmological history.

**Risk: the bounce is irrelevant to axion dynamics because m_a << H_bounce
by 56 orders of magnitude.**

### Likely Observable/Constraint

None meaningful. The axion abundance is set at T ~ Lambda_QCD,
completely independent of bounce dynamics.

---

## Candidate E: Torsion-Assisted Leptogenesis Through Four-Fermion Sector

### Basic Interaction

The (J^5)^2 interaction can be Fierz-rearranged to couple different
fermion species:

```
(J^5)^2 = (psi-bar_i gamma_mu gamma_5 psi_i)(psi-bar_j gamma^mu gamma_5 psi_j)
```

summed over species i,j. This includes cross-terms between
leptons and quarks, and between different lepton generations.

At bounce densities, these four-fermion interactions have effective
coupling G_eff ~ G ~ M_Pl^{-2}, with interaction rate:

```
Gamma_4f ~ G_eff^2 * T^5 ~ T^5 / M_Pl^4
```

At T ~ M_Pl: Gamma_4f ~ M_Pl, comparable to H ~ M_Pl.

### Bounce/Torsion Ingredient

The four-fermion interaction IS the torsion interaction. At bounce
densities, it is maximally strong (Gamma ~ H) and can drive lepton
number violation if combined with the chiral anomaly.

The key process: torsion four-fermion scattering + SU(2)_L
sphaleron = net B+L violation. The torsion interaction provides
additional fermion scattering channels at the Planck-scale bounce,
supplementing the sphaleron rate.

### Why It Might Work

1. The four-fermion coupling G ~ M_Pl^{-2} gives Gamma ~ H at T ~ M_Pl.
   This is the OPTIMAL regime: neither too fast (equilibrium, no asymmetry)
   nor too slow (no interaction).
2. The interaction is chirality-sensitive ((J^5)^2 distinguishes
   L from R).
3. The bounce provides departure from equilibrium.

### Biggest Theoretical Risk

**The (J^5)^2 interaction CONSERVES both baryon number and lepton
number.** It is a vector-like interaction: J^5_mu J^{5,mu} does not
change fermion number. It scatters fermions but preserves their
total B and L.

Baryon/lepton number violation requires either:
- Sphalerons (which violate B+L but conserve B-L)
- Dimension-6 B-violating operators (GUT physics)
- Majorana mass terms (which violate L by 2)

Torsion provides NONE of these. It adds a four-fermion scattering
channel that conserves B and L. It can modify the RATE of processes
that already violate B or L, but it cannot GENERATE the violation.

**Risk: (J^5)^2 conserves B and L. Torsion cannot generate baryon
or lepton asymmetry without an independent B/L-violating source.**

### Likely Observable/Constraint

If combined with standard sphalerons: modifies the sphaleron
washout factor. But the modification is proportional to
G_torsion/G_Fermi ~ (M_W/M_Pl)^2 ~ 10^{-34} at electroweak
temperatures where sphalerons operate. Negligible.

At Planck temperatures: sphalerons are in equilibrium, and
G_torsion ~ G_Fermi(Planck) is O(1). But ANY four-fermion
interaction of gravitational strength does the same -- torsion is
not special.

---

## Candidate F: PBH/Compact Relic Window from Bounce-Modified Perturbations

### Basic Interaction

If the bounce modifies the primordial power spectrum at small scales
(large k), it could produce enhanced density perturbations that
collapse into primordial black holes (PBHs).

The bounce transfer function from Branch K:

```
T(k) = 1    for k << k_b
T(k) ~ oscillatory    for k ~ k_b
```

The bounce peak is at k ~ k_b ~ M_Pl (ECH) or k ~ m_T (PGT).

### Bounce/Torsion Ingredient

The specific bounce profile modifies T(k) near k_b. If T(k_b) > 1
at the bounce scale, density perturbations are enhanced and PBHs
may form.

### Why It Might Work

1. PBHs are a viable DM candidate in certain mass windows.
2. The bounce DOES modify the transfer function at k ~ k_b (Branch K
   confirmed oscillatory features).
3. The PBH mass from bounce-scale perturbations:
   M_PBH ~ M_Pl^2 / H_bounce ~ M_Pl (ECH) or ~ M_Pl^2/m_T (PGT).

### Biggest Theoretical Risk

**PBHs of mass M ~ M_Pl evaporate via Hawking radiation in
t_evap ~ M^3/M_Pl^4 ~ M_Pl^{-1} ~ 10^{-43} s.**

They do not survive to the present epoch. They are INSTANTANEOUS
on cosmological timescales.

For PGT: M_PBH ~ M_Pl^2/m_T. For m_T ~ 10^7 GeV:
M_PBH ~ 10^{31} GeV ~ 10^8 g.
t_evap ~ (10^8)^3 / M_Pl^4 ~ 10^{24} / 10^{76} ~ 10^{-52} s.
Still sub-Planckian evaporation time. No.

For M_PBH to survive to today (t_evap > 10^{17} s), need
M > 10^{15} g ~ 10^{38} GeV. This requires
M_Pl^2/m_T > 10^{38} GeV, so m_T < M_Pl^2/10^{38} GeV ~ 10^{-19} GeV.
But then the PGT bounce scale is rho_crit ~ (10^{-19})^2 * M_Pl^2
~ 10^{-38} M_Pl^4, far below BBN scale. The bounce is irrelevant.

**Risk: bounce-scale PBHs evaporate instantly. Surviving PBHs require
m_T so small that the bounce occurs at sub-BBN scales.**

### Likely Observable/Constraint

PBH evaporation products COULD be observable as a burst of particles
at the bounce epoch. But this is just gravitational particle production
by another name, and the products thermalize instantly at Planck
temperatures. No relic survives.

---

## Candidate G: Bounce-Triggered Sterile Relic Population Through Spin-Density Coupling

### Basic Interaction

Sterile neutrinos nu_s do not couple to the SM gauge fields but DO
couple to gravity and hence to torsion through their energy-momentum
tensor. In Einstein-Cartan theory, any fermion with spin-1/2
participates in the (J^5)^2 interaction:

```
L_eff superset -(3kappa/16) * (J^5_SM + J^5_sterile)^2
```

The cross-term gives:

```
L_cross = -(3kappa/8) * J^5_SM . J^5_sterile
```

This is a GRAVITATIONAL-STRENGTH four-fermion interaction between
SM fermions and sterile neutrinos.

### Bounce/Torsion Ingredient

The cross-term coupling is the unique prediction of torsion: sterile
fermions that have NO gauge interactions still participate in the
axial four-fermion scattering through torsion exchange.

At bounce densities (T ~ M_Pl), the interaction rate:

```
Gamma_cross ~ G^2 * T^5 / 4pi ~ M_Pl^5 / (M_Pl^4 * 4pi) ~ M_Pl/(4pi)
```

This is comparable to H ~ M_Pl. Sterile neutrinos are in
EQUILIBRIUM with the SM plasma at the bounce.

### Why It Might Work

1. Torsion provides a UNIQUE production channel for sterile neutrinos
   that does not exist in standard gravity.
2. At T ~ M_Pl, the production rate is O(H), thermalizing the sterile
   population.
3. The relic abundance of sterile neutrinos depends on when they
   decouple from the torsion interaction.

### Biggest Theoretical Risk

**At T ~ M_Pl, ALL species -- including gravitons -- are in thermal
equilibrium due to gravitational scattering (Gamma_grav ~ G^2 T^5 ~ H
at T ~ M_Pl). The torsion cross-term adds one more channel among
many gravitational-strength interactions.**

Decoupling temperature for the torsion channel:
Gamma_cross ~ G^2 T^5 ~ T^5/M_Pl^4. Set Gamma = H ~ T^2/M_Pl:
T_dec ~ M_Pl.

So the torsion channel freezes out at T ~ M_Pl, the same scale as
all gravitational interactions. After decoupling, the sterile
neutrino population evolves as any other decoupled relativistic
species.

The contribution to N_eff (effective number of neutrino species):

```
Delta N_eff = (g_sterile / 2) * (T_sterile / T_nu)^4
```

For decoupling at T ~ M_Pl (same as graviton decoupling):

```
Delta N_eff ~ 0.027 per sterile Weyl fermion
```

(This is the standard graviton contribution formula, since decoupling
at the same epoch gives the same dilution.)

This is indistinguishable from the graviton contribution and is
NOT specific to torsion -- standard gravitational scattering
thermalizes ALL species at T ~ M_Pl.

**Risk: torsion production of sterile neutrinos is identical to
gravitational production at the same scale. Decorative torsion.**

### Likely Observable/Constraint

Delta N_eff ~ 0.03 per species. CMB-S4 sensitivity is ~0.03, so in
principle detectable. But the signal is the SAME as gravitational
thermalization -- there is no way to distinguish torsion production
from gravitational production. The constraint is on the NUMBER of
light species, not on the torsion mechanism.

---

## Summary Table

| Candidate | Torsion ingredient | CP/B violation? | Torsion-specific? | Biggest risk |
|-----------|-------------------|----------------|------------------|-------------|
| A: Axial mu_5 | (J^5)^2 -> mu_5^eff | Requires external CP | Partially | mu_5 doesn't create n_5 |
| B: Modified decay | (J^5)^2 mass shift | Requires Majorana | No (universal shift) | Erases mass hierarchy |
| C: Gravitational DM | Bounce profile a(t) | N/A (DM) | No (any bounce) | Standard grav. production |
| D: Axion relic | Modified H(t) | N/A (axion) | No | m_a << H_bounce by 10^{56} |
| E: Leptogenesis assist | (J^5)^2 scattering | Requires sphalerons | Partially | (J^5)^2 conserves B, L |
| F: PBH window | T(k) at k ~ k_b | N/A (PBH) | Partially | PBHs evaporate instantly |
| G: Sterile relics | J^5_SM . J^5_sterile | N/A (relic pop.) | Superficially | Same as gravitational thermalization |
