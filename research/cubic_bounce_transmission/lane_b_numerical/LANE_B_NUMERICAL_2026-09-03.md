# Lane (b) — numerical in-in evaluation of Δf_NL^bounce on the A2 backgrounds

**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` item #2, second half. Lane (a) =
`../lane_a_vertex_table/` (vertex table + regularisation prescription); lane (c) = model-specific
(Horndeski / dressed-metric) vertex corrections, separate and **not** done here.
**Date:** 2026-09-03 · **Venue:** local CPU (numpy/scipy) · **Cost:** $0 · **Wall clock:** 4 s.
**Artifacts (this directory):** `bounce_cubic_inin.py` → `bounce_cubic_inin.log`, `results.json`,
`dfnl_bounce_{quintin,lqc,poly}.png`; manifest
`reproducibility/manifests/experiments/p2-a2-lane-b-numerical-inin.json`.
**Provenance rule:** every number in §2–§6 is emitted by the committed script. `f_NL^before = −35/16`
(matter contraction, ledger #1) is an **input**, never recomputed. Nothing is tuned to any target.

## 1. What was computed

1. **Mode functions.** `μ'' + (k² − a''/a)μ = 0` integrated (DOP853, rtol 1e−11) from the A2 §4
   adiabatic vacuum — the *exact* matter-basis solution `e^{-iu}(1−i/u)/√(2k)` set at
   `η_i = −η_far`, growing-branch dominated (`|r| = 9A²I_∞/k³ ≫ 1`) — across the bounce on the three
   A2 backgrounds (`bg_quintin(dtB=1)`, `bg_lqc()`, `bg_poly(η_b=1)`), for `kη_B ∈ [10⁻³, 0.3]`.
   Scheme **S1** (geometric, `z = a`), so `ζ = μ/a`, `ζ' = (μ' − μ a'/a)/a`.
2. **In-in, every vertex.** Squeezed isoceles `k₁ = 0.02 k`, `k₂ = k₃ = k`, lab convention
   `B = −2 Im[u₁u₂u₃(η_*) ∫dη c_V^conf(η) Σ_{σ∈S₃} K_V(σ) ∏_j T_j[u*_{σj}(η)]]`,
   `f_NL = (5/6)B/(P₁P₂+P₁P₃+P₂P₃)`, all 3! attachments counted once, no hand symmetry factors
   (adjudication engine §1). Bulk window `[−η_B, +η_B]` (the NEC-violation window). Vertices V1–V7
   in S1 (`ε_eff = 1/2`, `c_s = 1`, `η_sr = 0`, `s = 0`, `λ = 0`), with the Fourier kernels derived in
   the script header from `χ̃ = ∂⁻²ζ̇ ⇒ χ̃_k = −ζ̇_k/k²`:
   V2 `K=1`; V3 `−(k_j·k_l)`; V4 `+(k_j·k_l)/k_l²`; V6 `(k_i·k_j)/k_j²`; V7 `k_i²(k_j·k_l)/(k_j²k_l²)`.
   V1 and V5 have **identically zero coefficients in S1** (`c_s=1, λ=0`; `η̇_sr = 0`).
3. **Redefinition/boundary terms R1–R4** evaluated at a post-bounce `η_*` with the numerically
   evolved modes (`R1 = 0` in S1 since `η_sr = 0`).
4. **Tests:** η_*-independence, window sensitivity, step-size convergence, Wronskian and
   normalisation gates. **S2** reported only as a divergence.

## 2. Gates (all pass)

| gate | result |
|---|---|
| Wronskian `Im(μ* μ') = −1/2` | `−0.50000000` on every leg, every k, every background |
| local redefinition `Fζ² ⇒ f_NL = (5/3)F` | exact to `<1e−12` (script assertion) |
| triangle closure `Σ_j k_i·k_j = 0` | residual `<1e−12` |
| step-size convergence (bulk, 1001→16001 pts) | rel. change `1.5e−8` (Quintin), `6.3e−12` (LQC), `2.1e−13` (poly) |
| numeric vs closed-form-mode evaluation | agree to `≤1e−3` at `kη_B ≤ 3×10⁻³` |

## 3. Results — Δf_NL^bounce per vertex (bounce window, scheme S1)

Headline row `kη_B = 10⁻³`, `η_* = 50 η_B` (`J(η_*)/I_∞ > 0.999`, `kη_* = 0.05`):

| vertex | Quintin (ρ_B=0.670) | LQC dust (ρ_B=1/2) | poly (ρ_B=0.609) |
|---|---|---|---|
| V1 `ζ̇³` | 0 (coefficient ≡ 0 in S1) | 0 | 0 |
| **V2 `ζζ̇²`** | **−0.139586** | **−0.104198** | **−0.126879** |
| V3 `ζ(∂ζ)²/a²` | +2.1e−07 | +3.2e−07 | +2.4e−07 |
| V4 `ζ̇∂ζ∂χ̃` | −6.45e−05 | −6.70e−05 | −5.56e−05 |
| V5 `ζ²ζ̇` | 0 (coefficient ≡ 0 in S1) | 0 | 0 |
| V6 `∂ζ∂χ̃∂²χ̃` | +8.06e−06 | +8.38e−06 | +6.95e−06 |
| V7 `∂²ζ(∂χ̃)²` | +7.34e−06 | +6.27e−06 | +6.55e−06 |
| **bulk sum** | **−0.139635** | **−0.104250** | **−0.126921** |
| R2 `ζζ̇/H` | −1.79e−04 | −3.67e−05 | −1.87e−04 |
| R3 (geometric gradient) | −1.11e−07 | −1.16e−07 | −1.05e−07 |
| R4 `ε∂ζ∂χ̃/H` | −5.15e−06 | −2.40e−05 | −2.71e−06 |
| **TOTAL Δf_NL^bounce** | **−0.13982** | **−0.10431** | **−0.12711** |

* **V2 dominates at the 99.95–99.97 % level** on all three backgrounds. Its sign is negative
  (adds to |f_NL|) on all three, as lane (a) predicted.
* **V4's sign, which lane (a) left open, is negative** (same sign as V2) but its magnitude is
  `5×10⁻⁴` of V2 — the squeezed angular average `(k_j·k_l)/k_l²` suppresses it.
* **V6+V7 are positive** (opposite sign to V2, as lane (a) said) but their combined weight is
  `1.1×10⁻⁴` of V2, **not** the `1/8` that lane (a)'s pure-time rewrite estimate suggested. The
  `−(1/8)` weight assumes the whole `V6+V7 → −½a³ε³ζζ̇²` piece survives; the numerical angular
  average of the actual `∂ζ∂χ̃∂²χ̃` and `∂²ζ(∂χ̃)²` kernels in the squeezed isoceles configuration
  cancels it to four digits. **Lane (a)'s remark "the S1 pure-time total ≈ −(7/8)·(5/24)ρ_B" is
  therefore not confirmed; the correct S1 total is −(5/24)ρ_B to 0.2 %.**
* V3 is `(kη_B)²`-suppressed as expected (it rises to `+2.5×10⁻²` by `kη_B = 0.3`).
* Dependence on k across the valid band is `≤2×10⁻³` absolute (`results.json: dfnl_bounce_spread_over_k`).

## 4. Agreement with lane (a)

Lane (a)'s closed form `Δf_NL^bounce[V2, S1] = −(5/24)ρ_B`:

| background | lane (a) closed form | lane (b) numeric V2 | rel. difference |
|---|---|---|---|
| Quintin+2015-type | −0.139581 | −0.139586 | **3.3×10⁻⁵** |
| LQC dust (= −5/48 exactly) | −0.104167 | −0.104198 | **3.0×10⁻⁴** |
| poly analytic non-LQC | −0.126875 | −0.126879 | **3.4×10⁻⁵** |

**Confirmed.** The agreement is a genuine cross-check: lane (a) used a symbolic super-Hubble
reduction with `ζ = C₁ + C₂J` and the leading `|r|≫1` kernel; lane (b) uses numerically evolved
finite-k mode functions, the exact kernel, and all six S₃ attachments. The residual scales as
`(kη_*)²` and as `1 − J(η_*)/I_∞` (both quantified in `results.json`).

## 5. η_*-independence, window sensitivity, convergence

**η_*-independence** (`kη_B = 10⁻³`; bulk integrated `[−η_B, η_*]`, boundary terms at η_*), poly:

| η_*/η_B | 2 | 5 | 10 | 20 | 50 | 150 | 250 |
|---|---|---|---|---|---|---|---|
| bulk | −0.35479 | −0.34861 | −0.34797 | −0.34787 | −0.34777 | −0.34693 | −0.34526 |
| redefinition | +0.1852 | +0.01736 | +2.34e−3 | +2.65e−4 | −1.90e−4 | −1.88e−3 | −5.22e−3 |
| **total** | −0.16961 | −0.33125 | **−0.34563** | **−0.34760** | **−0.34796** | **−0.34881** | **−0.35048** |

The total is flat to **1.4 % (poly), 1.3 % (Quintin), 3.6 % (LQC)** for `η_* ≥ 10 η_B`; the `2η_B`
and `5η_B` rows are *not* flat, exactly as lane (a)'s regularisation note predicts (R2/R3/R4 are
singular at `H = 0`, so η_* must be placed well clear of the NEC window). **Partial pass:** the
construction is η_*-independent in its stated domain, not globally. Note this total (−0.348) is the
*bounce + expansion* contribution up to η_*; the bounce-window-only number of §3 (−0.127) is a
window decomposition, not an η_*-independent object.

**Two competing requirements** set the validity band: `J(η_*) → I_∞` needs η_* deep post-bounce,
while the super-Hubble treatment of the boundary terms needs `kη_* ≪ 1`. Both hold only for
`kη_B ≲ 10⁻²`; rows with `kη_* > 0.3` or `J_*/I_∞ < 0.99` are flagged `valid: false` in
`results.json` and shaded in the figures. At `kη_B = 0.3` the R2 term reaches `−1.7` and the
"total" is meaningless — that is horizon re-entry, not a bounce effect.

**Window sensitivity** (poly, `kη_B = 10⁻³`): bulk = −0.1079, −0.1269, −0.1604, −0.1794, −0.1964 for
windows `[−f,f]η_B` with `f = 0.8, 1, 1.5, 2, 3`. The bounce-window integrand does **not** vanish
outside the NEC window (it falls off as `1/a²`), so the split between "bounce" and "expansion" is a
definition tied to `η_B`, not a convergent isolation. Stated explicitly rather than hidden.

**Step size:** the bulk integral is converged at the `10⁻⁸`–`10⁻¹³` level by 1001 Simpson points.

## 6. Combined post-bounce prediction (scheme S1, validity `kη_B ≪ 1`)

`f_NL^after = T_{f_NL}·(−35/16) + Δf_NL^bounce`, with `T_{f_NL} = (1−ρ_B)/2` from A2 §4.1:

| background | `T_{f_NL}` | `T·(−35/16)` | `Δf_NL^bounce` | **`f_NL^after`** |
|---|---|---|---|---|
| Quintin+2015-type | 0.165005 | −0.360949 | −0.13982 | **−0.5008** |
| LQC effective dust | 0.250000 | −0.546875 | −0.10431 | **−0.6512** |
| poly analytic non-LQC | 0.195501 | −0.427659 | −0.12711 | **−0.5548** |

The intrinsic bounce term is **19–39 % of the transmitted contraction term and has the same
(negative) sign**, so it partially undoes the linear suppression but does not reverse it:
`|f_NL^after| = 0.50–0.65` versus `|T·(−35/16)| = 0.36–0.55` and `|f_NL^before| = 2.19`.
**In scheme S1 there is no "orders of magnitude" enhancement** in the super-Hubble band.

## 7. Scheme S2 — reported as a divergence, not a number

Excising `|η| < d_cut·η_B` from the effective-fluid V6+V7 bounce-window integrand
(`c^conf = ¾a²ε³`, two `ζ'` legs weighted `1/z²`, `z² = 2a²ε`) over `d_cut = 3×10⁻²…3×10⁻⁴`:

| background | fitted log–log slope |
|---|---|
| Quintin | **−1.0050** |
| LQC dust | **−1.0071** |
| poly | **−1.0072** |

i.e. a clean `d_cut^{-1}` divergence with **no `d_cut → 0` limit**, reproducing lane (a)'s predicted
even `t⁻²` pole scaling and the lab's linear-order `z²` pathology. **No regulated S2 value is
quoted.** Every number in §3–§6 is S1.

## 8. Assumptions and limits (unchanged from lane (a), plus lane (b)'s own)

(A1) `kη_B ≪ 1`; results outside the flagged validity band are reported but not used.
(A2) `P(X,φ)` cubic action only — Horndeski/Galileon terms of the actual Quintin+2015 Lagrangian are
absent (lane (c)).
(A3) The S1 cubic coefficients are lane (a)'s **scheme assumption** (`ε → 1/2`, `c_s → 1`), not the
dressed-metric `H₃` of Agullo–Bolliet–Sreenath 2017. The S1 total is therefore an order-of-magnitude
anchor with a definite sign, now with a *verified* magnitude and a *measured* vertex hierarchy.
(A4) Squeezed isoceles configuration only (`k₁/k = 0.02`; V2/V4/V6/V7 were checked to be
squeeze-independent from `k₁/k = 0.2` down to `0.001`).
(A5) First-order in-in; no loops, no backreaction; symmetric bounce.

## 9. Ledger status

Item #2's second half is **closed at the S1 level**: `Δf_NL^bounce` is computed, for every vertex, on
all three A2 backgrounds, agreeing with lane (a)'s analytic anchor to `3×10⁻⁵`–`3×10⁻⁴`, with a
scheme label, a stated validity band, and an explicit divergence statement for S2. What remains open
is **lane (c)** — whether the true dressed-metric/Horndeski cubic Hamiltonian changes the S1
coefficients enough to move `f_NL^after` outside `[−0.65, −0.50]`. The A2 brief §5 verdict
("not currently predicted at better than order-of-magnitude") is now narrowed: *within S1* the
prediction is `f_NL^after ≈ −0.5` to `−0.65`; the residual uncertainty is the scheme, not the integral.
