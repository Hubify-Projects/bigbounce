# 01: Power Spectrum Derivation — COMPLETE

---

## Background Assumptions

Contracting matter-dominated universe:
- w = 0, epsilon = -dH/H^2 = 3/2 (constant)
- Conformal time eta < 0, with eta -> 0^- at the bounce
- Scale factor: a(eta) = a_0 (eta/eta_0)^2
- Conformal Hubble rate: H = a'/a = 2/eta
- Canonical scalar field phi with V = m^2 phi^2 / 2 in oscillating regime
- c_s = 1

---

## Mukhanov-Sasaki Equation

The Mukhanov variable v_k = z * zeta_k with

$$
z = \frac{a\sqrt{2\epsilon}}{c_s} = a\sqrt{3}
$$

For a = a_0 (eta/eta_0)^2: z = a_0 sqrt(3) (eta/eta_0)^2.

Absorb eta_0 into a_0 by defining a_0' = a_0 / eta_0^2, then z = a_0' sqrt(3) eta^2. For simplicity write z = A eta^2 where A = a_0 sqrt(3) / eta_0^2.

$$
\frac{z''}{z} = \frac{2}{\eta^2}
$$

The mode equation:

$$
v_k'' + \left(k^2 - \frac{2}{\eta^2}\right) v_k = 0
$$

This is the spherical Bessel equation with nu = 3/2.

---

## Mode Function (Bunch-Davies Vacuum)

General solution:

$$
v_k(\eta) = \alpha \frac{e^{-ik\eta}}{\sqrt{2k}}\left(1 - \frac{i}{k\eta}\right) + \beta \frac{e^{+ik\eta}}{\sqrt{2k}}\left(1 + \frac{i}{k\eta}\right)
$$

Bunch-Davies vacuum: at eta -> -infinity (deep subhorizon), select the positive-frequency mode:

$$
v_k(\eta) \xrightarrow{\eta \to -\infty} \frac{e^{-ik\eta}}{\sqrt{2k}}
$$

This fixes alpha = 1, beta = 0:

$$
\boxed{v_k(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}}\left(1 - \frac{i}{k\eta}\right)}
$$

### Verification: Wronskian normalization

$$
v_k v_k^{*\prime} - v_k^* v_k' = i
$$

Compute v_k':

$$
v_k' = \frac{e^{-ik\eta}}{\sqrt{2k}}\left(-ik + \frac{i}{k\eta^2} - \frac{ik \cdot (-i)}{k\eta}\right)
$$

Wait, let me do this directly:

$$
v_k = \frac{e^{-ik\eta}}{\sqrt{2k}} - \frac{i e^{-ik\eta}}{\sqrt{2k} \cdot k\eta} = \frac{e^{-ik\eta}}{\sqrt{2k}}\left(1 - \frac{i}{k\eta}\right)
$$

$$
v_k' = \frac{e^{-ik\eta}}{\sqrt{2k}}\left[-ik\left(1 - \frac{i}{k\eta}\right) + \frac{i}{k\eta^2}\right]
$$

$$
= \frac{e^{-ik\eta}}{\sqrt{2k}}\left[-ik - \frac{1}{\eta} + \frac{i}{k\eta^2}\right]
$$

The Wronskian:

$$
v_k v_k^{*\prime} - v_k^* v_k' = \frac{1}{2k}\left[\left(1 - \frac{i}{k\eta}\right)\left(ik - \frac{1}{\eta} - \frac{i}{k\eta^2}\right) - \left(1 + \frac{i}{k\eta}\right)\left(-ik - \frac{1}{\eta} + \frac{i}{k\eta^2}\right)\right]
$$

Expanding the first product:

$$
ik - \frac{1}{\eta} - \frac{i}{k\eta^2} + \frac{1}{\eta} + \frac{i}{k\eta^2} - \frac{1}{k^2\eta^3}
= ik - \frac{1}{k^2\eta^3}
$$

Wait — let me be more careful. First product:

$$
(1)(ik) + (1)(-1/\eta) + (1)(-i/(k\eta^2)) + (-i/(k\eta))(ik) + (-i/(k\eta))(-1/\eta) + (-i/(k\eta))(-i/(k\eta^2))
$$

$$
= ik - 1/\eta - i/(k\eta^2) + 1/\eta + i/(k\eta^2) - 1/(k^2\eta^3)
$$

$$
= ik - 1/(k^2\eta^3)
$$

Second product:

$$
(1)(-ik) + (1)(-1/\eta) + (1)(i/(k\eta^2)) + (i/(k\eta))(-ik) + (i/(k\eta))(-1/\eta) + (i/(k\eta))(i/(k\eta^2))
$$

$$
= -ik - 1/\eta + i/(k\eta^2) + 1/\eta - i/(k\eta^2) - 1/(k^2\eta^3)
$$

$$
= -ik - 1/(k^2\eta^3)
$$

Therefore:

$$
v_k v_k^{*\prime} - v_k^* v_k' = \frac{1}{2k}\left[(ik - 1/(k^2\eta^3)) - (-ik - 1/(k^2\eta^3))\right] = \frac{1}{2k} \cdot 2ik = \frac{i}{1} = i
$$

**Wronskian = i. CONFIRMED.** The mode function is correctly normalized.

---

## Zeta Mode Function

$$
\zeta_k(\eta) = \frac{v_k(\eta)}{z(\eta)} = \frac{1}{A\eta^2} \cdot \frac{e^{-ik\eta}}{\sqrt{2k}}\left(1 - \frac{i}{k\eta}\right)
$$

where A = a_0 sqrt(3) / eta_0^2 (or equivalently, z = A eta^2).

### Superhorizon limit (|k eta| << 1):

$$
\zeta_k(\eta) \xrightarrow{|k\eta| \ll 1} \frac{1}{A\eta^2} \cdot \frac{1}{\sqrt{2k}} \cdot \frac{(-i)}{k\eta} = \frac{-i}{A\sqrt{2k^3}\,\eta^3}
$$

**The growing mode: zeta grows as |eta|^{-3}.**

### Full-range form useful for integrals:

$$
\zeta_k(\eta) = \frac{e^{-ik\eta}}{A\sqrt{2k}\,\eta^2}\left(1 - \frac{i}{k\eta}\right)
$$

$$
\zeta_k'(\eta) = \frac{e^{-ik\eta}}{A\sqrt{2k}}\left[\frac{-ik}{\eta^2}\left(1 - \frac{i}{k\eta}\right) + \frac{1}{\eta^2}\left(-\frac{2}{\eta} + \frac{i}{k\eta^2} \cdot ... \right)\right]
$$

Actually, let me compute zeta_k' cleanly. Write u_k(eta) = (1 - i/(k eta)):

$$
\zeta_k = \frac{e^{-ik\eta}}{A\sqrt{2k}} \cdot \frac{u_k}{\eta^2}
$$

$$
\zeta_k' = \frac{e^{-ik\eta}}{A\sqrt{2k}} \left[\frac{-ik \cdot u_k}{\eta^2} + \frac{u_k'}{\eta^2} + u_k \cdot \frac{-2}{\eta^3}\right]
$$

with u_k' = i/(k eta^2). So:

$$
\zeta_k' = \frac{e^{-ik\eta}}{A\sqrt{2k}\,\eta^2} \left[-ik\left(1 - \frac{i}{k\eta}\right) + \frac{i}{k\eta^2} - \frac{2}{\eta}\left(1 - \frac{i}{k\eta}\right)\right]
$$

$$
= \frac{e^{-ik\eta}}{A\sqrt{2k}\,\eta^2} \left[-ik - \frac{1}{\eta} + \frac{i}{k\eta^2} - \frac{2}{\eta} + \frac{2i}{k\eta^2}\right]
$$

$$
= \frac{e^{-ik\eta}}{A\sqrt{2k}\,\eta^2} \left[-ik - \frac{3}{\eta} + \frac{3i}{k\eta^2}\right]
$$

### Superhorizon limit of zeta_k':

For |k eta| << 1, the -ik term is subleading:

$$
\zeta_k' \xrightarrow{|k\eta| \ll 1} \frac{1}{A\sqrt{2k}\,\eta^2}\left[-\frac{3}{\eta} + \frac{3i}{k\eta^2}\right] \approx \frac{3i}{A\sqrt{2k^3}\,\eta^4}
$$

Check: d/d eta [(-i)/(A sqrt(2k^3) eta^3)] = 3i/(A sqrt(2k^3) eta^4). **CONFIRMED.**

---

## Power Spectrum

$$
P(k, \eta) = |\zeta_k(\eta)|^2 = \frac{1}{2k A^2 \eta^4} \left|1 - \frac{i}{k\eta}\right|^2 = \frac{1}{2k A^2 \eta^4}\left(1 + \frac{1}{k^2\eta^2}\right)
$$

### Superhorizon:

$$
P(k, \eta) \xrightarrow{|k\eta| \ll 1} \frac{1}{2k^3 A^2 \eta^6}
$$

### Dimensionless power spectrum:

$$
\mathcal{P}_\zeta(k, \eta) = \frac{k^3}{2\pi^2} P(k, \eta) = \frac{1}{4\pi^2 A^2 \eta^6}
$$

Wait — let me recheck. With A = a_0 sqrt(3) / eta_0^2, and if we use the simpler convention z = a sqrt(3) = a_0 sqrt(3) eta^2/eta_0^2:

Actually, let me just use the explicit form z = a_0 sqrt(3) (eta/eta_0)^2. Then A = a_0 sqrt(3)/eta_0^2.

$$
P^{\rm super}(k, \eta) = \frac{1}{2k^3 A^2 \eta^6} = \frac{\eta_0^4}{2k^3 \cdot 3 a_0^2 \cdot \eta^6}
$$

For notational clarity, define the dimensionful normalization constant:

$$
\mathcal{N}^2 \equiv 2 A^2 = \frac{6 a_0^2}{\eta_0^4}
$$

Then:

$$
P^{\rm super}(k, \eta) = \frac{1}{\mathcal{N}^2 k^3 \eta^6}
$$

$$
\mathcal{P}_\zeta(\eta) = \frac{1}{2\pi^2 \mathcal{N}^2 \eta^6}
$$

### Key properties:

1. **Scale-invariant:** P_zeta is independent of k. n_s = 1. CONFIRMED.
2. **Time-dependent (growing):** P_zeta grows as |eta|^{-6}. This is the growing mode squared.
3. **The normalization N^2 cancels in f_NL.** Since f_NL = (5/12) B/(P*P), and both B and P^2 depend on N, the ratio is independent of a_0, eta_0.

---

## Boxed Results

$$
\boxed{v_k(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}}\left(1 - \frac{i}{k\eta}\right)}
$$

$$
\boxed{\zeta_k(\eta) = \frac{e^{-ik\eta}}{A\sqrt{2k}\,\eta^2}\left(1 - \frac{i}{k\eta}\right), \quad A = \frac{a_0\sqrt{3}}{\eta_0^2}}
$$

$$
\boxed{P^{\rm super}(k, \eta) = \frac{1}{\mathcal{N}^2 k^3 \eta^6}, \quad \mathcal{N}^2 = 2A^2 = \frac{6a_0^2}{\eta_0^4}}
$$

$$
\boxed{\mathcal{P}_\zeta(\eta) = \frac{1}{2\pi^2 \mathcal{N}^2 \eta^6} \quad (\text{scale-invariant, growing})}
$$

**The power spectrum is verified. Wronskian confirmed. Ready for bispectrum.**
