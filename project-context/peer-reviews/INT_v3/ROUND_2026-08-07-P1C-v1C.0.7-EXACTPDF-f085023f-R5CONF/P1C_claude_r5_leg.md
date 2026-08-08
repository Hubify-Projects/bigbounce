# P1C v1C.0.7 — Claude INT leg, R5 confirmation round

- **Manuscript:** arxiv/paper1c_nogo_survey/main.pdf (18 pages)
- **SHA-256 (verified before reading):** f085023fea37f4d1fa053fc30d04d5006c23f5998e8edebe683900a955048397
- **Date:** 2026-08-06 (round dir label 2026-08-07)
- **Role:** Independent skeptical journal referee (CQG calibre), Claude leg of the R5 confirmation board. Fresh read; no prior review of this paper consulted.
- **Scope reviewed:** mathematical correctness of every checkable displayed/inline equation; internal consistency; scope honesty; citation integrity; presentation blockers.

## VERDICT: ACCEPT — 0 MAJOR, 3 MINOR (all optional-polish level; none load-bearing, none blocking)

The manuscript is internally consistent to an unusual degree; every load-bearing
number I could recompute independently reproduced. The evidentiary-tier
discipline (Tier I/II/III labeling, Table II) is exemplary scope honesty: no
claim in the abstract or conclusions exceeds the tier at which it is
established in the body.

---

## Verification log (checks that PASSED)

Every item below was independently recomputed from the stated inputs, not taken
on trust.

1. **R1 benchmark (Sec. II, p.2; Table II):** κn_ψ²/ρ_Λ with κ = 8πG,
   n_ψ = 100 cm⁻³ (= 7.66×10⁻¹³ eV³), ρ_Λ = (2.3 meV)⁴ = 2.8×10⁻¹¹ eV⁴ →
   I get 3.5×10⁻⁶⁹ vs the quoted 3.6×10⁻⁶⁹ (rounding). Under
   ρ_Λ = (2.25 meV)⁴ = 2.56×10⁻¹¹ eV⁴ → 3.85×10⁻⁶⁹ vs quoted 3.9×10⁻⁶⁹. Both PASS.
   "≈68 orders below ρ_Λ" PASS (10^−68.4).
2. **Route-2 chain, Eq. (2) and evaluation (pp.6–7):** α_em/4π = 5.8×10⁻⁴
   ("rounded up to 10⁻³" — correctly conservative for a suppression claim);
   H₀/M_Pl = 1.15×10⁻⁶¹; M_Pl·(α/M) = 10⁻²; β_obs = 0.342° = 5.97×10⁻³ rad.
   Displayed contraction 10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) = 1.7×10⁻⁶⁰ ≈ 10⁻⁶⁰ PASS.
   Direct contraction (α_em/4π)(H₀/M_Pl)/β_obs = 1.7×10⁻⁶² ≈ 2×10⁻⁶² PASS
   ("two additional orders" PASS). 60 − 2 (loop-ordering allowance) = "≥58" PASS.
   58 − 10 = "≳48 under 10-order inflation" PASS. The two lines of Eq. (2)
   are algebraically identical (1/[M_Pl(α/M)] = M/(αM_Pl)) PASS.
3. **Shapiro–Teixeira coefficient ratio (Sec. IV A, p.6):** with the quoted
   α₄ = −6/(1+γ²) and Ω₄₄ = −(378+783γ²)/[20(1+γ²)²], the ratio
   |Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)] as printed; at γ = 0.24 I get 3.33 ≈ "≈3.3"
   PASS. (Note: an earlier visual read of the page image suggested a squared
   bracket; pdftotext extraction confirms the printed single power. No finding.)
4. **Route-3 integrated bound (Sec. IV B, pp.7–8):** integrating Eq. (4) with
   κ̃² = 16π/M_Pl², frozen coefficient at γ = 0.24 (γ²−1 = −0.94, 23γ²+5 = 6.32),
   ∫β dlnμ dominated by UV endpoint μ_UV = 10¹⁶ GeV: I get
   Δγ² ≈ 1.6×10⁻⁷ → Δγ/γ = Δγ²/(2γ²) ≈ 1.38×10⁻⁶ vs quoted ≈1.4×10⁻⁶.
   **Independent reproduction PASS.** Fixed-point structure of Eq. (4): β = 0 only
   at γ² = 1 for real γ (23γ²+5 > 0) PASS; UV-attractivity sign analysis PASS.
5. **Route-3 endpoints:** chiral-count Δγ/γ = ln(μ_GUT/μ_IR)/(12π²): 30/118.4 =
   0.25, 37/118.4 = 0.31 PASS; 32/(12π²) = 0.270 PASS; ln 10¹⁶ = 36.8 PASS.
   Margins: 0.3×10⁻⁶¹·³ → ~61 orders; 1.4×10⁻⁶×1.2×10⁻⁶¹ = 1.7×10⁻⁶⁷ → ~67
   orders. Abstract/Sec. IV/Sec. VI/Conclusions all quote the same 61–67 pair
   with the same attribution (derived = 67, pessimistic chiral = 61) PASS.
6. **B12 window (p.5):** ρ_crit = √3/(32π²γ³)ρ_Pl: γ = 0.2375 → 0.410; γ = 0.274
   → 0.267 PASS ("0.27–0.41"). Ω_GW ceiling (ρ_crit/ρ_Pl)²: 0.071–0.168 PASS
   ("0.07–0.17"). Attribution honesty (0.41 = Ashtekar–Singh canonical; 0.274 an
   internal extrapolation, "not a value quoted in Ref. [4]") PASS.
7. **R4 anchor (Sec. IV C, p.8):** β = (α/2M)Δφ with Δφ ~ M_Pl:
   α/M = 2β_obs/M_Pl = 9.8×10⁻²² ≈ 10⁻²¹ GeV⁻¹ PASS; Δφ ~ √(2ρ_θ)/m_θ for a
   frozen field PASS; β_obs = 0.342° ≈ 6×10⁻³ rad PASS.
8. **Appendix A hierarchy:** M_Pl⁴/ρ_Λ = (1.22×10²⁸/2.25×10⁻³ eV)⁴ = 8.6–8.7×10¹²²
   PASS; N_tot = 122 ln10/3 = 93.6 ≈ 94 PASS; Case-II 120-order variant → 92 PASS
   ("92-vs-94 spread"); ln10/3 ≈ 0.8 PASS; e^{−3·94} = 10^{−122.5} PASS.
   Eq. (A2): (α/M)M_Pl⁵ = [M_Pl(α/M)]M_Pl⁴ = 10⁻²M_Pl⁴ PASS; dimension of (A2)
   is 4 PASS.
9. **Dimension bookkeeping (Eq. (1), (5), (6), (8), App. A, Table III):**
   [β/M_Pl] + [∂ϑ_NY] + [J⁵] = −1+2+3 = +4 PASS; [α/M] + [εeeF] = −1+2 = +1 PASS
   (the three-unit deficit as stated); building blocks [e] = 0, [R] = +2,
   [S] = +3, [T] = [κS] = +1 PASS; bare dims εeeR = 2, NY = 2, T² = 2, R∧R = 4,
   εTeJ⁵ = 4 PASS; every Table III prefactor restores dim 4 PASS; O4 and O5 both
   land on κ(J⁵·J⁵) at the same κ-power (M_Pl²κ² = κ) PASS — the "+4 throughout"
   contract holds.
10. **Torsion contraction (Check D, p.15; p.11):** S^abc = ¼ε^abcd J⁵_d with
    ε_abcd ε^abce = −3!δ_d^e gives S_abcS^abc = −(3/8)(J⁵·J⁵); both quoted sites
    agree PASS.
11. **Fierz appendix (App. C, p.16–17):** the printed F_c is the standard
    Itzykson–Zuber (S,V,T,A,P) matrix; I verified F_c² = 𝟙 on five independent
    row·column contractions PASS. Axial row ¼(−4,−2,0,−2,4) = (−1,−½,0,−½,1)
    PASS; F_op = −F_c (one Grassmann exchange) PASS; Eq. (C2)
    AA → SS + ½VV + ½AA − PP follows from the operator row (1,½,0,½,−1) PASS;
    (F_c)_AS = −1 → (F_op)_AS = +1 → G_s = −3κ/16 PASS; F_VA^op = F_AV^op = ½
    PASS. Closure of {SS,VV,AA,PP} with {V,A} cross term only, no escape
    operator, PASS at the printed-matrix level.
12. **B14 proof (App. D):** four-step structure (zero spin density → zero torsion
    via invertible bivector kernel for real finite γ, 1+γ² > 0 → Levi-Civita →
    Holst vanishes by pointwise algebraic Bianchi ε^{μνρσ}R_{μνρσ}(Γ̂) = 0) is
    sound at the stated scope; exclusion list (complex γ = ±i, topological
    sectors, loops, anomalies, propagating torsion) is explicit PASS. Check A
    (A4) is the standard first-Bianchi contraction PASS; the caveat that the
    torsionful R does not satisfy it, with the O(κS) piece routed to O4/O5, is
    stated on p.15 PASS.
13. **Counting integrity:** 14 entries = 7 foundations (B1–B7) + 7 branch entries
    (B8–B14); B8 subsumed by B14 → "13 distinct" PASS everywhere it appears
    (abstract, Sec. I, Sec. III, Fig. 1 caption, Table I caption, Sec. VI,
    Conclusions). Novel {1,2,3,4,8,10,11,12,14} = 9, known {5,6,7,9} = 4,
    structural {13} = 1; 9+4+1 = 14 PASS; "eight of the nine ECH-specific, B10
    general" PASS. Branch letters H,J,L,M,N,O with I/K never assigned —
    disclosed PASS.
14. **B1 scaling (p.3):** g_eff ~ 1/(M_Pl√|t₃|) with √|t₃| ~ m_T⁻¹, m_T ~ H₀ →
    H₀/M_Pl ~ 10⁻⁶¹ PASS; (H₀/M_Pl)² ~ 10⁻¹²² PASS.
15. **Convention flags (Sec. II):** κ = 8πG = M̄_Pl⁻² exact; the declared
    factor-8π "abuse" for OoM prose; κ̃² ≡ 16πG import distinguished from this
    paper's κ² (dim −4); (α,M) dual-role disclosure; β(γ) vs β disambiguation —
    all internally consistent and actually adhered to in the body PASS.
16. **Citation integrity (spot-checked against knowledge):** Shapiro–Teixeira
    CQG 31 185002 (2014)/1402.4854; Benedetti–Speziale JHEP 2011(6)107/1104.4028
    and JPCS 360 012011/1111.0884; Ashtekar–Singh CQG 28 213001/1108.0893; Holst
    PRD 53 5966; Freidel–Minic–Takeuchi PRD 72 104002; Mercuri PRL 103 081302;
    Date–Kaul–Sengupta PRD 79 044008; Minami–Komatsu PRL 125 221301
    (β = 0.35°±0.14°); Eskilt–Komatsu PRD 106 063503 (β = 0.342°+0.094/−0.091°);
    Nieh–Yan JMP 23 373; Popławski PLB 694 181; Buchalla–Catà–Krause;
    Brivio–Trott; Isidori–Wilsch–Wyler; Nieves–Pal; Carroll; Cai et al. — all
    real, correctly attributed, and used within their actual content. The two
    Zenodo self-citations ([1],[13]) are explicitly declared "not an arXiv
    preprint and not peer reviewed" PASS. The Eq. (3) ansatz is explicitly NOT
    attributed to Date–Kaul–Sengupta ("does not itself present the explicit RG
    equation used below") and Eq. (1) is explicitly NOT attributed to Mercuri or
    Shapiro–Teixeira verbatim — provenance hygiene PASS.
17. **Presentation:** no visible column overflow, no orphaned equations, Table I/
    II/III and Fig. 1 legible and correctly cross-referenced; Data/Code
    availability paths and the frozen-commit footnote coherent. No blockers.

## MAJOR findings

None.

## MINOR findings

- **MINOR-1 (citation precision) — Sec. IV C, p.8, anchor: "βobs = 0.342° ± 0.094° [10, 11]".**
  The specific value 0.342°±0.094° is Ref. [11]'s (Eskilt–Komatsu 2022,
  WMAP+Planck) result; Ref. [10] (Minami–Komatsu 2020, Planck 2018 only)
  reported 0.35°±0.14°. The joint cite [10,11] attached directly to the [11]
  number is loose lineage-citation. Suggested fix: "β_obs = 0.342°±0.094° [11]
  (first Planck-2018 extraction: 0.35°±0.14° [10])" or move [10] to the
  discovery clause. Cosmetic; the prose "WMAP+Planck" already points to [11].
- **MINOR-2 (unmotivated range endpoint) — Sec. IV B, p.8, anchor:
  "lever arm ln(μGUT/μIR) ≈ 30–37 (μGUT ∼ 10¹⁶, μIR ∼ 1 GeV, ln 10¹⁶ ≈ 36.8)".**
  The stated endpoints give ln = 36.8 only; the lower edge 30 (which generates
  the 0.25 end of "Δγ/γ ≈ 0.25–0.31") is never tied to a stated μ choice
  (ln 30 corresponds to μ_GUT/μ_IR ~ 10¹³). Non-load-bearing — the budget adopts
  the larger 0.3 as the conservative value — but the range's lower edge should
  either be motivated (e.g. lower GUT scale / higher IR cutoff) or dropped.
- **MINOR-3 (opaque non-load-bearing figure) — Sec. IV A, p.7, anchor:
  "an alternative ordering … yields a deliberately loose ∼10⁻³³ upper bound, not used in the closure".**
  The ~10⁻³³ figure is not reproducible from any contraction of the stated
  inputs given in the text (I attempted the natural orderings). Since it is
  explicitly labeled loose and unused, it carries no logical weight, but a
  number a referee cannot reconstruct should either get a one-line derivation
  in a footnote or be removed.

## Scope-honesty assessment

Strong. The abstract itself carries the caveats (basis completeness "asserted
from the construction rules, not proved by exhaustive symbolic enumeration";
"channel-level, not operator-level"; only B14 Tier-I). Sec. VI's "What is not
established" list matches what the body actually leaves open. The
non-circularity argument for the NDA no-go (p.14) is logically sound: no
positive ρ_Λ is derived, so no derived-amplitude circularity arises. The
R2 "closed as bounded amplitude budget" vs "exploratory, not load-bearing"
dual framing is consistent once Table II's tier assignment is read as intended,
and the paper states that reading explicitly.

## Verdict rationale

Zero mathematically incorrect checkable equations found; zero internal
contradictions found; zero overclaims found; three optional-polish nits. At a
CQG bar this is an accept — the minors do not require re-review.

*Reviewer: Claude (Fable 5), INT leg, exact-PDF-bound. No manuscript edits made;
nothing committed or pushed.*
