# Best Next Calculation: Torsion Relic Energy Fraction

**Date:** 2026-03-16

---

## 1. Why This Calculation and Not the GW Spectrum

The user's initial suggestion was "full GW spectrum + detector-facing
parameter map." Branch M already completed this:

- Spectrum: Omega_GW h^2 = 5 x 10^{-6} x (m_T/M_Pl)^2 x S(f/f_b)
- Detector map: minimum gap 10^{17} to any detector
- Shape: flat plateau + exponential cutoff, one-parameter family in m_T

Refining the GW spectrum further (sub-leading corrections, exact
numerical Bogoliubov coefficients) changes the answer by O(1) factors
against a 10^{17} gap. This is not useful.

**The torsion relic energy fraction is the gating calculation for the
only surviving observable channel (BBN/CMB constraints on torsion decay).**

---

## 2. The Calculation

### 2.1 Setup

In ghost-free PGT Sector II, the propagating torsion mode is a massive
pseudoscalar phi with mass m_T = M_Pl / (2 sqrt(|t_3|)).

The field equation on a FRW background:

```
phi'' + 3H phi' + m_T^2 phi = J_eff
```

where phi' = d phi/dt, H = a'/a / a, and J_eff is the effective source
from the torsion-curvature coupling.

### 2.2 At the bounce

At the bounce (t = 0): H = 0, rho = rho_crit = m_T^2 M_Pl^2.

The torsion field is excited by the bounce dynamics. The question is:
what is phi(0) and phi'(0)?

**Two scenarios to distinguish:**

**(A) Torsion as geometric field:**
In PGT, the torsion enters through the connection. At the bounce, the
connection is maximally different from Levi-Civita (contorsion ~ M_Pl).
This suggests:

```
phi_0 ~ M_Pl,   phi'_0 ~ m_T M_Pl
```

giving torsion energy:

```
rho_T = (1/2) phi'^2 + (1/2) m_T^2 phi^2
      ~ m_T^2 M_Pl^2 = rho_crit
```

In this scenario, the torsion carries O(100%) of the energy at the bounce.

**(B) Torsion as perturbative fluctuation:**
If the torsion is a small perturbation on the radiation background
(not the driver of the bounce), then:

```
phi_0 ~ m_T / M_Pl x M_Pl = m_T
```

giving:

```
rho_T ~ m_T^2 x m_T^2 = m_T^4
rho_T / rho_crit ~ m_T^2 / M_Pl^2
```

In this scenario, the torsion is sub-dominant by (m_T/M_Pl)^2.

### 2.3 How to determine which scenario is correct

The answer depends on the BOUNCE MECHANISM in PGT:

**Key question:** Is the bounce driven by torsion or by the ρ^2 correction?

In EC (no propagating torsion): the bounce is driven by the non-propagating
torsion condensate, which is algebraically determined by the matter spin
density. The modified Friedmann equation H^2 = (8piG/3) rho (1 - rho/rho_crit)
follows from integrating out torsion.

In PGT with propagating torsion: there are TWO contributions:
1. The algebraic (non-propagating) torsion condensate (same as EC)
2. The propagating torsion mode (the new PGT ingredient)

The modified Friedmann equation rho_crit = m_T^2 M_Pl^2 comes from the
propagating torsion mass. But the bounce dynamics may still be dominated
by the algebraic component (as in EC) with the propagating mode as a
perturbation.

### 2.4 Exact equations to solve

**Step 1:** Write the full PGT field equations for FRW + homogeneous
pseudoscalar torsion mode phi(t):

```
H^2 = (8piG/3) [rho_rad + (1/2) phi'^2 + (1/2) m_T^2 phi^2
       - (correction terms from torsion-curvature coupling)]

phi'' + 3H phi' + m_T^2 phi = -(partial V_eff / partial phi)
```

The correction terms and V_eff come from the PGT Lagrangian with
Sector II couplings (t_2 = -2t_1, t_3 < 0).

**Step 2:** Determine initial conditions. At high density
(rho -> rho_crit), does the bounce solution have phi ~ M_Pl or
phi ~ m_T?

**Step 3:** Evolve through the bounce and into the expanding phase.
Track rho_T(t) / rho_total(t).

**Step 4:** Determine the late-time behavior:
- If rho_T / rho_rad grows (matter-like torsion vs radiation), the
  torsion eventually dominates
- If rho_T / rho_rad is constant (both radiation-like), the torsion
  is always sub-dominant

### 2.5 What determines scenario (A) vs (B)

The critical input is the PGT bounce solution for the homogeneous
torsion field. This requires solving the full coupled system
(Friedmann + torsion field equation) self-consistently.

In the literature (Yo, Nester, Baekler et al.), the PGT bounce solutions
with propagating torsion have:

- Bouncing solutions where torsion is the dominant dynamical field
  (phi ~ M_Pl at the bounce) -- **Scenario (A)**
- Solutions where torsion is a small oscillation around the EC background
  -- **Scenario (B)**

Which class is realized depends on the initial conditions of the
contracting phase. In a GENERIC cosmological evolution approaching
the bounce, the torsion field is driven to large amplitude by the
increasing curvature.

**Preliminary assessment: Scenario (A) is more natural** because:
1. The bounce is caused by the torsion sector (rho_crit set by m_T)
2. The curvature at the bounce is R ~ m_T^2, which sources the torsion
   field at amplitude phi ~ M_Pl through the torsion-curvature coupling
3. There is no mechanism to keep phi small while curvature grows

---

## 3. Exact Outputs

The calculation produces:

1. **f_T(m_T):** Torsion energy fraction rho_T / rho_total at the bounce,
   as a function of m_T

2. **Evolution:** rho_T(a) / rho_rad(a) as the universe expands

3. **Decay epoch:** Temperature T_decay at which torsion decays, vs m_T

4. **BBN constraint:** Lower bound on m_T from requiring torsion decay
   before BBN (T_decay > few MeV), given f_T

5. **N_eff constraint:** Delta N_eff from torsion decay products, vs m_T

6. **Parameter exclusion plot:** m_T vs t_3, with excluded regions from
   BBN and CMB

---

## 4. What Counts as a Win

### Strong win (BRANCH_P_PROMISING):

f_T ~ O(1), giving:
- Sharp BBN/CMB constraint on m_T (lower bound ~ 10^9 -- 10^{12} GeV)
- Detectable Delta N_eff for m_T near the boundary
- Clear parameter exclusion plot
- A genuine "cosmological moduli problem" for PGT torsion

### Moderate win (BRANCH_P_MIXED):

f_T ~ O(0.01 -- 0.1), giving:
- Weaker but non-trivial constraint
- m_T lower bound shifted downward
- Marginal Delta N_eff

### Loss (BRANCH_P_WEAK):

f_T ~ (m_T/M_Pl)^2, giving:
- No meaningful constraint from BBN/CMB
- Delta N_eff ~ (m_T/M_Pl)^4 (undetectable)
- Program effectively closed

---

## 5. What Kills Quickly

**Quick kill 1:** If the PGT bounce solution has phi(0) ~ m_T (not M_Pl),
then f_T ~ (m_T/M_Pl)^2 and the channel is dead. This can be checked by
examining the coupled Friedmann + torsion field equations at rho = rho_crit.

**Quick kill 2:** If the torsion field equation has a symmetry that forces
phi -> 0 on the FRW background (analogous to R-tilde R = 0 killing the
chiral anomaly), then there is no torsion excitation at all.

**Quick kill 3:** If the torsion behaves as radiation (not matter) after
the bounce, then rho_T / rho_rad = const and there is no growth, no
domination, no moduli problem.

**Estimated time to kill/confirm:** The coupled system is a set of ODEs.
The answer should be determinable analytically (examining the bounce
solution structure) within one focused calculation session. If the bounce
solution is known in the literature (Yo, Nester, Baekler), the answer
may already be available.

---

## 6. Comparison with Alternative Next Calculations

| Calculation | Time | Payoff if positive | Payoff if negative | Recommendation |
|-------------|------|-------------------|-------------------|---------------|
| Torsion relic fraction | ~1 session | BBN/CMB constraint | Clean closure | **DO THIS** |
| Full GW spectrum | ~1 session | None (10^{17} gap) | Already known | Skip |
| Ekpyrotic + PGT scalars | ~2 sessions | Not PGT-specific | Already known | Defer |
| Spectral distortion window | ~1 session | Narrow, conditional | Depends on relic calc | After relic calc |

**The torsion relic calculation is the clear next move. Everything else
either depends on it or is already known to give null results.**
