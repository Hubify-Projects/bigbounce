# paper1a R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P1A_v1A_0_34
**Wall time**: 143.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=29925, completion=15996, reasoning=15358, total=45921

---

## PAPER-GEM-M1
**Severity:** MAJOR
**Location:** Sec. IV.B (Route 2), Eq. 14 and surrounding text
**Issue:** The dimensional reconciliation for the Route 2 ratio is still broken. The text's primary ratio formula spuriously divides by $M_{\rm Pl}(\alpha/M)$, artificially inflating the suppression by a factor of 100 while muddying the dimensions. Worse, the "complementary cross-check" explicitly uses the expression $\alpha_{\rm em}/(4\pi\cdot M_{\rm Pl}\cdot(\alpha/M)\cdot\beta_{\rm obs})\cdot H_0$ and calls it a "dimensionless ordering", despite it having mass dimension +1 (units of $H_0$). 
**Fix:** Remove the dimensionful "complementary cross-check" sentence entirely. Correct the primary ratio to simply compare the induced angle to the observed angle: $\Delta\theta_{\rm one-loop}/\beta_{\rm obs} \sim \frac{\alpha_{\rm em}}{4\pi} \frac{H_0/M_{\rm Pl}}{\beta_{\rm obs}} \sim 10^{-61} / 10^{-3} \sim 10^{-58}$, removing the physically unjustified $M_{\rm Pl}(\alpha/M)$ denominator.

## PAPER-GEM-m1
**Severity:** minor
**Location:** Sec. XIII (Surviving Mechanism-Independent Tests), Structural incompatibility paragraph
**Issue:** There is a definition mismatch regarding $N_{\rm exit}$. The text calculates the scale shift as $e^{N_{\rm tot}-N_{\rm exit}} \sim e^{32}$ using $N_{\rm tot} \sim 92$ and $N_{\rm exit} \sim 60$, but explicitly defines $N_{\rm exit}$ as "the relative e-fold differential between bounce and CMB horizon-exit". If 60 is the differential from bounce to exit, the shift would be $e^{60}$. The value 60 actually represents the e-folds from horizon-exit to the *end* of inflation.
**Fix:** Redefine $N_{\rm exit} \sim 60$ as the e-folds from horizon-exit to the *end of inflation*, so that the differential from bounce to exit is correctly described as $N_{\rm tot} - N_{\rm exit} \sim 32$.

## PAPER-GEM-m2
**Severity:** minor
**Location:** Sec. IV.D (Route 4), L407-410
**Issue:** The text states the Chern-Simons 4-current divergence is $\partial_\mu K^\mu = \frac{1}{2} \tilde{F}_{\mu\nu} F^{\mu\nu}$. Under the standard definitions $\tilde{F}^{\mu\nu} = \frac{1}{2}\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma
