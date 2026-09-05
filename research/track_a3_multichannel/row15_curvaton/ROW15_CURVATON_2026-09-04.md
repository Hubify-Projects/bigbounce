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
