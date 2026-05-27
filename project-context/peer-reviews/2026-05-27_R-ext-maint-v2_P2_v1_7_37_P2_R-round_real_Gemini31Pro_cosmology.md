# P2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P2_v1_7_37
**Wall time**: 98.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=33202, completion=9049, reasoning=7801, total=42251

---

Here is the adversarial peer review of the manuscript, focusing on theoretical physics, model-class boundaries, and statistical consistency.

## PAPER-GEM-B1: Hallucinated ALP Birefringence "Prediction" (BLOCKER)
**Location:** Section 9.5, "with the prediction $\beta\approx 0.27^\circ$ depending on the ALP coupling..."
**Issue:** There is no generic, first-principles "bounce prediction" of $\beta \approx 0.27^\circ$ for cosmic birefringence. The value $\sim 0.27^\circ$--$0.34^\circ$ is an observational fit (from Minami & Komatsu, ACT, etc.) that a bounce-accommodated spectator ALP can be tuned to match. Framing an explicitly parameter-dependent accommodation ($g_{\phi\gamma}$, $m_a$) as a theoretical "prediction" to claim complementary evidence is a post-dictive hallucination that compromises theoretical integrity.
**Fix:** Remove the word "prediction". State strictly that bounce models can accommodate spectator ALPs that fit the observed $\beta \approx 0.3^\circ$, without claiming the specific angle derives from bounce physics.

## PAPER-GEM-M1: Fisher Matrix Fiducial Shift Contradiction (MAJOR)
**Location:** Section 4, "relies on the leading-order linearization that the Fisher matrix is approximately invariant under fiducial shifts of order the parameter uncertainty"
**Issue:** The shift from the Heinrich et al. fiducial $\fnl=0$ to the bounce target $\fnl=-4.375$ is $>6\sigma$, which is categorically *not* "of order the parameter uncertainty" ($\sigma=0.7$). At large $|\fnl|$, the non-Gaussian signal itself contributes to the estimator covariance matrix (the $B^2$ and $T$ terms), which strictly increases the variance and degrades $\sigma(\fnl)$. Assuming Fisher invariance across a $6\sigma$ shift ignores this signal-induced variance.
**Fix:** Delete the false claim that the shift is "of order the parameter uncertainty." Explicitly acknowledge that the $B^2$ covariance term at $\fnl=-4.375$ will degrade the effective $\sigma(\fnl)$ relative to the $\fnl=0$ baseline, flagging it as an unmodeled optimistic bias in the $5.2\sigma$ headline.

## PAPER-GEM-M2: "Gauge-Frame" Observable Confusion (MAJOR)
**Location:** Abstract and Section 1, "The forecast survey estimators (SPHEREx, MegaMapper) measure the conventional Planck/local-template $\fnl$ in the gauge frame, not the CFC physical-frame quantity directly"
**Issue:** Surveys do not measure quantities in a "gauge frame"; they measure physical observables (photon counts, angles, redshifts) on the past lightcone. The local template is a theoretical construct in comoving gauge, which must be forward-modeled via GR projection effects to the observer frame. Claiming the survey "measures in the gauge frame" fundamentally misunderstands cosmological perturbation theory.
**Fix:** Correct the phrasing to state that survey estimators are *calibrated* to the comoving-gauge local template, but actual measurements are on the past lightcone, requiring the GR projection corrections discussed later in the paper.

## PAPER-GEM-m1: Suyama-Yamaguchi Saturation Condition (minor)
**Location:** Section 9.4, "saturates this inequality only when $\zeta$ is a local quadratic functional of a single Gaussian field"
**Issue:** The Suyama-Yamaguchi inequality $\tau_{\rm NL} \geq (6\fnl/5)^2$ is saturated at tree level for *any* single-source model, not just strictly quadratic local functionals. A single field with higher-order local terms (e.g., $\zeta = \zeta_g + f \zeta_g^2 + g \zeta_g^3$) also saturates it.
**Fix:** Change "only when $\zeta$ is a local quadratic functional of a single Gaussian field" to "for single-source models."

## PAPER-GEM-m2: 2-Parameter Fisher Ratio Applied to Multi-Parameter Space (minor)
**Location:** Section 9.4, "the marginal/unmarginal ratio $\sigma_{\rm marg}/\sigma_{\rm unmarg} = 1/\sqrt{1-\rho^2} \approx 3.86$ ... implied $\sigma_{\rm unmarg}(\fnl) = \sigma_{\rm marg}/3.86 \approx 0.114$"
**Issue:** The identity $\sigma_{\rm marg} = \sigma_{\rm unmarg} / \sqrt{1-\rho^2}$ is exact only for a $2 \times 2$ Fisher matrix. In a multi-parameter SDB forecast where nuisance parameters (like $b_\phi$, $b_1$) are also marginalized, this ratio yields the variance *conditional on fixing $n_{\fnl}$ only*, not the fully unmarginalized raw Fisher element $1/\sqrt{F_{11}}$. Calling it "unmarginal" is statistically misleading.
**Fix:** Change "unmarginal" to "conditional on fixing $n_{\fnl}$" to accurately reflect the partial unmarginalization.

## PAPER-GEM-n1: "Gauge-Frame" Terminology (nit)
**Location:** Abstract and Section 1, "gauge-frame slow-roll value"
**Issue:** "Gauge-frame" is colloquial and non-standard. The Maldacena consistency relation is computed in a specific gauge (comoving) and evaluated in global coordinates, contrasting with Conformal Fermi Coordinates (CFC).
**Fix:** Replace "gauge-frame" with "comoving-gauge" or "global-coordinate" throughout the text.
