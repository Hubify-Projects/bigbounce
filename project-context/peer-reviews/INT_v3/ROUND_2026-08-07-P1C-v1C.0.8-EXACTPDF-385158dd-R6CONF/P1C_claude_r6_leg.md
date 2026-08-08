# P1C v1C.0.8 — Claude INT Leg, Round R6CONF (Confirmation Board)

- **Role:** Independent skeptical journal referee (CQG calibre), Claude leg. Fresh review; no prior rounds seen.
- **Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf` (18 pages, dated August 6, 2026, v1C.0.8)
- **SHA-256 (verified before reading):** `385158dd6351a515d1d0d73bdbbd7cc3b61ed1df90b88f067bed54d40778c575`
- **Review date:** 2026-08-06
- **Method:** Full-PDF read (all 18 pages); independent re-derivation of every checkable displayed equation and order-of-magnitude claim; internal-consistency sweep; citation spot-audit; scope-honesty and presentation review.

---

## VERDICT: MINOR REVISIONS (1 MAJOR, 8 MINOR)

The manuscript is internally consistent to an unusually high standard. Every displayed
equation and numeric I could check independently passed (list in "Verified" below),
including the Route-3 headline: integrating Eq. (4) myself with frozen coefficients at
γ = 0.24, κ̃² = 16πG, μ_UV = 10¹⁶ GeV, full M_Pl = 1.22×10¹⁹ GeV gives
Δγ² ≈ 0.237 (μ_UV/M_Pl)² ≈ 1.59×10⁻⁷, hence |Δγ/γ| = Δγ²/(2γ²) ≈ 1.38×10⁻⁶ —
matching the quoted 1.4×10⁻⁶ exactly. The evidentiary three-tier classification
(Table II) is scrupulous and nowhere overclaimed. The single MAJOR item is a
journal-level structural issue, not an error.

---

## MAJOR

**M1 — Load-bearing dependence on a non-peer-reviewed companion deposit [1].**
(Sec. I "Relation to the companion paper"; Sec. II imported conventions; Table II R1 row;
App. C convention note; refs [1], [13].) Several Tier-II inputs rest on the Zenodo
companion (doi:10.5281/zenodo.21481838), which the reference list itself states is
"not an arXiv preprint and not peer reviewed": the torsion-elimination normalization
and the −3κ/16 contact coefficient, the R1 benchmark κn_ψ²/ρ_Λ ≈ 3.6×10⁻⁶⁹, and the
Fierz-convention verification chain. App. D (B14) and App. A1/C reduction checks are
commendably carried self-contained, but the R1 closure numbers and the Cartan-elimination
derivation are companion-only. For journal publication, either (a) the companion must be
under review/accepted at a citable venue, or (b) the load-bearing derivations (contact
operator coefficient; R1 benchmark computation) must be reproduced in an appendix here.
As it stands, a referee cannot fully verify the R1 leg from this manuscript plus the
published literature alone. This is a venue/verifiability blocker, not a correctness
finding.

---

## MINOR

**m1 — Abstract length and density.** The abstract is a single ~450-word paragraph
carrying inline hedges, tier labels, and margin bookkeeping. CQG practice is roughly
half that. Recommend moving the evidentiary-classification caveats to the
Introduction/Sec. VI and cutting the abstract to the four results (catalog; Route-2
budget; Route-3 budget; operator-basis argument).

**m2 — Gravitational chiral anomaly omitted from the divergence-operator disposal
(p. 11, Sec. V).** The text disposing of √−g ∇_μJ^{5μ} states its "anomalous content
introduces FF̃ only once electromagnetic fields are added — outside the minimal field
content." This overlooks the *gravitational* contribution to the chiral anomaly,
∇_μJ^{5μ} ⊃ (const/π²) R R̃ (Kimura–Delbourgo–Salam), which is present within the
minimal field content. The closure is unaffected — R R̃ is exactly O3 (Pontryagin),
already in the basis and disposed as a total derivative — but the sentence as written
is technically incorrect and should acknowledge the R R̃ term and route it to O3.

**m3 — Full vs reduced Planck-mass bookkeeping.** Sec. II discloses the "deliberate
factor-8π abuse" (κ = 8πG exactly, prose writes κ ~ M_Pl⁻²), but downstream identities
inherit it silently: Table III / p. 15 use "M_Pl²κ² = κ" [exact only for M̄_Pl ≡ κ^{-1/2},
off by 8π at full M_Pl], while the verified Route-3 numeric 1.4×10⁻⁶ uses full M_Pl.
Each is individually harmless at the quoted margins, but the reader must re-derive which
convention each numeric uses. Recommend tagging each headline numeric with its convention
(as is already done well for the R1 3.6 vs 3.9 ×10⁻⁶⁹ pair on p. 2).

**m4 — Provenance footnote 1 (p. 13).** The pinned commit `9b92721d5d7e` and the current
repository head differ in the descriptive header of `dim4_parityodd_enumeration.py`.
Even with identical check results, a frozen-artifact claim should not carry a known
divergence; repin to a commit matching head (or freeze the planned updated Zenodo
deposit) before submission.

**m5 — Eq. (2) normalization choice.** Normalizing the one-loop amplitude by the
R4-fitted coupling benchmark (yielding ~10⁻⁶⁰) rather than contracting directly against
β_obs (yielding ~2×10⁻⁶²) is disclosed and both values given, and the "conservative"
labeling (quoting the *larger* ratio) is correct in direction. But the physical
motivation for the benchmark-normalized bookkeeping deserves one explicit sentence at
Eq. (2) itself (it currently arrives a paragraph later), since a fast reader can misread
the displayed ratio as a derived observable rather than a bookkeeping choice.

**m6 — Detection status of the birefringence benchmark.** β_obs = 0.342° ± 0.094°
(≈3.6σ) [10] and the ACT DR6 value 0.215° ± 0.074° (≈2.9σ) [12] are used as the
"observed birefringence amplitude." The suppression conclusion is insensitive to this
(a smaller/zero true signal only widens the margin), but one sentence noting the
current significance would prevent overstating the detection as established.

**m7 — Fig. 1 caption overload.** The caption carries the per-barrier arrow-attribution
semantics (upper Branch-H arrow = B8+B14; lower three-route fan = B14 alone) in prose
that is hard to map onto the figure at box granularity. A small in-figure legend or
edge labels would remove the ambiguity.

**m8 — Imported equation numbers not independently verifiable here.** The quoted
Shapiro–Teixeira anchors (their Eqs. 37, 41, 42 "arXiv version", 46, 51, 58) and the
Benedetti–Speziale Eq. (7) coefficient structure (23γ² + 5) are consistent with all
internal cross-checks I could run (e.g. |Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)] follows
correctly from the quoted Ω₄₄, α₄ and evaluates to ≈3.3 at γ = 0.24, as stated), but I
could not verify the source equation numbers against the published texts in this
sandbox. Since the paper itself flags "arXiv version" for Eq. 42, recommend the authors
confirm every imported equation number against the *journal* versions and note any
arXiv/journal numbering drift.

---

## Verified (independent checks that PASSED)

- **Eq. (1) dimensions:** [β(γ)/M_Pl] = −1, [∂ϑ_NY] = +2, [J⁵] = +3 → dim-4 density. ✓
- **Eq. (2) numerics:** α_em/4π = 5.8×10⁻⁴ (rounded up to 10⁻³ conservatively, as stated);
  H₀/M_Pl = 1.4×10⁻³³ eV / 1.22×10²⁸ eV ≈ 1.1×10⁻⁶¹; M_Pl·(α/M) = 10⁻²;
  β_obs = 0.342·π/180 = 5.97×10⁻³ rad; ratio 10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) ≈ 1.7×10⁻⁶⁰. ✓
  Alternative contraction 10⁻³·10⁻⁶¹/(6×10⁻³) ≈ 1.7×10⁻⁶² ("2×10⁻⁶², two additional orders"). ✓
- **Eq. (3) integration:** ln(10¹⁶) = 36.8; 36.8/(12π²) = 0.31; 32/(12π²) = 0.270; range 0.25–0.31. ✓
- **Eq. (4) fixed point & integrated flow:** only real fixed point γ² = 1 (23γ²+5 > 0);
  UV-attractive sign ✓; frozen-coefficient integral reproduces |Δγ/γ| ≈ 1.4×10⁻⁶ at full M_Pl
  (my value 1.38×10⁻⁶). ✓
- **ST coefficient ratio:** (378+783γ²)/[120(1+γ²)] at γ = 0.24 → 3.33 ("≈3.3"). ✓
- **B1:** g_eff ~ 1/(M_Pl·H₀⁻¹) = H₀/M_Pl ~ 10⁻⁶¹; (H₀/M_Pl)² ~ 10⁻¹²². ✓
- **B12:** ρ_crit/ρ_Pl = √3/(32π²γ³): γ = 0.2375 → 0.409; γ = 0.274 → 0.267; squares 0.07–0.17. ✓
- **R1 benchmark:** κn_ψ² at n_ψ = 100 cm⁻³ → 9.8×10⁻⁸⁰ eV⁴; /ρ_Λ = 2.8×10⁻¹¹ eV⁴ → 3.5×10⁻⁶⁹
  ("3.6×10⁻⁶⁹"); with (2.25 meV)⁴ → 3.8×10⁻⁶⁹ ("3.9×10⁻⁶⁹"). ✓ (≈68 orders ✓)
- **R4 anchor:** 2β_obs/M_Pl = 2·6×10⁻³/1.22×10¹⁹ GeV ≈ 10⁻²¹ GeV⁻¹. ✓
- **App. A:** M_Pl⁴/ρ_Λ = (1.22×10²⁸/2.25×10⁻³)⁴ eV⁰ = 8.6×10¹²² ("8.7×10¹²² ≈ 10¹²³") ✓;
  N_tot = 122 ln10/3 = 93.6 ≈ 94 ✓; 10¹²²-vs-10¹²³ shift ln10/3 ≈ 0.8 ✓; Eq. (A2)
  (α/M)M_Pl = 1.2×10⁻² ✓.
- **Check A:** ε^{μνρσ}R_{μνρσ} = 0 from pair antisymmetry + R_{μ[νρσ]} = 0 — standard, correct. ✓
- **Check D:** S_{abc}S^{abc} = (1/16)ε_{abcd}ε^{abce}J⁵ᵈJ⁵ₑ = −(3/8)(J⁵·J⁵) with
  Lorentzian ε_{abcd}ε^{abce} = −3!δᵈₑ. ✓
- **App. C:** axial row ¼(−4,−2,0,−2,4); F_op = −F_c → operator row (1,½,0,½,−1) →
  (J⁵·J⁵) → SS + ½VV + ½AA − PP ✓; (F_op)_AS = +1 → G_s = −3κ/16 consistent with the
  quoted companion coefficient. ✓
- **Table III dimension bookkeeping:** all six bare dims and prefactor promotions consistent
  ([e]=0, [R]=+2, [T]=+1, [J⁵]=+3). ✓
- **Internal counts:** "13 distinct / 14 historical, B8⊂B14" consistent across abstract,
  Sec. III, Fig. 1, Table I, Secs. VI–VII ✓; branch letters H,J,L,M,N,O (no I/K) explained ✓;
  tier assignments in Table II match the per-section prose ✓.
- **App. D proof logic:** zero spin density → algebraic Cartan → T = 0 → Levi-Civita →
  Holst dual vanishes pointwise by first Bianchi; exclusions stated. Sound within stated scope. ✓
- **Citations spot-audited:** [2] CQG 31 185002 / 1402.4854; [3] JHEP 2011(6)107 / 1104.4028;
  [4] 1108.0893; [5] PRD 53 5966; [6] hep-th/0507253; [7] 0902.2764; [8] 0811.4496;
  [10] PRD 106 063503 / 2205.13962 (β = 0.342±0.094° — matches); [11] PRL 125 221301
  (0.35±0.14° — matches); [16] Nieh–Yan 1982; [21] Itzykson–Zuber; [22] Nieves–Pal
  hep-ph/0306087. All real and correctly attributed as far as checkable. No fabricated
  citations detected.

## Scope honesty

Exemplary. The three-tier evidentiary classification (Table II), the repeated
"asserted from construction rule, not proved by exhaustive symbolic enumeration"
disclosure, the explicit "What is not established" subsection (Sec. VI), the ansatz
labels on Eqs. (3) and (A2)/Case II, and the strict-theoretical-limitation paragraph
(Sec. IV) leave essentially no overclaim surface. No instance found of the paper
headlining the more favorable of two values without stating both.

## Presentation blockers

None at the blocking level. No column overflows, no broken references, no undefined
symbols observed in the rendered PDF. m1 (abstract) and m7 (Fig. 1 caption) are the
only presentation items.

---

*End of report. Claude confirmation-board leg, R6CONF, exact-PDF-bound 385158dd.*
