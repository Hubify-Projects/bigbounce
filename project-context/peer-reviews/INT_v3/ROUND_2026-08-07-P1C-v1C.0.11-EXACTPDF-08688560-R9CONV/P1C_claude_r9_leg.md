# P1C v1C.0.11 — Independent Referee Report (Claude leg, R9 convergence round)

**Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf` — "A Structural No-Go Survey of Minimal
Spin-Torsion Routes to Dark Energy and Bounce Phenomenology", H. Golden.
**PDF SHA-256:** `0868856032e2eee5f26cd207d9fe1cc9b1db2eae827eac41b70c9b2aea394b37` — **verified against
the assigned hash before review; exact match.**
**Pages read:** 20 / 20 (full text, Table I–III, Fig. 1, Appendices A, A 1, B, C, D, E, bibliography).
**Date of review:** 2026-08-07.
**Role:** Independent, skeptical journal referee at CQG calibre. Blind leg — no prior review of this
manuscript or any earlier version was consulted. No manuscript file was edited; nothing committed or
pushed.
**Method note:** every suspect printed expression was re-rendered at 200–400 DPI with `pdftoppm`
before any math claim was asserted. This overturned one candidate finding (see "Candidate findings
withdrawn"). Numerical claims were re-derived independently in Python.

---

## VERDICT

**MAJOR REVISION.** The manuscript is unusually careful about its own evidentiary limits, the
arithmetic is overwhelmingly correct (I independently reproduced ~20 of its numbers, including the
non-trivial ones), the citation record is clean, and the presentation is production-quality (zero
overfull hboxes). It is not, however, publishable as printed: the operator-basis argument of Sec. V
— which the abstract, Discussion and Conclusions all headline — calls a linearly **dependent**
six-element list a "basis", and Table III assigns one of those elements a fate that its own quoted
Nieh–Yan identity contradicts. Separately, the abstract's Route-3 headline number ("61–67 orders of
magnitude below the observed dark-energy density") is asserted rather than derived anywhere in the
paper. None of these defects overturns the physics conclusion — every repair I can see leaves the
no-go intact — but each is a load-bearing printed claim that is presently wrong or unsupported, and
each is fixable within the existing material.

**Counts:** 4 MAJOR, 11 MINOR. **8 of the 15 findings are correctness-grade**
(MAJOR-1/2/3/4 and MINOR-2/4/6/8); the remaining 7 are presentation.

---

## MAJOR FINDINGS

### MAJOR-1 — {O1–O6} is not a basis: it contains a literal duplicate and an exact linear relation. [correctness]

**Anchors:** Abstract ("a six-member basis {O1–O6}"); Sec. V, Eq. (8) [p. 12]; Table III [p. 17];
Sec. VI "What is established"; Sec. VII; Appendix A 1.

Eq. (8) as printed (verified at 400 DPI) defines

- `O1^[4] = M_Pl² ε e^I e^J R_IJ` ("Holst dual"), and
- `O6^[4] = M_Pl² ε^{μνρσ} R_{μνρσ}`.

These are the **same density**. Contracting the internal indices with the tetrad,
`e^I_μ e^J_ν R_{IJρσ} = R_{μνρσ}`, so `ε^{μνρσ} e^I_μ e^J_ν R_{IJρσ} ≡ ε^{μνρσ} R_{μνρσ}`. The paper
itself performs exactly this conversion for Eq. (6) ("In components, the leading contribution reduces
to `∫d⁴x √−g (α/M) ε^{μνρσ} e^I_μ e^J_ν F_{IJρσ}`"), and Table III confirms the identification by
giving O1 and O6 identical "dim (bare) = 2", identical prefactor `M_Pl²`, identical "Fate
(bare) = vanishes (Bianchi, Check A)" and identical "Final = 0". Sec. V's own gloss — "it kills both
O1 (the Holst dual) and O6 (**any single-curvature parity-odd density**)" — concedes that O6 is the
class of which O1 is a member.

Worse, the paper *quotes the relation that makes a second member redundant*. Immediately after
Eq. (8): "the torsion piece of the Nieh–Yan identity `d(e^I ∧ T^I) = T_I ∧ T^I − e^I ∧ e^J ∧ R_IJ`
[19]". In the paper's own normalization that identity reads

    O2 = O4 − O1     (equivalently  O1 = O4 − O2),

so O1, O2, O4 satisfy an exact linear relation. Combining with O1 ≡ O6, the six-element list has
**rank ≤ 4** — an independent set is {O2, O3, O4, O5}.

"Basis" is therefore the wrong word, and the head-count "six-member" is inflated. This matters
because the six-member count is the quantitative content the abstract advertises for Sec. V ("a
six-member basis {O1–O6} … is shown to close") and is repeated verbatim in Sec. VI and Sec. VII.

*This does not damage the physics.* A redundant spanning set still bounds every admitted density, and
the surviving independent members land in exactly the three disposal classes the paper claims. The
fix is editorial-plus-honest: (i) call it a **spanning list / generating set**, not a basis; (ii)
state the two relations explicitly (O1 ≡ O6 by tetrad conversion; O1 = O4 − O2 by Nieh–Yan) and say
why the redundancy is deliberate (each entry is retained because it is a *recognizable* invariant);
and (iii) either recount as "four independent densities, presented as six named invariants" or
justify the six-count as a naming convention. If O6 is in fact intended to be built from the
Levi-Civita curvature `R̊` rather than the torsionful `R`, that must be written in Eq. (8) and
Table III — as printed both use the same symbol `R`, and the construction rule (Sec. V) admits only
"the curvature two-form of the torsionful connection".

### MAJOR-2 — Table III's "Final = 0" for O1, and the abstract's trichotomy, contradict the paper's own on-shell treatment of O1. [correctness]

**Anchors:** Table III row O1 [p. 17]; Abstract ("every member is a topological total derivative, a
Fierz-closed four-fermion contact term uniformly suppressed by `M_Pl^{-2}`, or identically vanishing
by the algebraic Bianchi identity"); Sec. V bullet (a); Sec. VII.

Table III records O1's fate as "vanishes (Bianchi, Check A)" → Final `0`. Check A [Eq. (A4)] proves
`ε^{μνρσ} R_{μνρσ} = 0` for a curvature obeying the pair antisymmetries **and the first Bianchi
identity** — i.e. for the Levi-Civita/torsion-free curvature. With the algebraic Cartan constraint
imposed and `T = κS ≠ 0` (the regime in which O4 and O5 are non-zero and the whole four-fermion
discussion lives), the first Bianchi identity acquires torsion terms and O1 does **not** vanish: by
the Nieh–Yan identity the paper quotes, `O1 = O4 − O2 → κ(J⁵·J⁵) − (total derivative)`. Table III
then reads `0 = κ(J⁵·J⁵) − 0`, an internal contradiction between two of its own rows.

The running prose is correct — Sec. V (a) writes "killing both O1 and O6 **on the torsion-free
branch**. The torsionful piece of R is O(κS) and merely feeds the O4/O5 four-fermion channel" — so
this is a table/abstract error, not a physics error. But the abstract's clean three-way trichotomy
mis-sorts O1 into "identically vanishing by the algebraic Bianchi identity", which is false with
torsion on shell, and Table III is the artifact a referee/reader will cite.

**Requested fix:** add the branch qualifier to Table III (O1: "0 on torsion-free branch;
→ κ(J⁵·J⁵) via Nieh–Yan when T = κS"), and reword the abstract's trichotomy so that "identically
vanishing" is scoped to the torsion-free branch.

### MAJOR-3 — The Route-3 headline ("61–67 orders below ρ_Λ") is asserted, never derived; the only quantitative step is an *amplitude* ratio silently promoted to a *density* ratio. [correctness]

**Anchors:** Abstract ("leaves the contribution 61–67 orders of magnitude below the observed
dark-energy density"); Sec. IV B [p. 8, final paragraph before the "Ansatz vs derivation" block];
Sec. VI "What is established"; Sec. VII; Table II row R3.

The complete printed chain for Route 3's dark-energy statement is:

> "The Holst sector amplitude that this running can source is fixed by mass dimension: any operator
> built from γ, R^ab, e^a, and the chiral current J^{5μ} must carry dimension four, which forces a
> single power of `M_Pl^{-1}` in the prefactor in any cosmologically relevant scalar-curvature
> regime. Plugging the conservative ∆γ/γ ∼ 0.3 into the resulting parity-odd amplitude, the
> cosmologically integrated effect is suppressed by an additional factor of `(∆γ/γ)·(H/M_Pl)
> ∼ 3×10^{-62}` **relative to the dimensionless parity-odd amplitude budget associated with a
> dark-energy-scale source**, closing this route by many orders of magnitude."

and then, one column earlier and one paragraph later:

> "Propagated to the dark-energy channel through the paper's own `(∆γ/γ)·(H0/M_Pl)` mass-dimension
> suppression, the derived torsion/Immirzi contribution to `ρ_Λ` sits ∼61–67 orders of magnitude
> below the observed dark-energy density."

Three problems, all correctness-grade:

1. **No equation.** There is no displayed expression anywhere in the paper for the Route-3
   contribution to `ρ_Λ`. Routes 1, 2 and 4 each get one — Table II's `κn_ψ²/ρ_Λ`, Eq. (2), and the
   `β = (α/2M)∆φ` chain of Sec. IV C. Route 3, which supplies the abstract's largest advertised
   margin, gets none.
2. **Undefined denominator.** "the dimensionless parity-odd amplitude budget associated with a
   dark-energy-scale source" is not defined anywhere in the manuscript. The first sentence therefore
   states a suppression *relative to an undefined quantity*; the second sentence states a suppression
   relative to `ρ_Λ,obs`. These are different denominators, and the step from one to the other is
   never made. Numerically I can confirm only that `0.3 × 1.18×10^{-61} = 3.5×10^{-62}` (→ "61
   orders") and `1.4×10^{-6} × 1.18×10^{-61} = 1.65×10^{-67}` (→ "67 orders"), i.e. the two endpoints
   are literally the product `(∆γ/γ)(H0/M_Pl)` read as a *density ratio*. Why a dimensionless
   amplitude-suppression factor equals `ρ_R3/ρ_Λ` is exactly the missing step. (Note that Appendix A
   is *not* available as a substitute: it bounds Eq. (6)'s `α/M ε e e F` operator, not a
   γ-running-sourced density.)
3. **`H` vs `H0` inconsistency.** The Sec. IV B sentence writes `(∆γ/γ)·(H/M_Pl)` with an unspecified
   epoch; the follow-up writes `(∆γ/γ)·(H0/M_Pl)`. At the bounce `H/M_Pl = O(1)`, which would
   destroy the number, so `H0` must be meant — but as printed the two statements differ by 61 orders
   of magnitude.

**Requested fix:** supply the one-line operator/density estimate that converts `∆γ` into a vacuum
energy (even a labelled Tier-III scaling equation would suffice), define the reference budget, and
make the Hubble symbol uniform. Alternatively, downgrade the abstract/Conclusions wording to a
statement about the *parity-odd amplitude*, matching what is actually computed. The margin is so
large that no plausible completion reopens the route — which is precisely why the missing line
should be cheap to add.

### MAJOR-4 — Route 2 is closed against a birefringence angle, not against a dark-energy density, yet the section title, abstract and Conclusions present it as a dark-energy closure. [correctness / scope honesty]

**Anchors:** Sec. IV title ("THE ROUTE-2/ROUTE-3 DARK-ENERGY ROUTE CLOSURES"); Eq. (2) and the
surrounding closure statement [pp. 6–7]; Abstract ("closes against the observed birefringence
amplitude with roughly sixty orders of magnitude … of suppression margin"); Sec. VI, Sec. VII.

Every quantitative object in Sec. IV A is a CMB rotation angle: `∆θ_one-loop`, `β_obs = 0.342°`,
Eq. (2)'s dimensionless budget ratio. The closure sentence is explicit — "the one-loop Holst-sector
parity-odd term cannot account for the observed **birefringence amplitude**". That is a clean and
correct result (I verified the arithmetic; see below). It is not, however, a bound on Route 2's
contribution to `ρ_Λ`, and the paper's own framing is that R1–R4 are "the four routes by which the
ECH bounce could plausibly source a Λ-like late-time density".

The paper does gesture at the missing bridge: "the off-shell dimension-(+1) parity-odd operator is in
any case bounded by the single-scale NDA no-go of App. A regardless of that O(1) coefficient". But
App. A bounds Eq. (6) — the `α/M ε e^I e^J F_IJ` phenomenological ansatz — which is a **different
operator** from Eq. (1)'s `(β(γ)/16π² M_Pl) ∂_μ ϑ_NY J^{5μ}`. Indeed the paper takes pains elsewhere
to show that Eq. (1)'s Lagrangian density is a *bona fide* dimension-+4 object ("carries dimension
−1 + 2 + 3 = +4 and the action is dimensionless, as required"), so calling it "the off-shell
dimension-(+1) parity-odd operator" in the App.-A-bridging sentence is a category error: Eq. (1) has
no dimension deficit at all.

**Requested fix:** either (i) state plainly at the head of Sec. IV that Route 2's *dark-energy*
closure is inherited from the Sec. V / App. A operator-basis bound and that Sec. IV A closes only the
*birefringence channel*, or (ii) supply the R2 → `ρ_Λ` step. Also correct the "off-shell
dimension-(+1)" phrase so it does not appear to describe Eq. (1). This is squarely a scope-honesty
item; the manuscript is elsewhere exemplary on this axis, which makes the gap more conspicuous.

---

## MINOR FINDINGS

**MINOR-1 [presentation]** — Sec. IV A, immediately after the Shapiro–Teixeira discussion: "The
dimensionless coefficient is O(α_em/4π) multiplied by the Planck mass to a single negative power." A
dimensionless coefficient multiplied by `M_Pl^{-1}` is not dimensionless. Reword ("the prefactor is
`α_em/(4π)` times a single inverse power of `M_Pl`"). The next sentence already gets this right.

**MINOR-2 [correctness]** — Table III caption and Appendix A 1 both say the Cartan-reduced
four-fermion operators carry "natural coefficient ∼ `M_Pl⁴` by single-scale NDA". By the paper's own
construction (Sec. V: "each `c_n O_n^[4]` is a bona-fide dimension-4 density" with `c_n` a
"dimensionless rational"), `M_Pl⁴` is the natural **density/vacuum-energy scale**, not the
coefficient. As printed it contradicts the dimensionless-`c_n` contract the same paragraph
establishes. Same wording recurs in Sec. V ("Fierz-closed basis with natural coefficient ∼ `M_Pl⁴`").

**MINOR-3 [presentation]** — Sec. V, collapse bullet (b): "the four-fermion contact operator
`κ²(J⁵·J⁵)` — itself parity-even (Appendix B)". Appendix B classifies only the Route-2 operator
`∂_μ ϑ_NY J^{5μ}`; it says nothing about `(J⁵)²`. The statement that a product of two axial currents
is a Lorentz scalar lives in B8 (Sec. III A). Retarget the cross-reference.

**MINOR-4 [correctness]** — Sec. IV B: Eq. (3) is described as "a conservative upper bound consistent
with the |γ|-dependent Benedetti–Speziale β-function structure recorded above (four-fermion-driven,
sole fixed point at γ² = 1, sign set by |γ| ≷ 1)". Eq. (3), `dγ/d ln μ = (N_F^L − N_F^R)γ/12π²`, has
a fixed point at γ = 0, has **no** fixed point at γ² = 1, and is purely logarithmic where Eq. (4) is
power-suppressed by `μ²κ̃²`. The two flows are structurally incompatible; only the *numerical
inequality* `0.3 ≫ 1.4×10^{-6}` is defensible. Reword to "numerically bounded above by" and drop the
claim of structural consistency.

**MINOR-5 [presentation]** — Terminology collision on "genuine dimension-4". Sec. V (and Table III's
caption) call O4 and O5 "the two genuine dimension-4 densities", while the same section states that
"the off-shell operators O1–O6 are genuinely dimension +4 (each carrying the compensating `M_Pl²`
factor)". The intended distinction is between the two *bare* invariants that already sit at dimension
4 before promotion (which are O3 and O5, per the same paragraph) and the two that land on the Fierz
basis (O4 and O5). Three different senses of the phrase appear within two columns. Fix the wording.

**MINOR-6 [correctness, immaterial to the result]** — Appendix D, Step 4: "Evaluated on the
Levi-Civita connection the Holst term reduces to `½ ε^{μνρσ} R_{μνρσ}(Γ̊)`". The Holst term carries
the explicit `γ^{-1}` prefactor introduced in Sec. II; the printed reduction drops it. Since the
expression vanishes identically the theorem is unaffected, but as written the reduction is not an
equality.

**MINOR-7 [presentation]** — "Of the four parity-odd/dark-energy channels enumerated by this
framework" (Abstract) and "R1–R4 cover the four parity-odd/dark-energy channels of this framework"
(Sec. IV C) read as classifying all four routes as parity-odd, whereas B8 and Sec. V both establish
that R1's operator `(J⁵)²` is **parity-even**. The slash is presumably disjunctive, but a referee
should not have to guess. Recommend "the four parity-odd or dark-energy channels" or a rephrase.

**MINOR-8 [correctness of a counting claim]** — Sec. III fixes the meaning of "distinct" as "no
barrier is a logical consequence of another". B11 (Decoupling Universality: "at low energies all
gauge fields decouple from the Planck-suppressed torsion sector equally") and B13 (Gravitational
Democracy: "torsion couples democratically to all spin-1/2 species") are the same universality
principle applied to two different sectors, and B4 (Planck Suppression) supplies the suppression both
invoke. Either argue their logical independence explicitly, as is done at length for B8 vs B14, or
absorb one and quote 12. As printed, the "13 distinct" headline rests on a criterion the manuscript
applies rigorously to exactly one pair.

**MINOR-9 [presentation]** — The released script filename actively contradicts what the script does.
I read `arxiv/scripts/dim4_parityodd_enumeration.py` (218 lines): it contains exactly `[CHECK A]` and
`[CHECK D]` and performs no enumeration — precisely as the paper discloses three separate times
("which, its filename notwithstanding, verifies the two identities and performs no basis
enumeration"). The disclosure is admirable, but the honest fix is to rename the file (e.g.
`dim4_parityodd_identities.py`) in the planned archival deposit rather than to caveat it three times.
I verified all four artifacts in the Data and Code Availability statement exist, and that commit
`c80b7487` exists and matches the quoted short SHA `c80b7487b01f`.

**MINOR-10 [presentation]** — Ref. [13] (Diego-Palazuelos & Komatsu, ACT DR6 birefringence,
arXiv:2509.13654, 2025) carries no journal reference and no preprint/peer-review status label, while
Refs. [1] and [14] are scrupulously labelled "not an arXiv preprint and not peer reviewed". Apply the
same standard: mark [13] as a preprint. The quoted `β = 0.215° ± 0.074°` is used only as context, and
the derived `≈2.9σ` is arithmetically correct.

**MINOR-11 [presentation]** — The robustness claim is asymmetric between routes. Sec. VI states "the
closures are robust to O(1)–O(10^10) rescalings of their ansatz-level normalizations" for both R2 and
R3, but the explicit `10^10` stress test appears only for Route 2 ("leaves ≳48 orders"). For Route 3
the abstract's *lower* endpoint (61 orders) is already the pessimistic chiral-count bound, so a
further `10^10` inflation would leave ~51 orders — true, but never stated. Add the one-line Route-3
analogue or scope the sentence to R2.

---

## Candidate findings withdrawn after high-DPI re-render

Recording these so the convergence board can distinguish "checked and clean" from "not checked".

- **B1 torsion-coupling exponent (p. 4).** Low-DPI text extraction rendered the relation as
  `|t3| ∼ m_T^{-1}`, which is dimensionally inhomogeneous with the displayed
  `g_eff ∼ 1/(M_Pl √|t3|) ∼ H0/M_Pl`. Re-rendering page 4 at 260 DPI shows the printed relation is
  **`√|t3| ∼ m_T^{-1}`**, giving `g_eff ∼ m_T/M_Pl = H0/M_Pl ∼ 10^{-61}` — correct as printed.
  Withdrawn.
- **Fig. 1 barrier→route arrows (p. 4).** At low resolution R3 appeared to be missing the Branch L/M
  arrow. At 400 DPI the arrow counts are R1 = 3, R2 = 4, R3 = 4, R4 = 3 (14 total), which matches the
  class-level bracket assignments in Sec. III A exactly: R1 ← {Found. A, Found. B, Branch H};
  R2 ← {Found. C, Found. D, Branch J, B14}; R3 ← {Found. E, Found. F, Branch L/M, B14};
  R4 ← {Found. G, Branch N/O, B14}. Figure and text agree. Withdrawn.

---

## Verified-correct items (independently re-derived; recorded for the audit trail)

Mathematics / internal identities:

- Eq. (1) dimension bookkeeping: `−1 + 2 + 3 = +4`, action dimensionless. ✓
- Eq. (2) both lines mutually consistent (`1/[M_Pl(α/M)] = M/(α M_Pl)`); numerical evaluation
  `10^{-3}·10^{-61}/(10^{-2}·6×10^{-3}) = 1.7×10^{-60}`, and the alternative contraction
  `1.7×10^{-62}` — "two additional orders", and `10^{-60}` is indeed the conservative side. ✓
- `α_em/4π = 5.81×10^{-4}` (rounded up to `10^{-3}`, conservative for the claim). ✓
- `β_obs = 0.342° = 5.969×10^{-3}` rad. ✓ Significances `3.64σ` and `2.91σ`. ✓
- `H0/M_Pl = 1.18×10^{-61}`; `∂_μϑ_NY ∼ H0² = 2.1×10^{-66}` eV². ✓
- **Eq. (4) integrates to the quoted result.** Frozen-coefficient integration of
  `μ ∂γ²/∂μ = −(γ²−1)(23γ²+5) μ²κ̃²/(8π)²` with `κ̃² = 16πG`, `γ = 0.24`, `μ_UV = 10^16` GeV,
  `M_Pl = 1.2209×10^19` GeV gives `∆γ² = 1.59×10^{-7}` → **`|∆γ/γ| = 1.38×10^{-6}`**, matching the
  printed `≈1.4×10^{-6}`. The `γ² = 1` UV-attractive fixed point and the sign flip at `|γ| ≷ 1`
  follow from Eq. (4) as claimed. A Planck-scale UV boundary gives `|∆γ/γ| ≈ 2`, consistent with the
  "→ O(1)" statement. ✓
- Chiral-count arithmetic: `12π² = 118.4`; `30/12π² = 0.253`, `37/12π² = 0.312`, `32/12π² = 0.270`;
  `ln 10^16 = 36.84`, `ln 10^13 = 29.93`; exponentiated `0.288–0.367` vs quoted "0.29–0.36". ✓
- Shapiro–Teixeira ratio algebra: `|Ω44/α4| = (378+783γ²)/[120(1+γ²)]` follows correctly from the
  quoted `α4`, `Ω44`; `= 3.33` at `γ = 0.24`, `= 4.84` at `γ = 1`, infimum `378/120 = 3.15` — all as
  stated. ✓
- B12 window: `ρ_crit/ρ_Pl = √3/(32π²γ³)` gives `0.409` at `γ = 0.2375` and `0.267` at `γ = 0.274`;
  squares `0.168` and `0.071` → quoted `0.07–0.17`. ✓
- B1/B4 hierarchy: `(H0/M_Pl)² = 1.4×10^{-122}`. ✓
- Appendix A: `[α/M] = −1`, `[εeeF] = +2` ⇒ `+1`. ✓ `(α/M)M_Pl = 1.22×10^{-2}` → Eq. (A2)'s
  `10^{-2}M_Pl⁴`. ✓ `M_Pl⁴/ρ_Λ = 8.67×10^{122}` (exact inputs) vs quoted `8.7×10^{122}`. ✓
  `122 ln10/3 = 93.6 ≈ 94`; `ln10/3 = 0.77` shift; the 92–94 spread follows from the `10^{-2}`
  Case-II offset. ✓ `e^{-282} = 10^{-122.5}`. ✓
- Eq. (8) dimension audit: all six entries reach `+4` under the stated building-block dimensions. ✓
  `M_Pl²κ² = κ` exact in the reduced-mass convention, as flagged. ✓
- Check D: `S_abc S^abc = (1/16)(−3!)(J⁵·J⁵) = −(3/8)(J⁵·J⁵)`, and `ε_{abcd}ε^{abce} = −3!δ^e_d` is
  correct for mostly-plus Lorentzian signature. ✓
- Check A: `ε^{μνρσ}R_{μνρσ} = 0` follows from `R_{μ[νρσ]} = 0` (three cyclic terms, each an even
  permutation of the ε indices ⇒ `3 ε·R = 0`). ✓
- **Appendix C Fierz matrix verified numerically:** the printed `F_c` (rows/columns in order
  S, V, T, A, P) satisfies `F_c² = 1` exactly. Axial row `¼(−4,−2,0,−2,4) = (−1,−½,0,−½,1)`;
  `F_op = −F_c` ⇒ `(1,½,0,½,−1)` ⇒ Eq. (C2) `(J⁵·J⁵) → SS + ½VV + ½AA − PP`, with a vanishing tensor
  entry, exactly as printed. `(F_c)_AS = −1 ⇒ G_s = −3κ/16`. ✓
- Appendix E: `Q_γ Q_γ^{-1} = 1` verified by direct expansion using `⋆² = −1`. ✓
  `4πG = κ/2`, `−(3/2)πG = −3κ/16`. ✓ Eq. (E4) matches the Sec. II coefficient. ✓
- Appendix E benchmark arithmetic, recomputed from `ħc = 1.9733×10^{-5}` eV·cm and
  `M_Pl = 1.2209×10^{28}` eV: `κn_ψ² = 9.96×10^{-80}` eV⁴ (quoted `1.0×10^{-79}`);
  `/ρ_Λ(2.3 meV) = 3.56×10^{-69}` (quoted `3.6×10^{-69}`, `68.4` orders);
  `×3/16 = 1.87×10^{-80} = 6.7×10^{-70}ρ_Λ` (quoted); `/ρ_Λ(2.25 meV) = 3.88×10^{-69}` (quoted
  `3.9×10^{-69}`). All ✓ — including the Sec. II cross-reference to the same numbers.
- Sec. IV C: `√(2ρ_Λ)/H0 = 0.41 M_Pl ∼ M_Pl`; `2β_obs/M_Pl = 9.8×10^{-22}` GeV⁻¹ → `10^{-21}`. ✓

Counting / structural consistency:

- 7 foundations + 6 branches; 14 entries; B8 subsumed ⇒ 13 distinct. Consistent across Abstract,
  Sec. I, Sec. III, Fig. 1 caption, Table I caption, Sec. VI, Sec. VII. ✓
- Classification partition 9 novel + 4 known + 1 structural = 14. ✓ "Five general
  naturalness/classification arguments (B5, B6, B7, B10, B13)" consistent in three places. ✓
- Route-3 endpoints: `0.3 × 1.18×10^{-61} → 61` orders; `1.4×10^{-6} × 1.18×10^{-61} → 67` orders —
  arithmetically consistent with the abstract's "61–67" and with which endpoint is attributed to
  which input (subject to MAJOR-3). ✓
- Route-2 margins: `≈60`, "conservatively ≥58", "10^10 inflation ⇒ ≳48" — mutually consistent. ✓

Citation integrity (all 25 entries checked against author/title/journal/volume/page/year/arXiv id):

- Refs. [2]–[12] and [15]–[25] are bibliographically correct as printed, including Ashtekar–Singh
  CQG 28 213001 (2011); Ghosh–Mitra PLB 616 114 (2005) with the `γ ≈ 0.274` state-counting value
  correctly attributed; Holst PRD 53 5966 (1996); Freidel–Minic–Takeuchi PRD 72 104002 (2005);
  Mercuri PRL 103 081302 (2009); Date–Kaul–Sengupta PRD 79 044008 (2009); Benedetti–Speziale
  JHEP 06 (2011) 107 and J. Phys. Conf. Ser. 360 012011 (2012); Shapiro–Teixeira CQG 31 185002
  (2014); Eskilt–Komatsu PRD 106 063503 (2022) with the correct `0.342° ± 0.094°`; Minami–Komatsu
  PRL 125 221301 (2020) with `0.35° ± 0.14°`; Nieh–Yan JMP 23 373 (1982); Kimura PTP 42 1191 (1969);
  Delbourgo–Salam PLB 40 381 (1972); Poplawski PLB 694 181 (2010); the three SMEFT power-counting
  refs; Itzykson–Zuber; Nieves–Pal AJP 72 1100 (2004).
- Attribution hygiene is above field norm: every borrowed result is labelled with what it does and
  does not establish ("motivated by (but not literally derived in)", "does not itself present the
  explicit RG equation used below", "not a value quoted in Ref. [4]"), the companion is explicitly
  flagged "not peer reviewed", and the acknowledgments carry a no-endorsement disclaimer. Only
  MINOR-10 applies.

Presentation blockers:

- `main.log`: **0 overfull hboxes**, 0 LaTeX warnings, no undefined references. 53 underfull hboxes
  (all justification-related in two-column revtex; none visually objectionable in the rendered
  pages I inspected).
- Fig. 1 renders cleanly at 400 DPI; Tables I–III are within column/page bounds; no `\texttt` path
  overflow; the four Data-and-Code paths and the pinned commit resolve locally.
- No blocking presentation defects found.

---

## Summary for the board

- **Verdict:** MAJOR REVISION.
- **MAJOR:** 4 — (1) `{O1–O6}` is not a linearly independent basis (O1 ≡ O6; O1 = O4 − O2 by the
  paper's own Nieh–Yan identity); (2) Table III / abstract assign O1 the fate "identically 0", which
  contradicts that same identity once `T = κS`; (3) the Route-3 "61–67 orders below `ρ_Λ`" headline
  has no derivation, an undefined reference budget, and an `H`-vs-`H0` inconsistency; (4) Route 2 is
  closed against a birefringence angle while being framed as a dark-energy closure, with the bridging
  sentence mis-describing Eq. (1) as the dimension-(+1) operator.
- **MINOR:** 11.
- **Correctness-grade findings:** 8 of 15 (MAJOR-1, 2, 3, 4; MINOR-2, 4, 6, 8).
- **Assessment:** none of the four MAJORs is fatal to the physics. Every one of them is a
  bookkeeping, wording, or missing-line defect in claims the paper is otherwise well positioned to
  support, and the closure margins (48–122 orders) are far too large for any of the repairs to change
  a conclusion. The arithmetic and citation record are the strongest I have seen in a single-author
  manuscript of this type. Recommend acceptance after the four MAJOR items are addressed.
