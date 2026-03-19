# Single Best Next Program: PBH + Induced GW Second Observable Channel

**Created:** 2026-03-19
**Purpose:** Detailed specification of the highest-priority post-submission research direction.

---

## Why It Dominates

### 1. Breaks the single-point-of-failure

The entire focused paper rests on f_NL = -35/8 being detectable by SPHEREx/MegaMapper. This is a strong prediction -- parameter-free, mechanism-independent, verified from two formalisms -- but it is ONE prediction tested by ONE class of experiments. If SPHEREx underperforms (photo-z degradation), or if MegaMapper is never funded, or if an unexpected systematic contaminates the bispectrum measurement, the program has no backup.

A second observable family at completely different scales and experiments transforms the architecture from "one number, one chance" to "two independent tests, either of which would be compelling."

### 2. Genuinely independent

| Property | f_NL channel | PBH + GW channel |
|----------|-------------|------------------|
| k-range | 0.002 - 0.2 Mpc^{-1} | 10^5 - 10^15 Mpc^{-1} |
| Observable | Bispectrum amplitude | DM fraction + GW spectrum |
| Experiments | SPHEREx, MegaMapper | PTA, LISA, Einstein Telescope |
| Generation mechanism | Pre-bounce contraction dynamics | Bounce transition dynamics |
| LQC dependence | Weak (contraction is classical) | Strong (bounce sharpness is LQC-specific) |
| Timeline | 2028-2035 | 2030s (LISA), 2035+ (ET) |
| Main systematic | GR projection, photo-z | Astrophysical foregrounds, PBH constraints |

The correlation between failure modes is near zero. Losing either channel still leaves the other. This is genuine two-observable resilience.

### 3. Quick determination

The viability question reduces to: **is the Wilson-Ewing LQC bounce sharp enough to enhance perturbations at k ~ k_bounce?**

This is an OOM estimate requiring the effective equation of state w_eff(t) through the bounce. The LQC effective Friedmann equation is known analytically: H^2 = (8piG/3) rho (1 - rho/rho_c). The bounce duration, sharpness parameter, and effective EOS transition can all be computed in a single session. The answer is either "yes, enhancement is possible" or "no, the bounce is too smooth" -- decisive, no ambiguity.

### 4. High payoff if viable

Asteroid-mass PBHs (10^{17} - 10^{22} g) are in the observational window where PBHs can constitute a significant fraction (or all) of dark matter. Current constraints allow f_PBH up to O(1) in parts of this mass range. The induced GW spectrum from the same enhancement peaks in the mHz - Hz band, detectable by:
- LISA (launch ~2037): mHz sensitivity
- Einstein Telescope (2030s): Hz-kHz sensitivity
- Cosmic Explorer (2030s+): complementary to ET

A concrete, testable prediction in this space would be a second paper of comparable impact to the focused PNG paper. The combination -- f_NL from contraction dynamics AND PBH/GW from bounce dynamics -- would be the most complete observational package from any bouncing cosmology model.

### 5. Clean failure mode

If the bounce is too smooth: T(k) ~ 1 for all k, no enhancement, channel dead. This is determined by the physics of the Wilson-Ewing bounce (which is fixed by the model, not a free parameter). The failure mode is clean: it tells us that the LQC bounce is adiabatic for perturbations at all scales, which is itself a result worth documenting.

---

## Exact First Calculation

### Step 1: Characterize the Wilson-Ewing LQC bounce transition

Write the effective Friedmann equation:

    H^2 = (8piG/3) rho (1 - rho/rho_c)

where rho_c = sqrt(3)/(32 pi^2 gamma^3) * M_Pl^4 ~ 0.41 M_Pl^4 is the LQC critical density and gamma ~ 0.2375 is the Barbero-Immirzi parameter.

For the Wilson-Ewing quasi-dust model:
- Pre-bounce: matter-dominated contraction (w = 0, rho grows as a^{-3})
- Bounce: rho = rho_c, H = 0, H-dot > 0
- Post-bounce: matter-dominated expansion (w = 0, rho falls as a^{-3})

Compute:
- w_eff(t) = p_eff / rho through the bounce (where p_eff includes the LQC quantum correction)
- The bounce duration: Delta_t_bounce ~ 1/sqrt(rho_c) ~ t_Pl
- The effective "sharpness" parameter: d(w_eff)/dt at the bounce
- Compare with Papanikolaou et al.'s enhancement criterion

**Key subtlety:** The Wilson-Ewing model has w ~ 0 on BOTH sides of the bounce (dust -> bounce -> dust). Papanikolaou et al.'s mechanism relies on an asymmetric EOS transition (matter -> bounce -> radiation). If the symmetric dust-to-dust transition does not produce sufficient parametric resonance, the enhancement is absent regardless of the bounce sharpness.

### Step 2: Estimate perturbation enhancement

For modes with k ~ k_bounce = a_bounce * H_bounce (where H_bounce is defined as the maximum of |dH/dt|^{1/2} or a similar characteristic scale):

- Compute the Bogoliubov coefficient beta_k from the sudden/gradual transition approximation:
  - If the bounce duration Delta_t << 1/k: sudden approximation, |beta_k|^2 ~ (Delta_w)^2 / 16
  - If the bounce duration Delta_t >> 1/k: adiabatic, |beta_k|^2 ~ exp(-pi k Delta_t) ~ 0
  - The transition regime Delta_t ~ 1/k determines the enhancement scale

- The transfer function is T(k) = 1 + 2|beta_k|^2

- Enhancement criterion: T(k) >> 1 requires |beta_k|^2 >> 1, which requires the non-adiabaticity parameter: |dw/dt| / k^2 >> 1 for k ~ k_bounce

- If enhancement > O(10^6): PBH production viable for Delta >> delta_c
- If enhancement ~ O(1): too smooth, channel dead

### Step 3 (if viable): Compute PBH mass function and induced GW spectrum

**PBH mass function:**
- Map the enhanced power spectrum P(k) through the Press-Schechter formalism (or peak theory for precision):
  f_PBH(M) = (beta(M) / 3.8 x 10^{-9}) * (0.12 / Omega_CDM h^2) * (M / M_sun)^{-1/2}
- The PBH mass is set by the horizon mass at re-entry: M ~ M_Pl^2 / H(t_re-entry) ~ M_Pl^2 * t_re-entry
- For k ~ k_bounce in LQC: M ~ 10^{17} - 10^{22} g (asteroid-mass window)

**Induced GW spectrum:**
- Standard second-order calculation:
  Omega_GW(f) ~ integral of kernel(k, q) * P(k) * P(q) dk dq
- The spectrum peaks at f_peak ~ k_peak / (2 pi a_0 H_0)
- For the LQC bounce scale: f_peak in the mHz - Hz range (LISA and ET bands)
- Compare with LISA sensitivity curve (strain sensitivity ~ 10^{-20} at mHz)
  and ET sensitivity curve (strain sensitivity ~ 10^{-25} at 10 Hz)

---

## What Success Looks Like

A concrete, testable prediction:

"The Wilson-Ewing LQC bounce produces asteroid-mass PBHs at f_PBH ~ X% of dark matter, with an induced stochastic gravitational wave background at Omega_GW ~ Y detectable by LISA at Z sigma."

Combined with the f_NL paper:

"The Wilson-Ewing LQC matter bounce makes two independent, parameter-free predictions: (1) f_NL^local = -35/8, testable by SPHEREx at 4-6 sigma in ~2028; (2) asteroid-mass PBHs with an induced GW spectrum testable by LISA in ~2037. A detection of either would be evidence for a pre-Big-Bang contracting phase. A detection of BOTH would be compelling."

This gives the program TWO legs to stand on.

---

## What Failure Implies

If T(k) ~ 1 for all k (the bounce is too smooth for enhancement):

- The science case remains one-observable (f_NL only)
- Not fatal: f_NL alone at 4-6 sigma is a strong detection if SPHEREx delivers
- But fragile: one systematic issue, one survey underperformance, and the program has no fallback
- Would motivate pursuing the formalism sensitivity audit (#2) to at least add theoretical robustness
- Would also motivate the Paper 1 framework paper (#3) to establish the broader context before SPHEREx data arrives

The failure is informative: it tells us that the LQC bounce, despite operating at Planck density, is adiabatic enough that perturbations pass through without amplification. This is worth documenting as a quantitative result.

---

## Resource Requirements

| Phase | Compute | Time | Tools |
|-------|---------|------|-------|
| Step 1: Bounce characterization | Laptop (ODE integration) | 1 session | Python/Mathematica, scipy.integrate |
| Step 2: Enhancement estimate | Laptop (Bogoliubov coefficient) | 1 session | Analytical + numerical |
| Step 3: PBH + GW (if viable) | Laptop (integrals) | 1-2 weeks | Press-Schechter, GW kernel |
| Paper draft (if viable) | None | 2-3 weeks | LaTeX |

No GPU, no RunPod, no heavy cluster compute. The entire program is laptop-scale until the PBH mass function calculation, which is still laptop-scale.
