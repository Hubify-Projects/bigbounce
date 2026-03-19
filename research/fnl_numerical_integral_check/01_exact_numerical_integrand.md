# 01: Exact Numerical Integrand

---

## Background and Setup

Matter contraction: a(η) = a₀ η², H = 2/η, ε = -Ḣ/H² = 3/2, η ∈ (-∞, 0⁻)

Mukhanov-Sasaki variable: v_k(η) = z ζ_k(η), where z = a√(2ε) = a₀√3 η²

Mode equation: v_k'' + (k² - 2/η²) v_k = 0

Bunch-Davies solution: v_k(η) = e^{-ikη}/√(2k) · (1 - i/(kη))

---

## Power Spectrum

$$
P_\zeta(k) = \lim_{\eta \to 0^-} |v_k(\eta)|^2 / z^2 = \frac{1}{6 a_0^2 k^3 \eta^6}
$$

Note: This DIVERGES as η → 0⁻ (growing mode). The divergence cancels in f_NL = B/(P·P).

---

## Stripped Mode Function

Define g_k(η) ≡ v_k(η) / z(η) = ζ_k(η) (the curvature perturbation mode function):

$$
g_k(\eta) = \frac{e^{-ik\eta}}{\sqrt{6} a_0 k^{3/2} \eta^2} \left(1 - \frac{i}{k\eta}\right)
$$

Its time derivative:

$$
g_k'(\eta) = \frac{e^{-ik\eta}}{\sqrt{6} a_0 k^{3/2} \eta^2} \left(-ik - \frac{3}{\eta} + \frac{3i}{k\eta^2}\right)
$$

---

## Dominant Cubic Vertex

From the Maldacena cubic action at ε = 3/2:

Term 1 (dominant): S₃ ⊃ (9/4) M²_Pl ∫ dη a² ζ (ζ')²

In the in-in formalism, this contributes to the bispectrum:

$$
B_\zeta^{(1)}(\mathbf{k}_1, \mathbf{k}_2, \mathbf{k}_3) = -2 \cdot \frac{9}{4} M_{\rm Pl}^2 \, {\rm Im}\left[g_{k_1}^*(\eta_f) g_{k_2}^*(\eta_f) g_{k_3}^*(\eta_f) \int_{-\infty(1-i\epsilon)}^{\eta_f} d\eta' \, a^2(\eta') \, g_{k_1}(\eta') g_{k_2}'(\eta') g_{k_3}'(\eta') \right] + 5 \text{ perms}
$$

The factor of -2 comes from the commutator in the in-in formula: B = -2 Im[...].

The "5 perms" means summing over all distinct assignments of which mode function gets no derivative. By symmetry of ζ(ζ')², there are 3 distinct permutations (which leg is the undifferentiated ζ).

With a(η) = a₀ η²: a²(η') = a₀² η'⁴

---

## Squeezed Limit: k₁ → 0, k₂ = k₃ = k

**Long mode (k₁ → 0):** On subhorizon scales of the short modes, the long mode is superhorizon:

$$
g_{k_1}(\eta') \approx \frac{-i}{\sqrt{6} a_0 k_1^{3/2} \eta'^3} \quad (\text{for } |k_1 \eta'| \ll 1)
$$

This approximation is VALID because we take k₁/k → 0 while evaluating the integral at scales |kη'| ~ 1.

**Short modes (k₂ = k₃ = k):** Use EXACT mode functions. NO superhorizon approximation.

---

## The Three Permutations in the Squeezed Limit

**Permutation 1:** ζ_{k₁} is undifferentiated, both ζ'_{k₂} and ζ'_{k₃} are differentiated.

$$
I_1 = \int_{-\infty}^{\eta_f} d\eta' \, a_0^2 \eta'^4 \, g_{k_1}(\eta') \, g_k'(\eta') \, g_k'(\eta')
$$

**Permutations 2 and 3:** ζ_{k₂} or ζ_{k₃} is undifferentiated (equivalent by k₂ = k₃):

$$
I_2 = I_3 = \int_{-\infty}^{\eta_f} d\eta' \, a_0^2 \eta'^4 \, g_{k_1}'(\eta') \, g_k(\eta') \, g_k'(\eta')
$$

For the long mode: g'_{k₁}(η') ≈ (3i)/(√6 a₀ k₁^{3/2} η'⁴), so I₂ and I₃ are suppressed by k₁/k relative to I₁ in the squeezed limit (the long mode derivative brings down an extra 1/η' which is compensated, but the overall scaling with k₁ differs).

Wait — let me be more careful. In the squeezed limit, the DOMINANT permutation is actually ALL THREE contributing comparably, because the vertex ζ(ζ')² already selects which mode is undifferentiated.

Actually, for the squeezed limit with k₁ → 0:
- Perm 1 (long mode undifferentiated): g_{k₁} ~ 1/(k₁^{3/2} η'³), g'_k g'_k ~ exact
- Perm 2,3 (long mode differentiated): g'_{k₁} ~ 1/(k₁^{3/2} η'⁴), g_k g'_k ~ exact

The extra 1/η' in g'_{k₁} is compensated by one fewer derivative on a short mode (g_k vs g'_k ~ k·g_k). In the squeezed limit, Perm 1 dominates because the RATIO of contributions scales as |g'_{k₁}/g_{k₁}| / |g'_k/g_k| ~ (1/η')/(k) ~ 1/(kη') which diverges at late times but is O(1) at horizon crossing.

**For a clean numerical evaluation:** Include all three permutations explicitly. Let the code handle the relative magnitudes.

---

## Dimensionless Integral

Define x = kη (dimensionless conformal time). Then:

$$
g_k(\eta) = \frac{k^{1/2} e^{-ix}}{\sqrt{6} a_0 x^2} (1 - i/x) = \frac{k^{1/2}}{\sqrt{6} a_0} \hat{g}(x)
$$

where $\hat{g}(x) = e^{-ix}(1 - i/x)/x^2$ is the dimensionless mode function.

Similarly: $g'_k(\eta) = k \cdot d\hat{g}/dx \cdot k^{1/2}/(\sqrt{6} a_0) = k^{3/2}/(\sqrt{6} a_0) \hat{g}'(x)$

where $\hat{g}'(x) = e^{-ix}(-i - 3/x + 3i/x^2)/x^2$

---

## Master Formula in Dimensionless Variables

For Permutation 1 (long mode undifferentiated) in the squeezed limit:

$$
I_1 = a_0^2 \cdot \frac{(-i)}{\sqrt{6} a_0 k_1^{3/2}} \cdot \frac{k^3}{6 a_0^2} \cdot \frac{1}{k} \int_{-\infty}^{x_f} \frac{dx}{x^3} \left[\hat{g}'(x)\right]^2
$$

Simplifying (keeping careful track of all factors):

$$
I_1 = \frac{(-i) k^2}{6\sqrt{6} a_0 k_1^{3/2}} \int_{-\infty}^{x_f} \frac{dx}{x^3} \left[\hat{g}'(x)\right]^2
$$

The bispectrum from Perm 1:

$$
B^{(1)} = -2 \cdot \frac{9}{4} M_{\rm Pl}^2 \cdot {\rm Im}\left[g_{k_1}^* g_k^* g_k^* \cdot I_1 \right] \cdot 1
$$

And f_NL^intrinsic:

$$
f_{\rm NL}^{\rm intr} = \frac{5}{12} \frac{B}{P(k_1) P(k)} = \frac{5}{12} \frac{-2 \cdot \frac{9}{4} M_{\rm Pl}^2 \cdot {\rm Im}[\ldots]}{P(k_1) P(k)}
$$

**The key simplification:** All factors of a₀, k, η_f, and M_Pl CANCEL in the ratio B/(P·P), leaving a pure number. This is guaranteed because f_NL is dimensionless and scale-invariant in the exact squeezed limit.

---

## The Integral to Compute Numerically

After all cancellations, the core dimensionless integral is:

$$
\mathcal{I} = \int_{-\infty}^{x_f} dx \, \frac{e^{-2ix}}{x^3} \left(-1 + \frac{6i}{x} + \frac{15}{x^2} - \frac{18i}{x^3} - \frac{9}{x^4}\right)
$$

where we used $[\hat{g}'(x)]^2 = e^{-2ix}/x^4 \cdot (-i - 3/x + 3i/x^2)^2$ and the expansion:

$$
(-i - 3/x + 3i/x^2)^2 = -1 + 6i/x + 15/x^2 - 18i/x^3 - 9/x^4
$$

This integral is a sum of terms of the form ∫ dx e^{-2ix} x^{-n} for n = 3, 4, 5, 6, 7.

The iε prescription (x → x(1-iε) at x → -∞) ensures convergence at early times.

At late times (x → 0⁻), the integral DIVERGES as powers of 1/x_f. These divergences cancel in f_NL.

---

## Implementation Strategy

Rather than analytically computing the integral and its cancellations, the NUMERICAL approach is:

1. Compute the FULL bispectrum B(k₁, k, k) at finite η_f using exact mode functions
2. Compute P(k₁)·P(k) at the same η_f
3. Take the ratio — all divergences cancel
4. Verify η_f-independence by varying η_f

This is the cleanest numerical strategy because it avoids manually cancelling divergences.
