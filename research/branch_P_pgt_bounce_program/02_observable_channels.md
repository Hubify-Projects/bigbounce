# Observable Channels: Comprehensive Map

**Date:** 2026-03-16

---

## Channel 1: Stochastic GW Background (Vacuum Amplification)

**Status: DEAD (Branch M)**

- Omega_GW h^2 = 5 x 10^{-6} x (m_T/M_Pl)^2 x S(f/f_b)
- Minimum detector gap: 10^{17} (ET at f ~ 10^4 Hz)
- Root cause: amplitude-frequency tradeoff Omega ~ f_b^4 / f_Pl^4
- Applies to ALL vacuum-amplification bounces, not PGT-specific

**Why still dead in Branch P:** No new physics changes the Bogoliubov
calculation. The vacuum amplification ceiling is fundamental.

---

## Channel 2: Non-Vacuum GW Sources

### 2a. Torsion oscillation decay

After the bounce, the propagating torsion mode (mass m_T) oscillates
coherently. If it decays, the decay products include gravitons.

**Assessment:**

Branch M Section 5 already computed the torsion oscillation GW yield:

```
epsilon = rho_GW / rho_crit ~ (m_T/M_Pl)^3
```

This is WORSE than vacuum amplification ((m_T/M_Pl)^2). The coherent
oscillation is too brief (~ 1 oscillation period ~ 1/m_T at the bounce)
for resonant buildup.

**Why alive vs dead:** The estimate above assumes gravitational-strength
coupling (torsion -> graviton + graviton). If the torsion mode decays to
matter fields first, and those fields undergo a secondary process (e.g.,
turbulence, phase transition) that produces GWs, the chain could be more
efficient. However, this requires specifying a reheating sector that is
not part of the minimal model.

**Biggest risk:** The efficiency estimate (m_T/M_Pl)^3 is robust for
direct gravitational decay. Any non-gravitational channel requires
additional model-building outside PGT.

**Verdict: DEAD for minimal model. SPECULATIVE for extensions.**

### 2b. Parametric resonance during bounce

The bounce lasts ~ 1/m_T (one dynamical timescale). Parametric resonance
requires multiple oscillations to build up. With only ~ 1 oscillation
period available, there is no time for resonant amplification.

**Quantitative check:**

Parametric resonance requires ~ n oscillations where n ~ 1/q for
broad resonance (q is the resonance parameter). For the bounce:
the available number of oscillations is N ~ t_bounce x m_T ~ 1.
So parametric enhancement requires q > 1, but the coupling is
gravitational: q ~ (m_T/M_Pl)^2 << 1.

**Verdict: DEAD. Insufficient time and coupling.**

### 2c. Phase transition triggered near bounce

If a first-order phase transition occurs at T ~ T_bounce, the resulting
bubble collisions and turbulence produce GWs with amplitude set by the
latent heat, NOT by (H/M_Pl)^2.

**Assessment:**

This is the one genuine escape route from the vacuum amplification ceiling.
Phase transition GWs have amplitude:

```
Omega_GW ~ 10^{-5} x (alpha / (1+alpha))^2 x (H_* / beta)^2
```

where alpha = latent heat / radiation energy, beta = nucleation rate,
H_* = Hubble at transition. This can be O(10^{-10}) or larger for strong
transitions (alpha > 1).

**Why alive:** The amplitude is NOT suppressed by (m_T/M_Pl)^2. A strong
phase transition near the bounce can produce detectable GWs.

**Why different from dead model:** This is NOT a bounce signature -- it is
a standard phase-transition signal that HAPPENS to occur near the bounce
epoch. The bounce sets the temperature and expansion rate, but the GW
production mechanism is entirely standard (bubble collisions, sound waves,
turbulence).

**Biggest risk:** (1) The phase transition is not predicted by PGT -- it
requires adding a hidden sector with a first-order transition at the right
scale. (2) The GW signal is not bounce-specific -- any cosmology reaching
the same temperature produces the same signal. (3) This reduces to
standard phase-transition GW phenomenology with the bounce merely setting
the initial temperature.

**Verdict: ALIVE but NOT BOUNCE-SPECIFIC. Standard cosmology grafted onto
bounce initial conditions.**

### 2d. Pre-bounce contraction amplification

If the contracting phase has a period of slow contraction (ekpyrotic,
w >> 1) or matter domination (w = 0), tensor modes can be amplified at
scales much larger than k_b.

**Assessment:**

This is model-dependent: it requires specifying a contraction history.
For ekpyrotic contraction:

```
P_T(k) ~ (H_ek / M_Pl)^2 x (k/k_end)^{n_T,ek}
```

where n_T,ek = 2(1-1/epsilon) for equation of state parameter epsilon.

**Why alive:** Can produce a large-scale tensor spectrum independent of
the vacuum amplification ceiling.

**Why different:** This is a pre-bounce effect, not a bounce signature.
The bounce merely transmits the spectrum (T(k) = 1 for k << k_b). The
observable is entirely determined by the contraction mechanism.

**Biggest risk:** Not PGT-specific. Any bounce model with the same
contraction history gives the same result. We are no longer testing PGT;
we are testing the contraction mechanism.

**Verdict: ALIVE but NOT BOUNCE-SPECIFIC. Pre-bounce model required.**

---

## Channel 3: Scalar Perturbation Spectrum

**Status: TRANSPARENT at observable scales (Branch K)**

T(k) = 1 for all k << k_b. The bounce adds nothing to the scalar spectrum.

**Possible escape: specify a pre-bounce mechanism.**

If we commit to a specific contraction model (ekpyrotic, matter contraction),
we get definite scalar predictions (n_s, running, etc.). These can be
confronted with CMB data.

**Assessment:**

This is a viable research direction, but it is NOT testing PGT. The
predictions come entirely from the contraction model. The bounce is
transparent. Comparing ekpyrotic + PGT bounce vs ekpyrotic + LQC bounce
vs ekpyrotic + generic bounce gives IDENTICAL scalar spectra (all have
T(k) = 1 for observable modes).

**Verdict: ALIVE for the composite model. DEAD for testing PGT specifically.**

---

## Channel 4: Reheating / Torsion Decay

After the bounce, the torsion mode is excited with amplitude ~ M_Pl and
mass m_T. It decays to standard model particles.

### Decay rate

The torsion couples to fermions via the axial current with coupling
g_eff ~ m_T / M_Pl^2 (mass-coupling lock). The decay rate:

```
Gamma_T ~ g_eff^2 m_T^3 / (8 pi) ~ m_T^5 / (8 pi M_Pl^4)
```

### Reheat temperature

Decay completes when Gamma_T ~ H. This sets the reheat temperature:

```
T_reh ~ (Gamma_T M_Pl)^{1/2} ~ m_T^{5/2} / M_Pl^{3/2}
```

For various m_T:

| m_T (GeV) | Gamma_T (GeV) | T_reh (GeV) | Compatible with BBN? |
|-----------|--------------|-------------|---------------------|
| 10^{18} (M_Pl) | 10^{18} | 10^{18} | YES |
| 10^{15} | 10^{3} | 10^{10} | YES |
| 10^{12} | 10^{-12} | 10^{3} | YES |
| 10^{9} | 10^{-27} | 10^{-5} | MARGINAL |
| 10^{7} | 10^{-37} | 10^{-10} | NO |
| 10^{5} | 10^{-47} | 10^{-15} | NO |

**BBN constraint:** T_reh > few MeV requires m_T > ~10^9 GeV (roughly).

This is a REAL CONSTRAINT on the PGT parameter space.

**Why alive:** Gives a concrete lower bound on m_T from BBN. This is
an indirect but genuine observational constraint.

**Why different from dead channels:** This does not require detecting a
signal -- it constrains the parameter space via existing data (BBN success).

**Biggest risk:** The decay rate estimate depends on assuming the torsion
mode is the dominant energy component after the bounce. If radiation
dominates (which it does in the standard scenario), the torsion energy
fraction is sub-dominant and the "reheating" is actually the radiation
itself. The torsion decays into an already-hot radiation bath.

**Refinement:** The torsion energy fraction at the bounce:

```
rho_torsion / rho_total ~ (m_T / M_Pl)^2
```

(from the mass-coupling lock / vacuum amplification logic). So the torsion
is NOT the dominant component -- radiation is. There is no "reheating"
problem. The universe is already hot. The torsion decays as a sub-dominant
component.

**Revised verdict: The BBN constraint is on the torsion energy fraction
times the decay rate, not on the reheat temperature per se. If
rho_torsion / rho_rad ~ (m_T/M_Pl)^2, the constraint is much weaker.**

**Need to check:** Does torsion energy dominate or not? At the bounce:

- In EC: rho = rho_crit, all radiation, torsion is non-propagating
- In PGT: rho_crit = m_T^2 M_Pl^2, torsion IS propagating with mass m_T

The modified Friedmann equation H^2 = (8piG/3) rho (1 - rho/rho_crit)
involves the TOTAL energy density rho, which is radiation. The torsion
modifies the gravitational sector (through the quadratic correction), not
the matter sector. So the energy budget is:

- Radiation: rho ~ rho_crit at bounce
- Torsion field energy: depends on the specific dynamics

In Sector II, the torsion is a pseudoscalar with mass m_T. Its field energy
at the bounce is at most rho_torsion ~ m_T^2 phi_0^2 where phi_0 is the
field amplitude. For phi_0 ~ M_Pl (maximum gravitational amplitude):

```
rho_torsion ~ m_T^2 M_Pl^2 = rho_crit
```

So the torsion energy could be comparable to the total energy at the bounce.
BUT: the torsion decays gravitationally (Gamma ~ m_T^5/M_Pl^4), and if
m_T << M_Pl, it decays SLOWLY. If it decays after BBN, it could spoil
light element abundances.

**This is the most promising constraint channel.**

**Verdict: ALIVE. Torsion as a long-lived relic constrainable by BBN/CMB.**

---

## Channel 5: Dark Radiation from Torsion Decay

If the torsion decays to relativistic species after neutrino decoupling
(T < few MeV), the decay products contribute to dark radiation, measured
as Delta N_eff.

```
Delta N_eff ~ (rho_torsion_at_decay / rho_nu)
```

The torsion energy density redshifts as matter (rho ~ a^{-3}) while
radiation goes as a^{-4}. If the torsion starts with energy fraction
f_T = rho_T / rho_total ~ 1 at the bounce, it grows relative to radiation
as a/a_b. By the time of decay (t ~ 1/Gamma_T), it dominates.

**Wait -- this changes the picture.** If the torsion starts at O(rho_crit)
and redshifts as a^{-3} while radiation goes as a^{-4}, the torsion
eventually DOMINATES. This is the standard moduli/gravitino problem.

**Epoch of torsion domination:**

```
rho_T / rho_rad ~ (a/a_b) x (rho_T,b / rho_rad,b)
```

If rho_T,b ~ rho_rad,b ~ rho_crit:

```
rho_T / rho_rad ~ a/a_b
```

Domination at a/a_b ~ 1 (immediately). The torsion dominates from the
bounce onward.

But this contradicts the standard bounce scenario where the post-bounce
expansion is radiation-dominated. The issue is whether the torsion
field oscillation actually carries energy comparable to rho_crit.

**Key question for the next calculation (Channel 4/5):** What fraction
of the bounce energy goes into torsion field oscillations vs radiation?

This determines whether:
- (A) Torsion subdominant: weak constraint, Channel 4/5 marginal
- (B) Torsion dominant: strong BBN/CMB constraint, potentially the
  most powerful observable in the program

**Verdict: ALIVE and potentially the strongest channel. Requires
calculation of torsion energy fraction at the bounce.**

---

## Channel 6: Cosmological Bounds on Bounce Scale (BBN, CMB)

Independent of torsion decay, the bounce scale affects:

### 6a. Graviton production at the bounce

Gravitons produced at the bounce contribute to N_eff:

```
Delta N_eff (gravitons) ~ Omega_GW / Omega_rad ~ (m_T/M_Pl)^2
```

For m_T = 10^{15} GeV: Delta N_eff ~ 10^{-6} (undetectable).
For m_T = M_Pl: Delta N_eff ~ 1 (detectable but this is EC, already explored).

**Verdict: DEAD for PGT (m_T << M_Pl). Too suppressed.**

### 6b. CMB spectral distortions

Energy injection from torsion decay at z ~ 10^4 -- 10^7 could produce
mu- or y-type spectral distortions.

The distortion amplitude: mu ~ (delta rho / rho) at injection epoch.
If torsion decays at T ~ 10 keV -- 10 MeV:

```
mu ~ Delta rho / rho ~ f_T x (T_decay / T_distortion_window)
```

This requires T_decay in the spectral distortion window (5 x 10^4 < z < 2 x 10^6,
corresponding to T ~ 10 eV -- 500 eV). The torsion decay temperature:

```
T_decay ~ m_T^{5/2} / M_Pl^{3/2}
```

For T_decay ~ 100 eV: m_T ~ 10^{11} GeV.

If the torsion energy fraction is significant at this epoch, spectral
distortions could constrain the model. PIXIE-class experiments have
sensitivity mu ~ 10^{-8}.

**Verdict: CONDITIONALLY ALIVE. Depends on torsion energy fraction
and decay temperature. Narrow parameter window.**

---

## Channel 7: Consistency Relations

Even if no individual signal is detectable, correlations between
bounce parameters could be tested:

- m_T determines: f_b, Omega_GW, Gamma_T, T_reh, Delta N_eff
- All are functions of ONE parameter (m_T) in the ghost-free sector
- Measuring any TWO quantities over-constrains the model

**Problem:** All individual signals are either undetectable (GW, r, f_NL)
or require the torsion energy fraction to be calculated first (BBN, N_eff,
spectral distortions).

**Verdict: POTENTIALLY USEFUL but only if Channel 4/5 yields constraints.**

---

## Channel 8: Modified Expansion History Near Bounce

The modified Friedmann equation H^2 = (8piG/3) rho (1 - rho/rho_crit)
modifies the expansion rate near the bounce. Observable consequences:

- Different expansion rate during nucleosynthesis? NO -- BBN occurs at
  T ~ 1 MeV, far below the bounce (T_bounce ~ m_T). The modification
  term rho/rho_crit ~ (T/T_bounce)^4 << 1.
- Different Hubble rate during recombination? NO -- same argument,
  even further from the bounce.

**Verdict: DEAD. The modification is exponentially small at observable
epochs.**

---

## Summary Table

| Channel | Status | Bounce-specific? | Needs calculation? | Biggest risk |
|---------|--------|:-----------------:|:------------------:|-------------|
| 1. Vacuum GW | DEAD | YES | No (done) | 10^{17} gap |
| 2a. Torsion oscillation GW | DEAD | YES | No (done) | (m_T/M_Pl)^3 |
| 2b. Parametric resonance | DEAD | NO | No | Too brief |
| 2c. Phase transition GW | ALIVE* | NO | Yes (but standard) | Not bounce-specific |
| 2d. Pre-bounce contraction | ALIVE* | NO | Yes (but pre-bounce) | Not PGT-specific |
| 3. Scalar spectrum | TRANSPARENT | NO | Only if pre-bounce chosen | Not PGT-specific |
| 4. Torsion decay / reheating | **ALIVE** | **YES** | **YES** | Energy fraction unknown |
| 5. Dark radiation (N_eff) | **ALIVE** | **YES** | **YES** | Energy fraction unknown |
| 6a. Graviton N_eff | DEAD | YES | No | (m_T/M_Pl)^2 |
| 6b. Spectral distortions | CONDITIONAL | YES | YES | Narrow window |
| 7. Consistency relations | CONDITIONAL | YES | YES | Requires other channels |
| 8. Modified expansion | DEAD | YES | No | Exponentially small |

*ALIVE but not bounce-specific -- standard cosmology grafted onto bounce.

**The only genuinely alive, bounce-specific channels are 4 and 5
(torsion decay and dark radiation), both gated on calculating the
torsion energy fraction at the bounce.**
