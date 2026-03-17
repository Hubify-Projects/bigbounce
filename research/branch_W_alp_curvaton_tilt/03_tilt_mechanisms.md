# 03: Tilt Generation Mechanisms

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Mechanism 1: Mass-Induced Tilt (Standard Curvaton)

### How it works

A massive spectator field σ on a matter-dominated contracting background has mode equation:

$$
\delta\sigma_k'' + \left(k^2 - \frac{a''}{a} + a^2 m_\sigma^2\right)\delta\sigma_k = 0
$$

For matter-dominated contraction with a(η) ∝ η² (η < 0, η → 0⁻):
- a''/a = 2/η²
- a²m_σ² = m_σ² a_0² (η/η_0)⁴

The effective potential is:

$$
\frac{a''}{a} - a^2 m_\sigma^2 = \frac{2}{\eta^2} - m_\sigma^2 a_0^2 \left(\frac{\eta}{\eta_0}\right)^4
$$

At Hubble crossing (k|η| ~ 1), the mass correction is:

$$
\frac{a^2 m_\sigma^2}{k^2}\bigg|_{k\eta \sim 1} \sim \frac{m_\sigma^2}{H_k^2}
$$

where H_k is the Hubble rate when mode k crosses the horizon.

### Spectral tilt

The power spectrum of δσ acquires a tilt:

$$
n_\sigma - 1 = -2\frac{m_\sigma^2}{3H_k^2} + O\left(\frac{m_\sigma^4}{H_k^4}\right)
$$

The sign is negative (red tilt) because the mass term suppresses long-wavelength modes that cross earlier (when H is larger and the mass correction is smaller) relative to short-wavelength modes that cross later (when H is smaller and the mass correction is more important).

Wait — let me be more careful about the sign.

During contraction, modes cross the Hubble radius from small k (early, large |t|, large H) to large k (late, small |t|, small H). The Hubble rate H = 2/(3|t|) increases as |t| → 0.

Actually: during contraction, |H| = 2/(3|t|) INCREASES as t → 0⁻. So modes that cross later see larger H, meaning m²/H² is SMALLER for later-crossing (larger k) modes.

The power per mode: P_σ(k) ∝ H_k²[1 − c × m²/H_k²] where c > 0.

For larger k: H_k is larger → m²/H_k² is smaller → P_σ is larger → spectrum is BLUE (n > 1).

**This gives a blue tilt, not a red tilt!**

### The sign problem

In the matter-dominated contracting phase:
- |H| grows as contraction proceeds
- Large-k modes cross later, when |H| is larger
- P_σ ∝ H_k² ∝ k^{something positive}

The Hubble rate at crossing: for a ∝ |t|^{2/3}, H = 2/(3|t|), and mode k crosses when k = a|H|.

Using a ∝ |t|^{2/3} and |H| = 2/(3|t|):
k = a|H| = c₁|t|^{2/3} × (2/3)|t|⁻¹ = c₂|t|⁻¹/³

So |t|_k ∝ k⁻³, giving |H_k| ∝ k³.

The massless spectator spectrum: P_σ ∝ H_k²/(4π²) ∝ k⁶ → extremely blue!

But wait — this contradicts the known result that dust contraction gives a scale-invariant spectrum. The resolution: the curvature perturbation ζ_σ = Hδσ/σ̇ involves additional factors that cancel the k-dependence.

For the curvaton, the relevant quantity is not P_σ(k) but the curvature perturbation ζ_σ = δN = (H/σ̇)δσ. The conversion from δσ to ζ introduces k-dependent factors.

**Let me redo this properly using the Mukhanov-Sasaki framework for the curvaton.**

### Corrected analysis

The Mukhanov variable for the curvaton:

$$
u_k = a\,\delta\sigma_k
$$

The mode equation:

$$
u_k'' + \left(k^2 - \frac{a''}{a} + a^2 m_\sigma^2\right)u_k = 0
$$

For a massless field on matter-dominated contraction: u'' + (k² − 2/η²)u = 0, with Bunch-Davies solution giving the same growing mode as the inflaton. The power spectrum of δσ is:

$$
P_{\delta\sigma}(k) = \frac{k^3}{2\pi^2}\left|\frac{u_k}{a}\right|^2
$$

On super-Hubble scales, the growing mode gives |u_k/a| ∝ 1/(k^{3/2}η³ a), and since a ∝ η²:

$$
\left|\frac{u_k}{a}\right|^2 \propto \frac{1}{k^3 \eta^{10}}
$$

So P_{δσ} ∝ k⁰ × (time-dependent growth) — scale-invariant! ✓

**The scale invariance comes from the a''/a = 2/η² pump term, same as for the inflaton.** The mass correction then gives:

$$
n_\sigma - 1 \approx 2\frac{m_\sigma^2 a^2(\eta_k)}{k^2}\bigg|_{k\eta_k \sim 1}
$$

Since a²/k² at crossing scales as η⁴/η⁻² = η⁶ and η_k ∝ 1/k (from k|η_k| ~ 1):

$$
n_\sigma - 1 \propto m_\sigma^2 \eta_k^4 \propto m_\sigma^2/k^4
$$

This is k-DEPENDENT → not a power-law tilt → more complex behavior.

Actually, I need to be even more careful. The standard result for a massive spectator on a de Sitter background gives n − 1 = −2m²/(3H²). But we are NOT on de Sitter — we are on a power-law contracting background.

### The correct result for matter-dominated contraction

For a(η) ∝ η² (matter-dominated contraction), the pump term is:

$$
\frac{a''}{a} = \frac{2}{\eta^2}
$$

With a mass term, the mode equation is:

$$
u_k'' + \left(k^2 - \frac{\nu^2 - 1/4}{\eta^2}\right)u_k = 0
$$

where $\nu^2 = 9/4 − m_\sigma^2/H_0^2 × (\eta/\eta_0)^4$.

**The mass term is NOT constant in conformal time for matter domination.** It has η⁴ dependence, which means it cannot be absorbed into a constant ν. The mode equation is not exactly solvable as a Bessel equation.

In the WKB approximation, the spectral index correction is (Cai & Brandenberger 2011):

$$
n_\sigma - 1 \approx 2\nu - 3
$$

where ν depends on the effective mass at horizon crossing. For small mass:

$$
\nu \approx \frac{3}{2} - \frac{m_\sigma^2}{3H_k^2}
$$

giving:

$$
n_\sigma - 1 \approx -\frac{2m_\sigma^2}{3H_k^2}
$$

**BUT: H_k varies for different k modes.** During matter contraction, |H| grows toward the bounce. If we evaluate at a fixed reference H (as in de Sitter), the tilt is constant. But in the contracting background, H_k is k-dependent, introducing additional k-dependence (running).

### Summary for mass-induced tilt

- **Standard curvaton physics** — not bounce-specific
- **Red tilt** for positive m² (n_σ < 1)
- **Magnitude:** n_σ − 1 ≈ −2m_σ²/(3H_k²), evaluated at Hubble crossing during contraction
- **Running:** non-zero because H_k varies during contraction (unlike de Sitter)
- **Scale-dependent H_k makes this more complex than the inflationary curvaton**

---

## Mechanism 2: Quasi-Matter Contraction Deviations (w ≈ ε ≠ 0)

### How it works

If the effective equation of state during contraction is not exactly w = 0 but w = ε (small), the pump term changes:

$$
\frac{z''}{z} = \frac{\nu^2 - 1/4}{\eta^2}, \quad \nu = \frac{3(1-w)}{2(1+3w)} \approx \frac{3}{2} - 6w + O(w^2)
$$

The spectral index becomes:

$$
n_s - 1 = 3 - 2\nu = \frac{12w}{1+3w} \approx 12w
$$

For n_s = 0.965: w ≈ 0.003.

### Assessment

- **This is NOT a curvaton mechanism** — it modifies the inflaton/dust spectrum directly
- **Not specific to the bounce or ECH** — purely a contraction-phase effect
- **Requires fine-tuning w to 0.3%** — not natural unless there's a dynamical reason
- **Already in the literature** (Quintin et al. 2015)

**Rating: standard, not ALP-related, already studied**

---

## Mechanism 3: Conversion-Induced Tilt

### How it works

If the isocurvature-to-curvature conversion efficiency depends on k (through the details of the bounce or the post-bounce decay), an additional tilt is generated at conversion:

$$
\zeta(k) = \alpha(k)\,\mathcal{S}(k)
$$

If α(k) ∝ k^{n_α}, the total tilt is n_s − 1 = (n_σ − 1) + n_α.

### When does α depend on k?

- If conversion happens on super-Hubble scales: α is k-independent → no additional tilt
- If conversion happens near Hubble crossing: α depends on k through H(t_conversion)
- If conversion involves a resonance or phase transition: α can have non-trivial k-dependence

For the standard curvaton (ALP oscillates, dominates, decays): conversion is on super-Hubble scales → α ≈ r_dec (k-independent) → **no conversion-induced tilt**.

**Rating: not operative for standard curvaton decay**

---

## Mechanism 4: Background Equation-of-State Effects

### How it works

If the ALP itself modifies the effective equation of state (by becoming energetically important during contraction), it changes the pump term and hence the spectral index of the inflaton perturbations.

### Assessment

For the curvaton to work, it must be subdominant during contraction (ρ_σ ≪ ρ_φ). If it modifies the EOS, it's no longer a spectator → consistency of the curvaton assumption breaks down.

**Rating: self-contradictory for standard curvaton setup**

---

## Summary

| Mechanism | Operates? | Bounce-specific? | ECH-specific? |
|-----------|----------|------------------|---------------|
| Mass-induced tilt | YES | NO (standard curvaton) | NO |
| Quasi-matter deviation | YES | NO (contraction-phase) | NO |
| Conversion-induced tilt | NO (for standard curvaton) | Would be bounce-specific | Possibly |
| Background EOS modification | NO (self-contradictory) | N/A | N/A |

**The only operative tilt mechanism for the ALP curvaton is the mass-induced tilt.** This is standard curvaton physics, not bounce-specific or ECH-specific. The bounce-specific aspects enter only through:
1. The cosmological scenario (contraction → bounce → expansion, instead of inflation)
2. The fact that H_k varies during contraction (unlike de Sitter), modifying the running
3. The ALP's ECH origin (motivating its existence, not its tilt)
