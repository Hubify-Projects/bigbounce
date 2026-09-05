# Row 15b — Entropy (spectator) sector through the A2 matter-bounce backgrounds

**Status:** IN PROGRESS (plan header committed 2026-09-04)
**Parent:** ledger row 15 (curvaton dilution factor ℱ) — named open item:
"ℱ needs an entropy sector in the A2 backgrounds."

## Plan

1. Evolve a spectator field δσ (massless, then light m² ≪ H_B²) on each of the
   three A2 backgrounds (Quintin, LQC-dust, poly) with adiabatic-vacuum ICs:
   u'' + (k² − a''/a + a² m²) u = 0. Extract the bounce transfer λ_σ(k).
2. Compare λ_σ against the adiabatic scalar λ_ζ (schemes S1, S2) and the tensor
   λ_T. Test the structural claim: a massless spectator shares the tensor's
   pump term a''/a, so λ_σ = λ_T exactly, and the σ/ζ amplitude ratio is
   preserved through the bounce in S1 (λ_ζ^S1 = λ_T) but rescaled by
   λ_T/λ_ζ^S2 in S2.
3. Convert row 15's requirement ℱ ≥ 25.8 (i.e. r < 0.036 with r = 24/[1 +
   (4/3) r_dec² (M_pl/σ_*)²], threshold r_dec M_pl/σ_* > 22.34) into a
   PRE-bounce condition on σ_* and r_dec, per background × scheme.
4. State (not compute) which cubic vertices apply to a spectator, i.e. whether
   the curvaton's intrinsic f_NL inherits the same Δf_NL^bounce structure.
5. Check the surviving discriminator n_T = n_s − 1 = −0.035: is λ_T
   k-dependent across the observable band (row 18a λ_T(kη_B) values)?

**Never tune.** All parameters are inherited from the A2 background definitions
and row 15; no fit factors are introduced.

## Outputs
- this .md (derivation, table, verdict, paper-ready sentences)
- row15b_entropy_sector.py + results.json + .log + .png
- manifest registered in programs/bounce-theory.json
- ledger row 15 status update (≤5 lines)

---

# Results (2026-09-04; every number from `row15b_entropy_sector.py` / `results.json`)

**Status: DONE. Row 15's named open item is closed at the level it can honestly be
closed: the entropy sector's *transfer* through all three A2 backgrounds is now
computed, and it is identical to the tensor's. The consequence is that the curvaton
viability condition is a purely PRE-bounce statement — the bounce neither helps nor
hurts it — and it is the same in both scalar schemes.**

## 1. The operator identity, and why it makes the transfer trivial

A spectator `\sigma` with `m^2 \ll H^2` and canonical kinetic term has `u = a\sigma`
obeying

```
u'' + (k^2 - a''/a + a^2 m^2) u = 0                                   (row 15b)
```

The tensor polarisation `h` has `v = a h` obeying `v'' + (k^2 - a''/a) v = 0`, and the
adiabatic `\zeta` in **scheme S1** (geometric / dressed-metric, `z = a`, `c_s = 1`) has
`\mu = a\zeta` obeying the same. For a massless spectator the three pump terms are
*literally the same function* `a''/a`, so

```
\lambda_\sigma(k)  =  \lambda_T(k)  =  \lambda_\zeta^{S1}(k)      identically (S1)
```

This is an operator identity, not a coincidence: nothing about the bounce
distinguishes a test scalar from a graviton polarisation once both are canonically
normalised on `z = a`. **In scheme S2** (fluid Mukhanov–Sasaki, `z^2 = 2a^2\epsilon/c_s^2`)
the adiabatic variable's pump term is `z''/z \neq a''/a` and the spectator's is
unchanged, so there the spectator still tracks the *tensor*:

```
\lambda_\sigma  =  \lambda_T ,        \Lambda \equiv \lambda_T/\lambda_\zeta \ne 1  (S2)
```

## 2. Numerical verification on all three A2 backgrounds

Both fields are seeded with the **exact** pre-bounce matter mode
`e^{-ik\tau}(1 - i/k\tau)/\sqrt{2k}` (exact for all `k\tau` in a matter era, so no
sub-Hubble requirement), integrated across a symmetric window `\eta \in [-20\eta_B,
+20\eta_B]`, and read out as `\sigma = u/a`, `h`. The tensor uses an **independent**
first-order formulation `h' = \Pi/a^2`, `\Pi' = -a^2k^2h` with `\Pi = a^2h'`, so the
comparison is a real numerical test rather than the same integration twice.

| background | `k\eta_B` | `\lambda_\sigma` | `\lambda_T` | `\lambda_\sigma/\lambda_T - 1` |
|---|---|---|---|---|
| Quintin-type | 0.001 | 4339.806 | 4339.461 | `+8.0\times10^{-5}` |
| Quintin-type | 0.01 | 4226.094 | 4225.757 | `+8.0\times10^{-5}` |
| LQC-eff.-dust | 0.001 | 1016.2634 | 1016.2634 | `+5.5\times10^{-10}` |
| LQC-eff.-dust | 0.01 | 987.2718 | 987.2718 | `+5.5\times10^{-10}` |
| poly-analytic | 0.001 | 7325.0155 | 7325.0155 | `+7.1\times10^{-10}` |
| poly-analytic | 0.01 | 7152.0412 | 7152.0411 | `+2.8\times10^{-9}` |

(The absolute `\lambda` depends on the window — it is the growing-mode amplification
between `-20\eta_B` and `+20\eta_B` — so these numbers are **not** comparable to row 18a's
`\lambda_T = 6.06`, which is measured from the NEC boundary to `50\eta_B`. Only the
*ratios* are physical, and they are window-independent.)

The Quintin residual `8\times10^{-5}` is a numerical floor of that background's
piecewise `t`-sampled arrays (it is `k`-independent to 3 digits, which a physical
effect would not be); LQC and poly reach `10^{-9}`, consistent with the analytic
identity and with row 14's `|\lambda_{scalar}/\lambda_{tensor}-1| \le 4\times10^{-11}`.

**Light mass.** `\Delta\lambda_\sigma/\lambda_\sigma` scales as `(m\eta_B)^2` and vanishes
smoothly: on Quintin, `-4.2\times10^{-7}` at `m\eta_B = 10^{-6}`, `-4.2\times10^{-5}` at
`10^{-5}`, `-4.2\times10^{-3}` at `10^{-4}`, `-0.37` at `10^{-3}`. The massless result is the
`m\eta_B \to 0` limit, and the departure at `m\eta_B \gtrsim 10^{-3}` is not a defect of the
transfer: over a window reaching `20\eta_B` the expansion has driven `H` down to
`\sim m`, which is exactly the epoch at which the curvaton *begins to oscillate* — the
physics that generates `\mathcal{F}` in the first place, and which happens well after the
bounce.

## 3. Background × scheme table and the pre-bounce viability condition

With `P_h/P_{\zeta,ad}|_{pre} = 24` (row 10) and `P_{\zeta,curv}/P_{\zeta,ad}|_{pre} =
(4/3)X^2`, `X \equiv r_{dec} M_{pl}/\sigma_*` (row 15), and `\lambda_\sigma = \lambda_T`:

```
r_{after} = 24 \Lambda^2 / [1 + \Lambda^2 (4/3) X^2] ,     \Lambda = \lambda_T/\lambda_\zeta
        =  24 / \mathcal{F}_{eff}^2 ,   \mathcal{F}_{eff}^2 = 1/\Lambda^2 + (4/3)X^2
```

| background | scheme | `\lambda_\sigma` | `\lambda_T` | `\lambda_\zeta` | `\Lambda` | single-field `r_{after}` | `X_{min}` for `r<0.036` | for `r<0.01` |
|---|---|---|---|---|---|---|---|---|
| Quintin / LQC / poly | S1 (`z=a`) | `=\lambda_T` | — | `=\lambda_T` | **1.0000** | 24 | **22.344** | 42.418 |
| Quintin | S2 (fluid MS) | `=\lambda_T` | 6.05860 | 0.96958 | **6.24871** | 937.1 | **22.360** | 42.426 |
| LQC, poly | S2 | `=\lambda_T` | — | not computed | — | — | — | — |

(`\lambda_T`, `\lambda_\zeta^{S1}`, `\lambda_\zeta^{S2}` for Quintin are row 18a's values at
`k\eta_B = 10^{-3}`, imported; S2 on the LQC and poly backgrounds is **not computed here**
and is disclosed as an open item, not asserted.)

**Central result.** `X_{min}` is the *same in both schemes to `7.3\times10^{-4}`*, and it is
exactly row 15's number: `\mathcal{F}_{eff} \ge 25.8199` for `r < 0.036`,
`\ge 48.99` for `r < 0.01`. The reason is structural, not numerical: because the
spectator and the tensor share `\lambda`, the scheme factor `\Lambda^2` appears in the
numerator *and* in the curvaton term, and cancels for `\Lambda^2(4/3)X^2 \gg 1`. Scheme S2
inflates the *single-field* ratio to `r = 937` (row 18a) — a 39× worse starting point —
yet the curvaton requirement is unchanged, because the curvaton channel is inflated by
exactly the same factor.

Equivalently, at `r_{dec} = 1` the condition is `\sigma_*/M_{pl} < 0.04476` for
`r < 0.036` (`< 0.02357` for `r < 0.01`) — a **pre-bounce** statement about the spectator
VEV, with no bounce-model input whatsoever.

## 4. Does the bounce touch the curvaton's non-Gaussianity? (stated, not computed)

Three separate questions, and the operator identity settles the first two:

1. **The curvaton's LOCAL `f_NL`** (LUW03/SVW06, `5/(4r_{dec}) - 5/3 - 5r_{dec}/6`) is
   generated at curvaton *decay*, from a Gaussian `\delta\sigma`, long after the bounce.
   `\Delta f_{NL}^{bounce}` does **not** act on it. Row 15 already stated this; row 15b
   adds the reason it is safe to say so — the linear transfer of `\delta\sigma` is the
   *tensor's*, and a single overall factor `\lambda_\sigma` on a Gaussian field changes
   no dimensionless ratio at decay.
2. **Any INTRINSIC `\delta\sigma`-sector non-Gaussianity generated before the bounce**
   (from `\sigma`'s own potential, `\delta\sigma \to \delta\sigma_L + (g/2)\delta\sigma_L^2`)
   transmits with the *same 1/λ structure* as the adiabatic case —
   `f_{NL}^{intrinsic} \to f_{NL}^{intrinsic}/\lambda_\sigma` — but with
   `\lambda_\sigma = \lambda_T`, **not** `\lambda_\zeta`. In S1 those coincide and the
   transmitted suppression is numerically the row-14/A2 one; in S2 they differ by
   `\Lambda = 6.25`, so a spectator's intrinsic `f_{NL}` is suppressed `6.25\times` more
   than the adiabatic one.
3. **Which cubic vertices apply to a spectator.** The A2/lane-A vertex table is built from
   the adiabatic cubic action, whose operators (`\epsilon^2\zeta\dot\zeta^2`,
   `\epsilon^2\zeta(\partial\zeta)^2`, the `\dot\zeta^3` and field-redefinition terms) all
   carry powers of `\epsilon` and of the *constraint* solutions `\delta N`, `\psi`. A test
   spectator contributes to the constraints only at `O(\delta\sigma^2/M_{pl}^2)`, so the
   gravitationally-induced `\delta\sigma^3` vertices are suppressed by
   `(\sigma_*/M_{pl})^2 < 2\times10^{-3}` at the viable point on top of the usual slow-roll
   counting. The surviving cubic vertices are `\sigma`'s own `V'''(\sigma)\delta\sigma^3`
   and the minimal-coupling `a^2 V''' `-type term. **We state this structurally and do not
   compute it here** — it requires the spectator's potential, which is model input the A2
   backgrounds do not fix.

## 5. The surviving discriminator `n_T = n_s - 1 = -0.035`: is it bounce-affected?

The matter bounce predicts `n_T = n_s - 1 = 12w/(1+3w) = -0.035` on row 10's anchor,
versus inflation's consistency relation `n_T = -r/8 \simeq -0.0045` at `r = 0.036` and
`\simeq 0` at the curvaton point. A `k`-dependent `\lambda_T` would shift it by
`\Delta n_T = 2\,d\ln\lambda_T/d\ln k`. Fitting `\lambda_T = \lambda_T(0)[1 - c(k\eta_B)^2]`
over `k\eta_B \in [10^{-3}, 10^{-2}]`:

| background | `c` | `\Delta n_T` at `k\eta_B = 10^{-3}` | at `k\eta_B = 10^{-2}` |
|---|---|---|---|
| Quintin-type | 262.0 | `-1.05\times10^{-3}` | `-1.05\times10^{-1}` |
| LQC-eff.-dust | 285.3 | `-1.14\times10^{-3}` | `-1.14\times10^{-1}` |
| poly-analytic | 236.1 | `-9.45\times10^{-4}` | `-9.45\times10^{-2}` |

The shift is `O((k\eta_B)^2)` — it is the same gradient correction that makes
`T_c \to 1` in row 15 §5. Observable CMB scales sit at `k\eta_B \lll 10^{-3}` (the
bounce-scale enhancement at `k\eta_B \sim 1` is a *separate* route, ledger row 9 / A3-1e),
so across the entire observable band the correction is utterly negligible and

```
n_T = n_s - 1 = -0.035   is TRANSMITTED UNCHANGED by the bounce.
```

The honest counterweight: at `r < 0.036` no planned experiment measures `n_T` — CMB-S4's
`\sigma(n_T)` at that `r` is `O(1)`. The discriminator is **theoretically clean and
observationally out of reach at the curvaton point**, which is the same trade row 15
found for `f_{NL}`.

## Verdict (ledger row 15's named open item)

**CLOSED, as a transfer statement; the microphysical `\mathcal{F}` remains model input.**

1. The A2 backgrounds now *do* carry an entropy sector: a massless spectator's transfer
   `\lambda_\sigma` is computed on all three and equals the tensor's `\lambda_T` to
   `8\times10^{-5}` (Quintin, a numerical floor) and `\sim10^{-9}` (LQC, poly), as the
   `z = a` operator identity requires.
2. Therefore the `\sigma/\zeta` amplitude ratio is **preserved through the bounce in S1**
   (`\Lambda = 1`) and **rescaled by `\Lambda = \lambda_T/\lambda_\zeta^{S2} = 6.249` in S2**
   — precisely as row 18a's tensor/scalar contrast predicted.
3. The curvaton viability condition is consequently a **pre-bounce** condition:
   `X = r_{dec}M_{pl}/\sigma_* > 22.34` (S1) / `22.36` (S2) for `r < 0.036`, i.e.
   `\mathcal{F}_{eff} \ge 25.82` in both schemes — scheme-independent to `7\times10^{-4}`,
   and background-independent because `\lambda_\sigma/\lambda_T = 1` on all three.
4. **What is still NOT closed:** `\mathcal{F}` itself. This row shows that whatever
   amplification the entropy sector achieves *survives the bounce untouched*; it does not
   derive that amplification, which requires a microphysical curvaton potential and decay
   history (CXB11's `g^2\phi^2` coupling, or the lab's branch-W ALP). Row 15's "`\mathcal{F}`
   is not computable here" is now sharpened to "`\mathcal{F}` is a pre-bounce,
   model-dependent number, and the bounce is guaranteed not to spoil it."
5. `\lambda_\zeta^{S2}` is measured on the Quintin background only; LQC and poly S2 are an
   open (small) item, not an assertion.

## Paper-ready sentences

> A spectator field with `m^2 \ll H^2` and a canonical kinetic term shares the tensor's
> pump term `a''/a` exactly, so its Mukhanov–Sasaki variable and the graviton's obey the
> same equation on any background. Integrating both through the three bounce backgrounds
> of Sec. [A2] — with the tensor evolved in an independent first-order formulation as a
> numerical control — we find `\lambda_\sigma/\lambda_T - 1 \le 8\times10^{-5}`, saturating
> the sampling floor of the piecewise background and reaching `10^{-9}` on the two smooth
> ones.

> Because the entropy and tensor channels are amplified identically, the scheme factor
> `\Lambda = \lambda_T/\lambda_\zeta` cancels between the tensor numerator and the curvaton
> contribution to the scalar power, and the tensor-to-scalar constraint reduces to the
> purely pre-bounce condition `r_{dec}M_{pl}/\sigma_* > 22.34`, equivalently
> `\mathcal{F}_{eff} \ge 25.82`, in both the geometric (`z = a`) and fluid Mukhanov–Sasaki
> schemes — despite the fact that the single-field ratio itself differs between them by a
> factor of 39.

> The transfer coefficient's scale dependence is `\lambda_T \propto 1 - c\,(k\eta_B)^2`
> with `c = 236`–`285` across the three backgrounds, so the tensor tilt is shifted by
> `|\Delta n_T| \lesssim 10^{-3}` already at `k\eta_B = 10^{-3}` and by vastly less on
> observable scales: the matter-bounce prediction `n_T = n_s - 1 = -0.035`, in contrast
> with inflation's `n_T = -r/8`, is transmitted through the bounce unchanged. At the
> tensor-viable curvaton point, however, `r < 0.036` places `n_T` beyond the reach of
> planned experiments.
