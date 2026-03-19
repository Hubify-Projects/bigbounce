# Second Observable Channel Audit

**Created:** 2026-03-18
**Status:** COMPLETE
**Purpose:** The program has a single-point-of-failure architecture (f_NL = -35/8). This file audits all candidate second observable channels to determine whether any can provide an independent test of the Wilson-Ewing LQC matter bounce.

---

## The Problem

Model B (Wilson-Ewing LCDM quasi-dust bounce) has exactly ONE distinctive, testable prediction: f_NL^local = -35/8 = -4.375.

Everything else is either:
- **Fitted** (n_s from epsilon = 0.003)
- **Undetectable** (r ~ 10^-4, tensor tilt, consistency relation)
- **Bounce-independent** (birefringence from ALP, MCMC constraints on DeltaN_eff)

If f_NL falls -- due to a calculation error, a formalism dependence, or LQC bounce transfer effects -- the model has no fallback. A second independent observable would transform the program from single-point-of-failure to two-test architecture.

---

## Channel A: Primordial Black Holes from Matter Bounce

### Mechanism
The matter bounce produces a nearly scale-invariant scalar power spectrum at large scales (CMB), but the transition from contraction to expansion can enhance perturbations at SMALL scales (near the bounce scale). If the enhancement is sufficient (delta_c ~ 0.45 threshold), asteroid-mass PBHs form and could constitute a fraction of dark matter. The associated second-order induced gravitational wave background would produce a stochastic signal detectable by PTA, LISA, or Einstein Telescope.

Key reference: Papanikolaou, Lymperis & Saridakis (2024, arXiv:2407.09831) compute this for a generic matter bounce with a short transition.

### Is it genuinely independent from f_NL?
**YES.** PBH formation probes small scales (k ~ 10^5-10^15 Mpc^-1), while f_NL probes large scales (k ~ 0.001-0.1 Mpc^-1). Different k-ranges, different observables (DM fraction and GW spectrum vs. galaxy bispectrum), different detectors (LISA/ET vs. MegaMapper).

### Is it realistic for the Wilson-Ewing LQC bounce?
**CONDITIONALLY.** The critical question is whether the LQC bounce transition is sharp enough to produce the required small-scale enhancement. The Papanikolaou et al. mechanism relies on a short, abrupt transition (parametrized by a transition duration Delta_eta). The LQC effective bounce is smooth and symmetric, with a characteristic timescale set by rho_c.

Possible outcomes:
- If the LQC transition is sharp enough: asteroid-mass PBHs + induced GW background. Detectable by LISA (f ~ 10^-3 Hz) or ET (f ~ 1-100 Hz) depending on the PBH mass.
- If the LQC transition is too smooth: negligible enhancement, no PBHs. Channel closes.
- If the transition is intermediate: model-dependent enhancement that is exponentially sensitive to bounce parameters. Not a sharp prediction.

### Is it detectable?
**IF** the enhancement is O(10^6) above the large-scale power spectrum (required for PBH formation), the induced GW background has Omega_GW ~ 10^-8 in the LISA band. This is above the LISA sensitivity for a 4-year mission. ET would provide complementary constraints in the Hz band.

However, the 2026 dust-radiation PBH calculation (cited in our bounce evidence audit) shows vanishing PBH fractions for smooth bounces. This is a warning sign.

### Worth pursuing?
**YES, with bounded investment.** Compute the scalar power spectrum through the LQC bounce at small scales. If the enhancement is negligible (as the 2026 result suggests), document the null result and close the channel. If enhancement exists, compute the PBH mass function and induced GW spectrum. Total effort: 2-4 weeks.

### Verdict: BEST SECOND CHANNEL CANDIDATE. Independent, potentially detectable, calculable.

---

## Channel B: Induced Gravitational Waves (Second-Order Tensor)

### Mechanism
Enhanced scalar perturbations at small scales (from Channel A) source second-order tensor perturbations through the nonlinear coupling (Espinosa, Konstandin, No & Servant 2018). This produces a stochastic gravitational wave background whose spectrum encodes the shape of the scalar enhancement.

### Is it genuinely independent from f_NL?
**PARTIALLY.** It is coupled to Channel A (same scalar enhancement drives both PBH formation and induced GWs). If Channel A closes (no enhancement), Channel B closes too. However, the GW spectrum provides additional information beyond the PBH mass function: it is sensitive to the SHAPE of the scalar enhancement, not just its amplitude.

### Is it realistic?
Same conditions as Channel A. If the LQC bounce produces scalar enhancement at small scales, the induced GW background follows automatically. The computation is standard (second-order cosmological perturbation theory, well-developed tools exist).

### Is it detectable?
If Omega_GW ~ 10^-8 at LISA frequencies (f ~ 10^-3 Hz), it is detectable. The spectral shape (peaked or broad) carries information about the bounce dynamics.

### Worth pursuing?
**YES, as part of Channel A.** The induced GW computation is a natural extension of the PBH calculation. The additional effort is small once the scalar power spectrum at small scales is known.

### Verdict: PACKAGE WITH CHANNEL A. Not independent, but provides complementary information.

---

## Channel C: Inflationary Consistency Relation Violation

### Mechanism
Inflation predicts the consistency relation r = -8 n_T (to leading order in slow roll), where n_T is the tensor spectral tilt. The matter bounce predicts n_T > 0 (blue tensor spectrum), violating this relation. Detection of n_T > 0 with r > 0 would be strong evidence against slow-roll inflation and for a bouncing cosmology.

### Is it genuinely independent from f_NL?
**YES.** This is a pure tensor-sector observable, completely independent of the scalar bispectrum.

### Is it realistic?
**NO.** This channel is dead for practical purposes. The LQC dressed-metric formalism gives r ~ 10^-4 for the Wilson-Ewing model. At this level:
- r is below the threshold of LiteBIRD (sigma_r ~ 0.001), CMB-S4 (sigma_r ~ 0.003), and all other planned experiments.
- n_T is unmeasurable if r is undetectable (you need to detect the tensor spectrum before you can measure its tilt).
- Even the generic matter-bounce prediction (r ~ 1 without LQC suppression) gives n_T at a level that is only marginally measurable. With r ~ 10^-4, it is hopeless.

### Worth pursuing?
**NO.** The channel is closed by the same LQC corrections that make the model viable (r < 0.036 requires the dressed-metric suppression, which pushes r below all detection thresholds).

### Verdict: DEAD. r too small to detect, n_T unmeasurable. Do not invest.

---

## Channel D: Low-ell Structure / Anomaly Modulation (Agullo et al.)

### Mechanism
LQC corrections to the initial quantum state modify the perturbation spectrum at the largest observable scales (ell < 30). This can produce:
- Power suppression at low ell (explaining the Planck quadrupole deficit)
- Parity asymmetry (explaining the odd-ell / even-ell power ratio anomaly)
- Hemispherical asymmetry (from the preferred direction set by the LQC initial state)

Key references: Agullo, Ashtekar & Nelson (2013, 2021), Agullo, Kranas & Sreenath (2021).

### Is it genuinely independent from f_NL?
**PARTIALLY.** Same LQC framework, same quantum-corrected initial state, but different observables (CMB power spectrum and bispectrum at ell < 30, not galaxy bispectrum at high k). There is a logical connection: if LQC modifies the initial state enough to affect the power spectrum at low ell, it should also affect the bispectrum at low ell.

### Is it realistic?
**MARGINALLY.** The CMB anomalies are individually 2-3 sigma:
- Low quadrupole: 2.5-3 sigma (depending on estimator)
- Parity asymmetry: 2-3 sigma
- Hemispherical asymmetry: ~3 sigma (but with look-elsewhere effect)

Durrer et al. (2023) challenged the LQC bispectrum prediction specifically. The fits are qualitative (no Bayesian model comparison with LCDM). The anomalies may be statistical flukes.

### Is it detectable?
**Already detected, but attribution is ambiguous.** The anomalies are in the existing Planck data. The question is whether they are better explained by LQC than by LCDM + statistical fluctuation. No new data at low ell is expected (cosmic variance limited).

### Worth pursuing?
**LOW PRIORITY.** Even if we compute the LQC prediction for the Wilson-Ewing model and show it fits the anomalies, the evidence will remain ambiguous (2-3 sigma individual anomalies, no prospect of improvement). This cannot serve as a decisive second test.

The one exception: if the LQC formalism comparison (Opening 1 in file 02) produces a working code for low-ell predictions, computing this as a LOW-MARGINAL-COST extension is worthwhile. But do not build infrastructure specifically for this channel.

### Verdict: WEAK. Evidence is ambiguous, no prospect of decisive data, Durrer challenge unresolved.

---

## Channel E: Scale-Dependent Non-Gaussianity f_NL(k)

### Mechanism
LQC corrections modify mode evolution near the bounce scale k_LQC. If observable modes probe the transition region, f_NL becomes scale-dependent: f_NL(k) rather than constant. This would show up as:
- Different f_NL at different redshift bins in galaxy surveys
- Scale-dependent bias in multi-tracer analyses
- Distinguishable from inflation (which predicts nearly constant f_NL)

### Is it genuinely independent from f_NL?
**PARTIALLY.** It is an extension of the f_NL story, not an independent observable. However, scale dependence is QUALITATIVELY different from a constant f_NL. Inflation does not produce scale-dependent local f_NL (at leading order), so detecting df_NL/d(ln k) != 0 would be a strong LQC-specific signal.

### Is it realistic?
**PROBABLY NOT at observable scales.** The LQC corrections to mode evolution are concentrated near k_LQC, which is set by the bounce energy density. For rho_c ~ 0.41 M_Pl^4 and the number of e-folds between the bounce and reheating, k_LQC is typically far above observable wavenumbers (k_obs ~ 0.001-0.1 Mpc^-1). The observable modes were superhorizon during the entire quantum epoch, so they experience the bounce as an instantaneous event.

For scale dependence to be observable, one of these must be true:
1. k_LQC is within a few orders of magnitude of k_obs (requires fine-tuned contraction duration)
2. The LQC corrections propagate to modes far below k_LQC through mode coupling (non-standard, no known mechanism)
3. The pre-bounce contraction phase itself introduces scale dependence that is distinct from the constant -35/8 (possible but not LQC-specific)

### Is it detectable?
**IF** f_NL(k) varies by O(1) over the range k = 0.01-0.1 Mpc^-1, multi-tracer galaxy surveys (MegaMapper with multiple tracers) could detect the running at ~3 sigma. If the variation is <10%, it is undetectable.

### Worth pursuing?
**YES, as natural extension of Path 1 infrastructure.** When computing f_NL in the dressed-metric formalism (Opening 1), compute it at multiple k values to check for scale dependence. This adds minimal effort to the already-planned calculation. If f_NL(k) is constant (expected), document it. If not, pursue aggressively.

### Verdict: WORTH CHECKING (low marginal cost), but PROBABLY NULL for observable modes.

---

## Channel F: Running of Scalar Spectral Index (alpha_s)

### Mechanism
The matter bounce with w = -0.003 predicts n_s = 0.964 and a specific running alpha_s = dn_s/d(ln k). For single-field matter contraction, the running is related to w by alpha_s ~ O(epsilon^2) ~ O(10^-5), which is too small to detect. However, LQC corrections could modify this.

### Is it genuinely independent from f_NL?
**YES.** alpha_s is a second-order power spectrum property, f_NL is a bispectrum property.

### Is it realistic?
**NO in practice.** Planck bounds on alpha_s are sigma(alpha_s) ~ 0.007. CMB-S4 will reach sigma(alpha_s) ~ 0.003. The predicted alpha_s ~ 10^-5 is 2-3 orders of magnitude below detection threshold. LQC corrections could enhance it, but there is no known mechanism to boost it by 2-3 orders of magnitude while keeping n_s fixed.

### Worth pursuing?
**NO.** Undetectable by any planned experiment.

### Verdict: DEAD. Predicted value is orders of magnitude below detection threshold.

---

## Summary Table

| Channel | Independent? | Detectable? | LQC-specific? | Worth Pursuing? | Priority |
|---------|-------------|-------------|--------------|----------------|----------|
| A: PBH from bounce | YES | CONDITIONALLY | YES (transition shape) | YES | #1 |
| B: Induced GW | PARTIALLY (coupled to A) | CONDITIONALLY | YES (coupled to A) | YES (part of A) | Package with A |
| C: Consistency relation | YES | NO (r ~ 10^-4) | YES | NO | DEAD |
| D: Low-ell anomalies | PARTIALLY | Already detected, ambiguous | YES | LOW PRIORITY | #4 |
| E: Scale-dep f_NL(k) | PARTIALLY | PROBABLY NOT | YES | CHECK (low cost) | #2 |
| F: Running alpha_s | YES | NO (too small) | POSSIBLE | NO | DEAD |

---

## Recommended Second Channel: PBH + Induced GW (Channels A+B)

### Why this is the best option

1. **Genuinely independent:** Different k-range (small-scale), different observables (DM fraction, GW spectrum), different detectors (LISA, ET, PTA).
2. **LQC-specific:** The PBH yield depends on the LQC bounce dynamics (transition sharpness, effective equation of state during bounce). This is not a generic matter-bounce prediction.
3. **Calculable:** Standard tools exist for PBH formation and induced GW computation. The new input is the LQC bounce transfer function at small scales.
4. **Testable on a concrete timeline:** LISA (launch ~2035), Einstein Telescope (first light ~2035), ongoing PTA campaigns.
5. **Complementary to f_NL:** If both f_NL and an induced GW signal are detected, the model passes two independent tests. If f_NL fails but the GW signal is detected, the bounce mechanism still has evidence. If neither is detected, the model is cleanly excluded.

### The honest risk
The most likely outcome (50-70%) is that the LQC bounce is too smooth to produce significant PBH enhancement, and this channel closes. The 2026 dust-radiation calculation already points in this direction. But the calculation is worth doing because:
- It is bounded (clear answer within weeks)
- It fills a genuine literature gap (LQC PBH production has not been computed for the Wilson-Ewing model)
- A null result is still informative (constrains the bounce transition dynamics)

---

## Recommended Extension of Primary Channel: f_NL(k) Scale Dependence (Channel E)

### Why this is the best extension

1. **Low marginal cost:** Once the LQC perturbation code is built for the formalism comparison (file 02, Opening 1), computing f_NL at multiple k values is trivial.
2. **LQC-specific:** Generic matter bounce gives constant f_NL. Any scale dependence is a quantum-gravity signature.
3. **Strengthens the flagship:** Even a null result (constant f_NL) strengthens the detection forecast by confirming the prediction is k-independent.
4. **Could produce a surprise:** If k_LQC happens to be near observable scales (unlikely but possible), the signal would be dramatic.

---

## Dead Channels

| Channel | Why Dead |
|---------|----------|
| Consistency relation (r, n_T) | r ~ 10^-4 is 10x below any planned detector. LQC suppression that makes the model viable also kills the tensor observables. |
| Running alpha_s | Predicted value ~10^-5, detection threshold ~10^-3. Two orders of magnitude gap. |
| Galaxy spin coupling | 9-12 OOM gap, previously assessed and effectively falsified. |
| Chiral GW | GHz frequency, permanently inaccessible. |
| GW echoes | Killed by frequency gate for Planck-scale bounce. |

---

## Architecture After Second Channel

If PBH + induced GW channel opens:

```
Wilson-Ewing LQC Matter Bounce
    |
    +--- Large scales (k ~ 0.001-0.1 Mpc^-1)
    |       |
    |       +--- f_NL = -4.375 (MegaMapper ~2032-2035)
    |       +--- n_s = 0.964 (fitted, not a test)
    |       +--- f_NL(k) scale dependence (check, probably null)
    |
    +--- Small scales (k ~ 10^5-10^15 Mpc^-1)
    |       |
    |       +--- PBH mass function (constrainable by microlensing)
    |       +--- Induced GW spectrum (LISA ~2035, ET ~2035)
    |
    +--- Birefringence (bounce-independent but ECH-linked)
            |
            +--- beta = 0.24 deg (already detected at 3.9 sigma)
```

This is a two-test architecture with a bonus bounce-independent signal. Losing any single test does not kill the program.
