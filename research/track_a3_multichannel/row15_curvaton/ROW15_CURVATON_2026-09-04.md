# Ledger row 15 — the curvaton-type matter bounce: (r, n_s, f_NL)

**Status:** DONE 2026-09-04. **Result: A VIABLE WINDOW EXISTS — `r` is free, `n_s = 0.9649`
is inherited unchanged, and the local `f_NL` is O(1) — BUT the `f_NL` at that point is the
curvaton's, not the bounce's: the intrinsic `-35/16` is diluted by `(r/24)^2 ~ 2e-6`. The
mechanism that saves the tensor channel destroys the flagship prediction's observability.**
**Owner lane:** row15_curvaton (does NOT touch `research/track_a3_multichannel/paper/main.tex`)
**Question (ledger row 15):** does a matter-bounce curvaton (Cai, Xue &
Brandenberger 2011, arXiv:1101.0822; the lab's branch-W ALP-curvaton work)
give `r < 0.036` with `n_s \simeq 0.965` and a local `f_NL` of O(1) — and at
what value and sign?

## Why

Row 10 (`../row10_r_ns/`) closed the canonical dust contraction at
`r = 16\epsilon = 24`, bounce-invariant, ~670x above BICEP/Keck. Row 14
(`../row14_cs_window/`) closed the k-essence remedy as a NULL: `r < 0.036`
needs `c_s < 1.5e-3` where `f_NL^{after} \sim 6e5`, while `|f_NL| \le 5.1`
needs `c_s \ge 0.444` where `r \ge 10.7` — disjoint by ~296x in `c_s`
(decision D-A3-11). The curvaton is the standard *surviving* route: it does
not touch the tensor sector at all, it adds a second, larger scalar channel,
so `r` falls by the ratio of scalar powers. Whether the surviving point also
has `n_s \simeq 0.965` and an O(1) `f_NL` decides whether the flagship line's
`f_NL` prediction can be re-anchored, or whether Track A must state the whole
matter-bounce family as excluded at the modelled level.

## Plan

1. **Spectator spectrum in the dust contraction.** A light scalar `\sigma`
   (`m \ll H`) on the same `a \propto (-\eta)^2` background: solve
   `u'' + (k^2 - a''/a)u = 0` (same MS operator as the adiabatic mode for a
   massless spectator, `u = a\sigma`), BD vacuum, extract `P_\sigma(k)` and
   its tilt from the small-mass correction. Cross-check against Cai, Xue &
   Brandenberger 2011's stated `n_s` for the curvaton in a matter contraction.
2. **Conversion to `\zeta`.** `\zeta = r_{dec}\,\zeta_\sigma` with
   `\zeta_\sigma = (1/3)\,\delta\rho_\sigma/\rho_\sigma =
   (2/3)\,\delta\sigma/\sigma` (quadratic potential), so
   `P_{\zeta,curv} = (r_{dec}^2/9)(2/\pi)^2 ... ` — coefficient from the
   script, not by hand; `r_{dec} = 3\rho_\sigma/(3\rho_\sigma + 4\rho_r)` at
   decay (Lyth–Ungarelli–Wands 2003, astro-ph/0208055).
3. **`r(r_{dec}, \sigma_*)`.** `P_h` unchanged from row 10; the adiabatic
   scalar unchanged. `r = P_h/(P_{\zeta,ad} + P_{\zeta,curv}) =
   24/(1 + P_{\zeta,curv}/P_{\zeta,ad})`. Solve for the suppression factor
   needed for `r < 0.036` and `r < 0.01`.
4. **`n_s`.** From the curvaton's own tilt in the contraction (mass term +
   background), test whether 0.9649 is reachable and with what `m/H`.
5. **`f_NL`.** Curvaton local formula `f_NL = 5/(4r_{dec}) - 5/3 -
   5r_{dec}/6` (LUW 2003; Sasaki, Valiviita & Wands 2006, astro-ph/0607627),
   evaluated over the `r_{dec}` values that satisfy (3); plus the *intrinsic*
   non-Gaussianity generated in the contraction (is it a `-35/16`-type term
   with a different coefficient?) — cite Cai+2011's own statement. Report
   SIGN and magnitude vs Planck `-0.9 \pm 5.1` and SPHEREx `\sigma \simeq 0.5`.
6. **Transmission.** The curvaton converts *after* the bounce, so state
   whether the A2 transfer applies to `\sigma` (same MS equation for a
   massless spectator?) and whether `\Delta f_NL^{bounce}` applies at all.
7. **Multi-channel map at the viable point:** which of A3's nulls survive,
   and SPHEREx's reach for the curvaton `f_NL`.

## Ground rules

Never tune. Every number in the results table comes from the committed script
`row15_curvaton.py`. Claims at exactly their evidential strength; a null is
published as a null (VISION R6).

---


# Results (2026-09-04, every number from `row15_curvaton.py`)

## 1. The curvaton's spectrum and tilt in the dust contraction

A light spectator `\sigma` (`m \ll H`) on the contracting background has `u = a\sigma`
obeying `u'' + (k^2 - a''/a)u = 0` — **the same Mukhanov–Sasaki operator as the
adiabatic variable** (for constant `\epsilon`, `z = a\sqrt{2\epsilon} \propto a`) **and
as the tensor mode**. For `a \propto (-\eta)^q`, `q = 2/(1+3w)`, the index is
`\nu = q - 1/2` and

```
n_\sigma - 1  =  3 - 2\nu  =  4 - 2q  =  12w/(1+3w)          [symbolic, sympy]
```

which is **identical to the adiabatic tilt derived in row 10**. Two consequences:

* For exact dust (`w = 0`, `q = 2`) the curvaton spectrum is **exactly scale-invariant**
  — Wands 1999 / Finelli–Brandenberger 2002 applied to a spectator, the mechanism CXB11
  rely on ("massless scalar fields … acquire a scale-invariant spectrum … in a
  matter-dominated contracting universe", their abstract).
* `n_s = 0.9649` is reached on the **same Planck-anchored branch `w = -0.0029`** that
  row 10 identified. The script returns `n_s = 0.96490`. **The curvaton does not need a
  mass to get the tilt, and the tilt is not a new prediction** — same anchor, same
  evidential status as row 10 (`w` is fitted, not predicted).

**A tracking curvaton mass makes it worse, not better.** With CXB11's coupling
`m_\chi^2 = g^2\phi^2` the mass enters as `m_\chi^2 a^2 = \gamma/\eta^2` and

```
n_\sigma - 1  =  2\gamma/3 ,   \gamma = m_\chi^2 a^2\eta^2 = 4 m_\chi^2/H^2
              =  (8/3)\, m_\chi^2/H^2                    [this work]
```

CXB11 Eq. (18) quotes `2m_\chi^2/(3H^2)` — that is the **de Sitter** spectator value
(`m^2a^2 = m^2/(H^2\eta^2)`); in a matter contraction `a^2\eta^2 = 4/H^2`, so the same
derivation gives a coefficient **4× larger**. The sign is unchanged and is what matters:
`m_\chi^2 > 0` gives a **BLUE** tilt. A red `n_s` from the curvaton mass alone would need
a tachyonic `g^2 < 0`. Honest statement: the tilt comes from `w`, and CXB11's
`|g m_{pl}| \ll \sqrt{2\pi}\,m` is a **null-tilt** condition, not a tilt mechanism.
(The lab's branch-W ALP-curvaton phase-1 note wrote `n_\sigma - 1 \sim -m^2/H^2`; that
sign is opposite to CXB11 Eq. (18) and to this derivation. Branch W's conclusion — "a
generic massive curvaton can fix the tilt with `m \simeq 0.2 H_k`" — does **not** survive
in a contraction: a positive mass tilts blue, and the red tilt must come from `w \neq 0`.)

## 2. Tensor-to-scalar ratio: `r` is free

Tensors are untouched by the curvaton, so `P_h` is row 10's. With a quadratic curvaton,
`\zeta_{curv} = r_{dec}\,\zeta_\sigma`, `\zeta_\sigma = (1/3)\delta\rho_\sigma/\rho_\sigma
= (2/3)\delta\sigma/\sigma_*` (LUW 2003), and `P_{\delta\sigma}` equals the adiabatic
`v`-mode power because the two obey the same equation:

```
P_{\zeta,curv}/P_{\zeta,ad}  =  (8\epsilon/9)\, r_{dec}^2 (M_{pl}/\sigma_*)^2
                             =  (4/3)\, r_{dec}^2 (M_{pl}/\sigma_*)^2   (dust, \epsilon = 3/2)

r  =  16\epsilon / [1 + (4/3) r_{dec}^2 (M_{pl}/\sigma_*)^2]  =  24 / [1 + \ldots]
```

**Any `r \le 24` is reachable** by choosing the curvaton VEV `\sigma_*`; nothing pushes
back in the tensor channel. `r < 0.036` needs `r_{dec} M_{pl}/\sigma_* > 22.35`;
`r < 0.01` needs `> 42.4`. In CXB11's own parametrisation (their Eq. 61,
`r \simeq 35\mathcal{F}^{-2}`; `24\mathcal{F}^{-2}` in the row-10 normalisation) the
required kinetic-amplification factor is **`\mathcal{F} \ge 25.82` for `r < 0.036`**
and `\ge 48.99` for `r < 0.01`. That number coincides with row 14's Quintin+2015
requirement `\lambda = 25.8` — but here the amplification acts on the **entropy** field
only, so unlike row 14's `\lambda` it is not cancelled by an equal tensor amplification.
The A2 backgrounds in this lab have no entropy sector, so `\mathcal{F}` is **not
computable here**; this row states the required value rather than claiming it.

## 3. Local `f_NL` and the dilution of the bounce prediction

Curvaton local non-Gaussianity (Lyth–Ungarelli–Wands 2003; Sasaki–Valiviita–Wands 2006,
exact-quadratic branch — SVW's non-quadratic terms `\propto \sigma V'''/V''` are extra
model freedom, not included):

```
f_NL^{curv} = 5/(4 r_{dec}) - 5/3 - 5 r_{dec}/6
```

monotonically decreasing in `r_{dec}`; sign change at **`r_{dec} = 0.5811`**, minimum
`-5/4 = -1.250` at `r_{dec} = 1`. Planck `-0.9 \pm 5.1` at `2\sigma` requires
**`r_{dec} \ge 0.1130`**.

The intrinsic matter-bounce non-Gaussianity does not disappear, but for two independent
channels `\zeta = \zeta_{ad} + \zeta_{curv}`, `f_NL^{tot} = \sum_i f_NL^i (P_i/P_{tot})^2`,
and the adiabatic power fraction is exactly `r/24`. At `r = 0.036` that is
`1.5\times10^{-3}`, so

```
f_NL^{bounce, effective} = (-35/16) \times T_{A2} \times (r/24)^2
                         = -8.1e-7 (Quintin) … -1.2e-6 (LQC)
```

**six orders of magnitude below SPHEREx.** Inverting: the bounce term stays above
`\sigma(f_NL) = 0.5` only for **`r \ge 22.95`** — only on the un-suppressed,
tensor-excluded branch. This is the row's central finding.

## 4. Viable-window table (from `results.json`; `n_s` at `w = -0.0029`, `r` set to 0.036)

| `r_dec` | max `\sigma_*/M_{pl}` for `r<0.036` | `r` | `n_s` | `f_NL^{curv}` | `f_NL^{tot}` | Planck 2σ | SPHEREx |
|---|---|---|---|---|---|---|---|
| 0.050 | 0.0022 | 0.036 | 0.9649 | +23.29 | +23.29 | no | — |
| 0.100 | 0.0045 | 0.036 | 0.9649 | +10.75 | +10.75 | no | — |
| **0.1130** | 0.0051 | 0.036 | 0.9649 | **+9.30** | +9.30 | edge | 18.6σ |
| 0.200 | 0.0090 | 0.036 | 0.9649 | +4.42 | +4.42 | yes | 8.8σ |
| 0.300 | 0.0134 | 0.036 | 0.9649 | +2.25 | +2.25 | yes | 4.5σ |
| 0.500 | 0.0224 | 0.036 | 0.9649 | +0.42 | +0.42 | yes | 0.8σ |
| 0.5811 | 0.0260 | 0.036 | 0.9649 | **0.00** | 0.00 | yes | 0σ |
| 0.750 | 0.0336 | 0.036 | 0.9649 | −0.63 | −0.63 | yes | 1.2σ |
| 1.000 | 0.0448 | 0.036 | 0.9649 | **−1.25** | −1.25 | yes | 2.5σ |

**Viable window: `r_{dec} \in [0.113, 1]`**, `r` free (0.036 here), `n_s = 0.9649`,
`f_NL^{local} \in [-1.25, +9.30]`. **Sign:** negative only for `r_{dec} > 0.5811`, and
then only as far as `-1.25`. CXB11's Case 1 is more predictive: with
`\mathcal{C} = (\pi/4d)^2` their Eq. (65) collapses to the **parameter-free**
`f_NL = -320/\pi^4 = -3.285` (they quote `-3.3`), `0.47\sigma` from Planck and a
`6.6\sigma` target for SPHEREx — and it keeps the negative sign. Their Case 2,
`f_NL \simeq -5.3\,m^4/(d^2M^4)` (Eq. 67), has one free combination and no predictive
content.

## 5. Transmission

The spectator ODE `u'' + (k^2 - a''/a)u = 0` is **literally** the ODE the A2 module
integrates and the ODE the tensor mode obeys, so `T_\sigma \equiv T_h` identically;
row 10 measured `T_h/T_\zeta - 1 \le 8\times10^{-5}` and row 14
`\lambda_{scalar}/\lambda_{tensor} - 1 \le 4\times10^{-11}` on all three backgrounds.
Direct check here of the frozen super-Hubble branch (`T_c \to 1`) at `k\eta_B = 0.01`:
LQC `|T_c-1| = 1.9\times10^{-4} \to 5.5\times10^{-6}` and Quintin
`7.8\times10^{-4} \to 2.7\times10^{-4}` as `u_{out}` falls from 0.1 to 0.05, both
converging to 1; the poly background's constant-branch preparation is less accurate there
(`2.7\times10^{-2}` at `u_{out}=0.05`, non-monotonic), and the analytic identity plus
row 14's `4\times10^{-11}` are the stronger evidence for that background.

**`\Delta f_NL^{bounce}` does NOT apply to the curvaton channel.** The curvaton's local
`f_NL` is generated at curvaton *decay*, after the bounce, from a Gaussian
`\delta\sigma`; the A2 transfer `T = 0.165-0.250` acts only on the pre-bounce adiabatic
bispectrum — the channel just diluted away. (In CXB11's variant the conversion happens
*at* the bounce and their Eq. (65) already contains that physics.)

## 6. Multi-channel map at the viable point

| Channel | Status at the curvaton point |
|---|---|
| nHz tensors (PTA) | **Null STRENGTHENED.** `\Omega_{GW}h^2(f_{yr})` scales with `r`: `1.69\times10^{-14}\times(0.036/24) = 2.5\times10^{-17}`, now `\sim10^{8}` below NANOGrav instead of `10^{5.3}`. |
| PBH | **Null unchanged.** Set by the small-scale scalar amplitude; the curvaton spectrum is scale-invariant on the same branch. |
| `f_NL` (flagship) | **Reinterpreted.** The observable is purely *local* and measures `r_{dec}`, not the bounce. The bounce's orientation-dependent shape `f(\mu) = -35/16 + (15/16)\mu^2` survives only at the `(r/24)^2 = 2\times10^{-6}` level. |
| DESI reproduction / unseparable channel | Unchanged (independent of `r` and of the `f_NL` amplitude). |

SPHEREx (`\sigma \simeq 0.5`) reaches the curvaton `f_NL` at `\ge 4.5\sigma` for
`r_{dec} \le 0.3` and `2.5\sigma` at `r_{dec} = 1`; CXB11 Case 1 at `6.6\sigma`. A
SPHEREx detection at this level would **not** be evidence for the bounce's cubic action —
it would measure a curvaton decay fraction, which inflationary curvaton models predict too.

## Verdict (ledger row 15)

**PARTIAL PASS — the ledger's success condition is met on `(r, n_s, f_NL)`, but the
flagship `f_NL` prediction does not survive the fix.**

1. `r < 0.036` — **achievable with no tension**, for `\sigma_*/M_{pl} < r_{dec}/22.35`
   (equivalently CXB11's `\mathcal{F} \ge 25.82`). Unlike row 14's `c_s` route, nothing
   pushes back.
2. `n_s = 0.9649` — **inherited unchanged** from row 10's `w = -0.0029` anchor, because
   the spectator tilt equals the adiabatic tilt exactly, `12w/(1+3w)`. Still an anchor,
   not a prediction. A curvaton *mass* cannot supply it (wrong sign: blue).
3. `f_NL^{local}` — **O(1) and Planck-compatible** over `r_{dec} \in [0.113, 1]`, from
   `+9.30` down to `-1.25`, negative only for `r_{dec} > 0.5811`; CXB11 Case 1 gives the
   parameter-free `-320/\pi^4 = -3.29`.
4. **But** the observable `f_NL` there is the *curvaton's*, not the bounce's: `-35/16` is
   suppressed by `(r/24)^2` to `\sim10^{-6}`, staying above SPHEREx only for
   `r \ge 22.95` — the excluded branch.

Track A's `f_NL = -35/16` is therefore **observable only where the model is
tensor-excluded, and the model is tensor-viable only where `f_NL` is unobservable.** With
row 14 this is one structural statement: every known mechanism that cures `r` either
amplifies `f_NL` past the bounds (`c_s`, row 14) or dilutes the bounce `f_NL` below
detectability (curvaton, this row). The matter-bounce family is **not excluded** — it is
*un-diagnosed* by the `f_NL` channel.

**Still open:** (i) `\mathcal{F}`, the entropy-only kinetic amplification, is an
assumption — computing it needs an entropy sector added to the A2 backgrounds; (ii) the
curvaton's *intrinsic* bispectrum generated during the contraction/conversion (CXB11
Eqs. 62–64) has not been re-derived here — only their final Eq. (65) is quoted; (iii)
whether any channel distinguishes a curvaton matter bounce from a curvaton inflation —
the shape is local in both, so the discriminator, if one exists, must be the tensor tilt
`n_T = -0.035` (row 10), not `f_NL`.

## Paper-ready reframing sentences

> A curvaton sector removes the tensor obstruction of the single-field matter bounce at no
> cost: because the light spectator obeys the same Mukhanov–Sasaki equation as the
> adiabatic mode, its spectrum is scale-invariant with the identical tilt `12w/(1+3w)`, and
> the tensor-to-scalar ratio becomes `r = 16\epsilon/[1 + (8\epsilon/9)r_{dec}^2
> (M_{pl}/\sigma_*)^2]` — any value below 24. The price is paid in the non-Gaussianity
> channel: the adiabatic power fraction is exactly `r/16\epsilon`, so the contraction's
> intrinsic `f_NL = -35/16` enters the observable bispectrum weighted by
> `(r/16\epsilon)^2`. At `r = 0.036` that weight is `2\times10^{-6}`, and the measurable
> local `f_NL` is the curvaton's `5/(4r_{dec}) - 5/3 - 5r_{dec}/6`, an O(1) number set by
> the decay fraction and shared with inflationary curvaton models.

> The two curative mechanisms fail in opposite directions. Reducing the scalar sound speed
> suppresses `r` only at `c_s < 1.5\times10^{-3}`, where `f_NL \sim 10^{6}`; adding a
> curvaton suppresses `r` freely but drives the bounce contribution to `f_NL` below
> `10^{-6}`. The matter bounce's cubic action is observable only on the branch its own
> tensor spectrum excludes.

## Reproduce

```
cd research/track_a3_multichannel/row15_curvaton && python3 row15_curvaton.py
```
Local CPU, ~4 s, $0, deterministic (no RNG, no data files, no network). Manifest:
`reproducibility/manifests/experiments/a3-row15-curvaton.json`.
