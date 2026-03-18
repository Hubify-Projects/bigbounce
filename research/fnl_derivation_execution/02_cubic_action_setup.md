# 02: Cubic Action / Interaction Hamiltonian Setup

---

## Starting Point: Maldacena (2003) Third-Order Action

For a canonical scalar field (c_s = 1) in comoving gauge (zeta is the dynamical variable), the full cubic action is (Maldacena astro-ph/0210603, Eq. 17-19):

$$
S_3 = M_{\rm Pl}^2 \int d\eta\, d^3x\; \bigg[ a^2 \epsilon^2 \zeta \zeta'^2 + a^2 \epsilon^2 \zeta (\partial\zeta)^2 - 2a^2\epsilon\, \zeta'(\partial_i\zeta)(\partial_i\chi) $$
$$+ \frac{a^2\epsilon}{2}\frac{d}{d\eta}\!\left(\frac{\epsilon}{\mathcal{H}}\right)\zeta^2\zeta' + \frac{\epsilon}{2}\partial^2\zeta(\partial\chi)^2 + \frac{\epsilon}{4}\frac{d}{d\eta}\!\left(\frac{\epsilon}{\mathcal{H}}\right)\partial^2\zeta\,\chi^2 + 2f(\zeta)\frac{\delta L}{\delta\zeta}\bigg|_1\bigg]
$$

where chi satisfies the constraint nabla^2 chi = a^2 epsilon zeta', and the last term vanishes on the linear equations of motion (can be removed by field redefinition).

---

## Specialization to Matter Contraction: epsilon = 3/2, constant

### What simplifies:

1. **epsilon is constant:** d(epsilon)/d eta = 0. Therefore:

$$
\frac{d}{d\eta}\!\left(\frac{\epsilon}{\mathcal{H}}\right) = \epsilon \frac{d}{d\eta}\!\left(\frac{1}{\mathcal{H}}\right) = \epsilon\left(-\frac{\mathcal{H}'}{\mathcal{H}^2}\right)
$$

With H = 2/eta: H' = -2/eta^2, so H'/H^2 = -2/(eta^2) / (4/eta^2) = -1/2.

$$
\frac{d}{d\eta}\!\left(\frac{\epsilon}{\mathcal{H}}\right) = \frac{3}{2}\cdot\frac{1}{2} = \frac{3}{4}
$$

Wait — this is a constant! Let me recheck. epsilon/H = (3/2)/(2/eta) = 3 eta/4.

$$
\frac{d}{d\eta}\!\left(\frac{3\eta}{4}\right) = \frac{3}{4}
$$

Yes: d/d eta (epsilon/H) = 3/4. This is a NONZERO CONSTANT.

2. **Numerical coefficients:** epsilon = 3/2, epsilon^2 = 9/4.

### The surviving terms:

$$
S_3 = M_{\rm Pl}^2 \int d\eta\, d^3x \bigg[ \frac{9}{4}a^2\zeta\zeta'^2 + \frac{9}{4}a^2\zeta(\partial\zeta)^2 - 3a^2\zeta'(\partial_i\zeta)(\partial_i\chi)
$$
$$
+ \frac{3}{8}a^2\zeta^2\zeta' + \frac{3}{4}\partial^2\zeta(\partial\chi)^2 + \frac{3}{8}\partial^2\zeta\,\chi^2 + \text{field redef}\bigg]
$$

Wait — I need to be more careful about the epsilon factors. Let me redo each term.

### Term by term:

**Term 1:** a^2 epsilon^2 zeta zeta'^2 = (9/4) a^2 zeta zeta'^2

**Term 2:** a^2 epsilon^2 zeta (del zeta)^2 = (9/4) a^2 zeta (del zeta)^2

**Term 3:** -2 a^2 epsilon zeta' (del_i zeta)(del_i chi) = -3 a^2 zeta' (del_i zeta)(del_i chi)

**Term 4:** (a^2 epsilon / 2) d/d eta (epsilon/H) zeta^2 zeta' = (a^2)(3/2)(1/2)(3/4) zeta^2 zeta' = (9/16) a^2 zeta^2 zeta'

Wait — I had the wrong product. The coefficient is:
(a^2)(epsilon/2)(d/d eta (epsilon/H)) = a^2 * (3/4) * (3/4) = (9/16) a^2

Hmm, let me re-examine. The Maldacena term is:

$$
\frac{a^2 \epsilon}{2} \frac{d}{d\eta}\left(\frac{\epsilon}{\mathcal{H}}\right) \zeta^2 \zeta'
$$

= a^2 * (3/2) / 2 * (3/4) * zeta^2 zeta' = a^2 * (3/4) * (3/4) * zeta^2 zeta' = (9/16) a^2 zeta^2 zeta'

**Term 5:** (epsilon/2) del^2 zeta (del chi)^2 = (3/4) del^2 zeta (del chi)^2

**Term 6:** (epsilon/4)(d/d eta(epsilon/H)) del^2 zeta chi^2 = (3/8)(3/4) del^2 zeta chi^2 = (9/32) del^2 zeta chi^2

### The constraint:

$$
\nabla^2 \chi = a^2 \epsilon \zeta' = \frac{3}{2} a^2 \zeta'
$$

In Fourier space: -k^2 chi_k = (3/2) a^2 zeta_k', so chi_k = -(3/2) a^2 zeta_k' / k^2.

---

## The Field Redefinition

Maldacena's field redefinition absorbs the "local" part of the non-Gaussianity into a redefined variable. The standard decomposition:

$$
\zeta = \zeta_n + \frac{\epsilon}{2}\zeta_n^2 + ...
$$

where zeta_n is the "intrinsic" Gaussian variable. This redefinition produces:

$$
S_2[\zeta] = S_2[\zeta_n] + \text{terms that look like } S_3
$$

The net effect: the cubic action splits into

$$
S_3^{\rm total} = S_3^{\rm intrinsic} + S_3^{\rm field\;redef}
$$

The field-redefinition piece gives a LOCAL contribution to the bispectrum:

$$
f_{\rm NL}^{\rm field\;redef} = \frac{5}{6}\epsilon = \frac{5}{6}\cdot\frac{3}{2} = \frac{5}{4}
$$

Wait — for the standard slow-roll result, f_NL = (5/12)(2 epsilon) = 5 epsilon/6. But this uses the relation specific to slow-roll where the Maldacena field redefinition zeta -> zeta + (epsilon/2) zeta^2 generates the full local piece.

For epsilon = 3/2:

$$
f_{\rm NL}^{\rm field\;redef} = \frac{5}{6}\cdot\frac{3}{2} = \frac{5}{4} = 1.25
$$

**This is a KNOWN, EXACT contribution.** The nontrivial part is the INTRINSIC contribution from the time integral.

---

## Which Terms Dominate on Superhorizon Scales?

### Power counting in eta:

On superhorizon scales (|k eta| << 1):
- zeta_k ~ eta^{-3} (growing mode)
- zeta_k' ~ eta^{-4}
- a^2 = a_0^2 eta^4/eta_0^4 ~ eta^4
- chi_k = -(3/2) a^2 zeta_k' / k^2 ~ eta^4 * eta^{-4} / k^2 ~ k^{-2} (constant!)
- del_i zeta ~ k * zeta ~ k * eta^{-3}

**Term 1 (zeta zeta'^2):** a^2 * zeta * zeta'^2 ~ eta^4 * eta^{-3} * eta^{-8} = eta^{-7}

**Term 2 (zeta (del zeta)^2):** a^2 * zeta * k^2 * zeta^2 ~ eta^4 * eta^{-3} * k^2 * eta^{-6} = k^2 eta^{-5}

On superhorizon scales, k^2 eta^2 << 1, so Term 2 ~ k^2 eta^{-5} is SUBLEADING compared to Term 1 ~ eta^{-7} by a factor of k^2 eta^2.

**Term 3 (zeta' del zeta del chi):** a^2 * zeta' * k * zeta * k * chi ~ eta^4 * eta^{-4} * k * eta^{-3} * k * k^{-2} = eta^{-3}

This is SUBLEADING compared to Term 1 by eta^4.

**Term 4 (zeta^2 zeta'):** a^2 * zeta^2 * zeta' ~ eta^4 * eta^{-6} * eta^{-4} = eta^{-6}

This is SUBLEADING compared to Term 1 by eta.

### Hierarchy (superhorizon, eta -> 0):

$$
\text{Term 1} \sim \eta^{-7} \gg \text{Term 4} \sim \eta^{-6} \gg \text{Term 2} \sim k^2\eta^{-5} \gg \text{Term 3} \sim \eta^{-3}
$$

**Term 1 (epsilon^2 a^2 zeta zeta'^2) DOMINATES the superhorizon bispectrum.**

---

## The Dominant Interaction Hamiltonian

Keeping only the dominant term:

$$
\mathcal{H}_3^{\rm dom} = -\mathcal{L}_3^{\rm dom} = -\frac{9}{4}M_{\rm Pl}^2 a^2 \zeta \zeta'^2
$$

In Fourier space:

$$
H_3(\eta) = -\frac{9}{4}M_{\rm Pl}^2 \int \frac{d^3k_1 d^3k_2 d^3k_3}{(2\pi)^9}\,(2\pi)^3\delta^3(\mathbf{k}_{123})\; a^2(\eta)\; \zeta_{k_1}(\eta)\; \zeta'_{k_2}(\eta)\; \zeta'_{k_3}(\eta) + \text{perms}
$$

The permutations give a factor of 3 (choosing which leg is the "zeta" vs the "zeta'" pair).

### Subleading corrections:

Term 4 contributes at relative order eta/eta_f ~ (next power of growing mode). For the squeezed-limit f_NL, which is dominated by the growing mode, Term 4 is a correction of order |k_1 eta_f| or a constant, depending on the exact structure. We will verify whether it contributes a finite piece to f_NL after completing the dominant integral.

---

## The In-In Master Formula

$$
\langle \zeta_{\mathbf{k}_1}(\eta_f)\zeta_{\mathbf{k}_2}(\eta_f)\zeta_{\mathbf{k}_3}(\eta_f)\rangle = -i\int_{-\infty(1-i\epsilon)}^{\eta_f} d\eta'\, \langle 0|[\zeta_{\mathbf{k}_1}(\eta_f)\zeta_{\mathbf{k}_2}(\eta_f)\zeta_{\mathbf{k}_3}(\eta_f),\, H_3(\eta')]|0\rangle + \text{c.c.}
$$

The Wick contraction for the dominant vertex (schematically, suppressing momentum labels):

$$
B_\zeta(k_1,k_2,k_3) = -i \cdot \frac{9}{4} M_{\rm Pl}^2 \cdot 2 \int_{-\infty}^{\eta_f} d\eta'\, a^2(\eta') \times
$$
$$
\bigg[\zeta_{k_1}^*(\eta_f)\zeta_{k_2}^*(\eta_f)\zeta_{k_3}^*(\eta_f) \cdot \zeta_{k_1}(\eta')\zeta'_{k_2}(\eta')\zeta'_{k_3}(\eta') + \text{2 perms over which leg is undifferentiated}\bigg] + \text{c.c.}
$$

The factor of 2 out front comes from: the commutator produces one term where the mode functions in the vertex are "unstarred" and the external legs are "starred" (and c.c. gives the other).

### Notation:

Define the mode function:

$$
\zeta_k(\eta) = \frac{e^{-ik\eta}}{A\sqrt{2k}\,\eta^2}\left(1 - \frac{i}{k\eta}\right) \equiv \frac{f_k(\eta)}{A}
$$

where f_k(eta) = e^{-ik eta}/(sqrt(2k) eta^2) * (1 - i/(k eta)).

Then:

$$
B = \frac{-2i \cdot (9/4) M_{\rm Pl}^2}{A^6} \int_{-\infty}^{\eta_f} d\eta'\, a^2(\eta') \left[f_{k_1}^*(\eta_f) f_{k_2}^*(\eta_f) f_{k_3}^*(\eta_f)\right] \left[f_{k_1}(\eta') f'_{k_2}(\eta') f'_{k_3}(\eta')\right]
$$
$$
+ \text{perms} + \text{c.c.}
$$

### The key relation: A and M_Pl

From z = a sqrt(2 epsilon) = a sqrt(3), and the second-order action:

$$
S_2 = \frac{1}{2}\int d\eta\, d^3x\, z^2 [\zeta'^2 - (\partial\zeta)^2] = M_{\rm Pl}^2 \int d\eta\, d^3x\, \frac{a^2 \epsilon}{1} [\zeta'^2 - (\partial\zeta)^2]
$$

Wait — the Mukhanov variable is v = z zeta with z^2 = 2 a^2 epsilon M_Pl^2. So z = a sqrt(2 epsilon) M_Pl = a sqrt(3) M_Pl.

I had dropped M_Pl from z. Let me correct: z = a sqrt(3) M_Pl, so A = a_0 sqrt(3) M_Pl / eta_0^2.

Then P(k) = 1/(2k^3 A^2 eta^6) = eta_0^4 / (6 k^3 a_0^2 M_Pl^2 eta^6).

And the cubic action coefficient (9/4) M_Pl^2 / A^6 becomes:

$$
\frac{(9/4) M_{\rm Pl}^2}{A^6} = \frac{(9/4) M_{\rm Pl}^2}{(a_0 \sqrt{3} M_{\rm Pl}/\eta_0^2)^6} = \frac{(9/4) M_{\rm Pl}^2 \eta_0^{12}}{27 a_0^6 M_{\rm Pl}^6} = \frac{\eta_0^{12}}{12 a_0^6 M_{\rm Pl}^4}
$$

**But this M_Pl dependence will cancel in f_NL = (5/12) B / (P P):**

P(k)^2 ~ 1/(A^4 k^6 eta^{12}) ~ M_Pl^{-4} ...

So the ratio B/P^2 will be independent of M_Pl and a_0. Good — f_NL is a pure number, as expected.

---

## The Integral to Evaluate (Next File)

The bispectrum from the dominant vertex is:

$$
B_\zeta(k_1,k_2,k_3) = \frac{(9/2)}{A^4} \cdot \text{Re}\left[-i \int_{-\infty}^{\eta_f} d\eta'\, a^2(\eta')\, \mathcal{F}(k_1,k_2,k_3;\eta_f,\eta')\right]
$$

Wait — I need to track the factors more carefully. Let me define the dimensionless integral and postpone the full evaluation to file 03.

The quantity that enters f_NL is:

$$
f_{\rm NL}^{\rm intrinsic} = \frac{5}{12}\frac{B^{\rm intrinsic}}{P(k_1)P(k)} - f_{\rm NL}^{\rm field\;redef}
$$

No — f_NL^total = f_NL^intrinsic + f_NL^field redef. The total bispectrum is B^intrinsic + B^field redef.

$$
f_{\rm NL}^{\rm total} = \frac{5}{12}\frac{B^{\rm total}}{P(k_1)P(k)} = f_{\rm NL}^{\rm intrinsic} + \frac{5}{4}
$$

The field-redefinition piece (5/4 = 1.25) is already determined. The intrinsic piece requires evaluating the time integral, which is done in file 03.

---

## Summary: What Goes Into File 03

1. The dominant vertex: (9/4) M_Pl^2 a^2 epsilon^2 zeta zeta'^2 with permutations
2. The mode functions: zeta_k(eta) and zeta_k'(eta) from file 01
3. The in-in integral: -i integral from -infty to eta_f of a^2(eta') * [products of mode functions]
4. The squeezed limit: k_1 -> 0, k_2 = k_3 = k
5. Extraction: f_NL = (5/12) B/(P*P) in the squeezed limit
6. The field redefinition contribution: 5/4, to be added to the intrinsic result

**The subleading terms (Terms 2-6) will be estimated after the dominant integral is completed.**
