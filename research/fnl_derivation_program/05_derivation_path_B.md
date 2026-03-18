# 05: Derivation Path B — In-In / Cubic Action Cross-Check

**Created:** 2026-03-17
**Status:** SCAFFOLD COMPLETE

---

## Purpose

Path B is the INDEPENDENT cross-check of Path A. If both paths give the same f_NL, the result is robust. If they disagree, the disagreement reveals which approximations matter.

Path B follows the method of Cai et al. (2009): compute the bispectrum directly from the cubic action using the in-in (Schwinger-Keldysh) formalism.

---

## The In-In Formalism

### The master formula:

The three-point function at time eta_f (late time, well before bounce) is:

$$
\langle \zeta_{\mathbf{k}_1} \zeta_{\mathbf{k}_2} \zeta_{\mathbf{k}_3} \rangle(\eta_f) = -i \int_{-\infty}^{\eta_f} d\eta' \, a(\eta') \langle [\zeta_{\mathbf{k}_1}(\eta_f) \zeta_{\mathbf{k}_2}(\eta_f) \zeta_{\mathbf{k}_3}(\eta_f), H_{\rm int}(\eta')] \rangle + \text{c.c.}
$$

where H_int is the interaction Hamiltonian derived from the cubic action S_3.

### Key differences from inflation:

1. **Growing mode dominates.** In inflation, zeta freezes at horizon crossing and the mode function is ~constant afterward. In matter contraction, zeta GROWS as |eta|^{-3} after horizon crossing. This means the late-time contributions to the integral are NOT suppressed — they are ENHANCED.

2. **The integral does NOT converge at eta_f.** In inflation, the oscillatory phase exp(ik eta) kills contributions from late times. Here, the growing mode overwhelms the oscillation. The integral must be evaluated at a specific late time eta_f (just before the bounce), and the result DEPENDS on eta_f through the growing mode.

3. **The vacuum is different.** The initial vacuum is set at eta -> -infinity (early contraction, large |eta|), where modes are deep inside the Hubble radius and the standard Minkowski vacuum applies. This is the same logic as inflation but with time reversed.

4. **epsilon = 3/2 is NOT small.** The standard Maldacena result uses epsilon << 1 to simplify the cubic action. For the matter bounce, epsilon = 3/2 and ALL terms in the cubic action contribute at the same order.

---

## The Cubic Action for a Canonical Scalar Field

### Maldacena (2003) cubic action:

For a canonical scalar field (c_s = 1) in the comoving gauge:

$$
S_3 = M_{\rm Pl}^2 \int d\eta \, d^3x \, a^2 \left[ \epsilon^2 \zeta \zeta'^2 + \epsilon^2 \zeta (\partial_i \zeta)^2 - 2\epsilon \zeta' (\partial_i \zeta)(\partial_i \chi) + \frac{\epsilon}{2} \frac{d}{d\eta}(\epsilon/\mathcal{H}) \zeta'^2 \zeta + \ldots \right]
$$

where chi is determined by the constraint equation: nabla^2 chi = epsilon zeta'.

**For epsilon = 3/2 (matter contraction):**

- epsilon is constant (since w = 0 is exact), so d(epsilon)/d eta = 0
- The term (epsilon/H) d(epsilon)/d eta vanishes
- The remaining terms are:

$$
S_3 = M_{\rm Pl}^2 \int d\eta \, d^3x \, a^2 \left[ \frac{9}{4} \zeta \zeta'^2 + \frac{9}{4} \zeta (\partial_i \zeta)^2 - 3 \zeta' (\partial_i \zeta)(\partial_i \chi) \right]
$$

plus boundary terms and field-redefinition terms.

### The field redefinition:

Maldacena shows that part of the cubic action can be removed by the field redefinition zeta -> zeta + (epsilon/2) zeta^2. This is the origin of the local-type non-Gaussianity in slow-roll inflation (f_NL = 5(1-n_s)/12).

**For matter contraction with epsilon = 3/2:** The field redefinition contributes f_NL^{field redef} = (5/4)(epsilon) = 15/8. But this is NOT the full answer — the remaining cubic vertices (the "intrinsic" non-Gaussianity from the time integral) also contribute, and for the matter bounce they are NOT slow-roll suppressed.

---

## The Mode Functions

### From file 02 (convention lock):

The Mukhanov-Sasaki equation:

$$
v_k'' + \left(k^2 - \frac{2}{\eta^2}\right) v_k = 0
$$

### General solution:

$$
v_k(\eta) = \alpha_k \frac{e^{-ik\eta}}{\sqrt{2k}} \left(1 - \frac{i}{k\eta}\right) + \beta_k \frac{e^{ik\eta}}{\sqrt{2k}} \left(1 + \frac{i}{k\eta}\right)
$$

### Bunch-Davies vacuum at early times (eta -> -infinity):

$$
\alpha_k = 1, \quad \beta_k = 0
$$

$$
v_k(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}} \left(1 - \frac{i}{k\eta}\right)
$$

### The mode function for zeta:

$$
\zeta_k(\eta) = \frac{v_k}{z} = \frac{v_k}{a\sqrt{3}} = \frac{1}{a_0\sqrt{3}\eta^2} \cdot \frac{e^{-ik\eta}}{\sqrt{2k}} \left(1 - \frac{i}{k\eta}\right)
$$

### On superhorizon scales (|k eta| << 1):

$$
\zeta_k^{\rm super} \approx \frac{1}{a_0\sqrt{3}\eta^2} \cdot \frac{1}{\sqrt{2k}} \cdot \frac{-i}{k\eta} = \frac{-i}{a_0\sqrt{6k^3}\eta^3}
$$

This confirms zeta grows as |eta|^{-3} — the growing mode.

---

## The Vertices

### In Fourier space, the cubic action gives three types of vertices:

**Vertex 1: zeta zeta'^2 type**
$$
V_1 \propto \int d\eta \, a^2 \epsilon^2 \, \zeta_{k_1}(\eta) \, \zeta'_{k_2}(\eta) \, \zeta'_{k_3}(\eta) + \text{perms}
$$

**Vertex 2: zeta (grad zeta)^2 type**
$$
V_2 \propto \int d\eta \, a^2 \epsilon^2 \, \zeta_{k_1}(\eta) \cdot (k_2 \cdot k_3) \, \zeta_{k_2}(\eta) \, \zeta_{k_3}(\eta) + \text{perms}
$$

**Vertex 3: zeta' (grad zeta)(grad chi) type**
This involves the constraint variable chi and produces a more complex k-dependent structure.

### Which vertex dominates in the squeezed limit?

In the squeezed limit (k_1 -> 0, k_2 = k_3 = k):
- Vertex 1: zeta_{k_1} is the long-wavelength mode (exits horizon earliest, has the most growth). The zeta'_{k_2} zeta'_{k_3} product oscillates as ~exp(-2ik eta) on subhorizon scales and freezes/grows on superhorizon scales.
- Vertex 2: The (k_2 . k_3) factor gives -k^2 in the squeezed limit (k_1 = 0 => k_2 = -k_3). This vertex is suppressed by k^2/H^2 on superhorizon scales.
- Vertex 3: Similar to Vertex 1 but with different k-weighting from the constraint.

**The dominant contribution in the squeezed limit comes from Vertex 1 and Vertex 3**, where the long mode modulates the short modes.

---

## The Time Integral Structure

### The critical difference from inflation:

In inflation (slow-roll, zeta constant after horizon exit):

$$
I \sim \int_{-\infty}^{0} d\eta \, a^2(\eta) \, \zeta_{k_1}^*(\eta_f) \zeta_{k_2}^*(\eta_f) \zeta_{k_3}^*(\eta_f) \cdot \text{vertex}(\eta)
$$

Since zeta is constant for modes outside the horizon, the late-time contribution (eta -> 0) is just zeta(eta_f)^3 times a convergent integral. The integral converges because a^2 ~ eta^{-2} for de Sitter, and the integrand oscillates at early times.

**In matter contraction:**

$$
a^2 = a_0^2 \eta^4
$$

The three zeta mode functions on superhorizon scales each go as eta^{-3}, giving:

$$
\text{integrand} \sim \eta^4 \cdot \eta^{-3} \cdot \eta^{-3} \cdot \eta^{-3} \cdot \eta^{n} = \eta^{-5+n}
$$

where n depends on the vertex (n = 0 for zeta zeta'^2 type, n = 2 for gradient terms).

**For n = 0:** integrand ~ eta^{-5}, which DIVERGES as eta -> 0. The integral is dominated by the latest times (closest to the bounce).

**This is the growing-mode enhancement.** The bispectrum is dominated by late-time nonlinear coupling between growing modes. The result depends on the cutoff eta_f, but this dependence cancels in the ratio B/(P * P) because the power spectrum also grows.

### The cancellation:

P(k) ~ |zeta_k(eta_f)|^2 ~ eta_f^{-6}

B(k_1,k_2,k_3) ~ |zeta|^3 times integral ~ eta_f^{-9} * eta_f^{-5+1} ~ ...

Actually, the exact scaling needs careful tracking. Let me note what must be verified:

**CHECK 1:** The ratio B/(P*P) must be independent of eta_f (no time dependence in f_NL).
**CHECK 2:** The ratio must be independent of k in the squeezed limit (scale-invariance of f_NL).
**CHECK 3:** The field-redefinition contribution must be added to the intrinsic contribution correctly.

---

## What Cai et al. (2009) Actually Computed

### Their method:
1. Write the cubic action for canonical scalar field in matter contraction
2. Use the exact mode functions (Bunch-Davies in-in vacuum)
3. Evaluate the time integrals at eta_f (some time well after all three modes have crossed the horizon)
4. Extract the shape function A_T(k_1, k_2, k_3)
5. Define |B|_NL = (10/3) A_T / (sum k_i^3)
6. Evaluate in the squeezed limit to get |B|_NL = -35/8

### What we need to reproduce:
The raw B_zeta(k_1, k_2, k_3) in the squeezed limit, then apply our locked extraction formula (file 02).

### The key question:
**Does Cai et al.'s A_T -> |B|_NL -> f_NL conversion introduce any factors beyond the physics?** If A_T is the correct bispectrum and the conversion to our convention is exact, then -35/8 is confirmed. If the conversion introduces approximation (e.g., assuming purely local shape), the true f_NL could differ.

---

## Execution Plan for Path B

### Step B1: Write the full cubic action for epsilon = 3/2

Starting from Maldacena (2003) Eq. (17) [or Chen et al. (2007) Eq. (3.11) for general c_s]:
- Set c_s = 1, epsilon = 3/2, eta_epsilon = 0
- Keep ALL terms (no slow-roll approximation)
- Include the field-redefinition boundary term

### Step B2: Mode functions

Use the exact Bunch-Davies mode function from above. Verify normalization by computing the power spectrum and checking P_zeta = k^2 / (12 pi^2 a_0^2 k^3 eta^6) [or whatever the exact form is].

### Step B3: Evaluate the time integrals

For each vertex, compute:
$$
I_n = \int_{-\infty}^{\eta_f} d\eta \, (\text{vertex}_n) \times \text{mode functions}
$$

Use the superhorizon approximation for the long mode (k_1 eta << 1 throughout the integral range that matters) and the exact mode function for the short modes.

### Step B4: Assemble B_zeta and extract f_NL

Sum all vertex contributions, add the field-redefinition piece, take the squeezed limit, and apply the extraction formula.

### Step B5: Compare with Path A

If both paths give the same answer, the result is established. If they disagree, the disagreement reveals whether the gradient expansion or the in-in formalism contains an uncontrolled approximation.

---

## What Should Match Between Path A and Path B

### The intermediate result that MUST agree:

The time-dependence of zeta at second order:

$$
\zeta^{(2)}(k, \eta) = f(\text{momenta}) \cdot \zeta^{(1)}(k_2, \eta) \cdot \zeta^{(1)}(k_3, \eta)
$$

The function f(momenta) in the squeezed limit, converted to f_NL via the extraction formula, must give the same number from both paths.

### What the Cai et al. shape function tells us:

Their A_T encodes the FULL momentum dependence, not just the squeezed limit. The squeezed limit is:

$$
A_T(k_1, k, k) \underset{k_1 \to 0}{\longrightarrow} -\frac{35}{8} \cdot \frac{k_1^3 + 2k^3}{(10/3)} \cdot ...
$$

Wait — the exact k-dependence of A_T in the squeezed limit is what determines whether |B|_NL = f_NL or not. This is the template projection problem (file 06).

---

## Critical Warning: The Growing Mode Changes Everything

In standard inflation, the in-in calculation is straightforward because:
1. Modes freeze after horizon crossing
2. The time integral converges
3. The result is dominated by horizon-crossing contributions
4. The shape function is determined at horizon crossing and doesn't evolve

In the matter bounce:
1. Modes GROW after horizon crossing
2. The time integral may diverge (cut off by the bounce)
3. The result is dominated by LATE-TIME contributions (near the bounce)
4. The shape function EVOLVES after horizon crossing due to mode growth

**This means the "shape at horizon crossing" (which determines the in-in bispectrum in inflation) is NOT the "shape at the time of observation" (which is what Planck measures).**

The shape continues to evolve after horizon crossing until the bounce. The observed shape depends on when the growing mode is terminated (at the bounce). This evolution could change the template projection.

**However:** If all three modes grow at the same rate (|eta|^{-3}), the shape RATIOS are preserved and f_NL is time-independent. This needs explicit verification.
