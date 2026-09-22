# Row 9b — does the row-9 Bardeen scheme selection extend to the LQC and polymer backgrounds?

**Lane:** `LS9-bardeen-lqc` · **Date:** 2026-09-22 · **Pre-registration:** `PREREGISTRATION.md` (committed
`d079d7bd`, before any number existed) · **Verdict: OUTCOME-UNIVERSAL(b) — pre-registered branch, gates
G1–G7 all PASS.**

**Headline.** The Bardeen route **does** extend. On the LQC-effective-dust and poly backgrounds — which,
unlike the Quintin-type parametrization, cross `rho + p = 0` **smoothly** — the Bardeen potential `Phi` and
its first derivative remain **continuous**, the divergence is confined to the momentum sector and is only
**logarithmic** with a closed-form amplitude, and the continuation through the crossing is the principal
value. The transmitted linear amplitude differs from scheme S1 on **all three** backgrounds, so the
selection is **background-independent in direction** — but its **magnitude is strongly background-specific**:

| background | `Q = 0` crossing | `R` ≡ transmitted `zeta_C` (Bardeen / S1) | closed form | `1/R` |
|---|---|---|---|---|
| Quintin-type | none (`Hdot` jumps) | `0.16004` | — | **6.248** |
| LQC effective dust | simple zero at `rho/rho_c = 1/2` | `0.500000` | **`1/2`** | **2.000** |
| poly (analytic non-LQC) | simple zero at `eta = ±1/sqrt3` | `0.375000` | **`3/8`** | **2.666** |

Consequently **A3M's LQC and poly rows are superseded in the same direction as its Quintin row already was,
but by 2.0× and 2.7×, not by the Quintin factor 6.25** — the S1 rows are *not* a conservative choice. The
`f_NL^after` linear transfer moves `-0.547 -> -1.094` (LQC) and `-0.428 -> -1.140` (poly), while `r_after`
moves `24.0 -> 96.0` and `24.0 -> 170.6`, i.e. the tensor no-go is **strengthened on both**. Separately,
A3M R11's ESSENTIAL evaluation-window item is closed by **computation**: a uniform `eta_*/eta_B = 15` sits in
the stationary region at every `k`-point and gives `f_NL^after[S2] = -1.249 / -1.249 / -1.246`, so the
committed `-1.25` survives the convention scan to 0.3 %.

**Artifacts (this dir):** `row9b_symbolic.py` -> `row9b_symbolic.log`, `symbolic_results.json`;
`row9b_backgrounds.py`; `row9b_numeric.py` -> `row9b_numeric.log`, `results.json`, `row9b_bardeen_lqc.png`;
`row9b_window.py` -> `row9b_window.log`, `window_results.json`; manifest
`reproducibility/manifests/experiments/a3-row9b-bardeen-lqc-poly.json`.
**Venue:** local CPU (numpy/scipy/sympy), symbolic 7.9 s + numeric 1.2 s + window 18 s, $0.
**Provenance rule:** *computed* = produced by the committed scripts here; *literature* = cited, not re-derived.

---

## 0. The reading, stated before anything else (unchanged from `PREREGISTRATION.md` §1)

The Bardeen equation takes `a(eta)` as its **only** background input. This lane therefore applies it under the
same reading that defines S1 and S2 throughout this program: `a(eta)` is given, and the linear scalar
perturbation is propagated as the classical single-minimally-coupled-scalar continuation on that `a(eta)`
(`c_s = 1`, arbitrary `V`, no anisotropic stress). **This is a continuation statement about a given `a(eta)`.
It is NOT loop-quantum-cosmology dressed-metric perturbation theory, and nothing here claims anything about
the LQC framework's own perturbation equations.**

**A structural fact about the LQC background, computed and not glossed (`row9b_symbolic.py` A5).** On the
committed `a2_transmission_linear.bg_lqc` the classical identity `rho + p = -2 Hdot` **fails**: the dust source
has `rho + p = x`, while `-2 Hdot = x(1-2x)`. Hence

```
z^2[S2, geometric]  =  2 a^2 eps  =  3 x^{-2/3}(1-2x)/(1-x)        (vanishes at x = 1/2)
z^2[S2, fluid]      =  a^2(rho+p)/H^2 = 3 x^{-2/3}/(1-x)           (never vanishes)
ratio = 1 - 2x
```

They are **two different variables on this background**, and the `T = 0.409` that A3M quotes as the LQC
effective-fluid number is the **fluid** one. It is not the quantity this lane computes and the two must not be
conflated. (They do coincide in one respect — §3.3.)

---

## 1. Leg A — the smooth NEC crossing, exactly (`row9b_symbolic.py`, every residual 0)

**A1.** With `Psi ≡ Phi' + Hc Phi` the Bardeen equation is exactly the first-order system

```
Phi' = Psi - Hc Phi ,        Psi' = (Q'/Q - Hc) Psi + (Q - k^2) Phi ,      Q = Hc^2 - Hc' = -a^2 Hdot
zeta = Phi + Hc Psi/Q ,      zeta' = -k^2 Hc Phi/Q ,      Xi = a^2 Psi/Q .
```
Residual against row 9's `Phi` equation: **0**. Residual of the `zeta'` identity: **0**. The single singular
coefficient in the whole system is `Q'/Q`.

**A2 — the crossing is a regular singular point.** `Q(eta_c) = 0` forces `h1 = h0^2` in
`Hc = h0 + h1 t + h2 t^2 + ...`, whence `Q = 2(h0^3 - h2) t + O(t^2)`, `t p(t) -> -1`, `t^2 q(t) -> 0`,
`t q(t) -> -h0`. Indicial equation `r^2 - 2r = 0`, roots **`{0, 2}`**.

**A3 — `Phi` and `Phi'` are continuous, and the degenerate constraint is derived not assumed.** The
`O(t^{-1})` recursion of the `r = 0` branch reads `-a0 h0 - a1 = 0`, i.e.

> **`Phi'(eta_c) = -Hc(eta_c) Phi(eta_c)`  for EVERY solution.**

This is the degeneration of the `0i` constraint at `rho + p = 0` that row 9's blind adjudicator flagged as a
limitation; here it is the ODE's own first recursion.

**A4 — the divergence is logarithmic, with a closed-form amplitude.** Because the exponents differ by the
integer 2, the `r = 0` branch carries a resonance. Solving the `t^0` coefficient gives

> **`C = -a0 k^2 / 2`,  i.e. the log amplitude is `-Phi(eta_c) k^2 / 2` multiplying `t^2 log t`.**

Hence `Phi ~ a0 - h0 a0 t + O(t^2 log t)` (continuous, `C^1`), `Phi''` diverges as `log t`,
`Psi = t(2C log t + C + 2a2) -> 0`, and
```
zeta  ->  finite part  +  c_log * log|t| ,        c_log = -k^2 Hc(eta_c) Phi(eta_c) / Q'(eta_c) ,
```
which is exactly what the independent identity `zeta' = -k^2 Hc Phi/Q` gives. **A logarithm is integrable, so
the continuation through the crossing exists; being logarithmic and not a pole, it has a unique symmetric
finite part — the principal value.**

**A5 — the two backgrounds, in closed form.**
`LQC`: `Q = x^{1/3}(1/2 - x)`, simple zero at `x = 1/2` (`dQ/dx = -2^{2/3}/2 != 0`), once on each side;
`a''/a = x^{1/3}(2x+1)/6` reproduces the committed `appa` exactly.
`poly`: `Q = 2(3u^2-1)/(1+u^2)^2`, simple zeros at `u = ±1/sqrt3` (`Q' = ±9 sqrt3/4 != 0`);
`-Q/a^2` reproduces the committed `Hd` exactly.
`Quintin-type`: `Hdot` **jumps** between `+Upsilon` and `-3H^2/2` and is never zero — **this background has no
`Q = 0` crossing at all.** That is precisely the structural gap row 9 could not test.

---

## 2. Leg B — the number (`row9b_numeric.py`)

### 2.1 What is computed, and why it is not `zeta(-eta_B)/zeta_C(+infty)`

A3M/`a2_transmission_linear` define `T_fNL = 1/lambda` with `lambda = zeta_C(+infty)/zeta(-eta_B)`: the
handoff surface is the NEC boundary. **On LQC and poly that surface is exactly the `Q = 0` point where, by
§1 A4, `zeta` is logarithmically divergent in the Bardeen continuation.** Measured (gate G7, `k eta_B = 1e-3`):

| background | measured log slope of `zeta` | Leg-A closed form | rel | `\|c_log / zeta_finite-part\|` |
|---|---|---|---|---|
| LQC | `1019.74` | `1016.97` | `2.7e-3` | **0.459** |
| poly | `2763.51` | `2758.65` | `1.8e-3` | **2.827** |

So the logarithm is real, its amplitude is Leg A's closed form to 0.2–0.3 %, and it is **not** small compared
with the finite part. The paper's handoff amplitude is therefore not a stable reference on these backgrounds,
and this lane does not build its result on it.

**The convention-free quantity used instead.** Both routes are started from the **same** dust adiabatic vacuum,
and in the dust contraction the Bardeen `zeta` and the S1 `zeta` are *the same function* (`epsilon = 3/2` is
constant there, so S1 ≡ S2 identically — row 9 §1 A1). Define

> **`R  ≡  | zeta_C^Bardeen(+infty) / zeta_C^S1(+infty) |`  at fixed incoming vacuum.**

`R` needs no handoff surface. And since `f_NL ∝ 1/zeta` under a common linear rescaling
(`B ∝ zeta^3`, `sum PP ∝ zeta^4`), **`f_NL^after,lin` scales as `1/R`** — that is the whole propagation rule.

### 2.2 Gates (all PASS; G1 was run first and nothing else would have been reported had it failed)

| gate | content | result |
|---|---|---|
| **G1** control | this lane's independent conformal-time chart integrator vs row 9's committed Quintin `lambda_Phi` (`0.969924/0.969946/0.970188`) | `0.969900/0.969943/0.970188`, rel `2.5e-5 / 3.1e-6 / 4.4e-7` — **PASS** |
| **G2** dust limit | `zeta/Phi -> 5/3` with `Phi` const | err `1.1e-16 / 4.0e-11 / 8.3e-9` — **PASS** |
| **G3** S1 reference | this lane's own projection vs committed `a2` `T_fNL` (`0.165005 / 0.250000 / 0.195501`) | `0.165012 / 0.249983 / 0.195467`, rel `4.3e-5 / 6.7e-5 / 1.8e-4` — **PASS** |
| **G4** crossing | P1 (`eps`-regulator) vs P2 (symmetric excision), each extrapolated | disagreement `6.0e-5` (LQC), `2.1e-4` (poly); last-three spreads `<= 2.7e-3` — **PASS** |
| **G5** Wronskian | `Phi_1 Xi_2 - Phi_2 Xi_1` (traceless system) over the sub-domain spanning both crossings and `H = 0` | `1.1e-11 / 2.7e-12 / 3.3e-11` — **PASS** |
| **G6** analytic | ODE-free super-Hubble principal-value quadrature (§2.4) | rel `2.5e-5 / 1.2e-4 / 2.0e-4` — **PASS** |
| **G7** log | measured log slope vs Leg A's `c_log` | rel `2.7e-3 / 1.8e-3` — **PASS** |

**G5's domain, stated because it was corrected.** Run over the *full* integration domain the gate FAILED on
poly (`9.1e+4`): over `|eta| <= 4000` the two basis solutions differ by many orders of magnitude and `W` is a
catastrophic cancellation of two nearly equal huge terms. Restricted to the bounded sub-domain that actually
contains the singular structure — both `Q = 0` crossings and `H = 0`, which is what the gate is for and what
row 9's own G3 did — it passes at `1e-11` with the two product terms of order unity. The failure was
numerical conditioning of the test, not of the solution; it is recorded rather than quietly rewritten.

### 2.3 `R`, with both principal-value prescriptions

`k eta_B = 10^-3` (the `k`-dependence over the whole validated band is `< 4e-4`):

| background | P1 `eps/eta_B` = 3e-3, 1e-3, 3e-4, 1e-4 | P2 `delta/eta_B` = same | limit |
|---|---|---|---|
| LQC | 0.497838, 0.499276, 0.499783, 0.499929 | 0.498699, 0.499568, 0.499871, 0.499958 | **0.50006** |
| poly | 0.371711, 0.373888, 0.374667, 0.374891 | 0.373928, 0.374644, 0.374894, 0.374966 | **0.37508** |

Both converge linearly in the regulator, from opposite sides, to the same value.
Quintin-type (no crossing, no regulator): `R = 0.160045 / 0.160055 / 0.160118`.

### 2.4 Independent analytic cross-check — and two exact closed forms

At `k = 0` the exact solutions are `zeta = C1 + C2 J_s`, `J_s = int deta/z_s^2`, and the dust adiabatic vacuum
has `C1 = C2 I_s` (i.e. `zeta(-infty) = 0`), so `zeta_C(+infty) = 2 C2 I_s`. In the dust tails
`z_eps^2 = 3 a^2 = 3 z_S1^2`, and matching the *same* `zeta(eta)` gives `C2_eps = 3 C2_S1`. Hence

> **`R = 3 I_eps / I_S1`,   `I_s = int_0^infty deta/z_s^2`,   `I_eps` a principal value through the `Q = 0` poles.**

Evaluated by direct quadrature with no ODE at all:

* **LQC:** `I_S1 = pi/sqrt3`; `PV I_eps -> 0.3022995 = pi/(6 sqrt3)`; **`R = 3(pi/(6 sqrt3))/(pi/sqrt3) = 1/2` exactly.**
* **poly:** `I_S1 = pi/4`; `PV I_eps -> 0.0981747 = pi/32`; **`R = 3(pi/32)/(pi/4) = 3/8` exactly.**
* **Quintin:** no crossing, ordinary integral, `R = 0.1600489` — matching the ODE's `0.1600449` to `2.5e-5`.

So `R = 1/2` and `R = 3/8` are exact rational numbers, obtained twice by independent routes.

**A third fact, worth stating for the paper.** `PV I_eps` on LQC equals `pi/(6 sqrt3)` — which is *exactly* the
effective-fluid mixing integral `a2_transmission_linear.fluid_scheme_contrast` already computes
(`I_inf_fluid_analytic_pi_over_6sqrt3`). The `(1 - 2x)` factor that distinguishes the geometric `z^2` from the
fluid `z^2` on this background **drops out of the principal value**. The two variables of §0 are different, but
their super-Hubble mixing integrals coincide. (This does **not** make `T = 0.409` the Bardeen number — that
value is built on the fluid variable's own handoff at `-eta_B`; see §3.2.)

---

## 3. Consequences, both directions (directive-F rule: neither half may be propagated alone)

### 3.1 The favourable half — `|f_NL|` gets larger on both new backgrounds

`f_NL^before = -35/16`; `T_eff ≡ f_NL^after,lin / f_NL^before = T_fNL[S1] / R`:

| background | `T_fNL[S1]` | `R` | `T_eff[Bardeen]` | `f_NL^after,lin` S1 -> Bardeen |
|---|---|---|---|---|
| Quintin-type | 0.1650 | 0.16004 | **1.031** | `-0.361 -> -2.255` |
| LQC | 0.2500 | 0.50006 | **0.500** | `-0.547 -> -1.094` |
| poly | 0.1955 | 0.37508 | **0.521** | `-0.428 -> -1.140` |

The Quintin row is a **consistency check, not a new result**: `T_eff = 1.031` and `f_NL^after,lin = -2.255`
reproduce the committed `lane9b2_s2_rawadm` values `~1.03` and `-2.256` (0.04 %), and adding that lane's
cubic `Delta_T = +1.007` returns `-1.249`, A3M's printed number.

### 3.2 What is NOT claimed — the cubic term on LQC/poly (declared out of scope in the pre-registration)

`f_NL^after = T f_NL^before + Delta` also carries the bounce's own cubic contribution, and `Delta` is
**scheme-dependent** (`-0.140` in S1 vs `+1.007` in the selected scheme, on Quintin). This lane computes the
**linear transfer only**. The raw-ADM in-in integral on LQC/poly carries the same `Q = 0` log structure at
cubic order and `lane9b2`'s `window_series`/`BounceModes` are written for the Quintin parametrization; that
computation is a separate, named step. Consequently the full `f_NL^after` on LQC/poly is reported **only as a
bracket between the two cubic endpoints this program has actually computed**, both labelled:

> LQC: `f_NL^after ∈ [-1.198 (Delta = Delta_S1), -0.087 (Delta = Delta_Quintin,S2)]`
> poly: `f_NL^after ∈ [-1.267, -0.133]`

**This bracket is a bracket. It must never be collapsed to a single value, and neither endpoint is a computed
`Delta` for these backgrounds.**

Also **not** claimed: that `T = 0.409` (A3M's LQC effective-fluid row) is superseded by `T_eff = 0.500`. Those
are two different constructions — `0.409` is `zeta_fluid(-eta_B)/zeta_C^fluid(+infty)` in the *fluid* variable,
`0.500` is `f_NL^after,lin/f_NL^before` in the *geometric* one. They are reported side by side, not merged.

**A pre-existing convention issue this lane names but does not fix.** A3M's LQC/poly rows pair
`T_fNL = zeta(-eta_B)/zeta_C(+infty)` — a handoff amplitude at `x = 1/2`, deep inside the bounce region — with
`f_NL^before = -35/16`, a *dust* value. On the Quintin-type background `-t_m` really is the end of the exact
dust phase, so no such mismatch arises there. On LQC and poly it does. `R` is immune to it (it involves no
handoff), which is the reason this lane's primary quantity is `R`.

### 3.3 The unfavourable half — the tensor no-go is strengthened on both

Row 18a established `lambda_T = lambda_zeta^S1` **identically** on every background and that the tensor
transfer is scheme-independent. With `r_after = 24 (lambda_T/lambda_zeta)^2` and
`lambda_zeta^Bardeen/lambda_zeta^S1 = R`:

| background | `r_after` S1 | `r_after` Bardeen `= 24/R^2` | vs BK18+Planck `r < 0.036` |
|---|---|---|---|
| Quintin-type | 24.0 | **937.0** | `6.7e2x -> 2.6e4x` |
| LQC | 24.0 | **96.0** | `6.7e2x -> 2.7e3x` |
| poly | 24.0 | **170.6** | `6.7e2x -> 4.7e3x` |

The Quintin value `937.0` reproduces row 18a's committed S2 number `9.37e2` — another independent check.
**Row 18's explicit gap "No S2 `r_after` for LQC/poly (lane 9b-2 (A1): `z_S2^2 = 0` at their `Hdot = 0`
crossings)" is now closed**, in the direction that makes the tensor channel worse on both.

---

## 4. Leg C — the evaluation-window convention (A3M R11 ESSENTIAL 2), closed by computation

R11 closed the item by *disclosing* that `lane9b2` uses the non-uniform rule `eta_*/eta_B = min(50, 0.2/k eta_B)`
(hence 50, 50, 20 at the three `k`-points). This leg scans `eta_*/eta_B ∈ {5, 7.5, 10, 12.5, 15, 20, 30, 50,
75, 100, 150, 200}` at all three `k` with the committed raw-ADM kernel, unmodified (`row9b_window.log`):

| `k eta_B` | 5 | 7.5 | 10 | 12.5 | 15 | 20 | 30 | 50 | 75 | 100 | 150 | 200 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1e-3 | -1.4198 | -1.2532 | -1.2496 | -1.2493 | -1.2492 | -1.2492 | -1.2491 | -1.2488 | -1.2483 | -1.2476 | -1.2455 | -1.2426 |
| 3e-3 | -1.4198 | -1.2531 | -1.2496 | -1.2491 | -1.2490 | -1.2487 | -1.2480 | -1.2457 | -1.2411* | -1.2346* | -1.2159* | -1.1895* |
| 1e-2 | -1.4197 | -1.2525 | -1.2485 | -1.2474 | -1.2464 | -1.2437 | -1.2359* | -1.2099* | -1.1579* | -1.0828* | -0.8557* | -0.5017* |

(* outside the `k eta_* <= 0.2` cap.)

**Pre-registered rule, reported first and as written:** "largest `eta_*` on a plateau (three consecutive within
0.5 %) subject to `k eta_* <= 0.2`" gives `eta_*/eta_B = 200 / 50 / 20` and `-1.2426 / -1.2457 / -1.2437`.
**That rule is degenerate here and I say so rather than hide it:** at `k eta_B = 1e-3` *every* triple inside the
cap qualifies, so "largest" selects the most `eta_*`-drifted one.

**Post-hoc refinement, labelled post-hoc because it was chosen after seeing the scan:** the well-motivated
criterion is *stationarity*, i.e. the **flattest** triple. That is `{12.5, 15, 20}` at `k eta_B = 1e-3` (spread
0.010 %) and at `3e-3` (0.033 %), and `{10, 12.5, 15}` at `1e-2` (0.172 %). A **single uniform convention
`eta_*/eta_B = 15`** therefore sits in the stationary region at every `k`-point, satisfies the cap at every
`k`-point (`k eta_* = 0.015 / 0.045 / 0.15`), and gives

> **`f_NL^after[S2] = -1.2492 / -1.2490 / -1.2464`  at `k eta_B = 10^-3 / 3x10^-3 / 10^-2`** — a spread of
> **0.22 %** across `k` and across the stationary window.

**Outcome: WINDOW-SETTLED.** The committed headline `-1.25` **survives** the scan; R11's ESSENTIAL was a real
disclosure gap, not a numerical error. The recommendation to A3M is to replace the non-uniform
`min(50, 0.2/k eta_B)` rule with the uniform `eta_*/eta_B = 15` and to quote `-1.25` with a stated 0.3 %
`eta_*`-systematic (i.e. three significant figures are justified; four are not).

---

## 5. Verdict against the pre-registration

**OUTCOME-UNIVERSAL(b)** (`PREREGISTRATION.md` §4.1): `|R - 1| > 0.02` on **both** LQC and poly, with G1–G7
all passing. The Bardeen selection is **background-independent in direction** — on every background tested the
`z = a` prescription transmits *more* `zeta` than the regular continuation does, so it *understates*
`|f_NL^after|` — and **background-specific in magnitude**, by 6.25× (Quintin), 2.00× (LQC), 2.67× (poly).
Row 9's "factor 6.25" is a Quintin-type number and must not be carried to the other two backgrounds.

**OUTCOME-BARDEEN-FAILS did not occur, and was a live possibility.** The pre-registration committed to
reporting it plainly if P1 and P2 had disagreed or `Phi` had diverged. They agreed to `6e-5`/`2e-4`.

---

## 6. What this does NOT establish (limits, stated plainly, not softened)

1. **Linear transfer only.** The cubic-order `Delta` on LQC/poly is not computed (§3.2) and the full
   `f_NL^after` there is a labelled bracket, not a number.
2. **A continuation statement, not LQC quantum cosmology.** §0. No claim is made about, or against, the
   dressed-metric framework's own perturbation equations; a refutation of a dressed-metric calculation is
   neither attempted nor implied.
3. **The two LQC `z^2` variables are different** (§0) and the paper's `T = 0.409` is the fluid one. This lane
   does not adjudicate between "which effective source is physical on an LQC effective background" — it
   adjudicates the *continuation* of a given `a(eta)` in classical GR.
4. **The principal value is a prescription.** It is derived to be the unique *symmetric* finite part of an
   integrable logarithm, and two independent implementations agree; but an asymmetric continuation is not
   excluded by anything computed here, and would shift `R`.
5. **`c_s = 1`, single scalar, no anisotropic stress**, and the bounce window requires the same kinetic-sign
   flip (`rho + p < 0`) the rest of the A3M transmission calculation already assumes. Inherited, not new.
6. **At `rho + p = 0` no metric-only variable is complete** — `Phi` stays finite and `C^1` and its equation
   regular, but the `0i` constraint degenerates to `Phi' + Hc Phi = 0` (now *derived*, §1 A3), so the full
   perturbation content at that instant needs the unreduced triple. Carried from row 9, refined here.
7. **The matching-surface and thin-shell caveats row 9 carried are not closed** by this lane either.

---

## 7. Independent blind adjudication

*(section written after the adjudication returned; see `ADJUDICATION.md` for the full text and the record of
the failed first attempt)*
