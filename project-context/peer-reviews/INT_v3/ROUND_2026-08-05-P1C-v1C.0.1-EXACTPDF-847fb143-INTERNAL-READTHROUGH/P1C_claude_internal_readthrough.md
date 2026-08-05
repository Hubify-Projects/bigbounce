# P1C — Internal Referee Read-Through (Raw Report)

**Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf`
**Title:** *A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and Bounce Phenomenology*
**Version:** v1C.0.1 (dated August 5, 2026 on the title page)
**Pages:** 15
**SHA-256:** `847fb143e11fbd1e13a337531af51051e047ac076dc0047d0a238f176d838a72` (verified by `shasum -a 256` before reading; matches the assignment hash)
**Date of review:** 2026-08-05
**Role:** Independent, skeptical internal journal referee (CQG / PRD calibre), first internal read-through. No stake in acceptance. No verdict-severity steering applied in either direction.
**Read:** full PDF, all 15 pages, plus (read-only, for consistency checking) `arxiv/paper1c_nogo_survey/main.tex`, `arxiv/paper1c_nogo_survey/main.log`, `arxiv/paper1c_nogo_survey/references.bib`, `arxiv/scripts/fierz_lemma_check.py`, `arxiv/scripts/dim4_parityodd_enumeration.py`, `arxiv/main.tex` (v2.3.18 monolith), and `arxiv/paper1a_ech_nogo.tex` (v1A.0.127 — the source that actually carries the title given in Ref. [1]).

---

## 1. Summary assessment

This is a competently organized survey with an unusually candid self-assessment apparatus: the three-tier evidentiary ladder (Table II), the explicit "What is not established" subsection (§VI), and the repeated insistence that the result is *channel-level, not operator-level* are all good practice and above the field average for this kind of paper. Several of the load-bearing quantitative results check out exactly when recomputed by hand (see §2 below), including the Route-3 integration, which I reproduced to the quoted precision.

However, the manuscript cannot be accepted in its current state. There is one hard presentation blocker (Fig. 1 and the barrier list physically overprint the adjacent column, with visible text corruption on p. 4), one wrong displayed equation whose own released "verification" script contradicts it (Eqs. B2/B3 vs Eq. B1), a symbol used with two mutually inconsistent definitions (κ), a headline suppression figure that cannot be reconstructed from the paper's own inputs and that the abstract then overstates, and — most consequential editorially — substantial duplication of the DOI-archived companion paper's Section and two Appendices, together with a direct contradiction of that companion's own stated position on the Route-2/Route-3 mappings.

**Verdict: major-revisions.** Not reject: the core physics that I could check independently is sound, the scoping discipline is genuine, and every one of the findings below is fixable without new science. Not minor-revisions: M1 is an editor bounce on sight, M2 is a wrong equation in a load-bearing appendix, and M7/M8 raise a duplicate-publication question that an editor will put to the author before sending the paper out.

---

## 2. What I checked and found CORRECT

Recorded so the author can see the boundary of the negative findings, and so a later round does not re-litigate settled ground.

- **Eq. (1) dimensional bookkeeping (p. 5).** With `[ϑ_NY] = +1`, `[∂_μ ϑ_NY] = +2`, `[J^{5μ}] = +3`, and the prefactor `β(γ)/M_Pl` at `−1`: `−1 + 2 + 3 = +4`. The action is dimensionless. Correct as stated.
- **Eq. (2) (p. 5).** The two displayed lines are algebraically equivalent. `α_em/(4π) = (1/137.04)/12.566 = 5.81 × 10⁻⁴`, so the paper's "≈ 5 × 10⁻⁴ (more precisely 5.8 × 10⁻⁴)" is right. `β_obs = 0.342° = 5.97 × 10⁻³ rad` is right.
- **§II contact term.** `−(3κ/16)[γ²/(1+γ²)](J⁵)²` with `κ = 8πG` is exactly the standard minimal-ECH axial-axial coefficient `−(3/2)πG γ²/(1+γ²)(J⁵)²` (Perez–Rovelli / Freidel–Minic–Takeuchi class result). Verified by substitution.
- **Spin-current contraction (pp. 10, 13).** From `S^{abc} = ¼ ε^{abcd} J⁵_d` and the Lorentzian `ε_{abcd} ε^{abce} = −3! δ^e_d`: `S_{abc}S^{abc} = (1/16)(−6)(J⁵·J⁵) = −(3/8)(J⁵·J⁵)`. Correct, and independently reproduced by `dim4_parityodd_enumeration.py` (its CHECK D).
- **Eq. (4) numerical integration (p. 6) — the single most load-bearing number in §IV, and it holds.** Frozen-coefficient evaluation at `γ = 0.24` (`γ² = 0.0576`): `(γ²−1)(23γ²+5) = (−0.9424)(6.3248) = −5.961`, so `dγ²/d ln μ = +5.961 μ²κ²/(8π)²`. With `κ² = 16πG = 3.372 × 10⁻³⁷ GeV⁻²`, `(8π)² = 631.65`, and `∫μ² d ln μ = μ_UV²/2 = 5 × 10³¹ GeV²`: `Δγ² = 1.59 × 10⁻⁷`, hence `|Δγ/γ| = Δγ²/(2γ²) = 1.38 × 10⁻⁶`. The paper's **1.4 × 10⁻⁶ is reproduced exactly**, and the quoted `(μ_UV/M_Pl)² = 6.7 × 10⁻⁷` scaling is the right order. Good.
- **`γ² = 1` as the unique physical fixed point of Eq. (4)'s bracket.** The other root `γ² = −5/23` is unphysical. Correct.
- **`32/(12π²) = 0.270`** (p. 7). Correct.
- **Eq. (A1):** `−1 + 2 = +1`. Correct. **`M_Pl⁴/ρ_Λ^obs`**: `(1.22 × 10²⁸ eV)⁴ / (2.25 × 10⁻³ eV)⁴ = 8.6 × 10¹²²`, i.e. `~10¹²²`. Correct. **`122 ln10/3 = 93.6 ≈ 94`.** Correct.
- **B1 (p. 3):** `g_eff ~ 1/(M_Pl √|t₃|) ~ m_T/M_Pl ~ H₀/M_Pl ~ 10⁻⁶¹` and `δm_T²/m_T² ~ 10⁻¹²²`. Internally consistent. **B4:** `(H₀/M_Pl)² ~ 10⁻¹²²`. Correct.
- **Eq. (B1) itself.** The printed 5×5 matrix *is* the standard Fierz matrix when read by rows (row 1 = `(1/4)(1,1,1,1,1)` is the standard scalar row), and `F² = 𝟙` holds — I verified row 1 and row 2 of `F²` by hand. The matrix is fine; what is done with it is not (see M2).
- **Citation integrity — mechanically clean.** All 20 `\cite` keys in `main.tex` resolve to bibliography entries; `main.log` shows zero undefined citations and zero undefined references; there are no unused `.bbl` entries. At the cite sites I could check: [2] Ashtekar & Singh does support the `ρ_crit/ρ_Pl ≃ 0.27–0.41` LQC window; [10] Minami & Komatsu (2020) and [11] Eskilt & Komatsu (2022) do support `β_obs = 0.342° ± 0.094°`; [19]/[20] (Itzykson–Zuber, Nieves & Pal) are the right provenance for the Fierz matrix; [3]/[4] (Holst; Freidel–Minic–Takeuchi) are correctly placed for the Nieh–Yan-on-shell statement. One numeric exception, see m3.
- **`dim4_parityodd_enumeration.py` runs clean (exit 0)** and does verify the two identities it claims to verify.

---

## 3. Findings

### MAJOR

---

**M1 — [MAJOR] Presentation blocker: Fig. 1 and the §III A barrier list physically overprint adjacent material; visible text corruption on p. 4. (p. 3 Fig. 1; p. 4 barrier list; `main.tex` L285–L288, L380–L466; `main.log` 9 overfull hboxes)**

Rendered at 130 dpi, three separate defects are visible without magnification:

1. **Fig. 1 (p. 3).** The italic band label *"6 Branches (H, J, L, M, N, O): observational-channel barriers"* is drawn **on top of** the Foundation-box row — it crosses the bottom borders of the `Found. A … Found. G` boxes and the connector arrows descending from them. Separately, the `R1 — NJL (Planck-suppressed)` box overlaps the bottom edge of the `Branch H / B8, B14` box. The figure as printed is not legible as a structural diagram.
2. **Fig. 1 typo.** The Route-3 box reads **"R3 — Innmirzi (mass-lock)"**. Should be *Immirzi*.
3. **Barrier list (p. 4).** The `\item[...]` labels overflow the column measure and collide with the right column. Concretely: `B6 — Attractor-Sensitivity Dilemma (Found. F) [R3].:` runs into the right column's *"redshift/dilution and by frequency-integration);"*; `B10 — UV→IR Specificity Dilemma (Branch L) [R3].:` runs into the §IV A opening; and worst, **`B11 — Decoupling Universality (Branches L/M) [R3].:e`** — the trailing `e` is the right column's own text ("…reduces to **the** Nieh–Yan density") being overprinted. This is character-level corruption on the page.

`main.log` corroborates: 9 overfull hboxes, eight of them in the barrier description list (lines 380–466), the largest 43.15 pt over a ~246 pt column (≈18% overflow).

Also cosmetic but pervasive: every barrier label terminates in the double-punctuation artifact `".:"` (e.g. *"B4 — Planck Suppression (Found. D) [R2].:"*) — the `\item[…]` label text ending in a period colliding with revtex's description separator.

*Required:* rebuild Fig. 1 with non-overlapping node/label placement (or drop the band labels into the caption); fix "Innmirzi"; convert the `description` list to a form that breaks the label (e.g. run-in `\paragraph`-style headers, or `\item[]` with the label as the first sentence of the body); strip the trailing periods from the labels; recompile to zero overfull hboxes in the body text.

---

**M2 — [MAJOR] Eqs. (B2) and (B3) are inconsistent with Eq. (B1), and the released verification script contradicts both. The claim "verified symbolically" is not supported by the released artifact. (p. 14, App. B; `arxiv/scripts/fierz_lemma_check.py`)**

The text states: *"the involution F² = 𝟙 is verified symbolically. Applying F to the generated operators gives the exact decompositions"*, followed by Eqs. (B2), (B3).

**(a) (B2)/(B3) apply the transpose of the printed matrix.** Eq. (B1)'s axial row is `(1/4)(4, 2, 0, −2, −4)`, i.e.

> `AA → SS + ½ VV + 0 · TT − ½ AA − PP`

Eq. (B2) as printed reads `¼ SS + ½ VV − ½ AA − ¼ PP`. The `VV` and `AA` entries match the row; the `SS` and `PP` entries are the **column** entries, wrong by a factor of 4. Identically for Eq. (B3) against row 2 (`(1/4)(4, −2, 0, 2, −4)` ⇒ `SS − ½VV + ½AA − PP`, vs the printed `¼SS − ½VV + ½AA − ¼PP`). The row reading is the physically correct one: the standard vector Fierz identity has unit coefficient on the scalar channel, not ¼. So (B2) and (B3) are, as displayed, wrong.

**(b) The released script prints a different matrix entirely.** `fierz_lemma_check.py` outputs

```
F_cnum = (1/4) [[1, 1, 1/2, -1, 1],
                [4, -2,  0,  -2, -4],
                [12, 0, -2,   0, 12],
                [-4, -2, 0,  -2,  4],
                [1, -1, 1/2,  1,  1]]
```

which differs from Eq. (B1) in the tensor column (½ vs 1), row 3 (12 vs 6), and the entire sign structure of the axial column/row. Its reported **axial operator row is `[1, ½, 0, ½, −1]`** — `S = 1`, `P = −1` (contradicting Eq. B2's ¼ and −¼) and `A = +½` (contradicting Eq. B1's row-4 entry `−½` *and* Eq. B2's `−½`). No arrangement of the script's output reproduces Eq. (B2).

**(c) Signature mismatch.** The paper says the matrix was *"Computed from the explicit Dirac matrices in the paper's mostly-plus signature (script `arxiv/scripts/fierz_lemma_check.py`)"*. The script sets `metric = sp.diag(1, -1, -1, -1)` and its docstring says *"the normalized (+---) basis of Nieves & Pal"* — mostly **minus**. Note also §III/§V use mostly-plus elsewhere (`ε⁰¹²³ = +1`, `ε_{abcd}ε^{abce} = −3!δ`), so the paper's own convention statement is the one that is right for the rest of the paper; the script is not computing in it.

**(d) The script does not verify what the paper says it verifies.** It never computes Eq. (B3), never computes `F²` for the *printed* matrix, never demonstrates the `(J·J⁵)` Holst partner "rotates only within the {V, A} block (`F_VA = F_AV = ½`)", and its own docstring explicitly limits itself: *"Only the scalar exchange coefficient is used in P1A's declared direct-channel mean-field check"* and *"The calculation does not remove the mean-field Fierz ambiguity or enumerate derivative, flavor/color-exchange, or gravitational-EFT operators."* The script is P1A's, scoped to P1A's use; P1C cites it for a broader claim it does not make.

*Mitigation, stated fairly:* the physical conclusion App. B is used for — that the generated structures close on `{SS, PP, VV, AA}` with `O(1)` coefficients and no change of `M_Pl` power — survives every one of these variants, because all the disputed coefficients are `O(1)` and all land inside the same closed set. So the no-go itself is not threatened. But a referee cannot pass a displayed equation that is wrong, contradicted by the paper's own artifact, and labelled "verified".

*Required:* recompute (B2)/(B3) in the paper's stated signature with the paper's stated matrix; state explicitly whether the c-number or the anticommuting-operator map is being displayed (the script maintains both, `F_op = −F_cnum`, and the sign of the `AA` entry turns on exactly that choice); either extend the script to verify the equations as printed or retitle the availability claim to what the script actually checks; fix the signature sentence.

---

**M3 — [MAJOR] The symbol κ carries two mutually incompatible definitions, and the Planck-power sentence that closes Route 2 depends on the collision. (§II p. 2; §IV A p. 5–6; Eq. (4) p. 6; Table III / App. B pp. 13–14. `main.tex` L118, L176, L543–544, L559, L580, L694, L701, L1399, L1494)**

- §II (L176): `κ ≡ 8πG = M_Pl⁻²` — κ has mass dimension −2. This is the definition the rest of the paper's algebra needs: the contact term `−(3κ/16)γ²/(1+γ²)(J⁵)²` is dimension 4 only with `[κ] = −2`, and Table III / L1399's identity `M_Pl²κ² = κ` holds only for `κ = M_Pl⁻²`.
- §IV A (L543–544): *"λ₄ = γ κ² (W·J) (their Eq. 37, **κ² = 16πG = M_Pl⁻²**)"*; L559 and L580 repeat `κ² = M_Pl⁻²`; Eq. (4) (L694) carries `κ² = 16πG` and L701 reads `μ²κ² = (μ/M_Pl)²`. Here κ has mass dimension −1.

Both cannot hold. Under §II's κ, `κ² = M_Pl⁻⁴`, which cannot equal `16πG` (dimension −2). The imported Shapiro–Teixeira and Benedetti–Speziale convention (`κ² = 16πG`) is the correct one *inside* Eq. (4) — `μ²κ²` must be dimensionless — but it is the same glyph as the paper's own κ, never renamed and never flagged.

This is not cosmetic: the sentence that carries the Route-2 closure past the unfixed `β(γ)` normalization is *"since ST's explicit κ² = M_Pl⁻² confirms the missing powers are Planck powers, not a light scale"* (L580). As printed, that sentence is only well-formed under a convention the paper contradicts three sections earlier.

**Compounded by silent reduced-vs-full Planck-mass switching.** `κ ≡ 8πG = M_Pl⁻²` defines the *reduced* mass, `2.435 × 10¹⁸ GeV`. But the §IV A numerics need the *full* mass: `M_Pl · (α/M) ~ 10⁻²` requires `1.22 × 10¹⁹ × 10⁻²¹ = 1.2 × 10⁻²` (reduced gives `2.4 × 10⁻³`), and Eq. (A2)'s `(α/M) M_Pl⁵ ~ 10⁻² M_Pl⁴` requires the same. Immaterial to a 60-order bound, but it must be declared.

*Required:* rename the imported coupling (e.g. `κ_ST`) or convert ST/BS results into the paper's own κ; state once, in §II, which Planck mass the numerics use.

---

**M4 — [MAJOR] The "~41–67 orders" figure (p. 7) is not reconstructable from the paper's own inputs, and the abstract, §VI and §VII all overstate the body's stated floor. (p. 7 `main.tex` L726; abstract L84; §VI L1108; §VII L1172; cf. §IV A L622)**

The sentence names its own propagation: *"Propagated to the dark-energy channel through the paper's own `(Δγ/γ)·(H₀/M_Pl)` mass-dimension suppression, the derived torsion/Immirzi contribution to ρ_Λ sits **~41–67** orders of magnitude below…"*. Carrying that out with the paper's own two endpoints for `Δγ/γ` and its own `H₀/M_Pl ~ 10⁻⁶¹`:

- derived value `Δγ/γ = 1.4 × 10⁻⁶` ⇒ `1.4 × 10⁻⁶ × 10⁻⁶¹ = 1.4 × 10⁻⁶⁷` ⇒ **66.9 orders**
- pessimistic value `Δγ/γ ~ 0.3` ⇒ `3 × 10⁻⁶²` ⇒ **61.5 orders**

The range is therefore **~61–67**, not 41–67. The number 41 appears exactly once in the manuscript, is never derived, and cannot be recovered from any combination of the paper's stated inputs. It reads as a typo for 61.

Left as printed, it collides with three separate summary claims:

- **Abstract (L84):** *"both leave more than sixty orders of magnitude of suppression margin"*
- **§VI (L1108):** *"closed here at the amplitude level with margins exceeding sixty orders of magnitude"*
- **§VII (L1172):** *"each leaving more than sixty orders of magnitude of suppression margin"*

41 < 60. As written the abstract claims more than the body shows.

**Separately, Route 2's own floor also undercuts "more than sixty".** §IV A (L622) states the R2 suppression is *"≈60 (conservatively ≥58) orders of magnitude relative to the observed signal"*. The abstract's "**both** leave **more than** sixty" is therefore an overstatement for R2 even after the 41→61 correction. `"of order sixty"`, or `"≳58"`, is what the body supports.

*Required:* correct 41→61 (or derive 41); harmonize the abstract/§VI/§VII wording to the body's actual floor.

---

**M5 — [MAJOR] B14's branch assignment is stated three incompatible ways; the abstract's 7 + 6 = 13 arithmetic cannot be reconstructed from Table I. (abstract; §II p. 2; Fig. 1 + caption p. 3; Table I p. 3. `main.tex` L285, L322, L349–L355)**

- **Table I, Source column (L355):** B14 → **"ECH Gates"**, a category distinct from every Foundation and every Branch.
- **Fig. 1 (L285):** B14 sits inside the node labelled **`Branch H \\ B8, B14`**, and the caption says *"B8 (Branch H, parity-even interaction) is subsumed by B14 … and they are grouped together"*.
- **§II prose (p. 2):** *"6 additional observational channels (Branches H, J, L, M, N, O, **plus** ECH perturbation gates)"* — i.e. six branches *and a seventh category*, totalling 7 + 6 + 1 = 14 entries.
- **Abstract:** *"thirteen distinct mechanism-class constraints — fourteen historical catalog entries, one subsumed by another — spanning **seven** foundational mechanism classes and **six** observational-channel branches."* 7 + 6 = 13 requires B14 to occupy a Branch slot (Branch H's, with B8 folded in), which is Fig. 1's reading and directly contradicts Table I.

Additionally, Fig. 1's caption asserts *"6 observational-channel branches (Branches H, J, L, M, N, O, middle row; Barriers 8–14)"* while the middle row contains **four** boxes (`Branch H`, `Branch J`, `Branch L/M`, `Branch N/O`). And Table I's Source column separately uses `Branch L` (B10), `Branch L/M` (B11) and `Branch M` (B12) as three distinct labels, which Fig. 1 collapses into one.

A reader who tries to verify the paper's own headline count — 14 entries, 13 distinct, 7 + 6 — from Table I as printed will fail. Since the catalog's structure *is* the paper's organizing contribution, this needs to be exactly right.

*Required:* pick one assignment for B14 and propagate it to Table I, Fig. 1, Fig. 1's caption, §II, and the abstract; make Fig. 1's box count match the branch count it claims, or restate the claim.

---

**M6 — [MAJOR] The operator-basis-completeness argument asserts the enumeration rather than deriving it; the abstract claims exhaustiveness at a confidence the argument does not deliver. (§V pp. 8–10, 13; abstract; Eq. (7), Eq. (8), Table III)**

The brief asks specifically whether the operator-basis argument supports the claimed exhaustiveness. My reading: the *architecture* of the argument is legitimate — exhibit a finite basis, show each member is topological / Fierz-reducible / Bianchi-vanishing, then note the single-scale NDA ceiling is monotone in dimension and class-blind, so bounding one representative bounds the tower. That is a real move and I would not object to it in principle.

What is missing is the step that makes it a *completeness* argument rather than an *exhibition*. Eq. (7) writes `{𝒪ⁿ⁽⁴⁾} = {O1–O6}` and Eq. (8) lists them, but the manuscript never states the generating rule from which that list follows as *the* complete one: which building blocks are admitted (`ε`, `e`, `T`, `R`, `J⁵`), at what derivative order, under which index-contraction closure. Without it, a referee cannot rule out, e.g., an `εTT` contraction with a different index pairing than O4, an `ε ∂T e e` structure, or a `(∇·T)`-type parity-odd density — all of which are built from the same admitted field content at the same dimension. §V's scope paragraph lists what is *excluded* (new light scale, dynamical Immirzi, propagating torsion, non-minimal trace/tensor irreps, derivative four-fermion terms, higher-curvature mixed invariants, multi-species chiral structures) — commendably explicit — but exclusions are not a construction rule, and the excluded list does not establish that the *included* list is closed.

The released `dim4_parityodd_enumeration.py` does not fill this gap: it verifies two identities (`ε^{μνρσ}R_{μνρσ} = 0` under algebraic Bianchi; `S_{abc}S^{abc} = −⅜(J⁵·J⁵)`) and then *asserts* the enumeration in its printed verdict. It performs no enumeration.

The abstract's phrasing therefore overreaches: *"every local, gauge-invariant, diffeomorphism-covariant parity-odd density of mass dimension exactly four admitted by the minimal-coupling ECH field content **is enumerated** and shown to be either a topological total derivative, a Fierz-closed four-fermion contact term…"*. §V's own verdict is more honest — *"Every admissible local dimension-4 parity-odd density in minimal ECH **within the enumerated set {O1–O6} at the stated power-counting order**"* — and that qualifier is exactly what the abstract drops.

This is also load-bearing in a second way: the O4/O5 branch of the argument routes entirely through App. B's Fierz lemma, whose displayed algebra is wrong and whose "verification" does not verify it (M2).

*Required:* either (a) state the generating rule and demonstrate closure (a short symbolic enumeration over admitted index structures would do it, and would make the released script actually match its own name), or (b) downgrade the abstract and §VII to match §V's own qualifier — "the following six representatives are exhibited and shown to close under the stated construction rules" — and say plainly that completeness of the list is asserted from construction, not proved.

---

**M7 — [MAJOR] Substantial content duplication with the DOI-archived companion: the barrier catalog, the single-scale NDA appendix, and the Fierz lemma are all already in P1A. (Ref. [1]; `arxiv/paper1a_ech_nogo.tex` v1A.0.127)**

P1C states its division of labour on p. 1: *"we cite that companion's contact-term and zero-spin-branch transparency results rather than re-deriving them, and **restrict the present survey to the barrier catalog, the Route-2/Route-3 closures, and the completeness argument** that establishes the catalog's scope."*

Ref. [1] resolves to *"Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches"*, Zenodo `10.5281/zenodo.21481838`. The current local source carrying that title is `arxiv/paper1a_ech_nogo.tex`, v1A.0.127. Inspecting it:

- It contains `\section{Structural Constraints on Dark-Energy Routes in Minimal ECH}\label{sec:barriers}` — **the same barrier catalog**, with the same framing: *"Through 7 foundation studies (Foundations A–G) and 6 observational research branches (Branches H, J, L, M, N, O), we establish 14 mechanism-class…"*, *"13 distinct barriers (14 historical catalog entries with B8 subsumed by B14)"*.
- It contains `\label{app:dimensions}` — **the same single-scale NDA dimensional no-go** that P1C reproduces as its Appendix A ("`ρ_Λ^ECH ~ M_Pl⁴`, never (meV)⁴", the off-shell dimension-+1 argument, the two admissible completions).
- It contains `\label{app:fierz}` — **the same Fierz-by-Fierz projection lemma** that P1C reproduces as its Appendix B.

So two of the three items P1C names as its exclusive scope — the barrier catalog and the completeness argument — are already published in the companion it cites. (The superseded monolith `arxiv/main.tex`, v2.3.18, carries the same catalog with 14 `\subsection{Barrier N}` blocks and a verbatim-identical "Constraint classification" paragraph; P1C's own header comment identifies `arxiv/paper1_unified.tex` as its extraction source and says *"Every equation and quantitative claim below is carried verbatim or near-verbatim from that source; no new derivation is introduced."*)

An editor comparing P1C against the archived companion will see this immediately. It needs to be disclosed and justified in-manuscript, not left for the reader to discover — the standard remedy is an explicit statement of what is reproduced, why reproduction (rather than citation) is necessary for self-containment, and a sharpened claim of what is genuinely new here.

*Note on Ref. [1] as printed:* nothing in the reference or the citing text tells a reader that the companion also contains the barrier catalog and both appendices. Given the overlap, that omission compounds the problem.

---

**M8 — [MAJOR] §IV reinstates the Route-2/Route-3 mappings that the cited companion explicitly retired, without acknowledging the disagreement. (§IV pp. 4–7; abstract; `arxiv/paper1a_ech_nogo.tex` v1A.0.127)**

The companion states, in its own scope paragraph:

> *"Earlier exploratory mappings from one-loop Holst/Immirzi running to late-time dark energy are **not retained as results**: the cited calculations **do not derive the required cosmological stress tensor and observable matching** [ShapiroTeixeira2014, BenedettiSpeziale2011run]."*

P1C's §IV is precisely those mappings, built from precisely those two references, and its abstract elevates them: *"we derive here the amplitude-level closures of Route 2 … and Route 3 … : Route 2 is one-loop-grounded via the explicit renormalization of the Holst-plus-fermion sector, and Route 3 is closed with an integrated one-loop renormalization-group flow."*

Critically, P1C does **not** supply the step the companion said was missing. It propagates to the dark-energy channel via *"the paper's own `(Δγ/γ)·(H₀/M_Pl)` mass-dimension suppression"* (p. 7) — a dimensional-assignment heuristic, not a cosmological stress tensor and not an observable matching. So the companion's stated objection applies unchanged to what P1C now presents as a closure.

To be fair to the manuscript: §IV is scrupulous about tiering (Table II rates R2 as Tier-III ansatz-level and R3 as Tier-II+III), the Riccati/no-fixed-point limitation of the Shapiro–Teixeira system is disclosed, and the "Strict theoretical limitation" paragraph on p. 7 says outright that *"the inputs cannot be promoted to precision derivations without a UV-complete treatment of the coupled Holst+fermion RG system."* That is honest. But the abstract's "amplitude-level closures … one-loop-grounded" is stronger than the companion's own assessment of the same literature, and the two papers are being posted as a coordinated pair.

*Required:* either reconcile — state that P1C reinstates a mapping the companion set aside, and say what changed (presumably: it is now presented as a bounded amplitude budget rather than a derivation) — or align the companion. Leaving two co-posted papers with opposite positions on the same two references is the kind of thing a referee flags and an editor will not let pass.

---

**M9 — [MAJOR] The "+1 vs +4" three-unit deficit is explained two incompatible ways, and the §V/§VI explanation does not reproduce its own arithmetic. (§V p. 9; §VI p. 10; App. A p. 11–12; Table III p. 14)**

Two accounts appear:

1. **App. A (p. 11–12):** the deficit is a coefficient-dimension fact — Eq. (6) carries the phenomenological `α/M` (dimension −1) where the genuine basis operators carry `M_Pl²` (dimension +2). `+2 → −1` is exactly the three-unit drop, and App. A says so: *"The three missing mass powers are therefore forced to be `M_Pl³`."* This is correct and it is the account the rest of the paper needs.
2. **§V (p. 9) and §VI (p. 10):** *"Eq. (6) with its dimension-+1 integrand is **the on-shell reduction of the dimension-4 basis after the algebraic Bianchi identity strips one curvature factor**"*, and *"Passing to the on-shell branch (algebraic torsion eliminated, one curvature factor stripped by the Bianchi identity) reduces this closed dimension-4 set to the single dimension-+1 representative displayed in Eq. (6)."*

Account (2) does not work on its own terms. Stripping one curvature factor removes **two** mass units, not three — it would land at +2, not +1. And by the paper's own Check A (p. 13, Eq. A4), the algebraic Bianchi identity does not *strip* anything from O1/O6: it makes them **vanish identically** (`ε^{μνρσ}R_{μνρσ} = 0`), which is a different operation with a different consequence. The two mechanisms are being conflated.

This matters because §V leans on the reconciliation to argue that the `+1`-dimensional Eq. (6) is *"a simplified stand-in for this closed set, not an ad-hoc object requiring an uncontrolled promotion"* — the central rebuttal to the obvious referee objection that the paper's representative operator has the wrong dimension. The rebuttal is right (account 1), but it is stated in a form (account 2) that a careful referee will read as incorrect.

*Required:* delete or repair the "Bianchi strips one curvature factor" formulation; state the deficit uniformly as the `α/M`-for-`M_Pl²` substitution, consistently in §V, §VI and App. A.

---

### MINOR

**m1 — [MINOR] Dropped sign in the `Ω₄₄/α₄` ratio. (p. 5)** With `α₄ = −6/(1+γ²)` and `Ω₄₄ = 81γ⁴/[16(1+γ²)²]`, the ratio is `−27γ⁴/[32(1+γ²)]`. The paper prints `+27γ⁴/(32(1+γ²))`. The magnitude and the quoted value at `γ₀ = 0.24` are fine (I get `2.65 × 10⁻³` vs the paper's "≈ 2.5 × 10⁻³"); only the sign is dropped. If the absolute value is intended, write it as such.

**m2 — [MINOR] The stated GUT-to-IR lever arm does not match its own stated endpoints. (p. 7, `main.tex` L739)** *"a GUT-to-IR lever arm `ln(μ_GUT/μ_IR) ≈ 30–35` (`μ_GUT ~ 10¹⁶`, `μ_IR ~ 1 GeV`)"* — but `ln(10¹⁶) = 36.8`, outside the quoted range. The paper then uses 32 in the worked example. Either widen the range to include 36.8 or state the endpoints that give 30–35.

**m3 — [MINOR] The ACT DR6 birefringence value is quoted with uncertainties but carries no citation. (p. 7)** *"(comparable to the independent ACT DR6 measurement `β = 0.215° ± 0.074°`)"* — no `\cite`. Every other quoted measurement in the manuscript is cited. The companion attributes this value to Diego-Palazuelos & Komatsu; that reference is absent from P1C's bibliography entirely. Add it.

**m4 — [MINOR] Extraction seam: the symbolic checks are labelled "Check A" and "Check D"; Checks B and C do not exist. (p. 13; `main.tex` L1433, L1448; Table III p. 14)** Orphaned labelling inherited from the pre-split monolith. The released script has the same gap (`[CHECK A]`, `[CHECK D]`). Table III's Fate column cites only "Check A", so a reader looking for B and C finds nothing. Renumber to A/B, in both the manuscript and the script. (Note the collision risk: §V's main-text version of the same enumeration uses `(a)/(b)/(c)`, and App. B is separately referred to as "App. B" — three numbering schemes for adjacent material.)

**m5 — [MINOR] "Two entries carry the only equations in the catalog (B1, B12)" is inaccurate on either reading. (p. 3, `main.tex` L365)** B4 carries `m_φ²/M_Pl²`, `(∂φ)²/M_Pl⁴`, `𝒪(10⁻¹²²)`; B5 carries `∫d⁴x√−g ρ_Λ`. If "equations" means displayed equations, then *no* catalog entry has one, including B1 and B12. Reword.

**m6 — [MINOR] B5's e-fold count is stated flatly where the paper elsewhere insists it is a range. (p. 4 vs App. A pp. 11–12; `main.tex` L401 vs L1337, L1353)** B5 says *"transfer the integrated vacuum energy across `~92` e-folds of inflation"*; App. A derives `N_tot ≈ 122 ln10/3 ≈ 94` and then says *"Readers should therefore treat `N_tot ≈ 92–94` as an order-of-magnitude estimate, not as a precise number."* B5 should carry the range or point to App. A.

**m7 — [MINOR] App. A argues against its own displayed equation without saying what that equation is for. (p. 12)** Eq. (A2) gives `ρ^bounce ~ 10⁻² M_Pl⁴`; three sentences later the text says *"the bounce-scale density entering this hierarchy is `ρ_bounce ~ M_Pl⁴`, **not** the local pseudo-density `ρ_bounce ~ 10⁻² M_Pl⁴` that Eq. (A2) labels"*. This is the origin of the 92-vs-94 split (m6) and reads as an unresolved internal disagreement. State once which density Eq. (A2) computes and which enters the hierarchy.

**m8 — [MINOR] Two different RG systems, two opposite fixed-point statements, within two columns and no signposting. (pp. 5–6)** p. 5: *"the system **has no renormalization-group fixed point**"* (Shapiro–Teixeira `λ₄(t), γ(t)` Riccati system). p. 6: *"whose **only fixed point** is the ultraviolet-attractive `γ² = 1`"* (Benedetti–Speziale). p. 7 then reverts to *"that sector's coupled RG flow has no fixed point"*. Both are correct for their own system, but a reader arriving at p. 6 has just been told there is no fixed point. Add the system name to each statement.

**m9 — [MINOR] Data and Code Availability gives bare relative paths with no repository URL or DOI. (p. 11)** The block prints `arxiv/scripts/dim4_parityodd_enumeration.py` and `arxiv/scripts/fierz_lemma_check.py` as unlinked text, described only as *"publicly available in the same repository as the companion papers"* — which repository is never named on the page. The preamble defines `\repoBase` and an `\artifact{}` macro that would produce resolvable links; they are not used here. A reader with only the PDF cannot resolve these paths.

**m10 — [MINOR] Route-2 framing oscillates between "closure" and "exploratory". (pp. 5–6)** Within one column: *"Route 2 remains exploratory framing, not load-bearing for the no-go"* and *"The closure of Route 2 is therefore robust to the ansatz-level status of the operator"*, alongside the abstract's *"we derive here the amplitude-level closures of Route 2"*. Table II resolves it (Tier III, *"exploratory; not load-bearing"*), but the body should not require the reader to consult the table to know which claim is operative. Pick one register.

**m11 — [MINOR] Abstract length and density.** At ~340 words the abstract runs well past PRD/CQG norms and contains six separate hedging clauses. Given M4 and M6 require rewriting parts of it anyway, this is the moment to cut it to the claims the body actually establishes.

---

## 4. Verdict

Nine MAJOR findings, eleven MINOR. The MAJOR set divides into: one presentation blocker (M1), three internal-correctness defects (M2, M3, M9), one numerical/scope-honesty defect (M4), one catalog-bookkeeping defect (M5), one scope-of-claim defect in the paper's central completeness argument (M6), and two cross-paper problems with the co-posted companion (M7, M8). None requires new physics; M7 and M8 require an editorial decision by the author about the scope split between P1A and P1C, and should be settled before the next compile.

**VERDICT: major-revisions**
