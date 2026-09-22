# The ECH contact term: stress tensor, equation of state, and the Popławski scale

**Lane** `bb-LS13-p1n-essentials` · 2026-09-22 · closes DP1N-60, DP1N-61
**Target** `arxiv/paper1bc_ech_note/main.tex` @ `v1N.0.7` — §II (l. 205–225), §VII.D (l. 815–836)
**Method** derivation from the manuscript's own Lagrangian and its own parametrization,
with every relation validated against a case whose answer is independently known,
and every external claim checked against the primary source rather than memory.

---

## 0. Conventions (the manuscript's own)

`main.tex:167-168` — mostly-plus signature `η_IJ = diag(-,+,+,+)`, `ε_0123 = +1`,
`κ = 8πG = 8π/M_Pl²`. The contact term (`main.tex`, Eq. `eq:4fermi`):

```
L_4ψ = -(3κ/16) · [γ²/(1+γ²)] · (J5^I J5_I),     J5^I = ψ̄ γ^I γ^5 ψ .
```

Stress-tensor convention used throughout: `T_μν = -2 ∂L/∂g^μν + g_μν L`, fixed by
the scalar-field check `L = -½(∂φ)² - V ⟹ T_μν = ∂_μφ∂_νφ - g_μν[½(∂φ)²+V]`.
With this convention `ρ = T_μν u^μ u^ν`, `p = ⅓ h^μν T_μν`, `h_μν = g_μν + u_μu_ν`.

---

## 1. DP1N-60 — the contact term's stress tensor and equation of state

### 1.1 What the manuscript asserts

`main.tex:215-219`:

> writing the contact term's contribution to the effective stress tensor as
> `ρ_4ψ = -L_4ψ`, `p_4ψ = L_4ψ` for a term with no explicit time derivatives, a
> repulsive (halts collapse) contact interaction requires `ρ_4ψ + 3p_4ψ < 0`,
> i.e. `2 L_4ψ < 0`, i.e. `L_4ψ < 0`.

That is `w = p/ρ = -1`, and a repulsion condition `L_4ψ < 0`.

### 1.2 Step 1 — the naive variation, and why it is not yet the answer

`J5^I J5_I = η_IJ (ψ̄γ^Iγ^5ψ)(ψ̄γ^Jγ^5ψ)` is built from **flat** indices contracted
with `η`; the Dirac field is a tetrad-independent dynamical variable. So the only
tetrad dependence of `∫d⁴x e·L_4ψ` is through `det(e)`, and

```
T^(4ψ)_μν  =  g_μν L_4ψ            ⟹   ρ = -L_4ψ ,  p = +L_4ψ ,  w = -1 .
```

This reproduces the manuscript's sentence exactly, and it is a correct computation
**of that one term, at fixed ψ, before the field equations are imposed**. It is the
analogue of a scalar potential's own stress tensor. It is not, however, the
contact term's contribution to the *cosmological* energy budget, for the reason in
§1.3: the contact term is an interaction *among the fermions*, so switching it on
also changes the Dirac sector's own stress tensor, and the two changes do not cancel.

### 1.3 Step 2 — the on-shell (cubic Dirac) substitution

Varying `S` with respect to `ψ̄` gives the nonlinear Dirac–Hehl–Datta equation
(the manuscript's own `eq:gap` sector). Contracting it with `ψ̄`:

```
i ψ̄ γ^μ ∇_μ ψ  =  m ψ̄ψ  -  2 L_4ψ        (the factor 2 is the quartic's ψ̄-degree)
⟹  K ≡ (i/2)(ψ̄γ^μ∇_μψ - h.c.)  =  m ψ̄ψ - 2 L_4ψ
⟹  L_D(on-shell)  =  K - m ψ̄ψ  =  -2 L_4ψ .
```

The free Dirac Lagrangian vanishes on shell; with the contact term it does not, and
its value is `-2L_4ψ`. Hence the **total** matter stress tensor is

```
T_μν = T^kin,sym_μν + g_μν (L_D + L_4ψ) = T^kin,sym_μν - g_μν L_4ψ ,
```

where `T^kin,sym_μν = (i/4)[ψ̄γ_μ∇_νψ + ψ̄γ_ν∇_μψ - h.c.]`.

**Primary-source check.** Popławski performs precisely this substitution explicitly:
arXiv:1005.0893 Eq. (3) carries the contact piece as `-(3κ/16)(J5·J5) g_i^k`, and
after substituting his cubic Dirac equation (1) his Eq. (4) carries it as
`+(3κ/16)(J5·J5) g_i^k` — the overall sign flips, exactly by the `-2L_4ψ` above.
(His `T ≡ (2/√-g) δL/δg^{ik}` is minus this note's convention, and his signature is
mostly-minus; both flips are accounted for below.)

### 1.4 Step 3 — the kinetic bilinear on the interacting solution

`T^kin,sym` is *not* the free-dust stress tensor once the interaction is on. Its
`uu`-component follows from the same contraction:

```
ρ_k  ≡  T^kin,sym_μν u^μ u^ν  =  ρ_m - 2 L_4ψ ,
```

`ρ_m = m n_ψ` being the rest-mass (free-dust) piece.

**Validation against a known answer** (non-relativistic mean-field contact gas,
`L = ψ†(i∂_t)ψ - |∇ψ|²/2m - (g/2)n²`): the Euler–Lagrange equation gives
`⟨ψ†(i∂_t)ψ⟩ = T_kin + g n² = T_kin - 2 L_int`, the identical structure, with
`L_int = -(g/2)n²`. ✔

### 1.5 Step 4 — the total, and the equation of state

```
ρ_tot = ρ_k + L_4ψ = ρ_m - L_4ψ        ⟹   ρ_4ψ = -L_4ψ
p_tot = p_k - L_4ψ
```

Covariant conservation with a separately conserved dust (`n_ψ ∝ a^-3`, `ρ_m ∝ a^-3`)
fixes the remaining freedom:

```
ρ̇_tot + 3H(ρ_tot + p_tot) = 0
  ⟹ (-3Hρ_m + 6H L_4ψ) + 3H(ρ_m - 2L_4ψ + p_k) = 3H p_k = 0
  ⟹ p_k = 0 ,  and therefore  p_4ψ = -L_4ψ .
```

**Result.**

```
ρ_4ψ = -L_4ψ        (the manuscript has this RIGHT)
p_4ψ = -L_4ψ        (the manuscript has +L_4ψ — WRONG SIGN)
w_4ψ = +1           STIFF, not -1 ;  ρ_4ψ ∝ n_ψ² ∝ a^-6 ✔ self-consistent
```

**Four independent validations of `w = +1`:**

1. *Thermodynamic identity.* Any component whose energy density depends on `a` only
   through a conserved `n` satisfies `p = n dε/dn - ε`. Checked against four known
   answers: `ε∝n` → `w=0` (dust); `ε∝n^{4/3}` → `w=1/3` (radiation); `ε∝n⁰` →
   `w=-1` (vacuum); `ε∝n²` → `w=+1`. The contact term is the `n²` case.
   (`outputs/eos_and_scales.json`, block `A_validation_w_from_density_power`.)
2. *Mean-field contact gas.* The textbook Gross–Pitaevskii equation of state
   `p = (g/2)n² = ε_int` is `w=+1` and is obtained without using identity 1. ✔
3. *Scaling consistency.* `w=+1 ⟹ ρ ∝ a^{-3(1+w)} = a^-6`, which is what `n_ψ²`
   already does. `w=-1` would require `ρ̇=0`, i.e. `ρ` constant — flatly
   inconsistent with the manuscript's own `n_ψ ∝ a^-3` parametrization.
4. *ECSK / Weyssenhoff spin fluid.* The standard torsion-cosmology result for this
   very interaction is `ε_spin = p_spin = -κs²/4`, `s² = s_ij s^ij/2 = (ħcn)²/8` —
   equal energy density and pressure, i.e. `w = +1`, scaling as `a^-6`. The
   derivation above reproduces it, including the equality `ε = p`. ✔

So the corrected §II is *more* consistent with the literature it cites, not less.

### 1.6 The repulsion-sign condition — it INVERTS

```
manuscript:  ρ+3p = -L_4ψ + 3L_4ψ = +2 L_4ψ   ⟹  repulsion ⟺ L_4ψ < 0
correct:     ρ+3p = -L_4ψ - 3L_4ψ = -4 L_4ψ   ⟹  repulsion ⟺ L_4ψ > 0
```

**DP1N-60 is CONFIRMED.** The manuscript's stated equation of state is wrong for the
configuration it parametrizes, and the sign condition it derives from it is inverted.

### 1.7 What this does to the paper's claim — the bridge does NOT survive

**This section was rewritten after an independent blind-adjudication leg. The
first version of this note argued that a second sign error cancelled the first
and that the paper's conclusion survived. That was wrong, and the correction is
recorded here rather than silently replaced.**

Take the manuscript entirely at its own word. Its coefficient gives
`L_4ψ = -(3κ/16)f·(J5·J5)`, and `main.tex:216-221` states that the relevant
configuration is one in which `J⁵` is "normalized spacelike in the paper's
mostly-plus convention — the case realized by a spin-aligned fermion ensemble's
axial current in the nonrelativistic, high-spin-density regime". Then
`(J5·J5) > 0`, so `L_4ψ < 0`, and by §1.5:

```
ρ_4ψ = -L_4ψ > 0        (positive stiff energy density)
p_4ψ = -L_4ψ > 0
ρ_4ψ + 3p_4ψ = -4L_4ψ > 0   ⟹  gravitationally ATTRACTIVE
```

So the manuscript's own equations, with the manuscript's own stated
configuration and the corrected equation of state, give **attraction, not
repulsion** — the opposite of what §II concludes.

**This is not a novelty of this lane; it is a published result.** Kerlick
(Phys. Rev. D **12**, 3004 (1975)) found that the ECSK spin-spin contact
interaction is *attractive* for the totally antisymmetric spin angular momentum
density appropriate to the Dirac field — a result explicitly verified by
R. F. O'Connell, *"Attractive spin-spin contact interactions in the
Einstein–Cartan–Sciama–Kibble torsion theory of gravitation"*,
Phys. Rev. D **16**, 1247 (1977). The derivation above reproduces exactly that
sign for exactly that case.

**Why this does not abolish the torsion bounce.** The repulsive ECSK result
(`ε_spin = p_spin = -κs²/4 < 0`, §1.5 check 4) is obtained for a *semiclassical
Weyssenhoff spin fluid* — an unpolarized ensemble whose `⟨s²⟩` is a fluctuation
average — which is the object Popławski's bounce papers use. The Kerlick–O'Connell
attractive result is for the Dirac field's totally antisymmetric spin density.
The two coexist in the literature as a long-recognized tension, and which one
governs at bounce densities is a genuine open modelling question, not a
bookkeeping choice.

**Consequence for the manuscript.** §II picks one side of that open question by
assertion, in a single subordinate clause, without deriving the medium
expectation value `⟨J5^I J5_I⟩` that decides it — and the side it picks is
contradicted by its own equations once the equation of state is corrected, and by
the Kerlick–O'Connell branch of the literature for precisely the Dirac-field case
it treats. The claim that the contact term "carries the same repulsive sign at
every finite `γ`" is therefore **unsupported as written**.

**What survives, precisely:**

* The operator identification — `eq:4fermi` reduces exactly to the Hehl–Datta
  term as `γ→∞` — is untouched. This is an algebraic identity and does not
  depend on any sign of a medium expectation value.
* The `γ`-dependence, `α`, `β`, `β/α = 2.11`, the `γ²/(1+γ²) = 0.053`
  suppression, and all of §II.A's arithmetic are verified correct.
* The paper's Tier-I result (the perturbation-transparency theorem), the
  14-barrier catalog, the operator list, and the amplitude closures are all
  untouched by this item.

**What does not survive:** the independent sign-of-pressure argument, and with
it the claim that minimal ECH torsion is shown *here* to supply the repulsive
branch of Popławski's bounce at finite `γ`.

**Scope boundary (honest).** This lane establishes §1.5 and §1.6 — the equation
of state and the inverted sign condition — with high confidence and two
independent derivations. It establishes that the manuscript's own stated
configuration yields attraction. It does **not** claim to settle the
Weyssenhoff-vs-Kerlick question, and it does not claim the torsion bounce is
wrong. Relatedly — and **out of this lane's scope, flagged not claimed** — the
manuscript's Fierz row (`eq:fierz_row`) assigns the scalar channel coefficient
`+1` and calls it signature-independent; that row is what makes `G_s < 0` and
hence the NJL no-condensate result. It deserves its own lane, since `G_s`'s sign
is a separate headline claim.

---

## 2. DP1N-61 — the Popławski dark-energy scale

### 2.1 What the manuscript asserts

`main.tex:816-836`: Popławski "proposes a torsion-sourced cosmological constant ...
set by the average cosmic fermion (baryon) spin density", this "maps directly onto
Route 1 ... evaluated at the cosmic fermion number density `n_ψ`", and §II already
closes it because `κ n_ψ² ≃ 9.954×10⁻⁸⁰ eV⁴`, a ratio `≃3.9×10⁻⁶⁹` — "sixty-eight
orders of magnitude too small". Conclusion claimed: "a direct, quantitative rebuttal
of Popławski's own stated dark-energy mechanism, evaluated in his own proposed
channel at his own order of magnitude."

### 2.2 What arXiv:1005.0893 actually proposes (primary source, verbatim)

Title: *"Cosmological constant from quarks and torsion."* Abstract: *"We present a
simple and natural way to derive the observed small, positive cosmological constant
from the gravitational interaction of condensing fermions. ... We show that this
nonlinear term acts like a cosmological constant if these fields have a nonzero
vacuum expectation value. For quark fields in QCD, such a torsion-induced
cosmological constant is positive and its energy scale is only about 8 times larger
than the observed value."*

Its chain: Eq. (2) the effective Lagrangian with `+(3κ/16)(ψ̄γ_kγ⁵ψ)(ψ̄γ^kγ⁵ψ)`;
Eq. (7) `⟨0|ψ̄ψ|0⟩ ≈ -(230 MeV)³`; Eq. (8) SVZ vacuum saturation; Eq. (9)
`⟨0|(ψ̄γ^jγ⁵t^aψ)(ψ̄γ_jγ⁵t^aψ)|0⟩ = (16/9)⟨0|ψ̄ψ|0⟩²`; **Eq. (10)
`⟨0|ρ_Λ|0⟩ = (κ/3)⟨0|ψ̄ψ|0⟩²`**; Eq. (11) `⟨0|ρ_Λ|0⟩ ≈ (54 meV)⁴`.

The mechanism is the **QCD quark chiral condensate — a vacuum expectation value**.
There is no cosmic baryon number density anywhere in it. The manuscript's
description at `main.tex:817-819` misidentifies the source.

### 2.3 Independent recomputation

All numbers recomputed from scratch (`scripts/eos_and_scales.py`):

| quantity | value (GeV⁴) | vs `ρ_Λ,obs = (2.25 meV)⁴` |
|---|---|---|
| Popławski's own Eq. (10), `⟨q̄q⟩ = -(230 MeV)³` | `8.320×10⁻⁴²` | `3.25×10⁵` (density), `23.9×` (energy scale) |
| manuscript's own `(3/16)κ⟨q̄q⟩²`, `-(235 MeV)³` | `5.325×10⁻⁴²` | `2.08×10⁵` (density), `21.3×` (energy scale) |
| what §VII.D evaluates: `κ n_ψ²` at `100 cm⁻³` | `9.954×10⁻¹¹⁶` | `3.884×10⁻⁶⁹` |

The first row reproduces Popławski's stated `(54 meV)⁴` to three significant figures
(`53.71 meV`), confirming the formula and condensate value are read correctly.

*Honest discrepancy, flagged.* Popławski's abstract says his scale is "about 8
times larger than the observed value"; against the manuscript's own
`ρ_Λ,obs = (2.25 meV)⁴` the ratio is `23.9×` in energy scale, not `8×`. His
`(54 meV)⁴` itself is reproduced exactly, so the difference is in which observed
normalization he compares against, not in his mechanism. It does not affect any
conclusion here: at `8×` or at `24×` the mechanism *over*-produces by a factor
of order `10³–10⁵` in density, and in neither case is it `10⁻⁶⁹` under-produced. The
third row reproduces the manuscript's own `9.954×10⁻⁸⁰ eV⁴` and `3.884×10⁻⁶⁹` to
4 s.f. — **the manuscript's arithmetic is correct**; the defect is which quantity it
computes, not how.

**The gap between the two scales is `10^73.9` in density — ~74 orders of magnitude.**

### 2.4 Verdict — the rebuttal does not hold and must be WITHDRAWN

1. **Wrong source description.** Popławski's `ρ_Λ` is set by a vacuum condensate,
   not by "the average cosmic fermion (baryon) spin density".
2. **Wrong quantity evaluated.** §VII.D evaluates `κn_ψ²` at an ISM number density,
   ~74 orders of magnitude from the scale of his proposal. This is not "his own
   proposed channel at his own order of magnitude"; the phrase is not supported.
3. **The conclusion inverts at the correct scale.** At the condensate, the mechanism
   *over*-produces by `~2–3×10⁵` in density (`~21–24×` in energy scale) — which is
   why Popławski presents it as a success, not a failure. An under-production claim
   of `10⁻⁶⁹` is the opposite of the true result.
4. **The sign/gap-equation leg does not rebut him either.** §VII.D's second argument
   is that `G_s < 0` is repulsive so "the mean-field gap equation admits no nonzero
   condensate". Popławski does not generate a condensate from the torsion coupling —
   he imports the QCD chiral condensate, generated by QCD dynamics. The gap-equation
   argument is therefore not addressed to his mechanism.
5. **The manuscript's own §II.A forbids the substitution it then performs.**
   `main.tex:262-263`: "number density also does not fix the renormalized composite
   `⟨J5^I J5_I⟩`, a vacuum stress tensor, or an equation of state." §VII.D does
   exactly that.

A rebuttal *could* still be attempted at the correct scale (an over-production by
`~10⁵` in density is a real objection, and a far weaker one than `10⁻⁶⁹`), but that
is a different, non-trivial argument that this paper does not make and this lane does
not manufacture. **Recommendation: withdraw the "direct, quantitative rebuttal"
claim** in both §VII.D and the abstract, correct the description of `Poplawski2012`,
and state honestly what Route 1 does and does not close.

---

## 3. Summary table

| Item | Reviewer's claim | This lane's derived finding |
|---|---|---|
| DP1N-60 EOS | `w=+1`, not `w=-1` | **CONFIRMED.** `ρ_4ψ = -L_4ψ` (manuscript right), `p_4ψ = -L_4ψ` (manuscript wrong), `w=+1` stiff, `∝a^-6`; reproduces ECSK `ε_spin = p_spin = -κs²/4`. |
| DP1N-60 sign condition | inverts | **CONFIRMED.** `ρ+3p = -4L_4ψ`; repulsion needs `L_4ψ > 0`, not `< 0`. |
| DP1N-60 effect on title | targets "positive/bounce" claim | **The sign claim does NOT survive.** With the manuscript's own configuration and the corrected EOS, the term is gravitationally *attractive* — the published Kerlick (1975) / O'Connell (1977) result for the Dirac field. The operator identification (`γ→∞` → Hehl–Datta) survives; the independent sign-of-pressure argument must be withdrawn. |
| DP1N-61 wrong scale | ~74 orders | **CONFIRMED**, `10^73.9` recomputed independently. |
| DP1N-61 misdescribed source | quark condensate, not baryon density | **CONFIRMED** against the primary source verbatim. |
| DP1N-61 outcome at correct scale | ~`2×10⁵` over-production | **CONFIRMED**; Popławski's own value `(54 meV)⁴` reproduced to 3 s.f. |
| DP1N-61 disposition | re-evaluate or withdraw | **WITHDRAW.** The rebuttal does not hold and this lane does not manufacture a replacement. |
| Independent blind adjudication | — | `blind-adjudicator-opus`, given neither this lane's conclusions nor its method and permitted to answer "undecidable": independently reached `w=+1`, the inverted sign condition, the ECSK cross-check, and every DP1N-61 finding — and supplied the Kerlick/O'Connell branch that corrected this note's first §1.7. |
| Adversarial "57-order unit error" (prior board) | — | **Re-falsified a fourth time**: `κn_ψ²` and the `3.884×10⁻⁶⁹` ratio reproduce to 4 s.f. |
