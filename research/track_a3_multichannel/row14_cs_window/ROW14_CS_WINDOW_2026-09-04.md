# Ledger row 14 — the (r, f_NL) window in the contraction's scalar sound speed c_s

**Status:** IN PROGRESS 2026-09-04 (plan header committed first; results appended below).
**Owner lane:** row14_cs_window (does NOT touch `research/track_a3_multichannel/paper/main.tex`)
**Artifacts (planned):** `row14_cs_window.py`, `results.json`, `row14_cs_window.log`,
`row14_cs_window.png`, manifest `reproducibility/manifests/experiments/a3-row14-cs-window.json`.

## Why

Row 10 (`../row10_r_ns/ROW10_R_NS_2026-09-04.md`) closed with `r = 16\epsilon = 24`
for the canonical dust contraction — bounce-invariant across all three A2
backgrounds, ~670x above BICEP/Keck's `r < 0.036`. The textbook remedy is a
scalar sound speed `c_s < 1` in the contracting phase, which suppresses `r`
while *enhancing* the scalar non-Gaussianity. The flagship line's `f_NL` must
therefore be re-stated on whatever `c_s` branch is CMB-viable, or Track A's
claim is conditional on unspecified physics. Ledger success/kill: a viable
`c_s` window with a stated `f_NL^after` -> the flagship claim re-anchored
honestly; no viable window -> Track A states the tensor problem as unresolved.

## Plan

1. **Analytic spectra with constant `c_s`.** `z^2 = a^2(\rho+p)/(c_s^2 H^2) = 2a^2\epsilon/c_s^2`,
   `v = z\zeta`, `v'' + (c_s^2k^2 - z''/z)v = 0`, BD normalisation
   `v \to e^{-ic_sk\eta}/\sqrt{2c_sk}`. Tensors are unchanged (`c_T = 1`).
   Derive `r(c_s,\epsilon)` for the contracting, growing-mode-dominated case —
   do NOT assume the inflationary formula; get the power of `c_s` from the
   index `\nu = q - 1/2`, `q = 2/(1+3w)`.
2. **Numerical confirmation** with a lane-b-style integrator at `k\eta_B << 1`.
3. **The window:** `c_s` at which `r = 0.036` and `r = 0.01`.
4. **`f_NL^{pre}(c_s)`** in the isoceles squeezed limit, TWO ways: (a) Li,
   Quintin, Wang & Cai 2016 (arXiv:1612.02036) Eq. (4.19); (b) the lab's own
   in-in machinery (`research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py`)
   with the `c_s`-modified cubic vertices. Li's `c_s = 1` limit must reproduce
   `-35/16`; report any discrepancy honestly.
5. **Transfer `T(c_s)`** through the Quintin-type A2 background (S1), noting
   whether `z`'s `c_s` factor changes the super-Hubble branch mixing; hence
   `f_NL^{after}` at the viable `c_s`.
6. **No-go check:** Quintin, Sherkatghanad, Cai & Brandenberger 2015
   (arXiv:1508.04141) — quote their exact small-`r`/acceptable-`f_NL`
   inequality and test the viable `c_s` against it. Compare `|f_NL^{after}|`
   to Planck 2018 `f_NL^{local} = -0.9 +/- 5.1` and SPHEREx `\sigma = 0.5-0.7`.
7. **What sets `c_s < 1`:** state plainly that a k-essence/DBI-type kinetic
   sector is required (Garriga & Mukhanov 1999; Chen, Huang, Kachru & Shiu
   2007) and that this lab's pressureless-dust model does NOT provide it.

## Ground rules

Never tune. Every number in the results table comes from the committed script.
Claims stated at exactly their evidential strength; a null is published as a null.

---

# Results (2026-09-04, every number from `row14_cs_window.py`)

**Status: DONE. VERDICT — NO VIABLE `c_s` WINDOW.** The `c_s` that brings `r` to the
BICEP/Keck bound raises the squeezed `f_NL` to `~10^6`; the `c_s` that keeps `f_NL`
inside Planck leaves `r ~ 11`. The two requirements are disjoint by a factor `~300`
in `c_s`. Per the ledger's kill condition, **Track A must state the tensor problem as
unresolved**, and the flagship `f_NL = -35/16` is a `c_s = 1` statement that cannot be
carried onto a CMB-viable tensor branch.

## 1. `r(c_s)` — derived, not imported

With constant `c_s` the scalar canonical variable is `v = z\zeta`,
`z^2 = a^2(\rho+p)/(c_s^2H^2) = 2a^2\epsilon/c_s^2`, obeying
`v'' + (c_s^2k^2 - z''/z)v = 0` with `v \to e^{-ic_sk\eta}/\sqrt{2c_sk}`; the tensor
sector has `c_T = 1` and is untouched. For `a \propto (-\eta)^q`, `z \propto a`, so
`z''/z = a''/a` and the index is `\nu = |q - 1/2|`. Taking the small-argument Hankel
limit of both sectors and forming `r = P_h/P_\zeta`:

> **`r = 16\,\epsilon\, c_s^{2\nu-2}`** — and for the dust contraction (`q = 2`,
> `\nu = 3/2`) **`r = 16\epsilon c_s = 24\,c_s`.**

Two independent symbolic routes in the script agree (general-`\nu` Hankel limit and
the exact `q = 2` mode functions `|v|^2 = (1+1/(c_sk\tau)^2)/(2c_sk)`,
`|\mu_T|^2 = (1+1/(k\tau)^2)/(2k)`). The power of `c_s` is **not** assumed from the
inflationary formula; it comes out as `c_s^{2\nu-2}`, which happens to coincide with
the inflationary `c_s^1` only because both cases have `\nu = 3/2`.

This **independently reproduces Li, Quintin, Wang & Cai 2016 (arXiv:1612.02036)
Eq. (3.18), `r = 24c_s`**, and reduces to row 10's `r = 24` at `c_s = 1`.
The scalar amplitude scales as `P_\zeta \propto 1/(\epsilon c_s)` (Garriga & Mukhanov
1999, hep-th/9904176), which is the whole mechanism.

**The window:** `r < 0.036` (BICEP/Keck 2021) requires **`c_s < 1.500\times10^{-3}`**;
`r < 0.01` requires `c_s < 4.167\times10^{-4}`.

## 2. `f_NL^{pre}(c_s)` — two routes, no discrepancy at `c_s = 1`

Li+2016 Eq. (4.19) gives the total shape function `\mathcal{A}_{\rm tot}(k_1,k_2,k_3;c_s)`
for the matter contraction with general `c_s`; `f_NL = (10/3)\mathcal{A}_{\rm tot}/\sum_ik_i^3`.
That expression is transcribed once into the script and **both of its limits are taken
symbolically here**, which is a genuine check of their algebra:

| configuration | derived here | Li+2016 quoted | match |
|---|---|---|---|
| equilateral `k_1=k_2=k_3` | `-335/32 + 65/(8c_s^2) + 45c_s^2/128` | `f_NL^{equil}` identical | exact |
| isoceles squeezed `k_1\to0`, `k_2=k_3=k` (`\mu\to0`) | `-165/16 + 65/(8c_s^2)` | `f_NL^{local}` identical | exact |

At `c_s = 1` the squeezed value is **`-35/16`**, which is **exactly** the lab's own
from-scratch in-in result (`research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py`,
commit `aa2987cf`, comoving-gauge isoceles squeezed limit, `f(\mu) = -35/16 + (15/16)\mu^2`
at `\mu = 0`; the exactly-isoceles squeezed triangle has `\hat k_1\cdot\hat k_2 = -\delta/2 \to 0`,
so `\mu = 0` is the right comparison point). **No discrepancy between the two routes.**

**Honest scope statement on the general-`c_s` cross-check.** The lab's in-in machinery
is built for `c_s = 1` (Maldacena comoving-gauge cubic action). A general-`c_s` in-in
requires the k-essence cubic action of Chen, Huang, Kachru & Shiu 2007 (hep-th/0605045),
whose `\dot\zeta^3` vertex carries a model-dependent coefficient `\lambda/\Sigma` that is
**not** fixed by `c_s` alone. The `65/(8c_s^2)` coefficient therefore inherits Li+2016's
choice of kinetic sector; this lane does **not** claim an independent lab derivation of it.
What is independent is (i) the `c_s\to1` limit, verified exactly against the lab's own in-in,
and (ii) the `1/c_s^2` *scaling*, which is the generic single-field result (CHKS 2007) and
is what drives the conclusion below. A fine-tuned `\lambda` could shift the coefficient but
not the divergence as `c_s\to0`.
