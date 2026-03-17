# Branch N: Order-of-Magnitude Screening

**Date:** 2026-03-16

---

## Methodology

Cheap-kill pass: compare the torsion-specific contribution to the
target observable. If the torsion effect is < 10^{-10} of the target
(i.e., 10 orders below), the candidate is DEAD. If comparable, it
SURVIVES this screen (but may still fail structural tests).

---

## Reference Scales

### ECH Bounce

| Quantity | Value |
|----------|-------|
| rho_crit | 0.21 M_Pl^4 ~ 5 x 10^{75} GeV^4 |
| T_bounce | ~ M_Pl ~ 1.2 x 10^{19} GeV |
| H_bounce | ~ M_Pl ~ 10^{43} s^{-1} |
| t_bounce | ~ t_Pl ~ 5 x 10^{-44} s |
| G_torsion | ~ G ~ 6.7 x 10^{-39} GeV^{-2} |
| n_fermion at bounce | ~ T^3 ~ 10^{57} GeV^3 |
| s (entropy density) | ~ 100 T^3 ~ 10^{59} GeV^3 |

### PGT Bounce (m_T = 10^7 GeV reference)

| Quantity | Value |
|----------|-------|
| rho_crit | ~ m_T^2 M_Pl^2 ~ 10^{52} GeV^4 |
| T_bounce | ~ (m_T M_Pl)^{1/2} ~ 10^{13} GeV |
| H_bounce | ~ m_T ~ 10^7 GeV ~ 10^{31} s^{-1} |
| t_bounce | ~ 1/m_T ~ 10^{-31} s |
| n_fermion at bounce | ~ T^3 ~ 10^{39} GeV^3 |
| s (entropy density) | ~ 100 T^3 ~ 10^{41} GeV^3 |

### Targets

| Observable | Value |
|-----------|-------|
| eta_B = n_B/n_gamma | 6.1 x 10^{-10} |
| Omega_DM h^2 | 0.12 |
| Delta N_eff (BBN) | < 0.4 |
| Delta N_eff (CMB-S4) | ~ 0.03 sensitivity |

---

## Candidate A: Axial Chemical Potential Baryogenesis

### Torsion-specific ingredient

```
mu_5 = (3pi G) n_5 = 3pi n_5 / M_Pl^2
```

### OOM estimate

At T ~ M_Pl (ECH), maximum n_5 ~ T^3 ~ M_Pl^3:

```
mu_5^max / T ~ 3pi M_Pl^3 / (M_Pl^2 * M_Pl) ~ 10
```

Sphaleron bias:

```
eta_B ~ (Gamma_sph / s) * (mu_5/T) * t_bounce
     ~ (alpha_W^5 T^4 / T^3) * (mu_5/T) / T
     ~ alpha_W^5 * (mu_5/T)
     ~ (1/30)^5 * O(1)
     ~ 4 x 10^{-8}
```

For equilibrium n_5 = 0, mu_5 = 0, eta_B = 0. For n_5 ~ n_5^max:
eta_B ~ 10^{-8}.

**PASSES OOM screen** (within 2 orders of target) but only for
maximal initial chirality.

### BUT: Torsion-specific?

The SAME baryogenesis occurs with ANY effective mu_5 at the Planck
scale. Standard gravitational scattering at T ~ M_Pl generates
four-fermion interactions of the SAME strength as torsion:

```
G_gravitational = G_Newton ~ M_Pl^{-2} = G_torsion
```

The torsion contribution is ONE of ~100 (g_*) gravitational-strength
channels. The torsion-specific fraction:

```
eta_B^torsion / eta_B^total ~ 1/g_* ~ 1/100
```

**Torsion contributes ~1% of the effect. Not dominant. Not specific.**

### Verdict: MARGINALLY PASSES OOM, FAILS SPECIFICITY

---

## Candidate B: Modified Heavy Fermion Decay

### Torsion-specific ingredient

```
delta_M ~ G_torsion * n_5 ~ M_Pl (at bounce)
```

### OOM estimate

Mass shift delta_M ~ M_Pl applies to ALL fermions. For right-handed
neutrinos with M_N ~ 10^{10} GeV:

```
delta_M / M_N ~ 10^{19} / 10^{10} ~ 10^9
```

The N_R is unrecognizable -- its mass is swamped by 9 orders of
magnitude. The CP asymmetry parameter epsilon ~ Im(Yukawa^2)
depends on MASS SPLITTINGS between N_R species:

```
epsilon ~ (delta M_{ij} / M_average) * Im(h^dagger h)_{ij}
```

With ALL masses shifted to ~ M_Pl, the splitting delta M_{ij} is
whatever it was originally, but M_average ~ M_Pl >> delta M_{ij}.

```
epsilon_bounce / epsilon_standard ~ (M_N / M_Pl)^2 ~ 10^{-18}
```

**The CP asymmetry is SUPPRESSED by 18 orders of magnitude.**

### Verdict: DEAD. Torsion mass shift DESTROYS leptogenesis.

---

## Candidate C: Gravitational DM Production

### Torsion-specific ingredient

The bounce profile a(t) determines |beta_k|^2.

### OOM estimate

For scalar DM with m_chi < M_Pl:

```
n_chi / s ~ 1 / g_* ~ 10^{-2}
Omega h^2 ~ 10^{-2} * (m_chi / 3 x 10^{9} eV) * 0.12
         ~ 0.12 * (m_chi / 3 x 10^{10} GeV)
```

Correct DM abundance for m_chi ~ 3 x 10^{10} GeV. Numerically
viable but IDENTICAL to any Planck-scale bounce.

### Torsion-specific correction

The (J^5)^2 interaction affects FERMIONIC DM production. Additional
production rate from torsion:

```
Gamma_torsion ~ G^2 n_5 T^2 ~ T^5 / M_Pl^4
```

At T ~ M_Pl: Gamma_torsion ~ M_Pl. Same order as gravitational
production. NOT dominant, just one more channel.

### Verdict: PASSES OOM, FAILS SPECIFICITY (any bounce at M_Pl gives same result)

---

## Candidate D: Axion Abundance

### Torsion-specific ingredient

Modified H(t) during bounce.

### OOM estimate

```
Delta_theta ~ m_a^2 * t_bounce / H_bounce ~ (10^{-5} eV)^2 / M_Pl^2
           ~ 10^{-48}
```

**DEAD by 48 orders of magnitude** (need Delta_theta ~ 1 for any
effect on the abundance).

Actually, the full estimate from Toy Model 3 gives Delta_theta ~
10^{-96}. Either way, catastrophically dead.

### Verdict: DEAD. Cleanest kill in the program.

---

## Candidate E: Torsion-Assisted Leptogenesis

### Torsion-specific ingredient

(J^5)^2 provides additional four-fermion scattering at bounce.

### OOM estimate

The (J^5)^2 interaction rate at T ~ M_Pl:

```
Gamma_{(J5)^2} ~ G^2 T^5 ~ M_Pl
```

Comparable to H ~ M_Pl. The interaction is "in equilibrium" at the
bounce. But (J^5)^2 CONSERVES B and L. Its contribution to
ASYMMETRY generation is exactly zero.

The only contribution is modification of sphaleron RATE, which at
T ~ M_Pl is already in equilibrium:

```
Gamma_sph ~ alpha_W^5 T^4 >> H at T ~ M_Pl
```

Adding more scattering channels does not help when sphalerons are
already in equilibrium. In equilibrium, the asymmetry is determined
by equilibrium thermodynamics, not by rates.

### Verdict: DEAD. (J^5)^2 conserves B,L. Equilibrium sphalerons
already maximize the asymmetry.

---

## Candidate F: PBH Formation

### Torsion-specific ingredient

Bounce profile modifies T(k) near k ~ k_b.

### OOM estimate (ECH)

```
M_PBH ~ M_Pl ~ 10^{-5} g
t_evap ~ t_Pl ~ 10^{-44} s
```

**DEAD. Evaporates in one Planck time.**

### OOM estimate (PGT, m_T ~ 10^7 GeV)

```
M_PBH ~ M_Pl^2 / m_T ~ 10^{12} GeV ~ 10^{-12} g (CORRECTION)
```

Wait, let me redo this more carefully.

```
M_PBH ~ (4pi/3) rho_crit / H^3 = (4pi/3) (m_T^2 M_Pl^2) / m_T^3
      ~ M_Pl^2 / m_T ~ 10^{38} / 10^7 GeV ~ 10^{31} GeV
```

Convert: 10^{31} GeV ~ 10^{31} / (6 x 10^{23} * 10^3) g ~ 10^4 g.

Actually: 1 GeV ~ 1.8 x 10^{-24} g. So 10^{31} GeV ~ 1.8 x 10^7 g.

```
t_evap ~ (M/M_Pl)^3 t_Pl where M_Pl ~ 2 x 10^{-5} g
       ~ (1.8 x 10^7 / 2 x 10^{-5})^3 * 5 x 10^{-44} s
       ~ (9 x 10^{11})^3 * 5 x 10^{-44} s
       ~ 7 x 10^{35} * 5 x 10^{-44} s
       ~ 4 x 10^{-8} s
```

Evaporates at t ~ 40 ns. Well before BBN (t ~ 1 s).

For M_PBH to survive to today (t_evap > 4 x 10^{17} s):

```
M > 5 x 10^{14} g ~ 5 x 10^{14} / (1.8 x 10^{-24}) GeV ~ 3 x 10^{38} GeV
M_Pl^2 / m_T > 3 x 10^{38} GeV
m_T < 10^{38} / (3 x 10^{38}) GeV ~ 0.3 GeV
```

At m_T ~ 0.3 GeV: T_bounce ~ (0.3 * 10^{19})^{1/2} ~ 5 x 10^8 GeV.

But then:
1. Need pre-bounce perturbations at k ~ 0.3 GeV with amplitude
   delta > 0.45. Model does not predict this.
2. The PBH mass function depends on the spectral shape at this
   ONE scale -- unconstrained.
3. No torsion-specific enhancement of perturbations (Branch K: T=1).

### Verdict: DEAD for ECH. PGT marginally possible at m_T ~ 0.3 GeV
but requires fine-tuned pre-bounce perturbations. Not predictive.

---

## Candidate G: Sterile Neutrino Production via Torsion

### Torsion-specific ingredient

Cross-coupling J^5_SM . J^5_sterile with G_cross ~ G.

### OOM estimate

Production rate at T:

```
Gamma_cross ~ G^2 T^5 / (4pi)
```

Freeze-out when Gamma = H ~ T^2/M_Pl:

```
T_dec ~ M_Pl^{3/4} / (4pi)^{1/4} ~ 0.4 M_Pl
```

After decoupling, the sterile neutrino temperature redshifts as a^{-1}.
The dilution factor relative to SM neutrinos:

```
(T_sterile / T_nu)^4 = (g_{*s}(T_nu_dec) / g_{*s}(T_sterile_dec))^{4/3}
                     ~ (10.75 / 106.75)^{4/3}    [if dec at T ~ M_Pl, g_* ~ 106.75]
                     ~ 0.027
```

So Delta N_eff per sterile Weyl fermion ~ 0.027.

### Is this torsion-specific?

Standard gravitational scattering (graviton exchange) thermalizes
ALL species at T ~ M_Pl with the same rate:

```
Gamma_grav ~ G^2 T^5 ~ Gamma_cross
```

The torsion channel is ONE AMONG MANY gravitational-strength
channels. The total thermalization rate is dominated by the SUM of
all such channels. Removing the torsion channel does not change
T_dec significantly.

### Verdict: PASSES OOM (Delta N_eff ~ 0.03, marginally detectable)
but FAILS SPECIFICITY (gravitational thermalization gives same result).

---

## Kill Summary

| Candidate | OOM screen | Specificity | Combined verdict |
|-----------|-----------|------------|-----------------|
| A: Axial mu_5 baryogenesis | **PASS** (eta_B ~ 10^{-8} max) | **FAIL** (1% of gravitational) | **MARGINAL** |
| B: Modified decay | **FAIL** (epsilon suppressed by 10^{18}) | FAIL | **DEAD** |
| C: Gravitational DM | **PASS** (m ~ 10^{10} GeV) | **FAIL** (any bounce) | **DEAD** (generic) |
| D: Axion abundance | **FAIL** (Delta_theta ~ 10^{-96}) | FAIL | **DEAD** (cleanest kill) |
| E: Leptogenesis assist | **FAIL** ((J^5)^2 conserves B,L) | FAIL | **DEAD** |
| F: PBH window | **FAIL** (evaporates) | FAIL | **DEAD** |
| G: Sterile relics | **PASS** (Delta N_eff ~ 0.03) | **FAIL** (same as grav.) | **DEAD** (generic) |

### Survivors after OOM screening: NONE

Three candidates (A, C, G) pass the OOM screen but fail the
specificity filter. The torsion contribution is either sub-dominant
(A: ~1% of gravitational effect) or identical to generic gravitational
physics (C, G).

---

## The Root Problem

At T ~ M_Pl, gravitational interactions have coupling G T^2 ~ O(1).
The torsion (J^5)^2 interaction has the SAME coupling strength. It
is not enhanced, not dominant, and not distinguishable from generic
gravitational four-fermion scattering.

The torsion interaction becomes distinctive only when:
1. It provides a QUALITATIVELY different channel (e.g., chirality-
   selective) that gravity does not, AND
2. That qualitative difference leads to a MEASURABLE quantitative
   difference in the observable.

Condition 1 is marginally met (the (J^5)^2 term IS chirality-
selective). Condition 2 is NOT met (the chirality selection is one
channel among ~100 gravitational channels, and it conserves B and L).

---

## Comparison to Previous Branches

| Branch | Root cause of failure | Applicable here? |
|--------|----------------------|-----------------|
| A-G | Mass-coupling lock, scale separation, etc. | Partially (Planck suppression) |
| H | Parity-even interaction | YES (directly) |
| K | Scale separation (k_CMB/k_b ~ 10^{-28}) | NO (early universe, no scale gap) |
| L | UV-IR specificity dilemma | YES (generic vs non-minimal) |
| M | Vacuum amplification ceiling | NO (not GW) |

The NEW failure mode here is:

> **Barrier 13 (Gravitational democracy at T ~ M_Pl):** At the Planck
> temperature, ALL gravitational-strength interactions -- torsion,
> graviton exchange, curvature scattering -- have comparable rates.
> The torsion (J^5)^2 interaction is one channel among ~g_* ~ 100
> such channels. It cannot dominate any observable because it is
> outnumbered, and it conserves B and L so it cannot generate
> asymmetries that other channels do not.
