# First Step Execution: PBH + GW Feasibility OOM Estimate

**Created:** 2026-03-19
**Status:** EXECUTED -- CHANNEL KILLED

---

## Objective

Characterize the Wilson-Ewing LQC bounce transition and determine whether perturbation enhancement at observationally accessible scales is possible.

---

## Step 1: The Wilson-Ewing Effective Friedmann Equation

The LQC effective dynamics give a modified Friedmann equation:

```
H^2 = (8 pi G / 3) rho (1 - rho / rho_c)
```

where:
- rho_c = sqrt(3) / (32 pi^2 gamma^3) * M_Pl^4 ~ 0.41 M_Pl^4 is the LQC critical density
- gamma ~ 0.2375 is the Barbero-Immirzi parameter
- M_Pl = sqrt(hbar c / G) ~ 2.18 x 10^{-5} g ~ 1.22 x 10^{19} GeV

The bounce occurs when rho = rho_c, at which point H = 0 and H-dot > 0.

---

## Step 2: Background Evolution Through the Bounce

For the Wilson-Ewing quasi-dust model (matter-dominated contraction):

```
rho = rho_0 (a_0 / a)^3
```

At the bounce: rho = rho_c, giving:

```
a_bounce = a_0 (rho_0 / rho_c)^{1/3}
```

The bounce is symmetric: matter-dominated contraction (w = 0) -> bounce -> matter-dominated expansion (w = 0).

The maximum of |H-dot| occurs AT the bounce:

```
H-dot_bounce = (8 pi G / 3) rho_c * (1 - 2 * rho_c / rho_c)
             = -(8 pi G / 3) rho_c
```

Wait -- let me compute this correctly. From the modified Friedmann equation:

```
H^2 = (8 pi G / 3) rho (1 - rho / rho_c)
```

Taking the time derivative and using the continuity equation (rho-dot = -3H(rho + p) = -3H rho for dust):

```
2H H-dot = (8 pi G / 3) rho-dot (1 - 2 rho / rho_c)
         = (8 pi G / 3) (-3H rho) (1 - 2 rho / rho_c)
```

So:

```
H-dot = -(4 pi G) rho (1 - 2 rho / rho_c)
```

At the bounce (rho = rho_c):

```
H-dot_bounce = -(4 pi G) rho_c (1 - 2) = + 4 pi G rho_c
```

This is positive (as it must be -- the universe transitions from contraction to expansion).

The characteristic timescale of the bounce:

```
Delta t_bounce ~ H-dot_bounce^{-1/2} ~ (4 pi G rho_c)^{-1/2}
               ~ (4 pi / M_Pl^2 * 0.41 M_Pl^4)^{-1/2}
               ~ (5.15 M_Pl^2)^{-1/2}
               ~ 0.44 / M_Pl
               ~ 0.44 t_Pl
```

The bounce duration is sub-Planckian in time. This is a VERY fast transition.

---

## Step 3: The Effective Equation of State Through the Bounce

The effective EOS is defined as:

```
w_eff = -1 - (2/3) H-dot / H^2
```

But at the bounce itself, H = 0 and H-dot > 0, so w_eff -> -infinity. This is not physically meaningful -- it reflects the coordinate singularity in the w_eff definition when H = 0.

More physically, the pressure is:

```
p_eff = p + p_quantum = 0 + p_quantum
```

where the quantum correction creates an effective repulsive pressure at rho ~ rho_c. The LQC effective dynamics encode this as:

```
p_eff = rho (1 - 2 rho / rho_c) / (something)
```

The key point is not the EOS but the RATE of change of the effective potential in the Mukhanov-Sasaki equation.

---

## Step 4: The Mukhanov-Sasaki Equation and Mode Enhancement

The Mukhanov-Sasaki equation for scalar perturbations:

```
v_k'' + (k^2 - z''/z) v_k = 0
```

where primes are conformal time derivatives, z = a * sqrt(2 epsilon), and v_k = z * zeta_k.

The effective potential z''/z determines mode evolution. Enhancement occurs when z''/z changes rapidly -- specifically, when modes transition from oscillating (k^2 > z''/z) to frozen (k^2 < z''/z) and back within a timescale shorter than their oscillation period.

For modes with wavenumber k, the adiabaticity condition is:

```
|d(omega_k) / dt| << omega_k^2
```

where omega_k^2 = k^2 - z''/z. Violation of this condition (non-adiabatic evolution) leads to Bogoliubov particle creation and mode amplification.

The critical question: **at what k does the adiabaticity condition break down?**

---

## Step 5: Characteristic Enhancement Scale

The adiabaticity condition breaks down for modes with k ~ k_* where:

```
k_*^2 ~ |z''/z|_max ~ a_bounce^2 * H-dot_bounce ~ a_bounce^2 * 4 pi G rho_c
```

Converting to physical wavenumber:

```
k_* / a_bounce ~ sqrt(4 pi G rho_c) ~ sqrt(4 pi * 0.41 M_Pl^2) ~ 2.27 M_Pl
```

So:

```
k_* ~ 2.27 * a_bounce * M_Pl
```

This is the COMOVING wavenumber of modes that are maximally affected by the bounce transition. Modes with k >> k_* are too short-wavelength (they oscillate many times during the bounce and average out). Modes with k << k_* are too long-wavelength (they are frozen superhorizon modes that pass through the bounce adiabatically, with T(k) -> 1).

---

## Step 6: Mapping k_* to Observable Frequency Today

The comoving wavenumber k_* corresponds to a physical frequency today:

```
f_* = k_* / (2 pi a_0) = 2.27 * M_Pl * (a_bounce / a_0) / (2 pi)
```

Now I need a_bounce / a_0. This depends on the expansion history after the bounce.

**Estimating a_bounce / a_0:**

The bounce occurs at energy density rho_c ~ 0.41 M_Pl^4 ~ 0.41 * (1.22 x 10^{19} GeV)^4.

The energy density today is rho_0 ~ 10^{-29} g/cm^3 ~ 10^{-47} GeV^4.

For a matter-dominated expansion from the bounce:

```
rho = rho_c * (a_bounce / a)^3
```

But the actual expansion history is more complex. After the bounce, there is:
1. A brief kinetic-energy-dominated phase (w = 1)
2. Transition to matter domination (w = 0)
3. Potentially reheating / radiation domination
4. Standard cosmological evolution (radiation -> matter -> Lambda)

However, for an OOM estimate, I can use entropy conservation. The total entropy of the observable universe is:

```
S ~ (a_0 T_0)^3 ~ (2.725 K * a_0)^3
```

At the bounce, the "temperature" associated with rho_c is:

```
T_bounce ~ rho_c^{1/4} ~ (0.41)^{1/4} M_Pl ~ 0.8 M_Pl ~ 10^{19} GeV ~ 10^{32} K
```

If entropy is roughly conserved from the bounce to today:

```
a_bounce * T_bounce ~ a_0 * T_0
a_bounce / a_0 ~ T_0 / T_bounce ~ 2.725 / 10^{32} ~ 3 x 10^{-32}
```

This is a rough estimate. The actual ratio depends on the details of reheating and entropy production. But for an OOM estimate, a_bounce/a_0 ~ 10^{-32} to 10^{-30} is reasonable.

**Therefore:**

```
f_* ~ 2.27 * 1.22 x 10^{19} GeV * 10^{-31} / (2 pi)
    ~ 2.77 x 10^{19} * 10^{-31} / 6.28 GeV
    ~ 4.4 x 10^{-13} GeV
```

Converting to Hz (1 GeV ~ 1.52 x 10^{24} Hz):

```
f_* ~ 4.4 x 10^{-13} * 1.52 x 10^{24} Hz ~ 6.7 x 10^{11} Hz
```

So:

```
f_* ~ 10^{11} - 10^{12} Hz
```

This is in the **sub-THz to THz** range. For comparison:
- LIGO: 10 Hz - 10^4 Hz (gap: 10^7 - 10^8)
- LISA: 10^{-4} - 10^{-1} Hz (gap: 10^{12} - 10^{13})
- PTA: 10^{-9} - 10^{-7} Hz (gap: 10^{18} - 10^{21})
- Einstein Telescope: 1 - 10^4 Hz (gap: 10^7 - 10^{11})

**The enhancement scale maps to ~ 10^{11} - 10^{12} Hz today. This is 7-8 orders of magnitude above LIGO/ET and 12-13 orders above LISA.**

---

## Step 7: What About Lower-k Modes?

Could there be enhancement at k << k_* (i.e., at modes that are deeply superhorizon during the bounce)?

For modes with k << k_*, the adiabaticity parameter is:

```
Q_k = |d(omega_k)/dt| / omega_k^2 ~ (k_*/k)^2 * (Delta t_bounce * omega_k)^{-1}
```

For k << k_*: omega_k^2 ~ -z''/z (frozen mode), and the mode evolves as a power law, not an oscillator. The Bogoliubov analysis does not apply in the usual sense. Instead, the transfer function for superhorizon modes is:

```
T(k) = zeta_post / zeta_pre
```

For modes with k << k_* (deeply superhorizon):

The conservation of zeta on superhorizon scales is a consequence of the separate universe approximation. In LQC, this has been studied extensively:

- Wilson-Ewing (2013) showed that long-wavelength perturbations pass through the LQC bounce with T(k) = 1.
- The bounce is adiabatic for these modes: they are so far outside the horizon that the bounce is instantaneous on their timescale.
- Corrections scale as (k/k_*)^2, which for CMB modes gives:

```
T(k) - 1 ~ (k/k_*)^2 ~ (k * a_0 / (2.27 * a_bounce * M_Pl * a_0))^2
```

For CMB modes (k ~ 0.05 Mpc^{-1} ~ 3.2 x 10^{-60} M_Pl):

```
(k / k_*)^2 ~ (3.2 x 10^{-60} / (2.27 * 10^{-31}))^2 ~ (1.4 x 10^{-29})^2 ~ 2 x 10^{-58}
```

For PBH-relevant modes. Asteroid-mass PBHs (M ~ 10^{17} - 10^{22} g) form from modes that re-enter the horizon during radiation domination at:

```
k_PBH ~ 10^{5} - 10^{12} Mpc^{-1}
```

Converting to natural units and computing the ratio:

```
k_PBH / k_* ~ (10^{12} Mpc^{-1}) / (2.27 * a_bounce * M_Pl / a_0)
```

I need k_* in Mpc^{-1}:

```
k_* = 2 pi f_* / c ~ 2 pi * 10^{12} Hz / (3 x 10^8 m/s) ~ 2 x 10^4 m^{-1}
    ~ 2 x 10^4 * 3.086 x 10^{22} Mpc^{-1} per m^{-1}
```

Wait, let me be more careful. 1 Mpc = 3.086 x 10^{22} m, so 1 m^{-1} = 3.086 x 10^{22} Mpc^{-1}. Then:

```
k_* ~ 2 x 10^4 m^{-1} ~ 2 x 10^4 * 3.086 x 10^{22} Mpc^{-1} ~ 6 x 10^{26} Mpc^{-1}
```

So for the most optimistic PBH scale (k_PBH ~ 10^{12} Mpc^{-1}):

```
k_PBH / k_* ~ 10^{12} / (6 x 10^{26}) ~ 2 x 10^{-15}
```

The PBH-relevant modes are at k/k_* ~ 10^{-15}. The transfer function correction is:

```
T(k_PBH) - 1 ~ (k_PBH / k_*)^2 ~ (2 x 10^{-15})^2 ~ 4 x 10^{-30}
```

**The transfer function for PBH-relevant modes is T = 1 + O(10^{-30}).** There is NO enhancement. The PBH-relevant modes are deeply superhorizon during the bounce and pass through with T = 1 to extraordinary precision.

---

## Step 8: The Papanikolaou et al. Mechanism -- Does It Apply?

Papanikolaou et al. (arXiv:2404.03779) claim enhancement from non-singular bounces. Their mechanism relies on:

1. A transition from matter-dominated contraction to expansion.
2. The transition being sufficiently sharp that modes near the transition scale experience parametric amplification.
3. The enhanced modes being at scales corresponding to asteroid-mass PBHs.

For their mechanism to work in the Wilson-Ewing model, the enhanced modes must be at k ~ k_PBH ~ 10^{5} - 10^{12} Mpc^{-1}. But the transition scale in the Wilson-Ewing model is k_* ~ 6 x 10^{26} Mpc^{-1} (Planck scale). The PBH-relevant modes are 14-21 orders of magnitude below the transition scale.

**Papanikolaou et al. use a parametrized bounce that can be tuned to have a transition at any scale.** Their bounce function is a smooth interpolation that can be made arbitrarily sharp or placed at arbitrary energy density. The Wilson-Ewing bounce is NOT tunable -- its transition scale is fixed by rho_c ~ 0.41 M_Pl^4, which is determined by the Barbero-Immirzi parameter gamma ~ 0.2375.

The Papanikolaou mechanism requires the bounce scale to be near the PBH mass scale. For asteroid-mass PBHs, this requires rho_bounce ~ 10^{40} - 10^{60} GeV^4, which is 10^{16} - 10^{36} times below the Planck density. This is NOT the LQC bounce -- it would be a completely different, sub-Planckian bounce mechanism.

**The Papanikolaou mechanism does not apply to the Wilson-Ewing LQC bounce.**

---

## Step 9: Is There Any Escape Route?

### Route 1: Non-standard LQC model with lower bounce density

If the bounce density were much lower than rho_c ~ 0.41 M_Pl^4 -- say rho_bounce ~ 10^{40} GeV^4 -- the transition scale would be at lower k, and PBH-scale enhancement might be possible. But:
- This contradicts the LQC effective dynamics, which FIX rho_c from the Barbero-Immirzi parameter.
- A lower bounce density means a weaker quantum gravity effect, undermining the theoretical motivation.
- This would be a different model, not the Wilson-Ewing model.

### Route 2: A secondary sharp feature AFTER the bounce

If the post-bounce evolution includes a sharp phase transition (e.g., reheating, symmetry breaking) at energy scales accessible to PBH production, the transition itself could enhance perturbations. But:
- This enhancement would come from the phase transition, not from the bounce.
- It would not be a bounce prediction -- it would be a standard phase-transition PBH mechanism.
- The Wilson-Ewing model does not predict any specific post-bounce phase transition.

### Route 3: Resonant amplification across multiple bounces (cyclic cosmology)

If the universe undergoes multiple bounces, modes could accumulate enhancement over many cycles. But:
- The Wilson-Ewing model does not predict cyclic behavior (it is a single bounce from contraction to expansion).
- Foundation G (`foundation_G_bounce_vacuum_selection/`) already closed the cyclic cosmology route.

### Route 4: Modified dispersion relation at trans-Planckian momenta

If the LQC effective dynamics modify the dispersion relation for modes with physical momenta near M_Pl, there could be enhancement at lower comoving k (because these modes had trans-Planckian physical momenta during the bounce). But:
- Trans-Planckian physics is precisely where the effective description breaks down.
- Any such modification would be model-dependent and introduce free parameters.
- This contradicts the "parameter-free prediction" philosophy of the program.

**No escape route survives.**

---

## Step 10: Comparison with the Chiral GW Frequency Gate

The physics is identical to what killed the chiral GW program (`project_chiral_bounce_GW/phase0_results.md`):

| Property | Chiral GW | PBH + Induced GW |
|----------|-----------|-------------------|
| Mechanism | Direct GW production at bounce | Scalar enhancement at bounce |
| Enhancement scale | k ~ k_bounce ~ a_bounce M_Pl | k ~ k_* ~ a_bounce sqrt(4piG rho_c) ~ a_bounce M_Pl |
| Frequency today | f ~ 10^{9-10} Hz (GHz) | f ~ 10^{11-12} Hz (THz) |
| Gap to LISA | 10^{12} | 10^{12-13} |
| Gap to LIGO/ET | 10^{6} | 10^{7-8} |
| Fundamental obstruction | Planck-scale bounce -> Planck-scale signals | Same |
| Status | DEAD | DEAD |

The slightly higher frequency for PBH+GW (THz vs GHz) reflects the inclusion of the sqrt(4piG rho_c) factor vs the simpler rho_c^{1/4} scaling for direct GW production. The qualitative conclusion is identical: both are permanently inaccessible.

The fundamental structural statement from the chiral GW program applies directly:

> A Planck-scale bounce produces Planck-scale signals. The entire observable universe today is the expanded version of a Planck-sized patch. Bounce-scale physics is irretrievably diluted by this expansion. The only bounce signals that reach observable frequencies are those generated during the CONTRACTION phase -- and those pass through the bounce transparently (T = 1).

---

## KILL RESULT

**The PBH + Induced GW channel is DEAD for the Wilson-Ewing LQC bounce.**

The Wilson-Ewing bounce occurs at Planck density (rho_c ~ 0.41 M_Pl^4). The perturbation enhancement scale is k_* ~ a_bounce * M_Pl, corresponding to frequencies ~ 10^{11} - 10^{12} Hz today. These frequencies are:
- 10^{7-8} above LIGO/Einstein Telescope
- 10^{12-13} above LISA
- 10^{18-21} above PTA

For PBH-relevant modes (k_PBH ~ 10^{5} - 10^{12} Mpc^{-1}), the transfer function is T = 1 + O(10^{-30}). There is ZERO enhancement at observable scales. The PBH-relevant modes are deeply superhorizon during the bounce and pass through adiabatically.

The Papanikolaou et al. mechanism requires a bounce at much lower energy density than LQC provides. Their parametrized bounce can be tuned; the Wilson-Ewing bounce cannot.

No escape route (lower bounce density, post-bounce phase transition, cyclic amplification, modified dispersion) survives within the Wilson-Ewing model framework.

**This is the SAME frequency-gate problem that killed the chiral GW program.** The physics is identical: Planck-scale bounce -> Planck-scale features -> permanently inaccessible to any detector.

---

## Summary

```
Wilson-Ewing LQC bounce density:     rho_c ~ 0.41 M_Pl^4
Bounce timescale:                     Delta t ~ 0.44 t_Pl
Enhancement scale (comoving):         k_* ~ 2.27 a_bounce M_Pl
Enhancement scale (frequency today):  f_* ~ 10^{11} - 10^{12} Hz
PBH-relevant scale:                   k_PBH ~ 10^{5} - 10^{12} Mpc^{-1}
Ratio k_PBH / k_*:                    ~ 10^{-15}
Transfer function at PBH scale:       T = 1 + O(10^{-30})
Enhancement at PBH scale:             ZERO
Channel status:                       DEAD (frequency-gate kill)
```
