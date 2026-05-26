# P2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v2_P2_v1_7_37
**Wall time**: 88.9s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=33230, completion=11332, reasoning=10387, total=44562

---

## PAPER-GEM-B1
**Severity:** BLOCKER
**Location:** Sec 8.4, "quasi-single-field inflation (QSFI)..."
**Issue:** The QSFI scaling limits are exactly reversed. The paper claims $\mu/H=0$ gives a super-squeezed $(k_3/k_1)^{-3/2}$ shape and $\mu/H=3/2$ reproduces the local template. In QSFI, the bispectrum scales as $(k_3/k_1)^{3/2-\nu}$ relative to the local shape, where $\nu = \sqrt{9/4 - \mu^2/H^2}$. Thus $\mu/H=0$ ($\nu=3/2$) yields $(k_3/k_1)^0=1$ (exact local template), while $\mu/H=3/2$ ($\nu=0$) yields $(k_3/k_1)^{3/2}$ (suppressed in the squeezed limit).
**Fix:** Swap the limits: state that $\mu/H \to 0$ reproduces the local template and $\mu/H \to 3/2$ produces the squeezed-suppressed shape.

## PAPER-GEM-B2
**Severity:** BLOCKER
**Location:** Appendix A, "Planck/Komatsu-Spergel convention ... c = 2"
**Issue:** The paper claims the Planck/Komatsu-Spergel convention for the curvature perturbation $\zeta$ uses $c=2$ in $B_\zeta = c f_{\rm NL} [P_\zeta P_\zeta + \dots]$. This is factually incorrect; the standard CMB convention for $\zeta$ is $c = 6/5 = 1.2$, derived directly from $\zeta = \zeta_g + \frac{3}{5} f_{\rm NL} \zeta_g^2$. The value $c=2$ applies to the Bardeen potential $\Phi$, not $\zeta$. 
**Fix:** Correct the Komatsu-Spergel $c$ value to $6/5$ and re-evaluate whether the Cai vs Li-Brandenberger discrepancy can actually be explained by this convention difference.

## PAPER-GEM-B3
**Severity:** BLOCKER
**Location:** Sec 8.4, "The 6-bin Fisher inputs are not yet on disk in this release"
**Issue:** The paper quotes a highly specific, unmarginalized $\sigma(f_{\rm NL}) \approx 0.114$ and a $9.9\sigma$ detection significance from a joint SDB Fisher forecast, while explicitly admitting the Fisher inputs are "deferred to a companion artifact" and "not yet on disk". Publishing phantom results based on unavailable data violates basic scientific reproducibility.
**Fix:** Remove the $9.9\sigma$ and $\sigma(f_{\rm NL}) \approx 0.114$ claims entirely until the Fisher inputs are actually published or included in the repository.

## PAPER-GEM-M1
**Severity:** MAJOR
**Location:** Sec 9.5, "with the prediction $\beta \approx 0.27^\circ$ depending on the ALP coupling..."
**Issue:** The paper frames the specific measured cosmic birefringence angle $\beta \approx 0.27^\circ$ as a "prediction" of bounce-motivated ALP models. A bounce model may motivate the existence of an ALP, but the specific angle depends on continuous free parameters (coupling $g_{\phi\gamma}$ and initial misalignment) and cannot be predicted a priori to match the Minami-Komatsu value.
**Fix:** Change "prediction $\beta \approx 0.27^\circ$" to "accommodation of the observed $\beta \approx 0.27^\circ$" and remove claims that the bounce predicts this specific angle.

## PAPER-GEM-m1
**Severity:** minor
**Location:** Sec 6.3, "chosen to drive the Monte Carlo estimate of the Bayes factor below the analytic shot noise"
**Issue:** The phrase "analytic shot noise" is an oxymoron. Analytic closed-form integrals do not have shot noise. The Monte Carlo ensemble over survey realizations reduces the sample variance of the expected Bayes factor distribution, it does not reduce noise in the analytic formula itself.
**Fix:** Change "below the analytic shot noise" to "to ensure convergence of the expected Bayes factor distribution".
