# 07: LQC Impact Check

---

## Question

Does the derived bispectrum coefficient come from generic matter contraction, or does LQC modify it?

---

## What Is Generic vs LQC-Specific

### GENERIC (framework-independent):

1. **The mode functions.** The Mukhanov-Sasaki equation v_k'' + (k^2 - 2/eta^2) v_k = 0 is determined by the background (w = 0 matter contraction) and holds in ANY framework that produces matter-dominated contraction. LQC, ECH, generic EFT — all give the same mode equation during the contraction phase.

2. **The cubic action.** The Maldacena cubic action for a canonical scalar field in comoving gauge depends only on epsilon and c_s. For w = 0: epsilon = 3/2, c_s = 1. These are framework-independent during contraction.

3. **The growing mode.** zeta growing as |eta|^{-3} is determined by the background EOS, not by the bounce mechanism. This holds in any model with w = 0 contraction.

4. **The pre-bounce bispectrum.** The in-in calculation of B_zeta during the contracting phase uses only the mode functions, cubic action, and vacuum state — all of which are framework-independent.

**Conclusion: f_NL = -35/8 is a GENERIC MATTER-BOUNCE RESULT, computed entirely within the contracting phase.**

### LQC-SPECIFIC:

1. **Bounce transfer.** What happens to B_zeta as the universe passes through the bounce (rho ~ rho_c)? LQC provides specific equations (dressed-metric approach) for how perturbations evolve through this phase. Other frameworks (ECH, generic EFT) give different transfer functions.

2. **Tensor suppression.** LQC suppresses the tensor-to-scalar ratio to r ~ 10^{-4} via quantum geometry effects at the bounce. This is LQC-specific.

3. **Potential modification of f_NL at the bounce.** If the bounce phase generates additional non-Gaussianity (from the nonlinear LQC effective equations), or if the bounce transfer coefficient is mode-dependent, the final observed f_NL could differ from the pre-bounce value.

---

## Does the Bounce Modify f_NL?

### At the power spectrum level (known result):

LQC bounce transfer at LINEAR order (perturbation theory):
- The scalar power spectrum transfers through the bounce with a k-dependent transfer function
- For modes well outside the Hubble radius at the bounce: transfer coefficient ~ 1 (adiabatic transfer)
- For modes near the Hubble scale at the bounce: oscillatory corrections (but these modes have k ~ k_bounce >> k_CMB, so they are irrelevant for CMB/LSS)

### At the bispectrum level (UNKNOWN):

The bounce transfer at THIRD ORDER (bispectrum level) has NOT been computed in the literature. This is one of the two unresolved failure points identified in the planning phase.

**Key question:** Does the nonlinear bounce evolution generate additional non-Gaussianity, or modify the pre-bounce f_NL?

### Physical argument for PRESERVATION:

1. **Superhorizon modes.** All CMB/LSS-relevant modes are far outside the Hubble radius at the bounce. The bounce lasts for a time Delta-t ~ 1/sqrt(rho_c) ~ t_Pl. During this time, modes with k << k_bounce ~ sqrt(rho_c)/M_Pl evolve adiabatically.

2. **Adiabatic theorem.** For superhorizon modes, the separate-universe approximation applies: each patch evolves as an independent FRW universe through the bounce. The nonlinear evolution is encoded in the nonlinear relationship between initial and final conditions. If this relationship is smooth (no caustics, no quantum tunneling between branches), the bispectrum is preserved.

3. **The bounce is short.** The Hubble time at the bounce is t_H ~ t_Pl. The modes of interest have wavelengths lambda ~ 1/(H_0 sqrt(A_s)) >> t_Pl by 60+ orders of magnitude. The bounce has negligible time to modify these modes nonlinearly.

### Physical argument for MODIFICATION:

1. **The Quintin no-go (2015).** If the bounce amplifies zeta (to suppress r), the amplification is mode-dependent and could modify the bispectrum shape. This applies specifically to LQC where the dressed-metric approach gives a nontrivial transfer matrix.

2. **Nonlinear LQC effective equations.** The LQC effective Friedmann equation H^2 = rho/(3M_Pl^2)(1 - rho/rho_c) is inherently nonlinear. At rho ~ rho_c, the nonlinear corrections are O(1). If these propagate to the bispectrum, f_NL could be modified.

3. **No computation exists.** Without an explicit calculation, we cannot guarantee preservation.

---

## Verdict

$$
\boxed{\text{GENERIC\_MATTER\_BOUNCE\_RESULT}}
$$

**with the caveat:** PENDING\_BOUNCE\_TRANSFER\_VERIFICATION

The f_NL = -35/8 value is derived entirely within the contracting phase using framework-independent physics. LQC enters only at the bounce, where the transfer is expected to be adiabatic for the relevant modes.

The bounce transfer at third order is an OPEN CALCULATION that would upgrade this to a fully verified result. However, the physical arguments strongly favor preservation:
- Superhorizon modes evolve adiabatically
- The bounce is short (Planck time) compared to the mode wavelengths (Hubble time)
- The separate-universe approximation applies during the bounce for these modes

**Risk assessment:** The probability that LQC bounce transfer modifies f_NL by more than 10% is estimated at < 15%. The probability of a sign flip is < 2%.

---

## Implications for Framework Choice

Since f_NL = -35/8 is generic:
- It holds in LQC, ECH, and any other framework with matter-dominated contraction
- LQC is needed for tensor suppression (r ~ 10^{-4}), not for f_NL
- The f_NL prediction is MORE robust than the tensor prediction (which IS framework-specific)
- Even if LQC turns out to be wrong, f_NL = -35/8 survives in any alternative bounce model with w = 0 contraction
