# P1C v1C.0.15 — Claude INT referee leg (R13 convergence board)

**Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf`
**SHA-256 (verified before reading):** `f3e29c45df35f7ac358d8f4e6a854d1b9f79fa20c71a725922732db82bd967d4` — MATCH
**PDF metadata:** v1C.0.15 (August 7, 2026), 25 pages, 562,347 bytes, pdfTeX-1.40.29
**Round:** ROUND_2026-08-08-P1C-v1C.0.15-EXACTPDF-f3e29c45-R13CONV
**Role:** independent, skeptical journal referee (CQG calibre), correctness-convergence board, Claude leg
**Prior exposure to this manuscript or to any prior review of it:** none — reviewed fresh
**Read:** full 25-page PDF (text layer + 300 DPI re-renders of pp. 1, 3, 4, 5, 7, 8, 15, 21, 22, 23, 24)
**Read-only consistency sources:** `arxiv/main.tex` (companion P1A), `arxiv/paper1c_nogo_survey/main.tex`,
`research/theory_audit/operator_basis_adjudication_2026_08_07.{md,py}` (incl. the 2026-08-08 erratum addendum),
`research/theory_audit/ech_torsion_onshell_2026_08_08.md`, `research/theory_audit/fierz_adjudication_2026_08_05.md`,
`arxiv/scripts/dim4_parityodd_enumeration.py`, `arxiv/scripts/fierz_lemma_check.py`, `main.log`

---

## VERDICT: **MAJOR REVISIONS** — 4 MAJOR, 8 MINOR. No physics conclusion changes; every fix is a local text/table edit.

The paper is a careful, unusually self-scoped piece of work. The v1C.0.15 incorporation of the
2026-08-08 on-shell-torsion erratum is largely complete and, where it landed, correct: I independently
re-derived `O4(bare) = -24αβ(J⁵·J⁵)` from Eq. (E2) by explicit ε-algebra, independently integrated
Eq. (5) to `|Δγ/γ| = 1.38×10⁻⁶` against the printed `1.4×10⁻⁶`, and verified `F_c² = 1` in exact
rational arithmetic. Four sites, however, still carry the pre-erratum physics or a parity
mis-classification, and one DOI-frozen artifact the paper points a referee to prints conclusions the
manuscript now contradicts.

---

## Independently verified as CORRECT (recorded so the board does not re-litigate)

| Object | Check performed | Result |
|---|---|---|
| Eq. (1) α, β vs Eq. (E2) | derived `T_abc = C_bac − C_cab` from the printed Eq. (E2) by hand | `α = 4πGγ²/(1+γ²) = κγ²/[2(1+γ²)]`, `β = 2πGγ/(1+γ²) = κγ/[4(1+γ²)]`, `β/α = 1/(2γ)` — **exact match** |
| Eq. (13) `O4^[4]` | independent ε-contraction of `ε^{abcd}T_{eab}T^e{}_{cd}` on `axial + trace-vector` torsion | `−24αβ(J⁵·J⁵)`; αα term = 0, ββ term = 0; substituting α,β gives `−3κ²γ³/(1+γ²)²` bare = `−192π²G²γ³/(1+γ²)²`, promoted `−3κγ³/(1+γ²)²` — **exact match, incl. the bare/promoted κ bookkeeping via `M̄_Pl²κ² = κ`** |
| `O4^[4]/O5^[4] = γ/(1+γ²) ≃ 0.22` | 0.2375/1.05640625 = 0.22482 | ✓ |
| Eq. (12) internal consistency | `2O1 + 2O2 − O4 = 0 ⇔ O1 = ½O4 − O2`; and with Eq. (11) `NY = ½B − A`, the relation reproduces the printed `[d(e_I∧T^I)]_dens = ¼B − ½A` "twice that" remark | ✓ self-consistent, and consistent with `operator_basis_adjudication` `[L30]`–`[L33]`, `[L65]` |
| Eq. (5) → `|Δγ/γ| ≈ 1.4×10⁻⁶` | frozen-coefficient integration at γ=0.24: `Δγ² = 0.2372(µ_UV/M_Pl)² = 1.591×10⁻⁷`, `Δγ/γ = Δγ²/2γ² = 1.381×10⁻⁶` | ✓ **1.4×10⁻⁶ confirmed** |
| Eq. (C1) `F_c² = 𝟙` | exact rational 5×5 matrix square from the 300 DPI render | ✓ identity, exactly |
| Eq. (C2) axial row | row 4 = ¼(−4,−2,0,−2,4) → `F_op = −F_c` → (1,½,0,½,−1) → `SS + ½VV + ½AA − PP` | ✓; tensor coefficient 0 as claimed |
| Check D | `S_abc S^abc = (1/16)(−3!)(J⁵·J⁵) = −(3/8)(J⁵·J⁵)`; `T_abcT^abc|_axial = −6α²(J⁵·J⁵)` | ✓ both |
| `ρ_crit = √3/(32π²γ³)ρ_Pl` | re-derived from `ρ_crit = 3/(8πGλ²γ²)`, `λ² = 4√3πγℓ_P²` | ✓ formula correct; 0.4094 at γ=0.2375, 0.2666 at γ=0.274 → printed "0.27–0.41" and `(·)² ≃ 0.07–0.17` ✓ |
| `|Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)]` | from the printed Ω₄₄, α₄ | ✓ algebra; 3.334 at γ=0.24 ("≈3.3" ✓); monotone, infimum 378/120 = 3.15 ("≈3.2" ✓); 4.84 at γ=1 ("O(3)–O(5)" ✓) |
| Eq. (3) numerics | `10⁻³·10⁻⁶¹/(10⁻²·5.97×10⁻³) = 1.67×10⁻⁶⁰`; direct contraction `1.67×10⁻⁶²`; loop-factor bookkeeping `log₁₀(1/16π²) = −2.20` vs `log₁₀3.3 = +0.52` → net −1.68 ("roughly 1.7 orders") | ✓ all |
| Eq. (6) numerics | `0.3 × 1.18×10⁻⁶¹ = 3.5×10⁻⁶²`; `1.4×10⁻⁶ × 1.18×10⁻⁶¹ = 1.65×10⁻⁶⁷` | ✓ "∼3×10⁻⁶²" / "∼1.7×10⁻⁶⁷" |
| App. A hierarchy | `M_Pl⁴/ρ_Λ = 8.67×10¹²²`; `N_tot = 122 ln10/3 = 93.6` | ✓ "8.7×10¹²²", "≈94"; the 92 endpoint follows from the 10⁻²M_Pl⁴ variant ✓ |
| Eq. (E5) | `κn_ψ² = 8π(7.684×10⁻¹³ eV³)²/M_Pl² = 9.96×10⁻⁸⁰ eV⁴`; `/2.8×10⁻¹¹ = 3.56×10⁻⁶⁹` ("68.4 orders" ✓); `×3/16 = 1.87×10⁻⁸⁰ = 6.7×10⁻⁷⁰ρ_Λ` ✓; `/2.563×10⁻¹¹ = 3.88×10⁻⁶⁹` ("3.9×10⁻⁶⁹" ✓) | ✓ all |
| Eq. (E3) | `4πG = κ/2`; `−(3/2)πG = −3κ/16` | ✓ |
| Birefringence σ's | 0.342/0.094 = 3.64; 0.215/0.074 = 2.91 | ✓ "≈3.6σ", "≈2.9σ" |
| Fig. 1 ↔ bracket tags | read the TikZ source (`main.tex:847–873`) | every arrow matches its `[Rn]` tag; entry counts 7+2+1+3+1 = 14 across 13 classes ✓ |
| Data & Code Availability freeze claim | `git show 1130b7c5e3d2:<path>` vs working tree for all five named files | **all five byte-identical** ✓ |
| Build hygiene | `main.log` | 0 undefined references, 0 Overfull `\hbox` ✓ |
| Citations | all 26 entries spot-checked against known bibliographic data (Shapiro–Teixeira CQG 31 185002; Benedetti–Speziale JHEP 2011(6)107 and JPCS 360 012011; Mercuri PRL 103 081302; Date–Kaul–Sengupta PRD 79 044008; Eskilt–Komatsu PRD 106 063503 with 0.342°±0.094°; Minami–Komatsu PRL 125 221301 with 0.35°±0.14°; Ghosh–Mitra PLB 616 114; Nieh–Yan JMP 23 373; Hehl et al. RMP 48 393; Freidel–Minic–Takeuchi PRD 72 104002) | no citation-integrity defect found. Ref. [13] (arXiv:2509.13654) is correctly flagged in-bibliography as an unrefereed preprint; refs [1] and [14] are correctly and repeatedly labeled not-peer-reviewed |

---

## MAJOR findings

### MAJOR-1 [correctness] — Sec. IV A's opening sentence still carries the pre-erratum `O4 = 0` physics, and contradicts itself within the same sentence

**Anchor:** PDF p. 7, left column, first paragraph of Sec. IV A; `main.tex:1150–1156`.

Printed:

> "At the classical level the Holst term γ⁻¹ e^a∧e^b∧R_ab vanishes identically in the torsion-free sector
> by the first algebraic Bianchi identity (**it is not a topological invariant … it reduces to the Nieh–Yan
> density plus a torsion-squared piece, both of which vanish at T = 0** …) **and reduces to the Nieh–Yan
> density on shell once torsion is integrated out** [6, 7]."

The parenthetical is right; the main clause is not. The two are the same statement evaluated on the
two branches, and on shell the "torsion-squared piece" is exactly `O4`, which this manuscript now
computes to be **nonzero** — `O4^[4] = −3κγ³/(1+γ²)²(J⁵·J⁵)` [Eq. (13)], carried by the axial × trace-vector
channel of Eq. (1). Consequently the Holst dual on shell is `O1^[4] = −O2^[4] + ½O4^[4]`, i.e. the Nieh–Yan
total derivative **plus a nonvanishing Fierz-closed contact term**, not the Nieh–Yan density.

**Sibling sites grepped (`main.tex`), all of which say the correct thing:**
- `main.tex:1388–1390` (Sec. IV A case (i)): "on the on-shell branch O1 equals −O2 plus ½𝒪₄^[4] [Eq. (12)], and 𝒪₄^[4] is the Fierz-closed (J⁵·J⁵) contact term of Eq. (13)"
- `main.tex:2085–2091` (Sec. V): "On the on-shell branch O1 and O6 are not pointwise zero, and Eq. (12) gives O1^[4] = O6^[4] = −O2^[4] + ½O4^[4] exactly … plus half the ε-contracted torsion-square … O1 and O6 are therefore not exact total derivatives on shell"
- `main.tex:2124` (Sec. V): "it vanishes only in the γ → ∞ Einstein–Cartan limit, where the trace-vector irrep switches off"
- App. A 1 Check A (PDF p. 20 right col.): "Off that branch O1 and O6 are not pointwise zero; they are disposed of instead by Eq. (12) …"
- Table III caption (PDF p. 21): "O1 = O6 is zero on the torsion-free branch and equal to −O2 plus ½𝒪₄^[4] on the on-shell branch"

This is site 16 of the erratum sweep: `ech_torsion_onshell_2026_08_08.md` §7 item 15 scoped only
"Sec. IV A, Route 2 dark-energy leg, case (i)", which *was* fixed; the section's opening paragraph was not.

**Fix:** "…and reduces on shell, once torsion is integrated out, to the Nieh–Yan density plus the
ε-contracted torsion-square of Eq. (13) [6, 7] — the latter vanishing only in the γ → ∞ Einstein–Cartan
limit." Nothing downstream in Sec. IV A changes.

---

### MAJOR-2 [correctness] — Sec. VI declares the trace-vector torsion irrep outside the survey's scope, contradicting five other sections and voiding Eq. (13)'s own standing

**Anchor:** PDF p. 16, right column, "What is not established"; `main.tex:2200–2205`.

Printed:

> "It does not enumerate derivative four-fermion terms …, multi-species chiral structures …,
> dynamical-Immirzi-field completions, or **non-minimal (trace/tensor) torsion irreps — any of these
> constitutes a genuine escape from the minimal-coupling scope, not a loophole within it.**"

The trace-vector irrep is *not* non-minimal. Read literally, this sentence places the entire on-shell
content of `O4` — and therefore the `½O4^[4]` remainder of `O1 = O6` — outside the survey's declared
scope, which would gut the corrected Sec. V analysis rather than support it.

**Sibling sites grepped (`main.tex`), all of which contradict it:**
- `main.tex:704–712` (Sec. II): "The axial (4) and **trace-vector (4) irreps are both nonzero at every finite nonzero γ**, the trace-vector piece being sourced by the axial current through the Holst term; the tensor (16) irrep vanishes identically."
- `main.tex:2564–2567` (App. A 1): "solving it with no restriction on which irreps may appear leaves the tensor (16) irrep identically zero on shell, **while the trace-vector (4) irrep is generated by the Holst term under strictly minimal coupling and is carried throughout**."
- `main.tex:2904–2909` (App. C — the site the 2026-08-08 erratum §7 item 14 explicitly told the authors to fix, and which *was* fixed): "**The trace-vector irrep, by contrast, is generated under minimal coupling by the Holst term and is inside the lemma's reach, not outside it**: it enters the operator list through O4 …"
- `main.tex:3047–3054` (App. E): "an axial irrep and a trace-vector irrep in the ratio β/α = 1/(2γ) … In the γ → ∞ Einstein–Cartan limit the trace-vector piece switches off"
- App. A 1 Verdict (PDF p. 20 right col.) correctly lists only "the tensor torsion irrep" among the excluded classes.

App. C was corrected; Sec. VI was missed. Verified against `ech_torsion_onshell_2026_08_08.md` `[L11]`
(tensor irrep identically zero — exclusion correct) and `[L15]` (trace-vector nonzero under minimal
coupling — exclusion false).

**Fix:** "…or the **tensor** torsion irrep and other non-minimal torsion couplings — …". One word.

---

### MAJOR-3 [correctness] — the construction rule equates "carries one ε" with "parity-odd"; one listed member is parity-EVEN, and one genuinely parity-odd dimension-4 density is silently excluded

**Anchors:** construction rule `main.tex:1897–1910` (PDF p. 14 right col.); `O5` definition `main.tex:1978`
and Eq. (10) (PDF p. 14); App. B (PDF p. 21 left col.); abstract (PDF p. 1); Sec. V opening (PDF p. 13 right col.);
App. A 1 heading (PDF p. 19 right col.).

The rule reads: "densities are formed at zero additional derivative order …, **with a parity-odd ε
contraction**, full index contraction to a scalar density, and mass dimension exactly four…". Two
consequences follow, neither of which the manuscript addresses:

**(a) `O5` is parity-EVEN off shell**, by the paper's own argument. App. B states, correctly:
"For ϑ_NY a pseudoscalar, ∂_μϑ_NY transforms as a pseudo-co-vector and J^{5μ} as a pseudo-vector, so
their Lorentz-scalar contraction ∂_μϑ_NY J^{5μ} is **parity-even** as a Lagrangian term."
Apply the identical count to `O5^[4] = ε^{μνρσ}T^I{}_{μν}e_{Iρ}J^5_σ`: `ε` contracted with true tensors
(`T`, `e`) yields a pseudo-vector in σ; contracted with the pseudo-vector `J^5_σ` this is pseudo × pseudo =
**parity-even**. Explicitly, every term of the ε-sum carries exactly three spatial indices, giving `(−1)³`,
and the axial `J^5` supplies one further `(−1)`. `O1, O2, O3, O4, O6` each carry one ε and zero axial
factors and are genuinely P-odd; `O5` is the sole exception. The paper's disclaimer
("the parity-odd label belongs to the pre-reduction ε-contracted densities", `main.tex:2103–2106`;
"They are parity-odd as ε-contracted densities before on-shell reduction", abstract) does not rescue
`O5`, whose P-evenness is already present *before* any on-shell reduction.

**(b) A genuinely parity-odd, zero-derivative, exactly-dimension-4 density built from the admitted
blocks is excluded by the ε requirement and is never enumerated or disposed of:** the torsion trace
contracted with the axial current,

    V·J⁵ ≡ T^a{}_{ab} J^{5b},   [T] = +1, [J⁵] = +3  ⇒  dimension exactly 4, dimensionless Wilson coefficient
                                (no M_Pl² promotion needed — the same footing as O3 and O5)

`T^a{}_{ab}` is a true vector (torsion is a true tensor), so its contraction with the axial `J⁵` is a
genuine pseudoscalar. It is local, Lorentz- and diffeo-invariant, built only from Eq. (1)'s algebraic
torsion and the minimal axial current, and carries no derivative beyond those internal to `T`. It
cannot be a linear combination of `{O1–O6}`, all of which carry an ε. On shell, using Eq. (1),
`V_c = 3β J^5_c`, so `V·J⁵ = 3β(J⁵·J⁵) = (3κγ/[4(1+γ²)])(J⁵·J⁵) ≠ 0`. By inspection of the block dimensions
(`e`:0, `T`:+1, `R`:+2, `J⁵`:+3) this is the *only* ε-free P-odd dimension-4 admissible density, so the gap
is exactly one operator wide.

**The no-go is unaffected** — `V·J⁵` is the same Fierz-closed `(J⁵·J⁵)` structure at the same `M_Pl⁻²`
power as `O4` and `O5`, covered verbatim by App. C's projection lemma and App. A's single-scale ceiling.
But as printed, "we exhibit every rule-admitted local, Lorentz- and diffeomorphism-invariant,
**parity-odd** density of mass dimension exactly +4" (App. A 1) and the abstract's "six-member spanning
list {O1–O6} of … **parity-odd densities** of mass dimension exactly four" overstate what the rule
delivers, and Sec. VI's list of disclosed exclusions does not include the ε-free P-odd sector.

**Fix (all local, no physics change):** (i) state the rule as "one spacetime ε contraction" and drop
"parity-odd" from the rule itself; (ii) note in App. B or Sec. V that `O5` is P-even off shell by the
same pseudo × pseudo count App. B already performs, so the list is the ε-contracted sector rather than
the P-odd sector; (iii) either add `V·J⁵ = 3β(J⁵·J⁵)` to the list (it lands in class (ii) and *strengthens*
the "every member is disposed of" statement) or add "ε-free parity-odd densities such as `T^a{}_{ab}J^{5b}`,
which are covered by the same Fierz closure" to the disclosed exclusions in Sec. VI and App. C.

---

### MAJOR-4 [presentation] — the DOI-frozen artifact the paper directs the referee to prints conclusions the manuscript now contradicts, with no scoping note

**Anchor:** Data & Code Availability (PDF pp. 17–18); Sec. V `main.tex:2074–2080`; App. A 1 `main.tex` Check A/D paragraph.
**Artifact:** `arxiv/scripts/dim4_parityodd_enumeration.py`, frozen at commit `1130b7c5e3d2`
(byte-identity verified by me — the freeze claim itself is sound).

The manuscript describes it as "verifies the two reduction identities of Appendix A 1 (Checks A and D)"
and, in Sec. V, flags only the filename ("which, its filename notwithstanding, verifies the two
identities and performs no basis enumeration"). Both statements are literally true. But the script's
own docstring and printed `VERDICT` block, which is what a referee sees on running it, assert:

- `"CHECK D … every epsilon-contracted torsion-square collapses under the algebraic Cartan constraint
  T = kappa S"` (line 29) — the exact premise falsified by `ech_torsion_onshell_2026_08_08.md` §8 and
  by this manuscript's own Sec. II;
- `"(iii) a single-curvature parity-odd density (O1, O6) -> 0 by Bianchi"` (line 41) and
  `"O1,O6 (single-curvature parity-odd) vanish by algebraic Bianchi."` (VERDICT) — **unqualified**, i.e.
  the pre-erratum class assignment that Table III and Eq. (12) now reverse on shell;
- `"the six-member basis {O1-O6}"` (lines 16–17, 35) and `"every member of the exhibited basis"` (VERDICT)
  — the word the manuscript now explicitly rejects ("spanning list, not a basis", abstract, Sec. V, Sec. VII);
- a sign typo in the docstring: `"epsilon_{abcd} epsilon^{abce} = 3! delta^e_d"` (line 27) versus the
  `−3! δ^e_d` the manuscript prints and the script's own `check_D` verifies (line 186: `equals -6*I`).

`operator_basis_adjudication_2026_08_07.md` was given a dated erratum addendum for precisely this class
of staleness; `dim4_parityodd_enumeration.py` was not, and it is the *first* artifact the paper names.
A referee running the cited chain gets stdout contradicting Table III.

**Fix:** add one sentence to Data & Code Availability scoping the first script's printed verdict to the
torsion-free / γ → ∞ branch and pointing to `ech_torsion_onshell_2026_08_08` for the on-shell branch;
or ship a dated erratum note alongside the frozen file, as was done for the 2026-08-07 report.

---

## MINOR findings

**MINOR-1 [correctness] — "the Holst sign convention flips it and changes nothing else" is falsified by the paper's own artifact.**
Anchor: PDF p. 3, `main.tex:701–704`: "the overall torsion sign is a convention, taken positive in the
axial channel, and the Holst sign convention flips it and changes nothing else."
Per `ech_torsion_onshell_2026_08_08.md` §3, `α = −γ²κλ/[2(γ²+s_H²)]` is independent of the Holst sign `s_H`
while `β = −γκλ s_H/[4(γ²+s_H²)]` is proportional to it, so `β/α = s_H/(2γ)`: flipping `s_H` flips β
**relative to** α, which is not an overall torsion-sign flip. Because `O4 = −24αβ(J⁵·J⁵)`, the printed
sign of Eq. (13), of Table III's `O4` row, and of the `½O4^[4]` remainder in the `O1`/`O6` rows all flip
under the other Holst convention — cf. `[L46]`, `[L47]` ("The Holst-sign convention flips the overall sign
and nothing else", said there of `O4`, not of the torsion). Magnitudes and the disposal class are
unaffected. Fix: "…and the Holst sign convention flips the relative sign of the trace-vector piece, hence
the overall sign of Eq. (13); no magnitude and no disposal class changes."

**MINOR-2 [presentation] — Table III's `Final` column for `O1`/`O6` does not follow from the table's own stated rule and disagrees with its own caption.**
Anchor: PDF p. 21, Table III rows `O1` and `O6` (verified at 300 DPI, not from `pdftotext`).
Printed: `Fate (bare)` = "0 at T=0 (Bianchi, Check A); **−NY + ½𝒪₄** on shell"; `Final (×prefactor)` = "**½𝒪₄^[4]**".
The caption defines "the 'Final' column restores the prefactor", which applied to the printed Fate gives
`−𝒪₂^[4] + ½𝒪₄^[4]` — precisely what the same caption ("equal to −O2 plus ½𝒪₄^[4] on the on-shell branch"),
Eq. (12), Sec. V and App. A 1 Check A all state. The `Final` cell silently drops the total derivative.
Separately, the `Fate (bare)` cell mixes bare `NY` with `½𝒪₄`, which the caption renders as the promoted
`½𝒪₄^[4]`; as printed the two addends sit at different mass dimensions. Fix: `Final` → `−𝒪₂^[4] + ½𝒪₄^[4]
(→ ½𝒪₄^[4] in EOM/vacuum energy)`, or restate the column rule as "EOM / vacuum-energy content, prefactor restored".

**MINOR-3 [presentation] — "`T_I∧T^I` is supported only by the non-axial torsion irreps" is a necessary condition presented as a characterization, and is corrected by the clause that immediately follows it.**
Anchors: Sec. V `main.tex:2109–2112`; App. A 1 `main.tex:2588–2592`. Both continue: "…the ε-contracted
square vanishes on the pure vector part and on the pure axial part, and is nonzero only on the tensor
irrep and on vector×axial cross terms" — i.e. `O4` requires a non-axial irrep **and** an axial one
(`ech_torsion_onshell` `[L25]`: `O4 = −24αβ`). Suggest "…is supported only *through* the tensor irrep and
the axial × trace-vector cross term; in particular it vanishes on a pure axial and on a pure trace-vector
torsion alike."

**MINOR-4 [presentation] — the residual `T = κS` reading is not closed out.**
Sec. II retains `S^abc = ¼ε^abcd J^5_d`, and `[T] = [κS] = +1` is used for dimension counting
(`main.tex:1935`, `2568`), while Eq. (1)/(E2) give `T_abc → (κ/2)ε_abcd J^{5d}` in the γ → ∞ limit
(PDF p. 24, verified at 300 DPI) — i.e. `T = 2κS`. The manuscript no longer *asserts* `T = κS` anywhere
(the R12 factor-2 conflict is genuinely resolved by adopting Eq. (E2) throughout, and `O4`/`O5` are now
consistently READING-I: `−3κγ³/(1+γ²)²` and `−3κγ²/(1+γ²)`, matching `ech_torsion_onshell` §6 READING-I
`[L32]`, `[L33]`). But a referee comparing to the textbook algebraic Cartan relation will hit the factor 2.
One sentence in Sec. II or App. E ("the Eq. (E2) normalization is twice the `T = κS` convention; all
operator values in Table III use Eq. (E2)") closes `ech_torsion_onshell` §7 item 16 explicitly rather
than by omission.

**MINOR-5 [presentation] — `B11` and `B12` carry unexplained `[R3]` route tags.**
Anchor: PDF p. 6. `B9` is given an explicit justification of its `[R2]` tag ("The [R2] tag records which
route this removes an escape from rather than which amplitude it bounds…"). `B11` (universal low-energy
gauge-field decoupling) and `B12` (a bounce-epoch GW energy-density ceiling) receive no analogous
sentence, and neither is an obvious escape route for quantum running of γ. Fig. 1 (`main.tex:864`) and
Table I are internally consistent with the tags — this is a text gap, not a diagram error. One clause
each would settle it.

**MINOR-6 [presentation] — the load-bearing correction rests on artifacts that are not yet archivally frozen.**
Data & Code Availability states that files 6–8 (`operator_basis_adjudication_2026_08_07.md`, which now
carries the 2026-08-08 erratum addendum, and both `ech_torsion_onshell_2026_08_08` files) "postdate that
commit and are available at the repository head", with "an updated archival deposit … planned prior to
publication". The entire corrected `O4` / `O1` / `O6` result — Eq. (13), Table III, App. A 1 — depends on
`ech_torsion_onshell_2026_08_08`, which is currently mutable and DOI-less. This is disclosed, but it is
the weakest link in an otherwise exemplary provenance chain, and a journal will ask for the DOI before
acceptance rather than after.

**MINOR-7 [presentation] — the headline "≈60 orders" is the double-normalized ratio, not the ratio to the observed signal.**
Eq. (3)'s LHS is `Δθ/(β_obs·[M_Pl(α/M)])`, whose value is `1.7×10⁻⁶⁰`; the direct ratio `Δθ/β_obs` is
`1.7×10⁻⁶²`. Sec. IV A discloses this fully and explains that the larger number is deliberately
conservative — but the abstract and Sec. VI both report it as "roughly sixty orders of magnitude of
suppression margin … **against the observed birefringence amplitude**", a register in which the honest
number is 62. The conservatism runs in the safe direction; a five-word parenthetical
("under the double normalization of Eq. (3)") would remove the ambiguity.

**MINOR-8 [presentation] — the trichotomy's third class is empty on the branch the paper actually works on.**
Abstract ("every member is a topological total derivative, a Fierz-closed four-fermion contact term …,
or identically vanishing") and Sec. V (`main.tex` class (iii): "densities that vanish identically (O1 and
O6 on the torsion-free branch)") state a three-way disjunction whose third class has **no member on the
ECH on-shell branch**. Both passages scope it correctly in the very next clause, so this is not an error;
but as a headline it reads as a property of the on-shell list. Suggest "…or, on the torsion-free branch
only, identically vanishing."

---

## Candidates raised and WITHDRAWN after high-DPI re-render or `main.tex` grep

1. **`B1`'s `g_eff ∼ 1/(M_Pl√|t3|)` with `|t3| ∼ m_T⁻¹` appeared dimensionally impossible** (it would give
   `g_eff ∼ √m_T/M_Pl`, not `H0/M_Pl`). **WITHDRAWN.** `pdftotext` drops the radical; `main.tex` and the
   300 DPI render of p. 4 both read `√|t3| ∼ m_T⁻¹`, giving `g_eff ∼ m_T/M_Pl ∼ H0/M_Pl` and, for `g_eff ∼ 1`,
   `m_T ∼ M_Pl` — exactly as the entry continues. Correct as printed.

2. **Fig. 1's Branch L/M box appeared to arrow into `R2` rather than `R3`,** contradicting the `[R3]` tags
   on `B10`–`B12`. **WITHDRAWN.** The TikZ source (`main.tex:862–873`) draws `LM → R3`; all fourteen edges
   match their bracket tags, and the arrow counts per route (R1:3, R2:4, R3:4, R4:3) are correct.
   The apparent mismatch was a raster-tracing error on my part.

3. **"Two Tier-I claims": Sec. IV A calls the `O1`/`O2` operator statement "rigorous (Tier-I) about the
   list" while the abstract says only perturbation transparency is Tier-I.** **WITHDRAWN after grep.**
   Every sibling site (`main.tex:503–504`, `600`, `772–780`, `901`, `1398–1404`, `1725`, `2218`, `2916`)
   consistently distinguishes a Tier-I *leg* / *rigorous theorem* (exactly one: B14, branch-scoped to
   zero spin) from a Tier-I *fact about the list*, and records the R2 dark-energy leg itself at Tier-II
   in Table II. The hedging is deliberate and correct.

4. **Table III's `O4` row appeared to lose a factor κ between `Fate (bare)` = `−3κ²γ³(1+γ²)⁻²(J⁵)²` and
   `Final` = `−3κγ³(1+γ²)⁻²(J⁵)²`.** **WITHDRAWN.** The prefactor is `M̄_Pl²` and the paper states
   `M̄_Pl²κ² = κ` explicitly in App. A 1 ("exact in the reduced-mass convention `κ = M̄_Pl⁻²` of Sec. II").
   Verified: correct, and consistent between Eq. (13), Table III and the caption.

5. **Eq. (12)'s `O1 = ½O4 − O2` appeared to conflict with the Nieh–Yan identity `d(e_I∧T^I) = T_I∧T^I −
   e_I∧e_J∧R^{IJ}`, which naively gives `O1 = O4 − O2`.** **WITHDRAWN.** `operator_basis_adjudication_2026_08_07.md`
   §4 `[L60]`–`[L65]` shows the naive 1:1:1 reading carries a factor-2 slip on `O4`, traceable to the
   form-versus-density normalization; the manuscript now fixes that normalization explicitly in Eq. (11)
   and derives the `¼B − ½A` vs `½B − A` factor-of-two in text. I re-checked the algebra: with
   `NY = ½B − A`, `2O1 + 2O2 − O4 = 2A + 2(½B − A) − B = 0` identically. Correct as printed, and the
   explanatory paragraph is a genuine improvement.

---

## Summary for the board

| | count |
|---|---|
| MAJOR | 4 (3 `[correctness]`, 1 `[presentation]`) |
| MINOR | 8 (1 `[correctness]`, 7 `[presentation]`) |
| Displayed equations / numerics independently re-derived and confirmed correct | 20 |
| Candidates withdrawn after 300 DPI re-render or `main.tex` grep | 5 |
| Citation-integrity defects | 0 |
| Presentation blockers (undefined refs, overfull boxes, broken artifact paths, stale freeze claims) | 0 |

None of the four MAJORs changes a physical conclusion of the survey: MAJOR-1 and MAJOR-2 are surviving
pre-erratum text at two sites the 2026-08-08 sweep did not enumerate, MAJOR-3 is a parity mis-labelling
whose one omitted operator lands in the disposal class the paper already establishes, and MAJOR-4 is an
artifact-consistency gap. With those four sites and the eight MINORs closed, I would expect to return
ACCEPT on the next pass.
