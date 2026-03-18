# 04: Derivation Path A — Gradient Expansion / Separate Universe

**Created:** 2026-03-17
**Status:** SCAFFOLD COMPLETE

---

## Strategy

Use the long-wavelength (gradient) expansion to compute the nonlinear relationship between zeta and a Gaussian seed, to second order, during matter-dominated contraction. The key physics: zeta has a GROWING mode on superhorizon scales, and the nonlinear coupling between growing modes generates a bispectrum.

---

## Step 1: Background Equations

### Friedmann:
$$
H^2 = \frac{\rho}{3 M_{\rm Pl}^2}
$$

### Continuity:
$$
\dot{\rho} + 3H(\rho + P) = 0
$$

For w = 0 (dust): rho = rho_0 a^{-3}

### Scalar field realization:
A canonical scalar with V = (1/2) m^2 phi^2 in the matter-like regime. The field oscillates rapidly compared to H^{-1}, and the time-averaged EOS is <w> = 0.

Alternatively: treat as a pressureless fluid (dust). For the bispectrum calculation, the scalar-field realization is needed for the cubic action. But for the gradient expansion, the fluid picture suffices.

### Background solution:
$$
a(t) = a_0 (-t/t_0)^{2/3}, \quad H = \frac{2}{3t}, \quad \rho = \frac{4}{3t^2} M_{\rm Pl}^2
$$

---

## Step 2: Linear Perturbation Theory — The Growing Mode

### Bardeen potential equation:
In the longitudinal gauge (Phi = Psi for w = 0):
$$
\ddot{\Phi} + 4H\dot{\Phi} = 0
$$

(for superhorizon modes, k/a << H)

### Solution:
$$
\Phi(t, \mathbf{x}) = C_1(\mathbf{x}) + C_2(\mathbf{x}) \cdot (-t)^{-5/3}
$$

The C_2 mode GROWS as t -> 0^- (approaching the bounce). In terms of the scale factor:
$$
\Phi^{(\rm grow)} \propto a^{-5/2}
$$

### Curvature perturbation:
$$
\zeta = -\Phi - \frac{H}{\dot{H}} (\dot{\Phi} + H\Phi)
$$

For the constant mode (C_1): zeta = -(5/3) C_1 (standard result).

For the growing mode (C_2): need to compute explicitly.

$$
\dot{\Phi}^{(\rm grow)} = \frac{5}{3} C_2 (-t)^{-8/3}
$$

$$
H = \frac{2}{3t}, \quad \dot{H} = -\frac{2}{3t^2}
$$

$$
\frac{H}{\dot{H}} = -t
$$

$$
\zeta^{(\rm grow)} = -C_2(-t)^{-5/3} - (-t)\left[\frac{5}{3}C_2(-t)^{-8/3} + \frac{2}{3t} \cdot C_2(-t)^{-5/3}\right]
$$

$$
= -C_2(-t)^{-5/3} + t \cdot \frac{5}{3}C_2(-t)^{-8/3} + t \cdot \frac{2}{3t} C_2(-t)^{-5/3}
$$

Wait — let me be more careful with signs. Let tau = -t > 0.

$$
\Phi^{(\rm grow)} = C_2 \tau^{-5/3}
$$

$$
\dot{\Phi}^{(\rm grow)} = \frac{d}{dt}(C_2 \tau^{-5/3}) = C_2 \cdot (-5/3) \tau^{-8/3} \cdot \frac{d\tau}{dt} = C_2 \cdot (-5/3) \tau^{-8/3} \cdot (-1) = \frac{5}{3} C_2 \tau^{-8/3}
$$

$$
H = \frac{2}{3t} = -\frac{2}{3\tau}
$$

$$
\dot{H} = -\frac{2}{3t^2} = -\frac{2}{3\tau^2}
$$

$$
\frac{H}{\dot{H}} = \frac{-2/(3\tau)}{-2/(3\tau^2)} = \tau
$$

$$
\zeta^{(\rm grow)} = -C_2 \tau^{-5/3} - \tau \left[\frac{5}{3} C_2 \tau^{-8/3} + \left(-\frac{2}{3\tau}\right) C_2 \tau^{-5/3}\right]
$$

$$
= -C_2 \tau^{-5/3} - \tau \left[\frac{5}{3} C_2 \tau^{-8/3} - \frac{2}{3} C_2 \tau^{-8/3}\right]
$$

$$
= -C_2 \tau^{-5/3} - \tau \cdot C_2 \tau^{-8/3}
$$

$$
= -C_2 \tau^{-5/3} - C_2 \tau^{-5/3}
$$

$$
= -2 C_2 \tau^{-5/3}
$$

So the growing mode of zeta is:
$$
\boxed{\zeta^{(\rm grow)} = -2 C_2 \tau^{-5/3} \propto a^{-5/2}}
$$

Wait — let me double-check by working in terms of a. We have a proportional to tau^{2/3}, so tau proportional to a^{3/2}. Then:

zeta^{grow} proportional to tau^{-5/3} = a^{-5/2}

Hmm, but from the Mukhanov-Sasaki analysis: zeta_k proportional to 1/eta^3 = 1/tau^3 (since we defined eta = -tau in the previous analysis... actually let me be careful).

The conformal time relation: a proportional to eta^2 where eta < 0. Setting eta = -tau_c (tau_c > 0), we get a proportional to tau_c^2. But the cosmic time relation: a proportional to tau^{2/3} where tau = -t > 0.

The discrepancy: from the Mukhanov variable analysis, zeta^grow proportional to eta^{-3} = tau_c^{-3} (conformal). From the Bardeen analysis above, zeta^grow proportional to tau^{-5/3} (cosmic).

Are these consistent? tau (cosmic) and tau_c (conformal) are related by d tau_c = dt/a, so:
tau_c = integral dt/a = integral tau^{-2/3} d(-tau) proportional to tau^{1/3}

So tau proportional to tau_c^3, and:
tau^{-5/3} proportional to (tau_c^3)^{-5/3} = tau_c^{-5}

But we said zeta^grow proportional to eta^{-3} = tau_c^{-3} from the Mukhanov analysis.

**DISCREPANCY: tau_c^{-5} vs tau_c^{-3}.**

This needs resolution. Let me recheck.

From Mukhanov-Sasaki: v_k'' + (k^2 - z''/z) v_k = 0 with z = a sqrt(3), z''/z = 2/eta^2.

Growing mode of v_k: v_k proportional to 1/eta (conformal).
zeta_k = v_k/z = (1/eta) / (a_0 sqrt(3) eta^2) = 1/(a_0 sqrt(3) eta^3)

So zeta proportional to eta^{-3} (conformal).

Now converting: a proportional to eta^2, so eta proportional to a^{1/2} proportional to tau^{1/3}.
zeta proportional to eta^{-3} = tau^{-1}.

From Bardeen: zeta^grow = -2 C_2 tau^{-5/3}.

**These don't match (tau^{-1} vs tau^{-5/3}).** There is an error somewhere. Let me recheck the Bardeen equation.

Actually, the superhorizon equation for Phi during matter domination is:
$$
\ddot{\Phi} + \frac{2(2+3w)}{3(1+w)t}\dot{\Phi} = 0
$$

For w = 0: coefficient is 2*2/(3*1*t) = 4/(3t)... wait, that's what I had: ddot{Phi} + 4H dot{Phi} = 0 with H = 2/(3t), giving 4H = 8/(3t).

Actually let me redo this. The exact superhorizon equation for Phi in a matter-dominated universe:

From Bardeen (1980) or Mukhanov et al.: for k -> 0, the growing mode of Phi in an expanding matter-dominated universe (a proportional to t^{2/3}, t > 0) is CONSTANT. The decaying mode goes as t^{-5/3}.

**In contraction (t < 0, a proportional to (-t)^{2/3}):** The "decaying" mode of expansion becomes the GROWING mode of contraction (because t -> 0^- makes t^{-5/3} grow).

But the standard result for EXPANDING matter domination: Phi has modes Phi = const (growing in expansion) and Phi proportional to t^{-5/3} (decaying in expansion).

The corresponding zeta:
- For the constant Phi mode: zeta = -(5/3) Phi = const. [This is the standard conserved mode]
- For the t^{-5/3} Phi mode: zeta from this mode needs careful calculation.

In the EXPANDING case, the zeta corresponding to the decaying Phi mode is zero (this is the adiabatic decaying mode — it corresponds to a purely temporal gauge artifact).

But in CONTRACTION, this "decaying" Phi mode becomes growing, and the corresponding zeta is not zero.

**THE ISSUE:** The relationship between the Bardeen Phi modes and the zeta modes is more subtle than I computed above. The growing mode of zeta (from Mukhanov-Sasaki) does NOT correspond simply to the growing mode of Phi.

**THIS IS EXACTLY THE SUBTLETY THAT MAKES THE f_NL CALCULATION NONTRIVIAL.**

Let me note this as a critical checkpoint and move to the correct approach.

---

## Correct Approach: Work Directly with zeta

Instead of going through Phi, work directly with the nonlinear evolution equation for zeta in the gradient expansion.

### The nonlinear zeta equation (Lyth & Rodriguez 2005):

On superhorizon scales, to leading order in the gradient expansion:

$$
\dot{\zeta} = -\frac{H}{\rho + P} \delta P_{\rm nad}
$$

where delta P_nad is the non-adiabatic pressure perturbation.

For a single adiabatic fluid (dust): delta P_nad = 0. Therefore:

$$
\dot{\zeta} = 0 \quad \text{(linear, adiabatic, single-field)}
$$

**But this contradicts the known growing mode!**

The resolution: the growing mode of zeta is a DECAYING adiabatic mode in the expanding picture that becomes growing in the contracting picture. In the gradient expansion, this mode corresponds to a deviation from the attractor solution — it is a homogeneous solution of the perturbation equation that is NOT captured by the standard "zeta = constant" result.

**The standard "zeta is conserved" theorem applies to the PARTICULAR solution (the attractor).** The growing mode is the HOMOGENEOUS solution that deviates from the attractor. In expansion, it decays and becomes irrelevant. In contraction, it GROWS and dominates.

### The correct framework: second-order perturbation theory in conformal time

For a scalar field with V = m^2 phi^2/2, the growing mode of zeta arises from the interplay between the scalar field kinetic and potential energy that is not captured by the perfect-fluid approximation.

**Key insight:** The "dust" approximation (w = 0 exactly, perfect fluid) does NOT have a growing mode of zeta. The growing mode comes from the SCALAR FIELD dynamics — specifically, the difference between the scalar field and a perfect fluid at the perturbation level.

This means we CANNOT use the perfect-fluid gradient expansion. We must use the scalar-field formulation.

---

## Revised Path A: Scalar Field Gradient Expansion

### The setup:
Canonical scalar field phi with V(phi) = (1/2) m^2 phi^2.

On superhorizon scales, each spatial patch evolves as a separate FRW universe with scalar field:

$$
\ddot{\phi} + 3H\dot{\phi} + m^2 \phi = 0
$$

$$
H^2 = \frac{1}{3M_{\rm Pl}^2}\left(\frac{1}{2}\dot{\phi}^2 + \frac{1}{2}m^2\phi^2\right)
$$

### The separate-universe approach:

Perturb the initial conditions: phi(t_i, x) = phi_0(t_i) + delta phi(x), dot{phi}(t_i, x) = dot{phi}_0(t_i) + delta dot{phi}(x).

The curvature perturbation at a later time t is:

$$
\zeta(t, \mathbf{x}) = \delta N = N(\phi_0 + \delta\phi, \dot{\phi}_0 + \delta\dot{\phi}; t) - N(\phi_0, \dot{\phi}_0; t)
$$

To second order:
$$
\zeta = N_{,\phi}\delta\phi + N_{,\dot{\phi}}\delta\dot{\phi} + \frac{1}{2}N_{,\phi\phi}(\delta\phi)^2 + N_{,\phi\dot{\phi}}\delta\phi\delta\dot{\phi} + \frac{1}{2}N_{,\dot{\phi}\dot{\phi}}(\delta\dot{\phi})^2
$$

### The growing mode origin:

In the matter-like regime (m >> H, field oscillating), the growing mode of zeta comes from the PHASE perturbation of the oscillating field. Two neighboring patches with slightly different initial phi or dot{phi} will oscillate with slightly different phases, and this phase difference grows as the Hubble rate changes.

Specifically: if phi = A(t) sin(mt + theta), then a perturbation delta theta leads to a growing zeta.

### The key calculation:

The nonlinear delta-N to second order, INCLUDING the growing mode, requires solving the perturbed Klein-Gordon + Friedmann system to find how N depends nonlinearly on the initial data (delta phi, delta dot{phi}).

**For the growing mode contribution:** the second-order zeta depends on (zeta^{(1)})^2 with a specific coefficient. This coefficient IS f_NL (up to the 5/6 or 3/5 factors from convention).

### The structure:

$$
\zeta = \zeta^{(1)} + \frac{3}{5} f_{\rm NL} (\zeta^{(1)})^2 + ...
$$

where zeta^{(1)} includes the growing mode. The coefficient f_NL comes from the ratio of the second-order to (first-order)^2 contributions.

---

## Execution Plan for Path A

### Step A1: Solve the linear perturbation for the oscillating scalar field
- Verify the growing mode zeta proportional to tau^{-1} (or equivalently eta^{-3})
- Identify the mode function normalization

### Step A2: Set up the second-order separate-universe equations
- Perturb (phi, dot{phi}) to second order
- Solve Friedmann + Klein-Gordon at second order in the perturbation
- Track both growing and constant modes

### Step A3: Extract the quadratic coefficient
- Compute zeta^{(2)} sourced by (zeta^{(1)})^2
- Identify the coefficient in zeta^{(2)} = (3/5) f_NL (zeta^{(1)})^2
- This gives f_NL

### Step A4: Cross-check
- Verify scale-invariance of the power spectrum at first order
- Verify that f_NL is a pure number (no time or k dependence at leading order)
- Compare with -35/8

---

## Critical Subtlety Identified

**The growing mode of zeta in the matter bounce is NOT a fluid mode — it is a scalar-field mode.** The perfect-fluid approximation (w = 0 dust) gives zeta = constant on superhorizon scales. The growing mode arises from the scalar field's internal dynamics (phase perturbation of oscillations).

This means:
1. A fluid-based gradient expansion WILL NOT capture the growing mode
2. The scalar-field separate-universe approach MUST be used
3. The m/H ratio matters (the growing mode depends on the scalar field being in the oscillating regime)
4. The f_NL calculation requires the nonlinear scalar-field dynamics, not just the nonlinear fluid dynamics

**This is likely the reason the naive delta-N calculation (branch_V) got 5/12 — it used fluid-like assumptions that miss the growing mode entirely.**
