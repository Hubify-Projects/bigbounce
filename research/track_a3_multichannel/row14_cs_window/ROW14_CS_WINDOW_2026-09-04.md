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

## 3. The transfer `T(c_s)` through the bounce is `c_s`-independent

For constant `c_s`, `z \propto a`, so `z''/z = a''/a` is unchanged and the only change to
the mode equation is `k^2 \to c_s^2k^2`: the `c_s` problem at wavenumber `k` **is** the
`c_s = 1` problem at the effective wavenumber `c_s k`. Because `T` is already flat over
`k\eta_B \ll 1` (row 10 / A2), lowering `c_s` moves the mode further into the super-Hubble
regime and changes nothing. `z`'s `1/c_s` factor is a constant and drops out of the
`{1, J(\eta)}` super-Hubble branch mixing entirely.

Verified numerically, not assumed: the scalar was re-integrated through all three A2
backgrounds with the gradient term `c_s^2k^2` for `c_s \in \{1, 10^{-1}, 10^{-2},
1.5\times10^{-3}, 10^{-4}\}` at `k\eta_B = 10^{-2}`.

| background | `T_{f_{\rm NL}}` | `\lambda_\zeta` | `\max|\lambda_S/\lambda_T - 1|` over the `c_s` grid | `r_{\rm after}/16\epsilon c_s` |
|---|---|---|---|---|
| poly-analytic non-LQC | 0.195501 | 5.115 | `5.6\times10^{-13}` | 1.00000000 |
| LQC-effective dust | 0.250000 | 4.000 | `4.1\times10^{-11}` | 1.00000000 |
| Quintin 2015-type (S1) | 0.165005 | 6.060 | `2.9\times10^{-12}` | 1.00000000 |

So `r_{\rm after} = 16\epsilon c_s` for every bounce in the class and every `c_s`
(row 10's bounce-invariance of `r` survives `c_s < 1` unchanged), and
`f_{\rm NL}^{\rm after} = T_{f_{\rm NL}}\,f_{\rm NL}^{\rm pre}` with the `c_s = 1`
transfer values.

## 4. The joint table

`\epsilon = 3/2`; `f_{\rm NL}^{\rm after}` on the Quintin 2015-type background (S1,
`T = 0.16501`, the *most favourable* of the three).

| `c_s` | `r = 24c_s` | `r/0.036` | `f_{\rm NL}^{\rm pre}` | `f_{\rm NL}^{\rm after}` (S1) |
|---|---|---|---|---|
| 1 | 24 | 667 | `-2.188` | `-0.361` |
| 0.5 | 12 | 333 | `+22.19` | `+3.661` |
| 0.1 | 2.4 | 66.7 | `+8.022\times10^{2}` | `+1.324\times10^{2}` |
| `10^{-2}` | 0.24 | 6.67 | `+8.124\times10^{4}` | `+1.341\times10^{4}` |
| **`1.500\times10^{-3}`** | **0.036** | **1.00** | **`+3.611\times10^{6}`** | **`+5.959\times10^{5}`** |
| `10^{-3}` | 0.024 | 0.67 | `+8.125\times10^{6}` | `+1.341\times10^{6}` |
| `4.167\times10^{-4}` | 0.010 | 0.28 | `+4.680\times10^{7}` | `+7.722\times10^{6}` |

Note the sign flip: `f_{\rm NL}` crosses zero near `c_s \simeq 0.887` and is **positive**
everywhere on the tensor-viable branch — the flagship line's negative `f_{\rm NL}` is a
`c_s \simeq 1` feature and does not survive the fix.

## 5. Observational comparison at the tensor-viable `c_s`

At `c_s = 1.500\times10^{-3}` (exactly `r = 0.036`):

| background | `f_{\rm NL}^{\rm after}` | `\sigma` vs Planck `-0.9\pm5.1` | `\sigma` vs SPHEREx `\sigma=0.5` |
|---|---|---|---|
| poly | `7.060\times10^{5}` | `1.38\times10^{5}` | `1.41\times10^{6}` |
| LQC | `9.028\times10^{5}` | `1.77\times10^{5}` | `1.81\times10^{6}` |
| Quintin (S1) | `5.959\times10^{5}` | `1.17\times10^{5}` | `1.19\times10^{6}` |

Read the other way — the largest `c_s`-suppression the `f_{\rm NL}` data permit:

| requirement | min `c_s` (S1) | implied `r` | `r`/0.036 |
|---|---|---|---|
| `\|f_{\rm NL}^{\rm after}\| \le 5.1` (Planck `1\sigma`) | 0.4440 | 10.66 | 296 |
| `\|f_{\rm NL}^{\rm after}\| \le 10.2` (Planck `2\sigma`) | 0.3356 | 8.06 | 224 |
| `\|f_{\rm NL}^{\rm after}\| \le 0.7` (SPHEREx) | 0.7472 | 17.93 | 498 |
| `\|f_{\rm NL}^{\rm after}\| \le 0.5` (SPHEREx) | 0.7804 | 18.73 | 520 |

**The two allowed regions do not overlap.** The gap is a factor `296` in `c_s`
(`224`–`542` across the three backgrounds and the four bounds).

## 6. The no-go check

**Li+2016's own no-go (arXiv:1612.02036 §5).** They state it as: *"There is no region of
parameter space where `c_s` can give a small tensor-to-scalar ratio and small
non-Gaussianities simultaneously."* With the weaker bound of their era, `r < 0.07`, they
get `c_s \lesssim 0.0029` and `f_{\rm NL} \gtrsim 9.55\times10^{5}`. Our formula at
`c_s = 0.0029` gives `f_{\rm NL}^{\rm pre} = 9.66\times10^{5}` — their number reproduced.
With the current `r < 0.036` the bound tightens to `c_s < 1.500\times10^{-3}` and
`f_{\rm NL}^{\rm pre} = 3.61\times10^{6}`. **The lab's independent computation confirms
their no-go and strengthens it by a factor `3.8`.**

**Quintin, Sherkatghanad, Cai & Brandenberger 2015 (arXiv:1508.04141).** Their route to a
small `r` is not `c_s` but a scalar-only amplification through the bounce. Their Eq. (31)
requires `|\Delta\zeta_{k_*}/\zeta_{k_*}(\eta_{B-})| \gtrsim 49.1` (for `r < 0.12`), and
their Eq. (44) `f_{\rm NL} \sim (\Delta\zeta)^2 M_p^2/\Delta t_B` is why paying that price
in `\zeta` buys a large `f_{\rm NL}`. Tested against this lab's own backgrounds:

- suppressing `r` from 24 to 0.036 by scalar amplification alone needs
  `\lambda = \sqrt{24/0.036} = 25.82`;
- the A2 bounces supply `\lambda = 4.00` (LQC), `5.12` (poly), `6.06` (Quintin-type) —
  short by a factor `4.3`–`6.5`;
- and, per row 10, those bounces amplify **tensors and scalars identically**
  (`T_h/T_\zeta - 1 \le 8\times10^{-5}`), so their true contribution to `r` suppression
  is **zero**, not merely insufficient.

So both routes out of the tensor problem — small `c_s`, or bounce amplification of `\zeta`
— fail on this lab's own backgrounds, and the `c_s` route fails against the `f_{\rm NL}`
data by five orders of magnitude.

## 7. What would have to set `c_s < 1` (and why this lab's model does not)

`c_s < 1` is not a free dial: it is a property of the matter sector. A canonical scalar
field — the standard realisation of the `w \simeq 0` contraction, and the one this
program's background assumes — has `c_s = 1` identically, because its perturbations are
adiabatic with `\delta p = \delta\rho`. To get `c_s < 1` at `w \simeq 0` one needs a
non-canonical kinetic sector: k-essence `P(X,\phi)` with
`c_s^2 = P_{,X}/(P_{,X} + 2XP_{,XX})` (Garriga & Mukhanov 1999, hep-th/9904176), of which
DBI is the standard example (Chen, Huang, Kachru & Shiu 2007, hep-th/0605045). Li+2016
use exactly this: a k-essence/ghost-condensate field engineered to contract as dust while
carrying `c_s \ll 1`. A *literal* pressureless fluid is not an escape either — it has
`c_s = 0`, for which `z^2 = 2a^2\epsilon/c_s^2` diverges and the perturbation problem is
ill-posed (no sound horizon, no adiabatic vacuum to normalise to).

> **This lab's contraction does not provide `c_s < 1`.** Adopting it means replacing the
> matter sector with a specified k-essence Lagrangian, which is new physics this program
> has not modelled, and which — per §5 — is ruled out by `f_{\rm NL}` at any `c_s` small
> enough to help `r`.

## 8. Verdict against the ledger's success/kill

Ledger row 14: *"A viable `c_s` window with a stated `f_NL^{after}` → the flagship claim
re-anchored honestly; no viable window → Track A states the tensor problem as unresolved."*

> **KILL CONDITION MET. There is no viable `c_s` window.** Row 14 closes as a **null**.
> Track A must state the tensor problem as **unresolved**, and must state that the `c_s`
> remedy is closed, not merely untried. The flagship `f_{\rm NL} = -35/16` remains a
> `c_s = 1` prediction of a background that is in `\sim670\times` tension with the CMB
> tensor bound (row 10); this row establishes that the standard fix for that tension
> destroys the `f_{\rm NL}` prediction rather than re-anchoring it.

## 9. Paper-ready sentences (at evidential strength)

> The tensor tension of row 10 has a textbook remedy — a scalar sound speed `c_s < 1` in
> the contracting phase, which suppresses `r` while leaving the tensor sector untouched.
> Carrying the constant-`c_s` Mukhanov–Sasaki problem through
> (`z^2 = 2a^2\epsilon/c_s^2`, `v \to e^{-ic_sk\eta}/\sqrt{2c_sk}`, `c_T = 1`) gives
> `r = 16\epsilon c_s^{2\nu-2}` with `\nu = |q-1/2|`, hence `r = 16\epsilon c_s = 24c_s`
> for the dust contraction, in agreement with Ref. [Li *et al.* 2016] Eq. (3.18). The
> bound `r < 0.036` therefore requires `c_s < 1.5\times10^{-3}`.

> The same `c_s` enters the bispectrum with the opposite sign of benefit. The squeezed
> isoceles amplitude is `f_{\rm NL} = -165/16 + 65/(8c_s^2)`, whose `c_s\to1` limit is
> `-35/16` — exactly the value derived independently here in the canonical case — and
> which grows as `1/c_s^2`, the generic single-field scaling [Chen *et al.* 2007]. The
> bounce transfer is `c_s`-independent (for constant `c_s` the mode problem is the
> canonical one at wavenumber `c_s k`, verified numerically to `4\times10^{-11}` across
> all three backgrounds), so `f_{\rm NL}^{\rm after} = T\,f_{\rm NL}^{\rm pre}` with
> `T = 0.165`–`0.250`.

> At `c_s = 1.5\times10^{-3}` this gives `f_{\rm NL}^{\rm after} = 6\times10^{5}`–
> `9\times10^{5}`, some `10^{5}\sigma` above `f_{\rm NL}^{\rm local} = -0.9\pm5.1`
> [Planck 2018] and `10^{6}\sigma` above the SPHEREx target `\sigma \simeq 0.5`.
> Conversely, keeping `|f_{\rm NL}|` within Planck's `1\sigma` requires `c_s > 0.44`,
> i.e. `r > 10.7`. **The two allowed regions are disjoint by a factor of about 300 in
> `c_s`**, confirming and — with the current tensor bound — strengthening by a factor
> `3.8` the extended no-go theorem of Ref. [Li *et al.* 2016]. The alternative route,
> suppressing `r` by amplifying `\zeta` through the bounce [Quintin *et al.* 2015,
> Eq. (31)], requires `\lambda \gtrsim 26` here, while the bounces of Ref. [A2] supply
> `\lambda = 4.0`–`6.1` and, amplifying tensors identically, no net suppression at all.

> We therefore state the tensor-to-scalar problem of the matter-bounce background as
> **unresolved**, and record that it is not resolvable within this class by a reduced
> scalar sound speed: doing so is excluded by the non-Gaussianity data, and in any case
> requires a k-essence matter sector [Garriga & Mukhanov 1999] that the single-clock dust
> contraction used throughout this work does not contain.

## 10. What changes in the A3 paper (for the closure lane; this lane does not edit `main.tex`)

1. Wherever the `r` limitation from row 10 is stated, add one sentence closing the `c_s`
   escape with the `\sim300\times` disjointness number — otherwise a referee will ask.
2. State `f_{\rm NL} = -35/16` explicitly as a `c_s = 1` result, and note the sign flip
   (`f_{\rm NL} > 0` for `c_s < 0.888`) so the negative sign is not read as robust.
3. Cite Li *et al.* 2016's extended no-go and record that this work reproduces it
   independently and tightens it with `r < 0.036`.
