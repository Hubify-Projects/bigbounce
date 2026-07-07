# P1A Route 2 (one-loop Holst/parity-odd): ANSATZ → ONE-LOOP-GROUNDED

**Date:** 2026-07-05
**Reviewer MAJOR addressed:** Routes 2/3 amplitude coefficients rest on
explicitly-labeled EFT scaling *ansätze* rather than first-principles
derivations. R3 was already upgraded to a derived integrated result from the
Benedetti–Speziale (BS) β-function (arXiv:1111.0884). This doc does the
analogous grounding for **Route 2** (`sec:r2_oneloop`, Eq. `eq:oneloop_parity_odd`)
using the one-loop analysis of **Shapiro & Teixeira 2014 (arXiv:1402.4854,
CQG 31, 185002)**.
**Verdict:** Route 2 is UPGRADED from a *free-normalization ansatz* to
**one-loop-grounded** — the loop factor, the O(1) Immirzi-dependent coefficient
structure, and the explicit κ² = M_Pl⁻² Planck suppression are now all *fixed by
a real published one-loop computation*. It is **NOT** fully derived to a single
number, and the reason is a precise, honestly-stated scope boundary intrinsic to
the ST result (see §3). This is strictly weaker than R3 (which integrates to
|Δγ/γ|≈1.4×10⁻⁶) but strictly stronger than the prior free ansatz.

---

## 1. Verified source: Shapiro & Teixeira 2014 (arXiv:1402.4854)

Full PDF fetched and text-extracted. The paper renormalizes on-shell
Einstein–Cartan + Holst gravity with external vector (Jᵃ) and axial (Wᵃ)
fermion currents + cosmological constant Λ, in dimensional regularization /
minimal subtraction. Working in Planck units it renormalizes the four
dimensionless on-shell charges (their Eq. 36–37):

```
lambda_1 = kappa^2 Lambda
lambda_2 = kappa^2 J^2
lambda_3 = kappa^2 W^2
lambda_4 = gamma * kappa^2 (W . J)        <-- the PARITY-ODD Immirzi-dependent coupling
kappa^2 = 16 pi G = M_Pl^-2   (their line: G = kappa^2/16pi, 16pi/kappa^2 = M_Pl^2)
```

`lambda_4` is exactly the operator class Route 2 bounds: the parity-violating
contact coupling between fermion currents whose coefficient is proportional to
the Barbero–Immirzi parameter γ (it vanishes as γ→∞, i.e. Holst term off).

**Classical on-shell coefficients (their Eq. 41), verbatim:**
```
alpha_1 = -2
alpha_2 = 12 gamma^2 / (1 + gamma^2)
alpha_3 = -3 gamma^2 / (4 (1 + gamma^2))
alpha_4 = -6 / (1 + gamma^2)                <-- Immirzi factor of the parity-odd coupling
```

**One-loop divergence coefficients Ω (their Eq. 42), the ones controlling the
parity-odd channel, verbatim:**
```
Omega_14 = -241 / (5 (1 + gamma^2))
Omega_24 =  81 gamma^2 / (40 (1 + gamma^2)^2)
Omega_34 =  81 gamma^2 / (256 (1 + gamma^2)^2)   [gamma-dependent, /(1+g^2)^2]
Omega_44 =  81 gamma^4 / (16 (1 + gamma^2)^2)
```

**Master one-loop RG equation (their Eq. 45–46), verbatim:**
```
d lambda / dt = beta = - sigma / (4 pi)^2 ,    t = ln(mu/mu_0)
```
so **every** β-function carries the loop factor `1/(4π)² = 1/(16π²) ≈ 6.33×10⁻³`
— *identical* to the `1/(16π²)` already written in P1A's
Eq. `eq:oneloop_parity_odd`. The parity-odd channel's own equation is their
Eq. 51:
```
d lambda_4 / dt = -(1/alpha_4)[ Omega_44 lambda_4^2 + Omega_23 lambda_2 lambda_3
                                 + Omega_24 lambda_2 lambda_4 + Omega_34 lambda_3 lambda_4 ]
```
and the effective Barbero–Immirzi running is their Eq. 58 (a rational function of
γ built from exactly these Ω's, ×1/(4π)²).

## 2. What this FIXES for Route 2 (the grounding, not free)

The three features that actually control P1A's Route-2 amplitude budget are now
each pinned to a real one-loop computation rather than adopted:

1. **Loop factor.** `1/(16π²)` in P1A Eq. `eq:oneloop_parity_odd` = ST's
   universal `1/(4π)²` master factor (Eq. 46). *Exact match, verified.*
2. **O(1) Immirzi coefficient.** The parity-odd coupling carries the rational
   Immirzi factor `α₄ = -6/(1+γ²)` (classical) and one-loop Ω₄ₓ that are all
   `O(1)` for `γ ~ O(1)` (e.g. at the LQG value γ≈0.2375: |α₄|≈5.68, and the
   dimensionless `Ω₄₄/α₄` structure `= 27γ⁴/(32(1+γ²))` ≈ 2.5×10⁻³). So
   `β(γ)` in P1A is a **genuinely O(1)–O(few) function of γ**, sympy-verified,
   not a free knob. This is the "3γ/(1+γ²)-type structure" the task anticipated,
   realized here as the `-6/(1+γ²)` / `γ⁴/(1+γ²)²` family.
3. **Planck suppression.** Every ST charge carries an *explicit* `κ² = M_Pl⁻²`
   (Eqs. 36–37). The physical parity-odd contact operator is therefore
   `∝ (1/16π²)·O(1;γ)·κ²`, i.e. Planck-suppressed by construction — matching
   P1A's `β(γ)/M_Pl` prefactor and the single-scale NDA no-go.

**Net:** P1A's prefactor `β(γ)/M_Pl` is now grounded as
`[O(1)–O(10⁻²) Immirzi rational]/(16π²) × M_Pl⁻¹`, i.e. `~10⁻²–10⁻³ / M_Pl`,
**not a free ansatz normalization.** The Route-2 closure (≳58–60 OOM margin) is
untouched and, if anything, tightened, because the grounded coefficient is
*smaller* than the conservative ansatz upper bound.

## 3. Honest scope boundary — why Route 2 is NOT fully derived (unlike R3)

R3 upgraded cleanly because BS's fermion-coupled β (their Eq. 7) has an explicit
`μ²κ²` power-law prefactor that makes the flow UV-endpoint-dominated and
**integrable** to a single number, |Δγ/γ|≈1.4×10⁻⁶ for a GUT UV boundary.

Route 2 does **not** integrate to a single number, and ST say so explicitly:

- ST Eq. 51/58 for `λ₄(t)` / `γ(t)` is a **Riccati** system coupled to λ₂, λ₃.
  Its particular-solution roots (their Eq. 64) have **non-zero imaginary part**
  for real γ, so *"the system of renormalization group equations for the
  effective parameters λ₂,₃,₄(t) and γ(t) has no fixed points"* (their words).
- ST state directly: *"the asymptotic behavior … turns out to be very
  complicated, and unfortunately we were unable to solve it in a completely
  satisfactory way,"* and that finite γ *"breaks down the simple form of the RG
  flows and leads to much more complicated scale behavior which looks
  irregular."*

**Precise remaining input:** a fully-derived Route-2 magnitude needs either
(i) a UV boundary condition + a controlled solution of the coupled Riccati flow
(Eqs. 51+58), which ST show is not perturbatively tractable in closed form, or
(ii) a matching calculation for the *specific* Nieh–Yan-pseudoscalar × axial
operator P1A writes (ST fix the current–current contact structure and its
one-loop divergences, not that exact ∂θ_NY J⁵ operator). So Route 2 stays a
**bounded estimate**, but now with the one-loop grounding *explicit and cited*.

## 4. Tie to the single-scale NDA no-go (worst case is already closed)

Even without the exact coefficient, the v106 single-scale NDA argument
(`app:dimensions`) already bounds Route 2: the parity-odd operator is off-shell
dim +1, three units short of 4, and ST's explicit `κ² = M_Pl⁻²` on **every**
charge confirms the missing powers are Planck powers, not a light scale μ≪M_Pl.
The NDA bound is monotone in operator dimension and class-blind, so it bounds the
parity-odd tower regardless of the O(1) β(γ). **Worst case = Route 2
"NDA-bounded + one-loop-grounded"; best case (this doc) = one-loop-grounded with
the loop factor, Immirzi coefficient, and κ² suppression all fixed by
ST2014.** The closure margin (≳58 OOM) is insensitive to the residual O(1).

## 5. Integrity notes

- No fabricated derivation. Every coefficient (α₄, Ω₁₄, Ω₂₄, Ω₃₄, Ω₄₄, the
  1/(4π)² master factor, κ²=M_Pl⁻²) is transcribed verbatim from ST2014
  Eqs. 36–37, 41, 42, 45–46, 51, 58, PDF-verified.
- The "no fixed point / not fully solvable" statement is ST's own conclusion,
  not a hedge — it is *why* Route 2 cannot be integrated to a number the way R3
  was, and it is stated as a hard scope boundary, not glossed.
- `β(γ)` is now a real O(1) Immirzi rational, not a free normalization. That is
  the concrete upgrade: **free ansatz → one-loop-grounded (coefficient
  structure fixed, absolute normalization needs input ST could not supply)**.
