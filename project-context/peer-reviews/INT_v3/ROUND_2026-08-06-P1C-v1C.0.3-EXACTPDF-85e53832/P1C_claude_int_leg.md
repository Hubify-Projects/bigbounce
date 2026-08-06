# P1C v1C.0.3 — Claude INT leg, raw referee report

- **Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf` — "A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and Bounce Phenomenology" (dated August 6, 2026, v1C.0.3), 16 pages.
- **SHA-256 (verified before reading):** `85e5383298625013cc41a80b5bedfc4bc4464315e946acb1a319432b8c665863` — MATCH.
- **Date of review:** 2026-08-06.
- **Role:** Independent skeptical journal referee (CQG/PRD calibre), Claude INT leg of the first full review board on this manuscript. No prior review of this paper assumed or consulted. Companion sources consulted read-only for cross-paper consistency (`arxiv/paper1a_ech_nogo.tex`).
- **Method:** Full read of all 16 pages of the exact PDF. Independent hand/numerical verification of every displayed equation that is verifiable offline, including an independent Grassmann-algebra computation of the Fierz identity (Eq. B2) and an independent numerical reconstruction of the c-number Fierz matrix (Eq. B1) — not the paper's own scripts. The paper's three released verification scripts were additionally run and pass as claimed.

---

## 1. Summary of the manuscript

The paper is a structural no-go survey for minimal Einstein–Cartan–Holst (ECH) spin-torsion as a source of late-time dark energy / bounce phenomenology. Content: (i) a 14-entry (13 distinct; B8 subsumed by B14) barrier catalog spanning 7 foundation classes and 6 observational branches; (ii) amplitude-budget closures of two historical routes — R2 (one-loop graviton-sector corrections to the Holst term, anchored in Shapiro–Teixeira) and R3 (Immirzi running, bounded by an integrated Benedetti–Speziale one-loop flow); (iii) an operator-basis-completeness argument: a six-member dimension-4 parity-odd basis {O1–O6} that is topological, Fierz-basis-reducible, or Bianchi-vanishing; (iv) an explicit three-tier evidentiary classification (Table II) and scope statement (Sec. VI).

## 2. Verification ledger (what I checked by hand / independently)

**PASS — mathematical checks:**

- **Eq. (1)** dimension count: [β(γ)/M_Pl] = −1, [∂ϑ_NY] = +2, [J⁵] = +3 → integrand +4. Correct.
- **Eq. (2)** (p. 6): dimensionally consistent as displayed — H₀/M_Pl, M_Pl(α/M), β_obs are each dimensionless. Numerics: α_em/4π = 5.81×10⁻⁴ ✓; H₀/M_Pl = 1.4×10⁻⁴² GeV/1.22×10¹⁹ GeV ≈ 10⁻⁶¹ ✓; M_Pl(α/M) = 10¹⁹·10⁻²¹ = 10⁻² ✓; β_obs = 0.342° = 5.97×10⁻³ rad ✓; ratio 5×10⁻⁴·10⁻⁶¹/(10⁻²·6×10⁻³) ≈ 8×10⁻⁶¹ ≈ 10⁻⁶⁰ ✓. The ≥58 conservative margin (two-order allowance) is arithmetically consistent.
- **Eq. (3)** integration: Δγ/γ = (N_F^L−N_F^R)·ln(μ_GUT/μ_IR)/(12π²); ln 10¹⁶ = 36.84 ✓; 30/118.4–37/118.4 = 0.25–0.31 ✓; 32/(12π²) = 0.270 ✓.
- **Eq. (4)** integrated value — independently reproduced: with κ̃² = 16πG, μ_UV = 10¹⁶ GeV, γ = 0.24: μ²κ̃²/(8π)² = 5.3×10⁻⁸; (γ²−1)(23γ²+5) = −5.96; UV-endpoint-dominated integral Δγ² ≈ β(μ_UV)/2 ≈ 1.6×10⁻⁷; Δγ/γ = Δγ²/2γ² ≈ **1.4×10⁻⁶** — matches the quoted value. The power-suppression (μ/M_Pl)² structure and UV-endpoint domination claims are correct.
- **Route-3 combined suppression:** (Δγ/γ)(H₀/M_Pl) with the pessimistic 0.3 → 3×10⁻⁶² ✓; the 61–67-order range = pessimistic (0.3) vs derived (1.4×10⁻⁶) endpoints ✓ internally consistent.
- **|Ω₄₄/α₄| arithmetic** (p. 5): (81γ⁴/16(1+γ²)²)/(6/(1+γ²)) = 27γ⁴/[32(1+γ²)] ✓; at γ = 0.24 → 2.65×10⁻³ ≈ quoted 2.5×10⁻³ ✓.
- **e-fold arithmetic** (App. A): N_tot = 122 ln10/3 = 93.6 ≈ 94 ✓; 120 ln10/3 = 92.1 → the quoted 92–94 spread ✓. D_inf = 10⁻¹²²: Ξ = (α/M)M_Pl·D_inf = 10⁻²·10⁻¹²² → ρ_Λ = Ξ M_Pl⁴ ≈ 10⁻¹²⁴·2.2×10⁷⁶ ≈ 2×10⁻⁴⁸ GeV⁴ ~ ρ_Λ,obs ✓ self-consistent.
- **B12 window:** (0.27)²–(0.41)² = 0.073–0.168 ✓ matches quoted 0.07–0.17.
- **ε-contraction** (App. A1): Lorentzian ε_abcd ε^abce = −3!δ_d^e ✓; S_abc S^abc = (1/16)(−6)(J⁵·J⁵) = −(3/8)(J⁵·J⁵) ✓.
- **Eq. (B1) involution:** F² = 𝟙 verified by hand for the printed matrix ✓ (but see MAJOR-1).
- **Eq. (B2) — independently verified TRUE.** I implemented a Grassmann algebra (8 generators, ψ and ψ̄ components as anticommuting symbols, Dirac basis, η = diag(+,−,−,−)) and confirmed the operator identity for identical Dirac fields: (J⁵·J⁵) = SS + ½VV + ½AA − PP holds exactly (max residual coefficient 0.0); the two plausible sign-variant alternatives fail (residuals 6.0, 4.0). The cross-term claim that (J·J⁵) has VA = AV also verified. This is the load-bearing endpoint of App. B, and it is correct.
- **Dimension bookkeeping of {O1–O6}** (Eq. 8 / Table III): bare dims (2,2,4,2,4,2) + prefactors (M_Pl², M_Pl², 1, M_Pl², 1, M_Pl²) → all +4 ✓; O4 restoration M_Pl²κ² = κ ✓ so O4^[4] = O5^[4] = κ(J⁵·J⁵) as claimed ✓; [TeJ⁵] = 1+0+3 = 4 ✓; (A1) count −1+2 = +1 ✓.
- **Internal consistency of the catalog:** 7 foundations (B1–B7) + 7 branch entries (B8–B14) = 14; B8⊂B14 → 13 distinct ✓ consistent across abstract, Sec. III, Fig. 1, Table I, Sec. VII. Novel(9)+Known(4)+Structural(1) = 14 ✓. Route↔barrier mapping in barrier texts matches Table I "Source" column and Fig. 1 ✓. Table II tier assignments match Sec. IV C text ✓.
- **Cross-paper consistency with companion (read-only):** the quoted contact operator −(3κ/16)[γ²/(1+γ²)](J⁵)² and G_s = −3κ/16 match `arxiv/paper1a_ech_nogo.tex` (lines ~1208, 1854–1870, 4846–4854) ✓. −3κ/16 = −(3/2)πG is the standard minimally-coupled ECSK axial-contact coefficient, and the γ²/(1+γ²) Holst factor matches Freidel–Minic–Takeuchi ✓.
- **Released artifacts:** all three cited script paths exist in the repo; `arxiv/scripts/dim4_parityodd_enumeration.py` runs and passes (Check A: εR = 0 under Bianchi; Check D: −3!δ and −3/8 factor); `arxiv/scripts/fierz_lemma_check.py` runs and passes.
- **Citation spot-checks (offline):** [11] Eskilt–Komatsu PRD 106, 063503 (2022), β = 0.342°±0.094° — exact match to the real measurement ✓. [10], [5], [6], [7], [8], [9], [3], [4], [14], [15], [16], [17], [18], [19], [20], [21] all correspond to real, correctly-attributed works to the best of offline verification. [1], [13] are Zenodo self-citations honestly labeled "not an arXiv preprint and not peer reviewed."

**Not verifiable offline (flagged, not failed):** exact equation numbers and coefficients quoted from Shapiro–Teixeira (Eqs. 37, 41–42, 46, 51, 58; Ω₂₄ = 81γ²/[40(1+γ²)²]) and Benedetti–Speziale ("their Eq. 7" = Eq. 4); ACT DR6 birefringence preprint [12] (arXiv:2509.13654, β = 0.215°±0.074°). See MINOR-5.

## 3. Assessment by review dimension

**Mathematical correctness:** Very strong. Every displayed equation I could check by hand or independent computation is correct, including the two nontrivial ones (the Route-3 integrated running and the operator-level Fierz identity). One genuine displayed-math inconsistency found: the printed Eq. (B1) matrix does not compose with the stated F_op = −F_c step to give Eq. (B2) (MAJOR-1).

**Internal consistency (table vs figure vs text):** Clean. The 13-vs-14 accounting, route mapping, tier labels, and margin numbers are consistent across all surfaces. One wording overreach at the top of Sec. IV (MINOR-1).

**Completeness argument — actual strength vs claims:** The six-member basis is plausibly complete *within the stated construction rule* and the paper is explicit — repeatedly — that completeness is asserted from the rule, not proved by exhaustive enumeration. I probed for escapes: √−g ∇_μJ^5μ is a gauge-invariant, diff-covariant, dimension-exactly-4 parity-odd density of the minimal field content that is *excluded by the zero-derivative rule* yet exists; it is an exact total derivative and therefore harmless, but the paper should say so (MINOR-4). The channel-level (not operator-level) scoping is stated honestly. The heavy lifting is done by single-scale NDA (App. A) plus the companion's Tier-I results; the catalog is a taxonomy of mixed-strength arguments and says so.

**Scope honesty:** Exemplary — arguably the paper's strongest feature, to the point of excess (MINOR-3). Tier labels (Table II), the "What is not established" block, the parity-classification footnote, and the ansatz-vs-derivation distinctions are all scrupulous.

**Citation integrity:** No fabricated or misattributed citations found. The two self-citations are honestly labeled. Quoted-coefficient verification against ST/BS sources remains outstanding (MINOR-5).

**Presentation:** No overflow/layout blockers observed in the rendered pages; tables and Fig. 1 are legible. The paper is substantially longer than its content requires due to repeated hedging (MINOR-3) and a two-thirds-column footnote (MINOR-6).

---

## 4. Findings

### MAJOR

**MAJOR-1 — Eq. (B1) as printed is inconsistent with the stated derivation of Eq. (B2) and with the paper's own released verification script.** (p. 15, App. B, Eqs. B1–B2.)
The printed matrix has axial row F_A = ¼(4, 2, 0, −2, −4). Composing this with the stated anticommuting exchange F_op = −F_c yields (J⁵·J⁵) → −SS − ½VV + ½AA + PP, which is *false* (my independent Grassmann computation gives residual 6.0 for this variant). The genuine c-number exchange matrix in the basis for which −F_c reproduces Eq. (B2) has axial row ¼(−4, −2, 0, −2, 4) and single-A-channel entries of opposite sign throughout (I reconstructed the full matrix numerically: rows S,V,T,A,P = ¼[(1,1,1,−1,1),(4,−2,0,−2,−4),(6,0,−2,0,6),(−4,−2,0,−2,4),(1,−1,1,1,1)]; F² = 𝟙; −F row A = (1,½,0,½,−1) = Eq. B2 exactly). The paper's own `arxiv/scripts/fierz_lemma_check.py` prints the axial c-number row as (−1,−½,0,−½,1) — matching my reconstruction, *not* the printed B1 — so the claim that the released script "independently checks the same convention's matrix involution and axial-row coefficients" is inaccurate for B1 as printed. Both sign conventions are involutory, so F² = 𝟙 does not discriminate. Note Eq. (B2) itself is **correct** (independently verified) and nothing downstream is affected — the closure onto {SS,VV,AA,PP}, the absent tensor channel, and the preserved M_Pl⁻² prefactor are convention-independent. Fix: print the matrix in the convention actually used (flip the four single-A-channel signs), or state explicitly that the tabulated Itzykson–Zuber/Nieves–Pal form uses the opposite axial-element sign convention and give the correct composition. As it stands, a reader who checks the displayed chain B1 → (−F_c) → B2 will find it does not compose.

**MAJOR-2 — The paper's only Tier-I results rest on unrefereed companion artifacts.** (Table II; Secs. I, III, IV; refs. [1], [13].)
The two "first-principles" anchors of the entire catalog — the perturbation-transparency theorem (B14, the sole Tier-I leg) and the Route-1 torsion-elimination derivation — are established in a Zenodo-archived companion that the bibliography itself states is "not an arXiv preprint and not peer reviewed." For a CQG/PRD-calibre publication this is a structural problem: the survey's one rigorous theorem cannot be refereed from this manuscript. Since the B14 proof is described as short (T = 0 for canonical scalar matter from vanishing spin density, plus the algebraic Bianchi identity killing the Holst dual), it should be reproduced self-contained in an appendix here, or publication should be coordinated so the companion is citable as a refereed/preprinted work. The same applies to the Fierz-appendix convention inherited from [1] and to the R1 ~70-order Tier-III number imported into Table II.

**MAJOR-3 — Contribution sharpness: the decisive content is thinner than the manuscript's length and apparatus suggest.** (Secs. III–V; 16 pp.)
The load-bearing engine of every closure is the single-scale NDA argument of App. A (no light scale between M_Pl and 0) plus the companion's Tier-I results. The R2/R3 "amplitude budgets" close historical mappings that — as the paper itself states — the companion "does not retain as results," i.e., routes with no current proponent within this program; and five of thirteen barriers (B5, B6, B7, B10, B13) are general naturalness/classification arguments not specific to ECH, with B9 an explicitly heuristic ordering argument. None of this is hidden — the tier system discloses it — but disclosure does not substitute for a positive case. The paper needs (i) a crisp statement, early, of what a reader learns beyond App. A + companion (in my reading: the route↔barrier taxonomy, the O1–O6 genuine-dimension-4 closure of Sec. V/App. A1 — which is real added value — and the R3 integrated bound), and (ii) substantial condensation: the same margin numbers (≈60 / ≥58 orders) and the same completeness disclaimer are restated ≥6 times each; the manuscript could deliver its content in roughly 9–10 pages. As submitted, the ratio of hedging to theorem invites the referee question "what exactly is the publishable unit here?" — the paper should answer it in one paragraph rather than by accumulation.

### MINOR

**MINOR-1 — Sec. IV opening overstates the R2 closure metric.** (p. 5, Sec. IV first paragraph.) "…amplitude budgets demonstrating that any completion of these mappings falls short of the observed *dark-energy density* by tens of orders" — but the R2 budget (Eq. 2) is a *birefringence-angle* ratio; the density-level closure for R2 rests on App. A NDA, as correctly stated later ("Closure: amplitude-suppressed by M_Pl⁻¹…", Table II row R2). Align the section-opening sentence with the actual closure metric per route.

**MINOR-2 — Notation collisions, acknowledged but still error-prone.** α/M is used both for the R4 photon coupling (fitted 10⁻²¹ GeV⁻¹, Secs. IV C, and inside Eq. 2) and as the Sec. V basis shorthand coefficient with M = M_area-gap ~ M_Pl/√γ (Eq. 5) — two different M's and two different physical roles; β denotes both the birefringence angle and β(γ); ϑ_NY vs θ is handled by an explicit note. Recommend distinct symbols (e.g., g_φγ for the R4 coupling) rather than disambiguation-by-prose.

**MINOR-3 — Redundant hedging inflates the manuscript.** The ≈60/≥58-order margin statement appears ≥8 times; "asserted from the construction rules, not proved by exhaustive symbolic enumeration" ≥5 times; the R2 ansatz-status disclaimer ≥4 times (p. 6 alone states it three ways). Consolidate to one authoritative statement per item (feeds MAJOR-3).

**MINOR-4 — State the fate of √−g ∇_μJ^5μ.** (Sec. V construction rule; App. A1.) This is a dimension-exactly-4, parity-odd, gauge-invariant density of the minimal field content that the zero-derivative construction rule silently excludes. It is an exact total derivative and thus harmless, but since the completeness claim is rule-based rather than enumerative, the paper should dispose of it explicitly to preempt the obvious probe (and note that its anomaly content introduces F F̃ only outside the minimal field content).

**MINOR-5 — Source-verification of quoted external coefficients.** The ST equation numbers and coefficients (Eqs. 37, 41–42, 46, 51, 58; α₄ = −6/(1+γ²); Ω₄₄ = 81γ⁴/[16(1+γ²)²]; Ω₂₄ = 81γ²/[40(1+γ²)²] — note the γ² vs γ⁴ asymmetry between Ω₂₄ and Ω₄₄ should be double-checked for transcription) and the BS β-function ("their Eq. 7" = Eq. 4 including the (23γ²+5) factor) could not be verified against the source papers in this offline review. The closures are insensitive (margins ≫ any plausible transcription error), but a quoted-equation audit against the published PDFs should be on record before submission. Same for the ACT DR6 preprint [12] (number, authors, central value).

**MINOR-6 — Footnote 1 (p. 5) is ~two-thirds of a column.** The parity-classification discussion is substantive and load-bearing for the "parity-odd" terminology used throughout Route 2; promote it to a short main-text subsection or appendix.

**MINOR-7 — "in agreement with a frozen-coefficient analytic estimate to four significant figures, |Δγ/γ| ≈ 1.4×10⁻⁶" (p. 7)** — a four-significant-figure agreement claim attached to a two-significant-figure quoted value. Either quote the four figures (and the integration settings) or drop the precision claim.

**MINOR-8 — Hierarchy arithmetic rounding.** (p. 13.) M_Pl⁴/ρ_Λ,obs with M_Pl = 1.22×10¹⁹ GeV and ρ_Λ = (2.25 meV)⁴ is ≈ 8.7×10¹²² (≈10¹²³), quoted as "~10¹²²"/"~120 orders." Fine at order-of-magnitude, and the paper's own dependency statement covers it, but the "as fixed above" phrasing suggests more precision than the rounding supports; one sentence fixing the convention (10¹²² vs 10¹²³ vs "≈123") would remove the wobble against N_tot = 122 ln10/3.

---

## 5. Verdict

**major-revisions**

The mathematics that can be checked is solid — I independently verified the two nontrivial computations (the Route-3 integrated running, 1.4×10⁻⁶, and the operator Fierz identity B2) and all the displayed arithmetic — and the scope honesty is exemplary. But (i) a displayed derivation chain in App. B does not compose as printed and contradicts the paper's own verification artifact (MAJOR-1, trivial to fix but mandatory), (ii) the paper's sole Tier-I theorem lives in an unrefereed companion (MAJOR-2), and (iii) the contribution needs to be stated and sized honestly relative to its decisive content (MAJOR-3). All three are addressable without new science. With MAJOR-1 corrected, MAJOR-2 resolved by a self-contained B14 appendix, and a serious condensation pass, this becomes a publishable no-go survey.

*Claude INT leg — reviewed against exact PDF SHA-256 85e5383298625013cc41a80b5bedfc4bc4464315e946acb1a319432b8c665863, 2026-08-06.*
