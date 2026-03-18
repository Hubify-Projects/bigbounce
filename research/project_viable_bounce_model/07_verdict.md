# 07: Verdict and Next Direction

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Question: Does a viable minimal bounce model exist?

## Answer: CONDITIONALLY YES.

---

## The Viable Model

**Two-Phase LQC Matter Bounce + Partial Curvaton**

| Component | Role | Parameters |
|-----------|------|-----------|
| Ekpyrotic pre-phase (w >> 1) | BKL resolution | ~10 e-folds |
| Matter contraction (w ≈ 0) | Scale-invariant base spectrum, f_NL | ~60 e-folds |
| LQC bounce | Singularity resolution + tensor suppression | ρ_c from γ |
| Partial curvaton (α ≈ 0.3) | Red spectral tilt | m_σ/H_k ≈ 0.76 |

**Total free parameters:** 3 beyond the bounce (m_σ, α, N_ek)
**Inflation comparison:** Starobinsky R² has 1 free parameter

---

## Predictions

| Observable | Prediction | Current data | Future test |
|-----------|-----------|-------------|------------|
| n_s | 0.965 | 0.9649 ± 0.0042 | CMB-S4: consistent |
| r | ~10⁻⁴ | < 0.036 | LiteBIRD: consistent (no detection) |
| **f_NL^local** | **−3.7** | −0.9 ± 5.1 | **MegaMapper: 7.4σ detection** |
| f_NL^equil | ~0 | −26 ± 47 | CMB-S4: consistent |
| α_s | ~−0.001 | −0.005 ± 0.007 | CMB-S4: consistent |
| n_T | >0 (blue) | Unmeasurable at r ~ 10⁻⁴ | No test |

**The single testable discriminator: f_NL^local ≈ −3.7**

---

## Critical Dependencies

### 1. LQC Perturbation Corrections (ESSENTIAL)

The model REQUIRES LQC-type quantum-geometry corrections to suppress tensor modes. Without these corrections, r ~ O(10) and the model fails.

**This means ECH is insufficient.** The ECH bounce provides the same background as LQC but has no perturbation corrections (Branch Vb result). The viable model lives in LQC territory.

**Implication for our program:** We need to shift from ECH-specific to LQC-compatible analysis. The background is the same; the perturbation treatment must use the dressed-metric approach.

### 2. Curvaton Dynamics During Contraction (NEEDS VERIFICATION)

The tilt formula n_s − 1 = −α² × 2m²/(3H²) is approximate. The exact curvaton dynamics during contraction need careful calculation:
- Does the curvaton perturbation grow or stay constant on superhorizon scales?
- Is the tilt formula sign correct (red, not blue)?
- What is the exact relationship between m_σ, α, and n_s?

**This is the highest-priority calculation to do next.**

### 3. Two-Phase Contraction Implementation (NEEDS MODEL)

The ekpyrotic-to-matter transition requires a specific scalar potential:
- Steep potential V(φ) for the ekpyrotic phase
- Flat potential for the matter phase
- A smooth transition between them

**This is model-dependent but well-studied in the literature** (e.g., Lehners & Steinhardt 2008, Cai et al. 2012).

### 4. Combined f_NL Calculation (NEEDS VERIFICATION)

The f_NL estimate (−3.7 for α = 0.3) uses approximate scaling:
$$
f_{\rm NL}^{\rm total} \approx f_{\rm NL}^{\rm matter} \times (1 - \alpha^2)^2 + f_{\rm NL}^{\rm curvaton} \times \alpha^4
$$

This may have additional cross-terms from the nonlinear transfer between matter and curvaton perturbations. A proper δN formalism calculation is needed.

### 5. The Sign of the Curvaton Tilt (CRITICAL UNKNOWN)

I derived n_σ − 1 ≈ −2m²/(3H²) for a curvaton during matter contraction, giving a red tilt. **This needs verification.** If the sign is wrong (blue tilt), the entire model fails.

The sign depends on:
- Which mode (growing or decaying) dominates
- The matching conditions at the bounce
- The curvaton's equation of motion in the contracting background

**If the curvaton tilt is blue in contraction, we need a different tilt mechanism.**

---

## What the Model Does Well

1. **Resolves the singularity** (bounce replaces Big Bang)
2. **Avoids trans-Planckian problem** (modes start large, contract)
3. **Resolves BKL** (ekpyrotic pre-phase)
4. **Satisfies all current observational constraints** (n_s, r, f_NL, α_s)
5. **Makes a sharp, testable prediction** (f_NL ≈ −3.7, detectable at 7.4σ by MegaMapper)
6. **The f_NL prediction is NEGATIVE** — distinctive from inflation, which typically predicts f_NL ≥ 0
7. **Comparable parameter count to inflation** (3 vs 1-2)

## What the Model Does Poorly

1. **More parameters than Starobinsky** (3 vs 1)
2. **The r prediction is untestable** (too small for LiteBIRD)
3. **Requires LQC perturbation corrections** — not ECH-compatible
4. **The n_s prediction is tuned** (unlike Starobinsky where it's predicted from N)
5. **Several unverified calculations** (curvaton tilt sign, combined f_NL, exact r)

---

## Is This Model New?

**Partially.**

- LQC matter bounce: Wilson-Ewing (2013) — known
- Curvaton in matter bounce: Cai & Brandenberger (2011) — known
- Two-phase contraction: Lehners & Steinhardt (2008), Cai et al. (2012) — known
- LQC tensor suppression: known

**What may be new:**
- The COMBINATION: LQC bounce + partial curvaton (α ≈ 0.3) + two-phase contraction
- The specific joint-constraint analysis showing a viable parameter window
- The prediction f_NL ≈ −3.7 (not −35/8 and not −1.25, but an intermediate value)
- The identification that α ≈ 0.3 is the sweet spot preserving most of the matter-bounce non-Gaussianity

**This needs a literature check.** Has anyone combined LQC + partial curvaton and computed the joint predictions?

---

## The Single Most Important Calculation to Do Next

**VERIFY THE CURVATON TILT SIGN IN MATTER CONTRACTION.**

Specifically:

1. Write the curvaton perturbation equation during matter contraction:
$$
\ddot{\delta\sigma} + 3H\dot{\delta\sigma} + \left(\frac{k^2}{a^2} + m_\sigma^2\right)\delta\sigma = 0
$$

2. During matter contraction: a(t) ∝ (−t)^{2/3}, H = 2/(3t) < 0

3. Solve for the superhorizon modes (k/a << |H|):
$$
\ddot{\delta\sigma} + \frac{2}{t}\dot{\delta\sigma} + m_\sigma^2 \delta\sigma = 0
$$

4. Find the two independent solutions and determine the spectral index:
$$
\delta\sigma \propto (-t)^{\lambda_\pm}
$$
where λ_± are roots of the indicial equation.

5. The spectral index of the GROWING mode (the one that dominates as t → 0⁻):
$$
n_\sigma - 1 = f(\lambda_+, w)
$$

**If n_σ < 1 (red tilt): the model works.**
**If n_σ > 1 (blue tilt): the curvaton mechanism fails for this application, and we need a different tilt source.**

---

## Quick Calculation: Curvaton Mode in Matter Contraction

During matter contraction: a(t) = a_0 (-t/t_0)^{2/3} for t < 0.

H = ȧ/a = 2/(3t) (negative for t < 0 ✓)

The curvaton perturbation equation for superhorizon modes:
$$
\ddot{\delta\sigma} + 3H\dot{\delta\sigma} + m^2\delta\sigma = 0
$$

$$
\ddot{\delta\sigma} + \frac{2}{t}\dot{\delta\sigma} + m^2\delta\sigma = 0
$$

Try δσ = (−t)^λ:
$$
\lambda(\lambda - 1)(-t)^{\lambda-2} + \frac{2}{t}\lambda(-t)^{\lambda-1} + m^2(-t)^\lambda = 0
$$

$$
\lambda(\lambda-1)(-t)^{-2} + 2\lambda(-t)^{-2}(-1) + m^2 = 0
$$

Wait, let me be more careful. For t < 0, let τ = −t > 0.

δσ = τ^λ

$$
\frac{d^2(\tau^\lambda)}{dt^2} = \lambda(\lambda-1)\tau^{\lambda-2}
$$

$$
3H = 3 \times \frac{2}{3t} = \frac{2}{t} = -\frac{2}{\tau}
$$

$$
\frac{d(\tau^\lambda)}{dt} = -\lambda\tau^{\lambda-1}
$$

So:
$$
\lambda(\lambda-1)\tau^{\lambda-2} - \frac{2}{\tau}(-\lambda\tau^{\lambda-1}) + m^2\tau^\lambda = 0
$$

$$
\lambda(\lambda-1)\tau^{\lambda-2} + 2\lambda\tau^{\lambda-2} + m^2\tau^\lambda = 0
$$

$$
[\lambda(\lambda-1) + 2\lambda]\tau^{-2} + m^2 = 0
$$

$$
\lambda^2 + \lambda + m^2\tau^2 = 0
$$

This is NOT a simple power law because of the m²τ² term. The m² term introduces a τ-dependent potential.

For the superhorizon regime (which corresponds to early times, τ → ∞ in contraction, or equivalently k²/a² << |m²|... wait, no. Superhorizon means k/a << |H|, which means τ >> 1/k_phys.

Actually, for τ → ∞ (early in contraction, far from the bounce):
- |H| = 2/(3τ) → 0
- m² is constant
- The dominant balance is: m²δσ ≈ 0 for generic m² ≠ 0... no, the oscillatory term matters.

For large τ, the curvaton oscillates: δσ ~ cos(mτ)/τ^{1/2} (WKB approximation for massive field in expanding/contracting FRW).

As τ → 0 (approaching the bounce), |H| → ∞ and the Hubble friction dominates. The curvaton freezes.

**The mode that becomes frozen near the bounce has properties determined by the matching between the oscillating and frozen regimes.** The spectral tilt depends on when each k-mode transitions from oscillating to frozen.

For mode k: the mode freezes when m ~ |H(τ_freeze)|, giving:
$$
m \sim \frac{2}{3\tau_{\rm freeze}} \implies \tau_{\rm freeze} \sim \frac{2}{3m}
$$

The frozen amplitude depends on the oscillation amplitude at τ_freeze, which depends on k:
$$
\delta\sigma_k(\tau_{\rm freeze}) \propto k^{3/2 - \nu}
$$

where ν depends on the effective mass and the background.

For a massive field in matter contraction:
$$
\nu = \frac{3}{2}\sqrt{1 - \frac{4m^2}{9H_k^2}}
$$

Wait — this should be the standard result for de Sitter (constant H). For time-varying H (matter contraction), the effective ν changes.

For the power-law case a ∝ τ^{2/3} (matter contraction):

The exact solution for a massive scalar in this background involves Bessel functions. The spectral index of the growing mode is:

$$
n_\sigma = 4 - 2\nu
$$

where
$$
\nu = \frac{1}{2}\sqrt{9 - \frac{4m^2}{H_k^2} \times g(w)}
$$

For w = 0 and m²/H² << 1:
$$
\nu \approx \frac{3}{2} - \frac{m^2}{3H_k^2}
$$

$$
n_\sigma \approx 4 - 2\left(\frac{3}{2} - \frac{m^2}{3H_k^2}\right) = 4 - 3 + \frac{2m^2}{3H_k^2} = 1 + \frac{2m^2}{3H_k^2}
$$

**n_σ = 1 + 2m²/(3H²) > 1 → BLUE TILT.**

**THIS IS A PROBLEM.** The curvaton spectrum in matter contraction has a BLUE tilt, not a red tilt.

### Re-checking

For an EXPANDING universe (inflation) with H = const:
$$
n_\sigma = 1 + \frac{2m^2}{3H^2} \quad \text{(blue for massive field during inflation, but...)}
$$

Wait, in inflation, a light field has:
$$
n_\sigma - 1 = -\frac{2m^2}{3H^2} \quad \text{(RED tilt)}
$$

The sign difference comes from whether the universe is expanding or contracting. Let me be more careful.

In de Sitter inflation (H > 0, constant):
The spectral index of a light scalar perturbation is:
$$
n_\sigma - 1 = 3 - 2\nu, \quad \nu = \sqrt{\frac{9}{4} - \frac{m^2}{H^2}}
$$
For m²/H² << 1: ν ≈ 3/2 − m²/(3H²), giving:
$$
n_\sigma - 1 = 3 - 2(3/2 - m^2/(3H^2)) = 2m^2/(3H^2) > 0 \quad \text{BLUE}
$$

But wait, this seems wrong for inflation too. In inflation, massive spectator fields have BLUE tilted spectra? No — the standard result is that a massive field in de Sitter has n_σ − 1 = 2m²/(3H²) which is POSITIVE (blue). The RED tilt in standard curvaton models comes from the DECAY of the curvaton happening later for different k-modes, not from the field perturbation spectrum itself.

Actually, I think I've been confusing two things. The curvaton spectrum P_δσ has a slight blue tilt. But the curvature perturbation ζ_σ produced by the curvaton at decay has a tilt that includes the background evolution:

$$
\zeta_\sigma = \frac{2r_{\rm dec}}{3}\frac{\delta\sigma}{\sigma_*}
$$

where σ_* is the curvaton field value when the mode exits the horizon. The spectral index of ζ_σ is:

$$
n_s^{\rm curv} - 1 = \frac{d\ln P_{\delta\sigma}}{d\ln k} - 2\frac{d\ln\sigma_*}{d\ln k}
$$

In inflation, σ_* is roughly constant (slow roll), so n_s ≈ n_δσ ≈ 1 + 2m²/(3H²) (blue). To get a red tilt, the curvaton needs specific interactions or a non-trivial potential.

**CONCLUSION: The standard curvaton mechanism gives a BLUE-tilted spectrum, not red.** The red tilt in inflationary curvaton models comes from corrections to the slow-roll dynamics, not from the basic curvaton formula.

### What This Means for Our Model

**The curvaton tilt is BLUE for a massive, minimally-coupled curvaton in matter contraction.** This goes the WRONG direction — it makes n_s > 1, worsening the n_s = 1 problem instead of fixing it.

**This is a serious problem for the model.** The curvaton cannot provide the required red tilt through its mass alone.

### Possible Fixes

1. **Non-minimal coupling (ξRσ²):** If ξ < 0, the effective mass m²_eff = m² + ξR can be negative (tachyonic) during contraction. During matter contraction, R < 0, so ξR > 0 for ξ < 0. This gives m²_eff > m² — BLUE tilt gets worse. For ξ > 0: m²_eff < m², potentially allowing red tilt if |ξR| > m². But R is time-dependent during contraction, so the tilt depends on when the mode exits.

2. **Self-interaction potential:** A curvaton with V(σ) = m²σ²/2 − λσ⁴/4 can have an effective tilt that depends on λ. This introduces another parameter.

3. **Different EOS during contraction (w < 0):** If w < 0, the tilt formula may change sign. But w < 0 during contraction means the contraction is accelerating — this is difficult to arrange.

4. **The tilt comes from elsewhere entirely:** Perhaps the curvaton is not the right tilt mechanism. Instead, consider the nearly-matter EOS (w slightly different from 0) — but we showed this gives a BLUE tilt for w > 0.

**For a RED tilt in contraction: need n_s − 1 < 0.**

From the base spectrum: n_s = 1 + 12w/(1+3w) for the adiabatic mode. Red requires w < 0.

From the curvaton: n_σ = 1 + 2m²/(3H²). Red requires m² < 0 (tachyonic — unstable).

**THERE MAY BE A FUNDAMENTAL OBSTRUCTION TO RED TILT IN MATTER CONTRACTION.**

---

## REVISED VERDICT

**The curvaton tilt sign is likely BLUE in matter contraction, not red.** This undermines the entire model:

- The base spectrum (w = 0): n_s = 1 (scale-invariant)
- Positive w: n_s > 1 (bluer)
- Massive curvaton: n_s > 1 (bluer)

To get n_s < 1 from matter contraction requires NEGATIVE effective mass (tachyonic instability) or NEGATIVE w (accelerated contraction). Both are problematic.

**This red-tilt problem may be FUNDAMENTAL to matter contraction.** It is possibly the reason that most matter bounce papers accept n_s = 1 and rely on "nearly-matter" EOS tuning.

### What This Teaches Us

The difficulty of getting n_s < 1 from matter contraction is not a problem with our specific model — it is a property of the matter bounce scenario. The spectral tilt is determined by the EOS and the mass of any spectator, and for standard matter content, both push toward BLUE tilts.

**The path forward requires either:**
1. A contracting phase with w < 0 (negative pressure domination — perhaps dark energy domination entering contraction, or a slow-roll-like phase during contraction)
2. A non-trivial transfer function at the bounce that converts a scale-invariant (or blue) input spectrum into a red output spectrum
3. Accepting that the bounce model predicts n_s = 1 and looking for ways to make this compatible with data (e.g., running that mimics a tilt over the observable range)

**Option 1 is the most promising and maps to the SLOW CONTRACTION scenario (Ijjas & Steinhardt).**

---

## The Slow Contraction Alternative

In slow contraction (Ijjas & Steinhardt 2024-2025):
- w >> 1 (ekpyrotic)
- The scalar spectrum is NOT scale-invariant; it has a RED tilt naturally
- n_s − 1 depends on the specific potential
- BKL is resolved
- But f_NL is different from −35/8

**This is a fundamentally different model** from the matter bounce. It uses ekpyrotic contraction throughout, not just as a pre-phase.

**The trade-off:**
- Matter bounce: f_NL = −35/8 (distinctive) but n_s = 1 (excluded)
- Slow contraction: n_s can be tuned to 0.965 but f_NL is model-dependent (not as distinctive)

**Is there a model that gets BOTH?** This is the key question for the next step.

---

## Updated Single Most Important Calculation

**Determine whether slow contraction / ekpyrotic models can produce f_NL ≈ −3 to −5 while matching n_s ≈ 0.965.**

If YES: we have a viable model with both a correct n_s AND a distinctive f_NL.
If NO: the red tilt and the negative f_NL cannot coexist, and the bounce model's main discriminator is weakened.

Specifically:
1. What is f_NL in the entropy mechanism for ekpyrotic contraction (Lehners, Koyama, et al.)?
2. Can the two-field ekpyrotic model be tuned to give f_NL ≈ −4?
3. What is the running α_s in these models?

**This is the next research direction.**
