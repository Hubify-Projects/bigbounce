# Pre-registration — ledger row 9 residual / decision D-A3-9: is the S1/S2 transmission band physical?

**Lane:** `LS4-ledger9-scheme` · **Date written:** 2026-09-19 · **Status at writing: NO NUMBER HAS BEEN COMPUTED.**
This file is committed BEFORE the computation. Nothing below is adjusted after the fact; the outcome is
recorded against these criteria verbatim, including the INCONCLUSIVE branch.

## 0. The open problem (restated from the ledger, not re-scoped)

Ledger row 9 residual + decision D-A3-9: the transmitted amplitude through the bounce is scheme-dependent.
On the Quintin-type background, at `k eta_B <= 1e-2`, with `f_NL^before = -35/16 = -2.187`:

| scheme | linear ζ-equation | `|λ_ζ|` | `f_NL^after` | artifact |
|---|---|---|---|---|
| S1 "geometric / dressed-metric" | `z = a` (the TENSOR potential `a''/a`) | 6.06 | −0.501 | `A2_TRANSMISSION_BRIEF`, `lane_b_numerical` |
| S2 "effective fluid" | `z^2 = 2 a^2 eps / c_s^2`, `eps = -Hdot/H^2` | 0.970 | −1.249 | `lane9b2_s2_rawadm` |

Factor 2.5, traced by lane 9b-2 to the **linear** MS-variable choice through `H = 0`. A3M currently prints the
two-scheme band `f_NL^after ∈ [−1.25, −0.50]`. The remaining theory problem, in the ledger's own words:
*"a scheme-independent variable choice through H = 0."*

## 1. The criterion (formulated before computing)

Both S1 and S2 are choices of the variable in which the linear mode is propagated **through** `H = 0`. The
adjudication is therefore not "which ζ-equation do we prefer" but **"is there a variable whose evolution
equation is regular at every degenerate point of this class of background, contains no `z` and no `1/H`, and
determines ζ unambiguously in the asymptotic regions where ζ is well defined?"**

The candidate is the **Bardeen / longitudinal-gauge potential Φ**. Two degenerate points exist on any
matter-contraction → NEC-violating-bounce → matter-expansion background:

* **`H = 0`** (the bounce): `z_S2^2 = 2a^2 eps = -2 a^2 Hdot / H^2 → ∞`; the comoving lapse/shift `N_1 = ζdot/H`,
  `ψ ⊃ -ζ/H` are individually singular (lane 9b).
* **`rho + p = 0`**, i.e. `Hdot = 0` (the NEC crossing): `z_S2^2 = 0`; comoving and uniform-density slicings
  degenerate against each other. The Quintin-type parametrization AVOIDS this point by jumping `Hdot`
  discontinuously (`-3H^2/2 → +Υ`) at `|t| = t_m`; every *smooth* bounce with matter-like contraction must
  cross it.

Claim to be **verified symbolically, not assumed**: for a single minimally-coupled scalar (`c_s = 1`, arbitrary
`V(φ)`) on an arbitrary `a(η)`, the exact linearised Einstein equations give Φ a self-adjoint equation
`(μ Φ')' + μ (k^2 + 2H' - 2H^2) Φ = 0` with `μ = a^2/(H^2 - H') = -1/Hdot`, whose indicial exponents at a simple
zero of `Hdot` are `{0, 2}` (both regular) and which is manifestly regular at `H = 0` whenever `Hdot ≠ 0`.
If that holds, Φ is regular at BOTH degenerate points, involves no `z`, and is the scheme-independent variable.
ζ is then reconstructed from `(Φ, Φ')` by the exact constraint dictionary in the asymptotic matter phases,
where `rho + p ≠ 0` and ζ is unambiguous — so `λ_ζ^Φ ≡ ζ(+∞)/ζ(−η_h)` is a scheme-free number.

## 2. What will be computed (exactly this, no more)

* **Leg A (symbolic, sympy).** Derive from the exact linearised Einstein equations, for arbitrary `a(η)` and
  arbitrary `V`: (A1) the exact ζ-equation; (A2) the exact Φ-equation and its integrating factor `μ`;
  (A3) the exact algebraic ζ↔(Φ,Φ') dictionary; (A4) the junction condition implied by the self-adjoint form.
  Record which of S1/S2 (A1) reproduces and under what condition.
* **Leg B (numeric).** On the exact Quintin-type background already committed in
  `lane9b2_s2_rawadm.py::Quintin` (`Υ = 8/(3 δt_B^2)`, `t_m = δt_B/2`), at `k eta_B ∈ {1e-3, 3e-3, 1e-2}`:
  integrate the Φ equation from the matter-contraction adiabatic-vacuum mode through the bounce to the matter
  expansion, reconstruct ζ, and report `|λ_ζ^Φ|`.
* **Leg B′ (smoothed-junction control — the tiebreaker).** Replace the discontinuous `Hdot` at `|t| = t_m` by a
  smooth interpolation of width `δ` (so the background genuinely crosses `rho + p = 0`) and take `δ → 0`.
  A smooth background admits no junction prescription at all, so its limit selects the physical matching.
* **Gates (must pass, or the result is INCONCLUSIVE):**
  * **G1** matter-domination limit: the Φ equation must reduce to `Φ'' + (6/η)Φ' + k^2 Φ = 0` and its
    super-Hubble solution must be `Φ = const` with `ζ = (5/3)Φ` to ≤ 1e-6.
  * **G2** constant-`eps` control: on a power-law background (`eps` constant, no bounce) S1 and S2 coincide
    identically; the Φ route must reproduce their common `λ` to ≤ 1e-6.
  * **G3** Wronskian / flux conservation of the Φ system, conserved to ≤ 1e-8 across the bounce.
  * **G4** the smoothed control must converge: `|λ(δ)|` stable to ≤ 2 % over the last decade of `δ`.

## 3. Pre-registered outcome conditions

Let `L ≡ |λ_ζ^Φ|` (the scheme-free number), compared against S1 `6.06` and S2 `0.970`.

* **OUTCOME-S2** — `|L/0.970 − 1| ≤ 0.02` and `|L/6.06 − 1| > 0.02`, gates G1–G3 pass.
  → S2 is the consistent continuation; S1's `z = a` is not a solution of the Einstein equations on this
  background. The band **collapses to the S2 value** and A3M's headline `f_NL^after` moves from `−0.50` to
  `−1.25` on the Quintin-type background. **This is a headline change → the single blind Fable adjudicator is
  spawned before anything is propagated.**
* **OUTCOME-S1** — `|L/6.06 − 1| ≤ 0.02` and `|L/0.970 − 1| > 0.02`, gates pass.
  → S1 is the consistent continuation; the band collapses to the paper's current headline `−0.50`.
  No headline change; PROPAGATION_NOTE records the strengthening.
* **OUTCOME-NEITHER** — `L` differs from both by > 2 % with all gates passing.
  → both schemes are variable choices that do not solve the regular gauge-invariant evolution; the band is
  replaced by the computed `L` and its `f_NL^after`. Headline change → Fable adjudicator.
* **OUTCOME-BAND-IS-PHYSICAL** — the Φ route is shown to be *itself* non-unique through `H = 0` (e.g. G4 fails
  because the `δ → 0` limit does not exist, or the two junction prescriptions give a `λ` spread ≥ the S1/S2
  factor 2.5). → the band is a genuine physical ambiguity; D-A3-9 stands as-is, now with a *reason* rather
  than a placeholder. No headline change.
* **INCONCLUSIVE / KILL** — any of G1–G3 fails, or the numerics do not converge (step/tolerance spread > 2 %),
  or the background hits a degeneracy not anticipated here. → recorded as a null; the band stands unchanged;
  the failing gate is named. **A null is an acceptable and publishable outcome of this lane.**

## 4. Integrity constraints binding this lane

* No number is quoted that was not produced by the committed script in this directory.
* Literature statements are cited, never re-derived from memory; ABS/AAN claims are taken only from the
  source-cited readings already committed in `lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md`.
* Nothing is steered toward either scheme. The INCONCLUSIVE branch is a real outcome, not a fallback.
* The A3M manuscript, SSOT, site data and Convex are NOT touched by this lane; the only cross-lane output is
  `PROPAGATION_NOTE.md` containing exact printable sentences for the A3M lane to accept or reject.
