# P1N v1N.0.1 — Claude INT referee leg (R1 board)

**Reviewer:** Claude INT referee leg (independent, skeptical Classical and Quantum Gravity referee)
**Model:** claude-opus
**Input PDF:** `arxiv/paper1bc_ech_note/main.pdf`
**sha256:** `2287537b1cf2420b2aa043b6d07da1281fb2844a82e296e7658467c7362747ba`
**Pages:** 6 (letter, revtex4-2 aps/prd twocolumn)
**Source:** `arxiv/paper1bc_ech_note/main.tex` (596 lines), `references.bib`
**Date:** 2026-09-02
**Binding:** every equation, sign, coefficient and numeric below was checked against the `.tex` line AND a ≥300-DPI render (`pdftoppm -r 300`) of the cited page. Independent 4-pass recompile from a clean temp dir: **6 pages, 0 overfull hbox, 0 undefined reference, 0 undefined citation.**

**Sources consulted for cross-checking condensed claims:**
`research/theory_audit/ech_torsion_onshell_2026_08_08.md`;
`research/theory_audit/operator_basis_adjudication_2026_08_07.md` (incl. the 2026-08-08 ERRATUM ADDENDUM);
`arxiv/paper1c_nogo_survey/main.tex` (P1C v1C.0.16);
`project-context/peer-reviews/INT_v3/ROUND_2026-08-08-P1C-v1C.0.15-EXACTPDF-f3e29c45-R13CONV/` (R13 leg + truth audit).

---

## VERDICT: **MAJOR REVISIONS** — 6 MAJOR, 10 MINOR

Two MAJORs (M1, M2) are **regressions**: corrections that the source survey P1C v1C.0.16 already made, under the R13 board, are absent from the merged Note and the pre-erratum text has returned. One MAJOR (M3) is a **dropped closure** from the same board. One (M4) is the Note's headline positioning claim stated above its evidential strength. One (M5) is an attribution defect whose fix is already sitting unused in the Note's own `.bib`. One (M6) is the evaluability question a CQG referee cannot get past.

No fabricated result was found. Every number I could trace (3.6e-69, ≳58, 61–67, 0.07–0.17, β_obs, f_NL = −35/16, G_s = −3κ/16, the γ²/(1+γ²) coefficient, rank 4 / rank 2, O1 = ½O4 − O2, β/α = 1/2γ) traces correctly to P1C v1C.0.16 or to the two theory-audit artifacts. The defects are **scope, branch, normalization, attribution, and verifiability** — not invention.

---

## Independently verified as CORRECT (recorded so the board does not re-litigate)

1. **Eq. (1)**, p. 2. `S = (1/4κ)∫(ε_IJKL + (2/γ)η_{I[K}η_{L]J}) e^I∧e^J∧R^KL`. Equals `(1/2κ)∫(½ε + γ^{-1}ηη)`, i.e. exactly the `Q_γ = ⋆ + γ^{-1}𝟙` the same paragraph asserts. Internally consistent; matches the component form `P^{IJ}_{KL} = δ^{[I}_Kδ^{J]}_L − (s_H/2γ)ε^{IJ}_{KL}` used in `ech_torsion_onshell_2026_08_08.md` §1.
2. **Eq. (2)**, p. 2. `L_4ψ = −(3κ/16)[γ²/(1+γ²)](J_5^I J_{5I})`. With κ = 8πG, `3κ/16 = 3πG/2`, reproducing Freidel–Minic–Takeuchi (PRD **72**, 104002) exactly. The stated bridge `4πG = κ/2` is correct.
3. **Eq. (4)**, p. 2. `G_s = −3κ/16 < 0`. Consistent with Eq. (2) at γ→∞ and with the declared direct-channel hard-cutoff mean-field NJL convention. The "no nonzero solution to the real homogeneous gap equation" statement is correct for a repulsive scalar coupling in that truncation, and is correctly hedged ("does not exclude other truncations, species structures…").
4. **Eq. (3) structure**, p. 2. `κn_ψ²` is dimensionally `energy⁴` (κ ~ E^{-2}, n² ~ E⁶). I recomputed independently: with `n_ψ = 100 cm^{-3}`, `M_Pl = 1.22089e28 eV`, `κ = 8π/M_Pl²`, one gets `κn_ψ² = 9.95e-80 eV⁴`. Matches P1C's own recorded `~1e-79 eV⁴`. (Ratio quibble → MINOR-4.)
5. **Transparency-theorem proof chain**, p. 2–3, steps (1)–(4). Zero spin density for a canonical scalar → zero source → `e^{[I}∧T^{J]} = 0` with invertible `Q_γ` → trivial kernel for invertible tetrad → `T^I = 0` → Levi-Civita → Holst term `½ε^{μνρσ}R_{μνρσ}(Γ̊)` vanishes pointwise by the **first (algebraic) Bianchi identity** `R_{μ[νρσ]} = 0`. Correct, and the explicit disclaimer that this is a **single-curvature** identity distinct from the two-curvature Pontryagin `RR̃`, with no total-derivative argument load-bearing, is exactly right and is the strongest writing in the Note. `E_R = E_L = ∂_η² + 2H∂_η + k²` is the correct FRW tensor operator, and the hypothesis list (γ = ±i excluded, global sectors, loops, fermion sources, non-minimal matter, dynamical Immirzi, propagating torsion) is honest and complete. The "on-connection-shell equality of local classical reduced actions — not an off-shell equality" caveat is precisely the right qualification.
6. **B8's parity count**, p. 3. `(J_5)²` = product of two axial currents = parity-**even**. Correct, and the stated logical independence from B14 (B14 requires zero spin density; B8 requires nonzero `J^5`) is a genuine disjointness, not a rhetorical one.
7. **Rank statements**, p. 4. rank 4 as densities, rank 2 modulo total derivatives, relations `O1 = O6` and `O1 = ½O4 − O2`. All three match `operator_basis_adjudication_2026_08_07.md` §2 null vectors `[1,0,0,0,0,−1]` and `[2,2,0,−1,0,0]` exactly, re-verified at finite γ. The "generating set, not a basis" framing and the explicit admission that spanning is *asserted from the construction rule, not proved by exhaustive enumeration* are correct and creditable.
8. **β/α = 1/(2γ) and "tensor irrep vanishes identically"**, p. 2. Both confirmed against `ech_torsion_onshell_2026_08_08.md` §3–§4 (`[L10]`, `[L11]`, `[L13]`, `[L20]`). The value is right. (Its *presentation* → MINOR-1; its sign-convention dependence → MINOR-2.)
9. **f_NL = −35/16**, p. 4. Matches the post-v110 corrected programme value. Not the superseded −35/8.
10. **Bibliography integrity.** All 18 cited keys are defined; no undefined citations; every published reference carries a DOI and/or arXiv ID and resolves. Author/journal/volume/page for Popławski, Freidel–Minic–Takeuchi, Shapiro–Teixeira, Benedetti–Speziale, Eskilt–Komatsu, Minami–Komatsu, Diego-Palazuelos–Komatsu, Mercuri all check out.
11. **Scope disclaimers.** The Intro's "channel-level assessment … not an operator-level completeness theorem", the abstract's closing "No ECH dark-energy or birefringence prediction is made", Table II's evidentiary tiering, and the B5/B6/B7/B10/B13-are-naturalness and B9-is-heuristic admissions are all present and honest. This is a manuscript that mostly declares its own weaknesses.

---

## MAJOR findings

### MAJOR-1 [correctness] — Sec. VI reintroduces the pre-erratum `O1 = O6 = 0` physics and contradicts itself within a single paragraph

**Anchor:** PDF **p. 4, right column**, Sec. VI ¶2 (rendered at 300 DPI and read verbatim); `main.tex:517–521`.

The Note prints:

> "On the on-shell ECH branch the single-curvature pair (O1, O6) vanishes by the algebraic Bianchi identity on the torsion-free connection, exactly as in Sec. III"

and, five lines earlier in the same paragraph, classifies "O1=O6 on the torsion-free branch" inside the **exact-total-derivative** class.

This is wrong on the ECH branch, and the paragraph refutes itself:

- The **on-shell ECH branch has nonzero torsion** — the Note establishes this itself on p. 2 (`α ≠ 0`, `β ≠ 0` at every finite γ) and restates it two sentences later on p. 4 ("the finite-γ ECH torsion carries a genuine trace-vector irrep … so O4 is nonzero"). A connection with nonzero torsion is **not** torsion-free, so `R_{μ[νρσ]} = 0` does **not** apply. The Sec. III Bianchi vanishing is valid only on the **zero-spin, torsion-free** branch of the transparency theorem — a different branch entirely, defined by zero spin density.
- The Note's **own** printed relation `O1 = ½O4 − O2`, combined with the Note's **own** printed conclusion `O4 ≠ 0`, forces `O1 = ½O4 − O2 ≠ −O2`, i.e. O1 is a total derivative **plus** a nonvanishing Fierz-closed contact term. Asserting `O1 = O6 = 0` on the same branch on which `O4 ≠ 0` is algebraically inconsistent with an equation printed 12 lines above it.

**Evidence checked:** `operator_basis_adjudication_2026_08_07.md`, 2026-08-08 ERRATUM ADDENDUM, "SCOPED to the γ→∞ Einstein–Cartan branch": *"On the ECH branch `O1 = O6 = −O2 + ½O4`, so O1 and O6 are **not** exact total derivatives and their Final entries are **not** zero."* Also `ech_torsion_onshell_2026_08_08.md` §7 item 3: the claim *"O4^[4] = 0 gives O1^[4] = O6^[4] = −O2^[4] exactly, so they … contribute zero to the equations of motion and zero to the vacuum energy"* is flagged **"false on the ECH branch"**, with the correct statement given as `O1^[4] = O6^[4] = −O2^[4] + ½O4^[4]`.

**This correction was already made in the source.** `arxiv/paper1c_nogo_survey/main.tex:343–347` records: *"(3) O1 = O6 = −O2 + (1/2) O4 on shell: O1 and O6 are NOT exact total derivatives on the ECH branch … (4) Disposal classes restated: (i) = {O2, O3}; (ii) = {O5, O4, and the O1 = O6 remainder}; (iii) = {O1, O6 on the torsion-free branch}."* The merge into the Note lost it. P1C's Sec. IV A carried the identical defect as R13 MAJOR-1 and it was closed at v1C.0.16 (commit `2d445855`); the Note is a **regression** against a closed finding.

**Fix (no physics change):** replace the sentence with — *"On the torsion-free branch (O1, O6) vanish by the algebraic Bianchi identity, exactly as in Sec. III. On the on-shell ECH branch `O1 = O6 = −O2 + ½O4`, an exact total derivative plus a Fierz-closed `M_Pl^{-2}`-suppressed contact term, so O1 and O6 join O4 and O5 in disposal class (ii)."* The no-go is untouched: the remainder is the same `(J⁵·J⁵)` structure at the same Planck power.

---

### MAJOR-2 [correctness] — the printed `O5^{[4]}` is the γ→∞ value, and the Note simultaneously carries both of P1C's two mutually-inconsistent normalizations

**Anchor:** PDF **p. 4, right column**; `main.tex:513–515` — `O5^{[4]} = −(3/2)κ(J⁵·J⁵)`, printed unqualified as "the surviving vacuum-energy content".

Two distinct defects at one site.

**(a) Wrong branch.** `ech_torsion_onshell_2026_08_08.md` §7 item 4: *"O5's reduction `−(3/2)κ(J⁵·J⁵)` is the γ→∞ value; the ECH value is `−(3/2)κγ²/(1+γ²)(J⁵·J⁵)` (READING-II) `[L39]`."* Printing the Einstein–Cartan limit unqualified is doubly awkward here, because the **entire point** of the surrounding paragraph is that the γ→∞ reading is the error being corrected. At the physical γ ≈ 0.2375, `γ²/(1+γ²) ≈ 0.053` — the printed value is ~19× the ECH one.

**(b) Two normalizations in one Note.** `ech_torsion_onshell_2026_08_08.md` §5 establishes that P1C fixed the same object twice, inconsistently, differing by a **factor 2 in torsion amplitude (factor 4 in any quadratic-in-T density)**:
- READING-I (App. E / FMT anchor): the eliminated-torsion operator equals `L_4ψ = −(3κ/16)[γ²/(1+γ²)](J⁵·J⁵)`, fixing `λ = ±1` `[L27]`,`[L28]`. Under READING-I, `O5^{[4]} → −3κ` at γ→∞ `[L33]`.
- READING-II (Sec. II literal anchor `T = κS`): fixes `λ = −1/2` `[L29]`. Under READING-II, `O5^{[4]} → −(3/2)κ` `[L39]`.
- `λ_I/λ_II = 2` `[L30]`. The audit calls this *"a real internal inconsistency in P1C."*

The Note's **Eq. (2)** is verbatim READING-I. The Note's **`O5^{[4]} = −(3/2)κ`** is verbatim READING-II. Both appear within two pages, with no normalization statement anywhere in the manuscript.

P1C **fixed this** at v1C.0.16 (`main.tex:351–353`): *"CONVENTION FIXED: Sec. II's T = kappa S and App. E's Eq. (E2) normalizations differed by a factor two in torsion amplitude. The survey now uses ONE normalization throughout — Eq. (E2)'s."* The Note reimports the pre-fix pair. This is the second regression against a closed P1C item.

**Fix:** state the normalization once (adopt Eq. (E2)/READING-I, as P1C v1C.0.16 did), and print `O5^{[4]} = −3κ γ²/(1+γ²)(J⁵·J⁵)` in that normalization — or keep `−(3/2)κ` and explicitly label it "(READING-II normalization, γ→∞ limit)". Do not carry both silently.

---

### MAJOR-3 [correctness / completeness] — the operator-completeness claim drops the R13-M3 closure: `O5` is parity-EVEN off shell, and the one genuinely P-odd ε-free density is neither enumerated nor disposed of

**Anchors:** PDF **p. 4, right column** (construction rule, `main.tex:497–503`); **p. 5** Conclusions (`main.tex:561–563`); abstract p. 1.

The Note's construction rule reads "zero additional derivative order, **parity-odd ε contraction**, full index contraction to a scalar density, and mass dimension exactly four", and the Conclusions claim the rank-four spanning list "**shows this conclusion is not an artifact of an incomplete operator basis**."

Two problems, both established and **closed** in P1C v1C.0.16 (R13 MAJOR-3, disposition GENUINELY-NEW-REAL, closed by scoping at commit `2d445855`), and both absent from the Note:

**(a) `O5` is parity-even off shell, so "one ε" ≠ "parity-odd".** `O5^{[4]} = ε^{μνρσ}T^I{}_{μν}e_{Iρ}J^5_σ`: `ε` contracted with the true tensors `T` and `e` gives a pseudo-vector in σ; contracted with the pseudo-vector `J^5_σ` this is pseudo × pseudo = **parity-even**. This is the identical count P1C's own App. B performs for `∂_μϑ_NY J^{5μ}`. `O1, O2, O3, O4, O6` each carry one ε and zero axial factors and are genuinely P-odd; `O5` — the one member the Note calls "the surviving vacuum-energy content" — is the sole exception. So the list is the **ε-contracted** sector, not the parity-odd sector, and the abstract's "six-member spanning list of dimension-four **parity-odd** local densities" mislabels it.

**(b) The genuinely P-odd, ε-free, exactly-dimension-4 density is missing.** `V·J⁵ ≡ T^a{}_{ab}J^{5b}`. `T^a{}_{ab}` is a true vector; contracted with the axial `J⁵` it is a genuine pseudoscalar. Dimensions: `[T] = +1`, `[J⁵] = +3` ⇒ exactly 4, dimensionless Wilson coefficient — same footing as O3 and O5. It is local, Lorentz- and diffeo-invariant, built only from the Note's own admitted blocks, and **cannot** be a combination of `{O1–O6}`, all of which carry an ε. It is excluded by the ε requirement in the rule and never mentioned. On shell it is **nonzero**: P1C v1C.0.16 Eq. `vj5_onshell` (`main.tex:2132–2136`) gives `T^a{}_{ab}J^{5b} = 3β(J⁵·J⁵)` with `β = κγ/[4(1+γ²)]`.

**The no-go survives** — `V·J⁵` is the same Fierz-closed `(J⁵·J⁵)` structure at the same `M_Pl^{-2}` power as O4 and O5. But as printed, a 6-page Note whose stated purpose in Sec. VI is to answer *"whether the conclusion survives the full local operator space"* has a known one-operator gap it does not disclose, while its Conclusions assert the conclusion "is not an artifact of an incomplete operator basis."

**Fix (P1C v1C.0.16's own option (b), one sentence + one equation):** state the rule as "one spacetime ε contraction" and drop "parity-odd" from the rule itself; note that `O5` is P-even off shell by the pseudo × pseudo count; and either exhibit `V·J⁵ = 3β(J⁵·J⁵)`, `β = κγ/[4(1+γ²)]` — which *strengthens* the "every member is disposed of" statement, since it lands in class (ii) — or add "ε-free parity-odd densities such as `T^a{}_{ab}J^{5b}`, covered by the same Fierz closure" to the disclosed exclusions.

---

### MAJOR-4 [evidential strength / positioning] — the Popławski identification is exact only in the Einstein–Cartan limit, and "the same sign" has no convention bridge

**Anchors:** abstract p. 1 ("the same mechanism that produces Popławski's torsion-induced avoidance of gravitational singularities"); Intro p. 1 ("This is the same contact term this Note derives below, **and the same sign**"); Sec. II p. 2 ("This is Popławski's torsion-bounce interaction restricted to minimal coupling: … generated by the **identical** elimination … and carries the **same repulsive sign**"); Conclusions p. 5 ("**algebraically identical** to the mechanism underlying Popławski's torsion-avoided singularity"); title.

This identification carries the title, the abstract's framing, and the whole "positive result" half of the Note's dichotomy. As stated it is stronger than what the Note itself establishes.

**(a) Exact only as γ→∞.** Popławski's black-hole cosmology (`arXiv:1007.0587`, `1102.5667`) is **Einstein–Cartan** — no Holst term, γ→∞, Hehl–Datta contact term, **purely axial** on-shell torsion. The Note establishes, 15 lines after the identification claim and on the authority of ref [9], that at finite γ the ECH on-shell torsion carries a **trace-vector irrep that Einstein–Cartan does not have**, and that "purely-axial … holds only in the strict Einstein–Cartan limit γ→∞, **not at the finite physical γ used elsewhere in this programme**." Furthermore the coefficient carries `γ²/(1+γ²)`, which at the LQG value γ = 0.2375 is ≈ 0.053 — a factor ~19 below the Einstein–Cartan magnitude the Note itself flags as "the maximal magnitude." And per `ech_torsion_onshell_2026_08_08.md` `[L23]`, at γ = 0.2375 the trace-vector coefficient is **2.11× the axial one** — the non-Popławski piece is the *larger* of the two at the programme's own γ. So "identical elimination", "the same contact term", "algebraically identical" are true in the Einstein–Cartan limit and **false at the finite γ the Note otherwise insists on**.

**(b) "The same sign" is not verifiable as printed.** The Note fixes mostly-plus `η = diag(−,+,+,+)` and `ε_{0123} = +1`; Popławski works in the opposite signature. `J_5^I J_{5I}` flips sign under signature reversal, so the literal coefficient sign in Eq. (2) and the literal sign in Popławski's Lagrangian **cannot** both be read off without a stated bridge, even when the physics (gravitational repulsion at high spin density halting collapse) agrees. The Note supplies a careful normalization bridge for FMT (`4πG = κ/2`) and none at all for Popławski, while making a sign-identity claim only about Popławski. Separately, the physical content that produces the bounce — the negative effective energy-density correction in the modified Friedmann equation — is never exhibited; the Note identifies a Lagrangian term and asserts the bounce by citation.

**Fix:** scope the identification — *"In the Einstein–Cartan limit γ→∞, Eq. (2) reduces to the Hehl–Datta contact term that underlies Popławski's torsion-avoided singularity; at finite γ it is suppressed by `γ²/(1+γ²)` and accompanied by a trace-vector torsion irrep absent from Einstein–Cartan."* Add one sentence giving Popławski's signature and the sign map, or state the claim in signature-independent physical terms (repulsive at high spin density). Do not write "identical" or "the same sign" unqualified.

---

### MAJOR-5 [attribution] — the axial–axial contact term is the Hehl–Datta term; Hehl is not cited, and the entries are sitting unused in the Note's own `references.bib`

**Anchors:** Sec. II p. 2, Eq. (2) and its attribution; Acknowledgments p. 5; reference list pp. 5–6.

Eq. (2) is the Hehl–Datta four-fermion term — the axial–axial contact interaction obtained by eliminating Einstein–Cartan torsion for minimally coupled Dirac matter (Hehl & Datta, *J. Math. Phys.* **12**, 1334 (1971); Hehl, von der Heyde, Kerlick & Nester, *Rev. Mod. Phys.* **48**, 393 (1976)). The Note attributes it exclusively to **Popławski (2010/2011)** and **Freidel–Minic–Takeuchi (2005)** — the latter correctly for the Holst/finite-γ generalization, but neither is the origin of the term.

This is not an oversight the author lacked the material for: `references.bib` **already contains** `HehlDattaNJL1971` and `Hehl1976`, both **defined and never cited** (verified by key-set diff of `\cite{}` keys against `@entry` keys). The Acknowledgments name Popławski, Mercuri, Freidel–Minic–Takeuchi, Shapiro–Teixeira and Benedetti–Speziale; Hehl appears nowhere in the rendered document.

Related thinness for a CQG Note positioned as a *systematic* no-go on Einstein–Cartan dark energy: **18 references total**, with **no** Kibble, **no** Sciama, **no** Boehmer (whose Einstein–Cartan / torsion-cosmology and dark-energy papers are directly on the Note's stated topic), and **no** Shapiro torsion review (*Phys. Rept.* **357**, 113 (2002)) — only Shapiro–Teixeira 2014 for the one-loop anchor. A CQG referee will read an 18-item list on this topic as under-engaged with the field, and the missing Hehl attribution as a priority error.

**Fix:** cite Hehl–Datta 1971 and Hehl *et al.* 1976 at Eq. (2) (the keys already exist); add Kibble/Sciama for the foundational Einstein–Cartan formulation and at least one Boehmer and the Shapiro review for the torsion-cosmology and torsion-phenomenology context.

---

### MAJOR-6 [evaluability] — Secs. IV–V, the bulk of the claimed contribution, cannot be verified from this Note plus public sources; the load-bearing sources are mutable GitHub URLs and an explicitly non-peer-reviewed deposit

**Anchors:** Sec. IV pp. 3–4 (B1–B14); Sec. V p. 4 (Routes 2–4); Data & Code Availability p. 5; refs [6], [7], [9], [15], pp. 5–6.

This is the finding that decides the verdict. Taking the four review dimensions in turn for the **fourteen barriers** and **Routes 2–4**:

**The barriers are unverifiable.** Each of B1–B14 is compressed to a single declarative sentence with no derivation, no defining inequality, and no intermediate step. The quantitative content — `g_eff ~ H_0/M_Pl ~ 10^{-61}`, the `10^{-122}` hierarchy, disformal couplings `O(10^{-122})` at `H_0`, `N_tot ≈ 92–94` e-folds, `(ρ_crit/ρ_Pl)² ≃ 0.07–0.17` — is asserted, never computed. A referee cannot check a single one of them from this document. The one exception is **B14**, which is Sec. III and is genuinely verifiable here.

**Routes 2–4 are partially traceable, not verifiable.** The anchors Shapiro–Teixeira (CQG **31**, 185002) and Benedetti–Speziale (`arXiv:1111.0884`) are public and correctly cited, but the **budget arithmetic** that turns them into "≳58 orders of suppression margin" and "61–67 orders below `ρ_Λ,obs`" appears nowhere in the Note. A referee can confirm the input papers exist; he cannot confirm the numbers.

**Where the missing content lives, and why that is not acceptable.** The Note's sole pointer for all of it is **ref [7]**, which is:
- a **bare GitHub tree URL** — `https://github.com/Hubify-Projects/bigbounce/tree/main/arxiv/paper1c_nogo_survey` — with **no DOI, no Zenodo deposit, no frozen commit hash**, i.e. a **mutable directory on a moving branch** that can change under the referee between submission and report; and
- declared by the Note itself to be a "**repository draft superseded by this Note** … **not independently submitted**."

So the Note asks CQG to accept fourteen barriers and four route closures on the authority of a manuscript that (i) will never be published, (ii) has never been refereed, and (iii) is not even archivally frozen.

The same problem, sharper, for **Sec. VI**: the entire finite-γ correction — the trace-vector irrep, `β/α = 1/(2γ)`, `O4 ≠ 0`, rank 4 / rank 2 — rests on refs **[9]** and **[15]**, both `blob/main/...` URLs with **no DOI and no commit pin**. These are the two most load-bearing citations in the Note's most technical section, and both are mutable files.

And for the **sole Tier-I result**: Sec. III ends "A full self-contained statement and second-order Holst-term verification is carried in the archived companion [6]" — ref [6] being a Zenodo deposit whose own bibliography note reads "**not an arXiv preprint and not peer reviewed**". The Note's one rigorous theorem defers its full statement and its verification to a non-refereed deposit. Sec. II does the same for the regulated NJL derivation ("the full regulated derivation is carried in the archived companion [6]").

**Status in the programme record:** this is R13's open MINOR-6 (*"the load-bearing correction rests on artifacts that are not yet archivally frozen"*) plus the pre-submission checklist item *"refereed-companion gate for cited-only companion results"* — both listed under **"Explicitly OPEN — carried to R14"** in `P1C_v1C.0.15_truth_audit.md`. They were **carried, not dropped**, but they were also not addressed before the merge, and the merge makes them materially worse: P1C at 25 pp carried its own derivations, so the deferrals were supplementary. The Note at 6 pp carries none of them, so the deferrals are now **load-bearing**.

**Fix (minimum for CQG):** (i) mint a version DOI (Zenodo) for the P1C survey and for the two theory-audit artifacts, and cite those DOIs rather than `tree/main` and `blob/main` URLs — or at minimum pin every GitHub URL to a commit SHA; (ii) bring enough of the barrier arguments back in-paper that each is checkable (see the page-budget statement below); (iii) either submit P1A/P1C so the deferrals point at refereed work, or reduce the Note's claims to what it carries itself.

---

## MINOR findings

**MINOR-1 [presentation/correctness] — as printed, the stated proportionalities give `β/α = 1/γ`, not `1/(2γ)`.** p. 2, `main.tex:186–191`: "an axial part with coefficient `α ∝ γ²/(γ²+1)` and a trace-vector part with coefficient `β ∝ γ/(γ²+1)`, ratio `β/α = 1/(2γ)`". A referee reading two `∝` symbols as carrying a **common** constant divides them and gets `1/γ`. The factor 2 lives in constants the Note suppresses: per `ech_torsion_onshell_2026_08_08.md` §4, `α_E2 = −4πGγ²/(1+γ²)` and `β_E2 = −2πGγ/(1+γ²)`, whence `β/α = 1/(2γ)`. **The stated value is correct; the derivation as printed is not.** Fix: print the constants explicitly, or give the ratio alone without the two `∝` statements.

**MINOR-2 [correctness] — `β/α` is Holst-sign-convention dependent and no Holst sign convention is stated.** p. 2. The audit's result is `β/α = s_H/(2γ)` `[L10]`,`[L13]`, computed under **both** conventions `s_H = ±1` `[L46]`,`[L47]`. The Note fixes signature and `ε_{0123}` but never fixes `s_H`, so its unsigned `1/(2γ)` silently selects `s_H = +1`. One clause fixes this.

**MINOR-3 [presentation] — the correction's actual size is understated.** p. 2. The Note says the trace-vector irrep exists; it does not say that at the programme's own γ ≈ 0.2375 the trace-vector coefficient is **2.11×** the axial one (`[L23]`; 1.82× at γ = 0.274). As written a reader takes the trace-vector for a small correction to a dominantly axial torsion. It is the larger piece.

**MINOR-4 [numeric] — Eq. (3)'s prefactor is inconsistent with the Note's own `ρ_Λ,obs`.** p. 2. The Note states `ρ_Λ,obs ≈ (2.25 meV)⁴` (p. 1). I recomputed `κn_ψ²/ρ_Λ` at `n_ψ = 100 cm^{-3}`: **3.88e-69** with 2.25 meV; **3.62e-69** with 2.29 meV. The printed `3.6×10^{-69}` corresponds to ≈2.29 meV, not the 2.25 meV the Note prints. An 8% discrepancy that changes nothing about "≈68 orders", but a referee who checks will find the paper's two numbers do not match each other. (P1C carries this as a known flag: `main.tex:95`, "benchmark rho_Lambda normalization flag (3.6 vs 3.9e-69)".) Fix: use one `ρ_Λ` value.

**MINOR-5 [evaluability] — `ρ_crit` is never defined and collides with standard usage.** B12, p. 3: `Ω_GW^ECH ≲ (ρ_crit/ρ_Pl)² ≃ 0.07–0.17`. `ρ_crit` appears nowhere else in the Note and, unqualified, reads as the **cosmological critical density**, for which `(ρ_crit/ρ_Pl)²` is ~`10^{-244}`, not 0.07–0.17. The intended object is the **LQG bounce critical density**, and the window is `ρ_crit/ρ_Pl ≃ 0.27–0.41` (P1C `main.tex:1041`; `0.27² = 0.073`, `0.41² = 0.168` — the printed endpoints). The defining window was dropped in the merge. Fix: give the ratio window inline, or rename to `ρ_bounce`.

**MINOR-6 [presentation] — Table I's "Src." column has no legend anywhere in the Note.** p. 3. The column carries bare letters `A, B, C, D, E, F, G, H, J, L, M, N/O`, and the prose tags read "[R1, Founds. A–B]", "[R2, Branch J]", "[R3, Branch L/M]". Nothing in the Note says what any letter denotes, and the sequence skips I and K, so it cannot be reconstructed by inspection. A reader can infer only that A–G are the seven foundations and H,J,L,M,N,O the six branches. As printed, an entire table column is unreadable. Fix: one caption clause naming the foundations and branches, or drop the column.

**MINOR-7 [consistency] — "closed operator-level" contradicts the Note's own Table II and P1C's Tier-II record.** p. 4, Sec. V: Route 2's "dark-energy leg is **closed operator-level** for constant Nieh–Yan coefficient". Table II (p. 5) records that same leg as **(II) structural argument**, and P1C v1C.0.16 (`main.tex:1400–1408`, `1792–1797`) is explicit that the step to "R2 sources no dark energy" is **Tier-II** because it *"inherits the unproved spanning assertion"*, adding *"No dark-energy amplitude is computed for Route 2 anywhere in this survey, and none is claimed."* Fix: "closed at the operator level modulo the spanning assertion (Tier-II)".

**MINOR-8 [presentation/reproducibility] — the three Data-and-Code links are typographically indistinguishable and float away from their own introduction.** p. 5, verified on the 300-DPI render. The `\artifact{}` macro is `\href{...}{repository artifact}`, so all three scripts — `dim4_parityodd_enumeration.py`, `operator_basis_adjudication_2026_08_07.py`, `ech_torsion_onshell_2026_08_08.py` — render as three identical lines reading "repository artifact", with **no filename visible anywhere in the rendered document**. Worse, the centered block floats to the **top of the right column**, above and detached from the sentence that introduces it, so the introducing colon at the foot of the left column points at nothing. A print reader, or any referee who does not hover the PDF, cannot tell which script is which or that there are three distinct ones. Fix: print the filenames as link text (`\href{URL}{\texttt{filename}}`) and place the list inline, not in a floating `center`.

**MINOR-9 [packaging] — `references.bib` ships ~100 unused entries inherited from the source manuscripts.** Key-set diff: 18 cited, ~118 defined; the unused set includes `DESI2024`, `Planck2018params`, `Riess2022`, `Shamir2012/2022/2024`, `Cobaya2021`, `Feroz2009`, etc. No compile impact (bibtex emits only cited keys), but the arXiv tarball must ship a pruned `.bbl`/`.bib`. Also note `Hehl1976` and `HehlDattaNJL1971` sit in this unused set — see MAJOR-5.

**MINOR-10 [presentation] — `β_obs` is quoted without its detection significance.** p. 4, Route 4: `β_obs = 0.342° ± 0.094°` and ACT DR6 `0.215° ± 0.074°` are presented as "the WMAP+Planck birefringence signal" with no significance and no caveat. P1C carries both (`main.tex:1642`: ≈3.6σ / 2.9σ, *"indications rather than established detections"*). A CQG referee will object to a `~3σ` indication being called a signal. Fix: restore the significances and the one-clause caveat.

---

## Candidates raised and WITHDRAWN after ≥300-DPI re-render or `.tex` grep

Recorded so the board does not re-litigate them:

1. *"Eq. (1)'s Holst weight `2/γ` is inconsistent with `Q_γ = ⋆ + γ^{-1}𝟙`."* **Withdrawn.** `(1/4κ)(ε_IJKL + (2/γ)η_{I[K}η_{L]J}) = (1/2κ)(½ε + γ^{-1}ηη)`; `⋆(e∧e)^{IJ} = ½ε^{IJ}{}_{KL}e^K∧e^L`. Consistent.
2. *"Eq. (2)'s `3κ/16` disagrees with FMT."* **Withdrawn.** `3κ/16 = 3πG/2` at `κ = 8πG`, matching FMT Eq. (23) exactly. The stated bridge `4πG = κ/2` is correct.
3. *"`G_s = −3κ/16 < 0` described as repulsive contradicts Eq. (2) also being called repulsive."* **Withdrawn.** Same sign, same object; the dichotomy (repulsion halts collapse **and** repulsion forbids a condensate) is coherent and is in fact the Note's cleanest idea.
4. *"`f_NL = −35/8` stale value."* **Withdrawn.** p. 4 prints `−35/16`, the corrected programme value, verified on the render.
5. *"Overfull hboxes / column escapes / undefined references."* **Withdrawn.** Independent clean-directory 4-pass recompile: 6 pages, **0** Overfull, **0** undefined reference, **0** undefined citation. Presentation is mechanically clean; the defects are MINOR-6 and MINOR-8, both semantic rather than typesetting.
6. *"`(J_5)²` parity-even claim in B8 is wrong."* **Withdrawn.** Product of two axial currents is P-even; correct. (The related P-parity issue is about `O5`, not `(J_5)²` — see MAJOR-3(a).)
7. *"Transparency theorem's all-orders claim requires an order-by-order verification it does not present."* **Withdrawn.** The Note explicitly and correctly states that the all-orders content follows from the algebraic Cartan constraint plus the pointwise Bianchi identity, *"not an order-by-order calculation."* That is the right argument.

---

## Is 6 pages adequate?

**No.** The page budget is the mechanism that produced MAJOR-1, MAJOR-2, MAJOR-3 and MAJOR-6: all four are losses sustained in compressing a 25-page survey plus a full companion paper into 6 pages, and three of them are regressions against corrections the source manuscripts had already made.

There are two honest resolutions, and the current draft is neither.

**Option A — restore the content and accept it is a Paper, not a Note (~12–16 pp).** What must come back:

| From | What | Why |
|---|---|---|
| **P1C** Sec. V / App. A / Table III | The disposal-class table with **on-shell ECH** entries for O1, O4, O5, O6 and the `V·J⁵` companion, under **one** stated normalization | Fixes MAJOR-1, MAJOR-2, MAJOR-3 at the root; Sec. VI's 400 words cannot carry a corrected operator argument |
| **P1C** Sec. III / Founds. A–G, Branches H–O | The defining inequality or one-paragraph derivation behind each of B1–B14, plus the foundation/branch legend | Fixes MAJOR-6 and MINOR-6; a fourteen-item table of one-line assertions is not refereeable |
| **P1C** Route 2/3 budget arithmetic | The steps producing "≳58" and "61–67 orders", and the LQG `ρ_crit/ρ_Pl ≃ 0.27–0.41` window | Fixes MAJOR-6 and MINOR-5 |
| **P1A** transparency appendix | The boundary/falloff conditions and the explicit second-order Holst-term verification | The Note's **sole Tier-I result** currently defers its own proof to a non-refereed deposit |
| **New** | Hehl–Datta/Hehl *et al.* attribution; a γ→∞ scoping clause and signature bridge for the Popławski identification | Fixes MAJOR-4 and MAJOR-5 |

**Option B — keep 6 pages and cut to what the Note can actually carry.** Publish only Sec. II (the contact term, correctly scoped to γ→∞ against Popławski) plus Sec. III (the transparency theorem, self-contained with its proof) — a genuine, verifiable, appropriately-sized CQG Note whose Tier-I result stands on its own. **Delete** Secs. IV, V and VI, and submit P1C separately as the survey it is. This is clean, but it requires reversing the Note's declaration that P1C is "not independently submitted" — a portfolio decision, not a referee's.

I note for the record that the Note's current structure is the worst of the two: it makes the strong claims of Option A (fourteen barriers, four routes, operator completeness, "not an artifact of an incomplete operator basis") on the page budget of Option B, and forecloses the separate publication that would let a referee check them.

---

## Novelty and positioning for CQG

Assessed against Popławski, Freidel–Minic–Takeuchi, Shapiro, Hehl *et al.*:

- **Eq. (2)** is Freidel–Minic–Takeuchi (2005) Eq. (23); at γ→∞ it is the Hehl–Datta (1971) term. **Not new**, and correctly presented as a derivation rather than a discovery — except for the attribution gap (MAJOR-5).
- **The transparency theorem (Sec. III)** is the Note's real contribution. That the Holst term does nothing without spin sources is folklore; stating it as an **all-orders classical statement** with an explicit hypothesis list, deriving it from the algebraic Cartan constraint plus the pointwise algebraic Bianchi identity, and explicitly distinguishing the single-curvature identity from the two-curvature Pontryagin density and from any total-derivative argument — that is a modest but genuine and cleanly-executed sharpening, and it is the one part of the Note a referee can fully verify. It is publishable.
- **The barrier catalog** is the Note's claimed systematic contribution and is where CQG novelty would live, but at one sentence per barrier it reads as an index to unpublished work rather than as a result (MAJOR-6).
- **The dichotomy framing** — one algebraic elimination read in two directions, positive for the bounce and negative for dark energy — is genuinely good and is the right organizing idea for a Note. It is undercut by MAJOR-4: the "positive" half is asserted by citation and holds exactly only in a limit the Note elsewhere disavows, so the Note's title promises a positive result it does not derive.

**Positioning risk:** as submitted, a CQG referee sees a Note whose negative half he cannot check and whose positive half is someone else's published result. That is the gap the revision must close.

---

## Verdict

**MAJOR REVISIONS.**

The Note is honestly written, mechanically clean (6 pp, 0 overfull, 0 undefined refs, all 18 citations resolving), unusually disciplined about tiering its own evidence, and contains one genuine, verifiable, publishable result — the perturbation-transparency theorem of Sec. III, whose proof strategy and hypothesis list I checked and found correct. I found **no fabricated result**: every value I traced reproduces its source. But it cannot be accepted in this form. Three of its six MAJORs (M1, M2, M3) are **regressions** — the merge from P1A and P1C v1C.0.16 silently reverted the on-shell branch correction (`O1 = O6 = −O2 + ½O4`, not zero), reimported the factor-2 normalization split that v1C.0.16 had explicitly fixed, and dropped the R13-closed operator-completeness scoping (`O5` P-even; the ε-free `V·J⁵` companion) — so the 6-page Note is, on precisely the technical points it exists to correct, **less accurate than the 25-page survey it supersedes**. M4 states the Popławski identification, which carries the title and abstract, above its evidential strength: "identical" and "the same sign" hold in the Einstein–Cartan limit, whereas at the programme's own γ ≈ 0.2375 the coefficient is suppressed ~19× and the non-Popławski trace-vector piece is 2.11× the axial one, with no signature bridge offered. M5 omits the Hehl–Datta attribution for the Note's central equation, with the bibliography entries already present and unused. M6 is decisive for the venue: the fourteen barriers and Routes 2–4 — the bulk of the claimed contribution — are one-line assertions whose only source is a **mutable, DOI-less GitHub tree** for a manuscript the Note declares will never be submitted, while the sole Tier-I result defers its own full statement to a deposit labelled "not peer reviewed." Every one of these is fixable, none requires new physics, and the underlying no-go conclusion survives all six corrections unchanged. But the fix for M6 is not editorial: either substantial content returns from P1A and P1C and this becomes a ~12–16-page Paper, or Secs. IV–VI are cut and P1C is submitted on its own. Six pages is not adequate for what this manuscript currently claims.
