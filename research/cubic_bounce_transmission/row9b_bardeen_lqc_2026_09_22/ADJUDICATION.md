# Row 9b — independent blind adjudication: the record

Commissioned because the Leg-B outcome (OUTCOME-UNIVERSAL(b)) changes A3M's headline transmission statement,
which `PREREGISTRATION.md` §3 Leg D makes the trigger condition. Spawned **once**, as required.

## 1. Attempt 1 — Fable tier — FAILED, no output

The lane brief specifies `model: "fable"` for this adjudicator. It was spawned at that tier and **produced no
output at all**:

```
status: failed
Agent terminated early due to an API error: You're out of usage credits.
(error type rate_limit, HTTP 429, request id req_011CfJ8rpc4jEdjvzs4zNPvk,
 model sent to the API: claude-fable-5-1)
```

**This is recorded as FAILED-INFRA, never as a verdict.** A leg that produced no output is FAILED (directive
I4's rule, applied here to an internal adjudication rather than an EXT leg). Nothing was back-filled, inferred,
or attributed to it.

## 2. Attempt 2 — Opus tier — substituted, and labelled

Directive I2's principle — an infrastructure failure must not become the excuse to skip a check that is
independently valuable — applies. The blind adjudication was re-run with the **byte-identical prompt** at
`model: "opus"`.

**This is an Opus-tier adjudication and is labelled as such everywhere it is cited. It is NOT a Fable
adjudication, and no claim in this lane's output describes it as one.** Under the directive N-AMENDED routing
table Opus is the designated tier for "truth-audits, closure decisions, referee legs on non-flagship papers,
cross-model reconciliation"; the Fable tier is reserved for contested-math adjudication, which is what this
would have been, so the substitution is a genuine (and stated) reduction in the strength of the check.

## 3. The prompt, and what the adjudicator was and was not told

**Told:** the two backgrounds in exact closed form (`H^2 = (x/3)(1-x)`, `a = x^{-1/3}`, `Hdot = -x(1-2x)/2`,
`a''/a`, `eta_B = 1.0601459575` for LQC; `a = 1 + eta^2` for poly); the two candidate prescriptions P-A
(`z = a`) and P-B (`z^2 = 2 a^2 epsilon`); the structural fact that `Hdot` passes smoothly through zero on
these backgrounds, twice; the exact definition of the transfer ratio `R` to report, including the incoming
vacuum normalisation and the three `k eta_B` values; and, as pipeline-check reference values, scheme P-A's
`T = 0.250` (LQC) / `0.196` (poly) and the mixing integrals `pi/sqrt3` and `pi/4`.

**NOT told:** that the Bardeen potential is the variable this lane used; the `(Phi, Psi)` or `(Phi, Xi)`
system; the indicial exponents, the `t^2 log t` resonance, or the closed-form log amplitude; the
principal-value prescription or that two of them were used; the `3 I_eps/I_S1` relation; the values
`1/2`, `3/8`, or `0.160`; the verdict OUTCOME-UNIVERSAL(b); the existence of row 9 or of this lane's
conclusion; or anything about the direction the answer "should" come out.

**Forbidden:** reading this directory or `row9_scheme_independence_2026_09_19/`.

**Explicitly permitted:** answering "UNDECIDABLE", or "neither prescription". It was asked in terms for its
own strongest counter-argument against its own conclusion.

## 4. Verdict

*(filled in below when the adjudication returned; recorded whether or not it agrees)*

## 4. Verdict — CONFIRMS the numbers, REFUTES a claim this lane had made

**On the numbers: full independent agreement, by a different route.** The adjudicator derived, from first
principles and forbidden to read this directory:

* `R = 1/2` exactly on LQC and `R = 3/8` exactly on poly — **the same two rationals this lane obtained**;
* the *same* partial-fraction decomposition of the poly integrand (`-1/16`, `1/4`, `3/16`) and the same
  observation that the `1/(3 eta^2 - 1)` term is an odd logarithm whose principal value vanishes;
* the same structural fact about LQC — `rho + p = x` while `-2 Hdot = x(1-2x)`, so the background violates
  the GR Friedmann relation and the geometric and matter-kinetic weights are different functions;
* `zeta` logarithmically divergent at the crossing, `Pi = W zeta'` (hence the Bardeen potential) continuous
  and `C^1` through it — this lane's Leg A, reached via a Frobenius analysis in a different variable;
* no logarithm and no monodromy at the bounce `H = 0` itself (exponents `{0,3}`, half-integer Bessel order),
  so *that* surface is benign — consistent with row 9;
* and independently, the coincidence that the LQC principal value equals the matter-kinetic mixing integral.

It also corrected a presentational point: the mixing integrals `pi/sqrt3` and `pi/4` quoted to it are the
**one-sided** (bounce-to-infinity) values. They are, and this lane uses them one-sided on both sides of the
ratio, so `R` is unaffected — but the document now says "one-sided" explicitly.

**On the physics: it refuted this lane's uniqueness claim, and it was right.** The adjudicator showed that at
a simple sign-changing zero of `z^2` the operator has `z''/z = -1/(4u^2)` — the critical inverse-square
potential — so it is **not essentially self-adjoint** and admits a one-parameter extension family per surface;
the connection is `(A,B) -> (A + lambda B, B)` with `lambda` undetermined. It measured an O(1) consequence: an
asymmetric/complex continuation multiplies `R` by `|1+i|` (LQC) and `|1+i sqrt3|` (poly).

**This lane reproduced that in its own code before accepting it** (G10, `row9b_numeric.py`): the complex
contour `1/Q -> 1/(Q - i mu)` converges, as `mu -> 0`, to `0.706958` (LQC) and `0.749633` (poly) against the
adjudicator's predicted `0.707048` and `0.749932` — agreement to `1e-4`, and a limit **different from** the
principal value rather than converging back to it. A real extension parameter moves `R` linearly and reaches
`R = 1` — indistinguishable from scheme S1 — at `nu = pi` (LQC) and `nu = 3.02` (poly).

**Consequence: commit `b037af0c`'s G9 conclusion is retracted.** G9 varied the *width* of the excision, which
moves only within the principal-value family; it never probed the extension parameter. The findings document
now records the retraction in §2.6 rather than silently replacing the earlier text, the caveat is restored in
quantified form, and every `R` is labelled as the time-symmetric continuation.

**One place the adjudication strengthened the result.** It elevated the LQC matter-kinetic weight
`z_K^2 = a^2(rho+p)/(c_s^2 H^2) = 3a^2/(1-x)` from a coincidence this lane had merely noted to a **second,
prescription-free anchor**: on LQC that weight is strictly positive with no zero at all, so its continuation
is unambiguous, and it gives `1/2` independently. `R(LQC) = 1/2` is therefore robust in a way `R(poly) = 3/8`
is not. Both the upgrade and its named assumption (that the effective theory leaves the scalar kinetic weight
proportional to `a^2(rho+p)/H^2`) are now carried in §2.6(b).

**Its own strongest counter-argument, recorded rather than dismissed.** If the effective theory's scalar
sector carries the same `(1 - 2x)` factor in its kinetic term — plausible, since in holonomy-corrected
effective dynamics that factor also multiplies `k^2` and signals **signature change** rather than ordinary
evolution — then `z_K^2 = z_PB^2`, the LQC anchor disappears, the `Ḣ = 0` surface is where the effective
metric degenerates, and evolution through it is not a well-posed initial-value problem at all. In that case
LQC is as undecidable as poly. This lane has not derived which weight the effective theory produces and does
not claim to have; the caveat is carried verbatim in the findings and in the propagation note.

**Its stated confidence:** high (`>= 95 %`) on the mathematics; **moderate (`~65 %`)** on the physical claim
that LQC is resolvable and poly is not.

**Tier:** Opus, not Fable — see §1–§2. The check that caught this lane's error was therefore run at a *lower*
tier than the brief specified, which makes the error's survival through Leg A, Leg B and eight gates the more
worth recording.
