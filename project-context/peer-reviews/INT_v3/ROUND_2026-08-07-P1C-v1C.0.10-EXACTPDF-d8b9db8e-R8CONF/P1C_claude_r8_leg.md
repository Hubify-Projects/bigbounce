# P1C v1C.0.10 — Claude INT Leg, R8 Confirmation Board

- **Role:** Independent skeptical journal referee (CQG calibre), Claude leg of the R8 confirmation board. Fresh review; no prior rounds seen.
- **Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf` (20 pages, "A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and Bounce Phenomenology", dated August 6, 2026, v1C.0.10)
- **SHA-256 (verified before review):** `d8b9db8e4b2441530feba1539498d90c08fce8ba861bcbfa84ab4e268528defd` — MATCH
- **Review date:** 2026-08-07
- **Scope of review:** mathematical correctness of every checkable displayed equation (incl. Appendices D and E), internal consistency, scope honesty, citation integrity, presentation blockers.

## VERDICT: MINOR REVISIONS — 0 MAJOR, 7 MINOR

The manuscript's quantitative content is in unusually good shape. I independently re-derived or re-computed every checkable number and equation; all but one algebraic expression check out exactly, and the one error found is a single-exponent typo with zero downstream propagation. Scope is stated with exceptional (indeed excessive) honesty. No presentation blockers (no column overflow, tables render correctly, figure/caption/table cross-references consistent).

---

## Verification log (what was checked and passed)

1. **Eq. (2) Route-2 budget arithmetic (p. 6–7).** α_em/(4π) = 5.81×10⁻⁴ (paper: 5.8×10⁻⁴, conservatively rounded up to 10⁻³) ✓. H₀/M_Pl ≈ 1.2×10⁻⁶¹ ✓. β_obs = 0.342° = 5.97×10⁻³ rad ✓. M_Pl(α/M) ~ 10⁻² ✓. Double-normalized ratio 10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) = 1.7×10⁻⁶⁰ ≈ 10⁻⁶⁰ ✓; single-normalized contraction ≈ 2×10⁻⁶² ✓; "≈60 (conservatively ≥58)" consistent ✓. The paper correctly quotes the *weaker* of the two normalizations as the headline — conservative direction ✓.
2. **Eq. (1) dimensional bookkeeping (p. 6).** [∂ϑ_NY] = +2, [J⁵] = +3, prefactor −1 → density +4 ✓; the intermediate Δθ ~ (α_em/4π)(H₀/M_Pl) chain is dimensionally clean (the eV-vs-eV·s trap the paper itself warns about is correctly avoided) ✓.
3. **Eq. (4) Benedetti–Speziale integration (p. 8).** Independently reproduced: with κ̄²/(8π)² = 1/(4πM_Pl²), ∫μ²dlnμ = μ_UV²/2, γ = 0.24 (γ² = 0.0576, (1−γ²)(23γ²+5) ≈ 5.96), μ_UV = 10¹⁶ GeV, full M_Pl = 1.22×10¹⁹ GeV: Δγ² ≈ 1.6×10⁻⁷ → |Δγ/γ| = Δγ²/2γ² ≈ 1.4×10⁻⁶. **Exact match to the paper's quoted value.** The UV-domination claim ((μ_UV/M_Pl)² ≈ 6.7×10⁻⁷ power-suppressed, not logarithmic) ✓.
4. **Eq. (3) chiral-count estimate (p. 7–8).** ln 10¹⁶ = 36.8 ✓; ln 10¹³ ≈ 30 ✓; 12π² = 118.4; 36.8/118.4 = 0.31, 30/118.4 = 0.25, 32/(12π²) = 0.27 — all match the quoted 0.25–0.31 band ✓ (see Minor 3 for a nuance).
5. **Route-3 endpoints (abstract, p. 8, Sec. VI).** 1.4×10⁻⁶ × 1.2×10⁻⁶¹ ≈ 1.7×10⁻⁶⁷ → ~67 orders ✓; 0.3 × 1.2×10⁻⁶¹ ≈ 3.6×10⁻⁶² → ~61 orders ✓. Abstract/body/conclusions all consistent on 61–67 ✓.
6. **Appendix E, Eq. (E5) R1 benchmark.** Full independent recomputation: 100 cm⁻³ = 100·(1.9733×10⁻⁵ eV)³ = 7.68×10⁻¹³ eV³; κ = 8π/(1.2209×10²⁸ eV)² = 1.69×10⁻⁵⁵ eV⁻²; κn_ψ² = 1.0×10⁻⁷⁹ eV⁴ ✓. (2.3 meV)⁴ = 2.8×10⁻¹¹ eV⁴ ✓; ratio 3.6×10⁻⁶⁹ ✓ (= 68.4 orders ✓); with (2.25 meV)⁴ = 2.56×10⁻¹¹ eV⁴ → 3.9×10⁻⁶⁹ ✓ (matches Sec. II's convention discussion exactly); with 3/16: 1.9×10⁻⁸⁰ eV⁴ = 6.7×10⁻⁷⁰ρ_Λ ✓.
7. **Appendix E, Eqs. (E1)–(E4).** Q_γ Q_γ⁻¹ = (⋆+γ⁻¹𝟙)·γ²/(1+γ²)·(γ⁻¹𝟙−⋆) = (1+γ⁻²)γ²/(1+γ²) = 1 using ⋆² = −𝟙 ✓. Normalization bridge: κ = 8πG → −(3/2)πG = −3κ/16 ✓; recovery of the pure-EC coefficient −3κ/16 as γ→∞ and γ²/(1+γ²) < 1 for finite γ ✓.
8. **Appendix A hierarchy and e-fold bookkeeping.** (1.2209×10²⁸/2.25×10⁻³)⁴ ≈ 8.7×10¹²² ✓; N_tot = 122 ln10/3 = 93.6 ≈ 94 ✓; ln10/3 ≈ 0.8 ✓; the 92-vs-94 spread from ρ_bounce ~ M_Pl⁴ vs Case-II 10⁻²M_Pl⁴ (120 vs 122 decades → 92.1 vs 93.6) ✓ — the "sharper dependency statement" is internally exact.
9. **Eq. (A2).** (α/M)M_Pl⁵ with M_Pl(α/M) ~ 10⁻² → 10⁻²M_Pl⁴ ✓.
10. **B12 window (p. 5).** ρ_crit = √3/(32π²γ³)ρ_Pl: γ = 0.2375 → 0.409 ✓ (canonical LQC 0.41); γ = 0.274 → 0.267 ✓; squared window 0.073–0.168 ≈ 0.07–0.17 ✓. The scheme-dependence disclosure (0.274 is an internal extrapolation, not in Ref. [4]) is honest ✓.
11. **B1 (p. 4).** g_eff ~ 1/(M_Pl√|t₃|) with √|t₃| ~ m_T⁻¹ → m_T/M_Pl ~ 10⁻⁶¹ ✓; δm_T² ~ M_Pl² → cancellation 1 in (M_Pl/H₀)² ~ 10¹²² ✓ (labeled scaling ansatz, honestly).
12. **Sec. IV C anchor.** α/M ~ 2β_obs/M_Pl = 2·6×10⁻³/1.22×10¹⁹ GeV ≈ 10⁻²¹ GeV⁻¹ ✓. Birefringence inputs: 0.342°±0.094° (≈3.6σ) ✓; 0.35°±0.14° ✓; ACT DR6 0.215°±0.074° (≈2.9σ) ✓ — significances arithmetically consistent with the quoted values.
13. **Eq. (8)/Table III dimension audit.** [εeeR] = 2, [NY] = 2, [R∧R] = 4, [εTT] = 2, [εTeJ⁵] = 1+0+3 = 4, [εR] = 2; prefactor promotions all land at +4 ✓; O4→κ²(J⁵·J⁵), O5→κ(J⁵·J⁵) κ-power tracking consistent with M_Pl²κ² = κ (reduced-mass convention) ✓.
14. **Check D (App. A1).** S_abcS^abc = (1/16)ε_abcd ε^abce J⁵ᵈJ⁵ₑ = (1/16)(−3!δ) = −3/8(J⁵·J⁵) ✓.
15. **Appendix C Fierz matrix (C1)/(C2).** F_c matches the standard normalized (S,V,T,A,P) rearrangement matrix; spot-checked F_c² = 𝟙 on multiple entries ✓. Axial row ¼(−4,−2,0,−2,4) → operator row (1,½,0,½,−1) under F_op = −F_c → (J⁵·J⁵) → SS + ½VV + ½AA − PP: internally consistent ✓. (F_c)_AS = −1 → G_s = −3κ/16 bridge consistent with (E4) ✓. Convention-dependence is disclosed and the script/Grassmann verification is cited.
16. **Appendix D (B14 theorem).** Proof chain (zero spin density → trivial kernel of the invertible bivector operator for real finite γ, 1+γ² > 0 → T = 0 → Levi-Civita → Holst contraction killed pointwise by the algebraic Bianchi identity) is logically sound within its stated scope; the exclusion list (γ = ±i, anomalies, non-minimal matter, dynamical Immirzi) is complete and honestly stated ✓.
17. **Count consistency.** 14 entries / 13 distinct (B8 ⊂ B14) consistent across abstract, Sec. III, Table I, Fig. 1, Sec. VI–VII ✓. Novel (9) + known (4) + structural (1) = 14 ✓. Branch letters H, J, L, M, N, O with I/K never assigned — disclosed ✓.
18. **Citation integrity.** Refs [2] (Shapiro–Teixeira CQG 31 185002, arXiv:1402.4854), [3]/[9] (Benedetti–Speziale), [5] (Holst PRD 53 5966), [6] (Freidel–Minic–Takeuchi PRD 72 104002), [7] (Mercuri PRL 103 081302), [8] (Date–Kaul–Sengupta PRD 79 044008), [10]–[12] (birefringence), [16]–[18] (Kimura; Delbourgo–Salam; Nieh–Yan), [19] (Popławski PLB 694 181), [20]–[24] (EFT power counting; Itzykson–Zuber; Nieves–Pal) are all real and correctly attributed to the claims they anchor. No phantom citations found. AI-assistance disclosure present and appropriately scoped.

---

## MAJOR findings

None.

## MINOR findings

**MINOR-1 (checkable equation error — must fix).** *Sec. IV A, p. 6, right column:* the inline ratio is printed as |Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)²]. Given the paper's own α₄ = −6/(1+γ²) and Ω₄₄ = −(378+783γ²)/[20(1+γ²)²], the ratio is (378+783γ²)/[120(1+γ²)] — **one power of (1+γ²), not two**. The printed formula contradicts the paper's own adjacent numerics: at γ ≈ 0.24 the correct form gives 3.33 (paper: "≈3.3" ✓) while the printed form gives 3.15; and the claim "bounded below by 378/120 ≈ 3.2 for all real γ" is true for the correct form (monotone 3.15→6.53) but **false** for the printed form (→0 as γ→∞). All numerical uses are consistent with the correct one-power form, so nothing propagates; fix the exponent.

**MINOR-2 (citation pointer).** *p. 8:* the fermion-coupled β-function Eq. (4) is attributed "Benedetti & Speziale [3] (their Eq. 7)" (the J. Phys. Conf. Ser. proceedings, arXiv:1111.0884), while the same flow is credited to "[9]" (the JHEP paper, arXiv:1104.4028) a few lines earlier and in Table II context. Both documents are by the same authors, but "their Eq. 7" must point to the specific document in which that equation number holds; harmonize [3]/[9] usage so the equation-number pointer is unambiguous.

**MINOR-3 (integration nuance, cosmetic).** *p. 8:* integrating Eq. (3), which is linear in γ, gives Δlnγ = (N_F^L−N_F^R)ln(μ_GUT/μ_IR)/(12π²) ≈ 0.25–0.31; the quoted "Δγ/γ ≈ 0.25–0.31" is strictly Δlnγ (exponentiating gives ≈0.29–0.36). Immaterial at the ≥60-order margins, but either write Δlnγ or note the identification, since the survey elsewhere prides itself on exact bookkeeping.

**MINOR-4 (abstract, presentation).** The abstract is a single ≈370-word paragraph saturated with internal taxonomy (route numbers, tier labels, entry counts, "closed-by" vocabulary). For CQG it should be cut by roughly half and lead with the physics result (all four parity-odd/dark-energy channels of minimal ECH close; two by ≥58-order amplitude budgets anchored in published one-loop results; operator-basis argument at dimension 4) with the classification detail left to Sec. III.

**MINOR-5 (repetition, presentation).** The evidentiary-tier disclaimer ("Tier-I only for B14; R2/R3 are ansatz-level budgets, not derivations; completeness asserted not proved") is restated in the abstract, Sec. I, Sec. III preamble, Sec. IV closures, Table II caption, Sec. VI, Sec. VII, and App. A — at least seven near-verbatim instances. Honest hedging is a strength; this much of it buries the actual results. Consolidate into the tier table plus one summary statement.

**MINOR-6 (numeric input consistency, trivial).** *App. A, p. 15:* the hierarchy is printed with M_Pl = 1.22×10¹⁹ GeV in the displayed quotient but the quoted result 8.7×10¹²² corresponds to the four-decimal 1.2209×10¹⁹ (1.22 exactly gives 8.6×10¹²²). Either print 1.2209 in the quotient or quote 8.6; at order-of-magnitude scope this is cosmetic, but the paper's own Sec. II convention flag invites this level of scrutiny.

**MINOR-7 (missing primary citation).** *B12, p. 5:* the SU(2) black-hole-entropy value γ ≈ 0.274 is sourced only to "entropy-counting schemes established in the companion paper." That value has a primary literature origin (SU(2) isolated-horizon/Ghosh–Mitra-type counting); cite the primary source alongside the companion so the scheme-dependence claim is externally checkable.

---

## Scope-honesty assessment

No findings. The paper is conspicuously careful: the completeness assertion for {O1–O6} is repeatedly labeled "asserted from construction rules, not proved by exhaustive enumeration"; Case-II on-shell dressing is labeled a heuristic; R2's missing absolute normalization (no ST fixed point, Riccati flow unsolved) is disclosed rather than papered over; B9 is flagged heuristic; B12's window is flagged scheme-dependent; the R4 closure is explicitly a naturalness objection, not an amplitude exclusion; non-minimal completions are placed outside scope with the fine-tuning relocation argument stated. The channel-level (not operator-level) granularity of "rules out" is stated in Table II's caption. This is the correct posture for a no-go survey.

## Presentation blockers

None found: no column overflow or margin escapes on any of the 20 rendered pages; Tables I–III and Fig. 1 render cleanly; code paths in Data Availability are line-broken correctly; all cross-references and hyperlinks render (external link targets not exercised).

---

*End of Claude R8 confirmation leg. No manuscript edits made; no commits; report file only.*
