# 08: First Executable Derivation Step

**Created:** 2026-03-17
**Status:** COMPLETE — READY TO EXECUTE

---

## The Single First Step

**Compute the power spectrum P(k) from the exact Bunch-Davies mode function in matter contraction, verify scale invariance, and extract the normalization.**

This is the foundation for EVERYTHING that follows. Both Path A and Path B require the correctly normalized linear mode function. The power spectrum is the simplest nontrivial quantity — if we get this wrong, the bispectrum has no chance.

---

## Why This Step First

1. **It tests the mode function.** The exact mode function v_k(eta) determines both the power spectrum (at second order in perturbation theory) and the bispectrum (at third order). Getting P(k) right validates the mode function.

2. **It tests the conventions.** The power spectrum connects the abstract mode function to the observable quantity P_zeta. All factors of 2pi, sqrt(3), epsilon, etc. must be tracked through. If the normalization is wrong, it will show up here.

3. **It provides the denominator for f_NL.** The extraction formula f_NL = (5/12) B / (P * P) requires P(k). We need the EXACT form of P(k), not just its k-scaling.

4. **It can be checked against the literature.** The matter bounce power spectrum is well-established. If our P(k) disagrees with the literature, we know something is wrong before investing in the harder bispectrum calculation.

---

## The Calculation

### Input:

Mode function (from file 02):

$$
v_k(\eta) = \frac{e^{-ik\eta}}{\sqrt{2k}} \left(1 - \frac{i}{k\eta}\right)
$$

Mukhanov variable relation:

$$
\zeta_k(\eta) = \frac{v_k(\eta)}{z(\eta)}, \quad z(\eta) = a(\eta)\sqrt{2\epsilon} = a_0\sqrt{3}\,\eta^2
$$

(using a(eta) = a_0 eta^2 and epsilon = 3/2, so sqrt(2 * 3/2) = sqrt(3))

### Step 1: Compute |zeta_k(eta)|^2

$$
\zeta_k(\eta) = \frac{1}{a_0\sqrt{3}\,\eta^2} \cdot \frac{e^{-ik\eta}}{\sqrt{2k}} \left(1 - \frac{i}{k\eta}\right)
$$

$$
|\zeta_k(\eta)|^2 = \frac{1}{3a_0^2\eta^4} \cdot \frac{1}{2k} \left|1 - \frac{i}{k\eta}\right|^2 = \frac{1}{6ka_0^2\eta^4} \left(1 + \frac{1}{k^2\eta^2}\right)
$$

### Step 2: Evaluate on superhorizon scales (|k eta| << 1)

$$
|\zeta_k(\eta)|^2 \xrightarrow{|k\eta| \ll 1} \frac{1}{6ka_0^2\eta^4} \cdot \frac{1}{k^2\eta^2} = \frac{1}{6k^3a_0^2\eta^6}
$$

**Note: this GROWS as |eta|^{-6} (since eta -> 0^-).** This is zeta growing as |eta|^{-3}, squared.

### Step 3: Extract the power spectrum

$$
P(k) = |\zeta_k(\eta)|^2 = \frac{1}{6k^3a_0^2\eta^6}
$$

Wait — this depends on eta! The power spectrum is NOT time-independent. This is expected because zeta GROWS.

**The dimensionless power spectrum:**

$$
\mathcal{P}_\zeta(k) = \frac{k^3}{2\pi^2} P(k) = \frac{1}{12\pi^2 a_0^2 \eta^6}
$$

**This is scale-invariant (k-independent)!** Confirmed: the matter bounce gives n_s = 1 at leading order, as expected.

But it grows as |eta|^{-6}. This growth must cancel in the f_NL extraction.

### Step 4: Verify the cancellation in f_NL

$$
f_{\rm NL} = \frac{5}{12} \frac{B_\zeta}{P(k_1)P(k)} \bigg|_{\rm sq}
$$

If B_zeta ~ |zeta|^3 ~ eta^{-9} (from the mode functions) times the time integral, and P * P ~ eta^{-12}, then:

f_NL ~ eta^{-9} * (integral factor) / eta^{-12} = eta^3 * (integral factor)

The integral factor from the time integral in the in-in formalism must scale as eta^{-3} to make f_NL time-independent.

**Check:** The time integral for the dominant vertex (zeta zeta'^2) on superhorizon scales:

zeta'^{(super)} = d/d eta [C / eta^3] = -3C / eta^4

So zeta'^2 ~ eta^{-8}.

Vertex ~ a^2 epsilon^2 * zeta * zeta'^2 ~ eta^4 * eta^{-3} * eta^{-8} = eta^{-7}

Time integral: integral from eta_i to eta_f of eta^{-7} d eta ~ eta_f^{-6} (for the dominant late-time contribution)

So: B ~ (mode functions at eta_f)^3 * integral ~ eta_f^{-9} * eta_f^{-6} = eta_f^{-15}???

That can't be right — it should be eta_f^{-12} for f_NL to be constant...

**This means I need to be more careful about the in-in formula structure.** The mode functions in the in-in integral are NOT all evaluated at eta_f. Some are at eta_f (the external lines) and some are at eta' (the interaction time). Let me redo:

**In-in formula structure:**

$$
B \sim \text{Im} \int d\eta' \, \zeta^*_{k_1}(\eta_f) \zeta^*_{k_2}(\eta_f) \zeta^*_{k_3}(\eta_f) \cdot V(\eta') \cdot \zeta_{k_1}(\eta') \zeta_{k_2}(\eta') \zeta_{k_3}(\eta')
$$

Wait — no. The in-in formula for the three-point function is:

$$
\langle \zeta_{k_1} \zeta_{k_2} \zeta_{k_3} \rangle(\eta_f) = -i \int_{-\infty}^{\eta_f} d\eta' \langle 0 | [\zeta_{k_1}(\eta_f)\zeta_{k_2}(\eta_f)\zeta_{k_3}(\eta_f), H_3(\eta')] | 0 \rangle
$$

Using Wick contraction, this becomes:

$$
B \sim \sum_{\rm perms} \zeta^*_{k_1}(\eta_f) \zeta^*_{k_2}(\eta_f) \cdot (\text{vertex factor at } \eta') \cdot \zeta_{k_3}(\eta') + \text{c.c.}
$$

So TWO external lines are at eta_f and ONE enters the vertex at eta'. The vertex itself involves time derivatives and spatial gradients of the remaining mode function.

For the zeta zeta'^2 vertex: the vertex contributes zeta_{k_1}(\eta') * zeta'_{k_2}(\eta') * zeta'_{k_3}(\eta').

In the squeezed limit, the standard procedure is:
- The long mode k_1 at eta' is on superhorizon scales throughout the integration: zeta_{k_1}(\eta') ~ eta'^{-3}
- The short modes k_2, k_3 at eta' transition from sub to superhorizon

The full analysis requires careful bookkeeping. **This is exactly what the derivation must do.**

### Step 5: The result to verify

The power spectrum normalization:

$$
\boxed{P(k, \eta) = \frac{1}{6k^3 a_0^2 \eta^6}}
$$

$$
\boxed{\mathcal{P}_\zeta(\eta) = \frac{1}{12\pi^2 a_0^2 \eta^6}}
$$

This should be checked against Cai et al. (2009) Eq. (23) or equivalent.

---

## Checks Before Proceeding to the Bispectrum

### Check 1: Scale invariance
P_zeta is k-independent. CONFIRMED above.

### Check 2: Correct time scaling
P_zeta grows as |eta|^{-6}. This matches zeta growing as |eta|^{-3}. CONFIRMED.

### Check 3: Literature comparison
The standard result for the matter bounce power spectrum (e.g., Wands 1999, Finelli & Brandenberger 2002) is P_zeta = H^2 / (8 pi^2 epsilon M_Pl^2 c_s) at horizon crossing, times the growth factor.

At horizon crossing (|k eta| = 1): H = aH = 2/eta, so H_phys = H/a = 2/(a_0 eta^3).

Actually, let me just verify by computing P_zeta in terms of physical quantities.

a_0 is the scale factor normalization. In the Friedmann equation:

$$
\mathcal{H}^2 = \frac{a^2 \rho}{3 M_{\rm Pl}^2}
$$

With H = 2/eta: 4/eta^2 = a^2 rho / (3 M_Pl^2), so rho = 12 M_Pl^2 / (a^2 eta^2) = 12 M_Pl^2 / (a_0^2 eta^6).

Our P_zeta = 1/(12 pi^2 a_0^2 eta^6) = rho / (144 pi^2 M_Pl^2)

Hmm, this should be checked more carefully, but the structural dependence is correct.

### Check 4: Correct vacuum
The mode function used is the Bunch-Davies vacuum, with the positive-frequency condition at eta -> -infinity. This is the standard choice and gives the minimum-excitation state. CONFIRMED.

---

## The Deliverable From This Step

**A verified, normalized power spectrum P(k, eta) that can be used as the denominator in the f_NL extraction formula.**

Once this is verified against the literature, the bispectrum calculation can begin with confidence that the mode function normalization is correct.

---

## Execution Instructions

### To execute this step:

1. Write out P(k, eta) explicitly (done above)
2. Verify n_s = 1 from the k-dependence (done above — k-independent P_zeta)
3. Compare with Cai et al. (2009) power spectrum
4. Verify the eta-dependence matches the growing mode scaling
5. Express a_0 in terms of physical parameters (M_Pl, rho_0, bounce energy scale)

### Time estimate: This step is ALREADY MOSTLY DONE in this file.

The real work begins at Step 2: computing the bispectrum from the cubic action (Path B) or from the second-order separate-universe equations (Path A).

---

## The Next Executable Step After This One

**Path A (gradient expansion):** Set up the scalar-field separate-universe equations to second order. Perturb the initial amplitude and phase of the oscillating field, solve the coupled Klein-Gordon + Friedmann system, and extract the second-order zeta.

**Path B (in-in):** Write the cubic action vertices for epsilon = 3/2, c_s = 1, substitute the mode functions, and evaluate the time integrals in the squeezed limit.

**Recommendation:** Do Path B first, because it most directly compares with Cai et al. and Li & Brandenberger. Path A provides the physical understanding of WHY f_NL takes the value it does (growing-mode nonlinearity).
