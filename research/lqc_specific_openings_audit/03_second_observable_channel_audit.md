# Second Observable Channel Audit

**Created:** 2026-03-18
**Status:** ACTIVE
**Purpose:** Assess whether ANY second independent channel could break the single-point-of-failure architecture.

---

## The Problem

The current live science case rests on ONE observable: f_NL = -35/8 = -4.375.

This is a single-point-of-failure architecture. If f_NL falls -- wrong value, excluded by Planck bounds, or LQC enhancement pushes it too high -- we have NO backup. The model becomes observationally indistinguishable from inflation.

Specifically:
- r ~ 10^-4 is below all planned detector thresholds (LiteBIRD targets r ~ 0.001).
- n_s = 0.964 is indistinguishable from Starobinsky R^2 inflation.
- n_T > 0 (blue tilt) is a distinctive prediction but cannot be measured independently without measuring r first.
- alpha_s (spectral running) is too small to be distinctive at current precision.

**The program needs a second independent observable to have structural resilience.**

---

## Channel A: PBH Production + Induced Gravitational Waves

### Mechanism

During the transition from contraction to expansion (the LQC bounce itself), there is a brief period where the effective equation of state changes rapidly. The effective EOS transitions from w ~ 0 (matter) through w -> -infinity (at the bounce, where H = 0 and H-dot > 0) to w ~ 1/3 (radiation) or back to w ~ 0 (dust).

If this transition is sharp enough, scalar perturbations at scales that were near-horizon at bounce time can be enhanced. The enhancement occurs because modes that enter the horizon just before the bounce experience a brief period of rapid growth as the effective potential in the Mukhanov-Sasaki equation changes sign.

Enhanced scalar perturbations at small scales have two observable consequences:
1. **Primordial Black Hole (PBH) formation:** If the enhanced perturbation amplitude exceeds a critical threshold (delta_c ~ 0.45 for radiation domination), overdense regions collapse to form PBHs when they re-enter the horizon. The PBH mass is set by the horizon mass at re-entry.
2. **Induced stochastic gravitational wave background:** At second order in perturbation theory, enhanced scalar perturbations source tensor perturbations. This produces a stochastic GW background with a characteristic spectrum determined by the scalar enhancement profile.

### Key paper: Papanikolaou et al. (arXiv:2404.03779)

This 2024 paper proposes that non-singular matter bounces can produce asteroid-mass PBHs (10^17 - 10^22 g) through the enhancement mechanism. Their key results:
- The bounce-to-expansion transition can enhance the scalar power spectrum by a factor of 10^6 - 10^8 at specific scales.
- The enhancement is peaked at k ~ k_bounce (the scale that is horizon-sized at the bounce).
- The PBH mass function is peaked at M ~ 10^17 - 10^22 g, in the "asteroid mass" window where PBHs can constitute a significant fraction (or all) of dark matter.
- The induced GW spectrum peaks in the mHz - Hz band, potentially detectable by LISA and Einstein Telescope.

**Critical caveat:** Their calculation uses a generic bounce (parametrized by a smooth function). They do not use the LQC effective equations. The enhancement depends on the SHARPNESS of the bounce-to-expansion transition.

### Is it genuinely independent of f_NL?

**YES -- completely independent.**

| Property | f_NL channel | PBH/GW channel |
|----------|-------------|----------------|
| k-range | k ~ 0.002 - 0.2 Mpc^-1 | k ~ 10^5 - 10^15 Mpc^-1 |
| Observable | Bispectrum amplitude | DM fraction + GW spectrum |
| Experiments | SPHEREx, MegaMapper | PTA, LISA, ET, CE |
| Generation mechanism | Pre-bounce contraction dynamics | Bounce transition dynamics |
| LQC dependence | Weak (pre-bounce is classical) | Strong (bounce sharpness is LQC-specific) |
| Timeline | 2028-2035 | 2030s (LISA), 2035+ (ET) |

Losing either channel still leaves the other. This is genuine two-observable resilience.

### Is it realistic for the Wilson-Ewing model?

**CONDITIONALLY -- depends on the sharpness of the LQC bounce.**

The LQC effective Friedmann equation gives:
H^2 = (8piG/3) rho (1 - rho/rho_c)

This produces a bounce that is smooth on the Planck time scale. The bounce duration is:
Delta t_bounce ~ 1/sqrt(rho_c) ~ t_Pl

The key question is whether this is "sharp enough" for significant scalar enhancement.

**Arguments FOR sufficient enhancement:**
- The EOS transition is FROM w ~ 0 TO w -> -infinity TO w ~ 0, which is a dramatic change.
- The effective potential in the Mukhanov-Sasaki equation changes sign at the bounce.
- Even a smooth LQC bounce has curvature comparable to the Planck scale, providing strong mode coupling.

**Arguments AGAINST sufficient enhancement:**
- The LQC bounce is Gaussian-like (symmetric, smooth). Sharp features (cusps, rapid oscillations) are absent.
- The Wilson-Ewing model returns to matter domination after the bounce (w ~ 0 on both sides). There is no abrupt EOS change.
- Papanikolaou et al.'s enhancement requires the parametric resonance between the changing EOS and the mode oscillation. A symmetric bounce may not provide this.
- Previous calculations of PBH formation from smooth bounces (e.g., Quintin & Brandenberger 2016, arXiv:1609.02556) found that the enhancement is typically O(1), not O(10^6).

**Estimated probability of viable PBH production: 30-50%.**

The lower end (30%) reflects the smooth-bounce argument. The upper end (50%) reflects the fact that the Wilson-Ewing model has NOT been specifically tested for this, and the quantum corrections near the bounce may introduce features that a simple parametric bounce misses.

### What would need to be checked:

1. **Compute the scalar transfer function T(k) for k ~ k_bounce through the Wilson-Ewing LQC bounce.**
   - Solve the Mukhanov-Sasaki equation numerically through the bounce using the LQC effective equations.
   - Input: the Wilson-Ewing background (dust + Lambda, LQC-corrected Friedmann equation).
   - Output: T(k) = |zeta_post-bounce / zeta_pre-bounce| as a function of k.
   - The computation is straightforward: it is a second-order ODE integration.

2. **Check if T(k) >> 1 for k ~ k_bounce.**
   - If T(k) ~ 1 for all k: no enhancement, channel dead. QUICK KILL.
   - If T(k) >> 1 for k ~ k_bounce: enhancement exists, proceed to step 3.

3. **Compute the PBH mass function from the enhanced power spectrum.**
   - Standard Press-Schechter or peak theory with the enhanced P(k).
   - Compare the PBH abundance with the observational constraints in the asteroid-mass window.

4. **Compute the induced GW spectrum.**
   - Standard second-order calculation from the enhanced scalar spectrum.
   - Compare with LISA sensitivity (mHz band) and ET sensitivity (Hz-kHz band).

### Quick kill:

If T(k) ~ 1 for all k through the LQC bounce, the channel is dead. This can be determined in a single numerical computation (solving the Mukhanov-Sasaki equation through the bounce for a range of k values). Estimated effort: 1-2 sessions.

### Success scenario:

T(k) >> 1 for k in a specific band around k_bounce. The enhanced spectrum produces PBHs in the asteroid-mass window and an induced GW spectrum in the LISA band. This gives:
- A prediction for the PBH dark matter fraction: f_PBH(M) as a function of PBH mass.
- A prediction for the induced GW spectrum: Omega_GW(f) as a function of frequency.
- Both are specific to the Wilson-Ewing model with LQC effective equations -- no free parameters beyond the model's single epsilon.

**Verdict: WORTH PURSUING as #2 priority. Quick kill available via the transfer function computation.**

---

## Channel B: Induced Gravitational Waves (Coupled to Channel A)

This is not independent of Channel A -- it is the gravitational-wave counterpart of the same enhancement mechanism.

If scalar perturbations are enhanced at small scales (Channel A is viable), then at second order in perturbation theory, these enhanced scalars source tensor perturbations. The induced GW spectrum is:

Omega_GW(f) ~ integral of [T(k)]^4 * P_s(k)^2

where T(k) is the transfer function from Channel A and P_s(k) is the primordial scalar power spectrum.

The spectrum peaks at a frequency determined by the enhancement scale:
f_peak ~ 10^-3 Hz * (k_peak / 10^12 Mpc^-1)

For k_peak ~ k_bounce in LQC, f_peak is determined by the LQC bounce energy density rho_c. With rho_c ~ 0.41 M_Pl^4, this gives f_peak in the mHz-Hz range, precisely in the LISA and ET sensitivity bands.

**Verdict: PACKAGE with Channel A. If PBH enhancement exists, induced GWs come for free. No additional calculation beyond what Channel A requires.**

---

## Channel C: Consistency Relation Violation (Tensor Sector)

Standard single-field slow-roll inflation predicts: r = -8 n_T (consistency relation).

The matter bounce predicts:
- n_T > 0 (blue tensor tilt, opposite sign from inflation)
- r ~ 10^-4 (from LQC dressed-metric suppression)
- The consistency relation is violated: r and n_T have the "wrong" relationship.

**However:** r ~ 10^-4 is undetectable by any planned experiment.
- LiteBIRD targets r ~ 0.001 (10x above our value).
- CMB-S4 targets r ~ 0.001.
- No proposed experiment reaches r ~ 10^-4.

Without measuring r, n_T cannot be measured independently (it requires the tensor spectrum amplitude as input).

**Verdict: DEAD as a practical observable.** Keep as a theoretical distinction (the model predicts blue tensor tilt, which is qualitatively distinctive). But it cannot be TESTED on any foreseeable timeline. Do not invest further effort.

---

## Channel D: Scale-Dependent f_NL

If LQC modifications produce k-dependent corrections to f_NL near the bounce scale, the bispectrum would have the form:

f_NL(k) = f_NL^(0) + alpha_fNL * ln(k/k_*)

where f_NL^(0) = -35/8 and alpha_fNL encodes the LQC correction.

### Assessment:

The relevant modes for CMB and LSS observations span k ~ 0.002 - 0.2 Mpc^-1. Over this range, the LQC corrections scale as (k/k_LQC)^2, where k_LQC is the bounce scale. With k_LQC/k_obs ~ 10^56, the running is:

alpha_fNL ~ (k_obs/k_LQC)^2 * (some O(1) coefficient) ~ 10^-112

This is absurdly small. No experiment can detect it.

**The only way scale dependence is observable:** if the contraction dynamics (not the bounce) produce scale dependence. This could happen if:
- The EOS has a slight time dependence during contraction (epsilon is not exactly constant).
- The quasi-dust approximation breaks down at some k.
- Non-linear mode coupling during contraction introduces k-dependent f_NL.

The first of these is real: with epsilon = 0.003, the EOS is not exactly w = 0, and there IS a slow-roll-like correction to f_NL:

delta(f_NL) / f_NL ~ epsilon * ln(k/k_*) ~ 0.003 * 5 ~ 0.015

This is a ~1.5% variation over the observable k range. At MegaMapper precision (sigma ~ 0.5), this corresponds to a delta(f_NL) ~ 0.07 -- detectable only at ~0.14 sigma. Not significant.

**Multi-tracer techniques could improve this.** With optimal multi-tracer analysis, the effective sigma(f_NL) could reach ~0.1 (Seljak 2009), making the running detectable at ~0.7 sigma. Still not significant.

**Verdict: WORTH CHECKING as a free byproduct of the formalism audit (Channel 8 in the openings map). The LQC-specific running is negligible, but the contraction-dynamics running is marginally interesting. Low marginal cost, low expected payoff.**

---

## Channel E: Low-ell CMB Modulation (Agullo et al.)

### Mechanism:
LQC initial-state effects modify the largest-scale modes (ell < 30). The specific vacuum state at the bounce (which modes are excited, which are in the ground state) affects the power at the largest observable scales. This can produce:
- Power suppression at ell < 30 (reduced C_ell relative to best-fit LCDM)
- Hemispherical asymmetry (if the initial state has a preferred direction)
- Oscillatory features in the power spectrum at ell ~ 20-40

### Key papers:
- Agullo, Ashtekar, Nelson (2013): initial conditions in LQC affect low-ell power.
- Agullo (2015): LQC can explain the observed low-ell anomalies.
- Agullo, Morris (2015): power suppression and hemispherical asymmetry from excited initial states.

### Assessment:
**The evidence for low-ell anomalies is 2-3 sigma.** Planck reports:
- Low quadrupole (C_2): ~2 sigma low relative to best-fit LCDM.
- Hemispherical asymmetry: ~3 sigma.
- Cold spot: ~2 sigma.

These anomalies are intriguing but NOT compelling:
- Cosmic variance at ell < 30 is large (only 2*ell+1 modes per ell).
- A posteriori statistics inflate significance (we look at many possible anomalies and report the most anomalous).
- No single LQC model simultaneously explains all anomalies with specific parameter values.

**For our specific model (Wilson-Ewing quasi-dust):**
- No quantitative prediction for low-ell power exists. The model specifies the contraction dynamics and the bounce, but the initial vacuum state at the bounce is an additional input.
- The low-ell anomalies could be explained by choosing an appropriate initial state, but this is FITTING, not predicting.
- Without a specific, parameter-free prediction for the C_ell at ell < 30, this channel cannot serve as a discriminator.

**Verdict: LOW PRIORITY.** Only revisit if the formalism audit (Opening 8 in the openings map) reveals that dressed-metric and hybrid give different low-ell predictions -- in that case, the vacuum prescription becomes observationally relevant and worth investigating. Otherwise, this is a fitting exercise, not a prediction.

---

## Summary Ranking

| Rank | Channel | Independence | Detectability | Quick Kill Available | Verdict |
|------|---------|-------------|--------------|---------------------|---------|
| 1 | PBH + Induced GW (A+B) | YES (different k, different experiment) | Conditional (30-50%) | YES (transfer function) | PURSUE |
| 2 | Scale-dependent f_NL (D) | Partial (same observable, different aspect) | Low (<1 sigma) | YES (OOM estimate) | CHECK AS BYPRODUCT |
| 3 | Low-ell modulation (E) | YES (different ell range) | Marginal (2-3 sigma anomalies) | Unclear | LOW PRIORITY |
| 4 | Consistency relation (C) | YES (tensor sector) | NONE (r too small) | N/A | DEAD |

---

## Architecture Recommendation

### Two-observable system:

**Primary:** f_NL = -35/8 at large scales
- Observable: local-type bispectrum amplitude
- Experiments: SPHEREx (2028-2030, marginal), MegaMapper (2032-2035, decisive)
- Status: 75% confidence in the prediction, needs verification

**Secondary:** PBH abundance + induced GW spectrum at small scales -- IF viable
- Observable: PBH dark matter fraction f_PBH(M) + GW energy density Omega_GW(f)
- Experiments: LISA (2037+, mHz band), Einstein Telescope (2035+, Hz-kHz band)
- Status: UNTESTED, 30-50% probability of viability

### Resilience analysis:

| Scenario | Primary survives | Secondary survives | Program status |
|----------|-----------------|-------------------|---------------|
| Both viable | YES | YES | STRONG -- two independent tests |
| f_NL confirmed, PBH dead | YES | NO | ADEQUATE -- single decisive test |
| f_NL wrong, PBH viable | NO | YES | ALIVE -- alternative test available |
| Both fall | NO | NO | DEAD -- model indistinguishable from inflation |

The current architecture (f_NL only) corresponds to row 2 or row 4, with no row 3 option. Adding the PBH channel opens row 3, providing genuine resilience.

**The probability of scenario "both fall" drops from ~25% (current) to ~12.5-17.5% (with PBH channel assessed).** Even if the PBH channel turns out dead, the quick-kill assessment costs only 1-2 sessions and resolves the uncertainty.

---

## Immediate Action Items

1. **PBH quick kill (priority #2 overall, after formalism audit):**
   - Solve the Mukhanov-Sasaki equation through the Wilson-Ewing LQC bounce numerically.
   - Extract T(k) for k ~ k_bounce.
   - If T(k) ~ 1: channel dead, document and move on.
   - If T(k) >> 1: proceed to PBH mass function and induced GW spectrum.
   - Effort: 1-2 sessions.

2. **Scale-dependent f_NL check (during formalism audit):**
   - Estimate alpha_fNL from contraction-dynamics running.
   - Confirm LQC-specific running is negligible.
   - Effort: 0 additional sessions (embedded in formalism audit work).

3. **Low-ell modulation (only if triggered by formalism audit):**
   - Revisit only if dressed-metric vs hybrid give different vacuum prescriptions with observable consequences.
   - Effort: 1 session if triggered, 0 otherwise.
