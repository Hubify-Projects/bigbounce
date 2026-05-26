# P1A R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v2_P1A_v1A_0_35
**Wall time**: 105.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=29683, completion=15629, reasoning=14806, total=45312

---

No BLOCKER-grade findings identified in this round. The structural closure logic and amplitude-budget no-go hold. However, two MAJOR kinematic and dimensional errors remain from incomplete prior-round fixes.

## PAPER-GEM-M1 (MAJOR)
**Section:** Abstract, Sec I.A, Sec XIII, Sec XIV.D
**Issue:** The notation $k_{\rm SPHEREx}^{\rm phys}$ is used to represent the physical scale *at horizon exit*, but the subscript implies the physical scale *today*. The ratio $e^{N_{\rm tot}-N_{\rm exit}} = e^{32}$ correctly computes $a_{\rm exit}/a_{\rm bounce}$, but equating this to $k_{\rm bounce}^{\rm phys}/k_{\rm SPHEREx}^{\rm phys}$ is kinematically false if $k_{\rm SPHEREx}^{\rm phys}$ is evaluated today (which would require an additional $a_0/a_{\rm exit} \sim e^{60}$ factor).
**Fix:** Replace the ambiguous $k_{\rm SPHEREx}^{\rm phys}$ with $k_{\rm exit}^{\rm phys}$ (or $H_{\rm inf}$) in the physical scaling ratio, and state explicitly that $k_{\rm bounce}^{\rm phys} = k_{\rm exit}^{\rm phys} e^{N_{\rm tot}-N_{\rm exit}}$.

## PAPER-GEM-M2 (MAJOR)
**Section:** IV.B (Route 2)
**Issue:** The text claims "A complementary cross-check using $\alpha_{\rm em}/(4\pi\cdot M_{\rm Pl}\cdot(\alpha/M)\cdot\beta_{\rm obs})\cdot H_0$ as the dimensionless ordering yields a numerically distinct ratio of order $10^{-33}$". This expression has units of mass (eV) because $H_0$ is dimensionful and the denominator is dimensionless; it cannot be a "dimensionless ordering".
**Fix:** Delete the broken "complementary cross-check" sentence entirely; the primary dimensionless ratio $\Delta\theta_{\rm one\text{-}loop}/\Delta\theta_{\rm obs} \sim 10^{-60}$ derived earlier in the paragraph is correct and sufficient.

## PAPER-GEM-m1 (minor)
**Section:** IV.D (Route 4)
**Issue:** The Chern-Simons current divergence is $\partial_\mu K^\mu = \tilde{F}_{\mu\nu}F^{\mu\nu}$ (assuming standard $\tilde{F}^{\mu\nu} = \frac{1}{2}\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$), not $\frac{1}{2}\tilde{F}_{\mu\nu}F^{\mu\nu}$. Consequently, integrating the action $-\frac{1}{4}\theta \tilde{F}F$ by parts yields $+\frac{1}{4}\partial_\mu\theta K^\mu$, meaning the text's $(\alpha/M)\partial_\mu\theta K^\mu$ is missing the $1/4$ EFT matching factor.
**Fix:** Correct the divergence identity to $\partial_\mu K^\mu = \tilde{F}_{\mu\nu}F^{\mu\nu}$ and add the $1/4$ factor to the integrated-by-parts term.

## PAPER-GEM-m2 (minor)
**Section:** X.G (Table III)
**Issue:** Table III lists $\fnl = -35/8$ for "Matter bounce (any host; not ECH-specific)", which directly contradicts Section XIII's explicit restriction that this value only holds for the "scalar-only $w=0$ matter-bounce class".
**Fix:** Update the Table III row label to "Scalar-only $w=0$ matter bounce" to align with the text's scope boundary.
