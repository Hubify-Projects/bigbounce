# 02: Redshift to Today

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Frequency Mapping

A comoving mode with wavenumber k has present-day frequency:

$$
f_0 = \frac{k}{2\pi a_0}
$$

The physical frequency at the time of production (at the bounce) was:

$$
f_* = \frac{k}{2\pi a_b}
$$

So:

$$
f_0 = f_* \times \frac{a_b}{a_0}
$$

The expansion ratio a_b/a_0 is the total redshift from the bounce to today.

---

## Computing a_b/a_0

### Method: entropy conservation

After the bounce, the universe expands through a radiation-dominated era (and later matter and dark energy eras). Assuming entropy conservation from the bounce to today:

$$
g_{*s}(T_b)\,T_b^3\,a_b^3 = g_{*s}(T_0)\,T_0^3\,a_0^3
$$

where g_{*s} is the effective number of entropic degrees of freedom.

$$
\frac{a_b}{a_0} = \frac{T_0}{T_b}\left(\frac{g_{*s}(T_0)}{g_{*s}(T_b)}\right)^{1/3}
$$

### The bounce temperature T_b

The energy density at the bounce:

$$
\rho_b = \rho_{\rm crit} = 0.21\,M_{\rm Pl}^4
$$

For a radiation-dominated fluid at the bounce:

$$
\rho_b = \frac{\pi^2}{30}\,g_*(T_b)\,T_b^4
$$

Solving for T_b:

$$
T_b = \left(\frac{30\,\rho_b}{\pi^2\,g_*}\right)^{1/4} = \left(\frac{30 \times 0.21}{\pi^2 \times g_*}\right)^{1/4}M_{\rm Pl}
$$

With g_*(T_b) = 106.75 (Standard Model at high temperature):

$$
T_b = \left(\frac{6.3}{1053}\right)^{1/4}M_{\rm Pl} = (5.98 \times 10^{-3})^{1/4}M_{\rm Pl} = 0.278\,M_{\rm Pl}
$$

$$
T_b = 0.278 \times 2.435 \times 10^{18}\,\text{GeV} = 6.77 \times 10^{17}\,\text{GeV}
$$

### The expansion ratio

Using T_0 = 2.725 K = 2.35 × 10⁻¹³ GeV and g_{*s}(T_0) = 3.91, g_{*s}(T_b) ≈ 106.75:

$$
\frac{a_b}{a_0} = \frac{2.35 \times 10^{-13}}{6.77 \times 10^{17}} \times \left(\frac{3.91}{106.75}\right)^{1/3}
$$

$$
= 3.47 \times 10^{-31} \times 0.330
$$

$$
= 1.15 \times 10^{-31}
$$

---

## Present-day frequency of the bounce scale

The physical frequency at the bounce:

$$
f_* \sim \frac{1}{2\pi\,\Delta t_{\rm bounce}} \sim \frac{\alpha}{2\pi} = \frac{0.265\,M_{\rm Pl}}{2\pi}
$$

In Hz: M_Pl = 1.22 × 10¹⁹ GeV, and 1 GeV⁻¹ = 6.58 × 10⁻²⁵ s, so:

$$
f_* = \frac{0.265 \times 1.22 \times 10^{19}}{2\pi \times 6.58 \times 10^{-25}\,\text{s}} = \frac{3.23 \times 10^{18}}{4.13 \times 10^{-24}} \,\text{Hz}
$$

Wait, let me redo this more carefully. In natural units, M_Pl = 2.435 × 10¹⁸ GeV. Converting to frequency:

$$
f = \frac{E}{2\pi\hbar} = \frac{E}{2\pi} \times \frac{1}{\hbar}
$$

With ℏ = 6.582 × 10⁻²⁵ GeV·s:

$$
f_* = \frac{0.265 \times 2.435 \times 10^{18}\,\text{GeV}}{2\pi \times 6.582 \times 10^{-25}\,\text{GeV·s}}
$$

$$
= \frac{6.45 \times 10^{17}}{4.134 \times 10^{-24}}\,\text{Hz} = 1.56 \times 10^{41}\,\text{Hz}
$$

### Present-day frequency:

$$
f_0 = f_* \times \frac{a_b}{a_0} = 1.56 \times 10^{41} \times 1.15 \times 10^{-31}\,\text{Hz}
$$

$$
\boxed{f_0 \approx 1.8 \times 10^{10}\,\text{Hz} = 18\,\text{GHz}}
$$

---

## Cross-check with standard formula

The standard formula for the present-day frequency of a GW produced at temperature T_* is:

$$
f_0 = 2.6 \times 10^{-8}\,\text{Hz} \times \left(\frac{T_*}{100\,\text{GeV}}\right) \times \left(\frac{g_*}{100}\right)^{1/6} \times \left(\frac{k}{H_*}\right)
$$

For our case: T_* = 6.77 × 10¹⁷ GeV, g_* = 106.75, and k/H_* ~ 1 (bounce-scale mode):

$$
f_0 = 2.6 \times 10^{-8} \times \frac{6.77 \times 10^{17}}{100} \times \left(\frac{106.75}{100}\right)^{1/6} \times 1
$$

$$
= 2.6 \times 10^{-8} \times 6.77 \times 10^{15} \times 1.01
$$

$$
= 1.78 \times 10^{8}\,\text{Hz} \approx 178\,\text{MHz}
$$

Hmm, this gives ~10⁸ Hz, which differs from the previous calculation by a factor of ~100. Let me reconcile.

The discrepancy is in what "k/H_*" means. The standard formula uses H_* as the Hubble rate at the time of GW production. But at the bounce, H = 0. The relevant physical scale is NOT H_* but rather the inverse bounce timescale α ~ 0.265 M_Pl.

Let me use the formula more carefully. The mode with physical wavenumber k_phys = α at the bounce has comoving wavenumber k = a_b × α. Today, this mode has frequency:

$$
f_0 = \frac{a_b \alpha}{2\pi a_0} = \frac{\alpha}{2\pi} \times \frac{a_b}{a_0}
$$

Using the entropy conservation result a_b/a_0 = 1.15 × 10⁻³¹:

$$
f_0 = \frac{0.265 \times 2.435 \times 10^{18}\,\text{GeV}}{2\pi} \times 1.15 \times 10^{-31} / (6.582 \times 10^{-25}\,\text{GeV·s})
$$

Let me compute step by step:

α = 0.265 × 2.435 × 10¹⁸ GeV = 6.45 × 10¹⁷ GeV

α/(2π) = 1.03 × 10¹⁷ GeV

Convert to Hz: 1.03 × 10¹⁷ / (6.582 × 10⁻²⁵) = 1.56 × 10⁴¹ Hz (physical frequency at bounce)

f_0 = 1.56 × 10⁴¹ × 1.15 × 10⁻³¹ = 1.8 × 10¹⁰ Hz = 18 GHz ✓

The standard formula cross-check:

The standard formula assumes f_0 = (a_*/a_0) × f_*, where f_* = k_phys/(2π) and k_phys = H_*. But our k_phys = α ≠ H_*. Using k_phys = α:

$$
f_0 = 2.6 \times 10^{-8}\,\text{Hz} \times \frac{T_*}{100\,\text{GeV}} \times \left(\frac{g_*}{100}\right)^{1/6} \times \frac{k_{\rm phys}}{H_*}
$$

What is H_* at the bounce? H = 0 at the bounce, but the characteristic Hubble scale is H_max = α/2 = 0.132 M_Pl. So k_phys/H_* = α/H_max = 2.

Using the cross-check formula with T_* corresponding to the bounce temperature:

Actually, let me just use the direct scaling. The key frequency of a thermal relic at temperature T is:

$$
f_{\rm peak} \approx 8 \times 10^{-6}\,\text{Hz} \times \left(\frac{T_*}{10^6\,\text{GeV}}\right)
$$

(from Caprini et al. 2016 for electroweak-scale phase transitions, extrapolated).

For T_* = 6.77 × 10¹⁷ GeV = 6.77 × 10¹¹ × 10⁶ GeV:

$$
f \sim 8 \times 10^{-6} \times 6.77 \times 10^{11} = 5.4 \times 10^{6}\,\text{Hz} = 5.4\,\text{MHz}
$$

This is O(MHz–GHz), consistent with our GHz estimate to within a couple orders of magnitude (the exact prefactor depends on the physical scale relative to H).

---

## Result for alternative bounce scales

### ECH bounce (ρ_crit = 0.21 M_Pl⁴)

$$
\boxed{f_0^{\rm ECH} \sim 10^{9}\text{–}10^{10}\,\text{Hz} \quad (\text{GHz})}
$$

### Lower-energy bounce: ρ_bounce = (10¹⁶ GeV)⁴ (GUT scale)

T_b = (30 × (10¹⁶)⁴/(π² × 106.75))^{1/4} = ((30/1053) × 10⁶⁴)^{1/4} GeV ≈ 0.28 × 10¹⁶ GeV

f_0 ∝ T_b, so:

$$
f_0^{\rm GUT} \sim 10^{10} \times \frac{0.28 \times 10^{16}}{6.77 \times 10^{17}} = 10^{10} \times 4.1 \times 10^{-3} \sim 4 \times 10^{7}\,\text{Hz} \quad (\text{40 MHz})
$$

### Lower-energy bounce: ρ_bounce = (10¹⁰ GeV)⁴ (intermediate scale)

$$
f_0^{\rm int} \sim 10^{10} \times \frac{10^{10}}{10^{18}} \sim 100\,\text{Hz} \quad (\text{LIGO band!})
$$

### Lower-energy bounce: ρ_bounce = (10⁶ GeV)⁴

$$
f_0 \sim 10^{10} \times \frac{10^{6}}{10^{18}} \sim 10^{-2}\,\text{Hz} \quad (\text{LISA band!})
$$

### Lower-energy bounce: ρ_bounce = (1 GeV)⁴ (QCD scale)

$$
f_0 \sim 10^{10} \times \frac{1}{10^{18}} \sim 10^{-8}\,\text{Hz} \quad (\text{PTA band!})
$$

---

## Summary: frequency vs bounce energy

| Bounce energy ρ^{1/4} | T_bounce | f_0 today | Detector band |
|----------------------|----------|-----------|---------------|
| 10¹⁸ GeV (ECH/Planck) | ~10¹⁸ GeV | ~10¹⁰ Hz (GHz) | NONE |
| 10¹⁶ GeV (GUT) | ~10¹⁶ GeV | ~10⁸ Hz (100 MHz) | NONE (high-f concepts only) |
| 10¹⁰ GeV | ~10¹⁰ GeV | ~10² Hz | LIGO/ET |
| 10⁶ GeV | ~10⁶ GeV | ~10⁻² Hz | LISA |
| 10³ GeV (TeV) | ~10³ GeV | ~10⁻⁵ Hz | LISA |
| 1 GeV (QCD) | ~1 GeV | ~10⁻⁸ Hz | PTA |

**The ECH bounce at ρ_crit = 0.21 M_Pl⁴ produces signals at GHz — completely inaccessible.**

**Observable frequencies require ρ_bounce ≤ (10¹⁰ GeV)⁴ — at least 32 orders of magnitude below the ECH value.**

---

## Can post-bounce inflation help?

If there is an inflationary phase AFTER the bounce, it redshifts the bounce-scale modes to lower frequencies:

$$
f_0^{\rm with\,inflation} = f_0^{\rm no\,inflation} \times e^{-N_{\rm inf}}
$$

where N_inf is the number of post-bounce e-folds of inflation.

To bring f_0 from GHz to LISA (mHz):

$$
e^{-N_{\rm inf}} = \frac{10^{-3}}{10^{10}} = 10^{-13}
$$

$$
N_{\rm inf} = 13 \times \ln(10) \approx 30
$$

To bring f_0 from GHz to PTA (nHz):

$$
N_{\rm inf} \approx 18 \times \ln(10) \approx 41
$$

So ~30–40 e-folds of post-bounce inflation would redshift the signal into observable bands.

**But this requires inflation after the bounce** — which means the bounce is no longer the final word on perturbation generation. If inflation generates its own perturbation spectrum (which it does), the bounce signal competes with and is potentially overwhelmed by the inflationary spectrum. The bounce chirality would be a sub-dominant correction to the inflationary SGWB.

Furthermore, invoking post-bounce inflation undermines the entire motivation: the bounce was supposed to REPLACE inflation as the perturbation-generating mechanism. If we need inflation anyway, the bounce adds nothing.
