# Ledger row 18(b) — A3-cs-bounce: the `c_s`-dependence of the bounce's own cubic term

**Status:** DONE 2026-09-04. **Result: the bounce's own cubic contribution scales as
`(6c_s^2-5)/c_s^4` — it flips sign near `c_s = 0.913` and grows faster than the
transmitted contraction term (`1/c_s^4` vs `1/c_s^2`). Carrying the same `c_s` through
the bounce MOVES the row-14 window boundary UP, from `c_s >= 0.444` to `c_s >= 0.600`
(`r >= 10.7` to `r >= 14.4`), and raises `f_NL^after` at the tensor-viable
`c_s = 1.5e-3` from `~6e5` to `~1.4e11`. The no-go of row 14 is STRENGTHENED, not
relaxed; the boundary moves the wrong way.**
**Owner lane:** row18b_cs_bounce_cubic (does NOT touch `research/track_a3_multichannel/paper/`
or `row18a_s2_tensor/`)
**Artifacts (this directory):** `row18b_cs_bounce_cubic.py` → `results.json`,
`row18b_cs_bounce_cubic.log`, `row18b_cs_bounce_cubic.png`; manifest
`reproducibility/manifests/experiments/a3-row18b-cs-bounce-cubic.json` (registered in
`programs/bounce-theory.json`; validator PASSED, 0 errors).
**Date/venue/cost:** 2026-09-04, local CPU, $0, 8.0 s wall clock.

## 1. The question and why it is not already answered

Row 14 (`../../track_a3_multichannel/row14_cs_window/`) evaluated the joint `(r, f_NL)`
window with three ingredients: `r = 24c_s`, `f_NL^pre(c_s) = -165/16 + 65/(8c_s^2)`, and a
transmission `T` verified `c_s`-independent to `4e-11`. It then wrote
`f_NL^after = T f_NL^pre(c_s)` — i.e. the bounce's *own* cubic contribution, computed in
lane (b) as `Delta f_NL^bounce = -(5/24)rho_B` at `c_s = 1`, was left frozen at its `c_s = 1`
value and, being `O(0.1)`, silently dropped. That is not consistent: the lane (a) vertex
coefficients carry `c_s` explicitly, with `1/c_s^2` and `1/c_s^4` factors. This row carries
the *same* `c_s` through both terms:

> `f_NL^after(c_s) = T · f_NL^pre(c_s) + Delta f_NL^bounce(c_s)`.

## 2. Exactly how `c_s` enters scheme S1 (this is the crux)

**Mode functions: only through the sound horizon.** Scheme S1 is the *geometric* scheme:
`z = a` by definition, adopted precisely because the effective-fluid `z^2 = 2a^2eps/c_s^2`
diverges at the bounce where `eps -> -inf`. Because `z = a` does not contain `c_s`, `z''/z =
a''/a` is `c_s`-independent, and the Mukhanov–Sasaki equation is

> `mu'' + (c_s^2 k^2 - a''/a) mu = 0`,

so **`c_s` appears in the S1 linear problem only multiplying `k^2`** — i.e. only in the sound
horizon. The problem at physical wavenumber `k` with sound speed `c_s` *is* the `c_s = 1`
problem at wavenumber `k_s = c_s k`. This is the same statement row 14 §3 verified numerically
for the transmission, and it is why `T` is `c_s`-independent.

Crucially there is **no extra `1/sqrt(c_s)` amplitude factor**. The Bunch–Davies solution of
that equation is `v -> e^{-i c_s k eta}/sqrt(2 c_s k)`, and `Im(v* v') = -c_s k |v|^2 = -1/2`:
the standard `1/sqrt(2 c_s k)` normalisation *is* what the universal Wronskian condition
gives for the `c_s^2k^2` equation. Evolving at `k_s = c_s k` with `Im(mu* mu') = -1/2` therefore
reproduces the correct `c_s` normalisation automatically — verified in the log
(`Wronskian -0.50000000` on every leg, every background, every `c_s`). Implemented literally:
**modes at `k_s = c_s k`, every momentum kernel and dot product at the physical `k`.**
(The `1/(eps c_s)` enhancement of `P_zeta` that drives `f_NL^pre` lives in the *contraction's*
effective-fluid normalisation, `z^2 = 2a^2eps/c_s^2`; it is already inside `f_NL^pre(c_s)` and
must not be double-counted in the S1 bounce window, where `z = a` and `eps -> eps_eff`.)

**Vertices: the whole effect.** `c_s` enters `Delta f_NL^bounce` through the lane (a)
coefficients, kept exactly as tabulated, with the S1 substitutions `eps -> eps_eff = 1/2`,
`eta_sr -> 0`, `s = dot c_s/(c_s H) -> 0` (constant `c_s`), `lambda -> 0`. Conformal-time
coefficients (`c^conf = c_V a^{1-n_dot}`, explicit `1/a^2` of the operator absorbed):

| id | operator | `c^conf(c_s)` in S1 | at `c_s = 1` | ratio to `c_s=1` |
|---|---|---|---|---|
| V1 | `zetadot^3` | `-(a'/a)·(1/2)(1/c_s^2 - 1/c_s^4)` | `0` | new, but `∝ a'/a` is **odd** in `eta` ⇒ cancels |
| V2 | `zeta zetadot^2` | `a^2(3c_s^2 - 5/2)/(2c_s^4)` | `a^2/4` | **`(6c_s^2-5)/c_s^4`** |
| V3 | `zeta(∂zeta)^2/a^2` | `(1/2)(3/2 - c_s^2)/c_s^2` | `1/4` | `(3-2c_s^2)/c_s^2` (`(k eta_B)^2`-suppressed) |
| V4 | `zetadot ∂zeta ∂chi` | `-a^2/(2c_s^4)` | `-a^2/2` | `1/c_s^4` |
| V5 | `zeta^2 zetadot` | `0` (`eta_sr = 0`, `c_s` const) | `0` | — |
| V6 | `∂zeta ∂chi ∂^2chi` | `a^2/(16c_s^4)` | `a^2/16` | `1/c_s^4` |
| V7 | `∂^2zeta (∂chi)^2` | `a^2/(32c_s^4)` | `a^2/32` | `1/c_s^4` |
| R2 | `zeta zetadot/(c_s^2H)` | `F = 1/(c_s^2H)` | `1/H` | `1/c_s^2` |
| R4 | `eps[...]/(2c_s^2H)` | `F = 1/(4c_s^2H)` | `1/(4H)` | `1/c_s^2` |

(R1 `∝ eta_sr` stays 0; R3 `= 1/(4a^2H^2)` carries no `c_s`.) This is the **`c_s` extension of
lane (a) assumption (A3)**: the vertex `eps` is the S1 regulator `eps_eff = 1/2` while `c_s` is
retained exactly. It is a scheme assumption, not the dressed-metric `H_3` of Agullo+2017.

Lane (b) showed V2 supplies **99.97 %** of `Delta f_NL^bounce`, so the total inherits V2's
scaling. The closed form of lane (a) generalises to

> **`Delta f_NL^bounce(c_s) = -(5/24) rho_B · (6c_s^2 - 5)/c_s^4`** (S1, `k eta_B << 1`),

which is `-(5/24)rho_B` at `c_s = 1`, **changes sign at `c_s = sqrt(5/6) = 0.9129`**, and grows
as `+(25/24)rho_B/c_s^4` as `c_s -> 0`. The script confirms this ratio numerically against the
full in-in integral to `<= 3e-4` relative at every `c_s` and background (log, "V2 coefficient
scaling" lines).

## 3. Gate and numerics

The `c_s = 1` limit must reproduce lane (b). It does, as an `assert` in the script:

| background | `rho_B` | this row at `c_s=1` | lane (b) | rel. diff |
|---|---|---|---|---|
| Quintin2015-type | 0.669989 | `-0.139818` | `-0.139818` | `3.3e-6` |
| LQC-effective dust | 0.500000 | `-0.104311` | `-0.104311` | `3.2e-6` |
| poly-analytic non-LQC | 0.608998 | `-0.127111` | `-0.127111` | `3.9e-6` |

All at `k eta_B = 1e-3`, squeezed isoceles `k_1 = 0.02k`, Wronskian `-0.50000000` exactly.
V1's new `c_s != 1` coefficient integrates to `<= 2e-7` on every background — the expected
cancellation of an odd-in-`eta` coefficient against even `zeta' = C_2/a^2` legs.

## 4. The table — `c_s` × background

`T` and `f_NL^pre(c_s) = -165/16 + 65/(8c_s^2)` from row 14; `r = 24c_s` from row 14.

| `c_s` | `r` | `f_NL^pre` | background | `T` | `T·f_NL^pre` | `Delta f_NL^bounce` | **`f_NL^after`** |
|---|---|---|---|---|---|---|---|
| 1 | 24 | `-2.1875` | Quintin | 0.165005 | `-0.36095` | `-0.13982` | **`-0.50077`** |
| | | | LQC | 0.250000 | `-0.54688` | `-0.10431` | **`-0.65119`** |
| | | | poly | 0.195501 | `-0.42766` | `-0.12711` | **`-0.55477`** |
| 0.8876 | 21.30 | `+0.00059` | Quintin | 0.165005 | `+0.00010` | `+0.06107` | **`+0.06117`** |
| | | | LQC | 0.250000 | `+0.00015` | `+0.04562` | **`+0.04576`** |
| | | | poly | 0.195501 | `+0.00012` | `+0.05549` | **`+0.05561`** |
| 0.6 | 14.40 | `+12.2569` | Quintin | 0.165005 | `+2.02246` | `+3.05775` | **`+5.08021`** |
| | | | LQC | 0.250000 | `+3.06423` | `+2.28203` | **`+5.34627`** |
| | | | poly | 0.195501 | `+2.39625` | `+2.77942` | **`+5.17567`** |
| 0.44 | 10.56 | `+31.6555` | Quintin | 0.165005 | `+5.22332` | `+14.2918` | **`+19.5151`** |
| | | | LQC | 0.250000 | `+7.91386` | `+10.6660` | **`+18.5798`** |
| | | | poly | 0.195501 | `+6.18868` | `+12.9911` | **`+19.1797`** |

Two structural facts are visible. (i) At `c_s = 0.8876` — row 14's sign flip of `f_NL^pre` —
the transmitted term vanishes and `f_NL^after` is the bounce term **alone**; the true zero of
`f_NL^after` therefore moves to `c_s = 0.8936–0.8973` (per background). (ii) Below
`c_s ~ 0.6` the bounce term **exceeds** the transmitted contraction term, and by
`c_s = 0.44` it is 1.4–2.7× larger. The bounce is not a correction there; it dominates.

## 5. The boundary — does it move?

**Yes, and in the wrong direction.** Solving `|f_NL^after(c_s)| = 5.1` (Planck `1σ`) on
`c_s ∈ (0, 1)`:

| background | row 14 (`T f_NL^pre` only) `c_s^min` / `r^min` | **this row (+ bounce term)** `c_s^min` / `r^min` | `r` penalty |
|---|---|---|---|
| Quintin2015-type | 0.4440 / 10.66 | **0.5997 / 14.39** | ×1.35 |
| LQC-effective dust | 0.5143 / 12.34 | **0.6064 / 14.55** | ×1.18 |
| poly-analytic non-LQC | 0.4725 / 11.34 | **0.6020 / 14.45** | ×1.27 |

So the window in `c_s` where `|f_NL^after| <= 5.1` **shrinks** from `[0.44, 1]` to
`[0.60, 1]`, and the minimum tensor-to-scalar ratio compatible with Planck's `f_NL` rises
from `r >= 10.7` to **`r >= 14.4`** — from `296×` to **`400× the BICEP/Keck bound`**. The
three backgrounds, which spread over `0.444–0.514` in row 14, collapse to `0.600–0.606`
here: the bounce term `∝ rho_B` and the transmission `T = (1-rho_B)/2` are anti-correlated,
so adding them makes the boundary nearly bounce-independent — a robustness statement, not a
coincidence.

At the *tensor*-viable end the effect is far larger, because `1/c_s^4` beats `1/c_s^2`:

| at `c_s = 1.5e-3` (`r = 0.036`) | `f_NL^after`, row 14 | `f_NL^after`, with the bounce term |
|---|---|---|
| Quintin | `5.96e5` | `1.38e11` |
| LQC | `9.03e5` | `1.03e11` |
| poly | `7.06e5` | `1.26e11` |

i.e. `~2.3e5×` worse, `~10^10 σ` from `f_NL^local = -0.9 ± 5.1`.

**Answer to the ledger question:** the `c_s`-dependence of the bounce's own cubic term does
move the no-go boundary — it moves it *against* the model, by `~35 %` in `c_s` at the
`f_NL`-limited end and by five orders of magnitude at the `r`-limited end. Row 14's null
verdict is unchanged in direction and **strengthened in magnitude**; the gap between the two
allowed regions widens from `~296×` to `~400×` in `c_s`.

## 6. Assumptions and limits (unchanged from lanes (a)/(b), plus one)

(A1) super-Hubble, `k eta_B << 1` (evaluated at `1e-3`); (A2) `P(X,phi)` cubic action only —
no Horndeski/Galileon vertices; (A3′) **new here:** the S1 coefficients retain `c_s` exactly
while `eps -> eps_eff = 1/2`, a scheme extension of lane (a)'s (A3); (A4) constant `c_s`
across contraction, bounce and post-bounce (the boundary terms R2, R4 carry `1/c_s^2` but
contribute `< 2e-4` at every `c_s` tested, so the assumption is not load-bearing); (A5)
first-order in-in, no loops or backreaction; (A6) `f_NL^pre(c_s)` inherits Li+2016's k-essence
kinetic sector — the `lambda` (i.e. `zetadot^3`) coefficient is not fixed by `c_s` alone
(row 14 §2). Since the conclusion here is driven by a *faster* divergence than `f_NL^pre`'s,
a different `lambda` cannot rescue the window: it would have to cancel the `1/c_s^4` bounce
term against the `1/c_s^2` contraction term at every `c_s`, which no constant can do.
As in row 14, this lab's canonical/dust contraction does not itself supply `c_s < 1`.

## 7. Paper-ready sentences (at evidential strength)

> The reduced sound speed enters the bounce's own cubic vertices as well as the
> contraction's. In the geometric scheme (`z = a`) the sound speed does not touch the
> super-Hubble mode functions at all — the Mukhanov–Sasaki equation is
> `mu'' + (c_s^2k^2 - a''/a)mu = 0`, so `c_s` acts only through the sound horizon, and the
> Wronskian normalisation already carries the `1/sqrt(2c_sk)` of the Bunch–Davies state.
> The entire `c_s`-dependence of the bounce-window bispectrum is therefore carried by the
> vertex coefficients, whose dominant term `zeta zetadot^2` scales as
> `eps(eps-3+3c_s^2)/c_s^4`.

> With `eps -> eps_eff = 1/2`, the closed form of the bounce-window contribution generalises
> to `Delta f_NL^bounce = -(5/24) rho_B (6c_s^2-5)/c_s^4`, reproduced by the full numerical
> in-in integral to `3e-4` and reducing to `-(5/24)rho_B` at `c_s = 1` to `4e-6`. It changes
> sign at `c_s = sqrt(5/6) = 0.913` and diverges as `1/c_s^4` — faster than the transmitted
> contraction amplitude `T f_NL^pre ∝ 1/c_s^2`.

> Evaluating the joint window at a single, common `c_s` therefore tightens it. Keeping
> `|f_NL^after|` within Planck's `1σ` now requires `c_s >= 0.600` rather than `0.444`, i.e.
> `r >= 14.4` rather than `10.7` — `400×` the BICEP/Keck bound rather than `296×` — and the
> requirement is nearly independent of which of the three nonsingular bounces is used
> (`c_s^min = 0.600, 0.606, 0.602`), because the bounce contribution `∝ rho_B` and the
> transmission `(1-rho_B)/2` are anti-correlated. At the sound speed that would satisfy
> `r < 0.036`, `c_s = 1.5e-3`, the bounce term raises `f_NL^after` from `~7e5` to `~1.2e11`.

> The `c_s` remedy for the matter bounce's tensor problem is therefore not merely closed by
> the contraction's non-Gaussianity, as previously shown; it is closed more strongly once the
> bounce's own cubic vertices are evaluated at the same sound speed. This is a statement about
> the modelled class, computed in one scheme (`z = a`, `eps_eff = 1/2`), and we state it at
> that strength.

## 8. Ledger row 18 status line for item (b)

See `project-context/NEXT_SCIENCE_LEDGER.md` row 18.
