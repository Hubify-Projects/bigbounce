# P1C v1C.0.5 — Claude INT Referee Report (R3 confirmation leg)

- **Role:** Independent skeptical journal referee (CQG calibre), Claude leg of the R3 confirmation board. Fresh review; no prior review of this paper or its history was consulted.
- **Manuscript:** `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1c_nogo_survey/main.pdf` (18 pages, dated August 6, 2026, v1C.0.5)
- **SHA-256 (verified before reading):** `a770491d56d1e02adb8318fd423a4886f3a479270f03b8cfb3ad1a4e8d96bb74` — MATCH
- **Review date:** 2026-08-06
- **Scope reviewed:** mathematical correctness of every checkable displayed equation; internal consistency (barrier table vs. figure vs. text vs. appendices); completeness-argument scope honesty; citation integrity; presentation blockers.

## VERDICT: minor-revisions

---

## Summary assessment

This is a carefully scoped structural no-go survey. I independently recomputed every checkable number and found the quantitative skeleton sound: the Route-2 amplitude ratio (Eq. 2), the alternative contraction, the Route-3 integrated flow (|Δγ/γ| ≈ 1.4×10⁻⁶ from Eq. 4 with the stated GUT boundary — my independent integration gives 1.38×10⁻⁶), the M⁴_Pl/ρ_obs hierarchy (8.64×10¹²², matching the quoted 8.7×10¹²²), N_tot ≈ 122 ln10/3 ≈ 93.6, the LQC ρ_crit window (my values 0.409 and 0.267 at γ = 0.2375 / 0.274, matching the quoted 0.41 / 0.27), the R1 benchmark 3.9×10⁻⁶⁹ vs. quoted 3.6×10⁻⁶⁹ (reduced-M_Pl κ, agreement at stated precision), and the full Fierz matrix (Eq. C1: F² = 𝟙 verified on sampled entries; row-4 extraction, sign flip to F_op, and Eq. C2 all internally consistent). Barrier bookkeeping (14 entries / 13 distinct / B8⊂B14; Foundations A–G ↔ B1–B7; Branches H/J/L/M/N/O ↔ B8–B14) is consistent across abstract, Sec. III, Table I, Fig. 1, and Table II. The three data-availability script paths exist in the repository. The evidentiary three-tier classification is honest and consistently applied; Sec. VI's "what is not established" is commendably explicit. One checkable algebraic slip was found (MINOR-1). The single MAJOR item is a substantive but bounded request concerning the Sec. V completeness argument.

---

## MAJOR findings (1)

### MAJOR-1 — Sec. V / Appendix A1: basis completeness is asserted, not enumerated, although the enumeration is finite and mechanizable
**Anchor:** Sec. V ("Completeness of the list is asserted from the construction rule — we know of no admitted contraction outside it — and is not established by an exhaustive symbolic enumeration. The released script verifies the two reduction identities used below, not the enumeration itself."); abstract ("completeness of the basis is asserted from the construction rules, not proved"); Sec. VI; App. A1; Table III.

The operator-basis-completeness argument is one of the paper's four headline contributions (Contributions list, Sec. I) and the load-bearing extension from "one representative operator" to "every member of the basis." Yet its central premise — that {O1–O6} exhausts the local, gauge-invariant, diffeomorphism-covariant, parity-odd, dimension-exactly-4 densities admitted by the stated building blocks (tetrad, ε/η, curvature two-form R, algebraic torsion T = κS, J⁵, zero additional derivatives, full contraction to a scalar density) — is a finite, bounded combinatorial problem over a small set of index structures. It is mechanizable with the same symbolic tooling the authors already ship (`arxiv/scripts/dim4_parityodd_enumeration.py` verifies Checks A and D but, by the paper's own statement, "contains no other checks" and does not perform the enumeration despite its filename suggesting otherwise). The paper is honest that the claim is asserted; honesty does not substitute for a proof that is straightforwardly obtainable. **Request:** either (a) extend the released script to an exhaustive symbolic enumeration of contractions at the stated derivative order and cite its output, or (b) demonstrate concretely why the enumeration is not finite/mechanizable as scoped, or (c) demote the section's framing from "completeness argument" to "candidate-basis argument" in title, abstract, and contributions list. Option (a) appears to be days of work, not months, and would promote the survey's second pillar from Tier-II/III assertion to a checked result. A filename that says "enumeration" while the script does not enumerate should also be fixed regardless of the option chosen.

---

## MINOR findings (7)

### MINOR-1 — p. 6 (Sec. IV A): printed |Ω₄₄/α₄| formula is inconsistent with its own inputs and its own quoted value
**Anchor:** left column, "the α₄/Ω₄ₓ family, e.g. |Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)²], which is ≈3.3 at the LQG value γ≈0.24."
From the paper's own quoted Shapiro–Teixeira inputs, α₄ = −6/(1+γ²) and Ω₄₄ = −(378+783γ²)/[20(1+γ²)²], the quotient is (378+783γ²)/[120(1+γ²)] — **first** power of (1+γ²) — which gives 3.33 at γ = 0.24, matching the quoted "≈3.3". The formula as printed (squared denominator) evaluates to 3.15. Verified numerically. The stated number is right; the displayed exponent is wrong. Fix the exponent. No downstream conclusion depends on it (the point is only that the coefficient is O(1)), but this is a checkable displayed equation and it is currently self-inconsistent.

### MINOR-2 — Abstract: "the derived contribution 61–67 orders of magnitude below" mislabels the 61-order endpoint
**Anchor:** abstract; cf. Sec. IV B and p. 8. The 67-order endpoint follows from the *derived* integrated flow (|Δγ/γ| ≈ 1.4×10⁻⁶ → ~10⁻⁶⁷); the 61-order endpoint follows from the deliberately pessimistic chiral-count *ansatz* (Δγ/γ ~ 0.3 → 3×10⁻⁶²). Calling the whole 61–67 range "derived" in the abstract overstates the 61-end, which the body itself labels "a deliberately pessimistic upper bound," "not a precisely derived value." Suggested wording: "bounded ... between a derived integrated-flow estimate (~67 orders) and a deliberately pessimistic chiral-count bound (~61 orders) below the observed dark-energy density."

### MINOR-3 — Sec. II: κ ≡ 8πG = M_Pl⁻² together with the full-Planck-mass numerics is strictly inconsistent, and reduced/full usage is mixed across appendices
**Anchor:** Sec. II ("κ = 8πG = M_Pl⁻²" and "the order-of-magnitude numerics in this survey use the full Planck mass M_Pl ≃ 1.22×10¹⁹ GeV"). Strictly, 8πG = M_Pl,reduced⁻²; with the full Planck mass the equality is off by 8π. The paper flags the reduced-vs-full distinction as immaterial at ≥58-order margins (true), but note the actual usage is mixed: the Table II R1 benchmark 3.6×10⁻⁶⁹ reproduces only with the *reduced* mass (I obtain 3.9×10⁻⁶⁹ reduced vs. 1.5×10⁻⁷⁰ full), while App. A's 8.7×10¹²² hierarchy uses the *full* mass. Each is fine at its stated precision, but the convention sentence should either say "reduced" in the κ definition or note the deliberate abuse once.

### MINOR-4 — Load-bearing companion references [1], [13] are non-peer-reviewed Zenodo deposits
**Anchor:** Refs. [1], [13]; Sec. I "Relation to the companion paper"; App. C; App. D. The Route-1 closure input (torsion-elimination, G_s = −3κ/16 convention, R1 benchmark), the tensor-sector extension of B14, and the entropy-window extrapolation behind B12's 0.27 endpoint all rest on a companion explicitly labeled "not an arXiv preprint and not peer reviewed." The self-contained App. D proof (scalar sector) and the honest Tier-I scoping in Table II ("for canonical scalar matter") substantially mitigate this, and the Zenodo DOI is permanent and public. Still, for journal publication the companion should at minimum be an arXiv preprint, or the minimal tensor-sector statement folded into App. D, so no Tier-I-adjacent claim depends on unrefereeable material.

### MINOR-5 — p. 6: "α_em/(4π) ≈ 5×10⁻⁴" rounds the wrong way
**Anchor:** below Eq. (2). The precise value 5.8×10⁻⁴ (which the paper itself gives parenthetically) rounds to 6×10⁻⁴. Immaterial to the closure (the text says so), but quote the ≈6×10⁻⁴ rounding or just the precise value.

### MINOR-6 — Presentation: hedging density impairs readability
**Anchor:** abstract; p. 6 conservatism paragraph ("the eV-vs-GeV unit conversion is exact ... and is not a source of ambiguity"); repeated evidentiary-status restatements across Secs. I, III, IV, V, VI and Table II. The abstract is very long and reads as a compliance document; the p. 6 bookkeeping paragraph re-derives its own conservatism three ways. The honesty is a strength; the repetition is not. One consolidated evidentiary-status statement (Table II + one paragraph) would suffice; the abstract could shed ~30% without losing content. Not a blocker.

### MINOR-7 — Reference formatting nits
**Anchor:** Ref. [12] "arXiv preprint  (2025)" (double space, no journal); Refs. [1] and [13] carry long prose annotations inside the bibliography entry (deposit dates, license, "concept DOI") better placed in the Data Availability section, which already exists. Ref. [20] (Itzykson–Zuber) could usefully cite the specific Fierz appendix/equation given that Eq. (C1) conventions are load-bearing for App. C.

---

## Checks performed (record)

- SHA-256 verified against the assignment hash before reading. Page count 18 confirmed.
- **Eq. (2):** independent evaluation gives 9.4×10⁻⁶¹ (log₁₀ = −60.0) for the canonical contraction and 1.1×10⁻⁶² for the direct-vs-angle contraction — both match the quoted ~10⁻⁶⁰ and ~2×10⁻⁶² (at the paper's own rounding of α_em/4π); "conservative side" claim confirmed; ≥58-order margin arithmetic consistent everywhere it appears (abstract, Sec. II, Sec. IV A, Sec. VII).
- **Eq. (1) dimension count:** −1+2+3 = +4 confirmed; ∂ϑ_NY ~ H₀² ~ 2×10⁻⁶⁶ eV² confirmed.
- **Eq. (3)/Route 3:** 12π² = 118.4; 30–37 lever arm → 0.25–0.31 confirmed; ln 10¹⁶ = 36.8 confirmed.
- **Eq. (4)/integrated flow:** independent integration with γ = 0.24, μ_UV = 10¹⁶ GeV, κ̃² = 16πG reproduces |Δγ/γ| = 1.38×10⁻⁶ vs. quoted 1.4×10⁻⁶. Fixed-point claim (γ² = 1 the only real zero, 23γ²+5 > 0) is internally consistent with the displayed equation.
- **61–67 order span:** 0.3×10⁻⁶¹ = 3×10⁻⁶² (≈61.5) and 1.4×10⁻⁶×10⁻⁶¹ (≈67) — endpoints confirmed (see MINOR-2 on labeling).
- **App. A:** (1.22×10²⁸/2.25×10⁻³)⁴ = 8.64×10¹²² confirmed; ln10/3 ≈ 0.77 e-fold shift confirmed; N_tot ≈ 93.6 confirmed; Case II (α/M)M_Pl = 1.2×10⁻² confirmed.
- **B12:** ρ_crit = √3/(32π²γ³)ρ_Pl gives 0.409 (γ=0.2375) and 0.267 (γ=0.274) — the quoted 0.41/0.27 window confirmed; squares 0.07–0.17 confirmed; scheme-extrapolation caveat honestly disclosed.
- **Table II R1 benchmark:** κn²_ψ/ρ_Λ = 3.9×10⁻⁶⁹ at n_ψ = 100 cm⁻³ with reduced-M_Pl κ vs. quoted 3.6×10⁻⁶⁹ — consistent at stated precision (see MINOR-3 on convention).
- **App. C:** Fierz matrix rows/columns spot-verified (F² = 𝟙 on sampled entries: (1,1), (1,2), (3,3)); axial row (1/4)(−4,−2,0,−2,4) extraction, F_op = −F_c sign flip, Eq. (C2) decomposition SS + ½VV + ½AA − PP, and (F_c)_AS = −1 → G_s = −3κ/16 chain all internally consistent.
- **Check D:** ε_abcd ε^abce = −3!δ (Lorentzian, one contraction convention as stated) → S_abcS^abc = −(3/8)(J⁵·J⁵) confirmed.
- **Dimension bookkeeping (Table III / p. 11 / p. 14):** all six bare dimensions (+2,+2,+4,+2,+4,+2), prefactors, and the O4/O5 convergence onto κ(J⁵·J⁵) via M²_Plκ² = κ confirmed.
- **Barrier bookkeeping:** Table I ↔ Fig. 1 ↔ Sec. III text ↔ Table II cross-checked entry by entry (foundations, branches, route tags, novel/known/structural partition 9+4+1 = 14, B8⊂B14 counted once). No mismatches found.
- **Citation integrity:** Refs. [2]–[11], [14]–[21] checked against known bibliographic data — titles, venues, volumes, arXiv IDs all correct as far as verifiable (Shapiro–Teixeira CQG 31 185002; Benedetti–Speziale JHEP 2011(6)107 and J.Phys.Conf.Ser. 360 012011; Ashtekar–Singh CQG 28 213001; Holst PRD 53 5966; Freidel–Minic–Takeuchi PRD 72 104002; Mercuri PRL 103 081302; Date–Kaul–Sengupta PRD 79 044008; Minami–Komatsu PRL 125 221301; Eskilt–Komatsu PRD 106 063503 (source of the 0.342°±0.094° value as quoted); Carroll PRL 81 3067; Cai et al. Phys.Rept. 493 1; Nieh–Yan JMP 23 373; Buchalla–Catà–Krause PLB 731 80; Brivio–Trott Phys.Rept. 793 1; Nieves–Pal AJP 72 1100). Ref. [12] (ACT DR6, arXiv:2509.13654) not independently verifiable here; value quoted is plausible and non-load-bearing.
- **Artifact paths:** all three Data-and-Code-Availability script paths exist in the local repository tree (`arxiv/scripts/dim4_parityodd_enumeration.py`, `arxiv/scripts/fierz_lemma_check.py`, `research/theory_audit/fierz_adjudication_2026_08_05.py`). Commit-hash immutability (9b92721d5d7e) not verified (no git repo access required for this leg).
- **Presentation blockers:** none found — no column overflow, no broken table layout, Fig. 1 legible, all cross-references resolve in the rendered PDF.

## Verdict rationale

No correctness failure was found in any checkable displayed equation; the one algebraic slip (MINOR-1) is a typo-level exponent whose correct value the paper already quotes. Internal consistency across table/figure/text/appendices is excellent. Scope honesty is exemplary — every claim is tiered, and Sec. VI states what is not established. The single MAJOR item is a bounded, mechanizable request (enumerate or retitle) that does not threaten the paper's conclusions but does affect how its second headline contribution may be advertised. Verdict: **minor-revisions**.

*— Claude INT referee leg (R3 confirmation), 2026-08-06. Report written to file only; no commit, no push, no manuscript edits.*
