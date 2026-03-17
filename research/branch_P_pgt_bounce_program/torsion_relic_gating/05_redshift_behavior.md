# 05 — Post-Bounce Evolution and Redshift Behavior

**Date:** 2026-03-16
**Depends on:** 01-04 (mode allowed, equations derived, amplitude estimated, numerics confirmed)

---

## 1. Three regimes of post-bounce evolution

Assuming phi(0) != 0 (as a free IC), the post-bounce evolution of the
pseudoscalar torsion mode has three distinct regimes:

### Regime I: Frozen (H >> m_T)

When the Hubble rate is much larger than the torsion mass, the friction
term 3H phi-dot dominates over the mass term m_T^2 phi. The field is
effectively frozen:

    phi ~ phi(0) = const
    rho_phi ~ (1/2) m_T^2 phi(0)^2 = const

This is the familiar slow-roll regime. The torsion density is constant
while radiation redshifts as a^{-4}. The torsion fraction GROWS:

    f_phi = rho_phi / rho_total ~ a^4 (growing rapidly)

This regime lasts from the bounce until H ~ m_T, which occurs at:

    t_osc ~ 1/m_T  (onset of oscillations)
    T_osc ~ sqrt(m_T M_Pl) (temperature at oscillation onset, in radiation era)

### Regime II: Oscillating, matter-like (H << m_T)

When H drops below m_T, the field begins rapid oscillations:

    phi(t) ~ phi_env(t) * cos(m_T t + phase)

where phi_env(t) is a slowly-varying envelope. The WKB solution gives:

    phi_env ~ a^{-3/2}

and the oscillation-averaged energy density:

    <rho_phi> = (1/2) m_T^2 phi_env^2 ~ a^{-3}

This is matter-like redshift (pressureless dust on average). Since radiation
goes as a^{-4}, the torsion fraction still GROWS but more slowly:

    f_phi ~ a (growing linearly with scale factor)

### Regime III: Decay (t > tau)

The torsion mode decays through gravitational interactions. The key question
is the decay rate.

## 2. Decay rate

The pseudoscalar torsion mode couples to matter through the gravitational
connection. The leading decay channels depend on the mass m_T:

### Gravitational decay (dimension-5 operator):

The torsion-fermion coupling is:

    L_int = (1/M_Pl) partial_mu phi * J^{5,mu}

where J^{5,mu} is the axial current. This gives:

    Gamma(phi -> f fbar) ~ (m_f^2 m_T) / (8pi M_Pl^2)  (for m_T > 2m_f)

Summing over all kinematically accessible fermion species:

    Gamma_total ~ (N_f m_T^3) / (8pi M_Pl^2)   (if m_T >> m_f for all f)

where N_f counts the effective number of final-state fermions (with mass
corrections). The m_T^3/M_Pl^2 scaling is the standard result for a
Planck-suppressed dimension-5 coupling.

**Lifetime:**

    tau = 1/Gamma ~ (8pi M_Pl^2) / (N_f m_T^3)

In conventional units:

    tau ~ (M_Pl/m_T)^2 * (1/m_T) * (8pi/N_f)

| m_T (GeV)  | m_T/M_Pl  | tau (seconds) | Compare to |
|------------|-----------|---------------|------------|
| 10^15      | 10^{-3}  | ~10^{-12}     | Pre-BBN    |
| 10^12      | 10^{-6}  | ~10^{-3}      | BBN onset  |
| 10^9       | 10^{-9}  | ~10^6         | ~10 days   |
| 10^6       | 10^{-12} | ~10^{15}      | ~30 Myr    |
| 10^3       | 10^{-15} | ~10^{24}      | >>t_universe|

### Cross-check: dimension-7 operator?

If the leading coupling is dimension-7 (two derivatives):

    L_int ~ (1/M_Pl^2) phi F_munu F-tilde^{munu}

then:

    Gamma ~ m_T^5 / (M_Pl^4)

This is MUCH slower. The lifetime would be:

    tau ~ M_Pl^4 / m_T^5

| m_T (GeV)  | tau (dim-7, seconds) |
|------------|---------------------|
| 10^15      | ~10^{-3}            |
| 10^12      | ~10^{12}            |
| 10^9       | ~10^{27}            |

**Which coupling dominates depends on the PGT model details.** The axial-vector
nature of S_mu gives a dimension-5 coupling to the axial current, so the
m_T^3/M_Pl^2 rate is the more natural one.

## 3. Cosmological history of the relic

Assuming phi(0) = phi_0 != 0 and using the dimension-5 decay rate:

### Timeline:

1. **Bounce** (t = 0):
   - rho_phi = (1/2) m_T^2 phi_0^2
   - rho_m = rho_crit = m_T^2 M_Pl^2
   - f_phi = (1/2)(phi_0/M_Pl)^2

2. **Frozen phase** (0 < t < t_osc ~ 1/m_T):
   - rho_phi = const
   - rho_rad ~ a^{-4}
   - f_phi grows as a^4
   - Ends when H ~ m_T

3. **Oscillation phase** (t_osc < t < tau):
   - rho_phi ~ a^{-3}
   - rho_rad ~ a^{-4}
   - f_phi grows as a
   - The torsion mode acts as cold dark matter

4. **Decay** (t ~ tau):
   - phi decays to fermion pairs (or gauge bosons)
   - Energy is transferred to the radiation bath
   - If tau < t_BBN: no cosmological consequence
   - If tau > t_BBN: constrained by BBN (Delta N_eff) and CMB

### BBN constraint (tau > t_BBN ~ 1 second):

For the relic to be cosmologically relevant at BBN, we need both:
- tau > t_BBN: the mode hasn't decayed yet
- f_phi(BBN) > some threshold: the mode carries significant energy

The energy fraction at BBN:

    f_phi(BBN) = f_phi(bounce) * a(BBN)/a(osc)    (in matter-like phase)

where a(osc) is the scale factor when oscillations begin. During the frozen
phase, f grows as a^4; during oscillation, as a. The total growth is large.

But this is ALL CONDITIONAL on phi(0) != 0, which has no dynamical justification.

## 4. The growing fraction problem

Even if phi(0) is tiny, the fraction f_phi GROWS with time. A torsion mode
with phi(0)/M_Pl = epsilon would reach f_phi = 1 (domination) when:

    a/a_bounce ~ 1/epsilon^2  (during frozen phase)

or

    a/a_osc ~ 1/(epsilon * a_osc^4/a_bounce^4)  (during oscillation phase, more complex)

For phi(0) = 10^{-6} M_Pl, domination occurs after a grows by ~10^{12}
from the bounce. Whether this happens before or after BBN depends on m_T
and the thermal history.

**This is the relic overproduction problem in reverse.** If phi(0) != 0, the
relic almost certainly overcloses the universe unless:
- It decays before BBN, OR
- phi(0) is exquisitely tuned to be small enough

This is the standard cosmological moduli problem applied to the torsion mode.

## 5. Summary

| Regime | rho_phi scaling | f_phi behavior | Duration |
|--------|----------------|----------------|----------|
| Frozen (H >> m_T) | const | ~ a^4 growth | 0 to 1/m_T |
| Oscillating (H << m_T) | a^{-3} | ~ a growth | 1/m_T to tau |
| Decayed (t > tau) | 0 | 0 | tau onward |

**Decay rate:** Gamma ~ m_T^3/M_Pl^2 (dimension-5, axial coupling)

**Lifetime:** tau ~ M_Pl^2/m_T^3

**Conclusion:** IF populated, the torsion relic behaves like a massive
cosmological modulus — frozen then oscillating then decaying. It faces the
standard moduli/relic overproduction problem. But the population mechanism
is absent: phi(0) = 0 is the dynamically preferred value.
