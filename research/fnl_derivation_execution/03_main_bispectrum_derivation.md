# 03: Main Bispectrum Derivation

---

## Setup

From file 02, the dominant contribution to the bispectrum comes from the vertex:

$$
\mathcal{L}_3^{\rm dom} = \frac{9}{4} M_{\rm Pl}^2\, a^2\, \zeta\, \zeta'^2
$$

The in-in formula:

$$
B_\zeta(k_1,k_2,k_3) = \frac{9}{2} M_{\rm Pl}^2 \sum_{\rm 3\,perms}\, \text{Re}\left[-i\int_{-\infty}^{\eta_f}d\eta'\, a^2(\eta')\, \zeta_{k_1}^*(\eta_f)\zeta_{k_2}^*(\eta_f)\zeta_{k_3}^*(\eta_f)\, \zeta_{k_1}(\eta')\zeta'_{k_2}(\eta')\zeta'_{k_3}(\eta')\right]
$$

The sum is over the 3 permutations of which momentum carries the undifferentiated zeta.

The overall factor: the commutator in the in-in formula gives a factor of 2 (from [,] = forward - backward), and the vertex factor is (9/4) M_Pl^2 with the volume integral producing the delta function. I group these as (9/2) M_Pl^2.

---

## Mode Functions (from file 01)

$$
\zeta_k(\eta) = \frac{e^{-ik\eta}}{A\sqrt{2k}\,\eta^2}\left(1 - \frac{i}{k\eta}\right)
$$

where A = a_0 sqrt(3) M_Pl / eta_0^2, and a^2(eta) = a_0^2 eta^4/eta_0^4.

Define the stripped mode function (absorbing A):

$$
g_k(\eta) \equiv A\,\zeta_k(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}\,\eta^2}\left(1 - \frac{i}{k\eta}\right)
$$

Then zeta_k = g_k / A, and:

$$
B = \frac{9}{2}\frac{M_{\rm Pl}^2\, a_0^2/\eta_0^4}{A^6}\sum_{\rm perms}\text{Re}\left[-i\int_{-\infty}^{\eta_f}d\eta'\,\eta'^4\, g_{k_1}^*(\eta_f)g_{k_2}^*(\eta_f)g_{k_3}^*(\eta_f)\, g_{k_1}(\eta')g'_{k_2}(\eta')g'_{k_3}(\eta')\right]
$$

### Simplify the prefactor:

A^6 = (a_0 sqrt(3) M_Pl / eta_0^2)^6 = 27 a_0^6 M_Pl^6 / eta_0^{12}

So:

$$
\frac{M_{\rm Pl}^2\, a_0^2/\eta_0^4}{A^6} = \frac{M_{\rm Pl}^2\, a_0^2\,\eta_0^{12}}{27\, a_0^6\, M_{\rm Pl}^6\,\eta_0^4} = \frac{\eta_0^8}{27\, a_0^4\, M_{\rm Pl}^4}
$$

And the power spectrum:

$$
P(k) = \frac{|g_k|^2}{A^2} \quad\Rightarrow\quad P^{\rm super}(k) = \frac{1}{2k^3 A^2 \eta^6}
$$

$$
P(k_1)P(k_2) = \frac{1}{4 k_1^3 k_2^3 A^4 \eta_f^{12}}
$$

So:

$$
\frac{B}{P(k_1)P(k)} = \frac{B \cdot 4k_1^3 k^3 A^4 \eta_f^{12}}{1}
$$

The A^4 from P^2 partially cancels the A^{-6} from B, leaving A^{-2} factors. But ultimately, f_NL must be independent of A, a_0, eta_0, eta_f. Let me work with a cleaner approach.

---

## Clean Approach: Work With Dimensionless Ratio Directly

Define:

$$
\mathcal{I}(k_1,k_2,k_3) \equiv \text{Re}\left[-i\int_{-\infty}^{\eta_f}d\eta'\,\eta'^4\, g_{k_1}(\eta')g'_{k_2}(\eta')g'_{k_3}(\eta')\right]
$$

Then:

$$
B = \frac{9}{2}\frac{M_{\rm Pl}^2\, a_0^2/\eta_0^4}{A^6}\left[g_{k_1}^*(\eta_f)g_{k_2}^*(\eta_f)g_{k_3}^*(\eta_f)\right]\left[\mathcal{I}_{123} + \mathcal{I}_{213} + \mathcal{I}_{312}\right] + \text{c.c.}
$$

where I_123 means k_1 is undifferentiated, k_2 and k_3 are differentiated.

And:

$$
\frac{B}{P(k_1)P(k)} = \frac{9}{2}\frac{M_{\rm Pl}^2 a_0^2/\eta_0^4}{A^6} \cdot \frac{[\text{external}][\text{integral}] + \text{c.c.}}{|g_{k_1}(\eta_f)|^2 |g_k(\eta_f)|^2 / A^4}
$$

$$
= \frac{9}{2}\frac{M_{\rm Pl}^2 a_0^2 A^4}{A^6 \eta_0^4} \cdot \frac{[\text{external}][\text{integral}] + \text{c.c.}}{|g_{k_1}|^2 |g_k|^2}
$$

$$
= \frac{9}{2}\frac{M_{\rm Pl}^2 a_0^2}{A^2 \eta_0^4} \cdot \frac{[\text{external}][\text{integral}] + \text{c.c.}}{|g_{k_1}|^2 |g_k|^2}
$$

A^2 = 3 a_0^2 M_Pl^2 / eta_0^4, so:

$$
\frac{M_{\rm Pl}^2 a_0^2}{A^2 \eta_0^4} = \frac{M_{\rm Pl}^2 a_0^2 \eta_0^4}{3 a_0^2 M_{\rm Pl}^2 \eta_0^4} = \frac{1}{3}
$$

Therefore:

$$
\frac{B}{P(k_1)P(k)} = \frac{9}{2}\cdot\frac{1}{3}\cdot\frac{g_{k_1}^* g_{k_2}^* g_{k_3}^* \cdot [\mathcal{I}_{123}+\mathcal{I}_{213}+\mathcal{I}_{312}] + \text{c.c.}}{|g_{k_1}|^2|g_k|^2}
$$

$$
= \frac{3}{2}\cdot\frac{g_{k_1}^* g_{k_2}^* g_{k_3}^* \cdot \sum\mathcal{I} + \text{c.c.}}{|g_{k_1}|^2|g_k|^2}
$$

And:

$$
\boxed{f_{\rm NL}^{\rm intrinsic} = \frac{5}{12}\cdot\frac{3}{2}\cdot\frac{g_{k_1}^* g_{k_2}^* g_{k_3}^* \cdot \sum\mathcal{I} + \text{c.c.}}{|g_{k_1}|^2|g_k|^2} = \frac{5}{8}\cdot\frac{g_{k_1}^* g_{k_2}^* g_{k_3}^* \cdot \sum\mathcal{I} + \text{c.c.}}{|g_{k_1}|^2|g_k|^2}}
$$

**This is the master formula.** All a_0, eta_0, M_Pl dependence has cancelled. f_NL^intrinsic is determined entirely by the dimensionless mode functions g_k and the integral I.

---

## Evaluating the Integral in the Squeezed Limit

### Squeezed limit: k_1 -> 0, k_2 = k_3 = k

In this limit, the long mode k_1 is always superhorizon throughout the relevant integration range. The short modes k_2 = k_3 = k cross the horizon at |k eta| ~ 1.

### The long-mode approximation:

For k_1 -> 0:

$$
g_{k_1}(\eta') \approx \frac{(-i)}{k_1\sqrt{2k_1}\,\eta'^3} = \frac{-i}{\sqrt{2k_1^3}\,\eta'^3}
$$

$$
g_{k_1}^*(\eta_f) \approx \frac{i}{\sqrt{2k_1^3}\,\eta_f^3}
$$

### The short-mode functions (exact):

$$
g_k(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}\,\eta^2}\left(1-\frac{i}{k\eta}\right)
$$

$$
g_k'(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}\,\eta^2}\left[-ik - \frac{3}{\eta} + \frac{3i}{k\eta^2}\right]
$$

(derived in file 01)

### The dominant integral in the squeezed limit:

For I_123 (k_1 undifferentiated, k_2, k_3 differentiated):

$$
\mathcal{I}_{123} = \text{Re}\left[-i\int_{-\infty}^{\eta_f}d\eta'\,\eta'^4\, g_{k_1}(\eta')\, g'_k(\eta')\, g'_k(\eta')\right]
$$

Using the long-mode approximation:

$$
= \text{Re}\left[-i\int_{-\infty}^{\eta_f}d\eta'\,\eta'^4\cdot\frac{-i}{\sqrt{2k_1^3}\eta'^3}\cdot [g'_k(\eta')]^2\right]
$$

$$
= \text{Re}\left[-\frac{1}{\sqrt{2k_1^3}}\int_{-\infty}^{\eta_f}d\eta'\,\eta'\,[g'_k(\eta')]^2\right]
$$

### Computing [g_k'(eta)]^2:

$$
g_k'(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}\,\eta^2}\left[-ik-\frac{3}{\eta}+\frac{3i}{k\eta^2}\right]
$$

$$
[g'_k(\eta)]^2 = \frac{e^{-2ik\eta}}{2k\,\eta^4}\left[-ik-\frac{3}{\eta}+\frac{3i}{k\eta^2}\right]^2
$$

Let me define x = k eta (where x < 0 and x -> 0^- at late times):

$$
[g'_k]^2 = \frac{k^3 e^{-2ix}}{2k\,x^4/k^4}\cdot\frac{1}{k^2}\left[-ix-3+\frac{3i}{x}\right]^2\cdot\frac{1}{k^2\eta^4}
$$

Actually, let me substitute x = k eta directly. Write eta = x/k, d eta = dx/k. Then:

$$
g'_k = \frac{k^2 e^{-ix}}{\sqrt{2k}\, x^2}\left[-ix - 3 + \frac{3i}{x}\right] \cdot \frac{1}{k}
$$

Wait, let me be more careful:

$$
g'_k(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}\,\eta^2}\left[-ik-\frac{3}{\eta}+\frac{3i}{k\eta^2}\right]
$$

With eta = x/k:

$$
= \frac{k^2 e^{-ix}}{\sqrt{2k}\, x^2}\left[-ik - \frac{3k}{x} + \frac{3ik^2}{kx^2}\right] = \frac{k^2 e^{-ix}}{\sqrt{2k}\, x^2}\left[-ik - \frac{3k}{x} + \frac{3ik}{x^2}\right]
$$

$$
= \frac{k^3 e^{-ix}}{\sqrt{2k}\, x^2}\left[-i - \frac{3}{x} + \frac{3i}{x^2}\right]
$$

So:

$$
[g'_k]^2 = \frac{k^6 e^{-2ix}}{2k\, x^4}\left[-i - \frac{3}{x} + \frac{3i}{x^2}\right]^2 = \frac{k^5 e^{-2ix}}{2\, x^4}\left[-i - \frac{3}{x} + \frac{3i}{x^2}\right]^2
$$

The integral becomes (with eta' = x/k, d eta' = dx/k):

$$
\mathcal{I}_{123} = \text{Re}\left[-\frac{1}{\sqrt{2k_1^3}}\int_{-\infty}^{x_f} \frac{dx}{k}\cdot\frac{x}{k}\cdot\frac{k^5 e^{-2ix}}{2x^4}\left(-i-\frac{3}{x}+\frac{3i}{x^2}\right)^2\right]
$$

$$
= \text{Re}\left[-\frac{k^3}{2\sqrt{2k_1^3}}\int_{-\infty}^{x_f} \frac{dx}{x^3}\, e^{-2ix}\left(-i-\frac{3}{x}+\frac{3i}{x^2}\right)^2\right]
$$

### Expanding the square:

$$
\left(-i-\frac{3}{x}+\frac{3i}{x^2}\right)^2 = -1 + \frac{6i}{x} + \frac{9}{x^2} + \frac{6i}{x^2} - \frac{18i}{x^3} - \frac{9}{x^4}
$$

Wait, let me expand carefully. Let u = -i - 3/x + 3i/x^2.

u^2 = (-i)^2 + (-3/x)^2 + (3i/x^2)^2 + 2(-i)(-3/x) + 2(-i)(3i/x^2) + 2(-3/x)(3i/x^2)

= -1 + 9/x^2 - 9/x^4 + 6i/x + 6/x^2 - 18i/x^3

= -1 + 6i/x + 15/x^2 - 18i/x^3 - 9/x^4

So the integrand is:

$$
\frac{e^{-2ix}}{x^3}\left(-1 + \frac{6i}{x} + \frac{15}{x^2} - \frac{18i}{x^3} - \frac{9}{x^4}\right)
$$

$$
= e^{-2ix}\left(-\frac{1}{x^3} + \frac{6i}{x^4} + \frac{15}{x^5} - \frac{18i}{x^6} - \frac{9}{x^7}\right)
$$

### The integral:

$$
J \equiv \int_{-\infty}^{x_f} dx\, e^{-2ix}\left(-\frac{1}{x^3} + \frac{6i}{x^4} + \frac{15}{x^5} - \frac{18i}{x^6} - \frac{9}{x^7}\right)
$$

This integral is dominated by the LATE-TIME behavior (x -> 0^-) because of the growing mode. As x_f -> 0^-, the powers 1/x^n diverge.

### Late-time (superhorizon) dominance:

Near x = 0, e^{-2ix} -> 1. The most divergent term is -9/x^7.

$$
\int^{x_f} dx\, \frac{-9}{x^7} = \frac{9}{6 x_f^6} = \frac{3}{2x_f^6}
$$

Similarly, the -18i/x^6 term gives:

$$
\int^{x_f} dx\, \frac{-18i}{x^6} = \frac{18i}{5 x_f^5}
$$

And 15/x^5:

$$
\int^{x_f} dx\, \frac{15}{x^5} = \frac{-15}{4x_f^4}
$$

The leading (most divergent) contribution to J is:

$$
J \approx \frac{3}{2x_f^6} + \frac{18i}{5x_f^5} - \frac{15}{4x_f^4} + ...
$$

### Assembling the intrinsic bispectrum:

$$
\mathcal{I}_{123} = \text{Re}\left[-\frac{k^3}{2\sqrt{2k_1^3}} J\right] = -\frac{k^3}{2\sqrt{2k_1^3}}\text{Re}[J]
$$

Since J is dominated by the real part 3/(2 x_f^6):

$$
\mathcal{I}_{123} \approx -\frac{k^3}{2\sqrt{2k_1^3}} \cdot \frac{3}{2x_f^6} = -\frac{3k^3}{4\sqrt{2k_1^3}\, x_f^6}
$$

With x_f = k eta_f:

$$
\mathcal{I}_{123} \approx -\frac{3k^3}{4\sqrt{2k_1^3}\, k^6\eta_f^6} = -\frac{3}{4\sqrt{2k_1^3}\, k^3\eta_f^6}
$$

### The other permutations in the squeezed limit:

I_213 has k_2 undifferentiated, k_1 and k_3 = k differentiated. But k_1 -> 0, so zeta'_{k_1} ~ k_1 * (something). This permutation is suppressed by k_1/k relative to I_123.

I_312 has k_3 undifferentiated, k_1 and k_2 differentiated. Same suppression.

In the squeezed limit, the DOMINANT permutation is I_123 (long mode undifferentiated) plus I_132 (equivalent by k_2 <-> k_3 symmetry, giving a factor of 2 for the symmetric case k_2 = k_3).

Wait — for the vertex zeta zeta'^2, the 3 permutations are:
- (1) k_1 undiff, k_2 k_3 diff
- (2) k_2 undiff, k_1 k_3 diff
- (3) k_3 undiff, k_1 k_2 diff

In the squeezed limit k_1 -> 0:
- (1) gives the dominant contribution (long mode modulates short modes)
- (2) and (3): k_2 or k_3 = k is undiff, while k_1 ~ 0 is diff. zeta'_{k_1} ~ k_1 * ..., suppressed.

But (2) and (3) also have a contribution where the SHORT mode that is undifferentiated couples to the OTHER short mode and the long mode, both differentiated. The long mode zeta'_{k_1} goes as 3i g_{k_1}/(eta^4 k_1 eta) ~ ... this needs checking.

Actually for k_1 -> 0: g'_{k_1}(eta) ~ g_{k_1}(eta) * (-3/eta), since the -ik term is subleading. So:

$$
g'_{k_1} \approx \frac{-i}{\sqrt{2k_1^3}\eta'^3} \cdot \frac{-3}{\eta'} = \frac{3i}{\sqrt{2k_1^3}\eta'^4}
$$

This is (3/eta') times g_{k_1}. So permutations (2) and (3) have an extra factor of (3/eta') relative to having g_{k_1} undifferentiated — and they also miss one factor of g'_k (replaced by g_k). Since g'_k ~ (-3/eta) g_k on superhorizon scales, the permutations (2) and (3) contribute at the SAME ORDER as (1).

**This is important.** Let me compute all three permutations properly.

### All three permutations in the superhorizon limit:

On superhorizon scales (all |k_i eta| << 1):

$$
g_k^{\rm super}(\eta) = \frac{-i}{\sqrt{2k^3}\eta^3}, \quad g_k'^{\rm super}(\eta) = \frac{3i}{\sqrt{2k^3}\eta^4}
$$

So g'_k = (-3/eta) g_k on superhorizon scales.

**Permutation (1):** k_1 undiff, k_2 k_3 diff

$$
g_{k_1} g'_{k_2} g'_{k_3} = g_{k_1} \cdot \frac{-3}{\eta} g_{k_2} \cdot \frac{-3}{\eta} g_{k_3} = \frac{9}{\eta^2} g_{k_1} g_{k_2} g_{k_3}
$$

**Permutation (2):** k_2 undiff, k_1 k_3 diff

$$
g_{k_2} g'_{k_1} g'_{k_3} = g_{k_2} \cdot \frac{-3}{\eta} g_{k_1} \cdot \frac{-3}{\eta} g_{k_3} = \frac{9}{\eta^2} g_{k_1} g_{k_2} g_{k_3}
$$

**Permutation (3):** k_3 undiff, k_1 k_2 diff

$$
= \frac{9}{\eta^2} g_{k_1} g_{k_2} g_{k_3}
$$

**ALL THREE PERMUTATIONS GIVE THE SAME RESULT on superhorizon scales.**

The sum of permutations = 3 * (9/eta^2) g_{k_1} g_{k_2} g_{k_3} = (27/eta^2) g_{k_1} g_{k_2} g_{k_3}.

### The total integral (superhorizon approximation):

$$
\sum \mathcal{I} = \text{Re}\left[-i\int_{-\infty}^{\eta_f}d\eta'\,\eta'^4\cdot\frac{27}{\eta'^2}\cdot g_{k_1}(\eta')g_{k_2}(\eta')g_{k_3}(\eta')\right]
$$

Using the superhorizon form g_{k_i} = -i/sqrt(2k_i^3)/eta^3:

$$
g_{k_1} g_{k_2} g_{k_3} = \frac{(-i)^3}{\sqrt{8 k_1^3 k_2^3 k_3^3}\,\eta'^9} = \frac{i}{\sqrt{8 k_1^3 k_2^3 k_3^3}\,\eta'^9}
$$

So:

$$
\sum\mathcal{I} = \text{Re}\left[-i\int d\eta'\,\eta'^2\cdot 27\cdot\frac{i}{\sqrt{8k_1^3k_2^3k_3^3}\,\eta'^9}\right]
$$

$$
= \text{Re}\left[\frac{27}{\sqrt{8k_1^3k_2^3k_3^3}}\int_{-\infty}^{\eta_f}\frac{d\eta'}{\eta'^7}\right]
$$

The integral:

$$
\int_{-\infty}^{\eta_f}\frac{d\eta'}{\eta'^7}
$$

For eta' < 0, write eta' = -|eta'|:

$$
\int_{\infty}^{|\eta_f|}\frac{-d|\eta'|}{(-|\eta'|)^7} = \int_{\infty}^{|\eta_f|}\frac{d|\eta'|}{|\eta'|^7} = -\int_{|\eta_f|}^{\infty}\frac{d|\eta'|}{|\eta'|^7}
$$

Hmm, I need to be careful with signs. eta < 0, so eta^7 = -|eta|^7. Let me substitute eta = -s, s > 0:

$$
\int_{-\infty}^{\eta_f}\frac{d\eta}{\eta^7} = \int_{\infty}^{s_f}\frac{-ds}{(-s)^7} = \int_{\infty}^{s_f}\frac{ds}{s^7} = -\frac{1}{6s^6}\bigg|_{\infty}^{s_f} = -\frac{1}{6s_f^6} = -\frac{1}{6|\eta_f|^6}
$$

Since eta_f < 0, eta_f^6 = |eta_f|^6. So:

$$
\int_{-\infty}^{\eta_f}\frac{d\eta'}{\eta'^7} = -\frac{1}{6\eta_f^6}
$$

Wait — I need to be more careful. For eta < 0: eta^7 < 0 (odd power). So 1/eta^7 < 0 for eta < 0.

$$
\int_{-\infty}^{\eta_f}\frac{d\eta}{\eta^7}
$$

Substituting eta = -s, d eta = -ds, limits s: infinity -> |eta_f|:

$$
= \int_{\infty}^{|\eta_f|}\frac{-ds}{(-s)^7} = \int_{\infty}^{|\eta_f|}\frac{-ds}{-s^7} = \int_{\infty}^{|\eta_f|}\frac{ds}{s^7} = \left[-\frac{1}{6s^6}\right]_{\infty}^{|\eta_f|} = -\frac{1}{6|\eta_f|^6} - 0 = -\frac{1}{6|\eta_f|^6}
$$

Since eta_f < 0: |eta_f|^6 = eta_f^6. So:

$$
\int_{-\infty}^{\eta_f}\frac{d\eta'}{\eta'^7} = -\frac{1}{6\eta_f^6}
$$

Therefore:

$$
\sum\mathcal{I} = \text{Re}\left[\frac{27}{\sqrt{8k_1^3k_2^3k_3^3}}\cdot\left(-\frac{1}{6\eta_f^6}\right)\right] = -\frac{27}{6\sqrt{8k_1^3k_2^3k_3^3}\,\eta_f^6}
$$

$$
= -\frac{9}{2\sqrt{8k_1^3k_2^3k_3^3}\,\eta_f^6} = -\frac{9}{4\sqrt{2k_1^3k_2^3k_3^3}\,\eta_f^6}
$$

(This is real, so Re[...] = itself.)

---

## Assembling f_NL^intrinsic

From the master formula:

$$
f_{\rm NL}^{\rm intrinsic} = \frac{5}{8}\cdot\frac{g_{k_1}^* g_{k_2}^* g_{k_3}^* \cdot \sum\mathcal{I} + \text{c.c.}}{|g_{k_1}|^2|g_k|^2}
$$

In the squeezed limit with k_2 = k_3 = k:

External modes on superhorizon scales:

$$
g_{k_1}^*(\eta_f) = \frac{i}{\sqrt{2k_1^3}\,\eta_f^3}, \quad g_k^*(\eta_f) = \frac{i}{\sqrt{2k^3}\,\eta_f^3}
$$

$$
g_{k_1}^* g_k^* g_k^* = \frac{i^3}{\sqrt{8k_1^3k^6}\,\eta_f^9} = \frac{-i}{\sqrt{8k_1^3k^6}\,\eta_f^9}
$$

And:

$$
g_{k_1}^* g_k^* g_k^* \cdot \sum\mathcal{I} = \frac{-i}{\sqrt{8k_1^3k^6}\,\eta_f^9} \cdot \frac{-9}{4\sqrt{2k_1^3k^6}\,\eta_f^6}
$$

$$
= \frac{9i}{4\sqrt{16\,k_1^6\,k^{12}}\,\eta_f^{15}} = \frac{9i}{16\,k_1^3 k^6\,\eta_f^{15}}
$$

Adding c.c.: 9i/(16...) + (-9i)/(16...) = 0???

**PROBLEM: The product is purely imaginary, so real part + c.c. = 0.**

This means the superhorizon-only approximation gives ZERO for the bispectrum. The leading contribution must come from the TRANSITION REGION where the short modes cross the horizon.

---

## Resolution: The Transition Region Dominates

The superhorizon-only approximation fails because the product g* g* g* * I is imaginary (the phases conspire). This is analogous to the standard in-in result where the bispectrum is generated at horizon crossing, not after.

**The correct procedure:** do NOT approximate the short-mode functions in the integral. Use the EXACT mode functions for k_2, k_3, and take k_1 -> 0 only.

### Redo with exact short modes:

In the squeezed limit, only the long mode is superhorizon throughout. The integral involves:

$$
\mathcal{I}_{123}^{\rm exact} = \int_{-\infty}^{\eta_f} d\eta'\,\eta'^4\, g_{k_1}^{\rm super}(\eta')\, [g'_k(\eta')]^2
$$

$$
= \int_{-\infty}^{\eta_f} d\eta'\,\eta'^4 \cdot \frac{-i}{\sqrt{2k_1^3}\eta'^3}\cdot [g'_k(\eta')]^2
$$

$$
= \frac{-i}{\sqrt{2k_1^3}}\int_{-\infty}^{\eta_f} d\eta'\,\eta'\,[g'_k(\eta')]^2
$$

Now [g'_k]^2 contains e^{-2ik eta'}, which oscillates on subhorizon scales and damps the early-time contribution. The integral is dominated by the transition region |k eta'| ~ 1.

### Change variable to x = k eta' (x < 0):

$$
\mathcal{I}_{123}^{\rm exact} = \frac{-i}{\sqrt{2k_1^3}} \int_{-\infty}^{x_f}\frac{dx}{k}\cdot\frac{x}{k}\cdot\frac{k^5 e^{-2ix}}{2x^4}\left(-i-\frac{3}{x}+\frac{3i}{x^2}\right)^2
$$

$$
= \frac{-ik^3}{2\sqrt{2k_1^3}}\int_{-\infty}^{x_f}\frac{dx}{x^3}\,e^{-2ix}\left(-i-\frac{3}{x}+\frac{3i}{x^2}\right)^2
$$

With the expansion from earlier:

$$
\left(-i-\frac{3}{x}+\frac{3i}{x^2}\right)^2 = -1+\frac{6i}{x}+\frac{15}{x^2}-\frac{18i}{x^3}-\frac{9}{x^4}
$$

$$
\mathcal{I}_{123}^{\rm exact} = \frac{-ik^3}{2\sqrt{2k_1^3}}\int_{-\infty}^{x_f} dx\,e^{-2ix}\left(-\frac{1}{x^3}+\frac{6i}{x^4}+\frac{15}{x^5}-\frac{18i}{x^6}-\frac{9}{x^7}\right)
$$

### Standard technique: Integration by parts / contour methods

These integrals are of the form:

$$
J_n = \int_{-\infty}^{x_f} dx\, \frac{e^{-2ix}}{x^n}
$$

For the in-in formalism with the i*epsilon prescription (eta -> eta(1-i delta) for convergence at early times), these are well-defined.

**At late times (x_f -> 0^-):** each J_n has a power-law divergence ~ x_f^{-(n-1)}/(n-1) plus subdominant terms. These divergences are the growing-mode contributions.

**The key physics:** The imaginary parts of J_n contribute to the REAL part of (-i) * J_n (because -i times i is real). The real parts of J_n contribute to the imaginary part and cancel in + c.c.

$$
\text{Re}[-i J_n] = \text{Im}[J_n]
$$

### Computing Im[J_n]:

Split each J_n into a late-time divergent piece (x ~ 0) and an oscillatory early-time piece.

For x < 0, write x = -|x|. Then e^{-2ix} = e^{2i|x|} = cos(2|x|) + i sin(2|x|).

The imaginary part comes from the sin(2|x|) piece at early times AND the power-law piece at late times.

**However**, for the power-law divergence near x = 0: e^{-2ix} -> 1 as x -> 0. So the divergent part is purely REAL (no imaginary part). The imaginary (oscillatory) contributions come from the finite, horizon-crossing region.

This means: **the late-time (growing mode) divergences cancel in the real part of (-i * integral)**, and the physical bispectrum comes from horizon crossing, just as in inflation.

### But this contradicts the growing-mode dominance!

**Resolution:** The growing-mode divergences in B_zeta do NOT cancel. They appear in the EXTERNAL mode functions g*(eta_f) which contain the dominant eta_f^{-9} factor. The integral itself is dominated by horizon crossing, but when multiplied by the growing external legs, the total B grows as eta_f^{-12} (and P*P grows as eta_f^{-12}), so f_NL is indeed time-independent.

Let me verify this by computing the integral properly.

### The finite integral:

Define the "stripped" integral (removing the divergent part that cancels in f_NL):

$$
\hat{J}_n \equiv \int_{-\infty}^{0^-} dx\, \frac{e^{-2ix}}{x^n}
$$

For x < 0 with the i*epsilon prescription (x -> x + i delta in the exponential), these converge.

**Using the substitution x = -s (s > 0):**

$$
\hat{J}_n = \int_{\infty}^{0}\frac{-ds}{(-s)^n}e^{2is} = (-1)^{n+1}\int_0^{\infty}\frac{ds}{s^n}e^{2is}
$$

For n >= 1, this is related to the incomplete gamma function:

$$
\int_0^{\infty}\frac{ds}{s^n}e^{2is}
$$

This diverges at s = 0 for n >= 1. The divergence is the late-time growing-mode contribution. We regularize by keeping x_f finite (not zero).

**The correct approach: compute the integral at finite x_f < 0 and then take the ratio B/(P*P) at the same eta_f.**

### Computing at finite x_f:

$$
J_n(x_f) = \int_{-\infty}^{x_f}\frac{dx}{x^n}e^{-2ix}
$$

Substituting x = -s, limits s: infinity -> |x_f|:

$$
= (-1)^{n+1}\int_{|x_f|}^{\infty}\frac{ds}{s^n}e^{2is}
$$

### The leading late-time (small |x_f|) behavior:

For small |x_f| (superhorizon evaluation):

$$
J_n(x_f) = (-1)^{n+1}\left[\int_{|x_f|}^{1}\frac{ds}{s^n}(1 + 2is + ...)\;+\;\int_1^{\infty}\frac{ds}{s^n}e^{2is}\right]
$$

The first integral gives:

$$
\int_{|x_f|}^1 \frac{ds}{s^n} = \frac{1}{n-1}\left(\frac{1}{|x_f|^{n-1}} - 1\right) \quad (n > 1)
$$

The dominant piece for small |x_f| is 1/((n-1)|x_f|^{n-1}).

The imaginary correction from the 2is term:

$$
2i\int_{|x_f|}^1\frac{ds}{s^{n-1}} = \frac{2i}{n-2}\left(\frac{1}{|x_f|^{n-2}} - 1\right) \quad (n > 2)
$$

The second integral is a finite complex number (call it C_n).

### Assembling the dominant terms:

$$
J_3 \approx \frac{1}{2|x_f|^2} + \frac{2i}{|x_f|} + C_3 + ...
$$

$$
J_4 \approx -\frac{1}{3|x_f|^3} - \frac{2i}{2|x_f|^2} + ...
$$

$$
J_5 \approx \frac{1}{4|x_f|^4} + \frac{2i}{3|x_f|^3} + ...
$$

$$
J_6 \approx -\frac{1}{5|x_f|^5} - \frac{2i}{4|x_f|^4} + ...
$$

$$
J_7 \approx \frac{1}{6|x_f|^6} + \frac{2i}{5|x_f|^5} + ...
$$

### Now assemble (-i) * (sum of terms):

$$
\mathcal{I}_{123} = \frac{-ik^3}{2\sqrt{2k_1^3}}\left[-J_3 + 6iJ_4 + 15J_5 - 18iJ_6 - 9J_7\right]
$$

Then the bispectrum involves:

$$
g^*_{k_1}(\eta_f)g^*_k(\eta_f)g^*_k(\eta_f)\cdot\mathcal{I}_{123} + \text{c.c.}
$$

The external legs contribute:

$$
g^*_{k_1}g^*_k g^*_k = \frac{i}{\sqrt{2k_1^3}\eta_f^3}\cdot\frac{1}{2k\eta_f^4}\left(1+\frac{i}{k\eta_f}\right)^2\cdot e^{ik\eta_f}\cdot e^{ik\eta_f}
$$

Hmm — wait, I should use the EXACT external mode functions, not just the superhorizon limit, because there may be phase factors that matter.

**On superhorizon scales (|k eta_f| << 1):**

$$
g_k^*(\eta_f) \approx \frac{i}{\sqrt{2k^3}\eta_f^3}
$$

So g*_{k_1} g*_k g*_k = -i / sqrt(8 k_1^3 k^6) / eta_f^9.

The product with I_123:

$$
g^*\cdot\mathcal{I}_{123} = \frac{-i}{\sqrt{8k_1^3k^6}\eta_f^9}\cdot\frac{-ik^3}{2\sqrt{2k_1^3}}[\text{integral}]
$$

$$
= \frac{-k^3}{2\sqrt{16k_1^6k^6}\eta_f^9}[\text{integral}] = \frac{-k^3}{8k_1^3k^3\eta_f^9}[\text{integral}] = \frac{-1}{8k_1^3\eta_f^9}[\text{integral}]
$$

And |g_{k_1}|^2|g_k|^2 = 1/(4k_1^3 k^3 eta_f^{12}) (using superhorizon form).

So:

$$
\frac{g^*\cdot\mathcal{I}_{123}+\text{c.c.}}{|g_{k_1}|^2|g_k|^2} = \frac{2\text{Re}[g^*\cdot\mathcal{I}_{123}]}{1/(4k_1^3k^3\eta_f^{12})} = 8k_1^3k^3\eta_f^{12}\cdot\text{Re}[\text{above}]
$$

$$
= 8k_1^3k^3\eta_f^{12}\cdot\text{Re}\left[\frac{-1}{8k_1^3\eta_f^9}[\text{integral}]\right] = k^3\eta_f^3\cdot\text{Re}[-\text{integral}]
$$

where "integral" = -J_3 + 6i J_4 + 15 J_5 - 18i J_6 - 9 J_7.

### Extracting the eta_f-independent piece:

The integral terms J_n ~ 1/|x_f|^{n-1} = 1/(k|eta_f|)^{n-1} = 1/(k^{n-1}|eta_f|^{n-1}).

The dominant J_7 term: J_7 ~ 1/(6 k^6 |eta_f|^6).

The dominant contribution to "integral":

-9 J_7 ~ -9/(6 k^6 eta_f^6) = -3/(2 k^6 eta_f^6)

(using eta_f < 0 so |eta_f| = -eta_f, and eta_f^6 > 0.)

So Re[-integral] ~ Re[3/(2k^6 eta_f^6)] = 3/(2k^6 eta_f^6).

Then:

$$
\frac{g^*\cdot\mathcal{I}_{123}+\text{c.c.}}{|g|^2|g|^2} \approx k^3\eta_f^3\cdot\frac{3}{2k^6\eta_f^6} = \frac{3}{2k^3\eta_f^3}
$$

**This STILL depends on eta_f!** f_NL would be time-dependent, which is wrong.

### Diagnosing the error:

The problem is that the super-Hubble approximation for the INTEGRAL picks up the dominant divergence, but the product with the external legs does not produce a clean cancellation because I was not careful about the full in-in structure.

**The resolution requires the FULL mode functions (not just super-Hubble) in the vertex integral.** The horizon-crossing contribution from the oscillatory piece provides the PHYSICAL bispectrum. The power-law divergences from the growing mode cancel when properly accounting for the interaction picture vs Heisenberg picture mode functions.

---

## The Correct In-In Structure (Maldacena's Method)

The key insight from Maldacena (2003) and Chen et al. (2007): for GROWING modes, the standard in-in formula must be supplemented by boundary terms at eta_f.

Alternatively, one can use the fact that f_NL is a RATIO and is time-independent. The correct procedure (Cai et al. 2009) is:

1. Compute the full shape function A_T at a time eta_f after all modes have crossed the horizon
2. A_T is defined such that the time-dependent growing-mode factors cancel

Cai et al. define:

$$
\langle\zeta_{k_1}\zeta_{k_2}\zeta_{k_3}\rangle' = \frac{(2\pi)^4\mathcal{P}_\zeta^2}{(k_1 k_2 k_3)^2}A_T
$$

Since P_zeta ~ eta_f^{-6} and the bispectrum ~ eta_f^{-12} (times the integral which adds more eta_f dependence), the A_T is constructed to be time-independent.

**The physical content:** A_T captures the SHAPE of the bispectrum, with the overall amplitude absorbed into P_zeta. Since both P_zeta and B_zeta grow from the same growing mode, their ratio is fixed.

### Directly extracting f_NL:

From our master formula and the analysis above, f_NL^intrinsic requires computing:

$$
f_{\rm NL}^{\rm intrinsic} = \frac{5}{8}\cdot k^3\eta_f^3\cdot\text{Re}[-\text{integral}(x_f)]
$$

For this to be time-independent, we need the HORIZON-CROSSING (finite) part of the integral, not the divergent part.

### Isolating the horizon-crossing contribution:

Write each J_n as:

$$
J_n(x_f) = J_n^{\rm div}(x_f) + J_n^{\rm finite}
$$

where J_n^div contains all powers of 1/|x_f| and J_n^finite is the constant (oscillatory integral from -infinity to 0).

The divergent parts of -J_3 + 6iJ_4 + 15J_5 - 18iJ_6 - 9J_7 at leading order:

From the superhorizon calculation above, these divergent parts produce the purely imaginary result that gives zero when combined with the external legs and taking real parts + c.c.

**Therefore, f_NL comes entirely from the FINITE parts J_n^finite.**

### Computing J_n^finite:

$$
J_n^{\rm finite} = (-1)^{n+1}\int_0^{\infty}\frac{ds}{s^n}e^{2is}\bigg|_{\rm regularized}
$$

These are related to:

$$
\int_0^{\infty}s^{-n}e^{2is}\,ds = \frac{(2i)^{n-1}}{(n-1)!}\left[-\gamma - \ln(2) + i\pi/2 - \psi(n) + ...\right]
$$

Wait — this is getting complicated because these integrals involve logarithmic and polygamma functions.

**A cleaner approach: use the recursion relation.** Note that:

$$
J_n^{\rm finite} = \frac{-2i}{n-1}J_{n-1}^{\rm finite}
$$

This follows from integration by parts: integrate e^{2is}/s^n by parts, differentiating s^{-(n-1)} and integrating e^{2is}.

No — integration by parts gives:

$$
\int_0^{\infty}\frac{e^{2is}}{s^n}ds = \left[\frac{e^{2is}}{2is\cdot s^{n-1}}\cdot...\right]
$$

This is getting messy. Let me use a different approach entirely.

---

## Alternative: Use the Consistency Relation

For any single-field model, Maldacena's consistency relation gives:

$$
\lim_{k_1\to 0}\frac{B_\zeta(k_1,k,k)}{P(k_1)P(k)} = -(2\epsilon + \eta_s)\cdot\frac{12}{5}
$$

Wait — the standard consistency relation is:

$$
f_{\rm NL}^{\rm sq} = \frac{5}{12}(1-n_s) = \frac{5}{12}(2\epsilon + \eta)
$$

For slow-roll inflation. For the matter bounce with n_s = 1 (scale-invariant), this would give f_NL = 0.

But the matter bounce has a GROWING mode, which violates the assumptions of the consistency relation. The consistency relation assumes that long-wavelength modes act as a coordinate transformation on the short-wavelength modes — this is true when zeta is constant, but FALSE when zeta grows.

**The growing mode invalidates the standard consistency relation.** This is precisely why the matter bounce has a LARGE f_NL rather than the tiny slow-roll-suppressed value.

The physical mechanism: when zeta_long grows, it doesn't just rescale coordinates — it CHANGES THE LOCAL EXPANSION HISTORY for the short modes. The short modes evolve differently in patches with different zeta_long because the local Hubble rate is modified. This generates a large local-type bispectrum.

---

## The Correct Calculation: Cai et al.'s Approach

Rather than wrestling with the divergent integrals (which Cai et al. also had to deal with), let me trace through their logic and identify where the -35/8 comes from.

### Cai et al. strategy:
1. Compute the full in-in bispectrum at eta_f (with growing divergences)
2. Compute the power spectrum at eta_f (with growing divergences)
3. Form the RATIO A_T = B_zeta * (k_1 k_2 k_3)^2 / ((2pi)^4 P_zeta^2)
4. Verify that A_T is eta_f-independent (divergences cancel)
5. Extract |B|_NL from A_T in the squeezed limit

### Their result for A_T in the squeezed limit:

In the squeezed limit k_1 << k_2 ~ k_3 = k, Cai et al. find (their Eq. 38):

$$
A_T^{\rm sq} = -\frac{21}{4}\frac{k^4}{k_1}\cdot\frac{k_1}{k} + ... = -\frac{21}{4}k^3 + \text{subleading in }k_1/k
$$

Wait, I need to read their equation more carefully. Their A_T has specific k-dependence. In the squeezed limit, the dominant term scales as k_1^2 k^4 (local-type scaling).

Their |B|_NL:

$$
|B|_{\rm NL} = \frac{10}{3}\frac{A_T}{k_1^3 + k_2^3 + k_3^3}
$$

In the squeezed limit k_1 -> 0: k_1^3 + 2k^3 -> 2k^3. So:

$$
|B|_{\rm NL}^{\rm sq} = \frac{10}{3}\frac{A_T^{\rm sq}}{2k^3} = \frac{5}{3}\frac{A_T^{\rm sq}}{k^3}
$$

For |B|_NL = -35/8, we need A_T^sq / k^3 = (-35/8)(3/5) = -21/8.

So A_T^sq = -(21/8) k^3 in the squeezed limit.

### Converting to our f_NL:

From the convention lock (file 02 of the planning program):

$$
B_\zeta = \frac{(2\pi)^4 \mathcal{P}_\zeta^2}{(k_1 k_2 k_3)^2}A_T
$$

In the squeezed limit:

$$
B_\zeta^{\rm sq} = \frac{(2\pi)^4 \mathcal{P}_\zeta^2}{k_1^2 k^4}A_T^{\rm sq}
$$

Our f_NL:

$$
f_{\rm NL} = \frac{5}{12}\frac{B_\zeta^{\rm sq}}{P(k_1)P(k)} = \frac{5}{12}\frac{(2\pi)^4\mathcal{P}_\zeta^2 A_T^{\rm sq}}{k_1^2 k^4}\cdot\frac{k_1^3 k^3}{(2\pi^2)^2\mathcal{P}_\zeta^2}
$$

$$
= \frac{5}{12}\cdot\frac{(2\pi)^4}{4\pi^4}\cdot\frac{k_1 A_T^{\rm sq}}{k}
$$

$$
= \frac{5}{12}\cdot 4\cdot\frac{k_1 A_T^{\rm sq}}{k}
$$

$$
= \frac{5}{3}\frac{k_1 A_T^{\rm sq}}{k}
$$

**This depends on k_1/k!** For this to be a constant (scale-independent f_NL), A_T^sq must scale as k/k_1 in the squeezed limit.

From Cai et al.'s result: A_T in the squeezed limit has a term proportional to k^4/k_1 (equivalently k^3 * (k/k_1)). So:

A_T^sq = C * k^4/k_1 where C is a numerical coefficient.

Then:

$$
f_{\rm NL} = \frac{5}{3}\frac{k_1}{k}\cdot C\cdot\frac{k^4}{k_1} = \frac{5C k^3}{3k} = \frac{5Ck^2}{3}
$$

This is STILL k-dependent. Something is wrong — f_NL should be a pure number.

### The resolution: P_zeta is scale-invariant but P(k) is not just P_zeta!

Recall P(k) = (2 pi^2/k^3) P_zeta. So P(k_1) P(k) = (2 pi^2)^2 P_zeta^2 / (k_1^3 k^3).

But the full A_T in the local limit goes as:

For a local shape: B^local = (12/5) f_NL P_zeta^2 (2pi^2)^2 / (k_1^3 k^3).

In Cai's notation: B = (2pi)^4 P_zeta^2 A_T / (k_1 k_2 k_3)^2 = (2pi)^4 P_zeta^2 A_T / (k_1^2 k^4).

Setting these equal:

$$
\frac{(2\pi)^4 A_T}{k_1^2 k^4} = \frac{12}{5}f_{\rm NL}\frac{(2\pi^2)^2}{k_1^3 k^3}
$$

$$
A_T = \frac{12}{5}f_{\rm NL}\frac{4\pi^4}{(2\pi)^4}\frac{k_1^2 k^4}{k_1^3 k^3} = \frac{12}{5}f_{\rm NL}\frac{1}{4}\frac{k}{k_1}
$$

$$
\boxed{A_T^{\rm sq, local} = \frac{3}{5}\frac{f_{\rm NL}\, k}{k_1}}
$$

And Cai's |B|_NL:

$$
|B|_{\rm NL} = \frac{10}{3}\frac{A_T}{2k^3} = \frac{10}{3}\frac{1}{2k^3}\cdot\frac{3}{5}\frac{f_{\rm NL}\, k}{k_1} = \frac{f_{\rm NL}}{k_1 k^2}
$$

**THIS IS NOT A PURE NUMBER.** It depends on k_1 and k.

But Cai et al. report |B|_NL = -35/8, a pure number. This means their A_T has a DIFFERENT k-dependence in the squeezed limit than what I'm computing.

### The k-dependence mismatch:

If |B|_NL = (10/3) A_T / (k_1^3 + 2k^3) is to be a pure number, then A_T must be proportional to (k_1^3 + 2k^3), which for k_1 << k gives A_T ~ 2k^3.

But for the LOCAL shape, A_T ~ k/k_1.

These can only be consistent if the LOCAL shape's A_T ALSO goes as k^3 in the squeezed limit — which means the k/k_1 piece must be wrong.

**The error is in my conversion.** Let me redo it more carefully.

Cai et al.'s normalization (their Eq. 16) is:

$$
\langle\zeta_{k_1}\zeta_{k_2}\zeta_{k_3}\rangle' = \frac{(2\pi)^4 \mathcal{P}_\zeta^2}{\prod k_i^3} \cdot A_T
$$

Note: **(k_i)^3 in the denominator, not (k_i)^2!**

So: B_zeta = (2pi)^4 P_zeta^2 A_T / (k_1^3 k_2^3 k_3^3)

In the squeezed limit:

$$
B_\zeta^{\rm sq} = \frac{(2\pi)^4\mathcal{P}_\zeta^2 A_T^{\rm sq}}{k_1^3 k^3 k^3} = \frac{(2\pi)^4\mathcal{P}_\zeta^2 A_T^{\rm sq}}{k_1^3 k^6}
$$

Our f_NL:

$$
f_{\rm NL} = \frac{5}{12}\frac{B_\zeta}{P(k_1)P(k)} = \frac{5}{12}\cdot\frac{(2\pi)^4\mathcal{P}_\zeta^2 A_T^{\rm sq}}{k_1^3 k^6}\cdot\frac{k_1^3 k^3}{(2\pi^2)^2\mathcal{P}_\zeta^2}
$$

$$
= \frac{5}{12}\cdot\frac{16\pi^4}{4\pi^4}\cdot\frac{A_T^{\rm sq}}{k^3} = \frac{5}{12}\cdot 4\cdot\frac{A_T^{\rm sq}}{k^3} = \frac{5}{3}\frac{A_T^{\rm sq}}{k^3}
$$

Now, for |B|_NL = -35/8:

$$
|B|_{\rm NL} = \frac{10}{3}\frac{A_T^{\rm sq}}{2k^3} = \frac{5}{3}\frac{A_T^{\rm sq}}{k^3} = -\frac{35}{8}
$$

**THEREFORE:**

$$
\boxed{f_{\rm NL} = \frac{5}{3}\frac{A_T^{\rm sq}}{k^3} = |B|_{\rm NL}^{\rm sq}}
$$

**In the squeezed limit, f_NL = |B|_NL EXACTLY.**

The quantity (5/3)(A_T/k^3) is the same as (10/3)(A_T/(2k^3)) = |B|_NL in the squeezed limit where k_1^3 + 2k^3 -> 2k^3.

**This means: if Cai et al.'s |B|_NL = -35/8 in the squeezed limit, then f_NL = -35/8 in the Planck convention.**

---

## THE CRITICAL CONVERSION RESULT

$$
\boxed{f_{\rm NL}^{\rm local} = |B|_{\rm NL}^{\rm squeezed} = -\frac{35}{8}\quad \text{(if Cai et al. is correct)}}
$$

The Cai normalization (10/3)(A_T / sum k_i^3) is ALGEBRAICALLY IDENTICAL to our (5/12)(B_zeta / P P) in the squeezed limit, assuming Cai's Eq. (16) defines A_T correctly.

**This eliminates Hypothesis C (different quantities) from the discrepancy map.** Cai's |B|_NL in the squeezed limit IS f_NL in the Planck convention.

---

## Where Does -35/8 Come From? (Coefficient Tracing)

The field-redefinition contribution is f_NL^FR = 5 epsilon / 6 = 5/4.

So the intrinsic contribution must be:

$$
f_{\rm NL}^{\rm intrinsic} = -\frac{35}{8} - \frac{5}{4} = -\frac{35}{8} - \frac{10}{8} = -\frac{45}{8}
$$

The total is the sum of the field redefinition (+5/4) and the intrinsic in-in integral (-45/8):

$$
f_{\rm NL}^{\rm total} = -\frac{45}{8} + \frac{10}{8} = -\frac{35}{8}
$$

### The factor-of-2 question:

If Li & Brandenberger get -35/16 instead of -35/8, the factor of 2 must sit in either:
1. The field-redefinition piece (they get 5/8 instead of 5/4) → unlikely, this is straightforward
2. The intrinsic integral (they get -45/16 instead of -45/8) → plausible if they have a different prefactor
3. The overall normalization of the cubic action → most likely

Since -35/16 = -35/8 / 2, and the ENTIRE result is halved (not just one piece), the factor of 2 likely sits in the OVERALL prefactor of the cubic action or the in-in formula, not in a specific vertex.

**Most likely location:** the factor of 2 from the commutator in the in-in formula. The commutator gives [H_int, external] = H_int * external - external * H_int, which in the free-field Wick contraction gives a factor of 2 relative to a single time-ordered product. If Li & Brandenberger omit this factor (or define their bispectrum without it), they get half the answer.

---

## Remaining Algebraic Bottleneck

The conversion above establishes that IF Cai et al.'s A_T is correct, THEN f_NL = -35/8 in Planck convention. But we have not independently verified A_T.

The independent verification requires computing the in-in time integral with exact mode functions (not just superhorizon approximation) and extracting the finite, eta_f-independent coefficient. This integral involves:

$$
\int_{-\infty}^{\eta_f}d\eta'\,\eta'^4\,g_k(\eta')\,g'_k(\eta')^2\,g_{k_1}^{\rm super}(\eta')
$$

with exact g_k, in the limit |k eta_f| << 1 but k_1/k -> 0.

**Status: The full analytic evaluation of this integral is the remaining bottleneck. The conversion factor between Cai's notation and Planck's f_NL is now resolved — they are equal in the squeezed limit.**
