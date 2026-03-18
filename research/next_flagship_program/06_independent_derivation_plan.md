# 06: Independent Derivation Plan for f_NL in Matter Bounce

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Objective

Independently derive f_NL^local for the matter bounce to resolve three discrepancies:
1. Cai et al. (2009): f_NL = -35/8 = -4.375
2. Li & Brandenberger (2016) at c_s = 1: f_NL ~ -2.19
3. Quintin et al. (2015) citation: -35/16 = -2.1875

**Priority outcome:** Determine which value is correct — or whether a FOURTH value emerges from a clean independent calculation.

---

## Formalism Selection

### Option A: In-In (Maldacena) Formalism — Reproduce Cai et al. Directly

**Pros:** Direct comparison with the source. Uses the same framework. Can identify where discrepancies enter.
**Cons:** Complex calculation with six terms in the cubic action. Error-prone without numerical verification.

### Option B: Gradient Expansion (Salopek-Bond / Separate Universe)

**Pros:** Conceptually cleaner. Physical interpretation (each superhorizon patch evolves as a separate FRW universe). Fewer computational steps.
**Cons:** The standard delta-N formalism assumes zeta is conserved on superhorizon scales. In the matter bounce, zeta GROWS. Must use the EXTENDED gradient expansion that tracks the growing mode.

### Option C: Second-Order Perturbation Theory (Direct)

**Pros:** Avoids both the in-in integral subtleties and the delta-N pitfalls. Directly solves the second-order Einstein equations.
**Cons:** Technically demanding. Requires consistent gauge treatment at second order.

### DECISION: Use BOTH Option A (reproduce Cai) and Option B (gradient expansion) as cross-check.

The previous failed attempt used a naive delta-N approach (getting 5/12 — wrong). The correct gradient-expansion approach must account for the growing mode. Using both methods provides the most robust verification.

---

## Detailed Plan: Option A — In-In Reproduction

### Step 1: Background

Matter contraction in conformal time eta:
- a(eta) = a_0 (eta/eta_0)^2 for eta < 0 (eta -> 0^- at the bounce)
- H = a'/a^2 = 2/(a_0 eta_0^2) * eta_0^2 / eta^3 ... actually use:
  - In cosmic time: a(t) = a_0 (-t/t_0)^{2/3} for t < 0
  - H = 2/(3t) (negative for t < 0)
  - In conformal time: a = a_0 eta^2, H_conformal = a'/a = 2/eta

Slow-roll parameter:
- epsilon = -H_dot/H^2 = 3/2 (exact for w = 0)

### Step 2: Linear Mode Functions

Mukhanov-Sasaki variable v_k satisfies:
v_k'' + (k^2 - 2/eta^2) v_k = 0

General solution:
v_k(eta) = A_k (1 - i/(k*eta)) e^{-ik*eta} + B_k (1 + i/(k*eta)) e^{ik*eta}

In terms of Bessel functions: v_k proportional to sqrt(-k*eta) * H_{3/2}^{(1)}(-k*eta)

Superhorizon limit (|k*eta| << 1):
v_k -> c_1 * eta^2 + c_2 / eta (the 1/eta mode is GROWING as eta -> 0)

Curvature perturbation:
zeta_k = v_k / z, where z = a * sqrt(2*epsilon) / c_s = a * sqrt(3) (for epsilon = 3/2, c_s = 1)

So zeta_k = v_k / (a_0 sqrt(3) eta^2)

For the growing mode (v_k ~ c_2/eta): zeta_k ~ c_2 / (a_0 sqrt(3) eta^3)

**Checkpoint 1:** The scalar power spectrum should be scale-invariant: P_zeta proportional to k^{n_s - 1} with n_s = 1.

### Step 3: Cubic Action

Maldacena's third-order action for a canonical scalar with epsilon = 3/2:

S_3 = integral d^3x d eta a^2 epsilon [...terms...]

The terms (in Maldacena 2003 notation, adapted for contraction):

1. epsilon * a^2 * zeta * (zeta')^2
2. epsilon * a^2 * zeta * (partial_i zeta)^2
3. -2 * epsilon * a * zeta' * (partial_i zeta)(partial_i chi)
   where chi satisfies nabla^2 chi = a * epsilon * zeta'
4. (epsilon^2/2) * a^2 * (partial_i partial_j chi)^2 - ... (from field redefinition)
5. Boundary / field-redefinition terms proportional to d/d eta [...]

**Key difference from inflation:** All coefficients are O(1) or O(epsilon) = O(1), not O(epsilon) << 1. Every term contributes at comparable order.

### Step 4: Time Integral

For each term, compute:
I_n = integral_{-infinity}^{eta_B} d eta' (interaction kernel) * (product of three mode functions)

In inflation, this integral is dominated by horizon crossing. In the matter bounce, the growing mode means the integrand GROWS toward eta -> 0 (the bounce). The integral is dominated by LATE TIMES (near the bounce), not by horizon crossing.

**Critical subtlety:** The upper limit eta_B (bounce time) matters. In the Cai et al. calculation, eta_B is finite. The result depends on (k * eta_B) to some power. For k << 1/eta_B (superhorizon), these terms may contribute.

### Step 5: Bispectrum Assembly

Sum all six contributions. The total three-point function in terms of shape:
<zeta_{k1} zeta_{k2} zeta_{k3}> = (2pi)^3 delta(k1+k2+k3) * B(k1, k2, k3)

B(k1, k2, k3) = sum over terms of (coefficient) * (k-dependent factors) * P_zeta(k1) * P_zeta(k2) [+ permutations]

### Step 6: Squeezed Limit

Set k_1 << k_2 = k_3 = k:
B(k_1, k, k) -> f_NL^local * 4 * P_zeta(k_1) * P_zeta(k) * [(10/3) / something...]

Extract f_NL^local from the coefficient.

**Checkpoint 2:** Compare with Cai et al. Eq. 38-39.

### Step 7: Resolve Li-Brandenberger Discrepancy

Li & Brandenberger (2016) derive a general formula for arbitrary c_s. At c_s = 1:
f_NL ~ -165/16 + 65/8 = -10.3125 + 8.125 = -2.1875

This differs from -35/8 = -4.375 by a factor of 2.

**Possible explanations:**
1. Different normalization convention for f_NL
2. Li & Brandenberger's formula is approximate (labeled "~" in their paper)
3. Cai et al.'s |B|_NL is not exactly f_NL^local (shape correction)
4. One calculation has an error

**Resolution strategy:** Compute the full shape function at c_s = 1 using both papers' notation. Identify where the factor of 2 enters. Check whether it's a convention issue or a computational error.

---

## Detailed Plan: Option B — Gradient Expansion

### The Standard Delta-N Problem

The standard delta-N formula:
zeta = N(phi_i) - N_0

gives f_NL = (5/6) * N''(phi)/(N'(phi))^2

For a massive scalar in matter contraction:
N = integral H dt = ...

**The problem:** This formula assumes zeta is the CONSERVED quantity evaluated when a given mode exits the Hubble radius. In the matter bounce, zeta GROWS after Hubble exit. The standard formula gives the value AT Hubble exit, not the value that propagates to the bounce.

### Extended Gradient Expansion

The Salopek-Bond gradient expansion writes the metric as:
ds^2 = -dt^2 + e^{2 alpha(t,x)} gamma_{ij} dx^i dx^j

where alpha(t,x) satisfies the local Friedmann equation:
(alpha_dot)^2 = (1/3) rho(t,x) + (1/6) K e^{-2 alpha}

with K encoding the spatial gradient (curvature) of the perturbation.

**To second order:**
alpha = alpha_0(t) + alpha_1(t,x) + (1/2) alpha_2(t,x) + ...

The curvature perturbation:
zeta(t,x) = alpha(t,x) - alpha_0(t) = alpha_1 + (1/2) alpha_2 + ...

### The Growing Mode

In matter contraction, the linear perturbation alpha_1 has two modes:
- Constant mode (analog of the conserved zeta in inflation)
- Growing mode proportional to a^{-3/2} (i.e., t^{-1} or eta^{-3})

**The growing mode dominates.** This is why the standard delta-N (which tracks the constant mode) gives the wrong answer.

### Correct Gradient-Expansion Calculation

1. Solve the local Friedmann equation to SECOND ORDER in the gradient expansion, keeping the growing mode:

alpha_1(t,x) ~ C_g(x) * a(t)^{-3/2} + C_c(x) (growing + constant)

2. The second-order perturbation alpha_2 is sourced by quadratic products of alpha_1:

alpha_2 ~ C_g^2 * a^{-3} + C_g * C_c * a^{-3/2} + C_c^2

3. Since C_g >> C_c at late times (near the bounce), the dominant contribution is:

zeta^{(2)} ~ C_g^2 * a^{-3} (the square of the growing mode)

4. f_NL is:
f_NL = (5/6) * zeta^{(2)} / (zeta^{(1)})^2 = (5/6) * (coefficient of C_g^2 * a^{-3}) / (C_g * a^{-3/2})^2

5. The coefficient ratio depends on the exact form of the second-order local Friedmann equation.

**This is the cleanest route to an independent f_NL.** It requires careful algebra but no time integrals.

### Intermediate Checkpoints

| Checkpoint | Expected Result |
|-----------|----------------|
| Linear growing mode zeta^{(1)} proportional to a^{-3/2} | Known |
| Power spectrum P_zeta proportional to k^0 (scale invariant) | Known |
| Second-order source term quadratic in growing mode | Must verify |
| f_NL = -35/8 or -2.2 or something else | THE ANSWER |

---

## Where Convention Mistakes Previously Entered

The earlier 5/12 calculation in `branch_V_bounce_evidence/dust_bounce_spectrum/06_fNL_estimate.md` made these errors:

1. **Used inflationary slow-roll formula** N = phi^2/(4 M_Pl^2) — not valid for contraction
2. **Assumed phi_* = sqrt(2) M_Pl** — a slow-roll horizon-crossing relation
3. **Claimed f_NL^Phi = 1/4** — unsourced, appears fabricated
4. **Applied "conversion factor" (5/3)** — spurious (conventions match directly)
5. **Ignored the growing mode entirely** — the dominant effect in matter contraction

**Lesson:** Never apply inflationary formulas to a contracting background without checking whether zeta is conserved or growing. This is the single most common error in bounce cosmology calculations.

---

## Timeline Estimate

| Step | Estimated Effort |
|------|-----------------|
| Background + linear modes (Step 1-2) | 1 session |
| Cubic action assembly (Step 3) | 1-2 sessions |
| Time integral evaluation (Step 4) | 1-2 sessions |
| Bispectrum + squeezed limit (Step 5-6) | 1 session |
| Li-Brandenberger comparison (Step 7) | 1 session |
| Gradient expansion (Option B) | 1-2 sessions |
| Cross-check and reconciliation | 1 session |
| **Total** | **7-10 sessions** |

**The gradient expansion (Option B) is faster than the in-in reproduction (Option A) and should be attempted FIRST.** If it gives a clean answer, the in-in reproduction becomes a verification rather than a discovery.
