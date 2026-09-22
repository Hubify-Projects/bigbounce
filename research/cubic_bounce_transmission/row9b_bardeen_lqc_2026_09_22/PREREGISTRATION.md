# Pre-registration — row 9b: does the row-9 Bardeen scheme selection extend to the LQC and poly backgrounds?

**Lane:** `LS9-bardeen-lqc` · **Date written:** 2026-09-22 · **Status at writing: NO NUMBER HAS BEEN COMPUTED.**
This file is committed BEFORE the computation, on its own. Nothing below is adjusted after the fact; the
outcome is recorded against these criteria verbatim, including every failure branch.

## 0. The open problem (restated, not re-scoped)

Ledger row 9 / decision D-A3-9 was closed on 2026-09-19
(`../row9_scheme_independence_2026_09_19/`): the Bardeen potential `Phi` is a scheme-free variable through
`H = 0`, it selects scheme S2 on the **Quintin-type** background, and `f_NL^after` there collapses from the
band `[-1.25, -0.50]` to the single value `-1.25`. That lane stated its own limit 2 verbatim:

> "Computed on the **Quintin-type background only** — the one on which both schemes' cubic numbers exist and
> on which the band is stated. LQC/poly have `Hdot = 0` crossings at which, per §3, zeta is log-divergent; the
> Phi route is regular there, so extending it to those two backgrounds is a well-posed next step, not done here."

A3M v3M.0.28 (R11) prints that limit as its own Next-steps item (i), and its R11 board raised two ESSENTIAL
items on exactly this material (`DISPOSITIONS/A3M.md` R11, items 8 and 9): the regularity proof, and the
`f_NL^after[S2]` **evaluation-window convention**. A3M's table `tab:s1_after` currently reads

| background | `T_fNL` | `Delta f_NL^bounce` | `f_NL^after` | scheme |
|---|---|---|---|---|
| Quintin-type | 0.165 | -0.140 | -0.501 | S1 (superseded by the Bardeen selection) |
| LQC effective dust | 0.250 | -0.104 | -0.651 | S1 — **the paper's only computed value on this background** |
| poly (analytic non-LQC) | 0.196 | -0.127 | -0.555 | S1 — **ditto** |
| Quintin-type | ~1.03 | +1.00 | -1.25 | S2 raw-ADM (selected) |

So the paper currently states a **selected** value on one background and **superseded-scheme** values on the
other two. This lane asks whether that is honest or whether the LQC/poly rows move too.

## 1. The reading of "the Bardeen route on LQC/poly", fixed before computing

The Bardeen equation derived in row 9 (`row9_symbolic.py`, all residuals 0) takes **`a(eta)` as its only
background input**:

```
Phi'' + 2(Hc - pp) Phi' + (k^2 + 2 Hc' - 2 Hc pp) Phi = 0 ,   pp = (2 Hc Hc' - Hc'')/(2(Hc^2 - Hc')) ,
Hc = a'/a ,   Q = Hc^2 - Hc' = -a^2 Hdot ,   pp = Q'/(2Q) ,   mu = a^2/Q = -1/Hdot .
```

This lane therefore applies it under the **same reading that defines S1 and S2 in this program**: `a(eta)` is
given, and the linear scalar perturbation is propagated as the classical single-minimally-coupled-scalar
continuation on that `a(eta)` (`c_s = 1`, arbitrary `V`, no anisotropic stress). S1's `z = a` and S2's
`z^2 = 2 a^2 eps` are both variable choices within the same reading; `Phi` is a third and, per row 9, the one
whose equation is regular at the degenerate points. **Stated up front and carried into the output: this is a
continuation statement about a given `a(eta)`. It is NOT loop-quantum-cosmology dressed-metric perturbation
theory, and no claim is made about the LQC framework's own perturbation equations.**

**A structural fact about the LQC background that this lane must not paper over.** On
`a2_transmission_linear.bg_lqc` (`H^2 = (rho/3)(1 - rho/rho_c)`, `w = 0`, `x = rho/rho_c`, `a = x^{-1/3}`),
the classical GR identity `rho + p = -2 Hdot` **fails**: the dust source has `rho + p = x`, while
`-2 Hdot = x(1 - 2x)`. The two differ by exactly the factor `(1 - 2x)`, which vanishes at `x = 1/2`. The
"effective-fluid scheme S2" number the A3M paper quotes on LQC (`T = 0.409`,
`a2_transmission_linear.fluid_scheme_contrast`) uses `z^2 = a^2(rho+p)/(c_s^2 H^2) = 3 x^{-2/3}/(1-x)`, i.e.
the **dust** `rho+p`, whereas row 9's S2 is `z^2 = 2 a^2 eps = 3 x^{-2/3}(1-2x)/(1-x)`, i.e. the **geometric**
`-2 Hdot`. On LQC these are two different variables. Both will be reported separately and never conflated.

## 2. The regularity criterion, stated before it is tested

Every matter-contraction -> NEC-violating-bounce -> matter-expansion background has two kinds of degenerate
point. Row 9 established the criterion at both **for the Quintin-type parametrization, which jumps `Hdot`
discontinuously and therefore never actually sits at `Hdot = 0`**. LQC and poly are smooth and **do** cross it:

* LQC: `Hdot = -x(1-2x)/2` has a simple zero at `x = 1/2`, once on each side of the bounce.
* poly (`a = 1 + u^2`, `eta_b = 1`): `Q = 2(3u^2 - 1)/(1+u^2)^2` has a simple zero at `u = +-1/sqrt(3)`.

**The criterion this lane verifies (or falsifies):** at a simple zero of `Q` at `eta_c`, the Bardeen equation is
a *regular singular point* whose indicial exponents are `{0, 2}`, so that (i) `Phi` and `Phi'` remain finite and
continuous through `eta_c`; (ii) every solution satisfies `Phi'(eta_c) = -Hc(eta_c) Phi(eta_c)`, i.e.
`Psi = Phi' + Hc Phi` vanishes there; (iii) the divergence is confined to the momentum sector — `zeta`, `Xi`
and `delta phi` — and is at worst **logarithmic** (`zeta' = -k^2 Hc Phi/Q` has a simple pole), hence
integrable, so the continuation of `(Phi, Phi')` through `eta_c` exists and is unique as a **principal value**.

Integration variables fixed now: `Psi = Phi' + Hc Phi`, giving the system

```
Phi' = Psi - Hc Phi ,        Psi' = (Q'/Q - Hc) Psi + (Q - k^2) Phi ,
zeta = Phi + Hc Psi / Q ,    zeta' = -k^2 Hc Phi / Q ,    Xi = a^2 Psi / Q .
```

The single singular coefficient is `Q'/Q`. It will be handled by **two independent prescriptions**, and the
result is only quoted if they agree:

* **P1 (regulator):** `1/Q -> Q/(Q^2 + epsilon^2)` — the symmetric principal value, `epsilon -> 0` scanned.
  This is the same prescription row 9 §3 used for its smoothed-NEC control.
* **P2 (excision):** excise `|eta - eta_c| < delta` and connect by the local Frobenius expansion of the
  `{0,2}` pair, `delta -> 0` scanned.

## 3. What will be computed (exactly this, no more)

* **Leg A (symbolic, sympy).** On an arbitrary `a(eta)`: (A1) re-derive the `(Phi, Psi)` system above from row
  9's equation and confirm residual 0; (A2) obtain the indicial equation at a simple zero of `Q` and its roots;
  (A3) obtain the first recursion coefficient and confirm (or refute) `Phi'(eta_c) = -Hc(eta_c) Phi(eta_c)`;
  (A4) determine the leading behaviour of `zeta` and `Xi` at `eta_c` (log vs pole); (A5) specialise to the exact
  LQC and poly `a(eta)` and confirm the zeros of `Q` are simple, with their locations in closed form.
* **Leg B (numeric, control first).** A single general `(Phi, Psi)` integrator, background-agnostic. Run it on
  the **Quintin-type** background first and require it to reproduce row 9's committed `lambda_Phi` before any
  new background is touched. Then LQC and poly at `k eta_B in {1e-3, 3e-3, 1e-2}`, with P1 and P2 both.
  `lambda_Phi = |zeta_const-branch(+infty) / zeta(-eta_i)|` — the same definition row 9 used, with `zeta`
  evaluated only in the asymptotic dust regions where it is unambiguous.
* **Leg B-ref.** On the same backgrounds and with the same asymptotic projection, the S1 reference
  (`mu'' + (k^2 - a''/a) mu = 0`, `zeta = mu/a`) and, on LQC only, the two S2 variants of §1.
* **Leg C (evaluation window — R11 ESSENTIAL 2).** Using the committed
  `lane9b2_s2_rawadm.full_fnl_after_S2` unmodified, scan `eta_*/eta_B` over
  `{5, 10, 20, 30, 50, 75, 100, 150, 200}` at all three `k eta_B`, and adopt the convention: **the largest
  `eta_*` lying on a plateau subject to `k eta_* <= 0.2`**, where a plateau is three consecutive scanned
  `eta_*` agreeing to `<= 0.5%`. Report the value, the adopted `eta_*`, and the `eta_*`-systematic per
  `k`-point. If a `k`-point has no plateau, that is reported and its number is quoted with its full spread as
  the systematic — not hidden, not dropped.
* **Leg D (blind adjudication).** Spawned exactly once, `model: "fable"`, told neither this lane's conclusion
  nor its method and forbidden to read this directory, explicitly permitted to answer "undecidable" —
  **if and only if** the Leg-B outcome would change A3M's headline transmission statement (outcome 4.1(b) or
  4.1(c) below).

**Explicitly OUT OF SCOPE, named now so it cannot be quietly claimed later.** The cubic-order bounce term
`Delta_T` in the selected scheme on LQC/poly. It requires the raw-ADM in-in integral of `lane9b2` on those
backgrounds, whose integrand carries the same `Hdot = 0` log structure at cubic order and whose
`window_series`/`BounceModes` machinery is written for the Quintin parametrization. This lane will therefore
report, per background: (i) the **linear-transfer-only** number `f_NL^after,lin = f_NL^before / |lambda|`,
which is unambiguous; and (ii) the full `f_NL^after` **only where `Delta_T` exists** (Quintin). For LQC/poly the
cubic term is reported as an explicit **bracket** between the two computed endpoints available in this program
(S1's `-0.104 / -0.127` and Quintin-S2's `+1.007`), always labelled as a bracket and **never collapsed to a
single value**.

## 4. Pre-registered outcome conditions

### 4.1 Regularity + linear transfer (Leg A+B)

Let `L_bg` be `lambda_Phi` on background `bg`, and `S1_bg` the S1 value on the same background with the same
definition. Gates G1-G5 of §5 must pass, or the outcome is INCONCLUSIVE with the failing gate named.

* **OUTCOME-UNIVERSAL(a) — selection is BACKGROUND-SPECIFIC, S1 survives on LQC/poly.**
  `|L_bg/S1_bg - 1| <= 0.02` on BOTH LQC and poly. Then the Bardeen route exists on all three backgrounds but
  selects S1 where the crossing is smooth and S2 where it is jumped. A3M's LQC/poly rows stand unchanged; the
  paper gains a positive statement that its LQC/poly numbers are scheme-free, not merely S1. No headline
  change; no adjudicator.
* **OUTCOME-UNIVERSAL(b) — selection is BACKGROUND-INDEPENDENT in direction.**
  `|L_bg/S1_bg - 1| > 0.02` on BOTH. Then A3M's LQC and poly rows are superseded in the same direction the
  Quintin row already was, and `f_NL^after` moves on all three backgrounds. **Headline change -> adjudicator.**
* **OUTCOME-UNIVERSAL(c) — MIXED.** Agrees with S1 on one background and not the other. Reported exactly as
  that, with the structural difference between the two backgrounds identified. **Headline change -> adjudicator.**
* **OUTCOME-BARDEEN-FAILS.** P1 and P2 disagree by `> 2%` after both are extrapolated, or either fails to
  converge (last-three spread `> 2%`), or `Phi`/`Phi'` diverge at a crossing. **This is a real and publishable
  outcome and will be reported plainly: the Bardeen route does not extend to smooth NEC crossings, the
  scheme ambiguity is NOT resolved on LQC/poly, and A3M must keep its S1 label there while additionally
  disclosing that no scheme-free variable is available on those backgrounds.** No rescue will be attempted;
  no alternative variable will be substituted to obtain a number.
* **OUTCOME-SCOPE-LIMITED.** Leg A shows the construction's premise is violated on a background in a way that
  makes the equation itself ill-posed there (as opposed to merely singular at isolated points). Reported as a
  scope statement with the exact violated premise.

### 4.2 Evaluation window (Leg C)

* **WINDOW-SETTLED** — every `k`-point has a plateau by the §3 definition. The convention is adopted, the
  three numbers are quoted at their plateau values with their systematics, and R11 ESSENTIAL 2 closes with a
  computation rather than a disclosure.
* **WINDOW-PARTIAL** — some `k`-point has no plateau. The convention is still stated explicitly, that
  `k`-point's number carries its full measured spread as an open systematic, and the paper is told to quote
  fewer significant figures there. Under no circumstances is a plateau asserted where the scan does not show one.

### 4.3 Consequences that must be propagated together (directive-F self-favouring check)

If 4.1(b) or 4.1(c) holds, the same pass must state **both** directions, as row 9 did:
`|f_NL|` on LQC/poly moves (favourable to the survey-reach channel) **and** `r_after = 24 (lambda_T/lambda_zeta)^2`
on LQC/poly moves against the paper, since row 18a established `lambda_T = lambda_zeta^S1` identically on
every background and `lambda_T` is scheme-independent. Neither half may be propagated without the other.

## 5. Gates (must pass, or the result is INCONCLUSIVE with the gate named)

* **G1 — control.** The new background-agnostic `(Phi, Psi)` integrator reproduces row 9's committed
  `lambda_Phi` on the Quintin-type background (`0.969924 / 0.969946 / 0.970188`) to `<= 1e-4` relative.
  *Run first; nothing else is reported if this fails.*
* **G2 — matter limit.** On each background, in the dust tail, `zeta/Phi -> 5/3` to `<= 1e-6`.
* **G3 — S1 reference.** The S1 route, computed by this lane with the same asymptotic projection, reproduces
  the committed `T_fNL` of `a2_transmission_linear` (`0.250` LQC, `0.196` poly, `0.165` Quintin) to `<= 1%`.
* **G4 — crossing convergence.** P1 (`epsilon -> 0`) and P2 (`delta -> 0`) each converge (last-three spread
  `<= 2%`) and agree with each other to `<= 2%`.
* **G5 — Wronskian.** `W = (a^2/Q)(Phi_1 Psi_2 - Phi_2 Psi_1)` is conserved to `<= 1e-8` across the whole
  integration domain, including both `Q = 0` crossings and `H = 0`.

## 6. Integrity rules in force (unchanged, absolute)

`/never-fabricate-derivation`: every claim below carries an equation reference or the script line that computes
it. Nulls stay nulls; a failure of the Bardeen route is reported as a failure. No verdict is steered. No number
is quoted that this lane did not compute or cite to a committed artifact. The blind adjudicator, if spawned, is
spawned once, is told neither conclusion nor method, and is explicitly permitted to answer "undecidable"; its
answer is recorded whether or not it agrees.
