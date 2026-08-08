# ECH connection equation, solved — on-shell torsion irreps and operator degeneracy

**Date:** 2026-08-08
**Adjudicator:** independent symbolic computation, `research/theory_audit/ech_torsion_onshell_2026_08_08.py`
**Machine output:** `research/theory_audit/ech_torsion_onshell_2026_08_08.json` (every `[L##]` below is a line of that run's log, reproduced verbatim in the JSON `log` array)
**Target:** `arxiv/paper1c_nogo_survey/main.tex` — Sec. II (`main.tex:612–614`), Sec. V (`main.tex:1784`, `1934`, `1950–1971`), App. A 1 (`main.tex:2384–2386`, `2406–2422`, `2503–2513`, Verdict `2544–2545`), Table III (`main.tex:2437–2440`, `2458`), App. C scope (`main.tex:2693–2695`), App. E Eq. (E1)–(E4) (`main.tex:2806–2846`), abstract (`main.tex:417–421`), Data & Code Availability (`main.tex:2156–2166`)
**Challenge adjudicated:** `project-context/peer-reviews/INT_v3/ROUND_2026-08-08-P1C-v1C.0.14-EXACTPDF-9dd5c708-R12CONV/P1C_claude_r12_leg.md`, MAJOR-1 and MAJOR-2
**Prior artifact re-examined:** `research/theory_audit/operator_basis_adjudication_2026_08_07.{py,json,md}` (erratum addendum written, see §8)

Nothing here is taken from the manuscript's scripts, from the 2026-08-07 adjudication script, or from the referee's arithmetic. The Einstein–Cartan–Holst connection equation is set up from the action in explicit components and **solved**; which torsion irreps survive is an **output**, never an input.

---

## HEADLINE VERDICT: **REFEREE-CORRECT**

| Referee claim | Verdict | Evidence |
|---|---|---|
| The minimal-ECH on-shell torsion is **not** purely axial at finite γ | **REFEREE-CORRECT** | `[L11]`–`[L17]` |
| Eq. (E2)'s 1/γ term is a genuine **trace-vector** torsion irrep sourced under **minimal** coupling | **REFEREE-CORRECT** | `[L19]`–`[L22]` |
| The non-axial piece **dominates** at the physical γ | **REFEREE-CORRECT** (ratio 2.11 at γ=0.2375; 1.82 at γ=0.274) | `[L23]`, `[L24]` |
| `O4 ≡ 0` on shell (P1C's claim) | **FALSIFIED** on the ECH branch; true only as γ→∞ | `[L25]`, `[L32]`, `[L35]`, `[L38]`, `[L41]` |
| Referee's `O4 = −192π²G²γ³/(1+γ²)²(J⁵·J⁵)` | **CONFIRMED EXACTLY** (difference 0, ratio 1) under App. E's own normalization | `[L43]` |
| `O1 = O6` survives | **CONFIRMED** (torsion-independent tetrad conversion) | `[L49]`–`[L66]` |
| `O1 = −O2` survives | **FALSIFIED** — it required `O4 = 0` | `[L50]`, `[L53]`, `[L56]`, `[L59]`, `[L62]`, `[L65]`, `[L66]` |
| The 2026-08-07 adjudication *imposed* pure axiality | **REFEREE-CORRECT** — γ never enters that computation | §8 below |
| App. C: trace-vector irreps appear "only when minimal coupling is relaxed" | **FALSIFIED for the trace-vector**; **CORRECT for the tensor irrep** | `[L11]`, `[L15]` |

**The physics conclusion of P1C survives.** Every operator the correction touches lands in the disposal class P1C already establishes — the `κ`-suppressed, Fierz-closed four-fermion sector — because the surviving content is proportional to `(J⁵·J⁵)`, the *same* structure as O5, with an O(1) ratio `O4^[4]/O5^[4] = γ/(1+γ²) = 0.225` at γ = 0.2375 `[L36]`. No new light scale appears. What must go is the printed *mechanism*, in about a dozen places (§7).

---

## 1. Conventions (stated, then self-checked)

Fixed once in the module docstring and used everywhere; each cites the manuscript.

- Mostly-plus `η = diag(−1,+1,+1,+1)` (P1C Check D, `main.tex:2503–2513`).
- `ε^{0123} = +1`, `ε_{0123} = −1` — the Lorentzian **tensor** normalization, which is what actually reproduces P1C's own printed identity `ε_{abcd}ε^{abce} = −3!δ^e_d`. Verified `[L01]`, `[L02]`. (P1C prints the word "symbol"; this is the R12 referee's MINOR-1, and it is a real wording defect.)
- `κ = 8πG = M̄_Pl^{−2}` (Sec. II).
- First-order ECH action in components,
  `S = (1/2κ)∫ e e^μ_I e^ν_J P^{IJ}{}_{KL} F_{μν}{}^{KL}`, `P^{IJ}{}_{KL} = δ^{[I}_K δ^{J]}_L − (s_H/2γ) ε^{IJ}{}_{KL}` — identity piece = Einstein–Hilbert (Palatini), ε piece = Holst at relative weight 1/γ. This is the component form of P1C's own `Q_γ = ⋆ + γ^{-1}𝟙` (Eq. (E1), `main.tex:2806–2812`). **Both Holst sign conventions** `s_H = ±1` are computed `[L46]`, `[L47]`.
- Minimal Dirac source enters **only** through the totally antisymmetric `S^{IJK} = ¼ε^{IJKL}J^5_L` (Sec. II, `main.tex:2820–2823`), coupling `L_m = λ C_{IJK}S^{IJK}` `[L06]`.
- Torsion from contorsion `T_{abc} = C_{bac} − C_{cab}`; irrep split `4 + 4 + 16 = 24` verified as an exact direct sum `[L03]`, using the **same** convention as the 2026-08-07 artifact so the two are directly comparable.

## 2. The connection equation, solved — no ansatz

**Route A (component-variational).** The C-quadratic part of the ECH action was built explicitly, the minimal Dirac source added, and the action varied with respect to **all 24 independent contorsion components** — no restriction to any irrep `[L04]`, `[L05]`. The solution is unique for every finite nonzero γ `[L07]`, confirming the non-degeneracy `Q_γ^{-1} = γ²/(1+γ²)(γ^{-1}𝟙 − ⋆)` that Eq. (E1) asserts. Torsion was reconstructed and its antisymmetry verified `[L08]`.

**Route B (differential-form).** Entirely independently, `Q_γ(e^{[I}∧T^{J]}) = J^{IJ}` was dualized to components and solved by null space of the exact coefficient matrix `[L09]`.

The two routes agree exactly `[L14]`. This is the computation the 2026-08-07 artifact never performed.

## 3. Which irreps are nonzero on shell — the answer

Writing the solution as `T_{abc} = α ε_{abcd}J^{5d} + β(η_{ab}J^5_c − η_{ac}J^5_b)`:

| irrep | on-shell coefficient | status | evidence |
|---|---|---|---|
| **axial** (4) | `α = −γ²κλ / [2(γ²+s_H²)]` | **NONZERO** | `[L12]`, `[L16]` |
| **trace-vector** (4) | `β = −γκλ s_H / [4(γ²+s_H²)]`, i.e. `V_c = T^a{}_{ac} = 3β J^5_c` | **NONZERO for every finite nonzero γ** | `[L12]`, `[L15]` |
| **tensor** (16) | `q_{abc}` | **IDENTICALLY ZERO** | `[L11]` |

γ-dependence of the ratio, which is normalization-independent and identical in both routes:

> **`β/α = s_H/(2γ)`**  `[L10]`, `[L13]`

and

> `γ → ∞` ⟹ `β/α → 0` — **pure axiality is the Einstein–Cartan limit, not the ECH on-shell solution** `[L17]`.

At the LQG values the non-axial piece is the **larger** of the two:

- γ = 0.2375: `β/α = 40/19 = 2.1053` `[L23]`
- γ = 0.274: `β/α = 250/137 = 1.8248` `[L24]`

So App. A 1's "no non-minimal (trace/tensor) torsion irreps are admitted" (`main.tex:2385`) is **half right**: the *tensor* irrep is indeed absent `[L11]`, but the *trace-vector* irrep is generated by the Holst term under strictly minimal coupling.

## 4. Reconciling with the manuscript's Eq. (E2)

Eq. (E2), quoted verbatim from `arxiv/paper1c_nogo_survey/main.tex:2826–2831` (label `eq:fmt_contorsion_p1c`) `[L18]`:

```latex
e_I{}^\mu C_{\mu JK}=4\pi G\,\frac{\gamma^2}{1+\gamma^2}
\left(\frac12\epsilon_{IJKL}J_5^L-\frac1\gamma\,\eta_{I[J}J^5_{K]}\right)
```

Converted to torsion with `T_{abc} = C_{bac} − C_{cab}` `[L19]`:

> `α_E2 = −4πGγ²/(1+γ²)`, `β_E2 = −2πGγ/(1+γ²)`, **`β/α = 1/(2γ)`**

which is **exactly** the independently solved ratio at `s_H = +1` `[L20]`. The trace vector is

> `T^a{}_{ac} = −6πG·γ/(1+γ²)·J^5_c` `[L21]`

— the referee's value, confirmed.

**Answering the three-way question the challenge poses.** The 1/γ term is:

- **not** an axial piece in a different basis — its totally antisymmetric part is identically zero and it carries the entire torsion trace, so it lies wholly inside the trace-vector irrep, orthogonal to the axial one `[L22]`;
- **not** a convention or normalization artifact — the independent solve of the connection equation reproduces it, with the same γ-dependence, under both Holst sign conventions `[L10]`, `[L13]`, `[L46]`, `[L47]`;
- **a genuine trace-vector torsion irrep**, present under minimal coupling, sourced (as a pseudo-vector) by the axial current `J^5` through the Holst term. Its being *sourced by* `J^5` is exactly why it is easy to misread as "axial"; irrep membership is fixed by index structure, not by the parity of the source.

## 5. Two readings — the manuscript's normalization is genuinely ambiguous

P1C fixes the same object twice, inconsistently, and the two anchors differ by a factor 2 in torsion amplitude (factor 4 in any quadratic-in-`T` density). **Both are carried; no verdict depends on the choice.**

- **READING-I — contact-operator anchor (App. E / Freidel–Minic–Takeuchi):** require the eliminated-torsion operator to equal `L_4ψ = −(3κ/16)[γ²/(1+γ²)](J⁵·J⁵)` (Eq. (E4), `eq:4fermi_p1c`). Back-substitution of the solved contorsion gives `L_int = −3γ²κλ²/[16(γ²+s_H²)](J⁵·J⁵)` `[L27]`, fixing `λ = ±1` `[L28]`.
- **READING-II — Sec. II literal anchor:** require `T^{abc} → κS^{abc} = (κ/4)ε^{abcd}J^5_d` as γ→∞ (`main.tex:612–614`, `2820–2823`). Fixes `λ = −1/2` `[L29]`.

> `λ_I/λ_II = 2` `[L30]`

This is a **real internal inconsistency in P1C**, independent of the referee's finding: App. E's Eq. (E2)/(E4) normalization is twice Sec. II's `T = κS` normalization. It is diagnosable from the manuscript alone: under READING-II, O5's printed fate `−(3/2)κ(J⁵·J⁵)` (Table III, `main.tex:2458`) comes out exactly in the γ→∞ limit `[L39]`, whereas READING-I gives `−3κ` there `[L33]`. So **Sec. V / Table III / App. A 1 use READING-II while App. E uses READING-I**, and the referee — reading Eq. (E2) directly — used READING-I.

## 6. O1, O2, O4, O5, O6 recomputed on the FULL on-shell torsion

Closed forms on a general `(axial + trace-vector)` torsion, computed symbolically:

> **`O4(bare) = ε^{μνρσ}T^I{}_{μν}T_{Iρσ} = −24 α β (J⁵·J⁵)`** `[L25]`
> **`O5(bare) = ε^{μνρσ}T^I{}_{μν}e_{Iρ}J^5_σ = −6 α (J⁵·J⁵)`** `[L26]`

`[L25]` vindicates P1C's *stated reason* precisely: O4 vanishes on a pure axial torsion (β = 0) **and** on a pure trace-vector torsion (α = 0), and is nonzero only on the axial × trace-vector cross term. P1C names the surviving channel correctly (`main.tex:2409–2411`, `2509–2511`) and then asserts, wrongly for ECH, that the on-shell torsion has nothing to put in it. `[L26]` also confirms the referee's point 5: the trace-vector piece drops out of O5 entirely, so O5's *disposal class* is untouched — only its coefficient moves.

Substituting the solved α, β (`s_H = +1`):

| quantity | READING-I | READING-II | evidence |
|---|---|---|---|
| `O4(bare)` | `−3κ²γ³/(1+γ²)² (J⁵·J⁵)` = **`−192π²G²γ³/(1+γ²)² (J⁵·J⁵)`** | `−(3/4)κ²γ³/(1+γ²)²` = `−48π²G²γ³/(1+γ²)²` | `[L32]`, `[L38]` |
| `O5(bare)` | `−3κγ²/(1+γ²) (J⁵·J⁵)` | `−(3/2)κγ²/(1+γ²) (J⁵·J⁵)` | `[L33]`, `[L39]` |
| promoted `O4^[4] = M̄_Pl²·bare` | `−3κγ³/(1+γ²)² (J⁵·J⁵)` | `−(3/4)κγ³/(1+γ²)² (J⁵·J⁵)` | `[L34]`, `[L40]` |
| promoted `O5^[4]` | `−3κγ²/(1+γ²) (J⁵·J⁵)` | `−(3/2)κγ²/(1+γ²) (J⁵·J⁵)` | `[L34]`, `[L40]` |
| `O4^[4] ≡ 0`? | **NO** | **NO** | `[L35]`, `[L41]` |
| `O4^[4]/O5^[4]` | `γ/(1+γ²)` = 0.2248 at γ=0.2375 | `γ/[2(1+γ²)]` = 0.1124 | `[L36]`, `[L42]` |

**Against the referee's claimed value.** The referee computes `O4 = −192π²G²γ³/(1+γ²)²(J⁵·J⁵)`. Computed here:

> READING-I: **difference = 0, ratio = 1 — CONFIRMED EXACTLY, sign included** `[L43]`
> READING-II: ratio = 1/4 `[L44]`

i.e. the referee's γ-dependence `γ³/(1+γ²)²` is exactly right, and their prefactor is exactly right *in the normalization Eq. (E2) itself uses* — the one they read it from `[L45]`. Under the normalization P1C's own Table III uses, it is one quarter of that. **Nonzero under both.** The Holst-sign convention flips the overall sign and nothing else `[L46]`, `[L47]`.

**O1, O2, O6 on an explicit curved on-shell ECH configuration.** Six configurations were built (γ ∈ {19/80, 1, 3} × two independent exact-rational axial-current seeds) with a trivial tetrad — so `ω̊ = 0` and the curvature is entirely torsion-generated: the finite-γ analogue of the Einstein–Cartan configuration the 2026-08-07 artifact used. O6 was computed by an **independent affine-connection (Γ) route**, not by tetrad conversion. Results `[L48]`–`[L66]`:

- **`O1 − O6 = 0` exactly, every configuration** — `O1 = O6` survives, as expected: it is a torsion-independent tetrad conversion.
- **`2·O1 + 2·O2 − O4 = 0` exactly, every configuration** — the Nieh–Yan relation of Eq. (11) re-verified independently, on shell, at finite γ.
- **`O1 + O2 = ½O4 ≠ 0`, every configuration** — so **`O1 = −O2` FAILS** on the ECH branch. E.g. at γ = 19/80, seed 0: `O1 = −22875126/45711121`, `O2 = 2166/6761`, `O4 = −16461600/45711121`, `O1+O2 = −8230800/45711121 = ½O4` `[L48]`–`[L50]`.

So on shell `O1^[4] = O6^[4] = −O2^[4] + ½O4^[4]`: minus the Nieh–Yan total derivative **plus** a genuine local four-fermion contact term `½O4^[4] = −(3/2)κγ³/(1+γ²)²(J⁵·J⁵)` (READING-I). O1 and O6 are **not** exact total derivatives on the ECH branch.

**Why the no-go still holds.** `O4^[4]`, and therefore the surviving parts of `O1^[4]` and `O6^[4]`, are proportional to `(J⁵·J⁵)` — literally the same operator as `O5^[4]`, with an O(1) coefficient ratio `[L36]`. They are covered unchanged by App. C's Fierz-closure lemma and by the single-scale NDA ceiling, at the same `M̄_Pl^{-2}` power. Disposal class (i) loses three members to disposal class (ii); class (iii) loses its torsionful member. Nothing acquires a new light scale.

## 7. What P1C must change (exact sites)

**Correctness — must be fixed:**

1. `main.tex:612–614` (Sec. II) — "varying the first-order action … gives an algebraic constraint … `T^{abc} = κS^{abc}`" is stated unqualified. It is the γ→∞ Einstein–Cartan limit. Scope it, or replace with the ECH solution `T_{abc} = α ε_{abcd}J^{5d} + β(η_{ab}J^5_c − η_{ac}J^5_b)`, `β/α = 1/(2γ)`.
2. `main.tex:1784` (Sec. V construction rule) — "the algebraically-fixed torsion `T = κS`". Same scope fix; this is what propagates into the whole operator list.
3. `main.tex:1950–1956` (Sec. V bullet (a)) — "`O4^[4] = 0` (below) gives `O1^[4] = O6^[4] = −O2^[4]` exactly, so they are minus the Nieh–Yan total derivative and contribute zero to the equations of motion and zero to the vacuum energy" — **false on the ECH branch** `[L50]`. Correct statement: `O1^[4] = O6^[4] = −O2^[4] + ½O4^[4]`, total derivative **plus** a Fierz-closed contact term.
4. `main.tex:1957–1962` (Sec. V bullet (b)) — O5's reduction `−(3/2)κ(J⁵·J⁵)` is the γ→∞ value; the ECH value is `−(3/2)κγ²/(1+γ²)(J⁵·J⁵)` (READING-II) `[L39]`.
5. Sec. V trichotomy `main.tex:~1934`, clause (iii) "O4 on the `T = κS` branch, because the ε-contracted torsion-square is supported only by the non-axial torsion irreps" — the *reason* is exactly right `[L25]`, the *conclusion* inverts, because the ECH torsion **has** a non-axial irrep.
6. `main.tex:2384–2386` (App. A 1) — "no non-minimal (trace/tensor) torsion irreps are admitted". True for the **tensor** irrep `[L11]`; false for the **trace-vector** irrep, which minimal coupling generates at every finite γ `[L15]`.
7. `main.tex:2406–2422` (App. A 1) — "The minimal Cartan torsion … is *purely axial* — its vector and tensor parts vanish identically — so `O4^[4] ≡ 0` on shell … This *strengthens* the closure". The "strictly stronger disposal" claim must be withdrawn; O4 joins O5 in disposal class (ii).
8. `main.tex:2414–2418` — the artifact citation says the released script evaluated "an explicitly curved on-shell **Einstein–Cartan** configuration"; that phrase is accurate, but the sentence it supports is an **ECH** claim. Either relabel the claim or cite this module.
9. Table III `main.tex:2458` (row O4) and caption `main.tex:2437–2440` — "Fate (bare) `0` (pure-axial T; needs non-axial irreps)" / "Final `0`" must become the computed value. Row O1/O6's "Final `0` (EOM)" must become `½O4^[4] ≠ 0`.
10. `main.tex:2503–2513` (Check D) — the ε-contracted-square support statement is correct `[L25]`; the "so under the purely axial Cartan torsion `O4^[4] ≡ 0`" conclusion is not, on the ECH branch.
11. App. A 1 Verdict `main.tex:2544–2545` — classes (i) and (iii) lose their torsionful members to class (ii).
12. Abstract `main.tex:417–421` — "identically vanishing (… the ε-contracted torsion-square under the purely axial Cartan torsion)". Must be scoped to Einstein–Cartan or removed.
13. Data & Code Availability `main.tex:2156–2166` — "establishing in particular that the ε-contracted torsion-square O4 vanishes identically under the purely axial Cartan torsion" promotes an Einstein–Cartan verification to an ECH one. State the branch.
14. App. C scope `main.tex:2693–2695` — "non-minimal torsion irreps (trace-vector and tensor irreps) that appear only when the minimal coupling assumption is relaxed". False for the trace-vector `[L15]`; true for the tensor `[L11]`. Split the two.
15. Sec. IV A, Route 2 dark-energy leg, case (i) — the operator-level step inherits items 3 and 7.

**Convention — should be fixed at the same time:**

16. The Sec. II (`T = κS`) versus App. E (Eq. (E2)/(E4)) normalizations differ by a factor 2 `[L30]`. Pick one and state it; the operator table currently uses one and App. E the other.
17. MINOR-1 stands: `main.tex:~578` and Eq. (9) say "Levi-Civita **symbol**" while quoting the Lorentzian **tensor** contraction `ε_{abcd}ε^{abce} = −3!δ^e_d` `[L01]`, `[L02]`.

**What does NOT change:** the Fierz-closure lemma (App. C), the single-scale NDA ceiling, `O1 = O6`, the Nieh–Yan relation `2O1 + 2O2 − O4 = 0`, and the final "no (meV)⁴ vacuum energy without a new light scale" conclusion.

## 8. Does the 2026-08-07 artifact need an erratum? — YES, written

`research/theory_audit/operator_basis_adjudication_2026_08_07.md` §1 states its own premise: "The paper's on-shell Cartan torsion `T^{abc} = κS^{abc} = (κ/4)ε^{abcd}J^5_d` is verified to be **pure axial** … **This fact turns out to decide MAJOR-2**." That is an **imposed input**, not a solved output — γ never enters that module at any point, so its "curved on-shell configuration" is Einstein–Cartan, not Einstein–Cartan–Holst. Its §5, §6, §7 on-shell branch (`O4 ≡ 0`, hence `O1 = −O2`, hence "every member is a total derivative or identically zero") is therefore correct **only on the γ→∞ branch it actually evaluated**.

A clearly-marked **2026-08-08 erratum addendum** has been appended to that file. Its original conclusions are left intact and unedited; the addendum scopes them. Its off-shell results (rank 4, nullity 2, the two null vectors, the Γ-route certification of `O1 = O6`, the `d(e∧T)` normalization cross-check) are **unaffected and re-confirmed here** at finite γ `[L49]`–`[L66]`.

---

## Reproduce

```
python3 research/theory_audit/ech_torsion_onshell_2026_08_08.py
```

Runtime ≈ 4 min, pure sympy, exact rational/symbolic arithmetic throughout, no external data. Emits `ech_torsion_onshell_2026_08_08.json` with both solve routes, the irrep decomposition, both normalization readings, the closed forms, the referee comparison, the six curved on-shell configurations, and the complete tagged log.
