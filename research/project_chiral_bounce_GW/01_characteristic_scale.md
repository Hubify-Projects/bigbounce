# 01: Characteristic Scale Identification

**Created:** 2026-03-17
**Status:** COMPLETE

---

## What sets the chiral signal's characteristic scale?

The chiral GW signal from the bounce has a characteristic wavenumber determined by the bounce dynamics. There are several candidate scales:

### Scale 1: The Hubble scale at the bounce

At the bounce, H = 0. So H_b is not directly useful as a frequency scale. However, the Hubble rate evolves rapidly near the bounce:

$$
H(t) = \frac{2\alpha^2 t}{1 + 4\alpha^2 t^2}
$$

The maximum of |H| occurs at t_max = 1/(2α), giving:

$$
H_{\rm max} = \frac{\alpha}{2} = \frac{1}{2}\sqrt{\frac{\rho_{\rm crit}}{3M_{\rm Pl}^2}}
$$

With ρ_crit = 0.21 M_Pl⁴:

$$
\alpha = \sqrt{\frac{0.21}{3}} M_{\rm Pl} = 0.265\,M_{\rm Pl}
$$

$$
H_{\rm max} = 0.132\,M_{\rm Pl} = 3.2 \times 10^{17}\,\text{GeV}
$$

### Scale 2: The bounce duration (inverse timescale)

The bounce timescale is set by the duration over which H transitions from negative to positive. For the ECH radiation bounce:

$$
\Delta t_{\rm bounce} \sim \frac{1}{\alpha} = \frac{1}{0.265\,M_{\rm Pl}} = 3.77\,t_{\rm Pl}
$$

The corresponding frequency:

$$
f_{\rm bounce} \sim \frac{1}{\Delta t_{\rm bounce}} \sim \alpha \sim 0.265\,M_{\rm Pl}
$$

### Scale 3: The comoving bounce scale k_b

The comoving wavenumber that is at the Hubble radius at the time of maximum H:

$$
k_b = a_b H_{\rm max} = a_b \times 0.132\,M_{\rm Pl}
$$

where a_b is the scale factor at the bounce. In Planck units with a_b = 1 (our Phase 1a convention):

$$
k_b = 0.132\,M_{\rm Pl}
$$

More precisely, the relevant scale for the chiral signal is the scale at which the parity-violating coupling is strongest. For the Chern-Simons coupling μ(η) = α_CS σ'/f_a:

$$
k_{\rm chiral} \sim a_b \times |\mu|_{\rm max}^{1/2}
$$

But μ has dimensions of inverse length, so modes with k ~ μ experience the strongest differential amplification. The scale μ is set by the ALP dynamics:

$$
\mu \sim \frac{\alpha_{\rm CS}\,\dot{\sigma}}{f_a}
$$

At the bounce, if σ̇ ~ M_Pl² (gravitational coupling, natural scale), then μ ~ α_CS M_Pl²/f_a. With f_a ~ M_Pl and α_CS ~ 1/γ:

$$
\mu \sim \frac{M_{\rm Pl}}{\gamma} \sim 3.6\,M_{\rm Pl}
$$

This is comparable to or larger than the bounce scale itself.

### Scale 4: The torsion scale (Nieh-Yan coupling)

For the Nieh-Yan coupling, the chiral source is proportional to the torsion, which is maximal at the bounce:

$$
T \sim \frac{\sqrt{\rho_{\rm crit}}}{M_{\rm Pl}} \sim \frac{(0.21)^{1/2} M_{\rm Pl}^2}{M_{\rm Pl}} \sim 0.46\,M_{\rm Pl}
$$

This is again Planck-scale.

---

## Summary: All characteristic scales are Planckian

| Scale | Value | In GeV |
|-------|-------|--------|
| H_max | 0.132 M_Pl | 3.2 × 10¹⁷ GeV |
| 1/Δt_bounce | 0.265 M_Pl | 6.5 × 10¹⁷ GeV |
| k_b/a_b | 0.132 M_Pl | 3.2 × 10¹⁷ GeV |
| Torsion scale | 0.46 M_Pl | 1.1 × 10¹⁸ GeV |
| Chern-Simons μ_max | ~M_Pl/γ | ~8.9 × 10¹⁸ GeV |

**Every characteristic scale of the chiral signal is O(0.1–1) M_Pl.** The ECH bounce occurs at ρ = 0.21 M_Pl⁴, which is deeply Planckian. There is no parametric separation between the bounce scale and the Planck scale.

This is a direct consequence of ρ_crit = 0.21 M_Pl⁴ being fixed by the Barbero-Immirzi parameter γ = 0.274. In ECH, the bounce energy is NOT a free parameter — it is within an order of magnitude of the Planck energy.

---

## Critical observation

For the frequency gate, the relevant quantity is the COMOVING wavenumber k_b, not the physical scale. The comoving k_b = a_b × (physical scale). Since a_b is the scale factor at the bounce, the present-day frequency depends on the TOTAL expansion from a_b to a_0:

$$
f_0 = \frac{k_b}{2\pi a_0} = \frac{a_b}{a_0} \times \frac{(\text{physical bounce scale})}{2\pi}
$$

The ratio a_b/a_0 encodes the entire expansion history from the bounce to today. This is what determines whether the Planckian signal reaches observable frequencies.

---

## Could a lower bounce scale help?

If we relax the ECH requirement ρ_crit = 0.21 M_Pl⁴ and consider a generic bounce at lower energy:

$$
\rho_{\rm bounce} = \rho_* \ll M_{\rm Pl}^4
$$

Then:
- Physical bounce scale ~ ρ_*^{1/4}
- More expansion needed to reach the same final state
- But also more redshift of the signal

The frequency today scales as:

$$
f_0 \propto \rho_*^{1/4} \times \frac{a_{\rm bounce}}{a_0}
$$

Lower bounce energy → lower source frequency, but also lower a_bounce → more expansion needed. The net effect depends on the expansion history and is computed in the next file.

**However:** lowering ρ_* below M_Pl⁴ by many orders of magnitude loses the ECH motivation (γ = 0.274 gives ρ_crit ~ 0.2 M_Pl⁴). A bounce at ρ ~ (10¹⁰ GeV)⁴ has no connection to the Barbero-Immirzi parameter.
