# Track 2: PBH + Induced GW Channel Assessment

**Created:** 2026-03-24
**Status:** COMPLETE
**Paper analyzed:** Papanikolaou, Banerjee, Cai, Capozziello, Saridakis (2024), arXiv:2404.03779, JCAP 06 (2024) 066, 37 citations.
**Supporting reference:** Papanikolaou, He, Ma, Cai, Saridakis, Sasaki (2024), arXiv:2403.00660 (f_NL-PBH-GW connection).
**Contrasting reference:** Quintin & Brandenberger (2016), arXiv:1609.02556 (PBH formation in contracting universes).

---

## 1. Paper Summary: What Papanikolaou et al. Actually Compute

### 1.1 Their Bounce Model

They use a **generic, model-independent parametrized bounce** -- explicitly NOT LQC, NOT Einstein-Cartan, NOT any specific UV-complete theory. Their bounce is:

**Three phases:**

| Phase | Scale factor | EOS |
|-------|-------------|-----|
| Matter contraction (t < t_-) | a(t) = a_- [(t - t~_-)/(t_- - t~_-)]^{2/3} | w = 0 |
| Bouncing phase (t_- < t < t_+) | a(t) = a_b exp(Upsilon t^2 / 2) | NEC-violating |
| Radiation expansion (t > t_+) | a(t) = a_+ [(t - t~_+)/(t_+ - t~_+)]^{1/2} | w = 1/3 |

The bounce parameter **Upsilon** controls the bounce curvature: H(t) = Upsilon * t during the bouncing phase. Larger Upsilon = sharper/faster bounce.

**Matching conditions** enforce continuity of a(t) and H(t) at t_- and t_+, giving:
- t_+ = H_+ / Upsilon
- t_- = 2 / (3 H_-)

### 1.2 Their Free Parameters

Three parameters:
1. **Upsilon** -- bounce curvature (determines transition rate)
2. **H_-** -- Hubble parameter at end of contraction (sets contraction energy scale)
3. **H_+** -- Hubble parameter at start of radiation era (sets expansion energy scale)

Plus the sound speed during the bounce **c_{s,b}**, which they leave unspecified (it depends on the underlying gravity theory).

One constraint: **CMB normalization** (their Eq. 2.17) forces the large-scale power spectrum to match P_zeta ~ 2.1 x 10^{-9}. This reduces effective freedom to 2 free parameters.

**Benchmark values (their Figure 1):**
- H_+ = 10^{-10} M_Pl
- H_- = 6 x 10^{-11} M_Pl
- Upsilon = 1.7345 x 10^{-10} M_Pl^2

**Critical observation: H_- != H_+.** This is an ASYMMETRIC bounce. The energy density at the start of the bounce differs from the energy density at the end. This asymmetry is a key ingredient.

### 1.3 Enhancement Mechanism

The power spectrum enhancement operates through **two compounding effects:**

**Effect 1: Growing mode during matter contraction.**
During dust contraction (w = 0), the curvature perturbation zeta has a constant mode and a growing mode. The growing mode goes as:

    zeta_growing ~ (k eta)^2

For modes with larger k (smaller wavelength), the growing mode contribution at the bounce is proportionally larger. This produces a power spectrum that rises as P_zeta(k) ~ k at intermediate scales.

**Effect 2: Asymmetric matter-to-radiation transition.**
The transition from w = 0 (contraction) to w = 1/3 (expansion) through the bounce creates a matching-coefficient enhancement. The Mukhanov-Sasaki variable v_k evolves differently in the three phases, and the matching at the transitions (t_- and t_+) introduces k-dependent amplification.

Their final power spectrum (Eq. 2.3) is a three-term expression:
- **Term 1 (k^0):** Scale-invariant constant, matched to CMB amplitude
- **Term 2 (k^{1/2} or k^1):** Linear growth on intermediate scales
- **Term 3 (higher k):** Oscillatory features at small scales

### 1.4 PBH Results

- **PBH mass window:** Asteroid-mass range, 10^{17} - 10^{24} g
- **Dark matter fraction:** f_PBH ~ 1 achievable (potentially ALL of dark matter)
- **Threshold:** Standard delta_c ~ 0.4 for radiation-dominated collapse
- **Formation mechanism:** Press-Schechter / peak theory on enhanced spectrum

### 1.5 Induced GW Results

- **Detectors:** SKA, PTAs, LISA, Einstein Telescope
- **Frequency range:** nHz (PTA) through mHz (LISA) to Hz (ET)
- **Source:** Second-order tensor perturbations from enhanced scalar spectrum
- **Omega_GW ~ [P_zeta(k)]^2** -- quadratic in the scalar enhancement

### 1.6 Energy Scale

Their benchmark uses H_+ ~ 10^{-10} M_Pl, corresponding to a bounce energy scale:

    rho_bounce ~ 3 M_Pl^2 H_+^2 ~ 3 x 10^{-20} M_Pl^4

This is **dramatically below Planck density** -- about 20 orders of magnitude below ours (rho_crit = 0.21 M_Pl^4 in the LQC model). This is NOT a Planck-scale bounce.

---

## 2. Their Model vs Our Model B: Critical Comparison

### 2.1 Background Equations

| Feature | Papanikolaou et al. | Our Model B (Wilson-Ewing LQC) |
|---------|--------------------|-----------------------------|
| Modified Friedmann eq | H = Upsilon * t (exponential a(t)) | H^2 = (8piG/3) rho (1 - rho/rho_c) |
| Bounce mechanism | Generic parametrization | LQC holonomy corrections |
| Bounce energy scale | H ~ 10^{-10} M_Pl (free parameter) | rho_c = 0.41 rho_Pl (fixed) |
| Bounce symmetry | ASYMMETRIC (H_- != H_+) | SYMMETRIC (same w on both sides) |
| EOS at bounce | Unspecified (NEC-violating) | w = 0 (dust) or w = 1/3 (radiation) |
| Contraction EOS | w = 0 (dust) | w = 0 (dust) -- SAME |
| Expansion EOS | w = 1/3 (radiation) | w = 0 (dust) initially, then reheating to radiation |
| Sound speed at bounce | c_{s,b} (free parameter) | Fixed by matter content |
| Free parameters | 3 (Upsilon, H_-, H_+) | 1 (epsilon = 0.003 for quasi-dust) |

### 2.2 The Three Critical Differences

**Difference 1: Energy scale.**
Their bounce is at H ~ 10^{-10} M_Pl. Ours is at rho_c ~ 0.41 M_Pl^4, which gives H_max ~ sqrt(rho_c / M_Pl^2) ~ 0.6 M_Pl. Our bounce is 10 orders of magnitude higher in energy. This changes the characteristic bounce wavenumber k_bounce = a_b * H_max by 10 orders of magnitude, shifting all PBH masses and GW frequencies.

**Difference 2: Symmetry of the bounce.**
Their bounce is ASYMMETRIC: matter contraction (w = 0) transitions to radiation expansion (w = 1/3) through the bounce. Our Wilson-Ewing Model B has the same EOS on both sides of the bounce: dust in, dust out. The w = 0 -> w = 1/3 transition happens AFTER the bounce (during reheating), not AT the bounce.

This is the single most important difference. Their enhancement mechanism relies on the EOS change from w = 0 to w = 1/3 occurring AT the bounce. In our model, the bounce occurs entirely within the dust phase. A symmetric dust-to-dust bounce may not produce the same enhancement.

**Difference 3: Bounce sharpness and profile.**
Their exponential bounce a(t) = a_b exp(Upsilon t^2/2) gives H(t) = Upsilon t, which is exactly linear in t -- the SIMPLEST possible bounce profile. Our LQC bounce has a(t) = a_b (1 + 4 alpha^2 t^2)^{1/4}, giving H(t) = 2 alpha^2 t / (1 + 4 alpha^2 t^2). The LQC profile has a SATURATION at large t (H -> 1/(2t)), whereas theirs grows without bound. The difference in the effective potential z''/z near the bounce could significantly affect the transfer function.

### 2.3 What Maps and What Doesn't

| Feature | Maps to our model? | Comment |
|---------|-------------------|---------|
| Dust contraction | YES | Identical dynamics far from bounce |
| Growing mode in contraction | YES | Same physics |
| k-dependent growing mode amplitude | YES | Same (k eta)^2 scaling |
| Bounce parametrization | NO | Different functional form |
| Matter-to-radiation at bounce | NO | Our bounce is matter-to-matter |
| Sound speed at bounce | PARTIALLY | c_s = 1 for scalar field dust |
| PBH mass window | NEEDS RECALCULATION | Different k_bounce |
| Induced GW frequency | NEEDS RECALCULATION | Different f_bounce |

---

## 3. Transfer Function Analysis: What Determines T(k) >> 1 vs T(k) ~ 1

### 3.1 Physics of the Enhancement

The transfer function T(k) = |zeta_post / zeta_pre| measures how much the curvature perturbation is amplified by the bounce. For our model to produce PBHs, we need T(k) >> 1 for some range of k near k_bounce.

Three physical ingredients determine T(k):

**Ingredient 1: The growing mode during contraction.**
During dust contraction, both the constant mode (zeta = const) and growing mode (zeta ~ (k eta)^2) are present. For super-Hubble modes (k eta << 1), the constant mode dominates. For near-Hubble modes (k eta ~ 1), the growing mode contributes comparably. At the bounce, modes with k ~ k_bounce have k eta ~ 1, so the growing mode is maximally important.

This ingredient is IDENTICAL in our model and theirs. The dust contraction dynamics are the same.

**Ingredient 2: The EOS transition.**
When the EOS changes from w = 0 to w = 1/3, the matching of zeta and zeta' at the transition boundary introduces k-dependent amplification. The curvature perturbation zeta is conserved on super-Hubble scales for adiabatic perturbations REGARDLESS of w. But for modes near the Hubble scale at the transition, zeta is NOT conserved -- the transition creates a new growing mode.

This ingredient is DIFFERENT in our model. In our Wilson-Ewing model, the bounce occurs at w = 0 on both sides. There is no EOS change at the bounce itself. The w = 0 -> w = 1/3 transition occurs later, during reheating, when the scalar field starts to decay. If the reheating is gradual, this transition does not produce sharp spectral features.

**Ingredient 3: The bounce itself (quantum gravity corrections).**
The LQC effective equations modify the Friedmann equation at rho ~ rho_c. This modifies the effective potential z''/z in the Mukhanov-Sasaki equation for k ~ k_bounce. The quantum corrections could EITHER enhance or suppress perturbations at these scales, depending on the sign and magnitude of the correction to z''/z.

This ingredient is UNIQUE to our model and has NOT been calculated for the specific Wilson-Ewing LQC bounce.

### 3.2 The Symmetric Bounce Problem

For a SYMMETRIC bounce (same EOS on both sides), there is a general argument that T(k) ~ 1 for all k:

**Argument:** If the bounce is symmetric under time reversal (t -> -t), then the Mukhanov-Sasaki equation is also symmetric. A mode that enters the bounce with amplitude A exits with amplitude A (possibly with a phase shift). There is no net amplification because the "growth" during the first half of the bounce is exactly undone by "decay" during the second half.

This argument applies to the Wilson-Ewing dust bounce: a(t) = a_b (1 + 4 alpha^2 t^2)^{1/4} is symmetric under t -> -t. The Bardeen potential equation is also symmetric (all coefficients depend on t^2, not t).

**Our Branch K confirmed this:** T(k) = 1 for all k << k_b, with deviations of order (k/k_b)^2.

**Our numerical results from dust_bounce_spectrum/05_power_spectrum.md:**

| k/k_b | T(k) | Deviation from 1 |
|--------|------|-----------------|
| 10^{-4} | 1.000 | reference |
| 3.6 x 10^{-4} | 1.008 | 0.8% |
| 10^{-3} | 1.061 | 6.1% |
| 3.3 x 10^{-3} | 1.740 | 74% |
| 10^{-2} | 5.69 | 469% |

**The transfer function DOES grow** as k -> k_b, reaching T ~ 5.7 at k/k_b = 10^{-2}. But we have NOT computed T(k) for k/k_b ~ 0.1 to 1. This is exactly the range needed for PBH formation.

### 3.3 What Could Save the Channel

Even though the bounce is symmetric in time, three effects could produce T(k) >> 1:

**Effect A: The dust-to-radiation transition before or after the bounce.**
If we include the reheating transition (w: 0 -> 1/3) that occurs after the bounce, modes that are near the Hubble scale at the transition time could be enhanced. This is the SAME mechanism as Papanikolaou et al., just temporally displaced from the bounce. The question is: how soon after the bounce does reheating occur? If it occurs within a few Hubble times, the effect could be significant for k ~ k_reheating.

**Effect B: Asymmetry from quantum corrections.**
The LQC effective equations have higher-order corrections beyond the (1 - rho/rho_c) term. If these break the t -> -t symmetry of the bounce, T(k) could deviate from 1 even for the symmetric bounce. This requires going beyond the effective Friedmann equation to the full LQC effective dynamics.

**Effect C: Non-adiabatic pressure perturbations.**
If the matter is a scalar field (not truly pressureless dust), the c_s = 1 propagation speed during the bounce creates oscillatory behavior in modes with k ~ k_b. These oscillations, combined with the rapid change in z''/z at the bounce, could produce parametric resonance -- amplification of specific k bands. This is a standard mechanism in preheating and could work here.

---

## 4. The Quick-Kill Computation

### 4.1 What Needs to Be Solved

**The Mukhanov-Sasaki equation through the Wilson-Ewing bounce for k ~ k_bounce:**

    v_k'' + (k^2 - z''/z) v_k = 0

where z = a phi_dot / H for a scalar field, and primes are conformal time derivatives.

**The LQC background:**

    a(eta) derived from a(t) = a_b (1 + 4 alpha^2 t^2)^{1/4}

with alpha^2 = rho_crit / (3 M_Pl^2) ~ 1.76 M_Pl^2.

### 4.2 For What k Values?

The bounce wavenumber:

    k_bounce = a_b * sqrt(2 alpha) ~ a_b * 1.88 M_Pl

In Planck units with a_b = 1: k_bounce ~ 1.88.

We need T(k) for k/k_bounce from 10^{-3} to 1 (and possibly above 1).

Our existing computation goes up to k/k_b = 10^{-2}. **We need to extend it by 2 orders of magnitude toward k/k_b ~ 1.**

### 4.3 What T(k) Threshold Is Needed?

For PBH formation, the scalar power spectrum must reach:

    P_zeta(k_PBH) > delta_c^2 / sigma^2 ~ 10^{-2}

The large-scale CMB amplitude is P_zeta ~ 2.1 x 10^{-9}. So the enhancement factor needed is:

    T(k)^2 * P_zeta_CMB > 10^{-2}
    T(k) > sqrt(10^{-2} / 2.1 x 10^{-9}) ~ 2 x 10^3

**We need T(k) > ~2000 for PBH formation.**

However, the growing mode during dust contraction ALREADY provides some k-dependent enhancement. The pre-bounce power spectrum is not flat -- it rises as P_zeta ~ k for the growing mode contribution. The question is whether the total enhancement (growing mode + bounce transfer) reaches 10^{-2} at any k.

### 4.4 Is This Analytical or Numerical?

**Primarily numerical.** The LQC bounce background a(t) = a_b (1 + 4 alpha^2 t^2)^{1/4} gives a complicated z''/z that does not admit simple Hankel function solutions. The Mukhanov-Sasaki equation must be integrated numerically through the bounce.

However, there is a useful analytical check: the WKB approximation for k >> k_b gives T(k) ~ 1 (high-frequency modes propagate freely). And the long-wavelength limit k << k_b gives T(k) = 1 (known from Branch K). The interesting region is k ~ k_b, which requires numerics.

**Estimated computation:** A straightforward ODE integration (Runge-Kutta 4/5) for ~100 k values spanning k/k_b = 10^{-3} to 10. This is a single-session computation, runnable in Python/numpy in minutes.

### 4.5 The z''/z Singularity Problem

**WARNING:** The Mukhanov-Sasaki variable v = z * zeta diverges at the bounce because z = a phi_dot / H -> infinity as H -> 0. This is a coordinate singularity, not physical. Our previous calculation (dust_bounce_spectrum/02_scalar_mode_equation.md) addressed this by switching to the Bardeen potential Phi, which is regular through the bounce.

**For the quick-kill computation, use the Bardeen potential equation:**

    Phi_ddot + (4 + 3c_s^2) H Phi_dot + [c_s^2 k^2/a^2 + 2 H_dot + (3 + 3c_s^2) H^2] Phi = 0

This is regular at H = 0 (all coefficients finite). At the bounce:

    Phi_ddot + [k^2/(3 a_b^2) + 2 H_dot(0)] Phi = 0

which is a simple harmonic oscillator.

---

## 5. If Viable: PBH Mass Window and GW Frequency

### 5.1 PBH Mass from LQC Bounce

The PBH mass is set by the horizon mass at re-entry:

    M_PBH ~ M_Pl^2 / H_reentry ~ M_Pl^2 * a_reentry / k

For modes with k ~ k_bounce = a_b * sqrt(2 alpha):

    M_PBH ~ M_Pl^2 / (sqrt(2 alpha)) ~ M_Pl / (1.88) ~ 0.5 M_Pl ~ 10^{-5} g

This is **Planck-mass PBH** -- they evaporate essentially instantly via Hawking radiation (evaporation time ~ 10^{-43} s).

**This is bad news.** The Planck-energy LQC bounce produces perturbation enhancement at the Planck scale, which corresponds to Planck-mass PBHs. These are far too light to survive to the present day. The asteroid-mass window (10^{17} - 10^{24} g) requires enhancement at much larger scales, which means k << k_bounce by many orders of magnitude.

### 5.2 The Scale Hierarchy Problem

To produce asteroid-mass PBHs (M ~ 10^{20} g ~ 10^{25} M_Pl):

    k_PBH / k_bounce ~ (M_Pl / M_PBH)^{1/2} ~ (10^{-25})^{1/2} ~ 10^{-12.5}

So we need enhancement at k/k_bounce ~ 10^{-13}. But our transfer function shows T(k) deviates from 1 only for k/k_bounce > 10^{-3}. At k/k_bounce ~ 10^{-13}, the transfer function is:

    T(k) - 1 ~ (k/k_b)^2 ~ 10^{-26}

**This is T(k) = 1 to 26 decimal places. There is ZERO enhancement at the asteroid-mass scale.**

### 5.3 How Papanikolaou et al. Avoid This Problem

Their bounce energy is H ~ 10^{-10} M_Pl, not H ~ 1 M_Pl. This is 10 orders of magnitude lower. Their bounce wavenumber is correspondingly smaller:

    k_bounce(theirs) / k_bounce(ours) ~ H_their / H_ours ~ 10^{-10}

This shifts the PBH mass upward by 20 orders of magnitude:

    M_PBH(theirs) ~ M_PBH(ours) * (k_ours / k_theirs)^2 ~ 10^{-5} g * 10^{20} ~ 10^{15} g

which is in the right ballpark for asteroid-mass PBHs.

**The low-energy bounce is essential for their mechanism.** A Planck-scale bounce cannot produce observable PBHs through the transfer function enhancement. The PBHs would be at the Planck mass and evaporate immediately.

### 5.4 Could the Growing Mode Save Us?

The growing mode during dust contraction produces P_zeta ~ k at intermediate scales, independent of the bounce transfer function. Could this linear growth reach the PBH threshold at some k?

The growing mode amplitude at k is:

    P_zeta(k) ~ A_s * (k / k_CMB) ~ 2.1 x 10^{-9} * (k / k_CMB)

For PBH formation: P_zeta > 10^{-2}

    k / k_CMB > 10^{-2} / (2.1 x 10^{-9}) ~ 5 x 10^6

So we need k > 5 x 10^6 * k_CMB ~ 0.25 Mpc^{-1}.

The corresponding PBH mass:

    M_PBH ~ (k_CMB / k)^2 * 10^{50} g ~ (5 x 10^6)^{-2} * 10^{50} g ~ 4 x 10^{36} g ~ 2000 M_sun

These are MASSIVE PBHs -- supermassive black hole seeds, not asteroid-mass PBHs. And they are in the mass range that is STRONGLY CONSTRAINED by CMB spectral distortions, accretion limits, and dynamical friction.

**BUT WAIT:** The linear growth P_zeta ~ k is the growing mode prediction from dust contraction. This growth continues until the mode enters the Hubble radius. For k >> k_CMB but k << k_bounce, the growth saturates when k * eta ~ 1, i.e., at the Hubble crossing time during contraction.

The actual power spectrum from the growing mode has been computed (Cai & Wilson-Ewing 2014, our dust_bounce_spectrum calculations). The result is more nuanced than simple linear growth -- the spectrum rises, peaks, and then oscillates. The peak location and amplitude depend on the transition from dust to whatever happens next.

**This is the same mechanism as Papanikolaou et al. -- but the details depend on the transition, not the bounce.**

### 5.5 GW Frequency for LQC Bounce

If PBHs were to form at k ~ k_bounce (Planck scale):

    f_GW ~ k_bounce / (2 pi a_0) ~ 8 GHz

This is the frequency we already computed in Branch M. It is 10+ orders of magnitude above any detector.

For the growing-mode-induced PBHs at k ~ 10^6 * k_CMB:

    f_GW ~ 10^6 * f_CMB ~ 10^6 * 10^{-18} Hz ~ 10^{-12} Hz

This is in the ultra-low-frequency regime, below even PTA sensitivity (nHz ~ 10^{-9} Hz).

**Neither the bounce-scale nor the growing-mode-scale PBHs produce GW in detectable frequency bands for the LQC bounce.**

---

## 6. The f_NL Consistency Test Idea

### 6.1 The Double-Observable Architecture

Papanikolaou et al. (2403.00660) showed that primordial non-Gaussianity (f_NL) imprints on:
1. PBH clustering properties (spatial distribution)
2. The spectral shape of induced GW (double-peaked spectrum)

If our model produced PBHs, the SAME f_NL = -35/8 that SPHEREx would measure in the CMB bispectrum would independently affect:
- The PBH abundance (non-Gaussian tail enhancement)
- The PBH clustering (scale-dependent bias)
- The induced GW spectrum shape (double peak vs single peak)

This would give TWO INDEPENDENT MEASUREMENTS of f_NL from DIFFERENT experiments:
- SPHEREx/MegaMapper: f_NL from galaxy bispectrum (2028-2035)
- LISA/ET: f_NL from GW spectral shape (2035+)

### 6.2 Viability Assessment for Our Model

**This is a beautiful idea that does NOT work for our specific model.**

The reason is Section 5 above: the LQC bounce at Planck energy does not produce PBHs in any observable mass window. The growing-mode enhancement occurs at scales too large (supermassive PBHs) or the bounce-transfer enhancement occurs at scales too small (Planck-mass PBHs, instant evaporation). There is no "sweet spot" that produces asteroid-mass PBHs with detectable induced GW.

The f_NL consistency test remains a powerful discriminator in PRINCIPLE, but it requires:
- A lower-energy bounce (H_bounce << M_Pl), OR
- A spectator field that introduces a new scale between k_CMB and k_bounce

Neither is present in our minimal Wilson-Ewing model.

---

## 7. Honest Probability Assessment

### 7.1 Can We Get T(k) >> 1 from the LQC Bounce?

**YES, we almost certainly can -- but only at k ~ k_bounce ~ M_Pl, which produces Planck-mass PBHs that evaporate instantly.**

Our existing data shows T(k) = 5.69 at k/k_b = 10^{-2}. Extrapolating the trend (T ~ (k/k_b)^2 growth), we expect:
- T(k/k_b = 0.1) ~ 50-100
- T(k/k_b = 0.5) ~ 500-2000
- T(k/k_b = 1.0) ~ 2000-5000

**The enhancement IS there -- it is just at the wrong scale.**

### 7.2 Can We Get PBHs in a Detectable Mass Window?

**NO, not from the minimal Wilson-Ewing Model B.**

The fundamental problem is the Planck-scale bounce. The bounce transfer function peaks at k ~ k_bounce ~ M_Pl. The PBH mass from these modes is M ~ M_Pl ~ 10^{-5} g, which evaporates in t ~ 10^{-43} s.

To get asteroid-mass PBHs (M ~ 10^{20} g), we would need enhancement at k/k_bounce ~ 10^{-13}, where the transfer function is T = 1 + O(10^{-26}).

### 7.3 Can the Growing Mode Produce PBHs?

**POTENTIALLY -- but this is NOT a bounce-specific prediction.**

The growing mode during dust contraction amplifies perturbations at intermediate scales. If the dust-to-radiation transition is sharp enough, the enhanced spectrum could reach PBH thresholds. But this mechanism:
1. Depends on the transition, not the bounce
2. Is NOT unique to LQC or any specific bounce model
3. Has been studied by Papanikolaou et al. and others using generic bounces
4. Produces PBHs at masses set by the transition time, not the bounce time

### 7.4 Updated Probability

| Scenario | Previous estimate | Updated estimate | Reason for change |
|----------|------------------|-----------------|-------------------|
| PBH from bounce-scale T(k) | 30-50% | **<1%** | Planck-mass PBHs evaporate instantly |
| PBH from growing mode | Not assessed | **10-20%** | Depends on transition, not bounce-specific |
| Detectable induced GW | 30-50% | **<1%** | Wrong frequency range for both mechanisms |
| f_NL consistency test | High if PBHs | **<1%** | No PBH production -> no test |

**Overall viability of Channel A (PBH + GW as second observable): 10-20%.**

The surviving possibility is the growing-mode mechanism, but this is NOT bounce-specific and does not uniquely probe the LQC model. It is a feature of the dust contraction, not the bounce.

---

## 8. Concrete Next Steps

### 8.1 The Quick Kill (1 session, HIGH VALUE)

**Compute T(k) for k/k_b from 10^{-2} to 10.**

We already have the numerical infrastructure (dust_bounce_spectrum/04_mode_solver.ipynb). Extend the k-range of the Bardeen potential integration to cover the near-bounce-scale modes. This will:

1. Confirm/refute whether T(k) >> 1 at k ~ k_b
2. Map the full shape of T(k) through the bounce
3. Determine whether the LQC bounce is "sharp enough" to produce significant enhancement
4. Produce a clean, publishable figure: T(k) for the Wilson-Ewing LQC bounce

**This computation has value even if PBHs are ruled out**, because it completes the characterization of the Wilson-Ewing bounce transfer function across ALL scales (currently we only have k/k_b << 1).

### 8.2 If T(k) >> 1 Is Found (2-3 sessions)

Even if the PBH mass window is wrong (Planck-mass), the enhanced spectrum near k_b could produce:
1. **Gravitational wave background at GHz** -- undetectable but theoretically interesting
2. **Constraints on the LQC bounce** from overproduction of Planck-mass PBHs (even if they evaporate, their Hawking radiation contributes to the radiation background)
3. **Modified BBN** if Planck-mass PBH evaporation injects entropy

### 8.3 If We Want to Pursue the Growing-Mode PBH Channel (3-5 sessions)

This requires specifying the dust-to-radiation transition in detail:
1. Model the reheating mechanism (scalar field decay to radiation)
2. Compute the power spectrum through the transition for k ~ k_transition
3. Determine whether the spectrum reaches P_zeta > 10^{-2}
4. If yes: compute PBH mass function and induced GW spectrum

**This is a substantial computation that should only be pursued if the quick kill in 8.1 reveals interesting near-bounce-scale physics.** Otherwise, the channel is dead at the quick-kill stage.

### 8.4 Tools and Codes Needed

| Tool | Purpose | Status |
|------|---------|--------|
| Python + numpy/scipy | ODE integration | Available |
| dust_bounce_spectrum/04_mode_solver.ipynb | Existing Bardeen solver | EXTEND k-range |
| Matplotlib | Transfer function plots | Available |
| (Optional) CLASS/CAMB modified | Full Boltzmann for PBH + GW | Not needed for quick kill |

### 8.5 Computational Details

The Bardeen potential ODE is:

    Phi'' + (4 + 3 c_s^2) H Phi' + [c_s^2 k^2/a^2 + 2 H' + (3 + 3 c_s^2) H^2] Phi = 0

with the LQC background:

    a(t) = a_b (1 + 4 alpha^2 t^2)^{1/4}
    H(t) = 2 alpha^2 t / (1 + 4 alpha^2 t^2)
    H'(t) = 2 alpha^2 (1 - 4 alpha^2 t^2) / (1 + 4 alpha^2 t^2)^2

For the scalar field with c_s = 1 during the bounce and c_s^2 = 0 (effectively) during dust contraction.

Initial conditions: Bunch-Davies vacuum in the far past, giving Phi_k = const + decaying mode.

Integration: From t_start << 0 through t = 0 (bounce) to t_end >> 0.

Output: T(k) = |Phi_out(k) / Phi_out(k_ref)| for ~200 k values.

**Estimated runtime:** < 10 minutes on a laptop.

---

## 9. Summary Verdict

### What Papanikolaou et al. Actually Show

Their paper demonstrates that a **generic, low-energy, asymmetric matter bounce** can produce asteroid-mass PBHs and detectable induced GW. The mechanism is real, the calculation is correct, and the results are interesting. The paper has 37 citations because it connects two active fields (bouncing cosmology and PBH dark matter).

### Why It Doesn't Apply to Our Model

Three fatal incompatibilities:

1. **Energy scale:** They use H ~ 10^{-10} M_Pl. We use rho_c ~ 0.41 M_Pl^4 (H ~ M_Pl). Our bounce is 10 orders of magnitude too energetic. Enhanced modes at k_bounce produce Planck-mass PBHs, not asteroid-mass PBHs.

2. **Symmetry:** They use an asymmetric bounce (matter in, radiation out). Our Wilson-Ewing bounce is symmetric (same w on both sides). The asymmetry is crucial for their enhancement mechanism.

3. **Transition:** Their power spectrum enhancement relies on a matter-to-radiation EOS transition occurring DURING the bounce. In our model, this transition occurs AFTER the bounce during reheating.

### What Remains Alive

The **quick-kill computation** (T(k) for k ~ k_b through the LQC bounce) is still worth doing because:
1. It completes our characterization of the Wilson-Ewing bounce
2. The result (whatever it is) is publishable as part of the model description
3. If T(k) >> 1 near k_b, it has implications for Planck-mass PBH overproduction constraints
4. The computation takes < 1 session

### Channel A Status

**DOWNGRADED from "PURSUE" to "QUICK KILL ONLY."**

The PBH/GW channel is not a viable second independent observable for our Model B. The energy scale mismatch and bounce symmetry prevent the Papanikolaou et al. mechanism from operating. The growing-mode alternative is not bounce-specific and does not probe the LQC model.

**The program's observational resilience remains single-point-of-failure: f_NL = -35/8 is the only distinctive, measurable prediction.**

### One Remaining Hope

If the f_NL verification (ranked path #1) confirms f_NL = -35/8, and if the Papanikolaou et al. (2403.00660) f_NL-PBH-GW connection can be adapted to a scenario where:
- A DIFFERENT bouncing model (lower energy, asymmetric) produces the bounce
- BUT the dust contraction is the SAME (producing the same f_NL = -35/8)

Then the f_NL value would be the LINK between the two models: our LQC-derived prediction for the bispectrum matches onto their PBH model's predictions for the GW spectrum. This is conceptually interesting but requires abandoning the specific LQC bounce in favor of a generic lower-energy bounce, which undermines the parameter-free nature of the Wilson-Ewing model.

---

## References

1. Papanikolaou, Banerjee, Cai, Capozziello, Saridakis (2024), arXiv:2404.03779, JCAP 06 (2024) 066.
2. Papanikolaou, He, Ma, Cai, Saridakis, Sasaki (2024), arXiv:2403.00660.
3. Quintin & Brandenberger (2016), arXiv:1609.02556.
4. Wilson-Ewing (2013), arXiv:1211.6269.
5. Cai & Wilson-Ewing (2014), arXiv:1412.2914.
6. Cai, Xue, Brandenberger & Zhang (2009), arXiv:0903.0631.
