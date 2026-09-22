# The P1N Fierz row: deriving the scalar-channel sign that drives `G_s`

**Lane** `bb-LS15-fierz-sign` · 2026-09-22
**Target (read-only)** `arxiv/paper1bc_ech_note/main.tex` @ `v1N.0.7`,
pinned at commit `27dd3143`: Eq. `eq:fierz_row` (l. 273–288), Eq. `eq:Gs`
(l. 289–296), Eq. `eq:gap` (l. 296–324).
**Method pre-registered** in `PRE_REGISTRATION.md`, commit `a44bc46d`, before
any symbolic or numerical result existed.
**Headline** the sign as printed is **CORRECT**. `G_s` is unchanged. Branch A
of the pre-registration.

---

## 0. The conventions, stated — and checked against what the paper uses

`main.tex:167-168` declares mostly-plus `η_IJ = diag(-,+,+,+)`, `ε_0123 = +1`,
`κ = 8πG = 8π/M_Pl²`. `main.tex:216-221` declares the configuration: a
spin-aligned Dirac ensemble whose axial current `J⁵` is normalized **spacelike**
in that mostly-plus convention. The bilinears are the manuscript's own:
`(ψ̄γ^μψ)²` means `(ψ̄γ^μψ)(ψ̄γ_μψ)`, `(J_5^I J_{5I}) = η_IJ (ψ̄γ^Iγ⁵ψ)(ψ̄γ^Jγ⁵ψ)`.

**Does the paper use what it declares?** For this equation the question has a
sharp answer, and it is better than "yes": §2.2 below proves that every
contracted channel — `(J_5^I J_{5I})` included — is *literally the same
four-index tensor* in mostly-plus and mostly-minus, because
`γ^μ_{(-+++)} = i γ^μ_{(+---)}` supplies `i² = -1` exactly where `η` flips sign.
So `eq:fierz_row` cannot be sensitive to a signature slip, and the manuscript's
"signature-independent" qualifier is a theorem here rather than a hopeful
adjective. The same argument makes the row insensitive to the sign convention
for `γ⁵` (which enters squared) and to the Dirac-matrix representation
(coefficients are traces).

This is the one convention question that mattered, and it is closed. The
`ε_0123 = +1` declaration is the *symbol* rather than the Lorentzian tensor
normalization (`ε_0123 = -1`, the convention that reproduces the on-shell
torsion identities — see `research/theory_audit/ech_torsion_onshell_2026_08_08.md`
§1), but `ε` does not enter `eq:fierz_row`, `eq:Gs`, or `eq:gap` at all, and the
contact-term prefactor it *does* enter is quadratic in the source normalization
(`λ²`, §4.2), so no sign rides on it here.

---

## 1. What is being tested

`main.tex:276-281`:

```
(J_5^I J_{5I})  ->  (ψ̄ψ)² + ½(ψ̄γ^μψ)² + ½(ψ̄γ^μγ⁵ψ)² - (ψ̄γ⁵ψ)²
```

`main.tex:282-288` asserts the scalar coefficient is "exactly `+1`, unique, and
signature-independent, with the single Grassmann exchange that maps the ordering
`(12)(34) → (14)(32)` supplying the overall minus sign relative to the c-number
Nieves–Pal identity". `main.tex:289-293` inserts that scalar row into the
declared interaction `+G_s(ψ̄ψ)²`, giving `G_s = -(3κ/16)γ²/(1+γ²) < 0`, which is
the *sole* input to the three-line no-condensate argument at `main.tex:310-322`.

A sign error here flips `G_s` to attractive, and the "admits no condensate"
result — an abstract-level claim — would have to be withdrawn.

---

## 2. Derivation

### 2.1 The machinery (no remembered coefficient table)

`scripts/fierz_row_sign.py` builds `γ^μ` explicitly as 4×4 complex matrices in
**three** representations (Dirac, Weyl, and a real Majorana basis) and **both**
signatures, gating each on the Clifford algebra `{γ^μ,γ^ν} = 2η^{μν}`,
`(γ⁵)² = 1`, and `{γ⁵,γ^μ} = 0` at machine precision. It then forms the five
contracted channel tensors

```
L^(X)_{abcd} = Σ_idx (Γ^X)_{ab} (Γ_X)_{cd},     X ∈ {S, V, T, A, P},
```

with `T` the `Σ_{μ<ν} σ^{μν} ⊗ σ_{μν}` half-sum, applies the Fierz index
exchange `b ↔ d`, and **solves** the resulting 256-component linear system for
the decomposition coefficients. `scripts/fierz_exact_and_anchors.py` repeats the
solve in exact rational arithmetic over `Q(i)` with `sympy.linsolve`, so nothing
rests on floating point.

### 2.2 The Grassmann sign, derived as its own step

`ψ̄_a ψ_b ψ̄_c ψ_d → ψ̄_a ψ_d ψ̄_c ψ_b` is the transposition of two Grassmann-odd
factors of a four-letter word. Counting adjacent transpositions mechanically
(`grassmann_sign_bruteforce`, no algebra package's conventions involved) gives

```
ψ̄_a ψ_b ψ̄_c ψ_d = − ψ̄_a ψ_d ψ̄_c ψ_b .
```

This is exactly the "single Grassmann exchange" the manuscript invokes, and it
is the entire difference between the c-number and operator rows.

### 2.3 The computed c-number Fierz matrix

Solved, not recalled; identical across all **twelve** convention combinations
(3 representations × 2 signatures × 2 `γ⁵` signs) to `6.7 × 10⁻¹⁶`, with
decomposition residual `1.1 × 10⁻¹⁵` and the five channel tensors independent
(rank 5 at the tensor level):

```
4 F  =   S    V    T    A    P
  S [  1    1    1   -1    1 ]
  V [  4   -2    0   -2   -4 ]
  T [  6    0   -2    0    6 ]
  A [ -4   -2    0   -2    4 ]
  P [  1   -1    1    1    1 ]
```

### 2.4 The answer

The axial row of `F` is `(-1, -½, 0, -½, +1)`; applying the Grassmann sign of
§2.2 flips every entry:

```
c-number   (J_5·J_5) → -SS - ½VV + 0·TT - ½AA + PP
Grassmann  (J_5·J_5) → +SS + ½VV + 0·TT + ½AA - PP
```

Exact-rational solve, both signatures (`outputs/fierz_exact_and_anchors.json`,
block `E1`): `S = 1`, `V = 1/2`, `T = 0`, `A = 1/2`, `P = -1`.

**This is the manuscript's printed row, entry for entry, including the tensor
channel's absence and the scalar coefficient `+1`.**

---

## 3. Validation — the pre-declared set, and what each one did

| Pre-registered gate | Result |
|---|---|
| Clifford algebra + `(γ⁵)² = 1` in every rep/signature | **PASS**, machine precision |
| Full 5×5 matrix reproduced by solving, not recalling | **PASS** (§2.3) |
| `F² = 1` — the Fierz transform is an involution | **PASS**, max deviation `6.7×10⁻¹⁶` |
| `V−A` self-conjugacy (textbook) | **PASS**: c-number coefficient `-1`, residual `0`, so the Grassmann operator maps to itself with `+1`, in both a mostly-minus Dirac basis and a mostly-plus Weyl basis |
| Grassmann sign derived mechanically | **PASS**, `-1` |
| Row holds as an operator identity for one Dirac field | **PASS**, residual `4.4×10⁻¹⁶` |
| Poplawski arXiv:1005.0893 Eq.(9)–(10) chain | **PASS** — see §4.1; this is the external published number |
| Kerlick (1975) / O'Connell (1977) | **NOT APPLICABLE AS PRE-REGISTERED** — see §4.3. Reported rather than quietly dropped. |
| Two signatures / representations must agree | **PASS**, and §2.2/`E2` shows *why* they must |

`F² = 1` is the check that a sign error cannot survive: it constrains all 25
entries simultaneously and a flipped row generically breaks it.

### 3.1 Agreement with the manuscript's own cited artifact

`main.tex:1125-1129` cites `research/theory_audit/fierz_adjudication_2026_08_05.py`
as certifying this coefficient. That file was opened **after** this lane's own
results were produced. It reaches the identical row `(1, ½, 0, ½, -1)`, the
identical `F_op = -F_c` rule, and `G_s = -3κ/16`; it also independently records
the single-species rank-3 caveat of §5. So the artifact link is not decorative —
it does what the paper says it does, and an independent re-derivation agrees
with it. (It also records that the *frozen monolith's* competing row and
`G_s = -3κ/64` are wrong; that is not P1N's text and is out of scope here.)

---

## 4. Cross-checks against published results

### 4.1 Poplawski arXiv:1005.0893 — an external number that the sign must hit

Poplawski's dark-energy chain is an independent, published evaluation of the
very same axial–axial composite:

* his Eq. (9), SVZ vacuum saturation:
  `⟨0|(ψ̄γ^jγ⁵t^aψ)(ψ̄γ_jγ⁵t^aψ)|0⟩ = +(16/9)⟨0|ψ̄ψ|0⟩²` — **positive**;
* his Eq. (10): `⟨0|ρ_Λ|0⟩ = (κ/3)⟨0|ψ̄ψ|0⟩²`;
* his Eq. (11): `≈ (54 meV)⁴`, **positive**, which is the entire point of his
  paper.

Vacuum-saturating this lane's row gives `⟨O_S⟩ → ⟨ψ̄ψ⟩²`, `⟨O_P⟩ → 0` by parity,
`⟨O_V⟩ = ⟨O_A⟩ → 0` in naive factorization, so `⟨J_5·J_5⟩ → c_S ⟨ψ̄ψ⟩²`. His
Eq. (9) is therefore his own measurement of `c_S`, and it reads `+`. Feeding
`c_S = +1` through his coefficient reproduces his published number:

```
(3κ/16) · (16/9) · (+1) · ⟨q̄q⟩²  =  (κ/3)⟨q̄q⟩²  =  +8.320×10⁻⁶ eV⁴  =  (53.71 meV)⁴
```

— and `(3/16)·(16/9) = 1/3` **exactly**, so the manuscript's `3/16` and
Poplawski's `1/3` are the same number once his colour factor is restored.
The counterfactual `c_S = -1` gives `ρ_Λ = -(53.71 meV)⁴`, a **negative**
cosmological constant, contradicting his published positive result.
(`outputs/fierz_exact_and_anchors.json`, block `E5`.)

So the scalar sign is confirmed against a number obtained by someone else, by a
different method, for a different purpose.

### 4.2 The prefactor — the remaining sign in the chain, and where it stands

`G_s`'s sign is the product of *two* signs: the Fierz coefficient (this lane)
and the prefactor of `eq:4fermi` (not this lane). The blind adjudicator raised
exactly this, unprompted. Its status:

* It is derived by a committed independent computation:
  `research/theory_audit/ech_torsion_onshell_2026_08_08.py` back-substitutes the
  solved contorsion into the ECH action and obtains
  `L_int = -3γ²κλ²/[16(γ²+s_H²)] (J⁵·J⁵)` (`[L27]`, report §READING-I), which is
  `-(3κ/16)γ²/(1+γ²)(J⁵·J⁵)` and is **quadratic in the source normalization `λ`
  and in the Holst sign `s_H`** — so the prefactor's sign is insensitive to both.
* It is separately consistent with Poplawski: combining `eq:4fermi` with lane
  `bb-LS13-p1n-essentials`'s derived `ρ_{4ψ} = -L_{4ψ}` and this lane's row gives
  `ρ = +(3κ/16)⟨J_5·J_5⟩ > 0`, matching the sign of Poplawski's Eq. (4) stress
  tensor and, with his colour factor, his Eq. (10) exactly. His mostly-minus
  `+(3κ/16)` and this paper's mostly-plus `-(3κ/16)` are the same physics.

This lane did not re-derive the prefactor from the action and does not claim to
have. It reports the prefactor as **verified elsewhere by a committed artifact
and independently consistent with a published result** — not as unchecked, and
not as this lane's own derivation.

### 4.3 Kerlick / O'Connell — a pre-registered check that does not apply

The pre-registration named the Kerlick (PRD **12**, 3004, 1975) / O'Connell
(PRD **16**, 1247, 1977) Dirac-field ECSK result as a validation target. On
working the problem it is clear that result determines the *sign of the
gravitational contribution* of the contact term for a given medium expectation
value — it is a stress-tensor statement, already adjudicated under DP1N-60 — and
carries no information about a **Fierz coefficient**, which is a purely
algebraic rearrangement identity. This gate is therefore reported as
**not applicable as pre-registered**, replaced in substance by §4.1, and is
recorded here rather than dropped.

---

## 5. What the two legs both found beyond the sign: "unique"

Both this lane and the blind adjudicator, independently, found that the five
species-singlet quartics are **not linearly independent as operators for one
Dirac field**. Exact rational null space (`E3`), rank 3, two relations:

```
O_S + ¼O_V + ⅙O_T − ¼O_A = 0          O_S + ⅓O_T + O_P = 0
```

equivalently `O_S + ½O_V − ½O_A − O_P = 0`, whose consequence
`O_A = 2O_S + O_V − 2O_P` is verified directly (`E4`) and is the fixed point of
applying the derived row to its own `A` term. So for a strictly one-species
field the row can be slid along a one-parameter family,

```
(J_5·J_5) = 2λ·O_S + λ·O_V + (1−λ)·O_A − 2λ·O_P   for every λ,
```

and the scalar coefficient is `2λ` — anything at all, including zero and
negative. The blind adjudicator derived the same family and verified it at
`λ = 0, ½, 1, 2, −3`.

**This does NOT touch the sign result, for two reasons, and the second is
decisive:**

1. The `+1` is the canonical single-exchange projection into the declared
   direct channel — the standard NJL mean-field construction — and the
   manuscript does declare that truncation explicitly (`main.tex:288-290`,
   `l.322-324`, `l.1088`). This is the textbook mean-field Fierz ambiguity, and
   the paper already hedges against it in the right places.
2. **The degeneracy is an artifact of having only four Grassmann components.**
   `scripts/multispecies_rank.py` rebuilds the operator projection for
   `ψ_{a,i}` with `N` species and finds rank **3** at `N=1` but rank **5** at
   `N=2` and `N=3` — the five channels are independent, and the decomposition
   (hence `G_s`) is unambiguous, as soon as the field carries any multiplicity.
   The manuscript's own gap equation `eq:gap` assumes a colour/flavour
   degeneracy factor `N_cN_f/(4π²)`, i.e. `N_cN_f > 1`. In the setting the
   paper's own argument runs in, "unique" is correct.

So the honest finding is a **wording defect, not a sign defect**: `main.tex:283`
says "unique" without the qualifier, while the manuscript's own cited artifact
(`fierz_adjudication_2026_08_05.md`, "Caveat") already states the rank-3
single-species caveat correctly. A one-clause repair is given in
`PROPAGATION_NOTE.md` §3. Nothing is withdrawn.

---

## 6. Answers to the three questions

**(a) Is the sign as printed correct?** **YES.** The scalar-channel coefficient
of `eq:fierz_row` is `+1`, derived from scratch in exact rational arithmetic,
identical across three Dirac representations, both signatures, and both `γ⁵`
conventions, with `F² = 1` satisfied and the row confirmed against Poplawski's
published Eq. (9). The whole row `(1, ½, 0, ½, -1)` is correct, tensor-channel
absence included.

**(b) What does `G_s` become?** **Unchanged:**
`G_s = -(3κ/16)·γ²/(1+γ²) < 0` at every finite `γ`, `→ -3κ/16` as `γ→∞`.
`eq:gap` step (2) stands: `2G_s I(M,Λ) < 0` while the left-hand side is `+1`,
with `I > 0` manifest, so the only solution is `M = 0`.

**(c) Which claims are affected?** **None.** Every `G_s`-dependent claim in the
paper is verified as printed; the enumeration by line number is in
`PROPAGATION_NOTE.md` §1.

---

## 7. The result reported against the lane's own expectations

This lane was opened because a sign error had just been confirmed in the
adjacent equation and an unchecked sign next to it should not be assumed
correct. It was not assumed, and it turned out to be right. That is worth
stating plainly rather than burying: **after DP1N-60, P1N's remaining §II sign
structure is now verified rather than presumed** — the Fierz row, the
`γ`-dependence, the `γ→∞` limit, the `G_s` sign, and the gap-equation step that
rides on it. The two withdrawals P1N is taking are its *only* sign-level
casualties in §II.

Equally plainly: this lane confirms `G_s`'s sign but adds **nothing** to the
separate question, settled against the paper under DP1N-61, of whether the
`G_s` argument rebuts Poplawski. It does not — his condensate is generated by
QCD, not by the torsion coupling — and §4.1 above sharpens that: the paper's
own interaction, evaluated at his scale with his colour factor, *reproduces* his
positive `ρ_Λ` rather than excluding it. The `G_s` leg is internally sound and
externally irrelevant to his mechanism, exactly as DP1N-61 concluded.
