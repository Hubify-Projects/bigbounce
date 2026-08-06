# P1C v1C.0.4 — Claude INT leg, Round 2 (confirmation board)

- **Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf` (17 pages)
- **SHA-256 (verified before review):** `7ec5f2218fa26eaf03252142e3576ccd0e76797327f90765f138b242cc6e8055`
- **Date:** 2026-08-06
- **Role:** Independent skeptical journal referee (CQG calibre), Claude leg, R2 confirmation board. Fresh review; no prior reviews of this paper consulted.
- **Scope reviewed:** full 17-page PDF — every checkable displayed equation, internal consistency (barrier table vs figure vs text vs appendices), completeness-argument scope honesty, citation integrity, presentation.

## VERDICT: minor-revisions

The paper's quantitative spine is sound: every displayed number I could independently recompute reproduces (see verification log). Scope honesty is exemplary — the three-tier evidentiary classification, the repeated "asserted from construction rules, not exhaustive enumeration" disclaimers, and Sec. VI's boundary statement are all consistent and non-overclaiming. One genuine internal contradiction in the paper's own constraint-classification apparatus must be fixed; the remaining findings are notational/traceability polish.

---

## MAJOR findings

### MAJOR-1 — B10 is classified as both "ECH-specific calculation" and "not an ECH-specific calculation" (Sec. III, p. 3; B10 entry, p. 4–5)

Direct textual self-contradiction on the same page, in the paper's central classification apparatus:

- Sec. III preamble (p. 3): "several—B5 …, B7 …, **B10 (UV→IR specificity)**, and B13 …—are **general naturalness or classification arguments** that apply to broad classes of bounce/modified-gravity models **rather than sharp ECH-specific calculations**."
- Sec. III *Constraint classification* (p. 3): "**Novel results** (Barriers 1, 2, 3, 4, 8, **10**, 11, 12, 14): **ECH-specific calculations** not immediate consequences of prior literature."
- B10's own catalog entry (p. 5) ends: "**(General naturalness argument.)**" — consistent with the preamble, contradicting the Novel-results list.

The same predicate ("ECH-specific calculation") is asserted and denied of B10 within one section. Because the paper's headline contribution *is* this taxonomy with its evidentiary honesty, the contradiction is a must-fix. Resolution is easy: either move B10 out of the "Novel results / ECH-specific" list, or reword the Novel-results descriptor so novelty (not-previously-catalogued-in-this-context) is decoupled from ECH-specificity, and make B10's three appearances (preamble, classification list, entry tag) agree. Also verify Sec. VI's echo ("five entries (B5, B6, B7, B10, B13) are general naturalness or classification arguments", p. 11) against whatever resolution is chosen — currently Sec. VI sides with the preamble against the classification list.

---

## MINOR findings

### MINOR-1 — O4 schematic invariant does not typecheck under the paper's own conventions (Eq. (8), p. 10; Table III, p. 15)

O4 is written ε_{IJKL} T^{IJ} T^{KL} ("torsion²"). Under the paper's stated field content the torsion two-form T^I carries **one** internal index (component tensor T^{abc} = κS^{abc}, three indices; Sec. II). No object T^{IJ} with exactly two internal indices is defined anywhere, so the schematic as printed cannot be contracted as shown. The *fate* computation is fine — Check D (p. 14) correctly works from S^{abc} = ¼ε^{abcd}J⁵_d and lands on −(3/8)(J⁵·J⁵) — but the displayed invariant in Eq. (8) and Table III should be rewritten in a form that parses (e.g., the component density ε^{μνρσ}T^a_{μν}T_{aρσ} ≡ the T∧T_I piece, or explicit contorsion notation), or a footnote should define the two-index shorthand.

### MINOR-2 — App. C cross-reference drops the γ²/(1+γ²) factor (p. 16 vs p. 2)

App. C states the Fierz bridge gives "the mean-field scalar-channel coupling **G_s = −3κ/16 quoted in Sec. II**." Sec. II (p. 2) actually quotes the contact operator as **−(3κ/16)[γ²/(1+γ²)] (J⁵)²**. The Fierz chain yields only the −3κ/16 channel factor; the γ²/(1+γ²) comes from the torsion elimination, not the Fierz rearrangement. As written the App. C sentence claims agreement with a coefficient that differs by γ²/(1+γ²). One clause ("…the γ-independent channel factor of the Sec. II operator, whose γ²/(1+γ²) prefactor arises from the Cartan elimination") fixes it.

### MINOR-3 — Table II R1 row's "∼70 orders below ρ_Λ" figure has no anchor in this manuscript (p. 9)

The R1 row cites an M_Pl^{−2} amplitude suppression "∼70 orders below ρ_Λ" as a Tier-III estimate. This number is imported from the companion paper and is not rederived, tabulated, or pointed to anywhere in this PDF (the manuscript's own hierarchy arithmetic uses 10^{122–123}). Since the survey is explicitly built to "be judged in one place," add a one-line scaling justification or an equation-level pointer into ref. [1] for the 70-order figure.

### MINOR-4 — Provenance of the 0.27 lower edge of the ρ_crit/ρ_Pl ≃ 0.27–0.41 window (B12, p. 5)

The standard headline effective-LQC critical density from Ashtekar–Singh [4] is ρ_c ≈ 0.41 ρ_Pl. The 0.27 lower edge of the quoted window is not standard shorthand; state its origin (e.g., Immirzi-parameter/quantization-ambiguity dependence within [4]) so the derived Ω_GW ≲ 0.07–0.17 band is traceable. The squares themselves check out (0.27² = 0.073, 0.41² = 0.168).

---

## Verification log (checks performed, all PASS unless noted)

**Arithmetic / equations independently recomputed:**

1. **Eq. (2) Route-2 contraction** — α_em/4π = 5.8×10⁻⁴ ✓; H₀/M_Pl ∼ 10⁻⁶¹ ✓; M_Pl·(α/M) = 1.22×10¹⁹ GeV × 10⁻²¹ GeV⁻¹ ≈ 10⁻² ✓; β_obs = 0.342° = 5.97×10⁻³ rad ✓; ratio 5.8×10⁻⁴·10⁻⁶¹/(10⁻²·6×10⁻³) ≈ 10⁻⁶⁰ ✓; conservative ≥58 with two-order allowance ✓; "≥48 under ten-order inflation" ✓. Dimensionless on both lines ✓.
2. **Eq. (4) Route-3 integration** — reproduced |Δγ/γ| ≈ 1.4×10⁻⁶ from scratch: κ̃² = 16πG, γ = 0.24 (γ² = 0.058), (γ²−1)(23γ²+5)·16π/(8π)² ≈ 0.47, UV-endpoint integral 0.47·(10¹⁶/1.22×10¹⁹)²/2 ≈ 1.6×10⁻⁷ in Δγ², Δγ/γ = Δγ²/2γ² ≈ **1.4×10⁻⁶** — exact match to the quoted value. Fixed point γ² = 1 consistent with the printed β-function form.
3. **Chiral-count ansatz (Eq. (3))** — ln 10¹⁶ = 36.8 (quoted 30–37 ✓); 32/(12π²) = 0.27 ✓; Δγ/γ ≈ 0.25–0.31 ✓; (Δγ/γ)(H₀/M_Pl): 0.3 → 3×10⁻⁶² (∼61.5 orders), 1.4×10⁻⁶ → ∼67 orders — the quoted 61–67 range is exactly the span of the two normalizations ✓.
4. **App. A hierarchy** — (1.22×10²⁸ eV / 2.25×10⁻³ eV)⁴ = 8.6×10¹²² (quoted 8.7×10¹²² ✓ ≈ 10¹²³ ✓); N_tot = 122 ln10/3 = 93.6 ✓; 10¹²²-vs-10¹²³ e-fold shift ln10/3 ≈ 0.8 ✓; 92–94 spread consistent with ρ_bounce ∈ [10⁻² M_Pl⁴, M_Pl⁴] ✓; e^{−3·94} ∼ 10⁻¹²² ✓; B5's N_tot ≈ 92–94 agrees ✓.
5. **Immirzi-rational coefficient** — |Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)] = 3.33 at γ = 0.24 (quoted ≈3.3 ✓); O(1)–O(5) over γ ≲ O(1) ✓; loop factor 1/16π² = 1/(4π)² consistency with the quoted master RG equation ✓.
6. **Fierz apparatus (App. C)** — Eq. (C1) is the standard c-number Fierz matrix in (S,V,T,A,P) (Itzykson–Zuber/Nieves–Pal normalization); F_c² = 𝟙 holds ✓. Axial row: ¼(−4,−2,0,−2,4) = (−1,−½,0,−½,1); F_op = −F_c → (1,½,0,½,−1) → Eq. (C2) (J⁵·J⁵) → SS + ½VV + ½AA − PP ✓. (F_c)_{AS} = −1, (F_op)_{AS} = +1, G_s = −3κ/16 ✓ (see MINOR-2 for the cross-reference wording).
7. **Torsion-square collapse** — S^{abc} = ¼ε^{abcd}J⁵_d with ε_{abcd}ε^{abce} = −3!δ_d^e gives S_{abc}S^{abc} = −(3/8)(J⁵·J⁵) ✓ (consistent at both occurrences, p. 11 and p. 14).
8. **Check A** — ε^{μνρσ}R_{μνρσ} = 0 by the algebraic Bianchi identity on the torsion-free branch: standard and correct; kills O1/O6 as claimed ✓.
9. **Dimension bookkeeping** — Eq. (6): [α/M] = −1, integrand +2, density +1 (A1) ✓; Eq. (8) operators all genuine dimension 4 with the M_Pl² promotions ✓ (modulo MINOR-1 notation); B1's δm²/m² ∼ (H₀/M_Pl)² = 10⁻¹²² ✓; ∂ϑ_NY ∼ H₀² ∼ 10⁻⁶⁶ eV² ✓.

**Internal consistency:** 13-distinct/14-historical count uniform across abstract, Sec. III, Fig. 1 caption, Table I note, Sec. VII ✓. Fig. 1 boxes (Found. A–G = B1–B7; Branch H = B8+B14; J = B9; L/M = B10–B12; N/O = B13) match Table I's Source column and each entry's bracketed route tag ✓. Novel(9)+Known(4)+Structural(1) = 14 ✓ (but see MAJOR-1). Abstract's "exactly one Tier-I rigorous theorem" matches Table II (only perturbation transparency at Tier I) and the Sec. III explanation of why Route-1's closure is not credited Tier-I ✓. B8-subsumption stated identically in abstract, Table I note, Fig. 1 caption ✓. Route-2/Route-3 margins identical in abstract, Sec. IV, Sec. VI, Sec. VII ✓.

**Scope honesty:** the completeness argument is consistently labeled "asserted from the construction rule … not established by exhaustive symbolic enumeration" at every occurrence (abstract, Sec. V, App. A1, Sec. VI); the released scripts are correctly described as verifying the two reduction identities only, not the enumeration ✓. Non-minimal escape routes are explicitly listed and excluded from scope ✓. Case-II on-shell dressing explicitly demoted to heuristic, with the no-go surviving at genuine dimension 4 without it (App. A1) ✓.

**Citation integrity:** all 17 arXiv IDs extracted from the PDF and spot-checked as real and correctly attributed (Shapiro–Teixeira 1402.4854; Benedetti–Speziale 1111.0884 and 1104.4028; Ashtekar–Singh 1108.0893; Holst gr-qc/9511026; Freidel–Minic–Takeuchi hep-th/0507253; Mercuri 0902.2764; Date–Kaul–Sengupta 0811.4496; Minami–Komatsu 2011.11254; Eskilt–Komatsu 2205.13962 = PRD 106, 063503; Carroll astro-ph/9806099; quintom review 0909.2776; EFT power-counting 1312.5624, 1706.08945, 2303.16922; Nieves–Pal hep-ph/0306087) ✓. β_obs = 0.342° ± 0.094° correctly attributed to [10,11] ✓. [12] (ACT DR6 birefringence, 2509.13654) is a 2025 preprint used only as a "comparable" cross-check — acceptable. Zenodo self-citations [1], [13] carry explicit "not peer reviewed" disclosure ✓. Imported Shapiro–Teixeira equation numbers (Eqs. 37, 41–42, 46, 51, 58) and Benedetti–Speziale Eq. 7 are cited, not rederivable here — the paper is explicit that they enter as normalization anchors, which is the honest framing.

**Repository artifacts:** all three linked scripts exist at the printed paths (`arxiv/scripts/dim4_parityodd_enumeration.py`, `arxiv/scripts/fierz_lemma_check.py`, `research/theory_audit/fierz_adjudication_2026_08_05.py`, plus the `.md` report) ✓.

**Presentation:** compile log shows **0 overfull hboxes**; no column overflow, no clipped tables/figures observed on any of the 17 rendered pages; Fig. 1 legible; long typewriter paths are safely set in centered blocks ✓. No presentation blockers.

---

*End of report — Claude R2 confirmation leg. File written only; no commit, no push, no manuscript edits.*
