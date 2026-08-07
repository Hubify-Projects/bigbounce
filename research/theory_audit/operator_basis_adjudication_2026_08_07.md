# Operator-basis independence adjudication — P1C v1C.0.11, Sec. V / Table III

**Date:** 2026-08-07
**Adjudicator:** independent symbolic computation, `research/theory_audit/operator_basis_adjudication_2026_08_07.py`
**Machine output:** `research/theory_audit/operator_basis_adjudication_2026_08_07.json` (all `[L##]` tags below are lines of that run's log, reproduced verbatim in the JSON `log` array)
**Target:** `arxiv/paper1c_nogo_survey/main.tex` — Eq. (8) `eq:dim4_defs` (main.tex:1459–1465), Table III `tab:dim4_parityodd` (label main.tex:1932, rows main.tex:1937–1942, caption main.tex:1916–1931), the quoted Nieh–Yan identity (main.tex:1472–1474), Check A (main.tex:1953–1967) and Check D (main.tex:1968–1982), abstract (main.tex:267–274)
**Claim adjudicated:** `project-context/peer-reviews/INT_v3/ROUND_2026-08-07-P1C-v1C.0.11-EXACTPDF-08688560-R9CONV/P1C_claude_r9_leg.md`, MAJOR-1 and MAJOR-2

Nothing was taken from the paper's released script. Every relation below was re-derived from explicit Cartan structure equations over an algebraically independent 2-jet, in exact rational arithmetic.

---

## HEADLINE VERDICT: **PARTIALLY-CORRECT**

| Referee claim | Verdict | Evidence |
|---|---|---|
| MAJOR-1: `{O1–O6}` is not a linearly independent basis | **REVIEWER-CORRECT** | rank 4, nullity 2 — `[L28]`, `[L29]` |
| MAJOR-1(a): `O1 ≡ O6` after tetrad conversion | **REVIEWER-CORRECT** (exact identity, off- and on-shell) | `[L31]`, `[L33]`, `[L49]`–`[L57]`, `[L59]`, `[L93]` |
| MAJOR-1(b): a relation ties `O1, O2, O4` | **REVIEWER-CORRECT in structure** | `[L30]`, `[L32]`, `[L62]`–`[L66]` |
| MAJOR-1(b) *literal* coefficients `O1 = O4 − O2` | **INCORRECT** — factor 2 on `O4` | `[L60]`, `[L61]`, `[L63]` |
| MAJOR-1: independent set is `{O2,O3,O4,O5}` | **REVIEWER-CORRECT** | `[L35]` |
| MAJOR-2: Table III's `O1 → Final = 0` is contradicted on shell | **REVIEWER-INCORRECT** | `[L78]`, `[L94]`, `[L97]`, `[L98]`, `[L99]` |
| — new finding, neither party | Table III's **`O4` row is wrong as printed** | `[L78]`, `[L81]`, `[L86]`, `[L89]`, `[L91]` |

The paper's *physics* conclusion is untouched by all of this, and one of the two corrections **strengthens** the no-go.

---

## 1. What was computed, and in what conventions

Conventions are fixed once in the module docstring and used throughout: mostly-plus `η = diag(−1,+1,+1,+1)` (the paper's own choice, main.tex Check D); `ε` is the Levi-Civita **symbol** with `ε^{0123} = +1`. Every one of O1–O6 carries exactly one `ε`, so the symbol-vs-tensor choice is a single overall `1/√−g` common to all six and cannot change a rank, a null space, or the truth of any homogeneous linear relation. Curvature is that of the **full torsionful** connection, per the paper's construction rule (main.tex:1397–1401).

Torsion irreducible decomposition (`T_{abc} = −T_{acb}`) into vector / axial / tensor was built and verified as an exact direct sum: `4 + 4 + 16 = 24` `[L08]`, with exact reconstruction `[L05]` and the correct orthogonality properties `[L06]`, `[L07]`. The paper's on-shell Cartan torsion `T^{abc} = κ S^{abc} = (κ/4) ε^{abcd} J^5_d` is verified to be **pure axial** — vector part zero, tensor part zero `[L09]`. This fact turns out to decide MAJOR-2.

The six operators were transcribed from Eq. (8) and written as exact polynomials in an algebraically independent 2-jet — `e(16), ∂e(64), ∂∂e(160), ω(24), ∂ω(96), J⁵(4)` `[L13]` — via the Cartan structure equations `[L14]`. Sizes: 432, 480, 360, 624, 240, 432 monomial terms `[L18]`–`[L23]`.

## 2. Rank and null space (off-shell, exact over ℚ)

Expanding all six over a **common basis of 1368 independent jet monomials** `[L27]` gives a 6×1368 exact rational coefficient matrix of

> **rank = 4** `[L28]`, **nullity = 2** `[L29]`

with the two null vectors (ordering `O1…O6`)

> `[1, 0, 0, 0, 0, −1]`  ⇔  **`O1 − O6 = 0`** `[L31]`
> `[2, 2, 0, −1, 0, 0]`  ⇔  **`2·O1 + 2·O2 − O4 = 0`** `[L30]`

each verified symbolically to have identically vanishing residual `[L32]`, `[L33]`. An exact-integer Gram certificate `G = M Mᵀ` independently confirms rank 4 `[L34]`, and an entirely separate 6×8 evaluation matrix built from random exact-rational Einstein–Cartan configurations also returns rank 4 `[L58]`.

The referee's proposed independent subset `{O2, O3, O4, O5}` **is** independent, rank 4 `[L35]`. So is `{O1, O3, O4, O5}` `[L36]` and `{O1, O2, O3, O5}` `[L37]`; `{O1, O2, O3, O4}` is not (rank 3) `[L38]`.

**Rank in the EFT sense.** "Operator basis" normally means independent *modulo total derivatives*. O2 (Nieh–Yan) and O3 (Pontryagin) are exact forms — the paper's own disposal class (i) — and span a 2-dimensional subspace `[L39]`. Quotienting:

> **rank modulo total derivatives = 4 − 2 = 2** `[L40]`, `[L41]`

i.e. in the sense the word "basis" is normally used, the six named invariants carry only **two** independent operators, `{O4, O5}` — and on shell even those collapse (§4).

## 3. MAJOR-1(a): `O1 ≡ O6` — confirmed, by an independent route

`O1 − O6 = 0` is exact `[L59]`. To make this more than a restatement of the tetrad conversion, `O6` was recomputed from a **completely independent construction**: the affine connection from the tetrad postulate, its own Riemann tensor `R^λ_{σμν}` built from `Γ` alone, then lowered with `g_{μν} = η_{IJ}e^I_μ e^J_ν`. For three independent random exact-rational configurations, all 256 components satisfy `R_{ρσμν}^Γ = e^I_ρ e^J_σ R_{IJμν}^ω` `[L49]`, `[L52]`, `[L55]`, and the Γ-route `O6` equals the tetrad-form `O1` exactly: `−2162/147`, `21170/441`, `4588/441`, differences all 0 `[L50]`, `[L53]`, `[L56]`. The identity also holds on shell `[L93]`.

A potential ambiguity was checked and **dismissed**: with torsion the pair-exchange symmetry of `R` fails, so "which index pair sits in slots 1,2 of `ε^{μνρσ}R_{μνρσ}`" could in principle matter. It does not — the swap is an even permutation of the `ε` indices, verified numerically at `[L51]`, `[L54]`, `[L57]`.

The alternative reading in which `O6` is built from the **Levi-Civita** curvature `R̊` was also computed: `O6 = 0` identically `[L104]`, so `O6` is then the zero operator and still not an independent sixth member; the rank of the remaining five is again 4 `[L105]`, `[L106]`. **The rank is 4 under both readings** — the conclusion does not depend on resolving that ambiguity.

## 4. MAJOR-1(b): the Nieh–Yan relation — exists, with different coefficients

The referee's literal relation `O1 − (O4 − O2) = 0` is **false** `[L60]`; the residual is exactly `(−1/2)·O4` `[L61]`. The true relation, read off the verified null space, is

> `O2 = (1/2)·O4 + (−1)·O1`, residual identically 0 `[L62]`, `[L63]`
> equivalently **`O1 = (1/2)·O4 − O2`** `[L64]`

This is cross-checked against the strict differential-form normalisation `d(e_I∧T^I)_dens = (1/4)O4 − (1/2)O1`, consistent `[L65]`. The **existence** of the three-operator relation is normalisation-independent; the referee's `1:1:1` coefficients carry a factor-2 slip on `O4`, which is traceable to the fact that **the paper never fixes the form-vs-density normalisation of "NY"** in Eq. (8) or Table III `[L66]`. This module's chosen normalisation is stated explicitly in the docstring (`O2 := ∂_μ(ε^{μνρσ} e_{Iν} T^I_{ρσ})`); a different admissible reading rescales `α, β` but not the rank.

## 5. MAJOR-2: Table III's `O1 → Final = 0` — the referee is wrong

The referee argues: by Nieh–Yan, `O1 = O4 − O2 → κ(J⁵·J⁵) − 0`, so Table III "reads `0 = κ(J⁵·J⁵) − 0`, an internal contradiction". That inference presumes `O4 → κ(J⁵·J⁵) ≠ 0` on shell. It does not.

> **On shell, the ε-contracted torsion-square vanishes identically: `O4 = 0`** `[L78]`, `[L81]`

Reason, computed: `O4 = T_I∧T^I` is supported only by the **non-axial** torsion irreps. Restricted to the pure vector irrep it is 0 `[L83]`; restricted to the pure axial irrep it is 0 `[L84]`; only the tensor irrep `q` (and vector×axial cross terms) can support it `[L82]`, `[L85]`, `[L86]`. Minimal-ECH Cartan torsion is pure axial `[L09]`, hence `O4 ≡ 0`. This is confirmed independently in a genuine **curved** on-shell Einstein–Cartan configuration built by solving the Cartan equation for `ω` given `T = κS ≠ 0` (max `|T^I_{μν}| = 121/972`) `[L90]`: the computed six-vector is `[91/405, −91/405, ≠0, 0, −198016/98415, 91/405]` `[L91]`, with `O4 = 0` `[L94]`.

Consequently, with `O4 = 0` the verified Nieh–Yan relation gives `O1 = −O2` exactly — confirmed numerically, `O1 + O2 = 0` `[L95]`, `[L97]`. So on shell `O1` **is minus the Nieh–Yan total derivative**: not pointwise zero `[L92]`, but contributing **zero to the equations of motion and zero to the vacuum energy** — exactly the status Table III itself assigns rows O2 and O3 ("`0` (EOM)"). Table III's `Final = 0` for O1 therefore **survives** `[L98]`, and the referee's "internal contradiction" is **falsified** `[L99]`.

What *is* defective is the **stated reason**. Check A was independently reproduced — a generic Riemann with pair antisymmetry plus the first Bianchi identity (20 free components remaining) gives `ε^{μνρσ}R_{μνρσ} = 0` `[L70]` — but that Bianchi identity is the **torsion-free** one, precisely what `T = κS ≠ 0` violates `[L71]`. On an explicit Levi-Civita configuration all of O1, O2, O4, O5, O6 vanish and only O3 survives `[L68]`, `[L69]`, so "vanishes (Bianchi, Check A)" is correct **only on the torsion-free branch** `[L70]`.

## 6. New finding (neither the paper nor the referee): Table III's O4 row is wrong

Table III (row main.tex:1940) lists `O4` with "Fate (bare) → `κ²(J⁵·J⁵)`, Fierz basis" and "Final → `κ(J⁵·J⁵)`"; the caption repeats it (main.tex:1923–1926) and App. A 1 asserts `O4^{[4]} = O5^{[4]}` in prose (main.tex:1906–1913). As computed:

- `O5` reproduces its Table III fate exactly: `O5 → (−3/2)·κ(J⁵·J⁵)` `[L79]`, `[L80]`.
- `O4` does **not**: `O4 ≡ 0` on shell `[L78]`, `[L81]`, so `O4^{[4]} = 0 ≠ O5^{[4]} = (−3/2)κ(J⁵·J⁵)` `[L88]`, `[L89]`.

The source of the error is identifiable. Check D proves `S_{abc}S^{abc} = −(3/8)(J⁵·J⁵)` — reproduced here exactly, `T_{abc}T^{abc} = −(3/8)κ²(J⁵·J⁵)` `[L87]` — but that is the **ε-free, parity-even** square `T_{abc}T^{abc}`, a *different invariant* from `O4 = ε^{μνρσ}T^I_{μν}T_{Iρσ}` as defined in Eq. (8) `[L86]`. The paper applies Check D's identity to the wrong contraction.

**This strengthens the no-go**: an operator contributing nothing at all is a stronger disposal than one contributing a Planck-suppressed contact term `[L89]`.

## 7. Net on-shell picture

Every member is either an exact total derivative (`O2`, `O3`, and `O1 = O6 = −O2`) or identically zero (`O4`), with a single operator carrying nonzero vacuum-energy content: `O5^{[4]} = (−3/2)κ(J⁵·J⁵)` `[L88]` — Planck-suppressed and inside the Fierz-closed basis. That is the paper's conclusion, reached by a cleaner route than the paper's own.

---

## What P1C must change

Nothing in the physics. Four textual/tabular corrections, all local:

1. **Sec. V, abstract, Sec. VI, Sec. VII — "basis" → "spanning list" / "generating set".** The head-count "six-member basis" is not defensible: computed rank is 4 as densities `[L28]` and 2 modulo total derivatives `[L40]`. Either recount ("four independent densities presented as six named invariants") or state explicitly that the six are a deliberately redundant *generating set* of recognisable invariants. The abstract's "a six-member basis {O1–O6}" (main.tex:267) and the identical phrasing at main.tex:319 and main.tex:368 all need the same edit.

2. **State the two relations explicitly** after Eq. (8): `O1 = O6` (tetrad conversion — the paper already performs this conversion for Eq. (7), main.tex:1376–1378), and `O1 = ½O4 − O2` (Nieh–Yan, in the density normalisation `O2 := ∂_μ(ε^{μνρσ}e_{Iν}T^I_{ρσ})`). **Fix the normalisation of "NY" in Eq. (8) / Table III while doing so** — as printed it is schematic, which is why the referee's coefficients came out wrong `[L66]`.

3. **Table III, row O1 — keep `Final = 0`, fix the reason.** Correct as printed in outcome `[L98]`, but "vanishes (Bianchi, Check A)" holds only on the torsion-free branch `[L70]`, `[L71]`. Honest wording: *"0 on the torsion-free branch (Bianchi, Check A); on the T = κS branch equals −NY, an exact total derivative → 0 EOM / 0 vacuum energy."* The abstract's trichotomy (main.tex:270–273) should likewise scope "identically vanishing by the algebraic Bianchi identity" to the torsion-free branch, or fold O1 into the total-derivative class on shell.

4. **Table III, row O4 (main.tex:1940) — this is the real error.** "Fate (bare) → `κ²(J⁵·J⁵)`" and "Final → `κ(J⁵·J⁵)`" are wrong for O4 as defined in Eq. (8): the ε-contracted torsion-square vanishes identically for pure-axial torsion `[L78]`, `[L81]`, `[L86]`. Replace with "`0` (pure-axial torsion; `T_I∧T^I` is supported only by the non-axial irreps)". The same mistake appears twice more in prose and must be corrected with it: the caption's "the two genuine dimension-4 densities O4 and O5 landing on the same operator `κ(J⁵·J⁵)`" (main.tex:1923–1926) and App. A 1's `O4^{[4]} = M_Pl²·κ²(J⁵·J⁵) = κ(J⁵·J⁵) = O5^{[4]}` chain (main.tex:1903–1913). Check D's `S_{abc}S^{abc} = −(3/8)(J⁵·J⁵)` remains correct `[L87]` but must be attributed to the ε-free square `T_{abc}T^{abc}`, not to O4. Sec. V's collapse bullet (b) (main.tex:1502–1512) inherits the same conflation and needs the same fix.

---

## Readings the computation had to choose (declared, not silent)

- **O1's `ε`.** Eq. (8) writes `ε e^I e^J R_{IJ}` with `ε` unqualified. Only the *spacetime* `ε^{μνρσ}` is admissible: an internal `ε_{IJKL}` has no free internal slots left (I, J are already contracted between the tetrads and `R_{IJ}`), and the `ε_{IJKL}` variant would be the parity-**even** Einstein–Hilbert/Palatini term, excluded from a parity-odd list. This reading is further forced by the paper's own component form Eq. (7) (main.tex:1376–1378) and by the Nieh–Yan identity it quotes, whose curvature term `e_I∧e_J∧R^{IJ}` carries no internal epsilon. **Not genuinely ambiguous.**
- **O2's normalisation.** Genuinely underdetermined by the paper. Fixed here as `O2 := ∂_μ(ε^{μνρσ}e_{Iν}T^I_{ρσ})` and cross-checked against the strict 4-form convention `[L65]`. Only the rational coefficients `α, β` depend on this; the rank, the null-space dimension, and every verdict above do not.
- **O5's contraction.** Eq. (8) writes `ε T e J^5` schematically. Taken as `ε^{μνρσ}T^I_{μν}e_{Iρ}J^5_σ`, the unique zero-derivative full contraction of those factors against one `ε`; dimensions `+1 + 0 + 3 = +4` match main.tex:1476–1477.
- **O6's curvature.** Torsionful `R` per the construction rule, with the Levi-Civita `R̊` alternative computed as well `[L104]`–`[L106]`. **Rank is 4 either way**, so no verdict rests on this choice.

## Reproduce

```
python3 research/theory_audit/operator_basis_adjudication_2026_08_07.py
```

Runtime ≈ 3.5 min, pure sympy, exact rational arithmetic throughout, no external data. Emits `operator_basis_adjudication_2026_08_07.json` with the Gram certificate, null space, subset ranks, Γ-route certification, on-shell values, per-relation verdicts, and the complete tagged log.
