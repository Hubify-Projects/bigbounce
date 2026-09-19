# Ledger row 9 residual / decision D-A3-9 — is the S1/S2 transmission band physical?

**Lane:** `LS4-ledger9-scheme` · **Date:** 2026-09-19 · **Pre-registration:** `PREREGISTRATION.md` (committed
`117051bd`, before any number existed) · **Verdict: OUTCOME-S2 (pre-registered branch, all gates passed).**

**Headline.** There *is* a scheme-independent variable through `H = 0`: the **Bardeen potential Φ**. Its exact
equation carries no `z` and no `1/H`; it is regular at *both* degenerate points of a bounce background
(`H = 0` and `ρ+p = 0`); and the first-order system it generates is delta-free, so it needs **no junction
prescription at all**. Propagating it across the Quintin-type bounce gives

> **|λ_ζ| = 0.96992 / 0.96995 / 0.97019** at `kη_B = 10⁻³, 3×10⁻³, 10⁻²`

— i.e. **scheme S2 to 7×10⁻⁸, and 84 % away from scheme S1's 6.06.** The two-scheme band is **not** a physical
ambiguity: S2 is the consistent continuation and S1's `z = a` is not a solution of the Einstein equations on
this background. `f_NL^after` on the Quintin-type background collapses from the band `[−1.25, −0.50]` to the
single S2 value **≈ −1.25**, and the scheme label on the *linear* transfer can be dropped.

**Artifacts (this dir):** `row9_symbolic.py` → `row9_symbolic.log`, `symbolic_results.json`;
`row9_numeric.py` → `row9_numeric.log`, `results.json`, `row9_scheme_independence.png`;
manifest `reproducibility/manifests/experiments/a3-row9-scheme-independence.json`.
**Venue:** local CPU (numpy/scipy/sympy), ~1 s, $0. **Provenance rule:** *computed* = produced by the committed
scripts here; *literature* = cited, not re-derived.

---

## 1. Leg A — exact symbolic derivation (`row9_symbolic.py`, every residual 0)

From the linearised Einstein equations in longitudinal gauge for a single minimally coupled scalar
(`c_s = 1`, arbitrary `V(φ)`) on an arbitrary `a(η)`, with `ℋ = a'/a`:

| # | result | residual |
|---|---|---|
| A2 | the closed Φ equation `Φ'' + 2(ℋ − pp)Φ' + (k² + 2ℋ' − 2ℋ·pp)Φ = 0`, `pp ≡ φ''/φ' = (2ℋℋ' − ℋ'')/(2(ℋ²−ℋ'))`, follows from the **energy** constraint (the pressure equation is redundant given the momentum constraint + background) | 0 |
| A2b | self-adjoint with `μ = a²/(ℋ²−ℋ') = −1/Ḣ` | 0 |
| A3 | exact dictionary `ζ = Φ + ℋ(Φ'+ℋΦ)/(ℋ²−ℋ')`; at `H = 0` this is `ζ = Φ` exactly | 0 |
| A3b | exact identity `ζ' = −k²ℋΦ/(ℋ²−ℋ')` (super-Hubble ζ-conservation is manifest: `ζ' = O(k²)`) | 0 |
| A3c | with `Ξ ≡ μ(Φ'+ℋΦ)`: `Φ' = −Ḣ Ξ − ℋΦ` and `Ξ' = (a² − μk²)Φ + ℋΞ` — **both right-hand sides are delta-free** | 0 |
| A1 | **S2's equation `(z²ζ')' + k²z²ζ = 0`, `z² = 2a²ε`, IS implied** by the above | 0 |
| A1 | **S1's equation with `z = a` is NOT** implied; its residual ∝ `N[a] = −a a₁a₃ + 2a a₂² − a₁²a₂`, which vanishes on a power law `a = η^q` and only there | ≠ 0 |

**A1 in words: S1's `z = a` is the exact scalar variable if and only if `ε = −Ḣ/H²` is constant.** It is constant
in the matter contraction (where S1 and S2 therefore agree, both giving `f_NL^before = −35/16`) and it is *not*
constant in the bounce window — which is precisely where the two schemes part company.

**A5 — regularity at the two degenerate points.** Any matter-contraction → NEC-violating-bounce background has
two: `H = 0`, where `z²_S2 = −2a²Ḣ/H² → ∞` and the comoving lapse/shift `N₁ = ζ̇/H`, `ψ ⊃ −ζ/H` are singular; and
`ρ+p = 0` (`Ḣ = 0`), where `z²_S2 = 0`. The Quintin-type parametrization *avoids* the second by jumping `Ḣ`
discontinuously; every **smooth** bounce must cross it. For Φ:
* at `H = 0` with `Ḣ = Υ ≠ 0` the window equation reduces exactly to **`Φ'' + (k² + 2a²Υ)Φ = 0`** (friction
  coefficient identically zero — verified symbolically), manifestly regular;
* at a simple zero of `Ḣ` the indicial exponents are **{0, 2}**, both regular.

So Φ is regular at both; neither S1's nor S2's `z` is.

**A4 — junction condition, and a trap.** The *naive* reading of the self-adjoint form ("`[Φ] = 0`, `[μΦ'] = 0`")
is **wrong**: by A3c the potential term itself carries the delta (`μW = μ(k²+2ℋ'−2ℋ²) + ℋμ'`, and `μ = −1/Ḣ`
jumps). Absorbing it gives the delta-free pair `(Φ, Ξ)`, hence `[Φ] = 0` **and** `[Ξ] = 0`. Using A3/A3b these are
identically `[ζ] = 0` and `[z²ζ'] = 0` — **scheme S2's junction prescription, derived rather than assumed.**

## 2. Leg B — the number (`row9_numeric.py`)

Cosmic-time form `Φ̇ = −ḢΞ/a − HΦ`, `Ξ̇ = (a + k²/(aḢ))Φ + HΞ`, `ζ = Φ + HΞ/a`, integrated from the contraction
side of the NEC boundary straight through to the expansion side on the **exact committed background**
(`lane9b2_s2_rawadm.Quintin`, imported unmodified); `ζ_after` is the surviving constant branch, projected on the
exact matter basis (`matter_real_basis`, also imported unmodified); `ζ_before ≡ ζ(−t_m)` — the same definition
used for the S1/S2 reference values, which reproduce the published `6.06` and `0.9699`.

| `kη_B` | **λ_Φ (scheme-free)** | S1 (`z=a`) | S2 (`z²=2a²ε`) | dev. from S1 | dev. from S2 |
|---|---|---|---|---|---|
| 10⁻³ | **0.969924** | 6.0601 | 0.96992 | 0.8400 | 1.8×10⁻⁷ |
| 3×10⁻³ | **0.969946** | 6.0601 | 0.96995 | 0.8399 | 2.0×10⁻⁸ |
| 10⁻² | **0.970188** | 6.0592 | 0.97019 | 0.8399 | 1.8×10⁻⁹ |

**Gates (all PASS).** G1 matter-domination limit `ζ/Φ = 5/3` exactly (2×10⁻¹⁶); G2 constant-`ε` control — on the
pure matter contraction, where S1 ≡ S2 identically, the Φ route reproduces the exact adiabatic-vacuum mode to
5.5×10⁻⁹; G3 Wronskian `Φ₁Ξ₂ − Φ₂Ξ₁` (the system matrix is traceless, so it is exactly conserved) across
`t ∈ [−20, 20]`, spanning both junctions and `H = 0`, to 5.1×10⁻⁹.

**Rejected control (reported, not hidden).** Imposing the naive `[μΦ'] = 0` instead of `[Ξ] = 0` gives
λ = 6.79×10⁶, 7.55×10⁵, 6.79×10⁴ — exactly `∝ k⁻²`. It excites the decaying mode and destroys scale invariance,
which is an independent confirmation that the A3c junction (= S2's) is the right one.

## 3. Leg B′ — smoothed NEC crossing (the pre-registered tiebreaker)

Replacing each `Ḣ` jump by a `C²` blend of half-width `d` makes the background genuinely cross `ρ+p = 0`, where
`z²_S2 = 0`. There the exact integrand `k²Φ/(aḢ)` in `Ξ̇` is non-integrable: **ζ is logarithmically divergent at
the NEC crossing while Φ and its equation stay finite** — a statement about the comoving curvature perturbation
itself, not about either scheme's numerics. The crossing is linear, so the principal value is the unique
symmetric finite part; `1/Ḣ → Ḣ/(Ḣ²+ε²)` with both `d` and `ε` scanned.

`ε`-dependence is ≤ 10⁻⁴ throughout. In `d` (at `kη_B = 10⁻³`): 1.14520 (`d=0.05`), 1.04481, 1.00805, 0.98916,
0.97765, 0.97377, **0.97188** (`d=5×10⁻⁴`). The deviation from the limit is **linear in `d`** (measured ratios
1.97, 1.95 for successive halvings), so Richardson extrapolation gives

> **λ(d → 0) = 0.969985 / 0.969952 / 0.970192**, agreeing with the sharp-background Φ route to 6×10⁻⁵, 7×10⁻⁶, 5×10⁻⁶.

**G4 PASS** (spread over the last three `d` = 5.9×10⁻³ < 2 %). The smooth limit therefore confirms the sharp
result and, independently, confirms S2's junction prescription.

## 4. Verdict, stated at its evidential strength

**OUTCOME-S2, high confidence for the LINEAR transfer.** Four independent legs agree: (a) S2's ζ-equation is
implied by the exact Einstein equations and S1's is not unless `ε` is constant (symbolic, residual 0); (b) the
regular, `z`-free, junction-free Bardeen system gives λ = 0.96992, matching S2 to 7×10⁻⁸ and missing S1 by 84 %;
(c) the delta-free junction condition *is* S2's, derived; (d) the smooth-NEC-crossing limit reproduces the same
number. The factor 2.5 in `f_NL^after` is **not** a physical scheme ambiguity — it is one correct continuation
and one variable choice that does not solve the Einstein equations on these backgrounds.

**What this does NOT establish (limits, stated plainly).**
1. It adjudicates the **linear** MS-variable choice — which lane 9b-2 already identified as the dominant source
   of the factor 2.5 (`|λ| 0.97 vs 6.06`). The cubic-order question (raw-ADM vs Maldacena-form action) is
   adjudicated only indirectly, by the fact that the raw form is the one that is finite on the now-selected S2
   modes (lane 9b-2 §2, unchanged).
2. Computed on the **Quintin-type background only** — the one on which both schemes' cubic numbers exist and on
   which the band is stated. LQC/poly have `Ḣ = 0` crossings at which, per §3, ζ is log-divergent; the Φ route
   is regular there, so extending it to those two backgrounds is a well-posed next step, not done here.
3. If S1 is intended as a genuinely *different theory* (LQC dressed-metric quantum geometry) rather than a
   continuation of this classical background, then the correct statement is not "S1 is wrong" but "S1 does not
   apply to the Quintin-type background". Note that the dressed-metric framework's own published gauge
   dictionary is `𝓡 = −(a/z)δφ` with **`z = aφ̇/H`** — the S2 `z`, not `z = a` (source-cited transcription in
   `../lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md` §1.2, their Eq. 25). This lane did **not** re-derive
   the AAN/ABS equations and does not claim to have refuted a dressed-metric calculation.
4. `c_s = 1`, single minimally coupled scalar, no anisotropic stress. Horndeski/Galileon constraint corrections
   are untouched.

## 5. Consequences (the direction is mixed, which is worth saying explicitly)

* `f_NL^after` on the Quintin-type background: band `[−1.25, −0.50]` → **−1.25**. `|f_NL|` gets **larger**, i.e.
  this change is *favourable* to the paper's survey-reach channel.
* The tensor sector: row 18a established `λ_T = λ_ζ^S1` identically and that the tensor transfer is
  scheme-**independent** (its equation has no `z`, no `ε`, no `c_s`). With the scalar transfer now fixed at
  `λ_ζ = 0.970`, `r_after = 24(λ_T/λ_ζ)²` takes row 18a's **S2 value `≈ 9.4×10²`**, not the S1 value `24.0`.
  Against BK18+Planck `r < 0.036` that is `2.6×10⁴×` rather than `6.7×10²×`: the tensor no-go is **strengthened,
  and the paper's currently-quoted conservative number moves against the paper.** Both directions are reported.

---

## 6. Independent blind adjudication — CONFIRMS, by a different route

Commissioned per the lane's brief because §5 is a headline change. The adjudicator (Fable-tier, one agent, one
run) was given the background, the two schemes and their two numbers, and was told **neither this lane's
conclusion nor its method**; it was instructed to derive from first principles, forbidden to read this
directory, and explicitly told that "neither" and "undecidable" were acceptable verdicts.

**Verdict: S2. `λ_ζ = 0.970` at all three `kη_B`. Confidence ≈ 90 %.** It reproduced S1's 6.06 from the S1
recipe and identified it as "the transfer of a fictitious field with `ε ≡ const`".

It reached this by a **different construction**: instead of this lane's `(Φ, Ξ)` pair it used
`D ≡ −δφ/φ̇` (the comoving-slice displacement), giving the `z`-free, `1/H`-free cosmic-time system
`Ψ̇ = Ḣ D − HΨ`, `Ḋ = −(1 + k²/(a²Ḣ))Ψ` with `ζ = Ψ − H D`; and it fixed the junction from **Israel matching**
(continuity of the induced metric and extrinsic curvature on the matter's own comoving surface,
`T = D/a`), obtaining `[Ψ] = 0`, `[D] = 0` ⟹ `[ζ] = 0`, `[z²ζ'] = 0`. Independent agreements with §1–§3:

* `(z²ζ')' + k²z²ζ = 0` with `z² = 2a²ε` has **residual ≡ 0** on the exact Ψ-equation; S1 is exact iff `ε' = 0`.
* `ζ' = −k²Ψℋ/(ℋ²ε)` — the same exact identity as A3b.
* The delta-free/conserved form is the only well-posed distributional equation; "naive integration of the
  expanded forms is invalid" because `ε'/ε` (and `φ''/φ'`) carry deltas multiplied by sign-flipping functions
  — independently reproducing this lane's A4 trap and its rejection.
* The junction conditions it derives from Israel matching are **exactly S2's**, and it notes S1's `[a²ζ'] = 0`
  would require `Ψ₊ = −Ψ₋`, contradicting induced-metric continuity.
* **ζ diverges logarithmically at a smooth NEC crossing** — independent confirmation of §3.
* Tensors are not scheme-dependent (`z_T = a` is exact in GR) — consistent with row 18a.

**Two things it adds that this lane had not stated explicitly, and which are adopted here:**

1. **The kinetic-sign flip is a physical assumption, not a detail.** A canonical scalar cannot produce `Ḣ > 0`;
   the window requires `P = σX − V` with `σ: +1 → −1`, i.e. the ghost sector that lane 9b-2 flagged as its
   assumption (A5). Both this lane's `φ'² = 2(ℋ²−ℋ')` and the adjudicator's `D` inherit it. The result is
   therefore conditional on the same NEC-violating matter idealisation the rest of the A3M transmission
   calculation already assumes — it does not add a new assumption, but it should be named.
2. **At `ρ+p = 0` no metric-only variable is complete.** Φ (=Ψ) stays finite and continuous there, and its
   equation is regular (§1 A5, which the adjudicator confirms), but the `0i` constraint degenerates to
   `Ψ' + ℋΨ = 0` independently of `δφ`, so the full perturbation content at that point needs the unreduced
   triple `(Ψ, δφ, δφ̇)`. This refines rather than contradicts §1: it is the same degeneracy that makes ζ
   log-divergent there, and it is why §3's smooth-crossing computation is a principal-value statement.

**Its strongest argument against its own verdict** (recorded verbatim in substance, not dismissed): the answer
inherits the choice of matching surface and the thin-shell idealisation of the kinetic-sign flip, and a smooth
NEC crossing could shift the `O(1)` window contribution — though it notes comoving versus uniform-density
surfaces differ only by `O(k²η_B²)`. §3's `d → 0` control addresses the smooth-crossing half of this directly
(the limit is linear in `d` and lands on the sharp value to `5×10⁻⁶`…`6×10⁻⁵`); the matching-surface and
thin-shell halves are **not** closed by this lane and are carried as named open caveats.

**One number to keep straight when propagating.** The adjudicator states S1 overestimates `λ_ζ` by 6.25, hence
the inherited `|f_NL|` is too small by that factor. That is correct **for the linear transfer alone**. The
paper's `f_NL^after = T·f_NL^before + Δf_NL^bounce` also carries the bounce's own cubic term, which differs
between the schemes, so the change in the quoted `f_NL^after` is **−0.50 → −1.25, a factor 2.5, not 6.25**.
Do not propagate "6.25×" into the manuscript.
