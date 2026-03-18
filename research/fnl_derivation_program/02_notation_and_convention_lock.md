# 02: Notation and Convention Lock

**Created:** 2026-03-17
**Status:** COMPLETE — ALL CONVENTIONS FIXED

---

## Locked Conventions

### Background

Cosmic time t < 0 (contraction), t = 0 at bounce.

$$
a(t) = a_0 \left(\frac{-t}{t_0}\right)^{2/3}, \quad t < 0
$$

Hubble rate:
$$
H \equiv \frac{\dot{a}}{a} = \frac{2}{3t} < 0 \quad (t < 0)
$$

Conformal time eta < 0 (eta -> 0^- at bounce):
$$
a(\eta) = a_0 \left(\frac{\eta}{\eta_0}\right)^2
$$

Conformal Hubble rate:
$$
\mathcal{H} \equiv \frac{a'}{a} = \frac{2}{\eta}
$$

where prime = d/d eta.

EOS and slow-roll parameter:
$$
w = 0, \quad \epsilon \equiv -\frac{\dot{H}}{H^2} = \frac{3}{2}
$$

Note: epsilon = 3(1+w)/2 = 3/2 for w = 0. This is NOT small.

---

### Perturbation Variables

**Comoving curvature perturbation zeta:**

$$
ds^2 = -dt^2 + a^2(t) e^{2\zeta(\mathbf{x},t)} \delta_{ij} dx^i dx^j
$$

(scalar perturbations only, neglecting tensor and vector; to linear order this is the standard comoving gauge)

**Bardeen potential Phi:**

On superhorizon scales in matter domination:
$$
\Phi = \frac{3}{5} \zeta + \text{decaying mode}
$$

We use **zeta throughout** and convert to Phi only for convention checks.

---

### Fourier Convention

$$
\zeta(\mathbf{x}) = \int \frac{d^3 k}{(2\pi)^3} \, \zeta_\mathbf{k} \, e^{i\mathbf{k} \cdot \mathbf{x}}
$$

$$
\zeta_\mathbf{k}^* = \zeta_{-\mathbf{k}}
$$

---

### Power Spectrum

Two-point function:
$$
\langle \zeta_\mathbf{k} \zeta_{\mathbf{k}'} \rangle = (2\pi)^3 \delta^{(3)}(\mathbf{k} + \mathbf{k}') P(k)
$$

where P(k) has dimensions of [length]^3.

Dimensionless power spectrum:
$$
\mathcal{P}_\zeta(k) = \frac{k^3}{2\pi^2} P(k)
$$

For the matter bounce with n_s = 1: P_zeta(k) = A_s = const.

The observed value: A_s = 2.1 x 10^-9.

---

### Bispectrum

Three-point function:
$$
\langle \zeta_{\mathbf{k}_1} \zeta_{\mathbf{k}_2} \zeta_{\mathbf{k}_3} \rangle = (2\pi)^3 \delta^{(3)}(\mathbf{k}_1 + \mathbf{k}_2 + \mathbf{k}_3) \, B_\zeta(k_1, k_2, k_3)
$$

B_zeta has dimensions of [length]^6.

---

### f_NL Definition (PLANCK CONVENTION — LOCKED)

$$
\zeta(\mathbf{x}) = \zeta_G(\mathbf{x}) + \frac{3}{5} f_{\rm NL} \left[ \zeta_G^2(\mathbf{x}) - \langle \zeta_G^2 \rangle \right]
$$

This generates:
$$
B_\zeta^{\rm local}(k_1, k_2, k_3) = \frac{6}{5} f_{\rm NL} \left[ P(k_1) P(k_2) + P(k_2) P(k_3) + P(k_3) P(k_1) \right]
$$

**Extraction formula in the squeezed limit (k_1 -> 0, k_2 = k_3 = k):**

$$
B_\zeta(k_1, k, k) \to \frac{12}{5} f_{\rm NL} \, P(k_1) P(k)
$$

Therefore:
$$
\boxed{f_{\rm NL} = \frac{5}{12} \frac{B_\zeta(k_1, k, k)}{P(k_1) P(k)} \bigg|_{k_1 \to 0}}
$$

This is THE formula we use to extract f_NL from any computed bispectrum.

---

### Equivalence with the Phi Convention

Planck's original paper (Komatsu & Spergel 2001) defines:
$$
\Phi(\mathbf{x}) = \Phi_G(\mathbf{x}) + f_{\rm NL} \left[\Phi_G^2(\mathbf{x}) - \langle \Phi_G^2 \rangle \right]
$$

Since Phi = (3/5) zeta on superhorizon scales:
$$
\frac{3}{5}\zeta = \frac{3}{5}\zeta_G + f_{\rm NL} \left(\frac{3}{5}\right)^2 \zeta_G^2
$$

$$
\zeta = \zeta_G + \frac{3}{5} f_{\rm NL} \, \zeta_G^2
$$

**The SAME f_NL appears in both.** No conversion factor. This is already locked by our zeta convention above.

---

### The Cai et al. Quantity |B|_NL

Cai et al. (2009) define their shape function A_T(k_1, k_2, k_3) and then their non-Gaussianity parameter as:

$$
|B|_{\rm NL}(k_1, k_2, k_3) \equiv \frac{10}{3} \frac{A_T(k_1, k_2, k_3)}{k_1^3 + k_2^3 + k_3^3}
$$

**This is NOT the same object as f_NL^local.** The |B|_NL is a shape-dependent quantity that varies over triangle configurations. In the squeezed limit, they identify |B|_NL^local = -35/8.

**The relationship to our f_NL convention:**

Cai et al.'s bispectrum is:
$$
\langle \zeta_{\mathbf{k}_1} \zeta_{\mathbf{k}_2} \zeta_{\mathbf{k}_3} \rangle = (2\pi)^3 \delta^{(3)}(...) \cdot (2\pi)^4 \frac{A_T(k_1,k_2,k_3)}{k_1^3 k_2^3 k_3^3} \cdot \mathcal{P}_\zeta^2
$$

Wait — we need to be more careful here. The exact relation depends on how Cai et al. normalize A_T. Let me work from their bispectrum directly.

From Cai et al. Eq. (16), the three-point function from the cubic action:
$$
\langle \zeta_{\mathbf{k}_1} \zeta_{\mathbf{k}_2} \zeta_{\mathbf{k}_3} \rangle' = \frac{(2\pi)^4 \mathcal{P}_\zeta^2}{(k_1 k_2 k_3)^2} A_T(k_1, k_2, k_3)
$$

where the prime means the delta function is stripped.

So: B_zeta = (2pi)^4 P_zeta^2 A_T / (k_1 k_2 k_3)^2

And P(k) = (2pi^2/k^3) P_zeta

So: P(k_1) P(k_2) = (2pi^2)^2 P_zeta^2 / (k_1^3 k_2^3)

Our extraction formula:
f_NL = (5/12) B_zeta / [P(k_1) P(k)] in squeezed limit

= (5/12) * [(2pi)^4 P_zeta^2 A_T / (k_1 k_2 k_3)^2] / [(2pi^2)^2 P_zeta^2 / (k_1^3 k^3)]

= (5/12) * [(2pi)^4 / (2pi^2)^2] * [A_T * k_1^3 k^3 / (k_1^2 k^4)]

= (5/12) * 1 * [A_T * k_1 / k]

Hmm — this is getting k-dependent, which means I need the explicit k-dependence of A_T in the squeezed limit. This is exactly why the conversion matters.

**The key point is that A_T itself has specific k-scaling in the squeezed limit.** In the squeezed limit k_1 -> 0, k_2 = k_3 = k:

From Cai et al. Eq. (38): the leading behavior is A_T proportional to k_1^2 k^4 in the local-type region (they state A_T is dominated by terms scaling as k_1^2 k^4).

Let A_T = A_sq * k_1^2 k^4 in the squeezed limit (where A_sq is the numerical coefficient).

Then:
B_zeta = (2pi)^4 P_zeta^2 * A_sq * k_1^2 k^4 / (k_1^2 k^4) = (2pi)^4 P_zeta^2 A_sq

And:
f_NL = (5/12) * (2pi)^4 P_zeta^2 A_sq / [(2pi^2)^2 P_zeta^2 / (k_1^3 k^3)] * ...

This is getting circular. Let me take a cleaner approach.

**RESOLUTION: The cleanest path is to compute B_zeta directly and extract f_NL from the boxed formula above, WITHOUT going through Cai et al.'s intermediate notation.**

The Cai et al. |B|_NL = -35/8 is their own extraction using their own normalization. We will verify or refute this by computing B_zeta independently and applying our locked extraction formula.

---

### Why Literature Can Differ by Factors of 2

There are THREE distinct sources of factor-of-2 type differences:

**Source 1: Different f_NL normalizations.**
Some authors define zeta = zeta_G + f_NL zeta_G^2 (no 3/5 factor). In that convention, f_NL would be (3/5) times the Planck value. This is NOT the issue here — both Cai et al. and Planck use the (3/5) convention.

**Source 2: Different bispectrum shape functions.**
The quantity |B|_NL from Cai et al. is normalized by (k_1^3 + k_2^3 + k_3^3), while the standard f_NL extraction uses P(k_1)P(k_2) + cyc. In the squeezed limit, these are not proportional — the ratio depends on the k-scaling. If Cai et al. extract |B|_NL from a differently-normalized shape function than the standard local template, a factor of 2 can easily appear.

**Source 3: Approximate vs exact calculation.**
Li & Brandenberger label their result with "~" (approximately equal). If their approximation drops subdominant terms that happen to contribute ~50% of the answer at c_s = 1, the discrepancy is explained.

**Our strategy: compute B_zeta directly and extract f_NL from the locked formula. This eliminates all normalization ambiguities.**

---

### Mukhanov-Sasaki Variable

$$
v_k = z \zeta_k, \quad z = \frac{a\sqrt{2\epsilon}}{c_s} = a\sqrt{3}
$$

(using epsilon = 3/2, c_s = 1)

$$
v_k'' + \left(k^2 - \frac{z''}{z}\right) v_k = 0
$$

For matter contraction: z = a_0 sqrt(3) eta^2, so z''/z = 2/eta^2.

$$
v_k'' + \left(k^2 - \frac{2}{\eta^2}\right) v_k = 0
$$

---

### Sign Convention for Growing Mode

As eta -> 0^- (approaching bounce), the growing mode of v_k is:

$$
v_k^{(\rm grow)} \propto \frac{1}{\eta} \quad (\text{grows as } |\eta| \to 0)
$$

Therefore:
$$
\zeta_k^{(\rm grow)} = \frac{v_k}{z} \propto \frac{1/\eta}{a_0\sqrt{3}\eta^2} = \frac{1}{a_0\sqrt{3}\eta^3}
$$

**zeta GROWS as |eta|^{-3} during matter contraction.**

---

## Convention Lock Summary

| Symbol | Definition | Convention |
|--------|-----------|------------|
| t | Cosmic time, t < 0 for contraction | t = 0 at bounce |
| eta | Conformal time, eta < 0 | eta -> 0^- at bounce |
| a | Scale factor, a proportional to eta^2 | Decreasing during contraction |
| epsilon | -H_dot/H^2 = 3/2 | NOT small |
| zeta | Comoving curvature perturbation | ds^2 contains e^{2 zeta} |
| Phi | Bardeen potential | Phi = (3/5) zeta on superhorizon |
| P(k) | Dimensional power spectrum | <zeta_k zeta_k'> = (2pi)^3 delta P(k) |
| P_zeta | Dimensionless power spectrum | = k^3 P(k) / (2pi^2) |
| B_zeta | Bispectrum | <zeta zeta zeta> = (2pi)^3 delta B |
| f_NL | Local non-Gaussianity | zeta = zeta_G + (3/5) f_NL zeta_G^2 |
| Extraction | f_NL from squeezed B_zeta | f_NL = (5/12) B/(P P) in squeezed limit |

**These conventions are LOCKED. Every subsequent file in this program uses them.**
