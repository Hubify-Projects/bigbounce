# 04: Parametric Window Test

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Question

Is there ANY non-absurd parameter window where the chiral bounce signal lands in an observable band with detectable amplitude?

---

## Parameter Space

The relevant parameters are:

1. **Bounce energy scale** ρ_bounce^{1/4}
2. **Post-bounce expansion history** (pure radiation, matter-dominated phase, inflation)
3. **Parity coupling strength** α_CS/f_a or α_NY/M
4. **ALP dynamics** (σ̇ at the bounce, which determines the chiral coupling strength)

---

## Scan 1: Bounce energy scale (no post-bounce inflation)

From the frequency-amplitude trade-off (File 03):

| ρ^{1/4}_bounce | f_0 today | Ω_GW at peak | In detector band? | Detectable? |
|----------------|-----------|-------------|-------------------|-------------|
| M_Pl | ~10¹⁰ Hz | ~10⁻⁵ | No (GHz) | No |
| 10⁻² M_Pl | ~10⁸ Hz | ~10⁻¹³ | No (100 MHz) | No |
| 10⁻⁸ M_Pl (10¹⁰ GeV) | ~10² Hz | ~10⁻³⁷ | Yes (ET) | No (amplitude zero) |
| 10⁻¹² M_Pl (10⁶ GeV) | ~10⁻² Hz | ~10⁻⁵³ | Yes (LISA) | No (amplitude zero) |
| 10⁻¹⁸ M_Pl (1 GeV) | ~10⁻⁸ Hz | ~10⁻⁷⁷ | Yes (PTA) | No (amplitude zero) |

**Verdict: No window exists with pure radiation expansion.** The Ω_GW ∝ f⁸ scaling makes the amplitude negligible at observable frequencies.

---

## Scan 2: Post-bounce inflation

Adding N e-folds of inflation after the bounce redshifts f_0 by e^{-N} without changing the source amplitude Ω_GW (inflation amplifies the vacuum, preserving the relative GW energy density — actually inflation dilutes pre-existing GWs relative to the inflationary vacuum).

**Correction:** Post-bounce inflation DILUTES pre-existing GWs. The GW energy density from the bounce is redshifted as radiation (ρ_GW ∝ a⁻⁴) while the total energy density during inflation is constant (ρ_inf = const). So:

$$
\frac{\Omega_{\rm GW}^{\rm after\,inf}}{\Omega_{\rm GW}^{\rm before\,inf}} = e^{-4N}
$$

To bring f_0 from 10¹⁰ Hz to 10⁻³ Hz: N = 30 → dilution factor e⁻¹²⁰ ≈ 10⁻⁵².

**The signal is exponentially diluted.** Post-bounce inflation does not help — it brings the signal to the right frequency but kills its amplitude by a comparable factor.

| Scenario | N_inf | f_0 | Dilution | Ω_GW final | Detectable? |
|----------|-------|-----|----------|-----------|-------------|
| ECH + 30 e-folds | 30 | ~mHz (LISA) | 10⁻⁵² | ~10⁻⁵⁷ | No |
| ECH + 40 e-folds | 40 | ~nHz (PTA) | 10⁻⁷⁰ | ~10⁻⁷⁵ | No |
| ECH + 60 e-folds | 60 | ~10⁻¹⁶ Hz | 10⁻¹⁰⁴ | ~10⁻¹⁰⁹ | No |

**Verdict: Post-bounce inflation kills the signal.**

---

## Scan 3: Extended matter-dominated phase after bounce

If there is an extended matter-dominated phase between the bounce and radiation domination (e.g., from a massive field oscillating), the GW spectrum is modified:
- During matter domination: a ∝ t^{2/3}, GWs redshift as a⁻¹ (superhorizon) or a⁻² (subhorizon, oscillating)
- The relative GW density Ω_GW grows during matter domination (GW redshifts as radiation, total ρ redshifts as matter): Ω_GW ∝ a during matter era

This can AMPLIFY the bounce GW signal by a factor:

$$
\text{amplification} = \frac{a_{\rm end,matter}}{a_{\rm start,matter}}
$$

But simultaneously, the extra expansion redshifts the frequency:

$$
f_0 \to f_0 \times \frac{a_{\rm start}}{a_{\rm end}}
$$

So: frequency goes down by factor X, amplitude goes up by factor X. Net effect on detectability:

$$
\Omega_{\rm GW}(f_0) \propto f_0^{-1} \times (\text{original spectrum})
$$

This is MUCH better than the ∝ f⁸ scaling! But starting from Ω ~ 10⁻⁵ at 10¹⁰ Hz:

To reach LISA (f = 10⁻³ Hz): need frequency reduction by 10¹³ → amplitude increase by 10¹³ → Ω ~ 10⁻⁵ × 10¹³ = 10⁸.

**Wait — that can't be right.** Ω_GW cannot exceed 1 (and in practice must be ≪ 1 to avoid overproducing radiation). The amplification is bounded by BBN constraints: ΔN_eff < 0.4 requires Ω_GW h² < 1.12 × 10⁻⁶ integrated over all frequencies.

Let me reconsider. The enhancement factor during a matter era applies to superhorizon modes. For modes that re-enter during the matter era, the transfer function gives additional amplification:

$$
\Omega_{\rm GW}(f) \propto f^{-2} \quad \text{for modes entering during matter era}
$$

versus Ω_GW ∝ f⁰ (flat) for modes entering during radiation. This means a matter-dominated epoch between bounce and radiation creates a BLUE tilt in Ω_GW at low frequencies — which goes the wrong way for detectability.

**Actually, the standard result is:** GW modes that re-enter the horizon during matter domination have Ω_GW(f) ∝ f⁻² relative to those entering during radiation. This creates a spectral BREAK, not an amplification of low-frequency modes.

The detailed spectral shape depends on when the matter phase ends and radiation begins. But the fundamental constraint remains: BBN bounds cap the total Ω_GW, so any amplification at one frequency comes at the expense of another.

**Verdict: An extended matter phase can reshape the spectrum but cannot overcome the GHz → mHz gap by 13 orders of magnitude while respecting BBN bounds.**

---

## Scan 4: Different parity coupling model

Could a different parity coupling extend the chiral signal to lower frequencies?

The chiral coupling μ(η) has a characteristic timescale τ_μ set by the ALP dynamics. If τ_μ ≫ Δt_bounce (the coupling is active for a long time), the chiral processing extends to lower-k modes.

For μ active over time Δt_μ, the affected modes have:

$$
k > k_{\rm min} \sim \frac{a_b}{\Delta t_\mu}
$$

The present-day frequency of k_min:

$$
f_{\rm min} = \frac{k_{\rm min}}{2\pi a_0} = \frac{a_b}{2\pi a_0 \Delta t_\mu}
$$

To get f_min ~ 10⁻³ Hz (LISA):

$$
\Delta t_\mu = \frac{a_b}{2\pi a_0 \times 10^{-3}} = \frac{1.15 \times 10^{-31}}{6.28 \times 10^{-3}} = 1.8 \times 10^{-29}\,\text{s}
$$

In Planck times: Δt_μ = 1.8 × 10⁻²⁹ / 5.39 × 10⁻⁴⁴ = 3.4 × 10¹⁴ t_Pl.

**The parity coupling would need to be active for 10¹⁴ Planck times — about 10⁻²⁹ seconds.** This is vastly longer than the bounce duration (~4 t_Pl). It corresponds to the ALP rolling or oscillating for this duration.

The Hubble rate at Δt ~ 10⁻²⁹ s after the bounce:

$$
H \sim \frac{1}{2t} \sim \frac{1}{2 \times 10^{-29}} \sim 5 \times 10^{28}\,\text{s}^{-1} \sim 3 \times 10^{-15}\,M_{\rm Pl}
$$

At this point, ρ/ρ_crit ~ (H/H_max)² ~ 10⁻²⁸. The universe is well into the radiation era, torsion is negligible, and any torsion-specific parity coupling is inactive.

**For a Chern-Simons coupling (σ̇R R̃):** The coupling is proportional to the curvature R, which drops as 1/t² after the bounce. The coupling strength at Δt ~ 10¹⁴ t_Pl is suppressed by (t_Pl/Δt)² ~ 10⁻²⁸ relative to the bounce. The chirality imprinted on these lower-k modes would be:

$$
\Delta_h(k_{\rm min}) \sim \Delta_h(k_b) \times \left(\frac{k_{\rm min}}{k_b}\right)^n \times 10^{-28}
$$

This is negligible.

**Verdict: No parametric extension of the coupling duration reaches observable frequencies with appreciable chirality.**

---

## Scan 5: Resonant / parametric amplification of chirality

Could a resonance between the ALP and GW modes amplify chirality at specific lower frequencies?

Parametric resonance occurs when the ALP oscillation frequency matches 2× the GW mode frequency: ω_σ = 2k/a. For a light ALP (m_σ ≪ H_bounce), there is no rapid oscillation → no resonance.

For a heavy ALP (m_σ ~ H_bounce ~ M_Pl), resonance occurs for modes with k ~ m_σ a ~ M_Pl a_b = k_b. This is again the bounce scale — no extension to lower frequencies.

**Verdict: Resonance does not help.**

---

## Overall Assessment

| Mechanism to reach low f | Works? | Why not |
|-------------------------|--------|---------|
| Lower bounce energy | No | Amplitude drops as f⁸ |
| Post-bounce inflation | No | Exponential dilution |
| Extended matter phase | No | BBN bounds + wrong spectral direction |
| Extended coupling duration | No | Coupling dies as 1/t² after bounce |
| Resonant amplification | No | Resonance at bounce scale only |

**There is NO non-absurd parameter window.** The frequency-amplitude trade-off and the rapid decay of torsion/curvature after the bounce make it fundamentally impossible for the ECH chiral bounce signal to reach any current or planned detector band with detectable amplitude.
